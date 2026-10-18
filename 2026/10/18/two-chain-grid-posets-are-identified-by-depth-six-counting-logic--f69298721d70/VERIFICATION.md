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

# Reproducibility and limits

The argument is the all-size coordinate-and-axis proof in `RESULT.md`. The computations below provide finite cross-checks only.

Run the exact programs in an extracted directory using Python 3 and no third-party modules:

```sh
python grid_refinement_check.py
python square_competitor_check.py
python sharp_boundary_check.py
```

The first program independently recomputes four complete relation-typing/counting refinements and compares them to the predicted automorphism-orbit partitions for 113 finite rectangles, including all dimensions from two through fifteen. The second enumerates all perfect-matching alternatives in the square-grid two-element colour cells of sides two, three and four; for side four its 512 possibilities reduce to 32 transitive ones, all isomorphic to the original grid. The third program explicitly constructs and compares the nontransitive crossed-matching companion for square sides four through eight, checking matching colour multiplicities at every refinement round. `CHECKS.txt` records captured output from actual executions of the included programs.

The tested sizes do not establish any universal statement by exhaustion. Logical identification is claimed among finite partial orders for square grids and among arbitrary finite one-binary-relation structures for nonsquare grids and squares of side at most three; for square side at least four a crossed-matching nontransitive competitor is exhibited. There is no independent audit or external certification.
