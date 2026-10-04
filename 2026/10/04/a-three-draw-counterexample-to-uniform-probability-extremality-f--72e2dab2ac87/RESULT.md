# A three-draw counterexample to uniform-probability extremality for discrete order-statistic correlation
## Finding
Let \(X_1,X_2,X_3\) be independent draws from the three-point lattice \(\{-1,0,1\}\), with
\[
\Pr(X_j=-1)=s,\qquad \Pr(X_j=0)=1-2s,\qquad \Pr(X_j=1)=s,
\]
where \(0<s<1/2\). Write \(L=\min(X_1,X_2,X_3)\) and \(U=\max(X_1,X_2,X_3)\). Then
\[
\rho(L,U)=\frac{s(9s^2-10s+3)}{3-12s+20s^2-9s^3}.
\]
At \(s=3/10\),
\[
\rho(L,U)=\frac{81}{319},
\]
whereas the uniform probability vector, \(s=1/3\), gives
\[
\rho(L,U)=\frac14.
\]
Thus
\[
\frac{81}{319}-\frac14=\frac5{1276}>0.
\]
In addition, \(\rho'(1/3)=-9/32<0\), so the uniform vector is not even a local maximizer along this symmetric probability path. This gives a counterexample to the probability-vector extremality conjecture stated for correlations of order statistics on a fixed finite lattice.

## Assumptions and scope
The claim concerns ordinary Pearson correlation of the extreme order statistics from exactly three iid draws. The parent support is the fixed equally spaced three-point lattice; only its probability vector varies. Correlation is invariant under positive affine changes of the support, so \(\{-1,0,1\}\) is equivalent to \(\{1,2,3\}\). The result does not claim a global maximizer over all probability vectors, nor does it address maximal correlation after nonlinear transformations of the order statistics.

## Proof
By symmetry, \(\mathbb E[L]=-\mathbb E[U]\) and \(\operatorname{Var}(L)=\operatorname{Var}(U)\). The law of the maximum gives
\[
\Pr(U=-1)=s^3,
\]
\[
\Pr(U=0)=(1-s)^3-s^3,
\]
and
\[
\Pr(U=1)=1-(1-s)^3.
\]
Hence
\[
\mathbb E[U]=3s(1-s)
\]
and
\[
\mathbb E[U^2]=s(3-3s+2s^2).
\]
Therefore
\[
\operatorname{Var}(U)=s(3-12s+20s^2-9s^3).
\]

For the product \(LU\), the value is \(1\) when all three observations have the same nonzero sign, it is \(-1\) when both signs occur in the sample, and it is \(0\) otherwise. The probability that both signs occur is
\[
1-2(1-s)^3+(1-2s)^3.
\]
Thus
\[
\mathbb E[LU]=2s^3-\left[1-2(1-s)^3+(1-2s)^3\right]
=2s^2(4s-3).
\]
Using \(\mathbb E[L]=-3s(1-s)\),
\[
\operatorname{Cov}(L,U)=s^2(9s^2-10s+3).
\]
Since the two variances coincide, division yields the displayed rational formula for \(\rho(L,U)\).

Substituting \(s=3/10\) gives \(\rho(L,U)=81/319\), while substituting \(s=1/3\) gives \(1/4\). Their difference is exactly \(5/1276\). Differentiating the rational expression and evaluating at \(s=1/3\) gives \(-9/32\).

## Verification
The standalone script `verify.py` enumerates all \(3^3=27\) ordered samples using exact rational arithmetic. It independently reconstructs the moments, checks the closed formula at several rational values of \(s\), verifies \(81/319\), \(1/4\), the gap \(5/1276\), and the derivative \(-9/32\). Running the script prints `VERIFY_OK`.

## Relationship to prior work
Papadatos studies order-statistic correlation for finite uniform populations and then explicitly proposes the extension in which the probability vector on a fixed finite lattice is allowed to vary. The paper states that it is expected that the correlation of any two order statistics is maximized by the uniform probability vector, while noting that no proof is available. The present three-draw calculation directly contradicts that expectation for the extreme pair on the three-point lattice.

López-Blázquez and Salamanca-Miño study maximal correlation for order statistics from discrete parents and develop numerical optimization machinery. Their problem optimizes transformations for a fixed parent distribution; it does not, from the inspected abstract and available descriptive material, supply the probability-vector counterexample proved here. The later Papadatos paper cites that work before stating the probability-vector conjecture.

## Limitations
The result is a counterexample, not a classification of all maximizing probability vectors. It treats three iid draws and the extreme pair only. A highly relevant 2021 paper on maximal correlation of discrete order statistics was not available here as a conveniently searchable full text; its abstract and the later source's discussion were inspected, so there remains a residual risk that a related numerical example appears there without being recognized as this probability-vector counterexample. This risk does not affect the exact proof of the stated counterexample.

## References
1. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1, 28 May 2022; later published in *Mathematical Methods of Statistics* 32 (2023), 122--132.
2. F. López-Blázquez and B. Salamanca-Miño, *Automatic differentiation and maximal correlation of order statistics from discrete parents*, *Computational Statistics* 36 (2021), 2889--2915, DOI: 10.1007/s00180-021-01103-5.
