# Unbounded 2-rank inside Kishi's Fibonacci class-number-five family

## Result

Let \(F_n\) denote the Fibonacci sequence. For every integer \(R\ge 1\), there is an odd positive integer \(U_R\) such that, for every odd prime \(Q\) outside a finite set, the imaginary quadratic field
\[
K_{R,Q}=\mathbf Q\!\left(\sqrt{-F_{25U_RQ}}\right)
\]
belongs to Kishi's family
\[
\mathbf Q\!\left(\sqrt{-F_{50s+25}}\right),\qquad s=\frac{U_RQ-1}{2},
\]
and satisfies
\[
\operatorname{rk}_2\operatorname{Cl}(K_{R,Q})\ge R.
\]
Consequently
\[
5\cdot 2^R\mid h(K_{R,Q}).
\]
Moreover, as \(Q\) varies, these fields contain infinitely many pairwise distinct imaginary quadratic fields.

Thus the 2-rank is unbounded within the same Fibonacci-parametrized family in which Kishi proved universal divisibility of the class number by 5. A recent refinement by Chakraborty--Rao--Dabhole obtains one additional factor of 2 on an explicit subfamily; the theorem above supplies arbitrarily many independent genus-theoretic 2-torsion directions on infinite subfamilies.

## Construction

Choose distinct odd primes \(r_1,\dots,r_R\), none equal to 5, and put
\[
m_i=25r_i.
\]
Since \(m_i>12\), Carmichael's primitive-divisor theorem for Fibonacci numbers gives a primitive prime divisor \(q_i\) of \(F_{m_i}\). Hence
\[
z(q_i)=m_i,
\]
where \(z(q)\) is the rank of apparition. The \(q_i\) are pairwise distinct: if \(m_i<m_j\), a prime dividing \(F_{m_i}\) cannot be primitive for \(F_{m_j}\). Also \(q_i\notin\{2,5\}\), since 2 and 5 already divide earlier Fibonacci numbers.

Write
\[
e_i=v_{q_i}(F_{m_i}),\qquad U_0=5\prod_{i=1}^R r_i.
\]
For each \(i\), choose \(\delta_i\in\{0,1\}\) so that
\[
e_i+v_{q_i}(U_0)+\delta_i\equiv1\pmod2,
\]
and define
\[
U_R=U_0\prod_{i=1}^R q_i^{\delta_i}.
\]
This is odd and has \(v_5(U_R)=1\).

Now let \(Q\) be any odd prime avoiding the finite set of prime divisors of
\[
5U_Rq_1\cdots q_R,
\]
and set \(n=25U_RQ\). Since every \(m_i\mid n\), Lengyel's valuation formula gives
\[
v_{q_i}(F_n)=v_{q_i}(n)+v_{q_i}(F_{z(q_i)})
=e_i+v_{q_i}(U_0)+\delta_i,
\]
which is odd by construction. Also
\[
v_5(F_n)=v_5(n)=3.
\]
Therefore the squarefree part \(D_n=\operatorname{sf}(F_n)\) is divisible by the \(R+1\) distinct odd primes
\[
5,q_1,\dots,q_R.
\]

Let \(\Delta_n\) be the fundamental discriminant of \(\mathbf Q(\sqrt{-D_n})\). Every odd prime dividing \(D_n\) divides \(\Delta_n\), so \(\Delta_n\) has at least \(R+1\) distinct prime divisors. Gauss genus theory therefore yields
\[
\operatorname{rk}_2\operatorname{Cl}(\mathbf Q(\sqrt{-D_n}))\ge R.
\]
Because \(\mathbf Q(\sqrt{-F_n})=\mathbf Q(\sqrt{-D_n})\), this proves the asserted 2-rank bound. Kishi's theorem gives \(5\mid h(\mathbf Q(\sqrt{-F_{50s+25}}))\) for every \(s\ge0\); hence coprimality of 5 and \(2^R\) gives \(5\cdot2^R\mid h(K_{R,Q})\).

## Infinitely many distinct fields in each fixed-rank subfamily

It remains to rule out the possibility that varying \(Q\) merely repeats finitely many quadratic fields. The following argument extends the fixed-base quartic argument used for the infinitude theorem in Chakraborty--Rao--Dabhole.

Fix the odd integer \(U=U_R\), put \(m=25U\), and consider
\[
\mathcal K_U=\left\{\mathbf Q(\sqrt{-F_{mQ}}): Q\text{ an odd prime},\ Q\nmid m\right\}.
\]
Assume that \(\mathcal K_U\) is finite. Then only finitely many rational primes occur in the squarefree parts \(\operatorname{sf}(F_{mQ})\). For each prime \(p\) in this finite support choose one admissible prime \(Q_p\) for which
\(p\mid\operatorname{sf}(F_{mQ_p})\). Choose a further admissible prime \(Q\) distinct from all \(Q_p\) and also avoiding the prime divisors of \(F_m\).

If \(p\mid\operatorname{sf}(F_{mQ})\), then for its representative \(Q_p\),
\[
p\mid \gcd(F_{mQ},F_{mQ_p})
=F_{\gcd(mQ,mQ_p)}
=F_m.
\]
Thus every prime in \(\operatorname{sf}(F_{mQ})\) divides \(F_m\). Conversely, for every prime \(p\mid F_m\), the parity of \(v_p(F_{mQ})\) is the same as that of \(v_p(F_m)\) once \(Q\ne p\): for \(p\ne2,5\) this follows directly from Lengyel's valuation formula; for \(p=5\) it follows from \(v_5(F_t)=v_5(t)\); and for \(p=2\) it follows from the standard explicit formula for \(v_2(F_t)\), noting that \(mQ\) is odd. Hence for all such \(Q\),
\[
\operatorname{sf}(F_{mQ})=D:=\operatorname{sf}(F_m).
\]
Therefore
\[
F_{mQ}=D A_Q^2
\]
for some integer \(A_Q\). Since \(mQ\) is odd, the Fibonacci--Lucas identity
\[
L_N^2-5F_N^2=4(-1)^N
\]
gives
\[
L_{mQ}^2=5D^2A_Q^4-4.
\]
Thus \((A_Q,L_{mQ})\) is an integral point on the fixed nonsingular genus-one quartic
\[
Y^2=5D^2X^4-4.
\]
As \(Q\) ranges over infinitely many primes, the Lucas values \(L_{mQ}\) are distinct and unbounded, producing infinitely many integral points. This contradicts Siegel's theorem. Hence \(\mathcal K_U\), and therefore the rank-\(R\) subfamily above, contains infinitely many distinct fields.

## Example

For \(R=2\), one may take \(r_1=3\) and \(r_2=7\). Primitive divisors can be chosen as
\[
q_1=230686501\mid F_{75},\qquad q_2=701\mid F_{175},
\]
with both occurring to exponent one. Here no parity correction is needed, so \(U_2=5\cdot3\cdot7=105\). Consequently, for every odd prime \(Q\) outside the finite exceptional set,
\[
\mathbf Q\!\left(\sqrt{-F_{2625Q}}\right)
\]
has 2-rank at least 2 and class number divisible by 20; infinitely many of these fields are pairwise distinct.

## Relation to recent work

Chakraborty--Rao--Dabhole recall Kishi's theorem that the class number of \(\mathbf Q(\sqrt{-F_{50s+25}})\) is always divisible by 5. Their Theorem 1 forces the two primes 5 and 3001 to survive in the squarefree part under explicit valuation-parity hypotheses, and genus theory then yields divisibility by 10. Their Proposition 2.2 records the Fibonacci valuation formulas used here, and their Theorem 4 proves infinitude of a different restricted subfamily through a fixed quartic and Siegel's theorem.

The present result combines those ingredients with Carmichael primitive divisors and independent parity steering of their valuations. The new point is that the number of surviving squarefree prime factors can be made arbitrarily large while retaining an infinite family of distinct Kishi fields.

## Limitations

The theorem gives unbounded 2-rank and divisibility by \(5\cdot2^R\), but it does not determine the full 2-primary class group, exhibit elements of exact order \(2^R\), or give a density for the constructed subfamilies. The integer \(U_R\) is effective once primitive divisors are chosen, but no attempt is made to minimize it.

Originality is asserted only to the best of our knowledge. The 2008 Kishi article is the most relevant source whose full text was not inspected here; its abstract and its main results as restated and used in the 2026 paper were inspected. Because it treats exactly the same Fibonacci family, an unadvertised stronger 2-rank statement there is the principal residual originality risk. Searches for unbounded 2-rank, arbitrary powers of 2 in the class numbers of this Fibonacci family, and equivalent squarefree-kernel/genus-theory formulations did not reveal prior coverage.

## References

1. Y. Kishi, *A new family of imaginary quadratic fields whose class number is divisible by five*, J. Number Theory **128** (2008), 2450--2458. https://doi.org/10.1016/j.jnt.2008.02.016
2. P. Rao, K. Chakraborty, A. Dabhole, *An infinite family of imaginary biquadratic fields with a large class number*, arXiv:2609.16678v1 (2026). https://arxiv.org/abs/2609.16678
3. T. Lengyel, *The Order of the Fibonacci and Lucas Numbers*, Fibonacci Quarterly **33** (1995), 234--239. https://doi.org/10.1080/00150517.1995.12429139
4. M. Yabuta, *A simple proof of Carmichael's theorem on primitive divisors*, Fibonacci Quarterly **39** (2001), 439--443. https://www.fq.math.ca/Scanned/39-5/yabuta.pdf
5. D. A. Cox, *Primes of the Form \(x^2+ny^2\)*, 2nd ed., Wiley, 2013 (genus theory for quadratic forms/class groups).
