# Independent audit — 2026-10-01

## Record

**Uniqueness of the primitive three-prime Lucas-Carmichael number**

Final claim: If a three-prime Lucas-Carmichael number \(n=pqr\) satisfies \(\gcd(p+1,q+1,r+1)=2\), then \((p,q,r)=(5,13,31)\), and conversely; hence \(2015\) is the unique primitive three-prime case.

Disposition: **PASSED**

## Correctness — PASS

Fresh proof reconstruction verifies the pairwise-coprimality step modulo \(2d\), the lcm quotient \(T\in\{1,2,3\}\), all three quotient cases, and the final direct divisibility check. An independent integer search of the remaining \(\lambda=1\), \(a\le4\) algebra recovered only \((a,b,c)=(3,7,16)\).

## Originality — PASS

Tamilvanan–Muthukrishnan Theorem 4.2 gives the general representation \((2hr_1-1)(2hr_2-1)(2hr_3-1)\) with pairwise-coprime \(r_i\), but the inspected full text does not classify \(h=1\). OEIS A006972 lists 2015 and general Lucas-Carmichael data without the uniqueness theorem. Targeted exact/synonym searches found no earlier classification.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Primary-source inspections and residual access risks are also recorded there.

## Scientific value — PASS

The minimal common shifted-factor gcd is a natural invariant in the standard three-prime decomposition, and the theorem gives a complete cutoff-free classification of that extremal stratum rather than a bounded census.

## Checked scientific sources

- Tamilvanan–Muthukrishnan, A New Characterization for the Lucas-Carmichael Integers and Sums of Base-p Digits, arXiv:2311.08012.
- Wright, There Are Infinitely Many Elliptic Carmichael Numbers, Bull. LMS 50 (2018), arXiv:1609.00231.
- OEIS A006972.
- Published-record semantic search for primitive three-prime Lucas-Carmichael classification.

## Residual risks

- Because the argument is elementary, older problem literature or differently indexed Lucas-Carmichael notes could contain the same specialization.

## Verification boundary

The audit reconstructed the argument and performed fresh algebraic or logical checks where needed. Existing package logs were treated as supporting evidence only. No formal proof-assistant or expert attestation is asserted.
