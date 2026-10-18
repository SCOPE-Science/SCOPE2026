# Symmetry-reduced bounded-morphism moduli of finite \(\mathsf{S5}\) frames

## Finding

Let \(P\) and \(Q\) be nonempty finite Kripke frames with **one equivalence accessibility relation** and no propositional valuation. Let \(N(P,Q)\) be the number of orbits of **globally surjective bounded morphisms** \(P\to Q\) under independent relabelings by \(\operatorname{Aut}(P)\times\operatorname{Aut}(Q)\). These are isomorphism classes of morphism diagrams with fixed source and target isomorphism types. The following describes the moduli space for all finite frames and counts it exactly.

Write the target equivalence blocks as \(B_1,\ldots,B_s\), of sizes \(b_j\ge1\). For every positive integer \(a\), write \(r_a\) for the number of source equivalence blocks of size \(a\), and define the finite profile set
\[
\Omega_a=\bigsqcup_{j=1}^{s}\Omega_{a,j},\qquad
\Omega_{a,j}=\{(j,u_1,\ldots,u_{b_j}):u_i\in\mathbb Z_{>0},\ \sum_i u_i=a\}.
\]
The target automorphism group \(H=\operatorname{Aut}(Q)\) acts on every \(\Omega_a\) by permuting target blocks of equal size and their points. The morphism moduli are in bijection with \(H\)-orbits of tuples \((M_a)_a\), where \(M_a\) is a multiset of exactly \(r_a\) profiles from \(\Omega_a\), subject to every target block index appearing in at least one profile.

For \(h\in H\), let \(\mathcal B(h)\) be its set of cycles on target block indices. Given \(S\subseteq\mathcal B(h)\), let \(\Omega_a(S)\) be the union of profile sets associated with the block indices in cycles belonging to \(S\). Let \(\mathcal O_{a,h,S}\) be the orbits of \(\langle h\rangle\) on \(\Omega_a(S)\). With \([z^r]\) denoting a coefficient, the exact answer is
\[
\boxed{N(P,Q)=\frac1{|H|}\sum_{h\in H}\ \sum_{S\subseteq\mathcal B(h)}
(-1)^{|\mathcal B(h)|-|S|}\prod_{a:r_a>0}
[z^{r_a}]\prod_{O\in\mathcal O_{a,h,S}}(1-z^{|O|})^{-1}.}
\]
Empty products have value one. When no source profile can reach a target block, the formula gives zero.

**Growth law.** Fix the target and a finite nonempty set \(A\) of permissible source-block sizes; let each multiplicity \(r_a\), for \(a\in A\), tend to infinity. Suppose every \(\Omega_a\) for \(a\in A\) is nonempty and every target block is reachable from at least one such \(a\). Put \(q_a=|\Omega_a|\), and let \(K\) be the kernel of the action of \(H\) on the disjoint union of these profile sets. Then \(N(P,Q)\), viewed as a function of these multiplicities, is eventually a multivariate quasi-polynomial, with each coordinate period dividing the exponent of \(H\). Its highest total-degree term is
\[
\boxed{\frac{|K|}{|H|}\prod_{a\in A}\frac{r_a^{q_a-1}}{(q_a-1)!}.}
\]
All other terms have total degree strictly smaller than \(\sum_{a\in A}(q_a-1)\) on each sufficiently large residue region. In particular, for every fixed nonempty target \(Q\), the exact moduli count is computable in polynomially many integer-arithmetic operations in the number of source points, without enumerating all functions between the underlying sets.

## Assumptions and scope

A bounded morphism of unvalued frames is a function satisfying the usual forth and back conditions on the single accessibility relation. It need not be globally onto in general; **global surjectivity is expressly imposed here**. A target block may receive several source blocks, but each contributing source block must individually cover every point of that target block. The labels used to define the profile coordinates are temporary labels inside a fixed representative of \(Q\); the final orbit count is label-independent. Source and target are nonempty, finite, and their accessibility relations are equivalence relations. No assumption is made that their blocks have equal sizes.

## Proof

**1. Characterize morphisms.** Let \(C\) be a source equivalence class and \(x\in C\). The forth condition forces \(f(C)\) into the target equivalence class \(D\) containing \(f(x)\). Conversely, the back condition at \(x\) ensures that every point of \(D\) is an image of a point of \(C\). Hence \(f|_C:C\twoheadrightarrow D\). Conversely, any function obtained by independently choosing such a surjection for every source class satisfies both conditions. Global surjectivity is equivalent to requiring every target class to be selected by at least one source class.

**2. Quotient the source automorphism group.** An automorphism of a finite equivalence frame freely permutes points within each source class and freely permutes all source classes of the same cardinality. For a fixed source class of size \(a\), a surjection onto target block \(B_j\) is determined up to permutations of that source class by its \(b_j\)-tuple of strictly positive fibre sizes, which sums to \(a\). Thus the orbit types for individual \(a\)-classes are exactly \(\Omega_a\). Permuting source classes of identical sizes turns the collection of their profile types into a multiset \(M_a\) of size \(r_a\). Equality of all such multisets is both necessary and sufficient for two maps to differ by a source automorphism. The coverage constraint from step 1 remains exactly the condition given in the finding.

**3. Quotient target automorphisms.** The target automorphism group is the product of symmetric groups within target blocks, semidirect with permutations among blocks of equal size. It therefore acts on the profile sets by moving the destination block and permuting the fibre coordinates. Passing to target-automorphism orbits of the tuples \((M_a)_a\) is exactly the quotient by independent source and target automorphisms. This proves the structural classification.

**4. Count the orbits.** Fix \(h\in H\). A multiset on a finite \(h\)-set is fixed by \(h\) exactly when its multiplicity function is constant on every cyclic \(h\)-orbit \(O\). Its generating factor is therefore \((1-z^{|O|})^{-1}\). For all source classes of size \(a\), extracting \([z^{r_a}]\) selects the required number of profiles. An \(h\)-fixed collection has a set of used target blocks that is a union of entire cycles of the block permutation induced by \(h\). Inclusion–exclusion over these block cycles, using the signs in the displayed formula, removes collections omitting any target block. Independence between distinct source-block sizes gives the product over \(a\). Burnside's orbit-counting lemma gives the average over \(h\in H\), proving the formula.

**5. Growth.** For fixed target and fixed source sizes \(A\), every factor in step 4 has denominator \(1-z^d\) with \(d\) dividing the order of the acting element, hence dividing the exponent of \(H\). Coefficients of these rational generating functions are eventually quasi-polynomials in each multiplicity, with the asserted period bound. A term from \(h\) acting trivially on the full disjoint profile set, and with no target blocks excluded, has highest total-degree term \(\prod_{a\in A}r_a^{q_a-1}/(q_a-1)!\), because the corresponding generating factors are \((1-z)^{-q_a}\). Exactly \(|K|\) group elements act trivially on all those profiles. If \(h\notin K\), some profile cycle has length greater than one, strictly reducing the total number of cycles and therefore the maximum total degree. If any target block is omitted from \(S\), then reachability ensures that at least one profile is lost for some source size; this again strictly reduces the maximum total degree, or makes the term zero. Consequently the displayed leading term is exact, and all other terms have smaller total degree.

**6. Algorithm.** If \(m=|Q|\) is fixed and \(n=|P|\), then for each source size \(a\le n\) there are at most \(\sum_j\binom{a-1}{b_j-1}\) profiles (terms with \(a<b_j\) are zero). The number and orders of target automorphisms are constants dependent on \(Q\). Build the profile permutations, identify their cycles, and compute coefficient extractions using truncated one-variable knapsack-style dynamic programming. The total number of profiles across all occurring source sizes is bounded by a polynomial in \(n\) of degree at most \(m\), and the coefficient dynamic programs add at most one further factor of \(n\). Thus a conservative \(O_Q(n^{m+2})\) bound holds for integer arithmetic operations; it is a polynomial-time exact count for every fixed target. No bound on coefficient bit lengths is implied by an arithmetic-operation count, but the result is at most \(m^n\), so output bit length is at most linear in \(n\) for fixed \(Q\).

## Verification

The file `s5_orbit_burnside.py` computes the exact orbit formula using target automorphisms and cyclic profile-orbit coefficient extraction. The file `s5_orbit_direct.py` independently enumerates all functions, checks the bounded-morphism and global-surjectivity conditions directly, and canonicalizes their source-fibre counts under target automorphisms. The file `s5_orbit_full_group.py` independently enumerates the complete source and target automorphism groups and checks their actual action on functions, without profile compression. Recorded checks cover 278 source/target frame pairs with up to six source points and four target points, plus 55 smaller full-group-action cases; all comparisons passed. An additional 45 calculations check the closed families below.

As a transparent example, take \(P\) with \(r\ge1\) blocks, each of size three, and take \(Q\) to have one block of size two. Then every profile is \((1,2)\) or \((2,1)\); the target involution interchanges them. The number of two-sided orbits is \(1+\lfloor r/2\rfloor\). For \(r=2\), there are 36 individually labelled surjective bounded morphisms but exactly **two** symmetry-reduced diagram types. Similarly, \(r\) source blocks of size two onto one two-point target block yield one type, while \(r\) singleton source blocks onto two singleton target blocks yield \(\lfloor r/2\rfloor\) types (zero for \(r=1\)).

## Relationship to prior work

Bounded morphisms are standard in modal-frame semantics; the Goranko–Otto handbook treatment supplies their forth/back definition. Figallo–Pascual–Ziliani develop an enriched category of monadic augmented Kripke frames, a nearby but different morphism setting. De Berardinis–Ghilardi show that finite \(\mathsf{S5}\) frames form a finite-family completion of the category of finite nonempty sets and surjections; their characterization strongly motivates the profile objects here, and is fully compatible with the structural step of the proof. The present result addresses a different counting question: simultaneous source-and-target relabeling classes of **globally onto** bounded morphisms, with explicit coefficient formula, a fixed-target algorithm, and the multivariate quasi-polynomial leading term. These enumerative statements were not identified in the inspected primary results. Burnside's lemma and integer-composition enumeration are established tools and are not claimed as new.

## Limitations

The formula concerns one unvalued equivalence accessibility relation. It does not automatically apply to several commuting or noncommuting accessibility relations, to valuations, to arbitrary preorders, or to homotopy classes of maps. The polynomial-time assertion fixes the target; no uniform polynomial-time bound is asserted as the target varies. The quasi-polynomial assertion fixes the finite set of permitted source block sizes and requires all corresponding multiplicities to grow; it does not describe an arbitrary sequence of source frames whose block sizes also increase. No independent scientific audit or external priority certification has been performed. Existing specialized orbit-enumeration formulas in the literature may imply aspects of the claim; publication priority requires expert checking.

## References

1. V. Goranko and M. Otto, *Model Theory of Modal Logic*, in *Handbook of Modal Logic* (2007), Chapter 5, Definition 15 and following discussion (bounded morphisms). DOI: 10.1016/S1570-2464(07)80008-5. Lawful author manuscript: https://www.mathematik.tu-darmstadt.de/~otto/papers/Chapter5_02_05_06.pdf .
2. A. V. Figallo, I. Pascual and A. Ziliani, *Monadic distributive lattices and monadic augmented Kripke frames*, publicly posted 2012-03-27, arXiv:1203.6059, sections 1 and 3. https://arxiv.org/abs/1203.6059 .
3. M. De Berardinis and S. Ghilardi, *An essentially algebraic glance to Kripke semantics: the S5 case*, arXiv:2511.00188 (2025), sections 2.1, 4, 5 and 6. https://arxiv.org/abs/2511.00188 .
4. W. Burnside, *Theory of Groups of Finite Order* (1911), orbit-counting lemma; standard mathematical background.
