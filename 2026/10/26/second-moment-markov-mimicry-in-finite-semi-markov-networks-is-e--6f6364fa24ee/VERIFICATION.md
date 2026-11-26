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

In the finite irreducible jump chain, the number of jumps to a fixed target has a geometric tail by a uniform positive hitting probability in a finite block. Conditioning on the stopped embedded path, the second moments of its holding times are bounded by the maximum conditional second moment over positive-probability edges; Cauchy–Schwarz bounds the second moment of the sum by that maximum times the squared jump count. The entry-epoch first-step mean recursion is therefore well defined and uses only the row means. The second recursion uses the unconditional second hold moment and the joint first cross-moments with destination, with killed-chain invertibility for each target. In the difference of the semi-Markov and comparator recursions the data agree for target t exactly when d_i+2 c_i h^t=0 for departures i!=t. The mean equation extends to the target row with correction -(pi mu)/pi_t by stationarity. For Z=(I-P+1 pi)^(-1), c_i 1=0 gives c_i h^t=c_i Z mu-[(pi mu)/pi_t](c_i Z)_t. Having every t except i makes (c_i Z)_t/pi_t constant A on those targets; the zero row sum makes c_i Z=A(pi-e_i), hence c_i=A(P_i-e_i). Its i-th coordinate vanishes because both joint cross-moments on the forbidden self-loop vanish. Since P_ii=0, A=0 and d_i=c_i=0. The converse is the identical right-hand side of the unique killed-chain solution. No division by a zero-probability destination is needed; that cross-moment condition is vacuous. The two lognormals in the witness have the stipulated common mean and distinct variances; their mixture has the desired second moment and is not exponential (its density tends to zero at zero). I also reproduced exact inversion on a sparse chain and a deterministic cycle and checked a separate positive finite-atom witness, using python3 /workspace/review-checks.py (semi_markov section).

## originality

PASS

The forward recursion, equality of means with pseudo-rates, and general forest expansion are prior. In particular Voits’s version 2 calculates exactly the edgewise sufficient cancellation condition; that is a later-dated revision, and in either version it is not the all-target necessity result. The supported original content is elimination of all possible cancellation across the complete hitting-moment table, not the already available moment machinery or the notion of non-Markov mimicry alone.

## value

PASS

The complete passage table neither determines the full holding laws nor hides arbitrary local discrepancies: it exactly recovers the second hold moments and first-order dependence on the destination for the stipulated comparator. The necessity proof and the destination-dependent positive witness separate those two limits, for a natural semi-Markov inverse problem. The result does not extend by itself to arbitrary observation epochs, self-loops, or entire passage distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
