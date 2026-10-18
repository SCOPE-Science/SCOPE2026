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

# Verification details

The proof checks the derivative numerator by direct differentiation and its reciprocal-quadratic discriminant by expansion. The nonzero critical-point count follows from the degree-three disk covering and a boundary angular derivative given by positive Poisson terms. Each root of the reciprocal equation is taken on the unique disk branch; the critical points of every higher cyclic lift then follow from the chain rule.

At the positive double-root locus the two parameter derivatives are \(F_{wc}=-8c_0(1-r^2)t^2/D_0^2\) and \(F_{www}=6(1-r^2)/D_0^2\). The first-order critical-point branch displacement has square \(k^2=8c_0t^2/3\). Their exact Taylor combination produces the asserted \(3/2\)-order critical-value separation with a positive coefficient. The negative locus is reflected by the elementary sign symmetry.

To reproduce symbolic and numerical corroboration, run `python checker.py` with Python 3 and SymPy installed. The program checks all displayed critical algebraic identities, chain-rule examples and several numerical splitting limits from both sides at three radii. It completed without failures in the package review. These finite probes are not used as an infinite proof.

**Limits:** No endpoint \(c=\pm1\) classification, no uniform cusp remainder for \(r\to0\) or \(r\to1\), no dynamical classification, and no independent mathematical audit. Publication-priority evidence is limited to identified and inspected literature.
