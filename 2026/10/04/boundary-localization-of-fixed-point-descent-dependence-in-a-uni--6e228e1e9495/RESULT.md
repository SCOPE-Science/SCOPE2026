# Boundary localization of fixed-point–descent dependence in a uniform permutation

## Finding

Let \(\Pi\) be uniformly distributed on \(S_n\), with \(n\ge2\). Define the fixed-point indicators
\[
I_i=\mathbf 1\{\Pi(i)=i\},
\qquad
1\le i\le n,
\]
and the ordinary descent indicators
\[
D_j=\mathbf 1\{\Pi(j)>\Pi(j+1)\},
\qquad
1\le j\le n-1.
\]

The entire cross-covariance matrix is sparse and explicit:
\[
\boxed{
\operatorname{Cov}(I_i,D_j)=0
\quad\text{if }i\notin\{j,j+1\},
}
\tag{1}
\]
while
\[
\boxed{
\operatorname{Cov}(I_j,D_j)
=
\frac{2j-n-1}{2n(n-1)}
}
\tag{2}
\]
and
\[
\boxed{
\operatorname{Cov}(I_{j+1},D_j)
=
\frac{n-2j-1}{2n(n-1)}.
}
\tag{3}
\]

Thus each descent coordinate receives the same total covariance from the whole fixed-point count
\[
F=\sum_{i=1}^n I_i:
\]
\[
\boxed{
\operatorname{Cov}(F,D_j)
=
-\frac1{n(n-1)},
\qquad
1\le j\le n-1.
}
\tag{4}
\]

In the opposite summation direction, all interior fixed points cancel exactly:
\[
\boxed{
\operatorname{Cov}(I_i,D)
=
\begin{cases}
-\dfrac1{2n},&i\in\{1,n\},\\[4pt]
0,&1<i<n,
\end{cases}
}
\tag{5}
\]
where
\[
D=\sum_{j=1}^{n-1}D_j.
\]
Consequently,
\[
\boxed{
\operatorname{Cov}(F,D)
=
-\frac1n.
}
\tag{6}
\]

The boundary interpretation becomes exact after cyclic closure. Define
\[
D_n^\circ
=
\mathbf 1\{\Pi(n)>\Pi(1)\}
\]
and the cyclic descent count
\[
C
=
\sum_{j=1}^{n-1}D_j+D_n^\circ.
\]
Then
\[
\boxed{
\operatorname{Cov}(I_i,C)=0
\quad\text{for every }1\le i\le n,
}
\tag{7}
\]
and therefore
\[
\boxed{
\operatorname{Cov}(F,C)=0.
}
\tag{8}
\]

For the ordinary descent count,
\[
\operatorname{Var}(F)=1,
\qquad
\operatorname{Var}(D)=\frac{n+1}{12},
\]
so
\[
\boxed{
\operatorname{Corr}(F,D)
=
-\frac{\sqrt{12}}{n\sqrt{n+1}}
\sim
-\sqrt{12}\,n^{-3/2}.
}
\tag{9}
\]

The negative fixed-point/descent covariance is therefore entirely an open-boundary effect: the two endpoint fixed-point coordinates contribute
\[
-\frac1{2n}
\]
each, every interior fixed-point coordinate has zero covariance with the total ordinary descent count, and the wrap-around descent restores exact orthogonality.

## Assumptions and scope

The permutation is uniform on the full symmetric group.

A fixed point is positional: \(I_i=1\) means \(\Pi(i)=i\). An ordinary descent compares positions \(j\) and \(j+1\). The cyclic descent count adds the single wrap comparison between positions \(n\) and \(1\).

Equations (1)--(3) are coordinate-level statements. They are strictly finer than a joint law that tracks only the total number of fixed points and the descent set, because the location of each fixed point has been retained.

The zero covariances in (5), (7), and (8) are not independence claims.

## Proof

For a uniform permutation,
\[
\Pr(I_i=1)=\frac1n,
\qquad
\Pr(D_j=1)=\frac12.
\tag{10}
\]

Condition on
\[
I_i=1.
\]
After fixing \(\Pi(i)=i\), the remaining values are uniformly permuted over the remaining positions.

If
\[
i\notin\{j,j+1\},
\]
then the two random values \(\Pi(j)\) and \(\Pi(j+1)\) are exchangeable under the conditioning. Hence
\[
\Pr(D_j=1\mid I_i=1)=\frac12,
\]
which proves (1).

If
\[
i=j,
\]
then
\[
\Pi(j)=j,
\]
and \(\Pi(j+1)\) is uniform on
\[
[n]\setminus\{j\}.
\]
Therefore
\[
\Pr(D_j=1\mid I_j=1)
=
\Pr(\Pi(j+1)<j\mid I_j=1)
=
\frac{j-1}{n-1}.
\tag{11}
\]
Using
\[
\operatorname{Cov}(I_j,D_j)
=
\Pr(I_j=1)
\left(
\Pr(D_j=1\mid I_j=1)-\frac12
\right)
\]
gives (2).

If
\[
i=j+1,
\]
then
\[
\Pi(j+1)=j+1,
\]
and \(\Pi(j)\) is uniform on
\[
[n]\setminus\{j+1\}.
\]
Thus
\[
\Pr(D_j=1\mid I_{j+1}=1)
=
\Pr(\Pi(j)>j+1\mid I_{j+1}=1)
=
\frac{n-j-1}{n-1}.
\tag{12}
\]
This gives (3).

Adding (2) and (3),
\[
\operatorname{Cov}(F,D_j)
=
\frac{2j-n-1+n-2j-1}{2n(n-1)}
=
-\frac1{n(n-1)},
\]
proving (4).

Now fix an index \(i\). If
\[
1<i<n,
\]
only \(D_{i-1}\) and \(D_i\) can have nonzero covariance with \(I_i\). Equations (2)--(3) give
\[
\operatorname{Cov}(I_i,D_{i-1})
=
\frac{n-2i+1}{2n(n-1)}
\]
and
\[
\operatorname{Cov}(I_i,D_i)
=
\frac{2i-n-1}{2n(n-1)}.
\]
They sum to zero. At the two endpoints there is only one ordinary adjacent descent:
\[
\operatorname{Cov}(I_1,D_1)
=
-\frac1{2n},
\qquad
\operatorname{Cov}(I_n,D_{n-1})
=
-\frac1{2n}.
\]
This proves (5), and summing (5) proves (6).

For the wrap indicator,
\[
D_n^\circ=\mathbf 1\{\Pi(n)>\Pi(1)\}.
\]
If
\[
1<i<n,
\]
conditioning on \(I_i=1\) leaves the two wrap values exchangeable, so
\[
\operatorname{Cov}(I_i,D_n^\circ)=0.
\]
If \(i=1\), then \(\Pi(1)=1\) and necessarily
\[
\Pi(n)>1,
\]
so
\[
\Pr(D_n^\circ=1\mid I_1=1)=1
\]
and
\[
\operatorname{Cov}(I_1,D_n^\circ)=\frac1{2n}.
\]
Similarly,
\[
\operatorname{Cov}(I_n,D_n^\circ)=\frac1{2n}.
\]
These two wrap contributions cancel the endpoint terms in (5), proving (7)--(8).

Finally, for \(n\ge2\), the fixed-point count satisfies
\[
\mathbb EF=1,
\qquad
\operatorname{Var}(F)=1.
\]
The standard descent-indicator calculation gives
\[
\operatorname{Var}(D)=\frac{n+1}{12}.
\]
Combining these identities with (6) proves (9).

## Verification

The accompanying checker exhaustively enumerates every permutation for
\[
2\le n\le9.
\]

It reconstructs every coordinate covariance in (1)--(3), every row sum in (5), every column sum in (4), the cyclic cancellations in (7)--(8), and the marginal variance identities used in (9).

The exhaustive replay covers
\[
409112
\]
permutations in total.

Finite enumeration is supplementary. The universal theorem follows from the conditional symmetry and one-point conditioning calculations in the proof.

## Relationship to prior work

Diaconis, Evans, and Graham study fixed points as a random subset of positions in a uniform permutation and prove a distributional equivalence with unseparated adjacent-value pairs. Their paper gives a probability-theoretic treatment of the fixed-point random set and has primary classification \(60C05\). It does not study descent indicators or the fixed-point/descent cross-covariance matrix.

Désarménien and Wachs study descent classes with a given total number of fixed points. Their Theorem 5.1 tracks exact descent classes together with the number of fixed points, so it is stronger than needed for many aggregate fixed-point/descent questions. However, it collapses the locations of the fixed points and therefore does not state the coordinate law (1)--(3), the endpoint cancellation (5), or the coordinatewise cyclic orthogonality (7).

Eriksen, Freij, and Wästlund enumerate derangements with descents in prescribed positions and prove positive correlation between being a derangement and specified descent events. Their framework again concerns global fixed-point restrictions or counts rather than the location-resolved covariance matrix here.

The global formula (6) should be viewed as a consequence of the new local decomposition, not as a claim that global fixed-point/descent dependence was absent from the older enumerative literature.

## Limitations

The argument uses uniformity of the permutation. Biasing by inversions, cycles, or fixed points generally destroys the simple conditional exchangeability used in (1).

The local matrix concerns fixed-point positions versus descent positions. It does not determine higher mixed moments or the full joint law of these indicator families.

Older refined descent enumerations may contain an equivalent position-resolved identity under a different encoding. The strongest inspected classical result tracks the total number of fixed points rather than their positions, so this remains the principal originality risk.

## References

1. P. Diaconis, S. N. Evans, and R. Graham, “Unseparated pairs and fixed points in random permutations,” arXiv:1308.5459, first submitted 2013-08-25; later *Advances in Applied Mathematics* 61 (2014), 102–124.
2. J. Désarménien and M. L. Wachs, “Descent Classes of Permutations with a Given Number of Fixed Points,” *Journal of Combinatorial Theory, Series A* 64 (1993), 311–328, DOI 10.1016/0097-3165(93)90100-M.
3. N. Eriksen, R. Freij, and J. Wästlund, “Enumeration of derangements with descents in prescribed positions,” arXiv:0811.1925, first submitted 2008-11-12; *Electronic Journal of Combinatorics* 16 (2009), R32.
