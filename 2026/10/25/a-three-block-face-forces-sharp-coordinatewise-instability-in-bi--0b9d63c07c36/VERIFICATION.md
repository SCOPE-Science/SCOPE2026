---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

On the support E_m of three complete m-by-m blocks plus cyclic successor matchings, Y=1/(m+1) on support is bistochastic and strictly interior to the face, and strictly negative off-support multipliers give a real local affine projection cell. Its derivative is the cycle-space orthogonal projector Q=I-D^T(DD^T)^+D. The six explicitly given potential groups solve every Laplacian equation for the special matching dipole, yielding exact row absolute mass Lambda_m=2(3m²+m−1)/((m+1)(m+2)). Taking input signs of that row attains the local amplification, and a common all-ones shift makes both observations strictly positive without changing projections. The full-support derivative has norm 4(1−1/n)²; the positive-coefficient m−4 polynomial proves strict advantage exactly from m=4 in this family, limit 6 vs 4. A fresh exact rational reconstruction for m=2..11 verifies every Kirchhoff equation and row mass, while all-m formula follows symbolic identities.

## originality

PASS

General tangent/Jacobian calculus of Li–Sun–Toh and Birkhoff face-support theory are acknowledged prior work. The symbolic potential solution and precise nonband family coordinatewise amplification, sign-witness, n=12 within-family crossing, and limiting gap are not stated or mechanically tabulated in inspected sources or indexed records. The Birkhoff conditioning literature may contain an unindexed equivalent electrical transfer-current result; that is retained as a risk.

## value

PASS

Entrywise-coordinate perturbation stability of bistochastic least-squares projection is natural and unlike Frobenius nonexpansiveness. A structured sparse face explicitly beats the best interior derivative and yields a nontrivial asymptotic separation 6 versus 4, with a sharp witnessed input pair. This is an informative infinite family lower bound, not claimed to be the global norm or earliest dimension among all faces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
