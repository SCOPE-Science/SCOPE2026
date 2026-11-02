# Exact cyclic-workload distribution of total traffic delay in Rule 184

## Finding

For integers \(k\ge1\), \(h\ge0\), put \(n=2k+h\). Consider all **indexed** binary configurations of a periodic ring of length \(n\) with exactly \(k\) ones, updated synchronously by elementary cellular automaton Rule 184: every one followed by a zero moves one site clockwise, and all other ones remain in place.

The **total traffic delay** \(D(x)\) is the number of stopped-car updates over the entire evolution, equivalently
\[
D(x)=\sum_{t\ge0}\sum_{i\in\mathbb Z/n\mathbb Z} (F^t x)_i(F^t x)_{i+1}.
\]
The sum is finite for the stated density range. For each \(d\ge0\), write \(N_{k,h}(d)\) for the number of those configurations with total delay \(d\).

Let \(\mathcal W_k\) be the set of **indexed, not rotation-quotiented** integer vectors \(w=(w_0,\ldots,w_{k-1})\) satisfying
\[
\min_i w_i=0,\qquad 0\le w_i\le k-1,\qquad w_i\le w_{i+1}+1
\]
with subscripts interpreted cyclically, and let \(z(w)=|\{i:w_i=0\}|\). Then the complete fixed-density distribution is
\[
\boxed{N_{k,h}(d)=\frac{2k+h}{k}
\sum_{\substack{w\in\mathcal W_k\\\sum_i w_i=d}}
\binom{h+z(w)-1}{z(w)-1}.}
\tag{1}
\]
In particular the entire polynomial in the surplus-hole variable \(h\) is determined by a finite path family depending only on \(k\), not on the circumference \(n\).

Equivalently, define a \(k\)-by-\(k\) matrix indexed by \(0\le a,b<k\), with formal variables \(q,u\), by
\[
M_{ab}(q,u)=\begin{cases}
0,&a>b+1,\\
(1-u)^{-1},&a=0,\\
q^a,&1\le a\le b+1.
\end{cases}
\]
Let \(M_+\) be its principal submatrix on positive indices, with trace of the empty matrix defined as zero. Then
\[
\boxed{\sum_{d\ge0}N_{k,h}(d)q^d
=\frac{2k+h}{k}[u^h]\left(\operatorname{tr}M(q,u)^k-\operatorname{tr}M_+(q,u)^k\right).}
\tag{2}
\]

The support of this distribution has a sharp maximum:
\[
\boxed{\max D=\binom{k}{2},\qquad N_{k,h}\!\left(\binom{k}{2}\right)=n.}
\tag{3}
\]
Exactly the \(n\) cyclic placements of one contiguous block of \(k\) cars attain this maximum. At the other end,
\[
N_{k,h}(0)=\frac{n}{k}\binom{n-k-1}{k-1},
\]
recovering the count of already free-flowing configurations.

For instance, at \(k=4,h=0\) (eight sites, four cars), the numbers with delays \(d=0,1,2,3,4,5,6\) are respectively \(2,8,12,16,16,8,8\); at \(k=4,h=2\), they are \(25,60,45,40,20,10,10\).

## Assumptions and scope

The cells are labeled \(0,\ldots,n-1\), and rotated strings are counted separately. All operations are parallel. A car is stopped precisely when its immediately clockwise neighboring cell is occupied at the start of an update. The initial density is at most one half, since \(n=2k+h\). The quantity \(D\) is total stopped-car time, *not* the time at which the last jam clears. The zero-density state is excluded by \(k\ge1\); its total delay is trivially zero.

## Proof

**1. Min-plus evolution of ordered cars.** Number cars in clockwise order and lift their positions to increasing integers \(p_i(t)\), with \(p_{i+k}(t)=p_i(t)+n\). Under Rule 184 the exact update is
\[
p_i(t+1)=\min\{p_i(t)+1,\;p_{i+1}(t)-1\}.
\]
Induction gives, for all \(t\ge0\),
\[
p_i(t)=\min_{0\le j\le t}\{p_{i+j}(0)+t-2j\}.
\tag{4}
\]
Let \(g_i=p_{i+1}(0)-p_i(0)-1\ge0\) be the initial clockwise empty gap, so that \(\sum_i g_i=n-k=k+h\). The number of updates at which car \(i\) has been stopped up to time \(t\) is
\[
w_i(t)=t-[p_i(t)-p_i(0)]
=\max_{0\le j\le t}\sum_{r=0}^{j-1}(1-g_{i+r}).
\tag{5}
\]
A complete tour of the \(k\) gaps contributes \(k-\sum_i g_i=-h\le0\). Thus the maximum over all \(j\ge0\) is attained for some \(0\le j<k\). In particular no car ever stops after the first \(k-1\) updates, and its total number of stops is
\[
w_i=\max_{0\le j<k}\sum_{r=0}^{j-1}(1-g_{i+r}).
\tag{6}
\]
Consequently \(D=\sum_i w_i\).

**2. Cyclic workload bijection.** Equation (6) satisfies the cyclic Lindley recurrence
\[
w_i=\max\{0,1-g_i+w_{i+1}\}.
\tag{7}
\]
The term corresponding to one full tour is \(-h\le0\), so it does not change the maximum. There is at least one zero workload: take an index where the partial sums of the cyclic sequence \(1-g_i\) attain their maximum; every forward prefix from that index has nonpositive sum, including prefixes wrapping across the nonpositive full-tour total. Equation (7) also implies \(w_i\le w_{i+1}+1\). Starting from an index of zero workload, this last inequality yields \(w_i\le k-1\) everywhere. Hence \(w\in\mathcal W_k\).

Conversely, choose \(w\in\mathcal W_k\) and nonnegative integers \(e_i\) at its \(z(w)\) zero positions such that \(\sum_{w_i=0}e_i=h\). Reconstruct gaps uniquely by
\[
g_i=\begin{cases}
1+w_{i+1}-w_i,&w_i>0,\\
1+w_{i+1}+e_i,&w_i=0.
\end{cases}
\tag{8}
\]
All gaps are nonnegative, sum to \(k+h\), and satisfy (7). The solution of (7) having at least one zero is unique: from any index, iterating the recurrence forward until the next zero gives the maximum of the intervening prefix sums, exactly (6). Thus this construction is a bijection between gap vectors and pairs \((w,(e_i))\). The number of weak compositions of \(h\) into \(z(w)\) slots is \(\binom{h+z(w)-1}{z(w)-1}\).

**3. Indexed-site correction and generating function.** A cyclic gap vector is rooted at a specified car. Count pairs consisting of an indexed ring configuration and one of its \(k\) cars. There are \(kN_{k,h}(d)\) such pairs of delay \(d\). Each gap vector can be placed with its rooted car at any of the \(n\) labeled sites, giving \(n\) pairs. Hence the factor \(n/k\) in (1). For the transfer-matrix form, a closed walk of length \(k\) in the matrix of (2) records a cyclic vector with the transition restriction \(a\le b+1\). A zero state contributes \((1-u)^{-1}\) and a positive state contributes \(q^a\). Subtracting \(\operatorname{tr}M_+^k\) removes precisely the walks without a zero; coefficient extraction then gives (1).

**4. Sharp maximum.** Fix a zero coordinate \(w_j=0\). Iterating \(w_i\le w_{i+1}+1\) backward gives \(w_{j-r}\le r\) for \(0\le r<k\), so \(\sum_i w_i\le\sum_{r=0}^{k-1}r=\binom{k}{2}\). Equality forces the unique cyclic descending staircase beginning at the maximum and ending at zero. There are exactly \(k\) indexed rotations of that staircase, each with one zero, and each permits exactly one allocation of the \(h\) spare holes. By (8) their gap vectors have all zeros except one gap of \(n-k\), which means a single contiguous block of cars. The indexed-site conversion gives exactly \(n\) maximizers. For \(D=0\), only \(w=(0,\ldots,0)\) contributes, giving the stated lower-end formula.

## Verification

The standalone standard-library file `verify.py` independently iterates the actual Boolean Rule-184 site update, counts every stopped car at each time, and compares the resulting delay histograms with (1) for 32 complete parameter pairs: \(1\le k\le6\) with \(0\le h\le4\), and \(k=7\) with \(h\in\{0,1\}\). It also checks a separately implemented cyclic gap-prefix formula, the total \(\binom nk\) number of initial states, and both sharp endpoint counts. Run `python3 verify.py`; success prints `VERIFY_OK`. These computations are corroboration; the proof above establishes all admissible parameters.

## Relationship to prior work

Fukś's 1997 analysis of Rule 184 provides a block-preimage/ballot characterization, the density-classification mechanism, and a convergence bound. His 1999 paper derives time-dependent mean flow using local preimage counts. These are genuine precedents, not claimed as new here. Jha, Wiesenfeld, Lee and Laval (first preprint January 14, 2025) define the aggregate total delay and give a Dyck-path based algorithm for measuring jam areas, then analyze sampled finite-size scaling. Biham, Hertzberg Rabinovich and Katzav (first preprint May 18, 2026) derive single-car first/last stopping and stop-count laws in the randomly initialized model. The result here instead gives an exact **entire finite-ring, fixed-car-count, whole-system total-delay distribution**, with a universal cyclic-workload enumerator, polynomial dependence on surplus holes, and sharp attained endpoint classification. The checked sources did not state that coefficient formula; known individual-trajectory or local-marginal formulas do not directly provide it without additional joint counting.

## Limitations

Only deterministic one-step Rule-184 motion is considered, on periodic labeled binary rings with at most one car per two sites initially. At densities above one half, cars remain blocked indefinitely, so this definition of cumulative delay is generally infinite. The formula is an exact finite combinatorial enumerator, not an explicit asymptotic limit theorem or a claim that all related queueing formulations are historically unprecedented. Completeness of searches of older unindexed queueing and traffic literature is not guaranteed. No independent audit has been performed.

## References

1. Henryk Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules* (first public arXiv submission March 7, 1997), https://arxiv.org/abs/comp-gas/9703001.
2. Henryk Fukś, *Exact results for deterministic cellular automata traffic models* (first public arXiv submission February 4, 1999), https://arxiv.org/abs/comp-gas/9902001.
3. Aryaman Jha, Kurt Wiesenfeld, Garyoung Lee, Jorge Laval, *Evidence of Non-Equilibrium Critical Phenomena in a Simple Model of Traffic* (first public arXiv submission January 14, 2025), https://arxiv.org/abs/2501.08417.
4. Ofer Biham, Gilad Hertzberg Rabinovich, Eytan Katzav, *First-passage processes in a deterministic one-dimensional cellular automaton model of traffic flow* (first public arXiv submission May 18, 2026), https://arxiv.org/abs/2605.19023.
