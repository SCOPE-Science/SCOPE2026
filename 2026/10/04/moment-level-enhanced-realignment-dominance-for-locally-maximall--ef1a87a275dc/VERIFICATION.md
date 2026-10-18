---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Direct index contraction for R(X)_{ik,jl}=X_{ij,kl} shows centered realignment annihilates normalized identity directions when marginals are maximally mixed. R(rho) is orthogonally a scalar c=1/sqrt(dA dB) plus centered B, so r_k(rho)=r_k(tilde rho)+c^(2k) for all k. Scaling a feasible centered truncated-moment vector by sqrt G and appending c gives an uncentered feasible vector, proving alpha_m quantitative bound; Cauchy-Schwarz gives sqrt G+c<=1. Independently tested random complex Hermitian LMM examples in 2x2,2x3,3x4 with moment errors <6e-17. Technical minor: the displayed general left-partial-trace row identity in RESULT.md uses a conjugate-star where a plain transpose is required for arbitrary complex X under the stated indexing; for the only uses, Tr_A tilde rho=0 and rho_A=I/d_A, both sides coincide, so the theorem and required orthogonal blocks are unaffected.

## originality

PASS

Mallick-Gulati-Nechita explicitly leave the finite-moment centered versus uncentered comparison open for arbitrary marginals; the audited orthogonal identity block proves it for LMM states. Earlier enhanced realignment/correlation tensor work supplies identity-traceless decompositions but no checked first-moment-to-all-finite-moment feasible-vector transfer on this full LMM class. Relevant primary full text 2609.29471 was inaccessible on attempted arXiv/OA and Oxford worker returned error; this is recorded, not treated as proof of absence.

## value

PASS

The theorem resolves a logically meaningful full subcase (all dA,dB>=2, every finite truncation m) of an explicit open problem in optimized separability criteria, with quantitative rather than only asymptotic trace-norm transfer. The maximally mixed marginal class is natural in quantum information and the block argument is structural.

The dated certificate retains the supplied scientific assessment, sources and limitations.
