# Exact Euclidean inradius and tangent-facet phase of complete multipartite symmetric edge polytopes
## Finding
Let \(G=K_{a_1,\ldots,a_k}\) be a complete multipartite graph with \(k\ge 3\), \(a_i\ge1\), and \(n=\sum_i a_i\). Its symmetric edge polytope is
\[
P_G=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G)\}\subset H,
\qquad H=\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\right\}.
\]
Give \(H\) the Euclidean metric induced from \(\mathbb R^n\). Define
\[
C_n=\frac{\lfloor n^2/4\rfloor}{n},
\qquad
L_*=\max_{i:a_i\ge2}\left(a_i-\frac{\mathbf 1_{a_i\text{ odd}}}{n}\right),
\]
with \(L_*=0\) when all parts are singletons. Then the intrinsic Euclidean inradius is
\[
\boxed{\displaystyle r(P_G)=\frac1{\sqrt{\max\{C_n,L_*\}}}.}
\]
There is also a complete description of the tangent facets at the centered largest ball. If \(L_*>C_n\), the tangent facets are exactly the type-I facets supported on parts attaining \(L_*\), with the \(+1\) and \(-1\) values as balanced as parity permits. If \(C_n>L_*\), the tangent facets are exactly the admissible type-II \(0/1\) facets with \(\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\) entries equal to one. If \(L_*=C_n\), both families occur. The origin is a Chebyshev center.

## Assumptions and scope
The graph is complete multipartite with at least three nonempty parts. This guarantees connectedness and dimension \(n-1\). Distances are measured inside the affine span \(H\), not in a coordinate quotient or in a lattice-normalized metric.

A facet of a symmetric edge polytope may be represented by an integer labeling \(f:V(G)\to\mathbb Z\), unique up to addition of a constant, whose tight-edge graph is connected. For complete multipartite graphs the published classification has two forms. Type I has one part taking only \(-1\) and \(+1\), with every other part equal to zero. Type II has values in \(\{0,1\}\), and either is constant on every part or splits at least two parts.

## Proof
Because \(P_G\) is centrally symmetric, if a Euclidean ball \(B(c,r)\) lies in \(P_G\), then \(B(-c,r)\) also lies in \(P_G\). Convexity implies that their midpoint set contains \(B(0,r)\). Hence some largest inscribed ball is centered at the origin, and its radius is the minimum distance from the origin to a facet hyperplane.

For a facet labeling \(f\), write \(\bar f=n^{-1}\sum_v f(v)\). The restriction of the functional \(x\mapsto\langle f,x\rangle\) to \(H\) has Euclidean normal
\[
f-\bar f\mathbf 1.
\]
The facet equation is \(\langle f,x\rangle=1\), so its distance from the origin is
\[
d(f)=\frac1{\|f-\bar f\mathbf1\|_2}.
\]
Thus the inradius is the reciprocal square root of the largest squared projected-normal norm among facets.

For a type-I facet supported on a part of size \(a\), let \(t\) vertices carry \(+1\) and \(a-t\) carry \(-1\). Directly,
\[
\|f-\bar f\mathbf1\|_2^2
=a-\frac{(2t-a)^2}{n}.
\]
This is maximized by the most balanced sign split. Its maximum is \(a\) when \(a\) is even and \(a-1/n\) when \(a\) is odd. Maximizing over the non-singleton parts gives exactly \(L_*\).

For a type-II facet with \(s\) ones and \(n-s\) zeros,
\[
\|f-\bar f\mathbf1\|_2^2
=\frac{s(n-s)}n
\le \frac{\lfloor n^2/4\rfloor}{n}=C_n.
\]
It remains only to see when the balanced values of \(s\) are admissible. If every part is a singleton, every nonconstant \(0/1\) labeling is type II. If at least two parts have size at least two, keep one selected and one unselected vertex in each of two such parts; then for every \(2\le s\le n-2\), choose any further \(s-2\) selected vertices among the remaining \(n-4\). Both distinguished parts stay split, so the labeling is admissible. In particular a balanced \(s\) exists.

The only remaining case has exactly one non-singleton part, of size \(a\), and \(n-a\) singleton parts. If \(\lfloor n/2\rfloor\le n-a\), a balanced type-II labeling is obtained by selecting only singleton parts. If instead \(\lfloor n/2\rfloor>n-a\), then the unique large part has more than half of all vertices; in this regime its type-I contribution is strictly larger than \(C_n\). Consequently any failure to realize a balanced type-II facet cannot change the maximum projected-normal norm. Combining the two facet types gives
\[
\max_f\|f-\bar f\mathbf1\|_2^2=\max\{C_n,L_*\},
\]
and therefore the displayed inradius formula. The equality cases in the two elementary maximizations give the stated tangent-facet phase description.

## Verification
A standalone checker reconstructs facet labelings directly from the general tight-edge criterion rather than assuming the specialized complete-multipartite classification. For every unordered multipartition of \(n\) with at least three parts and \(3\le n\le8\), it fixes one labeling value to zero, exhausts the finite range forced by graph diameter two and the edge-Lipschitz condition, requires the tight-edge graph to be connected, and compares the largest exact rational projected-normal norm with the formula above.

The replay result is:

`VERIFY_OK complete-multipartite symmetric-edge inradius partitions=42 facet_labelings=5868 n=3..8`

This finite computation is corroboration only. The theorem for arbitrary \(n\) follows from the analytic argument above and the published facet classification.

## Relationship to prior work
Higashitani, Jochemko, and Michałek classify all facets of symmetric edge polytopes of complete multipartite graphs; that classification is the structural premise used here. Their article does not state an intrinsic Euclidean inradius, Chebyshev-center, or tangent-facet phase theorem. D'Alì, Delucchi, and Michałek develop further face and adjacency theory for symmetric edge polytopes, but the inspected full text likewise contains no inradius result. The regular-matroid generalization by D'Alì, Juhnke-Kubitzke, and Koch supplies a broader combinatorial framework, not the Euclidean metric formula above.

The new point is the exact metric optimization over the complete known facet set: the nearest-facet obstruction is governed by a competition between a local signed split inside the largest part and a global balanced \(0/1\) cut, with an explicit parity correction and a sharp transition where both are tangent.

## Limitations
The result is specific to complete multipartite graphs and the intrinsic Euclidean metric inherited from the standard root-vector realization. It does not determine inradii after arbitrary linear equivalence, and it does not assert uniqueness of the Chebyshev center. The computational check reaches only \(n=8\) and is not used as evidence for the infinite quantifier. A residual literature risk is that the same metric formula may have appeared under older root-polytope, Lipschitz-polytope, or Kantorovich--Rubinstein terminology not indexed by the searches performed.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1; later published in *Mathematika*, DOI 10.1112/S0025579319000147. First public version: 2018-07-20.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, DOI 10.37236/10387.
3. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1.
