# A one-variable generator for every finite Boolean compatibility frame

## Finding

**Theorem (sharp modal generating rank).** For every integer \(n\geq 1\), let
\[
W_n=\mathcal P(\{1,\ldots,n\})\setminus\{\varnothing\},\qquad
S\,R_n\,T\ \Longleftrightarrow\ S\cap T\ne\varnothing,
\]
and let \(\mathcal A_n\) be the **full** complex modal algebra
\[
\big(\mathcal P(W_n),\cap,\cup,\neg,\varnothing,W_n,\Diamond\big),
\qquad
\Diamond X=\{S\in W_n:\exists T\in X\ (S\cap T\ne\varnothing)\}.
\]
Here \(\neg\) is complement *within* \(W_n\), not complement of a Boolean-algebra state inside \(\{1,\ldots,n\}\).

Let \(P_n=\{S\in W_n:\min(S)\text{ is odd}\}\). For every \(n\geq2\), the smallest modal subalgebra containing \(P_n\) equals all of \(\mathcal A_n\). Accordingly, the least number of generators of \(\mathcal A_n\) as a Boolean algebra **with** \(\Diamond\) is exactly \(1\) for \(n\geq2\), and \(0\) for \(n=1\). The underlying pure Boolean algebra requires exactly \(n\) generators for \(n\geq2\), and \(0\) for \(n=1\).

Equivalently, interpreting a single modal propositional variable \(p\) by \(P_n\), **every** subset of worlds is definable by a finitary formula in \(p\), Boolean connectives and \(\Diamond\). In particular, every individual nonempty Boolean state is definable by a one-variable formula. These claims concern the unrestricted propositional complex algebra, not restricted set-theoretic parameter valuations.

## Assumptions and scope

The atoms \(1,\ldots,n\) are labelled and linearly ordered solely to specify \(P_n\). Worlds are the nonempty subsets of this atom set; accessibility is nonempty intersection, including the reflexive loops. All modal valuations are arbitrary elements of \(\mathcal P(W_n)\) for the complex-algebra assertion. The valuation \(p\mapsto P_n\) is permitted in that unrestricted setting.

In the internal forcing semantics of Jockwich, Tarafder and Venturi, a propositional parameter with Boolean value \(a\) instead has the *principal-downset* extension \(\{b\in W_n:b\subseteq a\}\). For \(n\geq3\), \(P_n\) is generally **not** such a downset. This theorem neither states nor requires one-generator expressibility under that restricted translation convention; no equivalence between the two valuation classes is assumed.

## Proof

**1. Modal support identity.** For any \(X\subseteq W_n\), put \(U(X)=\bigcup_{T\in X}T\), a subset of the *base atom set*. Directly from the existential clause,
\[
\Diamond X=\{S\in W_n:S\cap U(X)\neq\varnothing\}.
\tag{1}
\]
In particular, \(\Diamond\{\{k\}\}=\{S:k\in S\}\).

**2. One-variable definitions of singleton worlds.** In the following recurrence, all expressions are modal formulas, evaluated under \(p\mapsto P_n\). Define \(\tau_1=\top\). For \(1\leq k<n\), put
\[
\rho_k=\begin{cases}p&k\text{ even},\\\neg p&k\text{ odd},\end{cases}
\quad q_k=\tau_k\wedge\rho_k,\quad
\epsilon_k=\tau_k\wedge\neg\Diamond q_k,\quad
h_k=\Diamond\epsilon_k,\quad
\tau_{k+1}=\tau_k\wedge\neg h_k.
\tag{2}
\]
At \(k=n\), put \(\epsilon_n=\tau_n\) and \(h_n=\Diamond\epsilon_n\).

We prove, for each \(1\leq k\leq n\), that
\[
\llbracket\tau_k\rrbracket=\{S\in W_n:S\subseteq\{k,\ldots,n\}\},\qquad
\llbracket\epsilon_k\rrbracket=\{\{k\}\},\qquad
\llbracket h_k\rrbracket=\{S\in W_n:k\in S\}.
\tag{3}
\]
For \(k=1\), the first equality follows from \(\tau_1=\top\). Suppose the first equality holds at \(k<n\). Within that tail, \(q_k\) selects worlds whose minimum has parity opposite to \(k\). Such worlds cannot contain \(k\), so the union of their constituent atoms is contained in \(\{k+1,\ldots,n\}\). Conversely, the specific nonempty world \(\{k+1,\ldots,n\}\) belongs to \(q_k\), because its minimum \(k+1\) has opposite parity. Hence
\[
U(\llbracket q_k\rrbracket)=\{k+1,\ldots,n\}.
\tag{4}
\]
By (1), a world in \(\llbracket\tau_k\rrbracket\) fails \(\Diamond q_k\) precisely when it is disjoint from \(\{k+1,\ldots,n\}\). Since worlds are nonempty, the **only** such world is \(\{k\}\). Thus \(\llbracket\epsilon_k\rrbracket=\{\{k\}\}\), and (1) gives the claimed meaning of \(h_k\). Removing worlds containing \(k\) leaves precisely the tail worlds supported on \(\{k+1,\ldots,n\}\), establishing the induction. For \(k=n\), \(\llbracket\tau_n\rrbracket=\{\{n\}\}\), so \(\epsilon_n=\tau_n\) and the remaining equalities hold as well.

**3. All worlds and all propositions.** For any nonempty \(S\subseteq\{1,\ldots,n\}\), form
\[
\chi_S=\bigwedge_{i\in S}h_i\ \wedge\ \bigwedge_{i\notin S}\neg h_i.
\tag{5}
\]
By (3), \(\llbracket\chi_S\rrbracket=\{S\}\) exactly. Every \(X\subseteq W_n\) is the finite union \(\bigcup_{S\in X}\{S\}\), so a finite disjunction of the \(\chi_S\) defines \(X\); the empty union is \(\bot\). All these formulas use **only** \(p\). Thus \(P_n\) generates \(\mathcal A_n\).

**4. Sharpness and the Boolean comparison.** For any \(n\), \(\Diamond\varnothing=\varnothing\) and \(\Diamond W_n=W_n\). Consequently the subalgebra with **zero** designated generators consists only of \(\varnothing\) and \(W_n\). This is the whole algebra exactly when \(n=1\). For \(n\geq2\), \(|W_n|=2^n-1\geq3\), so at least one generator is necessary, proving sharpness.

In a pure Boolean algebra, \(r\) generators induce at most \(2^r\) Boolean atoms. The Boolean atoms of \(\mathcal P(W_n)\) are the \(2^n-1\) singleton-world sets, hence \(r\geq\lceil\log_2(2^n-1)\rceil=n\) when \(n\geq2\). Conversely the \(n\) coordinate sets \(\{S:i\in S\}\), which are available as abstract Boolean generators whether or not they are independently named, separate every world and generate the full powerset. For \(n=1\) the two-element Boolean algebra needs zero generators. This completes the proof.

## Verification

The included standalone `checker.py` implements \(\Diamond\) directly using subset-intersection tests on bit masks, and independently constructs the recursive formulas \(\tau_k,\epsilon_k,h_k\). It tests their asserted truth sets, the union identity (4), and every point-isolating Boolean combination (5) for all \(1\leq n\leq11\). A separate modal partition-refinement calculation, based on one-step successor-color signatures rather than the explicit formula recursion, reaches discrete world partitions for \(1\leq n\leq8\). Run `python3 checker.py`; the recorded diagnostic result is `ALL_CHECKS_OK`. These finite checks do not establish the infinite family by themselves: the proof above does.

## Relationship to prior work

Jockwich, Tarafder and Venturi's 2026 study introduces the relevant Boolean compatibility relation and studies the associated modal logic and finite complete atomic Boolean algebras. Its Sections 5–6 analyze *translation-based principal-downset valuations*, global \(\mathsf{KTB}\) completeness, and finite-stage logic inclusions; the inspected text does not give a one-generator theorem for the **full** complex algebra under unrestricted valuations. Its fixed-algebra logic results are not equivalent to the present generating-rank assertion.

The general theory of modal/complex algebras and one-generated fragments is older. For example, Kostrzycka's 2006 treatment concerns one-variable Lindenbaum algebras for \(\mathsf{S5}\) and finite-depth Grzegorczyk logics. Those are not the full complex algebra of the labelled nontransitive Boolean-compatibility frames considered here. The normal-form support argument (1)–(5) is the source of the specific claim, not a consequence claimed from a generic one-variable fragment count.

A related published finite-stage result proves strictness of a hierarchy of forcing-inspired modal **validity logics** and bounds bounded-morphic quotients. It neither identifies the least number of generators of a fixed complex algebra nor provides the parity valuation (2). A result on finite measurable modal quotients likewise classifies partial-function frames, a different class from these branching overlap frames.

## Limitations

The theorem concerns finite *fully populated* nonzero Boolean carriers. It does not assert that the same one-variable construction works on arbitrary induced subframes, infinite atom sets with non-well-founded order, or the paper's parameter-restricted Boolean-valued set-theoretic translations. In particular, one must not identify the parity-minimum proposition \(P_n\) with a single Boolean-valued sentence's principal-downset extension.

The explicit recursive formulas are constructive but are not claimed to minimize modal depth or formula length. The sharpness assertion addresses only the **number of propositional generators**. The present work has not received an independent scientific audit. Related older work on one-generated modal algebras could contain a statement equivalent to this specialized construction under different terminology.

## References

1. S. Jockwich, S. Tarafder, G. Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977, first posted 28 July 2026; especially Sections 5–6. https://arxiv.org/abs/2607.25977
2. Z. Kostrzycka, *On the density of truth in modal logics*, Discrete Mathematics & Theoretical Computer Science (2006), Sections 2–3. https://dmtcs.episciences.org/articles/3500/download
3. Standard complex-algebra semantics of Kripke frames and the Jónsson–Tarski representation tradition, for terminology and the general modal algebra context.
