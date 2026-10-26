# A stochastic majorization law for variable-size coupon packets

## Finding
Fix integers \(n\ge2\), \(k\ge2\). In round \(i\), independently choose a uniformly random \(s_i\)-element subset of the same \(n\)-element coupon population, where \(0\le s_i\le n\). Let \(U_{\boldsymbol s}\) count coupons absent from every round. Write \(\boldsymbol s\succeq\boldsymbol t\) when the integer vectors have the same sum and \(\boldsymbol s\) majorizes \(\boldsymbol t\), so that \(\boldsymbol s\) is more uneven.

**Theorem.** For every such pair of packet-size vectors,
\[
\boldsymbol s\succeq\boldsymbol t
\quad\Longrightarrow\quad
U_{\boldsymbol s}\le_{\mathrm{st}} U_{\boldsymbol t},
\qquad
\Pr(U_{\boldsymbol s}\ge r)\le\Pr(U_{\boldsymbol t}\ge r)
\quad(r\in\mathbb Z).
\]
Here \(\le_{\mathrm{st}}\) denotes first-order stochastic dominance. Equivalently, at a fixed total number of coupon exposures, equalizing packet sizes can only make *coverage worse*, simultaneously at every missing-coupon threshold. In particular, the full-coverage probability \(\Pr(U=0)\) cannot increase under equalization.

For any \(1\le s_i\le n-1\) and fixed total \(S=\sum_i s_i\), the almost-equal vector with entries \(\lfloor S/k\rfloor\) and \(\lceil S/k\rceil\) stochastically maximizes \(U\). A vector obtained by starting all sizes at \(1\) and distributing the remaining \(S-k\) exposures to successive coordinates, up to the cap \(n-1\), stochastically minimizes \(U\). These extremizers are unique up to permutation in *expected* missing count. No unproved assumption about asymptotic rates is needed: the conclusion is finite-sample and exact.

## Assumptions and scope
Packet selections are independent between rounds; within each packet, coupons are sampled uniformly **without** replacement. The sizes are deterministic, possibly unequal. Majorization uses the standard sorted-prefix definition: if \(\boldsymbol s^\downarrow\) and \(\boldsymbol t^\downarrow\) are decreasing rearrangements, then \(\sum_{i=1}^h s_i^\downarrow\ge\sum_{i=1}^h t_i^\downarrow\) for all \(h<k\), and the full sums agree. No independence between coupon-unseen indicators is assumed. The constrained optimizer statement assumes \(k\le S\le k(n-1)\).

## Proof
Put \(m_i=n-s_i\) and let \(C_i\) be the complement of the packet drawn at step \(i\). Thus the \(C_i\) are independent uniform \(m_i\)-subsets and \(U_{\boldsymbol s}=|C_1\cap\cdots\cap C_k|\). It is enough to study an elementary balancing transfer on any two sizes \(a<b-1\), changing their complement-set sizes from \((a,b)\) to \((a+1,b-1)\). Both are between \(0\) and \(n\).

Let \(J_{a,b}\) denote the intersection cardinality of two independent uniform subsets of sizes \(a,b\). Its hypergeometric mass function is
\[
p_{a,b}(j)=\frac{\binom aj\binom{n-a}{b-j}}{\binom nb},
\qquad \max(0,a+b-n)\le j\le a.
\]
The balanced pair has exactly the same lower support endpoint and upper endpoint \(a+1\). Wherever \(p_{a,b}(j)>0\), direct cancellation yields
\[
\frac{p_{a+1,b-1}(j)}{p_{a,b}(j)}
=\frac{(a+1)(n-b+1)}{b(n-a)}\,\frac{b-j}{a+1-j}.
\]
This ratio increases with \(j\): for consecutive common-support values its quotient is at least one precisely because \(b-a-1>0\). The balanced law may also have one extra largest atom. Consequently the balanced intersection cardinality dominates the unbalanced one in likelihood-ratio order, and hence in usual stochastic order. Boundary cases \(a=0\), \(b=n\), and singleton supports follow from the same mass comparison and the extra endpoint (or by continuity in finite mass tables).

Conditioned on their sizes, either random intersection \(C_i\cap C_j\) is a uniform subset of the coupon population. Stochastically couple the two intersection cardinalities \(J\le J'\), choose one independent uniform permutation of the \(n\) coupons, and realize the two intersection sets as its first \(J\) and first \(J'\) elements. They have the correct separate distributions and are nested. Intersect both with the *same* independent collection of the remaining \(C_h\). Nesting persists, giving a coupling \(U_{\mathrm{before}}\le U_{\mathrm{after}}\). The complement transformation \(s_i\mapsto n-s_i\) preserves majorization, up to reversing the order of coordinates. The integer majorization transfer theorem expresses any move from an uneven size vector to a more even one as finitely many such pair transfers and permutations; iteration establishes the claimed stochastic order.

For completeness, the exact expectation is
\[
\mathbb E U_{\boldsymbol s}=n\prod_{i=1}^k\left(1-\frac{s_i}{n}\right).
\]
Under the elementary balancing transfer \((a,b)\mapsto(a+1,b-1)\) on the complementary sizes, its increase is exactly
\[
\frac{b-a-1}{n^{k-1}}\prod_{h\notin\{i,j\}}m_h.
\]
This is strictly positive whenever no remaining complement size is zero, proving strictness of expected missing count for non-permutation constrained profiles with \(1\le s_i\le n-1\). Classical majorization identifies the equalized and concentrated vectors as the extremizers among vectors with the prescribed sum and coordinate bounds.

## Verification
A standalone standard-library checker, `VERIFY.py`, reconstructs all relevant hypergeometric probabilities as exact rational numbers. It checks every pairwise transfer for \(2\le n\le17\), every ordered three-round transfer for \(3\le n\le8\), exact enumeration of all three-round sample spaces for \(2\le n\le4\), and the displayed four-coupon example. Executing `python3 VERIFY.py` returned **PASS: 6707 exact assertions**. The finite checker independently stress-tests the formulas; the all-size result is the preceding proof.

For \(n=4\), two packets of sizes \((1,3)\) leave \(0\) and \(1\) coupons unseen with probabilities \(1/4\) and \(3/4\), whereas packets of sizes \((2,2)\) leave \(0,1,2\) unseen with probabilities \(1/6,2/3,1/6\). Thus the more uneven allocation has full-coverage probability \(1/4\), compared with \(1/6\) for the balanced allocation, illustrating a distributional difference, not just a comparison of means.

## Relationship to prior work
Betken and Thäle (first public preprint 2022) analyze Gaussian/Poisson approximation for **equal-sized** uniform group drawings, rather than comparisons between deterministic schedules of unequal group sizes. Stadje (1990) studies fixed-sized group drawings and a distinct stopping/purchasing optimization, while Schilling (2021) and Berend–Sher (2026) compare **distributions of packets for a fixed size**. The hypergeometric formula itself is classical and is used here, not claimed as new. The contribution is the *arbitrary-round, entire-distribution majorization order* and the two simultaneous budget extremizers, established through a nested-set coupling. Search did not identify an earlier statement with these quantifiers; this is not definitive proof of priority.

## Limitations
This does **not** compare models with nonuniform packet selection, random or adaptive packet sizes, dependent rounds, or costs other than a fixed total exposure budget. Equality at a particular tail threshold can occur even when expectations differ; the proof claims strict expectation only under the stated interior constraints. Historical priority is not independently settled, and the full text of some older coupon-collection sources was not accessible; any broader theorem already yielding the arbitrary-schedule stochastic comparison would limit originality. No independent mathematical audit has been performed.

## References
1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485v1 (2022-02-15), *Journal of Applied Probability* 60 (2023), 1352–1366. https://arxiv.org/abs/2202.07485 ; https://doi.org/10.1017/jpr.2023.6
2. W. Stadje, *The collector's problem with group drawings*, *Advances in Applied Probability* 22 (1990), 866–882. https://doi.org/10.2307/1427566
3. J. Schilling, *Results and conjectures on the role of the uniform distribution in the Coupon collector's problem with group drawings*, *Information Processing Letters* 169 (2021), 106112. https://doi.org/10.1016/j.ipl.2021.106112
4. D. Berend and T. Sher, *On a conjecture on uniform group drawings in the coupon collector problem*, published 2026-05-27. https://doi.org/10.1080/15326349.2026.2671340
