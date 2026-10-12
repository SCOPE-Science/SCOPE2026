# Exact two-adic internal congruences for every even overpartition-tuple order

## Finding

Let \(B_m(n)\) count ordered \(m\)-tuples of overpartitions into odd parts, with total sum \(n\). For every **even** integer \(m\ge2\), let \(s=\nu_2(m)\), and set
\[
 e_i=\begin{cases}3i-4,&s=1\text{ and }i\ge3,\\3i+2s-5,&s\ge2\text{ and }i\ge2.\end{cases}
\]
Then the following congruence holds coefficientwise in formal power series over the integers:
\[
 \boxed{\sum_{n\ge0}\bigl(B_m(2^in)-B_m(2^{i-1}n)\bigr)q^n\equiv 2^{e_i}\sum_{r\ge0}q^{(2r+1)^2}\pmod{2^{e_i+1}}.}
\]
Consequently every difference is divisible by \(2^{e_i}\), and for every \(n\ge0\) its two-adic valuation is *exactly* \(e_i\) precisely when \(n\) is a positive odd square (and is at least \(e_i+1\) otherwise). In particular, the modulus is best possible for every permitted \(m,i\). This establishes the even-order polynomial-valuation recursion posed as Conjecture 6.2 by Saikia and Talukdar, and makes its conditional constants explicit: \(c_m=-4\) if \(s=1\), and \(c_m=2s-5\) if \(s\ge2\).

## Assumptions and scope

Everything takes place in \(\mathbb Z[[q]]\) and \(\mathbb Z[x]\); no analytic convergence assumption is needed. Write
\[
 A(q)=\prod_{j\ge1,\ j\text{ odd}}\frac{1+q^j}{1-q^j},\quad
 \xi=A(q)^4,\quad U\bigl(\sum c_nq^n\bigr)=\sum c_{2n}q^n.
\]
Thus \(\sum_{n\ge0}B_m(n)q^n=A(q)^m\). Define the Chebyshev polynomials \(T_0=1,T_1=x,T_{j+1}=2xT_j-T_{j-1}\), and the integer-linear operator \(\mathcal S(x^j)=T_{2j}(x)\). For even \(m\), put \(h=m/2\); after the first extraction \(U(A^m)=T_h(\xi)\) and \(U(P(\xi))=(\mathcal S P)(\xi)\) for every \(P\in\mathbb Z[x]\). These identities and \(\xi\in1+8q\mathbb Z[[q]]\) follow from the theta-function identities in [1, Section 6 and Lemmas 2.1–2.2].

## Proof

**1. The lifted polynomial operator.** Put \(z=x-1\) and
\[
 \mathcal F(R)=\frac{\mathcal S((x-1)R)}{x-1}.
\]
This is an integer polynomial because \((\mathcal SP)(1)=P(1)\). Let \(H_j(t)\) be given by \(H_0=2,H_1=t\) and \(H_j=t(H_{j-1}+H_{j-2})\). The identity \(T_j((u+u^{-1})/2)=(u^j+u^{-j})/2\) shows
\[
 \mathcal F(z^j)=\frac{H_{j+1}(4z(z+2))}{2z},\qquad j\ge0.
\]
Indeed, the quantities \(u^2-1\) and \(u^{-2}-1\) have sum \(4z(z+2)\) and product \(-4z(z+2)\), giving the displayed recurrence. In particular,
\[
 \mathcal F(1)=4+2z,\qquad
 \mathcal F(z)=8+36z+32z^2+8z^3.
\]
Furthermore, for every \(j\ge2\), \(\mathcal F(z^j)\) has zero constant coefficient, all its coefficients are multiples of \(8\), and its linear coefficient is a multiple of \(32\). To verify this without an unbounded coefficient computation, use \(H_3=t^3+3t^2\), \(H_4=t^4+4t^3+2t^2\) for \(j=2,3\). For \(j\ge4\), the recurrence gives \(H_{j+1}\in t^3\mathbb Z[t]\), hence \(\mathcal F(z^j)\in32z^2\mathbb Z[z]\). The linear coefficients for \(j=2,3\) are respectively \(96\) and \(64\).

**2. A stable lattice with an exact gain of three.** Consider all integer polynomials of the form
\[
 R=2b+az+\sum_{j\ge2}c_jz^j,\qquad b,a\text{ odd},\quad b\equiv a\pmod4.
\]
For such \(R\), the preceding formulas give
\[
 \mathcal F(R)=8(b+a)+(4b+36a+32K)z+\sum_{j\ge2}8d_jz^j
\]
for integers \(K,d_j\). Thus \(\mathcal F(R)=8R_*\), where \(R_*\) belongs to the same class: its constant term is \(2b_*\) with \(b_*=(b+a)/2\) odd, and its linear coefficient is \(a_*=(b+9a)/2+4K\), also odd, with \(a_*\equiv b_*\pmod4\). In particular, every iterate gains **exactly** three powers of \(2\) in the coefficient gcd, the value at \(1\) has one additional power, and the derivative at \(1\) has no additional power.

**3. Uniform initialization.** For every even \(m\), define
\[
 R_2(x)=\frac{\mathcal S(T_h)(x)-T_h(x)}{x-1},\qquad h=m/2.
\]
This represents the difference of the second and first extracted polynomials: for \(m\equiv2\pmod4\) start with \(P_1=T_h\), and for \(4\mid m\) start with \(P_0=x^{m/4}\), so \(P_1=\mathcal S(P_0)=T_h\). Hence the polynomial for all subsequent differences is \(R_i=\mathcal F^{i-2}(R_2)\) and
\[
 \sum_{n\ge0}\bigl(B_m(2^in)-B_m(2^{i-1}n)\bigr)q^n=(\xi-1)R_i(\xi).
\]
Differentiating the Chebyshev recurrence, or using \(T_h^{(k)}(1)=h^2\prod_{r=1}^{k-1}(h^2-r^2)/(2k-1)!!\) for \(k\ge1\), gives the *exact* values
\[
 R_2(1)=\frac{h^2(4h^2+5)}3,\qquad
 R_2'(1)=\frac{h^2(h^2+3)(4h^2-1)(4h^2+101)}{630}.
\]
For completeness, these follow by writing \(T_h=\sum_j t_jx^j\) and using \(\mathcal S(T_h)'(1)=4\sum_jj^2t_j\) and \(\mathcal S(T_h)''(1)=(16\sum_jj^4t_j-4\sum_jj^2t_j)/3\), then dividing \(\mathcal S(T_h)-T_h\) by \(x-1\).

If \(h\) is odd, the displayed value \(R_2(1)\) is odd. Writing \(R_2=a_0+a_1z+\cdots\), one has \(a_0\) odd; Step 1 yields \(R_3=\mathcal F(R_2)\in2\mathbb Z[z]\), with constant term \(4a_0+8a_1\) and linear term \(2a_0+36a_1+32K\). Consequently \(R_3/2\) belongs to the stable class in Step 2, with \(b=a_0+2a_1\) and \(a=a_0+18a_1+16K\). Thus for every \(i\ge3\),
\[
 \nu_2(R_i)=1+3(i-3)=3i-8,\quad
 \nu_2(R_i(1))=3i-7,\quad \nu_2(R_i'(1))=3i-8.
\]

If \(h=2^tu\), where \(t\ge1\) and \(u\) is odd, then \(T_{2^t}(x)-1\in2^{2t-1}(x-1)\mathbb Z[x]\): start with \(T_2(x)-1=2(x-1)(x+1)\) and induct using \(T_{2v}-1=2(T_v-1)(T_v+1)\), where \(T_{2^t}+1\) is even. Composing with \(T_u\) gives \(T_h-1\in2^{2t-1}(x-1)\mathbb Z[x]\). Applying \(\mathcal S\), which preserves coefficient divisibility and vanishing at \(x=1\), gives \(R_2\in2^{2t-1}\mathbb Z[x]\). The displayed exact value formulas additionally imply
\[
 \frac{R_2(1)}{2^{2t}}\equiv3\pmod4,\qquad
 \frac{R_2'(1)}{2^{2t-1}}\equiv3\pmod4.
\]
For the derivative, after dividing by \(2^{2t-1}\), the expression is \(u^2(h^2+3)(4h^2-1)(4h^2+101)/315\), whose reduction modulo \(4\) is \(3\). Therefore \(R_2/2^{2t-1}\) is in the stable class. For all \(i\ge2\),
\[
 \nu_2(R_i)=2t-1+3(i-2)=3i+2t-7,
\quad\nu_2(R_i(1))=3i+2t-6,
\quad\nu_2(R_i'(1))=3i+2t-7.
\]
Since \(s=\nu_2(m)=t+1\), this gives \(\nu_2(R_i)+4=3i+2s-5\). The case of odd \(h\) gives \(\nu_2(R_i)+4=3i-4\).

**4. The exact coefficient profile.** In either case \(R_i=2^v(2b+az+\cdots)\) with \(b\) odd and \(v=\nu_2(R_i)\). Since \(\xi-1\in8q\mathbb Z[[q]]\),
\[
 \frac{(\xi-1)R_i(\xi)}{2^{v+4}}\equiv\frac{\xi-1}{8}\pmod2.
\]
The source's theta identity (Lemma 2.2) states \((\xi-1)/8\equiv\sum_{r\ge0}q^{(2r+1)^2}\pmod2\). Multiplication by \(2^{v+4}\) proves the theorem and all valuation claims. \(n=0\) contributes zero on both sides.

## Verification

Run `python3 verification/verify.py` using Python 3 and no third-party dependencies. It checks the exact polynomial iterates and stable-lattice conditions for even \(m=2,4,\dots,24\) through extraction level \(i=6\) using arithmetic modulo \(2^{48}\). Independently, a truncated odd-parts product followed by integer-series exponentiation verifies the stated coefficientwise congruence for \(m\in\{2,4,6,8,10,12,16,24\}\) through the accessible indices of \(n\le256/2^i\). The verification output is included. The infinite theorem follows from the explicit algebraic induction above, not from these finite checks.

## Relationship to prior work

Saikia and Talukdar [1, Section 6] establish the polynomial recursion, conjecture the three-power growth in their Conjecture 6.2, and state the even-order congruences conditionally in Corollary 6.3. Their computations suggest the constants depend only on \(\nu_2(m)\); the present proof supplies both a uniform inductive mechanism and explicit constants and odd-square coefficients for **all** even \(m\). Their proved Theorem 1.1 applies to **odd** \(m\), not the present range. Earlier results by Adiga and Dasappa [2] establish multiple congruences for overpartition **pairs** (\(m=2\)), while Saikia, Sarma and Sellers [3] establish several congruences for particular numbers of tuple components and progressions; those results do not imply the displayed theorem uniformly for all even \(m\) and arbitrary \(i\). Particular special cases of the new congruence may overlap previously known congruences.

## Limitations

The claimed congruence concerns differences at successive dyadic indices, not the absolute valuations of individual \(B_m(n)\), and it does not extend to odd \(m\) without the different normalization of [1]. Independent mathematical validation has not been performed. Overlap searches do not exclude inaccessible or unindexed equivalent work; exact pair-case instances have related antecedents in [2].

## References

[1] Manjil P. Saikia and Prabal Talukdar, *Internal congruences modulo powers of 2 for overpartition tuples with odd parts*, arXiv:2609.11806v1 (10 September 2026), Sections 2 and 6, https://arxiv.org/html/2609.11806v1 .

[2] Chandrashekar Adiga and Ranganatha Dasappa, *On overpartition pairs into odd parts modulo powers of 2*, Discrete Mathematics 341 (2018), 3141–3147, doi:10.1016/j.disc.2018.08.002 .

[3] Manjil P. Saikia, Abhishek Sarma and James A. Sellers, *Arithmetic properties modulo powers of 2 for overpartition k-tuples with odd parts*, Journal of the Ramanujan Mathematical Society 40 (2025), 107–123, preprint arXiv:2312.12011, https://arxiv.org/pdf/2312.12011 .
