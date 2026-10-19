# A sharp four-sector re-entrant optimum for Leontief gross-output multipliers

## Finding

A common change in the intensity of intermediate inputs can change which sector yields the largest **total gross-output response** to one unit of final demand, and the same sector can regain first place after losing it. Such a *re-entrant global winner* is impossible for a productive economy with two or three sectors and occurs with four, even if all technical coefficients are strictly positive.

For a nonnegative \(n\times n\) matrix \(A\), \(\rho(A)<1\), set
\[
m_j(t)=\mathbf1^{\mathsf T}(I-tA)^{-1}e_j,\qquad 0<t<1.
\]
Theorem: for \(n\le3\), the winner set \(\{t\in(0,1):m_j(t)\ge m_k(t)\text{ for every }k\}\) is an interval for every sector \(j\). Four sectors are necessary and sufficient for a re-entrant *unique* winner.

The four-sector witness is
\[
A_0=\begin{pmatrix}
0&0&0&1/3\\
0&0&1/2&4/9\\
3/4&0&0&0\\
0&0&0&0
\end{pmatrix}.
\]
For this witness, sector 4 is uniquely optimal on \((0,1/3)\cup(2/3,1)\) and sector 1 is uniquely optimal on \((1/3,2/3)\). There is an exact tie between those two and no others at \(t=1/3\) and \(t=2/3\).

## Assumptions and scope

A sector index \(j\) denotes a unit final-demand impulse \(e_j\); the nonnegative entry \(A_{ij}\) is the intermediate input from sector \(i\) required for a unit of sector \(j\)'s production. The uniformly attenuated technology is \(tA\). Its Leontief gross-output vector is \((I-tA)^{-1}e_j\); summing its coordinates weights every unit of gross production equally. The matrix is productive: \(\rho(A)<1\). The parameter varies strictly within \((0,1)\), and ties count as co-optimality. The theorem does not vary wages, substitution, prices, or direct final-demand composition. The exact four-sector construction is acyclic, and a separate strictly positive construction proves the effect also holds without any zero coefficients.

## Proof

### Dimension bound

Since \(t\rho(A)<1\), \(I-tA\) is a nonsingular \(M\)-matrix, with \(D(t)=\det(I-tA)>0\) for \(0<t<1\). Its inverse is \(\operatorname{adj}(I-tA)/D(t)\). Each adjugate entry has degree at most \(n-1\) in \(t\), so the numerator of each column sum is a polynomial of degree at most \(n-1\). All multipliers equal \(1\) at \(t=0\). Consequently every pairwise difference is
\[
m_j(t)-m_k(t)=\frac{tP_{jk}(t)}{D(t)},
\qquad \deg P_{jk}\le n-2,
\]
where the zero polynomial represents an identity of scores. For \(n\le3\), each \(P_{jk}\) is constant or affine. Its nonnegative-sign set on \((0,1)\) is an interval (possibly empty or the whole interval). The set on which \(j\) is a maximizer is the intersection, over all \(k\), of these intervals; it too is an interval. Therefore a uniquely optimal sector cannot be uniquely optimal on two separated parameter regions while another is uniquely optimal between them.

### Sharp construction

The matrix \(A_0\) is nonnegative and nilpotent: \(A_0^4=0\). Its column sums are \(3/4,0,1/2,7/9\), all less than one. Hence it is productive, and its inverse terminates:
\[
(I-tA_0)^{-1}=I+tA_0+t^2A_0^2+t^3A_0^3.
\]
Direct column sums give
\[
\begin{aligned}
m_1(t)&=1+3t/4+3t^2/8,\\
m_2(t)&=1,\\
m_3(t)&=1+t/2,\\
m_4(t)&=1+7t/9+t^2/4+t^3/8.
\end{aligned}
\]
For every \(t>0\), \(m_1(t)>m_3(t)>m_2(t)\). The only possible global winners are therefore sectors 1 and 4. Their difference has the exact factorization
\[
m_4(t)-m_1(t)=\frac{t}{8}\left(t-\frac13\right)\left(t-\frac23\right).
\]
The signs on the three subintervals prove the two crossovers and the stated uniqueness/ties.

### Strictly positive technology

Set \(B=A_0+(1/1000)\mathbf1\mathbf1^{\mathsf T}\). Every coefficient of \(B\) is positive and its maximum column sum is \(1759/2250<1\), which gives \(\rho(B)<1\). Exact rational inversion at \(t=1/6,1/2,5/6\) produces unique winners 4, 1, and 4, with the respective positive gaps over the runner-up
\[
\frac{6000}{3453491},\qquad \frac{2000}{1149013},\qquad \frac{6000}{687631}.
\]
The multiplier functions are continuous on \((0,1)\); consequently this strictly positive, irreducible, productive technology undergoes at least two winner changes, with sector 4 re-entering first place. The argument does not claim its crossings occur at the original rational thresholds.

## Verification

A standalone `verify.py` uses only Python's standard-library exact rational arithmetic. Running `python verify.py` verifies nilpotence, every polynomial coefficient above, the sign and tie witnesses, positivity/productivity and the three exact strictly positive gaps by Gauss–Jordan rational solution. Expected successful output begins `VERIFY_OK nilpotence_degree=4 crossings=(1/3,2/3) positive_matrix_winners=(4,1,4)`.

The dimension bound is an analytic proof for all productive nonnegative matrices of the stated sizes; the finite arithmetic script only checks the four-dimensional witnesses, not that universal proof. All equalities and inequalities in the construction are exact.

## Relationship to prior work

Leontief resolvent multipliers and cross-sector shock propagation are established. The column-sum resolvent ranking is also a transposed-orientation instance of parameterized Katz/Bonacich centrality, so previous network centrality work already establishes that attenuation can affect rankings. Lerman and Ghosh explicitly study parameter-dependent centrality, and Arratia and Marijuán examine eigenvector and Katz-type centrality in directed acyclic networks. Zhan and coauthors likewise note that Katz rankings can change with the attenuation parameter. Those phenomena are not claimed new here. The mathematically narrower observation is the minimal sector number for *a globally highest-scoring sector to leave and re-enter first place twice*, with exact crossovers and a strictly positive witness. None of the inspected source passages establishes that sharp classification. A specialized general theorem on parameterized centrality rankings could nevertheless subsume it; no claim of exhaustive novelty verification is made.

## Limitations

The parameter represents uniform intermediate-input intensity, not a particular empirically identified economic reform. Total gross output is not the same as final value added, welfare, or socially optimal stimulus allocation. The proof handles nonnegative productive matrices and one-unit shocks, not endogenous technical substitution, equilibrium price changes or unequal sector weights. The dimension argument excludes re-entrance of a unique global winner for at most three sectors; it does not exclude a single pairwise rank crossover. The positive-matrix construction guarantees re-entrance by exact sample-point inequalities but does not classify every one of its crossover values. No independent audit has been performed.

## References

1. K. Lerman and R. Ghosh, *Parameterized Centrality for Network Analysis*, arXiv:0911.1095 (first submitted 2009-11-05). Full manuscript inspected. https://arxiv.org/abs/0911.1095
2. R. Ghosh and K. Lerman, *A Parameterized Centrality Metric for Network Analysis*, arXiv:1010.4247 (2010). Full manuscript inspected. https://arxiv.org/abs/1010.4247
3. J. D. Contreras and G. Fagiolo, *Propagation of Economic Shocks in Input-Output Networks: A Cross-Country Analysis*, arXiv:1401.4704 (2014). Full online text inspected. https://arxiv.org/abs/1401.4704
4. A. Arratia and C. Marijuán, *On graph combinatorics to improve eigenvector-based measures of centrality in directed networks*, Linear Algebra and its Applications (2016), doi:10.1016/j.laa.2016.04.011. Author-hosted full text inspected.
5. X. Zhan et al., *Identification of top-K influential communities in big networks*, Journal of Big Data (2016), doi:10.1186/s40537-016-0050-7. Full open-access HTML inspected.
