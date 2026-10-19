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

# Exact verification of the Pappus edge-colouring hexagon-switch classification

The graph is defined by \(y=mx+b\) over \(\mathbb F_3\), with edges ordered by \((x,y,m)\). All three colours are distinguished. A certificate contains the lexicographically ordered complete list of \(120\) edge-colouring vectors (\(27\) entries each) and the sorted list of \(216\) unordered hexagon-switch adjacency pairs, indexed from zero.

Run `python3 verify_factorizations.py --certificate reconstructed.json` to independently reconstruct a certificate by choosing each perfect matching, decomposing its complementary two-factor and assigning alternating colours. Inspect the final `VERIFY_OK` and the printed summary; compare `reconstructed.json` with `pappus_hexagon_certificate.json` by exact bytes or parsed fields (either is acceptable, as the generated serialization is canonical). Then run `python3 verify_local_constraints.py pappus_hexagon_certificate.json`. This second program enumerates edge colours by per-point permutations with line constraints and independently constructs all geometric six-cycles and all legal switch pairs. It checks the delivered canonical certificate entrywise and reports `VERIFY_OK`.

The saved stdout files `factorizations_output.txt` and `local_constraints_output.txt` record successful complete runs. Both implementations verify the same state-list SHA-256 (`10ee644ca090da4cd61ad4bbfdd7ca3ea362d6afb6db030117be487a1a636244`) and hexagon-adjacency-list SHA-256 (`645d32d0e16319c8b1bd07b5fdf92233b2891d99b61fb94c9d20134e4b868e48`) using compact JSON array serialization. Separate traversals confirm exactly two size-\(60\) components, sign partition, degree pattern, and complete \(T(K_{3,3})\) recognition. The first implementation also computes the free global colour-name permutation quotient, checks its previously established \(2(K_1\vee(3K_3))\) form, and verifies that every lifted vertex has exactly one neighbour over each neighbouring quotient vertex, proving a six-sheeted graph covering. Exact breadth-first search from every state gives radius and diameter \(6\) in the restricted graph, and the first program compares all-length edge-Kempe switches with radius and diameter \(4\).

The sign-preservation step is proved directly from an even number of local transpositions. Computation supplies the complete remaining finite exhaustive classification, including sufficiency of the sign invariant. The programs are finite, deterministic, use only the Python standard library, have no external data dependency, and assert that all search ranges are exhausted by their enumerators. This is a finite exact check, not an extrapolation to any infinite graph family. Independent external scientific audit has not been performed.
