# Cyclic-triangle covariance flips exactly at one score standard deviation

## Finding

Let \(T_n\) be the uniform random tournament on \(n\ge3\) labeled vertices: every edge of the complete graph is oriented independently, with the two directions equally likely. For a vertex \(v\), let \(D_v\) be its outdegree, and let \(C_n\) be the number of cyclic directed triangles.

Put
\[
q=n-1.
\]
For any function
\[
\phi:\{0,\ldots,q\}\to\mathbb R,
\]
define the additive score statistic
\[
S_\phi=\sum_v\phi(D_v).
\]
If
\[
B\sim\operatorname{Bin}(q,1/2),
\]
then the mixed covariance with cyclic triangles collapses to one binomial covariance:
\[
\boxed{
\operatorname{Cov}(S_\phi,C_n)
=
-\frac n8\operatorname{Cov}\!\left(\phi(B),(2B-q)^2\right).
}
\tag{1}
\]

Now let
\[
N_k=\#\{v:D_v=k\},
\qquad
0\le k\le q,
\]
and write
\[
p_{q,k}=\binom qk2^{-q},
\qquad
\delta_k=2k-q.
\]
Taking \(\phi=\mathbf 1_{\{k\}}\) in (1) gives
\[
\boxed{
\operatorname{Cov}(N_k,C_n)
=
\frac{n p_{q,k}}8\left(q-\delta_k^2\right).
}
\tag{2}
\]

Because \(D_v\) has mean \(q/2\) and standard deviation \(\sqrt q/2\), equation (2) gives an exact one-standard-deviation sign boundary:
\[
\boxed{
\begin{aligned}
\operatorname{Cov}(N_k,C_n)&>0&&\Longleftrightarrow&&|k-q/2|<\sqrt q/2,\\
\operatorname{Cov}(N_k,C_n)&=0&&\Longleftrightarrow&&|k-q/2|=\sqrt q/2,\\
\operatorname{Cov}(N_k,C_n)&<0&&\Longleftrightarrow&&|k-q/2|>\sqrt q/2.
\end{aligned}}
\tag{3}
\]
The zero case occurs only when the integer lattice meets that boundary.

The two marginal variances are also explicit:
\[
\boxed{
\operatorname{Var}(N_k)
=
n p_{q,k}
\left[
1-p_{q,k}\left(1+\frac{\delta_k^2}{q}\right)
\right]
}
\tag{4}
\]
and
\[
\boxed{
\operatorname{Var}(C_n)
=
\frac{nq(q-1)}{32}.
}
\tag{5}
\]
Consequently
\[
\boxed{
\operatorname{Corr}(N_k,C_n)
=
\frac{(q-\delta_k^2)\sqrt{p_{q,k}}}
{\sqrt{2q(q-1)\left[1-p_{q,k}(1+\delta_k^2/q)\right]}}.
}
\tag{6}
\]

There is a local central-limit profile. If \(k=k_n\) satisfies
\[
\frac{2k_n-(n-1)}{\sqrt{n-1}}\longrightarrow x,
\]
then
\[
\boxed{
n^{1/4}\operatorname{Corr}(N_{k_n},C_n)
\longrightarrow
\frac{(1-x^2)e^{-x^2/4}}{(2\pi)^{1/4}}.
}
\tag{7}
\]
Thus the positive-to-negative transition survives on the natural score-fluctuation scale and occurs exactly at \(|x|=1\).

Equation (1) also gives a monotonicity principle. If \(\phi(k)=h((2k-q)^2)\) with \(h\) nondecreasing, then
\[
\operatorname{Cov}(S_\phi,C_n)\le0,
\]
with strict inequality unless \(h((2B-q)^2)\) is almost surely constant. Cyclic triangles therefore favor score mass near the center and repel additive statistics that reward squared score imbalance.

## Assumptions and scope

The tournament is the standard independent fair orientation of the complete graph. The statistic \(N_k\) counts vertices of one exact outdegree, while \(C_n\) counts all directed 3-cycles.

The result is finite and exact. No Gaussian approximation is used in (1)--(6). The asymptotic profile (7) uses only the local central limit estimate for a fair binomial mass.

The deterministic fact that the number of cyclic triangles is determined by the score sequence is classical. The new statement studied here is the random mixed law between a score class and the cyclic-triangle count, including the exact one-standard-deviation sign transition.

## Proof

Fix a vertex \(v\). Conditional on
\[
D_v=k,
\]
its \(k\) outneighbors form a uniformly chosen \(k\)-subset of the other \(q\) vertices. Orientations among those \(q\) other vertices remain independent fair coins.

A triangle not containing \(v\) is cyclic with probability \(1/4\), so such triangles contribute
\[
\frac14\binom q3
\]
to the conditional mean.

A triangle containing \(v\) can be cyclic only when its two other vertices consist of one outneighbor and one inneighbor of \(v\). There are
\[
k(q-k)
\]
such pairs. For each pair, the edge between those two vertices has exactly one of its two orientations completing a directed 3-cycle. Hence
\[
\mathbb E[C_n\mid D_v=k]
=
\frac14\binom q3+\frac12k(q-k).
\tag{8}
\]
Unconditionally,
\[
\mathbb E C_n=\frac14\binom n3.
\tag{9}
\]
Using
\[
\binom n3-\binom q3=\binom q2
\]
and
\[
4k(q-k)=q^2-(2k-q)^2,
\]
equations (8)--(9) simplify to
\[
\boxed{
\mathbb E[C_n\mid D_v=k]-\mathbb E C_n
=
\frac{q-(2k-q)^2}{8}.
}
\tag{10}
\]

By exchangeability of the vertices,
\[
\operatorname{Cov}(S_\phi,C_n)
=
n\operatorname{Cov}(\phi(D_v),C_n).
\]
Taking conditional expectation with respect to \(D_v\), using (10), and noting that \(D_v\) has the law of \(B\), gives
\[
\operatorname{Cov}(S_\phi,C_n)
=
\frac n8\operatorname{Cov}\!\left(\phi(B),q-(2B-q)^2\right),
\]
which is (1).

For \(\phi=\mathbf 1_{\{k\}}\), the centered square satisfies
\[
\mathbb E(2B-q)^2=q.
\]
Therefore (1) reduces to (2), and (3) is immediate.

To prove (4), write \(I_{v,k}=\mathbf 1\{D_v=k\}\). For distinct vertices \(u,v\), conditioning on the orientation of their common edge gives
\[
\Pr(D_u=k,D_v=k)
=
b_{q-1,k-1}b_{q-1,k},
\]
where
\[
b_{m,r}=\binom mr2^{-m}.
\]
Since
\[
b_{q-1,k-1}=\frac{2k}{q}p_{q,k},
\qquad
b_{q-1,k}=\frac{2(q-k)}q p_{q,k},
\]
we obtain
\[
\Pr(D_u=k,D_v=k)
=
\left(1-\frac{\delta_k^2}{q^2}\right)p_{q,k}^2.
\tag{11}
\]
Summing the diagonal and off-diagonal covariances of the indicators \(I_{v,k}\) yields (4).

For (5), write \(C_n\) as the sum of cyclic-triangle indicators. Each indicator has success probability \(1/4\). Two distinct triangle indicators are independent when their triangles share at most one vertex. If they share one edge, condition on that edge: in each triangle, one of the four orientations of its remaining two edges completes a cycle, and the two remaining edge pairs are disjoint. Their conditional joint probability is therefore \(1/16\), so the indicators are still independent. Thus all distinct cyclic-triangle indicators are pairwise independent, giving
\[
\operatorname{Var}(C_n)
=
\binom n3\frac14\frac34
=
\frac{nq(q-1)}{32}.
\]
Equations (2), (4), and (5) give (6).

Finally, suppose
\[
\delta_{k_n}/\sqrt q\to x.
\]
The fair-binomial local central limit theorem gives
\[
p_{q,k_n}
\sim
\sqrt{\frac{2}{\pi q}}e^{-x^2/2}.
\]
Substituting this into (6), with \(q\sim n\), yields (7).

For the monotonicity principle after (7), apply (1) with \(\phi(B)=h((2B-q)^2)\). The covariance of a nondecreasing function of a real random variable with that variable is nonnegative, so the minus sign in (1) gives the claim.

## Verification

The accompanying checker enumerates every orientation through order \(6\). It computes cyclic triangles directly from triples rather than from the classical score identity.

For every tested order and every score class, it verifies the conditional mean (10), covariance (2), score-class variance (4), cyclic-triangle variance (5), and the exact correlation identity (6).

It separately verifies the master identity (1) for several nontrivial functions of the score and checks the sign rule in (3).

Finite enumeration is supplementary. The theorem for all \(n\) is the conditional-expectation argument above.

## Relationship to prior work

Beineke and Harary give a classical full-text proof that the number of transitive triples in a tournament is
\[
\sum_v\binom{D_v}{2},
\]
and explicitly remark that the number of cyclic triples is therefore determined by the score sequence. That deterministic identity explains why score imbalance is the right quantity, but it does not give a random score-class covariance.

Barbour, Godbole, and Qian study the same standard random-tournament model generated by independent fair orientations, with Poisson approximation for unbeaten subsets. Their paper supplies an archive-era probability setting for random tournaments but does not study score classes or cyclic triangles in its stated results.

Andersson develops asymptotic distribution theory for counts of fixed digraphs in the standard random tournament. Cyclic triangles are within that broad motif-count setting, but a score-class count \(N_k\) is not a fixed-digraph count, and the accessible source does not state the mixed covariance or its sign transition.

A random-tournament paper in the applied-probability literature explicitly classifies tournament probability under primary MSC \(60C05\), supporting the probability ownership of this direction. Later random-orientation work likewise uses primary MSC \(60C05\).

## Limitations

The exact formulas use fair independent edge orientations. A biased tournament changes both the score law and the cyclic-triangle conditional expectation.

The result describes covariance, not independence. A zero covariance at a lattice score exactly one standard deviation from the center does not imply that the score-class count and cyclic-triangle count are independent.

The full text of Andersson's 1998 random-subgraph paper was not accessible in the inspected source, so an older implicit mixed-statistic calculation there or in related tournament-probability literature remains the principal originality risk.

## References

1. A. D. Barbour, A. P. Godbole, and J. Qian, “Imperfections in Random Tournaments,” *Combinatorics, Probability and Computing* 6 (1997), 1–15, DOI 10.1017/S0963548396002829.
2. P. Andersson, “On the asymptotic distributions of subgraph counts in a random tournament,” *Random Structures & Algorithms* 13 (1998), 249–260, DOI 10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V.
3. L. W. Beineke and F. Harary, “The Maximum Number of Strongly Connected Subtournaments,” *Canadian Mathematical Bulletin* 8 (1965), 491–498, DOI 10.4153/CMB-1965-035-x.
4. Y. Itoh, H. Maehara, and N. Tokushige, “Oriented graphs generated by random points on a circle,” *Journal of Applied Probability* 37 (2000), 534–539, DOI 10.1239/jap/1014842556.
