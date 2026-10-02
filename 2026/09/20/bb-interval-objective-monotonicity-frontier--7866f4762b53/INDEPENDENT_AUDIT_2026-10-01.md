# Independent audit — Sharp objective-monotonicity frontier for Barzilai–Borwein interval steps

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** For an SPD quadratic, every contemporaneous BB interval step lies in \([1/L,1/\mu]\). The exact objective-gap ratio is the squared \(A\)-operator norm of \(I-\eta A\), hence is at most \((\kappa-1)^2\). The two-dimensional construction \(A=\mathrm{diag}(1,\kappa)\), followed by an exact-line-search warm-up from gradient \((1,\sqrt r)\), was re-derived: the next BB1 and BB2 endpoints both tend to 1 as \(r\downarrow0\), uniformly forcing every selector in the interval to approach the ratio \((\kappa-1)^2\). This proves both sharpness and the exact monotonicity frontier \(\kappa=2\). The committed random tests are corroborative only and are not used as proof.

## Originality

**PASS.** The closest primary literature defines and analyzes the whole BB1--BB2 interval family, but the inspected full text does not state the sharp one-step objective amplification or the condition-number-two universal monotonicity frontier.

### Equivalent formulations

The most plausible alias, the convex-combination spectral-gradient family, was checked directly.

Evidence: Dai--Huang--Liu explicitly identify every step in the BB2--BB1 interval as a member of their family. Their paper proves convergence properties, not the audited sharp one-step objective-gap bound.

### Broader coverage

No broader earlier statement was found that mechanically yields the full claim.

Evidence: Classical BB literature covers convergence and nonmonotone behavior, while monotone variants use additional step rules or globalization. No earlier inspected theorem gives the same selector-uniform sharp amplification after an exact-line-search history.

### Exact database or table

This is a sharp analytic worst-case constant; exact factor/threshold searches are the applicable database check.

Evidence: No earlier exact match was located.

### Claim versus prior implication

The claim is not merely the standard convergence theorem in different notation.

Evidence: The interval inclusion \([\mathrm{BB2},\mathrm{BB1}]\subset[1/L,1/\mu]\) gives the easy upper bound, but sharpness under a realizable BB history and the exact selector-uniform frontier require the explicit two-dimensional construction. The inspected convergence theorems do not imply this one-step worst-case classification.

### Source inspections

- **A family of spectral gradient methods for optimization** — RELATED_NOT_COVERING.
  Identifier: arXiv:1812.02974
  Material read: Full 22-page preprint, including the definition of the interval family, convergence sections, and condition-number experiments.
  Evidence: The paper states that every step in the BB2--BB1 interval belongs to the family and studies convergence; it does not state the sharp objective monotonicity threshold.
- **Two-Point Step Size Gradient Methods** — ACCESS_RISK.
  Identifier: DOI 10.1093/imanum/8.1.141
  Material read: Bibliographic record and accessible descriptions; complete theorem-level text was not available in the inspected interface.
  Evidence: No whole-document noncoverage conclusion is drawn from the partial access.

### Residual risks

- The complete text of the 1988 foundational article and some broad historical BB surveys was not inspected; an equivalent sharp one-step bound could be buried there or in poorly indexed optimization literature.

## Scientific value

**PASS.** The exact selector-uniform monotonicity frontier answers a natural stability question for a widely used nonmonotone step family. The sharp adversarial construction explains precisely when the entire BB interval is safe without line-search globalization.

## Final assessment

The final claim survives unchanged on all three scientific axes. No claim text or slogan change is proposed.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
