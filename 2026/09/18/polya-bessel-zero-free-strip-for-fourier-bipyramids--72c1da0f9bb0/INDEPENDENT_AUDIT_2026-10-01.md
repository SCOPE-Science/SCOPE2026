# Independent audit — 2026-10-01

## Final claim

A Pólya–Bessel zero-free strip for Fourier bipyramids

## Correctness — PASS

Writing \(q_s(x)=(1-x)^\ell B_\ell(s(1-x))\), two Bessel identities give \(q_s''\) proportional to \(H_\nu(s(1-x))\). By definition of the first positive zero \(r_d\), this is nonnegative on the whole support for \(0\le s\le r_d\), with the needed endpoint conditions \(q_s(1)=q_s'(1)=0\). Thus \(w_s=-q_s'\) is nonnegative and decreasing; pairing positive and negative half-waves makes its sine transform strictly positive, hence the cosine transform \(F_{d-1}(u,s)\) is positive for every real \(u\). The scaling to \(\kappa\) and the equal-volume ball is algebraically correct. Independently recomputing the dimension-three constants gives \(r_3=1.255783711794597\ldots\), \(j_{3/2,1}=4.493409457909064\ldots\), and \(A_3=91.6248852570044\ldots<100\), consistent with the exact rational certification in the proof.

## Originality — PASS

The motivating primary paper proves only existence of some positive strip width \(\sigma_d\), explicitly says its constants could be made quantitative but are not recorded, and leaves rigorous certification of a prescribed pair such as \((100,3)\) to future work by two-variable interval bounds. The audited Bessel-root strip is a different explicit one-dimensional criterion and is not mechanically implied by the source's qualitative compactness argument. The classical Pólya convex-kernel positivity principle is prior art, but its application via the displayed Bessel second derivative to this bipyramid kernel was not found elsewhere.

### Equivalent formulations

Searches/sources: Gómez-Serrano Levitin Platt Polterovich Fourier bipyramid zero-free strip; Pólya cosine transform convex kernel Bessel bipyramid.

Evidence: The source defines the same \(F_{d-1}(u,s)\) and proves existence of a strip.

Reasoning: The same object is used, but the source gives an unspecified \(\sigma_d\), whereas the audited statement identifies a concrete Bessel-root strip \([0,r_d]\).

### Broader coverage

Searches/sources: arXiv:2609.10517 Theorem 2.3 Remark 2.4 Remark 2.5.

Evidence: Theorem 2.3 proves existence; Remark 2.4 says explicit constants can in principle be extracted but are not recorded; Remark 2.5 leaves fixed-pair rigorous certification to future work.

Reasoning: The broader source theorem does not imply the claimed particular width without the new convexity/Bessel argument.

### Exact database or table

Searches/sources: published SCOPE index: Fourier bipyramid Bessel zero-free strip; alpha 100 d 3 Fourier bipyramid rigorous certification.

Evidence: No earlier exact Bessel-root threshold or exact fixed-pair certificate was located.

Reasoning: No exact table/database coverage was found; residual near-simultaneous work remains possible because the source preprint is recent.

### Claim versus prior implication

Searches/sources: Tuck 2006 positivity of Fourier transforms; DLMF Bessel derivative recurrences.

Evidence: Classical positivity and Bessel identities provide ingredients.

Reasoning: Those ingredients do not mechanically identify that this specific bipyramid slice remains convex exactly up to the stated first zero; the derivative computation and its application are the claim-specific step.

## Scientific value — PASS

The result turns a qualitative existence argument in a current Fourier-zero problem into an explicit all-dimensional threshold and gives a fully analytic certificate for the concrete \((100,3)\) example specifically highlighted as nonrigorous in the source paper. This is a motivated quantitative strengthening with a reusable one-dimensional certificate.

## Sources inspected

- **Javier Gómez-Serrano, Michael Levitin, Daniel Platt, Iosif Polterovich, An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies** (https://arxiv.org/abs/2609.10517): QUALITATIVE_PRECURSOR_NOT_EXACT_COVERAGE. It proves existence of a zero-free strip, does not record an explicit strip constant, and leaves rigorous fixed-pair certification to future work.
- **E. O. Tuck, On Positivity of Fourier Transforms** (https://doi.org/10.1017/S0004972700047511): GENERAL_INGREDIENT. The general cosine-transform criterion does not state the bipyramid Bessel-root threshold.

## Residual risks and limitations

- The threshold is sufficient and is not claimed to locate the actual nearest Fourier zero or the optimal elongation.
- The motivating preprint is very recent, so unindexed parallel work remains a residual originality risk.

## Disposition

**passed**
