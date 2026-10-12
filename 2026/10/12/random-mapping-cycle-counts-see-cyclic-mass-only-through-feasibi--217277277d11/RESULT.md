# Random-mapping cycle counts see cyclic mass only through feasibility thresholds

## Finding

Let \(T_n\) be uniformly distributed over all \(n^n\) mappings from \([n]\) to itself, with \(n\ge2\). Let
\[
L_n
\]
be the number of cyclic vertices in its functional digraph, and for \(1\le \ell\le n\) let
\[
A_{n,\ell}
\]
be the number of directed cycles having length \(\ell\).

For a nonnegative integer \(x\), write
\[
(x)_r=x(x-1)\cdots(x-r+1).
\]
Then for every \(r\ge1\) with \(r\ell\le n\),
\[
\boxed{
\mathbb E\!\left[(A_{n,\ell})_r\mid L_n\right]
=
\ell^{-r}\mathbf 1\{L_n\ge r\ell\}.
}
\tag{1}
\]

Consequently, for every measurable \(h\) for which the expectations exist,
\[
\boxed{
\operatorname{Cov}\!\left((A_{n,\ell})_r,h(L_n)\right)
=
\ell^{-r}
\operatorname{Cov}\!\left(\mathbf 1\{L_n\ge r\ell\},h(L_n)\right).
}
\tag{2}
\]

Thus every nondecreasing \(h\) gives a nonnegative covariance. If \(h\) is strictly increasing on the support of \(L_n\), the covariance in (2) is strictly positive whenever
\[
r\ell\ge2.
\]
The sole first-order exception is a single fixed point.

Put
\[
q_{n,s}=\frac{(n)_s}{n^s}.
\]
Then
\[
\Pr(L_n\ge s)=q_{n,s},
\tag{3}
\]
and therefore
\[
\boxed{
\mathbb E[(A_{n,\ell})_r]
=
\ell^{-r}q_{n,r\ell}.
}
\tag{4}
\]

For fixed \(s=r\ell\ge2\),
\[
\boxed{
\operatorname{Cov}\!\left((A_{n,\ell})_r,L_n\right)
\sim
\frac{s(s-1)}{2\ell^r}
\sqrt{\frac{\pi}{2n}}.
}
\tag{5}
\]

The case \(\ell=r=1\) is qualitatively different. Let
\[
F_n=A_{n,1}
\]
be the number of fixed points. Then
\[
\boxed{
\mathbb E[F_n\mid L_n]=1,
\qquad
\operatorname{Cov}(F_n,h(L_n))=0
}
\tag{6}
\]
for every integrable \(h\). In fact, for each fixed label \(i\), the indicator
\[
I_i=\mathbf 1\{T_n(i)=i\}
\]
is independent of \(L_n\).

This orthogonality is not independence of the counts. For \(n\ge2\), conditioning on \(L_n=1\) forces \(F_n=1\), whereas unconditionally \(F_n\) is binomial with parameters \(n\) and \(1/n\). The first hidden dependence appears at factorial order two:
\[
\boxed{
\operatorname{Cov}(F_n^2,L_n)
=
\frac{\mathbb E L_n-1}{n}
\sim
\sqrt{\frac{\pi}{2n}}.
}
\tag{7}
\]

## Assumptions and scope

A cyclic vertex is a vertex lying on a directed cycle of the functional digraph. A directed loop is a cycle of length one, so fixed points are precisely the one-cycles.

The theorem concerns the classical uniform random mapping. It is not asserted for nonuniform \(p\)-mappings or for random mappings whose cyclic permutation follows a nonuniform law.

Equation (1) describes falling-factorial moments, not ordinary powers. Ordinary mixed moments follow by the usual Stirling-number conversion.

## Proof

Condition on
\[
L_n=m.
\]
For any specified set \(C\subseteq[n]\) of \(m\) cyclic vertices and any specified permutation \(\sigma\) of \(C\), the noncyclic vertices form a directed forest rooted at \(C\). The number of such rooted forests is
\[
m n^{n-m-1}
\]
when \(m<n\), with the same formula interpreted as one when \(m=n\). This number is independent of both \(C\) and \(\sigma\).

Hence, conditional on \(L_n=m\), the cyclic set is a uniform \(m\)-subset of \([n]\), and conditional on that set, the restriction of \(T_n\) to the cyclic vertices is a uniform random permutation. This is also the standard decomposition used in the cited random-mapping literature.

Now fix \(\ell\) and \(r\). In a uniform permutation of \(m\) elements, the number of ordered \(r\)-tuples of pairwise distinct \(\ell\)-cycles is
\[
\frac{(m)_{r\ell}}{\ell^r}.
\]
For any specified such ordered collection, the probability that all of those cycles occur is
\[
\frac{(m-r\ell)!}{m!}
=
\frac1{(m)_{r\ell}}.
\]
Therefore
\[
\mathbb E[(A_{n,\ell})_r\mid L_n=m]
=
\begin{cases}
\ell^{-r},&m\ge r\ell,\\
0,&m<r\ell,
\end{cases}
\]
which proves (1). Multiplying by \(h(L_n)\), taking expectations, and subtracting the product of the marginals proves (2).

For any real random variable \(Y\), increasing functions of \(Y\) are nonnegatively correlated. Applying this to
\[
\mathbf 1\{L_n\ge r\ell\}
\]
and a nondecreasing \(h(L_n)\) proves the sign statement. When \(r\ell\ge2\), both sides of the threshold have positive probability, so strict increase of \(h\) makes the covariance strictly positive.

To obtain the tail law, the number of mappings with exactly \(m\) cyclic vertices is
\[
\binom nm m!\,m n^{n-m-1}
=
(n)_m m n^{n-m-1}.
\]
Thus
\[
\Pr(L_n=m)
=
\frac{m(n)_m}{n^{m+1}}.
\tag{8}
\]
Since
\[
q_{n,m}-q_{n,m+1}
=
\frac{m(n)_m}{n^{m+1}},
\]
(8) telescopes to (3). Averaging (1) now gives (4).

For fixed \(s\ge2\), (2) with \(h(x)=x\) gives
\[
\operatorname{Cov}(\mathbf 1\{L_n\ge s\},L_n)
=
(1-q_{n,s})\mathbb E L_n
-
\mathbb E[L_n;L_n<s].
\tag{9}
\]
For fixed \(s\),
\[
1-q_{n,s}
=
\frac{s(s-1)}{2n}+O(n^{-2}),
\qquad
\mathbb E[L_n;L_n<s]=O(n^{-1}).
\tag{10}
\]
Also, from
\[
\mathbb E L_n=\sum_{k=1}^n q_{n,k}
\]
and the standard Gaussian-scale estimate for \(q_{n,k}\),
\[
\frac{\mathbb E L_n}{\sqrt n}
\longrightarrow
\int_0^\infty e^{-x^2/2}\,dx
=
\sqrt{\frac\pi2}.
\tag{11}
\]
Substituting (10)--(11) into (9) and multiplying by \(\ell^{-r}\) proves (5).

For fixed points, (1) at \(\ell=r=1\) gives
\[
\mathbb E[F_n\mid L_n]=1
\]
because \(L_n\ge1\) always. This proves (6). More locally, conditional on \(L_n=m\), a fixed label \(i\) belongs to the cyclic set with probability \(m/n\); given that it is cyclic, it is fixed by the uniform cyclic permutation with probability \(1/m\). Hence
\[
\Pr(I_i=1\mid L_n=m)=\frac1n,
\]
independent of \(m\), so \(I_i\) and \(L_n\) are independent.

Finally,
\[
F_n^2=(F_n)_2+F_n.
\]
The linear covariance vanishes, while (1) at \(\ell=1,r=2\) gives
\[
\mathbb E[(F_n)_2\mid L_n]=\mathbf 1\{L_n\ge2\}.
\]
Since (8) gives
\[
\Pr(L_n=1)=\frac1n,
\]
we obtain
\[
\operatorname{Cov}(F_n^2,L_n)
=
\operatorname{Cov}(\mathbf 1\{L_n\ge2\},L_n)
=
\frac{\mathbb E L_n-1}{n},
\]
and (11) yields the asymptotic form in (7).

## Verification

The accompanying checker exhaustively enumerates every mapping on \([n]\) for \(2\le n\le6\), a total of \(50068\) functional digraphs.

For each mapping it reconstructs the cyclic vertices and every directed cycle length directly. It checks the exact distribution of \(L_n\), every admissible conditional factorial moment in (1), the covariance identity (2) for several test functions, the independence of a specified fixed-point indicator from \(L_n\), the zero covariance in (6), and the exact second-moment covariance (7).

The finite replay is supplementary. The all-\(n\) result is proved by the conditional uniform-permutation decomposition and elementary cycle counting.

## Relationship to prior work

Hansen and Jaworski explicitly state the key classical decomposition: conditional on the number of cyclic vertices, the cyclic set is uniform and the mapping restricted to it is a uniform random permutation. Their paper then studies the size of a typical connected component under that conditioning. The inspected full article does not formulate fixed-point independence, cycle-length factorial moments against the total cyclic count, or the threshold covariance identity (2).

Aldous, Miermont, and Pitman treat random \(p\)-mappings and identify random mappings and cyclic-point counts as objects of combinatorial probability; their arXiv version lists MSC \(60C05\). Their work is asymptotic and does not state the finite threshold law here.

English derives factorial moments for the number of components and the number of cyclic elements of random mappings. That is close in method and terminology, but the accessible statement concerns aggregate components and cyclic elements rather than counts of cycles of a fixed length jointly with \(L_n\).

Arratia and Tavaré give broad independent-process approximations for cycle and component structures of random combinatorial objects. This is the principal broader-coverage risk because such machinery can recover many small-cycle asymptotics. The accepted claim is finite and exact, and its fixed-point independence phenomenon is not implied by an asymptotic Poisson approximation alone.

## Limitations

The conditional permutation structure is classical. The claimed contribution is the exact reduction of all factorial mixed moments to a single feasibility threshold, together with the exceptional fixed-point orthogonality and its first nonlinear correction.

Older monographs and generating-function treatments of random mappings may encode equivalent joint identities implicitly. In particular, Kolchin's monograph and early cycle-count literature remain residual originality risks.

The result does not assert independence of the full fixed-point count and the cyclic-point count. It proves the opposite: first-order mean independence coexists with nontrivial higher-order dependence.

## References

1. D. J. Aldous, G. Miermont, and J. Pitman, “Weak convergence of random \(p\)-mappings and the exploration process of inhomogeneous continuum random trees,” arXiv:math/0401115, first submitted 2004-01-12; MSC \(60C05,60F17\).
2. J. C. Hansen and J. Jaworski, “Random mappings with a given number of cyclical points,” *Ars Combinatoria* 94 (2010), 341–359. The open full text states that, conditional on the cyclic set, the restriction of a uniform random mapping to its cyclic vertices is a uniformly distributed random permutation.
3. B. J. English, “Factorial moments for random mappings by means of indicator variables,” *Journal of Applied Probability* 30 (1993), 167–174.
4. R. Arratia and S. Tavaré, “Limit theorems for combinatorial structures via discrete process approximations,” *Random Structures & Algorithms* 3 (1992), 321–345.
