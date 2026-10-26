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

# Verification and limits

## Mathematical checks

The main proof works for arbitrary prime-power \(q\), every \(n\ge2\), every \(s\ge1\) coprime to \((q^n-1)/(q-1)\), and every valid \(r\). It does not extrapolate from finite enumeration. The essential checks are: \(T\equiv q-1\pmod{q^n-1}\), cyclic factorization \(K^\times=HL^\times\) with overlap \(\mathbb F_q^\times\), exact iterate identity \(F^m(uz)=u^{r^m}\mathcal L^m(z)\), and the power-map fibre size \(\gcd(r^m-1,S)\). The eigenvector counting statement uses the dimension of a kernel of a \(\mathbb F_q\)-linear transformation.

## Computational checks

Execute `python cycle_lift_verify.py` with a Python 3 interpreter. The self-contained checker implements exact arithmetic in \(\mathbb F_{64}\), \(\mathbb F_{256}\), and \(\mathbb F_{729}\), verifies irreducible defining polynomials by trial division, directly enumerates all cycles, and checks every iterate up to twice the largest cycle length. There are seven parameter configurations, including \(r\ne1\), different base-field sizes and nonlinear binomials. Successful execution prints `CERTIFICATE_OK` and `ODD_CERTIFICATE_OK`. The script is part of this same package, with no external data dependency.

## Boundaries

The checks cannot substitute for the proof in arbitrary extensions, and they do not certify all unrelated permutation-polynomial constructions. The cycle formulas concern precisely the stated unit-torus lift family. Previously known general wreath-product cycle algorithms are acknowledged; independent mathematical audit has not occurred.
