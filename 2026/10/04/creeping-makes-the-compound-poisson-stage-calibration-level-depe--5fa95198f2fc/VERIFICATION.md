---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the subordinator \(X_t=ct+\sum_{j\le N_t}G_j\), first passage at level \(x\) can occur continuously or by a jump. The creeping probability has Laplace transform \(c/\psi(s)\) with \(\psi(s)=cs+\lambda\theta s/(1+\theta s)\), which decomposes into the stated constant plus exponential term and yields \(q(x)=c/(c+\lambda\theta)+(\lambda\theta)/(c+\lambda\theta)e^{-\kappa x}\). Conditional on jump crossing, exponential memorylessness makes the overshoot exponential with mean \(\theta\), so \(E O_x=\theta(1-q(x))\). Since \(\tau_x\le x/c\), optional stopping of \(X_t-(c+\lambda\theta)t\) is justified and gives \((c+\lambda\theta)E\tau_x=x+EO_x\). Subtracting levels gives the positive correction. A fresh independent numerical reconstruction at \(c=\lambda=\theta=1,a=1,b=2\) gives \(E(\tau_2-\tau_1)=0.5292549110869696\), matching the closed form.

## originality

PASS

The motivating 2026 biological paper correctly distinguishes zero overshoot under continuous crossing from exponential overshoot conditional on jump crossing, but then explicitly replaces the unconditional mean overshoot at each boundary by \(	heta\) and cancels the two terms, producing its calibration equations (3.10)-(3.11). General Lévy first-passage literature already studies overshoot/undershoot and creeping, so no novelty is claimed for those concepts. The new scientific point is the source-specific finite-level atom/mean formula and the resulting positive level-dependent correction to the exact calibration identity. Current published-finding and literature searches found no prior statement of that correction for this model.

## value

PASS

The correction changes the exact stage-duration calibration used to fit the biological model: the omitted term is strictly positive and depends on the absolute stage levels, so the source identity is not merely imprecise notation. Providing a closed-form correction for the paper’s own constant-temperature special case is a substantive model-validation result even though it does not re-fit the field data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
