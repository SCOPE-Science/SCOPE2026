---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reassessed the complete corrected RESULT.md in /workspace/repairs/5. Correctness of the original mathematical counts was not the issue. Forth and back are equivalent to requiring that the image of each inclusive descendant cone be the suffix starting at its vertex's image. A leaf must go to top. With two worlds, bottom-root maps choose child maps independently; with three worlds, bottom-root child assignments exclude precisely the all-top assignment, since any child image containing bottom must contain middle. The corrected statement and proof preserve the non-onto scope, recurrences, path counts and star minimum. I separately enumerated every rooted shape through order seven by increasing-parent labellings (every shape has such a labelling), deduplicated via sorted balanced parentheses, and enumerated every vertex function using explicit descendant and value masks. The independent replay is `python3 /workspace/repairs/5/check_cutoffs.py`. It gave shape counts 1,1,2,4,9,20,48 and separate maxima (1,1),(2,2),(3,4),(4,7),(5,11),(7,16),(10,25); it checked the two unique maximizing shapes at orders six and seven. At order five the path can tie, consistent with 'maximizes'. The two-world witness count c goes to 2c−1 as the order goes up by two; bases 7>6 and 9>7 suffice. The three-world count at least triples as the order increases by three; bases 25>22, 40>29 and 65>37 and the strictly positive difference 3p(n)−p(n+3)=n²−4n−1 for p(n)=1+binom(n,2) prove all later cases. These analytic arguments, not execution on larger trees, prove the unbounded witness statements. The frozen checker and its saved output were inspected, not executed. The added finite checker was executed as independent corroboration.

## originality

PASS

For the narrowed extremal finding only. The frozen presentation did not acknowledge that both fixed-tree counting recurrences are immediate specializations of the earlier general subtree recurrence e532142d4dde; that portion is covered and cannot support an originality pass. In the corrected RESULT.md and SLOGAN.txt, fixed-tree formulas are explicitly credited and used only as tools. The sharp path cutoffs with unique first maximizing shapes and the explicit exponential witnesses for both targets at every larger order remain distinct in the inspected evidence. The corrected mathematical statements were rechecked. No historical-priority guarantee follows from the comparison.

## value

PASS

For the corrected scope: finding the first orders where a simple rooted source stops maximizing the same modal invariant identifies an exact and different boundary for each small target, including the first extremal shapes. The witness families show that exceeding the path is not a sporadic table entry and quantify a polynomial-to-exponential separation in all residue classes. This useful extremal information is distinct from evaluating the already-known recursion on any supplied tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
