# Singularity stratification of the two-disc quartic boundary
## Finding
Let \(\mathcal S\subset\mathbb C^3\) be the quartic surface in Example 3.2 of Gesmundo–Meroni, defined by
\[
F=x_1^4-2x_1^2x_2^2+x_2^4+2x_1^2x_3^2+2x_2^2x_3^2+x_3^4-4x_3^2.
\]
Its reduced singular locus is exactly
\[
L_+=V(x_1-x_2,x_3),\qquad L_-=V(x_1+x_2,x_3).
\]
There are precisely four pinch points,
\[
(1,1,0),\quad (-1,-1,0),\quad (1,-1,0),\quad (-1,1,0).
\]
Every other point of \(L_+\cup L_-\) except the origin is an ordinary double-curve point. The origin is a third local type: two smooth branches tangent to the same plane, with completed local equation analytically equivalent to
\[
W^2-U^2V^2=0.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The statement concerns the affine quartic component \(\mathcal S\) that Gesmundo–Meroni identify as the Zariski closure of the extreme points of the two-disc Minkowski sum \(D_2+D_3\). It does not classify the four plane components of the full algebraic boundary or singularities added by projective closure at infinity.

A “pinch point” means a hypersurface germ analytically equivalent to \(V^2-SW^2=0\). An “ordinary double-curve point” means a germ analytically equivalent to \(XY=0\) times a smooth one-dimensional parameter.

## Proof
Set
\[
u=x_1+x_2,\qquad v=x_1-x_2,\qquad w=x_3.
\]
Then \(uv=x_1^2-x_2^2\) and \(u^2+v^2=2(x_1^2+x_2^2)\), hence
\[
F=(u^2+w^2)(v^2+w^2)-4w^2.
\]
Therefore
\[
F_u=2u(v^2+w^2),\qquad
F_v=2v(u^2+w^2),\qquad
F_w=2w(u^2+v^2+2w^2-4).
\]

If \(w=0\), then \(F=u^2v^2\), and the hypersurface is singular exactly when \(uv=0\). If \(w\neq0\), \(F_w=0\) gives \(u^2+v^2+2w^2=4\). When \(u,v\neq0\), the other two gradient equations force \(u^2=v^2=-w^2\), a contradiction. If \(u=0\), then \(F_v=0\) forces \(v=0\), after which \(F_w=0\) gives \(w^2=2\), but then \(F=-4\); the case \(v=0\) is symmetric. Thus the reduced singular locus is exactly \(V(u,w)\cup V(v,w)\).

At a point of \(L_+=V(v,w)\), write \(u=a+s\) and \(A=(a+s)^2+w^2\). The local equation is exactly
\[
F=A v^2+(A-4)w^2.
\]
If \(a\notin\{0,2,-2\}\), the transverse quadratic form is nondegenerate, so the parametric analytic Morse lemma gives \(XY=0\) with parameter \(s\).

If \(a=\pm2\), \(A\) is a unit and
\[
A^{-1}F=v^2-Sw^2,\qquad S=-\frac{A-4}{A}.
\]
At \(s=w=0\), \(\partial S/\partial s=\mp1\neq0\). Hence \((S,w)\) is an analytic coordinate system transverse to the line, and the germ is the pinch-point form \(v^2-Sw^2=0\). These give \((1,1,0)\) and \((-1,-1,0)\). Symmetry on \(L_-\) gives \((1,-1,0)\) and \((-1,1,0)\).

At the origin, regard \(F\) as a quadratic in \(T=w^2\):
\[
T^2+(u^2+v^2-4)T+u^2v^2.
\]
Its discriminant is
\[
\Delta=((u+v)^2-4)((u-v)^2-4),
\]
which equals \(16\) at the origin. Thus the two roots \(\alpha(u,v)\), \(\beta(u,v)\) are analytic near the origin, with \(\alpha(0,0)=0\) and \(\beta(0,0)=4\). Because \(\alpha\beta=u^2v^2\) and \(\beta\) is a unit, the germ is equivalent, after removing the unit factor \(w^2-\beta\), to
\[
w^2-\frac{u^2v^2}{\beta(u,v)}=0.
\]
Taking an analytic square root of \(\beta\) and rescaling \(w\) yields \(W^2-U^2V^2=0\). Its factors \(W-UV\) and \(W+UV\) define smooth branches with common tangent plane \(W=0\); their intersection \(W=UV=0\) is the union of the two singular lines.

## Verification
The bundled verifier `artifacts/verify_target.py` expands the coordinate identity, differentiates the quartic, certifies by exact Gröbner saturation that no singular point has \(w\neq0\), checks the transverse Hessian determinant \(4a^2(a^2-4)\), verifies the pinch-coordinate derivative at \(a=\pm2\), and factors the origin discriminant. Its terminal output is `VERIFY_OK`.

## Relationship to prior work
Gesmundo–Meroni, Example 3.2, write this quartic explicitly as one of five irreducible components of the algebraic boundary of \(D_2+D_3\), and identify it as the Zariski closure of the extreme points. Their detailed codimension-one singularity analysis later in the paper concerns a different degree-\(24\) three-disc surface. The source contains no occurrence of “pinch”. Targeted searches using the exact quartic, the two-disc Minkowski-sum description, the factorized equation, and pinch-point terminology did not locate an earlier statement equivalent to the classification above.

## Limitations
This is an affine complex-analytic classification. It does not classify the projective closure at infinity, resolve the quartic, or describe its intersections with the four plane components of the complete algebraic boundary. An older projectively equivalent quartic hidden under unrelated classical terminology remains the principal originality risk.

## References
1. F. Gesmundo and C. Meroni, “The Geometry of Discotopes,” arXiv:2111.01241, first posted 2021-11-01; Le Matematiche 77 (2022), 143–171, DOI 10.4418/2022.77.1.8. See Example 3.2, especially equation (10).
