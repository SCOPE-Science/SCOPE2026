---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Every inverse branch is phi_i(u)=c_i+eps_i ell_i(u-1/2) with Lebesgue-preserving Perron P f = sum ell_i f(phi_i(u)). For g=u-1/2 and h=g^2-1/12 the invariant two-dimensional polynomial span obeys Pg=theta*g, Ph=A*h+B*g, with theta=sum eps_i ell_i^2, A=sum ell_i^3>0, B=2 sum eps_i ell_i^2(c_i-1/2). Iterating gives P^m h=A^m h+B sum_{q=0}^{m-1} A^{m-1-q}theta^q g. Transfer duality twice and orthogonality ∫g h=0, ∫g^2=1/12 imply C_{j,m}=(B theta^j/12) sum A^{m-1-q}theta^q for ALL j,m>=1. Thus C_{1,2}-C_{2,1}=theta A B/12; since A>0, full gap symmetry iff theta B=0. For four equal branches one flipped sign at positions 1 versus 2 gives common theta=1/8 and A=1/16, but B=3/32 versus1/32 and C11=1/1024 versus1/3072. For skew tents differentiate t(1-t^2)(1+3t^2)/192 to get positive critical t^2=(3+2sqrt(6))/15. Independent exact inverse-cylinder cubic integration for these witnesses reproduced moments and reversal contrasts. Positive gaps and Lebesgue stationarity are essential; no claim of full path reversibility.

## originality

PASS

Best-of-knowledge: earlier authors give exactly the pair autocorrelation invariants theta and A for these maps, but the explicitly evaluated two-positive-gap cubic tensor, its reversal criterion, and pair-ACF indistinguishability witness are additional statements.

## value

PASS

Higher-order time correlations can separate deterministic dynamical systems with identical entire linear and centered-square autocorrelation sequences. The exact two-gap tensor and symmetry condition quantify a motivated identifiability and temporal-direction invariant; skew-tent extremal point is natural within that subfamily and is not a free arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
