# A parity law for the Euclidean inradius of wheel symmetric edge polytopes
## Finding
Let \(m\ge5\), let
\[
W_m=K_1*C_m
\]
be the wheel with one cone vertex and an outer cycle of length \(m\), and let
\[
P_m=
\operatorname{conv}
\{\pm(e_u-e_v):uv\in E(W_m)\}
\subset
\left\{
x\in\mathbb R^{m+1}:\sum_i x_i=0
\right\}.
\]
With the intrinsic Euclidean metric of this hyperplane,
\[
\boxed{
r(P_m)=
\begin{cases}
\dfrac1{\sqrt{m-2}},&m\text{ even},\\[6pt]
\sqrt{\dfrac{m+1}{m^2-m-3}},&m\text{ odd}.
\end{cases}
}
\tag{1}
\]

The origin is an incenter. More precisely, the facets tangent to the centered maximal ball are exactly the following facet-label orbits.

If \(m\) is even, put
\[
a=\frac m2-1.
\]
The tangent facets are the \(m\) cyclic rotations of
\[
\underbrace{+\cdots+}_{a}\,0\,
\underbrace{-\cdots-}_{a}\,0.
\tag{2}
\]

If \(m\) is odd, put
\[
a=\frac{m-1}{2},
\qquad
b=\frac{m-3}{2}.
\]
The tangent facets are the \(2m\) words obtained from all cyclic rotations of
\[
\underbrace{+\cdots+}_{a}\,0\,
\underbrace{-\cdots-}_{b}\,0
\tag{3}
\]
and their sign reversals.

Equivalently, if \(c(W_m)\) denotes graph spread, namely the maximum variance of a real \(1\)-Lipschitz function on the \(m+1\) vertices under the uniform measure, then
\[
\boxed{
c(W_m)=
\begin{cases}
\dfrac{m-2}{m+1},&m\text{ even},\\[6pt]
\dfrac{m^2-m-3}{(m+1)^2},&m\text{ odd}.
\end{cases}
}
\tag{4}
\]

## Assumptions and scope
The symmetric edge polytope is taken in its canonical root-vector realization, so the metric claim is not invariant under arbitrary affine changes of coordinates.

The cone vertex of \(W_m\) is assigned label \(0\). D'Alì, Delucchi, and Michałek show that wheel facets are represented by cyclic words in \(\{+,0,-\}\) having no adjacent \(+-\) or \(-+\), and no cyclic occurrence of \(000\). The labels in (2)--(3) are interpreted in precisely that normalization.

The restriction \(m\ge5\) separates this theorem from the complete-multipartite small wheels. Indeed, \(K_1*C_3=K_4\) and \(K_1*C_4=K_{1,2,2}\), whereas \(K_1*C_m\) is not complete multipartite for \(m\ge5\).

## Proof
Write
\[
H=
\left\{
x\in\mathbb R^{m+1}:\sum_i x_i=0
\right\}.
\]
Because the vertices of \(P_m\) are the signed edge roots, its polar in \(H\) is
\[
P_m^\circ
=
\left\{
y\in H:
|y_u-y_v|\le1
\text{ for every }uv\in E(W_m)
\right\}.
\tag{5}
\]
This is the graph Lipschitz polytope.

For a centrally symmetric convex body \(K\), every inscribed ball can be recentered at the origin without decreasing its radius: if \(B(c,r)\subset K=-K\), then \(B(-c,r)\subset K\), and convexity gives \(B(0,r)\subset K\). Hence
\[
r(K)=\frac1{\max_{z\in K^\circ}\|z\|}.
\tag{6}
\]

Fix the cone label to be \(0\), and write the outer labels as
\[
x_1,\ldots,x_m.
\]
D'Alì--Delucchi--Michałek's wheel-facet classification says that every vertex of \(P_m^\circ\), modulo adding a constant before returning to \(H\), is represented by a cyclic word
\[
x_i\in\{-1,0,1\},
\tag{7}
\]
with no adjacent \(1,-1\) or \(-1,1\), and no three consecutive zeros.

Since the squared Euclidean norm is convex, its maximum on \(P_m^\circ\) is attained at a vertex. Let
\[
p=\#\{i:x_i=1\},
\qquad
q=\#\{i:x_i=-1\},
\qquad
z=m-p-q.
\]
After centering the \(m+1\) labels, including the cone label \(0\), the squared norm is
\[
N(p,q)
=
p+q-\frac{(p-q)^2}{m+1}.
\tag{8}
\]

Suppose first that \(p,q>0\). Moving cyclically from a positive label to a negative one requires a zero between them, and returning from negative to positive requires a second zero. Thus
\[
z\ge2,
\qquad
p+q\le m-2.
\tag{9}
\]
For a fixed value
\[
s=p+q,
\]
equation (8) is maximized when \(p\) and \(q\) are as balanced as possible. Therefore the best value at fixed \(s\) is
\[
M(s)=
\begin{cases}
s,&s\text{ even},\\[4pt]
s-\dfrac1{m+1},&s\text{ odd}.
\end{cases}
\tag{10}
\]
Both parity transitions strictly increase this quantity as \(s\) increases, so (9) forces the mixed-sign maximum to occur at
\[
s=m-2.
\tag{11}
\]

If \(m\) is even, then \(m-2\) is even, so
\[
p=q=\frac{m-2}{2}
\]
and
\[
\max N=m-2.
\tag{12}
\]
If \(m\) is odd, then \(m-2\) is odd, so
\[
\{p,q\}
=
\left\{
\frac{m-1}{2},
\frac{m-3}{2}
\right\}
\]
and
\[
\max N
=
m-2-\frac1{m+1}
=
\frac{m^2-m-3}{m+1}.
\tag{13}
\]

It remains to rule out a one-sign maximizer. If, say, \(q=0\), then
\[
N(p,0)
=
p-\frac{p^2}{m+1}
=
\frac{p(m+1-p)}{m+1}.
\tag{14}
\]
Even if the wheel-facet constraints are ignored, the right side is at most
\[
\frac{\left\lfloor (m+1)^2/4\right\rfloor}{m+1}.
\tag{15}
\]
For even \(m\ge6\),
\[
m-2-
\frac{m(m+2)}{4(m+1)}
=
\frac{3m^2-6m-8}{4(m+1)}
>0.
\tag{16}
\]
For odd \(m\ge5\),
\[
m-2-\frac1{m+1}-\frac{m+1}{4}
=
\frac{3m^2-6m-13}{4(m+1)}
>0.
\tag{17}
\]
So the mixed-sign values (12)--(13) are globally maximal.

Equality in (9) means there are exactly two zeros. Since both signs occur and opposite signs may not be adjacent, the two zeros must be precisely the two transition separators. Hence there is one positive cyclic block and one negative cyclic block. The balancing conditions above force exactly the words in (2)--(3). These words contain no \(000\), so the wheel-facet criterion confirms that every maximizer is indeed facet-defining.

For even \(m\), sign reversal is a rotation by \(m/2\), so (2) has exactly \(m\) distinct cyclic rotations. For odd \(m\), the positive and negative block lengths differ, so sign reversal is not a rotation; (3) and its negative give two rotation orbits, totaling \(2m\) facets.

Combining (6), (12), and (13) proves (1) and the tangent-facet count. Finally, the graph spread is
\[
c(W_m)
=
\frac1{m+1}
\max_{y\in P_m^\circ}\|y\|^2,
\tag{18}
\]
so (4) follows from the same maximization.

## Verification
The argument above is finite-dimensional but symbolic for every \(m\ge5\). The accompanying `verify.py` independently enumerates all ternary outer labelings through \(m=11\), enforces the wheel edge constraints and the source's \(000\) facet condition, centers the labels exactly using rational arithmetic, and checks:
- the maximum squared polar norm in each parity;
- the predicted number of maximizing facet words;
- the two-zero block structure of every maximizer.

The enumeration is corroborative only; equations (8)--(17) are the arbitrary-\(m\) proof.

## Relationship to prior work
D'Alì, Delucchi, and Michałek identify symmetric edge polytopes with adjacency polytopes, connect their polars to Lipschitz polytopes, and devote a full subsection to wheel graphs. Their wheel result classifies facets by ternary cyclic words and computes facet counts and normalized volumes. That classification is the structural input used here. The inspected full text contains no inradius theorem, and the wheel subsection states its goal as facet-count and normalized-volume computation.

Graph spread is a previously established invariant: it is the maximum variance of a \(1\)-Lipschitz function on graph vertices. Addario-Berry, Janson, and McDiarmid study its probabilistic behavior, and Yancey studies extremal Lipschitz functions and exact structural questions for several graph families. Those sources make equation (18) a natural dual interpretation rather than a new definition. Targeted searches for a wheel spread formula did not locate the parity law (4), and Yancey's inspected article did not expose a wheel-specific evaluation.

Later symmetric-edge and adjacency-polytope work on wheels computes enumerative invariants such as \(h^*\)-polynomials and normalized volume. Those results do not imply the Euclidean polar norm optimization or identify the inball-contact facets.

## Limitations
The formulas concern the canonical Euclidean realization of \(P_m\). They are not affine invariants.

The theorem starts at \(m=5\). The wheels with outer cycles \(C_3\) and \(C_4\) belong to the complete-multipartite family and are intentionally excluded from the new claim.

The originality assessment cannot exclude an equivalent wheel-spread computation hidden under different finite-metric or Lipschitz-free-space terminology. Search nonappearance is not treated as a formal novelty certificate.

## References
1. Alessio D'Alì, Emanuele Delucchi, and Mateusz Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193, first public version 2019-10-11; Electronic Journal of Combinatorics 29(3) (2022), #P3.24, DOI 10.37236/10387.
2. Louigi Addario-Berry, Svante Janson, and Colin McDiarmid, *On the Spread of Random Graphs*, Combinatorics, Probability and Computing 23 (2014), 477--504.
3. Matthew P. Yancey, *Positively Curved Graphs*, Journal of Graph Theory 94 (2020), 539--578, DOI 10.1002/jgt.22545.
4. Hidefumi Ohsugi and Akiyoshi Tsuchiya, *The \(h^*\)-Polynomials of Locally Anti-Blocking Lattice Polytopes and Their \(\gamma\)-Positivity*, Discrete & Computational Geometry 66 (2021), 701--722.
