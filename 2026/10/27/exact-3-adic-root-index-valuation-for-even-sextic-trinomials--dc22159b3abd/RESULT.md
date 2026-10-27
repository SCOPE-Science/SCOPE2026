# Exact 3-adic root-index valuation for even sextic trinomials

## Finding
Let \(F(x)=x^6+a x^m+b\in\mathbb Z[x]\) be irreducible, with \(m\in\{2,4\}\), \(9\mid a\), and \(b\equiv1\pmod9\). If \(\theta\) is a root and \(K=\mathbb Q(\theta)\), then
\[
\nu_3\!\left([\mathcal O_K:\mathbb Z[\theta]]\right)=2.
\]
Thus the defining root's order index is divisible by \(9\), but not by \(27\).

## Assumptions and scope
The polynomial is monic and irreducible of degree six, the exponent is exactly \(m=2\) or \(m=4\), and the coefficients satisfy \(a\in9\mathbb Z\) and \(b\equiv1\pmod9\). The notation \(\nu_3(n)\) means the exponent of \(3\) in the positive integer \(n\). The result concerns the index of the particular order \(\mathbb Z[\theta]\); it does not assert that the number field \(K\) is nonmonogenic.

## Proof
Put \(\phi(x)=x^2+1\). Its reduction is irreducible over \(\mathbb F_3\), and \(\overline F=\overline\phi^{\,3}\), since \(x^6+1=(x^2+1)^3\) in characteristic three.

Using \(x^2=\phi-1\), the exact \(\phi\)-expansions are
\[
\begin{aligned}
m=2:\quad F&=\phi^3-3\phi^2+(3+a)\phi+(b-1-a),\\
m=4:\quad F&=\phi^3+(-3+a)\phi^2+(3-2a)\phi+(b-1+a).
\end{aligned}
\]
For both exponents, the coefficients of \(\phi^2\) and \(\phi\) have 3-adic valuation exactly one: after division by \(3\), their reductions are nonzero modulo \(3\). The constant coefficient is divisible by \(9\), or is zero. Consequently the principal \(\phi\)-Newton polygon has the point \((1,1)\) as a vertex and also contains \((2,1)\) and \((3,0)\); the point \((2,1)\) lies strictly above the segment joining \((1,1)\) to \((3,0)\). If the constant coefficient is nonzero, there is additionally a left-hand side from \((0,v)\) to \((1,1)\), where \(v\ge2\); if it is zero, that side is absent.

The only lattice point with both coordinates positive lying on or below this polygon is \((1,1)\). Each side of the principal polygon has a degree-one residual polynomial with nonzero leading coefficient, hence is squarefree. Thus \(F\) is 3-regular for this \(\phi\). Its \(\phi\)-index is therefore \(\deg(\phi)\cdot1=2\). Ore's index theorem, with equality in the 3-regular case, gives
\[
\nu_3\!\left([\mathcal O_K:\mathbb Z[\theta]]\right)=2.
\]
This also covers the boundary case where the constant coefficient in the \(\phi\)-expansion vanishes, because the vertex \((1,1)\) and the remaining degree-one residual polynomial are unchanged.

## Verification
The two displayed expansions were multiplied out symbolically and agree exactly with \(x^6+a x^m+b\). The reductions modulo \(3\), coefficient valuations, polygon lattice-point count, and residual-polynomial degrees are given explicitly above. No finite experiment is used as a proof. The conclusion relies on the stated Ore index theorem and on irreducibility to define the degree-six field and its order index.

## Relationship to prior work
El Fadil's 2022 paper on index divisors and monogenity of trinomial number fields proves a field-level common-index-divisor result for the sextic family when \(9\mid a\) and \(b\equiv-1\pmod9\) (Theorem 2.4). That is a different sign branch and a different invariant. The calculation here gives the exact 3-adic valuation of the index of the defining root in the even-exponent branch \(m=2,4\), \(b\equiv1\pmod9\); it makes no claim about the common index of the field. The same paper states Ore's index theorem in §3, but does not give this evaluated branch as a result.

## Limitations
Only the two exponents \(m=2,4\) and the residue branch \(b\equiv1\pmod9\) are covered. The result does not decide whether \(K\) is monogenic, nor whether \(3\) divides the common index \(i(K)\). A related general trinomial-monogenity paper was not retrieved in full during this run, so a residual literature-overlap risk remains; it is not used as evidence of noncoverage.

## References
Lhoussain El Fadil, “On index divisors and monogenity of certain number fields defined by trinomials,” arXiv:2203.13353, submitted 24 March 2022, especially §2 (Theorem 2.4) and §3 (Ore's Theorem 3.2). https://arxiv.org/abs/2203.13353
