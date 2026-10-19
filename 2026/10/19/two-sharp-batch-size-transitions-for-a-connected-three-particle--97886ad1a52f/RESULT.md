# Two sharp batch-size transitions for a connected three-particle resetting correlation

## Finding
Consider \(N\ge3\) independent one-dimensional Brownian particles of diffusivity \(D>0\), subject to common rate-\(r>0\) Poisson reset events. At each event an independently uniform \(m\)-element subset, \(1\le m\le N\), is sent to the origin. In the unique stationary distribution, let \(Y_i=X_i^2\) and, for three **distinct** labels, define the connected correlation
\[
\kappa_{3}(N,m)=\mathbb E[Y_1Y_2Y_3]-3\mathbb E[Y_1Y_2]\mathbb E[Y_1]+2\mathbb E[Y_1]^3.
\]
Then \(\kappa_{3}(N,m)=(2D/r)^3V_N(m)\), where
\[
V_N(m)=\frac{2N^3(m-1)(2Nm-N-m^2-2m+2)}{m^3(2N-m-1)(3N^2-3Nm-6N+m^2+3m+2)}.
\]
**The unique maximizing batch size** among all integers \(1\le m\le N\) is
\[
m_*(N)=\begin{cases}
N-1,&3\le N\le9,\\
3,&10\le N\le73,\\
2,&N\ge74.
\end{cases}
\]
Thus the stationary connected three-particle squared-displacement correlation has two exact, parameter-independent optimizer transitions. In particular, \(V_N(1)=0\), \(V_N(N)=2\), and \(V_N(N-1)=2+2/(N-1)^3\).

## Assumptions and scope
The Brownian noises are mutually independent and satisfy \(\mathbb E[(B_i(t)-B_i(0))^2]=2Dt\). Reset events form a two-sided stationary homogeneous Poisson process of rate \(r\); each event independently selects a uniform subset of exactly \(m\) of the \(N\) labels and resets their positions to zero, without affecting the other particles. Labels \(1,2,3\) are distinct. The optimizer concerns the **unnormalized**, dimensionful connected third cumulant, not the pairwise covariance or the third cumulant of any single displacement.

Every label is reset at positive rate \(rm/N\). Constructing a stationary process from the last reset of each label in the infinite past yields a unique stationary law: all finite initial-position effects vanish after each coordinate has reset, and each coordinate has an exponentially distributed finite time since its last reset. All moments used below are finite. The claim is classified under primary MSC2020 **82C21** (dynamic continuum particle models).

## Proof
**1. Exact stationary moments.** For any fixed set of \(k\le3\) distinct labels, write \(M_k=\mathbb E[\prod_{i=1}^{k}X_i^2]\), and set \(M_0=1\). A Poisson event intersects these labels with probability
\[
q_k=1-\frac{\binom{N-k}{m}}{\binom Nm}
=1-\prod_{j=0}^{k-1}\frac{N-m-j}{N-j},
\]
where the binomial coefficient is zero if \(m>N-k\). Applying the stationary generator to \(\prod_{i=1}^k X_i^2\) gives
\[
0=2DkM_{k-1}-rq_kM_k,
\qquad M_k=\frac{(2D)^k k!}{r^k\prod_{j=1}^{k}q_j}.
\]
There is no unclosed higher-moment term: a reset touching any of the chosen labels annihilates their product, whereas independent diffusion differentiates precisely one squared factor. In particular, \(q_1=m/N\),
\[
q_2=\frac{m(2N-m-1)}{N(N-1)},\qquad
q_3=\frac{mH}{N(N-1)(N-2)},
\]
where \(H=3N^2-3Nm-6N+m^2+3m+2>0\). Substituting \(M_1,M_2,M_3\) into the connected-cumulant definition and simplifying yields the stated \(V_N(m)\). Its other numerator factor \(T=2Nm-N-m^2-2m+2\) is nonnegative throughout the stated domain and is strictly positive for \(m\ge2\), \(N\ge3\); indeed \(T=(m-1)(m-2)+(2m-1)(N-m)\).

**2. Exact candidates for large populations.** Put \(H_3=3N^2-15N+20\), and introduce the polynomial
\[
B(N,m)=\frac{(5N-13)m^3(2N-m-1)H-27(N-2)H_3(m-1)T}{m-3}.
\]
The numerator is identically divisible by \(m-3\); thus \(B\) is a polynomial, including at \(m=3\). Direct common-denominator algebra yields
\[
V_N(3)-V_N(m)=\frac{2N^3(m-3)B(N,m)}{27(N-2)H_3m^3(2N-m-1)H}.
\]
All denominator factors are strictly positive for \(N\ge10\) and \(4\le m\le N-2\). We now certify \(B>0\) throughout that integer region, without extrapolating from finite tests.

For each \(m=4,5,6,7\), put \(N=10+t\), \(t\ge0\). The coefficients of \(B(10+t,m)\) in descending powers of \(t\) are respectively

| \(m\) | Coefficients from \(t^4\) to \(t^0\) |
| --- | --- |
| 4 | 219, 4701, 34290, 90480, 40320 |
| 5 | 417, 8607, 60663, 158325, 87420 |
| 6 | 675, 13149, 86634, 208080, 100512 |
| 7 | 993, 18057, 109005, 231315, 82926 |

For \(m\ge8\), put \(m=8+t\) and \(N=10+t+u\), where \(t,u\ge0\), so \(N-m\ge2\). The exact expansion is
\[
\begin{aligned}
 B(10+t+u,8+t)={}&5t^6+(201+30u)t^5\\
 &+(3241+1005u+70u^2)t^4\\
 &+(26299+13044u+1904u^2+75u^3)t^3\\
 &+(108534+80709u+18989u^2+1545u^3+30u^4)t^2\\
 &+(191264+230736u+81541u^2+10446u^3+408u^4)t\\
 &+49536+225600u+125178u^2+23061u^3+1371u^4.
\end{aligned}
\]
All coefficients in these five explicit polynomial certificates are positive; hence \(V_N(3)>V_N(m)\) for every \(N\ge10\) and \(4\le m\le N-2\).

**3. Remaining large-population candidates.** The endpoints simplify to \(V_N(N)=2\) and \(V_N(N-1)=2+2/(N-1)^3\). For \(N\ge10\),
\[
V_N(3)-V_N(N-1)=\frac{2N(N-4)P(N)}{27(N-2)(N-1)^3H_3},
\]
where \(P(N)=5N^5-89N^4+508N^3-1306N^2+1620N-810\). On writing \(N=10+t\),
\[
P(10+t)=5t^5+161t^4+1948t^3+10534t^2+21900t+2790>0.
\]
Thus \(V_N(3)>V_N(N-1)>V_N(N)\), and also \(V_N(3)>V_N(1)=0\). For the only remaining candidate \(m=2\),
\[
V_N(3)-V_N(2)=\frac{-N^3(N^2-77N+228)}{108(N-2)(2N-3)H_3}.
\]
The quadratic has no integral zero and its larger real root is \((77+\sqrt{5017})/2\), strictly between \(73\) and \(74\). Its sign implies \(m=3\) is the unique maximizer for \(10\le N\le73\), and \(m=2\) is the unique maximizer for every \(N\ge74\).

**4. Small-population exhaustiveness.** For \(3\le N\le9\), substitute every \(1\le m\le N\) in the exact rational expression for \(V_N(m)\). The unique maximum and the strictly smaller second-largest value are:

| \(N\) | Unique maximizing \(m\) | Maximum \(V_N(m)\) | Second-largest value |
| ---: | ---: | ---: | ---: |
| 3 | 2 | \(9/4\) | \(2\) |
| 4 | 3 | \(56/27\) | \(2\) |
| 5 | 4 | \(65/32\) | \(2\) |
| 6 | 5 | \(252/125\) | \(2\) |
| 7 | 6 | \(217/108\) | \(2\) |
| 8 | 7 | \(688/343\) | \(2\) |
| 9 | 8 | \(513/256\) | \(2\) |

These finitely many exact comparisons complete the proof for all \(N\ge3\).

## Verification
The self-contained `verify.py` reconstructs the generator moments, simplifies the cumulant into \(V_N(m)\), checks every symbolic difference identity and every displayed polynomial coefficient, and independently compares exact rational values for all \(3\le N\le150\). The infinite statement is proved by the positive-coefficient identities above; the auxiliary finite enumeration does not stand in for that proof. Reproduce with `python verify.py` in an environment with SymPy.

## Relationship to prior work
De Mauro, Majumdar and Schehr (2026), arXiv:2601.20077, introduce this same batch-reset process and derive an exact recursive Fourier-marginal closure. They explicitly compute one- and two-particle correlations and find a single pair-correlation optimizer transition at \(N=6\). Their full text, including supplemental sections S1–S10, does **not** give a three-distinct-particle connected squared-displacement cumulant optimizer classification. Their all-order recursion provides a route to computing the moment formula here, so the contribution claimed here is specifically the *sharp global third-cumulant optimization and its two thresholds* rather than the general marginal closure. Majumdar and Schehr (2026), arXiv:2603.03162, likewise discuss pairwise batch-reset correlations but not these two optimizer transitions.

## Limitations
This result assumes uniform fixed-size independent batches, Poisson reset timing, independent Brownian particle noises, and a one-dimensional gas. It does not determine maxima for other observables, for weighted/non-Poissonian batches, or for higher connected cumulants. The third-cumulant formula is derived from the existing solvable model; the asserted additional finding is its complete integer optimization, which is not an independence or experimental claim. Unindexed research could still contain an equivalent optimization.

## References
1. G. de Mauro, S. N. Majumdar, G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077 (first posted 2026-01-27); complete HTML including supplemental sections: https://arxiv.org/html/2601.20077v3 .
2. S. N. Majumdar, G. Schehr, *Dynamically Emergent Correlations*, arXiv:2603.03162 (first posted 2026-03-03); complete HTML: https://arxiv.org/html/2603.03162v1 .
