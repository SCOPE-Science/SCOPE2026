# Exact algebraic degrees of periodic binary digit-parity series

## Finding
Let \(d\ge1\) and let \(a_0,\ldots,a_{d-1}\in\mathbb F_2\). Define \(a_{j+d}=a_j\) for all \(j\ge0\). For each \(n\ge0\), with binary digits \(b_j(n)\in\{0,1\}\), put
\[
u(n)=\bigoplus_{j\ge0}a_jb_j(n),\qquad U(x)=\sum_{n\ge0}u(n)x^n\in\mathbb F_2[[x]].
\]
Set
\[
A(T)=\sum_{j=0}^{d-1}a_jT^j,\quad B(T)=1+T^d,\quad D(T)=\gcd(A(T),B(T)),\quad E(T)=B(T)/D(T),\quad C(T)=A(T)/D(T).
\]
The gcd is monic, including \(D=B\) when \(A=0\). Write \(e=\deg E\). With \(Y=(1+x)U\), \(r=x/(1+x)\), and the Frobenius operation \(F(z)=z^2\), the identity
\[
E(F)Y=C(F)r
\]
holds as an identity in \(\mathbb F_2[[x]]\). Moreover, the polynomial
\[
P(Z)=\sum_{j=0}^{e}E_j\big((1+x)Z\big)^{2^j}
+\sum_{j\ge0}C_j\left(\frac{x}{1+x}\right)^{2^j}\quad\in\mathbb F_2(x)[Z]
\]
(where \(E_j,C_j\) denote polynomial coefficients) is irreducible and vanishes at \(Z=U(x)\). In particular, **the exact algebraic degree** is
\[
\boxed{[\mathbb F_2(x,U):\mathbb F_2(x)]=2^{\deg((1+T^d)/\gcd(A(T),1+T^d))}.}
\]
For periods of length three, the mask \(000\) has degree \(1\); \(111\) has degree \(2\); the three masks with exactly two ones have degree \(4\); and the three masks with exactly one one have degree \(8\).

As a concrete application, the sequence \(\mathcal M_2\) of Campbell and Cloitre has the period-three mask \((1,1,0)\). Its series \(U_2\) therefore has exact algebraic degree \(4\), and \(Y_2=(1+x)U_2\) satisfies the **irreducible** equation
\[
\boxed{Y_2^4+Y_2^2+Y_2=\frac{x}{1+x}.}
\]

## Assumptions and scope
All arithmetic involving \(U\), \(Y\), \(r\), \(A\), \(B\), \(C\), and \(D\) is over \(\mathbb F_2\), unless a field extension is explicitly stated. The symbol \(F\) is the Frobenius map and \(P(F)z\) means \(\sum_jP_jz^{2^j}\), not substitution of an indeterminate in a polynomial. Leading zeros in binary representations contribute zero. The period \(d\) need not be least. The assertion includes the zero mask, for which \(U=0\) and its algebraic degree is \(1\).

## Proof
**1. The exact Frobenius equation.** For each residue \(j\) modulo \(d\), let \(u_j(n)=\bigoplus_{k\ge0}a_{j+k}b_k(n)\), with associated series \(U_j(x)\) and \(Y_j(x)=(1+x)U_j(x)\). The binary-digit identities are
\[
u_j(2n)=u_{j+1}(n),\qquad u_j(2n+1)=u_{j+1}(n)+a_j.
\]
Summing even and odd indices in characteristic two gives
\[
U_j(x)=(1+x)U_{j+1}(x^2)+\frac{a_jx}{1+x^2}.
\]
Thus, since \(1+x^2=(1+x)^2\),
\[
Y_j(x)=Y_{j+1}(x)^2+a_j\frac{x}{1+x}=F(Y_{j+1})+a_jr.
\]
Iterating around the period and using \(Y_d=Y_0=Y\) gives
\[
(1+F^d)Y=\sum_{j=0}^{d-1}a_jF^j(r),
\]
which is exactly \(B(F)Y=A(F)r\).

**2. Cancelling the common Frobenius factor.** Since \(A=DC\), \(B=DE\), the preceding identity gives
\[
D(F)\big(E(F)Y+C(F)r\big)=0.
\]
The series \(Z=E(F)Y+C(F)r\) has constant coefficient zero. Because \(D\) divides \(B\), its constant coefficient is \(D_0=1\). On the space \(x\mathbb F_2[[x]]\), the map \(D(F)\) is injective: if a nonzero series starts in degree \(m\ge1\), its degree-\(m\) term survives \(D_0F^0\), whereas every higher Frobenius power starts in degree at least \(2m\). Hence \(Z=0\), proving \(E(F)Y=C(F)r\). This equation gives an algebraic upper bound of \(2^e\) for the degree of \(Y\), and hence for \(U\).

**3. Irreducibility and exactness.** We have \(\gcd(E,C)=1\) by construction. Choose polynomials \(H,J\in\mathbb F_2[T]\) satisfying \(HC+JE=1\). Define
\[
W=H(F)Y+J(F)r\in\mathbb F_2(x,Y).
\]
Commutativity of additive polynomials gives
\[
E(F)W=(HC+JE)(F)r=r.
\]
Let \(K=\mathbb F_2(x)\) and \(L=K(W)\). At any place of \(L\) above the rational place \(x=1\), let the normalized valuation be \(v\), with positive ramification index \(h\), so that \(v(r)=-h\). Since \(r\) has a pole, \(v(W)<0\). The term \(W^{2^e}\) has strictly smaller valuation than every other term of \(E(F)W\) (the assertion also holds when \(e=0\)). Therefore \(2^ev(W)=-h\). As valuations in \(L\) are integer-valued, \(2^e\mid h\). The fundamental ramification inequality yields \([L:K]\ge h\ge2^e\). But \(W\in K(Y)\), and the equation from step 2 has degree \(2^e\). Therefore
\[
2^e\le[K(W):K]\le[K(Y):K]\le2^e.
\]
Equality follows throughout. Because \(Y=(1+x)U\) and \(1+x\in K^\times\), the same degree holds for \(U\). Consequently \(P(Z)\), of degree \(2^e\) with nonzero leading coefficient, is irreducible over \(K\).

**4. The three-periodic classification.** When \(d=3\), \(B(T)=(1+T)(1+T+T^2)\). The eight masks yield gcd degrees \(3,0,0,1,0,1,1,2\) in the order \(000,100,010,110,001,101,011,111\), hence the degree classification in the finding. For \(\mathcal M_2\), Campbell and Cloitre's digit formula omits binary positions congruent to two modulo three, so \(A(T)=1+T\), \(D(T)=1+T\), \(E(T)=1+T+T^2\), \(C(T)=1\). Its displayed quartic follows and is irreducible by step 3.

## Verification
The standalone `CHECKER.py` enumerates all \(254\) binary masks with specified periods \(1\) through \(7\), independently computes the mask-specific algebraic equation, and checks the first \(2048\) coefficients in every case (\(520192\) checks). It separately compares the first \(65536\) terms of the period-three mask \(110\) with the independently stated four-state digit automaton for \(\mathcal M_2\). The exact output is in `CHECK_OUTPUT.txt`. These finite checks corroborate the calculations; the algebraic degree and irreducibility for every mask and every period are proved in steps 1–3.

## Relationship to prior work
Campbell and Cloitre (2026, arXiv:2602.23395, Theorems 22 and 26) introduce \(\mathcal M_2\), provide its finite automaton and a period-three binary-digit mask, and determine ordinary factor-complexity properties. The exact algebraic degree of the coefficient generating series is not a stated theorem there. Cloitre (2026, arXiv:2604.06243, Theorem 2.2 and Section 2.2) develops general parity-weighted binary digit sequences and their mask generating series, but the inspected mathematical statements do not classify the algebraic degrees of the corresponding coefficient generating series by polynomial gcd. Rowland, Stipulanti, and Yassawi (arXiv:2308.10977v2, 2025, introduction and Theorems 1–2) study general relations between algebraic series and automaton sizes, not the exact periodic-mask degree classification. OEIS A391614 records the masked sequence and its automaton, but not the quartic minimal polynomial. The present theorem adds the precise degree for **every periodic mask**, including complete period-three distinctions. This statement is subject to a residual risk of equivalent results under different terminology.

## Limitations
This classification assumes binary digit weights periodic in their position and coefficients in \(\mathbb F_2\); it does not cover arbitrary nonperiodic masks, other finite fields, or quantitative bounds on automaton minimization. The integer-sequence digit formula for \(\mathcal M_2\) is prior work. The new contribution is the exact minimal algebraic polynomial degree and its gcd law. No independent scientific audit has been performed.

## References
1. J. M. Campbell and B. Cloitre, *Meta-Automatic Sequences*, arXiv:2602.23395, first posted February 25, 2026; https://arxiv.org/html/2602.23395.
2. B. Cloitre, *The Thue-Morse Transform*, arXiv:2604.06243 (2026); https://arxiv.org/pdf/2604.06243.
3. E. Rowland, M. Stipulanti, and R. Yassawi, *An Elementary Proof of Bridy's Theorem*, arXiv:2308.10977v2 (2025); https://arxiv.org/pdf/2308.10977.
4. OEIS A391614, sequence record and mask formula; https://oeis.org/A391614.
