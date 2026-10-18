---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For the complete projective direction set P1(Z/N), weighted line-sum normalization sqrt(w_d/N) gives T_w*T_w diagonal in normalized Fourier characters with eigenvalue lambda_xi=sum_{<xi,d>=0}w_d. For primitive nonzero xi, there is exactly one perpendicular projective direction, and every direction is realized; hence the nonconstant minimal eigenvalue is min w_d. For any nonzero xi, choose a prime p with nonzero p-primary component; its reduction constrains all orthogonal directions to one mod-p projective fiber, yielding lambda_xi<=W_{p,ell}; conversely a character whose p^k local coordinate is p^(k-1) times a perpendicular nonzero mod-p vector and other local components vanish realizes *exactly* W_{p,ell}. Thus maximum is max_{p|N,ell} W_{p,ell}. Average over least-prime p_* fibers and min w_d <=S/D_N gives sharp kappa_0²>=D_N/(p_*+1), with equality only if all direction weights coincide. Local CRT count of orthogonality directions (p^v for nonzero local valuation v, p^(k-1)(p+1) for zero) and local frequency multiplicities p^{2(k-v)}-p^{2(k-v-1)} exhaust N² characters, proving full uniform spectrum. Independent construction of projective sets and weighted nonzero character eigenvalues for N=2..14 confirmed min/max and D_N, not infinity.

## originality

PASS

Best-of-knowledge originality for acquisition-weight constrained minimax and its unique optimizer, not for the classical discrete Fourier-slice principle. Source abstract and related orthogonalization literature were compared at objective level. A highly plausible primary 2005 full text remained inaccessible after open-source and institutional routes, so priority risk is retained explicitly rather than converting access trouble into O failure.

## value

PASS

Cyclic projective Radon transforms and scalar acquisition weights are natural discrete tomography objects. The theorem quantifies a sharp arithmetic conditioning barrier tied to the smallest prime, identifies the uniquely best positive view schedule and supplies exact mode multiplicities. It is mathematically useful even where more general frequency filtering can do better.

The dated certificate retains the supplied scientific assessment, sources and limitations.
