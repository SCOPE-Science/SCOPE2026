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

# Finite verification and limitations

`python3 verify_morse.py` independently enumerates every candidate subset of sixteen arcs, records the face vector and checks a deterministic acyclic matching. Its signed integral gradient-path recursion confirms every entry of the Morse differential. The complete directed Hasse diagram is topologically sorted rather than sampled.

`python3 verify_character.py` separately constructs the complex, verifies mod-two boundary ranks, reduces the top boundary over a field of characteristic 101, and evaluates all eight signed automorphisms. The integral rank bound supplied by the Morse proof and the trace bound \(8\) allow unique recovery of the rational characters. This is exact modular evidence together with a mathematically justified lift, not an approximate character computation.

The checkers are self-contained Python 3 files. The two output files are actual recorded results of execution, not proofs on their own. The mathematical implications from the Morse model to the homotopy wedge and from chain traces to homology characters are established in RESULT.md. No larger wheel sizes, integral equivariant splitting, or independent external validation are asserted.
