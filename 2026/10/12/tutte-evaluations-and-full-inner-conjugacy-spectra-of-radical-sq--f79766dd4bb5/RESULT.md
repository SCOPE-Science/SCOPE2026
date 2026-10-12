# Tutte evaluations and full inner-conjugacy spectra of radical-square-zero quiver algebras

## Finding

Let \(q\) be any prime power and \(Q\) a finite loopless quiver with nonempty vertex set \(V\), arrow multiset \(E\), and underlying undirected multigraph \(G\). Put \(n=|V|\), \(m=|E|\), \(A=\mathbb F_qQ/J^2\), and \(U=A^\times\). Inner conjugation by \(U\) gives the exact class counts
\[
\#(A/U)=q^{c(G)}T_G(q+1,q),\qquad
\#(U/\operatorname{Inn}(U))=(q-1)^{c(G)}T_G(q,q),
\]
where \(c(G)\) is the number of connected components, including isolated vertices, and \(T_G\) is the usual Tutte polynomial of the multigraph.

More strongly, both *complete conjugacy-class-size multisets* are determined by \(G\), independently of every arrow orientation. For a vertex labeling \(d:V\to D\), with \(D=\mathbb F_q\) for the action on all elements and \(D=\mathbb F_q^\times\) for the action on units, let \(E_d\) comprise the edges with equal endpoint labels. For every \(S\subseteq E_d\), put \(r(S)=n-c(S)\), \(\beta(S)=|S|-r(S)\), where \(c(S)\) is the component number of the spanning multigraph \((V,S)\). Then precisely \((q-1)^{\beta(S)}\) distinct conjugacy classes have the specified \((d,S)\) data, and every one has size
\[
q^{m-|E_d|}(q-1)^{r(S)}.
\]
Taking the disjoint union of these classes over all \((d,S)\), with multiplicity, is the entire conjugacy-class-size multiset. The empty edge set and disconnected graphs are included.

Consequently, for every \(n\ge3\), a consistently directed \(n\)-cycle and an acyclic orientation of the same undirected cycle have identical complete conjugacy spectra (both for algebra elements and for units), although their radical-square-zero algebras have, respectively, infinite and finite global dimension. The conjugacy spectra therefore cannot detect finite global dimension, even in arbitrarily large dimensions.

## Assumptions and scope

The path algebra has orthogonal vertex idempotents \(e_v\), arrows \(a:u\to v\) with \(e_u a=a=a e_v\), and all products of two arrows vanish in \(A\). Parallel arrows and oriented cycles of length at least two are allowed, but loops are excluded. The underlying undirected graph retains every parallel edge.

For a spanning edge subset \(S\subseteq E\), define \(c(S)\) to include isolated vertices. We use the rank-subset definition
\[
T_G(X,Y)=\sum_{S\subseteq E}(X-1)^{c(S)-c(G)}(Y-1)^{|S|-n+c(S)}.
\]
All conjugations are by *units* of \(A\); the vertex labels are fixed individually under inner conjugation. The second class count is the ordinary group conjugacy-class number of \(U\), since restricting the same action to \(U\) is group conjugation.

## Proof

**1. Coordinate multiplication and conjugation.** Every element and every unit respectively have unique forms
\[
x=\sum_{v\in V}d_v e_v+\sum_{a\in E}\xi_a a,\qquad
\nu=\sum_{v\in V}\lambda_v e_v+\sum_{a\in E}\eta_a a,
\]
where \(d_v,\xi_a,\eta_a\in\mathbb F_q\) and all \(\lambda_v\in\mathbb F_q^\times\). Inverting \(\nu\) using \(J^2=0\) gives the following exact conjugation coordinate on each arrow \(a:u\to v\):
\[
(\nu x\nu^{-1})_a=\frac{\lambda_u}{\lambda_v}\xi_a+
\frac{\eta_a}{\lambda_v}(d_v-d_u).
\]
Every vertex coordinate \(d_v\) remains unchanged. In particular, when \(d_u\ne d_v\), the free coordinate \(\eta_a\) translates \(\xi_a\) arbitrarily, independently for each such arrow. All those cross-label coordinates can be normalized to zero; the translation orbit contains \(q^{m-|E_d|}\) choices.

**2. Classification of remaining coordinates.** If \(d_u=d_v\), translation vanishes and diagonal units act by \(\xi_a\mapsto(\lambda_u/\lambda_v)\xi_a\). Thus the nonzero support \(S\subseteq E_d\) is invariant. On \((\mathbb F_q^\times)^S\), the image of the vertex-scaling homomorphism
\[
(\mathbb F_q^\times)^V\longrightarrow (\mathbb F_q^\times)^S,
\qquad (\lambda_v)_v\longmapsto(\lambda_u/\lambda_v)_{a:u\to v}
\]
has order \((q-1)^{n-c(S)}\). Indeed, its kernel consists exactly of functions \(V\to\mathbb F_q^\times\) constant on every connected component of \((V,S)\); this proof works with arbitrary orientations and parallel edges. It follows by orbit-stabilizer that there are
\[
\frac{(q-1)^{|S|}}{(q-1)^{n-c(S)}}=(q-1)^{\beta(S)}
\]
orbits of this support, each with \((q-1)^{r(S)}\) points. Together with the independent cross-label translations, every full conjugacy class with data \((d,S)\) has size \(q^{m-|E_d|}(q-1)^{r(S)}\). Support and vertex labels are invariant, and the scaling calculation classifies the remaining freedom, proving exhaustion and disjointness.

**3. Sum the conjugacy classes.** Sum first over vertex labels and supports and then interchange the two finite sums. For each fixed \(S\subseteq E\), the allowable labelings \(d\) are exactly those constant on every component of \((V,S)\). Their number is \(q^{c(S)}\) for all elements and \((q-1)^{c(S)}\) for units. Consequently,
\[
\#(A/U)=\sum_{S\subseteq E}q^{c(S)}(q-1)^{\beta(S)},\qquad
\#(U/\operatorname{Inn}(U))=
\sum_{S\subseteq E}(q-1)^{c(S)+\beta(S)}.
\]
Substitute the displayed definition of \(T_G\): these are respectively \(q^{c(G)}T_G(q+1,q)\) and \((q-1)^{c(G)}T_G(q,q)\), as stated. No hypothesis on characteristic was used.

**4. Homological separation.** For the quiver formed by orienting every edge of a cycle \(C_n\) coherently, each simple module has a periodic nonzero sequence of syzygies, so the radical-square-zero algebra has infinite global dimension. For an acyclic orientation of \(C_n\), syzygies of simples follow strictly directed paths; since such paths have bounded length, all simples have finite projective dimension and so does the algebra. The two quivers have the same undirected \(C_n\), hence identical full class-size multisets by steps 1–3. Their algebra dimensions are \(2n\), with \(n\) arbitrary.

## Verification

The standalone `verify.py` constructs the radical-square-zero multiplication and conjugation action directly. It enumerates *all* units and all algebra elements for five small quivers over \(\mathbb F_2\) and \(\mathbb F_3\), including two parallel arrows, a length-two path, and both cyclic and transitive orientations of a triangle. Independently it enumerates supports, graph components, predicted sizes, and the two Tutte subset evaluations. It also runs the one- and two-arrow cases over \(\mathbb F_4\). All equality assertions pass and the program prints `VERIFY_OK`.

For the two triangle orientations over \(\mathbb F_3\), the unit conjugacy-size spectrum (size, multiplicity) is \((1,2),(2,6),(4,10),(9,6),(18,6)\), totaling \(30\) classes; the algebra-element spectrum is \((1,3),(2,9),(4,15),(9,18),(18,18),(27,6)\), totaling \(69\) classes. Their equality is checked by independently computing the two actions, not only by evaluating the formulas.

Finite enumeration checks cases, not the arbitrary-prime-power theorem. The symbolic classification in the proof supplies the general argument.

## Relationship to prior work

Nasr-Isfahani's 2016 paper defines the same radical-square-zero quiver algebras and investigates singular equivalence induced by graph operations; Chen's 2011 work investigates their singularity categories, and Adachi's 2014 paper studies separated-quiver criteria for representation finiteness and \(\tau\)-rigid finiteness. Those results concern homological or module-theoretic invariants rather than the inner-conjugacy-class-size multiset calculated here.

The support stratification uses the familiar spanning-forest incidence map of a graph, and the final evaluation uses the standard subset expansion for the Tutte polynomial. Neither ingredient is claimed to be new. The claim concerns their exact combination into the complete finite-field inner-conjugacy classification of both algebra elements and units and the resulting unbounded homological blindness. A previously studied commuting-pair statistic for the same algebra class measures a different action and does not on its own specify the class-size spectrum.

## Limitations

The result concerns *split basic* algebras explicitly presented as \(\mathbb F_qQ/J^2\), not arbitrary nonsplit algebras with radical square zero, arbitrary field extensions at vertices, or actions by all algebra automorphisms. The class-size multiset need not determine the entire group structure or its character table. Equality of spectra for different orientations is not an assertion of algebra isomorphism or derived equivalence. An equivalent graph-gauge or semidirect-product formulation might already be known under different terminology; publication priority is not independently certified.

## References

1. A. R. Nasr-Isfahani, *Singular equivalence of finite dimensional algebras with radical square zero*, arXiv:1603.04191v1, first public 14 March 2016; *J. Pure Appl. Algebra* 220 (2016), 3948–3965. Primary MSC 16E35. https://arxiv.org/abs/1603.04191
2. X.-W. Chen, *The singularity category of an algebra with radical square zero*, arXiv:1104.4006v1, first public 20 April 2011; *Documenta Math.* 16 (2011), 921–936. https://arxiv.org/abs/1104.4006
3. T. Adachi, *Characterizing tau-rigid-finite algebras with radical square zero*, arXiv:1401.1438v1, first public 7 January 2014. https://arxiv.org/abs/1401.1438
4. W. T. Tutte, *A contribution to the theory of chromatic polynomials*, Canadian J. Math. 6 (1954), 80–91. (The rank-subset expression is used as the definition here.)
