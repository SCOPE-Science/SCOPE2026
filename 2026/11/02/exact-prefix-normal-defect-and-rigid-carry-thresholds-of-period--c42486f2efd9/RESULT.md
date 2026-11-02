# Exact prefix-normal defect and rigid carry thresholds of period-doubling prefixes

## Finding

Let \(p=p_0p_1p_2\cdots\) be the binary period-doubling fixed point of the morphism \(\mu(0)=01\), \(\mu(1)=00\), beginning in \(0\). For every integer \(N\ge1\), let \(P_N=p_0\cdots p_{N-1}\), and define its **prefix-normal defect** by
\[
\Delta(N)=\max_{1\le \ell\le N}\left(\max_{0\le a\le N-\ell}\sum_{j=a}^{a+\ell-1}p_j-\sum_{j=0}^{\ell-1}p_j\right).
\]
Thus \(\Delta(N)\) is the largest excess in the number of \(1\)'s that a factor of \(P_N\) can have over the prefix of equal length. The maximum is nonnegative because a prefix itself is an eligible factor.

**Theorem.** For every \(N\ge1\),
\[
\boxed{\Delta(N)=\max\left\{t\in\mathbb Z_{\ge0}:\frac{2(4^t-1)}{3}\le N\right\}=\left\lfloor\log_4\left(\frac{3N}{2}+1\right)\right\rfloor.}
\]
For every \(t\ge1\), the first prefix length with \(\Delta(N)\ge t\) is
\[
\boxed{N_t=\frac{2(4^t-1)}3.}
\]
At this first length the unique factor attaining excess \(t\) has starting index and length both equal to \((4^t-1)/3\). In particular, for complete substitution iterates of length \(2^k\),
\[
\Delta(1)=0,\qquad\Delta(2)=1,\qquad\Delta(2^k)=\lfloor k/2\rfloor\quad(k\ge2).
\]
The first positive threshold lengths are \(2,10,42,170,682,2730\).

## Assumptions and scope

All indices are zero-based except positive integers in floor sums. A factor of length \(\ell\) starting at \(a\) is \(p_a\cdots p_{a+\ell-1}\); it is admissible precisely when \(a\ge0\), \(\ell\ge1\), and \(a+\ell\le N\). Binary valuations \(\nu_2(m)\) are defined for positive integers \(m\). The result is for every **initial prefix** of one specified infinite word, not an arbitrary substring or a circular factor.

## Proof

**1. A valuation formula for the word.** The substitution gives \(p_{2m}=0\) and \(p_{2m+1}=1-p_m\) for every \(m\ge0\). It follows inductively that
\[
p_j=1\quad\Longleftrightarrow\quad \nu_2(j+1)\text{ is odd}.
\]
Consequently the number of ones in the first \(n\) symbols is
\[
H(n):=\sum_{j=0}^{n-1}p_j
=\sum_{r\ge1}(-1)^{r-1}\left\lfloor\frac n{2^r}\right\rfloor.
\]
The finite alternating sum counts positive integers with an odd \(2\)-adic valuation: the contribution from a number of valuation \(v\) is \(1-1+\cdots+(-1)^{v-1}\), equal to \(1\) for odd \(v\) and \(0\) for even \(v\).

**2. Carry bound.** Fix \(a\ge0\), \(\ell\ge1\), and write \(x=a+\ell\). For \(r\ge1\), set
\[
\gamma_r=\left\lfloor\frac{x}{2^r}\right\rfloor-\left\lfloor\frac a{2^r}\right\rfloor-\left\lfloor\frac\ell{2^r}\right\rfloor\in\{0,1\}.
\]
This is exactly the carry from the lowest \(r\) binary digits in the addition \(a+\ell=x\). The excess of this factor over the initial \(\ell\)-symbol prefix equals
\[
H(x)-H(a)-H(\ell)=\sum_{i\ge1}(\gamma_{2i-1}-\gamma_{2i}).
\]
Let \(x_j\in\{0,1\}\) be the digit of \(x\) in binary position \(j\), starting with position zero. For every \(i\ge1\),
\[
\gamma_{2i-1}-\gamma_{2i}\le x_{2i-1}.
\]
Indeed the left side can be positive only when the carry entering digit \(2i-1\) is \(1\) and the outgoing carry is \(0\). At that digit the two summands must both have digit \(0\), forcing the sum's digit \(x_{2i-1}=1\). In all other cases the left side is nonpositive, so the inequality is automatic. Therefore
\[
H(x)-H(a)-H(\ell)\le Q(x):=\sum_{i\ge1}x_{2i-1}.
\]

**3. Exact thresholds.** If \(Q(x)\ge t\), then \(x\) has at least \(t\) set bits in odd-indexed positions. The least such nonnegative integer is
\[
N_t=2+2^3+\cdots+2^{2t-1}=\frac{2(4^t-1)}3.
\]
Thus no factor contained in a prefix of length less than \(N_t\) can have excess \(t\) or more. Conversely put \(m_t=(4^t-1)/3=1+4+\cdots+4^{t-1}\), and choose \(a=\ell=m_t\). Binary addition of these identical summands has carry \(\gamma_{2i-1}=1\), \(\gamma_{2i}=0\) for \(1\le i\le t\), and no other carries. The excess is exactly \(t\), and the factor fits in the prefix of length \(2m_t=N_t\). This proves the stated all-prefix formula and first-attainment lengths.

**4. Uniqueness at the threshold.** Suppose \(a+\ell\le N_t\) and the excess is \(t\). Step 2 forces \(Q(a+\ell)\ge t\), and the minimality argument of Step 3 forces \(a+\ell=N_t\), whose only set bits lie in the \(t\) lowest odd-indexed positions. Equality in the carry bound forces \(\gamma_{2i-1}=1\) and \(\gamma_{2i}=0\) for every \(1\le i\le t\), with higher carries zero. At each even-indexed digit \(2i-2\), a carry \(0\to1\) requires both summands to have digit \(1\); at the next, odd-indexed digit, a carry \(1\to0\) requires both digits to be \(0\). Hence \(a=\ell=m_t\). This proves uniqueness.

**5. Dyadic specialization.** For \(k\ge2\), the inequalities \(N_{\lfloor k/2\rfloor}\le2^k<N_{\lfloor k/2\rfloor+1}\) follow directly from the closed form for \(N_t\); direct inspection handles the two smallest lengths. The dyadic formula follows.

## Verification

Running `python3 checker.py` with a standard Python 3 interpreter checks two independent constructions of the first \(4096\) symbols (iterated substitution and valuation parity), checks the alternating floor count against the direct prefix counts at every position, and exhaustively examines all factors of every prefix of length at most \(4096\). It also checks the carry upper bound, all six sharp first-attainment thresholds through length \(2730\), and their proposed witnesses. The checker completed without error. These computations are finite corroboration; the unrestricted statements are established by the proof above.

## Relationship to prior work

Fici and Lipták introduced prefix-normal words and factor-maximal-count functions, motivating jumbled indexing and the relevant invariant. Their general theory does not specify the period-doubling word's all-prefix maximal excess or the exact first-attainment thresholds. Parreau, Rigo, Rowland, and Vandomme studied \(2\)-regularity of Abelian and \(2\)-Abelian complexity in automatic sequences, including the period-doubling word; those results concern equivalence classes of factors in the infinite language and do not provide these finite-prefix extremal locations. Cicalese, Lipták, and Rossi developed prefix-normal forms and their connections with Abelian complexity for infinite words, discussing paperfolding and Thue–Morse, but no exact period-doubling defect threshold is stated in the inspected sections. The method here is a direct alternating-carry argument with a sharp two-summand witness.

## Limitations

The theorem determines the **maximum** excess across all factor lengths and locations within each initial prefix; it does not give the entire prefix-normal form or the maximizer set for every individual length. No assertion concerns general binary morphisms. Computer enumeration is not used as a proof for unbounded prefix lengths. Literature searches and the inspected sources do not establish exhaustive historical priority; unpublished or unindexed equivalent arguments remain a possibility.

## References

1. G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory, 2011, pp. 228–238. DOI: https://doi.org/10.1007/978-3-642-22321-1_20 (accessible author version: https://arxiv.org/abs/1805.12405).
2. A. Parreau, M. Rigo, E. Rowland, and E. Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences*, 2014 preprint, https://arxiv.org/abs/1405.3532.
3. F. Cicalese, Z. Lipták, and M. Rossi, *On Infinite Prefix Normal Words*, 2018 preprint, https://arxiv.org/abs/1811.06273.
