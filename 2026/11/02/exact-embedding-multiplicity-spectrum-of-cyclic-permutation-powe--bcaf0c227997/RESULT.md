# Exact embedding-multiplicity spectrum of cyclic permutation powers

## Finding

Let \(q\ge2\) and \(k\ge1\). In the repeated alphabet word
\[
W_{q,k}=(0\,1\,\cdots\,(q-1))^k,
\]
write \(E_{q,k}(u)\) for the number of distinct increasing positional embeddings of a nonempty target \(u=u_1\cdots u_m\). Put
\[
d(u)=\#\{i:1\le i<m,\ u_i\ge u_{i+1}\}.
\]
**Complete multiplicity law.** For every such target,
\[
E_{q,k}(u)=
\begin{cases}
\displaystyle\binom{k+m-1-d(u)}{m},&d(u)\le k-1,\\
0,&d(u)\ge k.
\end{cases}
\]
The exact number of target words with weak-descent statistic \(d\) is
\[
N_q(m,d)=\sum_{i=0}^{d}(-1)^i\binom{m+1}{i}\binom{q(d+1-i)}{m},
\]
with \(\binom{a}{m}=0\) whenever \(a<m\) or \(a<0\). Its bivariate generating function is
\[
\sum_{m\ge1}\sum_{d\ge0}N_q(m,d)x^mt^d
=\frac{(1+(1-t)x)^q-1}{1-t(1+(1-t)x)^q}.
\]
In particular \(N_q(m,d)>0\) if and only if
\[
\left\lfloor\frac{m-1}{q}\right\rfloor\le d\le m-1.
\]
Thus the entire **positive** embedding-multiplicity spectrum at length \(m\) has one value for every integer \(d\) between \(\lfloor(m-1)/q\rfloor\) and \(\min(k-1,m-1)\). Its exact cardinality is
\[
\min(k,m)-\left\lfloor\frac{m-1}{q}\right\rfloor.
\]
The value at \(d\) is \(\binom{k+m-1-d}{m}\) and its frequency is \(N_q(m,d)\). All these values are distinct. The maximum multiplicity is \(\binom{k+m-1-\lfloor(m-1)/q\rfloor}{m}\), and the minimum positive multiplicity is \(\binom{k}{m}\) if \(m<k\), otherwise \(1\).

If a random deletion chooses uniformly one of the \(\binom{qk}{m}\) position sets, every output word \(u\) has probability \(E_{q,k}(u)/\binom{qk}{m}\). The stated histogram is therefore also the **complete probability spectrum** of this finite deletion channel.

## Assumptions and scope

All alphabets are ordered and all parameters are integers. The alphabet is exactly \(\{0,1,\ldots,q-1\}\), the host consists of exactly \(k\) complete increasing periods, and \(1\le m\le qk\). An embedding counts an increasing tuple of positions; two tuples yielding the same word are counted separately. Values at \(m>qk\) are identically zero. The empty target is excluded from the theorem (it has exactly one embedding by convention). The formula specializes correctly to \(k=1\) and includes repeated target letters.

## Proof

**Step 1: block-index bijection.** Index the host's \(k\) permutation blocks by \(0,\ldots,k-1\). An embedding of \(u\) corresponds bijectively to integers \(0\le j_1,\ldots,j_m\le k-1\) naming the blocks containing the selected letters. Because each letter occurs exactly once per block, the selected positions increase if and only if
\[
j_{i+1}-j_i\ge\mathbf1_{\{u_i\ge u_{i+1}\}},\qquad 1\le i<m.
\]
Define nonnegative slacks
\[
s_0=j_1,\quad
s_i=j_{i+1}-j_i-\mathbf1_{\{u_i\ge u_{i+1}\}}\ (1\le i<m),
\quad s_m=k-1-j_m.
\]
They sum to \(k-1-d(u)\). Conversely, every weak composition of that number into \(m+1\) nonnegative parts reconstructs the unique block-index embedding by the same equations. When the sum is negative no embedding exists. Otherwise stars and bars gives \(\binom{k+m-1-d(u)}{m}\). This proves the multiplicity formula, including all boundary cases.

**Step 2: weak-descent enumeration.** Every length-\(m\) word with exactly \(d\) weak descents may be divided into strictly increasing nonempty blocks by cutting at all weak descents and at any subset of its \(m-1-d\) strict rises. If a decomposition has exactly \(j\) blocks, there are \(\binom{m-1-d}{j-1-d}\) choices of its additional cuts. A strictly increasing nonempty alphabet block has ordinary length generating function \(R(x)=(1+x)^q-1\), hence all \(j\)-block sequences have generating function \(R(x)^j\). The double count therefore yields
\[
R(x)^j=\sum_{m\ge1}\sum_{d\ge0}N_q(m,d)
\binom{m-1-d}{j-1-d}x^m.
\]
Multiply by \(y^{j-1}\) and sum over \(j\ge1\). With \(t=y/(1+y)\), then replacing \(x\) by \((1-t)x\), direct algebra gives
\[
\sum_{m,d}N_q(m,d)x^mt^d
=\frac{R((1-t)x)}{1-t-tR((1-t)x)}
=\frac{(1+(1-t)x)^q-1}{1-t(1+(1-t)x)^q}.
\]
For \(m\ge1\), its coefficient in \(x\) is
\[
\frac{(1-t)^{m+1}}t\sum_{j\ge1}\binom{qj}{m}t^j.
\]
Expanding the first factor by the binomial theorem yields the stated finite alternating sum for \(N_q(m,d)\).

**Step 3: no missing values in the spectrum.** Every strictly increasing consecutive segment has length at most \(q\), so a word of length \(m\) needs at least \(\lceil m/q\rceil\) such segments and thus at least \(\lceil m/q\rceil-1=\lfloor(m-1)/q\rfloor\) weak descents. The trivial upper bound is \(m-1\). For any intermediate \(d\), choose \(d+1\) positive segment lengths at most \(q\) summing to \(m\); such a bounded composition exists precisely when \(d+1\le m\le q(d+1)\). Concatenate for each segment the increasing word starting at zero of the chosen length. Each junction is a weak descent, and no interior position is, so this construction realizes exactly \(d\).

**Step 4: distinct values and normalization.** As \(d\) ranges over the nonempty spectrum, the upper parameter \(k+m-1-d\) in the binomial coefficient decreases by one while remaining at least \(m\). Therefore the positive multiplicities decrease strictly. Their frequencies are \(N_q(m,d)\), established above. Counting the integer range gives \(\min(k,m)-\lfloor(m-1)/q\rfloor\) positive values. The endpoints give the extrema. Finally, every length-\(m\) position subset produces exactly one word, so
\[
\sum_{d=0}^{\min(k-1,m-1)}N_q(m,d)
\binom{k+m-1-d}{m}=\binom{qk}{m}.
\]
This proves the exact deletion-output probability interpretation.

## Verification

Run `python3 verify_cyclic_subsequence_multiplicity.py` from this package. The script enumerates every positional embedding independently of the theorem for 16 small hosts, compares all literal target multiplicities and positive histograms, and checks larger exact coefficient identities and normalization. Its observed output begins `VERIFY_OK literal_hosts= 16 distinct_targets= 9287 histogram_bins= 380 absent_degree_checks= 272 formal_positive_coefficients= 52318`. These finite tests corroborate, but do not substitute for, the unrestricted combinatorial bijections in the proof.

## Relationship to prior work

Flaxman, Harrow and Sorkin (2004) proved that alphabet-cycling words maximize the *number of distinct subsequences* at each length, with a corresponding bivariate generating function. This gives the support size of the histogram, not individual positional multiplicities or the distribution of those multiplicities. Kosche, Koß, Manea and Siemer (first public preprint 2021) study absent, minimal absent, and shortest absent subsequences via arch factorization; their results describe which subsequences are missing rather than the positive embedding-count spectrum. Leroy, Rigo and Stipulanti (2017) develop general binomial coefficients of words; the present formula specializes that general notion to a complete, finite-block multiplicity histogram. The weak-descent enumeration is a classical Eulerian-type identity; it is proved here for self-containment rather than claimed as an independently novel identity. The specific all-parameter multiplicity spectrum and its probability interpretation are the contribution assessed here.

## Limitations

The host must be a complete repetition of one strictly increasing alphabet permutation. Arbitrary periodic words, truncated periods and nonuniform per-symbol occurrence counts are outside scope. This result does not determine the embedding histogram under biased deletions or characterize optimality among all source words. Finite software checks are not infinite proofs. Although inspected sources and database searches did not identify an equivalent exact histogram, a previously published specialization in classical \(P\)-partition or word-binomial literature remains possible; no independent assessment has been completed.

## References

1. A. Flaxman, A. W. Harrow and G. B. Sorkin, *Strings with maximally many distinct subsequences and substrings*, Electronic Journal of Combinatorics **11** (2004), R8. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r8/pdf
2. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public August 31, 2021), https://arxiv.org/abs/2108.13968
3. J. Leroy, M. Rigo and M. Stipulanti, *Generalized Pascal triangle for binomial coefficients of words*, arXiv:1705.08270 (2017), https://arxiv.org/abs/1705.08270
