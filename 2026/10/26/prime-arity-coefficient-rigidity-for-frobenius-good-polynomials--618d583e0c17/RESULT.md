# Prime-arity coefficient rigidity for Frobenius-good polynomials

## Finding

Let \(p\) be prime and \(n\ge 1\). Call a polynomial \(P\in\mathbb Z[x]\) **\(n\)-good** when
\[
P(x^{p^j})\equiv P(x)^{p^j}\pmod{p^{j+1}}
\]
coefficientwise in \(\mathbb Z[x]\) for every integer \(j\) with \(0\le j\le n\). If \(P\) is monic of positive degree \(d\) with \(p\mid d\), then every coefficient of \(x^i\) for which \(p\nmid i\) is divisible by \(p^n\). The exponent \(n\) is optimal for every prime and every \(n\ge1\): the polynomial \(P(x)=(1+x)^{p^n}\) is \(n\)-good, has degree divisible by \(p\), and has coefficient \(p^n\) at \(x\).

## Assumptions and scope

All congruences are formal coefficientwise congruences in \(\mathbb Z[x]\), not merely congruences after substituting integer values for \(x\). The prime \(p\) and integer \(n\ge1\) are arbitrary. The degree \(d\) is positive, \(p\mid d\), and the leading coefficient is exactly \(1\). No irreducibility hypothesis is imposed. The result gives a coefficient divisibility constraint only; it does not assert a factorization theorem or an ascending-chain property for a monoid algebra.

## Proof

First we derive a lifting step. If \(A-B\in p^r\mathbb Z[x]\) with \(r\ge1\), write \(A=B+p^rQ\). The binomial expansion shows \(A^p-B^p\in p^{r+1}\mathbb Z[x]\): the linear term has a factor \(p^{r+1}\), each intermediate binomial coefficient \(\binom pk\) is divisible by \(p\), and the final term has a factor \(p^{rp}\), where \(rp\ge r+1\). Since \(P\) is \(n\)-good, applying this to the congruence at \(j=n-1\) and combining it with the congruence at \(j=n\) gives
\[
P(x^{p^n})\equiv P(x^{p^{n-1}})^p\pmod{p^{n+1}}.
\]
Replacing \(x^{p^{n-1}}\) by a new indeterminate preserves coefficientwise divisibility, so
\[
P(x^p)\equiv P(x)^p\pmod{p^{n+1}}. \tag{1}
\]

Write \(P(x)=\sum_{i=0}^d b_i x^i\), where \(b_d=1\). Suppose the conclusion fails. Choose the largest index \(m\) such that \(p\nmid m\) and \(p^n\nmid b_m\). Because \(p\mid d\), we have \(m<d\). Set \(S=(p-1)d+m\). Then \(p\nmid S\), so the coefficient of \(x^S\) in \(P(x^p)\) is zero.

Consider a term contributing to the coefficient of \(x^S\) in \(P(x)^p\), with factor indices \(i_1,\ldots,i_p\) and \(i_1+\cdots+i_p=S\). Put \(\delta_a=d-i_a\). Their sum is \(d-m\), which is not divisible by \(p\). Thus at least one \(\delta_a\) is not divisible by \(p\); the corresponding index \(i_a=d-\delta_a\) is not divisible by \(p\) and satisfies \(i_a\ge m\). If \(i_a=m\), then all other deficits are zero, so this term is one of the \(p\) permutations of \(b_m b_d^{p-1}\). Otherwise \(i_a>m\), and maximality of \(m\) gives \(p^n\mid b_{i_a}\).

Moreover, every multinomial coefficient contributing to degree \(S\) is divisible by \(p\): if all \(p\) indices were equal, their sum would be divisible by \(p\), contrary to \(p\nmid S\). Therefore every term other than the \(p\) special permutations is divisible by \(p^{n+1}\). The coefficient of \(x^S\) in \(P(x)^p\) is consequently congruent to \(p b_m\) modulo \(p^{n+1}\). Since \(p^n\nmid b_m\), this coefficient is not divisible by \(p^{n+1}\), contradicting (1). This proves the divisibility assertion.

It remains to prove sharpness. For \(P(x)=(1+x)^{p^n}\) and any \(0\le j\le n\), the freshman's-dream congruence gives \((1+x)^{p^j}\equiv 1+x^{p^j}\pmod p\). Repeatedly applying the lifting step above yields
\[
(1+x)^{p^{n+j}}\equiv (1+x^{p^j})^{p^n}\pmod{p^{n+1}}.
\]
The right-hand side is \(P(x^{p^j})\) and the left-hand side is \(P(x)^{p^j}\). Since \(j\le n\), this implies the required congruence modulo \(p^{j+1}\). Thus \(P\) is \(n\)-good. Its degree is \(p^n\), and its coefficient of \(x\) is exactly \(p^n\), not divisible by \(p^{n+1}\). Hence the bound is sharp.

## Verification

The proof uses only coefficientwise polynomial congruences and the binomial expansion. The critical coefficient is \(S=(p-1)d+m\); its residue modulo \(p\) is nonzero, which forces the relevant multinomial coefficients to carry a factor of \(p\). The sharpness family is verified symbolically by the same lifting step. No finite enumeration is used as evidence for the universal statement.

## Relationship to prior work

Bu, Gotti, Li, and Zhao define \(n\)-good polynomials and prove the corresponding coefficient divisibility lemma for \(p=2\), monic polynomials of even degree, and odd exponents in Section 3.2, Lemma 3.7 of *One-dimensional monoid algebras and ascending chains of principal ideals* (arXiv:2409.00580v1). The present statement reduces to that lemma when \(p=2\), and extends the coefficient obstruction to every prime. Their paper uses the dyadic lemma in a factorization argument for a particular one-dimensional monoid algebra; no analogous downstream monoid-algebra conclusion is claimed here. The Frobenius-lift congruences in Beukers and Vlasenko's *Dwork Crystals III* are conceptually related but concern coefficients of Laurent-series expansions of rational functions under additional geometric hypotheses, not this monic-polynomial coefficient theorem.

## Limitations

The result is a sharp coefficient lemma, not a classification of all \(n\)-good polynomials. It does not establish that a corresponding factorization or almost-ACCP theorem holds for any family beyond the setting already studied in the cited literature. The novelty assessment is limited to the sources and targeted searches recorded in the accompanying review data; absence from a search is not a proof of universal novelty.

## References

1. Alan Bu, Felix Gotti, Bangzheng Li, and Alex Zhao, *One-dimensional monoid algebras and ascending chains of principal ideals*, arXiv:2409.00580v1, first submitted 2024-09-01; especially Definition 3.3 and Lemma 3.7. https://arxiv.org/abs/2409.00580
2. Frits Beukers and Masha Vlasenko, *Dwork Crystals III: From Excellent Frobenius Lifts Towards Supercongruences*, International Mathematics Research Notices (2023), DOI:10.1093/imrn/rnad101. https://doi.org/10.1093/imrn/rnad101
