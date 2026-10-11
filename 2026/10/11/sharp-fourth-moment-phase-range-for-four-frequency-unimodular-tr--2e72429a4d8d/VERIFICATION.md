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

The proof is symbolic and applies to every four-point integer support. The critical checks are:

1. Parseval for \(P^2\) identifies \(\|P\|_4^4\) with the squared \(\ell^2\)-norm of the ordered pair-sum coefficients.
2. For four distinct integers, unordered pair-sum collisions are only diagonal/off-diagonal three-term progressions or the single disjoint-pair equality associated with central symmetry; no fiber contains two distinct collision mechanisms.
3. The support relation types are exactly \((0,0),(1,0),(2,0),(0,1),(2,1)\), with \((2,1)\) precisely the four-term arithmetic progressions.
4. On a four-term progression the phase expression is \(28+4\cos\alpha+4\cos\beta+8\cos(\alpha+\beta)\). Writing \(u=(\alpha+\beta)/2\), \(v=(\alpha-\beta)/2\), and \(t=|\cos u|\), the minimum reduces to \(28+4(4t^2-2t-2)\), giving \(19\) at \(t=1/4\); the maximum is \(44\).

`verify.py` checks these formulas against direct pair-sum collision sums on every four-point subset of \(\{0,1,\ldots,18\}\), with deterministic phase samples and explicit extremizers. These computations corroborate the symbolic argument; they are not an exhaustive proof over all integer supports.
