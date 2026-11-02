# Peirce-law defects from boundary predecessors, with sharp rooted extremizers

## Finding
Let \(P\) be a nonempty finite poset and let \(H=J(P)\) be its Heyting algebra of downsets. Write \(h=|H|\), and count *ordered* counterexamples to Peirce's law by
\[
F(P)=\left|\{(A,B)\in H^2:((A\to B)\to A)\ne A\}\right|.
\]
For every downset \(A\), define its **minimal-exclusion predecessor boundary**
\[
S(A)=\bigcup_{p\in\operatorname{Min}(P\setminus A)}(\downarrow p\setminus\{p\}),
\]
where the union is empty when \(A=P\). This is itself a downset contained in \(A\). The following exact formula holds without hypotheses on the shape of \(P\):
\[
\boxed{F(P)=\sum_{A\in J(P)}\left(h-|J(P\setminus S(A))|\right).}
\]
Here \(P\setminus S(A)\) has the induced order. More precisely, an individual pair satisfies Peirce's identity if and only if \(S(A)\subseteq B\).

Suppose now that \(|P|\ge2\) and that \(P\) has a least element or a greatest element. Then
\[
\boxed{F(P)\ge h-2.}
\]
Equality holds **if and only if** \(P\) is isomorphic to \(A_1\oplus A_k\) or \(A_k\oplus A_1\) for some \(k\ge1\), where \(A_k\) denotes a \(k\)-element antichain and \(\oplus\) an ordinal sum. Thus equality is available precisely at the carrier sizes \(h=2^k+1\) within this rooted-or-co-rooted class.

More generally, if \(P=A_r\oplus A_s\) with \(r,s\ge1\), then
\[
\boxed{h=2^r+2^s-1,\qquad F(P)=(2^r-1)(2^s-1),}
\]
so the excess above the rooted lower bound is exactly
\[
F(P)-(h-2)=(2^r-2)(2^s-2).
\]
Consequently, for every non-Boolean \(H=J(P)\) with a least or greatest join-irreducible in \(P\), the probability of Peirce's equation for uniform independent \(A,B\in H\) is at most \(1-(h-2)/h^2\), with precisely the stated equality cases.

## Assumptions and scope
All posets and Heyting algebras are finite, and the order on \(J(P)\) is inclusion. The \(\to\) symbol is Heyting implication, and \(\downarrow p\) is the principal downset including \(p\). The term *least* means below every element; *greatest* means above every element. The universal boundary formula includes Boolean cases. The strict lower bound and equality classification apply only when \(|P|\ge2\) and \(P\) has a least or greatest point, rather than to all non-Boolean Heyting algebras.

## Proof
**Step 1 (implication in the downset algebra).** For downsets \(U,V\subseteq P\), the defining adjunction for the Heyting implication gives
\[
U\to V=\{p\in P:\downarrow p\cap U\subseteq V\}.
\]
Indeed the displayed set is a downset and is the largest one whose intersection with \(U\) lies in \(V\).

**Step 2 (the boundary characterization).** Fix \(A,B\in J(P)\), and set \(C=A\to B\). Every point of \(A\) belongs to \(C\to A\), since its entire principal downset lies in \(A\). Let \(q\) be minimal in \(P\setminus A\). All strict predecessors of \(q\) belong to \(A\), and hence
\[
q\in C\quad\Longleftrightarrow\quad
(\downarrow q\setminus\{q\})\subseteq B.
\]
If this last inclusion holds for *every* such \(q\), then each point \(p\in P\setminus A\) lies above a minimal excluded \(q\in C\setminus A\); thus \(p\notin C\to A\). Conversely, if it fails for one minimal excluded \(q\), then \(q\notin C\), while all its strict predecessors lie in \(A\); therefore \(q\in C\to A\) despite \(q\notin A\). This proves
\[
(C\to A)=A\quad\Longleftrightarrow\quad S(A)\subseteq B.
\]
Because \(S(A)\) is a downset, the map \(B\mapsto B\setminus S(A)\) is a bijection from downsets of \(P\) containing \(S(A)\) to downsets of \(P\setminus S(A)\). There are therefore exactly \(|J(P\setminus S(A))|\) successful choices of \(B\) for this \(A\). Summing their complements establishes the universal formula.

**Step 3 (a least point).** Suppose \(r\) is least and \(|P|\ge2\). Each nonempty proper downset \(A\) contains \(r\) and excludes at least one point. Every minimal excluded point \(q\ne r\) has \(r\) as a strict predecessor; hence \(r\in S(A)\) and \((A,\varnothing)\) is a Peirce failure. There are \(h-2\) such \(A\). If \(P\) has a chain \(r<x<y\), take \(A=\downarrow y\setminus\{y\}\): then \(y\) is minimal excluded, \(x\in S(A)\), and \(B=\{r\}\) produces an additional, distinct failure. Thus equality forces height at most two, which in a poset with least point means \(P=A_1\oplus A_k\). Conversely, in this star every nonempty proper downset has \(S(A)=\{r\}\); the only failing \(B\) is the empty downset, and equality holds.

**Step 4 (a greatest point).** Suppose \(g\) is greatest. Then \(Q=P\setminus\{g\}\) is a proper downset, and \(S(Q)=Q\). Exactly the \(h-2\) downsets \(B\subsetneq Q\) fail with antecedent \(A=Q\). If \(Q\) contains a comparable pair \(x<y\), take \(A=\downarrow y\setminus\{y\}\) and \(B=\varnothing\): then \(x\in S(A)\) and this gives an additional failure with \(A\ne Q\). Thus equality forces \(Q\) to be an antichain. Conversely, if \(Q\) is an antichain, every \(A\subsetneq Q\) has a missing minimal element of \(P\), so \(S(A)=\varnothing\); the sole failing antecedent is \(Q\), and equality follows. This is \(P=A_k\oplus A_1\).

**Step 5 (two antichain levels).** Write \(P=L\oplus U\), where \(|L|=r\) and \(|U|=s\). Every downset is either a proper subset of \(L\), or \(L\cup T\) for a subset \(T\subseteq U\). The latter description has \(2^s\) possibilities, so \(h=(2^r-1)+2^s\). The only antecedents with nonempty \(S(A)\) are \(A=L\cup T\) with \(T\subsetneq U\), and then \(S(A)=L\). There are \(2^s-1\) such antecedents, and their failing consequents are the \(2^r-1\) proper subsets of \(L\). Multiplication gives the exact defect count and the displayed excess formula.

## Verification
The self-contained Python script `verify_peirce.py` directly builds finite Heyting implications and checks the Peirce identity for every ordered pair of downsets. Its separate boundary calculation reproduces the same failure pairs. It enumerates all \(5{,}231\) naturally labeled posets with at most six points (\(101{,}658\) antecedent downsets in total), checks both equality classifications whenever a least or greatest point exists, checks both families of stars for \(1\le k\le9\), and checks two-level formulas for \(1\le r,s\le5\). Actual execution completed with `ALL_PEIRCE_CHECKS_PASS`. These tests corroborate but do not replace the proof for arbitrary finite orders.

## Relationship to prior work
Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first submitted 2021-10-21), develop probability-of-equation methods and show in Corollary 3.11 that Peirce's law has no uniform finite satisfiability gap. Their Section 3 also uses a Boolean algebra with a new top for a different binary identity. Neither their no-gap statement nor that material-implication construction supplies the boundary formula, the exact Peirce failure count, or the two one-ended equality classifications. Classical finite Birkhoff representation and Kripke semantics underpin the reduction to downsets. The 2022 revision of the Stanford Encyclopedia of Philosophy's *Intuitionistic Logic* entry explains the relevance of rooted frames without claiming numerical Peirce counts.

## Limitations
The bound \(F(P)\ge h-2\) is not asserted for non-Boolean posets having neither a least nor a greatest element, even though the universal exact formula applies there. The original source provides no general rate for Peirce's equation, but specialized historical results under other terminology have not been exhaustively excluded. Quantitative claims concern uniform, independent sampling of **ordered** pairs. 

## References
1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (initial public version 2021-10-21), Sections 1 and 3; https://arxiv.org/abs/2110.11515.
2. Classical finite Birkhoff representation theorem for distributive lattices (standard background; no bibliographic priority asserted).
3. *Intuitionistic Logic*, Stanford Encyclopedia of Philosophy, substantive revision 2022-12-16, Section 5.1; https://plato.stanford.edu/entries/logic-intuitionistic/.
