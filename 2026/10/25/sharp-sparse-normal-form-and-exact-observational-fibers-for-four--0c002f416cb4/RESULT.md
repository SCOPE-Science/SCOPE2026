# Sharp sparse normal form and exact observational fibers for four intuitionistic modalities

## Finding

Fix an integer \(n\geq 1\) and the labelled intuitionistic chain
\[
C_n=\{0<1<\cdots<n-1\}.
\]
A frame consists of \(C_n\) and an **arbitrary** binary relation \(R\subseteq C_n\times C_n\), without seriality or confluence assumptions. Use the four primitive modalities of Balbiani--Gencer: Prenosil possibility \(\Diamond_P\), its box \(\Box_P\), Wijesekera possibility \(\Diamond_W\), and its dual box \(\Box_W\). Propositional valuations are upward-closed.

For every row \(R(i)=\{j:iRj\}\), put
\[
\ell_i=\begin{cases}\min R(i),&R(i)\ne\varnothing,\\ n,&R(i)=\varnothing,\end{cases}
\qquad
h_i=\begin{cases}\max R(i),&R(i)\ne\varnothing,\\-1,&R(i)=\varnothing.\end{cases}
\]
Define the **four-extrema signature**
\[
P_i=\max_{t\le i}h_t,\quad
Q_i=\min_{t\ge i}\ell_t,\quad
D_i=\min_{t\ge i}h_t,\quad
E_i=\max_{t\le i}\ell_t.
\]
Then two relations on this labelled chain are observationally equivalent under **all** upward-closed valuations and **all** formulas in the full four-modal intuitionistic language (including implication and coimplication) **if and only if** their signatures \((P,Q,D,E)\) coincide. Equivalence is pointwise at corresponding worlds; it is stronger than equality of the two frames' valid formulas.

Every such equivalence class has a representative with **at most two outgoing edges per world**, obtained by retaining only each nonempty row's minimum and maximum. The global bound of \(2n\) edges is attained and cannot be reduced for every \(n\ge2\). (For \(n=1\), one edge suffices.) Moreover, the four primitive modal operations each supply information not determined by the other three, already for \(n=2\).

The theorem also gives the **exact size of every observational-equivalence class**. A candidate signature \(s=(P,Q,D,E)\) is attainable exactly when every local choice set \(\mathcal A_i(s)\), defined below, is nonempty; for attainable \(s\),
\[
\boxed{\ |[s]|=\prod_{i=0}^{n-1}\ \sum_{(a,b)\in\mathcal A_i(s)} w_n(a,b)\ }.
\]
Here \((a,b)\) ranges over the admissible endpoint pairs
\[
\mathcal L_n=\{(n,-1)\}\ \cup\ \{(a,b):0\le a\le b<n\},
\]
and its relation multiplicity is
\[
w_n(a,b)=\begin{cases}2^{b-a-1},&0\le a<b<n,\\1,&a=b\text{ or }(a,b)=(n,-1).\end{cases}
\]
With boundary values \(P_{-1}=E_{-1}=-1\) and \(Q_n=D_n=n\), the set \(\mathcal A_i(s)\) contains precisely those \((a,b)\in\mathcal L_n\) satisfying
\[
P_i=\max(P_{i-1},b),\quad E_i=\max(E_{i-1},a),\quad
Q_i=\min(a,Q_{i+1}),\quad D_i=\min(b,D_{i+1}).
\]
This supplies a finite, explicit decision test for attainable signatures and their fiber sizes, without enumerating all binary relations.

The exact numbers of observational classes on the first four chains are
\[
\boxed{2,\ 16,\ 279,\ 7171}\quad(n=1,2,3,4),
\]
out of respectively \(2,16,512,65536\) raw relations. The largest fiber sizes are respectively \(1,1,8,324\).

## Assumptions and scope

The order \(\le\) is the fixed total order on \(C_n\). The relation \(R\) is unrestricted; empty rows are permitted and require the stated endpoint sentinels. A valuation assigns each propositional variable an upward-closed subset of \(C_n\). Both intuitionistic implication and coimplication use the standard order clauses.

For any upward-closed truth set \(U\subseteq C_n\), the four semantic clauses at world \(i\) are
\[
\begin{aligned}
i\vDash\Diamond_P U&\iff\exists t\le i\ \exists u\in R(t):u\in U,\\
i\vDash\Box_P U&\iff\forall t\ge i\ \forall u\in R(t):u\in U,\\
i\vDash\Diamond_W U&\iff\forall t\ge i\ \exists u\in R(t):u\in U,\\
i\vDash\Box_W U&\iff\exists t\le i\ \forall u\in R(t):u\in U.
\end{aligned}
\]
The universal quantification over an empty row is true, and the existential quantification over an empty row is false. The modalities preserve upward closure, as do the other connectives, so they act on the lattice of upward-closed subsets.

An observational class is formed only among frames on the **same fixed labelled chain**, with common valuation assignments. It is not a classification up to abstract frame isomorphism, elementary equivalence, or validity alone. The fiber cardinality counts raw binary relations and not syntactic formulas.

## Proof

**Step 1: the signature is exactly the observable one-step data.** Every upward-closed subset is \(U_k=\{k,k+1,\ldots,n-1\}\) for a unique \(0\le k\le n\), with \(U_n=\varnothing\). For a row with endpoints \((\ell_t,h_t)\),
\[
R(t)\cap U_k\ne\varnothing\iff h_t\ge k,
\qquad
R(t)\subseteq U_k\iff\ell_t\ge k.
\]
The two equivalences remain correct when the row is empty because \(h_t=-1\) and \(\ell_t=n\). Substituting into the four semantic clauses yields
\[
\begin{array}{c|c}
\text{operator on }U_k&\text{truth at }i\\\hline
\Diamond_P& P_i\ge k\\
\Box_P&Q_i\ge k\\
\Diamond_W&D_i\ge k\\
\Box_W&E_i\ge k
\end{array}
\]
Therefore equal signatures give equal one-step operations on every upward-closed set. Structural induction on formulas gives equal truth at each world for every common valuation, including nested modalities, implication, and coimplication. Conversely, assigning a single variable \(p\) the value \(U_k\), and testing the four atomic modal formulas at each world for all \(k\), recovers every signature entry from its threshold comparison. Thus observational equivalence implies equal signatures.

**Step 2: complete fiber normal form.** For any candidate signature, the prefix-extrema definitions give
\[
P_i=\max(P_{i-1},h_i),\qquad E_i=\max(E_{i-1},\ell_i),
\]
while the suffix-extrema definitions give
\[
Q_i=\min(\ell_i,Q_{i+1}),\qquad D_i=\min(h_i,D_{i+1}),
\]
with the stated boundary conventions. Accordingly, each row's endpoints must lie in \(\mathcal A_i(s)\). Conversely, choosing any pair from every \(\mathcal A_i(s)\) and forming any row with precisely those endpoints realizes the signature, by forward induction for the prefix arrays and backward induction for the suffix arrays. Thus the nonemptiness of all local choice sets is necessary and sufficient for attainability, and the endpoint choices at different indices are genuinely independent. A nonempty row with \(a<b\) must contain its two endpoints and may contain any subset of its \(b-a-1\) interior elements, giving \(2^{b-a-1}\) possibilities. Empty and singleton rows have one realization. Multiplying their summed multiplicities proves the exact fiber formula.

**Step 3: sharp sparse representation.** Delete from each row every element strictly between its minimum and maximum, retaining both endpoints or the singleton or emptiness as appropriate. This keeps \((\ell_i,h_i)\) unchanged, hence keeps the four-extrema signature and all modal truths unchanged, using at most two edges per row.

To prove optimality for \(n\ge2\), take the relation with
\[
R(i)=\{i,i+1\}\quad(0\le i<n-1),\qquad
R(n-1)=\{n-2,n-1\}.
\]
Its row minima are \(0,1,\ldots,n-2,n-2\), and its row maxima are \(1,2,\ldots,n-1,n-1\). For \(i<n-1\), the prefix record \(E_i=i\), with the previous record strictly smaller (or the initial boundary at \(i=0\)), forces any equivalent relation to have \(\ell_i=i\). At the last row, \(Q_{n-1}=n-2\) forces its minimum. Every row's maximum is forced by \(D_i=h_i\), since its maxima sequence is nondecreasing. Thus **each** of the \(n\) rows of every equivalent relation contains both distinct prescribed endpoints, and at least \(2n\) edges are necessary. This proves sharpness.

**Step 4: none of the four operators is redundant.** On the two-world chain, omitting respectively \(\Diamond_P,\Box_P,\Diamond_W,\Box_W\), the following pairs of row lists have identical operations for the remaining three operators but differ on the omitted operator:
\[
\begin{array}{c|c|c}
\text{omitted}&(R(0),R(1))&(S(0),S(1))\\\hline
\Diamond_P&(\{0\},\varnothing)&(\{0,1\},\varnothing)\\
\Box_P&(\varnothing,\{1\})&(\varnothing,\{0,1\})\\
\Diamond_W&(\{1\},\{0\})&(\{1\},\{0,1\})\\
\Box_W&(\{1\},\{0\})&(\{0,1\},\{0\})
\end{array}
\]
Direct substitution into the four signature arrays verifies each pair. No other primitive operator is therefore determined by the remaining three as an operation on all upward-closed sets.

**Step 5: finite census.** By Step 1 the number of observational classes is the number of distinct attainable signatures. The standalone checker enumerates all binary relations for \(1\le n\le4\), forms signatures, and independently verifies the signature's four modal truth conditions for every upward-closed input. It also groups the relations by signature and independently recalculates the group sizes using the local endpoint formula. The resulting exact class counts and largest fibers are those stated above. This finite census is supported by exhaustive enumeration; the general equivalence, fiber formula, and sharp sparse bound follow from Steps 1--4 for all \(n\).

## Verification

Run `python3 checker.py` after extracting the standalone package files. The checker needs only the Python standard library. It enumerates \(2^{n^2}\) relations for \(1\le n\le4\), compares the original quantifier clauses with the four signature threshold tests for every \(U_k\), and checks every signature fiber against its independent rowwise factorization. It also checks the sharp family through \(n=12\) and finds a witness that each primitive operator is indispensable at \(n=2\). Its expected final line is `ALL_CHECKS_OK 337329`.

The checker does not enumerate relations for unbounded \(n\), and the finite results are not used as a substitute for the unrestricted proof.

## Relationship to prior work

Balbiani and Gencer (2026) introduce the four primitive modal clauses for arbitrary preordered frames and establish their heredity and general proof-theoretic properties. The clauses in their Section 3.4 are the definitions used here. Their work concerns correspondence, axiomatization, and decidability; the inspected sections do not give this chain-specific observational quotient, its exact equivalence fibers, or the sharp two-edge bound.

Related finite-chain results in the literature describe **special classes of relations that satisfy confluence conditions**, sometimes by monotone row minima and maxima or by row and column endpoints. Those classify which relations are permitted under additional frame axioms and count raw relations. The present result assumes **no confluence** and classifies when arbitrary relations are indistinguishable by all four modal operations. Neither direction of implication follows from the confluence classifications: signatures are prefix/suffix records of row endpoints, not monotonicity constraints on endpoints, and the exact fibers count multiple indistinguishable raw relations.

The general duality and correspondence frameworks for modal lattice expansions provide important conceptual background but do not themselves give these finite-chain numerical fibers or their sharp sparse representatives in the material inspected.

## Limitations

This theorem is for finite chains and unrestricted upward-closed valuations. It does not provide a constant two-edge bound on arbitrary posets, where a row may have many incomparable extreme elements. The observational equivalence is **common-valuation, pointwise equivalence**, not equality of frame validities under unrelated valuations, and is not a classification of formulas up to theoremhood. The exact fiber product formula is finite but does not simplify here to a closed expression for the total number of classes for arbitrary \(n\); only the first four class counts are enumerated. Independent external validation has not been performed. Older distributive modal-algebra or relation-hull literature might express the same quotient in different terminology; priority beyond inspected sources is not established.

## References

[1] Philippe Balbiani and Çiğdem Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348v1, first posted June 5, 2026. Section 3.4 defines all four semantics; Sections 4--5 study expressivity and correspondence. https://arxiv.org/abs/2606.07348

[2] Jim de Groot, Ian Shillito, and Ranald Clouston, *Duality for Constructive Modal Logics: from Sahqlvist to Goldblatt-Thomason*, arXiv:2601.03762, January 7, 2026. https://arxiv.org/abs/2601.03762

[3] Rodrigo Nicolau Almeida and Nick Bezhanishvili, *Coalgebraic Semantics for Intuitionistic Modal Logic*, *Advances in Modal Logic 15* (2024), pp. 59--77; arXiv:2406.10649. https://arxiv.org/abs/2406.10649
