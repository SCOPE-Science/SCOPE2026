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

# Computational and deductive verification

Run `python3 verify_free2.py` using Python 3 with only standard-library modules. The script generates each reduced-row-echelon subspace of the ambient space for \((r,q)=(1,2),(1,3),(2,2),(2,3)\), uses the explicit ordered-word product to check closure, and separately tests left and right multiplication by each standard basis element to determine ideal status. It compares every dimension coefficient and every projected-dimension count against both formulas.

The ambient subspace enumerations contain respectively \(5\), \(6\), \(2825\) and \(56632\) subspaces. At \((r,q)=(2,2)\), the exact subalgebra dimension profile is \((1,15,59,99,43,3,1)\), giving \(221\) subalgebras and \(77\) ideals; at \((r,q)=(2,3)\), the profile is \((1,40,238,508,157,4,1)\), giving \(949\) subalgebras and \(229\) ideals. The script also evaluates the Gaussian formulas for several larger parameters, including nonprime prime powers as integers in the combinatorial formulas only.

These finite checks do not establish the identities for arbitrary \(r\) or \(q\). Their proof requires the graph classification, the tensor-subspace dimension and the uniform Gaussian estimates given in `RESULT.md`. The code performs exhaustive arithmetic only over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\); it does not implement the field \(\mathbb F_4\), and evaluating the closed formula at \(q=4\) is not an exhaustive algebra enumeration over that field. No independent external audit has been performed.
