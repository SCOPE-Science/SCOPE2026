# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof reduces the geometric statement to a sharp point-evaluation inequality on the odd Fourier modes \(n\ge3\) of the support function after centering at the Steiner point. The required ingredients are standard and mutually consistent:

- constant width gives zeroth coefficient \(w/2\) and removes all positive even harmonics;
- Steiner centering removes the \(n=1\) harmonics;
- the support-function area formula gives
  \[
  \frac{\pi w^2}{4}-A(K)
  =\frac{\pi}{2}\sum_{n\ge3,\ n\ {\rm odd}}(n^2-1)(a_n^2+b_n^2);
  \]
- Hausdorff distance to the Steiner disk is the sup norm of the remaining support-function part;
- weighted Cauchy--Schwarz has exact evaluation constant
  \[
  \sum_{k\ge1}\frac1{(2k+1)^2-1}=\frac14.
  \]

These yield the asserted coefficient \(2\pi\).

Sharpness was checked independently from the inequality argument using the finite Fourier family
\[
q_N(\theta)=\sum_{k=1}^{N}\frac{\cos((2k+1)\theta)}{(2k+1)^2-1}.
\]
For \(t_NN<w/2\), the curvature density of \(w/2+t_Nq_N\) is strictly positive. The exact finite sum
\[
S_N=\frac{N}{4(N+1)}
\]
gives
\[
\frac{\varepsilon_N}{\rho_N^2}=2\pi\frac{N+1}{N}\to2\pi.
\]
Thus the claimed global constant is genuinely optimal, even in a smooth local class.

The nonattainment argument was also checked: formal equality in the evaluation inequality forces the infinite reproducing-kernel profile. Applying \(1+\partial_\theta^2\) produces opposite Dirac atoms, one of which is negative for every nonzero scalar multiple, contradicting nonnegativity of the curvature measure of a convex body.

## Originality

PASS, to the best of our knowledge.

The closest located prior result is Groemer (1988), Theorem 1(b): for diameter one and area at least \(\pi/4-\varepsilon\), there exists a disk within Hausdorff distance \(\frac12\sqrt{\varepsilon}\); for constant-width bodies the comparison disk may have diameter one. The present result gives the specific Steiner disk and coefficient \(1/\sqrt{2\pi}<1/2\), and proves this coefficient optimal for that canonical-center distance.

Later directly relevant literature was checked under the terms constant width, area deficit, Hausdorff distance, support function, Steiner point/disk, Fourier series, and stability. Cufí--Gallego--Reventós (2018) explicitly use the Steiner disk and Fourier support functions, but the surfaced statements concern the Hurwitz deficit and \(L^2\)-type quantities. Thäle (2025/2026) gives a current constant-width Fourier setup and the same area/Steiner-point formulas, for a different circumscribed-triangle problem. Later papers citing Groemer's 1988 stability theorem located in search concern other stability or asymmetry functionals.

No checked source states the sharp inequality
\[
\frac{\pi w^2}{4}-A(K)\ge2\pi\,d_H(K,B_S)^2
\]
or the smooth sharpness family above. Residual risk remains because the argument is an elementary sharp Sobolev/reproducing-kernel estimate on a restricted Fourier subspace, so an equivalent statement may appear in older approximation-theory or convexity literature under different terminology.

## Value

PASS.

The result strengthens a classical disk-stability estimate in three ways at once: it supplies a canonical center, improves the explicit Hausdorff coefficient, and determines the best possible constant for that canonical comparison. The extremizing sequence also explains why convexity prevents literal noncircular equality despite the sharp analytic evaluation constant.

## Scientific limitations

- Only planar Euclidean constant-width bodies are covered.
- Sharpness is for Hausdorff distance to the Steiner disk, not for the distance to the best translated disk.
- The best constant is approached rather than attained by noncircular bodies.
- Originality is to the best of our knowledge; terminology differences in older Fourier/approximation literature remain a plausible source of undiscovered equivalent coverage.

## Sources checked

- H. Groemer, *Stability Theorems for Convex Domains of Constant Width*, Canad. Math. Bull. 31 (1988), 328--337, DOI 10.4153/CMB-1988-048-3. The theorem statement and comparison constant were inspected in the paper.
- J. Cufí, E. Gallego, A. Reventós, *A note on Hurwitz's inequality*, J. Math. Anal. Appl. 458 (2018), 436--451, DOI 10.1016/j.jmaa.2017.09.017. Support-function, Steiner-point/disk, constant-width Fourier, and related deficit statements were inspected.
- C. Thäle, *A note on a problem posed by Linderholm*, J. Geom. 117 (2026), Article 1, DOI 10.1007/s00022-025-00783-4. The current support-function/Fourier formulas for constant-width bodies were inspected.
- H. Groemer, *Geometric Applications of Fourier Series and Spherical Harmonics*, Cambridge University Press, 1996, was identified as a standard reference for the Fourier framework; only bibliographic/preview material was inspected.
