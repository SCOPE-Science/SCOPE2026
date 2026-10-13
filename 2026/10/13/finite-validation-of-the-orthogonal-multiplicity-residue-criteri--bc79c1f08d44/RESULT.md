# Finite validation of the orthogonal-multiplicity residue criterion through degree 22
## Finding
For every squarefree monic polynomial \(f\in\mathbb F_2[T]\) with \(15\leq\deg f\leq22\) and \(\gcd(f,T(T+1))=1\), the orthogonal multiplicity \(m(f)\) is positive if and only if
\[
\psi_P(f)=0
\]
for every non-linear monic irreducible divisor \(P\mid f\). Here, because \(f\) is squarefree and prime to \(T(T+1)\), every such pole is simple and
\[
\psi_P(f)=\operatorname{Tr}_{\mathbb F_P/\mathbb F_2}\!\left(\frac{1}{T(T+1)(f/P)P'}\right),
\]
with all factors inside the trace reduced modulo \(P\).

The exhaustive check covers exactly 1,856,852 polynomials in degrees \(15\) through \(22\), with zero mismatches. The motivating source reports the same criterion as conjectural and verifies the prime-to-\(T(T+1)\), squarefree case only through degree \(14\). Thus the verified finite range in this natural class extends through degree \(22\).

## Assumptions and scope
Let \(\mathbb A=\mathbb F_2[T]\). For a monic polynomial \(f\) of degree \(d\), its orthogonal multiplicity \(m(f)\) is the number of numerators \(g\) with \(\deg g<d\), \(\gcd(g,f)=1\), and all partial quotients of \(g/f\) of degree one. The claim is finite: it concerns squarefree monic \(f\) with \(15\leq d\leq22\) and \(f(0)=f(1)=1\). It makes no assertion for repeated irreducible factors, for either linear factor \(T\) or \(T+1\), or for degrees above \(22\).

For a word \(w=(a_1,\ldots,a_d)\in\{T,T+1\}^d\), define its continuant by \(K_{-1}=0\), \(K_0=1\), and \(K_i=a_iK_{i-1}+K_{i-2}\). The standard word parametrization implies that \(m(f)>0\) exactly when \(f=K_d(w)\) for at least one such word.

## Proof
The finite statement is proved by exhaustive exact arithmetic over \(\mathbb F_2[T]\).

For each degree \(d\in\{15,16,\ldots,22\}\), the verifier first enumerates every one of the \(2^d\) words in \(\{T,T+1\}^d\) and marks the denominator continuants \(K_d(w)\). Membership in this marked set is therefore exactly the predicate \(m(f)>0\).

It then enumerates every monic degree-\(d\) polynomial, retains exactly those satisfying \(\gcd(f,f')=1\), \(f(0)=1\), and \(f(1)=1\), and factors each retained polynomial exactly. For a squarefree polynomial of degree at most \(22\), trial division by all monic irreducibles of degree at most half the total degree removes every possible small factor; any remaining nonconstant factor must be irreducible, because a composite remainder would have an irreducible factor of degree at most half its degree and hence at most half the original degree.

For every non-linear factor \(P\), the verifier computes \(P'\), the residue inverse modulo \(P\), and the finite-field trace by repeated Frobenius squaring. All operations are bitwise polynomial arithmetic over \(\mathbb F_2\), so no floating-point approximation enters. It compares the conjunction \(\psi_P(f)=0\) over all non-linear \(P\mid f\) with the exact continuant-membership predicate.

The degree-by-degree census is:

| \(d\) | tested squarefree polynomials prime to \(T(T+1)\) | mismatches |
| ---: | ---: | ---: |
| 15 | 7,286 | 0 |
| 16 | 14,559 | 0 |
| 17 | 29,132 | 0 |
| 18 | 58,249 | 0 |
| 19 | 116,514 | 0 |
| 20 | 233,011 | 0 |
| 21 | 466,040 | 0 |
| 22 | 932,061 | 0 |
| total | 1,856,852 | 0 |

Therefore the stated equivalence holds for every polynomial in the claimed finite domain.

## Verification
Compile and run `verify.cpp` with a C++17 compiler. The replay used exact integer and binary-polynomial arithmetic and ended with:

`VERIFY_OK degrees=15..22 coprime_squarefree_cases=1856852 mismatches=0`

As an independent internal consistency check on the continuant side, direct counts of distinct marked denominators in degrees \(15\) through \(22\) were \(10302,19921,38680,75053,146230,284755,556082,1085674\), exactly matching the table in arXiv:2610.02352v1 for those degrees.

## Relationship to prior work
The motivating preprint arXiv:2610.02352v1 introduces the residues \(\psi_P(f)\), states the equivalence between positivity of \(m(f)\) and vanishing of every non-linear local residue as its equation (4), and explicitly leaves that equivalence unproved. Its numerical evidence verifies equation (4) for squarefree polynomials only through degree \(14\); in the prime-to-\(T(T+1)\) class it reports 7,276 checked cases. The present result extends precisely that finite verification, without changing the conjecture, to every degree through \(22\) in the same prime-to-linear squarefree class.

Blackburn's 1998 work supplies the structural orthogonal-multiplicity framework, including the fact that positive multiplicity is a power of two indexed by non-linear prime factors. The recent source notes that Blackburn's published multiplicity table reaches degree \(21\). The new cutoff \(22\) therefore also crosses that historical tabulation boundary. Lauder's 1999 work and thesis develop related continued-fraction criteria; the recent source explicitly notes that criteria of this kind occur there, while nevertheless treating its residue criterion (4) as conjectural rather than as a known consequence.

## Limitations
This is an exact finite verification, not a proof of the criterion in arbitrary degree. It does not address nonsquarefree polynomials or the cases divisible by \(T\) or \(T+1\). The older Lauder thesis was not available for full-text comparison in this check; the novelty comparison therefore relies in part on the motivating source's explicit discussion of Lauder and its statement that equation (4) remains an unproved input. That creates a residual literature-equivalence risk, but no searched source was found to state the degree-\(22\) exhaustive validation or a theorem that would subsume it.

## References
1. D. Niedbala Giraudin, *The proportion of polynomials over \(\mathbb F_2\) with positive orthogonal multiplicity*, arXiv:2610.02352v1, first public version 2026-10-01.
2. S. R. Blackburn, *Orthogonal Sequences of Polynomials over Arbitrary Fields*, Journal of Number Theory 68 (1998), 99--111, DOI: 10.1006/jnth.1997.2201.
3. A. G. B. Lauder, *Continued fractions of Laurent series with partial quotients from a given set*, Acta Arithmetica 90 (1999), 251--271.
