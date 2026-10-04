# Exact curvature-distortion number of pineapple graphs
## Finding
For integers \(p\ge 3\) and \(q\ge 1\), let \(P_{p,q}\) be obtained from a clique \(K_p\) by attaching \(q\) pendant vertices to one distinguished clique vertex \(x\). Then
\[
\operatorname{DN}_{\mathrm{LLY}}(P_{p,q})=
\max\!\left\{1,\frac{p-2}{4}\left(\sqrt{1+\frac{8q}{(p-1)(p-2)}}-1\right)\right\}.
\]
In particular, the unit weight has nonnegative weighted Lin--Lu--Yau curvature on every edge exactly when
\[
q\le \frac{p(p-1)}{p-2}.
\]

## Assumptions and scope
The graph is finite, simple, and connected. Weighted Lin--Lu--Yau curvature and distortion are those of Xia: edge weights are positive, transition probabilities are normalized by weighted degree, while the transport distance remains the unweighted combinatorial graph distance. For an edge \(uv\),
\[
\kappa_{\mathrm{LLY}}^w(u,v)=\inf\{\Delta_w f(u)-\Delta_w f(v): f\in\operatorname{Lip}(1),\ f(v)-f(u)=1\},
\]
and \(\operatorname{DN}_{\mathrm{LLY}}\) is the infimum of \(\max_e w_e/\min_e w_e\) over positive weights with nonnegative curvature on every edge. The result covers the standard pineapple family with clique order \(p\ge3\) and any positive number of pendant vertices.

## Proof
Write \(D\) for the distortion of an arbitrary admissible weight and rescale so that the smallest edge weight is \(1\). Let \(x\) be the attachment vertex. Put \(L\) for the total weight of the \(q\) pendant edges and \(P\) for the total weight of the \(p-1\) clique edges incident with \(x\). Fix a clique neighbor \(a\) of \(x\), let \(r=w_{xa}\), and let \(R\) be the total weight of the \(p-2\) clique edges joining \(a\) to the other clique vertices.

For the edge \(xa\), use the feasible \(1\)-Lipschitz function that is \(0\) at \(x\), \(1\) at every other clique vertex, and \(-1\) at every pendant vertex. Nonnegative curvature forces its dual objective to be nonnegative:
\[
0\le \frac{P-L}{P+L}+\frac{r}{r+R}.
\]
After clearing denominators this is
\[
LR\le P(2r+R),\qquad\text{hence}\qquad L\le P\left(1+\frac{2r}{R}\right).
\]
Normalization gives \(L\ge q\), \(P\le(p-1)D\), \(r\le D\), and \(R\ge p-2\). Therefore every admissible weight satisfies
\[
q\le (p-1)D\left(1+\frac{2D}{p-2}\right).
\]
Solving this quadratic and also using \(D\ge1\) yields
\[
D\ge s:=\max\!\left\{1,\frac{p-2}{4}\left(\sqrt{1+\frac{8q}{(p-1)(p-2)}}-1\right)\right\}.
\]

For the matching upper bound, give weight \(s\) to each of the \(p-1\) clique edges incident with \(x\), and weight \(1\) to every other edge. Set
\[
d_x=(p-1)s+q,\qquad d_a=s+p-2
\]
for a clique vertex \(a\ne x\). A pendant edge has curvature \(2/d_x>0\). A clique edge whose endpoints both differ from \(x\) has curvature
\[
\frac{s+p-1}{s+p-2}>0.
\]
For an edge \(xa\), normalize a dual function by \(f(x)=0\) and \(f(a)=1\). Every other clique value lies in \([0,1]\), while each pendant value lies in \([-1,1]\). The coefficient of a pendant value in the dual objective is positive, so the minimum uses \(-1\). The coefficient of each other clique value is
\[
\frac{s}{(p-1)s+q}-\frac{1}{s+p-2},
\]
whose numerator is \(s^2-s-q<0\); hence the minimum uses value \(1\) on all other clique vertices. Thus
\[
\kappa_{\mathrm{LLY}}^w(x,a)=
\frac{2(p-1)s^2+(p-1)(p-2)s-q(p-2)}{((p-1)s+q)(s+p-2)}\ge0.
\]
The final inequality is exactly the defining quadratic inequality for \(s\). Hence this weight is admissible and has distortion \(s\), proving equality.

## Verification
The proof gives a lower bound for every positive admissible weight, not only for symmetric weights, because the test function is applied before any symmetry assumption. The upper-bound weight was checked edge type by edge type. The accompanying verifier checks the closed curvature formulas for \(600\) parameter pairs with \(3\le p\le12\) and \(1\le q\le60\), and independently minimizes the normalized dual objective by finite enumeration in \(20\) small cases. It reports `ALL CHECKS PASSED`. These finite checks are stress tests; the theorem itself follows from the inequalities above.

## Relationship to prior work
Xia introduced \(\operatorname{DN}_{\mathrm{LLY}}\), proved an explicit fixed-point theory for trees, and transferred tree information to the tree-like skeleton of a general graph. The same paper also gives a small non-tree example illustrating nonuniqueness of optimal weights. Its inspected full text does not treat pineapple graphs or derive the formula above. In a pineapple graph, the pendant edges are tree-like but the useful lower bound here comes from a clique edge lying in triangles; the published tree-like-edge degree bound therefore does not imply the claimed value. Pineapple graphs themselves are a standard named family obtained by attaching pendant vertices to one clique vertex.

## Limitations
The formula is specific to the standard pineapple family in which all pendant vertices attach to one clique vertex. It does not claim a formula for generalized pineapple graphs in which the independent vertices attach to several clique vertices, nor for curvature notions using a weight-dependent transport metric. The literature comparison is necessarily time-sensitive because the curvature-distortion invariant was introduced recently.

## References
Q. Xia, *Curvature-Distortion Numbers of Graphs: Nonnegative Lin--Lu--Yau Curvature*, arXiv:2609.12125, first public version 2026-09-10.

H. Topcu, S. Sorgun, and W. H. Haemers, *The graphs cospectral with the pineapple graph*, Discrete Applied Mathematics 269 (2019), 52--59. This is used only for the standard pineapple-family terminology.
