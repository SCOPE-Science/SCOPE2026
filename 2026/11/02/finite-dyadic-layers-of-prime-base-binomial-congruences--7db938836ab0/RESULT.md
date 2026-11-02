# Finite dyadic layers of prime-base binomial congruences

## Finding
For every positive integer \(e\), odd prime \(q\), and positive integer \(t\), put \(n=2^e q^t\) and \(s_q(m)\) for the sum of the base-\(q\) digits of \(m\). If
\[
\binom{qn}{n}\equiv q^n\pmod n,
\]
then necessarily
\[
\boxed{2\le t\le \frac{s_q((q-1)2^e)}{q-1},\qquad q<2^e.}
\]
In particular, for each fixed dyadic valuation \(e\), only finitely many solutions in this prime-power family exist, with an explicit finite enumeration of all candidates. The complete first four dyadic layers are
\[
\begin{array}{c|c}
e&\{n=2^e q^t:\ q\text{ odd prime},\ t\ge1,\ \binom{qn}{n}\equiv q^n\pmod n\}\\\hline
1&\varnothing\\
2&\{36\}\\
3&\varnothing\\
4&\{400\}.
\end{array}
\]
The individual numbers \(36\) and \(400\) were already listed in the applicable integer-sequence databases; the assertion concerns the **complete dyadic fibers** and the uniform prime-base finiteness obstruction, not discovery of these integers.

## Assumptions and scope
Only positive \(e,t\) and odd prime bases \(q\) are considered. Here \(\binom{qn}{n}\) is the usual integer binomial coefficient, and congruences are ordinary integer congruences. The upper bound on \(t\) is an integer because the digit sum of \((q-1)2^e\) is divisible by \(q-1\). The result classifies all such solutions with \(1\le e\le4\), but supplies a finite criterion rather than a closed solution list for general \(e\).

## Proof
**1. Exact prime-base valuation.** Legendre's digit-sum formula, together with \(s_q(qm)=s_q(m)\), gives
\[
\begin{aligned}
\nu_q\!\left(\binom{qn}{n}\right)
 &=\frac{s_q(n)+s_q((q-1)n)-s_q(qn)}{q-1}\\
 &=\frac{s_q((q-1)2^e)}{q-1}.
\end{aligned}
\]
Since \(n\ge t\), the right side \(q^n\) is divisible by \(q^t\). Thus the desired congruence modulo \(q^t\) forces \(t\le s_q((q-1)2^e)/(q-1)\); conversely, this inequality is precisely the needed condition modulo \(q^t\).

**2. The prime-base exponent cannot be one.** Modulo \(2\), the right side \(q^n\) is one. By Lucas' theorem, appending a common block of \(e\) zero binary digits does not alter binomial parity, so
\[
\binom{q^{t+1}2^e}{q^t2^e}\equiv\binom{q^{t+1}}{q^t}\pmod2.
\]
At \(t=1\), this is \(\binom{q^2}{q}\). Let \(h=\nu_2(q-1)\ge1\). Both \(q\) and \(q(q-1)\) have binary digit one in position \(h\), since
\[
q\equiv 1+2^h\pmod{2^{h+1}},\qquad
q(q-1)\equiv2^h\pmod{2^{h+1}}.
\]
Adding \(q+q(q-1)=q^2\) therefore entails a carry. By Lucas' theorem, equivalently Kummer's parity criterion, \(\binom{q^2}{q}\) is even. It cannot equal the odd right side modulo \(2\). Hence \(t\ne1\), and \(t\ge2\).

**3. Finite support at fixed dyadic valuation.** If \(q>2^e\), then the two base-\(q\) digits of \((q-1)2^e\) are \(2^e-1\) and \(q-2^e\), so
\[
s_q((q-1)2^e)=(2^e-1)+(q-2^e)=q-1.
\]
Step 1 would force \(t\le1\), contrary to Step 2. Thus \(q\le2^e\). Because \(q\) is an odd prime and \(2^e\) is a power of two, equality is impossible: \(q<2^e\). There are finitely many such primes, and Step 1 bounds \(t\) for each of them. This proves the uniform finiteness theorem.

**4. Exact remaining test.** The Chinese remainder theorem separates the original congruence modulo \(n\) into the conditions modulo \(q^t\) and \(2^e\). The first is exactly Step 1's digit-sum inequality. For the second, \(q^{q^t2^e}\equiv1\pmod{2^e}\) because \(q\) is odd and \(q^t2^e\) is a multiple of \(\varphi(2^e)\) for \(e\ge2\); the claim is also immediate for \(e=1\). Hence the exact finite test is
\[
\binom{q^{t+1}2^e}{q^t2^e}\equiv1\pmod{2^e}.
\]
For \(e\le4\), enumerate all odd primes \(q<2^e\) and positive \(t\) satisfying the digit-sum condition. The resulting residues for \((q,t)\), in order, are:
\[
\begin{array}{c|l|l}
e & (q,t) \text{ surviving the digit bound} & \binom{q^{t+1}2^e}{q^t2^e}\bmod2^e\\\hline
1& \text{none}&\text{none}\\
2&(3,1),(3,2)&0,1\\
3&(3,1),(3,2),(5,1),(7,1),(7,2)&4,5,2,0,6\\
4&(3,1),(3,2),(5,1),(5,2),(7,1),(7,2),(11,1),(13,1)&4,13,10,1,8,6,8,8
\end{array}
\]
Only \((e,q,t)=(2,3,2)\) and \((4,5,2)\) have residue one; thus only \(n=36\) and \(n=400\) survive. Direct full-modulus checks are \(\binom{108}{36}\equiv3^{36}\equiv9\pmod{36}\) and \(\binom{2000}{400}\equiv5^{400}\equiv225\pmod{400}\). This completes the four-layer classification.

## Verification
Run `python3 verify.py`, which deterministically performs exact prime enumeration, digit-sum checks, full integer binomial coefficient computation of all surviving candidates with \(e\le4\), and the full-modulus positive checks. The verifier also independently tests the exact \(q\)-adic valuation formula and binary-carry obstruction over a finite range. Those finite checks corroborate the argument; the unrestricted bound on \(q\) and \(t\) is established by Steps 1–3 and not by experiment.

## Relationship to prior work
Guedes and Machado, *Structured Solutions of Prime-Base Binomial Congruences* (first publicly submitted June 29, 2026), classify the structured branch \(n=q^t p\) with \(p\ne q\) prime via an independent modular and base-\(q\) digit-sum condition (Theorem 3.1), and treat isolated squares \(p^2\) (Theorem 6.2). Their theorem does not state the uniform dyadic bound \(q<2^e\) at general fixed \(e\ge2\). The formerly published classification of certain odd-prime-power towers assumes the second prime is at least five and does not include the dyadic branch. The OEIS entries A080469 and A109760 already record the numerical solutions \(36\) and \(400\), respectively; their lists do not establish that these exhaust an **infinite** restricted family at a prescribed dyadic valuation.

## Limitations
This theorem concerns only the shape \(n=2^e q^t\) with \(q\) an odd prime and is not an assertion about all solutions or other cofactors. The general \(e\) criterion still requires finite congruence testing; it does not assert existence in infinitely many dyadic layers or give their exact counts. The parity argument is a standard carry application; the contribution is its combination with the prime-base digit valuation to obtain a uniform structural exclusion and complete initial layers. Bibliographic priority remains subject to older or unindexed equivalences.

## References
- G. A. Guedes and R. N. Machado Junior, *Structured Solutions of Prime-Base Binomial Congruences*, arXiv:2606.30232, first public version June 29, 2026; especially Theorem 3.1 and Section 6. https://arxiv.org/abs/2606.30232
- OEIS A080469, composite solutions for base three, https://oeis.org/A080469.
- OEIS A109760, composite solutions for base five, https://oeis.org/A109760.
- E. Lucas, classical parity congruence for binomial coefficients; E. Kummer, carry characterization of binomial valuations.
