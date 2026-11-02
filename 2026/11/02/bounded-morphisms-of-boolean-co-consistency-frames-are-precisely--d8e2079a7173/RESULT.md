# Bounded morphisms of Boolean co-consistency frames are precisely surjective direct images

## Finding

Let \(I\) and \(J\) be arbitrary nonempty sets. Define the **nonzero powerset co-consistency frame** \(F(I)\) as follows: its worlds are all nonempty subsets of \(I\), and accessibility is
\[
S\,R_I\,T\quad\Longleftrightarrow\quad S\cap T\ne\varnothing.
\]
A **bounded morphism** \(f:F(I)\to F(J)\) means a total world map satisfying (forth) \(S R_I T\Rightarrow f(S)R_J f(T)\) and (back) whenever \(f(S)R_J Y\), there exists \(T\) with \(S R_I T\) and \(f(T)=Y\).

**Classification theorem.** Every bounded morphism has one and only one representation
\[
f(S)=\pi[S]\quad\text{for every nonempty }S\subseteq I,
\]
where \(\pi:I\twoheadrightarrow J\) is a surjection; conversely every such \(\pi\) induces a bounded morphism. This requires no finiteness assumption.

Consequently the category of nonzero powerset co-consistency frames and bounded morphisms is isomorphic to the category of nonempty sets and surjections. In the finite labelled case, \(|I|=m\ge1\), \(|J|=n\ge1\), its hom-set cardinality is exactly
\[
|\operatorname{Hom}(F(I),F(J))|=n!\,S(m,n)
=\sum_{k=0}^{n}(-1)^{n-k}\binom{n}{k}k^m,
\]
where \(S(m,n)\) is the Stirling number of the second kind (zero for \(n>m\)). In every cardinality, \(\operatorname{Aut}(F(I))\cong\operatorname{Sym}(I)\).

Equivalently, a bounded morphism between these two canonical frames exists precisely when there is a surjection \(I\to J\). Under the usual choice principle this is the cardinal inequality \(|I|\ge |J|\).

## Assumptions and scope

Both carriers \(I,J\) are nonempty sets. The source and target are their **entire nonzero powerset frames**, not arbitrarily selected induced subframes, and all nonempty subsets are allowed as worlds. The morphisms are ordinary (unvalued) Kripke-frame bounded morphisms with the forth/back conditions written above. The theorem makes no assertion about model morphisms with nontrivial fixed propositional valuations, arbitrary complete Boolean algebras without atoms, or bounded morphisms to other kinds of frames. The counting formula applies only to finite positive \(m,n\); the structural classification applies to arbitrary nonempty sets.

## Proof

Let \(f:F(I)\to F(J)\) satisfy forth and back.

**Step 1: images of atoms are singleton worlds.** Fix \(i\in I\). Since the target world \(f(\{i\})\) is nonempty, suppose for a contradiction that it contains distinct \(a,b\in J\). Then \(f(\{i\})\,R_J\,\{a\}\) and \(f(\{i\})\,R_J\,\{b\}\). Apply back twice: there are worlds \(T_a,T_b\subseteq I\) each meeting \(\{i\}\), such that \(f(T_a)=\{a\}\) and \(f(T_b)=\{b\}\). Both worlds contain \(i\), so \(T_aR_IT_b\). Forth then forces \(\{a\}R_J\{b\}\), contradicting \(a\ne b\). Thus \(f(\{i\})=\{\pi(i)\}\) for a uniquely determined function \(\pi:I\to J\).

**Step 2: the whole map is direct image.** If \(i\in S\ne\varnothing\), then \(\{i\}R_IS\); forth gives \(\pi(i)\in f(S)\). Hence \(\pi[S]\subseteq f(S)\). Conversely, fix \(a\in f(S)\). Since \(f(S)R_J\{a\}\), back supplies \(T\ne\varnothing\) meeting \(S\), with \(f(T)=\{a\}\). Choose \(i\in S\cap T\). Forth applied to \(\{i\}R_IT\) gives \(\pi(i)\in f(T)=\{a\}\), hence \(a=\pi(i)\in\pi[S]\). Therefore \(f(S)=\pi[S]\) for all nonempty \(S\).

**Step 3: surjectivity is forced by back.** Fix any \(i\in I\). The singleton world \(f(\{i\})=\{\pi(i)\}\) intersects the nonempty target world \(J\). Back yields \(T\ne\varnothing\) with \(f(T)=J\). Step 2 gives \(J=\pi[T]\), so \(\pi\) is onto.

**Step 4: every surjection works.** Conversely let \(\pi:I\twoheadrightarrow J\), and define \(f(S)=\pi[S]\). Nonempty intersections stay nonempty under direct image, proving forth. If \(\pi[S]\cap Y\ne\varnothing\), select \(i\in S\) with \(\pi(i)\in Y\). Put \(T=\pi^{-1}[Y]\). Then \(S\cap T\ni i\) and, using surjectivity, \(\pi[T]=Y\). This is back.

**Step 5: structural consequences.** Uniqueness follows from the singleton formula of Step 1. For surjections \(\pi:I\to J\) and \(\rho:J\to K\), direct images satisfy \(\rho[\pi[S]]=(\rho\circ\pi)[S]\). They also preserve identities, proving the asserted categorical isomorphism. For finite \(m,n\), there are exactly \(n!S(m,n)\) surjections by assigning a nonempty labeled fiber to every target point; inclusion-exclusion gives the displayed alternative formula. The invertible morphisms are exactly the maps induced by bijections of \(I\), proving the automorphism claim.

An equivalent algebraic corollary identifies each such morphism with the complete Boolean embedding \(\pi^{-1}:\mathcal P(J)\hookrightarrow\mathcal P(I)\). Conversely, a complete Boolean embedding between full powerset algebras partitions source atoms into nonempty inverse-image fibers and thus arises from a unique surjection. This is an equivalent description of the same classification, not a separate assertion of uniqueness outside its hypotheses.

## Verification

The accompanying self-contained Python checker (`checker.py`, Python 3 standard library) directly evaluates the two frame conditions for every possible world map in the following seven source/target size pairs \((m,n)\):
\[
(1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2).
\]
The respective numbers of bounded morphisms are \(1,0,1,2,0,1,6\), agreeing exactly with the surjection formula. It additionally checks 2,676 explicitly generated surjection-induced maps with source sizes up to six and target sizes up to four. Run `python3 checker.py`; successful output ends in `ALL_CHECKS_OK`.

These finite computations are corroborative, not a proof for arbitrary nonempty carriers. The proof in Steps 1–4 is entirely set-theoretic and covers infinite cardinalities without extrapolation.

## Relationship to prior work

Jockwich, Tarafder, and Venturi [1] introduce the accessibility relation \(aRb\) iff \(a\wedge b\ne0\) for Boolean values; their Sections 3, 5 and 6 develop the nonzero-state translation semantics and finite-power-set modal logics. In Lemma 6.13 they explicitly construct complete Boolean embeddings between finite powerset algebras from partitions, which explains the existence of certain direct-image bounded morphisms; their inspected arguments do not assert that **every** frame bounded morphism is thereby exhausted or count such morphisms.

The separately published paper [2] proves strictness of the finite hierarchy of those logics and finds a sharp \(2^{n-1}\) bound on bounded-morphic images whose targets are **complete reflexive graphs**, possibly from induced subframes. This is a different target class: it does not classify maps between the whole source frame \(F(I)\) and another complete powerset frame \(F(J)\). It therefore does not imply the singleton-image rigidity in Step 1 or the categorical hom-set formula.

Classical bounded-morphism theory [3] supplies the forth/back notion and modal preservation, while standard Boolean-algebra duality describes inverse-image embeddings. The distinctive step here is to recover, directly from the graph-theoretic forth/back properties, a uniquely determined surjection between the underlying atom sets, even for infinite carriers.

## Limitations

The classification relies on every nonempty subset being a world: a proper induced subframe need not contain all singleton worlds or all needed targets, and may have many other bounded morphisms. Its target is also required to be a full nonzero powerset frame. The result concerns frame morphisms rather than valuations or Kripke-model morphisms. The finite count is a labeled count; no new formula for Stirling numbers themselves is claimed.

No exhaustive literature theorem-equivalence proof is possible from keyword search alone. Related modal duality or older work on intersection/compatibility graphs may contain an equivalent classification under another terminology. An independent literature audit remains outstanding.

## References

[1] Santiago Jockwich, Sourav Tarafder, Giorgio Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977 (first public version, 28 July 2026), https://arxiv.org/abs/2607.25977. Relevant sections: 3 (co-consistency), 5 (nonzero frames), and 6 (finite algebras, especially Lemma 6.13).

[2] *Every finite stage of the internal forcing logic hierarchy is strict*, published mathematical report, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-every-finite-stage-of-the-internal-forcing-logic-hierarchy-is-st--069a2c03aeb3. Relevant result: complete reflexive bounded-morphic quotient bound on the same finite compatibility frames.

[3] Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press, 2001, standard theory of bounded morphisms.
