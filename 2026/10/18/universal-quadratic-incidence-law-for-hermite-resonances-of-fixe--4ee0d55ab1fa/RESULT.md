# Universal quadratic incidence law for Hermite resonances of fixed-width Gaussian annuli

## Finding

Fix a real width \(w>0\). For integers \(0\le m<n\), set
\[
q_j(a,w)=\frac1{j!}\int_a^{a+w}e^{-t}t^j\,dt,\qquad a\ge0.
\]
There is exactly one positive number \(a_{m,n}(w)\) with \(q_m(a_{m,n},w)=q_n(a_{m,n},w)\). This equality is transverse: the ratio \(q_n(a,w)/q_m(a,w)\) is differentiable and has strictly positive derivative for all \(a\ge0\). Put
\[
B_{m,n}=\left(\frac{n!}{m!}\right)^{1/(n-m)}.
\]
Every crossing satisfies the strict bounds
\[
 B_{m,n}-w<a_{m,n}(w)<B_{m,n}.
\]
At any fixed \(a,w\), no three distinct \(q_j(a,w)\) have the same value. Equalities can involve nonadjacent indices and thus need not occur at the largest eigenvalue.

Count pairs of Hermite indices whose crossing has occurred by inner area \(R\):
\[
N_w(R)=\#\{(m,n):0\le m<n,\ a_{m,n}(w)\le R\}.
\]
Then the limiting **pair-incidence density** exists and is independent of \(w\):
\[
\boxed{\lim_{R\to\infty}\frac{N_w(R)}{R^2}=
C:=\frac{e^2}{2}\int_0^1 t^{2t/(1-t)}\,dt
=1.1717702429648398\ldots.}
\]
The integral at \(t=0\) and \(t=1\) is taken by continuity. The count has *multiplicity by pairs*; possible coincident crossing radii for different pairs are not asserted distinct.

## Assumptions and scope

Take the unit \(L^2(\mathbb R)\) Gaussian \(g(t)=2^{1/4}e^{-\pi t^2}\), and its short-time Fourier transform
\[
V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt.
\]
For a bounded measurable \(\Omega\subset\mathbb R^2\), define the positive localization operator by
\[
\langle H_\Omega f,h\rangle
=\int_{\Omega}V_gf(x,\xi)\overline{V_gh(x,\xi)}\,dx\,d\xi.
\]
The annular symbol is
\[
\Omega_{a,w}=\{(x,\xi):a\le\pi(x^2+\xi^2)\le a+w\},\quad a\ge0,\ w>0.
\]
With standard normalized Hermite functions \(h_j\), the diagonal eigenvalues are precisely \(q_j(a,w)\); this is the radial Gaussian localization identity, available in the foundational literature. No assertion is made for nonspherical windows, variable-width annuli, or other localization windows. The primary MSC2020 classification is 42A38.

## Proof

**1. Radial diagonalization.** The normalized Gaussian Hermite spectrogram is radial and satisfies
\[
\int_{\{\pi(x^2+\xi^2)\in E\}}|V_gh_j(x,\xi)|^2\,dx\,d\xi
=\frac1{j!}\int_Ee^{-t}t^j\,dt.
\]
Angular orthogonality removes off-diagonal Hermite matrix entries; taking \(E=[a,a+w]\) yields the eigenvalue formula. Each eigenvalue is positive for \(w>0\).

**2. Exactly one transverse crossing per pair.** Fix \(0\le m<n\), write \(d=n-m\), \(h(t)=t^d\), \(f(t)=e^{-t}t^m\), and \(D(a)=\int_a^{a+w}f(t)\,dt\). The ratio is
\[
\frac{q_n(a,w)}{q_m(a,w)}
=\frac{m!}{n!}\frac{\int_a^{a+w}f(t)h(t)\,dt}{D(a)}.
\]
Its derivative has numerator
\[
 f(a+w)D(a)\bigl(h(a+w)-\overline h(a)\bigr)
 + f(a)D(a)\bigl(\overline h(a)-h(a)\bigr),
\qquad \overline h(a)=\frac{\int_a^{a+w}fh}{D(a)}.
\]
Both terms are nonnegative and the first is strictly positive, since \(h\) strictly increases and the conditional mean lies strictly between the endpoint values. Thus the derivative of the ratio is strictly positive, including its right derivative at \(a=0\).

At \(a=0\) the Poisson probabilities \(e^{-t}t^j/j!\) are integrated from zero to \(w\). The identity \(\int_0^w e^{-t}t^j/j!\,dt=\Pr\{\operatorname{Pois}(w)\ge j+1\}\) shows \(q_m(0,w)>q_n(0,w)\). As \(a\to\infty\), the ratio is at least \((m!/n!)a^d\), which tends to infinity. Hence exactly one transverse crossing exists.

At crossing, the weighted conditional mean of \(t^d\) is \(n!/m!\), and its strict location between \(a^d\) and \((a+w)^d\) proves \(a<B_{m,n}<a+w\).

**3. Maximum spectral multiplicity two.** Integration of the derivative of \(e^{-t}t^{j+1}\) gives the exact adjacent difference
\[
q_{j+1}(a,w)-q_j(a,w)
=\frac{e^{-a}a^{j+1}-e^{-(a+w)}(a+w)^{j+1}}{(j+1)!}.
\]
For \(a>0\), this is positive exactly when \(j+1<w/\log(1+w/a)\), zero at equality, and negative thereafter. For \(a=0\) all adjacent differences are negative. The sequence is strictly increasing then strictly decreasing, with at most one plateau of two consecutive entries. A horizontal value can therefore appear at at most two indices (one on either side of the peak), and no triple collision exists. Nonadjacent equal values are strictly lower than intervening values.

**4. Conductor-free universal pair count.** Let \(M(T)=\#\{(m,n):0\le m<n,\ B_{m,n}\le T\}\). The strict crossing bounds imply
\[
M(R)\le N_w(R)\le M(R+w)
\]
up to possible boundary convention (which is immaterial to the limit); indeed \(a<B<a+w\). A rigorous convenient version is \(M(R)\le N_w(R)\le M(R+w)\) exactly: if \(B\le R\), then \(a<B\le R\), while if \(a\le R\), then \(B<a+w\le R+w\).

The rising integers \(m+1,\ldots,n\) imply
\[
B_{m,n}\ge (n!)^{1/n}\ge n/e.
\]
Thus \(B\le T\) forces \(n\le eT\), ensuring finiteness and a compact scaling region. For scaled variables \(x=m/T\), \(y=n/T\), \(0<x<y\), Stirling's formula, equivalently convergence of logarithmic Riemann sums, yields
\[
\frac{B_{m,n}}T\longrightarrow
I(x,y):=\exp\left(\frac{y\log y-x\log x}{y-x}-1\right),
\]
with continuous extensions on both boundary rays. The set \(0\le x<y,\ I(x,y)\le1\) is bounded and its boundary is a curve of planar measure zero; lattice Riemann counting therefore gives \(M(T)/T^2\to\operatorname{area}\{I\le1\}\). To evaluate this area let \(x=ty\), \(0\le t<1\). Then
\[
I(ty,y)=e^{-1}y\,t^{-t/(1-t)},\qquad
0<y\le e\,t^{t/(1-t)}.
\]
The Jacobian is \(y\), so the area is
\[
\int_0^1\int_0^{e t^{t/(1-t)}}y\,dy\,dt
=\frac{e^2}{2}\int_0^1t^{2t/(1-t)}\,dt=C.
\]
Finally \(M(R)\le N_w(R)\le M(R+w)\) and fixed \(w\) prove \(N_w(R)/R^2\to C\).

## Verification

The bundled `check_annulus.py` evaluates incomplete-gamma interval probabilities in double precision, locates roots of unequal Hermite eigenvalues, checks the strict geometric-mean brackets, numerically tests transversality, and counts all pair crossings for several radii. It independently integrates the continuous limiting area. Its finite computations corroborate specified examples only; steps 1–4 above establish the infinite statements analytically. Execute `python check_annulus.py` with NumPy and SciPy installed. The checks are not a computer-assisted proof of the asymptotic.

## Relationship to prior work

Daubechies (1988) derived radial Gaussian localization operators and their Hermite/incomplete-gamma eigenvalues, including asymptotic spectral concentration. Abreu–Doerfler (arXiv:1202.5841v1, publicly dated 2012-02-27) address the inverse geometry of Hermite eigenfunctions of localization operators; their Proposition 1 concerns shape, not the pairwise annular crossing count. Knutsen (2020) explicitly studies radial localization eigenvalues and annular norms, but the inspected discussion concerns the largest eigenvalue and estimates, not the \(R^2\) incidence asymptotic for *all* ordered Hermite index pairs. Basic single-crossing behavior is consistent with standard monotone-likelihood-ratio principles; no novelty is claimed for that general principle in isolation. The claimed contribution is the complete pairwise spectral-resonance formulation with the width-independent quadratic density.

## Limitations

The result counts *pairs of indices*, not distinct resonance radii, and does not classify possible simultaneous unrelated pair crossings. The \(o(R^2)\) remainder is not made effective or uniform as \(w\) varies with \(R\). Results are restricted to Gaussian localization and fixed \(w>0\). A prior formulation in total positivity, gamma-distribution interval probabilities, or older radial Toeplitz theory may imply some parts; priority requires independent literature assessment.

## References

1. I. Daubechies, *Time-Frequency Localization Operators: A Geometric Phase Space Approach*, IEEE Transactions on Information Theory **34** (1988), 605–612. Author-hosted full text: https://sites.math.duke.edu/~ingrid/publications/ieee34-1988.pdf .
2. L. D. Abreu and M. Doerfler, *An Inverse Problem for Localization Operators*, arXiv:1202.5841v1 (2012-02-27), https://arxiv.org/abs/1202.5841 .
3. H. Knutsen, *Daubechies’ Time–Frequency Localization Operator on Cantor Type Sets I*, Journal of Fourier Analysis and Applications **26** (2020), https://doi.org/10.1007/s00041-020-09751-9 .
