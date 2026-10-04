# Sample size two is the exact boundary for three-point uniform-probability extremality
## Finding
For every integer \(n\ge3\), let \(X_1,\ldots,X_n\) be independent and identically distributed on \(\{-1,0,1\}\), with
\[
\Pr(X_j=-1)=\Pr(X_j=1)=s,\qquad \Pr(X_j=0)=1-2s,
\]
where \(0<s<1/2\). Put
\[
L_n=\min_{1\le j\le n}X_j,\qquad U_n=\max_{1\le j\le n}X_j,
\]
and let \(\rho_n(s)=\operatorname{Corr}(L_n,U_n)\). Then
\[
\rho_n'(1/3)<0\qquad\text{for every integer }n\ge3.
\]
Therefore the uniform probability vector is not even a local maximizer of the correlation of the extreme order statistics for any sample size \(n\ge3\) on the three-point lattice. The known sample-size-two result has the opposite behavior: uniform probabilities are the unique maximizer. Thus sample size two is the exact boundary for this extremality phenomenon on the smallest nontrivial lattice.

## Assumptions and scope
The parent support is fixed to the three equally spaced points \(\{-1,0,1\}\); only the symmetric probability path \((s,1-2s,s)\) is varied. Positive affine changes of the support do not change the correlation, so the statement is equivalent on \(\{1,2,3\}\). The claim concerns ordinary Pearson correlation of the sample minimum and maximum. It proves local non-optimality of the uniform mass vector for every \(n\ge3\); it does not identify a global maximizing mass vector.

## Proof
Write
\[
A=(1-s)^n,\qquad B=s^n,\qquad C=(1-2s)^n.
\]
By symmetry, \(\mathbb E L_n=-\mathbb E U_n\) and \(\operatorname{Var}(L_n)=\operatorname{Var}(U_n)\). The maximum satisfies
\[
\mathbb E U_n=1-A-B,
\qquad
\mathbb E U_n^2=1-A+B.
\]
Moreover, \(L_nU_n=1\) when all observations have the same nonzero sign, \(L_nU_n=-1\) when both signs occur, and \(L_nU_n=0\) otherwise. Since the probability that both signs occur is
\[
1-2(1-s)^n+(1-2s)^n,
\]
we obtain
\[
\mathbb E[L_nU_n]=-1+2A+2B-C.
\]
Consequently
\[
V_n(s):=\operatorname{Var}(U_n)=1-A+B-(1-A-B)^2
\]
and
\[
K_n(s):=\operatorname{Cov}(L_n,U_n)=-1+2A+2B-C+(1-A-B)^2,
\]
so \(\rho_n(s)=K_n(s)/V_n(s)\).

Set \(k=n-1\), \(t=2^k\), and \(q=3^{-k}\). Direct differentiation at \(s=1/3\), followed only by collecting powers, gives
\[
K_n'(1/3)V_n(1/3)-K_n(1/3)V_n'(1/3)
=-\frac{nq^2}{9}\,D_k,
\]
where
\[
D_k=4(8/3)^k+20(4/3)^k+11(2/3)^k+3^{-k}-9\,2^k-27.
\]
Because \(V_n(1/3)>0\), the sign of \(\rho_n'(1/3)\) is the sign of the displayed numerator.

It remains to show \(D_k>0\) for every integer \(k\ge2\). Directly,
\[
D_2=6,\qquad D_3=248/9.
\]
For \(k\ge4\), put
\[
E_k=4(8/3)^k-9\,2^k.
\]
At \(k=4\), \(E_4=4720/81>27\). Also
\[
E_{k+1}=2E_k+\frac{8}{3}(8/3)^k>2E_k,
\]
so \(E_k>27\) for every \(k\ge4\). Since all remaining terms in \(D_k=E_k-27+20(4/3)^k+11(2/3)^k+3^{-k}\) are positive, \(D_k>0\). Hence \(\rho_n'(1/3)<0\) for every \(n\ge3\).

For comparison, when \(n=2\) the same derivative calculation gives \(D_1=0\); the published sharp three-point result shows that the uniform probability vector is in fact the unique global maximizer in that case. This establishes the stated sample-size boundary.

## Verification
The standalone script `verify.py` uses exact rational arithmetic. It enumerates all ordered samples for several small sample sizes, reconstructs \(K_n(s)\) and \(V_n(s)\) from the probability law, checks the derivative numerator against the closed formula, confirms \(D_1=0\), \(D_2=6\), and \(D_3=248/9\), and verifies positivity through a finite stress range. The infinite step \(D_k>0\) for all \(k\ge4\) is proved analytically above and is not inferred from the computation.

## Relationship to prior work
Papadatos proves a discrete Terrell theorem for two observations and, in the concluding discussion, explicitly proposes varying the probability vector on a fixed finite lattice. The paper states that uniform probabilities are expected to maximize the correlation of any two order statistics, while noting that no proof is available. The present result shows that this expectation has an exact sample-size boundary on the three-point lattice: it holds for two observations but fails locally for every larger sample size along a symmetric one-parameter path.

A published database finding establishes the full \(n=2\), three-point probability-vector maximization and is therefore complementary rather than covering: its conclusion reverses as soon as the sample size is at least three. An earlier exact counterexample for \(n=3\) is the first member of the all-sample-size obstruction proved here; the present derivative formula and positivity argument cover every \(n\ge3\) at once.

López-Blázquez and Salamanca-Miño study maximal correlation for order statistics from fixed discrete parent laws and give numerical optimization machinery. Their inspected abstract and descriptive material concern optimization over transformations for a fixed parent, not the probability-vector extremality statement above. Papadatos cites that work before formulating the probability-vector conjectural direction.

## Limitations
The theorem is local in the probability parameter and does not identify the global maximizing vector for \(n\ge3\). It treats only the extreme pair and the three-point lattice. The originality assessment retains a residual risk that the elementary all-sample-size derivative obstruction appears in poorly indexed work on discrete order-statistic correlations, although targeted searches for the formula, the conjecture, and its aliases found no such statement.

## References
1. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1, 28 May 2022; later published in *Mathematical Methods of Statistics* 32 (2023), 122--132.
2. F. López-Blázquez and B. Salamanca-Miño, *Automatic differentiation and maximal correlation of order statistics from discrete parents*, *Computational Statistics* 36 (2021), 2889--2915, DOI: 10.1007/s00180-021-01103-5.
