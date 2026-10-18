# A simple nonordinary Jacobian from a minimal-automorphism Artin–Schreier curve

## Finding

Consider the smooth projective curve \(C\) over \(\mathbb F_5\) with affine function-field model
\[
y^5-y=x^2+x+\frac1x.
\]
Its exact Hasse–Weil zeta function is
\[
Z(C,T)=\frac{P_C(T)}{(1-T)(1-5T)},
\]
with
\[
\begin{aligned}
P_C(T)={}&1-4T-4T^2+21T^3+46T^4-100T^5-85T^6\\
&-500T^7+1150T^8+2625T^9-2500T^{10}-12500T^{11}+15625T^{12}.
\end{aligned}
\]
The polynomial is irreducible over \(\mathbb Q\). Consequently the Jacobian is simple **over \(\mathbb F_5\)**, and the Jacobian has \(3775\) rational points. Its \(5\)-adic Newton polygon has slopes \(0,\frac12,1\), each with multiplicity \(4\). This is a nonordinary, positive-\(5\)-rank example with the smallest possible geometric curve automorphism group in the Artin–Schreier locus. The source already proves the automorphism assertion.

## Assumptions and scope

The base field is exactly \(\mathbb F_5\). The curve is the unique smooth projective model of the displayed function field; we do not use the singular affine plane closure as the curve. The Artin–Schreier function has two poles, at \(0\) and \(\infty\), of orders \(1\) and \(2\) respectively. Since these orders are prime to \(5\), its degree-five extension is geometrically irreducible and totally ramified over both rational poles. Riemann–Hurwitz gives genus \(6\), and Deuring–Shafarevich gives \(5\)-rank \(4\). Proposition 4.2 of Tafazolian–Kazemifard, with parameters \(a=1,b=2,t=1\), establishes that the full geometric automorphism group is the deck group \(C_5\). The genus, rank, and automorphism statements are input from standard theory and the originating paper; the exact arithmetic invariants above are the result determined here.

## Proof

For every integer \(n\ge1\), write \(q=5^n\) and \(\operatorname{Tr}_n=\operatorname{Tr}_{\mathbb F_q/\mathbb F_5}\). The additive polynomial \(y\mapsto y^5-y\) has kernel \(\mathbb F_5\), and its image is exactly the trace-zero hyperplane. The two poles are rational and totally ramified, contributing exactly two rational points. Therefore
\[
\#C(\mathbb F_q)=2+5\#\{x\in\mathbb F_q^\times:\operatorname{Tr}_n(x^2+x+x^{-1})=0\}.
\]

The attached standalone exact-arithmetic script `verify.py` represents \(\mathbb F_{5^n}\), for \(1\le n\le6\), as the quotient of \(\mathbb F_5[Z]\) by a deterministically found monic irreducible degree-\(n\) polynomial. It verifies the modulus irreducibility by Rabin's finite-field criterion; enumerates all nonzero \(x\); computes the trace as \(\sum_{i=0}^{n-1}(x^2+x+x^{-1})^{5^i}\); and for \(n\le3\) additionally verifies directly that the Artin–Schreier map has exactly five preimages of each trace-zero element and zero otherwise.

The resulting exact counts are

| \(n\) | \(\#\{x\ne0:\operatorname{Tr}_n(x^2+x+x^{-1})=0\}\) | \(\#C(\mathbb F_{5^n})\) |
|---:|---:|---:|
| 1 | 0 | 2 |
| 2 | 0 | 2 |
| 3 | 15 | 77 |
| 4 | 120 | 602 |
| 5 | 604 | 3022 |
| 6 | 3267 | 16337 |

Let \(P_C(T)=\sum_{k=0}^{12}c_kT^k\) with \(c_0=1\), and let \(s_n=5^n+1-\#C(\mathbb F_{5^n})\). Then \(s_1,\ldots,s_6=(4,24,49,24,104,-711)\). Newton's identities give, for \(1\le k\le6\),
\[
kc_k=-\sum_{j=1}^k c_{k-j}s_j.
\]
Thus \((c_0,\ldots,c_6)=(1,-4,-4,21,46,-100,-85)\). For a genus-six curve over \(\mathbb F_5\), the functional equation gives \(c_{12-k}=5^{6-k}c_k\) for \(0\le k\le6\). This yields the displayed numerator and \(P_C(1)=3775\).

For irreducibility, reduce \(P_C(T)\) modulo \(3\). Its degree remains \(12\); the reduction is monic and satisfies
\[
T^{3^{12}}\equiv T\pmod{\overline P_C},\qquad
\gcd(\overline P_C,T^{3^6}-T)=\gcd(\overline P_C,T^{3^4}-T)=1.
\]
These are precisely Rabin's necessary and sufficient irreducibility tests for degree \(12\), whose distinct prime divisors are \(2\) and \(3\). The script checks all three congruences by direct finite-field polynomial arithmetic, without symbolic-algebra dependencies. Hence \(P_C\) is irreducible over \(\mathbb Q\). The characteristic polynomial of Frobenius on the Jacobian is its reciprocal and therefore also irreducible; if the Jacobian were isogenous over \(\mathbb F_5\) to a product of two positive-dimensional abelian varieties, that characteristic polynomial would factor. Thus the Jacobian is simple over \(\mathbb F_5\).

Finally the \(5\)-adic valuations of \((c_0,\ldots,c_{12})\) are
\[
(0,0,0,0,0,2,1,3,2,3,4,5,6).
\]
Their lower convex hull has vertices \((0,0),(4,0),(8,2),(12,6)\); the slopes, with horizontal multiplicity, are \(0^4,(1/2)^4,1^4\). The first four zero slopes independently agree with the known \(5\)-rank \(4\).

## Verification

The complete reproducible script `verify.py` uses only the Python standard library. Run `python3 verify.py` with Python 3.10 or later. It prints the six deterministic field moduli and point counts, the thirteen numerator coefficients, \(P_C(1)\), the modular irreducibility result, and `VERIFY_OK`. The code recomputes finite-field irreducibility and the mod-\(3\) certificate and checks the valuation inequalities. The actual packaged code has been executed and produced `VERIFY_OK`. Finite enumeration is exhaustive for the stated six finite fields; the extension to all \(n\) uses the proven genus-six functional equation, rather than an unproved extrapolation.

## Relationship to prior work

Tafazolian–Kazemifard, arXiv:2610.13279v1 (9 October 2026), explicitly constructs this \(N=3\), \(p=5\), positive-\(p\)-rank example and proves it has no geometric automorphisms beyond \(C_5\). The manuscript does not state the exact zeta numerator, Frobenius irreducibility, or Newton polygon, and its Question 7.5 specifically asks which Newton polygons can coexist with the minimal geometric automorphism group in fixed \(p\)-rank strata. The present computation supplies one precise nonordinary answer for the least permissible genus in the \(p=5\), \(5\)-rank-four stratum; it does not solve that general question.

Duque-Rosero and collaborators classify isomorphism invariants for genus-three and genus-four Artin–Schreier curves, a different numerical range. Scholten–Zhu study first-slope estimates for polynomial one-pole Artin–Schreier curves; their hypotheses do not cover this two-pole function. Li–Mantovan–Pries–Tang study Newton polygons in selected families of characteristic-prime-to-cover-order cyclic covers, not this wild degree-five cover. There are no claims that the general point-count method, Newton identities, or Rabin's criterion are original.

## Limitations

The assertion of simplicity is **over the ground field**, not geometric or absolute simplicity. The exact Newton polygon is for this individual explicit curve, not all curves in the same stratum. The paper's broader Newton-polygon prescription question remains unanswered. A nonindexed table or a more general theorem could already encode this exact arithmetic outcome. No claim of universal priority or independent certification is made.

## References

1. Saeed Tafazolian and Ahmad Kazemifard, *Artin–Schreier Curves of Prescribed p-Rank Without Extra Automorphisms*, arXiv:2610.13279v1, 9 October 2026. See Proposition 4.2 and Question 7.5. https://arxiv.org/html/2610.13279v1
2. Juanita Duque-Rosero, Heidi Goodson, Elisa Lorenzo García, Beth Malmskog, Renate Scheidler, *On invariants of Artin-Schreier curves*, arXiv:2401.08843v1, 2024. https://arxiv.org/abs/2401.08843
3. Jasper Scholten and Hui June Zhu, *Slope Estimates of Artin–Schreier Curves*, Compositio Mathematica 137 (2003), 275–292. https://doi.org/10.1023/A:1024116216156
4. Wanlin Li, Elena Mantovan, Rachel Pries, Yunqing Tang, *Newton polygons arising from special families of cyclic covers of the projective line*, Research in Number Theory 5 (2019), article 12. https://doi.org/10.1007/s40993-018-0149-3
