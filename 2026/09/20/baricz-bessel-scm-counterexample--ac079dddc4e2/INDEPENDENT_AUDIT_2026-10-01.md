# Independent audit — A rational-order counterexample to a Bessel complete-monotonicity problem

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The derivative reduction was reconstructed from the modified-Bessel recurrence. At \(\nu=-15/16\) and \(x=2\), the exact identity becomes \(F''(2)/F(2)=841/256-(39/16)r(2)\), where \(r=I_{1/16}/I_{-15/16}\). Independent rational series bounds reproduce the committed certificate: \(A_4=2131411/82467\), \(B_4=356659/162435\), \(A<A_{\rm upper}=658737071/25482303\), hence \(r(2)>58189629168/42817909615>841/624\) and therefore \(F''(2)/F(2)<0\). This single negative second derivative disproves complete monotonicity at that order; continuity in the order parameter gives an open failure neighborhood. It does not classify the whole interval.

## Originality

**PASS.** Best-of-knowledge originality survives. The exact problem is explicitly posed in the primary 2010 article, and the semantic/archive and primary-literature searches located no earlier counterexample at this order or equivalent negative second-derivative certificate.

### Equivalent formulations

The audited claim is precisely a negative answer to part (b) of the primary open problem, not a title-level similarity.

Evidence: Baricz's Section 2 explicitly asks whether \(x^{\nu+1}e^{-x}I_\nu(x)\) is strictly completely monotone for every \(\nu\in(-1,-1/2]\). No earlier searched source stated a counterexample or an equivalent sign failure for the second derivative at \(\nu=-15/16\).

### Broader coverage

No broader earlier covering theorem was located.

Evidence: Recent Bessel-ratio and complete-monotonicity papers found in the searches concern different ratio families or nonnegative-order regimes. No located theorem covers the entire Baricz part-(b) interval in a way that mechanically implies this rational witness.

### Exact database or table

This is an analytic counterexample rather than a tabulated invariant; exact-record search is the relevant database check.

Evidence: The only exact archive hit was the audited record itself; no earlier table/database entry supplied this sign certificate.

### Claim versus prior implication

The counterexample is not a corollary of the positive monotonicity theorems that motivated the question.

Evidence: The positive-order and neighboring monotonicity results in the primary paper do not imply a negative second derivative in the open interval. The rational tail estimate is a new certificate relative to the inspected prior statements.

### Source inspections

- **Bounds for modified Bessel functions of the first and second kinds** — OPEN_PROBLEM_CONFIRMED.
  Identifier: DOI 10.1017/S0013091508001016
  Material read: Full 25-page article, with detailed inspection of the definitions, Section 2 discussion, and the open problems on printed page 587.
  Evidence: Part (b) asks exactly whether \(x^{\nu+1}e^{-x}I_\nu(x)\) is SCM for every \(\nu\in(-1,-1/2]\).
- **A rational-order counterexample search in later Bessel literature** — NOT_COVERING_IN_MATERIAL_READ.
  Identifier: arXiv:2607.05538 and linked literature
  Material read: Accessible abstract/metadata and search-result scientific summaries.
  Evidence: The located later work treats other Bessel-ratio inequalities and does not expose this part-(b) counterexample.

### Residual risks

- A differently phrased or poorly indexed prior counterexample could exist; the literature search cannot prove first discovery.

## Scientific value

**PASS.** The result gives a rigorous exact counterexample to a long-standing explicitly posed special-function monotonicity question, with a short rational certificate and an open failure neighborhood. It is a motivated boundary result, not an arbitrary parameter check.

## Final assessment

The final claim survives unchanged on all three scientific axes. No claim text or slogan change is proposed.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
