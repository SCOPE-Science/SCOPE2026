# Exact observational fibers of two-sided instantial logic on finite chains

## Finding

For the positive two-sided instantial-neighbourhood semantics on a finite intuitionistic chain, every modal operation of arbitrary instance arity is determined by its nullary and unary instances. In addition, the complete observable behavior of each local box-neighbourhood family is classified by **whether the empty upset is present and the least nonempty upset present**; the corresponding diamond behavior is classified by **whether the empty upset is present and the greatest nonempty upset present**.

More precisely, let \(C_n=\{0<1<\cdots<n-1\}\) with \(n\ge1\), and denote its \(n+1\) upsets by \(E_0=\varnothing\) and \(E_j=\{n-j,\ldots,n-1\}\) for \(1\le j\le n\). At any fixed world, the \(2^{n+1}\) possible neighbourhood families have exactly \(2n+2\) distinct box-operation signatures, and exactly \(2n+2\) distinct diamond-operation signatures, when operations are evaluated on all upsets at every finite instance arity.

For a box family \(N\), its signature is the pair \((\epsilon,m)\), where \(\epsilon=1\) exactly when \(E_0\in N\), and \(m\) is the smallest index of a nonempty upset in \(N\), or \(0\) if none exists. For each \(\epsilon\in\{0,1\}\), the exact fiber sizes are
\[
 |[\epsilon,0]_{\Box}|=1,\qquad
 |[\epsilon,m]_{\Box}|=2^{n-m}\quad(1\le m\le n).
\]
For a diamond family, replace the smallest positive index by the largest positive index \(M\); its exact fibers are
\[
 |[\epsilon,0]_{\Diamond}|=1,\qquad
 |[\epsilon,M]_{\Diamond}|=2^{M-1}\quad(1\le M\le n).
\]
These are signatures of **operations**, not mere formula-validity profiles.

Consequently, in the natural homogeneous subclass where both neighbourhood families are constant across the \(n\)-world chain (so persistence is automatic), the \(2^{2(n+1)}\) concrete, labelled pairs of neighbourhood families induce exactly
\[
 (2n+2)^2
\]
distinct joint box/diamond signatures, with largest observational equivalence class of size
\[
 4^{n-1}.
\]
In this restricted class, exponentially many distinct concrete neighbourhood frames can be indistinguishable by every positive instantial formula under every common persistent valuation.

## Assumptions and scope

A *persistent two-sided neighbourhood frame* consists of a nonempty poset \((W,\le)\) with \(N^{\Box}(w)\) and \(N^{\Diamond}(w)\) families of upward-closed subsets of \(W\). For \(w\le v\), assume \(N^{\Box}(w)\subseteq N^{\Box}(v)\) and \(N^{\Diamond}(v)\subseteq N^{\Diamond}(w)\). Empty neighbourhood families and the empty upset are explicitly permitted. Each propositional variable denotes an upset. No supplementation, seriality, or other neighbourhood closure is assumed.

For a family \(N\) and an ordered tuple of upsets \(\boldsymbol A=(A_1,\ldots,A_k)\), define the local truth conditions for \(k\ge0\):
\[
 \operatorname{Box}_N(\boldsymbol A;B)
 \iff \exists U\in N\,\bigl(U\subseteq B\ \land\ \forall i\le k\,[U\cap A_i\ne\varnothing]\bigr),
\]
\[
 \operatorname{Dia}_N(\boldsymbol A;B)
 \iff \forall U\in N\,\bigl((\exists i\le k\,[U\subseteq A_i])\ \lor\ U\cap B\ne\varnothing\bigr).
\]
The quantifier over empty tuples is interpreted literally: the box instance condition is vacuous when \(k=0\), while the diamond instance disjunction is false when \(k=0\).

Two models on the same fixed ordered carrier are *observationally equivalent* if they assign the same truth set to each formula under every shared persistent valuation. Statements about identical signatures refer to all possible upset arguments, not only arguments currently named by a fixed finite set of propositional letters. Variables can independently name any required upset.

## Proof

**Arity reduction.** Any two nonempty upsets of a finite chain intersect in its greatest world. Hence, for every \(k\ge1\), a nonempty neighbourhood witnesses the box instance clauses for all \(A_i\) precisely when all \(A_i\) are nonempty. This is equivalent to intersecting \(A=\bigcap_{i=1}^{k}A_i\). Thus
\[
 \operatorname{Box}_{N}(A_1,\ldots,A_k;B)
 =\operatorname{Box}_{N}(\bigcap_{i=1}^{k} A_i;B).
\]
Because the upsets form a chain by inclusion, some \(A_i\) is their union, and a given upset \(U\) is contained in at least one \(A_i\) precisely when \(U\subseteq\bigcup_{i=1}^{k}A_i\). Therefore
\[
 \operatorname{Dia}_{N}(A_1,\ldots,A_k;B)
 =\operatorname{Dia}_{N}(\bigcup_{i=1}^{k} A_i;B).
\]
These identities hold for any local family \(N\), including the empty family and families containing the empty upset. Recursively replacing each nonnullary, greater-than-unary modality by the displayed unary formula gives a formula translation preserving truth at every world of every persistent two-sided chain, including formulas with nested modal subformulas.

**Box normal form.** Let \(\epsilon\) indicate \(E_0\in N\), and let \(m\) be the smallest positive index present, with sentinel \(0\) when there is none. At arity zero, the box condition holds just when \(\epsilon=1\), or \(m>0\) and \(E_m\subseteq B\). At every positive arity it holds precisely when \(m>0\), \(E_m\subseteq B\), and each instance upset is nonempty. Indeed, an empty neighbourhood cannot meet an instance argument; among nonempty neighbourhoods the least one is the easiest to fit within \(B\), and any two nonempty upsets intersect. This proves that \((\epsilon,m)\) determines every box operation.

The signature is also *recoverable*. The value of \(\operatorname{Box}_{N}(;E_0)\) recovers \(\epsilon\). With unary instance \(A=E_1\), \(\operatorname{Box}_{N}(E_1;B)\) holds for exactly those upset supports \(B\) containing \(E_m\) if \(m>0\), and for none if \(m=0\). In particular, \(m\) is the minimum positive \(j\) for which \(\operatorname{Box}_{N}(E_1;E_j)\) holds. For \(m>0\), the indices \(m+1,\ldots,n\) can be independently present or absent, giving \(2^{n-m}\) families per fixed empty flag. For \(m=0\), the empty flag uniquely specifies the family.

**Diamond normal form.** For \(k=0\), the diamond condition holds for support \(B=E_0\) precisely when \(N=\varnothing\), and for nonempty \(B\) precisely when \(E_0\notin N\) (all nonempty upsets intersect all nonempty upsets). For \(k\ge1\) and \(B\ne E_0\), the diamond condition always holds: each nonempty neighbourhood meets \(B\), while \(E_0\) is contained in every instance upset. When \(B=E_0\), the diamond condition holds precisely when every \(U\in N\) is contained in the largest instance upset \(\bigcup_i A_i\). If \(M>0\) is the largest positive index present, this means \(E_M\subseteq\bigcup_i A_i\); if no positive index exists, the condition is vacuously or trivially true. These observations prove that \((\epsilon,M)\) determines every diamond operation.

Conversely, the two nullary values \(\operatorname{Dia}_{N}(;E_0)\) and \(\operatorname{Dia}_{N}(;E_1)\) distinguish the empty family, the family containing only \(E_0\), and the two broad classes of nonempty families according to \(\epsilon\). The unary values \(\operatorname{Dia}_{N}(A;E_0)\) then recover \(M\) as the least positive support index \(j\) for which \(\operatorname{Dia}_{N}(E_j;E_0)\) holds (or identify \(M=0\) if the unary test holds even for \(A=E_0\)). For a fixed \(M>0\), smaller positive neighbourhoods \(E_1,\ldots,E_{M-1}\) are independently optional. This gives \(2^{M-1}\) families per fixed empty flag, while each sentinel class has one family. Therefore the two modalities each have exactly \(2(n+1)\) signatures.

**Whole-model and homogeneous consequences.** Suppose two persistent frames on the same chain have matching local box and diamond signatures at each world. Their algebraic modal operations agree on all upsets at each world; structural induction on the positive formula syntax shows equality of truth sets for every common persistent valuation. Conversely, if the interpretations agree on every formula under every such valuation, assign fresh variables the upsets appearing in the distinguishing nullary/unary tests above. Their differing local signatures would then produce different truth values at that world, a contradiction. Thus local-profile equality is necessary and sufficient for whole-model equivalence.

For homogeneous frames, arbitrary constant choices \(N^{\Box}(w)=N^{\Box}\) and \(N^{\Diamond}(w)=N^{\Diamond}\) obey persistence. Their local signatures range independently, giving \((2n+2)^2\) joint signatures. The largest box fiber has \(2^{n-1}\) members (choose \(m=1\)); the largest diamond fiber has \(2^{n-1}\) members (choose \(M=n\)). Independent choices multiply to \(4^{n-1}\), attaining the bound. All claims hold for \(n=1\) as well.

## Verification

A standalone Python checker directly evaluates the two semantic clauses over all upset arguments through unary instance arity, for every local neighbourhood family on chains of sizes \(1\le n\le6\). It confirms that the proposed profile is precisely the observational equivalence class, that both modalities have \(2n+2\) signatures, and that each class has the derived exact cardinality. For sizes \(1\le n\le4\), it independently checks the binary-to-unary reductions for every family and all ternary combinations of upset arguments. Direct output terminates with `ALL_CHECKS_OK`.

These finite computations do not establish the unbounded statements; the preceding quantified arguments supply the proofs for all \(n\ge1\) and all finite instance arities.

## Relationship to prior work

Das, Khanra, and Sardar (2026) introduce positive two-sided instantial-neighbourhood semantics, persistent frames and their algebraic interpretation. Their representation and completeness results motivate the question of which features of a concrete neighbourhood frame are actually observable by its positive modal operators. The exact finite-chain observational quotient, its fiber cardinalities and the uniform reduction from arbitrary instance arity to unary are not among the results located in the inspected semantic and representation sections.

De Groot's 2026 Thomason duality develops the original (classical) instantial operations on arbitrary powerset arguments and reconstructs full neighbourhood membership by naming each element through singleton instance arguments. A separately published finite-frame reconstruction result gives a sharp cutoff equal to the carrier size in that **unrestricted Boolean** setting. Those observations do not imply exact identifiability here: the *persistent positive* language has only upsets as inputs, so most neighbourhood membership bits are invisible even when all instance arities are allowed. The new statement goes in the opposite direction, identifying exact observational fibers for an explicitly more restricted semantic domain.

De Groot's 2022 study of arity-indexed INL fragments is relevant to modal arity but is not the same two-sided positive finite-chain semantics; full text was unavailable for a decisive all-theorem priority comparison. Related finite-chain Kripke relation normal forms classify binary relations under different modalities and do not entail the present neighbourhood-family quotient.

## Limitations

The exact global signature count \((2n+2)^2\) and largest fiber \(4^{n-1}\) are asserted only for the *homogeneous* subclass with both families constant across worlds, not for all persistent frames. The local normal forms and all-arity collapse hold for arbitrary persistent two-sided neighbourhood frames on chains. Observational equivalence compares two models on the same fixed, labelled, ordered carrier; it does not classify them up to isomorphism. The result does not apply to arbitrary non-linear finite posets, all-subset classical instantial semantics, or settings that exclude empty upset/neighbourhood families by additional axioms. Independent external mathematical validation and exhaustive historical priority certification have not been performed.

## References

1. Litan Kumar Das, Anupam Khanra, and Sujit Kumar Sardar, *Positive Instantial Neighbourhood logic: Typed Completeness and Admissible-Open Representation*, arXiv:2606.08083, initial submission 6 June 2026. https://arxiv.org/abs/2606.08083
2. Jim de Groot, *Thomason Duality for Instantial Neighbourhood Frames*, Journal of Symbolic Logic (2026). DOI:10.1017/jsl.2026.10202.
3. Johan van Benthem, Nick Bezhanishvili, Sebastian Enqvist, and Junhua Yu, *Instantial Neighbourhood Logic*, Review of Symbolic Logic 10 (2017), 116–144. DOI:10.1017/S1755020316000447.
4. Jim de Groot, *Hennessy-Milner and Van Benthem for Instantial Neighbourhood Logic*, Studia Logica 110 (2022), 717–743. DOI:10.1007/s11225-021-09975-w.
5. *Sharp finite instance-arity cutoff for instantial neighbourhood frames*, mathematical research record, October 2026. https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-sharp-finite-instance-arity-cutoff-for-instantial-neighbourhood--d0e614d1df15/RESULT.md
