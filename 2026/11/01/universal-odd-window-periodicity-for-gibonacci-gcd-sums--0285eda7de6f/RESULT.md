# Universal odd-window periodicity for Gibonacci gcd sums

## Finding
For arbitrary integer initial values \(a,b\), let \(G_0=a\), \(G_1=b\), and \(G_{n+2}=G_{n+1}+G_n\). For each integer \(k\ge1\), define the nonnegative greatest common divisors
\[
A(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}G_{n+j}\right),\qquad
B(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}G_{n+j}^{2}\right).
\]
If \((a,b)\ne(0,0)\), put \(d=\gcd(|a|,|b|)\), \(u=a/d\), \(v=b/d\), and \(\mu=v^2-uv-u^2\). Define \(M=2|\mu|\) and \(\pi\) as the least positive period of the pair \((g_n,g_{n+1})\) modulo \(M\), where \(g_0=u\), \(g_1=v\), and \(g_{n+2}=g_{n+1}+g_n\).

**Theorem.** For every odd \(k\ge1\), one has \(\mu\ne0\), and
\[
\begin{aligned}
A(k)&=d\gcd\bigl(M,\,g_{k+1}-g_1,\,g_{k+2}-g_2\bigr),\\
B(k)&=d^2\gcd\bigl(M,\,g_k g_{k+1}-g_0g_1,\,g_{k+1}^2-g_1^2,\,g_{k+2}^2-g_2^2\bigr).
\end{aligned}
\]
In particular, \(A(k)\mid dM\), \(B(k)\mid d^2M\), and **both functions are purely periodic on the odd positive integers**, with the common effective even shift
\[
T=\operatorname{lcm}(2,\pi),\qquad
A(k+T)=A(k),\quad B(k+T)=B(k).
\]
The period bound need not be minimal. For \((a,b)=(0,0)\), both gcd functions are identically zero and hence periodic.

## Assumptions and scope
Integers \(a,b\) may be positive, negative, or zero. The gcd of any family of integers means its unique nonnegative common divisor; an all-zero family has gcd zero. The window length is a positive odd integer and the shift is even, so the shifted window also has odd length. All modular periods refer to the ordered state pair, not merely one coordinate. The companion map \((x,y)\mapsto(y,x+y)\) is invertible over every residue ring because its determinant is \(-1\).

## Proof
**1. Nonzero invariant and finite modular period.** Define \(N(x,y)=y^2-xy-x^2\). Direct substitution yields \(N(y,x+y)=-N(x,y)\), hence
\[
N(g_n,g_{n+1})=(-1)^n\mu.\tag{1}
\]
If \(\mu=0\), the rational ratio \(v/u\) would solve \(z^2-z-1=0\) when \(u\ne0\), contradicting irrationality of its roots; if \(u=0\), then \(v^2=0\), contrary to \(\gcd(u,v)=1\). Thus \(M\ge2\). The invertible recurrence on the finite state set \((\mathbb Z/M\mathbb Z)^2\) has a positive period \(\pi\) from any starting pair, computable by repeated iteration.

**2. First-power windows.** Let \(S_n=\sum_{j=1}^{k}g_{n+j}\). Summing the recurrence shows \(S_n=g_{n+k+2}-g_{n+2}\). As a function of \(n\), it also obeys the order-two Fibonacci recurrence, so its gcd across all \(n\ge0\) is \(\gcd(S_0,S_1)\). By \(S_1-S_0=g_{k+1}-g_1\), this equals
\[
A(k)/d=\gcd(g_{k+1}-g_1,\,g_{k+2}-g_2).\tag{2}
\]
Write the right-hand gcd as \(h\). The two states \((g_{k+1},g_{k+2})\) and \((g_1,g_2)\) coincide modulo \(h\), so their norm values are equal modulo \(h\). For odd \(k\), identity (1) makes these values \(+\mu\) and \(-\mu\), respectively. Thus \(h\mid2\mu\), including the harmless case \(h=1\). Consequently \(h=\gcd(M,g_{k+1}-g_1,g_{k+2}-g_2)\).

**3. Square windows.** Let \(H_n=\sum_{j=1}^{k}g_{n+j}^2\). Every sequence of squared Gibonacci terms satisfies
\[
q_{n+3}=2q_{n+2}+2q_{n+1}-q_n,\tag{3}
\]
which follows by expanding the original second-order recurrence three times (or multiplying its characteristic roots \(\alpha,\beta\) and observing that \(\alpha^2,\beta^2,-1\) are the roots of \(z^3-2z^2-2z+1\)). Therefore the integer gcd of all \(H_n\) equals that of \(H_0,H_1,H_2\). Telescoping \(g_j^2=g_jg_{j+1}-g_{j-1}g_j\) gives \(H_0=g_kg_{k+1}-g_0g_1\). Moreover \(H_1-H_0=g_{k+1}^2-g_1^2\) and \(H_2-H_1=g_{k+2}^2-g_2^2\), hence
\[
B(k)/d^2=\gcd\bigl(g_kg_{k+1}-g_0g_1,\,g_{k+1}^2-g_1^2,\,g_{k+2}^2-g_2^2\bigr).\tag{4}
\]
Put \(X=g_kg_{k+1}-g_0g_1\), \(Y=g_{k+1}^2-g_1^2\), and \(Z=g_{k+2}^2-g_2^2\). Using \(g_{k+2}=g_k+g_{k+1}\), we obtain the exact identity
\[
Z-2Y-X=N(g_0,g_1)-N(g_k,g_{k+1})=(1-(-1)^k)\mu.\tag{5}
\]
For odd \(k\), the right-hand side is \(2\mu\). The gcd in (4) therefore divides \(M\), yielding the displayed bounded formula.

**4. Periodicity.** The defining formulas in steps 2 and 3 depend only on \((g_k,g_{k+1},g_{k+2})\) modulo the fixed modulus \(M\), plus the unshifted initial terms and constants. Every shift by \(\pi\) preserves those residues. Taking \(T=\operatorname{lcm}(2,\pi)\) makes the shift even, so both indices remain in the odd domain. Both gcds are unchanged after shifting by \(T\), as required. For zero initial values all window sums vanish. \(\square\)

## Verification
A standalone Python 3 verifier, `verify.py`, recomputes window sums directly rather than using only the asserted gcd formulas. For each of the \(168\) nonzero initial pairs in \([-6,6]^2\), it checks \(30\) odd lengths, their shifted versions, exact norm identities, and the divisibility bounds. The observed checks were \(5{,}040\) direct window-GCD comparisons, \(5{,}040\) shifted-period comparisons, and \(9{,}240\) norm identities, with all checks passing. For \((a,b)=(-1,3)\), the normalized modulus is \(22\) and the effective shift is \(30\), matching the paper's displayed example. The finite tests are not used to infer the universal quantifiers; those follow from steps 1–4.

To reproduce: run `python3 verify.py` from a directory containing the standalone script. No third-party dependencies are required.

## Relationship to prior work
Guyer and Mbirika (2021, arXiv:2104.12262) establish the first-power gcd formula (2) and an interpretation via generalized Pisano periods. Mbirika and Spilker (2022, arXiv:2204.12626, Theorem 3.4) establish the square-gcd formula (4); their odd-\(k\) results already contain the bound for the square-gcd, and Section 6.2 explicitly asks in Question 6.4 which initial values lead to periodicity. The formulas (2) and (4), their existing special cases, and the square divisibility bound are **not** claimed as new. The theorem here supplies the remaining norm-bound observation for the first-power gcd, the joint finite-modulus reduction, and an explicit uniform constructive answer: every integer initial pair is admissible. The proof reconstructs these steps to avoid relying on opaque computations.

## Limitations
The effective shift \(T\) is only a common period and is not claimed to be minimal. The result concerns first powers and squares, and only odd window lengths; no statement is made about higher powers or the generally unbounded even-window regime. Full novelty beyond the inspected literature cannot be guaranteed: in particular, the conclusion is a short additional deduction from strong published gcd identities, and an implicit or later published resolution may exist.

## References
- D. Guyer and aBa Mbirika, *GCD of sums of \(k\) consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, Journal of Integer Sequences 24 (2021), Article 21.9.8, arXiv:2104.12262 (first version 2021-04-25), https://arxiv.org/abs/2104.12262 .
- aBa Mbirika and J. Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269, arXiv:2204.12626 (first version 2022-04-26), https://arxiv.org/html/2204.12626v2 .
