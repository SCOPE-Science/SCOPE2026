# Universal dominant-prime law for rational stopping orders

## Finding

Let \(T:[2,\infty)\to[2,\infty)\) be the map
\[
T(x)=\lfloor x\rfloor(1+\{x\}),
\]
where \(\{x\}=x-\lfloor x\rfloor\). For a nonintegral rational \(x\ge2\), its *order* is the least positive integer \(n\) for which \(T^{\circ n}(x)\) is an integer, or infinity if no such integer exists. Fix a denominator \(M\ge2\). Let \(d_M(n)\) be the relative natural density, among integers \(a\ge2M\) with \(\gcd(a,M)=1\), of those with \(\operatorname{ord}(a/M)=n\).

Write \(M=p^s m\), where \(p\) is the largest prime divisor of \(M\), \(s=v_p(M)\ge1\), and \(\gcd(p,m)=1\). Put \(\rho=(p-1)/p\) and define
\[
F_M(z)=\sum_{n\ge1}d_M(n)z^{n-1}.
\]
Then **the entire dominant pole is universal**:
\[
\boxed{F_M(z)-\frac{1}{p^s(1-\rho z)^s}}
\]
is a rational function analytic in a neighborhood of the closed disc \(\lvert z\rvert\le1/\rho\). In particular, if \(m=1\), the displayed difference vanishes identically. If \(m>1\), define
\[
\eta_M=\max_{\substack{d\mid M,\ d>1\\d\notin\{p,p^2,\ldots,p^s\}}}\frac{\varphi(d)}d<\rho.
\]
Writing \(\tau(M)\) for the number of positive divisors, one has the exponentially accurate formula
\[
\boxed{d_M(n)=\frac{1}{p^s}\binom{n+s-2}{s-1}\rho^{n-1}
+O_M\!\left(n^{\tau(M)}\eta_M^n\right)}
\qquad(n\to\infty).
\]
For a prime-power denominator, the formula without its error term is an exact identity for all \(n\ge1\).

Let \(S_M(N)\) denote the relative density of reduced starting fractions with order at least \(N\), including any infinite-order fractions. Then
\[
\boxed{S_M(N)\sim \frac{1}{p^{s-1}}\binom{N+s-2}{s-1}\rho^{N-1}}
\qquad(N\to\infty).
\]
More precisely, \(S_M(N)-S_{p^s}(N)=O_M(N^{\tau(M)}\eta_M^N)\) for \(m>1\), with equality of the two tails for \(m=1\). Consequently, **the entire leading stopping-time profile—including its constant and polynomial factor—is determined only by the largest prime-power divisor**, with all other prime factors making an exponentially smaller contribution.

For example, the simplest composite denominator \(M=6\) has the **exact** rational generating function
\[
F_6(z)=\frac1{3-2z}+\frac1{2-z}-\frac2{3-z}.
\]
Its dominant term is precisely \(F_3(z)=1/(3-2z)\); the terms introduced by the additional factor \(2\) decay at rates \((1/2)^n\) and \((1/3)^n\), strictly faster than \((2/3)^n\).

## Assumptions and scope

The denominator \(M\) is any fixed integer at least two; all densities are relative to numerators coprime to \(M\). The limit defining \(d_M(n)\) is taken first, for each fixed order \(n\), before the limit \(n\to\infty\). The asymptotics are not asserted uniformly in growing \(M\). In the density \(S_M(N)\), an infinite order is counted as at least \(N\), but the set of infinite-order numerators has density zero by the published density-one theorem. No assertion that *every individual rational* has finite order is made.

## Proof

**1. Published exact-order recurrence.** Carvalho's Theorem 3.1 and Corollary 4.3 (arXiv:2605.21802v1) give exact residue classes modulo \(M^{n+1}\) for each positive order. With \(A(n,M)\) the number of classes,
\[
A(1,M)=\varphi(M),\quad
A(n,M)=\varphi(M)\sum_{d\mid M}A(n-1,d)(M/d)^{n-1}
\quad(n\ge2),
\]
where \(A(n,1)=0\) for \(n\ge1\). Consequently,
\[
d_M(n)=\frac{A(n,M)}{M^n\varphi(M)},\qquad
d_M(1)=\frac1M,
\]
and for \(n\ge2\),
\[
\boxed{d_M(n)=\frac1M\sum_{\substack{d\mid M\\d>1}}\varphi(d)d_d(n-1)}.
\]
In particular the power series \(F_M(z)\) obeys the rational recursion
\[
\boxed{(M-z\varphi(M))F_M(z)=1+z\sum_{\substack{d\mid M\\1<d<M}}\varphi(d)F_d(z)}.\tag{1}
\]
Induction over the divisor poset shows that all its possible poles are at \(z=d/\varphi(d)\) for divisors \(d>1\) of \(M\). There are no other poles.

**2. Prime-power pole.** Carvalho's Corollary 3.2 gives
\[
A(n,p^j)=\binom{n+j-2}{j-1}\varphi(p^j)^n.
\]
Since \(\varphi(p^j)=p^j\rho\), the density and its generating function are
\[
d_{p^j}(n)=\frac1{p^j}\binom{n+j-2}{j-1}\rho^{n-1},\qquad
F_{p^j}(z)=\frac{1}{p^j(1-\rho z)^j}.\tag{2}
\]

**3. Exact cancellation of all subordinate singular terms.** Set \(z_0=1/\rho\). A divisor \(d>1\) of \(M\) has \(\varphi(d)/d=\rho\) exactly when \(d\) is a positive power of \(p\). Every other divisor has \(\varphi(d)/d<\rho\). We prove by strong induction on \(M\) that \(F_M-F_{p^s}\) is analytic at \(z_0\). It is zero if \(M=p^s\). Assume \(m>1\), and regard two rational functions as equivalent when their difference is analytic at \(z_0\).

For every proper divisor \(p^j e\) of \(p^s m\), with \(j\ge1\), \(e\mid m\) and \(p\nmid e\), the induction hypothesis gives \(F_{p^je}\equiv F_{p^j}\). Divisors \(e>1\) of \(m\) without a factor \(p\) have generating functions analytic at \(z_0\). Since \(\sum_{e\mid m}\varphi(e)=m\), the proper-divisor sum in (1), modulo analytic terms, is
\[
\sum_{\substack{d\mid M\\1<d<M}}\varphi(d)F_d
\equiv m\sum_{j=1}^{s-1}\varphi(p^j)F_{p^j}
 +(m-\varphi(m))\varphi(p^s)F_{p^s}.
\]
Applying (1) at \(p^s\) to the first sum yields
\[
\begin{aligned}
(M-z\varphi(M))F_M
&\equiv zm\sum_{j=1}^{s-1}\varphi(p^j)F_{p^j}
+z(m-\varphi(m))\varphi(p^s)F_{p^s}\\
&\equiv \left(mp^s-z\varphi(m)\varphi(p^s)\right)F_{p^s}\\
&=(M-z\varphi(M))F_{p^s}.
\end{aligned}
\]
Here the omitted constants are analytic. Because
\(M-z_0\varphi(M)=M(1-\varphi(m)/m)\ne0\), division proves \(F_M\equiv F_{p^s}\). Thus **every coefficient of the Laurent principal part at \(z_0\)** is identical to that of the prime-power denominator, not merely the leading coefficient.

**4. Exponentially smaller remainder.** By step 1, poles of \(F_M-F_{p^s}\) can arise only from divisors \(d\mid M\), \(d>1\). Step 3 cancels every pole at \(z_0\), and all remaining poles have absolute modulus at least \(1/\eta_M>1/\rho\). Partial fractions bound their coefficient of \(z^{n-1}\) by \(O_M(n^{\tau(M)}\eta_M^n)\). Combining with (2) proves the exact-density formula and the announced ratio. Since \(0<\eta_M<1\), summing this error over \(n\ge N\) gives \(O_M(N^{\tau(M)}\eta_M^N)\).

**5. Tail density.** Carvalho's Theorem 4.4 proves that the set of numerators of infinite order has relative density zero. Therefore the density of order at least \(N\) is the complement of the finite union of the classes of orders below \(N\), so it equals \(\sum_{n\ge N}d_M(n)\). For a prime-power denominator, (2) and the ratio of consecutive binomial coefficients give
\[
S_{p^s}(N)\sim p\,d_{p^s}(N)
=\frac1{p^{s-1}}\binom{N+s-2}{s-1}\rho^{N-1}.
\]
The exponentially small comparison in step 4 transfers this to \(M\).

## Verification

The supplied `verify.py` performs exact rational-function computations in \(\mathbb Q(z)\) to confirm removal of the dominant pole for 29 composite denominators; checks 510 prime-power evaluations against the recurrence; and independently iterates the original rational map to count all order classes in 15 denominator/order pairs. It uses exact integers and fractions, not floating-point heuristics. These finite checks do **not** prove pole cancellation for arbitrary denominators; that is the purpose of step 3.

To execute: `python3 verify.py` with Python 3 and SymPy installed. Expected conclusion:

`VERIFY_OK symbolic_pole_cancellations=29 divisor_recurrence_primepower_cases=510 direct_orbit_cases=15 exact_arithmetic=yes`

## Relationship to prior work

André Carvalho, *Rational dynamics of a prime-representing map*, arXiv:2605.21802v1 (first public release 2026-05-20), proves the exact-order divisor recurrence, prime-power formula and density-one result used as starting points. The present theorem determines the dominant complex singularity and a sharp *composite-denominator* tail with its universal full principal part and exponentially smaller correction; these are not statements of Carvalho's paper. Its Theorems 3.1 and 4.4, Corollaries 3.2 and 4.3, and their proofs were compared at the level of the actual quantities.

Assis Azevedo, Maria Carvalho and António Machiavelo, *Dynamics of a quasi-quadratic map*, arXiv:1210.0042v1 (2012), study the **different** map \(x\mapsto x\lceil x\rceil\) and obtain the same divisor-count recurrence and a prime-power class formula. Their Theorem 2.3, Corollary 2.4 and Theorem 3.1 do not give the present full-pole universality or sharp large-order rate. The recurrence nevertheless implies that the newly proved analytic cancellation principle can be applied to that other model as well; this paper is credited for the shared recurrence rather than being represented as a different unexamined object.

## Limitations

The result assumes fixed \(M\) in the asymptotic limit. It does not decide the individual finite-order conjecture, determine the least numerator for a prescribed order, or quantify errors uniformly over varying denominators. The exact recurrence and prime-power coefficient formula were already known; the new contribution is the full-pole cancellation and universally sharp composite-denominator stopping tail. Prior art that implicitly performs this singularity analysis cannot be categorically excluded, and no independent review has been performed.

## References

1. A. Carvalho, *Rational dynamics of a prime-representing map*, arXiv:2605.21802v1, 20 May 2026. https://arxiv.org/pdf/2605.21802
2. A. Azevedo, M. Carvalho and A. Machiavelo, *Dynamics of a quasi-quadratic map*, arXiv:1210.0042v1, 28 September 2012; Journal of Difference Equations and Applications 20 (2014), 36–48. https://arxiv.org/pdf/1210.0042
