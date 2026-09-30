# Independent audit — 2026-09-29

Record: `2026/09/18/spectral-booksize-equality-balanced-multipartite--75d8398c42c7`  
Assigned and audited source tree: `e173104d48372f91b4000cf6a35f5cbec45e59c0`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `0574f471ca2659a0e6d79d463b028991ef8528f5`  
Disposition: **passed**

## Correctness

**independently_supported**. The equality classification is correct. Equality in bk(G)>=2lambda(G)-n forces equality through the degree-product and AM-GM chain on a spectral-radius component. The equality structure is regular or semiregular bipartite; the degree-sum constraint collapses the latter to regularity. Every edge then has N(u) union N(v)=V(G), so the graph is spanning and connected and its complement is induced-P3-free, hence a disjoint union of cliques. Regularity makes those cliques equal, giving a balanced complete multipartite graph. The converse is immediate. I independently exhaustively checked every graph on 2 through 5 vertices: the equality graphs are exactly the balanced complete multipartite ones.

## Originality

**subsequently_covered_by_source_revision**. The record was published 18 September 2026 against the then-current Liu--Ning version. A later arXiv v2, posted 24 September and updated 25 September with Yongtao Li added, now states in Proposition 3.6(a) that bk(G)=2lambda(G)-n exactly for regular Turan graphs T_{n,r} (r>=3 under its threshold hypotheses), which together with the bipartite endpoint covers the same equality family. Thus the mathematical finding survives, but it is no longer absent from the primary source literature. The audit does not infer dependence in either direction and does not assert priority beyond the record's dated provenance.

## Scientific value

**useful_independent_proof_now_convergent_with_primary_source**. The short equality-chain proof gives a transparent rigidity argument and remains scientifically useful, but the current v2 primary source now contains the same classification. Present-day novelty is therefore reduced relative to the record's publication date.

## Literature and evidence checked

- https://arxiv.org/abs/2609.20225
- https://arxiv.org/pdf/2609.20225v2
- https://doi.org/10.1006/jctb.2001.2052
- https://doi.org/10.1016/j.ejc.2004.01.007
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/spectral-booksize-equality-balanced-multipartite--75d8398c42c7
## Subsequent literature update

The September 24/25 arXiv v2 of 2609.20225 now contains Proposition 3.6(a), classifying equality in the 2lambda-n term by regular Turan graphs under its threshold hypothesis. This postdates the record's September 18 publication date. The audit therefore treats the record as a correct independently dated proof whose present-day novelty has been reduced by subsequent primary-source coverage; no inference of dependence or priority is made.

## Limitations

- The theorem is an equality classification, not a quantitative stability theorem.
- The primary source was materially revised after this record and now independently contains the same equality family.
- No claim of priority over the later v2 formulation is made by this audit.
