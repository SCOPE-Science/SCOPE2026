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

# Reproducibility and mathematical limits

Execute `python3 four_cube_dominance_verify.py` with Python 3.10 or later; no external dependencies, network services or specialized algebra packages are required. The exact stdout is embedded in `four_cube_dominance_verification.txt`.

The executable checks all \(65536\) subsets with two independent face predicates, verifies \(45706\) nonempty faces, \(22847\) disjoint Morse pairs and every one of the \(329552\) oriented Hasse cover incidences, and topologically sorts the complete directed Morse graph to certify acyclicity. Only one critical vertex, ten critical seven-simplices and one critical nine-simplex survive, which proves the full integral homology via the cellular theorem. The separate mod-two simplicial boundary computation checks ranks in every dimension and does not substitute for the integral proof.

The symmetry certificate constructs an integral nine-cycle with \(448\) signed simplices, verifies its boundary vanishes exactly, and evaluates the induced integral homology coordinate for all \(384\) graph automorphisms, independently of the Lefschetz enumeration of the seventh-degree character. Character averaging checks the rational quotient homology. The cited suspension theorem and Alexander duality are separately required for the five-cube conclusion; no finite calculation on \(Q_4\) alone is presented as a proof of a higher-dimensional uniform formula.

These are deterministic, finite, exhaustive mathematical checks under the stated combinatorial definitions. They do not constitute external or independent validation. Homology does not by itself determine the full (possibly unstable) homotopy type.
