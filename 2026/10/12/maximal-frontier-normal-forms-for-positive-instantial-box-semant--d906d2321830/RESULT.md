# Maximal-frontier normal forms for positive instantial box semantics

## Finding
Let \(P=(W,\le)\) be a finite nonempty poset and let \(\mathcal U=\operatorname{Up}(P)\), including \(\varnothing\). For any family \(N\subseteq\mathcal U\), any integer \(k\ge0\), and upsets \(A,B_1,\ldots,B_k\in\mathcal U\), define the positive instantial box test
\[
F_k^N(B_1,\ldots,B_k;A)\ \Longleftrightarrow\ \exists U\in N\ \bigl[U\subseteq A\ \land\ \bigwedge_{i=1}^{k}(U\cap B_i\ne\varnothing)\bigr].
\]
The empty conjunction when \(k=0\) is true. Let \(T=\operatorname{Max}(W)\) and, for \(U\in\mathcal U\), put \(\mu(U)=U\cap T\). For each \(M\subseteq T\), let \(\mathcal U_M=\{U\in\mathcal U:\mu(U)=M\}\), ordered by inclusion. Define the canonical maximal-frontier core
\[
C(N)=\bigcup_{M\subseteq T}\operatorname{Min}_{\subseteq}(N\cap\mathcal U_M),
\]
where minimality is within the indicated finite fibre.

**Theorem.** Two neighbourhood families \(N,N'\subseteq\mathcal U\) induce identical instantial box tests for every arity, scope and witness valuation if and only if \(C(N)=C(N')\). More strongly, equality of tests only for \(0\le k\le |T|\) suffices. Consequently, if \(a(Q)\) is the number of antichains of a finite poset \(Q\), **including the empty antichain**, then the exact number of observably distinct local positive-instantial box operations on \(P\) is
\[
\prod_{M\subseteq T}a(\mathcal U_M).
\]

For a chain of \(n\ge1\) points this number is \(2(n+1)\). For a discrete antichain of \(n\ge1\) points it is \(2^{2^n}\). For the height-two poset comprising \(r\ge1\) incomparable minimal points below a common maximal point (and for \(r=0\), the singleton poset), it is \(2D_r\), where \(D_r\) is the number of antichains in the Boolean lattice on \(r\) points. Thus for \(r=0,1,2,3\), the counts are \(4,6,12,40\). These are operation counts, not counts of pointed models, full two-sided neighbourhood structures or modal logics.

## Assumptions and scope
All neighbourhoods and all propositional valuations are **upsets**, rather than arbitrary subsets. The order is a finite partial order, and no nonemptiness, upward-closure-under-inclusion or closure-under-intersection condition is imposed on the family \(N\). A family of upsets may itself be empty and may contain the empty upset. The result classifies the local \(\Box\) semantic operation, not the separate \(\Diamond\) modality. The theorem may be applied separately at every world of a persistent two-sided model. **Taking cores worldwise need not preserve persistence of the raw neighbourhood assignment.** Thus the full-model invariance statement concerns pairs of already persistent models whose worldwise box cores agree and whose diamond neighbourhood assignments and propositional valuations agree.

For any local family \(N\), an example of a globally persistent realization with that local family is the constant assignment \(N_\Box(w)=N\) at every world; the independent diamond assignment may be fixed identically in both models. Thus all stated local distinctions have bona fide persistent-model realizations. Arities count the number of witness formulas, with \(k=0\) admitted.

## Proof
**1. Dominance within a maximal frontier.** In a finite poset, every element \(x\in U\) of an upset lies below a maximal element of \(U\), which is also maximal in \(W\). Suppose \(V\subseteq U\) are upsets with \(\mu(V)=\mu(U)\). If \(U\subseteq A\) and \(U\cap B_i\ne\varnothing\), choose \(x\in U\cap B_i\). Take \(m\in\mu(U)\) with \(x\le m\). Since \(B_i\) is an upset, \(m\in B_i\); since \(\mu(V)=\mu(U)\), \(m\in V\). Thus \(V\cap B_i\ne\varnothing\). Also \(V\subseteq A\). Hence every witness \(U\) may be replaced by any same-frontier subset \(V\). Because every nonempty finite fibre \(N\cap\mathcal U_M\) has a minimal element below each of its elements, all tests for \(N\) equal those for \(C(N)\).

**2. Reconstruction by bounded-arity tests.** For a given \(U\in\mathcal U\) put \(M=\mu(U)\). Every \(\{m\}\) with \(m\in M\) is an upset because \(m\) is maximal. Consider the test whose scope is \(A=U\), whose witnesses are the singleton upsets \(\{m\}\) indexed by \(M\), and whose arity is \(|M|\le |T|\). Its truth is exactly the existence of \(V\in N\cap\mathcal U_M\) with \(V\subseteq U\): a witnessing \(V\subseteq U\) must meet every singleton \(\{m\}\), so it contains \(M\) and has \(\mu(V)=M\); the converse is immediate. For \(U=\varnothing\), this is the legitimate zero-arity test, true precisely when \(\varnothing\in N\).

The collection of these tests as \(U\) ranges over \(\mathcal U_M\) identifies the upward closure, within \(\mathcal U_M\), of \(N\cap\mathcal U_M\). Its unique set of minimal elements is exactly \(\operatorname{Min}_{\subseteq}(N\cap\mathcal U_M)\). Thus equality of all tests of arity at most \(|T|\) forces equality of every fibre-minimal antichain, hence \(C(N)=C(N')\). Step 1 proves the converse for all arities.

**3. Census and examples.** For each \(M\subseteq T\), the possible fibre-minimal sets are precisely the antichains of \(\mathcal U_M\), including the empty antichain; every such choice is realizable by setting \(N\) equal to the union of the chosen antichains. The fibres are disjoint, yielding the displayed product. In an \(n\)-point chain, \(\mathcal U_\varnothing=\{\varnothing\}\), and the nonempty fibre is an \(n\)-element chain, with respectively \(2\) and \(n+1\) antichains. In a discrete \(n\)-point poset, each upset is its own maximal frontier, so each of the \(2^n\) fibres is a singleton. In the star with \(r\) incomparable minima and one maximum, all nonempty upsets are \(\{\mathrm{top}\}\cup S\) for \(S\subseteq[r]\), so the unique nonempty-frontier fibre is Boolean \(\mathcal P([r])\); the empty frontier fibre is a singleton. This gives \(2D_r\).

**4. Formula-level consequence and sharpness at discrete orders.** In the positive instantial language, every truth set in a persistent poset model is an upset. Equality of the local \(F_k\) operations therefore implies equality of the corresponding modal truth sets; structural induction on arbitrary modal formulas gives formula-level invariance when the other primitive modality is held fixed. Conversely, each reconstruction test is expressed by a depth-one box formula using fresh propositional letters valued as its indicated upsets. In a discrete poset of \(n\ge1\) points, the full family of all subsets and the same family minus the whole set agree on tests of every arity \(k<n\), yet the \(n\) singleton witness valuations with full scope distinguish them. The arity cutoff is therefore sharp in the unrestricted finite-poset class, although this discrete sharpness is previously known and not the principal new classification.

## Verification
The accompanying standalone `verify.py` computes all labelled partial orders on \(1,2,3\) points (respectively \(1,3,19\) orders). For **every** family of upsets, it computes the complete tuple of direct box truth values over all upset scopes and ordered witness-upset tuples of lengths \(0\) through the number of worlds; it compares the signatures against the proposed cores and separately checks the antichain product. It checked respectively \(4,32,928\) local neighbourhood families across those posets, and reported `VERIFY_OK` for all comparisons. Additional computations checked the chain and discrete formulas through four worlds, exact star counts through three lower points, and the discrete sharp-arity witnesses through four worlds. These finite tests are independent consistency checks only; the proof above establishes the theorem for arbitrary finite posets.

Run with an ordinary Python 3 interpreter: `python verify.py`. No third-party dependencies are required.

## Relationship to prior work
Das, Khanra and Sardar (2026) introduce persistent two-sided positive instantial neighbourhood semantics over upsets and establish its foundational syntax, algebra and canonical representation; their primary indexed semantic clauses motivate the restriction to positive-upset valuations. Existing classical instantial and coalgebraic separation results (e.g. Hansen and Poiger, 2025, Example 8) use unrestricted Boolean valuations and recover more of the raw neighbourhood data. Those unrestricted results do not imply the present maximal-frontier quotient for positive-upset valuations. Finite-set witness-arity bounds already cover the discrete sharpness example; that part is not claimed as original. The new mathematical object is the exact observational quotient and its fibre-antichain enumeration on general finite ordered carriers.

## Limitations
The theorem is finite, local and box-specific; it does not classify full two-sided models, arbitrary infinite posets or the independent diamond operation. The principal motivating preprint could be checked through its public abstract and substantive indexed excerpts of its semantic and canonical constructions, but its full PDF was not accessible for a complete reading. Its unread portions remain a literature-overlap risk; no claim of comprehensive absence from that text is made. Other equivalent descriptions may exist in order-theoretic or coalgebraic literature. Independent validation has not been performed.

## References
1. L. K. Das, A. Khanra and S. K. Sardar, *Positive Instantial Neighbourhood logic*, arXiv:2606.08083 (first public version 6 June 2026), https://arxiv.org/abs/2606.08083.
2. H. H. Hansen and K. Poiger, *Safety and Strong Completeness via Reducibility for Many-Valued Coalgebraic Dynamic Logics*, CALCO 2025, DOI:10.4230/LIPIcs.CALCO.2025.9, especially the instantial neighbourhood example and separating predicate liftings, https://doi.org/10.4230/LIPIcs.CALCO.2025.9.
3. J. van Benthem, N. Bezhanishvili, S. Enqvist and J. Yu, *Instantial Neighbourhood Logic*, Review of Symbolic Logic 10 (2017), DOI:10.1017/S1755020316000447.
