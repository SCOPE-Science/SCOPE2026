# Exact composite-conductor index for \(\zeta+c\zeta^{-1}\)
## Finding
Let \(n>1\) be odd and composite, let \(\zeta\) be a primitive \(n\)-th root of unity, let \(K=\mathbb Q(\zeta)\), and let \(c\in\mathbb Z\) with \(c\ne1\). Put \(u_c=\zeta+c\zeta^{-1}\). For each divisor \(m\mid n\), define
\[
R_n(m)=\prod_{p^e\parallel n,\ p^e\mid m}p^{e-1}(p-2)
\prod_{p^e\parallel n,\ p^e\nmid m}p^{e-1}(p-1),
\qquad
E_n(m)=\frac{R_n(m)-\mathbf 1_{m=n}}2.
\]
Then \(\mathbb Q(u_c)=K\) and
\[
[\mathcal O_K:\mathbb Z[u_c]]
=|1-c|^{\varphi(n)/2}
\prod_{m\mid n,\ m>1}|\Phi_m(c)|^{E_n(m)}.
\]
In particular, for odd composite \(n\) and integer \(c\ne1\), \(u_c\) is a power-basis generator of \(\mathcal O_K\) if and only if \(c=0\).

## Assumptions and scope
The conductor \(n\) is odd and composite. The root \(\zeta\) is primitive, \(c\) is an integer, and \(c=1\) is excluded because it gives the maximal real subfield. No statement is made here for even conductors or prime conductors. The symbol \(p^e\parallel n\) means that \(p^e\) is the exact \(p\)-power dividing \(n\), and \(\Phi_m\) is the \(m\)-th cyclotomic polynomial.

## Proof
For a unit \(a\in(\mathbb Z/n\mathbb Z)^\times\), write \(u_a=\zeta^a+c\zeta^{-a}\). For distinct units \(a,b\),
\[
u_a-u_b=(\zeta^a-\zeta^b)(1-c\zeta^{-a-b}).
\]
If two conjugates coincide, then \(c=\zeta^{a+b}\). Since an integer root of unity is \(1\) or \(-1\), oddness of \(n\) rules out \(-1\), while \(c=1\) is excluded. Thus the \(\varphi(n)\) conjugates are distinct and \(\mathbb Q(u_c)=K\).

Because \(\mathcal O_K=\mathbb Z[\zeta]\), the discriminant quotient gives
\[
[\mathcal O_K:\mathbb Z[u_c]]
=\left|\prod_{\{a,b\}\subset(\mathbb Z/n\mathbb Z)^\times,\ a\ne b}
(1-c\zeta^{-a-b})\right|.
\]
It remains to count how often each residue sum occurs. For \(t\in\mathbb Z/n\mathbb Z\), let \(R(t)\) be the number of ordered pairs of units \((a,b)\) satisfying \(a+b=t\). At a prime power \(p^e\parallel n\), the local number of choices is \(p^{e-1}(p-1)\) when \(p\mid t\), and \(p^{e-1}(p-2)\) when \(p\nmid t\). The Chinese remainder theorem therefore shows that if \(m\) is the order of \(\zeta^t\), then \(R(t)=R_n(m)\).

Since \(n\) is odd, the equation \(2a=t\) has one residue solution, and that solution is a unit exactly when \(t\) is a unit, equivalently when \(m=n\). Hence the number of unordered distinct unit pairs with sum \(t\) is
\[
\frac{R(t)-\mathbf 1_{m=n}}2=E_n(m).
\]
Grouping the discriminant product by the order of \(\zeta^t\), the residues of order \(m>1\) run through the primitive \(m\)-th roots. As \(m\) is odd,
\[
\prod_{\operatorname{ord}(\xi)=m}(1-c\xi)=\Phi_m(c),
\]
while \(t=0\) contributes \(1-c\) with exponent \(R_n(1)/2=\varphi(n)/2\). This proves the index formula.

For the power-basis classification, index one first forces \(|1-c|=1\), hence \(c\in\{0,2}\). At \(c=0\), every cyclotomic factor has absolute value one, so the index is one. At \(c=2\), odd compositeness gives
\[
R_n(n)=\prod_{p^e\parallel n}p^{e-1}(p-2)\ge3,
\]
so \(E_n(n)\ge1\). Moreover \(\Phi_n(2)>1\): pairing primitive roots with their conjugates gives factors \(|2-\xi|^2=5-4\cos(\arg\xi)>1\). Thus the index at \(c=2\) is strictly greater than one. Therefore \(c=0\) is the unique power-basis case in the stated domain.

## Verification
A standalone exact-integer replay enumerates every odd composite conductor \(n\le315\). It independently counts unordered pairs of units by their residue sum, checks every count against \(E_n(m)\), verifies the total pair count \(\binom{\varphi(n)}2\), and checks the \(c=0\) and \(c=2\) classification. The replay reports:

`VERIFY_OK odd_composite_conductors=93 n_max=315 residue_pair_checks=15759 classification_c0_c2=OK`

These finite calculations are consistency checks only; the proof above establishes the statement for all odd composite \(n\).

## Relationship to prior work
Karatarakis and Kaur study the same elements \(\zeta+c\zeta^{-1}\) and characterize when they generate a proper subfield; in particular, their Section 2 isolates \(c=1\) as the maximal-real-subfield boundary for odd conductor. Their proper-subfield monogeneity result does not give the exact index of \(\mathbb Z[\zeta+c\zeta^{-1}]\) when the element generates the full cyclotomic field. The formula above addresses that full-field composite-conductor case and shows that composite conductors require divisor-stratified residue-sum multiplicities rather than a single nonzero-residue multiplicity.

Shah and Nakahara study monogeneity of certain index-two imaginary abelian subfields of cyclotomic fields using Gauss-period generators. Their setting is a different proper-subfield problem and does not supply the full-cyclotomic-field index formula above.

## Limitations
The result deliberately excludes prime conductors, even conductors, and \(c=1\). It does not claim that this parametrized family exhausts all power-basis generators of an odd composite cyclotomic field. Targeted literature searches did not locate an earlier statement of this exact divisor-product index formula, but older literature under a transformed-cyclotomic or discriminant formulation remains a residual originality risk.

## References
1. M. Karatarakis and S. Kaur, *Monogenity of the irreducible factors of (k,t)-Fibonacci and (k,t)-Lucas polynomials*, arXiv:2609.38844v1, 2026.
2. S. Shah and T. Nakahara, *Monogenesis of the rings of integers in certain imaginary abelian fields*, Nagoya Mathematical Journal 168 (2002), DOI:10.1017/S0027763000008369.
