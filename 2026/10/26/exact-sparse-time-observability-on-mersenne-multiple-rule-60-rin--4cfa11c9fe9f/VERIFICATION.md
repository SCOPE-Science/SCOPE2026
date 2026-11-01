---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The time-jq observation rows of one fixed Rule 60 site correspond to 1,H,H²,... in F2[X]/(X^n-1) for H=(1+X)^q; row rank is the degree of the minimal polynomial of H, with initial powers independent. Over F_(2^r), X^n-1 splits into m=2^r-1 distinct mth roots, each of local thickness 2^a. The root at X=1 yields nilpotent exponent ceil(2^a/q), whereas each other root has leading nonzero w^(2^b) term, exponent 2^max(a-b,0); power-map collisions on F_(2^r)^× number h=m-1 if gcd(u,m)=1, otherwise m/gcd(u,m). Their LCM yields R=ceil(2^a/q)+2^max(a-b,0)h for all r>=2,a>=0,q>=1. Comparison with n proves perfect recovery iff (a=0 and gcd(q,m)=1) or (a>=1 and q=1). Independently computed actual bit rows and Gaussian-eliminated ranks for 570 parameter triples, all matching, without inferring infinity from those tests.

## originality

PASS

Best-knowledge PASS for explicit nilpotent/spectral gcd formula across all specified ring sizes and strides. General Kalman rank criterion is known and not new; potential earlier specialized derivations in inaccessible 2022 full texts remain a material risk.

## value

PASS

Sparse fixed-cell time sampling is an intrinsic observability question. Exact rank and nullity for infinite arithmetic ring families, including a sharp even-ring no-thinning criterion, expose information lost to nilpotent and finite-field power-map aliasing. This is not a routine fixed-size Kalman determinant evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
