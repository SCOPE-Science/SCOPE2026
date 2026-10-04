# Sharp cubic-harmonic curvature bound and the exact positive Wigner radius

## Finding
Let \(q\) be any real spherical harmonic of degree \(3\) on \(S^{n-1}\), \(n\ge2\), and define the support-curvature operator
\[
Q_q=\nabla^2_{S^{n-1}}q+q\,\mathrm{Id}.
\]
Then the dimension-free estimate
\[
\max_{u\in S^{n-1}}\|Q_q(u)\|_{\mathrm{op}}\le 8\|q\|_\infty
\]
is sharp. Applied to the cubic harmonic
\[
q_+(u)=(u_1^2-u_2^2)u_3-2u_1u_2u_4
\]
from arXiv:2608.11068v1, it gives the exact value
\[
M_+=\max_{S^3}\|Q_{q_+}\|_{\mathrm{op}}=\frac{16}{3\sqrt3}.
\]
Therefore, for every \(r>0\), the function \(h_\varepsilon=r+\varepsilon q_+\) is a support function of a convex body of constant width \(2r\) if and only if
\[
|\varepsilon|\le \frac{3\sqrt3}{16}r,
\]
and it is the support function of a \(C^2_+\) body if and only if the inequality is strict.

At the sharp endpoint \(|\varepsilon|=3\sqrt3\,r/16\), the source's quadratic and quartic Wigner quantities become
\[
\mathcal A_2=\frac{9\pi^2r^2}{1024},\qquad
V(h_{\mathrm{odd}}^{[4]})=\frac{729\pi^2r^4}{458752}.
\]

## Assumptions and scope
A real degree-three spherical harmonic means the restriction to \(S^{n-1}\) of a real homogeneous harmonic cubic on \(\mathbb R^n\). The operator norm is taken on the tangent space. The convexity conclusion for \(q_+\) concerns exactly the one-parameter support-function family displayed above; it does not determine the full convexity region of the two-dimensional harmonic plane considered later in the source.

The endpoint statement is about ordinary convexity, not positive curvature. At equality the support function is smooth, but its curvature operator has a zero eigenvalue somewhere, so the body is not of class \(C^2_+\).

## Proof
Fix \(u\in S^{n-1}\) and a unit tangent vector \(v\perp u\). Along the great circle
\[
\gamma(t)=u\cos t+v\sin t,
\]
put \(p(t)=q(\gamma(t))\). Since \(q\) is the restriction of a homogeneous cubic, \(p\) has only first and third Fourier frequencies:
\[
p(t)=A\cos 3t+B\sin 3t+C\cos t+D\sin t.
\]
The geodesic Hessian identity gives
\[
\langle Q_q(u)v,v\rangle=p''(0)+p(0)=-8A.
\]
Let \(R=\sqrt{A^2+B^2}\). After translating \(t\), the third-frequency part is \(R\cos 3t\). At the six points \(t_k=k\pi/3\), the alternating average kills both first-frequency terms and recovers \(R\):
\[
R=\frac16\sum_{k=0}^5(-1)^k p(t_k).
\]
Hence \(R\le\|p\|_\infty\le\|q\|_\infty\), so
\[
|\langle Q_q(u)v,v\rangle|\le8\|q\|_\infty.
\]
Taking the maximum over unit tangent \(v\) proves the operator-norm estimate. Sharpness in every dimension follows from the harmonic cubic \(q(u)=\operatorname{Re}(u_1+i u_2)^3\): at \(u=e_1\), \(v=e_2\), its great-circle restriction is \(\cos3t\), so \(|\langle Q_qv,v\rangle|=8=8\|q\|_\infty\).

For the source's \(q_+\), write \(a^2=u_1^2+u_2^2\) and \(b^2=u_3^2+u_4^2\). Then \(a^2+b^2=1\) and
\[
|q_+(u)|\le a^2b=(1-b^2)b\le\frac{2}{3\sqrt3},
\]
with equality at \(b=1/\sqrt3\). Thus \(M_+\le16/(3\sqrt3)\). Equality is witnessed by
\[
u=\left(\sqrt{\frac23},0,-\frac1{\sqrt3},0\right),\qquad
v=\left(0,\sqrt{\frac23},0,-\frac1{\sqrt3}\right).
\]
These are orthonormal, and direct substitution on their great circle gives
\[
q_+(u\cos t+v\sin t)=-\frac{2}{3\sqrt3}\cos3t.
\]
Therefore \(\langle Q_{q_+}(u)v,v\rangle=16/(3\sqrt3)\), proving the exact value of \(M_+\).

For \(h_\varepsilon=r+\varepsilon q_+\),
\[
Q_{h_\varepsilon}=r\,\mathrm{Id}+\varepsilon Q_{q_+}.
\]
Since \(q_+\) is odd, the spectrum of \(Q_{q_+}\) occurs with both signs at antipodal normals. Hence \(Q_{h_\varepsilon}\) is positive definite everywhere exactly for \(|\varepsilon|<r/M_+\), is positive semidefinite and singular at equality, and has a negative direction beyond equality. The equality case is a support function because it is the uniform limit of support functions from the strict range. Oddness also gives \(h_\varepsilon(u)+h_\varepsilon(-u)=2r\), so every admissible member has constant width \(2r\).

Finally, the source computes \(E(q_+)=\pi^2/12\) and \(V(q_+^{[4]})=\pi^2/7\). Substituting \(\varepsilon^2=27r^2/256\) and \(\varepsilon^4=729r^4/65536\) gives the displayed endpoint invariants.

## Verification
The proof is analytic and covers every dimension \(n\ge2\), every degree-three spherical harmonic, and the full real parameter range of the \(q_+\) deformation. The six-point identity is exact; it is not a sampling argument. The equality witness is an exact great circle on \(S^3\).

The accompanying `verify.py` checks the rational parts of the endpoint arithmetic and the squared sharp-constant identities. It is supplementary: no finite computation is used to prove the universal bound or the continuum convexity classification.

## Relationship to prior work
In Lemma 9.1 of arXiv:2608.11068v1, Zwierzyński introduces \(q_-\) and \(q_+\), computes their quadratic and quartic Wigner invariants, and defines
\[
M_\pm=\max_{S^3}\|Q_{q_\pm}\|_{\mathrm{op}}.
\]
The paper then uses the sufficient condition \(|\varepsilon|<r/M_\pm\) to obtain small constant-width perturbations, but it leaves \(M_\pm\) symbolic. The present result supplies a sharp dimension-free curvature inequality for every cubic spherical harmonic and evaluates the previously symbolic positive-example constant exactly as \(M_+=16/(3\sqrt3)\), thereby turning the source's local smallness statement for \(q_+\) into a complete one-parameter convexity interval.

Searches for the source identifier, the exact constant, the curvature operator \(\nabla^2q+q\,\mathrm{Id}\), great-circle Fourier formulations, and broader spherical-harmonic Bernstein bounds did not locate a statement that implies this sharp \(L^\infty\)-to-curvature estimate or this exact \(q_+\) threshold. General Bernstein--Markov literature found in the comparison search concerns different norms or derivative functionals.

## Limitations
The general inequality is specific to degree three. The argument uses the fact that a cubic restricted to a great circle contains only frequencies one and three; it does not provide the sharp analogue for higher degrees. For the source's two-parameter plane \(\alpha q_-+\beta q_+\), only the \(q_+\) axis is optimized here. No claim is made that the sharp endpoint body is extremal for the source's global quadratic--quartic feasible region.

## References
1. M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068v1, especially Section 2.1, Lemma 9.1, equations (9.21)--(9.24), and Theorem 9.3.
2. C. Müller, *Spherical Harmonics*, Lecture Notes in Mathematics 17, Springer, 1966; cited by the lead source for standard spherical-harmonic background.
