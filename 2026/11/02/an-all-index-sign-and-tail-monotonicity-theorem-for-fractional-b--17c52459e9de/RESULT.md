# An all-index sign and tail-monotonicity theorem for fractional BDF2 convolution weights

## Finding

For the BDF2 convolution quadrature (CQ) approximation to a fractional derivative, the signs and eventual strict decrease in the magnitudes of **every** weight can be certified by a finite algebraic argument. With \(0<\alpha<1\), \(h>0\), and
\[
\sum_{j=0}^{\infty}w_jz^j=h^{-\alpha}\left(\frac32-2z+\frac12z^2\right)^\alpha,
\]
using the Taylor branch positive at zero, the exact sign classification is
\[
\begin{array}{c|c}
\text{index}&\text{sign}\\ \hline
0&\text{positive}\\
1&\text{negative}\\
2&\operatorname{sgn}(\alpha-5/8)\\
3&\operatorname{sgn}(\alpha-7/8)\\
j\ge4&\text{strictly negative}.
\end{array}
\]
At the two exceptional fractional orders the corresponding coefficients vanish. In addition,
\[
0<-w_{j+1}<-w_j\quad(j\ge4),\qquad
\frac34<\frac{w_j}{w_{j-1}}<1\quad(j\ge6).
\]
The strict all-negative-history condition \(w_j<0\) for all \(j\ge1\) holds **if and only if** \(0<\alpha<5/8\). Its nonpositive variant holds **if and only if** \(0<\alpha\le5/8\). These claims concern the CQ convolution coefficients themselves, not start-up corrections or all stability properties of a time-stepping scheme.

## Assumptions and scope

The index \(j\) is any nonnegative integer, the derivative order \(\alpha\) is any real number strictly between zero and one, and the timestep \(h\) is any positive real. The coefficient sequence is defined by its Taylor series at zero, where the analytic branch is fixed by the positive real value of the symbol. No assumption is made on a spatial discretization, source term, or initial state. The only numerical-analysis connection used is the standard BDF2 convolution symbol specified in Jin--Lazarov--Zhou (2014), Section 2.2.

## Proof

**Normalization.** Write
\[
\left(1-\frac43z+\frac13z^2\right)^\alpha
=\sum_{j=0}^{\infty}c_jz^j.
\]
Then \(w_j=h^{-\alpha}(3/2)^\alpha c_j\), so all signs and adjacent ratios agree with those of \(c_j\). Define the polynomials
\[
\begin{aligned}
Q_4(\alpha)&=64\alpha^2-176\alpha+123,\\
Q_5(\alpha)&=64\alpha^2-208\alpha+183,\\
Q_6(\alpha)&=512\alpha^3-3264\alpha^2+7144\alpha-5475.
\end{aligned}
\]
Differentiating the generating function at zero yields
\[
\begin{aligned}
c_1&=-\frac{4\alpha}{3},\\
c_2&=\frac{\alpha(8\alpha-5)}9,\\
c_3&=-\frac{4\alpha(\alpha-1)(8\alpha-7)}{81},\\
c_4&=\frac{\alpha(\alpha-1)Q_4(\alpha)}{486},\\
c_5&=-\frac{2\alpha(\alpha-2)(\alpha-1)Q_5(\alpha)}{3645},\\
c_6&=\frac{\alpha(\alpha-2)(\alpha-1)Q_6(\alpha)}{65610}.
\end{aligned}
\]
The first three formulas give their stated signs. Since
\[
Q_4(\alpha)=64\left(\alpha-\frac{11}{8}\right)^2+2>0,
\quad
Q_5(\alpha)=64\left(\alpha-\frac{13}{8}\right)^2+14>0,
\]
we have \(c_4<0\) and \(c_5<0\).

**The base ratios.** Define \(r_j=c_j/c_{j-1}\) wherever both coefficients are negative. Direct division gives
\[
r_5=\frac{4(2-\alpha)Q_5(\alpha)}{15Q_4(\alpha)}>0.
\]
Putting \(\beta=1-\alpha\in(0,1)\), an exact identity is
\[
15Q_4(\alpha)-4(2-\alpha)Q_5(\alpha)
=9+244\beta+384\beta^2-256\beta^3>0,
\]
where positivity follows from \(384\beta^2-256\beta^3\ge128\beta^2\). Therefore \(0<r_5<1\). Similarly
\[
r_6=-\frac{Q_6(\alpha)}{36Q_5(\alpha)},\qquad
Q_6(\alpha)+27Q_5(\alpha)
=-512\beta^3+8\beta-30<0.
\]
The last inequality holds because \(0<\beta<1\) implies \(8\beta-30<-22\). Consequently \(r_6>3/4\), so \(c_6<0\). An upper bound \(r_6<1\) follows from the recurrence derived next, using \(r_5<1\).

**The all-index induction.** Differentiating the generating function and comparing coefficients gives the exact recurrence, for all integers \(j\ge1\),
\[
3(j+1)c_{j+1}=4(j-\alpha)c_j+(2\alpha-j+1)c_{j-1}.
\]
For \(j\ge5\) with two consecutive negative coefficients and positive ratio \(r_j\), this becomes
\[
r_{j+1}=\frac{4(j-\alpha)+(2\alpha-j+1)/r_j}{3(j+1)}.
\]
The numerator coefficient \(2\alpha-j+1\) is strictly negative. Thus \(0<r_5<1\) implies
\[
r_6<\frac{3(5)+1-2\alpha}{3(6)}<1.
\]
Now assume \(j\ge6\) and \(3/4\le r_j<1\), with both \(c_j,c_{j-1}\) negative. Since \(1<1/r_j\le4/3\), multiplying by the negative coefficient yields the two bounds
\[
\frac{8j+4-4\alpha}{9(j+1)}
\le r_{j+1}
<\frac{3j+1-2\alpha}{3(j+1)}<1.
\]
The lower bound is greater than \(3/4\), because
\[
\frac{8j+4-4\alpha}{9(j+1)}-\frac34
=\frac{5j-11-16\alpha}{36(j+1)}>0
\quad(j\ge6,\ 0<\alpha<1).
\]
It follows that \(r_{j+1}>0\), the next coefficient is negative, and the induction propagates the strict ratio bounds to every index beyond six. Combined with \(0<r_5<1\), this proves all claims on signs and strict decrease of absolute weights.

The order thresholds are necessary because \(c_2\) changes sign at \(5/8\) and \(c_3\) at \(7/8\), and no other index changes sign. This completes the proof for the entire infinite sequence.

## Verification

`verify_bdf2_signs.py` symbolically checks all six displayed low-order coefficients, the two completed-square identities, the base-ratio polynomials and the recurrence normalization. It also performs exact rational recurrence checks through index 301 for seven fractional orders including the boundaries \(5/8\) and \(7/8\). The program prints its total count of checks. Those finite checks are auxiliary only: the inequalities and induction in the proof cover every real \(\alpha\in(0,1)\) and every index.

Run with `python verify_bdf2_signs.py` after installing the package in `requirements.txt`. No external datasets are required.

## Relationship to prior work

Jin, Lazarov and Zhou (2014), arXiv:1404.3800, construct fractional diffusion schemes using the second-order backward-difference convolution symbol, but do not give the all-index coefficient sign and tail monotonicity classification above.

López-Fernández and Płociniczak (2023; arXiv:2311.00081, inspected 2025 revision), Section 2, Proposition 1, give the general hypergeometric coefficient formula and identify the \(5/8\) and \(7/8\) thresholds for the first few coefficients. They explicitly state that checking the signs of later weights is not straightforward and report numerical checks/plots of later negativity and magnitude decrease. The location of these exceptional thresholds and the *numerical observation* of later negativity are therefore acknowledged prior information. The distinct contribution here is a proof for the full infinite sequence, including strict tail monotonicity and quantitative uniform-in-order adjacent ratio bounds. Neither the displayed finite coefficients nor asymptotic negativity for large fixed orders alone implies those statements for every intermediate index and every real fractional order.

Related BDF2 scalar-decay positivity results concern nonfractional multistep solution trajectories, not the coefficients of a fractional convolution kernel. The preceding proof is self-contained and does not rely on numerical evidence to bridge an infinite range.

## Limitations

The result applies only to the classical constant-step BDF2 convolution symbol and orders strictly between zero and one. It does not classify BDF methods of other orders, variable-step convolution quadrature, starting corrections, complete monotonicity of the entire CQ solution operator, or a maximum principle for arbitrary spatial discretizations. No assertion is made that signed weights alone yield stability, convergence, or optimality of a particular PDE algorithm. The possibility of equivalent previously published proofs under coefficient or generating-function terminology cannot be eliminated without an exhaustive historical bibliography.

## References

1. B. Jin, R. Lazarov and Z. Zhou, *Two Schemes for Fractional Diffusion and Diffusion-Wave Equations with Nonsmooth Data*, arXiv:1404.3800 (first public 2014-04-15); later journal version *Two Fully Discrete Schemes for Fractional Diffusion and Diffusion-Wave Equations with Nonsmooth Data*, SIAM J. Sci. Comput. 38 (2016), A146--A170, DOI 10.1137/140979563. https://arxiv.org/abs/1404.3800
2. M. López-Fernández and Ł. Płociniczak, *Convolution Quadrature for the Quasilinear Subdiffusion Equation*, arXiv:2311.00081 (first public 2023-10-31), Section 2; later SIAM J. Numer. Anal. 63 (2025), 1482--1511. https://arxiv.org/html/2311.00081v3
