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

The bundled `verify.py` constructs clique bouquets directly as graphs with a distinguished central vertex and pairwise disjoint clique blades. It checks every assigned vertex for properness and checks that every color appearing in the open neighborhood appears an odd number of times. This direct definition-level predicate is separate from the formula evaluator.

The formula evaluator computes each signed binomial coefficient expression using exact integers. A separate constructive routine builds odd peripheral color multiplicities for uniform blades and balances a binary incidence matrix row by row, before checking all neighborhoods in the resulting graph.

Results: the full formula matches direct enumeration for \(138\) feasible comparison instances, encompassing \(151{,}311\) center-normalized proper palette assignments. For each of \(570\) uniform pairs \(2\le t\le20\) and \(1\le s\le30\), the program constructs and independently validates a minimum strong-odd coloring, checks the formula is positive at the displayed chromatic number, and checks that it vanishes with one fewer palette color.

The resulting program output is included in `verify_output.txt`:

```text
VERIFY_OK
sizes= (1, 1) palette q=6 count= 120
sizes= (2, 1) palette q=6 count= 360
sizes= (2, 2) palette q=6 count= 720
sizes= (2, 3) palette q=6 count= 720
sizes= (3, 1) palette q=6 count= 720
sizes= (3, 2) palette q=6 count= 720
sizes= (4, 1) palette q=6 count= 720
sizes= (4, 2) palette q=6 count= 0
sizes= (1, 2) palette q=6 count= 360
sizes= (1, 3) palette q=6 count= 720
sizes= (2, 3) palette q=6 count= 720
sizes= (3, 2, 1) palette q=6 count= 4320
sizes= (2, 1, 2) palette q=6 count= 2160
sizes= (2, 2, 2) palette q=6 count= 6240
sizes= (1, 1, 1) palette q=6 count= 390
sizes= (1, 1, 2) palette q=6 count= 960
sizes= (1, 2, 2) palette q=6 count= 2160
sizes= (3, 1, 1) palette q=6 count= 1800
sizes= (2, 3, 1) palette q=6 count= 4320
sizes= (1, 1, 1, 1) palette q=6 count= 1200
sizes= (2, 2, 1, 1) palette q=6 count= 9120
sizes= (3, 2, 1, 1) palette q=6 count= 16560
sizes= (1, 2, 1, 2, 1) palette q=6 count= 32400
independent_direct_palette_comparisons = 138
center_normalized_colorings_directly_checked = 151311
uniform_constructive_pairs = 570
constructed uniform range 2<=t<=20, 1<=s<=30
Every check matched
```

Only finitely many parameter values are computationally checked. The unrestricted polynomial and chromatic identities are established by the symbolic parity-projection and degree-balancing proofs in `RESULT.md`.
