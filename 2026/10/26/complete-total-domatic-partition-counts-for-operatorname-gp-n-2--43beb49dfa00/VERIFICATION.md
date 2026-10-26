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
# Reproducibility and scope

From the extracted files run `python3 verify_gp2.py`; the checker requires only Python 3's standard library. It creates a 256-state transfer digraph, verifies 576 transitions, computes all traces of powers 1 through 256 using integer path counts, uses the exact Newton recurrence to build every coefficient of \(\det(I-zT)\), and checks its equality to the five fully listed polynomial factors. It directly enumerates all named two-colorings for \(5\le n\le9\) and verifies all 729 possible initial 3-color recurrence sextuples across a 30-term period.

Actual console results were:

```
DETERMINANT_OK degree=64 states=256 transitions=576 checked_Newton_orders=1..256
TRACES_OK A_5..A_14=12,116,226,1286,2486,5172,13202,23232,48128,121844
DIRECT_BRUTE_OK n=5..9 counts=12,116,226,1286,2486
THREE_COLOUR_OK 729 initial assignments, six globally admissible 30-periodic sequences
ALL_CHECKS_PASSED
```

The correctness proof uses a finite matrix identity valid in all lengths; initial counts alone are not an infinite proof. The 729-case search is exhaustive only after the proved recurrence and divisibility by \(t^{30}-1\) reduce *every* admissible three-coloring to a 30-periodic sequence. All integer path calculations and polynomial products are exact, with no randomization, numerical tolerances, or external certificate dependence. An independent audit has not been performed.
