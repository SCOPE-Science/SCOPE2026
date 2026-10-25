---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The total variation is max over 2^{n−1} sign-word linear scores. For z=e^theta>1, comparison of endpoint and sign-transition contributions proves alternating signs uniquely maximize the exponential score for odd n or with both signs for even n. Their cumulant log mgfs are the exact displayed Z_n formula, strictly convex with support maximum 2. Relative-entropy variational equality gives the unique corresponding tilted probability comb(s). Competing sign words have a strict mgf gap at theta_t, hence exponentially negligible tails by Chernoff. For winning scores, maximal lattice spans are 3 and offset −N for n=3, and span 1 offset −2N for n>=4; exponential change of measure plus the lattice local CLT gives h exp(−theta delta)/[(1−e^{−h theta})sqrt(2π Nv)] and the even/odd multiplicity K_n. Endpoint D=2N is exactly the interior path independent-support condition. Independently enumerated all sign words for n=3..11 at rational z=2 and recovered claimed maximizing patterns. Assumption: n,t fixed as N grows.

## originality

PASS

The Banić–Elezović studies explicitly analyze expectation (2026) and a dynamic-programming Comb Test exact null distribution. Those are directly relevant to the same statistic, but an exact finite-N DP table or first moment does not alone yield the explicit fixed-n LD rate, all alternating entropy minimizers and lattice-prefactor formula. The full Comb Test paper remained unavailable (Oxford vpn_disconnected); this is a significant, explicitly bounded originality risk, not an automatic failure. Resultary searches retrieved mainly other multinomial modes and no claim with the same sharp tail and parity structure.

## value

PASS

Gives a calibrated small-p tail law for a natural ordered-histogram discrepancy used in uniformity testing, including the exact exponential rate, √N prefactor, arithmetic oscillation and rare-event profile(s). These quantities have clear mathematical and statistical uses beyond moment formulas and simulated critical values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
