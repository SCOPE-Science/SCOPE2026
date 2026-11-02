# One-switch permutation arches: exact shortest-absent spectra and sharp order extrema

## Finding

Fix a labeled alphabet \(\Sigma\) with \(q\ge 2\) symbols. Let \(P,Q\) be permutations of its symbols and let \(a,b\ge 1\) be integers. Write \(w=P^aQ^b\), concatenating \(a\) complete copies of \(P\) and \(b\) complete copies of \(Q\). A *scattered subsequence* of \(w\) is obtained by deleting arbitrary positions. A *shortest absent subsequence* (SAS) is a word absent as a scattered subsequence, of the smallest possible length.

Every SAS of \(w\) has length \(a+b+1\). Write \(p(c)\) and \(s(c)\) for the positions, numbered from \(1\), of \(c\in\Sigma\) inside \(P\) and \(Q\). A word \(x_1\cdots x_{a+b+1}\) is a SAS **if and only if**

\[
p(x_1)\ge p(x_2)\ge\cdots\ge p(x_{a+1})
\quad\text{and}\quad
s(x_{a+1})\ge s(x_{a+2})\ge\cdots\ge s(x_{a+b+1}).
\]

Thus its central symbol \(c=x_{a+1}\) is a pivot between two order-monotone pieces, and the exact number \(N_{P,Q}(a,b)\) of SAS words is

\[
\boxed{N_{P,Q}(a,b)=\sum_{c\in\Sigma}
\binom{a+q-p(c)}a\binom{b+s(c)-1}b.}
\]

For fixed \(P,a,b\), and among **all** permutations \(Q\), the unique minimizing choice is \(Q=P\), while the unique maximizing choice is \(Q=\operatorname{rev}(P)\). The sharp values are

\[
\boxed{N_{\min}(a,b,q)=\binom{a+b+q}{q-1}}
\quad\text{and}\quad
\boxed{N_{\max}(a,b,q)=\sum_{t=1}^q\binom{a+t-1}a\binom{b+t-1}b.}
\]

For fixed \(k=a+b\ge 2\), the latter maximum is uniquely achieved, up to interchanging \(a,b\), by \(a=\lfloor k/2\rfloor\) and \(b=\lceil k/2\rceil\). For fixed \(q\) and \(k\to\infty\), at the balanced maximizing split,

\[
N_{\max}\sim\frac{k^{2q-2}}{4^{q-1}((q-1)!)^2},
\qquad
N_{\min}\sim\frac{k^{q-1}}{(q-1)!}.
\]

One change of block ordering can therefore double the degree of polynomial growth of the shortest-absent spectrum: from \(q-1\) for uniform ordering to \(2q-2\) under a single reversal.

## Assumptions and scope

The alphabet is fixed and labeled; both permutation blocks contain **every** symbol exactly once. The exponent \(P^a\) means repetition of the full permutation word, not a group-theoretic power. The claim concerns distinct shortest absent **strings**, never the number of missing embeddings and never contiguous factors. All statements hold for every \(q\ge2\), every positive \(a,b\), and every pair \(P,Q\). The asymptotic statements keep \(q\) fixed and vary \(a+b\).

## Proof

**1. Shortest length.** Put \(k=a+b\). An arbitrary word of length \(k\) embeds in \(w\) by selecting its \(i\)-th letter from the \(i\)-th full permutation block, for \(1\le i\le k\). Every shorter word consequently embeds as well. In contrast, no word \(c^{k+1}\) embeds because the source contains exactly \(k\) occurrences of any letter \(c\). Hence the shortest absent length is exactly \(k+1\).

**2. Greedy permutation-block lemma.** Let \(R\) be a permutation of \(\Sigma\), and let \(v_1\cdots v_t\) be a nonempty target. Under leftmost greedy embedding in the infinite periodic word \(RRR\cdots\), the first letter occupies the first block, and the next target letter occupies the **same** block exactly when its \(R\)-rank is strictly greater than the previous letter's rank. Otherwise the match must advance to the next complete block. Induction therefore gives the exact block count

\[
1+\#\{i:1\le i<t,\ \operatorname{rank}_R(v_{i+1})\le \operatorname{rank}_R(v_i)\}.
\]

In particular, \(t\) target letters require all \(t\) blocks if and only if their ranks are weakly decreasing. They require at most \(t-1\) blocks if and only if at least one consecutive pair has strictly increasing ranks. This also holds when letters repeat: equality forces a new block.

**3. Characterization.** Suppose the first \(a+1\) symbols of a length-\(k+1\) target contain a strict increase in \(P\)-rank. By Step 2, that prefix fits into at most \(a\) full \(P\)-blocks, and the remaining \(b\) letters fit, one per block, in the \(Q^b\) suffix. Such a target is present. Likewise, if its last \(b+1\) symbols contain a strict increase in \(Q\)-rank, the first \(a\) letters fit one per \(P\)-block, and the last \(b+1\) letters fit into at most \(b\) \(Q\)-blocks; the target is present.

Conversely, assume both rank strings in the displayed criterion are weakly decreasing. Greedy matching of the first \(a\) letters consumes the \(a\) successive \(P\)-blocks (one symbol per block), because each next rank is no greater than the previous. The pivot \(x_{a+1}\) must therefore be matched within the first \(Q\)-block. From pivot onward, every next target symbol has no larger \(Q\)-rank, so greedy matching needs an additional \(Q\)-block at every step. Matching the pivot and the final \(b\) letters would require \(b+1\) \(Q\)-blocks, but only \(b\) exist. Since leftmost greedy subsequence matching succeeds whenever **any** embedding succeeds, this target is absent. The characterization follows.

**4. Exact count.** Fix the pivot \(c=x_{a+1}\). Its \(P\)-rank is \(p(c)\). The \(a\) symbols preceding it must be a weakly decreasing sequence with ranks drawn from the \(q-p(c)+1\) ranks at least \(p(c)\). By combinations with repetition, they have \(\binom{a+q-p(c)}a\) possibilities. Independently, the \(b\) symbols following it must be a weakly decreasing sequence with ranks among the first \(s(c)\) \(Q\)-ranks, contributing \(\binom{b+s(c)-1}b\) possibilities. Distinct pivot symbols give disjoint classes, proving the sum.

**5. Sharp extrema over second-block ordering.** Enumerate the symbols in increasing \(P\)-rank \(j=1,\ldots,q\). Put \(A_j=\binom{a+q-j}a\) and \(B_t=\binom{b+t-1}b\). Because \(a,b\ge1\), the \(A_j\) are strictly decreasing and the \(B_t\) are strictly increasing. Any permutation \(Q\) determines a permutation \(\sigma\) of \(1,\ldots,q\), sending \(j\) to the \(Q\)-rank of the symbol of \(P\)-rank \(j\). Our count is \(\sum_j A_jB_{\sigma(j)}\). The strict rearrangement inequality implies that this sum is uniquely smallest when \(\sigma(j)=j\) (so \(Q=P\)) and uniquely largest when \(\sigma(j)=q+1-j\) (so \(Q=\operatorname{rev}(P)\)).

In the minimum case, the sum equals \(\binom{a+b+q}{q-1}\) by Vandermonde convolution (equivalently, count a weakly decreasing length-\(a+b+1\) word on a \(q\)-letter ordered alphabet and separate at its unique marked position \(a+1\)). Reindexing \(t=q+1-j\) in the reversed case gives the maximum formula.

**6. Balanced split and asymptotics.** Write \(k=a+b\) and \(H_t(u)=\binom{u+t-1}u\). For \(b\ge a+2\) and \(t\ge2\),

\[
\frac{H_t(a+1)H_t(b-1)}{H_t(a)H_t(b)}
=\frac{(a+t)b}{(a+1)(b+t-1)}>1,
\]

because the numerator minus the denominator equals \((t-1)(b-a-1)>0\). For \(t=1\), the summands coincide. Thus transferring one unit from a longer phase to the shorter one strictly increases the maximum sum until the phase lengths differ by at most one. Symmetry in \(a,b\) proves precisely the asserted set of optimal lengths.

Finally, for each fixed \(t\) and large \(u\), \(H_t(u)\sim u^{t-1}/(t-1)!\). At balanced lengths, the \(t=q\) summand is of strictly higher polynomial degree than every \(t<q\) summand, giving the displayed asymptotic leading coefficient. Expanding the binomial expression for the minimum completes the proof.

## Verification

The standalone `verify.py` checks the word-embedding criterion against independent greedy subsequence membership for \(q=2,3,4\), all second permutations and \(1\le a,b\le3\); it also checks \(q=5\) and \(1\le a,b\le2\). In total it checks 768 parameter instances and 1,245,538 candidate strings. A separate dynamic set-of-subsequences constructor checks 56 small parameter instances without using the greedy criterion. It also checks strict rearrangement extrema at 12 parameter choices and balanced-split extrema at 441 choices across alphabet sizes \(2\) to \(10\). It prints:

`VERIFY_OK candidate_cases=768 candidate_patterns=1245538 independent_set_cases=56 strict_extrema_cases=12 balancing_cases=441`

Run with a standard Python 3 interpreter, `python verify.py`. These are finite tests; the preceding proof establishes the assertions for all permitted parameters.

## Relationship to prior work

The general concept of shortest absent scattered subsequences, characterization by arch factorizations, and permutation-block examples are studied in Kosche, Koß, Manea and Siemer [1]. Adamson and coauthors [2] establish global upper and lower bounds for absent subsequences, including highly structured block constructions. These sources explain why complete permutation arches are natural. Neither inspected source states the pivot characterization for an arbitrary one-time change \(P^aQ^b\), the rank-pair sum, its **unique conditional** order optimizers, or the balanced one-switch extremum. The general algorithms of [3] allow these counts to be computed instance by instance but do not supply the present closed all-parameter theorem. Standard greedy matching, combinations with repetition, Vandermonde's identity and the rearrangement inequality are classical tools and are not claimed as new.

## Limitations

The result applies specifically to a single transition between runs of repeated complete permutations; arbitrary word blocks, omitted symbols, multiple transitions and minimal absent subsequences of longer lengths are not classified. Existing general characterization theorems can in principle imply component pieces after specialization; the claimed contribution is the explicit unified exact formula, structural classification and sharp extremal analysis, not a novel greedy-embedding algorithm. An unlocated equivalent derivation in the wider absent-subsequence literature is an originality risk. Independent scientific audit has not been performed.

## References

[1] M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first public version 2021-08-31. https://arxiv.org/abs/2108.13968

[2] D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first public version 2024-07-26. https://arxiv.org/abs/2407.18599

[3] F. Manea et al., *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, 2025. https://arxiv.org/abs/2504.21471
