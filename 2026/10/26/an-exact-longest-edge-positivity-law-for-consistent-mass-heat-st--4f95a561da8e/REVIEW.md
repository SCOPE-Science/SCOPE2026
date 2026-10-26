# Scientific review

**Correctness — PASS.** The proof uses an exact branch Schur complement of the assembled positive-definite mass-plus-stiffness matrix. It establishes positive diagonal and adjacent update entries for all positive steps and constructs a **strict negative distance-two entry** for every edge with \(t<h_e^2/6\). For steps above the boundary, Stieltjes inverse positivity proves the other direction. All quantifiers, the isolated zero-step point, and the two-node exception are included. The standalone exact-rational test independently assembles finite-element edge matrices and exercises both strict inequalities and equality cases.

**Originality — PASS (with residual risk).** The closest inspected primary sources concern sufficient Stieltjes conditions and more general positivity thresholds on polygonal-domain meshes, not the exact necessary-and-sufficient metric-tree Neumann/Kirchhoff classification with an explicit negative two-hop witness. An existing exact path-mesh result has a different geometry and Dirichlet boundary elimination, so it is not a stronger theorem covering branching metric trees. Broad searches did not identify a matching original result; they do not prove uniqueness. A relevant 2015 author-hosted PDF could not be read and a specialized graph-network treatment remains possible.

**Value — PASS.** Branched heat-transport networks naturally use Kirchhoff-coupled metric edges. The result replaces a general one-sided nonnegativity time-step test with an exact **all-tree** criterion involving only the longest element, independent of number of junctions, grading, and branching. Its local distance-two sign certificate shows which mesh element destroys positivity and provides a direct diagnostic and benchmark for solvers. This substantive network-wide necessity statement is not just a rephrasing of Stieltjes sufficiency.

**Main limitations.** Constant diffusivity, natural Neumann/Kirchhoff vertices, consistent linear finite elements, single backward-Euler step, and trees only; no cyclic network assertion. Specialized unpublished or inaccessible prior coverage remains a risk.

Self-review: passed. Independent audit: not yet performed.
