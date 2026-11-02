# Dense Johnson super-coupon cover times are iterated coupon-collector epochs

## Finding

Let an observed subset of size \(n-k\) evolve by replacing one uniformly selected observed element with one uniformly selected unobserved element at each update. Every \(s\)-subset contained in an observed set is counted as collected. With \(T_{n,k,s}\) the number of updates until all \(s\)-subsets are collected, define \(C_k\) as the time to see every one of \(k\) equally likely types in independent draws, and let \(C_k^{(1)},\dots,C_k^{(s)}\) be independent copies. Write
\[
T^*_{k,s}=\sum_{a=1}^s C_k^{(a)}.
\]
For every \(n\ge k+s\), there is a coupling in which \(T_{n,k,s}\ge T^*_{k,s}\) almost surely and
\[
\Pr(T_{n,k,s}\ne T^*_{k,s})\le
\frac{\mathbb E[T^*_{k,s}(T^*_{k,s}-1)]}{2(n-k)}.
\]
Consequently, for fixed positive integers \(k,s\), the total-variation distance tends to zero as \(n\to\infty\), and
\[
\lim_{n\to\infty}\mathbb E T_{n,k,s}=s k H_k.
\]
Here \(H_k=\sum_{j=1}^k j^{-1}\) is the \(k\)-th harmonic number. More precisely, \(0\le \mathbb E T_{n,k,s}-s kH_k=O_{k,s}(n^{-1})\). The limiting probability-generating function is
\[
\mathbb E z^{T^*_{k,s}}
=\prod_{j=1}^{k}\left(\frac{(j/k)z}{1-(1-j/k)z}\right)^{s}.
\]
For every fixed \(s\ge1\), if \(k=k(n)\to\infty\) with \(k^2(\log k)^2=o(n)\), then
\[
\frac{T_{n,k,s}-sk\log k}{k}\ \Longrightarrow\
G_1+\cdots+G_s,
\]
where \(G_1,\ldots,G_s\) are independent standard Gumbel random variables. For \(s\ge2\), this is a genuine sum-of-Gumbels law rather than a single classical Gumbel law.

## Assumptions and scope

The ground set is \([n]=\{1,\ldots,n\}\). Fix integers \(n,k,s\) satisfying \(k\ge1\), \(s\ge1\), and \(k+s\le n\). Start from any deterministic observed \((n-k)\)-subset \(R_0\); the distribution of the cover time does not depend on that choice by permutation symmetry. At each integer update \(t\ge1\), independently select one uniformly distributed element of \(R_{t-1}\) to remove and one uniformly distributed element of \([n]\setminus R_{t-1}\) to insert. The selected elements are drawn from the *old*, pre-update sets, so the update is a genuine exchange. Collect all \(s\)-subsets contained in any \(R_u\), \(0\le u\le t\). Define \(T_{n,k,s}\) as the minimum \(t\ge0\) for which all \(\binom ns\) targets have appeared.

Equivalently, put \(A_t=[n]\setminus R_t\), a size-\(k\) set of omitted labels. A target \(B\) is not collected through update \(t\) exactly when \(B\cap A_u\ne\varnothing\) for *every* \(u\in\{0,\ldots,t\}\). Thus completion is equivalent to the minimum transversal of the omitted-set history having size strictly greater than \(s\). The number of updates, rather than the number of visited sets, is the time unit.

## Proof

**1. Independent omission slots.** Give the \(k\) elements of \(A_0\) distinct slots. At every exchange choose an independent uniform index \(J_t\in[k]\) and replace the omitted label in that slot by an element chosen uniformly from the old observed set \([n]\setminus A_{t-1}\). This exactly reproduces the complement of the original Markov chain, since the inserted observed label is a uniformly chosen omitted label. Indices \((J_t)_{t\ge1}\) are i.i.d. uniform independently of the choices of new labels.

**2. Fresh-label process and an interval-cover identity.** Construct an ideal process using the same slot indices but assigning a new, never previously used formal label whenever a slot is selected. A formal label has a single consecutive interval of times during which it belongs to the ideal omitted set, from its assignment to just before the next replacement of its slot. A transversal of the ideal omitted sets through time \(t\) is precisely a collection of label-lifespan intervals whose union covers every integer time from \(0\) through \(t\).

For intervals on a line, the usual farthest-right-endpoint greedy algorithm minimizes the number needed to cover a consecutive sequence of times: among intervals containing the first uncovered time, select one ending last, and repeat. In the ideal omission process, the chosen interval at time \(0\) ends just before the *last* of the \(k\) slots is selected for the first time; call the corresponding selection time \(M_1\). The next greedy interval starts at \(M_1\) and ends immediately before the last first selection of the slots after \(M_1\); recursively define \(M_a\) as the ending time of the \(a\)-th complete coupon-collection epoch. This proves that the minimum transversal size through time \(t\) exceeds \(s\) if and only if \(t\ge M_s\). Every slot-index epoch is an independent classical collector on \(k\) equiprobable types, hence
\[
T^*_{k,s}=M_s=\sum_{a=1}^s C_k^{(a)}.
\]
The standard decomposition of \(C_k\) into independent geometric waiting times with parameters \(j/k\), \(1\le j\le k\), proves the displayed probability-generating function and \(\mathbb E T^*_{k,s}=skH_k\). It also gives
\[
\mathbb E[T^*_{k,s}(T^*_{k,s}-1)]
=s^2 k^2 H_k^2+sk^2 H_k^{(2)}-2skH_k,
\quad H_k^{(2)}=\sum_{j=1}^k j^{-2}.
\]

**3. Coupling and collision estimate.** Whenever a new formal label appears, associate it with the actual newly omitted label drawn in the finite process. Identifications are allowed when finite labels recur. If a set of at most \(s\) formal labels hits *all* ideal omitted sets, its image of at most \(s\) actual labels hits all corresponding actual omitted sets. Thus lack of ideal coverage entails lack of actual coverage, pathwise, and \(T_{n,k,s}\ge T^*_{k,s}\).

Until a finite label recurs, the ideal-to-actual map is injective on all labels used so far. Before update \(j\), at most \(j-1\) formerly omitted labels have already departed from the omitted set and could be drawn again. The new finite omitted label is uniform among \(n-k\) currently observed labels. Thus the conditional probability of first recurrence at update \(j\), given none earlier, is at most \((j-1)/(n-k)\). A union bound through an independent slot-driven stopping time \(T^*_{k,s}\) gives
\[
\Pr(\text{recurrence by }T^*_{k,s})
\le\frac{1}{n-k}\mathbb E\sum_{j=1}^{T^*_{k,s}}(j-1)
=\frac{\mathbb E[T^*_{k,s}(T^*_{k,s}-1)]}{2(n-k)}.
\]
Without a recurrence the ideal and actual omitted-set histories are isomorphic as incidence patterns, so their completion times agree. The coupling inequality for total variation follows.

**4. Expected-time control.** For fixed \(k,s\), let \(L=sk\) and assume \(n-k\ge2L\). From *any* omitted set, prescribe the next \(L\) slot indices as \(1,2,\ldots,k\), repeated \(s\) times, and require each newly omitted finite label to be unused earlier in this block. The prescribed slot sequence has probability \(k^{-L}\); at each step the conditional chance of a previously unused label is at least \(1-(L-1)/(n-k)\ge1/2\). The block therefore succeeds with probability at least \(p=(2k)^{-L}\). The same interval-cover argument proves that it collects every target, regardless of the earlier history. By repeated blocks and the strong Markov property, the expected remaining time to completion from every state is at most \(L/p\). Coupling at time \(T^*_{k,s}\) now gives
\[
0\le\mathbb E(T_{n,k,s}-T^*_{k,s})
\le \frac{L}{p}\frac{\mathbb E[T^*_{k,s}(T^*_{k,s}-1)]}{2(n-k)},
\]
which is \(O_{k,s}(n^{-1})\).

**5. Growing omitted-set size.** For fixed \(s\), the second factorial moment above is \(O_s(k^2(\log k)^2)\). The stated growth assumption makes the coupling discrepancy vanish. The classical coupon-collector limit \((C_k-k\log k)/k\Rightarrow G\), together with independence of the \(s\) epochs and Slutsky's theorem, gives the sum-of-Gumbels limit for the finite Johnson walk.

## Verification

The standalone \(\texttt{CHECK.py}\) implements two independent finite checks: an exhaustive enumeration of slot-index words for small \(k\) and \(s\) comparing the exact ideal omission-history transversal with the complete-epoch criterion, and seeded finite-label sample paths verifying that actual completion cannot precede the ideal epoch clock. Both use direct subsets, without substituting a coupon-epoch formula for the target condition. Execute \(\texttt{python CHECK.py}\) with Python 3 standard library. Successful replay reports \(\texttt{FRESH_EQUIVALENCE_OK 11400}\) and \(\texttt{FINITE_MONOTONE_OK 144000}\). These are finite diagnostic checks; the line-interval greedy argument, coupling and residual-time estimate establish the general theorem.

## Relationship to prior work

Athreya, Mukherjee and Mukherjee introduce super-coupon coverage under independent and temporally dependent subset draws, including the single-swap Johnson walk. Their fixed-parameter coverage questions and fixed-\(r\) asymptotics do not imply the near-census regime \(r=n-k\). This theorem resolves an opposite limit where almost every element is observed on every step. Prior fixed-\(r\) Gumbel theorems concern a different parameter regime and are not contradicted. The mechanism here is an interval-transversal description of the *omitted* rather than observed labels, which reveals independent full rounds of a \(k\)-type collector.

## Limitations

The stated total-variation bound controls the dense regime and is not intended for a fixed small observed-set size. The \(O(n^{-1})\) expected-time estimate holds for fixed \(k,s\); when \(k\) grows, the conclusion supplied here is distributional under \(k^2(\log k)^2=o(n)\), without a matching uniform expected-time estimate. Nothing here settles the fixed-\(r\), \(n\to\infty\) Markovian super-coupon conjecture. A complete assessment of historical priority may require additional sources.

## References

1. S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, arXiv:2304.01145 (first public preprint 2023-04-03); *Journal of Theoretical Probability* 38 (2025), article 54, doi:10.1007/s10959-025-01417-w. https://arxiv.org/abs/2304.01145 ; https://doi.org/10.1007/s10959-025-01417-w
2. Classical coupon-collector decomposition, geometric waiting times, and Gumbel limit; standard elementary facts used and explicitly identified above.
