---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Write T_n as the constant term of (x^-1+1+x)^n. In characteristic five the factor for n=5q+d is (x^-1+1+x)^d times the qth power with x replaced by x^5. The first factor's support [-d,d] contains no nonzero multiple of five, so the digit product follows directly, with weights (1,1,3,2,4). Each block of five contributes one of each unit and an extra copy of the parent residue. This gives E_r(5q)=E_r(q), the complete-block counts including L=0, and the stated partial-block weight. Starting in state 1 with score zero, appending a digit reaches every N<5^L, with no inclusion of the endpoint. An independent prefix scan regenerated the seed vectors at L=2,3,4 and checked all twelve one-step vector identities. Translation equivariance yields +3 per step for the upper vectors from L=2 and -5 per two steps for the lower vectors from L=3, with L=2 checked separately. The parity bases give the stated alpha and beta, and finite paths attain both extrema. The proposed upper witness words follow by first reaching r and then taking the digit-1 loop and final digit 2 (for r=1 the initial factor is already 1). The envelopes give density 1/4 and sharp logarithmic excursions in both directions. The attribution to Deutsch–Sagan Theorem 4.7 is a locator error: that theorem concerns modulus three. The general product is explicitly stated in Rampersad–Shallit Theorem 9; the constant-term proof above independently removes any reliance on the erroneous locator. No mathematical claim needs to change.

## originality

PASS

The supported distinct claim is the residue-dependent exact, attained prefix envelopes at every L>=2. The digit rule, nonvanishing, full-block distribution and general finite-state technique are not themselves credited as new. The nearest inspected single-sequence laws and algorithmic analogues do not already solve the four weighted prefix optimizations.

## value

PASS

Uniform recurrence and complete-block equidistribution do not answer how unbalanced prefixes of the canonical modulo-five trinomial sequence can be. Attained extrema for each residue and each cutoff quantify that loss, expose genuinely asymmetric slopes and parity effects, and give sharp benchmarks beyond asymptotic density. This is a motivated exact distributional invariant, not just an evaluation of the already known digit product at a few lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
