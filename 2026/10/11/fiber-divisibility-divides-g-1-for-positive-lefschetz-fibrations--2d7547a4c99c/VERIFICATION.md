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

The proof is symbolic and has no computational certificate. The checked chain is:

1. In the free lattice \(H_2(X;\mathbb Z)/\operatorname{Tor}\), write the non-torsion fiber class as \(F=mA\) with \(A\) primitive.
2. Since \(F^2=0\), integrality gives \(A^2=0\).
3. The adapted almost-complex structure satisfies \(\langle c_1,F\rangle=2-2g\).
4. The standard identities \(c_1\bmod2=w_2\) and \(\langle w_2,A\rangle\equiv A^2\pmod2\) give \(\langle c_1,A\rangle\in2\mathbb Z\).
5. Therefore \(2-2g=m\langle c_1,A\rangle\) implies \(m\mid(g-1)\).
6. Corollary 8 of arXiv:2610.01776v1 says that positive multisection degrees \(d\ge2\) are exactly multiples of \(m\), yielding the stated low-genus and \(g-1\)-section consequences.

The source text was checked directly for items 1, 3, and 6 and for the statement of its open 2-section question. Items 2, 4, and 5 are standard integral intersection-form and characteristic-class deductions. Torsion is excluded from the lattice calculation, and no finite enumeration is used.
