# Exact phase-volume sums invalidate the showcased Lyapunov spectra of a 2023 four-dimensional Sprott-C extension
## Finding
For the Liu–Zhou–Guo four-dimensional flow \(\dot x=a(y-x),\;\dot y=cy-xz+p,\;\dot z=-bz+y^2,\;\dot p=-e(x+y)\), the divergence is the constant \(c-a-b\), so Liouville's formula gives \(\det D\phi_t=\exp((c-a-b)t)\) and every asymptotic Lyapunov spectrum, whenever defined, must sum to \(c-a-b\). At the source parameters \(a=40\), \(b=2\), \(c=22\), the required sum is \(-20\) for every \(e\), whereas the three showcased uncontrolled spectra sum to \(20.5159\), \(22.3152\), and \(24.3169\); for the controlled system, whose divergence is \(c-a-b+r_1+r_2+r_3+r_4\), the source feedback choices \(r_i=-25\) and \(r_i=-30\) require sums \(-120\) and \(-140\), but the reported controlled spectra sum to \(-62.6296\) and \(-82.0194\). Thus all five showcased exponent vectors violate an exact phase-volume identity and cannot be Lyapunov spectra of the stated differential equations; this corrects the quantitative spectra but does not, by itself, disprove the source's qualitative hyperchaos or stabilization conclusions.

## Assumptions and scope
Consider the smooth autonomous system
\[
\dot x=a(y-x),\qquad
\dot y=cy-xz+p,\qquad
\dot z=-bz+y^2,\qquad
\dot p=-e(x+y).
\]
The exact phase-volume statement holds for every real parameter choice for which the trajectory is defined on the time interval under consideration. The source-specific comparison uses \(a=40\), \(b=2\), \(c=22\), and \(e\in\{1/2,1,3\}\). For the controlled model, the added diagonal feedback terms are \(r_1x\), \(r_2y\), \(r_3z\), and \(r_4p\).

The conclusion is deliberately limited: it proves that the five quoted exponent vectors are incompatible with the printed differential equations. It does not prove that the uncontrolled system lacks a hyperchaotic invariant set, nor that the controlled system fails to stabilize the origin.

## Proof
The Jacobian of the uncontrolled vector field is
\[
J(x,y,z,p)=
\begin{pmatrix}
-a&a&0&0\\
-z&c&-x&1\\
0&2y&-b&0\\
-e&-e&0&0
\end{pmatrix}.
\]
Therefore
\[
\operatorname{tr}J=c-a-b,
\]
independently of the state and of \(e\). If \(\phi_t\) denotes the flow and \(M(t)=D\phi_t\) its variational matrix, Liouville's formula gives
\[
\frac{d}{dt}\log\det M(t)=c-a-b,
\qquad
\det M(t)=\exp((c-a-b)t).
\]
Because the product of the singular values of \(M(t)\) equals \(\det M(t)\), the sum of the four finite-time singular-value growth rates is exactly \(c-a-b\) for every \(t>0\). Consequently any four asymptotic Lyapunov exponents, whenever the individual limits exist, must sum to the same constant.

At \(a=40\), \(b=2\), and \(c=22\), this constant is \(-20\). The source reports the uncontrolled exponent vectors
\[
(16.9402,-3.4133,0,6.9890),
\]
\[
(18.2980,-4.0706,0,8.0878),
\]
and
\[
(19.5457,-4.1972,0,8.9684)
\]
for \(e=1/2\), \(e=1\), and \(e=3\), respectively. Their sums are \(20.5159\), \(22.3152\), and \(24.3169\), not \(-20\). The discrepancies are much larger than any rounding uncertainty at four decimal places.

For the controlled vector field, the diagonal feedback changes the trace to
\[
c-a-b+r_1+r_2+r_3+r_4.
\]
With the source choices \(r_1=r_2=r_3=r_4=-25\), the exact sum is \(-120\), while the reported controlled vector
\[
(-3.2103,-13.5230,-23.3526,-22.5437)
\]
sums to \(-62.6296\). With \(r_1=r_2=r_3=r_4=-30\), the exact sum is \(-140\), while the reported vector
\[
(-8.3379,-16.6337,-29.2114,-27.8364)
\]
sums to \(-82.0194\). Hence every one of the five showcased exponent vectors violates the exact determinant identity.

## Verification
The packaged `verify.py` performs the trace arithmetic and all five decimal-sum comparisons using exact decimal arithmetic and prints `VERIFY_OK`. The packaged `qr_replay.py` independently integrates the uncontrolled variational equations for \(e=1/2\), starting from \((1,1,1,1)\), with fourth-order Runge–Kutta and periodic QR orthogonalization. Over the documented finite window it returns approximately
\[
(1.0824255160,\;0.0927137433,\;-0.0209768592,\;-21.1541613287),
\]
whose sum is \(-19.9999989286\), consistent with the exact value \(-20\). This finite-time numerical replay is supportive only; the proof of the contradiction is the exact Liouville identity and does not depend on numerical convergence.

## Relationship to prior work
The introducing article prints the four-dimensional vector field, the three uncontrolled exponent vectors, and the two controlled exponent vectors used above. Targeted searches by DOI, full title, exact exponent values, the parameter tuple, and the terms “divergence”, “Liouville”, and “Lyapunov sum” found the source itself and later papers that cite it, but no located publication that states this five-case phase-volume inconsistency. Semantically closest published records concern Lyapunov-sum identities or finite-time cocycle behavior for different dynamical systems; those results do not imply the source-specific arithmetic contradiction proved here.

## Limitations
The result does not identify the unique asymptotic Lyapunov spectrum on every attractor and does not rule out multistability. The finite-time QR calculation is not an infinite-time proof and is not used to certify hyperchaos. A later erratum or unindexed correction could reduce the originality claim, although none was found in the searches performed. The exact determinant identity itself is standard; the new content assessed here is its decisive application to all five showcased numerical spectra of this specific published model.

## References
1. Y. Liu, Y. Zhou, and B. Guo, “Hopf Bifurcation, Periodic Solutions, and Control of a New 4D Hyperchaotic System,” *Mathematics* 11 (2023), 2699. DOI: 10.3390/math11122699.
2. MDPI article file-history page for the same paper, recording the original public HTML/PDF files on 14 June 2023.
