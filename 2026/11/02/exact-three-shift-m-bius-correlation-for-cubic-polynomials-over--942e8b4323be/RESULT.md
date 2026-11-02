# Exact three-shift Möbius correlation for cubic polynomials over noncubic finite fields

## Finding

For every odd prime power \(q\equiv2\pmod3\) and every triple of pairwise distinct constants \(c_1,c_2,c_3\in\mathbb F_q\),
\[
\sum_{\substack{f\in\mathbb F_q[T]\\ f\ \mathrm{monic},\ \deg f=3}}
\mu(f+c_1)\mu(f+c_2)\mu(f+c_3)=q^2.
\]
The three-shift sum is nonzero and independent of the three shifts, including their spacings.

## Assumptions and scope

Here \(\mu(g)=(-1)^r\) when the monic polynomial \(g\) is a product of \(r\) distinct monic irreducible factors; otherwise \(\mu(g)=0\). The field has odd cardinality \(q\equiv2\pmod3\), so its characteristic is neither \(2\) nor \(3\), and the cubing map is a bijection. Each shift has degree zero and the three constants are distinct. The quadratic character \(\chi\) is extended by \(\chi(0)=0\).

## Proof

**Character-correlation lemma.** Over any finite field of odd order, for three pairwise distinct constants \(c_1,c_2,c_3\),
\[
\sum_{u,v\in\mathbb F_q}\chi\!\left(\prod_{j=1}^{3}\bigl(u-(v+c_j)^2\bigr)\right)=q\chi(-1).\tag{1}
\]
To prove it, fix \(v\) and write \(a=(v+c_1)^2\), \(b=(v+c_2)^2\), and \(d=(v+c_3)^2\). Set
\[
K=(c_2-c_1)(c_2-c_3)\ne0,\qquad
L=\frac{c_2-c_1}{c_3-c_1}\notin\{0,1\}.
\]
There is exactly one exceptional value \(v_0=-(c_1+c_3)/2\) for which \(a=d\). At this value \(a-b=-K\), and therefore
\[
\sum_u\chi((u-a)^2(u-b))=-\chi(-K).\tag{2}
\]
For \(v\ne v_0\), set \(\lambda=(b-a)/(d-a)\) and \(x=(u-a)/(d-a)\). Direct subtraction gives
\[
\lambda-L=\frac{K}{d-a}.\tag{3}
\]
The map \(v\mapsto\lambda\) is a bijection from \(\mathbb F_q\setminus\{v_0\}\) to \(\mathbb F_q\setminus\{L\}\). Because \(\chi((d-a)^3)=\chi(d-a)\), the nonexceptional part of the left side of (1) becomes
\[
\chi(K)\sum_{x,\lambda\in\mathbb F_q}
\chi(x(x-1))\chi((\lambda-L)(x-\lambda)).\tag{4}
\]
For fixed \(x\ne L\), the inner \(\lambda\)-sum is \(-\chi(-1)\); for \(x=L\), it is \((q-1)\chi(-1)\). These are the standard elementary quadratic-character identities \(\sum_t\chi(t(t-h))=-1\) for \(h\ne0\), and \(\sum_t\chi(-t^2)=(q-1)\chi(-1)\). Since \(\sum_x\chi(x(x-1))=-1\), expression (4) equals
\[
\chi(-K)\bigl(1+q\chi(L(L-1))\bigr).
\]
Adding (2) cancels the constant term. Finally \(L(L-1)=K/(c_3-c_1)^2\), so \(\chi(L(L-1))=\chi(K)\), proving (1).

**Cubic Möbius reduction.** Every monic cubic is uniquely \(f(T)=(T+s)^3+A(T+s)+B\), with \(s,A,B\in\mathbb F_q\); for each pair \((A,B)\), exactly \(q\) cubics arise as \(s\) varies. Translation leaves discriminants invariant, and
\[
\operatorname{disc}(f+c_j)=-4A^3-27(B+c_j)^2
=27\bigl(u-(B+c_j)^2\bigr),\quad u=-\frac{4A^3}{27}.\tag{5}
\]
For monic cubics, the polynomial Möbius/discriminant identity is \(\mu(g)=-\chi(\operatorname{disc}(g))\), including zero for repeated factors. Thus the desired sum equals
\[
-q\chi(27)\sum_{A,B}\chi\!\left(\prod_{j=1}^{3}\bigl(u-(B+c_j)^2\bigr)\right).
\]
Because \(\gcd(3,q-1)=1\), the variable \(u\) ranges bijectively through the field as \(A\) does. Applying (1), this is
\[
-q^2\chi(-27)=-q^2\chi(-3).
\]
The polynomial \(X^2+X+1\) has no root in \(\mathbb F_q\), since a nontrivial cube root of unity would imply \(3\mid q-1\). Its discriminant is \(-3\), hence \(\chi(-3)=-1\), and the final sum is \(q^2\).

## Verification

Run `python3 verify.py`. The stand-alone script classifies cubic factorizations using roots and derivatives rather than the discriminant proof; it also tests the character lemma for four prime fields and an explicitly constructed field of order \(125\). Its successful output is `VERIFY_OK direct_mobius_triples=216 prime_character_triples=496 extension_triples=12 field_order=125`. Finite enumeration is corroboration, not the universal proof.

## Relationship to prior work

Carmon and Rudnick, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field* (arXiv:1205.1599), prove an asymptotic bound for correlations with multiple distinct polynomial shifts, including the present degree and number of shifts; that estimate does not imply this exact identity. Keating and Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions* (arXiv:1504.03444), establish different asymptotic mean and variance results, not the present finite-degree three-point formula. The new character-correlation lemma resolves the fixed-degree three-shift case with no error term.

## Limitations

The result applies only to monic cubics, odd field orders congruent to \(2\) modulo \(3\), and pairwise distinct constant shifts. It does not assert the same value for repeated shifts, even fields, field orders congruent to \(1\) modulo \(3\), nonconstant shifts, or polynomial degrees other than three. Historical literature may contain equivalent special-case results not located in the comparisons.

## References

Carmon, D., and Rudnick, Z., *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599v1 (first publicly available 2012-05-08), https://arxiv.org/abs/1205.1599.

Keating, J. P., and Rudnick, Z., *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444, https://arxiv.org/abs/1504.03444.
