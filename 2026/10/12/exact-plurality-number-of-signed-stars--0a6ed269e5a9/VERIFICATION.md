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

The universal proof uses only the signed-burning definition. On a star, after the centre becomes burned, every still-unburned leaf has exactly one burned neighbour, so its next spread colour is fixed by the sign of its incident edge. This reduces every process to the centre-first and leaf-first cases analyzed in `RESULT.md`.

`verify.py` independently simulates the spread-before-ignition rule rather than using the proof's case formula. For every signing of \(K_{1,m}\) with \(3\le m\le8\), it recursively enumerates every legal ignition vertex and both ignition colours, records every reachable final colouring, computes the plurality number directly, and compares it with the theorem. It checks \(504\) signatures and \(8160\) reachable final colourings. It also takes the direct minimum over all signatures for each exhaustive order and confirms \(\lceil(m+3)/2\rceil\).

The additional arithmetic loop checks the switching-minimum closed form through \(m=500\). This latter loop is not an independent proof; it only stress-tests the algebraic minimization. No computation is used to extend a finite observation to the universal theorem.

The literature verification inspected arXiv:2610.02506v1 at the defining process, plurality parameter, switching/code relation, signed-path section, and conclusion. The source's exact family results are for signed paths, while its conclusion proposes further study of signed-tree classes. No star-family statement was found. Very recent unindexed literature remains the stated originality risk.
