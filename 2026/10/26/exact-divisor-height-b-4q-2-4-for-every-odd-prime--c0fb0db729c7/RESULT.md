# Exact divisor height \(B(4q^2)=4\) for every odd prime

## Finding
For a nonzero integer polynomial \(P\), define its height \(H(P)=\max_j|[X^j]P|\), and for every positive integer \(n\) define
\[
B(n)=\max\{H(P):P\in\mathbb Z[X]\text{ is monic and }P\mid X^n-1\}.
\]
**Theorem.** For every odd prime \(q\),
\[
B(4q^2)=4.
\]
More strongly, for every monic integral divisor \(F\mid X^{4q}-1\) and every residue \(0\le r<q\),
\[
\sum_{j\ge0}\left|[X^{r+jq}]F\right|\le4.\tag{1}
\]
This yields the \(p=2\) specialization of the prime-square-pair maximal-height conjecture in Ryan--Ward--Ward (2010): the second of their proposed extremal cyclotomic products has height exactly four, and the maximum is four.

## Assumptions and scope
Throughout, \(q\) is an arbitrary odd prime, and \(X\) is an indeterminate. The coefficient \([X^j]F\) is zero outside the degree support. All polynomial factors considered are over \(\mathbb Z[X]\), and the maximum is over all divisors; no restriction on their degree or on which cyclotomic factors are selected is imposed. The statement does not concern other exponent pairs or the case of two odd primes.

## Proof
**Step 1: a residue-slice inequality at exponent \(4q\).** Write
\[
U=\Phi_q=\sum_{j=0}^{q-1}X^j,\qquad
U_-=\Phi_{2q}=\sum_{j=0}^{q-1}(-1)^jX^j,\qquad
V=\Phi_{4q}=\sum_{j=0}^{q-1}(-1)^jX^{2j}.
\]
Since the irreducible factors of \(X^{4q}-1\) are precisely \(\Phi_1,\Phi_2,\Phi_4,U,U_-,V\), any monic divisor is \(F=AB\), where \(A\) is a product of a subset of \(\{X-1,X+1,X^2+1\}\) and \(B\) is a product of a subset of \(\{U,U_-,V\}\). Define \(T_r(P)=\sum_{j\ge0}|[X^{r+jq}]P|\). Convolution obeys
\[
T_r(AP)\le \sum_i |[X^i]A|T_{r-i\pmod q}(P).\tag{2}
\]
Every possible \(A\) has coefficient \(\ell^1\)-norm at most four. For the following six types of \(B\), each residue modulo \(q\) supports at most one nonzero coefficient of magnitude one: \(1,U,U_-,V,UU_-\), and \(UU_-V\). Indeed
\[
UU_-=\sum_{j=0}^{q-1}X^{2j},\qquad UU_-V=\sum_{j=0}^{q-1}X^{4j},
\]
and \(1,2,4\) are invertible modulo the odd prime \(q\). Thus (2) proves \(T_r(AB)\le4\) for these six choices (including the empty product). The only remaining choices are \(B=UV\) and \(B=U_-V\). The substitution \(X\mapsto-X\) exchanges \(U\) with \(U_-\), fixes \(V\), exchanges \(\Phi_1\) with \(\Phi_2\) up to signs, and leaves all \(T_r\) unchanged. It therefore suffices to analyze \(B=UV\).

For \(B=UV\), if \(\Phi_1=X-1\) divides \(A\), use \((X-1)U=X^q-1\). When \(\Phi_4\) is absent, \(F\) is \((X^q-1)V\), optionally times \(X+1\); because \(V\) has one term per residue, its residue-slice sums are at most \(2\) before the optional multiplication and at most \(4\) after. If \(\Phi_4\) is present, the identity \((X^2+1)V=1+X^{2q}\) makes
\[
F=(X^q-1)(1+X^{2q})
\]
optionally times \(X+1\). The displayed polynomial consists of four signed monomials all in residue zero, and multiplication by \(X+1\) moves an additional copy to residue one without collisions, since \(q\ge3\); all slice sums are at most four.

If \(\Phi_1\) is absent but \(\Phi_4\) is present, then \(F=U(1+X^{2q})\), optionally times \(X+1\). Because \(U\) has exactly one coefficient per residue, its slice sums are exactly two before, and at most four after, the optional multiplication.

It remains to handle \(A=1\) and \(A=X+1\). For \(A=1\), the coefficient \([X^n]UV\) is an alternating sum over the consecutive integers \(j\) satisfying \(0\le j<q\) and \(0\le n-2j<q\), hence lies in \(\{-1,0,1\}\). Since \(\deg(UV)=3q-3\), each residue has at most three coefficient positions, so \(T_r(UV)\le3\).

For \(A=X+1\), write \(W=(X+1)UV=\sum_n w_nX^n\). The coefficients \(a_t=[X^t](X+1)U\) are one for \(t\in\{0,q\}\), two for \(1\le t\le q-1\), and zero otherwise. Thus
\[
w_n=\sum_{j=\max(0,\lceil(n-q)/2\rceil)}^{\min(q-1,\lfloor n/2\rfloor)}(-1)^j a_{n-2j}.
\]
For \(0\le n<q\), the alternating sum gives \(|w_n|=1\) for even \(n\) and \(|w_n|\le2\) for odd \(n\). For \(q\le n\le2q-1\), there are exactly \((q+1)/2\) consecutive summands: all coefficients \(a_{n-2j}\) equal two except one endpoint, which equals one. The alternating sum therefore equals \(+1\) or \(-1\) (the number of summands may be even or odd); hence \(|w_n|=1\) throughout the middle block. Finally, \(W\) is self-reciprocal of degree \(3q-2\), because each of \(X+1\), \(U\), and \(V\) is self-reciprocal for odd \(q\). For each \(0\le r\le q-2\), its three coefficient positions obey
\[
|w_r|+|w_{q+r}|+|w_{2q+r}|
=|w_r|+1+|w_{q-2-r}|\le 1+1+2=4,
\]
since \(q-2\) is odd and the outer indices have opposite parity. For \(r=q-1\) only the first two positions occur, with combined magnitude at most three. This proves (1) in every case.

**Step 2: lift to exponent \(4q^2\).** The irreducible cyclotomic factors of \(X^{4q^2}-1\) comprise the preceding six and \(\Phi_{q^2},\Phi_{2q^2},\Phi_{4q^2}\). The latter three equal \(U(X^q), U_-(X^q), V(X^q)\), respectively. Each possible product \(G\) of the three polynomials \(U,U_-,V\) has coefficients in \(\{-1,0,1\}\): this was proved above for the single factors, the products \(UU_-,UU_-V\), and \(UV\), while \(U_-V=(UV)(-X)\). Consequently every monic divisor of \(X^{4q^2}-1\) has the form \(F(X)G(X^q)\) with \(F\mid X^{4q}-1\), and \([X^j]G\in\{-1,0,1\}\). For every \(n\ge0\), writing \(n\equiv r\pmod q\),
\[
|[X^n]F(X)G(X^q)|\le\sum_{k\ge0}|[X^{n-kq}]F|\le T_r(F)\le4.
\]
Thus \(B(4q^2)\le4\).

**Step 3: sharpness.** The monic polynomial
\[
P(X)=\frac{X^4-1}{X-1}\cdot\frac{X^{q^2}-1}{X-1}
= (1+X+X^2+X^3)(1+X+\cdots+X^{q^2-1})
\]
is the product \(\Phi_2\Phi_4\Phi_q\Phi_{q^2}\), so it divides \(X^{4q^2}-1\). As \(q\ge3\), its coefficient at \(X^3\) is exactly four. Therefore \(B(4q^2)\ge4\), completing the proof.

## Verification
The accompanying standalone `verify.py` constructs every cyclotomic factor by exact integer coefficients, enumerates all 64 monic divisors of \(X^{4q}-1\), computes all residue-slice sums, and independently enumerates all 512 monic divisors of \(X^{4q^2}-1\) for \(q\in\{3,5,7,11,13\}\). Each case has maximal slice sum and coefficient height equal to four. The program also checks the displayed witness factorization and its coefficient at exponent three, and prints `VERIFY_OK`. These finite tests corroborate, but do not imply, the universal result; the proof above does.

## Relationship to prior work
Ryan, B. C. Ward and R. Ward (2010, arXiv:1009.5970, published Conjecture 4.1, preprint Conjecture 3.3) conjectured that the maximum for two squared distinct prime factors comes from one of two specified cyclotomic products, and supplied computations for \(p<q<60\). Specializing their second product to \(p=2\) gives the sharp witness here; the new result proves the uniform maximum and therefore their prediction in this specialization. Their Theorem 3.1 supplies the lower bound four in this setting; the residue-slice upper bound and its proof are the contribution. Kaplan (2009) and Decker--Moree (2010/2011) treat the exponent family \(p^2q\), which is distinct from \(p^2q^2\). Wang (2013) treats \(pq^b\), which likewise does not include \(4q^2\). Existing tables verify numerous individual values but are not proofs for every prime. The known absence of an explicit formula in the original conjectural account is not itself a proof of novelty; equivalently formulated later work remains a residual literature risk.

## Limitations
No assertion is made about \(B(p^2q^2)\) for odd \(p\), or \(B(2^a q^b)\) outside the specified exponent pair. This is a self-contained mathematical proof and finite computational corroboration, not an independent peer review or a claim of absolute bibliographic novelty.

## References
1. N. C. Ryan, B. C. Ward and R. Ward, *Some conjectures on the maximal height of divisors of* \(X^n-1\), Involve **3** (2010), 451--457. arXiv:1009.5970; https://arxiv.org/abs/1009.5970 ; doi:10.2140/involve.2010.3.451.
2. N. Kaplan, *Bounds for the maximal height of divisors of* \(X^n-1\), Journal of Number Theory **129** (2009), 2673--2688; doi:10.1016/j.jnt.2009.04.015.
3. A. Decker and P. Moree, *Coefficient convexity of divisors of* \(X^n-1\), arXiv:1010.3938 (2010); https://arxiv.org/abs/1010.3938.
4. S. Wang, *Maximal height of divisors of* \(X^{pq^b}-1\), arXiv:1312.3108 (2013); https://arxiv.org/abs/1312.3108.
