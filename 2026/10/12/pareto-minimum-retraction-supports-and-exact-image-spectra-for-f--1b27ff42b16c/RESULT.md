# Pareto-minimum retraction supports and exact image spectra for finite multimodal rectangular frames

## Finding

Fix integers \(r\ge 2\) and \(m\ge 1\). For each component label \(i\in[m]\), choose a vector \(\mathbf a_i=(a_{i1},\ldots,a_{ir})\) of positive integers. The finite frame \(X\) is the disjoint union of rectangles \(X_i=\prod_{t=1}^r[a_{it}]\). For each \(t\in[r]\), two points are \(R_t\)-related if they lie in the same component and agree in every coordinate other than \(t\). Each \(R_t\) is an equivalence relation, and these equivalences commute. Let \(\mathcal A(X)\) be the powerset Boolean algebra with the \(r\) named relational diamond operations.

Write \(\operatorname{Sur}(n,k)=k!\left\{\begin{smallmatrix}n\\ k\end{smallmatrix}\right\}\) for the number of surjections from an \(n\)-element set onto a \(k\)-element set, with value zero when \(k>n\). Put
\[
q_{ij}=\prod_{t=1}^r\operatorname{Sur}(a_{it},a_{jt}),\qquad
w_j=\prod_{t=1}^r a_{jt}.
\]

**Structural classification.** Every simultaneous bounded self-morphism of the \(r\) relational frames maps each entire source rectangle \(X_i\) onto a single rectangle \(X_{\phi(i)}\). Its restriction to \(X_i\) is the product of \(r\) independent coordinate surjections. Conversely, every such collection gives a bounded self-morphism. Hence the number of maps that send \(X_i\) onto \(X_j\) is exactly \(q_{ij}\).

**Complete image-rank polynomials.** The polynomials enumerating endomorphisms and idempotent endomorphisms of \(\mathcal A(X)\) by the cardinalities of their *algebraic* images are, respectively,
\[
E_X(z)=\sum_{\varnothing\ne J\subseteq[m]}\left[
 \sum_{L\subseteq J}(-1)^{|J|-|L|}
 \prod_{i=1}^m\left(\sum_{j\in L}q_{ij}\right)
 \right] z^{\,2^{\sum_{j\in J}w_j}}
\]
and
\[
I_X(z)=\sum_{\varnothing\ne J\subseteq[m]}
 \left[\prod_{i\notin J}\left(\sum_{j\in J}q_{ij}\right)\right]
 z^{\,2^{\sum_{j\in J}w_j}}.
\]
Here empty sums are zero and empty products are one. When different component supports have the same total number of worlds, their contributions combine into the same coefficient.

**Pareto-minimum support criterion.** Order distinct vectors \(\mathbf a_i\) coordinatewise and let \(\mathcal M\) be the set of minimal *vector types*, with \(c_\tau=|\{i:\mathbf a_i=\tau\}|\). A nonempty union of whole rectangles \(\bigcup_{j\in J}X_j\) is the exact image of a bounded idempotent self-map **if and only if** \(J\) contains at least one component of each type \(\tau\in\mathcal M\). Exactly the same component supports are attainable as images of unrestricted bounded endomorphisms. Their total number is
\[
\boxed{2^{\,m-\sum_{\tau\in\mathcal M}c_\tau}
\prod_{\tau\in\mathcal M}(2^{c_\tau}-1).}
\]
Consequently \(E_X\) and \(I_X\) have exactly the same sets of nonzero exponents. The criterion concerns *dual-frame image supports*; it does not equate different embedded retract subalgebras that arise from different retractions.

For a concrete two-modal example, take four labeled components of sizes \((1,2),(1,2),(2,1),(2,2)\). The first and third vector types are incomparable minima, and the other copy of \((1,2)\) may replace the first. There are six admissible supports. The algebra has \(2^{10}=1024\) elements, and the exact polynomials are
\[
\boxed{E_X(z)=64z^{16}+128z^{64}+64z^{256}+64z^{1024}},
\]
\[
\boxed{I_X(z)=16z^{16}+6z^{64}+4z^{256}+z^{1024}}.
\]
Thus this algebra has exactly \(320\) endomorphisms and \(27\) idempotents.

## Assumptions and scope

All sets are finite, every dimension \(a_{it}\) is positive, the number of named relations is at least two, and components carry *labels*. A different component with the same vector is still distinct. The two-modal case is the product-frame subclass of finite \(\mathsf{S5}^2\) frames, equivalently a subclass of finite two-dimensional diagonal-free cylindric set algebras. An arbitrary frame of commuting equivalence relations need not decompose into these thin rectangular products, so the theorem does not claim coverage of all such frames.

A bounded morphism is a function satisfying both forth and back for each named relation. Equivalently, for every world \(x\) and coordinate relation \(R_t\), it obeys \(f[R_t(x)]=R_t(f(x))\). Algebra homomorphisms are identified with bounded morphisms in the opposite direction through finite powerset duality; self-maps are in bijection under inverse image. The image of the inverse-image algebra homomorphism has \(2^{|f[X]|}\) elements.

## Proof

**1. Componentwise factorization.** Inside any rectangle, any two points can be connected by changing one coordinate at a time along the relations \(R_t\). The forth conditions therefore force the image of that connected component to remain in a single target component. For an output coordinate \(u\), changing any source coordinate \(t\ne u\) cannot change the output coordinate \(u\), by preservation of \(R_t\). By changing all coordinates other than \(u\) one at a time, the output coordinate \(u\) depends only on its corresponding source coordinate. Thus the restriction has a unique product form
\[
f_i(x_1,\ldots,x_r)=\bigl(g_{i1}(x_1),\ldots,g_{ir}(x_r)\bigr)
\]
inside its chosen target component. For each \(t\), the back condition at one source point requires the entire target \(R_t\)-class, obtained by varying the target \(t\)-coordinate, to be the image of the source \(R_t\)-class. This is precisely the surjectivity of \(g_{it}\). Conversely, coordinatewise surjections satisfy both forth and back. Their number is \(q_{ij}\), establishing the classification.

**2. Counting arbitrary images.** Each source component \(i\) independently chooses a target component \(j\) with weight \(q_{ij}\). Fix a putative image-component set \(J\). The number of all weighted assignments with targets restricted to a subset \(L\subseteq J\) equals \(\prod_i\sum_{j\in L}q_{ij}\). Inclusion–exclusion over missing target components counts assignments having image set *exactly* \(J\). Each chosen source rectangle surjects onto its target, so the world image has \(\sum_{j\in J}w_j\) points. Its dual Boolean image has the stated cardinality. This proves \(E_X\).

**3. Idempotents.** Let \(f^2=f\) and let \(J\) be its image-component set. An idempotent fixes every point of its image, and the factorization implies that the entire target rectangle \(X_j\) is in the image for each \(j\in J\). Hence \(f\) is the identity on every \(X_j\) with \(j\in J\). For each remaining component \(i\notin J\), it independently chooses a target \(j\in J\) and one of \(q_{ij}\) coordinatewise-surjective maps. All such choices are idempotent. Multiplication over omitted components gives \(I_X\).

**4. Pareto-minimum criterion.** A component of minimal vector type \(\tau\) can map only onto another component with exactly the same minimal type, because every target dimension must be no larger than the source dimension. Thus every unrestricted endomorphism image meets each class of minimal types. Conversely, every nonminimal vector dominates at least one minimal vector among the finite set of types. If \(J\) contains a representative of every minimal type, choose for every omitted component \(i\) a represented minimal type \(\tau\le\mathbf a_i\), map \(X_i\) coordinatewise-surjectively onto that selected component, and fix all components in \(J\) pointwise. This constructs a bounded idempotent with exactly the prescribed support. For each minimal type there are \(2^{c_\tau}-1\) nonempty choices of representatives, and every nonminimal component is independently in or out, giving the support count. The same-support and same-exponent conclusions follow.

## Verification

Run the self-contained standard-library checker with \(`python3 verify.py`\). It directly evaluates the bounded-morphism equalities for all functions on 19 small two-modal frames, independently tests direct powerset-algebra preservation of both diamonds on those cases, and checks the formulas and minimum-type criterion. It separately checks six three-modal frames and constructs all \(320\) distinct maps of the ten-world example from its proven coordinate-product normal form, rechecking every map against the original relational conditions. Output from the completed run was:

`VERIFY_OK 19 direct_shape_cases 23249 direct_function_tables 3658 bounded_maps 23249 direct_algebra_candidate_checks 5 larger_symbolic_support_checks example_320_endomorphisms_27_idempotents`

`ND_VERIFY_OK 6 three_modal_shapes 7022 direct_tables 28 bounded_maps`

`LARGE_EXAMPLE_OK 320 distinct_structural_maps_rechecked`

Direct function-table checks are exhaustive only for the enumerated small cases; the ten-world test is exhaustive relative to the separately proved normal form, not over all \(10^{10}\) raw functions. The general theorem rests on the proof, not on extrapolation from finite computation.

## Relationship to prior work

Bezhanishvili and Meadors (2023 preprint, later published) present two commuting modal operations and the associated finite duality, with the product bimodal system \(\mathsf{S5}^2\) explicitly connected to diagonal-free cylindric algebras. Their investigated invariants are local finiteness, depth, model properties, and translation of varieties. Their accessible full paper does not state these finite rectangular endomorphism and idempotent rank polynomials or the Pareto-minimum criterion. Standard Jónsson–Tarski duality, Stirling-number surjection counting, and the notion of product frames are prior tools, not originality claims.

Adams and Dziobiak (2007) investigate endomorphism monoids of *one*-modal monadic Boolean algebras. Their accessible abstract states an isomorphism reconstruction result, but the inaccessible full argument could contain relevant general techniques. The present structure has multiple independently named commuting modalities and has incomparable component dimension vectors. The contribution claimed here is their joint exact support and rank-spectrum enumeration, not an assertion that the factorization principles of rectangular products are new in isolation.

## Limitations

The result covers thin products of finite nonempty coordinate sets and disjoint unions thereof, not arbitrary finite commuting-equivalence frames with multiple points in a row–column intersection, arbitrary fusion frames, or infinite descriptive frames. Distinct image supports may have equal image cardinalities; the polynomial records multiplicity but does not reconstruct the entire endomorphism monoid. Search non-detection cannot certify absolute novelty. Independent mathematical audit has not been performed.

## References

1. G. Bezhanishvili and C. Meadors, *Local finiteness in varieties of MS4-algebras*, arXiv:2312.16754 (first posted 2023-12-28); *Journal of Symbolic Logic*, DOI 10.1017/jsl.2024.89. Full open-access text: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/local-finiteness-in-varieties-of-ms4algebras/AD07C4C9F67D51050DC0F23D33FA6177 .
2. M. E. Adams and W. Dziobiak, *Endomorphisms of monadic Boolean algebras*, *Algebra Universalis* **57** (2007), 131–142, DOI 10.1007/s00012-007-2028-y (abstract available; complete article not inspected).
3. B. Jónsson and A. Tarski, *Boolean algebras with operators*, *American Journal of Mathematics* (1952), DOI 10.2307/2372074 (duality foundations).
4. J. Harding, *Quantum monadic algebras*, *Journal of Physics A* **55** (2022), 394001 (background characterization of diagonal-free cylindric structures via commuting equivalence relations; only publicly indexed passages inspected).
