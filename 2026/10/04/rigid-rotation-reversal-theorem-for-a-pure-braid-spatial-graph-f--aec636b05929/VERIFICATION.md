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

The all-word argument was reconstructed from the actual public constructor, not from the figure alone. The frozen source defines \(A=(1,1)\), \(B=(2,2)\), advances the braid body one unit in \(x\) per Artin generator, and uses symmetric left/right host geometry and closure margins.

For one generator step, substituting \(u=1-t\) into the published coordinate formulas gives
\[
2|w|-(k+t)=(2|w|-1-k)+u,
\]
\[
\frac12-\frac12\cos(\pi(1-u))=1-\left(\frac12-\frac12\cos(\pi u)\right),
\]
and
\[
\sin(\pi(1-u))=\sin(\pi u).
\]
Together with \(z\mapsto-z\), this is exactly the reversed positive crossing with exchanged lane occupants. Since each source block consists of two identical generators, the reverse expanded braid is the expansion of the reversed block word.

The same half-turn swaps the left and right boundary vertices and their coupling/spacer edges. The three external closures have symmetric margins and are taken to themselves with reversed parametrization. Therefore the whole pre-normalization embedded graph is mapped to the reversed-word graph by a rigid orientation-preserving rotation.

The bundled standalone checker replays the source braid-body coordinate rules for all binary words through length \(10\) and prints:

`VERIFY_OK words=2047 max_length=10 max_coordinate_error=1.776e-15`

The finite released dataset was independently compared at the cited frozen commit: \(324\) rows, \(293\) directed comparisons for which the reversed row is present, zero raw-polynomial-hash mismatches and zero normalized-polynomial-hash mismatches. The source itself also records the finite condition `all_raw_reversals_match=true`.

Finite checks are not used to prove the infinite theorem. No claim is made that different reversal orbits are pairwise non-isotopic.

The independent-audit channel has not been performed.
