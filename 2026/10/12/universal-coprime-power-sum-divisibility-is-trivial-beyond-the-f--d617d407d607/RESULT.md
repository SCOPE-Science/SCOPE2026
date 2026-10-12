# Universal coprime power-sum divisibility is trivial beyond the first moment

## Finding

For integers \(m\ge 0\) and \(n\ge1\), set
\[
\varphi_m(n)=\sum_{\substack{1\le a\le n\\\gcd(a,n)=1}}a^m,
\qquad
\mathcal D_s=\{k\ge s:\varphi_s(n)\mid\varphi_k(n)\text{ for every }n\ge1\}.
\]
For every integer \(s\ge2\), the universal divisibility set is exactly
\[
\boxed{\mathcal D_s=\{s\}.}
\]
Equivalently, given distinct integers \(s,k\ge2\), the divisibility \(\varphi_s(n)\mid\varphi_k(n)\) fails for at least one positive integer \(n\). In fact the failure occurs among powers of a single suitably chosen prime (which may depend on \(s,k\)).

## Assumptions and scope

Divisibility means divisibility in the ordinary integers. Bernoulli numbers use \(B_0=1\), \(B_1=-1/2\), and the conventional generating series \(t/(e^t-1)\). No upper bound on \(s\), \(k\), or the prime-power exponent is assumed. This result is not a statement about \(s=0\) or \(s=1\).

## Proof

**1. The polynomial on prime powers.** Fix an integer \(m\ge2\) and a prime \(p\). Faulhaber's polynomial \(S_m(X)\in\mathbb Q[X]\) satisfies \(S_m(N)=\sum_{a=1}^N a^m\) at each positive integer \(N\). Define
\[
F_{m,p}(X)=S_m(X)-p^mS_m(X/p).
\]
For every integer \(u\ge1\), deleting the multiples of \(p\) from \(\{1,\dots,p^u\}\) gives the *exact integer identity*
\[
F_{m,p}(p^u)=\varphi_m(p^u).
\]
Faulhaber's formula, the vanishing of odd Bernoulli numbers above index one, and cancellation of the index-one coefficient yield
\[
F_{m,p}(X)=\sum_{\substack{0\le j\le m\\j\ \mathrm{even}}}
\frac{\binom{m+1}{j}B_j}{m+1}(1-p^{j-1})X^{m+1-j}.
\tag{1}
\]
Define \(h_m=1\) for even \(m\), and \(h_m=2\) for odd \(m\); put \(H_{m,p}(X)=F_{m,p}(X)/X^{h_m}\). Every even-index Bernoulli number of positive index is nonzero. Consequently \(H_{m,p}\) has degree \(r_m=m+1-h_m\), nonzero constant coefficient \(C_{m,p}\), and leading coefficient \(L_{m,p}\) given by
\[
L_{m,p}=\frac{p-1}{p(m+1)},\qquad
C_{m,p}=\begin{cases}
B_m(1-p^{m-1}),&m\text{ even},\\
\dfrac m2 B_{m-1}(1-p^{m-2}),&m\text{ odd}.
\end{cases}
\tag{2}
\]
Here \(r_m=2\lfloor m/2\rfloor\), so the only distinct indices with the same degree are neighboring even–odd pairs.

**2. Irreducibility at a good prime.** Given any fixed pair \(2\le s<k\), choose a prime \(p>k+2\) that divides neither the numerator of \(B_{e_s}\) nor the numerator of \(B_{e_k}\), where \(e_m=m\) for even \(m\) and \(e_m=m-1\) for odd \(m\). Such a prime exists because both numerators are fixed, nonzero integers. By the von Staudt–Clausen denominator theorem, \(B_j\) is \(p\)-integral for every even \(j\le k\). For \(m=s,k\), consider \(E_{m,p}(X)=pH_{m,p}(X)\).

By (1), every non-leading coefficient of \(E_{m,p}\) lies in \(p\mathbb Z_{(p)}\), whereas its leading coefficient is \((p-1)/(m+1)\), a \(p\)-unit. Formula (2), the choice of \(p\), and \(m\ge2\) give \(v_p(E_{m,p}(0))=1\). Multiplication by an integer prime to \(p\) clears all coefficient denominators without changing these valuations. Eisenstein's criterion at \(p\) therefore proves that **both \(H_{s,p}\) and \(H_{k,p}\) are irreducible over \(\mathbb Q\)**. The nonzero constant terms also show that neither is divisible by \(X\).

**3. Divisibility at all prime powers forces polynomial divisibility.** We use a general lemma. Suppose \(P,Q\in\mathbb Q[X]\), \(P\ne0\), and \(P(p^u),Q(p^u)\) are integers with \(P(p^u)\ne0\), while \(P(p^u)\mid Q(p^u)\) for all positive integers \(u\). Then \(P\mid Q\) in \(\mathbb Q[X]\). Indeed, divide \(Q=PA+R\) with \(\deg R<\deg P\). Choose a positive integer \(M\) making every coefficient of \(MA\) and \(MR\) integral. Then
\[
\frac{MR(p^u)}{P(p^u)}
=M\frac{Q(p^u)}{P(p^u)}-MA(p^u)\in\mathbb Z.
\]
As \(u\to\infty\), this quantity tends to zero since \(\deg R<\deg P\). It is eventually the zero integer, so \(R\) vanishes at infinitely many points and is the zero polynomial.

**4. Comparison of the two irreducible factors.** Suppose, contrary to the claim, that \(\varphi_s(n)\mid\varphi_k(n)\) for all \(n\). Applied to the chosen prime's powers, step 3 gives \(F_{s,p}\mid F_{k,p}\). Since \(F_{s,p}=X^{h_s}H_{s,p}\), \(F_{k,p}=X^{h_k}H_{k,p}\), and \(\gcd(H_{s,p},X)=1\), we deduce \(H_{s,p}\mid H_{k,p}\). Irreducibility of the latter forces the two factors to be associates.

But \(r_k>r_s\) unless \(s\) is even and \(k=s+1\). In that sole equal-degree case, the ratio of leading coefficients is
\[
\frac{L_{k,p}}{L_{s,p}}=\frac{s+1}{s+2},
\]
whereas the ratio of constant coefficients is
\[
\frac{C_{k,p}}{C_{s,p}}=\frac{s+1}{2}.
\]
These ratios differ for \(s\ge2\), contradicting association. Thus no \(k>s\) belongs to \(\mathcal D_s\); the tautological membership \(s\in\mathcal D_s\) proves the theorem. For the additionally stated reverse-order case \(s>k\ge2\), the prime-power witness \(n=3\) suffices, since \(\varphi_s(3)=1+2^s>1+2^k=\varphi_k(3)\).

## Verification

The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. It reconstructs Bernoulli numbers from their recurrence, checks the coprime-residue prime-power identity and the Eisenstein valuation pattern at an admissible prime for each moment \(2\le m\le20\), and performs independent polynomial divisions for all \(171\) pairs \(2\le s<k\le20\). Its recorded output is `verification_output.txt`. This finite regression is not used in place of the proof of the unrestricted statement.

## Relationship to prior work

Büyükaşık, Göral and Sertbaş introduced these divisibility sets and proved their finiteness for each \(s\ge0\) (Theorem 1), with detailed work on \(\mathcal D_1\) (Theorem 2). Their published Faulhaber/Bernoulli expansion and von Staudt–Clausen tools are acknowledged here; their finiteness theorem does not imply the present exact classification for every \(s\ge2\). Campbell subsequently established the special \(s=1\) conjecture \(\mathcal D_1=\{1,3,15\}\); the present proof instead treats all higher moments. The obstruction from irreducible prime-power polynomials gives a complete result for those higher indices.

## Limitations

The proof gives a witness prime and existence of a prime-power witness but not an effective bound for the smallest exponent witnessing failure in each pair. It makes no new assertion about the zeroth and first moments. An exhaustive claim about the entire world literature is not implied by the sources inspected; an unindexed equivalent result remains a bibliographic risk.

## References

1. E. Büyükaşık, H. Göral, and D. C. Sertbaş, *A note on variants of Euler's \(\varphi\)-function*, Publicationes Mathematicae Debrecen **105** (2024), 67–89. DOI: 10.5486/PMD.2024.9674. Author-deposited full text: https://www.researchgate.net/publication/363587058_A_note_on_variants_of_Euler's_varphi-function.
2. J. M. Campbell, *On a problem on a generalization of Euler's totient function* (2026), arXiv:2606.01633, https://arxiv.org/abs/2606.01633.
3. Classical Faulhaber power-sum formula, von Staudt–Clausen theorem for Bernoulli denominators, nonvanishing of positive even Bernoulli numbers, and Eisenstein's irreducibility criterion (standard background results).
