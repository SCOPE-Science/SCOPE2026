import numpy as np
import scipy
from scipy.integrate import solve_ivp

m = 4
L = np.pi / m
s_m = np.sin(2 * np.pi / m)
heights = np.array([0.4, 0.7, 0.8], dtype=float)
y0 = np.array([0.05, 0.10, 0.16, 0.20, 0.30, 0.38], dtype=float)


def green_at(x, endpoints):
    total = 0.0
    for j, c in enumerate(heights):
        a, b = endpoints[2 * j], endpoints[2 * j + 1]
        if b <= x:
            integral = 0.5 * (np.cos(2 * a) - np.cos(2 * b))
            total -= c * np.sin(2 * (L - x)) * integral / (2 * s_m)
        elif a >= x:
            integral = 0.5 * (np.cos(2 * (L - b)) - np.cos(2 * (L - a)))
            total -= c * np.sin(2 * x) * integral / (2 * s_m)
        else:
            left = 0.5 * (np.cos(2 * a) - np.cos(2 * x))
            right = 0.5 * (np.cos(2 * (L - b)) - np.cos(2 * (L - x)))
            total -= c * (
                np.sin(2 * (L - x)) * left + np.sin(2 * x) * right
            ) / (2 * s_m)
    return total


def rhs(_t, endpoints):
    return np.array([2 * green_at(x, endpoints) for x in endpoints])


def mass(endpoints):
    return sum(
        heights[j] * (endpoints[2 * j + 1] - endpoints[2 * j])
        for j in range(len(heights))
    )


def moment(endpoints):
    return 0.5 * sum(
        heights[j]
        * (np.cos(2 * endpoints[2 * j]) - np.cos(2 * endpoints[2 * j + 1]))
        for j in range(len(heights))
    )


def profile_l1_error(t, endpoints):
    c_star = heights[-1]
    B = 1.0 / c_star
    scaled = t * endpoints
    breaks = [0.0, B]
    breaks.extend(float(x) for x in scaled)
    breaks = sorted(set(x for x in breaks if x >= 0.0))
    err = 0.0
    for left, right in zip(breaks[:-1], breaks[1:]):
        if right <= left:
            continue
        mid = 0.5 * (left + right)
        f = 0.0
        for j, c in enumerate(heights):
            if scaled[2 * j] < mid <= scaled[2 * j + 1]:
                f += c
        target = c_star if 0.0 < mid <= B else 0.0
        err += abs(f - target) * (right - left)
    return err


def limiting_green(y):
    c_star = heights[-1]
    B = 1.0 / c_star
    if y <= B:
        return -y + 0.5 * c_star * y * y
    return -0.5 / c_star


sol = solve_ivp(
    rhs,
    (0.0, 5000.0),
    y0,
    method="DOP853",
    rtol=1e-11,
    atol=1e-13,
    dense_output=True,
    max_step=10.0,
)
assert sol.success

c_star = heights[-1]
B = 1.0 / c_star
print(f"numpy={np.__version__} scipy={scipy.__version__}")
print(f"predicted_B=1/c_star={B:.12f}")
print("t        t*b_n          t*L1           t^2*moment      profile_L1_error")
for t in [100.0, 500.0, 1000.0, 5000.0]:
    y = sol.sol(t)
    print(
        f"{t:7.0f}  {t*y[-1]:.12f}  {t*mass(y):.12f}  "
        f"{t*t*moment(y):.12f}  {profile_l1_error(t,y):.12f}"
    )

final_t = 5000.0
final_y = sol.sol(final_t)
print("scaled_inner_endpoints_at_t5000=", np.array2string(final_t * final_y[:-1], precision=10))
print("y        t^2*G(t,y/t)   limiting_G")
for y in [0.25, 0.75, 1.25, 1.50]:
    scaled_G = final_t * final_t * green_at(y / final_t, final_y)
    print(f"{y:4.2f}     {scaled_G:.12f}   {limiting_green(y):.12f}")
