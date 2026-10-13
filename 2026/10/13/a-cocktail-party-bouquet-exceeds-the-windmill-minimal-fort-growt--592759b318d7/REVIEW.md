# Scientific review

## Correctness — PASS
The proof directly separates hub-free from hub-containing forts. In the local block \(K_6-M_3\), the only minimal forts are three mate pairs and eight transversal triples; every pair dominates the block, while only nonmate pairs can appear in a globally inclusion-minimal hub-containing fort. The resulting disjoint enumeration proves \(P_{B_r}(z)=3rz^2+8rz^3+12^rz^{2r+1}\) for all positive integers \(r\), including the degree overlap at \(r=1\). Direct exhaustive checking for \(r=1,2,3\), including every proper subfort, agreed with the symbolic coefficients (532,605 nonempty subsets). The infinite statement rests on the proof, not these finite checks.

## Originality — PASS, with residual risk
Becker et al. (arXiv:2404.05963v1, 2024) already establish methods involving graph vertex amalgamation and prove the \(3^{1/3}\) windmill growth base, so neither is new. Earlier complete-multipartite fort classification already includes the individual \(K_{2,2,2}\) block. The inspected primary paper's windmill theorem and table do not provide the bouquet polynomial or \(12^{1/6}\) base; the new graph combines a particular dense deleted-matching page with an exact global-minimality argument. Search results do not show an equivalent published classification, but absence from indexed searches is not a uniqueness proof. An unindexed equivalent graph-bouquet construction remains possible.

## Value — PASS
The 2024 paper explicitly conjectures graph families with more minimal forts per vertex than the windmill benchmark. The new construction supplies a rigorously proved, strictly higher asymptotic base, alongside every coefficient of a natural minimal-fort polynomial. This is a substantive extremal growth improvement rather than a routine recalculation of the six-vertex block. Its limit applies to orders \(6r+1\), so it should not be misrepresented as proving every-order convergence or optimality.

## Closest literature and limits
Primary source: Becker, Cameron, Hanely, Ong, Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1, Sections 2, 5.3, Corollaries 28–29, Conjecture 31. An earlier exact complete-multipartite fort classification covers local blocks, not the combined graphs. Reproducibility code checks only \(r\le3\); analytic proof covers all \(r\ge1\). Prior-source indexing is incomplete, and independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
