---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is analytic. The critical steps checked are:

1. For a realization with \(N\) nonzero e-values, the base e-BH rule rejects if and only if \(Nc\ge K/\alpha\).
2. Under the complete null, FDR is exactly the probability of that rejection event.
3. For fixed \(p\), validity \(pc\le1\) and monotonicity make \(c=1/p\) the worst valid height.
4. On \(((r-1)\alpha/K,r\alpha/K]\), the integer threshold is exactly \(r\), and the corresponding binomial tail increases with \(p\).
5. For \(r\ge2\), \(\Pr(N\ge r)\le\mathbb E{N\choose r}\le(e\alpha)^r\); the \(r=1\) term is at least \(\alpha-\alpha^2/2\). This proves the one-spike optimizer when \(\alpha<1/(e^2+1/2)\).

The accompanying `verify.py` checks the finite maximization numerically over \(1\le K\le200\) at representative conventional levels and reproduces the reported values. These computations do not certify claims outside the proved domain and are not evidence for novelty.
