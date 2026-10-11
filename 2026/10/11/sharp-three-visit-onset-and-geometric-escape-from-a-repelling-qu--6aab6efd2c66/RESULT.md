# Sharp three-visit onset and geometric escape from a repelling quadrant focus

## Finding

For every real \(b>1/2\), consider the continuous piecewise-affine map
\[
F_b(x,y)=\bigl(|x|-y-1,\ x-|y|+b\bigr)
\]
and the open second quadrant \(Q_2=\{(x,y):x<0<y\}\). For integers \(n\ge1\), define the \(n\)-visit survivor set
\[
S_n(b)=\{z\in\mathbb R^2:F_b^j(z)\in Q_2\text{ for all }0\le j<n\}.
\]
Its unique fixed point in \(Q_2\) is \(p_b=(-(b+2)/5,(2b-1)/5)\). Put
\[
A=\begin{pmatrix}-1&-1\\1&-1\end{pmatrix},\qquad
\alpha=(b+2)/5,\quad\beta=(2b-1)/5.
\]
Then, as actual sets (not merely up to null boundaries),
\[
\boxed{S_n(b)=p_b+A^{-(n-3)}\bigl(S_3(b)-p_b\bigr)\qquad(n\ge3).}
\]
Consequently, for all \(n\ge3\),
\[
\boxed{\operatorname{area}(S_n(b))=2^{-(n-3)}C(b)},\qquad
\boxed{C(b)=\begin{cases}(2b-1)^2/8,&1/2<b\le1,\\(b^2+2b-2)/8,&b\ge1.\end{cases}}
\]
The threshold \(n=3\) is sharp: the displayed inverse similarity fails at \(n=2\), for every finite \(b>1/2\). The polygon \(S_3(b)\) is triangular when \(1/2<b\le1\) and pentagonal when \(b>1\), with a genuine second-derivative discontinuity of \(C\) at \(b=1\).

If an initial point is chosen according to uniform area measure on the bounded set \(S_3(b)\) and \(\tau\) is its first exit time from \(Q_2\), then the conditional distribution is exactly
\[
\boxed{\Pr(\tau=3+k\mid z\in S_3(b))=2^{-k-1}\quad(k=0,1,2,\ldots)},
\qquad \boxed{\mathbb E[\tau\mid z\in S_3(b)]=4.}
\]
The fixed point \(p_b\) is the only initial condition that never leaves \(Q_2\).

## Assumptions and scope

All statements concern real \(b>1/2\), the single normalized map above (affine offset \(-1\)), strictly open quadrants, two-dimensional Lebesgue area, and the first contiguous block of visits to \(Q_2\). No invariant probability distribution on the whole plane is presumed. For the geometric first-exit law, the probability law is uniform area conditional on survival for the first three visits. The first-exit time is \(\tau(z)=\min\{j\ge0:F_b^j(z)\notin Q_2\}\). The area and polygon closures are finite for \(n\ge3\); boundaries have area zero and are excluded from the strict sets. This does not claim a distribution for arbitrary initial measures or for returns after leaving \(Q_2\).

## Proof

**Affine reduction.** On \(Q_2\) the branch is \(F_b(x,y)=(-x-y-1,x-y+b)\). Direct substitution shows \(F_b(p_b)=p_b\). If \(w=(u,v)\), then the branch becomes \(w\mapsto Aw\). The quadrant requirement is precisely \(u<\alpha\) and \(v> -\beta\). The restrictions \(b>1/2\) imply \(\alpha>0\), \(\beta>0\), and \(\beta<2\alpha\). Thus the second-quadrant survivor sets in centered coordinates are intersections of the open half-planes imposed on \(A^j w\), \(0\le j<n\).

**Exact third survivor polygon.** Because
\[
A^2=\begin{pmatrix}0&2\\-2&0\end{pmatrix},
\]
three consecutive quadrant tests yield
\[
\begin{gathered}
 u<\alpha,\quad v>-\beta,\\
 -u-v<\alpha,\quad -u+v<\beta,\\
 2v<\alpha,\quad 2u<\beta.
\end{gathered}
\]
Since \(\beta/2<\alpha\), the first upper bound on \(u\) is redundant. Therefore \(S_3(b)-p_b\) is exactly the bounded open polygon
\[
\boxed{\{(u,v):v>-\beta,\ v<\alpha/2,\ -\alpha-v<u,\ v-\beta<u<\beta/2\}.}
\]
It is nonempty because it contains \((0,0)\) and bounded because the displayed inequalities bound both coordinates. At fixed \(v\), its horizontal width is
\[
 \frac\beta2-\max\{-\alpha-v,\,v-\beta\},
\]
when this is positive and zero otherwise. The two candidate lower edges meet at \(v_0=(\beta-\alpha)/2\). If \(\beta\le\alpha/3\), equivalently \(b\le1\), the active interval is \(-\beta<v<3\beta/2\) and the width is \(3\beta/2-v\); hence
\[
 \operatorname{area}(S_3)=\int_{-\beta}^{3\beta/2}(3\beta/2-v)\,dv=25\beta^2/8=(2b-1)^2/8.
\]
If \(\alpha/3<\beta<2\alpha\), equivalently \(b>1\), the active interval is \(-\beta<v<\alpha/2\). Integrating widths \(\beta/2+\alpha+v\) from \(-\beta\) to \(v_0\), and \(3\beta/2-v\) from \(v_0\) to \(\alpha/2\), gives
\[
 \operatorname{area}(S_3)=(-2\beta^2+18\alpha\beta-3\alpha^2)/8=(b^2+2b-2)/8.
\]
The corresponding boundary has three edges for \(b\le1\), five edges for \(b>1\). The two displayed formulas agree with first derivative at \(b=1\); their second derivatives are respectively \(1\) and \(1/4\).

**Exact inverse trapping.** The inverse branch matrix is
\[
 A^{-1}=\tfrac12\begin{pmatrix}-1&1\\-1&-1\end{pmatrix}.
\]
For every \(w=(u,v)\in S_3-p_b\), the first coordinate of \(A^{-1}w\) is \((-u+v)/2<\beta/2<\alpha\) by the second-visit inequality \(-u+v<\beta\). Moreover, the same inequality gives \(v<u+\beta\), and the third-visit inequality gives \(u<\beta/2\); therefore \(u+v<2u+\beta<2\beta\), so the second coordinate \(-(u+v)/2\) of \(A^{-1}w\) exceeds \(-\beta\). Hence
\[
 p_b+A^{-1}(S_3-p_b)\subset Q_2.
\]
The preimage of a survivor point by the affine second-quadrant branch thus lies in the quadrant and has all subsequent visits certified; therefore \(S_4=p_b+A^{-1}(S_3-p_b)\subset S_3\). Repeating this argument, since every smaller survivor set lies in \(S_3\), proves by induction the claimed set identity for every \(n\ge3\).

**Area and escape law.** The matrix has determinant \(2\) and \(A^\mathsf{T}A=2I\). Each inverse multiplies planar area by \(1/2\), proving the area law. The sets are nested and their diameters decay by a factor \(1/\sqrt2\) per visit. Their unique common point is \(p_b\), which is indeed fixed. The area ratio \(\operatorname{area}(S_{3+k})/\operatorname{area}(S_3)=2^{-k}\) gives \(\Pr(\tau\ge3+k\mid S_3)=2^{-k}\), and subtracting consecutive tails gives the geometric law and its expectation \(4\).

**Sharp onset.** The closure of \(S_2-p_b\) contains \(w=(\alpha,\alpha+\beta)\), since this point satisfies all four non-strict first-two-visit inequalities. But
\[
 A^{-1}w=(\beta/2,\,-\alpha-\beta/2)
\]
violates the second-quadrant lower bound on its second coordinate because \(\beta<2\alpha\). By strict inequality and continuity, some interior neighborhood inside \(S_2\) also has inverse image outside \(Q_2\). Hence \(S_3\ne p_b+A^{-1}(S_2-p_b)\), establishing sharpness of the three-visit start.

## Verification

The supplied standalone standard-library program `check_exact.py` performs independently implemented, rational-arithmetic half-plane clipping, computes the polygons defined by the first \(n\) branch constraints for \(3\le n\le11\), checks their exact areas, and compares the vertex sets with the inverse-affine images of the preceding polygons. Tests use the rational parameters \(b=51/100,3/4,1,5/4,2,10,101/2\), including both sides and the boundary of the polygon-shape transition. The program also checks an exact witness to the sharpness of the onset. Run `python check_exact.py`; successful output is `Q2_EXACT_RATIONAL_POLYGON_CHECK_OK`. The analytical proof above establishes the universal real-parameter and infinite-iterate statements; finite checks alone could not do so.

## Relationship to prior work

Cima, Gasull, Mañosa, and Mañosas introduced this normalized family and, in their Proposition 17, identified the repelling fixed point in \(Q_2\) for \(b>1/2\) and proved that other points cannot stay there indefinitely. Their results describe invariant absorbing graphs, periodic dynamics, and topological entropy, not a parameter-uniform exact planar finite-survival area or conditional exit-time distribution. The later paper by the same authors concerns entropy and limit sets on those invariant graphs, not the planar area of consecutive second-quadrant visits. Krisuk, Soprom, Pantain, and Tikjha consider a separate second-quadrant initial-condition classification at affine offsets \(-3\) and \(+1\), which normalizes to a different parameter regime \(b=1/3\) and does not imply the result for \(b>1/2\). The new contribution resolves a quantitative transient issue left implicit by the repelling-focus observation: an exact, sharply initiated polygonal similarity, its shape transition, and the induced area-law distribution. General affine exit-polygon methods could overlap; no claim of absolute publication priority is made.

## Limitations

The initial distribution for the geometric law is area-uniform on \(S_3\), not invariant or globally uniform. The result does not classify later quadrant returns, the basin on the invariant graph, other parameters \(b\le1/2\), or non-normalized values of the affine offset without corresponding rescaling. The linear algebra and polygon identity are elementary, but the first scale at which inverse trapping holds and the exact parameter-dependent polygon geometry require all branch inequalities. Historical priority relative to unidentified equivalent computations is not independently certified. No external independent mathematical audit has been performed.

## References

1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052v1 (first public 2024-10-01), especially Proposition 17 and Sections 4–5. https://arxiv.org/abs/2410.01052
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Entropy and ω-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411v1 (2025), especially Theorems on entropy and graph-supported limit sets. https://arxiv.org/abs/2503.02411
3. S. Krisuk, K. Soprom, J. Pantain, W. Tikjha, *Equilibrium Solution on a Two-dimensional Piecewise Linear Map*, KKU Science Journal 50(3) (2022), 223–230; public online 2023-01-28. https://ph01.tci-thaijo.org/index.php/KKUSciJ/article/view/251510 (different parameter regime and focus).
