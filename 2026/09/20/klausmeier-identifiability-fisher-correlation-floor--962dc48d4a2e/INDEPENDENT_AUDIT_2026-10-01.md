# Independent mathematical audit — SCOPE-20260920-962dc48d4a2e

Final disposition: **PASS**.

## Correctness
**PASS** — The trajectory identities follow by integrating the two ODEs and using \((\log n)'=wn-m\) when biomass is positive; on the invariant desert state, \(m\) disappears. At a positive equilibrium the inverse map is \((a,m)=(w(1+n^2),wn)\), with determinant \(w(1-n^2)\). Independent symbolic algebra reproduces the covariance \(D\Psi D\Psi^T\), the exact formula for \(1-\rho^2\), the unique critical point \(n^2=1+\sqrt{2(1+m^2)}\), and the stated closed correlation floor. Thus the structural/practical-identifiability distinction and the numerical value at \(m=0.45\) are correct under the stated observation model.

## Originality
**PASS** — Targeted searches found no published record with the exact full-state trajectory recovery dichotomy or the sharp equilibrium-only Fisher-correlation floor. The directly motivating 2026 preprint is highly relevant but only its primary abstract was accessible; open-access and authorized full-text attempts did not yield a verified PDF. The abstract discusses practical joint-inference difficulty near the bifurcation but does not state these exact formulas. Under the inaccessible-source rule, originality therefore passes only to the best of current knowledge, with hidden full-text overlap retained as a material risk.

### Equivalent formulations
Equivalent structural-identifiability and inverse-geometry formulations were compared; no inspected source states the exact dichotomy plus floor.

### Broader coverage
The broader model literature supplies context but does not mechanically imply the audited combined result.

### Exact database or table
There is no intrinsic finite database here; the search was for prior theorem coverage, not used alone as novelty proof.

### Claim versus prior implication
No inspected prior implication determines the final claim.

## Value
**PASS** — The exact formulas answer a concrete inference question posed by the motivating model study: they separate true structural non-identifiability on the desert invariant set from severe but full-rank correlation on the vegetated branch, and quantify the latter with a sharp global floor. This is a motivated natural inverse-geometry fact rather than an arbitrary computation.

## Source inspections
- **The Role of Bifurcations in Parameter Estimation: A UQ Analysis of the Non-spatial Klausmeier Model** (https://arxiv.org/abs/2609.18231): primary abstract; open-access full text was unavailable and a subsequent authorized retrieval attempt returned no verified PDF Method: primary record plus lawful full-text retrieval attempts. Assessment: ABSTRACT_ONLY_WITH_RESIDUAL_OVERLAP_RISK. Evidence: The accessible abstract reports practical parameter-estimation difficulty around the bifurcation but not the exact trajectory-recovery identities or Fisher-correlation floor.

## Checked sources
- https://arxiv.org/abs/2609.18231

## Residual risks
- The highly relevant 2026 preprint could not be inspected in full, so an internal derivation of some or all formulas remains possible.
- The Fisher floor is specific to repeated isotropic Gaussian full-state equilibrium observations and does not determine finite-sample posterior correlation under other designs.
