# Commutator-coordinate independence detects the graphic matroid

## Finding and scope

Let \(Q=(V,E)\) be a finite quiver with no oriented path of length two (no composable arrow pair, so loops are excluded). Isolated vertices and parallel arrows are allowed. In the path algebra \(A=\mathbb F_q Q\), over any finite field, sample \(X,Y\) independently and uniformly. Write \([X,Y]=\sum_{e\in E}C_e e\). For every \(T\subseteq E\), the labelled variables \((C_e)_{e\in T}\) are mutually independent **if and only if** \((V,T)\) is a forest. In particular, two distinct parallel arrows give a circuit of size two. This classifies the independence system as the graphic matroid of the underlying undirected multigraph. The statement is about the given arrow coordinates, not arbitrary choices of basis.

## Proof

Let \(z_v=(a_v,b_v)\) be the two independent uniform vertex coefficients of \(X,Y\), and \((x_e,y_e)\) their independent uniform arrow coefficient pairs. The path algebra has no products of two arrows. On \(e:u\to v\), its commutator coefficient is
\[
C_e=(a_u-a_v)y_e-(b_u-b_v)x_e.
\]
Vertex coefficients cancel. Conditional on the vertex labels, coefficients on different arrows are independent. A coefficient is zero deterministically if its two endpoint labels agree; otherwise it is uniform on \(\mathbb F_q\) by surjectivity of the displayed linear functional. The unconditional zero probability for any edge is \(p_0=q^{-1}(1+(q-1)q^{-2})\).

If \(T\) is a forest, the vertex labels correspond bijectively to a root label for every component and the oriented differences on its edges. Thus those differences are independent and uniform. Each edge coefficient uses just its own difference and arrow coefficient pair, so the coefficients are mutually independent, including the vacuous case \(T=\varnothing\).

Conversely, write \(r(F)=|V|-k(F)\), where \(k(F)\) counts the connected components of \((V,F)\) including isolated vertices. If all endpoints of edges in \(F\) are required to agree, the vertex labels are constant on its components, an event of probability \(q^{-2r(F)}\). For any \(T\), multiplying the conditional zero probabilities and expanding the equality indicators therefore yields
\[
\Pr(C_e=0\ \forall e\in T)-p_0^{|T|}
=q^{-|T|}\sum_{F\subseteq T}(q-1)^{|F|}
\big(q^{-2r(F)}-q^{-2|F|}\big).
\]
Every summand is nonnegative because \(r(F)\le |F|\). If \(T\) contains any cycle, taking \(F\) to be that cycle gives a strictly positive term. Thus independence fails, witnessed by just the all-zero event. This works for every finite field and also for a cycle of length two, because the two equality constraints for parallel arrows are redundant.

## Relation to existing formulas

The complete prescribed single-pair law is already available for arbitrary loopless radical-square-zero quotients in [Chromatic commutator length and Tutte fibers](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-chromatic-commutator-length-and-tutte-fibers-of-square-zero-quiv--b7fb936d5d53/RESULT.md); the present algebra is that quotient when there are no length-two paths. Neither the prescribed-fiber formula nor the ordinary graph partition-function expansion is a separate claim here. Joint zero probabilities on sets of edges can also be read as commuting probabilities on the corresponding subquivers; for simple graphs these relate to the known adjoint-rank formulas. What is isolated here is the uniform structural comparison to a product of the marginals: all forest subsets are independent in the full field-valued law, and every circuit forces strict failure of the product zero probability, with no cancellation. Independence refers to subsets of coordinates, not to the rank distribution of an inner derivation. Historical priority beyond the compared sources is not asserted.

## Verification

`python3 check_commutator_matroid.py` multiplies all element pairs in a single small quiver over \(\mathbb F_2\), which includes a parallel pair, a four-cycle, and an isolated vertex. For every arrow subset it checks factorization of the **entire** marginal law by integer arithmetic against a forest test by pruning leaves. It corroborates the general proof without replacing it.
