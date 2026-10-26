# Sharp two-adic stabilization of two-colored binary partitions

## Finding
Let \(b_2(N)\) be the coefficient of \(x^N\) in the formal generating series
\[B(x)=\prod_{j\ge0}(1-x^{2^j})^{-2}.\]
For every integer \(k\ge3\) and integer \(n\ge1\),
\[\boxed{\nu_2(b_2(2^{k+1}n)-b_2(2^{k-1}n))=k+\nu_2(n).}\]
For \(n=0\), the difference is zero. In particular the congruence in Gawron--Miska--Ulas, Conjecture 5.5, holds for parameter \(m=1\); at every positive index the 2-adic exponent is exact, not merely a lower bound.

## Assumptions and scope
All series are formal integer-coefficient power series; all indices are nonnegative integers, except \(n\ge1\) in the valuation identity. Let \(\nu_2\) be the exponent of two in a nonzero integer. Denote \(\mathbb Z_{(2)}=\{a/b:a,b\in\mathbb Z,\ b\text{ odd}\}\). A polynomial congruence modulo two is coefficientwise over this ring. The statement concerns two colors only; no assertion for other numbers of colors follows.

## Proof
**1. Coefficient-decimation polynomials.** Write \(\mathcal U(\sum_{r\ge0}c_rx^r)=\sum_{r\ge0}c_{2r}x^r\). The functional equation \(B(x)=(1-x)^{-2}B(x^2)\) implies \(\mathcal U(H(x)B(x))=\mathcal U((1-x)^{-2}H(x))B(x)\). Starting at \(H_0(x)=1\), define \(H_j(x)\) by \(\mathcal U^j B(x)=H_j(x)B(x)\). For \(j\ge1\), the coefficient \(p_j(n)=[x^n]H_j(x)\) is a polynomial in \(n\) and obeys
\[p_1(n)=2n+1,\qquad p_{j+1}(n)=\sum_{r=0}^{2n}(2n-r+1)p_j(r).\]
The explicit first and fourth intermediate polynomials are calculated by this finite algebraic recurrence. Its output gives
\[p_4(n)-p_2(n)=8R(n)h_2(n),\quad R(n)=\binom{n+2}{3},\]
\[h_2(n)=\frac{(2n+1)(512n^3+1568n^2+1596n+489)}{105}.\]
Thus \(h_2\in\mathbb Z_{(2)}[n]\) and \(h_2\equiv1\pmod2\).

**2. A polynomial divisibility lemma.** Define \(T(f)(n)=\sum_{r=0}^{2n}(2n-r+1)f(r)\). We prove for every \(h\in\mathbb Z_{(2)}[n]\) that
\[T(Rh)(n)=2R(n)(\mathcal Lh)(n),\qquad \mathcal Lh\in\mathbb Z_{(2)}[n],\qquad \mathcal L1\equiv1\pmod2.\]
It suffices by linearity to take \(h(r)=(r+1)^j\), with \(j\ge0\). Set \(s=n+1\) and \(m=2s\), and write
\[F_q(m)=\sum_{t=0}^{m-1}t^q,\qquad D_q(m)=F_{q+2}(m)-F_q(m)\quad(q\ge1).\]
These finite sums are rational polynomials in \(m\). Substitution \(t=r+1\) gives
\[\frac{T(R(r)(r+1)^j)(n)}{2R(n)}=\frac{mD_{j+1}(m)-D_{j+2}(m)}{2s(s^2-1)},\quad m=2s.\]
We first establish \(D_q(2s)\in2s\mathbb Z_{(2)}[s]\) for all integers \(q\ge2\). Write \(B_e\) for Bernoulli numbers with \(B_1=-1/2\). Faulhaber's formula gives the coefficient of \(s^e\) in \(D_q(2s)\):
\[\frac{2^e}{e}\left(\binom{q+2}{e-1}B_{q+3-e}-\binom q{e-1}B_{q+1-e}\right)\quad(e\ge1),\]
with absent terms taken as zero. The standard Bernoulli denominator property gives \(B_{2a}\equiv-1/2\pmod{\mathbb Z_{(2)}}\) for \(a\ge1\), \(B_1=-1/2\), and \(B_{2a+1}=0\) for \(a\ge1\). For \(e=1\), the two Bernoulli terms differ by a 2-adic integer. For \(e=2\), they give a 2-adic integer after the displayed binomial weights; the only exceptional small index \(q=2\) contributes \(4B_3-2B_1=1\). For \(e\ge3\), \(2^e/e\) has valuation at least two, while every Bernoulli number has valuation at least minus one. Therefore every coefficient of \(D_q(2s)\) is divisible by two, and the constant coefficient vanishes. The asserted divisibility follows.

Consequently, \(A_j(2s)/(2s)\in\mathbb Z_{(2)}[s]\), where \(A_j(m)=mD_{j+1}(m)-D_{j+2}(m)\). This polynomial vanishes at \(s=1\), since the only potentially nonzero summands \(t=0,1\) of \(D_q(2)\) both vanish. It also vanishes at \(s=-1\): extending Faulhaber polynomials to negative arguments gives \(D_q(-2)=-3(-2)^q\), and hence \(A_j(-2)=0\). Division by the monic polynomial \(s^2-1\) therefore stays inside \(\mathbb Z_{(2)}[s]\). This proves \(\mathcal Lh\in\mathbb Z_{(2)}[n]\) for every polynomial \(h\). Direct summation yields
\[(\mathcal L1)(n)=\frac{(2n+1)(2n+3)}5\equiv1\pmod2.\]

**3. Induction on decimation depth.** Put \(d_j(n)=p_{j+2}(n)-p_j(n)\), for \(j\ge2\). As \(d_{j+1}=T(d_j)\), the initial identity and the lemma give
\[d_j(n)=2^{j+1}R(n)h_j(n),\qquad h_j\in\mathbb Z_{(2)}[n],\quad h_j\equiv1\pmod2\]
for all \(j\ge2\), inductively with \(h_{j+1}=\mathcal Lh_j\). In formal series, this yields
\[H_{j+2}(x)-H_j(x)\equiv 2^{j+1}\sum_{n\ge0}R(n)x^n\pmod{2^{j+2}}.\]
The sequence \(R(n)=\binom{n+2}{3}\) is odd exactly when \(n\equiv1\pmod4\) and \(\sum R(n)x^n=x/(1-x)^4\). Also, reducing the finite binary-product identity modulo two gives
\[B(x)\equiv(1-x)^2=1+x^2\pmod2.\]
It follows that the coefficient of \(x^n\) in \((H_{j+2}-H_j)B/2^{j+1}\) is odd exactly when \(n\) is odd. Thus
\[\nu_2(b_2(2^{j+2}u)-b_2(2^ju))=j+1\qquad(j\ge2,\ u\ge1\text{ odd}).\]
For general \(n=2^tu\), with \(u\) odd, replace \(j\) by \(j+t\) in the last identity. Finally, setting \(k=j+1\) proves the claimed formula for every \(k\ge3\), \(n\ge1\).

## Verification
The included `verify.py` independently evaluates the integer recurrence for the two-colored partition counts and checks the valuation assertion at 1,105 pairs through the indicated range. It also checks the exact base polynomial identity and tests the rational-polynomial divisibility lemma in representative degrees. The infinite theorem is supplied by the displayed algebraic and Bernoulli argument; finite tests alone would not establish it.

## Relationship to prior work
Gawron, Miska and Ulas (2017), Section 5, Conjecture 5.5, predicts \(b_{2m}(2^{k+1}n)\equiv b_{2m}(2^{k-1}n)\pmod{2^k}\) for \(k\ge m+2\). Their Section 4 establishes other congruences; Theorem 4.13 in particular treats modulus five, while Theorem 5.4 classifies certain individual coefficient valuations. The present theorem resolves the first even-color case of their conjecture and strictly sharpens it to an exact difference valuation. Earlier literature on ordinary (single-color) binary partitions does not imply the formula for two independently colored parts. The same author's subsequent unboundedness conjecture paper concerns positive powers of the Thue--Morse series, a distinct problem.

## Limitations
The results establish only \(m=1\) of the conjecture; \(m>1\) is not addressed. The identity at \(n=0\) is a zero difference rather than a finite 2-adic valuation. The polynomial-contraction mechanism is specific to the two-color kernel. No independent mathematical audit or publication-priority determination has been performed.

## References
1. M. Gawron, P. Miska and M. Ulas, *Arithmetic properties of coefficients of power series expansion of* \(\prod_{n\ge0}(1-x^{2^n})^t\), arXiv:1703.01955v1 (2017), especially Theorem 4.13 and Conjecture 5.5; https://arxiv.org/pdf/1703.01955.
2. B. Reznick, *Some Binary Partition Functions*, in *Analytic Number Theory* (1990), DOI:10.1007/978-1-4612-3464-7_29 (ordinary binary-partition background).
3. J. Yu, W. Lei and S. Hong, *Proof of the Gawron--Miska--Ulas conjecture concerning unboundedness of coefficients...*, arXiv:2606.25825 (2026), on a different conjecture.
4. Classical von Staudt--Clausen Bernoulli denominator theorem, used in the stated special 2-adic form.
