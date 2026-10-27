# Exact cubic 2-adic separation for central Delannoy numbers

## Finding
For \(n\ge0\), let the central Delannoy number be \(D_n=\sum_{k=0}^n2^k\binom nk^2\), counting lattice paths from \((0,0)\) to \((n,n)\) using north, east and northeast steps. Write \(\nu_2\) for the 2-adic valuation. For every integer \(n\ge1\),
\[
\nu_2(D_n-(-1)^n)=
\begin{cases}
3\nu_2(n),&n\equiv0\pmod4,\\
3\nu_2(n+1),&n\equiv3\pmod4,\\
2,&n\equiv1,2\pmod4.
\end{cases}
\]
All valuations are finite; the formula is exact, not merely a congruence lower bound.

## Assumptions and scope
The integer index \(n\) is arbitrary and positive. We work in \(\mathbb Z_2\), where \(\binom zk\in\mathbb Z_2\) for every \(z\in\mathbb Z_2\) and integer \(k\ge0\). Define the continuous interpolation \(F(z)=\sum_{k\ge0}2^k\binom zk^2\). It converges uniformly on \(\mathbb Z_2\), and \(F(n)=D_n\) for nonnegative integers.

## Proof
**1. Even indices congruent to two.** If \(z=2u\), with \(u\) odd, terms \(k\ge3\) in \(F(z)\) vanish modulo \(8\). The terms \(k=1\) and \(k=2\) are respectively \(2z^2=8u^2\) and \(4\binom z2^2=4u^2(2u-1)^2\). Hence \(F(2u)-1\equiv4\pmod8\).

**2. The quadratic coefficient vanishes exactly.** Expand \(F(z)\) as a convergent 2-adic power series near \(z=0\). Its linear term is zero, and because \(\binom zk=(-1)^{k-1}z/k+O(z^2)\), its quadratic coefficient is \(L(2)=\sum_{k\ge1}2^k/k^2\). The 2-adic dilogarithm \(L(t)=\sum_{k\ge1}t^k/k^2\), on \(t\in2\mathbb Z_2\), obeys
\[
L(t)+L\bigl(t/(t-1)\bigr)=-\tfrac12\log^2(1-t).
\]
Indeed, differentiate both sides, use \(L'(t)=-\log(1-t)/t\), and evaluate at \(t=0\). At \(t=2\), the transformed argument is again \(2\), whereas the 2-adic logarithm of \(-1\) is zero. Therefore \(2L(2)=0\) and \(L(2)=0\), so the quadratic term is identically zero. The series expansion at \(z=0\) is justified on \(z\in4\mathbb Z_2\) by the coefficientwise estimates below.

**3. A sharp cubic coefficient.** Put \(z=4w\). For each integer \(k\ge1\), the \(k\)-th term is
\[
T_k(w)=2^k\binom{4w}{k}^2=2^{k+4}w^2k^{-2}\prod_{j=1}^{k-1}(1-4w/j)^2.
\]
The 2-adic Gauss valuation of every coefficient of \(T_k\) is at least
\[
B(k)=k+4-2\nu_2(k)-2\sum_{h\ge3}\left\lfloor\frac{k-1}{2^h}\right\rfloor.
\]
For \(9\le k\le31\), direct integer evaluation gives \(B(k)\ge7\). For \(k\ge32\), use \(\sum_{h\ge3}\lfloor(k-1)/2^h\rfloor\le(k-1)/4\) and \(\nu_2(k)\le\log_2k\), giving \(B(k)\ge k/2+9/2-2\log_2 k>7\). Thus the entire tail \(\sum_{k\ge9}T_k(w)\) lies in \(128\mathbb Z_2[[w]]\).

Exact expansion of the eight polynomial terms \(T_1,\ldots,T_8\), using rational arithmetic and reduction after cancelling powers of two from denominators, yields
\[
\sum_{k=1}^{8}T_k(w)\equiv64w^3\pmod{128\mathbb Z_2[[w]]}.
\]
The accompanying program independently verifies all polynomial coefficients and the finite bounds. The quadratic coefficient is exactly zero by Step 2, not just divisible by \(128\). Therefore
\[
F(4w)-1=64w^3U(w),\qquad U(w)\in\mathbb Z_2[[w]],\quad U(w)\equiv1\pmod{2\mathbb Z_2[[w]]}.
\]
For every nonzero \(w\in\mathbb Z_2\), \(U(w)\) is a unit; thus \(\nu_2(F(4w)-1)=6+3\nu_2(w)=3\nu_2(4w)\).

**4. Reflection and odd indices.** For every nonnegative integer \(m\), the hypergeometric rational identity
\[
\sum_{k\ge0}\binom{m+k}{k}^2t^k=(1-t)^{-2m-1}\sum_{j=0}^m\binom mj^2t^j
\]
can be evaluated 2-adically at \(t=2\). Since \(\binom{-m-1}{k}=(-1)^k\binom{m+k}{k}\), the identity yields \(F(-m-1)=-F(m)\). Both sides are continuous on \(\mathbb Z_2\); density of nonnegative integers extends this to all \(z\in\mathbb Z_2\): \(F(-z-1)=-F(z)\). For positive odd \(n\), put \(z=-n-1\). When \(n\equiv3\pmod4\), \(z\in4\mathbb Z_2\) and \(\nu_2(z)=\nu_2(n+1)\); when \(n\equiv1\pmod4\), \(z\equiv2\pmod4\). The even-index conclusions for \(F(z)-1\), together with reflection, give the claimed valuations for \(D_n+1\). This proves all cases.

## Verification
Run `python3 verify_delannoy.py` with the standard Python library. It independently checks the entire eight-term polynomial congruence coefficient by coefficient in exact rational arithmetic, the remaining finite tail-bound cases, and the valuation formula for indices from \(1\) through \(512\). The rigorous proof of the infinite tail uses the explicit inequality above; finite tests alone do not establish the infinite assertion.

## Relationship to prior work
Sun, *Congruences involving generalized central trinomial coefficients* (arXiv:1008.3887), identifies \(D_n\) with \(T_n(3,2)\) and establishes congruences for sums of their squares and odd-prime reductions, but its inspected main results do not yield the exact individual-index dyadic valuation here. Guo, *Some congruences involving powers of Delannoy polynomials* (arXiv:1412.7724), studies weighted sums of cubic and fourth powers of Delannoy polynomials. Sun, *Arithmetic properties of Delannoy numbers and Schröder numbers* (arXiv:1602.00574), proves integrality identities and odd-prime supercongruences for combined Delannoy–Schröder sums. These differ from individual \(\nu_2(D_n-(-1)^n)\) in object and quantification. No claim of exhaustive priority is made.

## Limitations
The theorem concerns only the prime \(2\), not valuations at odd primes. The novelty assessment is limited to searched accessible literature and records; an equivalent formulation may exist elsewhere. No independent mathematical audit has been performed.

## References
1. Zhi-Wei Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887 (first submitted 2010-08-23), https://arxiv.org/abs/1008.3887.
2. Victor J. W. Guo, *Some congruences involving powers of Delannoy polynomials*, arXiv:1412.7724 (2014-12-10), https://arxiv.org/abs/1412.7724.
3. Zhi-Wei Sun, *Arithmetic properties of Delannoy numbers and Schröder numbers*, arXiv:1602.00574 (2016-02-01), https://arxiv.org/abs/1602.00574.
