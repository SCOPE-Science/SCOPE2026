# A marked simple chord gives an exact crossing Palm law

## Finding

Let \(\mathcal C_n\) be a uniformly random chord diagram with \(n\ge2\) chords: equivalently, a uniformly random perfect matching of \(2n\) points placed in cyclic order.

Let
\[
S_n
\]
be the number of **simple chords**, meaning matched pairs of consecutive cyclic endpoints, and let
\[
X_n
\]
be the total number of crossing pairs of chords.

For every measurable function \(f\) for which the expectations below exist,
\[
\boxed{
\frac{\mathbb E[S_nf(X_n)]}{\mathbb E S_n}
=
\mathbb E f(X_{n-1}).
}
\tag{1}
\]
Here \(X_{n-1}\) is the crossing count in an independent uniformly random chord diagram with \(n-1\) chords.

Since
\[
\mathbb E S_n=\frac{2n}{2n-1},
\tag{2}
\]
equation (1) is equivalently
\[
\boxed{
\operatorname{Cov}(S_n,f(X_n))
=
\frac{2n}{2n-1}
\left(
\mathbb E f(X_{n-1})-\mathbb E f(X_n)
\right).
}
\tag{3}
\]

There is a natural coupling satisfying
\[
X_{n-1}\le X_n
\qquad\text{almost surely}.
\tag{4}
\]
Consequently, every nondecreasing \(f\) satisfies
\[
\boxed{
\operatorname{Cov}(S_n,f(X_n))\le0.
}
\tag{5}
\]
If \(f\) is strictly increasing on the support of the crossing count, then the inequality is strict.

Taking
\[
f(x)=x
\]
and using
\[
\mathbb E X_n=\frac{n(n-1)}6
\]
gives the exact covariance
\[
\boxed{
\operatorname{Cov}(S_n,X_n)
=
-\frac{2n(n-1)}{3(2n-1)}.
}
\tag{6}
\]

The simple-chord variance is
\[
\boxed{
\operatorname{Var}(S_n)
=
\frac{4n(n-1)}{(2n-1)^2}.
}
\tag{7}
\]
Together with the classical exact crossing variance
\[
\operatorname{Var}(X_n)
=
\frac{n(n-1)(n+3)}{45},
\tag{8}
\]
this yields the particularly simple exact correlation law
\[
\boxed{
\operatorname{Corr}(S_n,X_n)
=
-\sqrt{\frac5{n+3}}.
}
\tag{9}
\]

Thus the two marginal statistics that are respectively asymptotically Poisson and asymptotically Gaussian have an exact finite-size negative dependence:
\[
\sqrt n\,\operatorname{Corr}(S_n,X_n)\longrightarrow-\sqrt5.
\tag{10}
\]

## Assumptions and scope

A chord diagram is a perfect matching of \(2n\) labeled points in cyclic order. Crossings use the usual alternating-endpoint definition.

A simple chord joins two consecutive cyclic endpoints, including the wrap-around pair.

Equation (1) is a size-biased or Palm identity. Weighting a diagram by its number of simple chords and then looking only at its crossing count has exactly the same effect as deleting one marked simple chord and passing from size \(n\) to size \(n-1\).

The result concerns the total number of simple chords, not the total number of isolated vertices of the intersection graph. Every simple chord is isolated, but an isolated chord need not be simple.

## Proof

For each cyclic adjacent pair \(e_i\), \(1\le i\le2n\), let
\[
I_i=\mathbf 1\{e_i\text{ is a chord of }\mathcal C_n\}.
\]
Then
\[
S_n=\sum_{i=1}^{2n}I_i.
\]

For a fixed adjacent pair,
\[
\Pr(I_i=1)=\frac1{2n-1},
\tag{11}
\]
because one endpoint is matched uniformly to one of the other \(2n-1\) endpoints.

Conditional on
\[
I_i=1,
\]
delete that simple chord and close the cyclic gap. The remaining matching is uniform on \(2n-2\) endpoints. A simple chord crosses no other chord, and deleting it does not change any crossing among the remaining chords. Hence
\[
X_n\mid(I_i=1)
\overset d=
X_{n-1}.
\tag{12}
\]

Therefore
\[
\begin{aligned}
\mathbb E[S_nf(X_n)]
&=
\sum_{i=1}^{2n}\mathbb E[I_if(X_n)]\\
&=
\frac{2n}{2n-1}\,
\mathbb E f(X_{n-1}).
\end{aligned}
\tag{13}
\]
Putting \(f=1\) gives (2), and division proves (1). Subtracting
\[
\mathbb E S_n\,\mathbb E f(X_n)
\]
from (13) proves (3).

For the stochastic comparison, start instead with a uniform diagram \(\mathcal C_n\). Delete the chord incident to one distinguished endpoint and then relabel the remaining \(2n-2\) endpoints in cyclic order. The residual matching is uniform, so its crossing count has law \(X_{n-1}\). Deleting one chord can only remove crossings and cannot create any. Thus this construction gives the coupling (4).

For \(n\ge2\), the deleted chord has positive probability of crossing another chord. Hence
\[
\Pr(X_{n-1}<X_n)>0.
\]
Equations (3)--(4) now give (5) and strictness for strictly increasing \(f\).

For the first moment of \(X_n\), choose four endpoints. Among their three possible pairings, exactly one is crossing. Equivalently,
\[
\mathbb E X_n
=
\binom{2n}{4}
\frac1{(2n-1)(2n-3)}
=
\frac{n(n-1)}6.
\tag{14}
\]
Hence
\[
\mathbb E X_{n-1}-\mathbb E X_n
=
-\frac{n-1}{3}.
\]
Substitution in (3) proves (6).

It remains to compute the simple-chord variance. Equation (11) gives
\[
\lambda_n:=\mathbb E S_n=\frac{2n}{2n-1}.
\]
For an ordered pair of distinct adjacent edges \(e_i,e_j\), the two candidate simple chords can coexist exactly when they do not share an endpoint. For each \(i\), there are \(2n-3\) such choices of \(j\), and
\[
\Pr(I_i=I_j=1)
=
\frac1{(2n-1)(2n-3)}.
\]
Therefore
\[
\mathbb E[S_n(S_n-1)]
=
\frac{2n(2n-3)}{(2n-1)(2n-3)}
=
\lambda_n.
\tag{15}
\]
Thus
\[
\operatorname{Var}(S_n)
=
2\lambda_n-\lambda_n^2
=
\frac{4n(n-1)}{(2n-1)^2},
\]
proving (7).

The exact crossing variance (8) is the classical chord-diagram formula reproduced in the cited primary literature. Combining (6)--(8) gives
\[
\operatorname{Corr}(S_n,X_n)
=
\frac{-2n(n-1)/(3(2n-1))}
{\sqrt{4n(n-1)/(2n-1)^2}\,
 \sqrt{n(n-1)(n+3)/45}}
=
-\sqrt{\frac5{n+3}},
\]
which proves (9)--(10).

## Verification

The accompanying checker exhaustively enumerates all perfect matchings through size \(7\).

It reconstructs \(S_n\) and \(X_n\) directly from each matching, verifies the exact means, covariance, both variances, and the correlation-square identity. It also verifies the Palm identity (1) for polynomial test functions and for every point-mass indicator on the finite crossing support.

Finally, it checks the finite stochastic ordering of \(X_n\) over \(X_{n-1}\) from their exact enumerated distributions.

The exhaustive replay is supplementary. The all-\(n\) Palm identity is proved by deleting a marked simple chord, while monotonicity follows by deleting an arbitrary distinguished chord.

## Relationship to prior work

Acan studies uniformly random chord diagrams and their intersection graphs, defines simple chords explicitly, and develops uniform growth constructions. The paper also studies chord length and the crossing-degree structure of a random chord. It does not state a mixed law between the total number of simple chords and the total number of crossings.

Paguyo's probability treatment is the closest inspected source because it studies exactly the two marginals appearing here. Its crossing section records the exact mean and variance of \(X_n\), and its simple-chord section proves Poisson approximation for \(S_n\) by size-bias coupling. The inspected full text treats those statistics in separate sections and does not state their covariance, the marked-deletion identity (1), or the exact correlation (9).

Flajolet and Noy established the classical asymptotic Gaussian law and exact moments for crossings, together with component asymptotics. Their accessible abstract does not contain a joint simple-chord/crossing statement; full-text noncoverage is not asserted here and remains a residual originality risk.

## Limitations

The Palm identity exploits the fact that a simple chord crosses no other chord. A corresponding formula for chords of positive length has an additional random crossing contribution and is not claimed.

Zero covariance or negative covariance against monotone functions does not imply full negative association of the vector of all local chord indicators.

The exact crossing variance is taken from established chord-diagram literature rather than rederived combinatorially in the proof; the accompanying exhaustive checker independently confirms it through size \(7\).

Older generating-function literature could encode the same mixed moment implicitly. The originality claim is the explicit Palm deletion law, its monotone-function consequence, and the resulting closed-form covariance and correlation.

## References

1. H. Acan, “On a uniformly random chord diagram and its intersection graph,” arXiv:1501.01489, first submitted 2015-01-07; later *Discrete Mathematics* 340 (2017), 1967–1985, DOI 10.1016/j.disc.2016.11.004.
2. J. E. Paguyo, “Convergence rates of limit theorems in random chord diagrams,” arXiv:2104.01134, first submitted 2021-04-02, revised 2023-01-11. The manuscript lists 2020 Mathematics Subject Classification \(60C05,60F05\).
3. P. Flajolet and M. Noy, “Analytic Combinatorics of Chord Diagrams,” in *Formal Power Series and Algebraic Combinatorics*, 2000, 191–201, DOI 10.1007/978-3-662-04166-6_17.
