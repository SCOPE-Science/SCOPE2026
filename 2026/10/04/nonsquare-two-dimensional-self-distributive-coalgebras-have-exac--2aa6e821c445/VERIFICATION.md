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

The proof is finite after scalar extension. For a nonsquare \(a\), adjoining \(s\) with \(s^2=a\) produces two group-like elements \(g_+=x+s y\) and \(g_-=x-s y\). Every compatible product on the split coalgebra sends each ordered pair of group-like basis elements to \(0\), \(g_+\), or \(g_-\). The script checks all \(3^4=81\) tables and recovers exactly \(21\) self-distributive ones.

The nontrivial quadratic Galois automorphism swaps \(g_+\) and \(g_-\). The script conjugates each of the \(21\) tables by this swap and finds exactly \(5\) fixed tables. Exactly \(3\) fixed tables have no zero output and therefore satisfy multiplicative counit compatibility. Symbolic basis conversion verifies the four displayed nonzero ground-field formulas and the zero table.

As an independent finite check, the script enumerates every bilinear map \(C_2\otimes C_2\to C_2\) over \(\mathbb F_3\), where \(2\) is nonsquare, and tests both comultiplication compatibility and generalized self-distributivity on basis triples. It finds exactly \(5\) maps.

The finite-field enumeration does not prove the arbitrary-field theorem by itself. The general proof is the faithful scalar-extension and Galois-descent argument given in `RESULT.md`.
