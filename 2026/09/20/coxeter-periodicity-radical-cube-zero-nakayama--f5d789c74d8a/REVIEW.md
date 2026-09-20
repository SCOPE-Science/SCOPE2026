# Review: exact Coxeter periodicity for radical-cube-zero linear Nakayama algebras

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proof was checked separately in its odd- and even-dimensional parts.

For odd n, the known six-step Coxeter-polynomial recurrence is sufficient to derive the two displayed closed forms by induction. Their divisibility by 1+x^3 follows from the relevant exponent being an odd multiple of 3 in the periodic cases and an even multiple of 3 in the nonperiodic cases. Root multiplicities were checked directly from the factorizations: in residues 1, 3, 5, 7 modulo 12 the characteristic polynomial is squarefree; in residues 9 and 11 modulo 12, eigenvalue 1 has algebraic multiplicity exactly two and every other root is simple.

The possible weakness that a repeated root of unity need not imply nonperiodicity was addressed explicitly. The eigenspace at 1 is computed from ker(C_n+C_n^T). The induced fifth-order band recurrence reduces to the stated 12-periodic two-parameter pattern. Substitution into the final two boundary equations leaves one free parameter for both n congruent to 9 and n congruent to 11 modulo 12. Thus geometric multiplicity is one, so there is a 2x2 Jordan block at 1 and finite order is impossible.

For even n=2m, the cited derived-equivalent model A_m tensor A_2 reduces the problem to a tensor product of Dynkin Coxeter transformations. The eigenvalue-ratio argument forces every common exponent to be divisible by m+1 and 3, while the overall minus sign forces even parity; the converse is immediate. This gives the exact order lcm(2,3,m+1), not merely an upper bound.

Exact symbolic computations independently checked the odd characteristic-polynomial formulas through n=39 and the predicted finite/infinite behavior and exact periods through n=29. The computations are supporting evidence only; the theorem does not depend on finite enumeration.

## Originality — PASS, to the best of our knowledge

A 2020 MathOverflow question explicitly asks, for fixed r>=3, which matrices M_{n,r} are periodic and what their periods are; it identifies them with the Coxeter matrices of A_n/J^r. The currently indexed page has no posted answer. The theorem resolves the complete r=3 subproblem.

The most directly relevant older source located is de la Peña's 2014 work on cyclotomic Coxeter polynomials. A 2019 open chapter by the same author explicitly recalls that argument for N_n^3=A_n/J^3: it proves cyclotomicity for every n, gives the derived-equivalent tensor-product model in even dimension, and records the six-step Coxeter-polynomial recurrence. It does not state the periodic/nonperiodic residue classification or exact periods. The distinction is substantive because cyclotomic characteristic polynomial does not imply finite matrix order when nontrivial Jordan blocks occur; the theorem identifies precisely that obstruction.

Searches for the exact matrix family, A_n/J^3, N_n^3, Coxeter periods, radical-cube-zero linear Nakayama algebras, residue-class formulas, and Jordan obstructions did not locate prior coverage. Recent 2025--2026 work on linear Nakayama algebras and on Coxeter matrices concerns different homological or combinatorial questions and did not reveal this classification.

Residual risk remains. The full text of the 2014 article was not inspected, although the same author's later open exposition says it is recalling that argument in detail and presents it as a cyclotomicity result. The 2020 question also cites an older table of computed periods; the table was not treated as establishing a general theorem. An equivalent formula in obscure notes or differently indexed literature therefore remains possible.

## Value — PASS

The result completely resolves a concrete fixed-r instance of an explicit representation-theoretic periodicity problem. It gives exact orders in every finite-order case and explains an infinite family of failures by a precise Jordan-theoretic mechanism. It also isolates a reusable warning: for Coxeter transformations, cyclotomicity of the characteristic polynomial can conceal a unipotent obstruction to periodicity.

## Scientific limitations

The theorem is restricted to r=3 and gives no classification for r>=4. The originality assessment is qualified by the inaccessible 2014 full text and by the possibility of equivalent unpublished or weakly indexed formulas. The finite symbolic checks are not exhaustive and are not used as a substitute for proof.
