# Exact first Hopf threshold and recurrence half-space in a variable-index chaotic flow

## Finding

For the Yan–Jie–Zhang flow \(\dot x=-ax+yz\), \(\dot y=ax-xz\), \(\dot z=-az+x^2+a\) with \(a>0\), the real equilibria and first local bifurcations are exact: \(E_0=(0,0,1)\) is asymptotically stable for \(0<a<1\), has a zero eigenvalue at \(a=1\), and is a real saddle for every \(a>1\); the symmetry-related equilibria \(E_\pm=(\pm\sqrt{a(a-1)},\pm\sqrt{a(a-1)},a)\) exist exactly for \(a\ge1\), are asymptotically stable for \(1<a<3/2\), and undergo simultaneous supercritical Hopf bifurcations at \(a=3/2\). At the Hopf point the spectrum is \(\{-3,\pm i\sqrt3/2\}\), the crossing speed is \(d\operatorname{Re}\lambda/da=6/13\), and, in the standard Kuznetsov normalization, the first Lyapunov coefficient is \(l_1=-2\sqrt3/3<0\), so a stable small periodic orbit is born from each \(E_\pm\) for \(a>3/2\) sufficiently close to \(3/2\). For all \(a>3/2\), \(E_\pm\) have one negative real eigenvalue and a complex conjugate pair with positive real part. Moreover every bounded complete trajectory satisfies the exact memory law \(z(t)-1=\int_0^\infty e^{-as}x(t-s)^2\,ds\); hence every non-equilibrium bounded complete trajectory lies strictly in \(z>1\). In particular, at the source paper's \(a=3\), \(E_0\) has three real eigenvalues and is a saddle, not a saddle-focus.

## Assumptions and scope

Consider the smooth three-dimensional ODE
\[
\\dot x=-ax+yz,\\qquad \\dot y=ax-xz,\\qquad \\dot z=-az+x^2+a,
\]
with real parameter \\(a>0\\). The local statements below concern the real equilibria of this exact vector field. The global memory statement concerns bounded complete trajectories, meaning solutions defined and bounded for all real time. No assertion is made that the local periodic orbits persist all the way to the source paper's numerically studied range \\(a\\ge3\\).

## Proof

The equilibrium equations give \\(x(a-z)=0\\). If \\(x=0\\), the remaining equations force \\(y=0\\) and \\(z=1\\), giving \\(E_0\\). If \\(z=a\\), then the first equation gives \\(y=x\\) and the third gives \\(x^2=a(a-1)\\). Thus the additional real equilibria exist exactly for \\(a\\ge1\\) and are \\(E_\\pm\\).

At \\(E_0\\), the characteristic polynomial factors as
\[
p_0(\\lambda)=(\\lambda+a)(\\lambda^2+a\\lambda+1-a).
\]
For \\(0<a<1\\), both coefficients of the quadratic are positive, so all three eigenvalues have negative real part. At \\(a=1\\) one eigenvalue is zero. For \\(a>1\\), the quadratic has negative constant term and positive discriminant \\(a^2+4a-4\\), so it has one positive and one negative real root. Consequently \\(E_0\\) is a real saddle for every \\(a>1\\). In particular, at \\(a=3\\),
\[
p_0(\\lambda)=(\\lambda+3)(\\lambda^2+3\\lambda-2),
\]
so all three eigenvalues are real.

At either \\(E_+\\) or \\(E_-\\), the characteristic polynomial is
\[
p_\\pm(\\lambda)=\\lambda^3+2a\\lambda^2+a(2-a)\\lambda+2a^2(a-1).
\]
For \\(a>1\\), its Routh array has first column
\[
1,\\qquad 2a,\\qquad a(3-2a),\\qquad 2a^2(a-1).
\]
Hence \\(E_\\pm\\) are asymptotically stable for \\(1<a<3/2\\), while exactly two roots lie in the open right half-plane for \\(a>3/2\\). At \\(a=3/2\\),
\[
p_\\pm(\\lambda)=(\\lambda+3)(\\lambda^2+3/4),
\]
so the critical pair is \\(\\lambda=\\pm i\\sqrt3/2\\). Implicit differentiation of \\(p_\\pm(\\lambda,a)=0\\) gives the exact crossing speed
\[
\\left.\\frac{d}{da}\\operatorname{{Re}}\\lambda(a)\\right|_{a=3/2}=\\frac6{{13}}>0.
\]

To determine criticality, translate either equilibrium to the origin at \\(a=3/2\\). The quadratic part is represented by the symmetric bilinear map
\[
B(u,v)=\\bigl(u_2v_3+u_3v_2,-u_1v_3-u_3v_1,2u_1v_1\\bigr).
\]
Using right and adjoint eigenvectors normalized by \\(\\langle p,q\\rangle=1\\), the standard Kuznetsov Hopf formula with no cubic tensor gives
\[
l_1=\\frac{1}{2\\omega}\\operatorname{{Re}}\\left\\langle p,-2B\\bigl(q,A^{-1}B(q,\\bar q)\\bigr)+B\\bigl(\\bar q,(2i\\omega I-A)^{-1}B(q,q)\\bigr)\\right\\rangle=-\\frac{2\\sqrt3}{3}.
\]
Thus the crossing is nondegenerate and supercritical. Since the vector field is equivariant under \\((x,y,z)\\mapsto(-x,-y,z)\\), the two equilibria undergo simultaneous symmetry-related Hopf bifurcations, each producing a stable small periodic orbit for \\(a>3/2\\) sufficiently close to the threshold.

Finally, setting \\(w=z-1\\) yields the exact scalar equation
\[
\\dot w+aw=x^2.
\]
For a bounded complete trajectory, variation of constants from time \\(t-T\\) to \\(t\\) gives
\[
w(t)=e^{-aT}w(t-T)+\\int_0^T e^{-as}x(t-s)^2\\,ds.
\]
Boundedness and \\(a>0\\) allow \\(T\\to\\infty\\), proving
\[
z(t)-1=\\int_0^\\infty e^{-as}x(t-s)^2\\,ds\\ge0.
\]
If equality holds at one time, continuity forces \\(x\\) to vanish on the entire past half-line; the ODE then forces \\(y=0\\) and \\(z=1\\), and uniqueness gives the equilibrium trajectory. Therefore every non-equilibrium bounded complete trajectory satisfies \\(z(t)>1\\) for every \\(t\\).

For completeness, the cubic discriminant at \\(E_\\pm\\) is
\[
-4a^3(a-1)(59a^2-55a-8),
\]
which is negative for every \\(a>3/2\\). Thus the two unstable roots there are indeed a complex conjugate pair, while the third root is negative.

## Verification

The packaged script `artifacts/verify_hopf.py` symbolically verifies the equilibrium substitutions, both characteristic polynomials, the Hopf factorization, the exact crossing speed, the cubic discriminant, the first Lyapunov coefficient, and the scalar filter identity. Its recorded output ends in `VERIFY_OK`. The stability classification then follows from the displayed Routh array and elementary sign arguments; the supercritical Hopf conclusion uses the standard nondegenerate Hopf theorem.

## Relationship to prior work

Yan, Jie, and Zhang introduced this vector field in 2022, listed the same three formal equilibrium expressions, classified the equilibria at \\(a=3\\), and numerically explored \\(a\\in[3,15]\\). Their text explicitly says that \\(E_0\\) has one positive and two negative real characteristic roots at \\(a=3\\), but nevertheless calls it a saddle-focus. The article does not state the lower-parameter stability intervals, the \\(a=3/2\\) Hopf threshold, its criticality, or the bounded-complete-trajectory memory law. Targeted searches by exact equations, title, parameter threshold, Hopf terminology, and implication structure found no publication stating this theorem for the same vector field. Semantic comparison against published-results records found only analogous bifurcation or recurrence theorems for different systems.

## Limitations

The Hopf conclusion is local: it proves stable periodic orbits only for \\(a>3/2\\) sufficiently close to \\(3/2\\), not their continuation to the chaotic regimes reported for \\(a\\ge3\\). The memory law applies to bounded complete trajectories; it does not prove that every forward solution is bounded. The originality search was targeted but cannot exclude an unindexed equivalent result or one written after a non-obvious change of coordinates.

## References

1. M. Yan, J. Jie, P. Zhang, “Chaotic systems with variable indexs for image encryption application,” *Scientific Reports* 12, 19585 (2022), DOI 10.1038/s41598-022-24142-4. Published 15 November 2022.
2. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, standard first-Lyapunov-coefficient convention for Hopf bifurcation.
