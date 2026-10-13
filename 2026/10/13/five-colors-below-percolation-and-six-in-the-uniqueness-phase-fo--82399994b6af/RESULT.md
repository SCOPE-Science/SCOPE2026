# Five colors below percolation and six in the uniqueness phase for planar amenable quotients
## Finding

Let \(G\) be a connected countable locally finite transitive unimodular amenable planar graph in the framework of Hsu--Sium--Thornton. If a combinatorial embedding is fixed, use their convention that the automorphism group consists of orientation-preserving automorphisms, and assume the resulting action is transitive and unimodular.

For Bernoulli bond percolation with parameter \(p\), let \(G_p\) be the percolation subgraph and let
\[
\widetilde G_p
\]
be the graph obtained by contracting each connected component of \(G_p\) to one vertex.

If every percolation component is finite almost surely, then
\[
\boxed{\chi_{\mathrm{fiid}}(\widetilde G_p)\le5.}
\]

If there is almost surely exactly one infinite percolation component, then
\[
\boxed{\chi_{\mathrm{fiid}}(\widetilde G_p)\le6.}
\]

Consequently,
\[
p<p_c(G)\Longrightarrow\chi_{\mathrm{fiid}}(\widetilde G_p)\le5,
\]
and
\[
p>p_u(G)\Longrightarrow\chi_{\mathrm{fiid}}(\widetilde G_p)\le6.
\]

These bounds improve the source's general amenable bound \(\chi_{\mathrm{fiid}}(\widetilde G_p)\le7\) whenever planarity and the corresponding finite- or unique-infinite-cluster regime are available.

## Assumptions and scope

A factor-of-iid coloring of \(\widetilde G_p\) means, as in the source, an automorphism-equivariant factor map on iid labels of \(G\) which is constant on the \(G_p\)-components and assigns different colors to adjacent quotient components.

The Bernoulli graphing \(\mathcal B(G)\) converts such equivariant factors into measurable labellings. When all \(G_p\)-components are finite, the source forms
\[
\mathcal B(\widetilde G_p)=\mathcal B(G)/E_p,
\]
where \(E_p\) is the finite-cluster connectedness relation. In the unique-infinite-cluster case, the source first restricts to vertices lying in finite percolation components and applies the same quotient construction there.

The result does not assume that the critical and uniqueness thresholds coincide. It makes no assertion in a parameter regime where infinitely many infinite clusters occur.

## Proof

### Finite-cluster regime

Assume every connected component of \(G_p\) is finite almost surely.

Because \(G\) is amenable, Hsu--Sium--Thornton's Lemma 3.7 gives that the Bernoulli graphing \(\mathcal B(G)\) is hyperfinite. The equivalence relation \(E_p\) has finite classes and is therefore smooth on the conull domain used by the source. Their quotient argument shows that hyperfiniteness passes to
\[
\mathcal B(\widetilde G_p).
\]

Proposition 3.5 shows that this quotient graphing preserves the reweighted probability measure \(\widetilde\mu\), so it is pmp.

The source also observes that if \(G\) is planar, then
\[
\mathcal B(\widetilde G_p)
\]
is Borel planar. Local finiteness is preserved here: a quotient vertex represents a finite connected set of vertices of the locally finite graph \(G\), and hence has only finitely many incident quotient edges.

Therefore \(\mathcal B(\widetilde G_p)\) satisfies every hypothesis of the source's Theorem 6.4. It has a measurable proper \(5\)-coloring.

Corollary 3.6 identifies measurable chromatic number of the quotient graphing with factor-of-iid chromatic number of the percolation quotient. Hence
\[
\chi_{\mathrm{fiid}}(\widetilde G_p)\le5.
\]

Since \(p<p_c(G)\) implies that all percolation components are finite almost surely, the subcritical bound follows.

### Unique-infinite-cluster regime

Now assume that \(G_p\) has exactly one infinite component almost surely.

Following Definition 3.4 of the source, first restrict the Bernoulli graphing to vertices whose \(G_p\)-components are finite and quotient by the finite-component relation. Restricting a hyperfinite graphing remains hyperfinite, and quotienting by the finite smooth relation preserves hyperfiniteness. Proposition 3.5 supplies the pmp structure. Planarity and local finiteness are inherited exactly as in the finite-cluster case.

Theorem 6.4 therefore gives a measurable proper \(5\)-coloring of this finite-component quotient. Proposition 3.5(3) transfers it to an equivariant partial factor-of-iid \(5\)-coloring of \(G\) whose domain contains every finite \(G_p\)-component and which is constant on each such component.

Assign a new color, say \(5\), to every vertex belonging to the unique infinite \(G_p\)-component. Membership in an infinite percolation component is measurable and automorphism-invariant: in a locally finite graph it is the intersection, over all radii \(r\), of the events that the component reaches graph distance at least \(r\). Thus this extension is again an equivariant measurable factor.

After contraction, all finite-component vertices use colors \(0,1,2,3,4\), while the unique infinite-component vertex uses color \(5\). Edges among finite quotient vertices are properly colored by construction, and every edge incident to the infinite quotient vertex has different endpoint colors. Hence
\[
\chi_{\mathrm{fiid}}(\widetilde G_p)\le6.
\]

By definition of \(p_u(G)\), for \(p>p_u(G)\) there is almost surely a unique infinite cluster, yielding the stated uniqueness-phase bound.

## Verification

The primary source was inspected at the definitions of factor-of-iid processes and transitive unimodular amenable graphs; Definition 3.4 of the percolation quotient graphing; Proposition 3.5 and Corollary 3.6 giving the quotient labelling correspondence; Lemma 3.7 giving hyperfiniteness from amenability; the observation that planar base graphs give Borel-planar quotient graphings; and Theorem 6.4 giving measurable \(5\)-colorability of hyperfinite locally finite pmp planar graphs.

The only additional step is the explicit sixth-color extension in the unique-infinite-cluster case. It uses no probabilistic estimate: the unique infinite cluster is an invariant measurable set, and a color unused on all finite components separates it from every adjacent quotient component.

No finite computation or experimental evidence is used.

## Relationship to prior work

Hsu, Sium, and Thornton prove two ingredients separately: a general measurable \(5\)-color theorem for hyperfinite pmp planar graphs, and the correspondence between measurable colorings of percolation quotient graphings and factor-of-iid colorings. They state the square-grid consequence and, earlier, a general amenable \(7\)-color bound.

The source does not state the general planar amenable consequences proved here. In particular, it does not record the \(5\)-color factor-of-iid bound for every finite-cluster planar amenable quotient or the \(6\)-color extension in the unique-infinite-cluster regime.

Targeted searches for these formulations under factor-of-iid, percolation quotient, amenable planar graph, subcritical regime, uniqueness phase, and hyperfinite pmp coloring terminology found no equivalent published statement.

## Limitations

The theorem is an upper-bound result. It does not claim that either \(5\) or \(6\) is sharp for any graph beyond examples already studied in the literature.

The \(6\)-color argument requires uniqueness of the infinite percolation component. It does not address phases with infinitely many infinite clusters.

The result uses the transitive unimodular factor-of-iid framework of the source and does not claim an extension to arbitrary nontransitive random rooted graphs.

## References

[1] Justin Hsu, Daniel Sium, and Riley Thornton, “FIID Coloring Random Maps,” arXiv:2609.33890v1, first posted 27 September 2026.

[2] Clinton T. Conley and Benjamin D. Miller, “A bound on measurable chromatic numbers of locally finite Borel graphs,” *Mathematical Research Letters* 23 (2016), 1633–1644.

[3] Luke Postle and Robin Thomas, “Five-list-coloring graphs on surfaces: the many faces far-apart generalization of Thomassen's theorem,” arXiv:2108.12880.
