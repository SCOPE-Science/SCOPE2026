# Exact John–Löwner ellipsoids of Euclidean spherical orthants and a dimension-six contact transition

## Finding
For each integer \(d\ge3\), write \(f_i\) for the standard basis, \(e=d^{-1/2}\sum_i f_i\), and let \(K_d=\{x\in\mathbb R^d:x_i\ge0\text{ for all }i,\ \|x\|_2\le1\}\). Define the ellipsoid \(E(\lambda;s,t)=\{x:(e\cdot x-\lambda)^2/s+(\|x\|_2^2-(e\cdot x)^2)/t\le1\}\). Its center is \(\lambda e\); \(s>0\) is the squared axial semiaxis and \(t>0\) the repeated squared transverse semiaxis.

The **unique John ellipsoid** is
\[
J_d=E\left(\frac d{d+1};\frac1{(d+1)^2},\frac1{d+1}\right).
\]
The **unique Löwner ellipsoid** is
\[
L_d=\begin{cases}
E\left(\frac12;\frac14,\frac{\sqrt d+1}4\right),&3\le d\le5,\\[3pt]
E\left(\frac{\sqrt d+1}{d+1};\frac{d(\sqrt d-1)^2}{(d+1)^2},\frac d{d+1}\right),&d\ge6.
\end{cases}
\]
The full John contact locus is \(\{e\}\cup\{(\sum_j f_j-f_i)/\sqrt d:1\le i\le d\}\). The full Löwner contact locus is \(\{e,f_1,\ldots,f_d\}\), with the origin additionally contacting exactly when \(3\le d\le5\). Thus the Löwner contact set undergoes a strict **dimension-six transition**.

For the enclosing simplices \(S_d=\{x\ge0:\sum_i x_i\le\sqrt d\}\) and \(T_d=\operatorname{conv}\{0,e,f_1,\ldots,f_d\}\), there are exact, nontrivial invariances \(J(K_d)=J(S_d)\) and \(L(K_d)=L(T_d)\). Moreover for \(d\ge6\), the origin can be omitted from \(T_d\) without changing its Löwner ellipsoid. The exact Löwner-to-John volume ratio is
\[
\frac{\operatorname{vol}(L_d)}{\operatorname{vol}(J_d)}=
\begin{cases}
\dfrac{d+1}{2}\left(\dfrac{(d+1)(\sqrt d+1)}4\right)^{(d-1)/2},&3\le d\le5,\\[5pt]
(\sqrt d-1)d^{d/2},&d\ge6.
\end{cases}
\]

## Assumptions and scope
Every statement holds for integer dimension \(d\ge3\) with standard Euclidean volume, nonnegative closed orthant and unit Euclidean ball. The excluded planar sector \(d=2\) is not asserted as novel. An ellipsoid's shape matrix \(Q\) means \(\{c+Q^{1/2}u:\|u\|_2\le1\}\), not its inverse. No claim about other norms, tilted cones or arbitrary spherical polyhedra is made.

## Proof
**John containment and contacts.** Put \(c=d e/(d+1)\) and \(Q=s ee^\mathsf T+t(I-ee^\mathsf T)\), where \(s=(d+1)^{-2}\), \(t=(d+1)^{-1}\). Then every diagonal entry satisfies \(Q_{ii}=d/(d+1)^2=c_i^2\). The minimum of coordinate \(x_i\) over this ellipsoid equals \(c_i-\sqrt{Q_{ii}}=0\). Thus every coordinate is nonnegative. For \(z=e\cdot x\), the ellipsoid gives \((d-1)/(d+1)\le z\le1\) and
\[
\|x\|_2^2\le z^2+t\left(1-\frac{(z-d/(d+1))^2}{s}\right)=1-d(1-z)^2\le1.
\]
The upper equality holds at \(e\), and each coordinate minimum occurs at \(v_i=(\sum_j f_j-f_i)/\sqrt d\), which satisfies \(\|v_i\|_2^2=(d-1)/d<1\). The normalized points \(u_i=Q^{-1/2}(v_i-c)\) and \(u_{d+1}=Q^{-1/2}(e-c)\) are the \(d+1\) vertices of a regular simplex on the unit sphere: their pairwise inner products are \(-1/d\) and the sum is zero. Therefore \(\sum_{i=1}^{d+1}\frac d{d+1}u_i=0\) and \(\sum_{i=1}^{d+1}\frac d{d+1}u_iu_i^\mathsf T=I\). John's sufficient contact criterion proves global maximum volume and uniqueness. The same contacts lie on \(\partial S_d\), and the ellipsoid is inside \(S_d\), proving the additional John invariance.

**Löwner containment.** For each proposed pair \((\lambda;s,t)\), \(0<s<t\). A unit point \(\omega\) in the positive orthant has \(z=e\cdot\omega\in[1/\sqrt d,1]\). Its squared gauge in the proposed ellipsoid is
\[
q(z)=\frac{(z-\lambda)^2}{s}+\frac{1-z^2}{t}.
\]
It is a strictly convex quadratic function, and direct substitution yields \(q(1/\sqrt d)=q(1)=1\). Convexity yields \(q(z)\le1\), with equality only at \(z=1/\sqrt d\) or \(1\). The equality unit vectors are respectively \(f_i\) and \(e\). The origin has gauge \(\lambda^2/s\le1\): in the first regime it equals one, while in the second it equals \((\sqrt d+1)^2/[d(\sqrt d-1)^2]<1\), since \(d\ge6\). Since \(K_d=\operatorname{conv}(\{0\}\cup\{\omega\ge0:\|\omega\|_2=1\})\), convexity of the ellipsoid proves containment and identifies the complete contact locus. More explicitly, strict convexity of its squared gauge rules out any other boundary point inside those radial segments.

**Löwner optimality.** For \(3\le d\le5\), assign probability mass \(a=(\sqrt d+1)/(4d)\) to each of the \(d\) points \(f_i\), \(b=(2-\sqrt d+1/\sqrt d)/4\) to the origin, and \(c=(1-1/\sqrt d)/4\) to \(e\). These are positive (\(b>0\) precisely when \(d<3+2\sqrt2\)) and sum to one. Direct coordinate calculation gives weighted mean \(\lambda e\), where \(\lambda=1/2\), and weighted covariance \(Q/d\), where \(Q=(1/4)ee^\mathsf T+((\sqrt d+1)/4)(I-ee^\mathsf T)\). For \(d\ge6\), assign equal mass \(1/(d+1)\) to each of the \(d+1\) points \(f_1,\ldots,f_d,e\). Their mean is \(\lambda e\), with \(\lambda=(\sqrt d+1)/(d+1)\), and their covariance is \(Q/d\), with \(s=d(\sqrt d-1)^2/(d+1)^2\), \(t=d/(d+1)\). In either case all supporting points lie on \(\partial K_d\cap\partial L_d\). Normalize by \(Q^{-1/2}\); the transformed probability measure has mean zero and covariance \(I/d\), so multiplying weights by \(d\) satisfies the Löwner contact conditions \(\sum w_i u_i=0\), \(\sum w_i u_iu_i^\mathsf T=I\). The Löwner contact theorem proves the unique global minimum-volume enclosing ellipsoid. Since all its supporting contact points belong to \(T_d\), the same certificate applies to the finite polytope; for \(d\ge6\) the origin has zero weight and can be removed. This proves both invariances and the sharp contact transition.

**Volume ratio.** The volume of \(E(\lambda;s,t)\) is \(\kappa_d\sqrt{s}\,t^{(d-1)/2}\). Substitute the displayed parameters and cancel \(\kappa_d\) to obtain the two branches.

## Verification
The separate executable `check_orthant_ball.py` checks the explicit covariance/contact identities, candidate containment, and independent numerical optimal-design solutions. Numerical tests cover dimensions \(3\) through \(60\), and independent numerical optimization covers \(3,4,5,6,7,10,20\). The finite computations are corroboration, not substitutes for the all-dimensional proof and contact certificates. Invoke `python check_orthant_ball.py` with NumPy and SciPy.

## Relationship to prior work
Güler and Gürtuna (2007) prove the general John/Löwner contact framework and study several other families, including parallel-slab cuts and truncated circular cones; these are not an orthant cut by \(d\) mutually perpendicular halfspaces. Gruber and Schuster (2012) give a general arithmetic treatment of the John criterion but not this classification. Bansal et al. (2018) investigate the same nonnegative-orthant Euclidean ball in an algorithmic setting, but determine an enclosing **Euclidean ball**, not the minimum-volume enclosing ellipsoid and its contact transition. Existing calculations for circular spherical sectors and for diagonal-capped cubes concern different domains. Thus the explicit dual ellipsoid formulas, finite-set invariances, and dimension-six contact transition are not immediate consequences of those inspected results. Historical-priority uncertainty remains.

## Limitations
Novelty is assessed against the inspected sources and indexed comparisons; it is not an independent exhaustive priority certification. This theorem concerns only standard orthants and dimensions at least three; the shape matrices and Euclidean normalization are essential. The scientific correctness argument is analytical; no inference from finite computation to arbitrary dimension is made.

## References
- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases* (2007), arXiv:0709.0707, https://arxiv.org/abs/0709.0707.
- P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem* (2012), arXiv:1207.7246, https://arxiv.org/abs/1207.7246.
- N. Bansal, M. Böhm, M. Eliáš, G. Koumoutsos and S. W. Umboh, *Nested convex bodies are chaseable* (2018), DOI:10.1137/1.9781611975031.81.
