# Fibonacci length spectrum for minimal absent subsequences of doubled-run binary words

## Finding
For each integer \(r\ge1\), let \(w_r\) be the binary word with exactly \(r\) alternating constant-letter runs of length two, beginning with two zeros; thus \(w_1=00\), \(w_2=0011\), and \(w_3=001100\). A word is a *minimal absent subsequence* (MAS) of \(w_r\) if it is not a scattered subsequence of \(w_r\), but every proper scattered subsequence of it is.

Put \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For \(r\ge2\), the complete length distribution is
\[
\#\{u\in\operatorname{MAS}(w_r):|u|=\ell\}=\begin{cases}
F_r,&\ell=r,\\
2F_{r-1},&\ell=r+1,\\
F_{r-2},&\ell=r+2,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(r=1\), the MAS set is exactly \(\{1,000\}\). In particular, at **every** \(r\ge1\),
\[
\boxed{|\operatorname{MAS}(w_r)|=F_{r+2}.}
\]
Thus all MASs lie in at most three consecutive length layers, despite their total number growing exponentially with the number of doubled runs. A complete structural description is supplied below.

## Assumptions and scope
All subsequences are scattered: their letters must occur in source order but need not occupy consecutive positions. Minimality is under deletion of any nonempty set of candidate letters. It suffices to test all single-letter deletions, since subsequence containment is transitive. Candidates use precisely the binary alphabet \(\{0,1\}\). Empty candidates are never absent.

Represent a nonempty candidate as maximal constant-letter runs with lengths \(t_1,\ldots,t_m\). Let \(e(u)\) be the number of even run lengths, and let \(s(u)\) be \(1\) if its first letter is \(1\), and \(0\) otherwise. Define
\[
\Phi(u)=|u|-e(u)+s(u).
\]
For these words, \(u\) embeds into \(w_r\) **if and only if** \(\Phi(u)\le r\). This criterion covers all binary candidates and all \(r\ge1\).

## Proof
**Greedy embedding cost.** The source consists of alternating maximal blocks, each supplying two identical symbols. A candidate run of length \(t\) requires exactly \(\lceil t/2\rceil\) source blocks of its symbol; after completing that candidate run, the next candidate run starts with the next source block, whose symbol is opposite. The first required source block has index \(1+s(u)\). Thus the index of the last source block visited by the greedy leftmost embedding is
\[
1+s(u)+2\sum_{j=1}^{m}\bigl(\lceil t_j/2\rceil-1\bigr)+(m-1)
=|u|-e(u)+s(u)=\Phi(u).
\]
Greedy leftmost embedding is optimal for any subsequence, so the criterion follows.

**Minimality criterion.** Suppose \(u\) is a MAS. If one candidate run has even length, deleting a letter from that run makes it odd, reducing \(|u|\) and \(e(u)\) by one, so \(\Phi\) is unchanged. The shorter word would still be absent, a contradiction. Therefore every run of \(u\) has odd length.

When all runs are odd, deleting a letter in a run of length at least three reduces \(\Phi\) by two. Deleting an interior singleton run merges its two odd-length neighbors into one even-length run, also reducing \(\Phi\) by two. Deleting a first singleton run reduces \(\Phi\) by two if the word starts in \(1\), but leaves \(\Phi\) unchanged if it starts in \(0\). Deleting a final singleton reduces \(\Phi\) by one (unless this is also the first and only run, in which case the empty candidate embeds). Consequently, a MAS must start with a run of length at least three if it starts in \(0\), and it must satisfy
\[
\Phi(u)=r+1\quad\text{or}\quad
\bigl(\Phi(u)=r+2\ \text{and its final run has length at least three}\bigr).
\]
Conversely, each word satisfying these three run conditions (all runs odd; first run long if starting in \(0\); the displayed boundary condition) is absent by the greedy criterion, and every possible single-letter deletion reduces \(\Phi\) to at most \(r\). It is therefore a MAS. The singleton candidate \(u=1\) is also covered, with its deletion the empty word.

**Exact enumeration.** Let \(C_n\) count compositions of \(n\ge1\) into positive odd parts. Their ordinary generating function is
\[
\sum_{n\ge1}C_nz^n=\frac{z}{1-z-z^2},
\]
so \(C_n=F_n\). The first-part-long or last-part-long odd compositions have generating function \(z^3/(1-z-z^2)\); their count at size \(n\ge3\) is \(F_{n-2}\). Those with both first and last parts long have generating function
\[
\frac{z^3}{1-z^2}+\frac{z^6}{(1-z^2)(1-z-z^2)}
=\frac{z^3(1-z)}{1-z-z^2}.
\]
Here the first term accounts for a single long run, which simultaneously qualifies as both first and last. For sizes \(n\ge4\), the resulting coefficient is \(F_{n-4}\); at size three it is one.

For \(r\ge2\), the MAS candidates split disjointly as follows:

* Starting in \(1\) at length \(r\): all odd-part compositions, giving \(F_r\).
* Starting in \(1\) at length \(r+1\): the last part must be long, giving \(F_{r-1}\).
* Starting in \(0\) at length \(r+1\): the first part must be long, again giving \(F_{r-1}\).
* Starting in \(0\) at length \(r+2\): both end parts must be long, giving \(F_{r-2}\).

All remaining candidates violate the minimality criterion. Combining the four cases proves the length spectrum and total
\[
F_r+2F_{r-1}+F_{r-2}=F_{r+2}.
\]
The base case \(w_1=00\) has MASs \(1\) and \(000\), so the total formula remains valid for \(r=1\).

## Verification
The all-parameter theorem follows from the greedy embedding and odd-run counting arguments, not finite experiments. A standalone program, `verify.py`, independently tests subsequence containment by direct left-to-right scanning; compares the structural minimality criterion against every binary candidate through length \(2r+1\) for \(1\le r\le8\); checks the three exact length layers; and separately validates the greedy cost on bounded candidates for \(1\le r\le12\). Its recorded output is in `verification_output.txt`. The test comprises 412,292 exact word-level comparisons.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer, *Absent Subsequences in Words* (2021 preprint; published 2023), prove a general MAS characterization and exhibit exponentially many MASs in a larger-alphabet periodic construction. Their Section 3 example \(B_k\) is a repetition of an increasing permutation over an alphabet of size at least four, rather than the binary doubled-run family here; their result is an exponential lower bound, not this exact length distribution.

Manea, Ringleb, Siemer, and Winkler (2025) give asymptotically optimal algorithms to enumerate MASs and find a longest MAS. Their enumeration framework applies to any input, including \(w_r\), but the inspected results do not derive a closed Fibonacci count, a three-layer spectrum, or the odd-run structural classification for this family. A separate published Fibonacci extremal result concerns **shortest** absent subsequences, not all minimal absent subsequences and not this source-word family. Troníček (2023) gives an automaton for counting MASs in arbitrary words; only its abstract was accessible for this comparison, so it remains a specifically named priority risk rather than evidence of equivalent coverage.

## Limitations
The result treats only alternating binary runs of length **exactly two**, with the first block equal to \(00\); exchanging zero and one gives the complemented family immediately. It does not establish a count for unequal run lengths, other alphabets, or all binary words of a given length. Publication priority beyond inspected indexed literature is not independently certified.

## References
1. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, originally submitted 31 August 2021; *Fundamenta Informaticae* 189 (2023), 199–240. https://arxiv.org/abs/2108.13968
2. F. Manea, T. Ringleb, S. Siemer and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471v1, submitted 30 April 2025. https://arxiv.org/abs/2504.21471
3. Z. Troníček, *On Problems Related to Absent Subsequences*, COCOA (2) 2023, 351–363. DOI: 10.1007/978-3-031-49614-1_26. Abstract accessible; full text not inspected.
