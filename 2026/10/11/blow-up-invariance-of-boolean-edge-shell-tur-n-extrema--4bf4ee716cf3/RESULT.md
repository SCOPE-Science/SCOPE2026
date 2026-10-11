# Blow-up invariance of Boolean edge-shell Turán extrema
## Finding
Let \(H=(V,E)\) be a finite nonempty simple graph. For positive integers \(n_v\), form the vertex blow-up \(H(\mathbf n)\) by replacing each vertex \(v\) with an independent cluster of size \(n_v\), and replacing each edge \(uv\) with all edges between the two corresponding clusters. For any finite graph \(J\), define
\[
\Omega_J=\{{0\}}\cup\{{e_x+e_y:xy\in E(J)\}}\subset (\mathbb Z/2\mathbb Z)^{{V(J)}}
\]
and
\[
\tau(J)=\sup\left\{{\sum_{{z}}f(z): f(0)=1,\ f\text{{ positive definite}},\ \operatorname{{supp}}f\subseteq\Omega_J\right\}}.
\]
Then every vertex blow-up preserves the extremum:
\[
\tau(H(\mathbf n))=\tau(H).
\]
In particular, for every complete multipartite graph with \(r\ge2\) nonempty parts,
\[
\tau(K_{{n_1,\ldots,n_r}})=2\left\lceil\frac r2\right\rceil.
\]
Thus the sharp value depends only on the number of parts, not on their sizes.

## Assumptions and scope
All graphs are finite, simple, and the base graph has at least one edge. Counting measure is used on the Boolean group. Positive definiteness is equivalent to nonnegativity of every Fourier coefficient. No assertion is made here about the full set of extremizers for an arbitrary blow-up, nor about arbitrary graph substitutions that add edges inside clusters.

## Proof
Write \(a_e=f(e_x+e_y)\) for \(e=xy\in E(J)\), and put
\[
t=\sum_z f(z)=1+\sum_{{e\in E(J)}}a_e.
\]
A character of the Boolean group is indexed by a vertex subset \(S\subseteq V(J)\). Its Fourier coefficient is
\[
\widehat f(S)=t-2\sum_{{e\in\delta_J(S)}}a_e.
\]
Hence positive definiteness is exactly the family of cut inequalities \(t-2a(\delta_J(S))\ge0\).

Introduce the signed cut-packing value
\[
\sigma(J)=\sup\left\{{\sum_{{e}}w_e:\sum_{{e\in\delta_J(S)}}w_e\le1\text{{ for every }}S\subseteq V(J)\right\}}.
\]
For any admissible \(f\) with \(t>0\), setting \(w_e=2a_e/t\) gives a feasible signed cut packing and
\[
\sum_e w_e=2-\frac2t.
\]
Conversely, if \(w\) is feasible and \(W=\sum_e w_e\), then \(W<2\): for a uniformly random cut, the expected cut weight is \(W/2\), while every cut weight is at most \(1\) and the empty cut has weight \(0\). Therefore
\[
t=\frac2{{2-W}},\qquad a_e=\frac t2w_e
\]
produces an admissible positive-definite function. It follows that
\[
\tau(J)=\frac2{{2-\sigma(J)}}.
\]

It remains to prove \(\sigma(H(\mathbf n))=\sigma(H)\). Let \(w\) be feasible on \(H\). On every edge between the clusters over \(u\) and \(v\), put
\[
\widetilde w_{{xy}}=\frac{{w_{{uv}}}}{{n_un_v}}.
\]
For a cut \(A\) of the blow-up, set \(p_v=|A\cap V_v|/n_v\). Its weight is
\[
\sum_{{uv\in E(H)}}w_{{uv}}\bigl(p_u(1-p_v)+(1-p_u)p_v\bigr).
\]
If independent Bernoulli variables choose base vertices with probabilities \(p_v\), this is the expected weight of the resulting base cut. Every base cut has weight at most \(1\), so the displayed quantity is at most \(1\). The lifted packing is feasible and has the same total weight, proving \(\sigma(H(\mathbf n))\ge\sigma(H)\).

For the reverse inequality, average any feasible packing on the blow-up over all permutations inside each cluster. Convexity and invariance of the cut inequalities preserve feasibility and total weight. The averaged weight is constant, say \(c_{{uv}}\), on every complete bipartite block over a base edge \(uv\). Put \(w_{{uv}}=n_un_vc_{{uv}}\). Every base cut is realized by taking whole clusters on each side, so its weight is at most \(1\). Thus \(w\) is feasible on \(H\) with the same total weight, proving the reverse inequality and hence blow-up invariance.

For \(K_r\), symmetry permits averaging an admissible function so that every edge coefficient equals one real number \(a\). If \(m=\binom r2\) and \(M=\lfloor r^2/4\rfloor\), the tight Fourier condition comes from a maximum cut and gives
\[
a\le\frac1{{2M-m}}=\frac1{{\lfloor r/2\rfloor}}.
\]
The resulting objective is
\[
1+\frac{m}{\lfloor r/2\rfloor}=2\left\lceil\frac r2\right\rceil.
\]
Blow-up invariance transfers this value to \(K_{{n_1,\ldots,n_r}}\). The lifted symmetric extremizer has coefficient \(1/(\lfloor r/2\rfloor n_i n_j)\) on each edge between parts \(i\) and \(j\).

## Verification
The proof is finite-dimensional and analytic. The accompanying `verify.py` uses exact rational arithmetic to exhaust all Fourier characters for six representative complete multipartite blow-ups, including unequal part sizes and both parities of \(r\). It verifies nonnegativity of every Fourier coefficient and the claimed objective values. This computation corroborates the explicit extremizers; it is not used as a substitute for the all-graph blow-up proof.

## Relationship to prior work
Kolountzakis and Révész formulate Turán's extremal problem for positive-definite functions on arbitrary locally compact abelian groups and emphasize finite groups, including finite-group packing and spectral bounds. Their inspected paper does not formulate supports from graph edge shells or a vertex-blow-up invariance principle. Šámal introduces fractional cut coverings and the cubical chromatic number, gives the cut linear programs, proves homomorphism monotonicity, and computes complete-graph values; the inspected paper does not connect those graph parameters to positive-definite Turán extrema. The present statement instead identifies a direct invariance of the Boolean edge-shell Turán problem under arbitrary positive vertex multiplicities and uses it to cover all complete multipartite graphs, including non-edge-transitive choices of part sizes.

## Limitations
The theorem concerns the specific weight-two Boolean support encoded by a graph. It does not establish an equality between the Turán extremum and the cubical chromatic number for every graph, and it does not classify all nonsymmetric extremizers of a blow-up. The literature comparison leaves a residual possibility that an equivalent blow-up observation occurs under different finite-group or cut-polytope terminology.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first public 2003-12-10.
2. R. Šámal, *Cubical coloring — fractional covering by cuts and semidefinite programming*, arXiv:0911.2589, first public 2009-11-13; Discrete Mathematics & Theoretical Computer Science 17:2 (2015).
