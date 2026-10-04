# Exact refined width-Lipschitz modulus for every convex body

## Finding

Let \(K\subset\mathbb R^n\), \(n\ge2\), be any convex body. For \(u\in S^{n-1}\), let \(H_+(u)\) and \(H_-(u)\) be the supporting hyperplanes orthogonal to \(u\), oriented so that
\[
K\cap H_+(u)=\{x\in K:\langle x,u\rangle=h_K(u)\},
\qquad
K\cap H_-(u)=\{x\in K:\langle x,u\rangle=-h_K(-u)\}.
\]
Define
\[
s_K(u)=\max\{\lVert A-B\rVert:A\in K\cap H_+(u),\ B\in K\cap H_-(u)\},
\]
\[
p_K(u)=\sqrt{s_K(u)^2-w_K(u)^2},
\qquad
\widehat M_K=\max_{u\in S^{n-1}}p_K(u).
\]
With the projective spherical distance
\[
\rho(u,v)=\arccos|\langle u,v\rangle|
\]
and
\[
\Delta w_K(u,v)=\frac{|w_K(u)-w_K(v)|}{\rho(u,v)},
\]
put
\[
w'_K(u)=\limsup_{u',u''\to u}\Delta w_K(u',u'').
\]
Then
\[
\boxed{w'_K(u)=p_K(u)\quad\text{for every }u\in S^{n-1}}
\]
and consequently
\[
\boxed{\sup_{u\ne\pm v}\Delta w_K(u,v)=\widehat M_K.}
\]
Thus both inequalities in Proposition 4.4 of Mushkarov--Nikolov--Thomas are equalities for every convex body. This gives an affirmative answer to their Open Question 4.5.

## Assumptions and scope

A convex body means a compact convex subset of \(\mathbb R^n\) with nonempty interior. Its support function is
\[
h_K(u)=\max_{x\in K}\langle x,u\rangle,
\]
and its width is
\[
w_K(u)=h_K(u)+h_K(-u).
\]
The quantities \(s_K\), \(p_K\), \(\widehat M_K\), \(\rho\), \(\Delta w_K\), and \(w'_K\) are exactly the refined width quantities used in the cited primary paper.

No smoothness, strict convexity, polyhedrality, or uniqueness of support points is assumed. The result concerns the width function only; it does not settle the separate diameter-function questions in the same paper.

## Proof

The primary paper proves the upper bounds
\[
w'_K(u)\le p_K(u)
\]
for every \(u\), and
\[
\sup_{u\ne\pm v}\Delta w_K(u,v)\le\widehat M_K.
\]
It remains to prove matching lower bounds.

Fix \(u\in S^{n-1}\). By compactness of the two exposed faces, choose
\[
A\in K\cap H_+(u),
\qquad
B\in K\cap H_-(u)
\]
with
\[
\lVert A-B\rVert=s_K(u).
\]
Set
\[
D=A-B.
\]
Since \(A\) and \(B\) lie in the two supporting hyperplanes orthogonal to \(u\),
\[
\langle D,u\rangle=w_K(u).
\]
Hence the orthogonal decomposition of \(D\) is
\[
D=w_K(u)u+y,
\qquad y\perp u.
\]
Its tangential component has norm
\[
\lVert y\rVert
=
\sqrt{\lVert D\rVert^2-w_K(u)^2}
=
p_K(u).
\]

If \(p_K(u)=0\), the published inequality \(w'_K(u)\le p_K(u)\) immediately gives
\[
w'_K(u)=0=p_K(u).
\]
Assume therefore that \(p_K(u)>0\), and put
\[
\xi=\frac{y}{p_K(u)}.
\]
Then \(\xi\perp u\) and \(\lVert\xi\rVert=1\). For \(t>0\), define the unit vector
\[
v_t=\cos(t)u+\sin(t)\xi.
\]
For sufficiently small \(t\), its projective spherical distance from \(u\) is exactly
\[
\rho(u,v_t)=t.
\]

The fixed points \(A\) and \(B\) are admissible competitors in the support functions at \(v_t\) and \(-v_t\). Therefore
\[
\begin{aligned}
w_K(v_t)
&=h_K(v_t)+h_K(-v_t)\\
&\ge \langle A,v_t\rangle+\langle B,-v_t\rangle\\
&=\langle D,v_t\rangle\\
&=w_K(u)\cos t+p_K(u)\sin t.
\end{aligned}
\]
Thus
\[
\frac{w_K(v_t)-w_K(u)}{\rho(u,v_t)}
\ge
w_K(u)\frac{\cos t-1}{t}
+
p_K(u)\frac{\sin t}{t}.
\]
The right side tends to \(p_K(u)\). It is positive for all sufficiently small \(t\), so the absolute-value quotient satisfies
\[
\limsup_{t\downarrow0}\Delta w_K(u,v_t)\ge p_K(u).
\]
Consequently
\[
w'_K(u)\ge p_K(u).
\]
Together with the published upper bound this proves
\[
w'_K(u)=p_K(u)
\]
for every direction.

The primary paper proves that \(p_K\) is upper semicontinuous, so its maximum \(\widehat M_K\) is attained at some \(u_0\). If \(\widehat M_K=0\), the published global upper bound already gives equality. Otherwise the one-parameter construction above at \(u_0\) gives pairs \((u_0,v_t)\) whose width quotient tends to \(\widehat M_K\). Hence
\[
\sup_{u\ne\pm v}\Delta w_K(u,v)\ge\widehat M_K.
\]
Combining this with Proposition 4.4 yields the global equality.

## Verification

The only published premise used for the new conclusion is Proposition 4.4 of Mushkarov--Nikolov--Thomas, namely the two upper bounds. Its proof was inspected in the current open-access published version; it derives the local estimate by polytope approximation and upper semicontinuity of \(p_K\), and then obtains the global estimate on projective-spherical geodesics.

The new lower bound is self-contained and uses only the two support inequalities
\[
h_K(v_t)\ge\langle A,v_t\rangle,
\qquad
h_K(-v_t)\ge\langle B,-v_t\rangle.
\]
No differentiability theorem or regularity of \(K\) is needed.

The accompanying `verify.py` checks the witness formula on nonsmooth examples with non-singleton support faces, including a cube at a facet normal, as well as on a smooth ellipsoid. It confirms that the tangential component of a maximizing opposite-support chord has norm \(p_K(u)\) and that the stated geodesic perturbation attains the predicted first-order slope.

The replay output is:

`VERIFY_OK exact refined width modulus`

These finite checks are consistency tests only; the proof above applies to every convex body in every dimension \(n\ge2\).

## Relationship to prior work

Mushkarov, Nikolov, and Thomas introduced the refined quantities \(s_K(u)\) and \(p_K(u)\). Their Proposition 4.4 proves
\[
w'_K(u)\le p_K(u)
\]
and
\[
\sup\Delta w_K\le\widehat M_K
\]
for every convex body, and their Open Question 4.5 asks whether these inequalities are always equalities. The current 2026 published version still states that question. The same paper proves equality for polytopes and verifies it explicitly for an ellipse, but does not give the all-convex-body lower bound above.

The earlier Martini--Wenzel work proves a general Lipschitz condition for width functions, including in Minkowski spaces. It does not formulate the later direction-dependent quantity \(p_K(u)\) or the exact local identity in Open Question 4.5.

Targeted searches for the exact question, the notation \(w'_K(u)=p_K(u)\), support-face formulations, and equivalent local support-function moduli did not locate a prior all-convex-body equality.

## Limitations

This result settles the width-function equality asked in Open Question 4.5. It does not imply the analogous exact statements for the directional diameter function, whose geometry involves affine diameters rather than a support-function sum.

The originality search found no equivalent published statement, but an unindexed or differently phrased convex-analysis observation remains a residual risk because the decisive lower-bound argument is short.

## References

O. Mushkarov, N. Nikolov, P. J. Thomas, “Lipschitzness of the Width and Diameter Functions of Convex Bodies in \(\mathbb R^n\),” Journal of Convex Analysis 33 (2026), 171–181, DOI 10.68381/jca33011; preprint arXiv:2406.12537, first submitted 2024-06-18.

H. Martini, W. Wenzel, “A Lipschitz condition for the width function of convex bodies in arbitrary Minkowski spaces,” Applied Mathematics Letters 22 (2009), 142–145, DOI 10.1016/j.aml.2007.12.032; public preprint series version, Technische Universität Chemnitz, Preprint 25 (2007).
