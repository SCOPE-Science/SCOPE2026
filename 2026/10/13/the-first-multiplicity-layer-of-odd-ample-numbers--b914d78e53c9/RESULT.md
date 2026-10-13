# The first multiplicity layer of odd ample numbers
## Finding
Let \(a(n)\) be the recursive-divisor function
\[
a(1)=1,\qquad a(n)=1+\sum_{\substack{d\mid n\\ d<n}}a(d),
\]
and call \(n\) ample when \(a(n)>n\). Let \(\Omega(n)\) count prime factors with multiplicity.

Every odd ample integer satisfies
\[
\Omega(n)\ge17.
\]
The bound is sharp. The integer
\[
N_0=3^8\cdot5^4\cdot7^2\cdot11\cdot13\cdot17=488462349375
\]
has \(\Omega(N_0)=17\) and
\[
a(N_0)=523830280192>N_0.
\]

At the boundary \(\Omega(n)=17\), the only exponent multisets that can support an odd ample integer are
\[
(8,4,2,1,1,1),\qquad (7,4,3,1,1,1),\qquad (7,4,2,1,1,1,1).
\]
Their least odd representatives are respectively \(488462349375\), \(1139745481875\), and \(3093594879375\). Thus \(N_0\) is the least odd ample integer in the first possible multiplicity layer.

## Assumptions and scope
The theorem concerns positive odd integers. The function \(a(n)\) is exactly the recursive-divisor function introduced in the cited work. The source proves, and the defining recurrence makes transparent, that \(a(n)\) depends only on the multiset of exponents in the prime factorization of \(n\).

The result is a sharp statement about total prime-factor multiplicity \(\Omega\), not about numerical size. The source's least odd ample integer by value is
\[
3^9\cdot5^5\cdot7^2\cdot11\cdot13=430996190625,
\]
which has \(\Omega=18\). No classification is claimed for all odd ample integers with \(\Omega\ge18\).

## Proof
Write the exponent multiset of an odd integer in decreasing order as
\[
\lambda=(\lambda_1,\ldots,\lambda_r),\qquad
\lambda_1\ge\cdots\ge\lambda_r\ge1.
\]
Because \(a(n)\) depends only on this multiset, write its common value as \(A(\lambda)\).

For a fixed exponent multiset, the least odd integer having that multiset is
\[
m(\lambda)=3^{\lambda_1}5^{\lambda_2}7^{\lambda_3}\cdots p_r^{\lambda_r},
\]
where \(3,5,7,\ldots,p_r\) are the first \(r\) odd primes. Indeed, the prime bases must be at least these primes, and if \(p<q\) but exponents \(e<f\) are assigned in the opposite order, swapping them multiplies the number by \((p/q)^{f-e}<1\). Repeating swaps assigns the largest exponents to the smallest primes.

Consequently, if \(A(\lambda)\le m(\lambda)\), then no odd integer of signature \(\lambda\) is ample. Conversely, if \(A(\lambda)>m(\lambda)\), the least representative itself is ample.

It remains to make a finite, exhaustive signature census. The bundled verifier generates every integer partition \(\lambda\) of each \(k\) from \(1\) through \(17\). For each partition it computes \(A(\lambda)\) directly from the defining recurrence. If \(\mu\) ranges over all componentwise sub-exponent vectors with \(0\le\mu_i\le\lambda_i\), except \(\mu=\lambda\), then
\[
A(\lambda)=1+\sum_{\mu<\lambda} A(\operatorname{sort}(\mu_1,\ldots,\mu_r)),
\]
with zero components removed. Each sub-exponent vector corresponds to exactly one proper divisor, so this recursion is exact.

For each \(k\), the table shows the exponent partition maximizing the exact ratio \(A(\lambda)/m(\lambda)\) among all partitions of \(k\):

| \(k\) | partitions | maximizing \(\lambda\) | \(A(\lambda)\) | \(m(\lambda)\) |
| ---: | ---: | --- | ---: | ---: |
| 1 | 1 | \((1)\) | 2 | 3 |
| 2 | 2 | \((2)\) | 4 | 9 |
| 3 | 3 | \((2,1)\) | 16 | 45 |
| 4 | 5 | \((3,1)\) | 40 | 135 |
| 5 | 7 | \((3,1,1)\) | 264 | 945 |
| 6 | 11 | \((4,1,1)\) | 736 | 2835 |
| 7 | 15 | \((4,2,1)\) | 3776 | 14175 |
| 8 | 22 | \((5,2,1)\) | 11072 | 42525 |
| 9 | 30 | \((5,2,1,1)\) | 130496 | 467775 |
| 10 | 42 | \((5,2,1,1,1)\) | 1742912 | 6081075 |
| 11 | 56 | \((5,2,2,1,1)\) | 13856000 | 42567525 |
| 12 | 77 | \((5,3,2,1,1)\) | 84656640 | 212837625 |
| 13 | 101 | \((6,3,2,1,1)\) | 320061568 | 638512875 |
| 14 | 135 | \((7,3,2,1,1)\) | 1137195136 | 1915538625 |
| 15 | 176 | \((7,3,2,1,1,1)\) | 22784586880 | 32564156625 |
| 16 | 231 | \((7,4,2,1,1,1)\) | 140023741312 | 162820783125 |
| 17 | 297 | \((8,4,2,1,1,1)\) | 523830280192 | 488462349375 |

For every \(k\le16\), even the maximizing ratio is strictly below \(1\), so every odd integer with \(\Omega(n)\le16\) is depleted. At \(k=17\), exact enumeration finds precisely three partitions with \(A(\lambda)>m(\lambda)\), namely the three listed in the finding. The least corresponding representative is \(N_0\), and its exact excess is
\[
a(N_0)-N_0=35367930817.
\]
This proves the threshold, the boundary signature classification, and the least boundary-layer example.

## Verification
Run `python3 verify.py`. The verifier uses integer arithmetic only for theorem checks. It generates the standard partition counts through \(17\), checks all \(1211\) partitions with total size from \(1\) through \(17\), verifies the strict inequalities for every partition below the boundary, and identifies exactly the three qualifying signatures at the boundary.

As an independent normalization check, the verifier also evaluates \(a(n)\) directly on the actual divisor lattices of \(N_0\) and of the source's least odd ample example. The two divisor-lattice computations involve \(1080\) and \(720\) divisors respectively and reproduce \(523830280192\) and \(436791402496\). `partition_certificate.json` records the complete per-layer maxima and boundary data. A successful replay ends with `VERIFY_OK`.

The finite census is part of the proof, not an extrapolation from a numerical search range: integer partitions exhaust all possible exponent multisets at the stated values of \(\Omega\).

## Relationship to prior work
Fink introduced the recursive-divisor function in 2019 and later introduced ample numbers in 2020. The ample-number paper emphasizes that odd ample numbers exist but are rare, gives the least odd ample number by value as \(3^9\cdot5^5\cdot7^2\cdot11\cdot13\), and states a prime-avoidance conjecture. It does not state a lower bound for \(\Omega\) or classify the first multiplicity layer.

Two later papers derive Dirichlet-series, convolution, ordered-factorization, and closed-form representations for the same recursive-divisor function. These formulas provide alternative ways to evaluate \(a(n)\), but the inspected texts do not give the odd-ample multiplicity threshold or the boundary signature classification.

The exact sequence OEIS A067824 records the recursive-divisor function and its recurrence. It does not contain a classification by total prime-factor multiplicity. The integer \(488462349375\) also occurs independently in OEIS A171080, a sequence arising from a different product formula; that numerical coincidence does not assert or imply recursive abundance.

A previously published existence theorem for ample numbers on sufficiently abundant finite prime supports proves infinitely many prime-avoidance examples, but it gives no lower bound on \(\Omega\) and does not imply the present boundary classification.

## Limitations
The theorem determines only the first possible total-prime-factor layer for odd ample numbers and the exponent signatures that occur at that layer. It does not classify all odd ample integers with \(\Omega(n)=17\) inside those three signatures, nor does it classify higher multiplicity layers.

Originality searches cannot exclude an unindexed historical observation. The proof is computer-assisted in one finite step: the \(1211\)-partition census. The bundled code is short, deterministic, uses exact integer arithmetic for acceptance, and is accompanied by a machine-readable certificate and two independent direct divisor-lattice checks.

## References
1. Thomas Fink, “Recursively divisible numbers,” arXiv:1912.07979v1, first posted 17 December 2019; journal version DOI:10.1016/j.jnt.2023.08.008.
2. Thomas Fink, “Recursively abundant and recursively perfect numbers,” arXiv:2008.10398v1, first posted 24 August 2020.
3. T. M. A. Fink, “Properties of the recursive divisor function and the number of ordered factorizations,” arXiv:2307.09140v1, first posted 18 July 2023.
4. T. M. A. Fink, “Number of ordered factorizations and recursive divisors,” arXiv:2307.16691v1, first posted 31 July 2023.
5. OEIS A067824, recursive-divisor sequence.
