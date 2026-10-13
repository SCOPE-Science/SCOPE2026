# Mixed prime-power towers for prime-base binomial congruences
## Finding
Fix distinct primes \(q\) and \(p\), with \(p\ge5\), and an integer \(t\ge1\). For every integer \(j\ge0\), define
\[
B_j=\binom{q^{t+1}p^j}{q^tp^j},\qquad
\beta_{p,q,t}=\lim_{j\to\infty}B_j\in\mathbb Z_p.
\]
Let \(\omega_p(q)\) be the unique Teichmüller unit congruent to \(q\) modulo \(p\), and set
\[
H_{p,q,t}=\nu_p\bigl(\beta_{p,q,t}-\omega_p(q)^{q^t}\bigr)
\in\mathbb Z_{\ge0}\cup\{\infty\}.
\]
Here \(\nu_p(0)=\infty\), and \(s_q(k)\) is the sum of the base-\(q\) digits of \(k\). For every integer \(r\ge1\), put \(n=q^tp^r\). Then the exact equivalence is
\[
\boxed{\binom{qn}{n}\equiv q^n\pmod n
\quad\Longleftrightarrow\quad
r\le H_{p,q,t}\quad\text{and}\quad
s_q\bigl((q-1)p^r\bigr)\ge(q-1)t.}
\]
The first condition forms an initial segment in \(r\), while the independent digit-sum filter may delete its members. At \(t=1\) the digit condition always holds, so the solutions \(n=qp^r\) form **exactly** the initial segment \(1\le r\le H_{p,q,1}\), which may be empty or infinite.

For \(1\le r\le3\) the p-adic condition has the finite exact test
\[
\binom{q^{t+1}}{q^t}\equiv q^{q^t p^{r-1}}\pmod{p^r}.
\]
At higher layers the p-adic limit, not just the unscaled binomial coefficient, governs the answer. A sharp non-Wieferich cubic example is \((q,p,t)=(31,5,1)\): precisely \(r=1,2,3\) pass, while every \(r\ge4\) fails, although \(31^4\not\equiv1\pmod{25}\). In contrast, \((q,p,t)=(19,7,2)\) has \(H_{7,19,2}=2\) but neither \(r=1\) nor \(r=2\) passes its digit filter.

## Assumptions and scope
All parameters are ordinary integers, \(q,p\) are distinct positive primes, \(p\ge5\), \(t\ge1\), \(r\ge1\). There is no claim at \(p=2,3\), no restriction on which prime is larger, and no assertion that the p-adic distance \(H_{p,q,t}\) is finite. The q-adic digit criterion is exact for **each** \(r\), not an asymptotic bound. The first public source for the motivated congruence was arXiv:2606.30232v1, submitted June 29, 2026.

## Proof
**1. Existence and effective precision of the binomial limit.** For each \(j\ge1\), set \(a=q^{t+1}p^{j-1}\), \(b=q^tp^{j-1}\). Jacobsthal's binomial dilation congruence for \(p\ge5\) states that
\[
\binom{ap}{bp}\equiv\binom ab\pmod{p^{3+\nu_p(ab(a-b))}}.
\]
Here \(p\nmid q\) and \(\nu_p(ab(a-b))\ge3(j-1)\), hence
\[
B_j\equiv B_{j-1}\pmod{p^{3j}}.
\]
Consequently the sequence is Cauchy in \(\mathbb Z_p\), and for every \(j\ge0\)
\[
\beta_{p,q,t}\equiv B_j\pmod{p^{3(j+1)}}.
\]
In particular \(\beta_{p,q,t}\equiv B_r\pmod{p^r}\). No claim that the binomial limit is a p-adic unit is required: it can be divisible by \(p\).

**2. The matching p-adic exponential limit.** Since \(p\nmid q\), Fermat's theorem and lifting the exponent yield
\[
\nu_p\bigl(q^{p^{m+1}}-q^{p^m}\bigr)
=\nu_p(q^{p-1}-1)+m\ge m+1\qquad(m\ge0).
\]
Thus \(q^{p^m}\to\omega_p(q)\), and
\[
q^{q^tp^r}\equiv\omega_p(q)^{q^t}\pmod{p^r}.
\]
This works for all prime \(q\ne p\), including \(q=2\), because \(p\) is odd.

**3. The exact \(p^r\)-test.** By the two preceding congruences,
\[
\binom{q^{t+1}p^r}{q^tp^r}\equiv q^{q^tp^r}\pmod{p^r}
\ \Longleftrightarrow\ 
\beta_{p,q,t}\equiv\omega_p(q)^{q^t}\pmod{p^r}
\ \Longleftrightarrow\ r\le H_{p,q,t}.
\]
For \(r\le3\), the first-step tail bound gives \(\beta_{p,q,t}\equiv B_0\pmod{p^3}\), and the exponential tail gives \(\omega_p(q)\equiv q^{p^{r-1}}\pmod{p^r}\). The displayed finite criterion follows.

**4. The independent \(q^t\)-test.** For \(n=q^tp^r\), clearly \(q^t\mid q^n\), so its congruence modulo \(q^t\) is equivalent to \(q^t\mid\binom{qn}{n}\). Legendre's formula gives, with \(s_q(qm)=s_q(m)\),
\[
\nu_q\left(\binom{qn}{n}\right)
=\frac{s_q((q-1)n)+s_q(n)-s_q(qn)}{q-1}
=\frac{s_q((q-1)p^r)}{q-1}.
\]
Hence the second condition is exactly \(s_q((q-1)p^r)\ge(q-1)t\). Since \(p\ne q\), the Chinese remainder theorem combines the two tests into the full congruence modulo \(q^tp^r\). This proves necessity and sufficiency with all quantifiers.

**5. Sharp boundary examples.** For \((q,p,t)=(31,5,1)\), direct integer modular calculations give
\[
\binom{31^2}{31}\equiv\binom{31^2\cdot5}{31\cdot5}\equiv251\pmod{625}.
\]
As the next binomial increments are divisible by \(5^6\), \(\beta_{5,31,1}\equiv251\pmod{625}\). Because \(31\equiv1\pmod5\), its Teichmüller lift equals \(1\), so \(H_{5,31,1}=3\). The digit condition at \(t=1\) is automatic. Yet \(31^4\equiv21\pmod{25}\), not \(1\), so this cubic mixed-support tower is not a consequence of base-31 Wieferichness at \(5\).

For \((q,p,t)=(19,7,2)\), the residues \(\binom{19^3}{19^2}\equiv215\pmod{343}\) and \(\omega_7(19)^{19^2}\equiv19\pmod{343}\), together with equality modulo \(49\), give \(H_{7,19,2}=2\). However \(s_{19}(18\cdot7)=s_{19}(18\cdot7^2)=18<36\), so both p-adically permitted layers are excluded by the separate \(19^2\)-test. The p-adic precision at layer three also shows that no higher layer survives. These calculations are replayed independently in the verifier.

## Verification
The standalone `verify.py` uses only Python's standard library. It checks the complete congruence directly against the two independent conditions on an 82-instance small-parameter grid; tests nine boundary instances including the cube-and-fourth-power split for \(q=31,p=5\); and checks the necessary exact modular certificates, non-Wieferich residues, and digit obstructions. Its recorded expected result is `VERIFY_OK grid_direct_cases=82 digit_filtered=1 boundary_cases=9 non_wieferich_cubic=PASS`. None of these finite checks is used to infer the infinite theorem; the proof uses the cited Jacobsthal congruence and elementary valuation identities.

## Relationship to prior work
Guedes and Machado (2026) prove the exact \(n=q^tp\) criterion (the present \(r=1\) layer) and the separate \(n=p^2\) Wieferich criterion. A published result, *Prime-power towers for the prime-base binomial congruence* (published-finding corpus public archive, 2026), covers only \(n=p^r\), not \(n=q^tp^r\) for positive \(t\). Neither statement entails the mixed two-prime-support classification without additional p-adic lifting and accounting for the nonconstant digit filter. Meštrović (2013) establishes the underlying general prime-power binomial dilation congruences, which are explicitly treated as **known tools** here. The new claim is the exact interaction of that infinite tower with the base-\(q\) digital obstruction, including the non-Wieferich cubic example and the possibility that the digital condition deletes all p-adically allowed layers.

## Limitations
No finiteness theorem, closed formula, or upper bound for the general \(H_{p,q,t}\) is established. For \(t\ge2\), the digit-sum filter may fluctuate with \(r\); no monotonicity is asserted for the final solution set after filtering. The excluded small primes \(p=2,3\) need different Jacobsthal bounds. Mathematical originality was compared against highly relevant accessible primary literature and published related results, but unindexed equivalent statements remain a risk. Independent review has not occurred.

## References
1. G. A. Guedes and R. N. Machado Jr., *Structured Solutions of Prime-Base Binomial Congruences*, arXiv:2606.30232v1, first public June 29, 2026; especially Theorem 3.1 and §6. https://arxiv.org/pdf/2606.30232
2. R. Meštrović, *Variations of Lucas' Theorem Modulo Prime Powers*, arXiv:1301.0252v1 (2012/2013), especially Lemma (3) and Jacobsthal's congruence (7). https://arxiv.org/pdf/1301.0252
3. A. Granville, *Arithmetic Properties of Binomial Coefficients I: Binomial Coefficients modulo prime powers* (1997), §11. https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node12.html
4. *Prime-power towers for the prime-base binomial congruence* (2026), published published-finding corpus entry with opaque identifier a71ec1d0fa28, publicly discoverable by title at https://github.com/published-finding corpus/2026.
