---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. After reversing incidence arrows, an acyclic matching is a directed rooted forest with outdegree ≤1, and the universal hub supplies Kozlov's complete-source shellability hypothesis, giving pure dimension k-1 and concentrated reduced integral homology. For each dihedral g the quotient on vertex orbits admits an outgoing orbit-arrow precisely when the target is fixed by g^ell and lies in a different orbit; any cycle of quotient orbit-arrows lifts to a directed cycle because lengths are nonincreasing and constant round cycles. The signed augmented fixed-simplex trace is -det(I-L_g) by the directed rooted-forest determinant. Since homology is in degree k-1, χ_k(g)=(-1)^k det(I-L_g). For identity the wheel Laplacian spectrum has eigenvalues 0,k+1,3−2cos(2πj/k), j=1,...,k-1, yielding k³. Nontrivial rotations and both even-rim reflection classes leave a quotient zero-sum block, hence trace 0; odd reflections reduce to a tridiagonal Dirichlet path determinant with sign (-1)^((k-1)/2). Rational character comparison gives the regular/permutation twisted splittings. Independently implemented an orbit multigraph with exact SymPy determinants and verified EVERY 2k group element for k=5,...,12; these are auxiliary finite checks, not the uniform determinant proof.

## originality

PASS

PASS on inspected literature. Kozlov/Jojić establish complete-source shellability but no orbit-specific wheel character; an unadorned graph Laplacian or forest-count theorem provides rank but not signed reflection traces. A public four-rim wheel homotopy computation (outside k>=5) does not dominate the full equivariant claim. Both parity classes of reflections and natural dihedral action are substantive additional information, though an unindexed representation calculation cannot be ruled out because Resultary failed.

## value

PASS

PASS. Determines the full D_k-character of the top reduced homology of a canonical graph Morse complex for every wheel with k>=5, distinguishing exceptional odd-reflection traces. This equivariant invariant is motivated by the natural geometric dihedral group and not recoverable from the known shellability/wedge count. The integral wedge count is attributed to prior structural ideas, while the character and representation decomposition are the new nontrivial content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
