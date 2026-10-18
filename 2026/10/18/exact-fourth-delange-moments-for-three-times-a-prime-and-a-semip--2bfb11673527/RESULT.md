# Exact fourth Delange moments for three times a prime and a semiprime discrepancy limit law

## Finding
Let \(q\) and \(p\) be distinct primes, and, for \(0\le t\le1\), let \(N(qp,t)\) count positive integers \(a\le qpt\) with \(\gcd(a,qp)=1\). Define the **unnormalized** totative discrepancy
\[
D_{q,p}(t)=N(qp,t)-\varphi(qp)t,
\qquad \mathcal H_4(qp)=\int_0^1 D_{q,p}(t)^4\,dt.
\]
For each fixed prime \(q\), define \(h_q(u)=\{qu\}-\{u\}\), using fractional parts, and let \(U,V\) be independent uniform random variables on \([0,1]\). If \(T\) is uniform on \([0,1]\), then
\[
\sup_{x\in\mathbb R}\left|\mathbb P(D_{q,p}(T)\le x)-\mathbb P(h_q(V)-h_q(U)\le x)\right|\le\frac{2(q-1)}p.
\]
The limiting variable has the explicit distribution
\[
Z_q=\frac{q-1}{q}(U-V)-\frac{J-K}{q},
\]
where \(J,K\) are independent uniform integers from \(\{0,\ldots,q-1\}\), independent of \(U,V\). In particular, as distinct primes \(p\to\infty\),
\[
\int_0^1D_{q,p}(t)^2\,dt\longrightarrow\frac{q-1}{3q},\qquad
\int_0^1D_{q,p}(t)^4\,dt\longrightarrow\frac{(q-1)(9q^2-9q-2)}{30q^3}.
\]
For the first odd squarefree two-prime family, **every prime \(p\ge5\)** satisfies the exact closed form
\[
\boxed{\displaystyle
\mathcal H_4(3p)=
\begin{cases}
\dfrac{4(p-1)(13p^2-8p-14)}{405p^3},&p\equiv1\pmod3,\\[5pt]
\dfrac{4(13p^3-31p^2+14p+14)}{405p^3},&p\equiv2\pmod3.
\end{cases}}
\]
Both branches tend to \(52/405\). The corresponding **normalized** Delange integral is \(\mathcal H_4(3p)/\varphi(3p)^4\), not the displayed unnormalized fourth moment.

## Assumptions and scope
Throughout, \(q,p\) are rational primes with \(p\ne q\), and \(\{x\}=x-\lfloor x\rfloor\). The stochastic statement concerns the Lebesgue distribution of the real argument \(t\) and permits arbitrary \(p>q\) or \(p<q\). Only the exact fourth-moment formula imposes \(q=3\) and \(p\ge5\). Conventions at finitely many discontinuities do not change any integral or distribution.

## Proof
**1. Inclusion–exclusion and coupling.** For nonintegral \(qpt\), inclusion–exclusion gives
\[
N(qp,t)=\lfloor qpt\rfloor-\lfloor pt\rfloor-\lfloor qt\rfloor+\lfloor t\rfloor.
\]
The linear terms cancel against \(\varphi(qp)t=(q-1)(p-1)t\); therefore, almost everywhere,
\[
D_{q,p}(t)=\{pt\}+\{qt\}-\{qpt\}-\{t\}=h_q(t)-h_q(pt).
\]
Represent a uniform \(T\) by \(T=(K_p+U)/p\), where \(K_p\) is uniform on \(\{0,\ldots,p-1\}\) and \(U\) is independently uniform on \([0,1]\). Introduce an independent uniform \(W\) and put \(V=(K_p+W)/p\); \(V\) is uniform and independent of \(U\). The function \(h_q\) is affine of slope \(q-1\) on each open interval between successive breakpoints \(j/q\). At most \(q-1\) among the \(p\) equal subintervals of \([0,1]\) contain one or more breakpoints in their interiors. Off that event, \(h_q(T)-h_q(V)=(q-1)(U-W)/p\), so its absolute value is at most \((q-1)/p\); the bad event has probability at most \((q-1)/p\).

To control cumulative distributions, note that \(h_q(V)\) has density at most one. Indeed, conditioning on the interval \(V\in(j/q,(j+1)/q)\) produces a uniform law on \((-j/q,(q-1-j)/q)\), of length \((q-1)/q\) and mass \(1/q\), hence density \(1/(q-1)\). At most \(q-1\) such intervals overlap away from endpoints. Thus \(Z_q=h_q(V)-h_q(U)\) also has density at most one. Under the displayed coupling the CDFs differ by at most the bad-event mass plus \((q-1)/p\), proving \(2(q-1)/p\).

**2. Limiting distribution and moments.** Put \(V=(J+V_0)/q\), where \(J\) is uniform on \(\{0,\ldots,q-1\}\) and \(V_0\) is independently uniform. Then \(h_q(V)=((q-1)V_0-J)/q\). Taking two independent copies gives the stated law (the names \(U,V,J,K\) may be interchanged without changing its distribution). Integrating over each of the \(q\) pieces directly yields
\[
\mathbb E h_q(U)=\mathbb E h_q(U)^3=0,\quad
\mathbb E h_q(U)^2=\frac{q-1}{6q},\quad
\mathbb E h_q(U)^4=\frac{(q-1)(2q^2-2q-1)}{30q^3}.
\]
For independent centered copies \(H,H'\), \(\mathbb E(H-H')^4=2\mathbb EH^4+6(\mathbb EH^2)^2\), giving the fourth-moment formula; the second moment follows similarly. Since \(|h_q|<1\), all these moments converge under the coupling, even without invoking a general uniform-integrability theorem.

**3. Exact finite sum for \(q=3\).** Fix \(p\ge5\) prime, put \(n=3p\) and \(\Delta=2(p-1)=\varphi(3p)\). For \(0\le j<n\), define
\[
c_j=j-\lfloor j/3\rfloor-\lfloor j/p\rfloor,\qquad E_j=nc_j-\Delta j.
\]
There are exactly \(c_j\) integers coprime to \(3p\) in \(\{1,\ldots,j\}\). On \(t=(j+u)/n\), with \(0<u<1\), the discrepancy equals \((E_j-\Delta u)/n\). Integration of the fifth-power antiderivative gives the **exact integer certificate identity**
\[
\mathcal H_4(3p)=\frac{\displaystyle\sum_{j=0}^{3p-1}\left[E_j^5-(E_j-\Delta)^5\right]}{5\Delta(3p)^5}.
\tag{1}
\]

**4. A bounded-degree polynomial proof of the two branches.** The integer sum in (1) can be evaluated by a finite polynomial certificate rather than an unproved pattern extrapolation. Write \(p=3m+\kappa\), with \(\kappa\in\{1,2\}\). Partition \(j=kp+s\), \(k\in\{0,1,2\}\), \(0\le s<p\), and write \(s=3a+u\), \(u\in\{0,1,2\}\). Direct substitution yields
\[
E_j=2s+p\bigl((k\kappa+u)\bmod3-k\bigr),\quad
0\le a<m+\mathbf1_{u<\kappa}.
\]
For fixed \(k,u,\kappa\), both \(E_j\) and \(\Delta\) are affine polynomials in \(a,m\). Hence \(E_j^5-(E_j-\Delta)^5\) has total degree at most five, and its sum over the consecutive \(a\)-values is a rational polynomial in \(m\) of degree at most six (Faulhaber's formula). Summing all nine pieces preserves the degree-six bound. The claimed numerator is likewise degree at most six: set
\[
F_1(p)=(p-1)(13p^2-8p-14),\quad F_2(p)=13p^3-31p^2+14p+14,
\]
then the assertion equivalent to (1) is
\[
\sum_{j=0}^{3p-1}[E_j^5-(E_j-\Delta)^5]=24(p-1)p^2F_\kappa(p).
\tag{2}
\]
The complete, executable **14-node exact certificate** in `artifacts/verify.py` verifies (2) at the seven integer values \(m=0,1,\ldots,6\) separately for \(\kappa=1,2\). Two polynomials of degree at most six agreeing at seven distinct arguments are identical. Thus (2) holds for every nonnegative integer \(m\); division by \(5\Delta(3p)^5\) is justified for the claimed primes \(p\ge5\) only. Combining (1) and (2) simplifies to the displayed closed forms. This is a complete finite-algebra proof of the formulas, not an extrapolation from tested primes.

## Verification
Run `python3 artifacts/verify.py` from the extracted package root using Python's standard library. It first checks all 14 polynomial-interpolation nodes with exact integers; independently integrates the fourth power interval by interval for all 123 primes below 700; and checks the closed limiting-moment formulas as exact rational identities for five values of \(q\). A successful execution prints `POLYNOMIAL_CERTIFICATE_OK`, `DIRECT_PRIME_CHECKS_OK`, `CONTINUOUS_MOMENT_FORMULAS_OK`, then `VERIFY_OK`. The infinite claims rely on the explicit polynomial degree bound and coupling argument, not on the numerical checks alone.

## Relationship to prior work
Steven Brown, *On the calculation of an integral introduced by Hubert Delange* (arXiv:2610.14249v1, 9 October 2026), studies these exact discrepancy integrals and reduces the fourth case for general squarefree moduli to a fourfold Möbius sum involving Franel integrals. The accessible full paper presents no closed evaluation for \(3p\) and no fixed-factor semiprime limiting law. Delange's known second-moment identity is not claimed as new; the displayed limiting second moment agrees with it. Richard McIntosh, *Franel integrals of order four* (1996), treats general fourth-order Franel integrals and related sums; the full paper was compared to the fixed-semiprime closed form, which it does not explicitly present. The earlier Greaves–Hall–Huxley–Wilson *Multiple Franel integrals* (1993) is directly relevant foundational literature, but its full text was not obtained, so implicit specialization remains a residual originality risk.

## Limitations
The exact finite-prime rational formula is established for \(3p\), not for all semiprime moduli \(pq\). The distribution result fixes \(q\) while \(p\) tends to infinity; the displayed uniform bound is not useful when \(q/p\) fails to be small. No independent audit has been performed. A classical multiple-Franel-integral formula might imply this exact specialization after substantial simplification; such potential implicit coverage is not ruled out by negative searches alone.

## References
1. Steven Brown, *On the calculation of an integral introduced by Hubert Delange*, arXiv:2610.14249v1, 2026-10-09. https://arxiv.org/abs/2610.14249
2. Richard J. McIntosh, *Franel integrals of order four*, Journal of the Australian Mathematical Society A **60** (1996), 192–203. https://doi.org/10.1017/S1446788700037599
3. G. R. H. Greaves, R. R. Hall, M. N. Huxley and J. C. Wilson, *Multiple Franel integrals*, Mathematika **40** (1993), 51–70. https://doi.org/10.1112/S0025579300013711
4. H. Delange, *Sur la distribution des fractions irréductibles de dénominateur n ou de dénominateur au plus égal à x* (1968), as referenced in Brown (2026).
