# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The construction reduces MSARP on a nested codimension-one family to an exact Markov chain for the single omitted coordinate. The conditional transition law follows from the projection-DPP conditioning identity and the determinant formula for a principal minor of \(I-ee^T\). The oblique error is exactly \(1/e_j^2\) after normalization by the best rank residual. The hierarchical-angle limit makes each new stage multiply the conditional expectation by \(k_r+1\) uniformly. For the actual CSSP error, the selected-column orthogonal residual is computed independently from \(A^{-T}\), yielding \([\sigma^2(1-e_j^2)+e_j^2]^{-1}\); choosing \(\sigma\) below the smallest final normal component transfers the same limit to the orthogonal projector.

The standalone verification script checks the exact two-stage formula, several multi-stage limits, one-shot comparison, and a direct QR projection calculation. The direct and closed-form projection factors agree to floating-point accuracy in the supplied test.

Adversarial checks performed on the mathematics include: verifying that every cumulative stage subspace is nested; checking that the first-stage DPP has support only on the intended simplex block; confirming that all final selected column sets are full rank for positive parameters; distinguishing the oblique theorem error from the smaller orthogonal CSSP error; and verifying that \(V\) is an exact leading right-singular basis of the constructed matrix rather than merely an arbitrary auxiliary subspace.

## Originality

**PASS, to the best of our knowledge.** The motivating preprint arXiv:2609.20556 was inspected through its full HTML text. Its Theorem 3.3 gives the two-stage factor \((1+k)(1+p)\), and the paper states the multi-stage product \(\prod_i(1+k_i)\), including the singleton value \(2^t\). The paper separately proves tightness of its conditional Theorem 3.1 for a *prescribed initial set* (Theorem 3.2), but no sharpness construction for the full randomized MSARP product factor was found.

The original ARP paper arXiv:2412.13992 was checked for the one-shot guarantee and its relation to projection DPP/volume sampling. Classical volume-sampling work already establishes the sharp \(d+1\) scale for one-shot CSSP, so neither that constant nor projection-DPP sampling is claimed as new. The JMLR paper *A determinantal point process for column subset selection* was checked at the article/abstract level for DPP-based CSSP context. Searches using “multi-stage adaptive randomized pivoting”, “conditional DPP”, “conditional volume sampling”, “staged volume sampling”, “sharp bound”, and equivalent column-subset terminology did not locate a prior theorem establishing the product-factor lower bound.

The main residual originality risk is the broader volume-sampling and experimental-design literature: conditional or sequential determinant identities are classical, and an older result could imply parts of the hole-process calculation without using MSARP terminology. The 2006 volume-sampling paper and the 2020 DPP-CSSP paper were not checked line by line in full text. This does not affect correctness; it limits the strength of the originality claim to the source-specific MSARP sharpness theorem stated in RESULT.md. The motivating preprint is also very recent, so contemporaneous revisions or follow-up notes remain possible.

## Value

**PASS.** The result resolves whether the new product guarantee can be substantially improved under its present assumptions. It cannot: even exact dominant-subspace information and optimal projection onto the selected columns do not remove the multiplicative stage penalty. The construction also separates worst-case theory from the paper's favorable experiments and identifies the mechanism as rare, increasingly ill-conditioned omissions created by incremental conditioning. The singleton specialization shows that the stated exponential factor is a real worst-case effect rather than merely a loose induction.

## Limitations

The family is worst-case and nearly rank deficient. It uses a permitted ordering inside a degenerate dominant singular subspace and does not show that such behavior is typical. No lower bound is claimed for spectral-norm CSSP, Nyström approximation, high-probability error, or implementations that modify the incremental rule through oversampling, reordering, or regularization.
