# Self-review

## Correctness — PASS
The upper bound assigns each missing translated polytope to one of its violated facet halfspaces. The lower bound uses each relative-interior facet point \(p_j\) to construct an actual translated polytope whose intersection with the radius-\(R\) support ball is exactly the desired facet halfspace, since every other facet has clearance at least \(\eta\). Passing to the strict cutoff limit handles atoms. The contour formula follows from one-dimensional upper-ray quantiles; a one-coordinate segment law witnesses the sharp box threshold. The full quantifiers include every \(y\), every compactly supported law, every \(t\eta\ge 2R\) with \(t>0\), and degenerate support. The exact-rational checker passes 9,342 facet-witness checks plus four cutoff-gap witnesses; it does not substitute for the proof.

## Originality — PASS (priority remains provisional)
The closest directly pertinent source is Molchanov–Nagy (2026), read in arXiv full-text HTML. Their Theorem 5.2 establishes a limit under a boundary-null premise, not finite equality for arbitrary atomic measures; Section 7.4 gives arrangement computation, not a universal finite stopping time. Their other geometric depth and erosion identities do not imply eventual constancy from the limit statement. The older halfspace-depth literature concerns the unrestricted normal set rather than exact finite stabilization for translated polytopes. Targeted mathematical-record comparisons and primary literature searches revealed no claim covering the finite cutoff and its sharp parallelotope form. Unindexed earlier directional-depth work remains a genuine priority risk.

## Value — PASS
This resolves whether asymptotic convergence can be replaced by exact finite termination for the entire class of full-dimensional polytopal testing bodies, uniformly over query points and for probability laws with arbitrary atoms and dependence. It converts a high-dimensional continuum-of-translates optimization into finitely many univariate quantiles, gives exact polyhedral level regions and a computable finite cutoff, and proves the optimal geometric scale in the canonical parallelotope model. These structural and sharp-limit facts are not a numerical recomputation or an arbitrary parameter slice.

## Closest work, scope and limitations
Molchanov and Nagy, arXiv:2610.26108v1, Sections 2 and 5–7. The result applies to compactly supported measures and finite-sided full-dimensional polytopes. The general sufficient cutoff may be conservative. Independent historical priority and scientific validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
