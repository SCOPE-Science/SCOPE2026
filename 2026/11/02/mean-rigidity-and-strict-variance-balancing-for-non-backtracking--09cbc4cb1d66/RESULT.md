# Mean rigidity and strict variance balancing for non-backtracking cover times on cycle bouquets

## Finding

For the non-backtracking random walk started at the common hub of a bouquet of \(k\ge 2\) vertex-disjoint-away-from-the-hub simple cycles of respective lengths \(\ell_1,\ldots,\ell_k\ge3\), the expected vertex cover time is determined **only by the number of petals and total edge count**, whereas the cover-time variance increases strictly with petal-length imbalance. More precisely, let
\[
L=\sum_{i=1}^k\ell_i,\quad Q=\sum_{i=1}^k\ell_i^2,\quad
H=\sum_{j=1}^{k-1}\frac1j,\quad H_2=\sum_{j=1}^{k-1}\frac1{j^2},
\]
and put
\[
m_k=1+\frac{2k-1}{2}H,\qquad
v_k=\frac{(2k-1)^2}{4}H_2-\frac{2k-1}{2}H,\qquad
b_k=\frac1k+\frac{(2k-1)(k-2)}{2k(k-1)}H.
\]
If \(T\) is the number of traversed edges until every vertex has been visited, then
\[
\boxed{\mathbb E T=\frac{Lm_k}{k}-1,\qquad
\operatorname{Var}(T)=\frac{L^2v_k}{k^2}+b_k\left(Q-\frac{L^2}{k}\right).}
\]
In particular \(b_k>0\). For fixed feasible integer \(k,L\), the variance is **minimized exactly by the petal-length multisets whose lengths differ by at most one**. Changing the lengths while preserving \(k,L\) never changes the mean, but any unit transfer from a longer to a shorter petal with a gap of at least two strictly reduces the variance.

## Assumptions and scope

The graph is formed from simple cycles \(C_{\ell_i}\) with one common hub \(o\), no other shared vertices or edges, and \(\ell_i\ge3\). There are \(L\) edges and \(1+L-k\) vertices. The walk starts at \(o\), chooses its first edge uniformly from the \(2k\) available edges, and thereafter uniformly chooses among incident edges other than the immediately reversed edge. The cover time counts edge traversals, and the starting hub counts as already visited. No laziness, resetting, or other modifications are allowed. The graph is finite, \(k\ge2\), and \(L\ge3k\).

## Proof

**1. Reduce the walk to petal excursions.** Once it enters a petal from \(o\), the non-backtracking rule forces it around the entire cycle to \(o\); all other vertices of that petal are thereby visited. At the next departure from \(o\), exactly one of its \(2k\) neighbours (the just-used arriving neighbour) is forbidden. Hence the successive petal labels \(I_1,I_2,\ldots\) form a Markov chain whose initial label is uniform on \(\{1,\ldots,k\}\) and whose transition probabilities are
\[
P(i,i)=\frac1{2k-1},\qquad P(i,j)=\frac2{2k-1}\quad(i\ne j).
\]
Let \(J\) be the first excursion index by which all petals have been entered, and set \(C_i=\#\{s\le J:I_s=i\}\). The final previously unvisited vertex is reached one edge before the final return to \(o\), so the **vertex** cover time is exactly
\[
T=\sum_{i=1}^k\ell_i C_i-1.
\]
This final-edge correction is essential: counting complete excursions would give a different stopping time.

**2. Find the coupon-completion count.** When \(r\) distinct petals have been seen, the next excursion discovers a new petal with probability
\[
p_r=\frac{2(k-r)}{2k-1},\qquad 1\le r<k.
\]
This probability is independent of the current petal and the past. The strong Markov property therefore gives independent geometric variables \(G_r\), each on \(\{1,2,\ldots\}\) with success probability \(p_r\), and
\[
J\overset{d}=1+\sum_{r=1}^{k-1}G_r.
\]
Using \(\mathbb E G_r=1/p_r\) and \(\operatorname{Var}(G_r)=(1-p_r)/p_r^2\), the harmonic sums yield \(\mathbb EJ=m_k\) and \(\operatorname{Var}(J)=v_k\).

**3. Exploit petal-label exchangeability.** All \(C_i\) have the same distribution, \(\sum_i C_i=J\), and therefore \(\mathbb EC_i=m_k/k\). To compute the component of covariance perpendicular to the all-ones vector, set
\[
b_k^*=\operatorname{Var}(C_1)-\operatorname{Cov}(C_1,C_2)
=\frac{k\,\mathbb E\sum_{i=1}^k C_i^2-\mathbb E J^2}{k(k-1)}.
\]
We now evaluate this number without assuming any independence of the counts.

**4. Compute the self-occupation second moment.** At any visit to an already seen petal, suppose there are \(r<k\) seen petals. Let \(A_r\) be the expected number of *future* visits to the currently occupied marked petal before all petals are seen. For \(r\ge2\), let \(B_r\) be the same expectation when the marked petal is among the seen ones but is not current. First-step conditioning on the petal-chain transition probabilities above gives, for \(2\le r<k\),
\[
A_r-B_r=-\frac1{2k},\qquad
B_r-B_{r+1}=\frac{2k-1}{2k(k-r)},\qquad B_k=0.
\]
For clarity, the first identity follows by subtracting the two first-step equations, with difference \(\delta\) satisfying \(\delta=-(1+\delta)/(2k-1)\). Substituting \(A_r=B_r-1/(2k)\) into the second first-step equation gives the second identity. Consequently, for \(2\le r\le k\) the second quantity is \(B_r=(2k-1)H_{k-r}/(2k)\), with \(H_0=0\). At the one-petal boundary, first-step conditioning separately gives \(A_1=B_2+1/[2(k-1)]\), consistent with the same general formula for \(A_r\). Thus **for every** \(1\le r<k\),
\[
A_r=\frac{(2k-1)H_{k-r}-1}{2k},
\]
where \(H_j=\sum_{q=1}^j1/q\) for positive \(j\). Exactly \(G_r\) excursion positions occur while \(r\) petals have been seen, and the expectation of the future visits to the petal currently occupied at each such position is \(A_r\). Every unordered pair of equal petal labels is counted once this way. Thus
\[
\mathbb E\sum_{i=1}^k C_i^2
=m_k+2\sum_{r=1}^{k-1}\frac{A_r}{p_r}
=m_k+\frac{2k-1}{2k}\left[\frac{2k-1}{2}(H^2+H_2)-H\right].
\]
Here we used the exact harmonic identity \(\sum_{j=1}^{k-1}H_j/j=(H^2+H_2)/2\). Substituting this and \(\mathbb EJ^2=m_k^2+v_k\) into the formula for \(b_k^*\), and simplifying, yields
\[
b_k^*=\frac1k+\frac{(2k-1)(k-2)}{2k(k-1)}H=b_k>0.
\]
For \(k=2\), the second term vanishes and \(b_2=1/2\); for \(k>2\), both terms are nonnegative and the first is strictly positive.

**5. Recover the weighted cover-time moments.** Exchangeability makes the covariance matrix of \((C_i)\) have one eigenvalue \(\operatorname{Var}(J)/k\) along the all-ones vector and eigenvalue \(b_k\) on its orthogonal complement. Therefore
\[
\operatorname{Var}\left(\sum_i\ell_iC_i\right)
=\frac{L^2}{k^2}\operatorname{Var}(J)
+b_k\sum_i\left(\ell_i-\frac Lk\right)^2,
\]
proving the formula. A pair of integer lengths \(a,b\) with \(a\ge b+2\) can be changed to \(a-1,b+1\), retaining all lower bounds and lowering \(a^2+b^2\) by \(2(a-b-1)>0\). Repeated smoothing proves exactly the asserted balanced minimizers. The mean follows from \(\mathbb E C_i=m_k/k\), and its correction of \(-1\) accounts for the last untraversed edge.

## Verification

The standalone standard-library Python script `verify.py` independently builds the directed-edge/visited-vertex Markov chain of the original walk and solves its exact rational first and second hitting-time equations, without using the petal-label transition reduction. Its ten small bouquets, plus independent exhaustive length-vector balancing checks, passed **7,820 exact rational assertions** (`VERIFY_OK`). Examples: lengths \((3,3)\) give \(\mathbb ET=13/2\), \(\operatorname{Var}T=27/4\); lengths \((3,3,3)\) give \(53/4\) and \(585/16\). These finite checks corroborate the recurrences but do not prove the all-size statement: that is supplied by Steps 1–5.

Reproduce with `python3 verify.py` in a standard Python 3 environment. The checker uses only the standard library and has no network or data dependencies.

## Relationship to prior work

Breen and collaborators' 2022 non-backtracking Kemeny-constant analysis studies a different invariant (stationary averages of hitting times), including graph structures formed from cycles. Kemeny's constant, even when explicitly known for a graph, does not determine the vertex cover-time mean or variance, nor its response to redistributing cycle lengths. The later work on vertex-based Kemeny constants of pinwheel graphs addresses that separate statistic. Matsuo, Kawagishi and Ohsaki (2023, first public 2022) investigate mean cover times for non-backtracking walks in broad random-regular and random-degree settings; the formula here addresses arbitrary individual bouquet lengths and a strict variance comparison. The novelty assertion is specific to this exact mean-rigidity/variance-balancing combination, not to non-backtracking walks or coupon-collector methods as such.

## Limitations

The graph must be a one-hub bouquet of at least two simple cycles; the initial vertex must be the hub. The result does not give the full cover-time distribution for unequal petal lengths, exact graph-generic cover times, or a general cactus-graph theorem. Classical cover-time and Markov-reward theory could contain an equivalent formulation not found in the sources inspected. The checker establishes finitely many exact cases, not an independent proof or historical-priority certification. Independent external mathematical audit has not been performed.

## References

1. J. Breen and collaborators, *Kemeny's constant for non-backtracking random walks*, arXiv:2203.12049, first version 22 March 2022. https://arxiv.org/abs/2203.12049
2. S. Matsuo, D. Kawagishi, and M. Ohsaki, *On the mean first passage time and mean cover time of a non-backtracking random walk on graphs*, IEICE Communications Express 12 (2023), first publicly available 7 November 2022. https://www.jstage.jst.go.jp/article/comex/12/1/12_2022XBL0146/_pdf
3. J. Breen and collaborators, *On defining Kemeny's constant for a non-backtracking random walk*, arXiv:2510.06650 (2025), relevant pinwheel discussion. https://arxiv.org/abs/2510.06650
