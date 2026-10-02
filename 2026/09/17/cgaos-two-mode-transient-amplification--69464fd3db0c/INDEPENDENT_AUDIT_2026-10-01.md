---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

After one exact conjugate-gradient initialization step on a two-eigenmode strictly convex quadratic, the CG_AOS/Dai–Yuan step has exact distortion \(r=\mu L/(\mu^2\cos^2\theta+L^2\sin^2\theta)\), objective factor \((r-1)^2\), worst transient factor approaching \((\kappa-1)^2\), sharp scalar decrease safeguard \(0<\gamma\le 2/\kappa\), and an explicit family with \(f(x_2)/f(x_0)\sim \kappa/4\).

## Correctness — PASS

The two-mode proof was reconstructed independently. In the orthonormal basis aligned with the first direction, the true second-direction curvature gives \(v^TAv=a\det A\) and the AOS model gives \(v^T\bar Bv=a(a^2+h^2)\); substituting a rotated two-eigenvalue matrix yields the displayed distortion. A separate symbolic recomputation of the diagonal family reproduced \(r=(\kappa^2+1)/(2\kappa)\), the exact objective ratios, and the \(\kappa/4\) asymptotic. The package verifier was inspected rather than treated as proof by log alone.

**Evidence:** package RESULT.md; artifacts/verify_transient.py blob 09c6719e5101eb47d3d35ad0f3a6a8ec67f8fa27; Z. Liu, arXiv:2604.20506

**Residual risk:** The theorem concerns the first AOS step after exact initialization on a two-mode invariant subspace; it is not a global divergence result.

## Originality — PASS

The exact two-mode distortion, sharp transient factor, explicit \(\kappa/4\) excursion family, and \(2/\kappa\) safeguard were not found in the source algorithm paper, the closest 2024 Dai–Liao/AOS paper, published-corpus searches, or semantic searches. The source algorithm paper explicitly leaves CG_AOS convergence/rates open. The 2024 paper's accessible abstract describes a different Dai–Liao parameter construction with descent/convergence under additional conditions rather than this CG_AOS step.

**Equivalent formulations.** The audited formula is a local exact identity for the source CG_AOS model, not merely a generic nonlinear-CG convergence bound.

**Broader coverage.** Those results do not imply the exact distortion or sharp safeguard for the audited algorithm.

**Exact database or table.** This is an analytic formula rather than a database lookup.

**Claim versus prior implication.** No checked prior implication mechanically yields the final claim.

**Checked sources:** https://arxiv.org/abs/2604.20506; https://doi.org/10.1080/01630563.2024.2333255; semantic published-corpus search

**Residual risk:** The 2024 Dai–Liao paper full text was not available, so an unnoticed related local calculation remains a limited risk; its stated method and claims differ materially.

## Value — PASS

The result identifies a sharp, condition-number-scale obstruction in a newly proposed CG stepsize whose global theory is explicitly open, and gives an exact safeguard threshold. This is a motivated boundary mechanism relevant to any future convergence proof, not an arbitrary numerical slice.

**Residual risk:** Value is diagnostic/local rather than a complete convergence theorem.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
