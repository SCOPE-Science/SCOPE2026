# Fourier classification and exact policy dimensions for Lebesgue-preserving feedback between coprime expanding maps

## Finding
Let \(m,n\ge2\) be coprime integers. On the circle \(\mathbb T=\mathbb R/\mathbb Z\), from position \(x\) apply \(T_m(x)=mx\pmod1\) with probability \(p(x)\), or \(T_n(x)=nx\pmod1\) with probability \(1-p(x)\), where \(p:\mathbb T\to[0,1]\) is measurable. The following statements give a complete Fourier classification of the feedback policies preserving Lebesgue probability \(\lambda\), an exact polynomial design-space dimension, and uniqueness within absolutely continuous stationary laws under strictly interior feedback.

**Fourier characterization.** Lebesgue probability is stationary exactly when \(\widehat p(mk)=\widehat p(nk)\) for all nonzero integers \(k\). Every positive frequency has a unique representation \(r m^a n^b\) with \(a,b\ge0\), \(m\nmid r\), and \(n\nmid r\). Stationarity is thus equivalent to requiring
\[
\widehat p(rm^a n^{\ell-a})=c_{r,\ell}\quad (0\le a\le\ell)
\]
for each such \(r\) and \(\ell\ge0\); negative coefficients are conjugates. Here the complete freedom of the measurable policy consists of the constant coefficient and these level coefficients, subject exactly to real-valuedness, \(0\le p\le1\) almost everywhere, and Fourier square summability
\[
|\widehat p(0)|^2+2\sum_{\substack{r\ge1\\m\nmid r,\ n\nmid r}}\sum_{\ell\ge0}(\ell+1)|c_{r,\ell}|^2<\infty.
\]

**Exact finite-degree dimension.** The real vector space of trigonometric polynomials of degree at most \(N\) satisfying the stationarity equation has dimension
\[
1+2\sum_{\substack{1\le r\le N\\m\nmid r,\ n\nmid r}}
\left(1+\left\lfloor\log_{\max(m,n)}\frac Nr\right\rfloor\right).
\]
In particular the admissible probability-valued polynomial policies occupy a full-dimensional convex body in this vector space, with \(p\equiv 1/2\) an interior point relative to that space.

**Absolutely continuous uniqueness.** If \(0<p(x)<1\) for Lebesgue-almost every \(x\), then \(\lambda\) is the unique absolutely continuous stationary probability. This does not assert uniqueness among singular stationary probabilities: the common fixed point \(0\) supports a stationary Dirac mass.

For instance, for \((m,n)=(2,3)\),
\[
p(x)=\frac12+\varepsilon\bigl(\cos(4\pi x)+\cos(6\pi x)\bigr),
\qquad 0<|\varepsilon|<\frac14,
\]
is a nonconstant, strictly interior, Lebesgue-preserving feedback policy satisfying \(P_2p=P_3p=\tfrac12+\varepsilon\cos(2\pi x)\). Its Lebesgue stationary probability is the unique absolutely continuous one.

## Assumptions and scope
Throughout, \(m,n\in\mathbb Z\), \(m,n\ge2\), \(\gcd(m,n)=1\), and \(p\) is measurable with values in \([0,1]\) almost everywhere. Fourier coefficients are normalized as \(\widehat f(k)=\int_0^1 f(x)e^{-2\pi ikx}\,dx\). Probability-valued policies belong to \(L^\infty(\mathbb T)\subset L^2(\mathbb T)\). The Markov operator on integrable densities is \(Lf=P_m(pf)+P_n((1-p)f)\), with \(P_b f(x)=b^{-1}\sum_{j=0}^{b-1}f((x+j)/b)\).

## Proof
**1. Exact density equation.** Each \(P_b\) preserves the integral and sends the constant one to one. Consequently \(L1=P_mp+P_n(1-p)=1+P_mp-P_np\). For every integer \(k\), a direct change of variables gives \(\widehat{P_b f}(k)=\widehat f(bk)\). Thus \(L1=1\) if and only if \(\widehat p(mk)=\widehat p(nk)\) for all \(k\). The equation for \(k=0\) holds automatically.

**2. Arithmetic Fourier classes.** Because \(m,n\) are coprime, dividing a positive integer by \(m\) and \(n\) as long as possible gives a unique \(r m^a n^b\) with neither \(m\) nor \(n\) dividing \(r\). Uniqueness follows from comparing the maximal powers of \(m\) and \(n\), which cannot interfere because the two bases are coprime. The relation at \(k=rm^a n^b\) equates the coefficients at \(rm^{a+1}n^b\) and \(rm^a n^{b+1}\). At a fixed level \(\ell=a+b+1\), these equations join consecutive entries in the chain of all \(\ell+1\) frequencies, so all coefficients in that level agree. Conversely this constant-on-level property implies every Fourier relation. Parseval supplies the stated weighted square-summability and Fourier-series uniqueness; the additional almost-everywhere constraint \(0\le p\le1\) is necessary and sufficient for a feedback probability.

**3. Degree-cutoff exactness.** At a given \((r,\ell)\), all \(\ell+1\) coefficients are equal. A nonzero level can fit into a degree-\(N\) trigonometric polynomial if and only if its largest frequency \(r\max(m,n)^\ell\) is at most \(N\). Consequently precisely \(1+\lfloor\log_{\max(m,n)}(N/r)\rfloor\) levels survive for each \(r\le N\) not divisible by either base. Every surviving level contributes two real degrees of freedom (real and imaginary parts of the positive-frequency coefficient), and the constant term contributes one. This proves the dimension. Any sufficiently small real linear combination of these level harmonics added to \(1/2\) remains strictly between zero and one, proving the relative-interior and full-dimension assertion.

**4. Uniqueness among absolutely continuous stationary laws.** Suppose \(0<p<1\) almost everywhere, \(L1=1\), and \(f\ge0\) is a stationary \(L^1\) density of integral one. For \(\phi(t)=\sqrt{1+t^2}\), which is strictly convex on \([0,\infty)\) and obeys \(\phi(f)\in L^1\), Jensen's inequality with the Markov kernel in \(L\) gives \(\phi(Lf)\le L\phi(f)\) almost everywhere. Their integrals coincide because \(Lf=f\) and \(L\) preserves integrals. Equality must therefore hold almost everywhere. Strict convexity and positivity of all inverse-branch weights imply \(f(y)=f(T_my)\) for almost all \(y\). The integer expanding circle map \(T_m\) is ergodic for Lebesgue measure: for an invariant \(L^2\) function, its Fourier coefficients at \(k\ne0\) equal those at \(m^jk\) and tend to zero; truncation extends ergodicity to invariant \(L^1\) functions. Hence \(f\) is constant, and normalization gives \(f=1\). Finally \(\delta_0\) is stationary, so unrestricted uniqueness would be false.

**5. Explicit nonconstant witness.** \(P_2\cos(4\pi x)=\cos(2\pi x)\), \(P_3\cos(6\pi x)=\cos(2\pi x)\), and the two cross terms vanish. This gives the displayed identity and probability bounds.

## Verification
The independent, reproducible exact-arithmetic script `checker.py` (part of this package) checks uniqueness and completeness of finite frequency classes, verifies the dimension identity for all coprime bases from \(2\) through \(8\) and cutoffs \(1\) through \(89\), and checks the explicit feedback's Fourier identity using rational coefficients. These finite tests support the formulas but do not prove the infinite-level theorem or exclude unsearched literature; those conclusions are from the proof above.

## Relationship to prior work
Suzuki (2023) studies absolutely continuous invariant measures of random beta-transformations with a prescribed random environment, including independent choices. Alshekhi, Ding, and Rhee (2024) investigate numerical approximation of stationary densities for random maps with position-dependent probabilities. Bahsoun, Bose, and Quas (2008) give a deterministic representation of such random maps. The present result addresses the distinct **inverse-policy** question: which measurable position-dependent probabilities make the known Lebesgue density exactly stationary when the two integer slopes are coprime? It yields a complete spectral classification, an exact finite-degree dimension, and a strictly-interior uniqueness result rather than numerical approximation. The full 2024 numerical-paper text was not accessible during comparison, so priority against its detailed results remains a residual risk.

## Limitations
The Fourier classification assumes coprime integer slopes. The square-summability condition alone does not enforce positivity; the \([0,1]\) constraint is essential. The absolutely continuous uniqueness conclusion needs \(0<p<1\) almost everywhere and does not exclude singular stationary measures. The finite exact-arithmetic checks are not infinite proof, and independent mathematical audit and exhaustive literature-priority verification have not been performed.

## References
- Shintaro Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521, first posted 2023-03-30; https://arxiv.org/abs/2303.17521 .
- Azzah Alshekhi, Jiu Ding, Noah Rhee, *A Quadratic Spline Projection Method For Computing Stationary Densities of Random Maps*, Communications in Mathematical Sciences 22 (2024), https://doi.org/10.4310/CMS.2024.v22.n2.a9 .
- Wael Bahsoun, Christopher Bose, Anthony Quas, *Deterministic representation for position dependent random maps*, 2008, bibliographic record https://arxiv.org/search/?query=Deterministic+representation+for+position+dependent+random+maps&searchtype=all .
