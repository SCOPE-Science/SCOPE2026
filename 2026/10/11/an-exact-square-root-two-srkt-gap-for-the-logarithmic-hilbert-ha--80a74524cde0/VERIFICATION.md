---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For ψ(z)=-log(1-z) and normalized Szego kernels, disk automorphism ψ(φ_w(z))-ψ(w)=log(1-conj(w)z)-log(1+ηz) (|η|=1) gives exact Fourier coefficients ((-η)^n-conj(w)^n)/n. Parseval gives Φ(w)=π²/6+Li₂(|w|²)-2Re Li₂(-ηw). Angular monotonicity bounds Φ(w)≤π²/6+2Li₂(|w|), with equality for real positive w and limit π²/2. Separately Schur with p_j=(j+1/2)^(-1/2), convex midpoint quadrature and beta integral bounds Hilbert-matrix norm by π; log-block positive Rayleigh vectors give limiting lower bound π. The Bonsall identity equates kernel variance to testing norm. Positive-definite moment Gram blocks of arbitrarily large size prove infinite rank. All quantifiers over w in disk, not just tested sample points; finite checks are corroboration only.

## originality

PASS

Best-of-knowledge originality for the exact paired pi versus pi/sqrt(2) norm for the natural unbounded logarithmic symbol. The Hilbert norm pi and general Poisson/kernel identity are classical, not attributed as new. Published mathematical results inspected for finite-rank and polynomial SRKT do not cover the infinite-rank Hilbert symbol. Crucially the later arXiv v2 full text could not be re-read after multiple lawful access attempts and a safety-blocked authorized retrieval; its exact contents remain an explicit priority risk. No negative search is treated as proof of novelty.

## value

PASS

A canonical unbounded BMOA function generates the classical infinite-rank Hilbert Hankel matrix. Its exact Garsia/kernel-testing norm is a naturally motivated and separately computable invariant compared with the full operator norm; the ratio 1/sqrt2 quantitatively exhibits failure of the SRKT precisely in the 2026 unbounded-symbol research context. This is a useful sharp-for-the-symbol benchmark, not merely a routine relabeling, and neither claims a universal separation nor resolves existence of positive unbounded SRKT symbols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
