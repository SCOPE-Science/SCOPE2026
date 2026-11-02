# Exact local defects and prime-support thresholds for non-Wieferich integers

## Finding
Let \(n>1\) be odd and let \(\ell(n)=\operatorname{ord}_n(2)\). For each odd prime \(p\mid n\), put
\[
t_p=\operatorname{ord}_p(2),\qquad h_p=\nu_p(2^{t_p}-1),
\qquad H_p(P)=\max\bigl(\{0\}\cup\{\nu_p(t_q):q\in P,\ q\ne p\}\bigr),
\]
where \(P=\{p:p\mid n\}\) is the set of distinct prime divisors. Write \(n=\prod_{p\in P}p^{e_p}\), with each \(e_p\ge1\). The exact local valuations are
\[
\boxed{\nu_p(2^{\ell(n)}-1)=\max\{e_p,h_p+H_p(P)\}},
\qquad
\boxed{\nu_p\!\left(\frac{2^{\ell(n)}-1}{n}\right)=\max\{0,h_p+H_p(P)-e_p\}}.
\]
Thus the *complete* gcd obstruction is
\[
\boxed{\gcd\!\left(n,\frac{2^{\ell(n)}-1}{n}\right)
=\prod_{p\in P}p^{\min\{e_p,\max(0,h_p+H_p(P)-e_p)\}}}.
\]
Call \(n\) **non-Wieferich** when this gcd is \(1\), following the order-based definition. For every finite nonempty set \(P\) of odd primes, define
\[
W(P)=\prod_{p\in P}p^{h_p+H_p(P)}.
\]
**Exact prime-support classification:** every odd integer \(n>1\) with prime support exactly \(P\) is non-Wieferich if and only if \(W(P)\mid n\). In particular, \(W(P)\) is the unique smallest non-Wieferich integer with that prime support, and every larger exponent vector above its thresholds is non-Wieferich. The support-local criterion requires no unproved hypothesis about the existence of Wieferich primes.

As a counting consequence, for \(r=|P|\) and \(X\ge W(P)\), the number \(N_P(X)\) of non-Wieferich integers at most \(X\) with exact prime support \(P\) satisfies
\[
N_P(X)=\frac{(\log(X/W(P)))^r}{r!\prod_{p\in P}\log p}
+O_P\bigl((1+\log(X/W(P)))^{r-1}\bigr).
\]
This is a support-restricted logarithmic count, not a global density asymptotic.

## Assumptions and scope
All primes in \(P\) are odd, \(P\) is finite and nonempty, and each exponent \(e_p\) is a positive integer. The valuation \(\nu_p(m)\) is the exponent of \(p\) in a nonzero integer \(m\). The multiplicative order \(\operatorname{ord}_m(2)\) exists for each odd \(m\). When the set in a maximum is empty, the additional \(0\) makes its maximum \(0\). The gcd quotient is an integer because \(n\mid2^{\ell(n)}-1\). No assertion is made for even integers or for \(n=1\), which has empty prime support.

## Proof
For any odd prime \(q\), write \(t_q=\operatorname{ord}_q(2)\) and \(h_q=\nu_q(2^{t_q}-1)\). Since \(q\nmid t_q\) (indeed \(t_q\mid q-1\)), lifting the exponent shows, for each positive integer \(a\),
\[
\nu_q(2^{t_qa}-1)=h_q+\nu_q(a).
\]
Every exponent giving \(2^k\equiv1\pmod{q^e}\) is divisible by \(t_q\). Therefore the least such exponent is precisely
\[
\operatorname{ord}_{q^e}(2)=t_q q^{\max(0,e-h_q)}.
\]
Here the formula also covers \(e\le h_q\): in that case \(2^{t_q}\equiv1\pmod{q^e}\) already, and any exponent must be divisible by \(t_q\).

The Chinese remainder theorem gives
\[
\ell(n)=\operatorname{lcm}_{q\in P}\bigl(t_q q^{\max(0,e_q-h_q)}\bigr).
\]
Fix \(p\in P\). The only prime-power factor in this least common multiple with base \(p\) comes from the \(q=p\) term; the other terms may supply powers of \(p\) through their orders \(t_q\). Since \(p\nmid t_p\), it follows exactly that
\[
\nu_p(\ell(n))=\max\bigl(0,e_p-h_p,H_p(P)\bigr).
\]
Now \(t_p\mid\ell(n)\) and \(p\nmid t_p\). Another application of the same lifting identity yields
\[
\begin{aligned}
\nu_p(2^{\ell(n)}-1)
 &=h_p+\nu_p(\ell(n)/t_p)\\
 &=h_p+\max(0,e_p-h_p,H_p(P))\\
 &=\max(e_p,h_p+H_p(P)).
\end{aligned}
\]
Subtracting \(e_p=\nu_p(n)\) proves the displayed quotient valuation and then the gcd product formula. The quotient is coprime to \(n\) precisely when all these quotient valuations vanish; equivalently \(e_p\ge h_p+H_p(P)\) for every \(p\in P\). This is equivalent to \(W(P)\mid n\), with exact prime support understood, proving the classification and minimality.

For the counting consequence, each admissible integer has the unique representation
\[
n=W(P)\prod_{p\in P}p^{a_p},\qquad a_p\in\mathbb Z_{\ge0}.
\]
The bound \(n\le X\) becomes \(\sum_{p\in P}a_p\log p\le Y:=\log(X/W(P))\). The nonnegative orthant simplex of real variables with this inequality has volume \(Y^r/(r!\prod_{p\in P}\log p)\). Unit-cube comparison places the integer lattice count between the volumes with thresholds \(Y\) and \(Y+\sum_{p\in P}\log p\), up to the boundary convention. Their difference is \(O_P((1+Y)^{r-1})\), establishing the stated error term for all \(Y\ge0\).

Examples: for \(P=\{3,7\}\), \(t_3=2\), \(t_7=3\), \(h_3=h_7=1\), and the cross-order valuations give \(H_3=1,H_7=0\). Hence \(W(P)=3^2\cdot7=63\): \(21\) is Wieferich but \(63\) is non-Wieferich because \(\ell(63)=6\) and \((2^6-1)/63=1\). A distinct phenomenon occurs for the Wieferich prime \(1093\), where \(h_{1093}=2\); the least non-Wieferich integer supported only at that prime is \(1093^2\).

## Verification
Run `python3 verify.py` with Python 3 and its standard library. It computes multiplicative orders via independent Euler-totient reduction, evaluates the original gcd directly through modular exponentiation modulo \(n^2\), and separately computes the predicted prime-support valuation product. It checks all \(7500\) odd integers from \(3\) through \(15001\), including \(1538\) cases having nontrivial gcd, and six further prescribed supports (including \(1093\) and \(3511\)). The expected last lines start with `VERIFY_OK odd_n=7500 wieferich_cases=1538 supports=6` and `EXAMPLES`.

These finite checks are diagnostic; the proof of the universal formulas is the lifting-the-exponent argument above, not the enumeration.

## Relationship to prior work
Casia Siegel, *An Asymptotic for Non-Wieferich Numbers* (arXiv:2610.28685v1, first posted 2026-10-19), gives the order-based definition and a conditional global counting asymptotic. Its Lemma 2.1 provides a **sufficient** condition for a squarefree integer to be non-Wieferich; Lemma 2.2 gives one necessary condition; and Lemmas 2.4–2.5 use selected one-way local obstructions. None states the exact quotient valuations or the minimal non-Wieferich representative \(W(P)\) for every fixed support and all exponent vectors. The older order characterization in OEIS A182297 is a computational equivalence of the original definition, not an explicit description of the exponent-space threshold regions. These are precise statement comparisons, not a claim of absolute priority.

The original order-Wieferich work of Franco and Pomerance (1995), cited by Siegel, remains a priority risk: only bibliographic data, abstracts, and the specific lemma reproduced in Siegel were available, not its full text. Therefore independent priority verification is warranted.

## Limitations
The exact theorem is restricted to odd moduli and base \(2\); no claim is made that the prime-support condition is computationally cheaper than factorization and multiplicative-order determination, nor that the global counting function has any new asymptotic. Its proof uses standard multiplicative-order and lifting identities, while the stated outcome is their combined exact structural consequence. The derivation does not classify which primes have larger Wieferich height or determine orders across different primes without computing them. Priority risk from inaccessible older full text and unindexed equivalent work remains.

## References
1. Casia Siegel, *An Asymptotic for Non-Wieferich Numbers*, arXiv:2610.28685v1 (submitted 2026-10-19), https://arxiv.org/abs/2610.28685 .
2. Zachary Franco and Carl Pomerance, *On a conjecture of Crandall concerning the \(qx+1\) problem*, Mathematics of Computation **64** (1995), 1333–1336, https://doi.org/10.1090/S0025-5718-1995-1297468-4 .
3. OEIS A182297, *Wieferich numbers (2)*, https://oeis.org/A182297 .
