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

Run:

`python3 verify_odd_rough_veronese.py`

The packaged replay returns `VERIFY_OK`.

It checks the following items from the proof:

- for odd \(k=2r+1\), every weighted-degree monomial \(x^p y^q a^j\) projects to a lattice point satisfying \(q+2j\le k\), and the four proposed vertices occur;
- the four adjacent fan determinants are \(\pm1\);
- the exceptional-ray relation \((-1,-2)+(1,0)=2(0,-1)\) holds;
- the base-point combinatorics force every odd weighted-degree monomial to contain \(x\) or \(y\), while \(x^k\) and \(y^k\) exclude any other common zero;
- the normalized area equals \((k^2-1)/2\).

The script runs these formula checks for many odd values of \(k\). This finite replay is not used to infer the infinite theorem. The proof of the arbitrary-\(r\) statement is the symbolic lattice and fan argument in `RESULT.md`.

The remaining general inputs are standard toric facts: the normal fan of the weighted projective plane \(\mathbb P(1,1,2)\), the self-intersection rule from the primitive neighbor relation, and very ampleness of an ample divisor on a smooth complete toric surface. No independent audit has been performed.
