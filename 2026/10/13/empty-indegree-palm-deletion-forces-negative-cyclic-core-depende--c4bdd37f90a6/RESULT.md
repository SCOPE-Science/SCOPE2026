# Empty-indegree Palm deletion forces negative cyclic-core dependence

## Finding

Let
\[
T_n:[n]\to[n]
\]
be a uniformly random mapping, with \(n\ge2\). In its functional digraph let
\[
Z_n=\#\{v:\deg^-(v)=0\}
\]
be the number of vertices of indegree zero, and let
\[
L_n
\]
be the number of cyclic vertices.

For every measurable function \(f\) for which the expectations exist,
\[
\boxed{
\frac{\mathbb E[Z_nf(L_n)]}{\mathbb E Z_n}
=
\mathbb E f(L_{n-1}).
}
\tag{1}
\]
Moreover,
\[
\boxed{
\mathbb E Z_n
=
n\left(1-\frac1n\right)^n.
}
\tag{2}
\]

Thus size-biasing a uniform random mapping by its number of zero-indegree vertices and then observing only its cyclic core has exactly the same law as passing from size \(n\) to size \(n-1\).

For integers \(m\ge1\) and \(k\ge1\), define
\[
q_{m,k}
=
\begin{cases}
\dfrac{(m)_k}{m^k},&1\le k\le m,\\[6pt]
0,&k>m,
\end{cases}
\]
where
\[
(m)_k=m(m-1)\cdots(m-k+1).
\]
Then
\[
\boxed{
\Pr(L_m\ge k)=q_{m,k}.
}
\tag{3}
\]

Consequently, for every
\[
2\le k\le n,
\]
\[
\boxed{
\operatorname{Cov}\!\left(
Z_n,\mathbf 1_{\{L_n\ge k\}}
\right)
=
n\left(1-\frac1n\right)^n
\left(q_{n-1,k}-q_{n,k}\right)
<0.
}
\tag{4}
\]

Since \(q_{m,k}\) is strictly increasing in \(m\) for every fixed \(k\ge2\), \(L_n\) strictly stochastically dominates \(L_{n-1}\). Equation (1) therefore yields
\[
\boxed{
\operatorname{Cov}(Z_n,f(L_n))\le0
}
\tag{5}
\]
for every nondecreasing \(f\), with strict inequality whenever \(f\) is strictly increasing on
\[
\{1,\ldots,n\}.
\]

In particular, if
\[
\ell_m=\mathbb E L_m
=
\sum_{k=1}^m\frac{(m)_k}{m^k},
\tag{6}
\]
then
\[
\boxed{
\operatorname{Cov}(Z_n,L_n)
=
n\left(1-\frac1n\right)^n
(\ell_{n-1}-\ell_n)
<0.
}
\tag{7}
\]

The conclusion is an exact finite-size negative dependence law between a local fringe statistic and the size of the cyclic core.

## Assumptions and scope

A uniform random mapping means that the \(n\) images
\[
T_n(1),\ldots,T_n(n)
\]
are independent and uniform on \([n]\).

A vertex is cyclic when it lies on a directed cycle of the functional digraph. A zero-indegree vertex is never cyclic.

Equation (1) is a size-biased or Palm identity for the zero-indegree count. It concerns statistics of the cyclic core; it does not assert negative association between the entire indegree sequence and all global mapping statistics.

## Proof

For each vertex \(j\), put
\[
I_j=\mathbf 1\{\deg^-(j)=0\}.
\]
Then
\[
Z_n=\sum_{j=1}^n I_j.
\]

For a fixed \(j\),
\[
\Pr(I_j=1)
=
\left(1-\frac1n\right)^n,
\tag{8}
\]
because every one of the \(n\) independent images must avoid \(j\). Summing (8) proves (2).

Condition on
\[
I_j=1.
\]
Then no vertex maps to \(j\). In particular, \(j\) is not cyclic. On the remaining vertex set
\[
[n]\setminus\{j\},
\]
the restrictions
\[
T_n(v),\qquad v\ne j,
\]
are still independent and are each uniform on \([n]\setminus\{j\}\). Hence, after relabelling, the restriction is exactly a uniform random mapping on \(n-1\) vertices. Its cyclic vertices are precisely the cyclic vertices of the original mapping. Therefore
\[
L_n\mid(I_j=1)
\overset d=
L_{n-1}.
\tag{9}
\]

It follows that
\[
\begin{aligned}
\mathbb E[Z_nf(L_n)]
&=
\sum_{j=1}^n
\mathbb E[I_jf(L_n)]\\
&=
n\left(1-\frac1n\right)^n
\mathbb E f(L_{n-1}),
\end{aligned}
\]
which proves (1).

It remains to compare the cyclic-point laws. The number of mappings on \(m\) labeled vertices having exactly \(k\) cyclic vertices is
\[
k(m)_k m^{m-k-1}.
\tag{10}
\]
Indeed, choose the \(k\) cyclic labels and a permutation on them. The remaining vertices form a rooted forest directed toward those \(k\) roots. For a fixed root set of size \(k\), the number of such forests is
\[
k m^{m-k-1}.
\]
One way to verify this forest count is the all-minors matrix-tree theorem: the relevant minor is
\[
mI_{m-k}-J_{m-k},
\]
whose eigenvalues are \(m\), with multiplicity \(m-k-1\), and \(k\), with multiplicity one.

Dividing (10) by \(m^m\),
\[
\Pr(L_m=k)
=
\frac{k(m)_k}{m^{k+1}}.
\tag{11}
\]
But
\[
\frac{(m)_k}{m^k}
-
\frac{(m)_{k+1}}{m^{k+1}}
=
\frac{k(m)_k}{m^{k+1}}.
\]
Telescoping (11) proves (3).

For fixed \(k\ge2\),
\[
q_{m,k}
=
\prod_{r=0}^{k-1}
\left(1-\frac r m\right)
\]
is strictly increasing in \(m\). Thus
\[
q_{n-1,k}<q_{n,k},
\]
which proves the strict sign in (4) after applying (1) to the threshold indicator.

The tail inequalities in (3) show that \(L_n\) strictly stochastically dominates \(L_{n-1}\). Hence
\[
\mathbb E f(L_{n-1})
\le
\mathbb E f(L_n)
\]
for every nondecreasing \(f\), and the inequality is strict for strictly increasing \(f\). Substitution into the covariance form of (1) proves (5).

Finally,
\[
\mathbb E L_m
=
\sum_{k\ge1}\Pr(L_m\ge k)
=
\sum_{k=1}^m q_{m,k},
\]
which is (6). Taking
\[
f(x)=x
\]
in (1) proves (7).

## Verification

The accompanying checker exhaustively enumerates all mappings
\[
[n]\to[n]
\]
for
\[
1\le n\le7.
\]

For each mapping it computes the indegree sequence, deletes no vertices, and independently identifies cyclic vertices by functional-orbit tracing. It verifies the exact cyclic-point distribution, all tail probabilities in (3), the mean zero-indegree count, the full point-mass Palm identity in (1), every threshold covariance in (4), and the covariance formula (7).

The exhaustive replay covers
\[
873612
\]
mappings.

The finite replay is supplementary. The all-\(n\) proof is the conditional deletion argument and the exact rooted-forest count above.

## Relationship to prior work

Hansen and Jaworski develop a general random-mapping model parameterized by an exchangeable indegree sequence. Their full article treats the distribution of cyclic points and uses an explicit coding algorithm that repeatedly deletes zero-indegree vertices. It also discusses expected numbers of zero-indegree vertices in constrained mapping models. The inspected article does not state the mixed Palm identity (1), the threshold covariances (4), or the monotone-transform negative dependence (5).

The companion paper on local properties of mappings with exchangeable indegrees is classified primarily under combinatorial probability and studies local quantities such as predecessor and successor counts. Its stated scope is local-distribution theory rather than the exact zero-indegree-count/cyclic-core dependence law here.

Drmota studies correlations between strata measured by directed distance from the cyclic set. Those strata are different from the indegree-zero fringe: an indegree-zero vertex can occur at any positive distance from the core. The accessible abstract therefore does not imply the accepted identity.

Classical random-mapping monographs and papers give the cyclic-point distribution used in (3). The new content is the exact Palm link from the zero-indegree count to a one-vertex size reduction and the resulting all-monotone negative dependence.

## Limitations

The argument uses the fully uniform mapping law. In general exchangeable-indegree mapping models, conditioning one vertex to have indegree zero need not leave the same model at size \(n-1\).

The theorem concerns the number of cyclic vertices and its transforms. It does not prove negative association between all leaf-like and core-like statistics.

The cyclic-point distribution is classical. Originality is claimed only for the explicit zero-indegree Palm deletion identity and its mixed dependence consequences.

Older local-structure literature on random mappings is extensive, so an equivalent mixed identity could exist in different notation; this remains a residual originality risk.

## References

1. J. C. Hansen and J. Jaworski, “Random Mappings With Exchangeable In-Degrees,” *Random Structures & Algorithms* 33 (2008), 105–126, DOI 10.1002/rsa.20187; first published online 2007-09-04.
2. J. C. Hansen and J. Jaworski, “Local properties of random mappings with exchangeable in-degrees,” *Advances in Applied Probability* 40 (2008), 183–205, DOI 10.1239/aap/1208358892.
3. M. Drmota, “Correlations on the strata of a random mapping,” *Random Structures & Algorithms* 6 (1995), 357–365, DOI 10.1002/rsa.3240060223.
4. V. F. Kolchin, *Random Mappings*, Optimization Software, 1986.
