# A sharp Fourier noncancellation and translate-cyclicity phase diagram for two-scale gamma mixtures

## Finding
Let \(m>0\) and \(0<a<b\). Set \(g_{m,c}(x)=c^m x^{m-1}e^{-cx}/\Gamma(m)\) for \(x>0\) and zero otherwise, and \(f_\lambda=\lambda g_{m,a}+(1-\lambda)g_{m,b}\) for \(0<\lambda<1\). Its Fourier transform, with the positive-exponent convention, is
\[
F_\lambda(t)=\lambda\left(\frac a{a-it}\right)^m+(1-\lambda)\left(\frac b{b-it}\right)^m,\quad t\in\mathbb R.
\]
The powers are defined using the principal logarithm in the right half-plane.

**Sharp uniform relative noncancellation.** Write \(r=b/a>1\) and
\[
\Theta_r=2\arctan\sqrt r-\frac\pi2\in(0,\pi/2),\qquad
A_c(t)=\left(\frac c{\sqrt{c^2+t^2}}\right)^m.
\]
Then the following *global* infimum over all real frequencies and positive mixing weights is exact:
\[
\boxed{\displaystyle
\inf_{t\in\mathbb R,\,0<\lambda<1}
\frac{|F_\lambda(t)|}{\lambda A_a(t)+(1-\lambda)A_b(t)}
=\cos\!\left(\frac12\min\{m\Theta_r,\pi\}\right).}
\]
For \(m\Theta_r<\pi\), the positive infimum is attained precisely at \(t=\pm\sqrt{ab}\) and \(\lambda=b^{m/2}/(a^{m/2}+b^{m/2})\). At and above the critical angle \(m\Theta_r=\pi\), zero is attained for explicitly classified weights and frequencies.

**All real zeros and exceptional weights.** For each integer \(k\ge0\) with \(\varphi_k=(2k+1)\pi/m\le\Theta_r\), put
\[
 t_{k,\pm}=\frac{(b-a)\cot\varphi_k\pm
 \sqrt{(b-a)^2\cot^2\varphi_k-4ab}}{2},\qquad
 \lambda_{k,\pm}=\frac{A_b(t_{k,\pm})}{A_a(t_{k,\pm})+A_b(t_{k,\pm})}.
\]
When \(\varphi_k=\Theta_r\), the two signs give the *same* frequency \(\sqrt{ab}\) and one weight. Every positive real Fourier zero of every \(f_\lambda\) appears in this list with the indicated weight, and every listed pair gives a zero. Different listed positive frequencies have different weights. For each exceptional weight there is exactly one simple positive zero, one simple negative conjugate zero, and no other real zeros.

**Critical rate ratio and translation cyclicity.** If \(0<m\le2\), every \(F_\lambda\) is nonvanishing on \(\mathbb R\), for all finite positive rates and weights. If \(m>2\), at least one mixture has a real Fourier zero exactly when
\[
\boxed{\displaystyle r\ge r_c(m)=\tan^2\!\left(\frac\pi4+\frac\pi{2m}\right).}
\]
At equality there is one exceptional weight and the first zero occurs at \(t=\sqrt{ab}\). In particular, \(r_c(3)=(2+\sqrt3)^2\). For a subcritical ratio approaching the critical ratio from below, the sharp relative margin satisfies
\[
\cos(m\Theta_r/2)=\frac{m}{2\sqrt{r_c(m)}(1+r_c(m))}\bigl(r_c(m)-r\bigr)
+O_m\bigl((r_c(m)-r)^2\bigr).
\]
By the Wiener translation theorem, for any fixed \(m,a,b,\lambda\), translates of \(f_\lambda\) span a dense subspace of \(L^1(\mathbb R)\) exactly when its weight is *not* one of the exceptional weights above. Thus this also gives the complete translate-cyclicity classification, including noninteger shapes.

## Assumptions and scope
All results assume a common real shape \(m>0\), **two distinct positive rates** \(a<b\), strictly positive mixing weights \(0<\lambda<1\), and real Fourier frequencies. At the equal-rate or endpoint-weight degeneracies the transform reduces to one nonvanishing gamma transform. Negative zeros mirror positive zeros because the density is real. The relative margin is not a positive **absolute** bound on \(|F_\lambda(t)|\) at large frequencies; each component transform tends to zero at infinity.

## Proof
**1. Gamma integral and monotone phase gap.** The elementary gamma integral on \(\operatorname{Re}(c-it)=c>0\) yields the stated transform. For \(t>0\), factor the components as
\[
 \Phi_c(t)=\left(\frac c{c-it}\right)^m=A_c(t)e^{im\arctan(t/c)}.
\]
The phase difference is \(m\theta(t)\), with
\[
\theta(t)=\arctan(t/a)-\arctan(t/b),\qquad
\theta'(t)=\frac{(b-a)(ab-t^2)}{(a^2+t^2)(b^2+t^2)}.
\]
Therefore \(\theta\) increases strictly from zero to its unique maximum at \(\sqrt{ab}\), then decreases strictly to zero as \(t\to\infty\). The tangent subtraction formula or direct evaluation gives \(\theta(\sqrt{ab})=\Theta_r=2\arctan\sqrt r-\pi/2\).

**2. Exact cancellation.** Two nonzero complex vectors with positive real weights sum to zero if and only if their arguments differ by an odd multiple of \(\pi\) and their weighted moduli are equal. Accordingly
\[
 F_\lambda(t)=0\ \Longleftrightarrow\
 m\theta(t)=(2k+1)\pi,\quad
 \lambda=\frac{A_b(t)}{A_a(t)+A_b(t)}
\]
for some integer \(k\ge0\), at \(t>0\). Because \(0<\theta(t)\le\Theta_r<\pi/2\), all possibilities are the finite list in the finding. The identity
\[
\tan\theta(t)=\frac{(b-a)t}{ab+t^2}
\]
converts the phase equation to \(t^2-(b-a)\cot\varphi_k\,t+ab=0\). For each admissible angle at or below the maximum, the positive solutions are exactly \(t_{k,\pm}\). When the angle equals the maximum, the quadratic has a single repeated *quadratic-equation root*, not a double zero of the Fourier transform.

**3. One positive Fourier zero per weight, with simplicity.** The modulus ratio is strictly monotone:
\[
\frac{d}{dt}\log\!\frac{A_b(t)}{A_a(t)}
=m t\left(\frac1{a^2+t^2}-\frac1{b^2+t^2}\right)>0\quad(t>0).
\]
Hence \(\lambda(t)=A_b(t)/(A_a(t)+A_b(t))\) is strictly increasing, so two distinct candidate frequencies cannot correspond to the same mixture weight. To prove simplicity, put \(w(t)=\Phi_a(t)/\Phi_b(t)\). At a zero, \(F_\lambda'(t)=\lambda\Phi_b(t)w'(t)\). The derivative of \(\log|w(t)|=\log(A_a/A_b)\) is strictly negative for every \(t>0\); therefore \(w'(t)\ne0\), proving a simple zero even at the merger of the two quadratic frequency branches. Since \(F_\lambda(0)=1\), there is no zero at the origin. Conjugation accounts for negative frequencies.

**4. Sharp normalized lower bound.** At fixed \(t\), write \(U=\lambda A_a(t)/(\lambda A_a(t)+(1-\lambda)A_b(t))\), which ranges over \((0,1)\) when \(\lambda\) does. Elementary planar geometry gives
\[
\frac{|F_\lambda(t)|^2}{(\lambda A_a(t)+(1-\lambda)A_b(t))^2}
=1-4U(1-U)\sin^2\!\bigl(m\theta(t)/2\bigr).
\]
At fixed frequency the minimum over weights is \(|\cos(m\theta(t)/2)|\), attained when \(U=1/2\). The continuous phase interval is \([0,m\Theta_r]\); if it ends below \(\pi\), the minimum is \(\cos(m\Theta_r/2)>0\), attained only where \(\theta\) is maximal, giving the asserted frequency and weight. If the interval reaches \(\pi\), a phase-antipodal pair exists and the infimum is zero. This proves sharpness and supplies actual zero-producing weights; no numerical search or compactness assumption is needed.

**5. Shape/rate threshold, boundary slope, and dense translates.** Since \(\Theta_r<\pi/2\) for finite \(r\), one cannot reach \(\pi\) for \(m\le2\). For \(m>2\), \(\Theta_r\) is strictly increasing in \(r\), and solving \(m\Theta_r=\pi\) gives the unique finite \(r_c(m)\). Its derivative is \(d\Theta_r/dr=1/(\sqrt r(1+r))\), producing the displayed first-order critical margin by Taylor's theorem. Finally, each density belongs to \(L^1(\mathbb R)\) and the classical Wiener Tauberian theorem characterizes density of its translation span exactly by the absence of real Fourier zeros. Fourier-sign convention does not change nonvanishing.

## Verification
The accompanying numerical checker `check.py`, requiring `mpmath>=1.3.0`, evaluates the principal-power Fourier formula, enumerates exceptional mixtures, checks the exact critical ratio and margin derivative, and compares direct gamma-density Fourier quadrature with the formula at three noninteger/integer parameter samples. Its captured output is `checker_output.txt`. All included finite checks pass. In particular, for shape \(m=3\), rates \(a=1\), \(b=25\), the output identifies two distinct exceptional positive-frequency weights, while at \(b=10\) none exist. Finite numerical checks are **not** an exhaustive verification of the analytical statements.

## Relationship to prior work
Evin–Merleau–Perreault (2011) study statistical modeling and model selection for two-component gamma mixtures; the published article's mixture-model and model-comparison sections were inspected. That work provides a direct natural application context, but those sections do not present the present Fourier-zero/translation-cyclicity phase diagram. The gamma-product work of Gaunt (2015) concerns products rather than convex mixtures, so its transform formulas do not imply this two-rate cancellation criterion. John's treatise on Laplace-transform zeros was inspected in its Chapter 3 gamma sections, which primarily handle gamma/Erlang combinations with a common rate, hence do not imply the two distinct-rate, common-shape characterization proved here. Gharib's earlier gamma-mixture characterization paper (1995) was located and its abstract read; its full text could not be inspected and remains a publication-priority risk. The gamma integral and Wiener's Tauberian theorem are classical ingredients and are not claimed as original.

## Limitations
The classification is specific to **two** components having the **same positive real shape**; it does not extend automatically to three or more components or differing shapes. It addresses real-frequency zeros only, not the full complex zero locus. The translate-cyclicity statement is a standard consequence of Wiener's theorem, not a new Tauberian theorem. Published-source comparisons cannot certify global novelty, particularly where plausible older full text was inaccessible. No independent mathematical audit has been performed.

## References
1. G. Evin, J. Merleau, and L. Perreault, “Two-component mixtures of normal, gamma, and Gumbel distributions for hydrological applications,” *Water Resources Research* 47 (2011), DOI: 10.1029/2010WR010266. First publicly available online August 23, 2011. https://doi.org/10.1029/2010WR010266
2. R. E. Gaunt, “Products of normal, beta and gamma random variables: Stein operators and distributional theory” (2015), arXiv:1507.07696. https://arxiv.org/abs/1507.07696
3. K. J. John, “Distributions with zeros and poles in the Laplace transform or generating function,” publicly available treatise, Chapter 3, sections 3.1–3.2. https://newmancollege.ac.in/wp-content/uploads/2019/12/Minor-Project-of-John.pdf
4. M. Gharib, “Two characterisations of a gamma mixture distribution,” *Bulletin of the Australian Mathematical Society* (1995), DOI: 10.1017/S0004972700014842. Abstract inspected; full text unavailable in this examination. https://doi.org/10.1017/S0004972700014842
5. N. Wiener, classical Tauberian theorem for the density of translates in \(L^1(\mathbb R)\).
