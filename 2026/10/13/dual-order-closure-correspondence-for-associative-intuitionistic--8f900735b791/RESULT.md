# Dual order-closure correspondence for associative intuitionistic binary modalities

## Finding
Let \(W\) be a nonempty set equipped with a partial order \(\leq\), and let \(R\subseteq W^3\) satisfy the two monotonicity conditions of Kaminski's intuitionistic binary-modality frames (defined below). There is an exact, operator-specific criterion for the validity of all four associativity implications.

For a ternary relation \(T\) and a world \(u\), define
\[
L_T(u)=\{(a,b,c)\in W^3:\exists t\in W\;(T(t,a,b)\land T(u,t,c))\},
\]
\[
M_T(u)=\{(a,b,c)\in W^3:\exists t\in W\;(T(t,b,c)\land T(u,a,t))\}.
\]
Put \(E(u,a,b)\) if and only if \(R(v,a,b)\) for some \(v\in W\) with \(u\leq v\). Let \(\downarrow S\) and \(\uparrow S\) denote the lower and upper closures of \(S\subseteq W^3\) for the coordinatewise partial order.

**Theorem.** The two associativity implications for \(\circ\), namely
\[
((p\circ q)\circ r)\to(p\circ(q\circ r)),\qquad
(p\circ(q\circ r))\to((p\circ q)\circ r),
\]
are valid in the frame for every persistent valuation if and only if
\[
\boxed{\forall u\in W:\quad\downarrow L_R(u)=\downarrow M_R(u).}
\]
Independently, the two analogous implications for \(\bullet\) are valid in the frame for every persistent valuation if and only if
\[
\boxed{\forall u\in W:\quad\uparrow L_E(u)=\uparrow M_E(u).}
\]
Under monotonicity condition (ii), the composites of \(E\) are themselves upward closed in the three input coordinates, so this boxed condition simplifies to the strict associativity equality \(L_E(u)=M_E(u)\). Thus all four schemata are valid exactly when both equalities hold. If \(W\) has \(n\) worlds and the order and relation are given explicitly, the combined condition is decidable in \(O(n^7)\) time and \(O(n^4)\) space by finite relational composition and product-order closure comparison.

## Assumptions and scope
A **persistent valuation** interprets each propositional variable as an upward-closed subset of \(W\). Following Kaminski (2026), assume:

1. If \(R(u,v,w)\) and \(u\leq u'\), there are \(v'\geq v\), \(w'\geq w\) with \(R(u',v',w')\).
2. If \(R(u,v,w)\), \(v\leq v'\) and \(w\leq w'\), there is \(u'\geq u\) with \(R(u',v',w')\).

At a world \(u\), the existential operation has semantics \(p\circ q\) when \(R(u,v,w)\) holds for some \(v\models p\) and \(w\models q\). The universal operation has semantics \(p\bullet q\) when for every \(u'\geq u\) and every \(R(u',v,w)\), at least one of \(v\models p\) or \(w\models q\) holds. In particular, the universal connective uses **or**, not and. These clauses make modal truth persistent, so validity of the two implications is equivalent to equality of the respective truth sets for all triple valuations. No finiteness, seriality, or totality of the order is assumed for the theorem.

## Proof
**1. Existential associativity.** Fix upward-closed \(A,B,C\subseteq W\). Unwinding the existential semantics twice gives
\[
u\models(p\circ q)\circ r\quad\Longleftrightarrow\quad
L_R(u)\cap(A\times B\times C)\neq\varnothing,
\]
with the analogous condition involving \(M_R(u)\) for \(p\circ(q\circ r)\). An upward-closed product intersects \(L_R(u)\) precisely when it intersects its downward closure, since a lower triple below a product member can be promoted to a triple in the product. Hence equality of downward closures is sufficient.

For necessity, suppose \(x=(a,b,c)\in L_R(u)\setminus\downarrow M_R(u)\). Set \(A=\uparrow a\), \(B=\uparrow b\), and \(C=\uparrow c\), where the arrows here denote **principal upper subsets of \(W\)**. Then \(x\) witnesses the left-nested product, whereas no member of \(M_R(u)\) belongs to \(A\times B\times C\): otherwise that member would dominate \(x\). The converse direction is symmetric. As atomic truth sets may be any upsets, this proves necessity of equality.

**2. Universal associativity.** Define \(E(u,v,w)\iff\exists u'\geq u:R(u',v,w)\). For upsets \(A,B\), the universal semantics is exactly
\[
u\models p\bullet q\quad\Longleftrightarrow\quad
\forall(v,w)\,[E(u,v,w)\Rightarrow(v\in A\lor w\in B)].
\]
On expanding a second application of \(\bullet\), elementary distributivity of universal quantifiers over the inner disjunction yields
\[
u\models(p\bullet q)\bullet r\quad\Longleftrightarrow\quad
\forall(a,b,c)\in L_E(u):\;(a\in A\lor b\in B\lor c\in C),
\]
and the other nesting is the corresponding assertion for \(M_E(u)\). For upsets \(A,B,C\), the disjunctive predicate is upward closed on \(W^3\); hence it holds on a relation exactly when it holds on its upward closure. Equality of the two upward closures therefore suffices.

Conversely suppose \(x=(a,b,c)\in M_E(u)\setminus\uparrow L_E(u)\). Take
\[
A=W\setminus\downarrow a,\quad B=W\setminus\downarrow b,\quad C=W\setminus\downarrow c.
\]
Each set is an upset. The disjunctive predicate fails at \(x\), while at every point of \(L_E(u)\) it holds: failure at some \(y\in L_E(u)\) would mean \(y\leq x\) coordinatewise, contrary to \(x\notin\uparrow L_E(u)\). Thus one nesting is true at \(u\) and the other false. Exchanging \(L_E\) with \(M_E\) gives the reverse inclusion. This proves necessity without compactness or finite-valued assumptions. Moreover, monotonicity condition (ii) makes \(E(u,-,-)\) upward closed in its two input coordinates: if \(E(u,a,b)\) has a witness \(v\geq u\), then increasing \(a,b\) has a witness \(v'\geq v\) by (ii). Keeping each intermediate \(t\) fixed therefore shows that both \(L_E(u)\) and \(M_E(u)\) are already upward-closed subsets of \(W^3\). Hence equality of their upward closures is equivalent to strict relational equality of the two composites of the saturated relation \(E\).

**3. Effective finite recognition.** For \(|W|=n\), compute the output-coordinate saturation \(E\) in at most \(O(n^4)\) tests. Enumerating intermediate worlds generates \(L_R,M_R,L_E,M_E\) for all \(u\) using at most \(O(n^5)\) primitive tests. For every \(u\) and every tuple \(x\in W^3\), compare membership of \(x\) in each closure by scanning at most \(n^3\) generating tuples and testing coordinatewise comparability. This gives \(O(n^7)\) time and stores four relations on \(W^4\), hence \(O(n^4)\) space. The upper bound is deliberately conservative and does not require enumerating the \(2^{3n}\) possible triples of arbitrary Boolean valuations.

## Verification
The standalone Python 3 script `verify.py` constructs semantic truth sets directly from the two forcing clauses, independently constructs the two closure criteria, and compares them on every monotone ternary relation over one- and two-world chains; it independently checks that the universal criterion equals raw ternary associativity of the output-saturated relation. Counts are 2 and 67 monotone relations respectively, with no mismatches. It separately checks all 95 monotone ternary relations induced by binary operations on a three-world chain, again with no mismatches. It also tests explicit examples witnessing that strict ternary-relation associativity can be stronger than semantic associativity and that a three-point monotone frame may fail both semantic associativity requirements. These bounded tests are reproducible diagnostics; the unrestricted theorem is established by the proofs above.

Reproduce using `python3 verify.py` from the directory containing this document and the checker. No external Python packages or network data are required.

## Relationship to prior work
Kaminski (2026) provides the exact intuitionistic ternary-frame semantics and identifies the associative two-modality extension as an open strong-completeness problem. It observes that ordinary (unqualified) associativity of the ternary relation is sufficient for soundness. Kaminski (2024) treats the classical and intuitionistic logics of associative binary modality, with classical ternary-frame conditions. Kaminski and Francez (2016) examine the Lambek calculus joined to intuitionistic propositional logic; its full text could not be compared here. The present criterion instead characterizes **semantic validity** of each of the four associativity implications on every fixed ordered ternary frame: it uses a downward closure for \(\circ\) but strict ternary associativity of the output-saturated relation \(E\) for \(\bullet\); the latter is equivalent to the upward-closure equation because of frame monotonicity. It need not enforce raw associativity of \(R\), and it does not assert strong completeness.

## Limitations
This theorem is a frame-validity test, **not** a proof that the class satisfying these equations gives a sound-and-strongly-complete semantics for associative intuitionistic binary-modal logic. It does not resolve decidability, finite-model properties, or canonical-model closure of the full logic. The finite algorithm presupposes the complete explicit order and ternary relation. The 2016 source was only accessible by abstract and metadata; an older order-theoretic correspondence under different terminology remains a genuine originality risk. Finite verification does not certify the infinite case independently of the symbolic proof.

## References
1. Michael Kaminski, *Intuitionistic logic of a binary modality*, Archive for Mathematical Logic, published 2026-09-09, DOI: https://doi.org/10.1007/s00153-026-01025-3. Full open text, particularly Sections 3 and 6.
2. Michael Kaminski, *On undecidability of the propositional logic of an associative binary modality*, Archive for Mathematical Logic 63 (2024), 837–857, DOI: https://doi.org/10.1007/s00153-024-00921-w.
3. Michael Kaminski and Nissim Francez, *The Lambek calculus extended with intuitionistic propositional logic*, Studia Logica 104 (2016), 1051–1082, DOI: https://doi.org/10.1007/s11225-016-9665-0. Abstract and metadata only inspected.
