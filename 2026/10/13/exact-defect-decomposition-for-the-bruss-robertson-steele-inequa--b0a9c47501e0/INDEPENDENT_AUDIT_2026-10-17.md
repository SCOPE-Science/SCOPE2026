# Independent mathematical audit

## correctness

PASS

For any feasible cardinality-optimal index set A, the Rogers dual at eta=1/t is |B|+(s-S_B)/t. Subtract N=|A|, write |A|=S_A/t+sum_{i in A}(1-x_i/t), and separate B\A versus A\B: the defect is exactly (s-S_A+sum_{A triangle B}|x_i-t|)/t, both terms nonnegative. Taking expectations uses E S_B=s and E|B|=sum F_i(t). Equality requires and is implied by S_B=s almost surely since every x outside B exceeds t (ties have zero probability). Independence with a nondegenerate bounded truncated variable implies Var(S_B)>0. Independently verified exact rational arithmetic for 12,480 fixed finite configurations; the unrestricted proof is algebraic, not enumeration.

## originality

PASS

Rogers 2023 gives the LP dual certificate and BRS inequality; Bruss 2021 Theorem 3 subtracts only expected unused budget. Comparing the actual equalities, the mismatch sum and a.s.-constant-threshold characterization are not provided by those sources. The result is the full pathwise complementarity defect, not a stronger universal marginal-only bound.

## value

PASS

The exact two-part slack and equality condition answer a natural structural question about an influential stochastic packing inequality. They separate unused-capacity loss from disagreement with the threshold policy and characterize when the classical expected bound is sharp under arbitrary dependence; this is more informative than restating the old upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
