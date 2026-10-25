# A uniform 32-class dyadic bias law for two-summand Zeckendorf–Niven numbers

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For each fixed integer \(a\ge5\), residue \(r\pmod{2^a}\), and \(N\ge4\), define
\[
Z_{a,r}(N)=\#\{(i,j):2\le i<j\le N,\ j-i\ge2,\ F_i+F_j\equiv r\pmod{2^a},\ 2\mid F_i+F_j\}.
\]
These pairs give exactly the integers represented by legal two-summand Zeckendorf decompositions with largest index at most \(N\). The last condition is precisely the Zeckendorf–Niven condition (divisibility by the number of summands).

If \(r\) is odd, then \(Z_{a,r}(N)=0\). If \(r\) is even, then
\[
\boxed{Z_{a,r}(N)=\frac{\kappa(r\bmod32)}{18\cdot2^a}N^2+O_a(N),}
\]
where the complete positive coefficient function on the even classes is

| \(r\bmod32\) | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| \(\kappa(r)\) | 8 | 14 | 14 | 10 | 8 | 14 | 6 | 10 | 8 | 14 | 6 | 10 | 8 | 14 | 6 | 10 |

Every even dyadic progression consequently contains infinitely many two-summand Zeckendorf–Niven integers, but the extreme leading frequencies differ by the *exact* factor \(14/6=7/3\). The coefficient rule, including its independence of \(a\) above the universal scaling \(2^{-a}\), is the result; the aggregate two-summand Niven fraction \(5/9\) is previously known.

## Assumptions and scope

The Zeckendorf digits are nonconsecutive indices from \(F_2,F_3,\ldots\), so distinct eligible index pairs represent distinct positive integers by uniqueness of Zeckendorf decomposition. The cutoff \(N\) is an **index cutoff**; no asymptotic with an ordinary size cutoff \(n\le X\) is asserted. The modulus is \(2^a\) with integer \(a\ge5\); implied constants in \(O_a(N)\) may depend on \(a\). There is no assumption of independence between neighboring indices.

## Proof

**Step 1: a lifting law for Fibonacci residues.** For every integer \(k\ge1\), set \(t=6\cdot2^k\). We first show
\[
F_t=2^{k+3}v_k,\qquad F_{t+1}-1=2^{k+2}u_k,
\qquad u_k\equiv v_k\equiv1\pmod4.
\]
At \(k=1\), \(F_{12}=144=2^4\cdot9\) and \(F_{13}-1=232=2^3\cdot29\). To double \(t\), use
\[
F_{2t}=F_t(2F_{t+1}-F_t),\qquad F_{2t+1}=F_{t+1}^2+F_t^2.
\]
The two normalized new odd factors are respectively
\[
v_{k+1}=v_k\bigl(1+2^{k+2}(u_k-v_k)\bigr),\quad
u_{k+1}=u_k+2^{k+1}u_k^2+2^{k+3}v_k^2,
\]
both congruent to \(1\pmod4\). The induction is complete.

For any \(n\ge0\), the Fibonacci addition identity (with \(F_{-1}=1\) when needed) gives
\[
F_{n+t}-F_n=(F_{t+1}-1)F_n+F_tF_{n-1}.
\]
Direct reduction of the six-index Fibonacci recurrence modulo \(8\) gives three mutually exclusive cases: if \(3\nmid n\), \(F_n\) is odd; if \(n\equiv0\pmod6\), then \(8\mid F_n\) and \(F_{n-1}\) is odd; if \(n\equiv3\pmod6\), then \(F_n/2\equiv F_{n-1}\equiv1\pmod4\). Therefore the displayed identity and the odd-factor congruences imply the **exact valuation law**
\[
\nu_2(F_{n+t}-F_n)=
\begin{cases}
k+2,&3\nmid n,\\
k+3,&n\equiv0\pmod6,\\
k+4,&n\equiv3\pmod6.
\end{cases}
\]
In particular, \(P_a=6\cdot2^{a-2}=3\cdot2^{a-1}\) is a period modulo \(2^a\) for every \(a\ge5\). Minimality is unnecessary.

**Step 2: uniform lifting of the exact residue multiplicities.** Define
\[
C_a(x)=\#\{0\le n<P_a:F_n\equiv x\pmod{2^a}\}.
\]
For the base case \(a=5\), iteration of the 48 recurrence steps modulo 32 (reproduced by the integer verifier) gives \(C_5(x)=c(x)\), where
\[
c(x)=\begin{cases}
3,&x\equiv1\pmod4,\\
1,&x\equiv3\pmod4,\\
2,&x\equiv0\pmod8,\\
8,&x\equiv2\pmod{32},\\
0,&\text{otherwise}.
\end{cases}
\]
For the induction, two lifts of a class modulo \(2^a\) differ by \(2^a\), and \(P_{a+1}=2P_a\). If \(3\nmid n\), shifting the index by \(P_a\) flips exactly this bit, so the two copies of each index within one \(2P_a\) period distribute equally across lifts. If \(n\equiv0\pmod6\), the shift \(P_a/2\) flips this bit while preserving the residue modulo \(2^a\). It pairs the two occurrences of each residue \(x\equiv0\pmod8\) within the first \(P_a\) indices, and the second copy of that block doubles both lift counts. Cyclic wraparound of the shift changes Fibonacci values by a multiple of \(2^{a+1}\) on this index class, by the same valuation law. If \(n\equiv3\pmod6\), the shift \(P_a/4\) flips the bit; it permutes the indices of this class within the first \(P_a\) indices (because \(P_a/4\) is divisible by 6). Thus it pairs the eight occurrences of \(x\equiv2\pmod{32}\) equally across the two lifts, and repetition of the block gives eight occurrences per lift. The cyclic wraparound again preserves the lifted residue because shifting by \(P_a\) changes these values by a multiple of \(2^{a+1}\). These index classes are disjoint and exhaustive. Therefore
\[
\boxed{C_a(x)=c(x\bmod32)\quad\text{for every }a\ge5\text{ and }x\bmod2^a.}
\]

**Step 3: pair convolution and the asymptotic.** Write
\[
D_a(r)=\sum_{x\bmod2^a}C_a(x)C_a(r-x).
\]
The lifting formula shows \(D_a(r)=2^{a-5}D_5(r\bmod32)\). Exact convolution of the 32 displayed base-case multiplicities gives \(D_5(r)=64\) for odd \(r\), and \(D_5(r)=8\kappa(r)\) for even \(r\); the integer verifier computes every coefficient. Over \(1\le i,j\le N\), periodicity modulo \(2^a\) gives \(D_a(r)N^2/P_a^2+O_a(N)\) ordered pairs with \(F_i+F_j\equiv r\). Restricting to \(i<j\) halves the principal term; excluding diagonal and adjacent index pairs, and excluding indices \(0,1\), changes the count only by \(O(N)\). If \(r\) is even the divisibility-by-two condition is automatic; if \(r\) is odd it is impossible. Consequently, for even \(r\),
\[
Z_{a,r}(N)=\frac{2^{a-5}(8\kappa(r))}{2(3\cdot2^{a-1})^2}N^2+O_a(N)
=\frac{\kappa(r)}{18\cdot2^a}N^2+O_a(N).
\]
Every even coefficient is strictly positive, proving infinitude and the exact \(7/3\) bias. Summation of the 16 coefficients gives \(160\), consistent with the independently known aggregate Niven fraction \(5/9\); this aggregate is not asserted as new.

## Verification

The self-contained `verify.py` uses only exact integer operations. Execute `python3 verify.py` in the directory containing that file. It checks the 48-step base distribution, all 32 pair-convolution values, complete periods modulo \(2^a\) for \(5\le a\le11\), and direct enumeration of legal two-summand pairs for 16 index-cutoff/modulus combinations. It prints `VERIFY_OK powers=5..11 residue_cells=4064 mod32_pair_convolution=PASS exact_index_pairs=16 class_bias=PASS`. The finite tests corroborate, but do not replace, the universal lifting proof.

## Relationship to prior work

Lao, Miller, Rosa, Shiliaev, Tresch, Wong and Zhang (arXiv:2606.24006v1; June 22, 2026) prove existence of Zeckendorf–Niven integers in every arithmetic progression and study runs of such integers. Here the different question is the **exact two-summand, index-cutoff, per-dyadic-residue leading coefficient**, including the nonuniform factor \(7/3\). Bragman and Rowland (arXiv:2202.00704; *Research in Number Theory*, 2025) determine the 2-adic *image* of Fibonacci residues, including its limiting image density \(21/32\); image support alone does not give the index-frequency distribution \(C_a\), its self-convolution, or Niven counts. Prodinger (2026) gives generating-function convolutions of Fibonacci values along index classes, not the additive convolution of modular value frequencies here. Existing fixed-weight Zeckendorf–Niven counts give the aggregate weight-two fraction \(5/9\); this result does not claim that figure, and refines it by giving all dyadic residue coefficients. Older work of Ray and Cooper on natural densities of Zeckendorf–Niven numbers concerns a distinct global denominator, and was accessible for comparison only at the abstract level.

## Limitations

The asymptotic concerns index-restricted two-summand decompositions and fixed powers of two only, not a counting function ordered by integer magnitude, arbitrary moduli, or three or more Zeckendorf summands. The new formula can be recovered by a sufficiently detailed specialization of general Fibonacci-period methods; a bibliographically unindexed equivalent may exist. The Ray–Cooper full article was not accessible during the literature comparison, so priority requires independent checking. No independent mathematical audit has been performed.

## References

1. K. Lao, S. J. Miller, N. Rosa, M. Shiliaev, G. Tresch, T. W. H. Wong and H. Zhang, *On Zeckendorf-Niven Numbers and Arithmetic Progressions*, arXiv:2606.24006v1 (2026), https://arxiv.org/abs/2606.24006.
2. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, *Research in Number Theory* **11**, article 88 (2025), doi:10.1007/s40993-025-00667-1; arXiv:2202.00704.
3. H. Prodinger, *Fibonacci numbers along residue classes and convolutions*, *Notes on Number Theory and Discrete Mathematics* **32** (2026), 374–377, doi:10.7546/nntdm.2026.32.2.374-377.
4. A. Ray and C. Cooper, *On the natural density of the k-Zeckendorf Niven numbers* (2006), bibliographic abstract inspected; complete text not inspected.
