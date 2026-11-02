# Exact squarefree-derivative strata of quartic polynomials over finite fields

## Finding

Let \(q\) be any prime power, of characteristic \(p\). Among all monic quartics \(f\in\mathbb F_q[X]\), first require the **nonzero formal derivative** \(f'\) to be squarefree (a nonzero constant polynomial counts as squarefree). For \(j\ge0\), define
\[
M_j(q)=\#\{f\text{ monic quartic}: f'\ne0,\ \gcd(f',f'')=1,\ \deg\gcd(f,f')=j\}.
\]
All these counts vanish for \(j\ge3\); the complete three-stratum distribution is
\[
\boxed{
(M_0,M_1,M_2)=
\begin{cases}
(q^2(q-1),\,0,\,0),&p=2,\\
(q^2(q-1)^2,\,q(q-1)^2,\,q(q-1)),&p=3,\\
(q(q-1)(q^2-q+1),\,q(q-1)(q-2),\,q(q-1)),&p>3.
\end{cases}}
\]
In particular, \(M_0\) counts quartics for which **both** \(f\) and \(f'\) are squarefree.

Choose a monic quartic uniformly from the \(q^4\) such polynomials. Let \(A\) mean that \(f\) is squarefree and \(B\) that the nonzero derivative \(f'\) is squarefree. Then
\[
\boxed{\operatorname{Cov}(\mathbf1_A,\mathbf1_B)=
\begin{cases}0,&p=3,\\(q-1)/q^3,&p\ne3.
\end{cases}}
\]
Thus these two natural squarefreeness events are exactly independent **if and only if the characteristic is three**.

## Assumptions and scope

All polynomial arithmetic and formal differentiation occur in \(\mathbb F_q[X]\). The gcd is normalized to be monic; the gcd of two nonzero relatively prime polynomials is \(1\). The zero polynomial is **not** called squarefree, while any nonzero constant is. The events are defined on *all* monic degree-four polynomials, not on irreducible quartics. All statements apply to every prime power, including nonprime finite-field orders and characteristics two and three.

## Proof

**1. Size of the derivative-squarefree locus.** Write
\[f=X^4+aX^3+bX^2+cX+d,\qquad f'=4X^3+3aX^2+2bX+c.\]
Let \(T_q=\sum_j M_j(q)\).

When \(p>3\), the coefficient map \((a,b,c)\mapsto f'/4\) bijects \(\mathbb F_q^3\) with monic cubics. Exactly \(q^3-q^2\) monic cubics are squarefree, and the arbitrary \(d\) multiplies their number by \(q\). Therefore \(T_q=q^3(q-1)\).

When \(p=3\), \(f'=X^3+2bX+c\) and \(f''=2b\). Thus \(f'\) is squarefree exactly when \(b\ne0\), yielding \(T_q=q^3(q-1)\) after choosing \(a,c,d\) freely.

When \(p=2\), \(f'=aX^2+c\). If \(a\ne0\), it has zero derivative and is not squarefree; if \(a=c=0\), it is the excluded zero polynomial. Hence \(f'\) is squarefree exactly when \(a=0,c\ne0\), and \(T_q=q^2(q-1)\). In that case \(f'\) is a nonzero constant, so \(M_0=T_q\) and all other \(M_j\) vanish.

**2. What a common factor means in odd characteristic.** Suppose \(p\ne2\) and \(f'\) is squarefree. Every repeated geometric root of \(f\) is then exactly double: a root of multiplicity at least three would be a multiple root of \(f'\) (or force its derivative to vanish to even higher order). Since \(\deg f=4\), there can be at most two such geometric roots, and \(\deg\gcd(f,f')\in\{0,1,2\}\).

A quartic with a specified repeated root \(r\in\mathbb F_q\) has the unique form \(f=(X-r)^2g\), with \(g\) monic quadratic. If \(f'\) is squarefree, necessarily \(g(r)\ne0\). Translating \(r\) to zero, write \(g=X^2+uX+v\), with \(v\ne0\). Then
\[ f'=X(4X^2+3uX+2v).\]
For \(p>3\), this is squarefree exactly when \(v\ne0\) and \(9u^2-32v\ne0\). For \(u=0\), all \(q-1\) nonzero \(v\) work. For each of the \(q-1\) nonzero \(u\), precisely one nonzero \(v\) is excluded. Thus each \(r\) contributes \((q-1)^2\) quartics to the repeated-rational-root incidence count.

For \(p=3\), the quadratic factor of \(f'\) becomes \(X^2+2v\), so every \(u\in\mathbb F_q\) and \(v\in\mathbb F_q^\times\) is allowed. Thus each \(r\) contributes \(q(q-1)\) incidences. Summing over \(r\), the incidence counts are respectively \(q(q-1)^2\) and \(q^2(q-1)\).

**3. The two-double-root correction.** Any quartic with two distinct rational double roots must be \(f=(X-r)^2(X-s)^2\) for distinct \(r,s\in\mathbb F_q\). Its derivative is \(2(X-r)(X-s)(2X-r-s)\), which is squarefree in every odd characteristic when \(r\ne s\). There are exactly \(q(q-1)/2\) such quartics, counted twice in the incidence count. Therefore
\[
M_1=\begin{cases}
q(q-1)^2-q(q-1)=q(q-1)(q-2),&p>3,\\
q^2(q-1)-q(q-1)=q(q-1)^2,&p=3.
\end{cases}
\]

The remaining degree-two common gcds occur either in these \(q(q-1)/2\) split double-root quartics, or in squares \(f=h^2\) of monic **irreducible quadratic** polynomials \(h\). There are \((q^2-q)/2\) of the latter, because finite fields are perfect. For such \(h\), \(f'=2hh'\) is squarefree: \(h\) and the nonzero linear derivative \(h'\) are coprime. Thus
\[M_2=\frac{q(q-1)}2+\frac{q^2-q}2=q(q-1)\]
in every odd characteristic.

Finally, subtract \(M_1+M_2\) from \(T_q\) to obtain the displayed \(M_0\) formulas. These counts partition the entire derivative-squarefree locus, with no higher-degree gcd cases.

**4. Exact independence transition.** It is standard, and follows from the polynomial Euler product, that a uniformly chosen monic quartic is squarefree with probability \(\Pr(A)=1-1/q\). The counts in Step 1 give
\[\Pr(B)=\begin{cases}(q-1)/q^2,&p=2,\\1-1/q,&p\ne2.\end{cases}\]
The joint probability is \(\Pr(A\cap B)=M_0/q^4\). Subtracting \(\Pr(A)\Pr(B)\) yields the covariance in the theorem. Since \(q>1\), it vanishes exactly in characteristic three.

## Verification

The standalone file `verify.py` independently enumerates quartics over the prime fields of orders \(2,3,5,7,11\) and polynomial-basis extensions of orders \(4,8,9,16\). It computes formal derivatives and polynomial gcds directly using finite-field tables, not the incidence formulas. In all nine fields, the observed \((M_0,M_1,M_2)\) agree with the theorem. A total of \(94{,}213\) monic quartics were examined. Reproduce with `python3 verify.py` (standard library only).

## Relationship to prior work

Almousa and Wood, *Counting polynomials over finite fields with given root multiplicities*, arXiv:1210.0472v1 (publicly submitted October 1, 2012), count quartics and other polynomials by **root-multiplicity partition of \(f\)**; their principal theorem concerns refinement sums for such partitions. Here we additionally impose that **the derivative \(f'\) itself be squarefree**. This property is not fixed by the root-multiplicity partition of \(f\): over \(\mathbb F_5\), both \(X^4+X\) and \(X^4+X^3+1\) are squarefree, but only the first has squarefree derivative. The present joint stratification and its characteristic-three independence law therefore require an additional condition beyond the one-variable multiplicity counts in that paper.

Earlier work by Ragot on prescribed root multiplicities is also relevant; its broader implications should be considered in future literature review. The classical separate squarefree counts used in the proof are not claimed as new.

## Limitations

The enumeration is complete only in degree four. The term “squarefree derivative” is not equivalent to the stronger condition that all critical values be distinct (sometimes also called a Morse condition). The result does not classify the squarefree-derivative locus in higher degrees or determine the full distribution of critical values. Finite verification supplements, but does not substitute for, the counting proof. Novelty remains subject to further scrutiny of general historical discriminant-incidence formulas and less accessible root-enumeration literature.

## References

1. A. Almousa and M. M. Wood, *Counting polynomials over finite fields with given root multiplicities*, arXiv:1210.0472v1 (October 1, 2012), https://arxiv.org/abs/1210.0472; Journal of Number Theory 136 (2014), 394–402, DOI 10.1016/j.jnt.2013.10.015.
2. J.-F. Ragot, *Counting polynomials with zeros of given multiplicities in finite fields*, Finite Fields and Their Applications 5 (1999), 219–231, DOI 10.1006/ffta.1999.0244.
