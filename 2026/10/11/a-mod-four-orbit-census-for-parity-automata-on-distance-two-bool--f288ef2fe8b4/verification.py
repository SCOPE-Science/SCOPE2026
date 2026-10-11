"""Independent finite-field checks for the distance-two Hamming parity dynamics.

Execute with Python 3.10+: python verification.py
The universal theorem requires the separate algebraic proof.
"""
from itertools import combinations


def theoretical_rank(n):
    return 1 << (n - 1) if n % 2 == 0 else (1 << (n - 1)) - (1 << ((n - 1) // 2))


def parity_shift_matrix_rows(n):
    """Full binary adjacency matrix with one Python bitset per output vertex."""
    v = 1 << n
    offsets = tuple((1 << i) ^ (1 << j) for i, j in combinations(range(n), 2))
    rows = [sum(1 << (vertex ^ mask) for mask in offsets) for vertex in range(v)]
    if (n * (n - 1) // 2) % 2:
        rows = [row ^ (1 << k) for k, row in enumerate(rows)]
    return rows


def gf2_rank(rows):
    pivots = {}
    for entry in rows:
        v = entry
        while v:
            k = v.bit_length() - 1
            if k not in pivots:
                pivots[k] = v
                break
            v ^= pivots[k]
    return len(pivots)


def apply(rows, state):
    return sum(((row & state).bit_count() & 1) << k for k, row in enumerate(rows))


def test():
    count = 0
    for n in range(2, 11):
        N = 1 << n
        rows = parity_shift_matrix_rows(n)
        expected_rank = theoretical_rank(n)
        observed_rank = gf2_rank(rows)
        assert observed_rank == expected_rank, (n, observed_rank, expected_rank)
        count += 1
        # Verify zero square on every basis vector, without using theorem's symbolic representation.
        for col in range(N):
            mask = sum(((row >> col) & 1) << i for i, row in enumerate(rows))
            assert apply(rows, mask) == 0, (n, col)
            count += 1
        if n <= 4:
            parity = ((n * (n - 1) // 2) & 1)
            fixed = 0
            two_cycles_states = 0
            first_step_zero = 0
            step_two_zero = 0
            for state in range(1 << N):
                # adjacency = N_operator + cI
                next_state = apply(rows, state) ^ (state if parity else 0)
                next2 = apply(rows, next_state) ^ (next_state if parity else 0)
                assert next2 == (state if parity else 0)
                if parity:
                    if next_state == state:
                        fixed += 1
                    else:
                        two_cycles_states += 1
                else:
                    if next_state == 0:
                        first_step_zero += 1
                    else:
                        step_two_zero += 1
            assert first_step_zero + step_two_zero == (1 << N) if not parity else True
            if parity:
                assert fixed == 1 << (N - expected_rank)
                assert two_cycles_states == (1 << N) - fixed
            else:
                assert first_step_zero == 1 << (N - expected_rank)
                assert step_two_zero == (1 << N) - first_step_zero
            count += 1 << N
        print(f"dimension={n}, vertices={N}, square-zero-shift-rank={observed_rank}, checks-complete")
    print(f"VERIFY_OK; assertions={count}")


if __name__ == "__main__":
    test()
