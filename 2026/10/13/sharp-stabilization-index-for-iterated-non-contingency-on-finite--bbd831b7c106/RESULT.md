# Sharp stabilization index for iterated non-contingency on finite transitive frames

## Finding

For a positive integer \(n\), let \(s(n)\) be the least positive integer \(k\) for which every transitive Kripke frame on exactly \(n\) worlds validates \(\nabla^k\varphi\leftrightarrow\nabla^{k+1}\varphi\), for every modal formula \(\varphi\), with non-contingency defined as \(\nabla\psi:=\Box\psi\lor\Box\neg\psi\). The exact threshold is

\[
s(n)=\begin{cases}
1,&n=1,\\
2,&n=2,\\
n-1,&n\geq3.
\end{cases}
\]

For every \(n\geq3\), strict linear accessibility and a single atomic valuation attain the bound. Thus the last possible new stage of iterated 'knowing whether' on an \(n\)-world transitive frame is determined exactly, including exceptional small sizes.

## Assumptions and scope

A frame \((W,R)\) has a nonempty finite world set \(W\), with \(|W|=n\) and transitive accessibility: \(wRv\) and \(vRu\) imply \(wRu\). Neither reflexivity nor seriality is assumed; loops and nontrivial strongly connected components are permitted. The standard universal \(\Box\)-semantics is used, so a world with no successors satisfies both \(\Box\psi\) and \(\Box\neg\psi\). Equivalence is required for *all* valuations and *all* formulas simultaneously, though a single propositional letter suffices to establish sharpness.

For a subset \(X\subseteq W\), set \(R[w]=\{v:wRv\}\) and

\[
T(X)=\{w\in W:R[w]\subseteq X\ \text{or}\ R[w]\cap X=\varnothing\}.
\]

The truth set of \(\nabla^j\varphi\) is \(T^j(X)\), where \(X\) is the truth set of \(\varphi\). Define \(Y_0=X\), and \(Y_j=T^j(X)\) for positive integers \(j\). The theorem is therefore equivalent to the exact least universal stabilization index of this nonlinear set operator.

## Proof

**Forward-closure lemma.** For any \(X\subseteq W\), the set \(T(X)\) is forward closed under a transitive relation \(R\): if \(w\in T(X)\) and \(wRv\), then \(v\in T(X)\). Indeed, transitivity gives \(R[v]\subseteq R[w]\). Every subset of a homogeneous set of successor truth values remains homogeneous. If \(Y\subseteq W\) is forward closed, then \(Y\subseteq T(Y)\), because all successors of each \(w\in Y\) remain in \(Y\). Consequently

\[
Y_1\subseteq Y_2\subseteq Y_3\subseteq\cdots,
\]

and equality at any adjacent pair forces equality thereafter (because the same operator is iterated). The chain is an increasing sequence of subsets of a finite set.

**Main bound for \(n\geq3\).** If \(Y_1=\varnothing\), then \(Y_2=T(\varnothing)=W\), and equality holds from index \(2\). If \(|Y_1|\geq2\), each strict growth step consumes at least one of the at most \(n-2\) remaining worlds. Thus equality holds by index \(n-1\).

It remains to handle \(|Y_1|=1\). Suppose \(Y_2\ne Y_1\), and choose \(w\in Y_2\setminus Y_1\). Since \(w\notin T(X)\), the set \(R[w]\) has successors of both \(X\)-truth values, in particular at least two successors. Since \(w\in T(Y_1)\), one of \(R[w]\subseteq Y_1\) and \(R[w]\cap Y_1=\varnothing\) holds. The first is impossible because \(R[w]\) has at least two distinct elements and \(Y_1\) has one element. Hence \(R[w]\cap Y_1=\varnothing\).

The finite, nonempty forward-closed subgraph \(R[w]\) has a terminal strongly connected component \(C\). Every successor of every \(u\in C\) belongs to \(C\), since transitivity makes \(R[w]\) forward closed and \(C\) has no outgoing edge within it. If \(C\) were a singleton \(\{u\}\), its successor set would be either empty or \(\{u\}\). In either case, the successor set is homogeneous for \(X\), implying \(u\in T(X)=Y_1\). But \(C\subseteq R[w]\) is disjoint from \(Y_1\), a contradiction. Therefore \(|C|\geq2\). Because every \(u\in C\) has \(R[u]\cap Y_1=\varnothing\), all of \(C\) is contained in \(T(Y_1)=Y_2\). As \(C\cap Y_1=\varnothing\), at least two new worlds are gained at the second iterate. Thus \(|Y_2|\geq3\), leaving at most \(n-3\) further strictly increasing stages. Equality must hold at or before index \(n-1\). The proof includes nonreflexive and nonserial frames and all patterns of cycles.

For \(n=1\), every successor set has at most one element, so \(T(X)=W\) for every \(X\); hence \(s(1)=1\). For \(n=2\), the increasing chain from \(Y_1\) either already stabilizes or reaches \(W\) by the second iterate. If \(Y_1\) is empty then \(Y_2=W\); this proves \(s(2)\leq2\).

**Sharpness.** At \(n=2\), take \(W=\{0,1\}\), let \(R=W\times W\), and let the letter \(p\) hold only at \(1\). Then \(T(\{1\})=\varnothing\) but \(T^2(\{1\})=W\), proving \(s(2)>1\).

For each \(n\geq3\), take \(W=\{0,\ldots,n-1\}\), with strict-order relation \(iRj\) exactly when \(i<j\), and let \(p\) hold only at \(n-1\). Direct induction from the non-contingency clause gives

\[
T^j(\{n-1\})=\{n-1-j,\ldots,n-1\},\qquad 0\leq j\leq n-1.
\]

For each \(j<n-1\), the two consecutive truth sets differ. At \(j=n-1\), the set is \(W\) and therefore fixed by \(T\). Hence \(s(n)\geq n-1\), completing the exact determination.

## Verification

The included standalone standard-library program `verify.py` enumerates every labeled transitive directed relation on one, two, three and four worlds; checks all atomic valuations and the proposed universal cutoffs; tests the reflexive-transitive ancillary identity at these sizes; and checks the strict-order sharpness construction at all sizes from three through sixty. It also rechecks the two-world complete-relation witness. Run with `python3 verify.py`. The program reports \(2,13,171,3994\) transitive frames at the respective sizes and exactly \(65328\) frame/valuation pairs, followed by `VERIFY_OK`.

The finite tests independently exercise boundaries and implementation details; the universal result for every positive \(n\) follows from the preceding proof, not from enumeration.

## Relationship to prior work

Sierra Miranda, Wang and Zenger (2026) supply labeled calculi uniformly for generalized-path-condition frame classes, including transitivity, but do not give a sharp iteration-stabilization bound in the inspected manuscript. Petrukhin (2025) develops nested sequent calculi for nonstandard modalities over \(\mathbf K\) and several frame conditions; the inspected sections and searchable transcription do not determine the minimum stabilization stage on finite transitive frames. Zolin (2002) explicitly axiomatizes the *reflexive* \(\mathbf{S4}\) non-contingency implication \(\nabla p\to\nabla^2p\). That older implication and the resulting monotone growth intuition are acknowledged prior coverage, not presented as novel. The present claim instead gives the **exact cardinality-dependent bound and its sharp nonreflexive witnesses over all finite \(\mathbf{K4}\)-frames**. In particular, mere reflexive-transitive coverage does not furnish the strict-order lower bounds because those sharp frames lack reflexivity.

## Limitations

The exact \(n-1\) threshold applies to *all* transitive frames on \(n\) worlds, not to a single frame; it does not claim that every such frame needs that many iterations. The formula language permits arbitrary nesting and arbitrary valuations, but this result only bounds a consecutive *unbroken block* of non-contingency operators, not all nested modality patterns. Infinite transitive frames are excluded from the size-dependent conclusion; their iterates need not stabilize at a uniform finite stage. No claim of independent verification is made. Earlier presentations under different modal-algebra or information-cell terminology remain a possible priority risk.

## References

1. B. Sierra Miranda, Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975 (first public submission 2026-09-30), https://arxiv.org/abs/2609.38975.
2. E. E. Zolin, *Sequential Reflexive Logics with Noncontingency Operator*, Mathematical Notes 72 (2002), 784–798, DOI:10.1023/A:1021485712270; author-hosted full text: https://www.cs.man.ac.uk/~ezolin/pub/zolin_2002_Reflex_eng.pdf.
3. Y. Petrukhin, *Nested Sequent Calculi for Some Modal Logics with Non-Standard Modalities*, Logic and Logical Philosophy 34 (2025), 287–318, DOI:10.12775/LLP.2025.009.
