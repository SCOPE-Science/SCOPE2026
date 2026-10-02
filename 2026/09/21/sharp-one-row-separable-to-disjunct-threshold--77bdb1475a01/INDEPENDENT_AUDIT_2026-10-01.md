# Independent mathematical audit — SCOPE-20260921-77bdb1475a01

Final disposition: **PASS**.

## Correctness
**PASS** — The proof was reconstructed independently. Exact \(s\)-separability with more than \(s\) columns implies exact \(t\)-separability for every \(t<s\) by enlarging any colliding \(t\)-sets without changing their Boolean unions. In the explicit \(M_d\) family, the private rows reduce equality of two \((2d-1)\)-column unions to equality of the two omitted-column pairs, and the special rows separate every such pair. The two distinct covering obstructions force contradictory values for any single added row, whereas singleton rows for the two central columns make the matrix \(d\)-disjunct. Combining this lower construction with the Chen-Hwang theorem that a \(2d\)-separable matrix becomes \(d\)-disjunct after at most one added row gives \(G(s)=\lfloor s/2\rfloor\). The package verifier was inspected and an independent finite replay for \(d=2,\ldots,6\) reproduced exact separability and failure of every one-row augmentation; the general proof does not depend on that finite replay.

## Originality
**PASS** — Chen and Hwang's primary three-page article was inspected and supplies the sharp upper implication used here, but it does not state a universal row-augmentation frontier or the two-obstruction witness proving optimality at every order. Searches used the equivalent union-free/cover-free terminology as well as separable/disjunct terminology, and current published-database search found no earlier statement of \(G(s)=\lfloor s/2\rfloor\). The lower construction is therefore original to the best of current knowledge, with residual risk from older superimposed-code/set-system literature.

### Equivalent formulations
The searches covered both matrix and set-system aliases; the new content is the exact universal frontier and sharp lower witness.

### Broader coverage
The earlier upper theorem is essential but does not imply the matching lower bound.

### Exact database or table
This is supporting evidence only; the originality conclusion also relies on statement-level comparison with the primary upper-bound theorem.

### Claim versus prior implication
The final equality requires genuinely additional lower-bound structure.

## Value
**PASS** — The theorem closes a natural quantitative gap left by the Chen-Hwang conversion theorem: it identifies the exact largest disjunctness order universally obtainable with one extra test row, for every separability order, and supplies an explicit sharp obstruction. This is a motivated structural threshold in nonadaptive group testing rather than a parameter renaming.

## Source inspections
- **Exploring the missing link among d-separable, d-bar-separable and d-disjunct matrices** (https://doi.org/10.1016/j.dam.2006.10.009): complete primary article text, including definitions and the theorem that a 2d-separable matrix can be made d-disjunct by adding at most one row Method: primary full-text inspection. Assessment: PRIOR_UPPER_BOUND_ONLY. Evidence: The article supplies the upper conversion but no sharp all-order augmentation frontier or matching obstruction.
- **Assigned verification program** (repository artifact `artifacts/verify.py`): complete source; its finite claims were independently replayed for d from 2 through 6 Method: repository artifact inspection and independent replay. Assessment: SUPPLEMENTARY_CHECK_REPRODUCED. Evidence: The replay confirmed exact separability and that no one-row augmentation makes the tested witnesses d-disjunct.

## Residual risks
- Older union-free/cover-free or superimposed-code literature may phrase the same augmentation frontier differently.
- The finite artifact does not prove the infinite theorem; correctness rests on the analytic construction and Chen-Hwang theorem.
