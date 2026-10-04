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

Run `python3 artifacts/verify.py`. A successful replay prints `VERIFY_OK`.

The script performs exact integer/rational arithmetic and checks:

- all 18 source points lie on the archived degree-\(8\) form;
- all 28 partial derivatives of total order below \(7\) vanish at \(P_0=[3:5:1]\);
- the resulting \(46\times45\) interpolation matrix has a nonzero kernel vector and rank \(44\) modulo \(1000003\), \(1000033\), \(10007\), and \(65537\);
- the 18 point-evaluation rows have rank \(18\), so \(\dim I(Z)_8=27\);
- after translation to \((u,v)=(0,0)\), the curve has only degree-\(7\) and degree-\(8\) terms, so the multiplicity at \(P_0\) is exactly \(7\);
- the degree-\(8\) piece equals the displayed product, while the degree-\(7\) piece has the displayed coefficients;
- the exact rational gcd of \(A_7(u,1)\) and \(B_8(u,1)\) is constant, and \(A_7(1,0)\neq0\), excluding a common homogeneous factor.

The script verifies the explicit witness and the finite algebra used in the proof. It does not computationally enumerate the exceptional assigned-point locus. The generic step is theoretical: the source gives generic one-dimensionality, rank \(44\) persists near the witness, and the reducible locus in the projective space of octics is Zariski closed.
