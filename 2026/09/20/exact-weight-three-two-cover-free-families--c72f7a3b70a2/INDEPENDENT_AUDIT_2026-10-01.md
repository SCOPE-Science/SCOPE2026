---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For 3-uniform 2-cover-free families, the exact maximum is \(1,2,3\) for \(v=3,4,5\) and equals \(D(v,3,2)\) for every \(v\ge6\); every maximum family is linear for \(v\ge7\), with a sharp non-linear optimum at six points.

## Correctness — PASS

A repeated pair forces all third vertices in its blocks to have degree one, yielding the deletion recurrence. Linear triple families are precisely partial Steiner triple packings and are automatically 2-cover-free. Combining the recurrence with the exact classical \(D(v,3,2)\) formulas proves all orders and strict extremal linearity from seven. The finite MILP artifact was inspected only as corroboration.

**Checked sources.** assigned RESULT.md; artifacts/verify_small.py; Erdos--Frankl--Furedi 1982 context; Li--van Rees--Wei 2006 abstract; Yu--Wang--Ji 2025 public article

**Residual risks.** 

## Originality — PASS

The foundational source gives the classical upper-bound/asymptotic framework and Steiner equality cases. Recent sparse-disjunct work gives an asymptotically optimal limited-column-weight bound, not the exact weight-three capacity; the 2006 paper's abstract concerns constructions and unrestricted optimal small-point CFFs.

### Equivalent formulations

Aliases through disjunct matrices and packings were included.

### Broader coverage

Neither inspected source implies the exact all-order weight-three theorem.

### Exact database or table

The database value is only one side of the comparison.

### Claim versus prior implication

The repeated-pair deletion lemma closes the gap and proves extremal structure; this is not mechanically implied.

**Checked sources.** https://doi.org/10.1016/0097-3165(82)90004-8; https://doi.org/10.1002/jcd.20109; https://doi.org/10.1002/jcd.21986; Resultary assigned-record hit

**Residual risks.** The complete 1982 and 2006 bodies were not independently read in this run.

## Value — PASS

This is a natural exact constant-column-weight group-testing capacity and an extremal-structure classification, not a finite table recomputation.

**Checked sources.** EFF foundational problem; classical triple-packing values; recent sparse-disjunct literature

**Residual risks.** 

## Limitations

- Specific to block size three and two covering blocks.
- Older superimposed-code terminology remains a residual search risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
