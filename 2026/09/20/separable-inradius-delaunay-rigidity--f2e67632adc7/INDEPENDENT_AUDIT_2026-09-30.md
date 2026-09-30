# Independent audit — 2026-09-30

**Record:** `2026/09/20/separable-inradius-delaunay-rigidity--f2e67632adc7`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `66a2f333e68aafe17a913381d0938a3cb592a427`  
**Disposition:** **PASSED**

## Correctness — PASS

Universal four-point Delaunay extremality from the two sides of a cyclic quadrilateral forces equality on every cyclic quadrilateral. The displayed cyclic kite realizes arbitrary midpoint pairs: its two AC inradii are u and the BD inradii are u(1±delta), with delta spanning (-1,1) and scaling making u arbitrary. Continuity therefore reduces the problem to the midpoint Jensen equation and forces phi affine. The explicit noncyclic quadrilateral fixes the slope sign; Lambert's linear inradius theorem gives the converse. Strict convexity/concavity plus a near-cyclic perturbation gives the p≠1 power counterexamples.

## Originality — PASS (literature-bounded)

Lambert (1994) establishes the linear mean/sum-inradius Delaunay criterion, and the Japanese theorem supplies cyclic invariance for the untransformed sum. Searches of the open proceedings index, later Delaunay-optimality literature, Japanese-theorem literature, and separable/convex-transform formulations did not locate the affine-rigidity characterization or the near-cyclic power-sum counterexamples.

## Scientific value — PASS

The result identifies the exact continuous separable transform class for universal Delaunay inradius extremality and explains why the linear inradius criterion is exceptional, contrasting sharply with more flexible circumradius functionals.

## Evidence and literature

- CCCG 1994 proceedings index containing Lambert, The Delaunay Triangulation Maximizes the Mean Inradius: https://cg.cs.carleton.ca/proceedings/1994/Contents.pdf
- Dolbilin–Edelsbrunner–Musin, On the Optimality of Functionals over Triangulations of Delaunay Sets: https://arxiv.org/abs/1209.3541
- Minculete–Barbu–Szöllősy, About the Japanese Theorem: https://cms.math.ca/wp-content/uploads/crux-pdfs/CRUXv38n5.pdf

## Limitations

- Continuity of phi is assumed; no weakest-regularity theorem is claimed.
- Lambert's original six-page paper was verified through open proceedings/bibliographic and later-source statements rather than a fully extracted original text; it remains the closest residual priority risk.
