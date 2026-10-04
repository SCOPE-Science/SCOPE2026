# Weak local deficiency one for all complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\). Then
\[
\operatorname{def}_{\mathrm{wloc}}(G)\le1.
\]
Therefore \(\operatorname{def}_{\mathrm{wloc}}(G)=0\) exactly when \(G\) is interval colorable, and it equals \(1\) for every other complete multipartite graph. In particular, there is no complete multipartite graph with weak local deficiency \(2\).

This settles the weak-local-deficiency half of Problem 6.6 posed by Casselgren and Petrosyan. Their Theorem 3.3 gives the general bound \(2\), while Theorem 3.2 gives the bound \(1\) when the largest part is unique. The proof below supplies the remaining case, when the maximum part size is attained at least twice.

## Assumptions and scope
All graphs are finite and simple. A proper edge-coloring uses integer colors. For a finite set \(A\) of integers, its weak local deficiency is the length of the largest consecutive block that must be inserted between \(\min A\) and \(\max A\) to obtain an interval. Thus a color set is a weak near-interval whenever its missing integers contain no two consecutive values.

Write \(N=|V(G)|\), and let \(t\) be the maximum part size. The cases with two parts are interval colorable. If one part is uniquely largest, Casselgren--Petrosyan Theorem 3.2 already gives weak local deficiency at most \(1\). Hence assume \(r\ge3\) and at least two parts have size \(t\).

We repeatedly use the elementary fact that a complete multipartite graph on \(m\ge3\) vertices whose largest part has size at most \(m/2\) has a Hamiltonian cycle: its minimum degree is at least \(m/2\), so Dirac's theorem applies. Reading the part names along such a cycle gives a cyclic word with the prescribed multiplicities and with no equal adjacent symbols.

## Proof
First suppose that \(N\) is odd. Since two parts have size \(t\), we have \(2t\le N\); parity strengthens this to \(t\le(N-1)/2\). By the Hamiltonian-cycle fact, label the vertices by \(\mathbb Z_N\) so that no two cyclically consecutive residues belong to the same part. Color every edge \(xy\) of \(G\) by
\[
c(xy)=x+y\pmod N,
\]
with residues represented by consecutive integer colors. At a fixed vertex \(x\), the map \(y\mapsto x+y\) is injective, so the coloring is proper. If \(P\) is the part containing \(x\), then the colors absent at \(x\), relative to the full residue palette, are exactly
\[
x+P=\{x+y:y\in P\}.
\]
The set \(P\) contains no two cyclically consecutive residues, and translation preserves that property. Hence the missing colors at \(x\) contain no consecutive integers. The coloring is weakly near-interval at every vertex.

Now suppose that \(N\) is even. Choose a smallest part \(P_0\) of size \(s\), choose a vertex \(\infty\in P_0\), and put \(q=N-1\). Label the remaining vertices by \(\mathbb Z_q\). Because \(r\ge3\), \(s\le N/3\). Give the finite vertices of \(P_0\) the labels
\[
S_0=\{0,3,6,\ldots,3(s-2)\}\subseteq\mathbb Z_q.
\]
When \(s=1\), this set is empty. The inequalities \(3(s-2)\le q-5\) when \(s\ge2\) show that no two elements of \(S_0\) differ by \(\pm1\) or \(\pm2\) modulo \(q\).

On \(\mathbb Z_q\), let \(H\) be the cycle joining residues that differ by \(\pm2\). It is a single cycle because \(q\) is odd. Let \(L=N-s\) be the number of vertices outside \(P_0\). Since the maximum part size is attained at least twice, the largest remaining part size is at most \(L/2\). Therefore the complete multipartite graph whose parts have the remaining sizes has a Hamiltonian cycle, yielding a cyclic word in the remaining part symbols with no equal adjacent symbols.

If \(S_0\) is empty, place this cyclic word directly around \(H\). If \(S_0\) is nonempty, deleting \(S_0\) from \(H\) leaves a disjoint union of paths. Concatenate their vertex orders and place a linear cut of the cyclic word along that concatenation. Every edge of \(H\) whose endpoints avoid \(S_0\) then joins different parts. Consequently, for every part other than \(P_0\), its finite label set contains no pair differing by \(\pm2\) modulo \(q\); the same is true of \(S_0\).

Use the standard one-factorization coloring of \(K_N\) on \(\mathbb Z_q\cup\{\infty\}\):
\[
c(\infty x)=x,\qquad c(xy)=2^{-1}(x+y)\pmod q
\]
for distinct finite \(x,y\), and restrict it to \(G\). This is proper: at a finite vertex \(x\), the finite edges use every residue except \(x\), while \(\infty x\) has color \(x\); at \(\infty\), the incident colors are all residues.

For a finite vertex \(x\notin P_0\), two missing colors can be consecutive modulo \(q\) only if the corresponding omitted same-part labels differ by \(\pm2\), which the construction forbids. For a finite vertex \(x\in P_0\), the missing-color set is
\[
\{2^{-1}(x+y):y\in S_0\},
\]
where the term \(y=x\) accounts for the omitted edge to \(\infty\); again no two are consecutive because \(S_0\) has no difference \(\pm2\). At \(\infty\), the missing colors are exactly \(S_0\), and these contain no consecutive residues because no two elements of \(S_0\) differ by \(\pm1\). Thus every vertex has a weak near-interval color set.

Combining the bipartite case, the published unique-largest-part case, and the two constructions above proves \(\operatorname{def}_{\mathrm{wloc}}(G)\le1\) for every complete multipartite graph. Since weak local deficiency is zero exactly for interval-colorable graphs, the stated dichotomy follows.

## Verification
The proof is symbolic and applies to arbitrary part sizes. A standalone verifier in `artifacts/verify.py` independently constructs the new tied-maximum colorings and checks properness and the weak near-interval condition for every integer partition of orders \(3\) through \(16\) to which the new argument applies. It checks \(222\) multipartite types and \(16133\) graph edges and prints `ALL CHECKS PASSED`.

The verifier is a finite stress test, not the proof of the infinite statement. The infinite proof uses only Dirac's theorem, elementary modular arithmetic, and the published Theorem 3.2 for the unique-largest-part case.

## Relationship to prior work
Casselgren and Petrosyan introduced weak local deficiency in arXiv:2609.15873v1. Their Theorem 3.1 proves the bound \(1\) for complete tripartite graphs, Theorem 3.2 proves it when the largest part is unique, and Theorem 3.3 proves the bound \(2\) for arbitrary complete multipartite graphs. Their Problem 6.6 explicitly asks whether a complete multipartite graph with weak local deficiency \(2\) exists. The theorem here answers that weak version negatively.

Asratian, Casselgren, and Petrosyan proved earlier that every complete multipartite graph admits a cyclic interval edge-coloring. That result does not imply the present theorem: a cyclic interval color set may wrap around the palette and leave one long ordinary consecutive gap. The 2026 paper cites this cyclic-interval literature and nevertheless leaves Problem 6.6 open, confirming that the two notions are not interchangeable.

published-finding corpus searches for the exact invariant, the weak-near-interval formulation, Problem 6.6, and the cyclic-interval alias found no statement covering the bound \(1\) for all complete multipartite graphs. The closest returned complete-multipartite records concern different interval-like or coloring invariants.

## Limitations
The result concerns weak local deficiency, not local deficiency. It therefore does not settle the local-deficiency half of Problem 6.6. The exact distinction between value \(0\) and value \(1\) still depends on the separate interval-colorability problem: the theorem identifies the weak local deficiency as \(0\) for interval-colorable instances and \(1\) otherwise, but it does not classify interval colorability for every multipartite parameter tuple.

The literature comparison was performed against the initiating full text, the full text of the cyclic-interval paper, targeted web searches, published-finding corpus, and the available prior ledger. Because the initiating problem is recent, later revisions or future publications could change the novelty status.

## References
1. C. J. Casselgren and P. A. Petrosyan, "Local measures of interval edge-uncolorability," arXiv:2609.15873v1, first posted 2026-09-14. https://arxiv.org/abs/2609.15873
2. A. S. Asratian, C. J. Casselgren, and P. A. Petrosyan, "Some Results on Cyclic Interval Edge Colorings of Graphs," arXiv:1606.09389v2; Journal of Graph Theory 87 (2018), 239--252. https://arxiv.org/abs/1606.09389
3. L. N. Muradyan, "On interval edge-colorings of complete multipartite graphs," Proceedings of the YSU A: Physical and Mathematical Sciences 56 (2022), 19--26. DOI: 10.46991/PYSU:A/2022.56.1.019.
