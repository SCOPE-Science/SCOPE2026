# Exact squarefree endpoint profile for the cubic moment curve
## Finding
Let \(N>1\) be squarefree with \(\gcd(N,6)=1\), and for \(d\ge 3\) define
\[
\mathcal M_N^{(d)}=\{(t,t^2,\ldots,t^d):t\in\mathbb Z_N\}\subseteq\mathbb Z_N^d.
\]
Write
\[
\mathcal C_6(S)=\sup_{\substack{f\ne0\\ \operatorname{supp}(f)\subseteq S}}
\frac{\|\widehat f\|_\infty}{\|\widehat f\|_6},
\]
with the unitary Fourier normalization used in Iosevich--Li--Yu. Then
\[
\mathcal C_6(\mathcal M_N^{(d)})
=
N^{-(d-3)/6}
\prod_{p\mid N}\left(6-\frac9p+\frac4{p^2}\right)^{-1/6}.
\]
Consequently, for the cubic moment curve \(\mathcal M_N^{(3)}\), along any sequence of squarefree moduli coprime to \(6\) with \(N\to\infty\), uniform \(\ell^6\) spectral synthesis holds if and only if
\[
\omega(N)\longrightarrow\infty,
\]
where \(\omega(N)\) is the number of distinct prime divisors. Thus the critical exponent fails along primes but holds along squarefree moduli containing an increasing number of prime factors.

## Assumptions and scope
The modulus is squarefree and every prime divisor exceeds \(3\). The result concerns the moment curve in ambient dimension \(d\ge3\) and the sixth Fourier moment. The endpoint statement is critical only when \(d=3\); for \(d>3\), the explicit factor \(N^{-(d-3)/6}\) already forces decay.

For a positive integer \(s\), let \(J_{s,d}(N)\) denote the number of ordered tuples
\[
(t_1,\ldots,t_s,u_1,\ldots,u_s)\in\mathbb Z_N^{2s}
\]
satisfying
\[
\sum_{j=1}^s t_j^k=\sum_{j=1}^s u_j^k\pmod N
\qquad (1\le k\le d).
\]

## Proof
Because \(N\) is squarefree, the Chinese remainder theorem separates all congruence equations prime by prime:
\[
J_{3,d}(N)=\prod_{p\mid N}J_{3,d}(p).
\]
Fix \(p>3\). Equality of the first three power sums of two triples over \(\mathbb F_p\) determines equality of their three elementary symmetric functions. Indeed Newton's identities give
\[
e_1=P_1,\qquad
2e_2=e_1P_1-P_2,\qquad
3e_3=e_2P_1-e_1P_2+P_3,
\]
and \(2,3\) are invertible modulo \(p\). Hence two triples satisfy the equations for \(k=1,2,3\) exactly when they are two orderings of the same multiset. Once the elementary symmetric functions agree, the two triples are roots of the same monic cubic, so all higher power sums agree as well. Thus \(J_{3,d}(p)=J_{3,3}(p)\) for every \(d\ge3\).

Count ordered pairs of ordered triples with the same multiset. If the multiset has three distinct elements, there are \(\binom p3\) choices and \(6^2\) ordered pairs. If exactly two entries coincide, there are \(p(p-1)\) choices of repeated and singleton values and \(3^2\) ordered pairs. If all entries coincide, there are \(p\) choices and one ordered pair. Therefore
\[
J_{3,d}(p)
=
36\binom p3+9p(p-1)+p
=
p(6p^2-9p+4).
\]
Multiplying over the prime divisors of \(N\) yields
\[
J_{3,d}(N)
=
N^3\prod_{p\mid N}\left(6-\frac9p+\frac4{p^2}\right).
\]

Iosevich--Li--Yu prove that affine transitivity of the moment curve makes the indicator extremal and gives the exact identity
\[
\mathcal C_{2s}(\mathcal M_N^{(d)})
=
\left(N^{d-2s}J_{s,d}(N)\right)^{-1/(2s)}.
\]
Substituting \(s=3\) and the preceding count gives
\[
\mathcal C_6(\mathcal M_N^{(d)})
=
N^{-(d-3)/6}
\prod_{p\mid N}\left(6-\frac9p+\frac4{p^2}\right)^{-1/6}.
\]

For \(p\ge5\),
\[
\frac{109}{25}
\le
6-\frac9p+\frac4{p^2}
<
6.
\]
Hence, on squarefree moduli coprime to \(6\), the product of local factors tends to infinity exactly when \(\omega(N)\to\infty\). In dimension \(d=3\), the exact synthesis criterion \(\mathcal C_6(\mathcal M_N^{(3)})\to0\) is therefore equivalent to \(\omega(N)\to\infty\).

## Verification
The accompanying verifier exhaustively computes the first-three-power-sum fibers over \(\mathbb F_p\) for \(p=5,7,11\), checks the exact local formula
\[
J_{3,3}(p)=p(6p^2-9p+4),
\]
checks that the fiber multiplicities are exactly \(1,3,6\) according to triple multiplicity type, and checks the Chinese-remainder product formula symbolically for representative squarefree moduli. These computations are finite consistency checks; the general theorem is proved algebraically above.

## Relationship to prior work
Iosevich, Li, and Yu reduce exact moment-curve synthesis constants to the congruence counts \(J_{s,d}(N)\), and explicitly identify precise growth and dependence on general composite moduli as further work. Their result supplies the symmetry identity used above but does not evaluate the cubic sixth moment for squarefree composite moduli.

Hickman and Wright establish prime-power growth information for moment-curve restriction and, in particular, endpoint blowup phenomena over powers of a fixed prime. Their results do not give the squarefree exact product above or the resulting if-and-only-if criterion in terms of \(\omega(N)\).

The new point is the exact critical arithmetic profile for the first cubic endpoint: prime moduli and squarefree highly composite moduli have opposite \(\ell^6\) synthesis behavior even though they lie on the same geometric moment curve.

## Limitations
The argument uses squarefreeness to factor the solution count without ramified local analysis, and it excludes primes \(2\) and \(3\) so that the first three power sums determine the elementary symmetric functions by Newton identities. It does not determine the exact sixth moment for prime powers or arbitrary nonsquarefree moduli. Those ramified local factors are the natural remaining case.

## References
A. Iosevich, Z. Li, and K. Yu, “Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\),” arXiv:2609.25404v1, 2026.

J. Hickman and J. Wright, “The Fourier restriction and Kakeya problems over rings of integers modulo \(N\),” Discrete Analysis 2018:11; arXiv:1801.03176v2.
