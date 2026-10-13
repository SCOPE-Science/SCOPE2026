# Cyclotomic generalized totients coincide with Euler’s totient only on the underlying prime powers
## Finding
Let \(m=\ell^a\ge 3\) be a prime power, where \(\ell\) is prime and \(a\ge1\), and let \(\Phi_m\) denote the \(m\)-th cyclotomic polynomial. For every integer \(n\ge2\), let \(arphi_{\Phi_m}(n)\) be the number of residues \(0\le r<n\) for which \(\gcd(\Phi_m(r),n)=1\). Then
\[
arphi_{\Phi_m}(n)=arphi(n)
\quad\Longleftrightarrow\quad
n=\ell^b	ext{ for some }b\ge1.
\]
In particular, for every non-linear prime-power cyclotomic polynomial, the generalized totient introduced by Robu agrees with the classical Euler totient on exactly one prime-power ray.

## Assumptions and scope
The index is restricted to prime powers \(m=\ell^a\ge3\). The excluded cyclotomic polynomial \(\Phi_2(X)=X+1\) is linear and gives the classical totient for every \(n\), so it is genuinely exceptional. No restriction is placed on the exponent pattern or size of \(n\).

For a prime \(p\), write \(ho_m(p)\) for the number of distinct roots of \(\Phi_m\) in \(\mathbb F_p\). The exact local root count is
\[
ho_m(p)=
egin{cases}
1,&p=\ell,\
arphi(m),&p
e\ell	ext{ and }p\equiv1\pmod m,\
0,&p
e\ell	ext{ and }p
ot\equiv1\pmod m.
\end{cases}
\]
Consequently
\[
arphi_{\Phi_m}(n)
=n\prod_{p\mid n}\left(1-rac{ho_m(p)}pight).
\]

## Proof
For any integer polynomial \(P\), the condition \(\gcd(P(r),n)=1\) is equivalent to requiring \(P(r)
ot\equiv0\pmod p\) for every prime \(p\mid n\). By the Chinese remainder theorem, the corresponding local proportions multiply, giving
\[
arphi_P(n)=n\prod_{p\mid n}\left(1-rac{ho_P(p)}pight),
\]
where \(ho_P(p)\) is the number of roots of \(P\) modulo \(p\).

Now take \(P=\Phi_m\) with \(m=\ell^a\ge3\). In characteristic \(\ell\),
\[
\Phi_{\ell^a}(X)=rac{X^{\ell^a}-1}{X^{\ell^{a-1}}-1}
\equiv (X-1)^{\ell^a-\ell^{a-1}}
=(X-1)^{arphi(m)}\pmod\ell,
\]
so \(ho_m(\ell)=1\). If \(p
e\ell\), the roots of \(\Phi_m\) in \(\mathbb F_p\) are precisely the primitive \(m\)-th roots of unity. Since \(\mathbb F_p^	imes\) is cyclic of order \(p-1\), there are \(arphi(m)\) such roots when \(m\mid p-1\), and none otherwise. This proves the displayed local root count.

Suppose next that \(arphi_{\Phi_m}(n)=arphi(n)\). The local factor for \(p=\ell\) is the same on both sides, so after cancelling it and clearing the remaining prime denominators we obtain
\[
\prod_{\substack{p\mid n\p
e\ell}}igl(p-ho_m(p)igr)
=
\prod_{\substack{p\mid n\p
e\ell}}(p-1).
	ag{1}
\]
Because \(m\ge3\), the number \(arphi(m)\) is even. Hence for every odd prime \(p
e\ell\), the factor \(p-ho_m(p)\) on the left of (1) is odd.

If \(\ell=2\), every prime occurring in (1) is odd. Thus the left side is odd, while the right side is even as soon as any such prime occurs. Therefore no prime other than \(2\) divides \(n\).

Assume now that \(\ell\) is odd. The only possible even factor on the left of (1) comes from \(p=2\), for which \(ho_m(2)=0\) and the factor is \(2\). If \(2
mid n\), parity again forces the set of primes other than \(\ell\) to be empty. If \(2\mid n\), comparing \(2\)-adic valuations in (1) shows that there can be exactly one odd prime \(q
e\ell\) besides \(2\), and then (1) reduces to
\[
2igl(q-ho_m(q)igr)=q-1.
\]
The case \(ho_m(q)=0\) is impossible. If \(ho_m(q)=arphi(m)\), then \(q=2arphi(m)-1\). But nonzero root count also requires \(m\mid q-1=2(arphi(m)-1)\). Since \(m\) is odd, this would force \(m\midarphi(m)-1\), impossible because \(0<arphi(m)-1<m\). Hence no such \(q\) exists, and again only \(\ell\) divides \(n\).

Conversely, if \(n=\ell^b\), then the only local root count is \(ho_m(\ell)=1\), so
\[
arphi_{\Phi_m}(\ell^b)=\ell^b\left(1-rac1\ellight)=arphi(\ell^b).
\]
This completes the classification.

## Verification
A standalone verifier evaluates cyclotomic polynomials directly and compares the defining count with the local-product formula and with the claimed equality locus. It checks the prime-power indices \(3,4,5,7,8,9,11,16,25,27\) and every \(2\le n\le400\). The extracted verifier reports:

`VERIFY_OK m_cases=10 n_limit=400 checked=3990`

This finite computation is regression evidence only. The theorem is unbounded and follows from the symbolic local-root and parity argument above.

## Relationship to prior work
Robu introduced \(arphi_P(n)\) for irreducible integer polynomials and derived the general local-product framework in service of an asymptotic lower bound. The paper’s stated main result is asymptotic and its full text does not discuss cyclotomic polynomials or classify when \(arphi_P\) coincides with the classical Euler totient. The present result specializes the local framework to the infinite family \(P=\Phi_{\ell^a}\), determines every local root count exactly, and then gives the complete coincidence set with \(arphi\).

The finite-field input is the standard factorization theory of cyclotomic polynomials: for \(p
mid m\), the roots of \(\Phi_m\) in \(\mathbb F_p\) are the primitive \(m\)-th roots of unity, so they exist exactly when \(m\mid p-1\). This standard fact supplies a local ingredient but does not imply the global coincidence classification.

## Limitations
The theorem concerns prime-power cyclotomic indices only. Composite indices with at least two distinct prime divisors can have different behavior at primes dividing the index, so the parity argument here does not by itself classify their coincidence sets. No claim is made about equalities \(arphi_{\Phi_m}(n)=carphi(n)\) for constants \(c
e1\), nor about other irreducible polynomials.

## References
1. Vlad Robu, “A Generalisation of Euler Totient Function”, arXiv:2211.10644v1, first submitted 2022-11-19, https://arxiv.org/abs/2211.10644.
2. Rudolf Lidl and Harald Niederreiter, *Finite Fields*, standard cyclotomic factorization over finite fields; see also the finite-field factorization summary at https://en.wikipedia.org/wiki/Cyclotomic_polynomial.
