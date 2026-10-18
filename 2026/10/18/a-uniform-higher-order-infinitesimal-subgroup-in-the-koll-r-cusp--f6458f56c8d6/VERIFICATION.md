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

# Reproducibility and limits

The proof is self-contained over \(\overline{\mathbb F}_2\) and applies to all integers \(n\ge2\); computation is supplementary only. Run `python3 check_stabilizer.py` with Python 3 and no external packages to obtain the finite-field comparison in `CHECK_OUTPUT.txt`. The enumerated matrices all fix the unique singular point and tangent line, and the script compares every coefficient of the transformed homogeneous defining equation. It performs the tests at \(q\in\{4,8,16\}\) over \(\mathbb F_4\); counts are respectively \(1,3,1\). The linearized coefficient map at each parameter has rank \(5\) on the \(9\) raw matrix entries, with one scalar direction, hence Lie dimension \(3\).

The all-parameter finite geometric-point theorem is proved by symbolic monomial coefficient comparison. The new subgroup scheme construction is an identity over arbitrary characteristic-two coefficient algebras. The connected factor has length \(q^3\), and the normalized cyclic diagonal factor acts on it by explicit conjugation, giving exact subgroup length \(q^3(q+1)\). Neither a finite-field census nor tangent-space dimension alone would establish this group-scheme lower bound. The total scheme length of the full stabilizer and its entire infinitesimal structure are not computed; an independent audit has not been performed.
