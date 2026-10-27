# Sharp radical bound and squarefree generating-power rigidity of cyclic orbit signatures

## Finding
Let \(n\ge2\) and let \(\sigma\) be a single \(n\)-cycle on an \(n\)-element linearly ordered set \(S\). For any \(x\in S\) and \(t\ge1\), its *left-right orbit signature* records whether \(\sigma^t(x)\) is less than, equal to, or greater than \(x\). Let \(U(\sigma)\) consist of residues \(u\in(\mathbb Z/n\mathbb Z)^\times\) for which \(\sigma^u\) has exactly the same signatures at every point and every positive time as \(\sigma\). Let \(\operatorname{rad}(n)=\prod_{p\mid n}p\), the product of distinct prime divisors.

**Theorem.** For every such \(\sigma\),
\[
U(\sigma)\subseteq\{u\pmod n:u\equiv1\pmod{\operatorname{rad}(n)}\}.
\]
For each integer \(n\ge2\), there is an explicitly constructed \(n\)-cycle attaining equality. In particular,
\[
\max_{\sigma}|U(\sigma)|=\frac{n}{\operatorname{rad}(n)}.
\]
Thus **every squarefree cycle length is rigid among powers of the same cycle**: no nonidentity generating power preserves the full left-right signature. This is compatible with the existence of unrelated distinct cycles with identical signatures at composite lengths.

## Assumptions and scope
A cycle has minimal period \(n\) at all its points. The order on \(S\) is fixed and total; the sign at time \(t\) compares the orbit point with its own starting point, not with its predecessor or with the previous orbit point. Powers are restricted to \(u\) coprime to \(n\), so \(\sigma^u\) is another generator of the **same** cyclic group and itself a single \(n\)-cycle. No assertion of uniqueness among arbitrary unrelated permutations sharing signatures is made. The value of \(U(\sigma)\) need not attain the maximum for an arbitrary order.

## Proof
**1. Universal prime-divisor obstruction.** Fix any prime \(p\mid n\) and put \(d=n/p\). The permutation \(\tau=\sigma^d\) decomposes into \(d\) disjoint cycles of length exactly \(p\). Take one such \(p\)-orbit \(C\), ordered as a subset of \(S\), and let \(x\) be its second-smallest point. Let \(y\) be its smallest point. There exists a unique \(t_0\in\{1,\ldots,p-1\}\) satisfying \(\tau^{t_0}(x)=y\); it is the unique positive time below \(x\) within this \(p\)-orbit.

For any \(u\in U(\sigma)\), the maps \(\tau\) and \(\tau^u=(\sigma^u)^d\) have the same left-right signatures on \(C\), because these signatures are entries of those of \(\sigma\) and \(\sigma^u\) at multiples of \(d\). In particular, at time \(t_0\), both powers must map \(x\) below itself. The only point in \(C\) below \(x\) is \(y\), so \(\tau^{ut_0}(x)=\tau^{t_0}(x)\). As \(\tau\) is a \(p\)-cycle, \(p\mid(u-1)t_0\). Since \(1\le t_0<p\), we conclude \(u\equiv1\pmod p\). This holds for every prime divisor, proving \(u\equiv1\pmod{\operatorname{rad}(n)}\). The latter congruence class has exactly \(n/\operatorname{rad}(n)\) residues modulo \(n\), all coprime to \(n\), giving the upper bound.

**2. An attaining order by Chinese remainder digits.** Write the prime-power factorization \(n=\prod_{i=1}^s p_i^{a_i}\), with primes indexed increasingly. Label the points by orbit times \(j\in\mathbb Z/n\mathbb Z\), and define the cycle by \(\sigma(j)=j+1\). The Chinese remainder theorem identifies each time \(j\) with its residues modulo every \(p_i^{a_i}\). Write each residue in base \(p_i\) in *least-significant-digit-first* order,
\[
(j_{i,0},j_{i,1},\ldots,j_{i,a_i-1}),\qquad 0\le j_{i,r}<p_i.
\]
Order the times lexicographically by the concatenation of these digit strings, taking the blocks in increasing prime order. As the digit strings uniquely encode the residue class, this defines a total order on all \(n\) points.

Suppose \(u\equiv1\pmod{\operatorname{rad}(n)}\). Fix a time \(j\) and an increment \(t\), viewed modulo \(n\). For a prime-power block \(p_i^{a_i}\), if \(t\equiv0\pmod{p_i^{a_i}}\), both \(j+t\) and \(j+ut\) have exactly the same block as \(j\). Otherwise write \(r=v_{p_i}(t)<a_i\). For both increments \(t\) and \(ut\), the digits below position \(r\) are unchanged, while the digit at position \(r\) changes by the *same nonzero residue* \(t/p_i^r\pmod{p_i}\): indeed \(u\equiv1\pmod{p_i}\), and no carry can enter digit \(r\) from lower positions because the increments are divisible by \(p_i^r\). Therefore the earliest changed digit within this prime-power block is the same for \(j+t\) and \(j+ut\), and its new digit has the same value in both.

Across all blocks, the **first globally differing digit** in the lexicographic order is consequently at the same position and has the same changed value for both increments. Hence \(j+t\) is to the left of \(j\) exactly when \(j+ut\) is; the analogous statement holds to the right. If \(t\equiv0\pmod n\), both are equal to \(j\). As \(j,t\) were arbitrary, \(u\in U(\sigma)\). Combining with step 1 proves exact equality for the constructed cycle, and the theorem follows. \(\square\)

## Verification
The independent finite checker `VERIFY.py` performs exact comparisons of all nonzero-time left-right signs. It checks the attaining digit order for every \(n\in\{2,\ldots,80\}\) and independently enumerates **every** cyclic permutation for \(2\le n\le8\) (\(5913\) oriented cycles after selecting the least point as phase zero). All \(5992\) assertions pass. Run `python3 VERIFY.py` in an ordinary Python 3 environment. The proof above is universal; these finite computations are not substituted for it.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi (2026), Section 2, introduce left-right orbit signatures and prove complete reconstruction of an **arbitrary** cycle of *prime* length from its signature (Lemma 2.1). They explicitly observe that unrelated distinct permutations of every composite length may share signatures (discussion preceding Lemma 2.1). These statements do not determine the number of **generating powers of the same cycle** preserving a signature. A published quadratic-time reconstruction result concerns prime cycles only and is not an all-length ambiguity bound.

The prime-power restriction \(n=p^a\) of the sharp bound and its digit-order construction was already obtained previously; it is **not** claimed as new here. The additional result is the **joint-prime** sharp theorem for arbitrary mixed-factor lengths, together with the squarefree-composite rigidity dichotomy. The upper proof uses prime subcycles, while the attaining lower construction must satisfy all prime-power constraints simultaneously under the Chinese remainder identification.

## Limitations
The bound concerns only generating powers of one fixed cycle, not arbitrary pairs of cycles sharing a signature. It is a sharp maximum over orders, not a complete classification of all possible subgroups \(U(\sigma)\) or all maximizing orders. Existing literature under alternative terminology for orbit-comparison signatures or cyclic digit orderings may contain equivalent statements; bibliographic priority beyond the inspected sources is not independently certified. Verification covers finite examples while the proof covers every \(n\ge2\).

## References
1. G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (first posted 2026-10-05), particularly Section 2 and Lemma 2.1. https://arxiv.org/abs/2610.07435
2. *Quadratic-time reconstruction of prime cycles from left-right orbit signatures*, published mathematical research record (2026-10-11), with full result at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-quadratic-time-reconstruction-of-prime-cycles-from-left-right-or--f270190d0cd7
