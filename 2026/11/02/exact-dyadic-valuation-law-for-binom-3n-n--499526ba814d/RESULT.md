# Exact dyadic valuation law for \(\binom{3n}{n}\)

## Finding
For each integer \(n\geq0\), let \(V(n)=\nu_2\!\left(\binom{3n}{n}\right)\), with \(V(0)=0\). For each integer \(r\geq0\), define the finite polynomial
\[
P_r(z)=\sum_{0\leq n<2^r}z^{V(n)}.
\]
Then the complete bivariate valuation enumerator is the rational function
\[
\boxed{\sum_{r\geq0}P_r(z)t^r=
\frac{(1+t)(1-tz)}{1-(1+z)t+(z-z^2-1)t^2+(z+z^2)t^3}.}
\]
The fraction is reduced over \(\mathbb Q(z,t)\); in particular its denominator gives a minimal order-three polynomial recurrence in the block length for generic \(z\).

Consequently, for every integer \(r\geq0\), no term \(\binom{3n}{n}\) with \(0\leq n<2^r\) has exact 2-adic valuation one, and exactly \(F_{r+2}\) of them have valuation zero, where \(F_0=0,F_1=1\) are Fibonacci numbers. If \(N_r\) is uniform on \(\{0,\ldots,2^r-1\}\), then
\[
\boxed{\mathbb EV(N_r)=\frac r2-\frac23+\frac{3+(-1)^r}{6\,2^r},\qquad
\operatorname{Var}(V(N_r))=\frac{11r}{12}+O(1).}
\]
Moreover, as \(r\to\infty\),
\[
\frac{V(N_r)-r/2}{\sqrt{11r/12}}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).
\]

## Assumptions and scope
All variables \(n,r\) are nonnegative integers. Coefficient extraction in \(z\) gives the *exact* count at every nonnegative valuation: \([z^j]P_r(z)=\#\{0\le n<2^r:V(n)=j\}\). The stated normal limit concerns uniform random indices in the initial dyadic interval, and makes no assertion about finer pointwise arithmetic distributions or odd prime valuations.

## Proof
By Kummer's theorem, \(V(n)\) is the number of binary carries in the addition \(n+2n=3n\). Let \(a_i\in\{0,1\}\) be the binary digits of \(n\), with \(a_{-1}=0\) and \(a_i=0\) for \(i\ge r\), and let \(c_0=0\) be the initial carry. The successive carry bits obey
\[
c_{i+1}=\left\lfloor\frac{a_i+a_{i-1}+c_i}{2}\right\rfloor.
\]
For a length-\(r\) word, the total carry number is \(\sum_{i=0}^{r}c_{i+1}\): after the final actual input digit, one extra zero input digit produces the possible terminal carry, after which all carries vanish.

Record the pair \((a_{i-1},c_i)\). The two states \((1,0)\) and \((0,1)\) have identical weighted transitions and identical terminal weights. Merge them to obtain \(A=(0,0)\), \(B=\{(1,0),(0,1)\}\), and \(C=(1,1)\). Each choice of the next input bit contributes a weight \(z\) if and only if the new carry is one. The resulting weighted transition matrix, initial row, and terminal column are
\[
M(z)=\begin{pmatrix}1&1&0\\1&0&z\\0&z&z\end{pmatrix},\quad
u=(1,0,0),\quad w(z)=(1,1,z)^{\mathsf T}.
\]
The terminal column incorporates exactly the extra possible carry from the zero input digit. Therefore, for every \(r\ge0\),
\[
P_r(z)=\nu M(z)^r w(z).
\]
Inverting the three-by-three polynomial matrix yields
\[
\nu(I-tM(z))^{-1}w(z)=
\frac{(1+t)(1-tz)}{1-(1+z)t+(z-z^2-1)t^2+(z+z^2)t^3},
\]
as claimed. The two possible numerator factors have no common factor with the denominator over \(\mathbb Q(z)\): substitution of \(t=-1\) gives \(-(z-1)(2z+1)\), and substitution of \(t=1/z\) gives \(-(z-1)/z\). Hence the displayed reduced denominator is genuinely order three. In particular
\[
P_0(z)=1,\quad P_1(z)=2,\quad P_2(z)=3+z^2
\]
and for every \(r\ge3\),
\[
P_r=(1+z)P_{r-1}+(1-z+z^2)P_{r-2}-(z+z^2)P_{r-3}.
\]

For the missing valuation one, if the first carry occurs at position \(i+1\), then \(a_i=a_{i-1}=1\) and \(c_i=0\). On the next digit, the shifted copy of \(n\) contributes \(a_i=1\) alongside \(c_{i+1}=1\), so another carry necessarily occurs, including when the next input digit is the terminal zero. Thus a positive carry count cannot equal one. For the zero valuation, all binary digits of \(n\) have no adjacent ones; the number of length-\(r\) binary words with that property is \(F_{r+2}\), also immediately obtained by setting \(z=0\) in the rational generating function.

Differentiation at \(z=1\) gives
\[
\sum_{r\ge0}P_r'(1)t^r=
\frac{7}{6(2t-1)}+\frac1{2(2t-1)^2}
+\frac1{6(t+1)}-\frac1{2(t-1)}.
\]
Since \(P_r(1)=2^r\), extracting coefficients proves the displayed exact expectation.

For the limiting fluctuation law, the characteristic polynomial of the transfer matrix is
\[
Q(\lambda,z)=\lambda^3-(1+z)\lambda^2+(z-z^2-1)\lambda+z+z^2.
\]
At \(z=1\), its three distinct roots are \(2,1,-1\). The nonnegative matrix \(M(1)\) is primitive, so the simple dominant root \(\lambda(z)\) continues analytically near \(z=1\). Implicit differentiation of \(Q(\lambda(z),z)=0\) gives \(\lambda(1)=2\), \(\lambda'(1)=1\), \(\lambda''(1)=4/3\). The transfer-matrix expression and the spectral gap therefore give an analytic nonzero prefactor \(A(s)\), with \(A(0)=1\), such that uniformly for complex \(s\) near zero,
\[
\mathbb E[e^{sV(N_r)}]=A(s)\left(\frac{\lambda(e^s)}2\right)^r(1+O(\rho^r)),\qquad0<\rho<1.
\]
The logarithm of the principal factor has first derivative \(1/2\) and second derivative \(11/12\) at zero; the latter follows from \(\lambda'(1)=1\) and \(\lambda''(1)=4/3\). Two logarithmic derivatives yield the stated \(O(1)\) variance estimate. Substituting \(s=iu/\sqrt{11r/12}\), centering at \(r/2\), and expanding through second order yields the characteristic function \(e^{-u^2/2}\) for each real \(u\). Lévy's continuity theorem proves the Gaussian limit.

## Verification
The standalone standard-library program `verify.py` checks each complete polynomial \(P_r\) for \(0\le r\le16\) against direct digit-sum valuation counts, verifies the exact order-three polynomial recurrence, verifies the exact mean identity, and independently reconstructs every carry for \(0\le r\le13\). It reports `VERIFY_OK`. The verification is a consistency check; the proofs above cover all \(r\).

## Relationship to prior work
Kummer's carry theorem yields the individual valuation \(\nu_2\binom{3n}{n}\). Earlier work on fibbinary integers identifies the no-adjacent-ones structure, while Yang (2017) treats divisibility of composite binomial products. Spiegelhofer and Wallner (2017–2018) compute valuation statistics **across entries of one fixed row** of Pascal's triangle, with a different summation domain; their statements do not imply the present exact dyadic-block statistics along the diagonal pair \(\bigl(3n,n\bigr)\). Their general generating-function techniques are important context but the specialization requires a distinct overlapping-digit carry analysis. Yang's 2017 paper analyzes the 2-adic order of a different composite binomial quotient \(s(n,k)\), not the dyadic block-frequency distribution of \(\binom{3n}{n}\). The 2023 paper of Adegoke, Frontczak and Goy studies analytic series in these binomial coefficients and their reciprocals rather than this coefficient-by-coefficient valuation distribution. Kummer plus finite-state enumeration is the method here; the exact reduced three-state generating function and resulting normal law are the added classification. Earlier unindexed or differently formulated coverage remains possible.

## Limitations
The theorem is specific to the factor three, prime two, and initial intervals of length a power of two. It does not give distributions for arbitrary intervals, other primes, or general multipliers; it also does not claim priority beyond the inspected sources. 

## References
1. E. E. Kummer, classical carry theorem for \(p\)-adic binomial valuations (1852); statement at https://en.wikipedia.org/wiki/Kummer%27s_theorem.
2. Q.-H. Yang, *A refinement of Guo's theorem concerning divisibility properties of binomial coefficients*, Ars Combinatoria 135 (2017), 213–221; public source dated 2017-10-31: https://combinatorialpress.com/ars-articles/volume-135-ars-articles/a-refinement-of-guos-theorem-concerning-divisibility-properties-of-binomial-coefficients/.
3. L. Lindroos, A. Sills, H. Wang, *Odd Fibbinary Numbers and the Golden Ratio*, arXiv:1812.02107, first posted 2018-12-05: https://arxiv.org/abs/1812.02107.
4. L. Spiegelhofer, M. Wallner, *Divisibility of binomial coefficients by powers of two*, arXiv:1710.10884, first posted 2017-10-30: https://arxiv.org/abs/1710.10884.
5. L. Spiegelhofer, M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089, first posted 2016-04-24: https://arxiv.org/abs/1604.07089.
6. K. Adegoke, R. Frontczak, T. Goy, *On Some Series Involving the Binomial Coefficients \(\binom{3n}{n}\)*, arXiv:2306.16889, first posted 2023-06-29: https://arxiv.org/abs/2306.16889.
