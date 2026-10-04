# Review of Exact secure domination number of connected chain graphs

## Correctness
**PASS.** The proof has three independent structural pieces. The common-support leaf-twin lemma is an exact reduction in both directions; after trimming, a universal bipartite argument forces \(\gamma_s\ge\min\{4,|X|,|Y|\}\); and matching upper bounds come from an entire bipartition side or the four extreme vertices of a nested-neighborhood ordering. The exceptional cases are included rather than discarded. Exhaustive exact checking on all \(511\) canonical connected chain profiles of total order at most \(10\) matches the theorem and rechecks the twin reduction.

## Originality
**PASS.** The closest source is arXiv:2512.23989v2, Section 3.3. Its Algorithm 2 begins with four extreme vertices and adds all but one multiple pendant on each end. The theorem here is not implied by that routine: on the half graph \(H_3\), the displayed routine returns four vertices, but one whole bipartition side is a secure dominating set of size \(3\), and the general bipartite lower bound rules out size \(2\). Focused searches under chain graph, half graph, and Ferrers graph terminology did not locate the closed formula. Secure total domination on chain graphs is a distinct stronger parameter.

## Value
**PASS.** The result is a complete exact formula for a standard graph class. It reduces the optimum to leaf multiplicities and bipartition sizes, supplies a constant-time evaluation once the chain representation is known, explains exactly when four guards are necessary, and identifies a concrete small-side boundary missed by the closest same-object routine.

## Closest literature and limitations
The archive-era source *Finite Order Domination in Graphs* provides the secure-domination protection framework and lists AMS 05C69; the public manuscript copy is dated 11 September 2003. The closest same-object source is arXiv:2512.23989v2. Jha's DOI:10.1016/j.akcej.2019.10.005 treats secure total domination instead. The theorem does not classify all minimum sets, and its finite verifier is supplementary rather than an infinite proof. A 2003 Bulletin article was bibliographically identified but its full text was not available for direct inspection; this remains a minor historical overlap risk.

Same-model review: passed. Independent audit: not yet performed.
