# Fourth-root upper tails and crossover scaling of random central cylinder sections

## Finding

For a solid right circular cylinder of radius \(r>0\) and half-height \(h>0\), put \(k=h/r\). Choose a central cutting plane with Haar-uniform unoriented unit normal \(U\). Write \(Y_k=r^{-2}\operatorname{area}(K_{r,h}\cap U^\perp)\), and \(M(k)=\max Y_k\) over all directions. The established sharp maximizing-plane transition at \(k=\sqrt3\) acquires the following **new quantitative distributional law**.

Put \(\alpha=2/\sqrt3\), \(\beta=12\sqrt3/5\), and, for each fixed \(\tau\in\mathbb R\) and sufficiently small \(\varepsilon>0\), put \(k_\varepsilon=\sqrt{3-\tau\sqrt\varepsilon}\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-1/4}\Pr\{M(k_\varepsilon)-Y_{k_\varepsilon}\le\varepsilon\}=\Phi(\tau),
\]
where the positive, continuous two-sided crossover function is
\[
\Phi(\tau)=\begin{cases}
\displaystyle\sqrt{\frac{\alpha\tau+\sqrt{\alpha^2\tau^2+4\beta}}{2\beta}},&\tau\le0,\\[8pt]
\displaystyle\sqrt{\frac{5\tau}{36}+\beta^{-1/2}}-\sqrt{\max\!\left\{0,\frac{5\tau}{36}-\beta^{-1/2}\right\}},&\tau>0.
\end{cases}
\]
In particular, at the critical aspect \(k=\sqrt3\),
\[
\Pr\{M(\sqrt3)-Y_{\sqrt3}\le\varepsilon\}\sim
\left(\frac{5}{12\sqrt3}\right)^{1/4}\varepsilon^{1/4}.
\]
The fourth-root exponent, the leading constant, and the entire parameter-dependent crossover are the claim; the cylinder-section area formula and aspect-ratio maximizer threshold are acknowledged prior results.

## Assumptions and scope

The cylinder is \(K_{r,h}=\{(x,y,z)\in\mathbb R^3:x^2+y^2\le r^2,\ |z|\le h\}\). Its axis is the \(z\)-axis, its full height is \(2h\), and the cut always passes through the origin. Haar-uniform orientation means the normal is uniform on the unit sphere, identified under reversal. Consequently \(C=|U_z|\) is exactly uniform on \([0,1]\). Section area is two-dimensional Euclidean area, not orthogonal shadow area; all deficits are normalized by \(r^2\). Both \(\tau\) and the shape of the cylinder vary only as specified, and all limits hold for each fixed real \(\tau\).

## Proof

**1. Exact starting formula and known sharp transition.** Rotational symmetry reduces section area to a function of \(c=C\). Parametrizing the plane as \(z=-\sqrt{1-c^2}\,x/c\) gives the Jacobian \(1/c\). For \(0<c<(1+k^2)^{-1/2}\), define \(x_0=kc/\sqrt{1-c^2}\in(0,1)\). Integrating the disk chord widths under the axial clipping yields
\[
Y_k(c)=\frac2c\left[\arcsin x_0+x_0\sqrt{1-x_0^2}\right].
\]
For \(c\ge(1+k^2)^{-1/2}\) the section is a complete ellipse and \(Y_k(c)=\pi/c\); at \(c=0\) it is a rectangle and \(Y_k(0)=4k\). This directional law and the optimizing-plane phase threshold are included in Dirksen [1]. They are reproduced here as premises, not claimed as original.

In the truncated branch, use \(x=x_0\) as an independent coordinate, so \(c=x/\sqrt{k^2+x^2}\), and put
\[
F_k(x)=2\sqrt{k^2+x^2}\left(\frac{\arcsin x}{x}+\sqrt{1-x^2}\right),\quad 0\le x\le1.
\]
The value at zero is understood continuously. Define
\[
H(x)=\arcsin x-x\sqrt{1-x^2}=2\int_0^x\frac{t^2}{\sqrt{1-t^2}}\,dt
\]
and \(Q(x)=2x^3\sqrt{1-x^2}/H(x)\). Direct differentiation gives
\[
\operatorname{sign}F_k'(x)=\operatorname{sign}(Q(x)-k^2),\quad0<x<1.
\]
But
\[
\frac{H(x)}{x^3}=2\int_0^1\frac{s^2}{\sqrt{1-x^2s^2}}\,ds
\]
is strictly increasing, and \(\sqrt{1-x^2}\) strictly decreases. Hence \(Q\) strictly decreases from \(3\) to \(0\). The outer ellipse branch also strictly decreases as \(c\) increases. Therefore \(M(k)=4k\) for \(k\ge\sqrt3\); for \(0<k<\sqrt3\), the unique maximizer is the interior truncated-section direction \(x_*(k)>0\) solving \(Q(x_*)=k^2\). This supplies an independent derivation of the known maximizer property required below.

**2. Uniform quartic degeneracy.** Elementary Taylor expansion of the analytic truncated-section formula at \(c=0\), uniform for \(k\) in a compact neighborhood of \(\sqrt3\), gives
\[
Y_k(c)=4k+\frac{2k}{3}(3-k^2)c^2+\left(\frac{3k}{2}-k^3-\frac{k^5}{10}\right)c^4+O(c^6).
\]
At the critical aspect the quadratic term vanishes and the quartic coefficient is \(-\beta=-12\sqrt3/5\). Accordingly
\[
M(\sqrt3)-Y_{\sqrt3}(c)=\beta c^4+O(c^6).
\]
Since the maximum is unique at zero, and since \(C\) is uniform, the measure of the near-maximal directions is \(\beta^{-1/4}\varepsilon^{1/4}(1+o(1))\). This proves the critical law and its positive constant.

**3. Location and height of the emerging oblique maximum.** From the integral expression for \(Q\),
\[
Q(x)=3-\frac{12}{5}x^2+O(x^4).
\]
Writing \(\delta=3-k^2\downarrow0\), the equation for the nonzero maximizer yields
\[
x_*^2=\frac5{12}\delta+O(\delta^2),\qquad
c_*^2=\frac5{36}\delta+O(\delta^2),
\]
and evaluation of the preceding fourth-order polynomial gives
\[
M(k)-4k=\frac5{36\sqrt3}\delta^2+O(\delta^3).
\]
In particular, for \(k_\varepsilon^2=3-\tau\sqrt\varepsilon\),
\[
\frac{M(k_\varepsilon)-4k_\varepsilon}{\varepsilon}
\longrightarrow m(\tau)=\frac{\alpha^2}{4\beta}(\max\{\tau,0\})^2.
\]

**4. Joint critical-window limit.** Substitute \(c=\varepsilon^{1/4}y\), where \(y\ge0\). Step 2 gives, uniformly for \(y\) in bounded intervals,
\[
\frac{Y_{k_\varepsilon}(\varepsilon^{1/4}y)-4k_\varepsilon}{\varepsilon}
\longrightarrow \alpha\tau y^2-\beta y^4.
\]
To justify passage from pointwise convergence to probabilities, note that the strict maximizer at \(k=\sqrt3\) gives a fixed positive area gap outside every fixed neighborhood of \(c=0\). Inside a sufficiently small neighborhood, the uniform Taylor bounds give a quartic negative term dominating both the remainder and the bounded parameter-dependent quadratic term whenever \(c\ge B\varepsilon^{1/4}\), for some finite \(B\) depending only on the fixed \(\tau\). Hence every \(\varepsilon\)-near-maximizing direction lies inside \(0\le c\le B\varepsilon^{1/4}\). Its rescaled indicator converges almost everywhere to that of
\[
\left\{y\ge0:m(\tau)-\alpha\tau y^2+\beta y^4\le1\right\}.
\]
All boundary points form a finite set, so bounded convergence applies. Since \(C\) has density one, the limit of \(\varepsilon^{-1/4}\) times the probability is the length of this set.

For \(\tau\le0\), the polynomial is strictly increasing in \(y\ge0\); solve its quadratic in \(y^2\) to obtain the first branch of \(\Phi\). For \(\tau>0\), completing the square gives \(\beta(y^2-5\tau/36)^2\le1\); its nonnegative interval length is precisely the second branch. Both agree at zero and are positive. This completes the claim for every real \(\tau\).

## Verification

The accompanying self-contained `checker.py` uses only the Python standard library. It independently integrates plane-section disk chords by Simpson quadrature for 600 orientations, checks the global maximum against a 3001-point grid for six aspect ratios, tests the critical fourth-order coefficient and emerging optimizer, checks the fourth-root law, and compares both branches of the crossover for five values of \(\tau\) at two small scales. These finite tests corroborate the exact formulas; the proof of the infinite-parameter and asymptotic statements is the analytic argument above. Run `python3 checker.py` from the extracted directory.

## Relationship to prior work

Dirksen [1], especially Lemma 2.1 and Theorem 3 with its proof in Section 3.1, already provides the complete directional-section formula, recognizes rectangular/truncated-ellipse/ellipse regimes, and identifies the \(\sqrt3\) maximizer aspect after accounting for height normalization. Consequently none of these earlier statements is claimed as new. The additional statement here is the sharp **Haar near-maximal probability** including fourth-root critical behavior and a two-sided parameter-window crossover function. Those statements are not contained in the inspected sections of [1]; there is nevertheless residual historical-priority uncertainty beyond the materials inspected. Finch [2] treats mean width and surface area of related circular solids, not these near-maximal central-section probabilities.

## Limitations

The result is for **central** planar sections of filled right circular cylinders in three dimensions, sampled with Haar-uniform plane normals. It does not describe noncentral or randomly translated cuts, nonsymmetric cylinders, or higher-dimensional generalized cylinders. The crossover is pointwise in fixed \(\tau\); uniform convergence over unbounded parameter windows is not asserted. Asymptotic approximations are not exact finite-threshold formulas. Independent external mathematical validation and exhaustive historical priority analysis have not been performed.

## References

[1] H. Dirksen, *Hyperplane Sections of Cylinders*, arXiv:1602.07854v1 (publicly posted 25 February 2016), especially Lemma 2.1 and Theorem 3. https://arxiv.org/abs/1602.07854

[2] S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1 (publicly posted 24 December 2012). https://arxiv.org/abs/1212.5946
