# Exact two-level occupation generating function at the minimum of a symmetric random walk

## Finding
Let \(S_0=0\) and \(S_j=X_1+\cdots+X_j\), where the increments are independent and \(\Pr(X_i=1)=\Pr(X_i=-1)=1/2\). Define the *sample-path* minimum and its two lowest occupation counts by
\[
M_n=\min_{0\le i\le n}S_i,\qquad
L_{r,n}=\sum_{i=0}^{n}\mathbf1\{S_i=M_n+r\}\quad(r=0,1).
\]
These counts treat repeated lattice heights as distinct time observations. They are not the number of distinct sites visited.

Write
\[
s=\sqrt{1-z^2},\quad e=\frac{1-s}{2},\quad q=\frac{1+z+s}{2s},\quad h=\frac{q}{1-e},
\]
with the square root expanded at \(z=0\). Define
\[
A(z,v)=\frac{z^2v}{4[1-ve(z)]},\qquad
C(z,v)=1+\frac{zv}{2[1-ve(z)]}\left(1+\frac{zh(z)}2\right).
\]
Then the **exact finite-horizon joint occupation generating function** is
\[
\boxed{\sum_{n\ge0}z^n\mathbb E\!\left[u^{L_{0,n}}v^{L_{1,n}}\right]
=\frac{u\,C(z,v)^2}{1-uA(z,v)}.}
\]
The identity holds in formal power series, so each joint finite-sample probability is obtained by extracting \([z^nu^av^b]\) from the displayed right-hand side. In particular, for every integer \(n\ge2\),
\[
\boxed{\Pr(L_{0,n}=1,L_{1,n}=1)=\frac12\Pr(S_1\ge0,\ldots,S_{n-2}\ge0)\sim\frac1{\sqrt{2\pi n}}.}
\]

## Assumptions and scope
The walk starts at zero, has exactly \(n\ge0\) independent fair nearest-neighbour steps, and observes all \(n+1\) positions, including time zero. The variable \(u\) marks occurrences of the global minimum; \(v\) marks occurrences of the value exactly one greater than that minimum. The formula is not for ordinary visits to a fixed spatial level, nor for the range or number of visited sites. For coefficient manipulations, \(z\) is a formal variable; analytical limits use \(0<z<1\).

## Proof
**1. Unweighted elementary excursions.** A strictly positive first-return excursion is a sequence that starts at zero, stays strictly positive until its last return to zero, and ends at zero. The number of such paths of length \(2m\) is the Catalan number \(\mathrm{Cat}_{m-1}\), hence its probability-length generating function is
\[
e(z)=\sum_{m\ge1}\mathrm{Cat}_{m-1}\frac{z^{2m}}{4^m}
=\frac{1-\sqrt{1-z^2}}2.
\]
Let \(q(z)\) be the probability-length generating function of *strictly positive meanders*, with the empty path included, and \(h(z)\) that of nonnegative meanders, again including the empty path. Splitting a nonnegative meander at each complete positive excursion before its terminal strictly positive meander gives \(h=q/(1-e)\).

**2. Evaluate \(q\).** Any finite walk decomposes uniquely at its first global minimum into a time-reversed strictly positive meander and a nonnegative suffix. Since fair increments are invariant under sign reversal and time reversal, the weighted length generating function of the first part is \(q\); that of the second part is \(h=q/(1-e)\). Summing all walks by their (unique) first-minimum index gives \(q^2/(1-e)=1/(1-z)\). Its solution with nonnegative coefficients and constant term one is
\[
q(z)=\sqrt{\frac{1-e(z)}{1-z}}=\frac{1+z+\sqrt{1-z^2}}{2\sqrt{1-z^2}}.
\]
All square roots have constant term one.

**3. Excursions with level-one marks.** Let \(A(z,v)\) generate strictly positive excursions from level zero back to zero, where each time spent at height one contributes a factor \(v\). Each such excursion begins \(0\to1\), has an arbitrary concatenation of excursions from one to one staying strictly above one between returns, and ends \(1\to0\). The translated interior excursions each contribute \(e(z)\), and the starting and each subsequent arrival at level one contribute \(v\). Therefore
\[
A(z,v)=\frac{z^2v}{4}\sum_{r\ge0}[ve(z)]^r
=\frac{z^2v}{4[1-ve(z)]}.
\]
The final return to zero is not counted at level one.

**4. Strict meanders with level-one marks.** Let \(C(z,v)\) enumerate strictly positive meanders, weighting the number of their level-one observations by \(v\). Apart from the empty path, each begins with \(0\to1\), proceeds through zero or more complete excursions from one into heights at least two (each of weight \(ve(z)\)), and terminates either at level one or after a final step \(1\to2\), followed by an arbitrary nonnegative meander shifted up to start at two. The final segment contributes \(1+zh(z)/2\). Thus
\[
C(z,v)=1+\frac{zv}{2}\sum_{r\ge0}[ve(z)]^r
\left(1+\frac{zh(z)}2\right).
\]
For \(v=1\), this reduces to \(C(z,1)=q(z)\), independently verifying the normalization.

**5. Global-minimum decomposition.** Every finite path has a unique first time attaining its global minimum. Reversing the part strictly before that time gives a strictly positive meander; after that time the path splits into exactly \(L_{0,n}-1\) complete strictly positive excursions followed by one terminal strictly positive meander. Reversal preserves length, height relative to the global minimum, and fair path probability. Each minimum visit contributes \(u\); each visit one unit higher contributes \(v\). Consequently, paths with exactly \(k\ge1\) minimum visits have generating function \(u^k C(z,v)^2A(z,v)^{k-1}\). Sum the geometric series in \(k\) to obtain the asserted trivariate identity. Every path occurs in exactly one term and all coefficients are nonnegative.

**6. A rare finite-horizon joint cell.** The coefficient of \(u^1v^1\) in the joint generating function comes solely from \(C(z,v)^2\). Direct expansion of its two meanders gives
\[
[u^1v^1]\frac{uC(z,v)^2}{1-uA(z,v)}
=z+\frac{z^2}{2}h(z).
\]
Therefore, at every \(n\ge2\), the probability of exactly one visit to the minimum and exactly one to the next level is half the probability that a simple walk stays nonnegative for its first \(n-2\) steps. The reflection principle gives
\[
\Pr(S_1\ge0,\ldots,S_t\ge0)=2^{-t}\binom{t}{\lfloor t/2\rfloor},
\]
so the displayed joint event equals \(2^{-(n-1)}\binom{n-2}{\lfloor(n-2)/2\rfloor}\), and Stirling's formula gives the claimed sharp equivalent. For \(n=1\) its probability is one; for \(n=0\) it is zero.

## Verification
Run the standalone `verify.py` using Python 3's standard library. The checker independently enumerates all fair \(\pm1\) paths through ten steps, compares every joint count against the excursion/meander convolution, checks the closed rational-algebraic series coefficients of \(A\) and \(C\) at five distinct rational weights, and verifies the rare-cell identity. Exact fractions are used throughout. These bounded enumerations are checks, not proofs for all horizons; the proof above uses complete path decomposition and formal generating functions.

## Relationship to prior work
Pitman and Tang, *Extreme order statistics of random walks* (arXiv:2007.13991), Section 4 and Theorem 4.1, identify the **limiting** occupation-count process near the minimum of a simple symmetric random walk, including its branching-process description. The limiting one-level and two-level laws are therefore prior theory. The formula here instead provides a closed trivariate generating function for the **entire finite-horizon joint law** of the two lowest occupation counts, yielding finite-time cells such as the sharp \(n^{-1/2}\) rare-event law.

Katzenbeisser and Panny, *Simple Random Walk Statistics. Part I: Discrete Time Results* (1990), provide exact distributions of visits to a **fixed level** and numbers of visits to the global maximum, including endpoint-conditioned identities. Their listed joint distributions involving the maximum concern its height or hitting time rather than the joint occupation counts of the maximum and the immediately neighbouring level. Their formulas are important prior finite-horizon coverage, but the cited results do not state the bivariate minimum-neighbour occupation series above. By symmetry, maxima can replace minima in the present theorem.

Csáki and Hu (2003) give exact laws for the ranked lengths and heights of excursions measured from a fixed origin; Régnier, Dolgushev, Redner and Bénichou (2022) study the process counting **distinct visited sites**. Neither of those statistics equals the joint number of observations at the two lowest order-statistic values.

## Limitations
This result assumes fair nearest-neighbour increments. It does not claim a new limiting joint occupation law, a result for continuous increments, a uniform-in-increment theorem, or an independently certified historical priority search. General finite-state transfer-matrix techniques could potentially imply the displayed formula through an unrecognized earlier identity. The exact rare-cell probability is one consequence of the full finite law, not an independent assertion of broad new theory. No independent validation has been performed.

## References
- J. Pitman and W. Tang, *Extreme order statistics of random walks*, first publicly posted July 28, 2020, arXiv:2007.13991, https://arxiv.org/abs/2007.13991 .
- W. Katzenbeisser and W. Panny, *Simple Random Walk Statistics. Part I: Discrete Time Results*, 1990, https://research.wu.ac.at/ws/portalfiles/portal/19844788/document.pdf .
- E. Csáki and Y. Hu, *Lengths and heights of random walk excursions*, DMTCS AC (2003), https://dmtcs.episciences.org/articles/3337/download .
- L. Régnier, M. Dolgushev, S. Redner and O. Bénichou, *Complete Visitation Statistics of 1d Random Walks*, 2022, arXiv:2202.13820, https://arxiv.org/abs/2202.13820 .
