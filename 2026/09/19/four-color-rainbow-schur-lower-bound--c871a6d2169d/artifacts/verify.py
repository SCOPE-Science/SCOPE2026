from fractions import Fraction

BREAKS = [0, 23, 30, 40, 50, 59, 62, 75, 85, 96, 100]
COLORS = [1, 2, 3, 4, 2, 4, 3, 2, 4, 3]


def positive_square(x):
    return max(x, 0) ** 2


def twice_area_below(a, b, c, d, t):
    return (
        positive_square(t - a - c)
        - positive_square(t - b - c)
        - positive_square(t - a - d)
        + positive_square(t - b - d)
    )


def exact_density():
    contributions = []
    for k in range(10):
        total = 0
        for i in range(10):
            for j in range(10):
                if len({COLORS[i], COLORS[j], COLORS[k]}) < 3:
                    continue
                total += twice_area_below(
                    BREAKS[i], BREAKS[i + 1],
                    BREAKS[j], BREAKS[j + 1],
                    BREAKS[k + 1],
                )
                total -= twice_area_below(
                    BREAKS[i], BREAKS[i + 1],
                    BREAKS[j], BREAKS[j + 1],
                    BREAKS[k],
                )
        contributions.append(total)
    density = Fraction(sum(contributions), 10000)
    return contributions, density


def color_of(m, n):
    for j in range(10):
        if 100 * m < BREAKS[j + 1] * n:
            return COLORS[j]
    return COLORS[-1]


def finite_count(n):
    colors = [0] + [color_of(m, n) for m in range(1, n + 1)]
    count = 0
    for x in range(1, n + 1):
        for y in range(1, n - x + 1):
            if len({colors[x], colors[y], colors[x + y]}) == 3:
                count += 1
    return count, Fraction(count, n * (n - 1) // 2)


if __name__ == "__main__":
    contributions, density = exact_density()
    expected_contributions = [0, 0, 280, 648, 648, 220, 1086, 922, 1272, 454]
    assert contributions == expected_contributions
    assert density == Fraction(553, 1000)

    print("scaled contributions:", contributions)
    print("exact limiting density:", density, "=", float(density))

    expected = {
        200: 11114,
        500: 69266,
        1000: 276786,
    }
    for n, expected_count in expected.items():
        count, ratio = finite_count(n)
        assert count == expected_count
        print(f"n={n}: count={count}, ratio={float(ratio):.12f}")
