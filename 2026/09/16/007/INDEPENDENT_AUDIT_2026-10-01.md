# Independent audit — 2026-10-01

## Finding

**Disposition: passed.** The final claim was reassessed on correctness, originality, and scientific value.

## Correctness — PASS

For every nonzero one-qubit vector v, homogeneous D=1 PEPS include |v>^n, so a universal nonzero postselection must satisfy C|v>^m!=0. Homogeneous D=2 PEPS include |v1>^n+|v2>^n. When v1,v2 are independent and n-m>=1, their complement powers are independent, so the filtered cat is product across the cut exactly when C|v1>^m and C|v2>^m are collinear. Universal success therefore forces rank(C|Sym^m(C^2))<=1. Rank zero kills every product; rank one gives a nonzero homogeneous binary form of positive degree, which has a projective zero over C and hence kills some product state. Thus no fixed A- and n-independent patch operator can satisfy the demand.

## Originality — PASS

The cited PEPS paper is background on injectivity and phases, and targeted literature/published-record searches found no theorem with this fixed-filter product/cat obstruction.

### Equivalent formulations

Standard PEPS injectivity/filtering literature uses tensor-dependent hypotheses and does not state this A-independent, size-independent no-go.

### Broader coverage

The elementary product/cat argument remains a separate implication not found in the broader PEPS references searched.

### Exact database or table

Database/table coverage is inapplicable because the theorem is symbolic and uniform in patch size; the search nevertheless checked for an exact published-record match.

### Claim versus prior implication

The claimed no-go follows from a new elementary implication using product states and two-branch cat states.

### Sources inspected

- Twisted Injectivity in PEPS and the Classification of Quantum Phases — https://arxiv.org/abs/1307.7763: BACKGROUND_NOT_COVERING. No universal fixed-patch filtering impossibility is stated.

## Scientific value — PASS

The result eliminates an entire universal cut-and-glue strategy for homogeneous bond-dimension-two PEPS at every nonempty patch size, while sharply identifying the assumptions under which the obstruction applies.

## Limitations and residual risks

The theorem concerns one fixed nonzero linear patch operator independent of the PEPS tensor and system size. Tensor-dependent, size-dependent, approximate, adaptive, and multi-Kraus procedures are outside its scope.
