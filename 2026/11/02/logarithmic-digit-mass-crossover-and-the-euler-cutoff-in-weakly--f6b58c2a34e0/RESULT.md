# Logarithmic digit-mass crossover and the Euler cutoff in weakly weighted infinite-branch maps

## Finding
Fix a real exponent \(q>1\). For \(0<c<1/\zeta(q)\), consider the explicitly separated countable affine expanding map below, with inverse-branch contraction ratios \(c n^{-q}\). Write \(d_N(c)\) for the Hausdorff dimension of the invariant survivor on the first \(N\ge2\) symbols and \(d_\infty(c)\) for the full countable-symbol survivor. Let \(J\) be the first symbolic digit under the corresponding invariant conformal probability measure.

Put \(s=c^{1/q}\) and, for each fixed \(\tau>0\), let \(N_s=\lfloor\exp(\tau/s)\rfloor\). There is exactly one real number \(z_\tau\) satisfying
\[
\int_0^\tau e^{-z_\tau u}\,du=1.
\]
As \(c\downarrow0\), the truncated and full dimensions obey
\[
\boxed{\quad d_{N_s}(c)=\frac1q+\frac{s}{q}z_\tau+o(s),\qquad d_\infty(c)=\frac1q+\frac{s}{q}+o(s).\quad}
\]
More significantly, under the *dimension-conformal equilibrium probabilities*, the logarithmic first digit \(U_s=s\log J\) converges in distribution to an explicit law:
\[
\boxed{\quad U_s\ \Longrightarrow\ e^{-z_\tau u}\mathbf1_{[0,\tau]}(u)\,du\quad\text{on the truncated survivor},\qquad U_s\ \Longrightarrow\ e^{-u}\mathbf1_{[0,\infty)}(u)\,du\quad\text{on the full survivor}.\quad}
\]
The first density is correctly normalized by the displayed root equation. In particular, it increases strictly for \(\tau<1\), is uniform on \([0,1]\) at \(\tau=1\), and decreases strictly for \(\tau>1\). The finite dimension approaches the convergence exponent \(1/q\) from below when \(\tau<1\) and from above when \(\tau>1\), whereas the full dimension always exceeds \(1/q\).

The exact first-symbol cutoff needed to cross the convergence exponent has a sharper, Euler-constant calibration. With \(H_N=\sum_{n=1}^N1/n\), let \(N_*(c)=\min\{N\ge2:sH_N>1\}\). Then
\[
\boxed{\quad d_N(c)>1/q\iff N\ge N_*(c),\qquad N_*(c)=\exp(s^{-1}-\gamma+o(1)),\quad}
\]
where \(\gamma\) is Euler's constant. Equality \(d_N(c)=1/q\) holds exactly when \(sH_N=1\). These assertions are for a fixed \(q>1\), not for the distinct limit \(q\downarrow1\).

## Assumptions and scope
Let \(H_n^{(q)}=\sum_{k=1}^n k^{-q}\) and \(P_n=H_n^{(q)}/\zeta(q)\). For each \(n\ge1\), define a closed interval and affine inverse branch of \([0,1]\) by
\[
I_n=[P_n-c n^{-q},P_n],\qquad \psi_n(x)=P_n-c n^{-q}+c n^{-q}x.
\]
The intervals are pairwise disjoint: for \(n\ge2\), the gap between \(I_{n-1}\) and \(I_n\) has length \((1/\zeta(q)-c)n^{-q}>0\). They accumulate only at the right endpoint. The forward map is \(T_c(\psi_n(x))=x\) on \(W_c=\bigcup_{n\ge1}I_n\). Every inverse derivative is the constant \(c n^{-q}<1\), so this is an exactly solvable infinite-piecewise expanding map with strong separation and bounded distortion one.

A survivor is a point whose entire forward itinerary remains in the specified collection of branches. The finite survivor uses \(\{1,\ldots,N\}\) and the full survivor uses all positive integers. The probability measure of interest is the invariant conformal Bernoulli measure on that survivor, not normalized Lebesgue measure on its ambient interval. Its symbol probabilities are given explicitly in the proof. The limits keep \(q\) and \(\tau\) fixed as \(c\downarrow0\); no uniformity as \(q\downarrow1\) or \(\tau\to0,\infty\) is claimed.

## Proof
**1. Pressure, geometric dimension, and the conformal digit law.** Write \(\ell_n=c n^{-q}\). For each finite \(N\ge2\), the strong open set condition for similarities gives the unique Moran root
\[
\sum_{n=1}^N \ell_n^{d_N}=1.
\]
This root lies in \((0,1)\), since the left-hand side is \(N>1\) at exponent zero and is at most \(c\zeta(q)<1\) at exponent one. For the infinite alphabet, the pressure sum is \(c^d\zeta(qd)\), finite exactly when \(d>1/q\); it decreases from infinity to \(c\zeta(q)<1\), hence has a unique root \(d_\infty\in(1/q,1)\). The finite roots increase to that infinite root. Indeed, the ordinary cylinder covers provide the upper bound on the countable-coded limit set, and its inclusion of every finite subsystem gives the reverse bound, so these roots equal the stated Hausdorff dimensions. At either root the weights
\[
\Pr(J=n)=\ell_n^{d_N}\quad(1\le n\le N),\qquad \Pr(J=n)=\ell_n^{d_\infty}\quad(n\ge1)
\]
sum exactly to one. Independent repetition of these weights on symbolic sequences induces the invariant conformal measure; the mass of a cylinder is the derivative to the dimension power.

**2. Uniform near-pole sum estimate.** For any bounded real \(z\), set \(d=(1+sz)/q\). Since \(c=s^q\), its finite pressure is
\[
c^d\sum_{n=1}^{N_s}n^{-qd}=s^{1+sz}\sum_{n=1}^{N_s}n^{-1-sz}.
\]
For bounded \(z\) and sufficiently small \(s\), the summand is positive and decreasing. Comparing its sum with its integral gives
\[
\left|s\sum_{n=1}^{N_s}n^{-1-sz}-\int_0^{s\log N_s}e^{-zu}\,du\right|\le s.
\]
Because \(s\log N_s\to\tau\) and \(s^{sz}=\exp(sz\log s)\to1\), the finite pressure converges uniformly for \(z\) in any compact interval to \(F_\tau(z)=\int_0^\tau e^{-zu}\,du\). This function decreases strictly from infinity to zero as \(z\) runs from minus to plus infinity. Its unique unit root \(z_\tau\) can therefore be bracketed on a fixed compact interval. Monotonicity of the exact pressure then gives \((qd_{N_s}-1)/s\to z_\tau\).

For the full pressure and a bounded positive \(z\), the classical pole of the zeta function gives \(s\zeta(1+sz)\to1/z\), uniformly on compact subsets of \((0,\infty)\). Consequently the full normalized pressure tends to \(1/z\); bracketing its unit root proves \((qd_\infty-1)/s\to1\). Neither limit depends on the placement of the branches, only on their exact ratios.

**3. Weak convergence of the conformal first digit.** Let \(z_s=(qd_{N_s}-1)/s\). By the first part, \(z_s\to z_\tau\), and the symbol weights are exactly \(s^{1+sz_s}n^{-1-sz_s}\). For any \(0\le u\le\tau\), the probability \(\Pr(s\log J\le u)\) is a partial generalized harmonic sum with upper limit \(\min\{N_s,\lfloor e^{u/s}\rfloor\}\). The same integral comparison, now uniformly for bounded \(z_s\), yields
\[
\Pr(s\log J\le u)\longrightarrow\int_0^u e^{-z_\tau v}\,dv.
\]
For \(u<0\) this probability is zero; for \(u\ge\tau\) it tends to one. The limiting CDF is continuous, giving the stated weak limit. For the full measure, the same computation with its positive scaled root tending to one gives \(\Pr(s\log J\le u)\to\int_0^u e^{-v}dv\) at every \(u\ge0\), hence the exponential law. This is a measure-level statement not furnished by the dimension roots alone.

**4. Phase boundary and the exact Euler correction.** The continuum pressure at \(z=0\) is \(F_\tau(0)=\tau\), so its decreasing root has sign negative, zero, or positive according as \(\tau<1\), \(\tau=1\), or \(\tau>1\). For a finite alphabet, the exact finite pressure evaluated at \(d=1/q\) is \(sH_N\). Its strict monotonicity in \(d\) proves the exact crossing criterion. Moreover, the minimal integer \(N_*\) crossing \(sH_N=1\) tends to infinity; minimality implies \(H_{N_*}=s^{-1}+O(1/N_*)\). Applying \(H_N=\log N+\gamma+O(1/N)\) gives \(\log N_*=s^{-1}-\gamma+o(1)\), as required. The limiting density types follow from the sign of \(z_\tau\).

## Verification
The standalone program `verify_crossover.py` evaluates pressure roots using arbitrary-precision Hurwitz-zeta differences, computes exact conformal digit probabilities, checks affine interval separation, and compares finite-parameter values against the continuum laws. With `mpmath` 1.3, `python verify_crossover.py` completed 162 sample consistency assertions. For \(q=2\), the limiting scaled roots at \(\tau=1/2,1,2\) are respectively approximately \(-2.51286241725234\), \(0\), and \(0.79681213002002\). At \(\tau=1\), the midpoint conformal mass approaches \(1/2\). The program confirms numerical consistency only; the proof is the integral comparison and exact pressure identities above.

## Relationship to prior work
Mauldin and Urbański (1996) give the general countable conformal-IFS pressure and conformal-measure framework. Those classical results, and the fixed-parameter Moran equations, are credited rather than claimed new. Cunha, Novaes, and Ponce (2026) motivate the polynomial-derivative infinite-branch setting and prove qualitative dynamical and geometric conclusions, but do not compute this simultaneous weak-contraction/exponential-alphabet conformal digit law. Das and Simmons (2022) study possible dimension spectra of infinite CIFS subsystems, not the specific joint critical digit distribution.

The separately published *Exponential-alphabet crossover for Zipf-normalized expanding maps* treats the **same similarity-ratio form** on a different singular slice, with \(q\downarrow1\), a fixed retained-length fraction, and a finite-alphabet *dimension* crossover. Its accessible complete result establishes neither the fixed-\(q\), \(c\downarrow0\) phase law nor the limit distribution of conformal symbolic digits, and expressly excludes invariant-measure convergence rates. The present result is not presented as a new general pressure formalism or as proof of priority against uninspected critical Zipf-law literature.

## Limitations
The exact results are restricted to affine, strongly separated branches with ratios \(c n^{-q}\) and fixed \(q>1\). They do not give the same critical behavior for arbitrary nonlinear branches, slowly varying multiplicative corrections, or cutoff-dependent renormalization. The weak limit concerns the logarithmic *first symbolic digit* under the conformal invariant measure; it is not weak convergence of the ambient measures on \([0,1]\). No general infinite-IFS rigidity or critical behavior for nonconformal systems is asserted. An equivalent calculation in specialized truncated-power-law literature remains a historical-priority risk.

## References
1. M. G. C. Cunha, D. D. Novaes and G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398v1, 2026-08-01. https://arxiv.org/abs/2608.00398
2. R. D. Mauldin and M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. Lond. Math. Soc. 73 (1996), 105–154, DOI:10.1112/plms/s3-73.1.105. https://www.urbanskimath.com/wp-content/uploads/2014/01/34_Urbanski.pdf
3. T. Das and D. Simmons, *On the dimension spectra of infinite conformal iterated function systems*, J. Fractal Geom. 9 (2022), 73–87. https://arxiv.org/html/1910.10259v3
4. *Exponential-alphabet crossover for Zipf-normalized expanding maps*, publicly accessible research result (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exponential-alphabet-crossover-for-zipf-normalized-expanding-map--9738a052e9b1
5. K. Boamah-Addo, T. J. Kozubowski and A. K. Panorska, *A discrete truncated Zipf distribution*, Stat. Neerl. 77 (2023), 156–187. DOI:10.1111/stan.12280. https://doi.org/10.1111/stan.12280
