import math

def states(t):
    x = 0.5 + 0.05 * math.sin(t)
    dx = 0.05 * math.cos(t)
    y = 0.3 + 0.02 * math.cos(2.0 * t)
    dy = -0.04 * math.sin(2.0 * t)
    return x, dx, y, dy

def holling_rates(t, A, B, C):
    x, dx, y, dy = states(t)
    alpha = (dx / x + A * y / (B + x)) / (1.0 - x**4)
    delta = C * x / (B + x) - dy / y
    return alpha, delta

def ratio_rates(t, A, B, C):
    x, dx, y, dy = states(t)
    alpha = (dx / x + A * y / (B * y + x)) / (1.0 - x**4)
    delta = C * x / (B * y + x) - dy / y
    return alpha, delta

def residuals(model, t, A, B, C):
    x, dx, y, dy = states(t)
    if model == "holling":
        alpha, delta = holling_rates(t, A, B, C)
        rx = dx - (alpha * x * (1.0 - x**4) - A * x * y / (B + x))
        ry = dy - (C * x * y / (B + x) - delta * y)
    else:
        alpha, delta = ratio_rates(t, A, B, C)
        rx = dx - (alpha * x * (1.0 - x**4) - A * x * y / (B * y + x))
        ry = dy - (C * x * y / (B * y + x) - delta * y)
    return rx, ry, alpha, delta

triples = [(1.0, 1.0, 2.0), (1.3, 1.2, 2.5)]

for model in ("holling", "ratio"):
    for triple in triples:
        vals = [residuals(model, k / 1000.0, *triple) for k in range(1001)]
        max_res = max(max(abs(v[0]), abs(v[1])) for v in vals)
        min_alpha = min(v[2] for v in vals)
        max_alpha = max(v[2] for v in vals)
        min_delta = min(v[3] for v in vals)
        max_delta = max(v[3] for v in vals)
        print(
            model,
            triple,
            f"max_residual={max_res:.16e}",
            f"alpha_range=[{min_alpha:.12f},{max_alpha:.12f}]",
            f"delta_range=[{min_delta:.12f},{max_delta:.12f}]",
        )
