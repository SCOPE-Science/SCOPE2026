# Independent Audit — skewed-hajnal-szemeredi-maximum-degree-two--2b89b837f418

**Audit date:** 2026-09-29 (UTC)  
**Assigned/current source tree:** `3137296f4038fc8d05ffe08b020516ff0d306ba3`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree; no source-path file changed between the source-check commit and the current audited commit.

## Correctness — PASS

PASS. The auxiliary exact criterion for bipartite graphs of maximum degree two is correct: the complete color-to-component flow has no nontrivial cut obstruction beyond max c_i<=α(H), because for any two or more colors 2α(H_j)>=|H_j| on each path/even-cycle component; integrality then gives local multiplicities bounded by the relevant path/cycle independence number, and the standard no-equal-adjacent word criterion realizes them. The odd-cycle-transversal lemma is also correct: one can choose one vertex from every odd-cycle component inside a global maximum independent set and enlarge to ceil(n/3) vertices, leaving a bipartite graph. The three cases of Birken's conjecture then follow exactly as stated: Birken's theorem handles no large class, the transversal plus the bipartite criterion handles one large class, and Hajnal--Szemerédi plus splitting the third independent class handles the two-large-class case when m=2.

## Originality — PASS

PASS. Birken's September 2026 paper states the prescribed-size theorem up to floor(n/(r+1)) and then explicitly poses the s/s+1 extension as Conjecture 5. Targeted searches did not locate a prior resolution for r=2. Older bounded/prescribed coloring literature may contain variants of the auxiliary path/cycle criterion, so originality is assigned primarily to the theorem resolving Birken's new conjecture at maximum degree two, not to every ingredient.

## Scientific value — PASS

PASS. The theorem settles the first nontrivial maximum-degree case of an explicit recent Hajnal--Szemerédi strengthening, and the exact bipartite Δ<=2 criterion is a useful structural lemma. The proof is short but not merely computational and cleanly isolates why the nondivisible-order extra classes are feasible at degree two.

## Independent checks

- rederived the max-flow cut inequalities for all subsets of colors and checked integral-flow sufficiency
- checked the cyclic and path multiplicity arrangement criteria, including the dummy-symbol reduction for paths
- verified the odd-cycle representative set can be embedded in a maximum independent set and enlarged to ceil(n/3)
- checked all n=3s+m cases and residual class-size sums, including small s
- verified Birken's recent source describes the s+1 extension as Conjecture 5 and searched for the r=2 specialization and synonymous prescribed-coloring formulations
- confirmed no assigned record path changed between the dispatcher source-check commit and audited current main

## Limitations

- The result settles only r=2 and does not address Birken's conjecture for larger maximum degree.
- An equivalent older formulation of the auxiliary bipartite path/cycle criterion cannot be ruled out; the main originality verdict does not depend on that auxiliary lemma being wholly new.
- The conjecture is extremely recent, leaving a residual simultaneous-work risk.

## Evidence and references

- https://arxiv.org/abs/2609.18629
- https://arxiv.org/abs/2603.08259
- https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.134/LIPIcs.ICALP.2026.134.html
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/skewed-hajnal-szemeredi-maximum-degree-two--2b89b837f418

This audit changes only the independent-audit channel. Lean verification and expert attestation remain unchanged.
