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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. The program constructs \(\mathbf F_4=\mathbf F_2[\omega]/(\omega^2+\omega+1)\) by an explicit four-element multiplication table; constructs all \(21\) normalized rational points of \(\mathbf P^2(\mathbf F_4)\); identifies the sole zero \([0:0:1]\) of \(Q=X^2+XY+\omega Y^2\); and calculates the \(20\times30\) binary trace-evaluation matrix on degree-four homogeneous forms. Its columns are indexed by the ordered quartic monomials \(X^iY^jZ^{4-i-j}\), with \(i=0,\ldots,4\), \(j=0,\ldots,4-i\), and by coefficient basis \((1,\omega)\) in that order.

The following \(19\) zero-based column indices are checked to be independent:

`1,0,2,8,3,5,4,9,10,13,12,16,11,14,15,17,6,7,29`.

Their 20-bit column vectors in the fixed point order, written in five-digit hexadecimal, are:

`a6aa6,6c66c,eeee0,ffff0,e00e0,66a60,aaca0,f00f0,00ee0,0cc60,066a0,00ff0,0eeee,06c60,0a6a0,0fff0,6c660,a6aa0,0ffff`.

All \(30\) columns have even parity, giving an independent upper bound of \(19\) on the rank. An additional row-wise elimination confirms rank \(19\). Each basis quadratic is also checked to map to zero under trace after applying \(H\mapsto H^2+QH\). The argument that this image is the entire kernel uses the exact binary dimensions \(12-1=11\) and \(30-19=11\), and the polynomial-domain identity \(H(H+Q)=0\) only for \(H=0\) or \(H=Q\).

The program does not enumerate all geometrically integral del Pezzo surfaces, prove the quoted geometric classification, or verify that cited propositions exhaust the previous cases. Those are explicitly identified literature inputs. There is no independent audit or machine-checked formal proof. The implication from kernel equality to geometric factorization is written algebraically in `RESULT.md` and does not depend on a finite experiment.
