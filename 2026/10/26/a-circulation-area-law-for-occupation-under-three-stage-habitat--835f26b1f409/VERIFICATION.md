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

The stationary joint occupied-probability row q obeys q=(qD+pi diag(c))P, so U(P)=pi diag(c)(I-PD)^-1 1, with ||PD||infty<1 since 0<c_i,s_i<1; uniqueness and convergence of the resolvent do not require aperiodicity. The reversed chain has the same positive determinant because D commutes with Pi and det(I-AB)=det(I-BA). Write the stationary edge flow Pi P as symmetric pair flows h_ij plus signed cyclic current J/2. Independently constructed symbolic 3x3 matrices and verified identically, not by parameter sampling, that the adjugate numerator difference is J times c1(d2-d3)+c2(d3-d1)+c3(d1-d2); substituting d=s-c cancels the pure-c area and yields the stated oriented (c,s) area. A positive denominator makes the sign and iff criterion exact. A two-state stationary chain satisfies detailed balance automatically. Rechecked the given rational six-state example P,pi,c,s, with J=1/25, area=7/100, det=6287/20000 and difference=56/6287; source random 50 tests are only supplementary.

## originality

PASS

PASS, qualified: the stationary resolvent and time-reversal transition formula are general Markov-chain prior art. Full primary McVinish–Pollett–Chan models Markovian habitat/dual landscape; full Solow–Smith article uses reversed succession for first-passage histories. Neither inspected full text presents the combined binary occupancy model with the sharp 3-state current-times-oriented-area identity, exact sign-zero classification and minimality. A general Markov-modulated affine-recursion identity might subsume the calculation and remains a residual risk.

## value

PASS

Reversing transition direction while retaining identical long-run habitat stage proportions is a substantive ecological discrimination problem. The exact three-factor decomposition separates circulation, colonization/survival geometry, and positive scale, gives complete equality/sign cases, and proves the minimal number of stages. It is relevant to habitat histories rather than an arbitrary isolated 3x3 determinant calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
