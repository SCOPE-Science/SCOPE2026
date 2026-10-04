# Exact dependence phases of fixed-composition run transitions

## Finding

Fix integers
\[
a\ge1,
\qquad
b\ge1,
\qquad
N=a+b,
\]
and choose a binary word
\[
X_1,\ldots,X_N
\]
uniformly among all words containing exactly \(a\) ones and \(b\) zeros. Define the local transition indicators
\[
T_i=\mathbf 1\{X_i\ne X_{i+1}\},
\qquad
1\le i<N,
\]
so the ordinary number of runs is
\[
R=1+\sum_{i=1}^{N-1}T_i.
\]
Put
\[
d=a-b.
\]

Every transition indicator has success probability
\[
p=\Pr(T_i=1)=\frac{2ab}{N(N-1)}
=
\frac{N^2-d^2}{2N(N-1)}.
\tag{1}
\]

For every adjacent pair,
\[
\boxed{
\operatorname{Cov}(T_i,T_{i+1})
=
\frac{(N^2-d^2)(d^2-N)}{4N^2(N-1)^2}.
}
\tag{2}
\]
For \(N\ge4\), every disjoint pair \(|i-j|>1\) has
\[
\boxed{
\operatorname{Cov}(T_i,T_j)
=
\frac{(N^2-d^2)\left[N(N-2)-(2N-3)d^2\right]}
{2N^2(N-1)^2(N-2)(N-3)}.
}
\tag{3}
\]

Define the nonintegral threshold
\[
\theta_N
=
\frac{N(N-2)}{2N-3}.
\tag{4}
\]
Then the complete sign diagram is:

- If \(d^2<\theta_N\), adjacent transition indicators are negatively correlated and disjoint transition indicators are positively correlated.
- If \(\theta_N<d^2<N\), both kinds of pairs are negatively correlated.
- If \(d^2=N\), adjacent transition indicators are independent and every disjoint pair is negatively correlated.
- If \(d^2>N\), adjacent transition indicators are positively correlated and every disjoint pair is negatively correlated.

The disjoint covariance in (3) is never zero for an admissible integer composition. The adjacent covariance in (2) vanishes exactly when
\[
d^2=N.
\]
Therefore adjacent transition indicators are independent exactly for square sample sizes
\[
N=q^2
\]
and the two category counts are
\[
\left\{
\frac{N+q}{2},
\frac{N-q}{2}
\right\}.
\tag{5}
\]
At those compositions local transition events are pairwise independent at distance one but remain strictly negatively correlated at every disjoint distance.

Summing the complete covariance field gives
\[
\boxed{
\operatorname{Var}(R)
=
\frac{2ab(2ab-N)}{N^2(N-1)},
}
\tag{6}
\]
the classical fixed-composition runs variance. Thus the scalar variance in (6) hides a composition-dependent cancellation among local negative and positive transition associations.

## Assumptions and scope

The word is sampled uniformly conditional on fixed category counts. This is the usual finite random-arrangement null underlying the binary Wald--Wolfowitz runs statistic.

The main two-distance statement assumes \(N\ge4\), because only then can two transition indicators use four distinct positions. Formula (2) remains valid for \(N=3\). For \(N=2\) there is only one transition indicator.

The result concerns pairwise dependence of the transition indicators. It does not claim joint independence of larger families, Markov structure, or a new formula for the marginal distribution of the total run count.

## Proof

Exchangeability of positions under uniform fixed-composition sampling gives
\[
\Pr(T_i=1)
=
\Pr(01)+\Pr(10)
=
\frac{2ab}{N(N-1)},
\]
which is (1).

For adjacent transitions, both indicators equal one precisely for the local patterns \(010\) or \(101\). Hence
\[
\begin{aligned}
\Pr(T_i=T_{i+1}=1)
&=
\frac{ba(b-1)+ab(a-1)}{N(N-1)(N-2)}\\
&=
\frac{ab}{N(N-1)}.
\end{aligned}
\tag{7}
\]
Subtracting \(p^2\), using
\[
ab=\frac{N^2-d^2}{4},
\]
gives (2).

Now suppose \(|i-j|>1\). The four positions used by the two transitions are distinct. Both transitions equal one exactly when each of the two ordered pairs is either \(01\) or \(10\). There are four orientations, each using exactly two ones and two zeros, so
\[
\Pr(T_i=T_j=1)
=
\frac{4a(a-1)b(b-1)}{N(N-1)(N-2)(N-3)}.
\tag{8}
\]
Subtracting \(p^2\) and simplifying gives (3).

Because \(a,b>0\), one has \(N^2-d^2>0\). Therefore the sign in (2) is exactly the sign of
\[
d^2-N,
\]
whereas the sign in (3) is exactly the sign of
\[
N(N-2)-(2N-3)d^2.
\]
Since
\[
0<\theta_N<N,
\]
the four cases in the stated phase diagram follow.

It remains to exclude equality at the disjoint threshold. If
\[
d^2=\frac{N(N-2)}{2N-3},
\]
then the integer \(2N-3\) divides \(N(N-2)\). But
\[
\gcd(2N-3,N-2)=1,
\]
so \(2N-3\) would divide \(N\). This is impossible for \(N\ge4\), because
\[
2N-3>N.
\]
Thus (3) never vanishes.

For two Bernoulli variables, zero covariance is equivalent to independence because the two marginal probabilities and \(\Pr(1,1)\) determine their full two-by-two table. Hence adjacent transition indicators are independent exactly when \(d^2=N\). This has an admissible integer solution precisely when \(N=q^2\); then \(q\) and \(N\) have the same parity and (5) follows.

Finally,
\[
\operatorname{Var}(R)
=
(N-1)\operatorname{Var}(T_1)
+2(N-2)\operatorname{Cov}(T_1,T_2)
+(N-2)(N-3)\operatorname{Cov}(T_1,T_3).
\tag{9}
\]
Substitution of (1)--(3) reduces (9) to (6).

## Verification

The accompanying checker uses exact rational arithmetic. It exhaustively enumerates every fixed-composition binary word for all \(4\le N\le12\), reconstructs the transition covariance matrix, and verifies the marginal, adjacent, and disjoint formulas pair by pair.

It also checks every admissible composition through \(N=250\) against the sign classification, verifies that the disjoint covariance never vanishes, verifies the square-sample-size characterization of adjacent independence, and checks that summing the local covariance field gives (6).

The enumeration is finite replay only. The universal result follows from the exact sampling probabilities and divisibility argument above.

## Relationship to prior work

Wald and Wolfowitz introduced the two-sample runs statistic under random ordering, and the classical theory gives the fixed-composition mean, variance, and exact run-count distribution. Mood developed the distribution theory of runs in the same period.

Smeeton and Cox give a directly inspected modern treatment of the conditional random-arrangement model. They emphasize that the number of runs is a clustering-versus-alternation statistic, distinguish conditional fixed-count arrangements from unconditional multinomial sampling, and compute a new run whenever the present category differs from the preceding one. Their article studies the distribution of the total number of runs by random shuffling; it does not state the pairwise transition-covariance phase diagram (2)--(5).

Modern runs-test papers continue to classify the problem as nonparametric hypothesis testing. The inspected bibliographic record for Corzo and Babativa's modified runs test lists primary MSC \(62G10\).

Targeted searches for fixed-composition transition-indicator covariance, adjacent versus disjoint transition dependence, the imbalance threshold \(d^2=N\), and the disjoint threshold in (4) did not locate the phase classification above. The raw covariance calculations are elementary enough that they may be implicit in classical variance derivations; the originality claim is therefore concentrated on the complete pairwise sign diagram, the square-size independence classification, and the proof that disjoint transition pairs are never independent.

## Limitations

This is a second-order classification. It does not determine the full joint law of the transition vector.

The category alphabet is binary. Multiple-category fixed-count arrangements have more overlap types and do not reduce to the single imbalance parameter \(d\).

The full 1940 scanned papers were not machine-readable through the inspected route, so no whole-document noncoverage claim is made for them. Older monographs on runs may contain equivalent pairwise formulas under another notation.

## References

1. A. Wald and J. Wolfowitz, “On a Test Whether Two Samples are from the Same Population,” *The Annals of Mathematical Statistics* 11 (1940), 147–162, DOI 10.1214/aoms/1177731909.
2. A. M. Mood, “The Distribution Theory of Runs,” *The Annals of Mathematical Statistics* 11 (1940), 367–392, DOI 10.1214/aoms/1177731825.
3. N. Smeeton and N. J. Cox, “Do-it-yourself shuffling and the number of runs under randomness,” *The Stata Journal* 3 (2003), 270–277, DOI 10.1177/1536867X0300300304.
4. J. Corzo and G. Babativa, “A modified runs test for symmetry,” *Journal of Statistical Computation and Simulation* 83 (2013), 984–991, DOI 10.1080/00949655.2011.647026.
