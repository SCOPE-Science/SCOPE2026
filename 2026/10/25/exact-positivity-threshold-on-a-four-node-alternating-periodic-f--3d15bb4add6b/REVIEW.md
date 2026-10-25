# Review

**Correctness — PASS.** The consistent mass and stiffness matrices are stated explicitly. The transition entries share a positive denominator; every diagonal and edge-class numerator is positive for positive step size, while the only potentially negative entries are the opposite-node entries. Their sign is governed by a strictly increasing quadratic with one positive root, yielding the exact necessary-and-sufficient threshold.

**Originality — PASS, with a documented literature-access risk.** The result is restricted to the four-node periodic alternating mesh and gives an explicit contrast-dependent formula. The equal-cell specialization is not claimed as new. The accessible primary literature discusses finite-element positivity thresholds and sufficient timestep bounds, but the inspected material does not state this exact periodic formula. The full text of the closest 2015 heat-equation article could not be retrieved, so a possible uninspected special-case overlap remains a residual risk.

**Value — PASS.** The formula quantifies when a common maximum-cell sufficient restriction is conservative on the smallest nonuniform periodic mesh. As the ratio of the shorter to the longer cell tends to zero, the exact threshold divided by the longer cell length squared tends to zero. This gives a concrete, mathematically proved contrast effect relevant to step-size selection, without asserting a general mesh theorem.

**Closest literature and limitations.** P. Chatzipantelidis, Z. Horváth, and V. Thomée (2015), DOI 10.1515/cmam-2015-0018, study heat-equation positivity for piecewise-linear finite elements with homogeneous Dirichlet boundary conditions. B. Jin, R. Lazarov, V. Thomée, and Z. Zhou (arXiv:1510.02825; 2017 journal version) study broader nonnegativity-preservation questions and timestep bounds. The result here is only for the stated four-node periodic mesh. The closest 2015 article's full text remains inaccessible, and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
