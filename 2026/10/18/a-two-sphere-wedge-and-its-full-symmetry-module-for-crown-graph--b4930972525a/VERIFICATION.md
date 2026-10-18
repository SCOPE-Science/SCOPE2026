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
# Reproduction and limits

The mathematical proof is the two-stage good-cover nerve argument in `RESULT.md`. Both covers use actual full simplices, so all nonempty intersections are contractible. Integrality follows from the nerve theorem; the natural homology module follows from the equivariant augmentations of the two Čech double complexes. The representation is not asserted at the equivariant homotopy level.

The standalone `verify.py` builds the induced connected components from scratch, checks the predicted exact face membership for every subset, exhaustively determines maximal faces, reduces simplicial boundaries over the field of two elements, and computes signed reduced Lefschetz numbers from every fixed oriented face. It uses all diagonal permutations and both bipartition exchanges for \(n\le6\), and selected nonidentity symmetries for \(n=7,8\). It also verifies the \(n=3\) boundary case without relying on that case in the theorem.

Reproduce with `python3 verify.py --max-n 8` using only the standard library. The exact captured output is `verification_output.txt`. For dimensions beyond the tested range, the mathematical argument, not finite enumeration, supplies the proof. Integral homology torsion-freeness follows from the explicit wedge type; the finite boundary computation alone only checks mod-two ranks. No independent mathematical audit has been performed.
