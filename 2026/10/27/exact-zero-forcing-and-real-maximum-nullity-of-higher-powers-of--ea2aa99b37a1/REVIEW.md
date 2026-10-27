# Mathematical review

## Correctness — PASS
The theorem uses a complete, explicit forcing chronology giving \(Z\le(m-1)r\) and a real symmetric witness \(A\) with exact off-diagonal support and a \((m-1)r\)-dimensional kernel. The window-incidence matrix has rank \(\ell-r\) by an explicit triangular minor; its Gram matrix has the requisite within-arm support. Every cross-arm matrix entry and centre entry is nonzero exactly for distance at most \(r\). Symmetric branch differences in the kernel of the window matrix yield the claimed lower bound. The general inequality \(M\le Z\) completes the proof and ranks. The argument handles the tight boundary \(\ell=r+1\). The independent verifier checked 83 exact matrix/support/forcing instances (47 at higher powers), and independently brute-forced the zero-forcing number in 30 small instances. No finite enumeration is used as an infinite proof.

## Originality — PASS, qualified
The direct motivating work [1], inspected through its full HTML text in the relevant sections, gives the upper bound as Proposition 9 but labels equality Conjecture 10. Work [2] on tree squares, and [3] on path powers and strict tree powers, has different power ranges or adjacency definitions. A previously established isolated cube result settles only exponent three; its statement neither implies the result for \(r\ge4\) nor reduces the entire conjecture to a finite check. Exact-publication and equivalent-parameter searches did not reveal a general formula, but the absence of a search hit is not treated as proof of novelty. Historical priority remains a residual risk.

## Value — PASS
This proves an explicitly published open infinite-parameter conjecture in its genuinely unproved high-power range, matching a known upper bound for every exponent \(r\ge4\) and arm length \(\ell\ge r+1\). It additionally constructs exact-support matrices attaining maximum nullity and gives a real minimum-rank formula. These structural certificates explain the equality and are not isolated numerical checks or cosmetic reformulations.

## Closest literature and limits
[1] Abiad et al., arXiv:2610.03892v1, Proposition 9 and Conjecture 10; [2] Chang--Lin, *Minimum Rank of Powers of Cycles and Trees*, Theorem 4.1 for squares; [3] DeAlba et al., *Minimum Rank of Powers of Trees*, Electron. J. Linear Algebra 23 (2012), mainly the path/strict-power results; [4] the classical zero-forcing/max-nullity inequality. The result does not classify arbitrary unequal-arm spiders or all tree powers, and independent review and historical-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
