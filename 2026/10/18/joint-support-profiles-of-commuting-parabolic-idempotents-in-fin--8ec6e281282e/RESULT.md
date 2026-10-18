# Joint support profiles of commuting parabolic idempotents in finite Coxeter monoids

## Finding

Let \((W,S)\) be a finite Coxeter system, \(\Gamma\) its (unlabeled) Coxeter graph, and \(H_0(W)\) its 0-Hecke **monoid** (not the full 0-Hecke algebra). For each \(I\subseteq S\), let \(e_I\) be the longest parabolic 0-Hecke element, with \(e_\varnothing=1\). Every monoid idempotent has this form, uniquely. Define its *parabolic support size* \(\sigma(e_I)=|I|\); this is not the cardinality of its image in a transformation representation. For commuting idempotents, \(e_Ie_J=e_{I\cup J}\). The complete triple support-size enumerator is
\[
\mathcal C_\Gamma(u,v,w)=\sum_{\substack{I,J\subseteq S\\e_Ie_J=e_Je_I}}
 u^{|I|}v^{|J|}w^{|I\cup J|}
 =\sum_{U\subseteq S}w^{|U|}\prod_{C\in\pi_0(\Gamma[U])}
 \left(u^{|C|}(1+v)^{|C|}+v^{|C|}(1+u)^{|C|}-(uv)^{|C|}\right).
\]
Here \(\pi_0(\Gamma[U])\) is the set of vertex sets of connected components of the induced subgraph; the empty product equals one. Thus each coefficient counts ordered commuting idempotent pairs by the supports of both factors and of their product, uniformly across all finite Coxeter types.

For type \(A_m\), equivalently a path with \(m\) vertices, put
\[
Q(x;u,v,w)=\frac{xuw(1+v)}{1-xuw(1+v)}
+\frac{xvw(1+u)}{1-xvw(1+u)}
-\frac{xuvw}{1-xuvw}.
\]
Writing \(\mathcal C_m=\mathcal C_{A_m}\), the following is an identity of formal power series:
\[
\boxed{\sum_{m\ge0}\mathcal C_m(u,v,w)x^m=
\frac{1+Q(x;u,v,w)}{1-x-xQ(x;u,v,w)}.}
\]
In particular, the total number \(c_m=\mathcal C_m(1,1,1)\) obeys \(c_0=1\), \(c_1=4\), and \(c_m=4c_{m-1}-2c_{m-2}\) for \(m\ge2\). Equivalently,
\[
 c_m=\frac{(2+\sqrt2)^{m+1}-(2-\sqrt2)^{m+1}}{2\sqrt2}.
\]
The first values for \(m=0,\ldots,8\) are \(1,4,14,48,164,560,1912,6528,22288\). The proportion among all \(4^m\) ordered idempotent pairs is exponentially decreasing. For **any connected** finite Coxeter graph on \(m\) vertices, the number of commuting pairs with \(I\cup J=S\) is exactly \(2^{m+1}-1\).

## Assumptions and scope

All finite Coxeter systems, including reducible types, and the finite 0-Hecke **monoid** with idempotent generators and Coxeter braid relations are included. The parabolic-idempotent parametrization and the connected-component commutation criterion are established prior results (Sentinelli 2018, Propositions 3.3–3.5; longest-parabolic classification also cited by Berenstein–Greenstein–Li, Proposition 2.11). This finding makes a quantitative assertion beyond those premises. Coxeter edges are present precisely when the Coxeter generators do not commute; their labels do not enter the resulting support-size polynomial. All variables are formal indeterminates. Type \(A_0\) denotes the trivial system.

## Proof

**Known criterion and product identification.** For connected \(I,J\subseteq S\), Sentinelli's Proposition 3.3 says their parabolic projections commute exactly if the two subsets are nonadjacent or one contains the other. Proposition 3.4 factors projections across connected components, and Proposition 3.5 proves that the factor projections commute pairwise exactly when the originals commute. These facts, applied to the faithful 0-Hecke monoid projection representation in his Section 4, yield the following restatement: \(e_I,e_J\) commute if and only if every connected component \(C\) of the induced graph on \(I\cup J\) satisfies \(C\subseteq I\) or \(C\subseteq J\). For completeness, if an induced component contains a vertex exclusive to each subset, a path between them inside the union crosses connected \(I\)- and \(J\)-subcomponents that are neither orthogonal nor nested; the cited propositions exclude commutativity. Conversely, if an entire union-component lies in one subset, its longest parabolic idempotent absorbs the other subset's parabolic idempotent on both sides, and components of the union pairwise commute because there are no Coxeter edges between them. The product is therefore the longest parabolic idempotent on the union, namely \(e_{I\cup J}\). The graph criterion is **not claimed as new**.

**Sum over the union.** Fix \(U=I\cup J\). Each vertex in \(U\) belongs to at least one of \(I,J\). Within an induced connected component \(C\subseteq U\), the criterion permits two families of assignments: all \(|C|\) vertices belong to \(I\) (with arbitrary membership in \(J\)), of weight \(u^{|C|}(1+v)^{|C|}\); or all belong to \(J\) (with arbitrary membership in \(I\)), of weight \(v^{|C|}(1+u)^{|C|}\). Both families include the unique assignment where every vertex belongs to both, whose weight \((uv)^{|C|}\) must be subtracted once. Components are independent. Each union vertex contributes one factor \(w\), proving the graph polynomial identity, with empty union contributing one.

**Path rational series.** On a path, the vertices of a fixed nonempty induced connected component form one consecutive run. Its length-\(r\) weight including the factor \(w\) is
\[
 \bigl(uw(1+v)\bigr)^r+\bigl(vw(1+u)\bigr)^r-(uvw)^r.
\]
Summing over all \(r\ge1\) gives \(Q(x;u,v,w)\). Every path configuration is uniquely a string of vacant vertices (weight \(x\)) and nonempty occupied runs (weight generating series \(Q\)), with at least one vacant vertex between successive runs. Allowing arbitrary initial/trailing vacant vertices yields \((1+Q)/(1-x-xQ)\) by a geometric series. When \(u=v=w=1\), it simplifies exactly to \(1/(1-4x+2x^2)\). Coefficient comparison proves the recurrence, and the quadratic characteristic equation gives the displayed closed form. The full-union formula for connected graphs is the single-component factor at \(u=v=1\), namely \(2^{m+1}-1\).

## Verification

The accompanying `checker.py` independently constructs actions of the parabolic 0-Hecke idempotents by repeated sorting on permutation groups of degree \(2\) through \(9\), checks all ordered support pairs against the graph criterion, and compares their three-dimensional coefficient distributions with a distinct three-state transfer recurrence. It additionally checks equality as maps of **every** permutation for degrees \(2\) through \(6\), including product equality with the union idempotent. A separate signed-permutation action of the type \(B_n\) 0-Hecke monoid verifies the criterion and union product on every signed permutation for \(n=2,3,4\). Finally, a direct induced-component polynomial sum is compared with a path transfer computation up to seven vertices and with direct star-graph pair enumeration up to seven vertices. The actual run prints `FINAL_ALL_CHECKS_PASSED`.

## Relationship to prior work

Sentinelli, *Artin group injection in the Hecke algebra for right-angled groups* (arXiv:1801.04233, 2018), Propositions 3.3–3.5 and Theorem 3.7, already establishes the commutation criteria and faithful projection realization; these are premises rather than novel results. His *Special idempotents and projections* (arXiv:2008.03065, Remark 4.17) also explicitly discusses the associated noncommuting graph. The 2020 paper *Right-angled Coxeter groups, universal graphs, and Eulerian polynomials* studies that graph, but full text was not accessible in the present comparison; its accessible abstract describes universality and Eulerian representations rather than a complete three-support enumeration. Berenstein, Greenstein, and Li, *Artin monoids, their homomorphisms and twins* (arXiv:2606.26776, 2026), discusses longest parabolic idempotents and their commutation in homomorphism constructions. The additional result here is the uniform **weighted counting polynomial** and the type-A triple-profile rational series, not an extension of the known zero/nonzero commutation criterion. Search coverage and residual risks are recorded separately in the review metadata.

## Limitations

No independent peer review has been performed. The result does not count *all* commuting pairs of elements in the 0-Hecke monoid, only ordered **idempotent** pairs. Its support size \(|I|\) is the rank of the associated standard parabolic generating set, not the Coxeter word length nor the transformation-image rank. A pre-existing equivalent weighted graph enumeration outside the inspected literature cannot be excluded, particularly in unindexed presentations of the same noncommuting graph. The 2020 Sentinelli primary full text was not accessible; this is a material originality risk, not evidence of absence. The closed path formula is an exact consequence of the cited commutation criterion plus the new component-weight enumeration, and no broader representation-theoretic implication is asserted.

## References

1. P. Sentinelli, *Artin group injection in the Hecke algebra for right-angled groups*, arXiv:1801.04233 (first preprint 2018-01-12), particularly Section 3, Propositions 3.3–3.5 and Theorem 3.7. https://arxiv.org/pdf/1801.04233
2. P. Sentinelli, *Special idempotents and projections*, arXiv:2008.03065 (first preprint 2020-08-07), Remark 4.17. https://arxiv.org/pdf/2008.03065
3. P. Sentinelli, *Right-angled Coxeter groups, universal graphs, and Eulerian polynomials*, European Journal of Combinatorics 84 (2020), 103040, doi:10.1016/j.ejc.2019.103040 (abstract inspected; full text inaccessible).
4. A. Berenstein, J. Greenstein and J. Li, *Artin monoids, their homomorphisms and twins*, arXiv:2606.26776 (2026), Proposition 2.11 and Example 3.32. https://arxiv.org/pdf/2606.26776
