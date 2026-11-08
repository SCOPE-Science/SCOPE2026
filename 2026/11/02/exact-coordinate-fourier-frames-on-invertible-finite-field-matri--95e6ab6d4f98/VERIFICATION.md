---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The uniform nonzero first column gives rank-one character mean a=-1/(q^d-1). Averaging an independent ordered first-two-column pair yields rank-two mean b=1/((q^d-1)(q^(d-1)-1)), valid for any nontrivial additive character and all prime powers. Coordinate Gram entries form a rook-scheme block: all-ones mode lambda0=1+2(d-1)a+(d-1)^2*b, row/column contrasts lambda1=1+(d-2)a-(d-1)b (multiplicity 2(d-1)), zero-row/column contrasts lambda2=1-2a+b (multiplicity (d-1)^2). The constant couples to all ones via d*a giving two roots mu±=(1+lambda0 ±sqrt((1-lambda0)^2+4d^2*a^2))/2. Multiplicities sum to d²+1. Direct elementary inequalities, including q=d=2, show mu_->0, and determinant comparison with lambda2 has sign controlled by (4-d)+(6-2d)t-(d-2)t² for t=1/(q^(d-1)-1); hence upper lambda2 for d=2,3 and mu+ for d>=4. Independent direct uniform GL matrix enumeration verified rank1 and rank2 Fourier averages for (q,d)=(2,2),(3,2),(5,2),(2,3); full package NumPy spectrum checker was inspected. Finite checks do not prove arbitrary fields.

## originality

PASS

Delsarte 1978 determines general matrix rank-metric character sums and is credited for the rank-one and rank-two input. The present natural band (constant plus each coordinate Fourier character) has a particular rook decomposition, sharp upper-mode dimension-four switch and Riesz bounds; related Resultary SL2, rank-one and symplectic sampling families have different domains, with an overlap q=2,d=2 already known. Originality is qualified because Delsarte full text and possible broader matrix association scheme spectral treatment were not fully inspected. An authorized institutional attempt for the same primary DOI was blocked by safety checks and was not retried/bypassed.

## value

PASS

The complete sharp frame Gram eigenvalue spectrum for invertible matrices is a natural Fourier restriction invariant and answers both independence and optimal conditioning. An unexpected dimension-four universal switch and fixed-q asymptotic tightness are nontrivial structural properties beyond merely plugging rank-character sums into a formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
