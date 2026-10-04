# Same-model review

## Correctness
**PASS.** The expansion of Liu’s middle term was reconstructed directly and checked against the definitions. The identities
\[
\frac{(k+2)s}{2}(M_k-2s)=E+(k-1)D
\]
and
\[
(k+2)s(T-M_k)=kE+2(1-k)D
\]
are exact. Liu’s Lemma 2.2 supplies \(D\ge0\) and its equality case, while Erdős–Mordell supplies \(E\ge0\). The isosceles-coordinate calculation, half-angle parameterization, derivative, unique critical point, and continuity passage from the side midpoint to interior counterexamples were independently recomputed. The packaged checker tests the same identities and boundary behavior but is supplemental to the analytic proof.

## Originality
**PASS.** The primary 2016 paper was inspected at Conjecture 6.3 and Lemma 2.2. Claim-specific searches covered the exact parameter interval, the defect-ratio language, endpoint decimals, and the eliminating quartic. Tran’s 2021 arXiv full text was inspected as a later weighted-family comparison. Accessible material for Liu 2018, Liu 2019, and Tran 2026 was also compared. None of the inspected statements implies the exact scalar reduction plus the displayed algebraic boundary obstruction. Residual risk remains because the full text of two closely related later papers was not accessible in this check.

## Value
**PASS.** The finding addresses the numerical parameter window of a published open conjecture. It gives a structural reduction from a two-sided weighted inequality to one scalar ratio and proves a nearly matching exact outer obstruction: Liu’s proposed \([0.48,1.36]\) can be extended, if at all, by at most about \(0.015565\) on the lower side and \(0.005714\) on the upper side before this natural family produces counterexamples. This is a motivated boundary result, not an arbitrary numerical slice.

## Closest literature and limitations
The closest source is Liu 2016, DOI 10.1186/s13660-015-0947-2, which states Conjecture 6.3 and the inequality underlying \(D\ge0\). Tran 2021, arXiv:2105.07885, develops a different weighted Erdős–Mordell family. Liu 2018 (DOI 10.1007/s00454-017-9917-4) and Tran 2026 (DOI 10.1080/0025570X.2026.2653460) remain access-related overlap risks. The result proves necessity outside an exact outer interval, not sufficiency inside it.

Same-model review: passed. Independent audit: not yet performed.
