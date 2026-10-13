# Quantifier-rigid morphisms of finite functional monadic Gödel powers

## Finding

Let \(C_k=\{0=c_0<c_1<\cdots<c_{k-1}=1\}\) be the bounded \(k\)-element Heyting chain. For \(k\ge2\) and \(m\ge1\), let
\[
\mathcal G_{k,m}=(C_k^m,\wedge,\vee,\to,0,1,\forall,\exists),
\qquad
\forall x=\overline{\min_i x_i},\quad
\exists x=\overline{\max_i x_i}.
\]
The lattice and implication operations are coordinatewise, and bars denote constant vectors.

**Theorem (complete morphism classification).** Fix \(k,\ell\ge2\) and \(m,n\ge1\). Every bounded Heyting-algebra homomorphism \(h:C_k^m\to C_\ell^n\) that preserves **either one** of the two displayed global quantifiers automatically preserves both. Such a map exists precisely when \(n\ge m\), and it has the following unique form:
\[
 h(x)_j=\phi(x_{\sigma(j)})\quad(1\le j\le n),
\]
where \(\sigma:[n]\twoheadrightarrow[m]\) is a surjection and \(\phi:C_k\to C_\ell\) is a bounded Heyting-chain homomorphism. Conversely, every such pair defines a morphism. Composition corresponds to composition in each factor, giving the categorical factorization of this family into finite nonempty sets with surjective maps, contravariantly, and finite bounded Heyting chains, covariantly.

Write \(S(n,m)\) for the Stirling number of the second kind. The exact homomorphism count is
\[
 \left|\operatorname{Hom}(\mathcal G_{k,m},\mathcal G_{\ell,n})\right|
 =m!S(n,m)\sum_{t=0}^{\min(k-2,\ell-2)}\binom{\ell-2}{t},
\]
with \(S(n,m)=0\) when \(n<m\). More finely, if \(P_{k,m}^{\ell,n}(z)\) counts homomorphisms by cardinality of their set-theoretic image, then
\[
 P_{k,m}^{\ell,n}(z)
 =m!S(n,m)\sum_{t=0}^{\min(k-2,\ell-2)}
 \binom{\ell-2}{t}z^{(t+2)^m}.
\]

There are exactly
\[
 m!S(n,m)\binom{\ell-2}{k-2}
\]
injective homomorphisms when \(k\le\ell\), and none otherwise. A surjective homomorphism onto \(\mathcal G_{\ell,n}\) exists exactly when \(m=n\) and \(k\ge\ell\), in which case there are exactly \(n!\) of them.

In particular,
\[
 \operatorname{End}(\mathcal G_{k,n})\cong
 S_n\times\operatorname{End}(C_k),\qquad
 |\operatorname{End}(\mathcal G_{k,n})|=n!2^{k-2}.
\]
Here \(S_n\) is the symmetric group. Exactly \(k-1\) endomorphisms are idempotent, one with each of the image sizes \((2)^n,(3)^n,\ldots,(k)^n\). The invertible endomorphisms are exactly the \(n!\) coordinate permutations.

## Assumptions and scope

All algebras are finite and nontrivial. Morphisms preserve the named bounds, meet, join, Heyting implication, and (when specified) at least one quantifier. Implication on a chain is \(a\to b=1\) for \(a\le b\), and \(a\to b=b\) otherwise. The quantifiers always range over **all** coordinates of a nonempty full Cartesian power, not over independently selected clusters or an arbitrary monadic Gödel algebra. An image is the ordinary set-theoretic range of a morphism; injective and surjective refer to that range. For all formulas \(k,\ell\ge2\), \(m,n\ge1\); no empty products are tacitly allowed.

## Proof

**Step 1: coordinate factorization before adding quantifiers.** For a bounded lattice homomorphism \(u:C_k^m\to C_\ell\), let \(e_i\) be the vector with value \(1\) at coordinate \(i\) and \(0\) elsewhere. They satisfy \(\bigvee_i e_i=1\) and \(e_i\wedge e_j=0\) for \(i\ne j\). Therefore the \(u(e_i)\) have maximum \(1\) and pairwise minimum \(0\) in a chain. Exactly one index \(s\) has \(u(e_s)=1\); all others have image \(0\). For any vector \(x\), decompose it as \(\bigvee_i(e_i\wedge\overline{x_i})\). Applying \(u\) leaves just the \(s\)-summand, equal to \(u(\overline{x_s})\). Hence \(u(x)=\phi(x_s)\), with \(\phi(c)=u(\overline c)\). This \(\phi\) is a bounded Heyting-chain homomorphism when \(u\) preserves implication. Both \(s\) and \(\phi\) are unique. Applying this argument to every target coordinate of \(h\) yields indices \(\sigma(j)\) and potentially different chain homomorphisms \(\phi_j\).

**Step 2: one quantifier enforces global uniformity.** Every constant source vector \(\overline c\) is fixed by both quantifiers. If \(h\) commutes with \(\exists\), then \(h(\overline c)\) is fixed by target \(\exists\), so its coordinates \(\phi_j(c)\) are all equal. Thus all \(\phi_j\) coincide with one \(\phi\). Fix source coordinate \(i\) and take the test vector having \(1\) at \(i\) and \(0\) elsewhere. Its existential quantification is the constant \(1\). Since \(\phi(0)=0\) and \(\phi(1)=1\), preservation forces \(i\) to occur in the image of \(\sigma\). This works for every \(i\), hence \(\sigma\) is surjective. If only \(\forall\) is assumed preserved, use constants as before and then the test vector having \(0\) at \(i\) and \(1\) elsewhere; the same conclusions follow. Conversely, a common order-preserving \(\phi\) and a surjective \(\sigma\) commute with both the minimum and maximum over all source coordinates, since each source coordinate appears among the selected output coordinates. This proves the classification and the one-quantifier redundancy assertion.

**Step 3: classify the chain morphisms.** A bounded Heyting-chain homomorphism \(\phi:C_k\to C_\ell\) preserves order. For any \(x>y\), implication preservation requires
\[
 \phi(y)=\phi(x\to y)=\phi(x)\to\phi(y).
\]
If \(\phi(y)<1\), this forces \(\phi(x)>\phi(y)\). Taking \(y=0\) shows every positive input has positive image. Thus there is a unique integer \(t\) with \(0\le t\le\min(k-2,\ell-2)\) such that the first \(t\) proper nonzero input values have strictly increasing images chosen among the \(\ell-2\) proper nonzero target values, while all remaining proper input values map to \(1\). Conversely, each such choice preserves meet, join, bounds, and implication, including pairs collapsed to \(1\). There are exactly \(\binom{\ell-2}{t}\) choices of rank \(t+2\), yielding the binomial sum.

**Step 4: counts, ranks, and composition.** There are exactly \(m!S(n,m)\) surjections \([n]\twoheadrightarrow[m]\), independently of the chain map. Once \(\sigma\) is surjective, the image of \(h\) is isomorphic, as a finite monadic Gödel algebra, to the full \(m\)-fold power of \(\phi[C_k]\). Thus its size is \((t+2)^m\), and both enumerations follow. Two such morphisms compose via the surjection composite and the chain-map composite. The composite remains surjective on the indexing sets. An embedding requires that \(\phi\) be injective, forcing \(t=k-2\); it exists exactly when \(k\le\ell\) and has the stated binomial count. Surjectivity of \(h\) forces \(\sigma\) to be bijective, hence \(m=n\), and \(\phi\) to be surjective. The latter is possible exactly when \(k\ge\ell\) and has one choice, namely the map taking the first \(\ell-2\) positive levels in order onto the proper target levels and sending all remaining positive levels to \(1\).

**Step 5: the endomorphism monoid and its idempotents.** When the source and target coincide, every indexing surjection is a permutation, and every chain endomorphism is specified by an arbitrary subset of the \(k-2\) proper target levels. Hence the direct-product description and order \(n!2^{k-2}\). For a chain endomorphism \(\phi:C_k\to C_k\), every value is mapped upward or left fixed. If a proper value \(c\) is strictly raised to a proper value \(d\), strict growth below \(1\) gives \(\phi(d)>d\), so \(\phi\) is not idempotent. The idempotents are therefore precisely the \(k-1\) threshold retractions fixing an initial segment of proper positive levels and mapping every higher level to \(1\). A permutation is idempotent only when it is the identity, giving the claimed complete idempotent census and image sizes. An automorphism must use the identity chain map, leaving exactly all coordinate permutations.

As an illustration, \(\mathcal G_{4,2}\) has exactly \(12\) morphisms into \(\mathcal G_{3,3}\): six have image size \(4\), and six have image size \(9\); none is surjective onto the \(27\)-element target. The endomorphism monoid of \(\mathcal G_{5,3}\) has \(48\) elements and four idempotents with image sizes \(8,27,64,125\).

## Verification

The standalone `verify_morphisms.py` uses independent truth-table semantics, rather than presupposing the morphism factorization. It enumerates all bounded Heyting-chain maps for \(2\le k,\ell\le6\), enumerates **all** bounded Heyting maps from specified small direct powers into one chain by testing meet, join, bounds and implication on all input pairs, then forms all target-coordinate tuples and checks both global quantifiers on every input. It independently checks the predicted total, image-cardinality distribution, embeddings, and surjections. Composition tests compare concrete tuple evaluations against the product description. The successful replay prints:

`VERIFY_OK chain_parameter_pairs 25 coordinate_hom_cases 11 enumerated_full_homomorphisms 40 composition_checks 222286`

Run using `python3 verify_morphisms.py` with only Python's standard library. These are finite sanity checks, not a substitute for the universal proof.

## Relationship to prior work

Castaño, Cimadamore, Díaz Varela, and Rueda (2020) establish duality for monadic Gödel algebras, prove structural properties of global quantifiers, and characterize congruences and free objects. The general duality supplies the natural categorical background. The present calculation specializes to full finite functional powers and gives direct coordinate formulas, an explicit Stirling-binomial hom-set census, quantifier redundancy, image-rank counts, and an idempotent census; these exact conclusions were not identified in the inspected source.

Cintula, Metcalfe, and Tokuda (2023) place functional monadic lattices with global meet and join in the broader setting of one-variable first-order logics. Their functional construction confirms that the objects under study form a natural semantics, but does not state this morphism census.

Aguzzoli and Mordonini (2024 conference version, published 2025) study homomorphism counting for **ordinary** finite Gödel algebras. The accessible abstract does not specify morphisms preserving global quantifiers. Its full text was not obtained, so a specialized implicit antecedent cannot be ruled out. By contrast, the ordinary Heyting-power hom-set count allows independently selected source coordinates and chain maps for every target coordinate; the two global quantifiers force one common chain map and make the source-index assignment surjective.

## Limitations

The result applies only to finite full powers of a single nontrivial Heyting chain with **global** infimum/supremum quantifiers. It does not classify morphisms of arbitrary finite monadic Gödel algebras, nonfull functional subalgebras, heterogeneous-coordinate products, or infinite powers. Published general duality may imply the classification indirectly; the novelty claim concerns this explicit complete specialized description and its exact enumerations, not the existence of duality or standard finite-surjection counts. A full historical audit has not been performed, and one closely related ordinary Gödel-homomorphism paper could be assessed only from accessible bibliographic and abstract material.

## References

1. Diego Castaño, Cecilia Cimadamore, José Patricio Díaz Varela, Laura Rueda, *An algebraic study of S5-modal Gödel logic*, arXiv:2006.10180v1 (public 2020-06-17), https://arxiv.org/pdf/2006.10180; Studia Logica 109 (2021), DOI:10.1007/s11225-020-09934-x.
2. Petr Cintula, George Metcalfe, Naomi Tokuda, *One-variable fragments of first-order logics*, arXiv:2310.15806v1 (public 2023-10-24), https://arxiv.org/html/2310.15806v1; Bulletin of Symbolic Logic 30 (2024).
3. Stefano Aguzzoli, Matteo Mordonini, *Counting homomorphisms between finite Gödel algebras*, IPMU 2024 conference / 2025 volume, DOI:10.1007/978-3-031-74000-8_30; accessible abstract: https://air.unimi.it/handle/2434/1166075.
