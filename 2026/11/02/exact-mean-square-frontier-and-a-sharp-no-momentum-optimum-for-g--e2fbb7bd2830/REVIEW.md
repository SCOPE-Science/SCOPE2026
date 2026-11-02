# Scientific review: Gaussian momentum mean-square frontier

## Correctness — PASS
Gaussian second and fourth moments give the exact transfer matrix for E||x_k||², E<x_k,x_{k-1}>, and E||x_{k-1}||². The PSD Gram determinant recurrence equals omega² times the old determinant plus (d+1)alpha² times the squared first moment, yielding a primitive positive map for omega>0 and exact Perron growth. The characteristic polynomial satisfies P(1)=alpha[2(1-omega²)-alpha(d(1+omega)+2)] and det(M)=omega³, giving the iff stability frontier. An explicit completed-square identity at r=(d+1)/(d+2) gives P(r)<0 except the stated unique optimizer. Symbolic reproduction and 60 finite rational spectral cases independently passed; they are not a substitute for the general proof.

## Originality — PASS (qualified)
The original 2022 paper defines mBGK and provides sufficient convergence estimates. Kidambi et al (2018) already establish qualitative heavy-ball failure on a different two-coordinate stochastic problem, using a related moment-transfer technique; this known phenomenon is not claimed as new. The assessed contribution is the dimension-uniform exact Gaussian spectral frontier and unique global mean-square optimizer. Actual semantic searches, synonyms, and implication comparisons against these and published mathematical claims did not reveal a covering theorem. An equivalent treatment in stochastic recurrence literature remains possible; independent priority review has not occurred.

The most relevant sources are Han and Xie, arXiv:2208.05437 (especially Section 5.6), Kidambi et al., arXiv:1803.05591 (Section 3 and Appendix A), and Bollapragada et al., arXiv:2206.07553. The general possibility of stochastic-heavy-ball nonacceleration is old; the exact rank-one Gaussian frontier and equality classification are the claimed new portion. Best-knowledge searching cannot establish global priority.

## Value — PASS
The exact region exposes an increasingly restrictive stability penalty from fixed momentum and cleanly separates fast convergence of the mean iterate from the true mean-square error. The sharp optimum and uniqueness answer a meaningful tuning question for the original rank-one Gaussian numerical method and give a reproducible benchmark in every dimension, not an arbitrary finite computation. The theorem does not assert a universal impossibility of stochastic acceleration.

## Limitations and remaining risks
Identity systems, independent standard-Gaussian rank-one sketches, fixed nonnegative momentum and exact arithmetic only. Theoretical bounds are about expected squared error rather than expected iterate or finite-precision residuals. Equivalent prior material might exist and requires independent verification.

Self-review: passed. Independent audit: not yet performed.
