# Exact dyadic Rudin–Shapiro string-attractor sizes through length 1024

## Finding

Let \(r_i\in\{0,1\}\) be the parity of the number of overlapping occurrences of the bit pattern `11` in the ordinary base-two representation of the nonnegative integer \(i\), with \(r_0=0\). Let \(R_N=r_0r_1\cdots r_{N-1}\), and let \(\gamma(w)\) be the smallest cardinality of a string attractor of a finite word \(w\). Then the following four natural dyadic-prefix values are exact:

\[
\boxed{\gamma(R_{128})=10,\quad\gamma(R_{256})=11,\quad\gamma(R_{512})=12,\quad\gamma(R_{1024})=12.}
\]

The accompanying exact integer certificates prove both inequalities for each value. In particular, the final two dyadic lengths exhibit a plateau; nothing about all larger dyadic lengths or asymptotic growth is asserted.

## Assumptions and scope

A position set \(\Gamma\subseteq\{1,\ldots,N\}\) is a string attractor of \(w=w_1\cdots w_N\) when, for every distinct nonempty factor \(x\), there is at least one occurrence interval \([a,b]\) of \(x\) with \(\Gamma\cap[a,b]\ne\varnothing\). All positions in the theorem and stored witnesses are **one-based**. The sequence uses the binary `0/1` coding of the Rudin–Shapiro signs and has prefix `0001001000011101`. Complementing all bits does not change attractor sizes.

For a factor \(x\), define its position coverage
\[
C_w(x)=\bigcup_{a:\,w[a..a+|x|-1]=x}[a,a+|x|-1].
\]
The relevant covering hypergraph \(\mathcal H_N\) consists of all inclusion-minimal sets among these coverages. The verifier reconstructs this hypergraph from **every** distinct factor rather than accepting a precomputed list as authoritative. Its cardinalities are respectively \(48,64,80,96\).

## Proof

**1. Exact finite reduction.** A set \(\Gamma\) is an attractor if and only if it meets every \(C_w(x)\). Because the factor family is finite, each such coverage contains an inclusion-minimal coverage. Therefore \(\Gamma\) is an attractor if and only if it meets every member of \(\mathcal H_N\). The code computes every factor and its complete union of occurrence intervals by finite enumeration, deduplicates the resulting bit masks, and retains precisely inclusion-minimal masks by checking set containment. The stored masks in `certificates.json` are checked for exact equality with this regenerated family.

**2. Upper bounds.** The explicit position sets below each hit all regenerated minimal coverages, which proves the required upper bounds by Step 1:

\[
\begin{aligned}
N=128:&\quad\{33,49,57,73,77,85,93,101,105,121\};\\
N=256:&\quad\{57,71,97,109,121,145,162,193,197,209,235\};\\
N=512:&\quad\{99,131,189,201,225,285,305,329,385,407,433,471\};\\
N=1024:&\quad\{225,269,357,409,449,561,609,665,769,817,843,935\}.
\end{aligned}
\]

**3. Integer dual lower bounds.** In each regenerated hypergraph, the certificate names a subfamily \(C_i\) of \(s\) distinct minimal coverages and a denominator \(d\in\{1,2\}\), satisfying
\[
\textstyle\sum_{i=1}^s \mathbf 1_{\{p\in C_i\}}\le d\quad\text{for every position }p.
\]
Each attractor must hit every \(C_i\); double counting incidence therefore proves \(|\Gamma|\ge s/d\). The stored indices refer to verified actual coverages and the checker verifies these inequalities at all \(N\) positions with integers, without using floating optimization tolerances. The four certified pairs \((s,d)\) are \((9,1),(10,1),(22,2),(24,2)\), giving lower bounds \(9,10,11,12\).

**4. Excluding equality at the first three lengths.** Suppose a size-\(s/d\) attractor existed at one of \(N=128,256,512\). The double-counting inequalities would have to be equalities throughout. Thus every selected position belongs to **exactly** \(d\) of the positive-dual coverages, and each positive-dual coverage is hit **exactly once**. The certificate identifies further genuine minimal coverages (20, 40, and 51 total constraints, respectively, including all positive-dual ones). A complete exact-cover recursion enumerates all possibilities for points satisfying these equality conditions, requiring simultaneous coverage of those additional sets. It returns **no solution** in each case.

For transparency, the recursion represents uncovered positive-dual sets as an integer bit mask. It picks an uncovered set and branches over every available position meeting that set and no previously covered positive-dual set; then removes precisely the newly hit positive-dual sets. At each node, it also tracks uncovered additional constraints. A branch is discarded only when an uncovered additional constraint has no possible future position; at the leaf it accepts only when both masks are empty. Identical candidate incidence patterns are merged, and a point is discarded in favor of another only when both meet the same positive-dual sets and the latter meets every additional constraint the former meets. These replacements preserve feasibility in both directions. The recursion is exhaustive by induction on the number of uncovered positive-dual sets. The replayed searches visit only 30, 2566, and 1316 distinct memoized states, respectively.

Consequently each of the first three bounds must be increased by one; at the fourth length the dual and displayed upper bound already coincide. This proves the four claimed exact values.

## Verification

From a directory containing `verify.py` and `certificates.json`, run `python3 verify.py`. Python 3.10 or later suffices; no external solver, network, or third-party package is needed. The code independently regenerates the full Rudin–Shapiro word and all distinct factors, reconstructs all minimal coverages, verifies each position witness, checks every dual incidence inequality exactly, and exhaustively excludes the three equality cases. It ends with `VERIFY_OK` only when all claims hold. The source code, finite certificate masks, and full word prefixes are embedded as standalone files in this result package.

The distinct-factor counts at lengths \(128,256,512,1024\) are respectively \(7008,28128,112608,450528\), independently reconstructed in the finite verifier. Exhaustiveness here is for those four finite strings only; no extrapolation to infinite-word behavior is used.

## Relationship to prior work

Schaeffer and Shallit (arXiv:2012.06840) studied attractors of automatic sequences and showed broad decidability and complexity bounds, with concrete results for period-doubling, Thue–Morse and other sequences. Banbara et al. (arXiv:2602.16152) classified optimal attractors for Fibonacci and period-doubling words. Faro, Marino and Pavone (arXiv:2610.10950) gave a structural classification of optimal attractors and essential factor-coverages for finite **Thue–Morse** words, rather than Rudin–Shapiro words. Their factor-coverage viewpoint motivates the verified finite reduction above.

The closest identified published Rudin–Shapiro benchmark (published-finding corpus entry `2026/9/8/SCOPE079`) reports exact dyadic minima only through length \(64\), together with attractor **upper bounds** \(12,13,15,16\) at lengths \(128,256,512,1024\). Its searchable summary does not assert the exact values given here. This finding determines the four values exactly and improves those reported upper bounds. The complete underlying benchmark artifact was not accessible during comparison, so an unobserved equivalent calculation remains an explicit originality risk.

## Limitations

These are four exact, finite computational theorems with independently checkable integer certificates; no formula for other lengths and no asymptotic classification is proved. The required factor enumeration has quadratic numbers of tested intervals in the prefix length and the certificate is specialized to these lengths. The hypergraph equality cases are certified by exhaustive finite recursion, not an informal argument from an optimization log. Originality comparison cannot exclude unpublished results, unavailable supplementary tables or unindexed previous enumerations. Independent external mathematical audit has not been performed.

## References

1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (original public version 2020). https://arxiv.org/abs/2012.06840
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno and Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152, first published 2026-02-18. https://arxiv.org/abs/2602.16152
3. S. Faro, F. P. Marino and A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950v1, first published 2026-10-07. https://arxiv.org/html/2610.10950v1
4. *Exact minimal string attractors for Rudin-Shapiro and regular-paperfolding dyadic prefixes (n<=64) with certified bounds to n=1024*, published research record `2026/9/8/SCOPE079` (2026-09-08), https://github.com/published-finding corpus/2026/tree/main/2026/9/8/SCOPE079 . The searchable abstract was accessible, but the underlying complete artifact was not.
