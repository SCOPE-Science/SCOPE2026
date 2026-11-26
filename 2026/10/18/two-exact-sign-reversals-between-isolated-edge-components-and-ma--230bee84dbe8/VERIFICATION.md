---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a fixed isolated edge e, the identical maximal-edge indicator contributes 1 conditional on isolation, incident distinct edges contribute 0, and each disjoint f contributes p q^(n−4) since the isolation removes two possible common neighbors. Thus E[I_n M_n]=E[I_n](1+a_n p q^(n−4)), while E[M_n]=b_n p q^(n−2). For n=3 simplify the sign function to F_3=3p(1−p²), with one maximum and F_3(1/2)=9/8; n=2 is the Bernoulli variance. For n≥4, F_n is positive only below p_0=sqrt(1−sqrt(a_n/b_n)). On this interval write x=p², q=1−x. The log derivative in x is 1/(2x)−(n−4)/q−2b_n q/(b_n q²−a_n); its derivative is strictly negative since the derivative of the last quotient before its minus sign is 2b_n(b_n q²+a_n)/(b_n q²−a_n)². The log derivative runs from +∞ to −∞. The witness F_4(1/4)=547/512 and the n≥5 lower bound (15/16)(2−4/n)≥9/8 prove exactly two crossings and signs +,−,+. At p=c/n, F_n→2c; its lower crossing is identified by bracketing about c=1/2 below the witness scale 1/n. For p=t/√n, F_n/√n→t(2−t²)e^(−t²); for each 0<t<√2 this gives a lower bound on the upper crossing, and √n p_0→√2 gives the matching upper bound. The positive prefactor divided by n tends at p=c/n to (c/2)e^(−2c), proving the normalized limit. Read the verification metadata and script without executing it. Their finite run is reported, not independently reproduced; the graph moment calculations are exact, while an extra boundary diagnostic uses floating point. Use Python 3.10+ for int.bit_count rather than the Python 3.9 minimum stated in VERIFICATION.md.

## originality

PASS

The marginal formula for triangle-free edges is known; even the exact mixed moment can be recovered from a general connected-motif identity by edge-rooted book inclusion–exclusion. The distinct contribution supported here is the exact all-order two-crossing classification for this mixed statistic and the separated critical scales (with the sparse covariance profile). Neither the fixed-motif sign theorem nor the one-crossing all-edge specialization gives that classification.

## value

PASS

Pointwise containment of isolated edges among maximal edges does not predict covariance sign. A sharp two-crossing theorem valid even at n=3, together with the separation between n⁻¹ and n⁻¹ᐟ² root scales, explains a nontrivial dependence effect missed by taking all edges or only considering the sparse regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
