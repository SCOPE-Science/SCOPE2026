# A sharp support-sensitive cleanup bound for Condat's simplex projection algorithm
## Finding
Consider the proposed simplex-projection algorithm of Condat, and count one cleanup examination each time step 4 tests a current candidate against the running threshold. For an input of length \(N\ge 2\), let \(K\) be the number of positive coordinates in the projected point.

If \(K=1\), step 4 starts with a singleton and performs exactly one cleanup examination. If \(2\le K\le N\), the sharp maximum number of cleanup examinations is
\[
T_{N,K}=\sum_{s=K}^{N}s
=\frac{N(N+1)-(K-1)K}{2}.
\]
Every pair \((N,K)\) with \(2\le K\le N\) is attained by an explicit rational input family. Thus the cleanup cost has a sharp support-sensitive discontinuity: \(K=1\) forces immediate collapse, whereas \(K=2\) can attain
\[
T_{N,2}=\frac{N(N+1)}2-1.
\]

## Assumptions and scope
The statement concerns the exact real-arithmetic pseudocode in Fig. 2 of Condat's algorithm for Euclidean projection onto
\[
\Delta_a=\left\{x\in\mathbb R^N:x_i\ge0,\ \sum_{i=1}^N x_i=a\right\},
\qquad a>0.
\]
A cleanup examination means one execution of the comparison \(y\le\rho\) inside step 4. The count does not include the first scan, step 3, final thresholding, arithmetic operations, memory movement, or floating-point effects.

For \(2\le K<N\), put \(d=N-K\), \(H=4N^2\), \(r_0=0\), \(z_0=-1\), and
\[
r_1=\frac1{N-1}.
\]
For \(q=1,\ldots,d-1\), define
\[
z_q=\frac{r_{q-1}+r_q}{2},
\qquad
r_{q+1}=r_q+\frac{r_q-z_q}{N-q-1}.
\]
Set the first \(d\) input coordinates in the reverse order
\[
(y_1,\ldots,y_d)=(z_{d-1},\ldots,z_0),
\]
set \(y_{d+1}=\cdots=y_N=H\), and choose
\[
a=\sum_{i=1}^N y_i.
\]
For \(K=N\), take \(y_i=H\) and \(a=NH\).

## Proof
First consider an arbitrary input. At the beginning of each nonterminal cleanup pass, the candidate list has some size \(s\). Condat's correctness argument shows that every nonterminal pass removes at least one element. The terminal list has exactly \(K\) elements. Therefore, if step 4 begins with \(m\le N\) candidates, its pass sizes are bounded by
\[
m,m-1,\ldots,K,
\]
and hence the number of cleanup examinations is at most
\[
\sum_{s=K}^{m}s\le \sum_{s=K}^{N}s.
\]

There is a stronger fact when \(K=1\). Let \(M\) be the unique coordinate above the final threshold, so the threshold is \(\tau=M-a\), and every other coordinate is at most \(\tau\). Before \(M\) is read, the maintained threshold satisfies \(\rho\le\tau\). If the current candidate list has size \(q\) and sum \(S\), then \(S\le q\tau\). After provisionally adding \(M\),
\[
\rho'=\frac{S+M-a}{q+1}
\le\frac{q\tau+\tau}{q+1}
=\tau=M-a.
\]
Thus step 2.2 cannot accept the enlarged list: step 2.3 resets to the singleton \((M)\) with threshold \(\tau\). All later coordinates are at most \(\tau\) and are ignored, while every earlier buffered coordinate is also at most \(\tau\) and fails the strict step-3 test. If \(M\) is the first coordinate, the same singleton state holds from initialization. Hence step 4 starts with one element and performs exactly one terminal examination.

It remains to attain the upper bound for \(K\ge2\). For the family above, let
\[
\delta_q=r_q-r_{q-1}.
\]
For \(q\ge1\),
\[
\delta_{q+1}=\frac{\delta_q}{2(N-q-1)}>0.
\]
Consequently the \(r_q\) increase, \(z_0=-1\), and for \(q\ge1\),
\[
r_{q-1}<z_q<r_q.
\]
Moreover \(\delta_{q+1}\le\delta_q/2\), so \(0<r_q<1\). Thus all prefix values lie in \([-1,1]\).

Because \(K\ge2\) and \(H=4N^2\), the choice \(a=\sum_i y_i\) is positive and makes the threshold associated with the full candidate list exactly \(0\). The large final block of \(K\) copies of \(H\) also guarantees, by direct substitution in steps 2.1--2.3, that every prefix value and every copy of \(H\) is retained in the first pass and no reset occurs. In particular, step 4 starts with all \(N\) coordinates and threshold \(r_0=0\).

The first cleanup pass scans
\[
z_{d-1},\ldots,z_1,z_0,H,\ldots,H.
\]
All \(z_q\) with \(q\ge1\) are positive, while \(z_0=-1\le r_0\), so exactly \(z_0\) is removed. The update formula gives threshold \(r_1\). Inductively, after \(q\) removals the threshold is \(r_q\), and the next scan sees every \(z_j\) with \(j>q\) above \(r_q\), then sees
\[
z_q=\frac{r_{q-1}+r_q}{2}<r_q
\]
and removes exactly that one element. The update is precisely the defining recurrence for \(r_{q+1}\). After all \(d=N-K\) prefix elements have been removed, only the \(K\) copies of \(H\) remain; since \(r_d<1<H\), the final pass removes none.

Therefore the successive cleanup-pass sizes are exactly
\[
N,N-1,\ldots,K,
\]
so the number of examinations is exactly \(T_{N,K}\). This meets the general upper bound.

## Verification
The accompanying `verify.py` implements the Fig. 2 recurrence using exact rational arithmetic. It constructs the family for every \(2\le N\le30\) and every \(2\le K\le N\), checks that the first cleanup pass starts with all \(N\) candidates, checks that the final support has size \(K\), and verifies the exact examination count
\[
\frac{N(N+1)-(K-1)K}{2}.
\]
It separately tests the singleton-support collapse on a collection of exact rational examples. These finite checks support the implementation details; the all-\(N\), all-\(K\) result is established by the proof above.

## Relationship to prior work
Condat's 2014 preprint gives the same proposed algorithm, proves finite termination, states quadratic worst-case complexity, and explicitly transforms a Michelot adversary into an adversary for the proposed method. The later final author version retains the \(O(N^2)\) worst-case statement but omits that explicit transformed sequence. Those results already cover the existence of quadratic examples and are not claimed as new here.

The distinction here is an exact, support-conditioned maximum for the cleanup loop. The source uses \(K\) for the final number of nonzero projected coordinates, but its complexity table gives only \(O(N^2)\) for the proposed algorithm rather than a sharp function of \(N\) and \(K\). The singleton case is structurally exceptional because the reset mechanism forces the cleanup list to collapse to one element as soon as the unique active coordinate is encountered.

A 2026 preprint on dynamic-threshold algorithms generalizes the addition/reset/removal mechanism to weighted continuous quadratic knapsack problems and studies quadratic worst cases and long removal phases. Its abstract and indexed summaries do not state the support-sensitive formula above, but its full text could not be inspected through the available lawful access route; this is the main residual originality risk.

## Limitations
The result counts only step-4 element tests in exact arithmetic. It is not an exact wall-clock bound for an implementation, and it does not count the first pass, buffering, final thresholding, or memory costs. The adversarial family is deliberately structured and does not assert typical behavior. The result is specific to Condat's Fig. 2 ordering semantics and strict/non-strict comparisons.

The 2026 weighted dynamic-threshold preprint is a close later source whose accessible abstract emphasizes the same reset/removal mechanism and quadratic complexity. Because its full text was unavailable in this review, an equivalent support-conditioned count there cannot be excluded.

## References
1. Laurent Condat, *Fast Projection onto the Simplex and the l1 Ball*, preprint HAL-01056171 v1, August 2014; Optimization Online record 4498, published August 17, 2014.
2. Laurent Condat, *Fast Projection onto the Simplex and the l1 Ball*, Mathematical Programming 158 (2016), 575--585, DOI: 10.1007/s10107-015-0946-6.
3. Krzysztof C. Kiwiel, *Variable Fixing Algorithms for the Continuous Quadratic Knapsack Problem*, Journal of Optimization Theory and Applications 136 (2008), 445--458, DOI: 10.1007/s10957-007-9317-7.
4. Yong-Jin Liu, Peicheng Xie, Chuan Yang, *Dynamic-Threshold Algorithms for the Continuous Quadratic Knapsack Problem: Reset Mechanisms and Complexity*, arXiv:2608.00740v1, 2026.
