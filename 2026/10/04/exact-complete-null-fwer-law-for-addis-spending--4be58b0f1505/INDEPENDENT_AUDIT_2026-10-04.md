# Independent mathematical audit

## correctness

PASS

At state \(j\), the test level is \(a_j=\alpha q\gamma_j\). Because \(a_j\le\lambda\), rejection \(P\le a_j\) and state advancement \(\lambda<P\le\tau\) are disjoint and have probabilities \(a_j\) and \(q\); all other outcomes leave the state unchanged. Conditioning on the almost-sure first occurrence of either terminating event gives rejection probability \(\alpha\gamma_j/(1+\alpha\gamma_j)\) and survival probability \((1+\alpha\gamma_j)^{-1}\). Multiplying survival through the states and using continuity from above proves the infinite product. The lower envelope follows by expanding \(\prod_j(1+\alpha\gamma_j)\ge1+\alpha\), with equality only for one-point spending; the strict upper envelope follows from \(\sum_j\log(1+\alpha\gamma_j)<\alpha\), and uniform-on-\(N\) spending approaches the supremum. Euler's product for \(\sinh\) gives the inverse-square specialization. The inspected checker only corroborates finite recursions and numerical identities; the infinite result is proved analytically.

## originality

PASS

Tian--Ramdas give the exact ADDIS-Spending state index and level and prove PFER/FWER control, while Fischer later proves that the original ADDIS principle is conservative and constructs an exhaustive uniform improvement. Neither inspected primary source evaluates the original procedure's complete-null FWER as a gamma-dependent product, gives the sharp spending envelope, or derives the inverse-square \(\sinh\) closed form. A targeted Resultary search found no published SCOPE record with an implication-equivalent formula.

## value

PASS

The result quantifies a known and practically relevant conservatism of a named online FWER method exactly, separates the effect of the spending sequence from the discard thresholds in the complete-null regime, and identifies the sharp possible range together with a closed form for a published inverse-square schedule. This is a natural statistical invariant of the procedure rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
