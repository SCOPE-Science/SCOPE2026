# Exact scattered-subsequence universality of Rudin–Shapiro prefixes

## Finding
Let \(r(n)\) be the parity of the number of overlapping occurrences of the binary digit pair \(11\) in the base-two expansion of \(n\). For \(N\geq 0\), write \(R_N=r(0)r(1)\cdots r(N-1)\). Let \(U(N)\) be the largest nonnegative integer \(k\) such that **every** binary word of length \(k\) is an order-preserving, not necessarily contiguous, subsequence of \(R_N\).

For each integer \(m\geq4\),
\[
U(2^m)=\begin{cases}
5\cdot 2^{m-4}-1,&m\text{ even},\\
5\cdot 2^{m-4},&m\text{ odd}.
\end{cases}
\]
The four preceding values, for \(m=0,1,2,3\), are \(0,0,1,2\), respectively. Moreover, for **every** integer \(N\geq1\),
\[
\left|U(N)-\frac{5N}{16}\right|\leq s_2(N),
\qquad \lim_{N\to\infty}\frac{U(N)}{N}=\frac5{16},
\]
where \(s_2(N)\) is the number of ones in the binary expansion of \(N\). Thus the exact dyadic alternation is accompanied by a uniform logarithmic discrepancy bound.

## Assumptions and scope
Indices start at zero. A subsequence is obtained by deleting arbitrarily many letters while retaining order; it is **not** required to be a contiguous factor. The alphabet is fixed to \(\{0,1\}\), including for prefixes with only one letter. For the empty prefix, \(U(0)=0\). The theorem concerns prefixes of the conventional binary Rudin–Shapiro sequence and makes no claim for arbitrary factors starting away from zero.

Use the two-uniform morphism \(\sigma\) on \(\{a,b,c,d\}\):
\[
\sigma(a)=ab,\qquad\sigma(b)=ac,\qquad
\sigma(c)=db,\qquad\sigma(d)=dc,
\]
with coding \(\pi(a)=\pi(b)=0\) and \(\pi(c)=\pi(d)=1\). Let \(W_{m,x}=\pi(\sigma^m(x))\), of length \(2^m\). The prefix \(R_{2^m}\) is \(W_{m,a}\).

## Proof
**1. Identification of the morphic word.** Label the four morphism states by the pair (parity of binary \(11\) occurrences, last binary digit), as \(a=(0,0)\), \(b=(0,1)\), \(c=(1,1)\), \(d=(1,0)\). Appending a zero preserves the parity and sets the last digit to zero. Appending a one toggles the parity exactly when the previous last digit was one. The pair of transitions under append-zero and append-one is exactly the displayed morphism. Starting from \(a\) proves the fixed-point coding and the digit definition agree for all nonnegative indices.

**2. Greedy arches equal the universality index.** Scan a binary word left to right, collecting unseen binary symbols until both have appeared; at that moment complete an *arch* and reset the collection. Say \(k\) arches are completed. Any prescribed binary word of length \(k\) embeds by choosing its successive letters from successive arches. Conversely, let \(v_i\) be the last (first newly encountered) letter of arch \(i\), for \(1\leq i\leq k\), and let \(v_{k+1}\) be a letter missing from the final incomplete tail. In any embedding of \(v_1\cdots v_kv_{k+1}\), the first \(v_i\) cannot occur before the end of the \(i\)-th arch, inductively; the final requested letter cannot then occur. Therefore there is a missing length-\(k+1\) word. Hence \(U(N)\) is exactly the completed-arch count.

**3. A three-state additive cocycle.** The scanner states are \(0\) (nothing seen since the last arch), \(1\) (only binary zero seen), and \(2\) (only binary one seen). For a finite binary word \(v\), let \(T_v(t)=(e,c)\) mean: starting in state \(t\), the scanner exits in state \(e\) and completes \(c\) arches. These profiles compose exactly: if \(T_u(t)=(e,c)\) and \(T_v(e)=(f,d)\), then \(T_{uv}(t)=(f,c+d)\). Thus \(T_{W_{m+1,x}}\) is the composition of the two profiles for the letters in \(\sigma(x)\).

Put \(q=5\cdot2^{m-4}\) for \(m\geq4\). The following *complete* profiles hold; the middle entry is their common exit state, and the final triple gives the number of arches on starting in states \(0,1,2\), respectively.

For **even** \(m\geq4\):

| Block | Exit | Counts at states \(0,1,2\) |
| --- | --- | --- |
| \(W_{m,a}\) | \(2\) | \((q-1,q-1,q)\) |
| \(W_{m,b}\) | \(1\) | \((q,q,q+1)\) |
| \(W_{m,c}\) | \(2\) | \((q,q+1,q)\) |
| \(W_{m,d}\) | \(1\) | \((q-1,q,q-1)\) |

For **odd** \(m\geq5\):

| Block | Exit | Counts at states \(0,1,2\) |
| --- | --- | --- |
| \(W_{m,a}\) | \(1\) | \((q,q,q+1)\) |
| \(W_{m,b}\) | \(2\) | \((q-1,q-1,q)\) |
| \(W_{m,c}\) | \(1\) | \((q-1,q,q-1)\) |
| \(W_{m,d}\) | \(2\) | \((q,q+1,q)\) |

The base case \(m=4\) is verified by applying the one-letter transition rules to the four explicit coded length-sixteen blocks. For the inductive step, compose according to \(a\mapsto ab\), \(b\mapsto ac\), \(c\mapsto db\), \(d\mapsto dc\). In each row, the exit state is independent of the initial state; therefore the count is the left-block count plus a constant determined by the left-block exit. Substitution gives precisely the odd table from the even table, and the even table from the odd table, upon replacing \(q\) by \(2q\). These eight identities are also checked as symbolic affine-polynomial identities, not just at sampled numerical levels, in `verify.py`. This proves the displayed complete profile tables for all \(m\geq4\).

**4. Exact dyadic formula.** Starting from the empty scanner state, \(U(2^m)\) is the first count in the row for \(W_{m,a}\). This yields \(q-1\) for even \(m\) and \(q\) for odd \(m\). Direct transitions at levels \(m=0,1,2,3\) give the four exceptional values.

**5. Uniform prefix discrepancy.** For any state and any \(x\in\{a,b,c,d\}\), the tables prove
\[
\left|\text{arches completed while scanning }W_{m,x}
-\frac{5\cdot 2^m}{16}\right|\leq1 \qquad(m\geq4).
\]
Direct evaluation at \(m=0,1,2,3\) gives maximal absolute errors \(11/16,10/16,12/16,8/16\), respectively, so the same bound holds for all \(m\geq0\). Express \(N\) as a sum of its distinct powers of two in decreasing order. The corresponding prefix of the infinite fixed point partitions into exactly \(s_2(N)\) *aligned* morphism blocks, because every block begins at a multiple of its own length \(2^m\). Each such block is some \(W_{m,x}\). Additivity of arch counts along the successive scanner states gives the asserted \(s_2(N)\) discrepancy. Since \(s_2(N)\leq1+\lfloor\log_2N\rfloor\), division by \(N\) proves the limit.

## Verification
Run the accompanying standalone Python 3 file `verify.py` without external libraries. It checks the explicit base profiles and the two parity-switch induction identities **symbolically in the variable** \(q\), comparing integer affine coefficients and exit states. It also verifies the morphism coding against an independent binary-digit oracle, directly scans all prefix lengths through \(2^{18}\), checks nineteen dyadic levels, and compares greedy arch counts with brute-force subsequence universality at lengths up to twenty-two. The observed verifier output is:

```
VERIFY_OK symbolic_induction=even_to_odd_and_odd_to_even small_block_bounds=yes morphism_prefix=2^12 direct_prefixes=262144 exact_dyadic_levels=19 brute_subsequences_lengths=0..22
```

The symbolic composition identities and proof establish the infinite result. The finite direct scans are consistency checks, not a substitute for induction.

## Relationship to prior work
Barker et al., *Scattered Factor-Universality of Words* (arXiv:2003.04629), and Schnoebelen–Veron, *On arch factorization and subword universality for words and compressed words* (arXiv:2304.11932), provide the established arch framework and, in the latter paper, compositional universality signatures. Their results make generic computation of the index possible but do not state the exact \(5/16\) limiting density, dyadic parity correction, or uniform all-prefix discrepancy for the Rudin–Shapiro word. Adamson et al., *Tight Bounds for the Number of Absent Subsequences* (arXiv:2407.18599), develops structural and enumerative theory of absent subsequences for words with a prescribed universality index; it does not determine that index for these morphic prefixes. Rampersad–Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic* (arXiv:2302.00405), concerns ordinary arithmetic prefix sums of this automatic word rather than the greedy arch-count statistic.

The novelty asserted here is the **named-word exact profile and resulting asymptotic/dyadic theorem**, not invention of the arch algorithm or of compositional signatures. General statements about shortest absent subsequences, ordinary contiguous factors, or arithmetic prefix sums do not imply the displayed formula without additional analysis of the fixed point.

## Limitations
The proof is specific to the standard binary Rudin–Shapiro fixed point and its prefixes; it does not determine the index for arbitrary shifts or morphisms. The discrepancy bound is an explicit uniform upper bound, not claimed optimal at every length. Searches may miss an earlier unindexed equivalent calculation; the claimed relationship to prior work is therefore subject to that identifiable bibliographic limitation.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (first posted 2020-03-10), https://arxiv.org/abs/2003.04629.
2. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932 (first posted 2023-04-24), https://arxiv.org/abs/2304.11932.
3. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first posted 2024-07-26; primary MSC 68R15), https://arxiv.org/abs/2407.18599.
4. N. Rampersad and J. Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic*, arXiv:2302.00405 (first posted 2023-02-01), https://arxiv.org/abs/2302.00405.
