# An explicit simple isogeny class for a genus-five Artin–Schreier curve with minimal automorphisms

## Finding
Let \(C\) be the smooth projective normalization over \(\mathbb F_3\) of
\[
y^3-y=x^2+x+\frac1x+\frac1{x-1}.
\]
Its zeta function is
\[
Z(C,T)=\frac{P_C(T)}{(1-T)(1-3T)},
\]
where
\[
\begin{aligned}
P_C(T)={}&1+2T+6T^2+8T^3+10T^4+15T^5\\
&+30T^6+72T^7+162T^8+162T^9+243T^{10}.
\end{aligned}
\]
Consequently \(\#\operatorname{Jac}(C)(\mathbb F_3)=P_C(1)=711=9\cdot79\). The Jacobian is simple **over \(\mathbb F_3\)**. The exact initial extension-field point counts are
\[
\bigl(\#C(\mathbb F_3),\#C(\mathbb F_9),\#C(\mathbb F_{27}),\#C(\mathbb F_{81}),\#C(\mathbb F_{243})\bigr)
=(6,18,24,66,291).
\]

## Assumptions and scope
All statements concern this one explicitly specified smooth projective curve over \(\mathbb F_3\) and its arithmetic over that base field. The rational function has poles precisely at \(0\), \(1\), and \(\infty\), of orders \(1,1,2\). These pole orders are prime to \(3\); hence the Artin–Schreier extension is geometrically irreducible and of degree \(3\). The Artin–Schreier genus and Deuring–Shafarevich formulas give
\[
g(C)=\frac{3-1}{2}\left(-2+(1+1)+(1+1)+(2+1)\right)=5,
\qquad \gamma(C)=(3-1)(3-1)=4.
\]
The cited construction establishes that this curve has no geometric automorphisms besides its deck group of order three. That automorphism statement is input from the originating publication, not a newly claimed result.

## Proof
Every one of the three rational branch points of \(C\to\mathbb P^1\) is totally ramified, with a unique rational point over it over every extension \(\mathbb F_{3^m}\). Let \(f(x)=x^2+x+1/x+1/(x-1)\). For any \(a\in\mathbb F_{3^m}\setminus\{0,1\}\), the equation \(y^3-y=f(a)\) has exactly three solutions if \(\operatorname{Tr}_{\mathbb F_{3^m}/\mathbb F_3}f(a)=0\), and none otherwise. Thus
\[
\#C(\mathbb F_{3^m})=3+3\#\left\{a\in\mathbb F_{3^m}\setminus\{0,1\}:\operatorname{Tr}(f(a))=0\right\}.
\]
The attached complete finite-field enumeration, performed for all field elements (not sampled elements) and separately cross-checked by direct solution counting, gives the following trace-frequency triples for \(m=1,2,3,4,5\):
\[
(1,0,0),\quad(5,2,0),\quad(7,15,3),\quad(21,28,30),\quad(96,90,55).
\]
The entries correspond to traces \(0,1,2\), and yield the five stated point counts. The field moduli in the verifier are each certified irreducible by exhaustive monic trial division of degree at most half the modulus degree.

Write \(P_C(T)=\sum_{i=0}^{10}a_iT^i\), with \(a_0=1\), and set \(S_m=3^m+1-\#C(\mathbb F_{3^m})\). Newton's recurrence
\[
k a_k=-\sum_{j=1}^{k}a_{k-j}S_j
\]
produces \((a_0,\ldots,a_5)=(1,2,6,8,10,15)\). The functional equation of a genus-five Weil polynomial gives \(a_{10-k}=3^{5-k}a_k\) for \(0\le k\le5\), determining the remaining coefficients displayed above. Substitution at \(T=1\) gives \(711\).

For simplicity, reduce \(P_C\) modulo \(5\) and scale to monic form:
\[
\overline P(T)=T^{10}+4T^9+4T^8+4T^7+T^3+2T^2+4T+2\in\mathbb F_5[T].
\]
Exact polynomial arithmetic establishes
\[
\gcd(\overline P,T^{5^2}-T)=\gcd(\overline P,T^{5^5}-T)=1,
\quad T^{5^{10}}\equiv T\pmod{\overline P}.
\]
Because the prime divisors of \(10\) are \(2\) and \(5\), these are the standard finite-field irreducibility criterion for degree \(10\). The rational Frobenius characteristic polynomial, reciprocal to \(P_C\), is therefore irreducible over \(\mathbb Q\). By the isogeny decomposition theorem for abelian varieties over finite fields, \(\operatorname{Jac}(C)\) is simple over \(\mathbb F_3\).

## Verification
Run `python3 verify.py` with the Python standard library. It constructs each finite field of cardinality \(3^m\), certifies its modulus, enumerates the full affine fibers independently by traces and direct \(y\)-values, derives all ten Weil coefficients, evaluates the Jacobian order, and checks the stated irreducibility criterion via exact finite-field polynomial arithmetic. Expected last line begins \(`VERIFY_OK`\). The proof of genus, rank, zeta functional equation, and simplicity implication uses the standard stated mathematical results; the verifier supplies exhaustive certificates for the only finite computations.

## Relationship to prior work
Tafazolian and Kazemifard construct exactly this equation in Proposition 5.5 (Case 2, \(r=2,m=1\)) as an explicit curve with minimal geometric automorphism group. Their classification establishes its geometric context but does not report these extension-field counts, this zeta polynomial, or the arithmetic simplicity statement in the inspected article. Kudo and Harashita examine genus-five characteristic-three curves with *many* rational points over \(\mathbb F_9\); their enumerated high-point regime does not include a curve with \(18\) points over \(\mathbb F_9\). The LMFDB classifies abstract isogeny classes in dimension five over \(\mathbb F_3\); this finding claims neither a previously unknown abstract Weil polynomial nor discovery of a new isogeny class. The new contribution is the explicit identification of the 2026 naturally constructed curve with one arithmetic isogeny class and the consequent simplicity determination. No claim of independent historical priority is made.

## Limitations
Simplicity is proved over \(\mathbb F_3\), **not** geometric or absolute simplicity; no assertion is made about the full Jacobian endomorphism ring or the group structure of \(\operatorname{Jac}(C)(\mathbb F_3)\). Although the enumeration is complete over the first five extension fields and determines the zeta function, it is not a classification of all curves with this polynomial. Earlier unindexed arithmetic tabulations could have implicitly included this particular curve; that possibility remains a priority risk.

## References
1. S. Tafazolian and A. Kazemifard, *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms*, arXiv:2610.13279v1 (2026), Proposition 5.5 and Section 7, https://arxiv.org/html/2610.13279v1.
2. M. Kudo and S. Harashita, *Genus-five hyperelliptic or trigonal curves with many rational points in characteristic three*, arXiv:2204.06805 (2022), https://arxiv.org/abs/2204.06805.
3. LMFDB, *Isogeny classes of abelian varieties over finite fields*, https://www.lmfdb.org/Variety/Abelian/Fq/.
