# Exact support-conditioned variance of the nonparametric bootstrap mean
## Finding
Fix real observations
\[
x_1,\ldots,x_N,
\qquad N\ge2,
\]
with empirical mean
\[
\bar x=\frac1N\sum_{i=1}^N x_i
\]
and unbiased empirical variance
\[
s_N^2=\frac1{N-1}\sum_{i=1}^N(x_i-\bar x)^2.
\]
Draw a bootstrap resample of size \(b\ge1\) uniformly with replacement from the \(N\) labeled observations. Let \(C_i\) be the multiplicity of original index \(i\), let
\[
\bar X^*=\frac1b\sum_{i=1}^N C_i x_i,
\]
and let
\[
K=\#\{i:C_i>0\}
\]
be the number of original indices represented at least once.

For every feasible
\[
1\le k\le\min(N,b),
\]
write \(S(r,k)\) for a Stirling number of the second kind and set
\[
a_{b,k}=\frac{S(b-1,k)}{S(b,k)}.
\]
Then
\[
\boxed{\mathbb E[\bar X^*\mid K=k]=\bar x}
\]
and
\[
\boxed{
\operatorname{Var}(\bar X^*\mid K=k)
=
\frac{N-b+N(b-1)a_{b,k}}{Nb}\,s_N^2.
}
\]
The exact unconditional coupling between support size and squared mean fluctuation is
\[
\boxed{
\operatorname{Cov}\!\left(K,(\bar X^*-\bar x)^2\right)
=-\frac{b-1}{b(N-1)}
\left(1-\frac1N\right)^b s_N^2.
}
\]
Hence the covariance is strictly negative whenever \(b>1\) and the observed data are nonconstant.

For the ordinary bootstrap, \(b=N\),
\[
\operatorname{Var}(\bar X^*\mid K=k)
=
\frac{N-1}{N}\frac{S(N-1,k)}{S(N,k)}s_N^2
\]
and
\[
\operatorname{Cov}\!\left(K,(\bar X^*-\bar x)^2\right)
=-\frac1N\left(1-\frac1N\right)^N s_N^2.
\]
At the two extreme support strata, the formula has transparent interpretations. If \(k=1\), the resample is copies of one uniformly chosen original observation. If \(k=b\le N\), there are no repeats and the resample mean is the mean of a simple random sample without replacement of size \(b\).

## Assumptions and scope
The original observations are treated as fixed, as in the conditional nonparametric bootstrap. The support count \(K\) counts represented original indices, not distinct numerical values; tied observed values therefore remain separate sampling units.

The resample size \(b\) is arbitrary and need not equal \(N\). The formulas require uniform resampling of labeled observations with replacement. They do not assert the same expressions for weighted, Bayesian, block, parametric, or unequal-probability bootstraps.

## Proof
Condition on \(K=k\). The occupied index set is a uniformly random \(k\)-subset of \(\{1,\ldots,N\}\). Conditional on a particular occupied set, the \(b\) labeled bootstrap draws are uniformly distributed over all surjections onto those \(k\) labels.

For a fixed occupied label, symmetry gives
\[
\mathbb E C_i=\frac bk.
\]
For a fixed ordered pair of distinct draw positions, the probability that they have the same occupied label is
\[
a_{b,k}=\frac{S(b-1,k)}{S(b,k)},
\]
because merging the two positions leaves a surjection from \(b-1\) labeled units onto the same \(k\) labels. Hence
\[
\mathbb E(C_i)_2
=\frac{b(b-1)}k a_{b,k}.
\]
For two distinct occupied labels \(i\ne j\), the complementary probability that a fixed ordered pair of draw positions receives different labels gives
\[
\mathbb E(C_iC_j)
=\frac{b(b-1)}{k(k-1)}(1-a_{b,k}).
\]
Now put \(W_i=C_i/b\) and average also over the uniformly random occupied subset. For every \(i\),
\[
\mathbb E[W_i\mid K=k]=\frac1N,
\]
so
\[
\mathbb E[\bar X^*\mid K=k]=\bar x.
\]
Moreover,
\[
\mathbb E[W_i^2\mid K=k]
=\frac{1+(b-1)a_{b,k}}{Nb},
\]
and, for \(i\ne j\),
\[
\mathbb E[W_iW_j\mid K=k]
=\frac{(b-1)(1-a_{b,k})}{N(N-1)b}.
\]
Set \(y_i=x_i-\bar x\), so \(\sum_i y_i=0\) and \(\sum_i y_i^2=(N-1)s_N^2\). Exchangeability of the conditional weights yields
\[
\operatorname{Var}(\bar X^*\mid K=k)
=
\left(
\mathbb E W_1^2-\mathbb E W_1W_2
\right)
\sum_{i=1}^N y_i^2,
\]
which simplifies to the stated conditional-variance formula.

For the global covariance, put
\[
q=\left(1-\frac1N\right)^b,
\qquad
Z=\bar X^*-\bar x.
\]
Direct multinomial moments give
\[
\mathbb E C_1^2=\frac{b(N+b-1)}{N^2},
\qquad
\mathbb E C_1C_2=\frac{b(b-1)}{N^2}.
\]
For a different index, conditioning it to be absent gives
\[
\mathbb E[\mathbf 1\{C_2=0\}C_1^2]
=q\frac{b(N+b-2)}{(N-1)^2},
\]
and, with a third index absent,
\[
\mathbb E[\mathbf 1\{C_3=0\}C_1C_2]
=q\frac{b(b-1)}{(N-1)^2}.
\]
Since \(K=N-\sum_j\mathbf 1\{C_j=0\}\), exchangeability gives
\[
\mathbb E[K C_1^2]-\mathbb E[K C_1C_2]
=b+q\frac{b(-N^2+2N-b)}{(N-1)^2}.
\]
Using \(\sum_i y_i=0\),
\[
\mathbb E[KZ^2]
=\frac{\mathbb E[K C_1^2]-\mathbb E[K C_1C_2]}{b^2}
\sum_i y_i^2.
\]
Finally,
\[
\mathbb E K=N(1-q)
\]
and
\[
\mathbb E Z^2=\frac{N-1}{Nb}s_N^2.
\]
Subtracting \(\mathbb E K\,\mathbb E Z^2\) and simplifying proves the covariance identity.

## Verification
The accompanying `checker.py` independently enumerates every bootstrap draw sequence for \(2\le N\le6\) and \(1\le b\le7\) on a fixed nonconstant rational data configuration for each \(N\). For every feasible support size it computes the exact conditional mean and squared fluctuation, then checks both closed conditional formulas. It also checks the unconditional covariance identity for every \((N,b)\) pair.

All computations use integers and exact rational arithmetic. The finite enumeration is supplementary and is not used to establish the universal formulas.

## Relationship to prior work
Rao, Pathak, and Koltchinskii identified randomness in the number of distinct observations as a source of varying information content in ordinary bootstrap samples and proposed sequential resampling that fixes this count. Their complete article develops asymptotic correctness of that modified resampling scheme, including sample-mean examples, but does not state the finite conditional variance or the exact covariance above.

Babu, Pathak, and Rao subsequently studied second-order correctness of a Poisson approximation to the sequential bootstrap. That work again treats the fixed-support idea asymptotically rather than deriving the ordinary bootstrap mean's exact finite law conditional on its realized support size.

Pauly introduced a fixed-size subsample-bootstrap variant motivated explicitly by the random number of distinct observations in the classical bootstrap. The article supplies the subject classification and a direct literature anchor for the support-size problem, but its result is consistency of an empirical process rather than the finite moment identities here.

## Limitations
The theorem conditions on the observed dataset and concerns the bootstrap mean only. It does not quantify conditional higher moments, studentization, or nonlinear statistics. The support count is index-based when observations are tied.

Although the most directly relevant sequential-bootstrap article was inspected completely and several exact-form searches were checked, older resampling and occupancy literature is extensive; an unindexed equivalent finite identity cannot be excluded.

## References
1. M. Pauly, “Consistency of the Subsample Bootstrap empirical process,” *Statistics* 46 (2012), 621–626. DOI: 10.1080/02331888.2010.543469.
2. C. R. Rao, P. K. Pathak, and V. I. Koltchinskii, “Bootstrap by sequential resampling,” *Journal of Statistical Planning and Inference* 64 (1997), 257–281. DOI: 10.1016/S0378-3758(97)00041-4.
3. G. J. Babu, P. K. Pathak, and C. R. Rao, “Second-order correctness of the Poisson bootstrap,” *The Annals of Statistics* 27 (1999), 1666–1683. DOI: 10.1214/aos/1017939146.
