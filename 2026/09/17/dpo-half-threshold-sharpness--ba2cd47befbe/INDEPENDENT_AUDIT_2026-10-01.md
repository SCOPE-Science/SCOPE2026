# Independent scientific audit — The one-half threshold is sharp for discrete-potential AVE certification

Audit date: 2026-10-01 (UTC) UTC.

Disposition: **PASSED**.

## Correctness

**PASS** — The displayed 2-by-2 family was reconstructed algebraically. For epsilon in (0,1/2), both induced 1-norm and rho(|inverse of A|) equal 1/2+epsilon<1; the (+,+) candidate is positive and is the unique AVE solution, while exact rational differences show (+,-) strictly exceeds all three other DPO potentials. Its second candidate coordinate is positive, so the sign is wrong, and the mismatch flip has strictly negative potential increment. The epsilon=1/20 exact-arithmetic artifact was independently replayed, reproducing the four potentials and the gap 40/1197. The scalar minimality and block-diagonal embedding arguments are valid.

## Originality

**PASS** — The source DPO paper proves the sub-one-half global-maximizer theorem and the diagonal-scaling spectral-radius extension, but the inspected theorem-level material does not give an above-threshold counterexample or sharpness family. Resultary semantic search returned this record as the only direct sharpness match; no equivalent or stronger prior implication was located. Originality therefore passes to the best of knowledge, with the usual residual risk from very recent AVE follow-up work.

### Equivalent formulations

The searched aliases included global-maximizer failure, sign-flip descent, norm threshold and spectral-radius scaling.

Searches: Resultary: DPO half threshold sharpness AVE global maximizer wrong unique 1/2; Chen--Xia arXiv:2609.12763v2.

Evidence: No equivalent counterexample family or alternate formulation was located outside the audited record.

### Broader coverage

Those broader results motivate the gap but do not imply existence of the explicit wrong DPO maximizer above one half.

Searches: Chen--Xia arXiv:2609.12763v2; AVE uniqueness rho(|inverse of A|)<1 literature.

Evidence: Chen--Xia establishes the sufficient sub-one-half DPO regime; standard AVE well-posedness extends to the larger rho<1 regime.

### Exact database or table

Database/table coverage is genuinely inapplicable beyond checking indexed mathematical records because the claim is a symbolic family theorem.

Searches: Resultary semantic search for exact family and threshold.

Evidence: No finite database or table determines this analytic threshold claim.

### Claim versus prior implication

Neither inspected source implies the displayed DPO landscape counterexample; the record supplies new sharpness evidence for the DPO objective itself.

Searches: Chen--Xia theorem statements; Radons sharp one-half signed-elimination context.

Evidence: The source theorem is one-sided (<1/2); earlier one-half sharpness results concern a different sign-selection property.

### Source inspections

- **Discrete Potential Optimization for Absolute Value Equations: A Sign-Flip Framework with Polynomial Complexity** (https://arxiv.org/abs/2609.12763v2): Assessment: sets the sufficient threshold but does not state the audited above-threshold counterexample family. Material read: abstract and theorem-level statements describing the global-maximizer result under ||inverse of A||_1<1/2 and the rho(|inverse of A|)<1/2 diagonal-scaling extension. Evidence: The abstract explicitly identifies 1/2 as the sufficient DPO norm threshold and gives the spectral-radius scaling extension.

Checked sources: https://arxiv.org/abs/2609.12763v2; Resultary semantic search for DPO sharpness aliases; record artifacts/verify_eps_1_20.py and artifacts/verified_output.txt.

Residual risks: The DPO paper is extremely recent, so an unindexed follow-up could contain an equivalent sharpness construction.

## Scientific value

**PASS** — This is a natural sharpness theorem for a newly introduced universal certification threshold. The counterexample is parameter-uniform, dimension-minimal, robust, rationally approximable, and simultaneously addresses the norm and scaling formulations; it identifies a meaningful boundary rather than an arbitrary finite instance.

## Final claim

For every c in (1/2,1), a two-dimensional uniquely solvable absolute-value equation can have norm and absolute-inverse spectral radius both equal to c while the DPO potential has a unique global maximizer with one wrong sign; correcting that sign decreases the potential. Dimension two is minimal, the construction is robust, embeds in every higher dimension, and cannot be moved below the source threshold by positive diagonal scaling.

This audit is a scientific assessment of the claim and supplied evidence. It is not peer review, formal verification, or a guarantee of first discovery.
