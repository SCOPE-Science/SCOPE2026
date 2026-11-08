---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For each n>=2, K>1, alpha threshold, the 2n precommitted short/long inputs share n-1 unit goods and target-specific special goods. At alpha<=1/K a deterministic initial distinct prefix and final allocation attains all inputs. At alpha>1/K every successful short input requires an injective prefix; with unique empty recipient b, a=b admits both horizons, and each a!=b admits at most one. Optimal deterministic response to arbitrary prior q therefore equals max_b(q_bS+q_bL+sum_(a!=b) max(q_aS,q_aL)). Writing r_a=q_aS+q_aL and d_a=|q_aS-q_aL| gives F=(1+D+max_b(r_b-d_b))/2>= (n+1)/(2n), with equality uniquely at uniform q. Uniform b and a coin in the mismatch give exact pointwise equalizer; deterministic minmax zero at high alpha. Independent rational finite-game enumeration for n=2,3 and nonuniform priors matched.

## originality

PASS

The 2n hard-instance family is identical to Chen–Long Section 4.2, but their published upper bound for unrestricted online input sequences is different from proving attainable minimax on only this subfamily with unique dual solution. The uniform-prior upper bound alone neither proves a restricted-family saddle point nor forces uniqueness across arbitrary input priors; the threshold at alpha=1/K is another separate statement. The claim is a limited, credited refinement of the same model. Best-of-knowledge priority risk remains explicit; unsuccessful search alone is not claimed as proof of novelty.

## value

PASS

Closes the finite hard-instance game underlying a published online-EF1 impossibility bound: the exact restricted minimax value, threshold and unique adversarial distribution are actionable strategic invariants. It does not claim the unrestricted online problem is solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
