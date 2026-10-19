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

The explicit finite-dimensional Lyapunov kernel provides the analytical certificate: substitute all blocks into \(Q-K^\dagger QK=I\), grouped into equal positions, separation two, and larger even separations. A left-boundary eigenvector argument proves strict contraction in spectral radius and legitimizes the infinite survival sum.

To replay the exact symbolic checks, use Python 3 with the declared SymPy dependency and execute `python check_kernel.py` in the directory containing that file. The checker expands each of the generic symbolic polynomial equalities and performs 27 additional exact finite-strip boundary checks. Its finite set of tested strip lengths is illustrative, not the proof of the statement for every length.

The initial-state mean formula follows from the onsite \(2\times2\) block of the certified operator. The comparison with earlier literature may be incomplete; no independent validation was performed.
