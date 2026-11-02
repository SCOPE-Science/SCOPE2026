# Exact two-cycle spectrum of norm-lift binomials over quadratic finite-field extensions

## Finding
Let \(q\) be any prime power, \(K=\mathbb F_q\), \(L=\mathbb F_{q^2}\), and \(a\in L\setminus K\). Consider the polynomial self-map
\[
F_a(x)=x^{q+2}+ax=x\bigl(\operatorname N_{L/K}(x)+a\bigr)
\]
on \(L\). Every such map has the unique fixed point \(0\). Let \(P_2(q,a)\) count elements of **least period exactly two**. Then
\[
P_2(q,a)=
\begin{cases}
2(q+1),&q\text{ odd},\ \operatorname{Tr}_{L/K}(a)=0,\
\chi_q(a^2-1)=1,\\
0,&\text{otherwise}.
\end{cases}
\]
Here \(\chi_q\) is the quadratic character of \(K\), extended by \(\chi_q(0)=0\). The expression \(a^2-1\) belongs to \(K\) whenever the trace condition holds. In the nonzero case, the two-cycles are exactly the \(q+1\) cycles pairing the two norm fibers \(\operatorname N(x)=t\) and \(\operatorname N(x)=-t\), for either root \(t\in K\) of \(t^2=a^2-1\).

For odd \(q\), exactly
\[
\frac{q-\chi_q(-1)}{2}
\]
of the \(q^2-q\) coefficients \(a\in L\setminus K\) have nonzero \(P_2(q,a)\); for even \(q\), none does.

In the *permutation-binomial family* of Zieve's 2013 classification (the nonzero \(a\) for which \(F_a\) permutes \(L\)), this gives the sharp dichotomy: if \(q\equiv2\pmod 3\), every admissible permutation has **no** two-cycles; if \(q=3^m\), exactly \((q-\chi_q(-1))/2\) of its \(q-1\) admissible coefficient choices have \(q+1\) two-cycles each, and the remaining choices have none. There are no such nonzero-coefficient permutation binomials when \(q\equiv1\pmod3\).

## Assumptions and scope
\(q=p^m\) with \(p\) prime and \(m\ge1\). The coefficient \(a\) lies in \(L\setminus K\). Nothing is assumed about the bijectivity of \(F_a\) for the main two-cycle classification; the last paragraph specializes to exactly the permutation coefficients classified in the cited source. A point has least period two when \(F_a(F_a(x))=x\) but \(F_a(x)\ne x\). The maps have degree \(q+2\), and the norm map from \(L^*\) onto \(K^*\) has fibers of size \(q+1\).

## Proof
Put \(c=\operatorname{Tr}(a)=a+a^q\in K\), \(d=\operatorname N(a)=aa^q\in K\). Since \(a\notin K\), the elements \(1,a\) form a basis of \(L\) over \(K\), and \(a^2-ca+d=0\).

If \(x\ne0\), write \(t=\operatorname N(x)\in K^*\). Then \(F_a(x)=x(t+a)\). Equality \(F_a(x)=x\) would force \(a=1-t\in K\); hence \(0\) is the sole fixed point. Put \(u=\operatorname N(F_a(x))\). Multiplicativity of the norm gives
\[
u=t(t+a)(t+a^q)=t(t^2+ct+d).
\]
The equality \(F_a^2(x)=x\) for \(x\ne0\) is equivalent to
\[
(t+a)(u+a)=tu-d+(t+u+c)a=1.
\]
By independence of \(1,a\), these are exactly the two equations
\[
t+u+c=0,\qquad tu=d+1.
\]
Eliminating \(u\) yields \(t^2+ct+d+1=0\). Substituting into the norm recursion gives \(u=t(-1)=-t\). Consequently \(c=0\), and the remaining condition is \(t^2=-d-1\). Conversely, if \(c=0\) and \(t^2=-d-1\), then \(u=-t\) and the two displayed coefficient equations hold, so \(F_a^2(x)=x\). Thus the conditions are both necessary and sufficient.

In characteristic two, \(c=0\) implies \(a^q=a\), contrary to \(a\notin K\). In odd characteristic, \(c=0\) implies \(a^q=-a\), whence \(a^2=-d\in K\). In fact \(a^2\) is a nonsquare in \(K\): otherwise both of its square roots belong to \(K\), contrary to \(a\notin K\). Therefore \(a^2-1\ne0\). The equation \(t^2=a^2-1\) has either two or zero roots in \(K^*\), according to whether \(\chi_q(a^2-1)\) equals \(1\) or \(-1\). Every allowed norm \(t\) occurs on exactly \(q+1\) elements of \(L^*\). None is fixed, so the stated point and cycle counts follow. The two root fibers exchange under \(F_a\), since \(u=-t\).

For the coefficient census, the trace-zero non-base-field coefficients in odd characteristic number \(q-1\). The map \(a\mapsto a^2\) maps them two-to-one onto the nonsquares in \(K\): for each nonsquare \(b\in K^*\), its square roots in \(L\) have Frobenius conjugate negatives. Let \(A\) count nonsquares \(b\) with \(b-1\) a nonzero square. The standard quadratic-character identity \(\sum_{b\in K}\chi_q(b)\chi_q(b-1)=-1\), together with the vanishing linear character sums and correcting the spurious term at \(b=0\), gives
\[
A=\frac14\left[q+1-(1+\chi_q(-1))\right]
=\frac{q-\chi_q(-1)}4.
\]
Thus exactly \(2A=(q-\chi_q(-1))/2\) coefficients yield two-cycles.

Finally, Zieve's classification [1, Corollary 2.3] states that, for \(a\ne0\), the map \(F_a\) permutes \(L\) precisely when either \(q\equiv2\pmod3\) and \(a=\mu(1-\omega)\) with \(\mu\in K^*\) and \(\omega\) a primitive cube root of unity in \(L\setminus K\), or \(q=3^m\) and \(a^q=-a\). In the former case \(\operatorname{Tr}(a)=3\mu\ne0\), including in characteristic two. The general criterion forces zero two-cycles. In the latter case the admissible coefficients are exactly the nonzero trace-zero elements, so their exact split is supplied by the coefficient census just proved. This uses [1] for permutation ownership only; the two-cycle statements are established independently above.

## Verification
Run `python verification/verify_cycles.py` from the package directory. It uses no third-party dependencies. It constructs finite fields using specified irreducible polynomials, performs quadratic-extension arithmetic, enumerates every element in the test fields, and counts actual fixed and least-period-two points. The test also independently evaluates \(x^{q+2}+ax\) by extension-field exponentiation against the norm-based expression. It checked 156 admissible permutation-parameter cases over nine field orders \(q\in\{2,3,5,8,9,11,17,23,27\}\); it also checked 386 non-base-field coefficient cases (exhaustively for \(q\le11\), bounded samples otherwise) and 5,549 direct exponentiation identities. Output:

`VERIFY_OK permutation_parameters= 156 general_parameters= 386 direct_power_checks= 5549`

These are finite corroborations, not proofs for all prime powers; the preceding algebraic argument proves the unrestricted statements. The verifier intentionally does not attempt all higher cycles.

## Relationship to prior work
[1] classifies exactly when \(x^{q+2}+ax\) permutes a quadratic extension and proves its classification using induced cubic maps. Its Corollary 2.3 supplies the parameterization used above, but does not classify fixed points of the second iterate or their norm fibers. [2, Theorem 1.4] later treats the broader permutation family \(x^{q+2}+bx^q+cx\); its coefficient classification also does not imply an iterate-two census. [3] studies cycle structures of other trace-based permutation families, specifically maps of the form \(x+\gamma\operatorname{Tr}(x^k)\); its cycle formulas do not apply to the norm-multiplied map studied here. Relevant primary literature and accessible public mathematical research records were compared for direct, equivalent, and stronger statements. No equivalent theorem was identified; priority beyond inspected sources is not certified.

## Limitations
The complete criterion assumes \(a\notin K\); parameters in \(K\) can behave differently. Only the first two iterates are classified. Nothing is concluded about exact periods three or greater, permutation signs, or arbitrary polynomials \(x^{q+r}+ax\). Computational evidence is finite. Historical literature outside the inspected records, including the difficult-to-locate Tucker–Zieve 2000 preprint cited by [1], may contain related results. Independent mathematical audit has not been performed.

## References
[1] Michael E. Zieve, *Permutation polynomials induced from permutations of subfields, and some complete sets of mutually orthogonal latin squares*, arXiv:1312.1325v1 (first submitted 2013-12-04), Corollary 2.3; https://arxiv.org/html/1312.1325v3 . Primary MSC: 11T06.

[2] Zhiguo Ding, Wei Xiong, Michael E. Zieve, *Determination of all complete mappings of \(\mathbb F_{q^2}\) of the form \(aX^{3q}+bX^{2q+1}+cX^{q+2}+dX^3\)*, arXiv:2510.16640 (submitted 2025-10-18), especially Theorem 1.4; https://arxiv.org/abs/2510.16640 .

[3] Daniel Gerike and Gohar M. Kyureghyan, *Permutations on finite fields with invariant cycle structure on lines*, Designs, Codes and Cryptography 88 (2020), 1723–1740, published 2020-02-14; https://link.springer.com/article/10.1007/s10623-020-00721-2 .
