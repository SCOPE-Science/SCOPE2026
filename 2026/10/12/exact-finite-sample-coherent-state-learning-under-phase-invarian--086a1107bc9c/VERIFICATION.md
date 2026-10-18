---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Independent reconstruction: passive compression sends n identical coherent training modes to |sqrt(n)α>; common uniform phase forces orthogonal fixed-total-number sectors. Each sector is a difference of two nonnegative rank-one operators of weights a_k,b_k and overlap q_k=(n/(n+1))^k. Determinant is -a_k b_k(1-q_k), and rank-two spectral formula gives sqrt((a_k-b_k)^2+4a_k b_k(1-q_k)); sum finite in trace norm since Σa_k=Σb_k=1. Correct equal-prior Helstrom risk =1/2−sum/4. Gaussian mixing gives geometric weights. For v=μ²/n, dominated convergence with geometric envelope and n(1−q_k)≤k gives stated polylogarithmic sqrt(n) coefficient. Independently computed n=1,v=1 P_err=0.21356409008208982 and n=10000 local coefficient 0.3374226648786782 versus limit 0.33681343818393766. Tests do not prove infinite sum or limit.

## originality

PASS

Full primary shared-model article gives averaged hypotheses and perturbative Gaussian analysis but not the evaluated all-radial exact Helstrom series or singular circular local scaling; general Helstrom/twirling already known. Best-of-knowledge PASS with explicit stronger-coverage risk.

## value

PASS

Genuine finite-sample Bayes optimum and implementable mathematical photon-number-sector measurement for an entire natural rotationally invariant prior class, with quantitative certified Gaussian truncation and singular learning limit; neither an arbitrary parameter point nor mere application of a supplied numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
