# Sharp Berezin cusp-width law for superattracting Hardy composition symbols

## Finding

Let \(\varphi\colon\mathbb D\to\mathbb D\) be any analytic selfmap with first nonzero Taylor coefficient of degree \(m\ge2\):
\[
\varphi(z)=a_m z^m+O(z^{m+1}),\qquad a_m\ne0.
\]
On the classical Hardy space \(H^2(\mathbb D)\), write \(C_\varphi f=f\circ\varphi\), and let \(\mathcal B_\varphi\) denote the Berezin range of \(C_\varphi\). At the real coordinate \(1-\delta\), define the *entire vertical section*
\[
I_\varphi(\delta)=\{\operatorname{Im}\zeta:\zeta\in\mathcal B_\varphi,\ \operatorname{Re}\zeta=1-\delta\}.
\]
There is \(\delta_0>0\) such that for every \(0<\delta<\delta_0\), this set is a nonempty compact interval with endpoints \(h_-(\delta)\) and \(h_+(\delta)\), satisfying
\[
\boxed{\quad h_+(\delta)=|a_m|\delta^{(m+1)/2}+O(\delta^{(m+2)/2}),\quad h_-(\delta)=-|a_m|\delta^{(m+1)/2}+O(\delta^{(m+2)/2}).\quad}
\]
The remainder constants may depend on the symbol. Equivalently, the normalized section converges in Hausdorff distance, at rate \(O(\sqrt\delta)\), to \([-|a_m|,|a_m|]\). Hence the unparameterized Berezin set recovers both the zero multiplicity and the magnitude of the first nonzero Taylor coefficient:
\[
\gamma=\lim_{\delta\downarrow0}\frac{\log(h_+(\delta)-h_-(\delta))}{\log\delta}=\frac{m+1}{2},\qquad
|a_m|=\lim_{\delta\downarrow0}\frac{h_+(\delta)-h_-(\delta)}{2\delta^\gamma}.
\]
In particular, equality of the Berezin ranges near \(1\) for two such nonlinear symbols forces the same \(m\) and the same \(|a_m|\), even if all their later Taylor coefficients are different.

## Assumptions and scope

The unit disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Hardy space is normalized by \(\|\sum_{n\ge0}c_nz^n\|_{H^2}^2=\sum_{n\ge0}|c_n|^2\). Its normalized reproducing kernels have the standard norm. For each \(w\in\mathbb D\), the Berezin transform of the composition operator is
\[
F_\varphi(w)=\frac{1-|w|^2}{1-\overline w\varphi(w)},\qquad \mathcal B_\varphi=F_\varphi(\mathbb D).
\]
No polynomial, rational, univalence, compactness, smooth-boundary, or coefficient-sign assumption is imposed on \(\varphi\). The only local condition is the displayed finite zero order \(m\ge2\) at the origin. The theorem concerns the near-\(1\) horizontal/vertical geometry of the *Berezin* range, not of the full numerical range.

## Proof

**1. All near-\(1\) points originate near the origin.** By iterating the Schwarz lemma, \(|\varphi(w)|\le |w|^m\). For \(r=|w|\in(0,1)\),
\[
|F_\varphi(w)|\le G_m(r):=\frac{1-r^2}{1-r^{m+1}}<1.
\]
Here \(G_m\) extends continuously to \(r=1\) with limit \(2/(m+1)<1\). Thus for each fixed \(\varepsilon\in(0,1)\), the supremum of \(G_m(r)\) over \(\varepsilon\le r<1\) is strictly less than one. Choose \(\delta_0\) small enough that \(\operatorname{Re}F_\varphi(w)=1-\delta\), with \(0<\delta<\delta_0\), implies \(|w|<\varepsilon\). This excludes additional radial branches or noncompact portions of the level set near the boundary of the disk.

**2. Uniform polar expansion and unique radial level.** Write \(w=re^{i\theta}\). Taylor expansion, uniform in \(\theta\), gives
\[
F_\varphi(re^{i\theta})=1-r^2+a_m r^{m+1}e^{i(m-1)\theta}+O(r^{m+2}).
\]
The polar derivatives of the remainder satisfy the corresponding differentiated estimates, uniformly in \(\theta\), by analyticity on a fixed small closed disk. Consequently, with \(\Delta(r,\theta)=1-\operatorname{Re}F_\varphi(re^{i\theta})\),
\[
\Delta(r,\theta)=r^2+O(r^{m+1}),\qquad \partial_r\Delta(r,\theta)=2r+O(r^m)>0
\]
for every \(0<r<\varepsilon\) after decreasing \(\varepsilon\). Uniform strict radial monotonicity, \(\Delta(0,\theta)=0\), and the localization just proved imply that for each sufficiently small \(\delta>0\) and each \(\theta\), exactly one radius \(r(\delta,\theta)\in(0,\varepsilon)\) solves \(\Delta=\delta\). By the implicit-function theorem these radii depend continuously on \(\theta\), and uniformly
\[
r(\delta,\theta)=\sqrt\delta\bigl(1+O(\delta^{(m-1)/2})\bigr).
\]

**3. The entire section has the claimed sharp profile.** Substituting the unique radial level into the imaginary part yields the uniform angular estimate
\[
\frac{\operatorname{Im}F_\varphi(r(\delta,\theta)e^{i\theta})}{\delta^{(m+1)/2}}
=\operatorname{Im}(a_m e^{i(m-1)\theta})+O(\sqrt\delta).
\]
Since \(m-1\ge1\), the first term ranges over the full interval \([-|a_m|,|a_m|]\). A continuous image of the circle in \(\mathbb R\) is a compact interval. The uniform estimate therefore gives its two extrema with errors \(O(\sqrt\delta)\) after normalization, and indeed gives the asserted Hausdorff-distance bound. There are no other section points by Step 1. Multiplication by \(\delta^{(m+1)/2}\) proves the endpoint formulas.

**4. Inverse determination.** The width is \(2|a_m|\delta^{(m+1)/2}(1+O(\sqrt\delta))\), with strictly positive leading coefficient. Taking logarithms gives \(\gamma\) and then dividing by \(2\delta^\gamma\) recovers \(|a_m|\). These operations use only the set \(\mathcal B_\varphi\), not a chosen kernel parameterization. This completes the proof.

## Verification

A standalone script, `verify_cusp.py`, calculates finite-delta sections for four nonmonomial analytic disk selfmaps of vanishing orders \(2,3,4,5\). It uses the exact Berezin transform, radial root finding and angular grids. Its 44 supplementary assertions passed; the proof above, not the finite grid, establishes the limits and the full continuous sections.

## Relationship to prior work

Bourdon–Le–Thompson (2026), *Berezin Ranges of Composition Operators on \(H^2\)*, Lemma 3.10 and Theorem 3.11 with Remark 3.12(i), establish radial localization and the qualitative cusp property at \(1\) for symbols fixing the origin. Their Proposition 3.7 also treats a special rational/monomial family. The present statement identifies an exact *vertical-section exponent and coefficient* for **every** analytic disk selfmap with a zero of order at least two; its inverse-recovery conclusion is not supplied by qualitative corner/cusp results. Formulas available for pure monomial symbols are relevant special-case comparisons, not the claimed novelty.

Cowen–Felder (2021/2022) study the convexity problem and examples, while Augustine–Garayev–Shankar (2023) and Augustine–Das–Bhunia–Shankar (2025) treat convexity/Berezin bounds in other symbol classes. These results do not supply the stated arbitrary-tail quantitative section law. The conclusion is a best-knowledge originality assessment, not a proof of publication priority.

## Limitations

The theorem does not recover the phase of \(a_m\), any subsequent coefficient, or the entire composition symbol. It requires finite vanishing order at the origin, \(m\ge2\), and treats sections near \(1\) only. The lower-order big-O remainder is not claimed optimal for every symbol. Some older range-geometry literature might implicitly contain equivalent local jet formulas; independent mathematical audit and a definitive priority determination have not been performed.

## References

1. P. Bourdon, T. Le and D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)*, arXiv:2610.17634v1 (first public 2026-10-13), especially §3.4.
2. C. C. Cowen and E. A. Felder, *Convexity of the Berezin Range*, arXiv:2109.12095 (2021).
3. K. Augustine, M. Garayev and S. K. Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547 (2023).
4. K. Augustine, S. Das, P. Bhunia and S. K. Shankar, *On the convexity of Berezin range and Berezin radius inequalities via a class of semi-norms*, arXiv:2507.22427 (2025).
