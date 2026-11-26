# The optimal one-sided run cap for binary subsequence universality

## Finding

For an integer \(r\ge1\), let \(W_{r,n}\) be a uniformly random length-\(n\) binary word avoiding \(0^{r+1}\), with no restriction on runs of ones. Write \(\iota(w)\) for the largest \(k\ge0\) for which every binary word of length \(k\) occurs as a scattered subsequence of \(w\). For fixed \(r\), set \(\mathbb E\iota(W_{r,n})=\mu_r n+O_r(1)\). Then
\[
 \mu_1=\tfrac12-\tfrac{\sqrt5}{10}<\tfrac13,\qquad
 \mu_2>\mu_3>\mu_4>\cdots>\tfrac13.
\]
In particular, the unique cap maximizing the asymptotic mean per letter is \(r=2\), that is, forbidding \(000\). The gain above the unrestricted rate for weak caps has the sharp expansion
\[
 \mu_r-\tfrac13=\frac{3r-4}{9\,2^{r+2}}+O(r^2 4^{-r})\qquad(r\to\infty).
\]
The expectation concerns \(n\to\infty\) at fixed \(r\) before comparing rates across caps; it does not assert a uniform estimate when \(r\) varies with \(n\).

## Generating function input

Greedy arches are successive shortest prefixes containing both symbols, greedily removed until no such prefix remains. Each completed arch contributes one letter of any target subsequence. Conversely, if the final letters of the successive arches are \(c_1,\ldots,c_k\), the earliest embedding of their concatenation uses precisely the arch endpoints. Appending a letter absent from the incomplete tail gives an unattainable length-\((k+1)\) target; thus the number of complete arches is exactly the index, including for unary or empty words.

Here is a two-state arch transfer derivation of the length and index generating function. Use one state for an empty current arch preceded by a one (or at a fresh start), and one for an empty arch preceded by a zero. The transition to a completed arch ending in one is a nonempty zero-run followed by one, with zero-run cap \(r\) from the first state and \(r-1\) from the second. The transition to a completed arch ending in zero is a nonempty one-run followed by zero, with no one-run cap. With \(z\) marking length and \(u\) marking completed arches, the matrix in this state order is
\[
 M=\begin{pmatrix} A&B\\ A'&B\end{pmatrix},\qquad
 A=\frac{uz^2(1-z^r)}{1-z},\quad A'=\frac{uz^2(1-z^{r-1})}{1-z},\quad B=\frac{uz^2}{1-z}.
\]
The incomplete final tail is empty or a unary run. Its generating function in the first state is \(T_1=(1-z)^{-1}+\sum_{j=1}^r z^j\); in the second it is \(T_0=T_1-z^r\). Solving the two equations with transition matrix \(M\) and tails \((T_1,T_0)\) gives the fresh-start function
\[
 F_r(z,u)=\frac{(1-B)T_1+BT_0}{1-A-B+B(A-A')}
 =\frac{1+z-z^{r+1}-uz^{r+2}}{D_r(z,u)},
 \qquad D_r(z,u)=1-z-2uz^2+uz^{r+2}+u^2z^{r+3}.
\]
This generating function is also established for the bit-complement language in the prior result cited below.

At \(u=1\), \(D_r(z,1)=(1-z^2)(1-z-\cdots-z^{r+1})\), and the numerator is \((1+z)(1-z^{r+1})\). The unique positive solution \(\rho_r\in(1/2,1)\) of \(\sum_{j=1}^{r+1}\rho_r^j=1\) is a simple zero. There can be no other zero of the second factor at modulus at most \(\rho_r\), by the equality condition in the triangle inequality (the terms with exponents one and two must both point along the positive real direction). The extra roots \(\pm1\) are farther out and the numerator does not vanish at \(\rho_r\). Thus near \(u=1\) the simple dominant pole is an analytic root \(\rho_r(u)\), separated in modulus from all others. Subtracting the single pole and bounding analytic coefficients on a larger fixed circle yields an exponentially small error uniformly in a complex neighborhood of \(u=1\). The derivative in \(u\) of the coefficient ratio at one gives \(\mathbb E\iota(W_{r,n})=-n\rho_r'(1)/\rho_r+O_r(1)\). Implicit differentiation gives
\[
 \mu_r=\frac{D_{r,u}(\rho_r,1)}{\rho_rD_{r,z}(\rho_r,1)}.
\]
The same unconstrained calculation with \(F_\infty(z,u)=(1+z)/(1-z-2uz^2)\) gives the reference rate \(1/3\).

## Global comparison of caps

Put \(m=r+2\), \(z_m=\rho_{m-2}\), and \(e_m=2z_m-1=z_m^m\) by summing the geometric series in the defining equation for the root. At \(z=z_m\), direct differentiation gives \(D_{r,u}(z,1)=2z^2-1\) and \(zD_{r,z}(z,1)=(1+z)(me_m-2z)\). Therefore
\[
 \mu_{m-2}-\frac13=\frac{e_m(m-4+b_m)}{3(1-(m-1)e_m)},\qquad b_m=\frac{2}{3+e_m}=\frac1{1+z_m}.
\tag{1}
\]
The denominator is positive by the negative derivative at the simple pole. The excess above \(1/3\) is positive for \(m\ge4\), since \(b_m>1/2\), and for \(m=3\) substitution of \(z_3=(\sqrt5-1)/2\) gives \(\mu_1\) as stated.

The simple positive roots strictly decrease with \(m\) (one more positive term in the defining sum at each step). For \(m\ge5\),
\[
 \frac{e_{m+1}}{e_m}=z_{m+1}(z_{m+1}/z_m)^m<z_4<\frac9{16}.
\]
The last strict bound follows by evaluating \(z+z^2+z^3\) at \(9/16\). In particular \(m e_{m+1}<(m-1)e_m\), so the denominator of (1) strictly increases from \(m\) to \(m+1\). The ratio of the non-\(e\) numerator factors is bounded by
\[
 \frac{m-3+b_{m+1}}{m-4+b_m}<\frac{m-7/3}{m-7/2}\le\frac{16}{9}\qquad(m\ge5),
\]
using \(1/2<b_m<2/3\). Multiplying by \(e_{m+1}/e_m<9/16\) makes the whole numerator decrease. This proves all successive comparisons from \(r=3\) on.

The one remaining comparison follows from rational bounds. Evaluating the defining sums at the endpoints gives \(54368/10^5<z_4<54370/10^5\) and \(51878/10^5<z_5<51880/10^5\). For fixed \(m\ge4\), the right-hand side of (1), viewed as a function of \(e\) on the interval with positive denominator, strictly increases: its numerator derivative is \(m-4+6/(3+e)^2>0\) and its denominator decreases. Inserting the lower endpoint for \(z_4\) and the upper endpoint for \(z_5\) yields
\[
 \mu_2>\frac{3992423}{11124144}>\frac{3588}{10000}>\frac{3579}{10000}>\frac{1442791}{4032414}>\mu_3.
\]
All checks in this comparison are integer arithmetic; this is a certificate of the initial inequality rather than an extrapolation from sampled caps.

Finally \(e_m=z_m^m\le z_3^m\) implies \(me_m\to0\). From \(e_m=2^{-m}(1+e_m)^m\) it follows first that \(e_m=O(2^{-m})\), and then that \(e_m=2^{-m}(1+O(m2^{-m}))\). In (1), \(b_m=2/3+O(e_m)\) and \((1-(m-1)e_m)^{-1}=1+O(me_m)\). These estimates give the expansion in the Finding after setting \(m=r+2\).

## Verification and relation to prior work

The accompanying `verify.py` checks finite distributions by word enumeration, finite-state counting and coefficient extraction. It concerns the generating-function input, not the infinite sequence of slope inequalities; the latter uses (1), the analytic estimates and the rational certificate above.

The [exact one-sided run-limited universality law](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-subsequence-universality-distribution-of-binary-run-limite--b87cc26c6be8) forbids long runs of ones rather than zeros. Bit complementation preserves the index, so that result gives the same generating function, fixed-cap derivative formula and limit \(1/3\); those facts are not claimed as distinct here. The [unconstrained binary law](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37) gives the unconstrained baseline. Adamson et al., *k-Universality of Regular Languages* (https://arxiv.org/abs/2311.10658v1), give fixed-length counting algorithms for arbitrary DFAs. The present result compares the exact rates across all one-sided caps, establishing the unique maximizing cap and the leading excess above the unconstrained baseline.
