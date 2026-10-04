# Exact calibration boundary for inverse-CDF antithetic Monte Carlo p-values

## Finding
Let \(B\ge1\). Let \(F\) be a continuous strictly increasing null distribution and draw independent \(U_0,U_1,\ldots,U_B\sim\mathrm{Uniform}(0,1)\). Define
\[
X_0=F^{-1}(U_0),\qquad X_{b,+}=F^{-1}(U_b),\qquad X_{b,-}=F^{-1}(1-U_b).
\]
Each antithetic resample has null marginal law \(F\), but each pair is dependent. For
\[
P_B=\frac{1+\sum_{b=1}^B[\mathbf 1\{X_{b,+}\ge X_0\}+\mathbf 1\{X_{b,-}\ge X_0\}]}{2B+1},
\]
one has, for \(j=1,\ldots,2B+1\),
\[
\Pr\!\left(P_B=\frac{j}{2B+1}\right)=\begin{cases}\dfrac1{2(B+1)},&j\ne B+1,\\[3pt]\dfrac1{B+1},&j=B+1.\end{cases}
\]
Hence
\[
\Pr\!\left(P_B\le\frac{j}{2B+1}\right)=\begin{cases}\dfrac{j}{2(B+1)},&1\le j\le B,\\[3pt]\dfrac{j+1}{2(B+1)},&B+1\le j\le2B+1.\end{cases}
\]
The p-value is superuniform at every \(\alpha<(B+1)/(2B+1)\), in particular every \(\alpha\le1/2\), but first fails at
\[
\alpha_* = \frac{B+1}{2B+1},\qquad \Pr(P_B\le\alpha_*)=\frac{B+2}{2(B+1)} > \alpha_*.
\]
At support point \(j/(2B+1)\) the excess for \(B+1\le j\le2B\) is
\[
\frac{2B+1-j}{2(B+1)(2B+1)},
\]
so the maximal additive anti-conservatism is \(B/[2(B+1)(2B+1)]\), attained at \(j=B+1\). For \(B=1\), the masses are \(1/4,1/2,1/4\) at \(1/3,2/3,1\), so the nominal level \(2/3\) has size \(3/4\).

## Assumptions and scope
The test is one-dimensional with larger values more extreme. The null statistic has an exactly known continuous strictly increasing CDF \(F\), so ties have probability zero. The observed null statistic is independent of the \(B\) base uniforms. Dependence occurs only within the inverse-CDF antithetic pairs \((U_b,1-U_b)\).

The result does not cover arbitrary antithetic permutations, discrete null laws, estimated null distributions, or general dependent resampling schemes.

## Proof
Write \(u=U_0\). Strict monotonicity of \(F\) reduces every comparison to the uniform scale.

If \(u>1/2\), the events \(U_b\ge u\) and \(U_b\le1-u\) are disjoint, so pair \(b\) contributes one exceedance with probability \(2(1-u)\) and otherwise zero. Conditional on \(U_0>1/2\), \(2(1-U_0)\) is uniform on \((0,1)\). Therefore for \(c=0,\ldots,B\),
\[
\Pr(C=c\mid U_0>1/2)=\int_0^1 {B\choose c}p^c(1-p)^{B-c}\,dp=\frac1{B+1}.
\]
So the numerator \(1+C\) is uniform on \(\{1,\ldots,B+1\}\) on this half of the sample space.

If \(u<1/2\), each pair contributes at least one exceedance and contributes two exactly when \(u\le U_b\le1-u\), which has probability \(1-2u\). Conditional on \(U_0<1/2\), \(1-2U_0\) is uniform on \((0,1)\). Thus the number \(C'\) of second exceedances is likewise uniform on \(\{0,\ldots,B\}\) after beta-binomial mixing, and the numerator \(B+1+C'\) is uniform on \(\{B+1,\ldots,2B+1\}\).

The two halves each have probability \(1/2\) and overlap only at numerator \(B+1\). This gives the mass function and CDF. For \(j\le B\), \(j/[2(B+1)]<j/(2B+1)\). Between support points the CDF is constant, proving superuniformity up to the first failing support point. For \(j\ge B+1\), subtraction from the nominal support threshold gives \((2B+1-j)/[2(B+1)(2B+1)]\), which is positive exactly for \(j=B+1,\ldots,2B\) and is maximized at \(j=B+1\).

## Verification
`verify.py` checks the beta-binomial identity, mass normalization, CDF formula, first failing support point, and maximal excess in exact rational arithmetic for \(1\le B\le200\). The proof above, not the finite checker, establishes the theorem for all \(B\).

## Relationship to prior work
Ramdas, Barber, Candès, and Tibshirani prove validity for exchangeable Monte Carlo permutation samples and explicitly show that antithetic permutation sampling can invalidate the usual empirical p-value. Their Example 2.2 gives a specific reverse-permutation Gaussian construction with two resamples that is anti-conservative at \(\alpha=1/3\). It does not state the inverse-CDF antithetic distribution, the all-\(B\) CDF, the protected sub-half range, or the first-failure formula above.

Barber and Ramdas later study Monte Carlo testing without joint exchangeability and provide broad finite-sample bounds, rather than this exact antithetic specialization. Hall's classical antithetic-bootstrap work supplies the variance-reduction motivation but does not give this p-value calibration law.

Targeted literature and published-finding corpus searches for inverse-CDF antithetic empirical p-values, exact rank laws, and half-level calibration found no covering statement.

## Limitations
The conclusion is specific to exact inverse-CDF reflection. It does not license arbitrary antithetic or dependent resampling. Indeed, the primary source gives a different antithetic permutation construction that can fail below \(1/2\). The value of this result is the complete calibration of one canonical coupling, not a general antithetic-validity theorem.

## References
1. A. Ramdas, R. F. Barber, E. J. Candès, and R. J. Tibshirani, “Permutation tests using arbitrary permutation distributions,” arXiv:2204.13581 (first public 2022-04-28); Sankhya A 85 (2023), 1156–1177, DOI:10.1007/s13171-023-00308-8. Primary classification 62G10.
2. R. F. Barber and A. Ramdas, “Monte Carlo testing: non-asymptotic guarantees without joint exchangeability,” arXiv:2607.23010 (2026).
3. P. Hall, “Antithetic resampling for the bootstrap,” Biometrika 76 (1989), 713–724, DOI:10.1093/biomet/76.4.713.
