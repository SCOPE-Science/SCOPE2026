---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For C2, averaging over the whole group gives O=(P+Q)/2; summing subgroup averages adds the trivial subgroup term P to give F=(3P+Q)/2. The displayed edge lists make (0 1) a nonidentity automorphism and its orbit quotient has a loop contributed by edge (0,1) in both examples. Duplicate quotient edges impose duplicate constraints and can be collapsed. A set partition into k color classes, t of which contain an edge or loop, contributes (x-y) falling t times (x-t) falling (k-t): assign distinct unrestricted colors to the t classes, then assign the other classes distinct unused colors. An independent sparse integer polynomial calculation gives P_A-P_B=-2T and Q_A-Q_B=6T, so F agrees and O_A-O_B=2T, with value 64 at (3,1). Independent vertex augmentation, with canonicalization over permutations ordered by degree, generated 2,4,11,34,156,1044 unlabeled graphs on 2 through 7 vertices. Deleting a vertex from any graph and relabeling the remainder to its representative proves completeness of this extension generator. All 5,823 nonidentity involutory automorphisms were tested, with 2,680 distinct 3P+Q keys and no equal keys with distinct P+Q. The generator includes disconnected graphs; orders zero and one admit no faithful action. Thus the result does not rest on the frozen graph-atlas dependency or finite evaluation of polynomials. Replay: python3 /workspace/branches/6b857cbc-b2a5-4f64-bfe7-0f11a5fc53bf/independent_exact_check.py; full output independent_exact_check_full.txt in the same directory. The frozen script was inspected but not executed.

## originality

PASS

The primary paper explicitly asks this implication. Its published counterexample is in the reverse direction. The verified C2 example resolves the forward implication in the negative and the lower-order search establishes the first possible order in the specified class. This does not claim priority for the invariant, its definitions or the graph-class enumeration.

## value

PASS

A concrete nonzero difference at equal multiorbital invariant answers an explicitly posed implication question. The exact cutoff shows how early the failure occurs in the simplest nontrivial acting group and gives a small regression example with all smaller actions excluded. This is useful beyond recomputing known atlas counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
