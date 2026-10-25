# A one-relation counterexample to finite generated-subframe preservation

## Finding
Let \(\mathcal E_\sigma\) be the fragment of first-order logic over a finite relational vocabulary \(\sigma=\{R_1,\ldots,R_r\}\) of binary relations generated from equality and relation literals by conjunction, disjunction, arbitrary universal quantification, and successor-guarded quantifiers \(\exists y(R_i(x,y)\land\theta)\) and \(\forall y(R_i(x,y)\to\theta)\), with \(x\ne y\). A generated subframe is an induced substructure on a successor-closed set.

**Theorem.** There is a first-order sentence \(\widehat\chi\) over a *single* binary relation \(E\) such that, on finite directed graphs (loops allowed), (i) \(\widehat\chi\) is preserved under all generated subframes, but (ii) \(\widehat\chi\) is not equivalent to any sentence of \(\mathcal E_{\{E\}}\). Thus the one-binary-relation case left open after Theorem 8 in van Benthem, ten Cate and Yang (2026) also fails the proposed finite preservation characterization.

More generally, for every finite all-binary signature \(\sigma\) and every first-order sentence \(\chi\) preserved under finite generated subframes with \(\chi\) true on the empty structure, an effective one-relation forward interpretation gives a sentence \(\widehat\chi\) preserved under finite generated subframes. If \(\widehat\chi\) has a finite-structure equivalent in \(\mathcal E_{\{E\}}\), then \(\chi\) has a finite-structure equivalent in \(\mathcal E_\sigma\). The nondefinability conclusion uses the published four-relation \(\chi\).

## Assumptions and scope
All structures are finite, arbitrary directed edge relations may contain loops, and equality is available. The encoding allows empty structures as well as nonempty structures; the source sentence from Theorem 8 is universally quantified and true on the empty structure. The symbol \(r\) denotes a fixed positive integer, not a variable part of a structure. Generated subframes are successor-closed induced substructures for *every* relation in the vocabulary. The logical fragment is precisely the \(\exists\)-bounded fragment defined in Section 3.3 of the cited 2026 paper, including unrestricted universal (but not unrestricted existential) quantification.

## Proof
**1. Forward-local tags.** For the single relation \(E\), define \(U(x):=E(x,x)\). Define \(C_1(t):=\forall u\neg E(t,u)\), and for \(j\ge1\) set
\[
C_{j+1}(t):=\exists u\big(E(t,u)\land C_j(u)\land\forall v(E(t,v)\to v=u)\big).
\]
Let \(T_i(z):=\exists t(E(z,t)\land C_i(t))\). Each of these formulas depends only on the forward-generated subframe of its argument. Consequently, their truth at any retained point is unchanged on restricting a structure to an \(E\)-successor-closed subset.

**2. Forward interpretation.** In any single-edge structure \(G\), interpret a \(\sigma\)-structure \(I(G)\) on \(U(G)=\{a:E(a,a)\}\), with
\[
R_i^{I(G)}(a,b)\iff U(a)\land U(b)\land\exists z\big(E(a,z)\land\neg U(z)\land E(z,b)\land T_i(z)\big).
\]
If \(H\) is an \(E\)-generated subframe of \(G\), every witness \(z\) and all of its successors used in these formulas remain in \(H\) whenever \(a\in H\). Thus \(I(H)\) is exactly the induced \(\sigma\)-structure on \(U(G)\cap H\); this set is successor closed under every interpreted \(R_i\). In particular, \(I(H)\) is a generated subframe of \(I(G)\).

Given any source sentence \(\chi\), define \(\widehat\chi\) by standard first-order interpretation: relativize its quantifiers to \(U\) and replace each \(R_i\)-atom by the displayed defining formula. Then \(G\models\widehat\chi\) iff \(I(G)\models\chi\). If \(\chi\) is preserved under finite generated subframes, the preceding paragraph proves preservation of \(\widehat\chi\), including the case \(I(H)\) empty because \(\chi\) is true on empty structures.

**3. Realizing arbitrary sources.** For each finite \(\sigma\)-structure \(A\), construct a finite directed graph \(F(A)\). For each element \(a\), insert a vertex \(o_a\) carrying a self-loop. For each edge \(R_i(a,b)\), insert a fresh vertex \(e_{i,a,b}\) and a fresh path of \(i\) vertices \(t_{i,a,b,1},\ldots,t_{i,a,b,i}\). Insert only the following additional arcs:
\[
o_a\to e_{i,a,b},\quad e_{i,a,b}\to o_b,\quad e_{i,a,b}\to t_{i,a,b,1},\quad t_{i,a,b,j}\to t_{i,a,b,j+1}\ (1\le j<i).
\]
The last path vertex is a sink. Precisely the original vertices carry self-loops. The new edge vertex has two distinct successors, namely the original target and the first tag vertex; the tag chain has its unique deterministic length. Therefore \(T_i\) detects exactly the intended edge type at every edge vertex, and \(I(F(A))\cong A\) for all finite \(A\), including empty structures.

**4. Backward reflection of the restricted syntax.** Fix any \(\exists\)-bounded sentence \(\beta\) in the language \(\{E\}\). We prove by induction on formulas that its truth on graphs \(F(A)\) is expressible by an \(\exists\)-bounded sentence \(\beta^{\leftarrow}\) on \(A\). Each variable of \(\beta\) is represented by one of finitely many *sorts*: original \(o_a\); an edge \(e_{i,a,b}\) subject to \(R_i(a,b)\); or a tag \(t_{i,a,b,j}\) for an edge of that type. A sort has one or two source parameters. The equality and \(E\)-atomic formulas between any two sorts are Boolean combinations of parameter equalities and source relation literals: a self-loop on an original, an original-to-edge arc, an edge-to-target arc, an edge-to-first-tag arc, or a tag-to-next-tag arc are all the possibilities. Thus literals and their negations translate to allowed literal Boolean combinations.

Conjunction and disjunction translate componentwise. An unrestricted universal quantifier becomes a finite conjunction over the sorts. Its original-vertex branch is \(\forall a\) of the translated formula; an edge or tag branch is \(\forall a\forall b(R_i(a,b)\to\cdots)\). These use only unrestricted universals and Boolean connectives. For a guarded quantifier at a given sort, inspect its full list of outgoing arcs. An original \(o_a\) has a self-successor \(o_a\) and one edge-successor \(e_{i,a,b}\) for each \(R_i(a,b)\); hence, for example, the bounded existential translates to the disjunction of the body at \(o_a\) and finitely many formulas \(\exists b(R_i(a,b)\land\operatorname{body}_{e_i}(a,b))\). An edge vertex has only successors \(o_b\) and \(t_{i,a,b,1}\), requiring no new quantification. A tag vertex has only the next tag (or no successors). Bounded universals give the dual finite conjunctions, including \(\forall b(R_i(a,b)\to\operatorname{body}_{e_i}(a,b))\) on originals. Therefore *no unguarded existential quantifier* appears in any branch of the inductive translation. The bound variable is replaced by the source parameters of its chosen sort, with bound variables renamed to avoid capture. This proves the reflection lemma for all formulas and assignments, in particular sentences.

**5. One-relation failure.** Theorem 8 and Lemmas 9–10 of van Benthem, ten Cate and Yang (2026, Section 3.3) supply a concrete sentence \(\chi\) in four binary relations which is true on the empty structure, preserved under finite generated subframes, and not equivalent on all finite four-relation frames to any \(\exists\)-bounded sentence. Apply steps 1–3 with \(r=4\). If \(\widehat\chi\) were equivalent on all finite one-relation frames to such a \(\beta\), then for every finite four-relation frame \(A\),
\[
A\models\chi\iff I(F(A))\models\chi\iff F(A)\models\widehat\chi\iff F(A)\models\beta\iff A\models\beta^{\leftarrow}.
\]
Step 4 says the final sentence is \(\exists\)-bounded, contradicting Theorem 8. Thus \(\widehat\chi\) is the required one-relation counterexample. \(\square\)

## Verification
The accompanying pure-Python checker exhaustively verifies the recovery equality \(I(F(A))=A\) across all binary-structure samples with up to two elements and up to three source relations (as limited in code), together with compatibility of the forward interpretation with every successor-closed subset of all directed graphs on up to three vertices. The checker reports `FORWARD_GADGET_FINITE_SANITY_OK 2133` when run successfully. These finite computations test the coding and restriction identities but **do not** prove the induction over arbitrary formulas nor the unbounded finite-model theorem. The proof above supplies those deductions. Run `python check_generated_coding.py` using Python 3, with no nonstandard dependencies.

## Relationship to prior work
Van Benthem, ten Cate and Yang (2026), Section 3.3, prove a four-relation finite counterexample in Theorem 8 and explicitly leave the single-relation case open after their proof. The present argument supplies a forward-local coding and a restricted-syntax backward translation proving that their four-relation obstruction persists for one binary relation. General first-order transduction backward translations, and classical edge-gadget codings, are background techniques, but they do not by themselves establish preservation of *this* \(\exists\)-bounded syntactic fragment; the sort-by-sort guarded-quantifier reflection in step 4 is essential. Bogaerts, ten Cate, McLean and Van den Bussche (2024) investigate different preservation problems for relation-algebra operations and do not directly give the claimed one-relation finite generated-subframe obstruction. Courcelle (2026) surveys general FO transductions, which provide a broad methodological comparison rather than the precise restricted-fragment preservation statement.

## Limitations
The construction uses directed graphs in which loops are permitted, one fixed finite source signature, and finite structures. It does not prove a corresponding obstruction for symmetric/irreflexive simple graphs or for subframes that are not successor closed. The finite checker does not establish the general induction. The nondefinability theorem depends on the published Theorem 8 of the first cited paper, treated here as a prior theorem rather than independently re-proved. Literature searches cannot exclude an unlocated equivalent one-relation result, so historical priority remains to be independently examined. No independent validation has been performed.

## References
1. J. van Benthem, B. ten Cate and X. Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1 (first posted 2026-03-12), Section 3.3, Theorem 8 and final open question. https://arxiv.org/html/2603.12171v1
2. B. Bogaerts, B. ten Cate, B. McLean and J. Van den Bussche, *Preservation theorems for Tarski's relation algebra*, arXiv:2305.04656v5 (2024), especially introduction and Sections 3–5. https://arxiv.org/html/2305.04656v5
3. B. Courcelle, *On first-order definable operations on relational structures*, arXiv:2605.31260 (2026), abstract on backward translation for general FO transductions. https://arxiv.org/abs/2605.31260
