# A cubic Schatten resonance for weighted Bergman monomial Toeplitz commutators

## Finding

Let \(\alpha>-1\), and let \(p,q,r,s\) be nonnegative integers. On the weighted analytic Bergman Hilbert space \(A^2_\alpha(\mathbb D)\), let \(T_{p,q}=P_\alpha M_{z^p\bar z^q}\vert_{A^2_\alpha}\), and define \(K=[T_{p,q},T_{r,s}]=T_{p,q}T_{r,s}-T_{r,s}T_{p,q}\). Set \(\Delta=qr-ps\). Exactly one of the following cases occurs.

**Generic case.** If \(\Delta\ne0\), then \(K\) has infinite rank, and its singular values in decreasing order satisfy
\[
\lim_{j\to\infty}j^2s_j(K)=(\alpha+1)|\Delta|>0.
\]
Consequently, \(K\in\mathcal S_t\) if and only if \(t>1/2\).

**Cubic-resonant case.** Suppose \(\Delta=0\) and neither ordered pair of exponents is \((0,0)\). Write uniquely \((p,q)=u(a,b)\) and \((r,s)=v(a,b)\), where \(u,v\) are positive integers and \(a,b\) are coprime nonnegative integers, not both zero. If \(a,b>0\), \(a\ne b\), and \(u\ne v\), then \(K\) has infinite rank and
\[
\lim_{j\to\infty}j^3s_j(K)=(\alpha+1)abuv|a-b|\,|u-v|>0.
\]
Consequently, \(K\in\mathcal S_t\) if and only if \(t>1/3\).

**Zero case.** In every remaining case, \(K=0\). In particular, for polynomial monomial symbols there is no nonzero finite-rank commutator. The zero/finite-rank classification is recorded for completeness, not claimed as a new discovery.

In either nonzero case, let \(d\) be the corresponding exponent \(2\) or \(3\), and let \(L\) be its positive singular-value coefficient displayed above. Then the critical logarithmic residue is exact:
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^{N}s_j(K)^{1/d}=L^{1/d}.
\]
Thus \(|K|^{1/d}\) lies in the weak trace class, is not trace class, and every normalized Dixmier trace of it equals \(L^{1/d}\). The ordinary best rank-\((j-1)\) operator-norm approximation error is \(s_j(K)\), so the two decay laws give sharp approximation rates. For fixed noncommuting exponents, the leading singular coefficient varies *exactly linearly* with \(\alpha+1\), allowing this weight parameter to be reconstructed from the asymptotic spectrum.

## Assumptions and scope

Use the probability measure \((\alpha+1)(1-|z|^2)^\alpha\,dA(z)\), where \(dA\) is normalized disk area. Let \(P_\alpha\) be orthogonal projection onto the closed subspace of holomorphic square-integrable functions. All Toeplitz symbols \(z^p\bar z^q\) are bounded on the disk. Singular values include multiplicity and are ordered decreasingly. The Schatten index \(t\) may be any positive real number, including quasi-Banach indices below one. The result is for exactly two monomial Toeplitz operators on the disk, not arbitrary polynomial sums or higher-dimensional domains. No assertion is made for the singular Hardy-limit parameter \(\alpha=-1\).

## Proof

**Step 1: exact monomial action.** Define the moments and normalized basis by
\[
\mu_n=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},\qquad e_n(z)=\frac{z^n}{\sqrt{\mu_n}},\qquad n\ge0.
\]
Angular orthogonality shows that \(T_{p,q}e_n=0\) if \(n+p-q<0\), and otherwise
\[
T_{p,q}e_n=\frac{\mu_{n+p}}{\sqrt{\mu_n\mu_{n+p-q}}}e_{n+p-q}.
\]
Put \(k=p-q\), \(\ell=r-s\), \(m=k+\ell\), and \(R_h(n)=\mu_{n+h}/\mu_n\) whenever \(n,n+h\ge0\). For all sufficiently large \(n\), the commutator is a single-step weighted shift
\[
Ke_n=c_ne_{n+m},\qquad
c_n=\frac{R_r(n)R_p(n+\ell)-R_p(n)R_r(n+k)}{\sqrt{R_m(n)}}.
\]
For the finitely many initial indices, the same single-diagonal property holds, with coefficients obtained from the action formula and with zero when the target degree is negative. Hence \(K^*K\) is diagonal in \((e_n)\), and the nonzero singular values are precisely the absolute values of the nonzero coefficients \(c_n\), in decreasing order.

**Step 2: universal asymptotic coefficients.** Write \(A=\alpha+1>0\). For every fixed nonnegative integer \(h\), the exact ratio formula and its expansion are
\[
R_h(n)=\prod_{i=1}^{h}\frac{n+i}{n+i+A}
=1-\frac{Ah}{n}+\frac{A(A+1)h(h+1)}{2n^2}+O(n^{-3}).
\]
For the numerator \(D_n=R_r(n)R_p(n+\ell)-R_p(n)R_r(n+k)\), Taylor expansion of the fixed shifts yields
\[
D_n=\frac{A(qr-ps)}{n^2}+\frac{E}{n^3}+O(n^{-4}),
\]
where
\[
E=A\big[(A+1)(-\ell p(p+1)+k r(r+1))-\ell^2p+k^2r+Apr(k-\ell)\big].
\]
Here \(\sqrt{R_m(n)}=1+O(n^{-1})\), also when \(m<0\). Thus the first displayed singular coefficient is \(A|qr-ps|\). If \(qr=ps\) and both exponent pairs are nonzero, primitivity of \((a,b)\) gives the integer factorization \((p,q)=u(a,b)\), \((r,s)=v(a,b)\), and direct substitution reduces the cubic numerator coefficient to
\[
E=-Aabuv(a-b)(u-v).
\]
The stated strict conditions are exactly those making this coefficient nonzero. They exhaust the infinite-rank zero-bracket possibilities.

**Step 3: complete degeneracy classification.** If one exponent pair is zero, one Toeplitz operator is the identity. If \(a=0\), both symbols are coanalytic monomials, and the two operators commute. If \(b=0\), both are analytic monomials, and they commute. If \(a=b\), both are radial symbols, so their Toeplitz operators are diagonal and commute. If \(u=v\), the two operators are identical. These are all cases in which the quadratic and cubic coefficients vanish; no hidden finite-rank remainder survives.

**Step 4: singular-value ordering and ideals.** If \(c_n=Cn^{-d}+O(n^{-d-1})\) with \(C\ne0\), its absolute values have counting function \(\#\{n:|c_n|>x\}\sim(|C|/x)^{1/d}\) as \(x\downarrow0\). A finite number of initial coefficients does not change this. Therefore \(s_j(K)\sim|C|j^{-d}\). Summation of \(s_j(K)^t\) gives the sharp Schatten threshold. At the boundary \(t=1/d\), the summands equal \(|C|^{1/d}j^{-1}+o(j^{-1})\), yielding the logarithmic mean limit. Measurability for normalized Dixmier traces follows from that ordinary logarithmic Cesàro limit, not from finite numerical experiments.

## Verification

The standalone file `checker.py` executes exact rational identities for the moment ratios, symbolic verification of the quadratic and cubic coefficients, rational asymptotic checks for several positive rational values of \(\alpha+1\), and independent finite weighted-Bergman matrix checks using Gamma-function moments. It reports 1,247 passed assertions on the tested cases. The infinite asymptotics and all parameter quantifiers follow from the explicit proof above, not the finite tests.

To replay: from the same package, run `python checker.py` with Python 3, SymPy, and NumPy installed. The script has no network dependency.

## Relationship to prior work

Čučković and Louhichi's published 2008 article studies finite-rank commutators and semicommutators of quasihomogeneous Bergman Toeplitz operators. Their finite-rank and Mellin-transform framework includes this monomial setting; no novelty is claimed for the familiar monomial action or the zero-versus-finite-rank classification. Dong and Zhou's 2014 public preprint (2016 version) gives a broader finite-rank analysis and explicitly classifies monomial commutators on the analytic Bergman space in Section 6, Corollary 6.5. The novel target here is instead the *quantitative infinite-rank spectrum*: the universal quadratic coefficient, the nontrivial cubic resonance, its sharp weak-Schatten threshold, and the weighted family of critical residues. These statements are not identified in the inspected corresponding sections of those primary sources. Known symbol-calculus methods may give qualitative compactness or first-order behavior, and this work does not claim their discovery.

## Limitations

The exact zero/finite-rank part is already covered by the cited finite-rank literature; it is included only to make the spectral trichotomy exhaustive. The asymptotic claims concern fixed integer exponents and fixed \(\alpha>-1\); no uniform joint large-exponent or Hardy-limit estimate is asserted. The literature comparison is limited to inspected sources and publicly indexed searches; equivalent historical asymptotic formulae could remain under other terminology. No independent mathematical or bibliographic audit has been completed.

## References

1. Ž. Čučković and I. Louhichi, *Finite Rank Commutators and Semicommutators of Quasihomogeneous Toeplitz Operators*, Complex Analysis and Operator Theory **2** (2008), 429–439; published online 14 January 2008; DOI: 10.1007/s11785-007-0044-8. Author-hosted published text: https://faculty.kfupm.edu.sa/MATH/issam/Publications/Cuckovic_me_final.pdf.
2. X.-T. Dong and Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213 (first public posting 2 November 2014; revised February 2016), Section 6 and Corollary 6.5; https://arxiv.org/abs/1411.0213.
3. C. Jiang, X.-T. Dong and Z.-H. Zhou, *Commuting and Semi-commuting Monomial-type Toeplitz Operators on Some Weakly Pseudoconvex Domains*, Canadian Mathematical Bulletin **62** (2019), 327–340, DOI: 10.4153/CMB-2018-026-1. Related higher-dimensional finite-rank classification, not the singular-value asymptotics claimed here.
