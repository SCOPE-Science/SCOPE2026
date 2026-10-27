# Three logarithmic orders for partitions with a fixed number of distinct part sizes

## Finding
For a fixed integer \(k\ge 2\), let \(p^{(k)}(n)\) count partitions of \(n\) into exactly \(k\) different positive part sizes, with unrestricted positive multiplicities, and put \(P_k(X)=\sum_{0\le n\le X}p^{(k)}(n)\). Define \(L=\log X\), \(H_k=\sum_{j=1}^k j^{-1}\), \(H_k^{(2)}=\sum_{j=1}^k j^{-2}\), and let \(\gamma\) be Euler's constant. For every fixed integer \(k\ge3\), as real \(X\to\infty\),
\[
P_k(X)=\frac{X^k}{(k!)^2}\left\{L^k+k(2\gamma-H_k)L^{k-1}+\binom{k}{2}\left[(2\gamma-H_k)^2+H_k^{(2)}-2\zeta(2)\right]L^{k-2}+O_k(L^{k-3})\right\}.
\]
For \(k=2\) the complete quadratic polynomial has a power-saving error:
\[
P_2(X)=\frac{X^2}{4}\left\{L^2+2(2\gamma-\tfrac32)L+(2\gamma-\tfrac32)^2+\tfrac54-2\zeta(2)\right\}+O(X^{3/2}\log X).
\]
The subtraction of \(\binom{k}{2}\zeta(2)\) in the third logarithmic coefficient, beyond the \(-\binom{k}{2}\zeta(2)\) already arising from the unconstrained divisor-convolution simplex, is the first effect of requiring *different* part sizes. This distinguishes the fixed-number-of-sizes spectrum from a mere symmetrization of divisor tuples.

## Assumptions and scope
The statements hold for each fixed integer \(k\ge2\) with constants allowed to depend on \(k\); they are cumulative rather than pointwise in \(n\). All logarithms are natural, and \(p^{(k)}(0)=0\) for \(k\ge1\). No uniformity as \(k\to\infty\) is asserted. The classical divisor estimate used below is \(D(Y)=\sum_{1\le m\le Y}d(m)=Y\log Y+(2\gamma-1)Y+O(\sqrt{Y})\) for \(Y\ge1\).

## Proof
**1. Ordered part-size pairs and smoothing.** A partition with \(k\) different part sizes is an unordered collection of \(k\) pairs \((a_i,r_i)\) with \(a_i,r_i\ge1\) and all \(a_i\) distinct, where its weight is \(\sum_i a_i r_i\). Let \(U_k(X)\) count the same objects with \(k\) ordered pairs but without the distinctness restriction. Thus
\[
U_k(X)=\sum_{m_1+\cdots+m_k\le X}\prod_{i=1}^k d(m_i),
\]
where each \(m_i\ge1\). The cumulative measure \(\sum_{m\ge1}d(m)\delta_m\) differs, on \([1,Y]\), from the positive continuous density \(\log y+2\gamma\) by a signed cumulative mass \(O(\sqrt Y)\). Replacing its factors successively in the nonnegative simplex count and integrating by parts against the decreasing cumulative convolution of the other factors gives
\[
U_k(X)=\int_{y_i\ge1,\ \sum_i y_i\le X}\prod_{i=1}^k(\log y_i+2\gamma)\,dy_i+O_k\!\left(X^{k-1/2}(\log X)^{k-1}\right).
\]
Indeed every remaining convolution has total mass \(O_k((X\log X)^{k-1})\) and is nonincreasing as a function of the residual allowance. Extending the continuous domain to \(y_i\ge0\) costs \(O_k(X^{k-1}(\log X)^k)\), because \(\int_0^1|\log y|dy<\infty\).

**2. Logarithmic simplex moments.** Put \(y_i=Xu_i\), where the simplex \(\Delta_k=\{u_i\ge0:\sum_{i=1}^k u_i\le1\}\) has volume \(1/k!\). The Dirichlet beta integral with the slack variable \(1-\sum_i u_i\) gives
\[
\frac{1}{\operatorname{vol}\Delta_k}\int_{\Delta_k}\log u_1\,du=-H_k,
\quad
\frac{1}{\operatorname{vol}\Delta_k}\int_{\Delta_k}\log u_1\log u_2\,du=H_k^2+H_k^{(2)}-\zeta(2).
\]
For example, differentiate \(\Gamma(1+s)\Gamma(1+t)/\Gamma(k+1+s+t)\) at \(s=t=0\) and normalize by its value there. Expanding the product gives
\[
U_k(X)=\frac{X^k}{k!}\left\{L^k+k(2\gamma-H_k)L^{k-1}+\binom{k}{2}\left[(2\gamma-H_k)^2+H_k^{(2)}-\zeta(2)\right]L^{k-2}+O_k(L^{k-3})\right\}
\]
for fixed \(k\ge3\). For \(k=2\) this integral expansion is an exact quadratic in \(L\), with error \(O(X^{3/2}\log X)\) from smoothing.

**3. Exactly one repeated size.** For two prescribed ordered indices sharing their size \(a\), their combined weight is \(a(r+s)\), with \(r,s\ge1\). The number of such ordered pairs of multiplicities up to allowance \(Y\) is
\[
B_2(Y)=\sum_{a\le Y}\binom{\lfloor Y/a\rfloor}{2}=\frac{\zeta(2)}2Y^2+O(Y\log Y).
\]
The estimate follows from \(\binom{\lfloor t\rfloor}{2}=t^2/2+O(t)\), summation over \(a\), and the convergent tail of \(\sum a^{-2}\). With \(k-2\) further unrestricted ordered pairs, smoothing as above gives
\[
B_{12,k}(X)=\frac{\zeta(2)}{k!}X^k L^{k-2}+O_k\!\left(X^kL^{k-3}+X^{k-1/2}L^{k-2}\right)
\]
for \(k\ge3\). To check the leading coefficient, the density \(d(\zeta(2)Y^2/2)=\zeta(2)Y\,dY\) contributes \(\zeta(2)X^2u_1\,du_1\) after scaling; \(\int_{u_i\ge0,\sum u_i\le1}u_1\,du=1/k!\) in the \(k-1\)-variable simplex. At \(k=2\), \(B_{12,2}(X)=\zeta(2)X^2/2+O(X\log X)\).

**4. Inclusion-exclusion and its remainder.** Let \(E_{ij}\) be equality of sizes \(a_i=a_j\). Inclusion-exclusion begins with \(U_k-\binom{k}{2}B_{12,k}\). Every intersection of at least two distinct \(E_{ij}\) either contains a triple of equal sizes or two disjoint equal-size pairs. A block of \(r\ge2\) indices sharing size \(a\) has at most \(O_r(X^r)\) choices of size and positive multiplicities with total weight \(\le X\), by \(\sum_{a\ge1}a^{-r}<\infty\). Therefore all higher intersections contribute \(O_k(X^kL^{k-3})\) for \(k\ge3\) (and there are none for \(k=2\)). This proves
\[
k!P_k(X)=U_k(X)-\binom{k}{2}B_{12,k}(X)+O_k(X^kL^{k-3}),\qquad k\ge3,
\]
with the exact equality \(2P_2=U_2-B_{12,2}\) at \(k=2\). Combining the displayed estimates proves both claims, including the second \(-\binom{k}{2}\zeta(2)\) term from forbidding size collisions. \(\square\)

## Verification
The accompanying `verify.py` computes exact partitions by a part-size dynamic program and independently checks the finite convolution identities
\[
2p^{(2)}(n)=(d*d)(n)-b(n),\quad 6p^{(3)}(n)=(d*d*d)(n)-3(b*d)(n)+2t(n),
\]
where \(b(n)=\sigma(n)-d(n)\) and \(t(n)=\sum_{a\mid n}\binom{n/a-1}{2}\), for every \(0\le n\le120\). It also evaluates the exact cumulative \(k=2\) count at \(X=1000,10000,100000\), giving relative residuals approximately \(0.00194012\), \(0.00018661\), and \(0.00001722\) against the explicit asymptotic polynomial. The verifier finishes with `VERIFY_OK`. Finite checks do not replace the analytic proof.

## Relationship to prior work
Agarwal and Garg (2026, arXiv:2610.18371) prove weighted partition identities for \(p^{(k)}(n)\), but no cumulative logarithmic asymptotic occurs in their inspected Theorem 1.2, proof, or conclusions. Kim (2012, DOI 10.1016/j.jnt.2012.01.003) studies this same statistic via generating functions and divisor convolutions; only its abstract and bibliographic description were accessible here, so indirect coverage is an unresolved bibliographic risk. Keith (2017) studies congruences for two- and three-size counts, not this asymptotic expansion. Merca (2026) studies a signed and odd-multiplicity *different* generating function. The OEIS entries A365676 and A002133 provide exact enumeration and formulas, not the three explicit cumulative logarithmic coefficients. The leading term and standard divisor-smoothing machinery are not individually claimed as novel; the combined general third-order formula and the first explicit collision correction are the specific contribution under consideration.

## Limitations
The estimate holds with fixed \(k\) and cumulative weight cutoff; it does not imply a pointwise asymptotic for individual \(p^{(k)}(n)\). The \(k\ge3\) remainder permits additional logarithmic coefficients at lower orders. Published exact generating-function representations may support alternative derivations; priority has not been independently established, particularly because Kim (2012) was not inspected in full. The verifier checks finite identities and representative numerical values, not the infinite-domain error bounds. No independent audit was performed.

## References
- Archit Agarwal and Meghali Garg, *A Combinatorial Proof of Partition Identities for the Number of Distinct Part Sizes*, arXiv:2610.18371 (first posted 2026-10-13).
- Byungchan Kim, *On the number of partitions of n into k different parts*, Journal of Number Theory 132 (2012), 1306–1313, DOI:10.1016/j.jnt.2012.01.003.
- William J. Keith, *Partitions into a small number of part sizes*, International Journal of Number Theory 13 (2017), 229–241, arXiv:1502.00366.
- Mircea Merca, *Signed Enumeration of Partitions with Exactly k Distinct Magnitudes of Odd Multiplicity*, Mediterranean Journal of Mathematics (2026), DOI:10.1007/s00009-026-03168-2.
- OEIS A365676 (partitions by their number of distinct part sizes) and A002133 (exactly two sizes).
- Classical Dirichlet divisor summatory estimate, \(D(X)=X\log X+(2\gamma-1)X+O(\sqrt X)\).
