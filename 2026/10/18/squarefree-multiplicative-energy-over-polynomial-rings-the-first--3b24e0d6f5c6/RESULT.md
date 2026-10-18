# Squarefree multiplicative energy over polynomial rings: the first correction

## Finding
Let \(q\) be any prime power, \(d\ge2\) a fixed integer, and \(\mathcal S_d(q)\) the monic squarefree polynomials of degree exactly \(d\) in \(\mathbb F_q[T]\). Define the ordered multiplicative energy
\[
\mathcal E_d(q)=\#\{(A,B,C,D)\in\mathcal S_d(q)^4:AB=CD\}.
\]
As \(q\) runs through prime powers tending to infinity,
\[
\boxed{\mathcal E_d(q)=(d+1)q^{2d}-(9d-8)q^{2d-1}+O_d(q^{2d-2}).}
\]
The constant in the error term depends only on the fixed degree \(d\), uniformly in the characteristic. In the first nontrivial degree the *exact* identity, valid for every prime power \(q\), is
\[
\boxed{\mathcal E_2(q)=3q^4-10q^3+12q^2-5q.}
\]
For comparison, without squarefreeness the energy is exactly \((d+1)q^{2d}-dq^{2d-1}\) (Afifurrahman, Theorem 2.2). The first-order squarefree penalty is therefore \(8(d-1)q^{2d-1}\).

## Assumptions and scope
All four factors are monic, squarefree, and have the *same exact positive degree* \(d\). Ordered tuples are counted; factors \(A\) and \(B\) may have common factors, as may \(C\) and \(D\). No restriction on the characteristic is imposed. The limiting parameter is the field size \(q\), not the polynomial degree. The case \(d=1\) is \(\mathcal E_1(q)=2q^2-q\) and follows directly from unique factorization; the displayed general coefficient concerns \(d\ge2\).

## Proof
**Canonical parametrization.** Set \(U=\gcd(A,C)\), monic, and write \(A=UV\), \(C=UW\) with \(\gcd(V,W)=1\). The equation \(AB=CD\) forces \(B=WX\) and \(D=VX\) for a unique monic \(X\). The common degree condition gives
\[
\deg V=\deg W=b,\qquad \deg U=\deg X=a=d-b,\qquad 0\le b\le d.
\]
Conversely every such tuple \((U,V,W,X)\) with \(\gcd(V,W)=1\) produces exactly one ordered solution.

**Squarefree local constraints.** The four factors \(UV,WX,UW,VX\) are squarefree exactly when each of \(U,V,W,X\) is squarefree and each of the five edges
\[
(U,V),\ (U,W),\ (V,W),\ (V,X),\ (W,X)
\]
is coprime. Sharing an irreducible factor between \(U\) and \(X\) is permitted. The six choices of a given monic irreducible \(P\) of degree \(k\) are: absent; present only in \(U\), \(X\), \(V\), or \(W\); or present in both \(U\) and \(X\). This also gives the exact coefficient identity
\[
\mathcal E_d(q)=\sum_{b=0}^{d}[u^{d-b}x^{d-b}v^bw^b]\prod_{P\ \mathrm{monic\ irreducible}}\left(1+u^{\deg P}+x^{\deg P}+(ux)^{\deg P}+v^{\deg P}+w^{\deg P}\right).
\]
Only irreducibles of degree at most \(d\) affect the stated coefficient, so this is a finite effective identity.

**Uniform first-order sieve.** There are \(q^{2d}\) unrestricted choices of the four monic parameters at each \(b\). For any fixed positive-degree monic variables, the probability that a specified pair shares a factor is \(q^{-1}+O_d(q^{-2})\). For any fixed variable of degree at least \(2\), the probability it has a squared irreducible factor is \(q^{-1}+O_d(q^{-2})\). These statements hold uniformly for all prime powers: among the \(q\) monic linear polynomials, a specified root divides two given independent positive-degree monic polynomials with probability \(q^{-2}\), or its square divides one given monic polynomial of degree at least \(2\) with probability \(q^{-2}\). Contributions from irreducibles of degree \(k\ge2\) total \(O_d(q^{-2})\), since there are at most \(q^k\) such polynomials and a specified event has probability \(q^{-2k}\). Distinct bad events intersect with probability \(O_d(q^{-2})\): events at distinct linear primes impose four independent root conditions, and two distinct restrictions at the same linear prime impose at least three. This proves by inclusion-exclusion that for each \(b\), the number of admissible parameter tuples is
\[
q^{2d}\left(1-\frac{c_{a,b}}q+O_d(q^{-2})\right),
\quad c_{a,b}=5\mathbf1_{a,b\ge1}+2\mathbf1_{a\ge2}+2\mathbf1_{b\ge2}
\]
when \(a,b\ge1\); at the endpoints the five edge restrictions contribute respectively \(0\) when \(b=0\), and \(1\) when \(a=0\). Explicitly \(c_{d,0}=2\) and \(c_{0,d}=3\) for \(d\ge2\). For \(1\le b\le d-1\), \(c_{d-b,b}=5+2\mathbf1_{d-b\ge2}+2\mathbf1_{b\ge2}\). Thus
\[
\sum_{b=0}^d c_{d-b,b}=2+3+5(d-1)+4(d-2)=9d-8.
\]
Summing the \(d+1\) strata proves the uniform two-term formula.

**Exact quadratic-degree identity.** For \(d=2\), the three strata \(b=0,1,2\) have counts, respectively,
\[
(q^2-q)^2,\qquad q(q-1)(q-2)^2,\qquad q(q-1)^3.
\]
The first selects two arbitrary squarefree quadratics; the second selects two different linear polynomials \(V,W\) and then \(U,X\) each avoiding their roots. For the third, ordered coprime squarefree quadratic pairs are counted by classifying the first quadratic as irreducible or a product of two distinct linear factors: there are \(q(q-1)/2\) of each kind, leaving respectively \(q^2-q-1\) or \(q^2-3q+3\) choices for the second. Summation yields \(q(q-1)^3\). Expanding the three strata yields the displayed polynomial identity for all prime powers.

## Verification
The accompanying `verify.py` enumerates monic squarefree polynomials and groups products into exact ordered-pair multiplicities for several finite prime fields. It checks the degree-two polynomial identity and compares direct energy counts with the canonical-gcd parametrization. This is a finite independent consistency test; the universal asymptotic comes from the inclusion-exclusion proof above, not the enumeration. Invoke `python3 verify.py` from the extracted artifact directory; no third-party packages are needed.

## Relationship to prior work
Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first posted 2026-10-08), Theorem 2.2 and its proof, computes unrestricted prescribed-degree product energy. Its expression \((d+1)q^{2d}-dq^{2d-1}\) does not impose any squarefree restriction on individual factors and therefore does not give the five-edge local exclusion coefficient \(9d-8\). Sawin, *Square-root cancellation for sums of factorization functions over squarefree progressions in \(\mathbb F_q[t]\)*, arXiv:2102.09730, Theorems 1.1–1.3, treats distribution in arithmetic progressions with squarefree *moduli*, rather than this four-factor squarefree multiplicative energy. The exact two-variable local prime choices and first correction stated here were not found in the inspected works.

## Limitations
No fixed-\(q\), growing-\(d\) asymptotic or prime-field-only refinement is claimed. The proof does not yield a dimension-uniform error constant. The result uses classical squarefree and coprimality sieve estimates and could conceivably be implicit in a more general Euler-product treatment not located in the literature. Novelty has not been independently validated. The exact coefficient identity counts only four individually squarefree factors and does not require their common products to be squarefree.

## References
1. M. Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1, 2026, https://arxiv.org/pdf/2610.11240; Theorem 2.2, Sections 2.1 and 5.
2. W. Sawin, *Square-root cancellation for sums of factorization functions over squarefree progressions in \(\mathbb F_q[t]\)*, arXiv:2102.09730v2, 2022, https://arxiv.org/pdf/2102.09730; Theorems 1.1–1.3.
3. J. P. Keating, B. Rodgers, E. Roditty-Gershon and Z. Rudnick, *Sums of divisor functions in \(\mathbb F_q[t]\) and matrix integrals*, 2017, Oxford Research Archive record c94ce0fb-a6e8-4744-afa2-5b3f1f4370c6 (background on unrestricted divisor-function moments).
