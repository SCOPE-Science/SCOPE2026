# Sharp Korenblum radius for every radial entire-function \(L^2\) norm

## Finding

**Theorem (universal radial sharp radius).** Let \(W:[0,\infty)\to[0,\infty)\) be measurable, not zero almost everywhere, and suppose every moment
\[
0<m_j=\int_0^\infty t^jW(t)\,dt<\infty\qquad(j=0,1,2,\ldots)
\]
is finite. Let \(F_W^2\) consist of all entire functions for which
\[
\|f\|_W^2=\frac1\pi\int_{\mathbb C}|f(z)|^2W(|z|^2)\,dA(z)<\infty.
\]
Set \(R_W=\sqrt{m_1/m_0}\). For every pair \(f,g\in F_W^2\), exterior domination
\[
|f(z)|\le |g(z)|\qquad\text{whenever }|z|>R_W
\]
implies \(\|f\|_W\le\|g\|_W\). The radius is optimal: no larger radius is admissible. Consequently
\[
\boxed{\mathcal K_W=\sqrt{m_1/m_0}\quad\text{for every nonzero radial weight with finite moments}.}
\]

In particular, for \(W(t)=t^\beta e^{-\alpha t}\), \(\alpha>0\), **every** \(\beta>-1\) is allowed and
\[
\mathcal K_W=\sqrt{(\beta+1)/\alpha}.
\]
For \(W(t)=\mathbf1_{[1-d,1+d]}(t)\), \(0<d<1\), the sharp radius is \(1\). These include the previously unresolved weights specifically singled out in Question 7.4 of the cited 2026 work.

## Assumptions and scope

Here \(dA\) is ordinary, unnormalized planar Lebesgue area and the factor \(1/\pi\) is part of the norm. The exterior hypothesis holds at **all** complex points of modulus greater than \(R_W\), regardless of the support of \(W\). Functions \(f,g\) are entire, not merely holomorphic on a bounded support disk. An admissible radius is one at which exterior domination forces the displayed norm inequality for every such pair. It is not assumed that \(W\) is decreasing, continuous, or strictly positive.

The moment positivity is automatic from a nonzero nonnegative measurable weight: a positive-measure subset lies in \(t>0\). For an entire \(f(z)=\sum_{j\ge0}a_jz^j\), radial orthogonality and Tonelli yield
\[
\|f\|_W^2=\sum_{j=0}^\infty m_j|a_j|^2.
\]
Let \(\mathcal H_W\) denote the Hilbert completion of polynomials with this coefficient norm; this avoids any completeness issue when \(W\) has compact support. Every function of \(F_W^2\) belongs to \(\mathcal H_W\).

## Proof

**1. The moment-weighted backward shift is a contraction at the asserted scale.** The moments are log-convex by Cauchy–Schwarz:
\[
m_j^2\le m_{j-1}m_{j+1}\qquad(j\ge1).
\]
Thus \(m_j/m_{j-1}\) is nondecreasing, whence
\[
\frac{m_{j-1}}{m_j}\le\frac{m_0}{m_1}=R_W^{-2}\qquad(j\ge1).
\]
The coefficient backward shift \(B(\sum_{j\ge0}a_jz^j)=\sum_{j\ge0}a_{j+1}z^j\) therefore extends from polynomials to \(\mathcal H_W\) with
\[
\|R_WBf\|_W^2
=R_W^2\sum_{j\ge1}m_{j-1}|a_j|^2
\le\sum_{j\ge1}m_j|a_j|^2\le\|f\|_W^2.
\]
Write \(T=R_WB\). It is a Hilbert-space contraction.

**2. Exterior domination yields a rational Schur function.** If \(g\equiv0\), domination and analyticity force \(f\equiv0\). Otherwise \(h=f/g\) is meromorphic on \(\mathbb C\). At every point \(|z|>R_W\), a zero of \(g\) is also a zero of \(f\) to at least the same order (by the inequality on a punctured neighborhood), so any such quotient singularity is removable and \(|h|\le1\) there. Boundedness near infinity makes \(\infty\) a removable singularity. At every point \(|z|=R_W\), a nonremovable pole would force \(|h|\) unbounded on approach from \(|z|>R_W\), also impossible. All genuine poles of \(h\) therefore lie strictly inside the compact disk \(|z|<R_W\); there are finitely many because \(g\) is entire and not identically zero. Hence \(h\) is meromorphic on the Riemann sphere, and therefore rational.

Write the rational function in reduced form \(h(z)=p(z)/q(z)\) with polynomials \(p,q\), \(d=\deg q\), \(\deg p\le d\), and every zero of \(q\) strictly inside \(|z|<R_W\). Define reversed polynomials
\[
P(w)=w^dp(R_W/w),\qquad Q(w)=w^dq(R_W/w).
\]
Then \(H(w)=P(w)/Q(w)=h(R_W/w)\) extends analytically to a neighborhood of the closed unit disk; \(Q\) has no zeros there, and \(|H(w)|\le1\) on \(|w|\le1\), including \(w=0\) by continuity.

**3. Exact quotient realization through the backward shift.** From \(q(z)f(z)=p(z)g(z)\) and the formal coefficient identity
\[
B^d(z^k u)=B^{d-k}u\qquad(0\le k\le d),
\]
which holds for every analytic \(u\), we obtain, without assuming polynomial multiples lie in \(\mathcal H_W\),
\[
Q(T)f=P(T)g.
\]
Indeed, if \(q(z)=\sum_{k=0}^dq_kz^k\), then \(Q(T)=R_W^d\sum_{k=0}^dq_kB^{d-k}\), and the analogous identity holds for \(P\); equality follows coefficient-by-coefficient. All terms on the last displayed equation are bounded operators on \(\mathcal H_W\).

Since \(Q\) has no zeros in the closed unit disk and \(T\) is a contraction, \(Q(T)\) is invertible. Thus \(f=H(T)g\). The standard von Neumann inequality, applied to the rational function \(H\) analytic on a neighborhood of the closed unit disk, gives
\[
\|H(T)\|\le\sup_{|w|\le1}|H(w)|\le1.
\]
Therefore \(\|f\|_W\le\|g\|_W\). This holds even when the Hilbert completion contains non-entire elements, because only its contraction property and the embedding of the two given entire functions are used.

**4. Sharpness.** Let \(S>R_W\) and choose a real \(c\) with \(R_W<c<S\). Put \(f(z)\equiv c\) and \(g(z)=z\). They belong to \(F_W^2\) by the moment hypothesis and satisfy \(|f(z)|\le|g(z)|\) whenever \(|z|>S\), yet
\[
\|f\|_W^2=c^2m_0>m_1=\|g\|_W^2.
\]
Hence \(S\) is not admissible. The theorem follows.

**5. Explicit families.** For \(t^\beta e^{-\alpha t}\), integration gives \(m_j=\Gamma(j+\beta+1)/\alpha^{j+\beta+1}\), hence \(m_1/m_0=(\beta+1)/\alpha\). For the uniform narrow-ring weight \(\mathbf1_{[1-d,1+d]}\), \(m_0=2d\) and \(m_1=2d\), giving \(R_W=1\) for every \(0<d<1\), including the small-\(d\) weights that defeat the source's sufficient moment-measure condition.

## Verification

The proof is analytic and uses only log-convexity of moments, the rationality of meromorphic functions on the sphere, polynomial coefficient identities, and the classical von Neumann inequality for a Hilbert-space contraction. The last ingredient applies to rational functions analytic in a neighborhood of the closed unit disk; here every denominator zero maps strictly outside that disk.

The optional standalone `CHECK.py` executes exact-rational checks of log-convexity, backward-shift bounds, reversed-polynomial operator identities, strict test-pair domination for a nonmonotone two-exponential radial weight, sharpness, and a narrow-ring example. The script's finite checks illustrate rather than establish the all-weights theorem. Execute it with `python3 CHECK.py` using only Python's standard library.

## Relationship to prior work

Frank Wikström's *The sharp radius in Korenblum's maximum principle for the Fock space* (arXiv:2609.39622v1, 30 September 2026), Theorems 1.1 and 1.3, established the Gaussian case and all nonincreasing radial weights. Corollary 1.4 proved the same sharp-radius formula for \(t^\beta e^{-\alpha t}\) only for \(-1<\beta\le5.4475\ldots\). Sections 7.1 and 7.3 distinguish the limitations of the source's moment-measure criterion from the original norm inequality. In particular, Propositions 7.2 and 7.3 give ring and large-Gamma weights for which that criterion fails, and Question 7.4 asks whether the sharp formula survives. The theorem here settles those questions affirmatively **for the stated entire-function/exterior domination problem**, using contractive functional calculus rather than the moment-measure criterion.

Wee and Le established upper bounds and discussed weighted Fock variants in 2022/2023; the sharpness test above agrees with those bounds. Efraimidis, Llinares and Vukotić treated domination for weighted **disk Bergman spaces** under annular domination, a different hypothesis and not a result that implies the exterior entire-function theorem.

## Limitations

No assertion is made for \(L^p\) Fock norms with \(p\ne2\), nonradial weights, functions merely holomorphic on a bounded disk, or domination only on a bounded annulus. For compactly supported radial weights, exterior domination is required **also outside the weight's support**. The proof supplies no classification of all equality pairs; a separate previous classification for nonincreasing weights is not extended here. Equivalence with an unindexed older formulation cannot be ruled out by searches alone. Independent mathematical validation has not been performed.

## References

1. Frank Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1 (first posted 30 September 2026), Theorems 1.1–1.3, Corollary 1.4, Propositions 7.1–7.3, and Question 7.4. https://arxiv.org/html/2609.39622v1
2. JunJie Wee and Le Hai Khoi, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385–1406. DOI: 10.1080/17476933.2022.2052862.
3. Iason Efraimidis, Adrián Llinares and Dragan Vukotić, *Korenblum's Principle for Bergman Spaces with Radial Weights*, Computational Methods and Function Theory 25 (2025), 239–250. DOI: 10.1007/s40315-024-00543-6.
4. J. von Neumann, *Eine Spektraltheorie für allgemeine Operatoren eines unitären Raumes*, Mathematische Nachrichten 4 (1951), 258–281 (the contraction inequality).
