# Exact modular period and preperiod phases of weighted involution numbers

## Finding

For each integer \(c\), define the weighted involution sequence by
\[
T_c(0)=T_c(1)=1,\qquad
T_c(n)=T_c(n-1)+c(n-1)T_c(n-2)\quad(n\ge2).
\]
This is the matching enumerator of a complete graph with weight \(c\) per edge (for negative \(c\), the same integral polynomial is evaluated algebraically). For each integer modulus \(M\ge2\), let \(s(c,M)\) be the **least** nonnegative index from which the sequence modulo \(M\) is periodic, and let \(d(c,M)\) be the **least** period of that eventual tail.

Write \(M=2^a m\), where \(m\) is odd and \(a\ge0\), and put
\[
d_o=\frac{m}{\gcd(m,|c|)},\qquad \gcd(m,0):=m.
\]
The complete classification is as follows.

* If \(c=0\), then \((s,d)=(0,1)\).
* If \(c\) is odd, then \(d=d_o\); moreover \(s=0\) when \(a=0\), and \(s=4a-2\) when \(a\ge1\).
* If \(c\ne0\) is even, set \(t=\nu_2(c)\ge1\). Then \(s=0\) and \(d=d_oP_2(a,t)\), where
\[
P_2(a,t)=
\begin{cases}
1,&a\le t,\\
2^{\max\{2,a-1\}},&t=1<a,\\
2^{a-t+1},&t\ge2,\ a>t.
\end{cases}
\]

The underlying sharper dyadic facts are, for every \(n\ge0,r\ge1\):
\[
\nu_2\bigl(T_c(n+2^r)-T_c(n)\bigr)=r+t-1
\quad\text{if }t\ge2,
\]
and, for \(t=1,r\ge2\),
\[
T_c(n+2^r)\equiv T_c(n)\pmod{2^{r+1}}.
\]
The cancellation in the second formula is the source of the exceptional \(c\equiv2\pmod4\) branch.

## Assumptions and scope

Every asserted formula quantifies over **all** integer weights \(c\) and moduli \(M\ge2\), including composite moduli, zero, and negative weights. Valuations of nonzero integers are taken in the standard sense; the dyadic exact-shift assertion is only for \(c\ne0\) with \(\nu_2(c)\ge2\), so its difference is indeed nonzero. A period is required to work at every index in the claimed tail, not only up to a finite cutoff. A preperiod is the earliest such starting index; both minima are global.

The known \(c=1\) period/preperiod classification is explicitly excluded from any claim of priority. The new arithmetical content is the uniform weighted theorem, especially the two nontrivial even-weight dyadic branches, including a sharp exact-shift valuation.

## Proof

**1. Integral binomial representation and prime-power shift.** Counting disjoint edges gives the exact polynomial identity
\[
T_c(n)=\sum_{j=0}^{\lfloor n/2\rfloor}(2j-1)!!\,c^j\binom n{2j},
\qquad (-1)!!:=1.
\]
For any nonnegative \(n,h\), Vandermonde's identity therefore yields
\[
T_c(n+h)-T_c(n)=
\sum_{j\ge1}(2j-1)!!\,c^j
\sum_{\ell=1}^{2j}\binom h\ell\binom n{2j-\ell}.
\tag{1}
\]
All sums are finite, with out-of-range binomial coefficients zero. If \(h=p^r\), then for \(1\le\ell\le h\),
\[
\nu_p\binom{p^r}{\ell}=r-\nu_p(\ell),
\]
obtained from \(\binom{p^r}{\ell}=\frac{p^r}{\ell}\binom{p^r-1}{\ell-1}\), whose last binomial is a \(p\)-unit. Terms with \(\ell>h\) vanish.

**2. Odd prime powers and sharp lower bound.** Fix an odd prime \(p\), exponent \(e\ge1\), and \(v=\nu_p(c)\), with \(\nu_p(0)=\infty\). If \(v\ge e\), all terms except \(j=0\) are zero modulo \(p^e\), so the sequence is constant \(1\). Otherwise put \(r=e-v\ge1\) (in particular \(r=e\) when \(v=0\)). For every \(j\ge1\), \(1\le\ell\le2j\), the term of (1) has valuation at least
\[
r-\nu_p(\ell)+jv+\nu_p((2j-1)!!).
\]
When \(v=0\), \(p^{\nu_p(\ell)}\) is odd and at most \(2j\), hence appears among the odd factors through \(2j-1\); so \(\nu_p((2j-1)!!)\ge\nu_p(\ell)\). When \(v\ge1\), for \(j=1\) every \(\ell\le2\) is prime to \(p\); for \(j\ge2\), \(\nu_p(\ell)\le\lfloor\log_p(2j)\rfloor\le j-1\), hence \(jv\ge v+\nu_p(\ell)\). Thus the shift \(p^{\max(e-v,0)}\) is a period modulo \(p^e\).

To prove minimality, suppose \(h>0\) is any **eventual** period modulo \(p^e\). Subtract the recurrences at indices \(n+h\) and \(n\), using periodicity at three consecutive terms, to obtain
\[
ch\,T_c(n-1)\equiv0\pmod{p^e}
\]
for every sufficiently large \(n\). The already established pure period modulo \(p^e\) gives arbitrarily large indices \(n-1\) with \(T_c(n-1)\equiv T_c(0)=1\pmod{p^e}\). Consequently \(p^e\mid ch\), proving that the least eventual period at \(p^e\) equals \(p^{\max(e-v,0)}\). Chinese remaindering over the odd prime powers gives exactly \(d_o\); this odd-modulus component is purely periodic.

**3. Even weights divisible by four.** Suppose \(t=\nu_2(c)\ge2\) and put \(h=2^r\), \(r\ge1\). The \(j=1\) contribution to (1) is
\[
c\left(hn+\binom h2\right)
=c\,2^{r-1}(2n+2^r-1),
\]
which has exact valuation \(r+t-1\) because the parenthesis is odd. Every contribution with \(j\ge2\) has valuation at least
\[
r+jt-\lfloor\log_2(2j)\rfloor\ge r+t.
\]
The final inequality holds for all \(j\ge2,t\ge2\), including \(j=2,t=2\). Hence the exact-shift formula follows without any cancellation ambiguity. If \(a\le t\), the entire sequence equals \(1\pmod{2^a}\). Otherwise \(2^{a-t+1}\) is a period; the recurrence comparison above requires every eventual period to be divisible by \(2^{a-t}\), and the exact-shift formula shows that \(2^{a-t}\) itself fails. The period-divisibility property of a periodic tail therefore forces the least period to be \(2^{a-t+1}\). All these periods work from index zero.

**4. Even weights congruent to two modulo four.** Write \(c=2u\) with \(u\) odd. If \(h=2^r\) and \(r\ge2\), every \(j\ge3\) contribution to (1) has valuation at least
\[
r+j-\lfloor\log_2(2j)\rfloor\ge r+1.
\]
For \(j=1\), only \(c\binom h2\) remains modulo \(2^{r+1}\), contributing \(2^r u\). For \(j=2\), the only term surviving modulo \(2^{r+1}\) has \(\ell=4\) and contributes
\[
3c^2\binom h4\equiv2^r u^2\pmod{2^{r+1}},
\]
because \(\nu_2\binom{2^r}4=r-2\) and its odd part contributes \(1\pmod2\). The two terms sum to \(2^r(u+u^2)\), divisible by \(2^{r+1}\), as \(u\) is odd. Thus \(2^r\) is a period modulo \(2^{r+1}\), for every \(r\ge2\).

Modulo two, the sequence is constantly one. Modulo four, \(T_c(2)-T_c(0)=c\not\equiv0\pmod4\), so period two is impossible while the proved period four works. For \(a\ge3\), the period \(2^{a-1}\) follows from the congruence above; the recurrence comparison forces every period to be divisible by \(2^{a-1}\). Hence the least period is \(2^{\max\{2,a-1\}}\) whenever \(a>1\). All shifts hold from index zero.

**5. Odd weights and the sharp preperiod.** Suppose \(c\) is odd. Induction on \(k\ge0\) gives
\[
\begin{aligned}
\nu_2(T_c(4k))&=k,\\
\nu_2(T_c(4k+1))&=k,\\
\nu_2(T_c(4k+2))&\ge k+1,\\
\nu_2(T_c(4k+3))&\ge k+1.
\end{aligned}
\tag{2}
\]
For \(k=0\), the first two values equal one and the next two are even. If (2) holds through \(4k+1\), the recurrence and the oddness of \((4k+1)c\) show that \(T_c(4k+2)\) is divisible by \(2^{k+1}\). The recurrence for \(4k+3\) similarly gives divisibility by \(2^{k+1}\). Substitution twice yields the exact identities
\[
\begin{aligned}
T_c(4k+4)&=(4k+2)c\,T_c(4k+1)+(4k+4)c\,T_c(4k+2),\\
T_c(4k+5)&=T_c(4k+4)+(4k+4)c\,T_c(4k+3).
\end{aligned}
\]
The first term in the first identity has exact valuation \(k+1\), and the second valuation at least \(k+3\); thus the sum has exact valuation \(k+1\). The second identity preserves that exact valuation. This completes the induction.

Equation (2) implies \(T_c(n)\equiv0\pmod{2^a}\) for all \(n\ge4a-2\), while \(T_c(4a-3)\) has exact valuation \(a-1\). Every eventual-periodic tail must start at or after \(4a-2\), since its dyadic residues are eventually zero and the earlier nonzero value cannot recur infinitely often. Thus the exact dyadic preperiod is \(4a-2\), with eventual period one. For \(a=0\) this component does not arise.

**6. Assemble arbitrary moduli.** By the Chinese remainder theorem, eventual equality modulo \(M\) holds exactly when equality holds at its odd prime powers and dyadic prime power. The odd component is purely periodic with exact period \(d_o\); the dyadic component is purely periodic with a power-of-two period for even \(c\), or eventually identically zero at exact index \(4a-2\) for odd \(c\). Their least common multiple is therefore the claimed \(d(c,M)\), with the claimed earliest \(s(c,M)\). For \(c=0\), every term equals one. This proves all cases.

## Verification

The attached standalone `verify.py` checks the recurrence directly for integer weights and composite moduli, compares periods with all proper-divisor candidates on finite windows, tests the exact dyadic shift valuations and the exceptional cancellation, and performs deeper dyadic tests through modulus \(2^{12}\). Its tests are finite checks; Steps 1–6 above establish the infinite assertions. Reproducible execution: `python3 verify.py` using the standard library.

## Relationship to prior work

Kim and Kim (2009), Section 6, **already prove the exact minimum preperiod and period for the unweighted case** \(c=1\), including the formula \(4a-2\) for even moduli. Their Section 4 develops weighted involution polynomials. Those results must not be represented as new here. Amdeberhan and Moll (2014) give the classical involution recurrence, generating functions, and arithmetic background. Bednarz and Wołowiec-Musiał (2019), Theorems 8 and 10, give general weighted telephone-number shift congruences (notably for odd shift moduli). Kallat (2026) develops even broader universal weighted-permutation shift congruences and residue-class dynamics. These established results overlap with and in places imply portions of the odd-modulus discussion here, but none of their inspected statements gives the exact minimum periods for every **nonunit weighted** \(c\) across all dyadic exponents, or the exact all-index dyadic shift valuation for weights divisible by four. The new structural distinction is precisely the valuation-controlled period family versus the exceptional cancellation at weights congruent to two modulo four, assembled with the odd and zero weights.

The existence of another unlocated historical specialization is not ruled out.

## Limitations

The classification applies only to the one-parameter weighted involution/matching family, not arbitrary weighted-permutation sequences. It determines minimal eventual periods and starting indices, not complete residue distributions or odd-part prime-power lifting at arbitrary perturbed recurrences. The \(c=1\) case and basic odd-modulus congruences are known prior work; neither is independently novel. Computational tests cannot establish priority or replace the proof.

## References

1. D. Kim and J. S. Kim, *A combinatorial approach to the power of 2 in the number of involutions*, arXiv:0902.4311, first posted 2009-02-25, Sections 3, 4, 6. https://arxiv.org/abs/0902.4311
2. T. Amdeberhan and V. H. Moll, *Involutions and their progenies*, arXiv:1406.2356, first posted 2014-06-09, Sections 2–4. https://arxiv.org/abs/1406.2356
3. U. Bednarz and M. Wołowiec-Musiał, *On a new generalization of telephone numbers*, Turkish Journal of Mathematics **43** (2019), 1595–1603, DOI:10.3906/mat-1812-108, especially Theorems 8 and 10. https://doi.org/10.3906/mat-1812-108
4. A. Kallat, *Universal Shift Congruences for Weighted Permutation Sequences*, arXiv:2610.15849, first posted 2026-10-11, Theorem 1 and Corollary 25. https://arxiv.org/abs/2610.15849
