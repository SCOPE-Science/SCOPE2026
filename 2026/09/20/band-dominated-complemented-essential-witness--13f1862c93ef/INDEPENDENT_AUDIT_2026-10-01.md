# Independent mathematical audit — SCOPE-20260920-13f1862c93ef

Audited at: 2026-10-01T18:05:11.787582Z

Disposition: **passed**

## Correctness — PASS

Finite-dimensional input fibers make every finite-coordinate truncation finite rank, so every tail restriction of a finite-propagation approximant has norm at least its essential norm. Recursive separation in a locally finite metric space produces disjoint input blocks whose finite-propagation images have disjoint supports. The blockwise norming-functionals define an explicit norm-one projection onto their \(\ell_p\) or \(c_0\) span. Norm approximation transfers the lower bound to band-dominated operators, while compact and strictly singular perturbations cannot remain bounded below on the witness. This yields the exact compact/FSS/SS distances. Finite-coordinate projections approximate compact maps in norm on the codomain, giving the approximation-number limit; \(b_n\le a_n\) and the infinite witness give the Bernstein limit.

### Correctness sources

- assigned RESULT.md
- Hagger-Lindner-Seidel arXiv:1504.00540
- Roch 2022 DOI:10.1080/17476933.2021.1913134

### Correctness risks

- Finite-dimensional fibers and local finiteness are essential to the proof; \(\ell_\infty\)-sums are excluded.

## Originality — PASS

Full inspection of Hagger-Lindner-Seidel confirms sharp essential-norm/limit-operator localization, but it does not state the audited complemented disjoint-block witness or strict-singularity/Bernstein consequences. Roch's 2022 article studies closed ideals in the Hilbert-space band-dominated algebra; its accessible abstract does not cover the classical strictly singular/FSS distances. Resultary returned the assigned record as the exact match and several narrower later same-day s-number results, not an earlier general theorem.

### Equivalent formulations

No equivalent complemented-witness formulation was located.

### Broader coverage

Those frameworks do not, in the material inspected, imply equality of distances to compact, FSS and SS ideals or the Bernstein-number asymptotic via a complemented block witness.

### Exact database or table

This is an operator-theoretic structural theorem, so table coverage is inapplicable beyond semantic theorem indexing.

### Claim versus prior implication

The final claim is not a formal corollary of the inspected prior statements.

### Sources inspected

- Essential pseudospectra and essential norms of band-dominated operators — https://arxiv.org/abs/1504.00540. NOT_COVERING: The paper identifies essential norms with limit-operator norms; no complemented disjoint-block witness or SS/FSS/Bernstein theorem was found in the inspected full text.
- Ideals of band-dominated operators — https://doi.org/10.1080/17476933.2021.1913134. PLAUSIBLE_BUT_NOT_DECISIVE: The accessible scope concerns central-rank ideals and slowly oscillating quotient centers, not strict singularity or Bernstein numbers.

### Checked sources

- https://arxiv.org/abs/1504.00540
- https://doi.org/10.1080/17476933.2021.1913134
- Resultary semantic search

### Residual risks

- The 2004 Rabinovich-Roch-Silbermann monograph and full Roch 2022 article were not exhaustively inspected theorem by theorem; an older equivalent formulation remains a bounded best-of-knowledge risk.

## Value — PASS

The theorem converts essential noncompactness into a sharp, explicitly complemented classical sequence-space witness and thereby collapses three operator-ideal distances while identifying the asymptotic Bernstein scale. It works over arbitrary locally finite metric spaces with nonuniform finite-dimensional fibers, making it a substantive structural result.

### Value sources

- Hagger-Lindner-Seidel arXiv:1504.00540
- Roch 2022

### Value risks

- The theorem does not cover infinite-dimensional fibers or \(\ell_\infty\)-sums.

## Limitations

- Finite-dimensional coordinate fibers and local finiteness are required.
- Domain and codomain use the same outer \(\ell_p\) exponent or both \(c_0\).
- The 2004 monograph and full Roch 2022 paper were not exhaustively inspected theorem by theorem.
