# Eventual diameter–height locking in Bernoulli two-step recursive trees

## Finding

Let \(0<p<1\), \(q=1-p\). Starting with vertices \(1,2\) and their edge, independently attach vertex \(j\ge3\) to \(j-1\) with probability \(p\) or \(j-2\) with probability \(q\). Write \(H_n\) for the maximum distance from vertex \(1\), and \(L_n\) for the graph diameter of the tree induced by \(1,\ldots,n\). There exists an integer-valued finite random variable \(K\ge0\) and an almost-surely finite random \(N\) such that

\[
L_n=H_n+K\qquad(n\ge N).
\]

The random offset has explicit exponential two-sided bounds for all integers \(k\ge2\):

\[
q^{2k}\le\mathbb P(K\ge k)\le\min\left\{1,\frac{2q^k}{1-q}\right\}.
\]

Thus the finite offset has genuinely unbounded support, despite being almost surely finite. Moreover,

\[
\frac{L_n}{n}\longrightarrow\frac{1}{1+q}\quad\text{a.s.},\qquad
\frac{L_n-n/(1+q)}{\sqrt n}\ \Rightarrow\
\mathcal N\!\left(0,\frac{pq}{(1+q)^3}\right).
\]

The same strong law and central limit theorem hold with \(H_n\) in place of \(L_n\).

## Assumptions and scope

The choices of parent are independent at all indices \(j\ge3\), with the same parameter \(p\in(0,1)\). Graph distances and diameters refer to unweighted edges; the root is vertex \(1\). The theorem is **not** a claim about the usual uniform-attachment recursive tree, nor about the infinite graph's diameter (which is infinite). There is no uniformity assertion as \(p\) approaches \(0\) or \(1\).

## Proof

**1. Root heights and neighboring labels.** Set \(h_j=d(1,j)\) and \(h_1=0,h_2=1\). Since the parent of \(j\) is \(j-1\) or \(j-2\),

\[
h_j=1+h_{j-1}\ \text{or}\ h_j=1+h_{j-2}.
\]

Writing \(X_j=h_j-h_{j-1}\), with \(X_2=1\), gives \(X_j=1\) on a one-step attachment and \(X_j=1-X_{j-1}\) on a two-step attachment. By induction \(X_j\in\{0,1\}\), so \(H_n=h_n\) exactly. Let \(D_j=d(j,j-1)\), \(D_2=1\). Its exact recursion is \(D_j=1\) on a one-step attachment and \(D_j=1+D_{j-1}\) on a two-step attachment. Thus \(D_j\) equals one plus the trailing run length of two-step choices. In particular, for integer \(r\ge2\), \(\mathbb P(D_j\ge r)\le q^{r-1}\). A union bound and Borel–Cantelli yield \(D_j=O(\log j)\) almost surely. Meanwhile the ancestry step size is at most two, hence \(h_j\ge\lceil(j-1)/2\rceil\).

**2. Exact ancestor crossing.** Fix \(2\le i<j\). The decreasing-index ancestral path from \(j\) first enters the set of labels at most \(i\) at either \(i\) or \(i-1\). In the first case the lowest common ancestor of \(i,j\) is \(i\); in the second it is the lowest common ancestor of \(i,i-1\). The tree metric therefore gives the **exact alternative**

\[
d(i,j)-h_j\ \in\ \{-h_i,\ D_i-h_{i-1}\}.
\]

Consequently, uniformly over all \(j>i\),

\[
d(i,j)-h_j\le B_i:=\max\{-h_i,D_i-h_{i-1}\}.
\]

The bounds in Step 1 imply \(B_i\to-\infty\) almost surely.

**3. Stabilization of pairwise offsets.** There are almost surely infinitely many one-step attachments. For any fixed \(i\), choose one such attachment at some index \(m>i+1\). Vertices \(m,m-1\) are then parent and child. Every later vertex has an ancestor among \(m,m-1\), hence follows the same side of the earlier cut \(\{i,i-1\}\). It follows that

\[
e_i:=\lim_{j\to\infty}(d(i,j)-h_j)
\]

exists and equals one of the two integers in Step 2. Put \(e_1=0\) and \(K=\max_{i\ge1}e_i\). Because \(e_i\le B_i\to-\infty\), \(K\) is finite, nonnegative, and attained by at least one finite index \(i_*\).

Choose a sufficiently large fixed \(I\) with \(B_i<0\) for all \(i>I\). For every \(i\le I\), the pairwise offset equals \(e_i\le K\) whenever \(j\) is sufficiently large. The finitely many remaining pairs have finite diameter, while \(h_n\to\infty\). Using \(h_j\le h_n\) for all \(j\le n\), this proves \(L_n\le h_n+K\) for all large \(n\). Conversely, for all sufficiently large \(n\), \(d(i_*,n)=h_n+e_{i_*}=h_n+K\), so \(L_n\ge h_n+K\). Equality follows.

**4. Upper tail for the offset.** For \(k\ge2\), neither \(e_1=0\) nor \(e_2\in\{-1,1\}\) can reach \(k\). For \(i\ge3\), the event \(e_i\ge k\) forces \(D_i\ge k+h_{i-1}\ge k+\lceil(i-2)/2\rceil\). The trailing-run bound and a union bound give

\[
\mathbb P(K\ge k)\le
\sum_{i=3}^{\infty}q^{k+\lceil(i-2)/2\rceil-1}
=\frac{2q^k}{1-q}.
\]

**5. Lower tail for the offset.** Require the first \(2k\) choices, at labels \(3,\ldots,2k+2\), all to attach two steps backward; this has probability \(q^{2k}\). The resulting tree contains two disjoint paths emanating from root \(1\), of respective lengths \(k\) and \(k+1\). Since subsequent one-step choices eventually ensure just one infinite ray, one of these two initial arms is finite. Its terminal vertex is at depth at least \(k\), with the root as its lowest common ancestor with all sufficiently late vertices. Therefore \(K\ge k\) on this event. This proves the lower bound.

**6. Diameter fluctuations.** The process \(X_j\) is a two-state irreducible aperiodic Markov chain. In the order \((0,1)\), its transitions are \(0\to1\) surely and \(1\to0\) with probability \(q\), \(1\to1\) with probability \(p\). Its stationary probability of state \(1\) is \(1/(1+q)\). Its nontrivial eigenvalue is \(-q\), and its stationary lag covariance is \(q(1+q)^{-2}(-q)^r\). Summing the covariance series yields the asymptotic variance

\[
\frac{q}{(1+q)^2}\left(1+2\sum_{r=1}^{\infty}(-q)^r\right)=\frac{pq}{(1+q)^3}.
\]

The finite-state ergodic theorem and Markov-chain central limit theorem apply to \(h_n=\sum_{j=2}^nX_j\). The almost-sure eventual identity \(L_n=h_n+K\), with \(K\) finite, transfers both limits to \(L_n\).

## Verification

The accompanying standalone `checker.py` exhaustively enumerates all \(8191\) attachment-choice words of lengths zero through twelve (trees of sizes \(2\) through \(14\)). It verifies monotonic height increments, the neighbor-distance recursion, the two-crossing formula for every ordered vertex pair, and agreement between direct pairwise diameter and a separately implemented postorder-diameter algorithm. It additionally checks \(75\) seeded longer constructions for the finite deterministic upper bound. The code reports \(1,797,528\) successful assertions. These finite calculations are **not** proofs of almost-sure stabilization, tail bounds, or central limits; those follow from Steps 1–6.

Reproduce with `python3 checker.py` using Python 3 without third-party packages.

## Relationship to prior work

Tang, Wang and Wu (arXiv:2607.02916, first publicly available 2026-07-03) introduced the last-or-penultimate Bernoulli attachment tree, proved its one-endedness and infinite random-walk collisions, and investigated branch structure. The present result concerns a different natural metric statistic: eventual *pathwise equality* of diameter and height up to a finite random correction, its nontrivial exponential tail, and an explicit Gaussian fluctuation law. The published one-endedness assertion alone does not imply such metric locking: arbitrary one-ended trees may have arbitrarily long finite branches. The decisive additional input here is the exact adjacent-label distance recursion and its summable tail.

For comparison, Broutin–Flajolet (2012) study height and diameter of uniform non-plane binary trees, and Janson (2021) develops broad tree-limit theory; neither addresses this specific last-two-parent Bernoulli model in the material inspected.

## Limitations

This theorem gives exponential **bounds**, not an exact probability generating function or exact large-\(k\) tail equivalent for \(K\). The motivating 2026 preprint's complete text could not be accessed during the literature comparison; its metadata/abstract and available scientific summary were examined, creating residual priority risk from possible implicit consequences of its branch calculations. The self-review does not constitute independent validation.

## References

1. J.-s. Tang, F. Wang and X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916 (2026), https://arxiv.org/abs/2607.02916.
2. N. Broutin and P. Flajolet, *The distribution of height and diameter in random non-plane binary trees*, Random Structures & Algorithms 41 (2012), 215–252, https://doi.org/10.1002/rsa.20393.
3. S. Janson, *Tree limits and limits of random trees*, Combinatorics, Probability and Computing 30 (2021), 849–893, https://doi.org/10.1017/S0963548321000055.
