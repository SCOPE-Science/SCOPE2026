# A finite exact counterexample to variance-matched concentration equalization

## Finding

Let \(\nu^k\) be the uniform law on \(\{-k+1,-k+3,\ldots,k-1\}\). Define \(T(\alpha)\), for \(\alpha\in[1/(k+1),1/k]\), by
\[
T(\alpha)=\tau\nu^k+(1-\tau)\nu^{k+1},\qquad \tau=k(k+1)\alpha-k.
\]
For three independent summands with \((\alpha_1,\alpha_2,\alpha_3)=(1/20,1/20,1/10)\), the variance-matched common parameter is \(\alpha_*=619/10710\), but
\[
\mathcal Q_2\!\left(\sum_{i=1}^3T(\alpha_i)\right)=\frac7{160}
>\frac{219116707}{5055477000}
=\mathcal Q_2\!\left(\sum_{i=1}^3T(\alpha_*)\right).
\]
Here \(\mathcal Q_2(X)=\sup_{x\in\mathbb R}\Pr(X\in(x,x+2])\). Thus the variance-matched equalization inequality stated as Conjecture 6.1 by Juškevičius is false.

## Assumptions and scope

All summands are independent. The law \(\nu^k\) has mean zero and variance \((k^2-1)/3\). For \(\alpha\in[1/(k+1),1/k]\), the mixture parameter \(\tau=k(k+1)\alpha-k\) lies in \([0,1]\), and the variance of \(T(\alpha)\) is the corresponding mixture of the variances of \(\nu^k\) and \(\nu^{k+1}\). The claim concerns only the three-summand instance above; it does not classify all failures or supply a replacement inequality.

## Proof

At the endpoint parameters, \(T(1/20)=\nu^{20}\) and \(T(1/10)=\nu^{10}\). Since \(\operatorname{Var}(\nu^k)=(k^2-1)/3\), the heterogeneous sum has variance
\[
2\frac{20^2-1}{3}+\frac{10^2-1}{3}=133+133+33=299.
\]

For the concentration of this sum, write \(\nu^k\overset d=2U_k-(k-1)\), where \(U_k\) is uniform on \(\{0,\ldots,k-1\}\). The sum therefore has the same law as
\[
2(U_{20}^{(1)}+U_{20}^{(2)}+U_{10})-47.
\]
Its support consists only of odd integers, so an interval of length \(2\) can contain at most one support point. The atom counts are the coefficients of
\[
(1+x+\cdots+x^{19})^2(1+x+\cdots+x^9).
\]
If \(a_t\) is the coefficient of \(x^t\) in \((1+x+\cdots+x^{19})^2\), then \(a_t=t+1\) for \(0\le t\le19\), \(a_t=39-t\) for \(20\le t\le38\), and \(a_t=0\) otherwise. The coefficient \(c_s=\sum_{j=0}^9a_{s-j}\) is symmetric and unimodal: \(c_{s+1}-c_s=a_{s+1}-a_{s-9}\), which is nonnegative through the center and nonpositive after it. Directly, \(c_{23}=c_{24}=175\), so the largest atom is \(175/(20\cdot20\cdot10)=7/160\).

Now set \(\alpha_*=619/10710\). It lies in \([1/18,1/17]\), and
\[
17\cdot18\alpha_*-17=\frac{24}{35}.
\]
Consequently \(T(\alpha_*)=(24/35)\nu^{17}+(11/35)\nu^{18}\), and
\[
\operatorname{Var}(T(\alpha_*))
=\frac{24}{35}\,96+\frac{11}{35}\,\frac{323}{3}
=\frac{299}{3}.
\]
Thus three copies have exactly the same total variance \(299\). On each interval \([1/(k+1),1/k]\), the variance is linear and strictly decreasing in \(\alpha\), because \(\operatorname{Var}(\nu^k)<\operatorname{Var}(\nu^{k+1})\); the pieces join continuously at the endpoints. Hence the variance-matching parameter is unique.

For the equalized sum, let \(p_j=\Pr(\sum_{i=1}^3T(\alpha_*)=j)\). Exact coefficient extraction for the four possible counts of \(\nu^{17}\) components gives
\[
p_0=\frac{3\cdot24\cdot11^2}{35^3}\frac{13}{306}
+\frac{24^3}{35^3}\frac{217}{4913}
=\frac{4818196}{210644875},
\]
and
\[
p_1=\frac{11^3}{35^3}\frac1{24}
+\frac{3\cdot24^2\cdot11}{35^3}\frac{25}{578}
=\frac{6087059}{297381000}.
\]
The component probabilities \(13/306,217/4913,1/24,25/578\) are obtained by counting coefficients in the finite products of the corresponding uniform-support polynomials. Theorem 1.2 of Juškevičius states that the central interval \((-1,1]\) maximizes the concentration of these \(T\)-sums; exhaustive exact convolution over the finite support also confirms the maximum adjacent-pair mass. Therefore
\[
\mathcal Q_2\!\left(\sum_{i=1}^3T(\alpha_*)\right)
=p_0+p_1=\frac{219116707}{5055477000}.
\]
Finally,
\[
\frac7{160}-\frac{219116707}{5055477000}
=\frac{8241647}{20221908000}>0,
\]
which contradicts Conjecture 6.1.

## Verification

The accompanying standard-library Python script uses exact rational arithmetic (`fractions.Fraction`) to reconstruct the mixture laws, variances, finite convolutions, and maximum interval probabilities. It asserts the exact variance match and the strict inequality. The support of each sum is finite, so this computation exhausts every attainable atom and every adjacent-integer interval; it is not an asymptotic or sampled numerical test.

## Relationship to prior work

Juškevičius proves an optimal concentration bound in Theorem 1.2 and then states Conjecture 6.1: among the extremal laws \(T(\alpha_i)\), equalizing the parameters at matched total variance should not decrease concentration. The present example addresses precisely that additional equalization claim, not Theorem 1.2 itself. The paper notes that Kanter's earlier equalization result covers the regime \(\alpha_i\ge1/2\); the parameters here are below \(1/2\). Mattner and Roos study a related two-point concentration bound for symmetric three-point convolutions, which does not imply the present comparison for these multi-point laws.

## Limitations

This is a single exact counterexample to a universal conjecture, not a classification of the parameter region where equalization fails. The numerical gap is small but strictly positive and is given exactly. The calculation establishes the stated finite claim only; no broader inequality or application-specific consequence is asserted. The literature searches found no exact matching result, but search failure alone does not prove global novelty.

## References

1. T. Juškevičius, “The sharp form of the Kolmogorov–Rogozin inequality and a conjecture of Leader–Radcliffe,” *Bulletin of the London Mathematical Society* 56 (2024), 3289–3299. First public version: arXiv:2201.09861, submitted 2022-01-24. DOI: 10.1112/blms.13132.
2. L. Mattner and B. Roos, “A shorter proof of Kanter’s Bessel function concentration bound,” *Probability Theory and Related Fields* 139 (2007), 191–205. arXiv:math/0603522.
