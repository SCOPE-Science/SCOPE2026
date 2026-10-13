# Scientific review — sharp ten-coordinate quadratic norm rigidity

## Correctness — PASS
The eight displayed norm identities are all exact. Their coefficient matrix has rank \(8\), certified by the integer minor \(-608\), and its two-dimensional kernel is precisely the span of constants and squares. The recurrence from the exact identity \((n+8)^2+4(n+3)^2=n^2+4(n+5)^2\) propagates the conclusion from the ten initial entries to all positive integers; hence the global \(G/F\) characterization is proved without extrapolating finite enumeration. For finite truncations the checker groups **all** representations and computes their ranks over the rationals: rank \(6\) at \(N=9\) and rank \(8\) at \(N=10\). Thus the lower side of sharpness is proved, not merely observed.

## Originality — PASS, with residual risk
The decisive asserted advance is the **minimality** of finite collision radius \(10\), including a nonquadratic radius-\(9\) assignment. Kátai and Phong (2014) provide a general affine-plus-periodic sumset criterion whose key difference-set hypothesis fails for the present weighted-square support. You et al. (2016, arXiv:1606.05039v1, Section 5) derive several **overlapping norm identities** for the already-solved nonlinear equation; in particular, some computations use index \(11\), but they do not show sharp radius \(10\) for arbitrary linked complex data or give the rank-\(6\) obstruction at radius \(9\). Khanh (2017, Lemmas 1-2) obtains a quadratic-plus-periodic necessary form for the auxiliary general linear relation and solves the nonlinear equation, not this minimum finite-collision problem. The specific published theorem and nearby indexed findings searched did not cover the threshold. Unindexed earlier derivations and overlooked overlap remain risks. The previously established nonlinear classification is not presented as new.

## Value — PASS
The exact test radius gives a natural completeness threshold for norm-collision constraints in a classical additive functional-equation setting and proves why all smaller nontrivial truncations are insufficient. At the threshold, eight explicit identities force the entire infinite connected problem through a recurrence. This is a structural minimum with a meaningful obstruction, rather than an arbitrary finite slice or raw search result.

## Scientific limits and reproducibility
No claim is made for independent summands, different norm coefficients, unrepresented outer-function arguments, or priority over the nonlinear equation. Exact arithmetic checks are reproducible using `python3 verify.py`. Its finite calculation does not replace the induction in the proof.

Self-review: passed. Independent audit: not yet performed.
