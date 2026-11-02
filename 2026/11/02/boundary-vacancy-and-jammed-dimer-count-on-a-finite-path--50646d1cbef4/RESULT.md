# Boundary vacancy and jammed dimer count on a finite path

## Finding

For the discrete Page–Rényi dimer-parking process on a path of \(n\ge 2\) sites, let \(U_n\) indicate that the left endpoint is vacant at jamming, and let \(M_n\) be the number of accepted dimers. Then
\[
\operatorname{Cov}(U_n,M_n)=0\quad\text{if }n\in\{2,3,5\},
\qquad
\operatorname{Cov}(U_n,M_n)<0\quad\text{for all other }n\ge2.
\]
Moreover,
\[
\lim_{n\to\infty}\operatorname{Cov}(U_n,M_n)
=-\frac{e^{-1}+e^{-3}}4.
\]
The mixed-moment ordinary generating function is exactly
\[
\sum_{n\ge1}\mathbb E[U_nM_n]x^n
=\frac{x e^{-x}\bigl(1-x+2x^2-(1+x)e^{-2x}\bigr)}{4(1-x)^2}.
\]
For the one-site path the covariance is trivially zero as well.

## Assumptions and scope

Let \(n\ge1\) be an integer. Process the \(n-1\) edges of the line graph on \(\{1,\ldots,n\}\) in a uniformly random permutation. Accept an edge exactly when neither endpoint belongs to an earlier accepted edge. The final state is a maximal matching; its size is \(M_n\), and \(U_n=1\) exactly if site \(1\) is uncovered. Equivalently, one may repeatedly choose adjacent vacant sites uniformly from all currently feasible pairs and park a dimer; the distribution of the accepted configuration is the same. All expectations concern this finite-volume random-order model; no thermodynamic-limit assumptions are made.

Set \(a_n=\mathbb E M_n\), \(u_n=\mathbb E U_n\), and \(c_n=\mathbb E[U_nM_n]\). By convention, \(a_0=a_1=0\), \(u_0=0\), \(u_1=1\), and \(c_0=c_1=0\). All stated covariance signs are exact, not numerical approximations.

## Proof

**First-accepted-edge decomposition.** For \(n\ge2\), the earliest attempted edge is uniformly distributed over the \(n-1\) edges. If it is the edge joining \(i\) and \(i+1\), the remaining accepted dimers occur independently in paths of lengths \(i-1\) and \(n-i-1\). When \(i=1\), the left endpoint is covered; otherwise it is vacant precisely when the left subpath's left endpoint is vacant. Independence gives
\[
\begin{aligned}
(n-1)a_n&=(n-1)+2\sum_{j=0}^{n-2}a_j,\\
(n-1)u_n&=\sum_{j=1}^{n-2}u_j,\\
(n-1)c_n&=\sum_{j=1}^{n-2}\bigl(c_j+u_j(1+a_{n-j-2})\bigr).
\end{aligned}
\]
The last recurrence counts the first accepted dimer, accepted dimers in the left subpath, and accepted dimers in the independent right subpath, all multiplied by the left-vacancy indicator.

**Solving the mixed moment.** Define ordinary generating functions \(A(x)=\sum_{n\ge1}a_nx^n\), \(U(x)=\sum_{n\ge1}u_nx^n\), \(C(x)=\sum_{n\ge1}c_nx^n\). The recurrences imply, as formal power-series identities,
\[
\begin{aligned}
\left(\frac{A(x)}x\right)'&=\frac1{(1-x)^2}+\frac{2A(x)}{1-x},\\
\left(\frac{U(x)}x\right)'&=\frac{U(x)}{1-x},\\
\left(\frac{C(x)}x\right)'&=\frac{C(x)+U(x)}{1-x}+U(x)A(x).
\end{aligned}
\]
The initial coefficients and these equations yield
\[
A(x)=\frac{x(1-e^{-2x})}{2(1-x)^2},\qquad
U(x)=\frac{xe^{-x}}{1-x}.
\]
Dividing the last differential equation by \(U(x)/x\), using the equation for \(U\), and integrating with \(C(x)/U(x)\to0\) at zero gives
\[
\left(\frac{C(x)}{U(x)}\right)'=\frac{x}{1-x}+xA(x),\qquad
\frac{C(x)}{U(x)}
=\frac{2-(x+1)e^{-2x}}{4(1-x)}-\frac{2x+1}{4}.
\]
Multiplication by \(U(x)\) proves the stated expression for \(C(x)\).

**Exact coefficients.** For integers \(m\ge0\), let
\[
E_m(z)=\sum_{j=0}^m\frac{z^j}{j!},\qquad
T_m(z)=\sum_{j=0}^m(m+1-j)\frac{z^j}{j!},
\]
with \(E_m=T_m=0\) for negative \(m\). Extracting coefficients gives the finite formulas
\[
\begin{aligned}
u_n&=E_{n-1}(-1),\\
a_n&=\frac{n-T_{n-1}(-2)}2,\\
c_n&=\frac{T_{n-1}(-1)-T_{n-2}(-1)+2T_{n-3}(-1)-T_{n-1}(-3)-T_{n-2}(-3)}4.
\end{aligned}
\]
Thus \(c_n-u_na_n\) is a completely explicit rational number for each finite \(n\).

**The limiting constant and the uniform sign bound.** Put \(R_m(z)=\sum_{j=m}^{\infty}z^j/j!\) for positive \(z\) and nonnegative integer \(m\). For \(m\ge0\), the coefficient comparison
\[
\big|T_m(-z)-(m+1+z)e^{-z}\big|\le zR_{m+1}(z)
\]
follows by subtracting the truncated exponential from its full series and combining adjacent tails. Consequently, with \(\alpha=(1-e^{-2})/2\),
\[
\begin{aligned}
u_n&=e^{-1}+\delta_{u,n},& |\delta_{u,n}|&\le R_n(1),\\
a_n&=\alpha n-e^{-2}+\delta_{a,n},& |\delta_{a,n}|&\le R_n(2),\\
c_n&=e^{-1}\alpha n-\frac{e^{-1}+5e^{-3}}4+\delta_{c,n},
\end{aligned}
\]
where
\[
|\delta_{c,n}|\le\frac{R_n(1)+R_{n-1}(1)+2R_{n-2}(1)+3R_{n-1}(3)+3R_n(3)}4.
\]
For \(n\ge10\), the covariance differs from \(-\bigl(e^{-1}+e^{-3}\bigr)/4\) in absolute value by at most
\[
B_n=\frac{R_n(1)+R_{n-1}(1)+2R_{n-2}(1)+3R_{n-1}(3)+3R_n(3)}4
+R_n(2)+R_n(1)\bigl(n/2+1+R_n(2)\bigr).
\]
Each tail \(R_m(z)\) decreases as \(m\) increases; moreover \(R_{m+1}(1)\le R_m(1)/(m+1)\), so the product \((n/2+1)R_n(1)\) also decreases for \(n\ge10\). Therefore \(B_n\le B_{10}\) for all \(n\ge10\). The elementary geometric-series bound
\[
R_m(z)\le\frac{z^m}{m!}\,\frac{m+1}{m+1-z}\qquad(m+1>z)
\]
yields the exact rational estimate
\[
B_{10}\le\frac{5574423318619}{74071065600000}<\frac1{12}.
\]
Since \(e<3\), the limiting covariance has absolute value \((e^{-1}+e^{-3})/4>1/12\), and hence \(\operatorname{Cov}(U_n,M_n)<0\) for all \(n\ge10\). The error bounds also prove convergence to the stated limit.

For the remaining sample sizes, exact coefficient extraction gives
\[
\begin{array}{c|rrrrrrrr}
n&2&3&4&5&6&7&8&9\\\hline
\operatorname{Cov}(U_n,M_n)&0&0&-2/9&0&-77/450&-91/1296&-1751/14700&-25651/259200.
\end{array}
\]
Together these complete the all-size sign classification.

## Verification

Run `python3 verify.py` using only the Python standard library. It independently enumerates every attempted-edge order for all path sizes \(2\le n\le8\), compares those exact moments with the first-edge recurrence and coefficient expressions through \(n=150\), checks exact sample-size signs and the rational tail bound at \(n=10\). This produces 629 exact assertions. Finite tests corroborate the formal proof; they are not a proof of the infinite family.

## Relationship to prior work

The discrete Page–Rényi parking process and its first-edge decomposition were studied by Gerin [1], building on earlier work. Krapivsky [2] analyzes the mathematically isomorphic nearest-neighbor-exclusion monomer RSA model on \(n-1\) candidate sites, deriving the marginal total-count law and boundary-occupation expectations. Those marginal results do not alone determine the mixed moment \(\mathbb E[U_nM_n]\). The present claim is specifically the mixed boundary/global generating function, its all-size sign classification (including the exceptional fifth size), and its nonzero limiting covariance; neither the model nor the classical splitting method is claimed new.

## Limitations

This result applies only to the uniform random-order discrete path model with dimers; it does not assert the same sign for cycles, nonuniform arrival rates, continuum parking, or longer cars. Independence, mixing, and infinite-volume constructions are not established by this covariance identity. Published spatial-correlation and general adsorption frameworks may provide alternative derivations; complete historical priority cannot be certified from the sources available for inspection. The proof is self-reviewed but has not undergone independent audit.

## References

[1] L. Gerin, *The Page–Rényi Parking Process*, arXiv:1411.8002 (first publicly posted 2014-11-28), https://arxiv.org/abs/1411.8002; *Electronic Journal of Combinatorics* 22(4), P4.4 (2015).

[2] P. L. Krapivsky, *Large Deviations in One-Dimensional Random Sequential Adsorption*, arXiv:2009.08609 (first publicly posted 2020-09-18), https://arxiv.org/abs/2009.08609.

[3] J. W. Evans, *Random and Cooperative Sequential Adsorption*, *Reviews of Modern Physics* 65 (1993), 1281–1329, https://doi.org/10.1103/RevModPhys.65.1281 (background; full text not verified for an exclusion comparison).
