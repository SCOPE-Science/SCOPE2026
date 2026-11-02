# Four Thue–Morse progressions of three-square obstructions for five-colored binary partitions

## Finding

Let \(b_5(n)\) count partitions of the nonnegative integer \(n\) into powers of two, with five independently available colors for every part, and put \(t(k)=(-1)^{s_2(k)}\), where \(s_2(k)\) is the sum of the binary digits of \(k\). For **every** integer \(k\ge0\) and every \(r\in\{48,49,52,53\}\),

\[
b_5(64k+r)\equiv16+12t(k)\pmod{32}.
\]

Consequently, on each of these four arithmetic progressions, \(b_5(64k+r)\) fails to be representable as a sum of three integer squares **if and only if** \(t(k)=1\). The union of these explicit obstruction families has natural density exactly \(1/32\). In particular, the set of all indices \(n\) for which \(b_5(n)\) is not a sum of three integer squares has lower asymptotic density at least \(1/32\).

## Assumptions and scope

All congruences are in ordinary integer coefficients or in the formal power series rings \((\mathbb Z/8\mathbb Z)[[X]]\) and \((\mathbb Z/32\mathbb Z)[[X]]\). The definition is

\[
F(X)=\sum_{n\ge0} b_5(n)X^n=\prod_{j\ge0}(1-X^{2^j})^{-5},\qquad
T(X)=\prod_{j\ge0}(1-X^{2^j})=\sum_{k\ge0}t(k)X^k.
\]

All power series with constant term one are invertible. Three squares means \(u^2+v^2+w^2\) with arbitrary integers \(u,v,w\), including zero.

## Proof

**1. Finite six-step dissection.** Define the integer polynomial

\[
P(X)=\prod_{j=0}^{5}\left(\sum_{h=0}^{2^{6-j}-1}X^{h2^j}\right)^5,
\qquad \deg P=5\sum_{j=0}^5(64-2^j)=1605.
\]

Factoring out the first six blocks of \(F\) gives the *exact* identity

\[
F(X)=\frac{P(X)}{(1-X^{64})^{30}}F(X^{64}).
\]

For \(0\le r<64\) write \(P_r(Y)=\sum_{h\ge0}[X^{64h+r}]P(X)Y^h\). Extracting the coefficients indexed by \(64k+r\) shows

\[
\sum_{k\ge0}b_5(64k+r)Y^k
=\frac{P_r(Y)}{(1-Y)^{30}T(Y)^5}.
\]

**2. First finite polynomial certificate.** Multiplying the six explicit geometric-polynomial factors defining \(P\), and reducing their integer coefficients modulo \(32\), gives \(P_{48}\equiv P_{49}\equiv P_{52}\equiv P_{53}\equiv P_*\pmod{32}\), where the nonzero coefficients of \(P_*\) modulo \(32\) are exactly

```
(index, coefficient):
(0,28), (1,16), (3,16), (4,8), (5,16), (7,16),
(8,20), (12,16), (16,4), (17,16), (19,16),
(20,8), (21,16), (23,16), (24,12).
```

There are no remaining coefficients: \(\deg P_r\le24\) for these four residues. The included script `verify.py` reconstructs \(P\) from its factors, checks all \(1606\) coefficients and all four projections against this list.

**3. A mod-eight Mahler certificate.** Define

\[
\begin{aligned}
Q(Y)={}&1+2Y+Y^2+6Y^4+4Y^5+6Y^6+7Y^8+6Y^9+7Y^{10}\\
&+4Y^{12}+4Y^{14}+5Y^{16}+2Y^{17}+5Y^{18}+2Y^{20}\\
&+4Y^{21}+2Y^{22}+3Y^{24}+6Y^{25}+3Y^{26}.
\end{aligned}
\]

A finite calculation (included in `verify.py`) establishes in \((\mathbb Z/8\mathbb Z)[Y]\) that

\[
Q(Y)(1+Y^{32})\equiv (1-Y)^6 Q(Y^2)\pmod8.
\]

The rational formal series \(Q(Y)/(1-Y^{32})\) and \(T(Y)^6\) therefore solve the same Mahler equation \(U(Y)=(1-Y)^6U(Y^2)\) modulo \(8\), with constant term one. Comparing coefficients inductively gives uniqueness, hence

\[
T(Y)^6\equiv\frac{Q(Y)}{1-Y^{32}}\pmod8.
\]

Define \(H(Y)\) as the polynomial with nonzero coefficients modulo eight

```
(index, coefficient):
(0,1), (1,4), (3,4), (4,6), (5,4), (7,4),
(8,3), (12,4), (16,7), (17,4), (19,4),
(20,6), (21,4), (23,4), (24,5).
```

The second exact finite certificate, also checked coefficientwise in `verify.py`, is

\[
(1-Y)^{30}Q(Y)\equiv(1-Y^{32})H(Y)\pmod8.
\]

Thus \((1-Y)^{30}T(Y)^6\equiv H(Y)\pmod8\). Finally the finite coefficient lists satisfy, for all degrees including zero coefficients,

\[
P_*(Y)\equiv16(1-Y)^{24}+12H(Y)\pmod{32}.
\]

Since \(T(Y)\equiv(1-Y)^{-1}\pmod2\), multiplication by \(16\) yields \(16(1-Y)^{29}T(Y)^5\equiv16(1-Y)^{24}\pmod{32}\). Therefore

\[
P_*(Y)\equiv16(1-Y)^{29}T(Y)^5+12(1-Y)^{30}T(Y)^6\pmod{32}.
\]

Divide by the invertible series \((1-Y)^{30}T(Y)^5\). For each stated residue \(r\),

\[
\sum_{k\ge0}b_5(64k+r)Y^k
\equiv\frac{16}{1-Y}+12T(Y)\pmod{32},
\]

which proves the all-index coefficient congruence.

**4. Three squares and density.** When \(t(k)=1\) the coefficient is \(28\pmod{32}\), so it has \(2\)-adic valuation exactly two and the odd quotient is \(7\pmod8\). Legendre's three-square theorem excludes it. When \(t(k)=-1\) the coefficient is \(4\pmod{32}\), whose odd quotient is \(1\pmod8\); Legendre's theorem then supplies a three-square representation. Among the first \(K\) values of \(k\), exactly \(K/2+O(1)\) have \(t(k)=1\), since \(t(2j)=t(j)\) and \(t(2j+1)=-t(j)\) cancel in every complete adjacent pair. The four progressions are disjoint, yielding \(N/32+O(1)\) obstructed indices in their union below \(N\). This proves the asserted exact density for the explicit subset and the lower-density bound for the entire exceptional set.

## Verification

Run `python3 verify.py` with the Python 3 standard library. It recomputes all four numerator projections, both finite polynomial Mahler identities, the concluding degree-at-most-24 identity, and \(32768\) coefficients by the independent recurrence \((1-X)^5F(X)=F(X^2)\). The expected terminal message is `VERIFY_OK finite_polynomial_degree=1605 sections=4 mahler_modulus=8 target_modulus=32 checked_coefficients=32768`. These finite checks establish explicit *polynomial identities* used in the infinite proof; the extra coefficient recurrence is only a consistency test.

## Relationship to prior work

Sobolewski and Ulas, arXiv:2211.16622 (initially public 2022-11-29), give full three-square characterizations for the numbers of colors \(2^j-1\), and their Problems 7.2 and 7.4 ask for the other color counts and simpler descriptions of their modular binary-partition coefficients. Five is not of this form. Their general automaticity statement for a fixed modulus does not itself give these four explicit Thue–Morse congruences or their three-square obstruction density. Gawron, Miska, and Ulas, arXiv:1703.01955, study the general coefficients and obtain exact valuation results for color counts of the form \(2^j-1\), providing earlier arithmetic background but not the stated four-progression formula. Finite-polynomial computations here are fully spelled out for independent reproduction.

## Limitations

This finding identifies an explicit subset of exceptional indices; it **does not** determine the full set of nonrepresentable five-colored coefficients, establish that its overall natural density exists, or bound the \(2\)-adic valuations on other progressions. A bibliographic search cannot prove absolute priority. The polynomial identities are independently checkable from the supplied finite code, but no independent mathematical audit has been performed.

## References

1. B. Sobolewski and M. Ulas, *Values of binary partition function represented by a sum of three squares*, arXiv:2211.16622 (first posted 2022-11-29); *Results in Mathematics* 78, article 188 (2023), DOI: 10.1007/s00025-023-01966-8; especially Section 7, Problems 7.2 and 7.4.
2. M. Gawron, P. Miska, and M. Ulas, *Arithmetic properties of coefficients of power series expansion of products of \((1-X^{2^j})^t\)*, arXiv:1703.01955; *Monatshefte für Mathematik* 185 (2018), 307–360, DOI: 10.1007/s00605-017-1041-2.
3. Legendre's classical three-square theorem: a nonnegative integer is a sum of three integral squares precisely when it is not of the form \(4^a(8b+7)\).
