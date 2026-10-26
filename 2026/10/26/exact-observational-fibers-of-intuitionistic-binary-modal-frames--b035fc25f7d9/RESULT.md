# Exact observational fibers of intuitionistic binary-modal frames on finite chains

## Finding

Let \(C_n=\{0<1<\cdots<n-1\}\) be a fixed, labelled finite chain, \(n\ge1\), and let \(R\subseteq C_n^3\) satisfy the two binary-modal monotonicity conditions of Kaminski's semantics, stated below. The first coordinate is the evaluation world. For \(i\in C_n\) set
\[
R_i=\{(v,w):(i,v,w)\in R\},\quad D_i=\downarrow R_i,\quad S_i=\bigcup_{t\ge i}R_t,\quad S_n=\varnothing.
\]
The arrows are coordinatewise closure in \(C_n^2\). Call two such relations *pointwise observationally equivalent* if, for every common hereditary valuation of all propositional variables, every formula of intuitionistic propositional logic with Kaminski's existential binary modality \(\circ\) and universal binary modality \(\bullet\) has the same truth value at each labelled world in the two models.

**Observational classification.** Two relations are pointwise observationally equivalent if and only if their entire \((D_i,S_i)_{i<n}\) records coincide. Already the depth-one instances \(p\circ q\) and \(p\bullet q\), with two independent hereditary propositional valuations (including the empty valuation), separate any unequal records.

**Exact fibers and canonical representatives.** For any attained record, let \(M_i=\operatorname{Max}(D_i)\), its product-order maximal elements, and define
\[
L_i=M_i\cup(S_i\setminus S_{i+1}),\qquad H_i=D_i\cap S_i.
\]
The equivalent valid frames with this record are *exactly* the independent choices of rows \(Q_i\) satisfying \(L_i\subseteq Q_i\subseteq H_i\). Consequently every observational fiber is a Boolean interval and its cardinality is
\[
\boxed{\displaystyle
2^{\sum_{i=0}^{n-2}\left|(D_i\cap S_{i+1})\setminus M_i\right|}.}
\]
The frames with rows \(L_i\) and \(H_i\) are respectively the unique least and greatest representatives under relation inclusion.

**Sharp uniform redundancy.** Among all observational fibers of legal frames on \(C_n\), the maximum number of members is exactly
\[
\boxed{\displaystyle 2^{(n-1)(n^2-1)}.}
\]
For \(n=2\), the 256 possible ternary relations include exactly 67 legal frames partitioned into 45 observational classes: 33 singleton fibers, nine two-element fibers, two four-element fibers, and one eight-element fiber. These finite counts are diagnostics, not the basis of the all-\(n\) theorem.

## Assumptions and scope

The order \(\le\) is the displayed chain order. In a modal frame \((C_n,\le,R)\), Kaminski's frame conditions are:

(M1) For every \((i,v,w)\in R\) and every \(j\ge i\), there exist \(v'\ge v\) and \(w'\ge w\) such that \((j,v',w')\in R\).

(M2) For every \((i,v,w)\in R\) and every \(v'\ge v,w'\ge w\), there is a \(j\ge i\) with \((j,v',w')\in R\).

A hereditary valuation makes each propositional variable true on an upper set \(U_a=\{j\in C_n:j\ge a\}\), where \(0\le a\le n\) and \(U_n=\varnothing\). Formulas use intuitionistic implication, its usual propositional connectives, and the two binary modalities, with semantic clauses
\[
i\Vdash A\circ B\iff\exists(v,w)\in R_i:\ v\Vdash A\text{ and }w\Vdash B,
\]
\[
i\Vdash A\bullet B\iff\forall t\ge i\ \forall(v,w)\in R_t:\ v\Vdash A\text{ or }w\Vdash B.
\]
Equivalence is at each named world for every formula and every common valuation, not merely equality of valid formulas. No commutativity, associativity, seriality or nonemptiness assumption is imposed on \(R\).

## Proof

**1. Shadow normal form for the legal relations.** From (M1) with \(j=i+1\) we get \(D_i\subseteq D_{i+1}\): each element below some row-\(i\) pair remains below a row-\(i+1\) witness. Conversely, these consecutive inclusions give (M1) for arbitrary \(j\ge i\) by iteration. Condition (M2) states exactly that each suffix union \(S_i\) is a coordinatewise upper set: a pair in \(S_i\) comes from a row \(j\ge i\), and its coordinatewise enlargements occur in some row at or after \(j\). Conversely, if every \(S_i\) is an upper set, each enlargement of a pair in \(R_i\) belongs to \(S_i\), proving (M2). Thus legality is equivalent to the two simple shadow conditions
\[
D_0\subseteq D_1\subseteq\cdots\subseteq D_{n-1},\qquad S_i=\uparrow S_i\text{ for all }i.
\]

**2. Depth-one recovery of both shadows.** Evaluate \(p\circ q\) with \(p\) true exactly on \(U_a\) and \(q\) true exactly on \(U_b\), for \(0\le a,b<n\). Its truth at \(i\) is equivalent to the existence of a pair in \(R_i\) dominating \((a,b)\), hence equivalent to \((a,b)\in D_i\). This recovers every bit of \(D_i\).

Now fix \((a,b)\in C_n^2\), and evaluate \(p\bullet q\) with \(p\) true exactly on \(U_{a+1}\), \(q\) true exactly on \(U_{b+1}\) (the value \(n\) represents the empty upper set). The formula fails at \(i\) precisely if there is \((v,w)\in S_i\) with \(v\le a,w\le b\), i.e. \((a,b)\in\uparrow S_i\). Since legality gives \(S_i=\uparrow S_i\), the failure test recovers exactly the membership relation of \(S_i\). Thus differing shadows are separated already at depth one.

**3. All-depth sufficiency.** Under (M1)--(M2), every formula is hereditary: the propositional induction is standard, for \(\circ\) use (M1), and for \(\bullet\) its universal quantification over all later rows is automatically hereditary. Therefore the truth sets of the two inputs to either binary modality are upper sets \(U_a,U_b\). For \(\circ\), the output at \(i\) depends only on the membership of \((a,b)\) in \(D_i\). For \(\bullet\), failure depends only on \((a-1,b-1)\in S_i\) when \(a,b\ge1\); more generally it depends on whether \(S_i\) meets \(\{v<a,w<b\}\), which is decided by \(S_i\) even when \(a=0\) or \(b=0\). The intuitionistic connectives depend only on their input truth sets and the shared order. Induction on formula complexity now proves agreement of every nested formula whenever the records agree.

**4. Exact interval of presentations.** Fix an attained record \((D_i,S_i)\). Every row \(Q_i\) of a realization lies in \(D_i\cap S_i\). Because \(D_i=\downarrow Q_i\), every maximal element of \(D_i\) must lie in \(Q_i\) (finiteness and maximality). Because \(S_i=Q_i\cup S_{i+1}\), every element of \(S_i\setminus S_{i+1}\) must also lie in \(Q_i\). Hence \(L_i\subseteq Q_i\subseteq H_i\).

Conversely, any row choices inside these intervals satisfy \(\downarrow Q_i=D_i\), since they contain all of \(M_i\) and lie inside \(D_i\). Descending induction on \(i\), beginning with \(S_n=\varnothing\), gives \(Q_i\cup\bigcup_{t>i}Q_t=S_i\): mandatory newly appearing elements are supplied by \(L_i\), and no extraneous elements appear because \(Q_i\subseteq S_i\). The resulting relation is legal by Step 1, and it has the prescribed records. Choices are independent between rows, so the fiber is a product of Boolean intervals. The optional pairs in row \(i<n-1\) are precisely \((D_i\cap S_{i+1})\setminus M_i\). Row \(n-1\) is forced, since \(S_{n-1}=Q_{n-1}\). The displayed power-of-two formula follows, as does uniqueness of the least and greatest frame.

**5. Sharp fiber bound.** Each optional set for \(i<n-1\) has size at most \(n^2-1\): if \(D_i\ne\varnothing\), it has at least one maximal member, and if it is empty there are no optional pairs. Thus the fiber has size at most \(2^{(n-1)(n^2-1)}\). Equality is attained by taking every row to be all of \(C_n^2\). Its shadows are \(D_i=S_i=C_n^2\) for all \(i\). In its fiber the top row remains full, while each earlier row may contain any subset provided it includes the single pair \((n-1,n-1)\). There are exactly \(2^{(n-1)(n^2-1)}\) such relations. This includes the boundary case \(n=1\).

## Verification

The standalone implementation in `checker.py` reconstructs both frame conditions directly from the quantified definitions and separately from the two shadow conditions. It computes the two modal truth tables on every pair of hereditary propositional truth sets, checks the fiber reconstruction and exact fiber powers, and verifies that distinct observed shadows produce distinct modal operation tables. It exhausts all \(2\) ternary relations at \(n=1\) and all \(256\) ternary relations at \(n=2\), and tests 5,000 additional legal \(n=3\) relations plus members of the extremal family. The successful output is `ALL_CHECKS_OK` together with the exact \(n=2\) counts stated above. The infinite family of theorems is proved by Steps 1--5, not inferred from these finite tests.

## Relationship to prior work

Kaminski (2026) introduces the paired intuitionistic binary-modal semantics and proves completeness, providing exactly the two ternary frame monotonicity conditions analyzed here. The new result is a semantic classification **within** his finite-chain frames: it identifies the full observation quotient and the precise, sometimes exponentially large, fibers of relation presentations, neither of which is given by the published semantic clauses alone.

Kaminski (2024) studies undecidability of associative binary-modal logics via semigroup encodings rather than observational equality of non-associative, two-operator chain frames. Aloni and collaborators (2026) study a classical binary fusion modality interpreted by semilattice suprema, not arbitrary ternary accessibility with Kaminski's two confluences. Related finite-chain results for unary birelational modal frames depend on one-dimensional successor boundaries; they do not imply the present two-dimensional row/suffix-shadow fiber theorem.

## Limitations

The characterization concerns *all valuations and pointwise equivalence* on one fixed labelled finite chain. It does not characterize equivalence of frame-validity theories, bisimulation between differently labelled or ordered carriers, arbitrary partial orders, or frames constrained by extra associativity or commutativity axioms. For broad historical priority, equivalent descriptions may exist in older algebra-with-operators, binary-modality or ordered-relation literature; the inspected texts and searches do not establish absolute priority. The finite checker is diagnostic, not an independent audit or a substitute for the proof.

## References

1. M. Kaminski, *Intuitionistic logic of a binary modality*, Archive for Mathematical Logic, published 2026-09-09, DOI: 10.1007/s00153-026-01025-3. https://link.springer.com/article/10.1007/s00153-026-01025-3
2. M. Kaminski, *On undecidability of the propositional logic of an associative binary modality*, Archive for Mathematical Logic 63 (2024), 837--857, DOI: 10.1007/s00153-024-00921-w. https://link.springer.com/article/10.1007/s00153-024-00921-w
3. M. Aloni, A. Baltag, J. van Benthem, N. Bezhanishvili, and S. B. Knudstorp, *Teams, Truthmakers, Translations*, first posted 2026-10-11, arXiv:2610.15680. https://arxiv.org/html/2610.15680
