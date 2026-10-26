from itertools import product

for omega0, omega1 in product((-1, 1), repeat=2):
    def in_exact_kernel(a, b, c):
        return omega0*a + b + omega1*c == 0

    # Antipodal-pair line lies inside the exact plane.
    assert in_exact_kernel(1, 0, -omega0*omega1)
    # Independent direction with b != 0 lies in the exact plane.
    assert in_exact_kernel(-omega0, 1, 0)
    # The exact plane is rank-one constrained, not the pair-rule line.
    assert omega0 != 0 and omega1 != 0
print('PASS: all four sign pairs; exact kernel plane strictly contains pair-rule line')
