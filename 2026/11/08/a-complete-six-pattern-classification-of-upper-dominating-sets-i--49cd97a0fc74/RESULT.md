# A complete six-pattern classification of upper-dominating sets in ladders

## Finding
Let \(L_n=P_2\square P_n\) be the ordinary open two-row ladder with \(n\ge2\) rungs. A dominating set \(D\) is *minimal* if no proper subset dominates. Its upper-domination number \(\Gamma(L_n)\) is the maximum size of such a set. Then
\[
\Gamma(L_n)=n,
\qquad
\#\{D:D\text{ is minimal dominating},\ |D|=n\}
=4+2\mathbf1_{2\mid n}.
\]
Every extremal set has one of six explicit forms given below. Exactly two extremal sets are independent, for every \(n\ge2\). In particular, although \(\Gamma=\alpha\) on bipartite graphs, the other extremizers need not be independent.

## Assumptions and scope
All graphs are finite, simple and undirected. Label the upper and lower vertices of rung \(i\) by \(u_i,v_i\), with edges \(u_iv_i\), \(u_iu_{i+1}\), and \(v_iv_{i+1}\), whenever the indices exist. Encode the intersection of \(D\) with rung \(i\) by \(a_i\in\{0,1,2,3\}\): code \(0\) means no vertex; \(1\) means \(u_i\) only; \(2\) means \(v_i\) only; and \(3\) means both. For \(n\ge2\), exactly the following distinct words encode upper-dominating sets:

* \(1^n\) and \(2^n\);
* the length-\(n\) prefixes of \((12)^\infty\) and \((21)^\infty\);
* only when \(n\) is even, the length-\(n\) prefixes of \((0330)^\infty\) and \((3003)^\infty\).

This is an enumeration of *maximum-cardinality minimal* dominating sets, not minimum-cardinality dominating sets or all minimal dominating sets.

## Proof
**Maximum size.** The rungs form a perfect matching of \(L_n\), so every independent set has size at most \(n\). A checkerboard set has size \(n\), hence \(\alpha(L_n)=n\). The classical bipartite upper-domination equality of Cockayne–Favaron–Payan–Thomason implies \(\Gamma(L_n)=\alpha(L_n)=n\). This known equality is used only for the upper bound, not for the classification.

**All displayed words are admissible.** Every all-upper or all-lower selection has a private neighbor at the opposite vertex on its rung. Each alternating single-vertex selection is independent and dominating: each selected vertex privately dominates itself, and each unselected vertex is adjacent to the selected rung-mate. In either of the two \(0/3\) patterns, every empty rung has a neighboring full rung, while every selected vertex on a full rung has a private neighbor on an adjacent empty rung. The even-length boundary condition ensures that the last rung is not an undominated empty rung. Each displayed word therefore represents a minimal dominating set of size \(n\). The words are pairwise different. The alternating single-vertex words are the only independent ones.

**Local finite-state characterization.** Write \(N[w]\) for the closed neighborhood of vertex \(w\). A set \(D\) is minimal dominating if and only if (a) \(N[w]\cap D\ne\varnothing\) for every vertex \(w\), and (b) for each \(u\in D\) some \(w\in N[u]\) has \(N[w]\cap D=\{u\}\). The witness \(w\) is a private neighbor, possibly \(w=u\). For each vertex in rung \(i\), these conditions can be evaluated from the five rung codes \(a_{i-2},\ldots,a_{i+2}\), with a special absent-rung symbol \(4\) beyond the ends.

Construct the deterministic finite-state machine whose states are four consecutive codes in \(\{0,1,2,3,4\}^4\) (\(625\) possible states). On appending code \(e\), a state \((a,b,c,d)\) shifts to \((b,c,d,e)\) only if the two real vertices of its central rung, coded by \(c\), satisfy both local tests using \((a,b,c,d,e)\). Start from \((4,4,a_1,a_2)\); append each remaining real rung and finally two absent-rung symbols \(4,4\). The machine accepts exactly the minimal dominating sets. Appending an actual rung of code \(k\) contributes the excess weight \(\operatorname{popcount}(k)-1\); the final accumulated weight is \(|D|-n\).

For a prefix of \(j\ge2\) real rungs, let \(f_j(s)\) be the maximum excess weight among locally valid prefixes ending in state \(s\), or negative infinity if unreachable. The transition rule is the finite max-plus recurrence
\[
f_{j+1}(t)=\max_{s\to t\text{ with new code }k}\left(f_j(s)+\operatorname{popcount}(k)-1\right).
\]
The standalone verifier constructs all \(625\) states directly from the local tests and, by exact integer computations, checks the vector identities \(f_7=f_9\) and \(f_8=f_{10}\), each with \(123\) reachable states. Since the transition is time-homogeneous, these two equalities imply \(f_{j+2}=f_j\) for *all* \(j\ge7\).

Any accepted set with \(|D|=n\) has an optimal-weight prefix in every state reached at a prefix length \(j\ge7\): otherwise replacing that prefix by a higher-weight prefix with the same last four codes yields another accepted minimal dominating set with more than \(n\) selected vertices, contradicting \(\Gamma(L_n)=n\). Therefore all extremal words of length at least seven lie in the *tight-transition* automaton given by equality in the max-plus recurrence. Record also the length modulo four and a six-bit mask indicating which displayed periodic patterns still agree with the prefix. At length seven all optimal-weight prefixes can be enumerated from \(4^7\) words. Then the tight-transition automaton has exactly \(492\) reachable augmented states and \(704\) distinct explored transitions. A complete reachability check shows that every state which admits the final absent-rung padding and has full excess zero retains at least one applicable periodic pattern (the two \(0/3\) patterns being admissible only for even lengths). This is a **finite closure proof for all subsequent lengths**, not a finite-length extrapolation. The full transition generator and closure checker are given in `artifacts/verify.py`.

Finally, independent direct vertex-subset enumeration verifies the classification for every \(2\le n\le10\), including all \(n<7\). Together with the finite-state induction, this establishes the stated classification for every \(n\ge2\).

## Verification
Run `python3 artifacts/verify.py` with a standard Python 3 interpreter. It constructs the local predicates and the \(625\)-state transfer machine, proves the two max-plus vector identities, explores the entire finite tight-transition closure, and independently enumerates every vertex subset of cardinality \(n\) for \(2\le n\le10\). It additionally checks the local periodic templates and all boundary residues. It exits with `VERIFY_OK` if all assertions succeed. The direct finite enumerations alone are *not* an infinite proof; the two vector identities, induction, and complete augmented-state closure provide the universal certificate.

## Relationship to prior work
Sahbi's 2026 grid note [1] derives \(\Gamma(P_m\square P_n)=\lceil mn/2\rceil\) from the classical bipartite theorem, hence establishes the value \(n\) for ladders but not the number or complete structure of maximizing minimal sets. The OEIS records the total numbers of minimal dominating sets of ladders and grids [2,3], without resolving the maximum-size layer. Mertens [4] computes the ordinary domination polynomial, which counts *all dominating sets*, not inclusion-minimal ones; it cannot directly give the classification above. The reported result refines the value of a known extremal parameter and is conditional on the correctly cited classical upper-domination theorem. No assertion of exhaustive historical novelty is made.

## Limitations
The theorem is for the open two-row ladder, not wider grids, cylindrical ladders, or modified domination predicates. The finite-state computation is exact but depends on the included generator, local-test specification, and reproducible closure; no external independent mathematical audit has been performed. Published unindexed or otherwise inaccessible enumerations of upper-dominating sets remain a historical priority risk.

## References
[1] R. Sahbi, *Upper Domination in Rectangular Grid Graphs and Its Relation to Sub-Quorum Colorings*, first public 2026-09-30, arXiv:2610.03785, https://arxiv.org/abs/2610.03785.

[2] OEIS A290379, *Number of minimal dominating sets in the n-ladder graph*, https://oeis.org/A290379.

[3] OEIS A286847, *Number of minimal dominating sets in the grid graph*, https://oeis.org/A286847.

[4] S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, first public 2024-08-15, arXiv:2408.08053, https://arxiv.org/html/2408.08053v1.

[5] E. J. Cockayne, O. Favaron, C. Payan and A. G. Thomason, *Contributions to the theory of domination, independence and irredundance in graphs*, Discrete Mathematics 33 (1981), 249–258.
