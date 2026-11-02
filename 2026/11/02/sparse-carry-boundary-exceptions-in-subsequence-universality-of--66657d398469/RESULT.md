# Sparse carry-boundary exceptions in subsequence universality of Baum–Sweet prefixes

## Finding

Let \(b_0=1\). For \(j\ge1\), let \(b_j=1\) exactly when **all maximal blocks of zeros in the ordinary binary expansion of** \(j\) **have even length**, and otherwise let \(b_j=0\). Write \(B_N=b_0b_1\cdots b_{N-1}\), \(S(N)=\sum_{j=0}^{N-1}b_j\), for integer \(N\ge6\). A *scattered subsequence* keeps its selected indices in increasing order; it need not be contiguous. Its binary *universality index* \(\iota(w)\) is the largest integer \(r\) for which **every** binary word of length \(r\) occurs as a scattered subsequence of \(w\).

**Theorem.** For every integer \(N\ge6\),
\[
\boxed{\iota(B_N)=S(N)-2-\mathbf1_{\{N=4^t+1\text{ for some integer }t\ge2\}}.}
\]
In particular, with Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), every integer \(k\ge3\) satisfies
\[
\boxed{\iota(B_{2^k})=F_{k+2}-2.}
\]
The exceptional prefix lengths are exactly \(17,65,257,1025,\ldots\); at each such length, a newly read \(1\) has not yet finished a two-symbol-covering arch. The results concern the binary alphabet, even if one of its symbols is very rare.

## Assumptions and scope

An *arch* is the shortest nonempty prefix of the remaining unprocessed word containing both \(0\) and \(1\). Greedily remove complete arches until the remainder lacks at least one symbol. Empty remainder is permitted. All claims about binary expansions refer to the canonical expansion with no leading zeros, with \(b_0=1\) specified separately. Positions in the proof are zero-based. No assertion is made about factors beginning at arbitrary indices or about all shortest absent subsequence strings.

## Proof

**Step 1: exact adjacent-one locations.** We first prove
\[
 b_jb_{j+1}=11\quad\Longleftrightarrow\quad j=4^t-1\text{ for some integer }t\ge0.
\]
For \(j=0\), both digits equal \(1\), giving \(t=0\). If \(j>0\) is even with \(b_j=1\), its final block of zeros has positive even length \(2a\), where \(a\ge1\). Incrementing \(j\) turns that block into \(0^{2a-1}1\), creating an odd zero block; therefore \(b_{j+1}=0\). If \(j\) is odd, let \(1^h\) be its terminal block of ones. If it is preceded by a zero, then for \(b_j=1\) that zero belongs to an even-length zero block. Incrementing shortens that block by one, making it odd, so \(b_{j+1}=0\). Otherwise the expansion of \(j\) consists entirely of \(h\) ones and \(j+1=2^h\); this latter digit is \(1\) exactly when \(h\) is even. Hence the displayed characterization. It follows that \(111\) never occurs. Moreover, immediately after each pair at \(j=4^t-1\) with \(t\ge1\) are two zeros: \(b_{4^t+1}=0\) because the binary expansion has an internal odd block \(0^{2t-1}\), and \(b_{4^t+2}=0\) because its last zero run has length one.

**Step 2: the exact arch structure at every prefix.** The infinite word begins \(1101100\). Thus the first six characters are exactly two greedily completed arches \(110\,|\,110\), consuming four ones, followed by a zero. From there, proceed left to right. An arch starting with a zero consists of a positive run of zeros followed by its first one, hence contains exactly one one. If that finishing one is immediately followed by another one, the adjacent-one characterization shows it is the first member of one of the isolated pairs \((4^t-1,4^t)\), necessarily with \(t\ge2\). The second one starts the next arch, and the next character is zero, finishing an arch \(10\), again with exactly one one. The following character is also zero, so the same analysis repeats. If there is no adjacent second one, the next character is zero and the next zero-starting arch begins. Inductively **each complete arch after the first two contains exactly one one**. An unfinished suffix has only zeros, except when the prefix terminates *directly after the second one of a pair*, in which case it is precisely the one-character string \(1\). For \(N\ge6\), those exceptional termination points have lengths \(N=4^t+1\), \(t\ge2\). Therefore the number of complete arches is exactly \(S(N)-2\) minus one at these exceptional lengths.

**Step 3: universality equals number of arches.** For any finite binary word with \(r\) complete greedy arches, all binary words of length \(r\) occur as scattered subsequences: select the desired letter from each successive arch. Conversely, choose for each arch its terminal letter. Greedy matching of the concatenation of these \(r\) chosen terminal letters ends exactly at the final position of the \(r\)-th arch, since a terminal letter has no earlier occurrence within its own arch. Appending a letter absent from the remaining suffix (either binary letter if the suffix is empty) produces a binary string of length \(r+1\) that cannot be matched. Thus \(\iota(w)=r\). Combining this with Step 2 proves the all-prefix formula.

**Step 4: dyadic Fibonacci specialization.** The standard four-state binary-reading machine for Baum–Sweet has states \(A,B,C,D\), starting in \(A\), with transitions \(A\mapsto AB\), \(B\mapsto CB\), \(C\mapsto BD\), \(D\mapsto DD\) for inputs \(0,1\) respectively, and output \(1\) on \(A,B\), output \(0\) on \(C,D\). State \(A\) is the leading-zero state; \(B\) has no bad completed zero run and even trailing-zero parity; \(C\) has odd trailing-zero parity; \(D\) has already completed an odd zero run. Thus all padded binary integers of width \(k\) yield exactly \(B_{2^k}\). If \(x_k,y_k,z_k\) count accepted length-\(k\) continuations from states \(A,B,C\), then
\[
 x_{k+1}=x_k+y_k,\quad y_{k+1}=y_k+z_k,\quad z_{k+1}=y_k,
\]
with \(x_0=y_0=1,z_0=0\). Hence \(y_k=F_{k+1}\) and \(x_k=F_{k+2}\), so \(S(2^k)=F_{k+2}\). For \(k\ge3\), the power \(2^k\) is not \(4^t+1\); the main formula yields \(\iota(B_{2^k})=F_{k+2}-2\).

## Verification

The standalone `checker.py` independently evaluates the binary zero-run definition and a four-state morphic representation, verifies the proposed formula for **every** \(N\) from \(6\) through \(65{,}536\), confirms the exact adjacency positions over that range, and checks dyadic letter counts through \(k=16\). For small prefixes it separately enumerates all candidate binary subsequences at the critical lengths. Run with `python3 checker.py`. These finite tests are corroboration, not a replacement for the unrestricted proof above.

## Relationship to prior work

Waldschmidt's *Words and Transcendence* (2009), Section 2.3.3, presents the Baum–Sweet automatic sequence. Kosche, Koß, Manea and Siemer's *Absent Subsequences in Words* (first public preprint 2021), particularly Definitions 2.2–2.3 and Theorem 3.5, establishes general arch-factorization and absent-subsequence frameworks. These established ingredients make the exact index computable at any fixed prefix, but do not, in the inspected passages, state the all-prefix sparse-exception law or the dyadic Fibonacci specialization. The contribution assessed here is the Baum–Sweet-specific synchronization of greedy arches at the sparse positions \(4^t\), not the underlying general arch lemma, the automatic sequence's definition, or the familiar Fibonacci recurrence itself.

## Limitations

The formula applies to initial prefixes \(B_N\) only, with \(N\ge6\); it does not classify full languages of shortest absent subsequences, noninitial factors, or other automatic sequences. It is a self-review, not an independent audit. The 1976 original Baum–Sweet article was identified bibliographically but its complete text was not available for direct comparison, so historical priority remains subject to independent review. A generic algorithm's ability to calculate individual finite indices must not be confused with publication of this uniform formula.

## References

1. Michel Waldschmidt, *Words and Transcendence*, arXiv:0908.4034, first submitted 27 August 2009, Sections 2.3.3 and 5.1. https://arxiv.org/abs/0908.4034
2. Maria Kosche, Tore Koß, Florin Manea and Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first submitted 31 August 2021, Definitions 2.2–2.3 and Theorem 3.5. https://arxiv.org/abs/2108.13968
3. Alexander Okhotin, *On the State Complexity of Scattered Substrings and Superstrings*, *Fundamenta Informaticae* 99 (2010), 325–338, first published online 1 April 2010. https://doi.org/10.3233/FI-2010-252
4. L. E. Baum and M. M. Sweet, *Continued fractions of algebraic power series in characteristic 2*, *Annals of Mathematics* 103 (1976), 593–610. https://doi.org/10.2307/1970953
