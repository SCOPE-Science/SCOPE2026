# A mixed prime-power criterion for the prime-base binomial congruence

## Finding

Let \(q\) and \(p\ge5\) be distinct primes, and let \(t,e\ge1\) be integers. Define
\[
n=q^tp^e,\quad r=\left\lfloor\frac{e-1}{3}\right\rfloor,\quad
C_t=\binom{q^{t+1}}{q^t},\quad
B_{t,r}=\binom{q^{t+1}p^r}{q^tp^r}.
\]
Write \(s_q(k)\) for the sum of base-\(q\) digits of \(k\). Then
\[
\binom{qn}{n}\equiv q^n\pmod n
\]
**if and only if** all the following hold:

1. \(C_t\equiv q^{q^t}\pmod p\);
2. \(B_{t,r}^{p-1}\equiv1\pmod{p^e}\);
3. \(s_q((q-1)p^e)\ge(q-1)t\).

For the first three \(p\)-power layers \(1\le e\le3\), one has \(r=0\) and \(B_{t,r}=C_t\), giving a test that needs only the fixed binomial integer \(C_t\), one exponentiation modulo \(p^e\), and a digit sum. At \(e=4\) the actual binomial lift \(B_{t,1}\) generally cannot be replaced by \(C_t\).

In particular the values \(n=1127,775,3875\), with respective parameters \((q,t,p,e)=(23,1,7,2),(31,1,5,2),(31,1,5,3)\), satisfy the displayed binomial congruence. These are verified instances, not an assertion of infinite solution counts.

## Assumptions and scope

Throughout \(p\ge5\) is prime, \(q\ne p\) is prime, and \(t,e\) are positive integers. The congruence is in ordinary integers modulo the composite modulus \(q^tp^e\). The digit sum is computed without leading zeros. For a prime \(\ell\), \(v_\ell\) is its additive valuation on nonzero integers. No hypothesis of primality on the binomial integers \(C_t,B_{t,r}\) is imposed; the first criterion ensures they are units modulo \(p\).

## Proof

**The \(q\)-part.** Since \(n=q^tp^e\), the integer \(q^n\) is zero modulo \(q^t\). Legendre's factorial valuation formula gives
\[
 v_q\!\left(\binom{qn}{n}\right)
 =\frac{s_q(n)+s_q((q-1)n)-s_q(qn)}{q-1}
 =\frac{s_q((q-1)p^e)}{q-1}.
\]
Indeed multiplication by a power of \(q\) only appends zeros in base \(q\), and \(s_q(qn)=s_q(n)\). Thus the desired congruence modulo \(q^t\) is exactly condition (3). This is an equality of valuations and entails no unproved cancellation.

**The \(p\)-part.** The Davis--Webb binomial prime-power congruence, as also proved by Meštrović [2], states for any nonnegative integers \(u\ge v\), prime \(p\ge5\), and integer \(e\ge1\),
\[
\binom{up^e}{vp^e}\equiv
\binom{up^r}{vp^r}\pmod{p^e},\qquad
r=\left\lfloor\frac{e-1}{3}\right\rfloor.
\]
Substitution \(u=q^{t+1}\), \(v=q^t\) shows
\[
\binom{qn}{n}\equiv B_{t,r}\pmod{p^e}.
\]
Lucas's theorem for multiples of \(p\) gives \(B_{t,r}\equiv C_t\pmod p\).

For any \(p\)-adic unit \(z\), let \(\omega_p(z)\) denote the unique \((p-1)\)-st root of unity congruent to \(z\pmod p\). By Hensel's lemma it exists and is unique modulo each \(p^e\). The quotient \(q/\omega_p(q)\) lies in \(1+p\mathbb Z_p\), and its \(p^e\)-th power is congruent to one modulo \(p^{e+1}\). Also \(\omega_p(q)^{p^e}=\omega_p(q)\), since \(p^e\equiv1\pmod{p-1}\). Consequently,
\[
q^{q^tp^e}\equiv\omega_p(q)^{q^t}\pmod{p^e}.
\]
The latter root is characterized uniquely modulo \(p^e\) by being a \((p-1)\)-st root of one and reducing to \(q^{q^t}\pmod p\). Hence \(B_{t,r}\equiv q^n\pmod{p^e}\) holds precisely when \(B_{t,r}\equiv q^{q^t}\pmod p\) and \(B_{t,r}^{p-1}\equiv1\pmod{p^e}\). The former is condition (1) by Lucas's theorem, and the latter is condition (2).

Finally the moduli \(q^t\) and \(p^e\) are coprime. The Chinese remainder theorem combines the two equivalences to prove the assertion.

**First-layer and fourth-layer boundaries.** If \(1\le e\le3\), then \(r=0\), so the fixed \(C_t\) suffices. At \(e=4\), consider \(q=3,t=1,p=5\): exact integer arithmetic yields
\[
\binom{45}{15}\equiv584\pmod{625},\qquad
\binom9{3}\equiv84\pmod{625},
\]
so a general substitution of \(C_t\) for the Davis--Webb lift in the fourth layer is invalid. This comparison is only a sharpness witness for the *binomial reduction*, not a claim that this modulus is a solution of the original congruence.

## Verification

The accompanying `verify.py` uses the standard-library exact `math.comb` operation to compare the complete congruence against the three conditions for 106 parameter tuples with \(q\in\{2,3,5,7,11,13,17,19,23,31\}\), \(p\in\{5,7,11,13\}\setminus\{q\}\), \(t\in\{1,2\}\), \(e\in\{1,2,3,4\}\), and \(q^{t+1}p^e\le16000\). It separately verifies the three highlighted higher-prime-power solutions and the fourth-layer comparison. It performs no floating-point computations. These finite checks are not substitutes for the infinite proof above.

For the three highlighted solutions, \(\binom{qn}{n}\pmod n\) and \(q^n\pmod n\) are, respectively, \(851\) at \(n=1127\), \(651\) at \(n=775\), and \(3751\) at \(n=3875\).

## Relationship to prior work

Guedes and Machado [1], first publicly posted June 29, 2026, prove a criterion for the **single distinct prime factor** case \(n=q^tp\), and also discuss solutions of the pure square form \(n=p^2\). This result concerns the different mixed form \(n=q^tp^e\) for all \(e\ge1\), including genuine new squared and cubed mixed-prime examples. For \(e=1\), it specializes to their prime-factor case. Their published assertions do not supply the all-exponent mixed criterion.

The modulus-compression congruence itself is classical: Davis and Webb, with a proof by Meštrović [2], established it for arbitrary binomial coefficients. It is **not** claimed as a new theorem here. The new claim is the simultaneous composite-modulus test after combining that congruence with the root-of-unity and digit-sum obstructions. A related published research finding [3] treats \(n=p^e\) (one prime factor), using a \(p\)-adic limit; that parameter family does not imply the mixed \(q^tp^e\) result. The absence of a matching search hit does not prove originality; an implicit derivation from classical congruences remains possible.

## Limitations

The reduction requires \(p\ge5\). It gives a finite decision criterion but neither an infinite family of solutions nor an optimal complexity bound for computing large binomial integers. At \(e\ge4\), \(B_{t,r}\) may be huge and genuinely depends on the lift level. This is a mathematical argument based on stated classical congruences, without independent formal verification. The full text of [2] was not available during comparison; its precise theorem was verified through its publicly available abstract. Earlier unstated consequences of related literature cannot be ruled out.

## References

[1] G. A. Guedes and R. N. Machado Junior, *Structured Solutions of Prime-Base Binomial Congruences*, arXiv:2606.30232v1, submitted June 29, 2026. https://arxiv.org/abs/2606.30232

[2] R. Meštrović, *Variations of Lucas' Theorem Modulo Prime Powers*, arXiv:1301.0252, submitted December 29, 2012. The abstract states the Davis--Webb prime-power congruence. https://arxiv.org/abs/1301.0252

[3] *Prime-power towers for the prime-base binomial congruence*, published research record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-prime-power-towers-for-the-prime-base-binomial-congruence--a71ec1d0fa28
