# Exact finite antidictionary spectra of Rudin–Shapiro dyadic prefixes

## Finding
Let \(r_0r_1\cdots\) be the binary Rudin–Shapiro sequence, where \(r_i\) is the parity of the number of occurrences of `11` (overlaps included) in the binary expansion of \(i\), and put \(R_m=r_0r_1\cdots r_{2^m-1}\). A **minimal absent factor** of a finite word is a nonempty binary string not occurring contiguously, all of whose proper contiguous factors occur.

Write \(H_m(\ell)\) for the number of distinct minimal absent factors of \(R_m\) of length \(\ell\). **For every integer \(7\le m\le16\)**, its complete length spectrum is
\[
H_m(5)=8,\quad H_m(6)=4,\quad H_m(7)=10,\quad
H_m(8)=4,\quad H_m(9)=4,
\]
and, for every integer \(3\le j\le m-2\),
\[
H_m(2^j+2)=
\begin{cases}
1,&j=m-2,\\
12,&j=m-4,\\
8,&\text{otherwise}.
\end{cases}
\]
All other values of \(H_m\) are zero. In particular, these ten dyadic prefixes have exactly \(8m-5\) minimal absent factors; the unique longest has length \(2^{m-2}+2\). For example the prefix of length \(65536\) has exactly \(123\) minimal absent factors, with a unique longest one of length \(16386\).

## Assumptions and scope
These are finite, exact statements restricted to the ten integer parameters \(7\le m\le16\). They concern **linear** factors of words beginning at index zero (not cyclic factors), and minimality under all proper **contiguous** factors (not scattered subsequences). No statement for \(m>16\), no infinite-word antidictionary formula, and no asymptotic assertion is made. The alphabet is exactly \(\{0,1\}\), and distinct absent factors, rather than their possible occurrences, are counted.

## Proof
The proof is a finite exhaustive enumeration justified by a complete candidate-reduction lemma and reproduced in the self-contained `verify.py` and `SPECTRUM.tsv`.

**Candidate-reduction lemma.** Let \(w\) be any finite binary word and let \(x=aub\) be one of its minimal absent factors of length at least two, where \(a,b\in\{0,1\}\) and \(u\) may be empty. The strings \(au\) and \(ub\) occur in \(w\), whereas \(aub\) does not. Choose one occurrence of \(au\) starting at \(s\), and one of \(ub\) starting at \(t\). The suffixes beginning at \(s+1\) and at \(t\) have common prefix \(u\), but they cannot have a longer common prefix: following the chosen occurrence of \(au\), either the word ends or the following character is not \(b\). Consequently their longest common prefix is exactly \(u\). In a lexicographically sorted suffix array, the LCP of any two suffixes equals the minimum of the adjacent LCP entries between their ranks. Every suffix between two sharing prefix \(u\) also begins with \(u\). Hence \(u\) appears as the initial \(|u|\) letters of a positive adjacent LCP, except that the empty \(u\) is treated explicitly. This lemma excludes no minimal absent factor.

For each candidate \(u\), the algorithm scans all its occurrences, building the sets \(L(u)\) and \(R(u)\) of observed immediately preceding and following letters, respectively, and the set \(B(u)\subseteq\{0,1\}^2\) of observed pairs of both neighbors around the same occurrence. It reports exactly \(aub\) with \(a\in L(u)\), \(b\in R(u)\), and \((a,b)\notin B(u)\), plus any one-letter strings absent from \(w\). Indeed, these conditions are equivalent to \(au\) and \(ub\) occurring but \(aub\) being absent, and two longest proper factors occurring is equivalent to all proper factors occurring. Boundaries are handled by adding a side's letter only when that side exists; no fictitious sentinel is counted as a letter. Thus the algorithm is both exhaustive and sound for arbitrary finite binary words.

The suffix array is constructed by doubling-prefix ranks, terminating when all suffix ranks are distinct; adjacent exact LCPs are then computed by the standard linear scan. The word \(R_m\) is computed directly by counting adjacent set bits in the binary expansion of each index; the independent recurrence \(r_{2i}=r_i\), \(r_{2i+1}=r_i\oplus(i\bmod2)\) is checked across each generated prefix. The verifier executes the proved enumeration at **each** integer \(m=7,8,\ldots,16\); checks the displayed spectrum and the count \(8m-5\); independently tests every reported word for absence and both longest-proper-factor occurrences; and compares the sorted outputs to stored SHA-256 digests. The script also uses a different, all-substrings-set exhaustive construction to check equality of the entire antidictionaries at \(m=7,8\), and cross-checks on deterministic binary test words. The observed exact spectra establish every case in the finite quantifier range, not an inference from sampled parameters.

The small-length contribution is \(8+4+10+4+4=30\). The remaining permitted lengths have \(m-4\) indices \(j\); two exceptional multiplicities \(12\) and \(1\) replace \(8\), so their sum is \(8(m-6)+12+1=8m-35\). This yields \(8m-5\). The largest permitted length follows from \(j=m-2\), where the multiplicity is one.

## Verification
From the directory containing these two files, run `python3 verify.py` using standard-library Python. The expected terminal line is `VERIFY_OK`. The tab-separated file `SPECTRUM.tsv` records the ten counts, unique maximum lengths, and digests of complete sorted absent-factor lists. Every finite input is regenerated rather than read from external files. The complete derived output, including each long absent word, can be reconstructed using `absent_words(rudin_shapiro_binary(1 << m))` from the program.

## Relationship to prior work
Allouche and Bousquet-Mélou (1994) give deep descriptions of factors, recurrence, and factor complexity for generalized Rudin–Shapiro sequences, including a count of \(8\ell-8\) factors of length \(\ell\) in the infinite sequence for sufficiently large \(\ell\). Their results are about infinite-sequence factor languages and do not state the finite dyadic-prefix antidictionary length spectra computed here. The exact number of occurring factors of each length does not by itself specify which simultaneous left/right extensions are missing, and it does not encode truncation boundaries of the particular finite prefix.

Barton, Heliou, Mouchard, and Pissis (2014) provide general algorithms and a suffix-array characterization for enumerating minimal absent words of an arbitrary finite input. Their result guarantees computability and underpins this enumeration approach, but does not provide the claimed Rudin–Shapiro-specific numerical spectra. The public sequence database OEIS A005943 records *factor complexity*, not these minimal-absent-factor counts. No assertion of absolute literature uniqueness is made.

## Limitations
The displayed regularity across ten consecutive dyadic levels suggests a possible continuation, but is **not** a proof beyond \(m=16\). The independent all-substrings verifier is deliberately restricted to small levels, whereas the principal suffix-array method handles the full stated range and is proved exact. This is a finite exact classification, not a theorem about growth for unbounded \(m\). Older, differently indexed antidictionary tables might still exist.

## References
1. J.-P. Allouche and M. Bousquet-Mélou, *Facteurs des suites de Rudin-Shapiro généralisées*, Bulletin of the Belgian Mathematical Society 1 (1994), 145–164; available at https://ftp.gwdg.de/pub/EMIS/journals/BBMS/Bulletin/bul942/ALLBOU.PDF.
2. C. Barton, A. Heliou, L. Mouchard, and S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341, first posted 2014-06-24; https://arxiv.org/abs/1406.6341; final journal version BMC Bioinformatics 15, 388 (2014).
3. OEIS A005943, *Factor complexity of the Golay–Rudin–Shapiro binary word*, https://oeis.org/A005943 (related invariant, not an antidictionary table).
