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

`verify.py` is a self-contained Python standard-library verifier for the single claim \(\operatorname{dFl}(P_{31})\simeq\bigvee^{960}S^4\).

It constructs the quadratic-residue orientation on \(\mathbb Z/31\mathbb Z\), checks tournament skewness, outdegree \(15\), and common outdegree \(7\). It enumerates every transitive vertex subset and checks the face vector \((31,465,3255,9765,10695,3255,465)\), totaling \(27931\) nonempty faces. It checks all \(126015\) nonempty Hasse covers.

The fixed repeated-toggle matching is reconstructed from the pivot order in the script. Every matched cover is reversed, every unmatched cover is oriented downward, and a complete topological sort checks acyclicity. The matching has \(13396\) pairs and critical-cell counts \(c_0=1\), \(c_3=89\), \(c_4=1049\).

The script then constructs the signed Morse boundary \(D:C_4^M\to C_3^M\) by exact gradient-path cancellation. It checks rank \(89\) modulo \(2,3,5,7,101,601\). A fixed \(89\)-column minor has exact Bareiss determinant \(-601\). Because \(D\) also has rank \(89\) modulo \(601\), the gcd of its maximal minors is \(1\), hence all \(89\) nonzero Smith factors are units. The kernel is therefore free of rank \(1049-89=960\).

Finally, the homotopy conclusion uses only standard CW facts: after Morse reduction the \(3\)-skeleton is \(\bigvee^{89}S^3\); Hurewicz identifies \(\pi_3\) with \(H_3\); Smith-equivalent attaching matrices are related by homotopy equivalences of wedges of \(3\)-spheres; and the cofiber of \([I_{89}\;0]\) is \(\bigvee^{960}S^4\).

The computation is exhaustive for this finite object. It is not an all-order theorem, and it does not provide independent validation.
