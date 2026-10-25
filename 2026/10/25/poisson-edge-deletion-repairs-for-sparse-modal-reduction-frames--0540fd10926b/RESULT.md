# Poisson edge-deletion repairs for sparse modal reduction frames

## Finding

Let \(m\ge2\), \(k\ge1\) be fixed integers and \(c>0\). Let \(G_n\) be the directed loop-free random graph on \([n]\), with each ordered pair of different vertices independently made an arc with probability \(p_n=c n^{-1-1/m}\). Read the arc relation \(R_n\) as ordinary Kripke accessibility, without adding reflexive loops. Write \(\rho_{m,k}\) for the universal-frame validity assertion that every valuation of one letter makes the formula
\[
\Box^{m+k}p\longrightarrow\Box^m p
\]
true at every world. Let \(D_n\) denote the minimum number of existing arcs to remove so that \(\rho_{m,k}\) holds, and let \(H_n\) be the number of distinct minimum-cardinality deletion subsets. If \(Z\) is Poisson with mean \(c^m\), then
\[
(D_n,H_n)\ \xrightarrow{\ d\ }\ (Z,m^Z),\qquad
\Pr(\rho_{m,k})\longrightarrow e^{-c^m}.
\]
In fact, with probability tending to one, every directed length-\(m\) walk belongs to a different isolated directed path component with exactly \(m\) arcs, and the frame has no length-\((m+k)\) walk. On this event the optimal repairs are *exactly* the sets obtained by deleting one of the \(m\) arcs from each such component.

For general sequences of independent arc probabilities \(p_n\), a further density contrast holds:
\[
\begin{array}{ll}
 p_n=o(n^{-1-1/m}) &\Longrightarrow\Pr(\rho_{m,k})\to1,\\
 n^{-1-1/m}\ll p_n\ll n^{-1-1/(m+k)} &\Longrightarrow\Pr(\rho_{m,k})\to0,\\
 p_n=p\in(0,1]\text{ fixed} &\Longrightarrow\Pr(\rho_{m,k})\to1.
\end{array}
\]

## Assumptions and scope

A directed path of length \(m\) has \(m+1\) pairwise distinct vertices and \(m\) directed arcs in order. A directed walk may revisit a vertex. An *isolated directed path component* means no other arc has either endpoint in the path's vertex set. Powers \(R^a\) denote relational composition, not reflexive-transitive closure. All asymptotics fix \(m,k,c\); the edge probability may depend on \(n\). Deletion means removing existing arcs only, without adding vertices or arcs. For a directed graph with no valid m-walk we define \(D=0\), \(H=1\).

## Proof

**Step 1: Modal frame correspondence.** At a world \(u\), the formula \(\Box^t p\) states that every \(v\) with \((u,v)\in R^t\) satisfies \(p\). Thus the implication \(\Box^{m+k}p\to\Box^m p\) is valid for every valuation at every world if and only if
\[
R^m\subseteq R^{m+k}.
\]
For the reverse direction, if a pair \((u,v)\) belongs to \(R^m\setminus R^{m+k}\), assign \(p\) true to precisely the \(R^{m+k}\)-successors of \(u\), producing a countervaluation at \(u\).

**Step 2: The isolated path Poisson limit.** Let \(Z_n\) count injective oriented paths of \(m\) arcs. The ordered vertex sequence determines each path, and
\[
\mathbb E Z_n=(n)_{m+1}p_n^m\longrightarrow c^m.
\]
For any fixed factorial-moment order \(r\), the contributions of \(r\) vertex-disjoint paths tend to \(c^{mr}\). Every non-disjoint collection is represented by a finite union of directed paths. In each connected overlap component containing at least two distinct paths, the union has \(e\ge m+1\) arcs and \(v\le e+1\) vertices. Its expected embedding order at the critical scaling is bounded by
\[
O(n^v p_n^e)=O(n^{v-(1+1/m)e})=O(n^{1-e/m})=o(1).
\]
The finitely many possible overlap patterns for fixed \(m,r\) show that all non-disjoint contributions vanish. Therefore \(\mathbb E(Z_n)_r\to(c^m)^r\) for each fixed \(r\), and the factorial-moment theorem gives \(Z_n\Rightarrow\operatorname{Poisson}(c^m)\).

For any one candidate simple \(m\)-path, there are at most \(2(m+1)n\) possible additional nonloop arcs incident to one of its vertices. The expected number of present simple \(m\)-paths having an additional incident arc is at most
\[
(n)_{m+1}p_n^m\,2(m+1)n p_n=O(n^{-1/m})=o(1).
\]
Hence all occurring simple \(m\)-paths are isolated components with high probability. A non-simple walk of length \(m\) contains a directed cycle of length at most \(m\); the expected number of directed cycles of any given positive bounded length is \(O((np_n)^a)=o(1)\). Thus all \(m\)-walks are the isolated paths just counted, with high probability. Similarly, writing \(L=m+k\), the expected number of injective \(L\)-paths is
\[
(n)_{L+1}p_n^L=O(n^{1-L/m})=O(n^{-k/m})=o(1).
\]
A nonsimple \(L\)-walk contains a cycle of length at most \(L\), and each bounded cycle length again has vanishing expectation. Therefore no \(L\)-walk survives with high probability.

**Step 3: Optimal repairs.** On the event just proved, the graph has \(Z_n\) pairwise disjoint isolated path components of length \(m\), and no walk of length \(m+k\). Deleting arcs cannot create a longer walk. By Step 1, each surviving \(m\)-path witnesses failure of the axiom, so at least one existing arc from *each* of the \(Z_n\) path components must be deleted. Deleting one arc from each component is sufficient, and any other deleted arc would prevent minimum cardinality. The number of optimal sets is therefore \(m^{Z_n}\), with minimum size \(Z_n\). The continuous mapping theorem on the discrete state space yields the asserted joint law and \(\Pr(D_n=0)\to e^{-c^m}\).

**Step 4: The other density regimes.** If \(p_n=o(n^{-1-1/m})\), the expected number of simple \(m\)-paths tends to zero; all directed cycles of length at most \(m\) also have expectation tending to zero, since \(np_n\to0\). The frame then has no \(m\)-walk and the axiom is valid. If \(n^{-1-1/m}\ll p_n\ll n^{-1-1/(m+k)}\), the expected number of simple \(m\)-paths diverges. Pairs sharing \(h\) directed arcs, for \(1\le h\le m-1\), contribute to the variance relative to the squared mean only \(O((n^{h+1}p_n^h)^{-1})=o(1)\); pairs sharing vertices but no arcs likewise have negligible relative contribution. Hence at least one \(m\)-path exists with high probability. Meanwhile simple \((m+k)\)-paths and all short directed cycles have vanishing expectation, so \(R^{m+k}\) is empty and the axiom fails. Finally, when \(p_n=p>0\) is fixed, for every ordered pair of endpoints there are \(\lfloor(n-2)/(m+k-1)\rfloor\) internally vertex-disjoint candidate walks of length \(m+k\), each using a disjoint arc set and hence appearing independently with probability \(p^{m+k}\). By a union bound over at most \(n^2\) ordered pairs, \(R^{m+k}\) is universal with probability tending to one, making the axiom valid. This also handles coinciding endpoints. (For sufficiently large \(n\), the candidate internal vertices are distinct from the endpoints.)

## Verification

The separate, standard-library-only program `check_sparse_modal_repair.py` exhaustively evaluates all \(4164\) loop-free labelled directed frames on two, three and four vertices for \(m\in\{2,3\}\) and \(k\in\{1,2\}\). It verifies frame correspondence against every propositional valuation; and, in all enumerated path-isolation cases, it brute-forces every arc-deletion subset to check the exact optimum and number of minimizers. The observed result is `SPARSE_MODAL_REPAIR_FINITE_OK 16656 frame_formulas 264256 valuations 1072 repair_counts`. The asymptotic assertions depend on the mathematical factorial-moment and second-moment arguments above, not on finite exhaustive checks.

## Relationship to prior work

Knudstorp studies the modal reduction axioms \(\Box^a p\to\Box^b p\), relational-power correspondence and finite-model phenomena. The present result concerns a different question: validity under sparse Bernoulli random frames and the *number of minimal existing-arc deletion repairs*. Classical Poisson asymptotics for sparse path counts supply a key probabilistic ingredient; their general form is not claimed as a new theorem. Work on logics of random frames, including Goranko–Kapron and Sliusarev, provides context but was not identified as giving this particular repair law. The claim of novelty is limited to the explicit joint modal-repair law and phase analysis for this axiom, not to Poisson path counts or the frame correspondence by themselves.

## Limitations

The result treats independent, loop-free directed arcs and fixed \(m,k\) only. It does not classify the intermediate window beyond the stated inequalities, dense probabilities tending to zero outside those windows, deletion costs with weights, random reflexive frames or all modal formulas. The historical comparison may miss an earlier graph-covering result that subsumes the repair count; independent validation has not occurred.

## References

1. S. B. Knudstorp, *Knocking Down Boxes: The Finite Model Property for K with a Modal Reduction Principle*, arXiv:2510.00864 (initial posting 2025-10-01), https://arxiv.org/abs/2510.00864.
2. V. Goranko and B. Kapron, *The modal logic of the countable random frame* (2003), primary source located through bibliographic records; full text not fully inspected.
3. M. Sliusarev, *Modal logics of almost sure validities in some classes of euclidean and transitive frames*, arXiv:2406.10770 (2024), https://arxiv.org/abs/2406.10770; abstract inspected.
