# Exact parity-restricted least common multiples of Pascal rows

## Finding
For each integer \(N\ge1\), put
\[
\Lambda_N=\operatorname{lcm}_{0\le k\le N}\binom Nk,\qquad
E_N=\operatorname{lcm}_{\substack{0\le k\le N\\k\equiv0\pmod2}}\binom Nk,\qquad
O_N=\operatorname{lcm}_{\substack{0\le k\le N\\k\equiv1\pmod2}}\binom Nk.
\]
If \(N\) is odd, then \(E_N=O_N=\Lambda_N\). If \(N=2m\) is even, with \(m\ge1\) and \(w=m+1\), then
\[
\frac{\Lambda_{2m}}{E_{2m}}=
2^{1+\nu_2(w)-\mathbf1_{\{w=2^a\text{ for some integer }a\ge1\}}}
\]
and
\[
\frac{\Lambda_{2m}}{O_{2m}}=
\begin{cases}
p,&w=p^a\text{ for an odd prime }p\text{ and integer }a\ge1,\\
1,&\text{otherwise}.
\end{cases}
\]
Thus the full-row LCM loses only a power of two on retaining even-indexed entries, whereas retaining odd-indexed entries loses at most one factor of one odd prime, exactly when the shifted half-row index is an odd prime power.

## Assumptions and scope
All LCMs are of positive integers; \(\binom Nk\) denotes the usual integer binomial coefficient, and \(\nu_p(u)\) is the exponent of the prime \(p\) in positive integer \(u\). Empty index sets do not occur because \(N\ge1\). The indicator \(\mathbf1_{\{\cdots\}}\) is one when its condition holds and zero otherwise. The statements hold for every positive integer \(N\), without size or primality restrictions on \(m\).

## Proof
**1. Universal prime-adic maximum.** Fix \(N\ge1\) and a prime \(p\). Let \(r\) be the unique nonnegative integer with \(p^r\le N+1<p^{r+1}\), and let \(t=\nu_p(N+1)\), so \(0\le t\le r\). When \(r=t\), the lowest \(r\) digits of \(N\) are all \(p-1\); the highest possible digit is at position \(r\), from which no subtraction of an index \(k\le N\) can borrow. Thus every binomial coefficient is prime to \(p\). More generally, the first \(t\) base-\(p\) digits of \(N\) equal \(p-1\), so subtracting any \(k\in[0,N]\) from \(N\) cannot borrow in those positions. At most \(r-t\) borrows are possible, and choosing \(k=p^r-1\) produces exactly that many (or zero if \(r=t\)). By Kummer's theorem,
\[
\nu_p(\Lambda_N)=\max_{0\le k\le N}\nu_p\binom Nk=r-t.\tag{1}
\]
The case \(r=t=0\) is immediate, and the same bound holds when \(N+1\) is exactly a prime power.

**2. Odd row indices.** If \(N\) is odd, the involution \(k\mapsto N-k\) exchanges even and odd indices and preserves \(\binom Nk\). Therefore \(E_N=O_N=\Lambda_N\).

**3. Retaining even indices when \(N=2m\).** For any odd prime \(p\), the index \(k=p^r-1\) from (1) is even; hence \(\nu_p(E_N)=\nu_p(\Lambda_N)\). For the prime two, Legendre's digit-sum formula gives, for \(0\le j\le m\),
\[
\nu_2\binom{2m}{2j}=\nu_2\binom mj,
\]
since binary digit sums are unchanged by doubling. Consequently \(\nu_2(E_{2m})=\lfloor\log_2(m+1)\rfloor-\nu_2(m+1)\) by (1). As \(2m+1\) is odd, (1) also gives \(\nu_2(\Lambda_{2m})=\lfloor\log_2(2m+1)\rfloor\). Their difference is
\[
\lfloor\log_2(2w-1)\rfloor-\lfloor\log_2w\rfloor+\nu_2(w)
=1+\nu_2(w)-\mathbf1_{\{w\text{ is a power of }2\}}.
\]
Indeed the first two floors differ by zero exactly when \(w\) is a power of two, and by one otherwise. No odd prime is lost, so the first quotient follows.

**4. Retaining odd indices when \(N=2m\): the prime two.** Here \(\nu_2(N+1)=0\). For \(r\ge1\), the odd index \(k=2^r-1\) attains \(\nu_2(\Lambda_N)=r\) by (1); for \(r=0\) both valuations vanish. Hence no power of two is lost.

**5. Retaining odd indices: an odd prime.** Fix an odd prime \(p\) and let \(r,t\) be as in (1). If \(r-t=0\), there is no possible loss. Otherwise \(r\ge1\), and consider the base-\(p\) digits \(N_i\) of \(N\).

If \(t\ge1\), the odd index \(k=p^r-2\) is permitted: its units digit is \(p-2\) and its digits in positions \(1,\ldots,r-1\) are \(p-1\). It produces a borrow first at position \(t\) and one at every subsequent position through \(r-1\), exactly \(r-t\) borrows. If \(t=0\) and \(N_0\le p-3\), the same odd index initiates a borrow at position zero and continues through \(r-1\), realizing \(r\).

It remains to handle \(t=0\) and \(N_0=p-2\), equivalently \(p\mid N+2\). If some digit \(N_j\le p-2\) with \(1\le j\le r-1\), choose the odd index \(k=p^r-1-p^j\). Its units digit \(p-1\) starts a borrow; the decreased digit \(p-2\) at position \(j\) still exceeds the borrowed-from digit \(N_j-1\); and all other positions up to \(r-1\) have digit \(p-1\). Thus all \(r\) borrows occur. If no such \(j\) exists, then \(N\equiv p^r-2\pmod{p^r}\), so \(N+2=c p^r\) for a positive integer \(c\). Because \(N\) is even and \(p\) odd, \(c\) is even. When \(c\ge4\), the odd index \(k=2p^r-1\le N\) has low \(r\) digits all \(p-1\), so also produces \(r\) borrows.

The sole remaining possibility is \(c=2\), or \(N=2p^r-2\), which is equivalent to \(w=p^r\). In this case the low \(r\) digits of \(N\) are \((p-2,p-1,\ldots,p-1)\). To borrow in all \(r\) positions, an index must be congruent to \(p^r-1\) modulo \(p^r\): each of its low \(r\) digits must be \(p-1\). The only such permitted index between zero and \(N\) is \(p^r-1\), which is even; the next is \(2p^r-1>N\). Hence no odd index reaches \(r\) borrows. The odd index \(k=p^r-1-p^{r-1}\) does yield exactly \(r-1\) borrows (for \(r=1\) it yields zero). Thus exactly one factor \(p\) is lost. As \(w\) cannot be a positive power of two different odd primes, at most one odd prime is lost. This proves the second quotient and the theorem. \(\square\)

## Verification
The accompanying standalone `verify.py` performs direct, exact arbitrary-precision binomial and LCM computations for all \(1\le N\le800\), comparing both ratios with the closed formulas. It independently checks \(\nu_2\binom{2m}{2j}=\nu_2\binom mj\) for all \(1\le m\le150\) and \(0\le j\le m\). The expected output is `VERIFY_OK exact_row_lcms=800 doubled_index_checks=11475`. Finite tests are not substituted for the infinite proof above.

## Relationship to prior work
Farhi [1] proves the full-row formula \(\Lambda_N=\operatorname{lcm}(1,\ldots,N+1)/(N+1)\) and the full-row prime-valuation maximizer. The present theorem concerns retaining exactly the even or odd *index set*, a selection not resolved by the full-row identity alone. Hong [2] proves equivalence of Farhi's formula with Nair's identity; it does not treat parity-restricted subrows. Huber [3] optimizes LCMs of selected entries, including the fixed-row formulation, but the inspected theorem addresses extremal subsets and asymptotics, not this complete closed classification for the prescribed parity subsets. Classical Kummer's theorem [4] provides the borrow interpretation used here. No claim is made to discovering the full-row formula or the general borrow theorem.

## Limitations
The statement is only about two parity classes of the index set, not arbitrary residue-class restrictions. The exact expressions are algebraic identities, not estimates for the magnitude of the full-row LCM. An exhaustive publication-priority guarantee is not possible from indexed literature; further independent priority checking is warranted. Independent audit has not been performed.

## References
[1] B. Farhi, *An identity involving the least common multiple of binomial coefficients and its application*, arXiv:0906.2295 (first public version 12 June 2009); American Mathematical Monthly 116 (2009), 836–839. https://arxiv.org/html/0906.2295v2

[2] S. Hong, *Nair's and Farhi's identities involving the least common multiple of binomial coefficients are equivalent*, arXiv:0907.3401 (2009). https://arxiv.org/abs/0907.3401

[3] F. Huber, *Extremal Least Common Multiples in Rows of Pascal's Triangle*, arXiv:2609.23024 (2026). https://arxiv.org/abs/2609.23024

[4] E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik 44 (1852), 93–146.
