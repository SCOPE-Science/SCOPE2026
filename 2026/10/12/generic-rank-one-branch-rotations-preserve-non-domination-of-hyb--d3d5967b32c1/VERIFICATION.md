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

The classification is analytic. The channel operator system contains every branch coordinate projector
\[
|e_{j+1}\rangle\langle e_{j+1}|,
\]
so a quantum code of dimension at least two must annihilate all branch coordinates and hence lie in the protected qubit sector. The cross operators are
\[
E_0^*E_j=\langle f_1,\phi_j\rangle |e_1\rangle\langle e_{j+1}|,
\]
which force every scalar block coexisting with that qubit to be supported on the zero-overlap branch coordinates. This yields at most \(z\) such scalar blocks, and the coordinate lines attain the bound.

The purely classical code of size \(m+1\) is realized by the input lines \(e_0,e_2,\ldots,e_{m+1}\), whose output supports are \(f_0,\phi_1,\ldots,\phi_m\). Output dimension rules out a larger exact classical code. The two maximal candidates are comparable exactly when \(m+1\le z+2\), and since \(z\le m-1\), this occurs exactly at \(z=m-1\).

The attached checker `artifacts/verify.py` independently constructs representative Kraus families, confirms trace preservation and the zero-overlap count, and checks the relevant cross-operator coefficients. It returns `VERIFY_OK` using only the Python standard library. These finite examples corroborate but do not replace the all-\(m\) proof.

Unproved limits: no approximate-error threshold, tensor-power classification, entanglement-assisted version, or higher-rank-branch analogue is asserted.
