# Scientific review

## Correctness — PASS
The conditional-on-vacancy calculation gives the exact finite covariance, and the size-biased binomial identity converts the absolute symmetric-walk expectation to a monotone expectation of central binomial ratios. This establishes existence and uniqueness for all integers \(L\ge2\), with endpoint and one-object boundaries. The triangular-array central limit theorem with an explicit second-moment uniform-integrability bound establishes the cube-root constant. The embedded Python verifier independently evaluates all 3^L cases through L=7 at rational parameters and checks large-size root brackets. The finite checks are not claimed as a proof.

## Originality — PASS (qualified)
Actual published-finding corpus queries for occupancy maxima, vacancy covariances, fixed-frequency statistics, thinning and the cube-root threshold yielded related statements about occupied-box precision, richness/frequency covariance, and maximum parts of compositions, but not the joint statistic and retention-parameter threshold. Accessible prior claims in the relevant current ledgers were compared; the closest concerned different occupancy frequencies and parameters. Bogachev–Gnedin–Yakubovich's arXiv:math/0609498, Sections 1–2, studies occupancy and Poissonization rather than this mixed maximum covariance. Historical maximum-frequency papers by Yusas (1972/1973) and Freeman (1979), and Proschan–Sethuraman's count-association paper (1975), could not be inspected fully and may contain implicit coverage. A qualified best-knowledge originality assessment is appropriate, not an independent priority guarantee.

## Value — PASS
Vacancies measure underutilization, while the maximum load measures overload. Under a fixed finite potential workload with independently thinned arrivals, their covariance could plausibly have a single, several, or no sign reversals. The theorem proves an all-size unique transition, its two opposite signs, an exact small-size benchmark, and a nontrivial cube-root scaling constant. This is a structural classification for a natural queueing/occupancy statistic, rather than a routine moment restatement.

## Closest literature and limitations
Bogachev–Gnedin–Yakubovich (2006, arXiv:math/0609498) gives accessible occupancy context, including dependence of occupied-box counts and Poissonization; that framework does not imply the finite-\(L\) sign reversal for a maximum. Yusas (1972/1973), Freeman (1979), and Proschan–Sethuraman (1975) were identified but complete substantive texts were unavailable. The conclusion concerns only two equally likely bins with Bernoulli thinning and is not independent verification.

Self-review: passed. Independent audit: not yet performed.
