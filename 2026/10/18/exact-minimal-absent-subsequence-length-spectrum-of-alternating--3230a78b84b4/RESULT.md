# Exact minimal absent-subsequence length spectrum of alternating binary blocks

## Finding

For every integer \(k\geq 1\), let \(B_k=(01)^k\) be the binary word of length \(2k\). A *scattered subsequence* of \(B_k\) is obtained by deleting arbitrary positions without changing the order of those retained. A binary word \(u\) is a *minimal absent subsequence* (MAS) if it is not a scattered subsequence of \(B_k\), but every proper scattered subsequence of \(u\) is present in \(B_k\).

Let \(M_k(m)\) count the distinct MAS of length \(m\). For all integers \(j\geq 1\),

\[
\boxed{M_k(k+j)=\binom{k+3-j}{2j-1}},
\]

where \(\binom{r}{s}=0\) when \(s<0\) or \(r<s\), and there are no MAS of length at most \(k\). In particular, the possible MAS lengths are exactly

\[
 k+1, k+2,\ldots, k+\left\lfloor\frac{k+4}{3}\right\rfloor.
\]

The number of *shortest* absent subsequences is \(k+2\), whereas the total number of MAS is

\[
 T_k=\sum_{j=1}^{\lfloor(k+4)/3\rfloor}\binom{k+3-j}{2j-1}.
\]

The ordinary generating function and recurrence are

\[
\sum_{k\geq1}T_k z^k=\frac{3z-z^2+2z^3}{1-2z+z^2-z^3},\qquad
T_k=2T_{k-1}-T_{k-2}+T_{k-3}\quad(k\geq4),
\]

with \((T_1,T_2,T_3)=(3,5,9)\). In particular, \(T_k=\Theta(\rho^k)\), where \(\rho\approx1.754877666\) is the unique real root greater than one of \(\rho^3-2\rho^2+\rho-1=0\). Thus this canonical binary \(k\)-universal word has only linearly many shortest absent subsequences, but exponentially many minimal absent subsequences.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The word \(B_k\) is **linear**, not cyclic, and all subsequences are scattered rather than contiguous. Distinct absent words are counted once each, regardless of their hypothetical embeddings. The statements hold for every integer \(k\geq1\) and use no asymptotic assumption. A minimal absent subsequence is equivalently absent with every *single-letter deletion* present: if a shorter proper subsequence were absent, it would lie inside one of those single deletions, contradicting downward closure of the present-subsequence set.

Every binary word of length at most \(k\) embeds into \(B_k\), by using at most one selected position in each `01` block. Hence all MAS have length \(m\geq k+1\).

## Proof

**Greedy embedding position.** Let \(u=u_1\cdots u_m\) be nonempty, let \(a=u_1\in\{0,1\}\), and let \(E(u)\) count indices \(1\leq i<m\) for which \(u_i=u_{i+1}\). Match \(u\) greedily to the *infinite* word `010101...`, beginning at its first occurrence of \(a\). The first matched position is \(1+a\). Each subsequent match advances one position for unequal neighboring bits and two for equal neighbors. Thus the final matched position is

\[
 P(u)=1+a+(m-1)+E(u)=m+a+E(u).
\]

Greediness minimizes the last matched position. Consequently,

\[
 u\text{ is a subsequence of }B_k\quad\Longleftrightarrow\quad P(u)\leq2k.
\tag{1}
\]

**Deletion costs.** For \(m\geq2\), write \(\Delta_i=P(u)-P(u\setminus u_i)\), deleting position \(i\). A direct comparison of the greedy-position formula gives:

* \(\Delta_1=0\) precisely when the first two bits are `01`; otherwise \(\Delta_1=2\).
* For \(1<i<m\), \(\Delta_i=0\) precisely when the neighboring triple is `010` or `101`; otherwise \(\Delta_i=2\).
* \(\Delta_m=1\) when the final two bits differ, and \(\Delta_m=2\) when they are equal.

For example, at an interior position the difference is

\[
\Delta_i=1+[u_{i-1}=u_i]+[u_i=u_{i+1}]-[u_{i-1}=u_{i+1}],
\]

where brackets are indicators; the binary alphabet forces this to be zero or two. In particular, every deletion decreases \(P\) by at most two. From (1), a word is an MAS exactly when \(P(u)>2k\) but \(P(u)-\Delta_i\leq2k\) for every \(i\). Therefore \(P(u)\) is either \(2k+1\) or \(2k+2\).

When \(P=2k+1\), every \(\Delta_i\) must be positive: the word cannot start in `01`, and no internal run can have length one. Its final run may have length one. When \(P=2k+2\), every \(\Delta_i=2\): in addition, its last run must have length at least two. These conditions are jointly necessary **and sufficient**.

**Run compositions.** Let \(R\) denote the number of maximal constant-letter runs of \(u\). Since \(E(u)=m-R\),

\[
P(u)=2m-R+a.
\tag{2}
\]

Write \(m=k+j\), where \(j\geq1\), and put \(H=m-2j+1\). The four mutually exclusive possibilities are counted by compositions of \(m\) into \(R\) positive run lengths, with the lower bounds described above:

| Greedy endpoint | First bit | Run count \(R\) | Number of eligible run compositions |
|---|---:|---:|---:|
| \(2k+1\) | 0 | \(2j-1\) | \(\binom{H}{2j-2}\) |
| \(2k+1\) | 1 | \(2j\) | \(\binom{H}{2j-1}\) |
| \(2k+2\) | 0 | \(2j-2\) | \(\binom{H}{2j-3}\) |
| \(2k+2\) | 1 | \(2j-1\) | \(\binom{H}{2j-2}\) |

Here any row with an impossible nonpositive run count contributes zero. In the first and third rows, the first run must have length at least two (unless it is also the only run, in which case \(m\geq2\) already ensures this). In the first two rows, interior runs must have length at least two but the last may be a singleton; in the last two, the final run must have length at least two. The second and fourth rows permit a singleton initial run. Subtracting these mandatory lengths and distributing the remaining positions among the runs gives the displayed binomial coefficients by stars and bars. For the one-run boundary cases \(j=1\), the compositions are the words of \(k+1\) identical zeros and of \(k+1\) identical ones, both directly eligible, and the same binomial conventions give their contributions correctly.

Pascal's identity twice now yields

\[
M_k(k+j)=2\binom{H}{2j-2}+\binom{H}{2j-1}+\binom{H}{2j-3}
=\binom{H+2}{2j-1}=\binom{k+3-j}{2j-1}.
\]

The binomial coefficient is positive exactly when \(k+3-j\geq 2j-1\), or \(j\leq\lfloor(k+4)/3\rfloor\). This proves the exact spectrum, the largest length, and the shortest-layer count.

**Total and growth.** For \(j=1\), the coefficient is \(k+2\). For each \(j\geq2\), the smallest allowed \(k\) is \(3j-4\), and the binomial generating identity gives

\[
\sum_{k\geq 3j-4}\binom{k+3-j}{2j-1}z^k
=\frac{z^{3j-4}}{(1-z)^{2j}}.
\]

Summing the geometric series over \(j\geq2\), and adding the \(j=1\) contribution, gives

\[
\sum_{k\geq1}T_kz^k
=\frac{z(3-2z)}{(1-z)^2}
+\frac{z^2}{(1-z)^2((1-z)^2-z^3)}
=\frac{3z-z^2+2z^3}{1-2z+z^2-z^3}.
\]

Coefficient comparison gives the recurrence. The denominator has one positive simple zero at \(z=1/\rho\), with its two other zeros having greater modulus, and its numerator does not vanish there; hence \(T_k=\Theta(\rho^k)\). This completes the proof.

## Verification

The accompanying standalone `verify.py` uses a separate method: it constructs all subsequences of the finite word `01` repeated \(k\) times and tests candidate absent words by direct greedy searches in that finite text. For each \(k=1,\ldots,12\), it checks every single-letter deletion of each candidate, and compares the independently obtained full MAS length histogram with the formula. It also checks the rational-generating-function recurrence for \(1\leq k\leq 50\). Run with `python3 verify.py`; no external packages are required.

The first twelve exact totals are \(3,5,9,16,28,49,86,151,265,465,816,1432\). Finite testing corroborates the formulas; the proof above independently covers every \(k\geq1\).

## Relationship to prior work

Kosche, Koß, Manea and Siemer introduced the MAS/SAS distinction, characterized minimal absent subsequences and studied the repeated-permutation family in *Absent Subsequences in Words* (arXiv:2108.13968, Section 3). Their exponential-separation construction assumes a fixed even alphabet of size at least four and does not state the binary exact spectrum. Our result determines every length layer for its binary counterpart; the general definition and relevant idea of studying permutation powers are credited to them.

Adamson and collaborators study the numbers of all present and absent subsequences at fixed length, including extremal arch structures (arXiv:2407.18599, Theorem 2). This concerns the full set of absent words, not its subsequence-minimal elements, so it does not imply the binomial spectrum here. Manea, Ringleb, Siemer and Winkler provide algorithms for enumerating MAS and finding a longest MAS for arbitrary input (arXiv:2504.21471); their general algorithms do not assert this binary-family closed form. A prior result about *shortest* absent subsequences alone also does not determine all *minimal* absent subsequences. Formal database and primary-literature checks did not reveal an equivalent formula, but cannot exclude all unindexed equivalents.

## Limitations

The formula applies only to the repeated two-letter permutation `01` and its images under global alphabet swapping. No statement is proved for nonbinary permutation powers, arbitrary binary words, circular words, or contiguous minimal absent factors. The exponential estimate is asymptotic, with the exact finite counts given by the binomial sum. No independent external mathematical audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public 2021-08-31), especially Section 3, Proposition 3.6. https://arxiv.org/abs/2108.13968
2. D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (2024), especially Theorem 2. https://arxiv.org/abs/2407.18599
3. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025), especially Sections 1–3. https://arxiv.org/abs/2504.21471
