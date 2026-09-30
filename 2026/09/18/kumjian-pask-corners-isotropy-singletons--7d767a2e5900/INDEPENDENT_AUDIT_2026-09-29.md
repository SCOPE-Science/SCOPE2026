# Independent audit — 2026-09-29

**Record:** `2026/09/18/kumjian-pask-corners-isotropy-singletons--7d767a2e5900`  
**Title:** Vertex corners and isotropy point masses in Kumjian–Pask algebras  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `1fd7936c6d529e1993ec1240bf805de35c4eb2fa`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The two correction criteria are correct. Cutting a Steinberg algebra by 1_{Z(v)} gives the reduction to Z(v); if the corner is only R·1_{Z(v)}, Boolean separation forces Z(v) to be a singleton, and the remaining corner is the group algebra of the isotropy group, hence scalar exactly when the periodicity group is trivial. Likewise, a singleton isotropy characteristic function is a Steinberg element exactly when the underlying unit is open: local constancy gives the forward implication and an ample bisection gives the converse. The one-loop and two-loop examples then invalidate the quoted universal corner and singleton-embedding assertions.

## Originality

**PASS** — The reduction/corner mechanism and open-singleton/minimal-ideal facts are prior work and are properly disclaimed. The distinct contribution is the application of those facts to diagnose two concrete universal assertions in arXiv:2609.20230v1, identify the exact missing hypotheses, and repair the unital restriction construction. Current searches located only v1 and no public correction stating this package.

## Scientific value

**PASS** — The record prevents two representation-theoretic constructions from being used outside their valid hypotheses and supplies minimal counterexamples plus the correct corner/source-fiber alternatives. As a correction note its value is narrower than a new structural theorem, but it is mathematically consequential for the recent preprint's induction/restriction framework.

## Findings

- The scalar-corner criterion follows from the Steinberg reduction and the free R-basis of a nontrivial isotropy group algebra.
- For a finite vertex set, a singleton infinite-path cylinder necessarily becomes periodic along a repeated vertex, so it cannot also be aperiodic.
- Singleton isotropy point masses lie in a Hausdorff ample Steinberg algebra exactly at open singleton units.
- The record correctly distinguishes unital restriction e_xM from naive restriction of all of M along the corner inclusion.

## Independent checks

- Reconstructed both implications of the vertex-corner criterion directly from the groupoid model.
- Checked the finite-vertex periodicity argument and the one-loop/two-loop counterexamples.
- Reconstructed the open-singleton isotropy proof for a general Hausdorff ample groupoid.
- Compared the structural ingredients with Abrams–Dokuchaev–Nam and Clark et al.; searched the current arXiv record for a revision/correction.

## Sources

- https://arxiv.org/abs/2609.20230 — Recent Kumjian–Pask induction/restriction preprint targeted by the correction; current search still exposes v1 only.
- https://arxiv.org/abs/1909.03964 — Prior corner/reduction context for Steinberg and graph algebras.
- https://arxiv.org/abs/2502.15574 — Prior open-singleton/minimal-ideal and Kumjian–Pask socle context.
- https://arxiv.org/abs/2006.09931 — Prior source-fiber induction for graded Steinberg algebras.

## Limitations

- The structural corner and open-singleton ingredients are not new; originality is only in the diagnosis and exact repair of the recent preprint.
- The audit did not reassess the preprint's unrelated theorems.
- The current arXiv full text was not available through the browsing endpoint during this run; the audit therefore does not claim to have reread inaccessible sections beyond the record's exact quotations and currently indexed abstract/version metadata.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
