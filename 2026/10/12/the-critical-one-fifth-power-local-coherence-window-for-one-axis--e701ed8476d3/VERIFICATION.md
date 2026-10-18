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

Direct conjugation by commuting pairwise zz interactions gives exact mean spin <Jx>=n eta cos^(n-1)(tau)/2 and yz covariance Q, followed by independent single-qubit channel scaling only x,y. The minimum covariance eigenvalue is det(Q)/lambda_+; independent symbolic expansion confirmed H_n(tau): coefficient tau^2=1-n; tau^4=(n-1)(6n-11)/3; tau^6=(n-1)(15n^3-270n^2+945n-934)/90. Under tau=a n^(-3/5), eta=c n^(-1/5), eta^2 H_n -> c^2a^6/6 and lambda_+~c^2a^2n^(2/5), with uniform compact-parameter remainders. Hence limit 1/(c^4a^2)+a^4/(6c^2); unique positive minimum a=(3/c^2)^(1/6), threshold c*=(3^(2/3)/2)^(3/10). No global optimization over arbitrary time sequences or claim at equality finite n.

## originality

PASS

Best-of-knowledge PASS with genuine source-priority risk. Earlier exact OAT moment/noise studies Ji et al. and Zhong et al. treat collective dephasing generators proportional to Jz, whereas tensor-product local phase damping has different coherence decay by number of altered spins. Published collective-noise asymptotics do not imply the stated eta~n^-1/5 local visibility and Wineland-normalized limit. Broad independent-noise metrology literature remains to be exhaustively checked.

## value

PASS

Local post-twist dephasing directly governs scalable metrological gain. The critical visibility/time exponents and closed optimization function locate a nontrivial squeezing/no-squeezing boundary for a mathematically motivated experimental noise family; finite c threshold is not an arbitrary invariant slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
