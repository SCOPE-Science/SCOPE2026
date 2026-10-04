# Rigorous decorrelation of part count and maximum in uniform compositions

## Finding

Let \(\Xi_N\) be uniformly distributed over the \(2^{N-1}\) additive compositions of \(N\), with \(N\ge2\). Let
\[
K_N
\]
be its number of parts and
\[
M_N
\]
its largest part.

Put
\[
n=N-1.
\]
Represent the composition by independent fair cut bits
\[
X_1,\ldots,X_n\in\{0,1\},
\]
where a one means that a cut is placed after the corresponding unit. Let
\[
S=\sum_{i=1}^n X_i
\]
and let
\[
L
\]
be the longest consecutive run of zeros in the bit string. Then
\[
\boxed{
(K_N,M_N)\overset d=(1+S,1+L).
}
\tag{1}
\]

The largest part is negatively regressed on the number of parts in a strong sense. For every pair of nondecreasing real functions \(f,g\) for which the covariance exists,
\[
\boxed{
\operatorname{Cov}\!\left(f(K_N),g(M_N)\right)\le0.
}
\tag{2}
\]
If both functions are strictly increasing on their realized supports, the inequality is strict.

There is also an exact coordinate-influence identity. For a bit string \(x\) and a zero coordinate \(i\), let \(x^{(i)}\) be obtained by changing only that zero to one. Then
\[
\boxed{
-\operatorname{Cov}(K_N,M_N)
=
\frac12
\mathbb E
\left[
\sum_{i:X_i=0}
\left(
L(X)-L(X^{(i)})
\right)
\right].
}
\tag{3}
\]

Consequently, if
\[
m=\left\lceil\log_2 n\right\rceil,
\]
then
\[
\boxed{
0<
-\operatorname{Cov}(K_N,M_N)
\le
\frac{m^2+4m+6}{8}.
}
\tag{4}
\]

Since
\[
\operatorname{Var}(K_N)=\frac n4
\]
and the classical variance of the longest fair-coin run stays bounded away from zero, (4) gives
\[
\boxed{
\operatorname{Corr}(K_N,M_N)
=
O\!\left(
\frac{(\log N)^2}{\sqrt N}
\right)
\longrightarrow0^-.
}
\tag{5}
\]

Thus the number of parts and the maximum part are not merely negatively correlated: conditioning on more cuts shifts the entire maximum-part distribution downward. At the same time, their ordinary correlation vanishes at least at the explicit root-\(N\), polylogarithmic rate in (5).

## Assumptions and scope

The composition is uniform over all unrestricted positive-integer compositions of \(N\).

The stochastic order behind (2) concerns the maximum part conditional on the total number of parts. No independence statement is claimed at finite \(N\).

The bound in (4) is universal and elementary, but it is not claimed to have the optimal constant or logarithmic power. Its role is to prove a rigorous quantitative decorrelation rate.

The longest-run variance has small periodic fluctuations rather than a single exact limiting constant. Only its classical uniform positive lower bound for large \(n\) is needed for (5).

## Proof

The cut representation gives (1) immediately. Conditional on
\[
S=s,
\]
the set of one-coordinates is a uniform \(s\)-subset of \([n]\).

Couple a uniform \(s\)-subset to a uniform \((s+1)\)-subset by choosing one of its \(n-s\) zero coordinates uniformly and changing it to one. The resulting \((s+1)\)-subset is uniform because every \((s+1)\)-subset has exactly \(s+1\) predecessors and
\[
\frac{s+1}{\binom ns(n-s)}
=
\frac1{\binom n{s+1}}.
\]
Changing a zero to one cannot increase the longest zero-run length. Hence
\[
L\mid(S=s+1)
\le_{\mathrm{st}}
L\mid(S=s).
\tag{6}
\]
For each \(s<n\), the coupling has positive probability of hitting a zero whose change strictly shortens the unique longest run, so the stochastic decrease is strict.

If \(g\) is nondecreasing, define
\[
h(s)=\mathbb E[g(1+L)\mid S=s].
\]
By (6), \(h\) is nonincreasing. Therefore
\[
\operatorname{Cov}(f(1+S),g(1+L))
=
\operatorname{Cov}(f(1+S),h(S))
\le0.
\]
The usual independent-copy identity for an increasing function and a decreasing function proves the sign, and strictness follows from the strict conditional decrease. This proves (2).

For the coordinate identity, fix \(i\). For a configuration of all coordinates except \(i\), put
\[
\Delta_i
=
L(X_i=0)-L(X_i=1)\ge0.
\]
Because \(X_i\) is fair,
\[
-\operatorname{Cov}(X_i,L)
=
\frac14\mathbb E\Delta_i.
\tag{7}
\]
On the other hand,
\[
\mathbb E
\left[
\mathbf 1_{\{X_i=0\}}
\left(
L(X)-L(X^{(i)})
\right)
\right]
=
\frac12\mathbb E\Delta_i.
\tag{8}
\]
Summing (7)--(8) over \(i\) and using
\[
K_N=1+S,
\qquad
M_N=1+L
\]
gives (3).

It remains to bound the total influence in a fixed string. If there are two or more longest zero runs, changing any single zero leaves another longest run untouched, so every summand in (3) is zero unless the string has a unique longest zero run.

Suppose the unique longest zero run has length \(\ell\). Only its \(\ell\) coordinates can shorten \(L\). Changing the \(j\)-th zero of that run leaves zero subruns of lengths
\[
j-1
\quad\text{and}\quad
\ell-j.
\]
Therefore its decrease is at most
\[
\ell-\max(j-1,\ell-j)
=
\min(j,\ell-j+1).
\]
Summing over the run,
\[
\sum_{i:X_i=0}
\left(
L(X)-L(X^{(i)})
\right)
\le
\left\lfloor\frac{(\ell+1)^2}{4}\right\rfloor.
\tag{9}
\]
Thus
\[
-\operatorname{Cov}(K_N,M_N)
\le
\frac18\mathbb E(L+1)^2.
\tag{10}
\]

For every \(k\ge1\), a union bound over starting positions gives
\[
\Pr(L\ge k)\le n2^{-k}.
\tag{11}
\]
Let
\[
m=\lceil\log_2 n\rceil.
\]
For a nonnegative integer-valued \(L\),
\[
\mathbb E(L+1)^2
=
1+\sum_{k\ge1}(2k+1)\Pr(L\ge k).
\]
Use the trivial bound one for \(k\le m\) and (11) afterwards:
\[
\begin{aligned}
\mathbb E(L+1)^2
&\le
(m+1)^2
+
n\sum_{k=m+1}^{\infty}(2k+1)2^{-k}\\
&=
(m+1)^2
+
n(2m+5)2^{-m}\\
&\le
m^2+4m+6.
\end{aligned}
\tag{12}
\]
Combining (10) and (12) proves the upper bound in (4). Strict positivity follows already from (2), or directly from the positive-probability all-zero configuration in (3).

Finally,
\[
S\sim\operatorname{Bin}(n,1/2),
\qquad
\operatorname{Var}(K_N)=\frac n4.
\]
Classical longest-run asymptotics give
\[
\operatorname{Var}(L)
=
\frac{\pi^2}{6\log^2 2}
+
\frac1{12}
+
\text{a uniformly tiny periodic term}
+
o(1),
\tag{13}
\]
so \(\operatorname{Var}(L)\) is bounded below by a positive constant for all sufficiently large \(n\). Equations (4) and (13) then imply (5).

## Verification

The accompanying checker exhaustively enumerates every fair bit string through length \(16\).

For each length it reconstructs the covariance, verifies the coordinate-influence identity (3) exactly, checks the explicit bound (4), and verifies strict first-order stochastic decrease of the longest zero-run distribution as the number of ones increases.

The replay covers \(131070\) bit strings and \(136\) adjacent conditional stochastic-order comparisons.

Finite enumeration is supplementary. The all-\(N\) result follows from the uniform-subset coupling, the exact influence decomposition, and the longest-run tail bound above.

## Relationship to prior work

Philippou and Makri derived an exact formula for the conditional distribution of the longest success run given the total number of successes in Bernoulli trials. This is a strong exact predecessor for the conditional object in (6). Their inspected paper does not state the subset coupling, the coordinate-influence identity (3), or a covariance/correlation decay bound.

Schilling's treatment of the longest run of heads gives the classical logarithmic scale and the asymptotic variance formula used in (13). That marginal theory does not address covariance with the total number of successes.

Finch studies exactly the number of parts and maximum part of a uniform random composition. His full public text converts the problem to the number of ones and the longest zero run of a fair bit string, computes mixed moments recursively, reports negative numerical correlations, and explicitly calls for a rigorous proof that the correlation tends to zero. Equations (2)--(5) supply such a proof and give a quantitative rate.

The probability classification \(60C05\) is independently supported by archive literature on probabilistic geometric-sample and composition statistics.

## Limitations

The explicit quantitative bound is an upper bound; no matching lower asymptotic for the covariance is claimed.

The proof uses the uniform composition model, equivalently fair independent cut bits. A biased-cut composition model still has coordinate monotonicity, but conditioning on the number of cuts and the quantitative constants require separate treatment.

The 1986 conditional-distribution formula is strong prior art. The originality claim is therefore not the existence of a joint law, but the monotone coupling, influence representation, and rigorous asymptotic decorrelation bound for the composition problem highlighted later.

## References

1. A. N. Philippou and F. S. Makri, “Successes, runs and longest runs,” *Statistics & Probability Letters* 4 (1986), 101–105, DOI 10.1016/0167-7152(86)90025-8; corrected reprint in issue 4, 211–215.
2. M. F. Schilling, “The Longest Run of Heads,” *The College Mathematics Journal* 21 (1990), 196–207, DOI 10.1080/07468342.1990.11973306.
3. M. Archibald and A. Knopfmacher, “The Largest Missing Value in a Sample of Geometric Random Variables,” *Combinatorics, Probability and Computing* 23 (2014), 670–685, DOI 10.1017/S096354831400011X.
4. S. Finch, “Covariance within Random Integer Compositions,” arXiv:2010.06643, first submitted 2020-10-13.
