# Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and let \(K_t(z,w)\) be the reproducing kernel of the weighted holomorphic square-integrable space for the Euclidean boundary-distance weight \((1-|z|)^t\), \(t>-1\). Put \(s=z\overline w\). The scalar function \(K_t(s)\) has precisely the simple zeros
\[
 s_j(t)=-\tan^2\!\left(\frac{\pi j}{t+2}\right),\qquad j\in\mathbb Z,\quad 1\le j<\frac{t+2}{4}.
\]
There are no other zeros for \(|s|<1\). Thus \(K_t(z,w)\neq0\) for every \(z,w\in\mathbb D\) if and only if \(-1<t\le2\). The exact count of scalar zeros is
\[
 N(t)=\left\lceil\frac{t+2}{4}\right\rceil-1.
\]
Every new zero crosses the boundary \(|s|=1\) at \(t=4j-2\), for a positive integer \(j\), entering along the negative real axis as \(t\) increases.

## Assumptions and scope
The norm is defined using **unnormalized** planar Lebesgue area \(dA(z)=dx\,dy\):
\[
 \|f\|_t^2=\int_{\mathbb D}|f(z)|^2(1-|z|)^t\,dA(z),\qquad t>-1.
\]
The distance is genuinely Euclidean: \(\delta(z)=1-|z|\), not \(1-|z|^2\). When \(s=z\overline w\), the domain is \(|s|<1\). The phrase 'number of scalar zeros' counts distinct zeros of \(s\mapsto K_t(s)\), not zeros of an individual section \(z\mapsto K_t(z,w)\) for every fixed \(w\). Every scalar zero is realized by some \(z,w\in\mathbb D\).

## Proof
**Step 1: Complete orthogonal expansion.** Radial symmetry and angular Fourier orthogonality give
\[
 \|z^n\|_t^2=2\pi\int_0^1r^{2n+1}(1-r)^t\,dr
 =2\pi\,\mathrm B(2n+2,t+1)
 =\frac{2\pi\Gamma(2n+2)\Gamma(t+1)}{\Gamma(2n+t+3)}.
\]
All monomial norms are positive and finite for \(t>-1\). The Taylor partial sums converge in the Hilbert-space norm: angular Parseval followed by Tonelli identifies the squared norm of an analytic function with the sum of its nonnegative monomial norm contributions. Hence the monomials form a complete orthogonal basis. Therefore
\[
 K_t(s)=\sum_{n=0}^{\infty}\frac{\Gamma(2n+t+3)}{2\pi\Gamma(2n+2)\Gamma(t+1)}s^n,\qquad |s|<1.
\]

**Step 2: Closed form and analytic branches.** Set \(a=t+2>1\). For \(x^2=s\) and \(|x|<1\), the binomial series gives
\[
 (1-x)^{-a}-(1+x)^{-a}
 =2\sum_{n\ge0}\frac{(a)_{2n+1}}{(2n+1)!}x^{2n+1}.
\]
Since \((t+1)(a)_{2n+1}=\Gamma(2n+t+3)/\Gamma(t+1)\), this equals the reproducing-kernel series after division by \(4\pi x/(t+1)\). Thus
\[
 K_t(s)=\frac{t+1}{4\pi x}\big[(1-x)^{-a}-(1+x)^{-a}\big],\quad x^2=s\ne0,
\]
where the powers use the unique holomorphic logarithms on the disks \(1\pm\mathbb D\) agreeing with the real logarithm at \(1\). The expression is even in \(x\), hence independent of the square-root choice. At \(s=0\), it extends to \(K_t(0)=(t+1)(t+2)/(2\pi)>0\).

**Step 3: Exhaustive zero equation.** For \(0<|x|<1\), equality of the two powered terms is equivalent to
\[
 a\big[\operatorname{Log}(1+x)-\operatorname{Log}(1-x)\big]=2\pi i k
\]
for an integer \(k\). The Cayley quotient \(q=(1+x)/(1-x)\) has positive real part for \(|x|<1\), so its principal logarithm has imaginary part strictly between \(-\pi/2\) and \(\pi/2\). Furthermore \(\operatorname{Log}q=\operatorname{Log}(1+x)-\operatorname{Log}(1-x)\), as both sides are holomorphic in the disk, have the same derivative, and vanish at \(x=0\). Consequently \(|k|<a/4\). The index \(k=0\) gives \(x=0\), which is not a kernel zero. For any nonzero admissible index, solving \(q=\exp(2\pi i k/a)\) yields
\[
 x=i\tan\left(\frac{\pi k}{a}\right),\qquad
 s=x^2=-\tan^2\left(\frac{\pi k}{a}\right).
\]
Conversely, for every integer \(1\le k<a/4\), this \(x\) lies in \(\mathbb D\) and solves the zero equation. Indices \(k\) and \(-k\) give the two square roots of the same \(s\). The tangent is strictly increasing on \((0,\pi/4)\), so different positive indices give distinct negative real zeros and none are overlooked.

**Step 4: Simplicity, count, and boundary.** Let \(F(x)=(1-x)^{-a}-(1+x)^{-a}\). At any nonzero zero of \(F\), the two powered terms have a common nonzero value \(c\), and
\[
 F'(x)=a c\left(\frac1{1-x}+\frac1{1+x}\right)=\frac{2ac}{1-x^2}\ne0.
\]
Because \(x\ne0\) and \(s=x^2\), every scalar kernel zero is simple. Counting integers \(1\le j<a/4\) gives \(N(t)=\lceil a/4\rceil-1\). There is at least one such integer exactly when \(a>4\), or \(t>2\). At \(a=4j\) the prospective \(j\)-th root is \(s=-1\), excluded from the open disk; increasing \(a\) moves it inside. Each listed \(s\) can be realized by choosing \(z=\sqrt{|s|}\) and \(w=-\sqrt{|s|}\) real, so the scalar conclusion is equivalent to the stated bidisk conclusion.

## Verification
A standalone checker, `kernel_check.py`, independently evaluates the beta-moment kernel coefficients and the closed form at several parameters and points, then checks the predicted zeros and boundary transition numerically. It is a reproducibility and arithmetic check only: the proof's all-parameter completeness depends on the exact analytic argument above, not on the finite checks.

## Relationship to prior work
Marinescu and Xing (2026) study real-analytic dependence in the parameter for kernels with Euclidean boundary-distance weights \(\delta^t\) on smooth bounded pseudoconvex domains. That theorem concerns parameter regularity, not an exact Lu Qi-Keng transition. The present disk specialization determines all off-diagonal zeros for every real \(t>-1\). The closely related classical weight \((1-|z|^2)^t\) has a zero-free kernel proportional to \((1-z\overline w)^{-t-2}\); replacing it with genuine Euclidean distance changes the answer dramatically. Zeytuncu (2011) constructs zero-producing radial weights bounded above and below, unlike the boundary-degenerate weights here for positive exponents. Perälä (2018) proves finiteness and constructs families with arbitrarily many zeros, without the exact Euclidean-distance phase diagram being established in the inspected abstract and presentation material.

## Limitations
This is a theorem for the unit disk and **Euclidean boundary distance**, not for general smoothly bounded pseudoconvex domains or arbitrary radial weights. The zero count is for the scalar variable \(s=z\overline w\) in the unit disk. No assertion is made about the number of zeros of a fixed kernel section for all base points. The primary contemporary manuscript and the full Perälä article were not available for full-text comparison; a future full-text review may uncover prior equivalent coverage, which is not ruled out by the present literature checks.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1 (first public September 21, 2026), https://arxiv.org/abs/2609.24258.
2. A. Perälä, *Vanishing Bergman Kernels on the Disk*, Journal of Geometric Analysis 28 (2018), 1716–1727, DOI:10.1007/s12220-017-9885-1; arXiv:1703.05976v1.
3. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: \(L^p\) Regularity and Zeros*, Proceedings of the American Mathematical Society 139 (2011), 2105–2112, DOI:10.1090/S0002-9939-2010-10795-5; arXiv:1009.2806v1.
4. Mathematics Subject Classification 2020, entry 32A25, canonical kernels and integral representations, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=32A10.
