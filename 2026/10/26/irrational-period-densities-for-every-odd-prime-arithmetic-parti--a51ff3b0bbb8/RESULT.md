# Irrational period densities for every odd-prime arithmetic partial derivative

## Finding

For every odd prime \(p\) and every \(t\in\{1,\ldots,p\}\), the set of exponents \(m\ge p\) for which the \(p\)-adic valuations of the successive arithmetic partial derivatives of \(p^m\) have eventual least period \(t\) has an **irrational natural density** \(\alpha_{p,t}\). More precisely,
\[
\#\{p\le m\le X:\operatorname{per}_p(m)=t\}
 =\alpha_{p,t}X+O_p(\log(X+2)).
\]
The \(p\) densities are strictly between zero and one and sum to one.

Here is a convergent and exact specification. Define \(H_p:\mathbb Z_{\ge1}\longrightarrow\{1,\ldots,p\}\) recursively by
\[
H_p(r)=\begin{cases}
r,&1\le r\le p,\\
H_p\!\left(1+\nu_p\!\left(\left\lfloor\frac{r-1}{p}\right\rfloor\right)\right),&r>p.
\end{cases}
\]
Then
\[
\boxed{\alpha_{p,t}=(p-1)\sum_{r\ge1}\frac{\mathbf1_{\{H_p(r)=t\}}}{p^r}.}
\]
Every density in this formula is irrational, including the fixed-point density \(t=1\). The special case \(p=3\) gives approximately \((0.703654777631,0.222271148295,0.0740740740742)\). The final digits are descriptive, not exact decimal identities.

## Assumptions and scope

Throughout \(p\ge3\) is a fixed **odd prime**, \(m\) ranges through positive integers at least \(p\), and \(\nu_p(n)\) denotes the exponent of \(p\) in a positive integer \(n\). For integer \(N\ne0\), the arithmetic partial derivative is \(D_p(N)=N\nu_p(N)/p\). The starting integer is \(N=p^m\); the observable is the integer sequence \(\nu_p(D_p^j(N))\), indexed by \(j\ge0\). Eventual least period means the smallest positive period of its eventual infinite periodic tail. The result counts **initial exponents** \(m\), not all integer starting values \(N\), and does not claim that the integers \(D_p^j(N)\) themselves are periodic.

The recursion for \(H_p\) terminates: for \(r>p\), its new argument \(1+\nu_p(\lfloor(r-1)/p\rfloor)\) is a positive integer strictly smaller than \(r\).

## Proof

**1. Reduction to an integer valuation map.** If \(\nu_p(N)=v\ge1\), then
\[
\nu_p(D_p(N))=v-1+\nu_p(v).
\]
Consequently the valuations are governed exactly by \(f_p(v)=v-1+\nu_p(v)\). If \(v\ge p\) is not divisible by \(p\), iterations subtract one until they first reach \(p\lfloor v/p\rfloor\). The valuation never falls below \(p\) afterward: at multiples of \(p\), \(f_p(v)\ge v\), and between them all steps decrease by one. Thus the iteration is infinite on the positive valuations of interest.

**2. Cycle classification.** Suppose a valuation \(v\) is a positive multiple of \(p\) with \(r=\nu_p(v)\). When \(1\le r\le p\), one step sends \(v\) to \(v+r-1\) and the next \(r-1\) steps subtract one. Every intermediate value is nondivisible by \(p\), so this is a cycle of **least period exactly** \(r\) (with period one when \(r=1\)). If \(r>p\), the first step sends \(v\) to \(v+r-1\), after which subtract-one steps reach the largest positive multiple of \(p\) not exceeding this value, namely \(v+p\lfloor(r-1)/p\rfloor\). Let \(q=\lfloor(r-1)/p\rfloor\). Because \(0<pq<p^r\),
\[
\nu_p(v+pq)=\nu_p(pq)=1+\nu_p(q).
\]
This is exactly the reducing step in \(H_p(r)\). Iterating establishes that the eventual least period from a valuation divisible by \(p\) with exponent \(r\) is \(H_p(r)\).

**3. Exact classification of initial exponents.** For \(m\ge p\), write \(m=pq+j\), where \(q\ge1\) and \(0\le j<p\). The first \(j\) valuation steps subtract one, ending at \(pq\), whose \(p\)-adic valuation is \(1+\nu_p(q)\). Hence
\[
\boxed{\operatorname{per}_p(m)=H_p(1+\nu_p(\lfloor m/p\rfloor)).}
\]
In particular, the complete set of possible periods is \(1,\dots,p\).

**4. Density and error term.** Among positive integers \(q\le Q\), those satisfying \(\nu_p(q)=r-1\) number
\[
\left\lfloor\frac Q{p^{r-1}}\right\rfloor-
\left\lfloor\frac Q{p^r}\right\rfloor
=\frac{(p-1)Q}{p^r}+O(1).
\]
Each full block of \(p\) initial exponents has the same eventual period. Summing the formula over \(1\le r\le1+\lfloor\log_p Q\rfloor\), with at most \(p\) incomplete boundary exponents, proves the displayed density asymptotic, since the omitted tail of the defining series is \(O(p^{-\lfloor\log_p Q\rfloor})\). All constants are uniform in \(t\) for fixed \(p\). Every \(t\) occurs with positive density from its term \(r=t\); their densities sum to \((p-1)\sum_{r\ge1}p^{-r}=1\) and are therefore all less than one.

**5. Irrationality for each period.** Fix \(t\in\{1,\ldots,p\}\), and let \(a_r=\mathbf1_{\{H_p(r)=t\}}\). Since the base-\(p\) digits \((p-1)a_r\) lie in \(\{0,p-1\}\), the displayed convergent sum is the base-\(p\) expansion \(0.((p-1)a_1)((p-1)a_2)\ldots\). It suffices to show that \((a_r)\) is **not eventually periodic**; the sequence is neither eventually all zeros nor all ones by the argument below, so there is no terminating-expansion ambiguity.

For every integer \(m\ge1\), the defining recursion gives
\[
a_{pm+1}=\mathbf1_{\{H_p(1+\nu_p(m))=t\}}
=:c_{\nu_p(m)}.
\]
The sequence \((c_k)_{k\ge0}\) is not eventually constant. Indeed, for any \(s\in\{1,\ldots,p\}\), every integer \(u\ge1\) not divisible by \(p\) gives
\[
H_p(1+p^s u)=s,
\]
so each value \(s\) occurs for arbitrarily large arguments, and thus both \(c_k=1\) and \(c_k=0\) occur for arbitrarily large \(k\).

Suppose for contradiction that \((a_r)\) is eventually periodic with period \(L\ge1\). Then \((a_{pm+1})_{m\ge1}=(c_{\nu_p(m)})_{m\ge1}\) is also eventually periodic with period \(L\): shifting \(m\) by \(L\) shifts the index \(pm+1\) by \(pL\), a multiple of \(L\). Set \(h=\nu_p(L)\). For every sufficiently large \(k>h\), take \(m=p^k\). Since \(\nu_p(p^k+L)=h\), eventual periodicity forces \(c_k=c_h\) for all large \(k\), contradicting the preceding paragraph. Therefore the base-\(p\) expansion is not eventually periodic. The classical rational-base-expansion criterion proves that \(\alpha_{p,t}\) is irrational. \(\square\)

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses integer arithmetic to compare the direct map \(v\mapsto v-1+\nu_p(v)\) with the recursively classified period for every initial exponent \(p\le m<1500\), for the primes \(p=2,3,5,7,11\). It also evaluates exact rational partial sums, checks constructed witnesses for each possible period, and compares finite counts to the stated logarithmic-discrepancy scale. These finite checks are supporting tests, not a replacement for the symbolic proof.

The exact density is computable to an error at most \(p^{-R}\) by summing the first \(R\) terms. The indicated example decimals are bounded by this certified truncation rule; they do not assert a closed elementary expression.

## Relationship to prior work

Emmons and Xiao, *The Arithmetic Partial Derivative* (arXiv:2201.12453v1, January 28, 2022), Theorem 8, provide an **individual-orbit** reduction and prove that eventual valuation periods are at most \(p\). Their paper gives no natural-density formula or irrationality theorem. Their later *A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields* (arXiv:2307.04912v1, July 10, 2023), Theorem 2.8, extends orbit dynamics to local fields but does not address the irrational distribution of eventual periods over positive integer **initial exponents**. The present claim uses the known single-orbit reduction as motivation and supplies a uniform, global counting theorem together with the nonperiodicity obstruction that forces irrationality. A previously available result for the special prime \(p=2\) is not claimed as a new case; the theorem here is expressly restricted to **odd primes**.

## Limitations

The densities concern exponents \(m\), not all positive starting integers or Haar measure over arbitrary local fields. No transcendence, algebraic independence, explicit closed forms, or distributional estimates uniform as \(p\to\infty\) are claimed. An unindexed earlier global frequency theorem cannot be ruled out. The manuscript has not undergone independent mathematical audit.

## References

1. Brad Emmons and Xiao Xiao, *The Arithmetic Partial Derivative*, Journal of Integer Sequences 25 (2022), Article 22.4.7; first preprint arXiv:2201.12453v1 (2022-01-28), https://arxiv.org/abs/2201.12453.
2. Brad Emmons and Xiao Xiao, *A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields*, Notes on Number Theory and Discrete Mathematics 30 (2024), 357–382; first preprint arXiv:2307.04912v1 (2023-07-10), https://arxiv.org/abs/2307.04912.
