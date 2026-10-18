# Sharp modal-depth cardinality types for binary-union information logic

## Finding
Fix a set \(U\), finite or infinite, and use the powerset join-semilattice \((\mathcal P(U),\cup)\). Interpret the designated atoms \(Z\) and \(A\) at an information state \(X\subseteq U\) by \(Z(X)\) iff \(X=\varnothing\) and \(A(X)\) iff \(|X|=1\). Formulas have Boolean connectives and one binary modality \(\langle\cup\rangle(\varphi,\psi)\), true at \(X\) iff \(X=Y\cup Z'\) for some \(Y,Z'\subseteq U\) satisfying \(\varphi,\psi\), respectively. The modality contributes one unit to modal nesting depth.

**Theorem.** For every \(d\ge0\), arbitrary sets \(U,V\), and points \(X\subseteq U\), \(Y\subseteq V\), agreement on **all** formulas of modal depth at most \(d\) is equivalent to equality of their truncated sizes:
\[
X\equiv_d Y\quad\Longleftrightarrow\quad \tau_d(|X|)=\tau_d(|Y|),\qquad
\tau_d(\kappa)=\begin{cases}\kappa,&\kappa\le 2^d,\\2^d+1,&\kappa>2^d.\end{cases}
\]
The cardinal \(\kappa\) can be infinite. Every individual size \(0,1,\ldots,2^d\) is expressible by a depth-\(d\) formula, as is the remaining class of larger finite and infinite sizes. Consequently there are exactly \(2^d+2\) pointed theories of depth at most \(d\), and exactly \(2^{2^d+2}\) equivalence classes of formulas of depth at most \(d\) modulo validity in all these marked powerset structures. If \(1\le n<m\) are finite, the least depth distinguishing a point of size \(n\) from one of size \(m\) is \(\lceil\log_2 n\rceil\); size zero is distinguished from every nonzero size already at depth zero.

## Assumptions and scope
The universe of a model is the **entire** powerset \(\mathcal P(U)\), including its empty element. The valuations of \(Z\) and \(A\) are fixed by the displayed cardinality conditions, not arbitrary propositional valuations. Splitting is **lax**: the two component subsets can overlap or be empty. The only modal operator is binary join; there is no converse, residual implication, finite-iteration modality, arbitrary least fixed point, or unrestricted predicate valuation. Boolean negation is available. The conclusion holds whether \(U\) and the designated point are finite or infinite. The usual syntactic nesting depth counts each application of \(\langle\cup\rangle\) once, and Boolean operations do not increase depth.

## Proof
Write \(t_d=2^d\), and let a rank-\(d\) size type be one of the integers \(0,\ldots,t_d\) or the tail symbol \(>t_d\). We prove simultaneously (I) invariance of each depth-\(d\) formula under equality of these types, and (II) existence of a depth-\(d\) characteristic formula \(E_{d,k}\) for each exact cardinality \(k\in\{0,\ldots,t_d\}\), valid over all sets \(U\).

At \(d=0\), the only atomic distinctions are \(Z\), \(A\), and their Boolean combinations. Hence (I) holds for types \(0\), \(1\), and \(>1\), while \(E_{0,0}:=Z\) and \(E_{0,1}:=A\) establish (II).

Assume (I) and (II) at depth \(d\), and set \(t=t_d\). Any modal child formula has a truth value determined solely by the size types \(0,\ldots,t,>t\). We analyze which pairs of such types can occur for two subsets \(B,C\subseteq X\) with \(B\cup C=X\).

For exact child types \(i,j\le t\), such a decomposition exists precisely when
\[
\max(i,j)\le |X|\le i+j.
\]
This follows by choosing an overlap of size \(i+j-|X|\), and is valid only for finite \(X\). If one child type is \(>t\) and the other is an exact \(j\le t\), then **every** \(X\) of cardinality \(>2t\), including infinite \(X\), admits such a decomposition: choose the first component to be \(X\) and the second to be a \(j\)-element subset of \(X\) (with the components interchanged if necessary). Two tail child types are realized by choosing both components to be \(X\). Conversely, for \(|X|>2t\), a pair of two exact child types is impossible because its union contains at most \(2t\) elements.

Thus for every pair of rank-\(d\) child types, its realizability at \(X\) is constant throughout the region \(|X|>2t\). When two points have the same size at most \(2t\), their unions of subsets have exactly the same cardinality-witness possibilities, independently of the ambient universes. Applying the induction hypothesis to the modal children proves invariance of every formula \(\langle\cup\rangle(\varphi,\psi)\) of depth at most \(d+1\). Boolean connectives preserve invariance. Hence (I) holds at depth \(d+1\).

For (II), retain \(E_{d+1,k}:=E_{d,k}\) for \(0\le k\le t\). For every \(t<k\le 2t\), define
\[
H_k:=\langle\cup\rangle(E_{d,t},E_{d,k-t}).
\]
By the exact-cardinality induction hypothesis and the union-cardinality criterion, \(H_k\) holds **exactly** at states of cardinality in the interval \([t,k]\). Starting with \(k=t+1\) and proceeding upward, set
\[
E_{d+1,k}:=H_k\land\bigwedge_{j=t}^{k-1}\neg E_{d+1,j}.
\]
Each new formula has depth at most \(d+1\); it is true exactly at size \(k\), by induction on \(k\). This proves (II) at depth \(d+1\). Moreover \(\neg\bigvee_{j=0}^{2t}E_{d+1,j}\) characterizes the tail class \(>2t\).

For any two different rank-\(d\) types, a characteristic formula distinguishes them, proving the reverse direction of the theorem. Every Boolean subset of the \(2^d+2\) types is definable by a disjunction of their characteristic formulas; conversely the invariance result makes every formula a union of whole types. This proves the exact number \(2^{2^d+2}\) of depth-bounded formula equivalence classes. Finally, for \(1\le n<m\), the two cardinalities are identified at depth \(d\) exactly when \(n>2^d\), so the first distinguishing depth is \(\lceil\log_2 n\rceil\), with equality cases covered by the exact-size formulas. This completes the proof.

## Verification
The standalone standard-library script `check_union_modal.py` implements two independent finite semantic calculations: direct enumeration of all subset decompositions in powersets, and a cardinality-only evaluator based on the exact interval criterion. It compares 35,770 direct subset/formula evaluations and 9,709 characteristic-formula evaluations on powersets of sizes \(0\) through \(8\). A separate finite-depth signature refinement for cardinalities through \(70\) returns the profile counts \(3,4,6,10,18,34\) for depths \(0\) through \(5\), matching \(2^d+2\). Run `python3 check_union_modal.py` in a directory containing the embedded checker file; the expected terminal prefix is `BINARY_UNION_DEPTH_VERIFY_OK`. These tests corroborate the proof only for bounded finite instances; they are not an infinite proof.

## Relationship to prior work
Aloni, Baltag, van Benthem, Bezhanishvili, and Knudstorp's 2026 *Teams, Truthmakers, Translations* introduces and studies modal information logic with a binary supremum modality and distributive semilattice models, and develops translations involving richer finite-suprema and fixed-point operations. The present theorem isolates the weaker **binary-only, fixed empty/singleton observation** fragment on complete powersets and derives an optimal, depth-indexed logical classification of pointed cardinalities. The inspected Sections 2–4 and relevant appendix portions of that paper do not supply this cardinality cutoff.

Knudstorp's 2025 *Diamonds and Dominoes* investigates the unrestricted modal/equational theory of binary union semilattices and proves undecidability; it does not state a finite-depth classification under the fixed marker valuations used here. Knudstorp's 2023 *Modal Information Logics: Axiomatizations and Decidability* concentrates on preorders and posets and expressly defers semilattice frame questions.

An earlier result entitled *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras* gives a superficially similar cutoff for **first-order quantifier rank** when comparing entire Boolean algebras in the Boolean-operation language. It neither treats the pointed binary-union modal language nor proves the formula-classification result here; the mechanisms and syntactic depth measures differ. However, general work on finite-rank Boolean algebra and modal bisimulation could conceivably yield the present specialization indirectly. Novelty is accordingly asserted only relative to the inspected statements, not as an exhaustive priority guarantee.

## Limitations
Fixed observations matter: with arbitrary propositional valuations, additional types are possible. The exact profile fails as a description of richer languages admitting residual implication, the finite-suprema star modality, arbitrary named elements, or other unrestricted modalities; no claim about those logics is made. This theorem concerns pointed information states and their modal depths, not general validity or complexity of arbitrary-valued modal information logic. The equivalence-class counts are semantic and do not bound the minimal **length** of distinguishing formulas. The proof is general for arbitrary sets, while the program tests finite examples only. Older uncatalogued or differently formulated depth-bisimulation theorems remain a literature-priority risk.

## References
1. M. Aloni, A. Baltag, J. van Benthem, N. Bezhanishvili, and S. B. Knudstorp, *Teams, Truthmakers, Translations*, arXiv:2610.15680v1 (first posted 2026-10-11), https://arxiv.org/html/2610.15680v1.
2. S. B. Knudstorp, *Diamonds and Dominoes: Impossibility Results for Associative Modal Logics*, arXiv:2506.16366v1 (first posted 2025-06-19), https://arxiv.org/html/2506.16366v1.
3. S. B. Knudstorp, *Modal Information Logics: Axiomatizations and Decidability*, Journal of Philosophical Logic 52 (2023), 1723–1766, https://doi.org/10.1007/s10992-023-09724-5.
4. *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras*, publicly accessible mathematical research record (2026-10-04), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-2-q-atom-visibility-threshold-for-finite-boolean-algebras--938cb5f89dc7/RESULT.md.
