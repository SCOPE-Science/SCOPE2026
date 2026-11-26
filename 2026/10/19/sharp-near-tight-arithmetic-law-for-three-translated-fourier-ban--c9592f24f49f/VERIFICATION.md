---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fourier synthesis on one interval and columnwise unitary multiplication reduce the three indexed cosets to the stated three-row phase matrix. The optimal squared norm bounds are the extreme eigenvalues, not their square roots; a collision of cosets is a rank loss in the prescribed three-coset basis problem. An independent way to check the Taylor matrix is to shift the column powers to −1,0,1 by a row phase: its Gram entries become 1+2 cos of the angle differences. At angles 0, 2π/3+d/n, 4π/3+a/n, the first-order off-diagonals, divided by √3/n, are −d,a,d−a. Exchange of the first two rows/columns sends a to d−a and convexity of spectral diameter gives the midpoint minimum. At the midpoint the antisymmetric vector yields eigenvalue d and the other eigenvalues are d(−1±√3)/2. The candidate gives a=d/2 with |d|=2π/3 in both residues. Conversely, actual minimizers exist away from rank loss; trace 9 and the candidate bound force all entries of G−3I to be O(1/n). Simple roots of 1+z+z² and the bound on the row-pair difference force distinct equilateral orientations, conjugate to the one above. After picking that orientation, cluster points of d belong to 2π(Z+(2−r)/3) in residue r, all with |d|≥2π/3; a is bounded. The spectral-diameter lower bound thus applies to every potentially minimizing subsequence, and division by the limiting lower eigenvalue 3 gives the claimed constant. The exact tightness criterion follows from the same roots; the bundled NumPy checker was inspected as finite corroboration, not run or relied on for the infinite limit.

## originality

PASS

Only the optimized non-tight first-order rate is credited. Existing sources give the fiber mechanism, exact tightness or different optimizations; most notably a later matched-family determinant result does not provide this norm-condition-ratio optimum.

## value

PASS

The first-order constant measures the unavoidable conditioning loss in natural translated-band bases when exact root-of-unity conditioning is forbidden. Both the attainable explicit construction and the matching all-shifts lower bound go beyond generic stability bounds. This is an exact asymptotic benchmark for the specified three equally spaced cosets, not a claim about unrestricted bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
