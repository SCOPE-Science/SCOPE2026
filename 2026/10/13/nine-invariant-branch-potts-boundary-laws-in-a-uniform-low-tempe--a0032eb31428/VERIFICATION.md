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

The proof has four exact components:

1. The substitution \(t=e^{h/k}\) converts \(h=kf_\theta(h)\) into \(F_{k,\theta}(t)=0\).
2. Descartes' rule gives at most three positive roots of \(F_{k,\theta}\); the signs at \(0\), \(2/\theta\), \(1\), \(\theta/2\), and \(\theta\) give exactly three for \(k\ge4\), \(\theta>24\).
3. For each such root, \(x=e^{l/(k-1)}\) and \(x=t^{1/(k-1)}y\) convert the second equation into \(H_t(y)=0\). Descartes' rule again gives at most three positive roots, and the sign brackets in `RESULT.md` give three in each of the cases \(t<1\), \(t=1\), and \(t>1\).
4. Exponentiation is bijective on the real fields, so the resulting nine positive-root pairs are exactly the nine real boundary-law pairs on this branch.

`verify.py` numerically replays the root brackets and substitutes representative reconstructed pairs into the original equations for several orders and parameters. This replay is not used to infer the universal theorem; it is only a consistency check on the algebra and implementation.

The theorem does not assert that \(\theta=24\) is sharp and does not classify solutions outside the stated invariant branch. No independent audit has been performed.
