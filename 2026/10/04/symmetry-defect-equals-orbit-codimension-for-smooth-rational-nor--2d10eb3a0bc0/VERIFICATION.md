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

The proof has three independently checkable layers. First, for \(E=\bigoplus_i\mathcal O(a_i)\), direct summation of \(H^0(\mathcal O(a_j-a_i))\) agrees with \(k^2+h^1(\operatorname{End}E)\) by Riemann--Roch. Second, Harris's balance degeneration theorem identifies the balanced projective orbit as dense in the scroll locus, turning the stabilizer-dimension excess into orbit codimension. Third, the elementary inequality in the proof gives the global maximum defect and its unique equality case.

`verify_scroll_aut.py` was replayed from the packaged path. It exhaustively checked 2212 positive nondecreasing splitting types for \(2\le k\le6\) and \(k\le d\le22\). For every type it verified the direct \(H^0(\operatorname{End}E)\) formula, the cohomological defect identity, the unique balanced minimum, and the unique least-balanced maximum. It separately checked all 1225 surface pairs with \(1\le a\le b<50\) against the published surface automorphism dimension. The captured output is in `verification_output.txt`.

The finite enumeration is not used to infer the infinite theorem. It is a regression check on formulas whose general proof is given in `RESULT.md`. No claim is made about singular scrolls, finite component groups, or scheme-theoretic orbit-closure multiplicities.
