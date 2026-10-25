# Canonical hard-core path and cycle correlations have distinct square-root thresholds

## Finding

Choose exactly \(k\) occupied sites uniformly among the independent sets of the path \(P_n\) or cycle \(C_n\). Write \(X_i\) for the indicator that vertex \(i\) is occupied. The first non-forbidden pair of sites, \(1\) and \(3\), has the following **exact** covariance on the path, with \(N=n-k+1\):

\[
\operatorname{Cov}_{P_n,k}(X_1,X_3)
=\frac{k(N-k)(k^2+1-n)}{N^2(N-1)(N-2)}.
\]

For the cycle,

\[
\operatorname{Cov}_{C_n,k}(X_1,X_3)
=\frac{k\bigl(k(k+1)-n\bigr)}{n^2(n-k-1)}.
\]

On a path, away from the completely packed singleton state, the sign changes exactly at \(n=k^2+1\); on a cycle it changes at \(n=k(k+1)\). For \(k\ge2\), these give infinite families of nondegenerate, exactly uncorrelated occupancies despite the exclusion constraint. For fixed \(c>0\) and integer sequences \(k/\sqrt n\to c\), both covariances obey

\[
 n^{3/2}\operatorname{Cov}(X_1,X_3)\longrightarrow c(c^2-1).
\]

In contrast, under the grand-canonical hard-core law on \(P_n\), giving each independent set probability proportional to \(\lambda^{|I|}\) for any \(\lambda>0\), the same covariance is strictly **positive** for every \(n\ge4\). Thus conditioning on the exact particle count can reverse the sign of a nearest-allowed-pair correlation, with a sharp geometric distinction between open and periodic boundary conditions.

## Assumptions and scope

The path has labeled vertices \(1,\ldots,n\), edges joining consecutive integers, and \(n\ge4\). The cycle has the same labels and also the edge joining \(n\) and \(1\), with \(n\ge5\). An independent set includes no adjacent vertices. For the canonical path measure, \(1\le k\le\lfloor(n+1)/2\rfloor\); for the canonical cycle measure, \(1\le k\le\lfloor n/2\rfloor\). Every independent \(k\)-set is equally likely. The indicators \(X_1\) and \(X_3\) are defined within the selected graph, not by sampling sites independently. The grand-canonical comparison concerns only the path and uses strictly positive activity \(\lambda\). No infinite-volume assumptions are made.

## Proof

**Path count.** Removing the obligatory unoccupied site immediately after each occupied site except the last bijects independent \(k\)-subsets of \(\{1,\ldots,n\}\) with ordinary \(k\)-subsets of \(\{1,\ldots,N\}\), where \(N=n-k+1\). Therefore the partition count is \(Z_P=\binom Nk\). Fixing vertex \(1\) occupied leaves \(\binom{N-1}{k-1}\) possibilities; fixing both vertices \(1\) and \(3\) occupied leaves \(\binom{N-2}{k-2}\) possibilities. Fixing \(3\) occupied while \(1\) is vacant leaves \(\binom{N-3}{k-1}\) possibilities. Binomial coefficients with out-of-range lower index are interpreted as zero. In particular,

\[
\begin{aligned}
\mathbb E X_1&=\frac{k}{N},\\
\mathbb E(X_1X_3)&=\frac{k(k-1)}{N(N-1)},\\
\mathbb E X_3&=\frac{\binom{N-2}{k-2}+\binom{N-3}{k-1}}{\binom Nk}.
\end{aligned}
\]

Substitution into \(\mathbb E(X_1X_3)-\mathbb E X_1\mathbb E X_3\), cancellation and replacement of \(N\) by \(n-k+1\) yield the asserted rational formula. Its denominator is positive throughout the stated range. Its numerator factors as \(k(N-k)(k^2+1-n)\). The factor \(N-k=0\) is equivalent to \(n=2k-1\), the completely packed path with its one deterministic independent \(k\)-set. Outside that case the sign is exactly the sign of \(k^2+1-n\). If \(k\ge2\), the critical value \(n=k^2+1\) lies in the permitted range and is not the packed case. These are all path zeros.

**Cycle count.** The number of independent \(k\)-subsets of \(C_n\) is

\[
Z_C=\frac{n}{n-k}\binom{n-k}{k}.
\]

Indeed, count independent \(k\)-sets with a marked selected site; going clockwise from the mark specifies \(k\) positive intervening gaps summing to \(n-k\), giving \(\binom{n-k-1}{k-1}\) gap compositions, and each set has \(k\) potential marks. Rotational symmetry gives \(\mathbb EX_1=\mathbb EX_3=k/n\). If both \(1\) and \(3\) are occupied, their neighboring sites \(n,2,4\) are vacant, and choosing the remaining \(k-2\) sites from the interval \(5,\ldots,n-1\) gives \(\binom{n-k-2}{k-2}\) independent sets. Hence

\[
\mathbb E(X_1X_3)=\frac{\binom{n-k-2}{k-2}}{Z_C}
=\frac{k(k-1)}{n(n-k-1)},
\]

with both sides zero at \(k=1\). Subtracting \(k^2/n^2\) gives the cycle formula. The denominator is positive; its only zeros occur at \(n=k(k+1)\), which is admissible exactly for the asserted \(k\ge2\) sequence. In particular, when \(n=2k\) and \(k\ge3\), the measure is supported by the two alternating maximum independent sets and the covariance is \(1/4\).

**Grand-canonical contrast.** Write \(A=\{X_2=0\}\). Conditional on \(A\), vertex \(1\) is isolated from the remaining path \(3,\ldots,n\), so \(X_1\) and \(X_3\) are conditionally independent and \(\mathbb E(X_1\mid A)=\lambda/(1+\lambda)>0\). On \(A^c\), both indicators are zero. Let \(r=\mathbb P(A)\in(0,1)\), \(a=\lambda/(1+\lambda)>0\), and \(b=\mathbb E(X_3\mid A)>0\). Then \(\mathbb E(X_1X_3)=rab\), \(\mathbb EX_1=ra\), and \(\mathbb EX_3=rb\), proving \(\operatorname{Cov}(X_1,X_3)=r(1-r)ab>0\).

**Joint square-root limit.** Let \(k/\sqrt n\to c>0\) with admissible integer \(k\). In the path formula, dividing its numerator by \(n^{5/2}\) and its denominator by \(n^4\) gives respective limits \(c(c^2-1)\) and \(1\). In the cycle formula, dividing numerator by \(n^{3/2}\) and denominator by \(n^3\) gives the same limits. Therefore the asserted scaled covariance limit holds even at \(c=1\), where it equals zero; exact finite thresholds differ by \(k-1\).

## Verification

Run `python3 verify.py` using Python 3 with its standard library. The executable independently enumerates canonical independent sets of paths through \(21\) sites and cycles through \(21\) sites, compares their exact rational covariances with both formulas, and checks all predicted zeros. It checks infinitely parameterized threshold rules algebraically for a finite range of \(k\), and computes exact grand-canonical sums for paths through \(15\) sites at four positive activities. The observed run returned `VERIFY_OK 1305 exact assertions; 139038 canonical samples; grand-canonical positives`. These finite computations do not establish the unrestricted identities: the binomial count and conditional-independence arguments above do.

## Relationship to prior work

The hard-core model is a standard statistical-physics and probabilistic independent-set model: Blanca, Chen, Galvin, Randall, and Tetali (2016 preprint, 2018 publication) study phase coexistence on the two-dimensional lattice; its published primary MSC is 60C05. Davies and Perkins (2021 preprint) distinguish the fixed-size model from the fugacity-weighted model, proving approximation-complexity results for bounded-degree graphs. Joseph and Roby (2017 preprint, 2018 publication) study toggle dynamics and homomesies on path independent sets. Those cited results motivate the models but do not, in the material examined, supply these particular distance-two canonical covariance factorizations, the two exact independence thresholds, or their joint sign reversal relative to the grand-canonical model. General one-dimensional hard-rod counting methods could implicitly contain the formulas; no claim of independently certified historical priority is made.

## Limitations

This result concerns the labeled sites \(1\) and \(3\) only, exactly fixed cardinality, and the uniform canonical measures on finite paths and cycles. The positive-activity grand-canonical comparison is proved for paths, not claimed for cycles. Pairwise zero covariance does not imply independence of all occupations or higher-order independence; for Bernoulli pairs alone, zero covariance does imply their pairwise independence. The finite verifier covers only the stated parameter ranges and is not an infinite proof. Earlier literature on canonical one-dimensional lattice gases may encode equivalent identities in more general correlation functions and warrants expert priority review.

## References

1. A. Blanca, Y. Chen, D. Galvin, D. Randall, and P. Tetali, *Phase Coexistence for the Hard-Core Model on \(\mathbb Z^2\)*, arXiv:1611.01115v1 (public November 3, 2016); *Combinatorics, Probability and Computing* 28 (2019), 1–22; DOI:10.1017/S0963548318000238.
2. E. Davies and W. Perkins, *Approximately Counting Independent Sets of a Given Size in Bounded-Degree Graphs*, arXiv:2102.04984v1 (public February 9, 2021); *SIAM Journal on Computing* 52 (2023), 618–640.
3. M. Joseph and T. Roby, *Toggling Independent Sets of a Path Graph*, arXiv:1701.04956 (2017); *Electronic Journal of Combinatorics* 25(1) (2018), #P1.18; DOI:10.37236/6755.
