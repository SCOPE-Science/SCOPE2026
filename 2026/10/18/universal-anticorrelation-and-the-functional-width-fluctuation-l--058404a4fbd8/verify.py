"""Independent numerical checks of exact direction-lag width covariance for regular polygons.

Uses only Python's standard library; geometric widths are computed from vertices,
not from the analytic width-profile representation in the proof.
"""
import math


def analytic(n, lag):
    q = math.pi / n if n % 2 == 0 else math.pi / (2 * n)
    amplitude = 2.0 if n % 2 == 0 else 2.0 * math.cos(q)
    period = 2 * q
    r = lag % period
    r = min(r, period - r)
    mean_unit = math.sin(q) / q
    second_unit = ((2*q-r)*math.cos(r) + r*math.cos(2*q-r)
                  + math.sin(2*q-r) + math.sin(r)) / (4*q)
    return amplitude * mean_unit, amplitude**2 * (second_unit - mean_unit**2)


def geom_width(n, angle):
    c, s = math.cos(angle), math.sin(angle)
    projected = [c * math.cos(2 * math.pi * j / n)
                 + s * math.sin(2 * math.pi * j / n) for j in range(n)]
    return max(projected) - min(projected)


def run():
    N = 24000
    worst_mean = 0.0
    worst_cov = 0.0
    comparisons = 0
    for n in (3, 4, 5, 6, 7, 8, 11, 12, 17):
        q = math.pi / n if n % 2 == 0 else math.pi / (2*n)
        for frac in (0.0, 0.17, 0.53, 1.0, 1.47):
            lag = frac * q
            vals0 = []
            vals1 = []
            for j in range(N):
                angle = 2*math.pi*(j+0.31)/N
                vals0.append(geom_width(n, angle))
                vals1.append(geom_width(n, angle+lag))
            empirical_mean = math.fsum(vals0) / N
            empirical_other = math.fsum(vals1) / N
            empirical_cov = math.fsum((x-empirical_mean)*(y-empirical_other)
                                       for x,y in zip(vals0, vals1)) / N
            predicted_mean, predicted_cov = analytic(n, lag)
            worst_mean = max(worst_mean, abs(empirical_mean - predicted_mean))
            worst_cov = max(worst_cov, abs(empirical_cov - predicted_cov))
            comparisons += 1
    print('cases', comparisons, 'worst_mean_error', worst_mean,
          'worst_covariance_error', worst_cov)
    assert worst_mean < 3.0e-7
    assert worst_cov < 3.0e-7
    print('PASS: direct vertex-projection integration agrees with closed formulas')


if __name__ == '__main__':
    run()
