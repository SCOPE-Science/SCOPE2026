# A sharp odd-prism section law and a factor-two parity transition

## Finding
For every odd integer \(n\ge5\), the maximal number of sides of a generic central plane section of a regular right \(n\)-gonal prism is \(n+2\). Its probability under a uniformly oriented central plane has the exact formula
\[
 p_n(h)=\frac{2n}{\pi}\bigl[2H_h(\delta)-H_h(\delta/2)-H_h(3\delta/2)\bigr],\qquad
 H_h(x)=\arcsin\!\left(\frac{\sin x}{\sqrt{1+h^2}}\right),\qquad \delta=\frac\pi n.
\]
The maximal-section probability is strictly positive for every positive height, has a unique maximizing aspect ratio, and obeys
\[
 p_n(h)=\frac{\pi^2h^2}{2(1+h^2)^{3/2}n^2}+O_h(n^{-4}),\qquad
 \lim_{\substack{n\to\infty\\n\text{ odd}}}n^2\sup_{h>0}p_n(h)=\frac{\pi^2}{3\sqrt3}.
\]
The unique maximizing half-height converges to \(\sqrt2\). For comparison, the previously established even-sided prism law has twice the limiting constant when both families are normalized by the squared number of base vertices.

## Assumptions and scope
The base vertices have unit circumradius and angular positions \(2\pi j/n\), for \(0\le j<n\); the top and bottom bases lie at \(z=\pm h\), with \(h>0\). The cutting plane passes through the origin and has a uniformly random unoriented normal on the unit sphere. Exclude the probability-zero set of planes passing through any vertex. All probabilities refer to this orientation model, not random plane translations. The primary result concerns every odd \(n\ge5\), without an upper bound on \(n\).

## Proof
Write a normal as \((u_x,u_y,w)\), and denote \(a_j=u_x\cos(2\pi j/n)+u_y\sin(2\pi j/n)\), \(s=h|w|\). Define \(r_+=\#\{j:a_j>s\}\), \(r_-=\#\{j:a_j<-s\}\), and \(r_0=n-r_+-r_-\). Every vertical edge contributes exactly when \(|a_j|<s\); the two horizontal base polygons each contribute either zero or two crossing edges. Because the base contains the origin in its interior, the horizontal contributions are \(2\mathbf1_{r_+>0}\) and \(2\mathbf1_{r_->0}\). Thus
\[
 N=r_0+2\mathbf1_{r_+>0}+2\mathbf1_{r_->0}\le n+2.
\]
Equality holds exactly when \(r_+=r_-=1\). This condition has positive angular measure for every \(h>0\), as shown below.

Let \(\delta=\pi/n\). Dihedral symmetry reduces the azimuthal angle of the projected normal to a uniform \(\alpha\in[0,\delta]\). Its planar length is \(\rho=\sqrt{u_x^2+u_y^2}\). The positive maximum of the \(a_j/\rho\) is \(\cos\alpha\), and its second maximum is \(\cos(2\delta-\alpha)\); the maximum and second maximum of the negatives are \(\cos(\delta-\alpha)\) and \(\cos(\delta+\alpha)\), respectively. All other values are no more extreme. Hence the condition \(r_+=r_-=1\), written in terms of \(S=h|w|/\rho\), is
\[
 \max\{\cos(2\delta-\alpha),\cos(\delta+\alpha)\}<S<\min\{\cos\alpha,\cos(\delta-\alpha)\}.
\]
The interval has positive length when \(0<\alpha<\delta\). On \(0\le\alpha\le\delta/2\) it simplifies to \(\cos(\delta+\alpha)<S<\cos(\delta-\alpha)\); the other half of the azimuthal sector is its reflection. Haar-normal sampling makes \(|w|\) uniform on \([0,1]\), independently of azimuth. Consequently \(S\) has cumulative distribution \(F_h(s)=s/\sqrt{s^2+h^2}\), for \(s\ge0\). Averaging over the sector yields
\[
 p_n(h)=\frac2\delta\int_0^{\delta/2}
 \left[\frac{\cos(\delta-\alpha)}{\sqrt{h^2+\cos^2(\delta-\alpha)}}-
 \frac{\cos(\delta+\alpha)}{\sqrt{h^2+\cos^2(\delta+\alpha)}}\right]d\alpha.
\]
Since \(H_h'(x)=\cos x/\sqrt{h^2+\cos^2x}\), integration gives exactly the stated inverse-sine formula.

For the unique optimum, set \(t=(1+h^2)^{-1/2}\in(0,1)\), \(a=\sin\delta\), \(b=\sin(\delta/2)\), and \(c=\sin(3\delta/2)\). Apart from a positive constant, the derivative of the probability with respect to \(t\) is
\[
 D(t)=\frac{2a}{\sqrt{1-a^2t^2}}-\frac b{\sqrt{1-b^2t^2}}-\frac c{\sqrt{1-c^2t^2}}.
\]
Strict concavity of sine gives \(D(0)=2a-b-c>0\), whereas strict convexity of tangent on \((0,\pi/2)\) gives \(D(1)=2\tan\delta-\tan(\delta/2)-\tan(3\delta/2)<0\). Expanding \((1-y)^{-1/2}\) in its positive-coefficient series shows that \(D(t)\) is strictly decreasing on \((0,1)\): for every odd exponent \(q\ge3\), the function \(\sin^q x\) is strictly convex on \([\delta/2,3\delta/2]\), because \(\sin^2(3\pi/10)=(3+\sqrt5)/8<2/3\le(q-1)/q\). Accordingly, \(2a^q-b^q-c^q<0\) for each coefficient beyond the constant. There is exactly one critical point, the unique global maximum.

The Taylor expansion, uniformly for \(0\le t\le1\), is
\[
 \arcsin(t\sin x)=t x+\frac{t^3-t}{6}x^3+O(x^5).
\]
Substitution into the exact formula gives, uniformly for \(t\in[0,1]\),
\[
 p_n(h)=\frac{\pi^2}{2n^2}\,t(1-t^2)+O(n^{-4}).
\]
The polynomial \(t(1-t^2)\) has its unique maximum at \(t=1/\sqrt3\), equivalent to \(h=\sqrt2\); the uniform remainder gives both the limiting optimum and the sharp constant. This concludes the proof.

## Verification
Run the standalone standard-library file `odd_regular_prism_verify.py` using `python odd_regular_prism_verify.py`. It separately enumerates crossed prism edges, verifies the count from the threshold inequalities, integrates the angular probability independently, compares with the exact inverse-sine formula for several odd orders and positive heights, and checks large-order asymptotics. The program finishes with `ALL_CHECKS_PASSED`. Finite numerical tests are corroboration; the proof above establishes the universal statements.

## Relationship to prior work
Brandenburg, De Loera and Meroni (2023) develop the general hyperplane-arrangement method for classifying slices of arbitrary polytopes, including constancy of crossed-edge sets within slicing chambers; their inspected paper does not evaluate these odd-prism Haar probabilities or optimizing aspect ratios. Earlier specific calculations cover the regular even-gon prism maximal-section law, with an exact formula and its different sharp asymptotic, and the separate equilateral triangular prism (three-sided base). The odd family with \(n\ge5\) is not implied by those results: unlike the even case, the most extreme positive and negative projected base vertices have distinct azimuthal offsets. That mismatch produces the new three-term inverse-sine expression and precisely half the even-family sharp large-order constant. Historical priority remains subject to broader scholarly confirmation.

## Limitations
Only central planes and right prisms over exactly regular odd base polygons are included. The statement concerns only the probability of attaining the maximal number of section sides, not the entire distribution of all polygon types, nor areas and perimeters of sections. Other distributions on plane orientations, affine plane offsets, and irregular bases are not covered. Independent mathematical audit has not been performed.

## References
- M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, first public April 27, 2023; Sections 1–3 (general section-arrangement framework). https://arxiv.org/abs/2304.14239
- *Sharp maximal-section probability and aspect-ratio rigidity for regular even-gon prisms*, earlier mathematical result (even-sided comparison only; publication status not asserted).
- *Exact central-section type law and aspect-ratio recovery for equilateral triangular prisms*, earlier mathematical result (three-sided comparison only; publication status not asserted).
