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

The bundled `verify.py` uses only the Python standard library. It implements the Burnside formula with exact integers and independently enumerates fixed-content words up to all rotations and reversals whenever the total word length is at most \(10\).

Checks performed:

- every pair \((d,k)\) with \(1\le d\le4\), \(1\le k\le4\), and \(dk\le10\);
- the displayed first seven values for \(d=1,2,3\);
- the \(d=1\) specialization \(a_1(k)=(k-1)!/2\) for \(k\ge3\), with the small cases \(a_1(1)=a_1(2)=1\);
- integrality of the Burnside numerator in tested cases.

The exhaustive part is finite verification only; it is not used as a proof for arbitrary \(d,k\). The infinite formula is proved symbolically by Burnside's lemma in `RESULT.md`. A successful replay ends with `VERIFY_OK`.
