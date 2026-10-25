# Review of the consecutive-deletion pseudo-Frobenius theorem

## Correctness — PASS
The proof derives the exact gap sets from two-generator offset intervals, then establishes a consecutive block of semigroup elements to certify the conductor. Each candidate pseudo-Frobenius number is tested against all generators; every omitted gap is defeated by an explicit generator. Interval cardinalities yield the type and defect formulas, and the Apéry-socle/Koszul argument yields the last Betti number over any coefficient field. The proof explicitly handles the boundary \(j=1\), the boundary \(j=k\), and possible emptiness of the \(j>k\) regime. The standalone separately implemented enumeration returned `VERIFY_OK cases=10857 checked_gap_counts=530299 e_max=48`. Finite tests are supporting evidence only; the interval argument is the infinite proof.

## Originality — PASS, subject to stated residual risk
Goel–Şahin–Singh–Srinivasan, *Numerical Semigroups of Sally Type II*, arXiv:2512.10812v2, Theorems 2.2 and 3.3, explicitly classify the one- and two-deletion cases, not the interior consecutive blocks of \(k\geq3\). Singh–Srinivasan, *Structure and Symmetry of Sally Type Semigroup Rings*, arXiv:2512.18136, studies the exact present family and establishes its Frobenius numbers, genera and Gorenstein symmetry criterion, but its inspected full text does not state general pseudo-Frobenius sets, an all-type bijection, or last Betti numbers across positions. The previously established symmetric case is acknowledged rather than reclaimed. Published record searches did not identify a stronger equivalent result. An unindexed manuscript, alternative parametrization, or unavailable full text could still contain equivalent formulas; absence from search is not proof of uniqueness.

## Mathematical value — PASS
For any fixed multiplicity and embedding dimension in the substantial family \(e\geq2k+1\), the theorem realizes each nonmaximal Cohen–Macaulay type exactly once by varying only the consecutive deletion position. This is a complete realization spectrum, not a single parameter substitution. Explicit pseudo-Frobenius sets resolve the socle and the terminal Betti number, while the exact almost-symmetry defect measures non-Gorenstein behavior. The earlier symmetry characterization alone neither determines the type spectrum nor the pseudo-Frobenius generators.

## Scope and limits
The theorem does not cover \(e\leq2k\), disconnected deletion sets, intermediate Betti numbers, or a general uniqueness theorem over all literature. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
