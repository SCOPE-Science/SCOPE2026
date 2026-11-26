---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The missing positive-rank weight must be at most two, so the four largest signs must all be positive and the two smallest cannot both be negative. Exactly three of 64 independent fair sign vectors reject. Conditional on the entire magnitude vector, K=B_3+⋯+B_6 has E[K]=2 and E[K(K−1)]=3. Thus E[(K−1)(K−2)]=1; its values at K=0,1,2,3,4 are 2,0,0,2,6, establishing the conditional 1/6 bound. Under the proposed upper law (K=1,2,4 with weights 1/3,1/2,1/6), high-bit exchangeability gives the required pair moments, either low bit is fair given the high vector, and the low pair is jointly positive with probability (1/2)P(K=2)=1/4. The law therefore attains 1/6. Under the stated lower law the same two K moments hold and K never reaches 4, while the low bits are independent of the highs and each other. Mixtures preserve these pair laws. For any two fixed observation labels, conditioning on all magnitudes gives independent fair signs at their two determined distinct ranks. Integrating against the two independent iid magnitudes gives actual pairwise independence, with a common symmetric atomless marginal. An independent 24-ticket exact computation of the upper law and its complemented zero-size law checked all four outcomes of all 15 sign pairs and the rejection rates; replay /workspace/branches/independent_checks/wilcoxon.py. The packaged script was inspected without execution, and no LP computation is needed. For clarity, the phrase 'stronger than merely demanding pairwise independence of the observations' should be read as 'not implied by bare observation-level pairwise independence': conditional sign fairness/independence alone need not force independence of magnitudes. The Finding and its endpoint realization use the correct scopes.

## originality

PASS

The tight unweighted four-success bound and the moment-LP method are known. The separate contribution is the exact calibration range for this weighted rejection event, including a feasible completion of the extremal high signs by the two low signs and realization by pairwise-independent continuous observations. No examined source covers that combined statement.

## value

PASS

The sample size and tail are motivated by a conventional one-sided exact test near 5%, not by an arbitrary event. The result gives the maximum and minimum true sizes, shows attainable inflation by 32/9, and realizes it even for identically distributed symmetric observations with pairwise independence. It makes the cost of relying on pairwise rather than joint independence concrete while retaining a precisely stated conditional null.

The dated certificate retains the supplied scientific assessment, sources and limitations.
