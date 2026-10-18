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

# Reproducibility and verification

Use Python 3.10 or later, without third-party packages, in the directory containing the two checker programs:

```sh
python3 check_wheel.py
python3 check_persistence.py
```

The first program exhaustively enumerates induced-forest simplices and computes full mod-two boundary ranks for rim lengths \(8\) through \(12\), all forest degree thresholds from \(2\) through the stabilization threshold. It also enumerates rotations and reflections to check their signed edge traces. Its reference output is `verification_output.txt`.

The second program performs an independent filtered boundary-matrix reduction at rim lengths \(8\), \(9\), and \(10\), checking all nonzero-length bars against the asserted formula. Its reference output is `verification_persistence_output.txt`.

These are finite computational checks, not proof for arbitrary rim length, and mod-two agreement alone does not exclude odd integral torsion. The uniform proof of integral torsion-freeness uses the known torsion-free homology of the full cycle-independence complex, exact skeletal chain identities, and the fact that top-chain kernels of free abelian groups are free. The proof of rational quotient homology uses the finite-group invariant comparison and the integral homology character.

No external mathematical audit has been performed. No numerical experiments outside the enumerated rim-length ranges are asserted.
