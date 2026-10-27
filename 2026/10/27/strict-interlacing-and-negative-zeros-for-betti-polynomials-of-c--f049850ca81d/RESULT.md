# Strict interlacing and negative zeros for Betti polynomials of cyclic rational-curve compactifications

## Finding

Fix integers \(r\ge 2\) and \(n\ge 0\), and a primitive \(r\)-th root of unity \(\zeta\). Write \(X_{r,n}=\overline{\mathcal L}^{r}_{n}(\zeta)\) for the connected component of the smooth projective moduli space of stable rational curves with a cyclic action introduced by Clader–Damiolini–Huang–Li–Ramadas. Define the even Poincaré polynomial
\[
P_{n}^{(r)}(t)=\sum_{j=0}^{n}b_{2j}(X_{r,n})t^{j},\qquad b_{2j}=\dim_{\mathbb Q}H^{2j}(X_{r,n};\mathbb Q).
\]
Then \(P_{0}^{(r)}=1\), and for every \(n\ge1\), the monic polynomial \(P_n^{(r)}\) has precisely \(n\) **distinct, strictly negative real zeros**. For \(n\ge2\), the zeros of \(P_{n-1}^{(r)}\) strictly interlace those of \(P_n^{(r)}\). In particular, the Betti numbers are strictly log-concave in internal degrees for \(n\ge2\); indeed their binomially normalized sequence is strictly log-concave. This proves, and strengthens, Conjecture 4.15 of Clader–Damiolini–Li–Ramadas for all \(r\ge2\) and \(n\ge0\).

The full space (without fixing \(\zeta\)) has \(\varphi(r)\) isomorphic components; multiplying \(P_n^{(r)}\) by the positive integer \(\varphi(r)\) preserves all root and log-concavity statements.

## Assumptions and scope

The base field is \(\mathbb C\). The spaces are the maximal-building-set wonderful compactifications of the \(r\) coordinate-hyperplane arrangements in each factor of \((\mathbb P^1)^n\), as in Theorem 3.4 of the cited paper. All cohomology is singular cohomology with rational coefficients. By the iterated blow-up presentation of these spaces, their odd-degree cohomology vanishes and their Chow ranks equal their even Betti numbers. The claim concerns the cohomology *ranks*, not multiplication in their Chow rings or individual cohomology representations.

## Proof

**1. Exact formula from the established additive Chow decomposition.** Theorem 4.13 of Clader–Damiolini–Li–Ramadas supplies one summand for each ordered tuple \(\mathbf j=(j_1,\ldots,j_\ell)\) with each \(j_a\ge2\) and \(s=j_1+\cdots+j_\ell\le n\). The number of decorated chains with these jumps is \(n!r^s/((n-s)!\prod_a j_a!)\); the degree shifts range independently over \(1\le\mu_a\le j_a-1\). Including the empty tuple, this gives
\[
P_n^{(r)}(t)=(1+t)^n+
\sum_{\ell\ge1}\ \sum_{\substack{j_1,\ldots,j_\ell\ge2\\s=\sum_a j_a\le n}}
\frac{n!\,r^{s}}{(n-s)!\prod_{a=1}^{\ell}j_a!}
(1+t)^{n-s}\prod_{a=1}^{\ell}\left(t+t^2+\cdots+t^{j_a-1}\right).
\tag{1}
\]
This is the published decomposition with each ordered jump composition counted once. The formula is empty-sum \((1+t)^n\) for \(n\le1\).

**2. Exponential generating series and a differential recurrence.** Set \(F_r(z,t)=\sum_{n\ge0}P_n^{(r)}(t)z^n/n!\) and
\[
B_r(z,t)=\sum_{j\ge2}\frac{r^jz^j}{j!}(t+\cdots+t^{j-1}).
\]
Ordering the tuple in (1) gives \(F_r=e^{(1+t)z}/(1-B_r)\). The identity
\[
(1-t)B_r=t e^{rz}-e^{rtz}+1-t
\]
therefore yields the formal exponential generating function
\[
F_r(z,t)=\frac{(1-t)e^{[1-(r-1)t]z}}{1-t e^{r(1-t)z}}.
\tag{2}
\]
The apparent singular specialization at \(t=1\) is removable coefficientwise; (2) is an identity over \(\mathbb Q(t)[[z]]\). Direct differentiation and substitution of (2) show
\[
(1-rtz)\partial_zF_r=(1+t+r(r-2)tz)F_r+rt(1-t)\partial_tF_r.
\tag{3}
\]
Comparing coefficients of \(z^n/n!\) gives, for every \(n\ge1\),
\[
\boxed{\ P_{n+1}^{(r)}(t)=\bigl(1+(rn+1)t\bigr)P_n^{(r)}(t)
+rt(1-t)\frac{dP_n^{(r)}}{dt}(t)
+r(r-2)n\,tP_{n-1}^{(r)}(t).\ }
\tag{4}
\]
The initial values are \(P_0^{(r)}=1\) and \(P_1^{(r)}=1+t\). In particular, (4) inductively shows that every \(P_n^{(r)}\) has constant term one and is monic of degree \(n\): its top coefficient in (4) is \((rn+1)-rn=1\), and the final term has degree at most \(n\).

**3. Strict interlacing for all parameters.** Fix \(r\ge2\). The base \(P_1^{(r)}=1+t\) has one simple negative zero, and the polynomial \(P_0^{(r)}=1\) interlaces it vacuously. Inductively suppose \(P_n^{(r)}\) has simple negative zeros \(\rho_1<\cdots<\rho_n<0\), strictly interlaced by the simple negative zeros of the monic \(P_{n-1}^{(r)}\). At any zero \(\rho_i\), (4) reduces to
\[
P_{n+1}^{(r)}(\rho_i)=r\rho_i\left[(1-\rho_i)(P_n^{(r)})'(\rho_i)+(r-2)nP_{n-1}^{(r)}(\rho_i)\right].
\tag{5}
\]
For monic interlacing polynomials, \((P_n^{(r)})'(\rho_i)\) and \(P_{n-1}^{(r)}(\rho_i)\) have exactly the same, nonzero sign, namely \((-1)^{n-i}\). Because \(1-\rho_i>0\), \(r-2\ge0\), and \(r\rho_i<0\), the bracket in (5) is nonzero with that sign, and \(P_{n+1}^{(r)}(\rho_i)\) has the opposite sign. These evaluations alternate in sign. Moreover \(P_{n+1}^{(r)}(0)=1>0\), while monicity gives \(\operatorname{sgn}P_{n+1}^{(r)}(t)=(-1)^{n+1}\) for sufficiently negative real \(t\). Thus each of the \(n+1\) disjoint open intervals
\[
(-\infty,\rho_1),\quad (\rho_1,\rho_2),\quad\ldots,\quad(\rho_{n-1},\rho_n),\quad(\rho_n,0)
\]
contains a zero of \(P_{n+1}^{(r)}\). Since its degree is \(n+1\), these are all its zeros, each simple. Strict interlacing follows and the induction is complete.

**4. Log-concavity.** A monic polynomial of degree \(n\) with only simple negative zeros and positive constant term has positive coefficients. Newton's inequalities for its coefficient sequence \((b_0,b_2,\ldots,b_{2n})\) give strict log-concavity of \(b_{2j}/\binom{n}{j}\) at each internal index \(1\le j<n\), hence strict log-concavity of the unnormalized Betti numbers. The empty set of internal indices when \(n\le1\) presents no exception.

## Verification

The included standalone `verify.py` implements three mathematically different exact-integer calculations: (i) the ordered-jump additive Chow decomposition (1), (ii) the Stirling-number expansion obtained from the boundary-chain generating function, and (iii) the differential recurrence (4). For each \(r\in\{2,3,4,5,7,11\}\) and \(0\le n\le8\), all three polynomial coefficient lists agree; the checker also tests palindromicity, degree, positivity, and published table entries. Execution yielded `VERIFY_OK r-values=6 n=0..8 crosschecked_pairs=54`. The *unbounded* conclusion follows from the sign/interlacing induction, not from this finite test.

## Relationship to prior work

Clader–Damiolini–Li–Ramadas, *Wonderful compactifications and rational curves with cyclic action*, Theorems 3.4 and 4.13, determine the underlying wonderful compactification and its additive Chow groups; Example 4.14 provides small Betti tables; Conjecture 4.15 asks for log-concavity for all \(r\) and \(n\). The present finding uses their exact additive decomposition to prove a stronger property—strict negative real-rootedness and consecutive strict interlacing—by means of (2)–(5). Their known \(r=2\) case recovers type-B Eulerian polynomials; the universal \(r\ge3\) conclusion is the additional content. The earlier paper *Permutohedral Complexes and Rational Curves with Cyclic Action* establishes the geometric combinatorics, not this root-location theorem. Generalized Eulerian-polynomial literature supplies related generating functions, but a stated covering implication for these Betti polynomials was not identified in the checked material.

## Limitations

This proof does not address arbitrary wonderful compactifications, equivariant cohomology, integral torsion, or any distributional limit for the roots. The exact proof depends on the published additive Chow decomposition for this particular moduli space, including the corrected ordered-jump multiplicities in the publicly available revised version of the primary paper. The finite executable checks provide reproducibility, not exhaustive certification of the infinite theorem. Literature overlap beyond the checked sources remains possible.

## References

1. E. Clader, C. Damiolini, S. Li, R. Ramadas, *Wonderful compactifications and rational curves with cyclic action*, Forum of Mathematics, Sigma **11** (2023), DOI: 10.1017/fms.2023.26; arXiv:2208.05463, first posted 2022-08-10, revised text v3 dated 2025-06-13. Relevant: Theorems 3.4, 4.13, Example 4.14, Conjecture 4.15. https://arxiv.org/html/2208.05463v3
2. E. Clader, C. Damiolini, D. Huang, S. Li, R. Ramadas, *Permutohedral Complexes and Rational Curves with Cyclic Action*, arXiv:2104.06526 (2021). Relevant: moduli and boundary-chain descriptions. https://arxiv.org/html/2104.06526v1
3. E. Clader, C. Damiolini, C. Eur, D. Huang, S. Li, *Multimatroids and rational curves with cyclic action*, arXiv:2311.09314 (2023). Related later geometry and intersection theory. https://arxiv.org/abs/2311.09314
