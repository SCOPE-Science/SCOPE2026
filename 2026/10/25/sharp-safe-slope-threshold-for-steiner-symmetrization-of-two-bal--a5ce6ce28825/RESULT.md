# Sharp safe-slope threshold for Steiner symmetrization of two-ball lenses

## Finding
For \(p\in\mathbb R^2\) put
\[
\mathcal H(p)=\sqrt{1+\|p\|^2}\bigl(I_2+pp^{\mathsf T}\bigr),\qquad
\rho_*=\sqrt{2+\sqrt6}.
\]
**Sharp matrix-convexity theorem.** For \(\rho\ge0\), the map \(\mathcal H\) is convex in Loewner order on the closed disk \(D_\rho=\{p:\|p\|\le\rho\}\) if and only if \(\rho\le\rho_*\). Here Loewner convexity means that, for all \(p,q\in D_\rho\) and \(0\le t\le1\),
\[
\mathcal H((1-t)p+tq)\preceq(1-t)\mathcal H(p)+t\mathcal H(q).
\]
At the threshold, the directional matrix Hessian first loses strict positivity at \(\|p\|=\rho_*\), in directions making squared radial-to-transverse component ratio \(1+\sqrt6\).

**Sharp lens consequence.** Let \(L\subset\mathbb R^3\) be the intersection of two unit Euclidean balls, and perform Steiner symmetrization along an arbitrary fixed axis. At a smooth, positive-fiber mixed branch, denote by \(p_1,p_2\in\mathbb R^2\) the horizontal gradients of the two spherical cap functions whose endpoints determine that fiber. If \(\|p_1\|,\|p_2\|\le\rho_*\), every principal curvature of the symmetral at either corresponding smooth boundary graph point is at least \(1\). The constant \(\rho_*\) is optimal in this *pointwise universal* assertion: for each \(\rho>\rho_*\), a two-unit-ball lens and a smooth mixed-fiber point exist with both cap gradients of norm less than \(\rho\) but some normal curvature of the Steiner symmetral strictly below \(1\).

## Assumptions and scope
A mixed-fiber point means that the lower and upper endpoints of the original lens's vertical interval are attained on **different** generating spheres, with strict endpoint inequalities and positive fiber length. Consequently the graph is \(C^\infty\) in a neighborhood. The same statement applies to the reflected lower graph. Principal curvatures are taken positive for convex surfaces. The result is restricted to intersections of **two equal-radius unit balls in dimension three**; it does not assert curvature preservation at nonsmooth branch interfaces or for arbitrary intersections of more balls. The gradient bound is pointwise for the two active spherical caps, not a bound on the positions of the sphere centers.

## Proof
**1. Exact cap Hessian and curvature criterion.** For a unit sphere centered at horizontal \(a\in\mathbb R^2\), the upper cap \(f(x)=\sqrt{1-\|x-a\|^2}\), with \(\|x-a\|<1\), has gradient \(p=-(x-a)/f(x)\). Elementary differentiation gives
\[
-D^2f=\sqrt{1+\|p\|^2}\,(I_2+pp^{\mathsf T})=\mathcal H(p).
\]
On a mixed fiber the upper symmetral graph is \(h=(f_1+f_2)/2+C\), where \(C\) is constant. Put \(p=(p_1+p_2)/2\). Then \(\nabla h=p\), and \(-D^2h=[\mathcal H(p_1)+\mathcal H(p_2)]/2\). For an upper graph \(z=h(x)\), the metric and positive second fundamental form satisfy
\[
\mathrm I(v,v)=\|v\|^2+(p\cdot v)^2,\qquad
\mathrm{II}(v,v)=\frac{-D^2h[v,v]}{\sqrt{1+\|p\|^2}}.
\]
It follows that all its normal curvatures are at least \(1\) precisely when
\[
\tfrac12\bigl(\mathcal H(p_1)+\mathcal H(p_2)\bigr)-\mathcal H(p)\succeq0.\tag{1}
\]

**2. Exact sharp matrix Hessian test.** Rotational covariance allows us to compute at \(p=(\sqrt R,0)\), \(R=\|p\|^2\ge0\). For a direction \(d=(a,b)\), set \(M=\sqrt{1+R}\,D^2\mathcal H(p)[d,d]\). Direct differentiation yields
\[
M=\begin{pmatrix}
3(1+2R)a^2+(1+R)b^2&2(1+2R)ab\\
2(1+2R)ab&a^2/(1+R)+(3+2R)b^2
\end{pmatrix}.
\]
Both diagonal entries are positive for \(d\ne0\), so positive semidefiniteness is equivalent to nonnegative determinant. Its exact factorization is
\[
(1+R)\det M=A(R)a^4+B(R)a^2b^2+C(R)b^4,
\]
with
\[
A(R)=3(1+2R),\quad
B(R)=-4R^3+4R^2+14R+6,\quad
C(R)=2R^3+7R^2+8R+3.
\]
The discriminant of the quadratic in \(a^2/b^2\) equals
\[
B(R)^2-4A(R)C(R)=16R^2(1+R)^2(R^2-4R-2).\tag{2}
\]
For \(0\le R\le R_*=2+\sqrt6\), this is nonpositive, while \(A(R)>0\) and \(C(R)>0\); thus \(\det M\ge0\), including when \(b=0\) by direct inspection. At \(R=R_*\), equality occurs when \(a^2/b^2=-B/(2A)=1+\sqrt6\). For \(R>R_*\), the discriminant is positive and \(B(R)<0\), while \(A,C>0\); hence its two roots in \(a^2/b^2\) are positive and between them \(\det M<0\). This produces a negative eigenvalue of the matrix Hessian. Since a twice continuously differentiable symmetric-matrix-valued function is Loewner convex on a convex region exactly when all second directional derivatives are positive semidefinite there, these observations establish the sharp disk radius \(\rho_*=\sqrt{R_*}\).

**3. Positive part of the lens statement.** If \(p_1,p_2\in D_{\rho_*}\), the whole line segment between them remains in this disk. Loewner convexity gives inequality (1), hence every normal curvature and both principal curvatures are at least \(1\) at the graph point. Reflect the graph across the horizontal plane to obtain the identical lower-bound statement below.

**4. Every larger radius admits a genuine mixed-fiber counterexample.** Fix \(\rho>\rho_*\) and choose \(p\) with \(\rho_*<\|p\|<\rho\). Step 2 supplies \(d\) and a vector \(v\ne0\) for which \(v^{\mathsf T}D^2\mathcal H(p)[d,d]v<0\). For sufficiently small \(\varepsilon>0\), both \(p_1=p+\varepsilon d\) and \(p_2=p-\varepsilon d\) have norm less than \(\rho\) and the symmetric midpoint deficit satisfies
\[
v^{\mathsf T}\left(\tfrac12\bigl(\mathcal H(p_1)+\mathcal H(p_2)\bigr)-\mathcal H(p)\right)v
=\tfrac{\varepsilon^2}{2}v^{\mathsf T}D^2\mathcal H(p)[d,d]v+O(\varepsilon^4)<0.\tag{3}
\]
To realize these gradients, define \(s_i=(1+\|p_i\|^2)^{-1/2}\), \(q_i=-s_i p_i\), \(a=(q_2-q_1)/2\), \(x=(q_1+q_2)/2\), and \(c=(s_1+s_2)/4\). Consider the two unit spheres centered at \((a,c)\) and \((-a,-c)\). At horizontal coordinate \(x\), their spherical heights are exactly \(s_1,s_2\), and their cap gradients are exactly \(p_1,p_2\), because \(x-a=q_1\) and \(x+a=q_2\). For \(\varepsilon\) small, \(s_1\) and \(s_2\) are close; hence
\[
|s_1-s_2|<2c=\tfrac12(s_1+s_2)<s_1+s_2.\tag{4}
\]
The inequalities are strict, so the lower active endpoint is \(c-s_1\) from the first sphere, the upper active endpoint is \(-c+s_2\) from the second, and the fiber has positive length \((s_1+s_2)/2\). Thus this is an open smooth mixed branch of a genuine three-dimensional lens. Inequality (3), combined with the curvature criterion (1), proves that some normal curvature of its Steiner symmetral is less than \(1\). This works with gradients arbitrarily close to the threshold from above, proving sharpness.

**5. An explicit negative certificate.** For \(p_1=(13/4,1/4)\), \(p_2=(11/4,-1/4)\) and \(v=(1,-2)\), direct substitution gives
\[
 v^{\mathsf T}\left(\tfrac12\bigl(\mathcal H(p_1)+\mathcal H(p_2)\bigr)-\mathcal H(3,0)\right)v
 =\frac{201\sqrt{186}+249\sqrt{138}}{128}-14\sqrt{10}<0.
\]
For an exact rational sign check, use the strict elementary brackets \(\sqrt{186}<13.638182\), \(\sqrt{138}<11.747341\), \(\sqrt{10}>3.162277\). They imply an upper bound of \(-437893/128000000<0\). The same construction in step 4 produces explicit ball centers from these data and satisfies (4).

## Verification
Run `python3 verify.py` with Python 3 and SymPy installed. It recomputes the complete matrix second derivative, the polynomial determinant and discriminant, the threshold root, the exact negative example, and the strict lens-fiber inequalities. The symbolic equalities in steps 1–4 provide the proof; finite computational tests are supplemental, not substitutes for the quantified analytic argument. The exact sign of the example uses certified rational square bounds, not floating-point sign inference.

## Relationship to prior work
Artstein-Avidan and Florentin, *Symmetrizations of Ball-Bodies*, arXiv:2602.14090v1 (2026-02-15), Section 4.2, prove that Steiner symmetrization can decrease sectional curvature below one for a lens of two unit balls. Section 4.3 demonstrates that the loss can be arbitrarily large and realizes prescribed supporting gradients. Those results establish failure of **unrestricted** curvature preservation. The present result instead determines the exact universal *bounded-slope safe region*, its algebraic boundary, and arbitrarily close counterexamples immediately beyond that boundary; neither a qualitative counterexample nor arbitrary large losses gives that threshold. The indexed finding *Rank-one curvature loss under Steiner symmetrization of a two-ball lens* gives the maximum number of deficient principal directions and an identity on transverse directions, but does not bound the gradients required for **zero** deficient directions. Classical Steiner symmetrization preserves ordinary convexity; a principal-curvature lower bound is a different, stricter requirement.

## Limitations
The sharp bound controls cap-gradient magnitudes on the active mixed-fiber branch, not an entire lens, all of its nonsmooth seams, or arbitrary ball-bodies. The result gives no universal quantitative curvature gap when the gradient bound is violated, only an existence result arbitrarily close above the exact threshold. Curvature here is classical at smooth points; generalized nonsmooth curvature is not addressed. Published indexing and text searches cannot exclude every older equivalent matrix-convexity calculation. Independent external mathematical audit has not been performed.

## References
1. S. Artstein-Avidan and D. I. Florentin, *Symmetrizations of Ball-Bodies*, arXiv:2602.14090v1 (first public 2026-02-15), Section 4, https://arxiv.org/html/2602.14090 .
2. S. Artstein-Avidan and D. I. Florentin, *An in-depth study of ball-bodies*, arXiv:2505.09200 (2025), https://arxiv.org/abs/2505.09200 .
3. *Rank-one curvature loss under Steiner symmetrization of a two-ball lens*, mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rank-one-curvature-loss-under-steiner-symmetrization-of-a-two-ba--10f17b0b28f3 .
