#!/usr/bin/env python3
"""Arithmetic regression for the Alexander-span filter.

The knot-theoretic inequalities are premises proved in the cited literature.
This finite enumeration checks only that the packaged deductions follow from
those premises and parity; it is not a proof of the knot-theoretic premises.
"""

checked = 0
fail_tau_cases = 0
fail_s_cases = 0

for g in range(0, 9):
    two_g = 2 * g
    for g4 in range(0, g + 1):
        two_g4 = 2 * g4
        for sp_delta in range(0, two_g + 1, 2):
            for deg_pz in range(sp_delta, 2 * g + 7):
                for two_tau in range(0, two_g4 + 1, 2):
                    for abs_s in range(0, two_g4 + 1, 2):
                        checked += 1

                        if two_tau > deg_pz:
                            fail_tau_cases += 1
                            assert sp_delta < two_tau <= two_g
                            assert two_g - sp_delta >= 2

                        if abs_s > deg_pz:
                            fail_s_cases += 1
                            assert sp_delta < abs_s <= two_g
                            assert two_g - sp_delta >= 2

                        if sp_delta == two_g:
                            assert two_tau <= deg_pz
                            assert abs_s <= deg_pz

print(
    "VERIFY_OK "
    f"tuples={checked} "
    f"tau_failure_tuples={fail_tau_cases} "
    f"s_failure_tuples={fail_s_cases}"
)
