# Review of Exact proper conflict-free chromatic number of crown graphs

## Correctness assessment
PASS. The proof isolates the only way a color can occur on both sides of a crown graph: it must be used exactly on one deleted matched pair, so it is singleton on both sides. The four-color construction for \(n\ge4\) leaves two such shared singleton colors, guaranteeing a unique neighborhood color after any one deleted partner is omitted. The lower bound exhausts the possible numbers of shared colors in a coloring with at most three colors: zero forces a monochromatic side; one leaves the matched partner's vertex seeing only a repeated side-exclusive color; two cannot color both residual sides without making the third color shared; three shared colors cover only three vertices per side. The cases \(n=2\) and \(n=3\) are checked separately. `verify.py` exhaustively confirms minimality for \(n=2,3,4,5\) and checks the constructions through \(n=12\).

## Originality assessment
PASS, best-of-knowledge. Targeted searches used the terms “proper conflict-free crown graph,” “\(K_{n,n}\) minus perfect matching,” “deleted perfect matching,” “PCF crown graph,” and “open-neighborhood proper conflict-free crown graph.” They found the foundational PCF papers, complexity and general-bound literature, but no exact crown-graph statement or stronger theorem that specializes to this formula. Published-finding searches returned nearby bipartite coloring results—strong-majority edge coloring, prescribed colorings at maximum degree two, and rainbow path covers of \(K_{2,m}\)—but none concern proper conflict-free vertex coloring of crown graphs. The prior local ledger finding concerns odd coloring of complete multipartite graphs; it is not equivalent because crown graphs delete a perfect matching and the present condition requires a uniquely occurring neighborhood color rather than merely odd multiplicity.

## Value assessment
PASS. Crown graphs are a standard dense bipartite family with unbounded maximum degree. The exact constant value \(4\) for every \(n\ge4\), together with the shared-color structural lemma, provides a sharp benchmark for PCF algorithms and general upper bounds and cleanly separates high degree from PCF complexity on this family.

## Closest literature
- arXiv:2202.02570: introduction of proper conflict-free coloring with respect to neighborhoods; first public version 2022-02-05.
- arXiv:2203.01088: exact values on several basic graph classes and general PCF bounds.
- arXiv:2208.08330: NP-completeness of fixed-\(k\) PCF coloring on bipartite graphs.
- arXiv:2211.02818 / DOI:10.1137/23M1563281: general large-maximum-degree bounds; published MSC includes 05C15.
- DOI:10.1002/rsa.21285: asymptotically optimal general maximum-degree upper bound.

## Scientific limitations
The literature search is necessarily incomplete and cannot prove global novelty. The result does not classify all optimal colorings, does not address PCF list coloring or \(h\)-conflict-free coloring, and the finite exhaustive replay is not a formal proof.

Same-model review: passed. Independent audit: not yet performed.
