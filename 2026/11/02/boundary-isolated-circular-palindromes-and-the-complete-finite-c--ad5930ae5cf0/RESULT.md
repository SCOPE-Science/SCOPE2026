# Boundary-isolated circular palindromes and the complete finite Cantor spectrum

## Finding
Let \(\operatorname{Pal}(w)\) denote the **distinct nonempty** contiguous palindromic factors of a finite word \(w\). Let \(\operatorname{CPal}(w)\) denote its distinct nonempty palindromic *circular factors*, namely factors of length between \(1\) and \(|w|\) read cyclically. Define \(\operatorname{pre}_d(w)\) and \(\operatorname{suf}_d(w)\) as the length-\(d\) prefix and suffix.

**Boundary-isolated transfer theorem.** If a binary palindrome \(w\) has length \(N\ge3\), first and last symbols \(1\), and no contiguous \(11\) internally, then
\[\operatorname{CPal}(w)=\operatorname{Pal}(w)\;\sqcup\;\{\operatorname{suf}_d(w)\operatorname{pre}_d(w):1\le d\le\lfloor N/2\rfloor\}.\]
In particular, if \(w\) is rich (meaning \(|\operatorname{Pal}(w)|=N\)), it has exactly \(N+\lfloor N/2\rfloor\) distinct nonempty circular palindromes.

**Complete Cantor specialization.** Set \(C_0=1\) and \(C_{k+1}=C_k0^{3^k}C_k\). For each \(k\ge1\), put \(N=3^k\), \(m=3^{k-1}\), and let \(P_k^{\circ}(\ell)\) be the number of distinct circular palindromes of length \(\ell\) in \(C_k\). For every integer \(1\le\ell\le N\),
\[
P_k^{\circ}(\ell)=\begin{cases}
2,&\ell=1,\\
3,&3\le\ell\le m\text{ and }\ell\text{ odd},\\
2,&2\le\ell<m\text{ and }\ell\text{ even},\\
1,&\text{otherwise}.
\end{cases}
\]
Every circular palindrome not already in \(C_k\) is uniquely \(\operatorname{suf}_d(C_k)\operatorname{pre}_d(C_k)\), for \(1\le d\le (N-1)/2\). Thus
\[|\operatorname{CPal}(C_k)|=\frac{3N-1}{2}.\]
For \(k=0\), the only circular palindrome is \(1\).

## Assumptions and scope
The alphabet is the literal binary alphabet \(\{0,1\}\). Factors are considered **distinct by their entire word**, not by occurrence or up to cyclic conjugacy. Circular factors make at most one full traversal (length at most \(N\)); the empty word is excluded throughout. A word is rich if it has the maximum possible \(N\) distinct nonempty ordinary palindromes. All integer ranks, lengths and prefix/suffix parameters are quantified explicitly above. The result is not a claim about unbounded-length factors of the periodic word \(w^\omega\).

## Proof
**1. The general boundary transfer.** Since \(w\) has no internal \(11\) and both its endpoints equal \(1\), the cyclic word has exactly one adjacent \(11\), at the join from the last to the first symbol. Every circular factor that is not an ordinary contiguous factor in its chosen occurrence crosses that join and contains this \(11\). Within that factor there is exactly one occurrence of \(11\). Reversal of a palindrome preserves the positions of its length-two factors after reflection. Hence its unique \(11\) must map to itself, forcing this pair to be exactly the two central symbols: the palindrome has even length \(2d\), and its occurrence consists of the last \(d\) symbols of \(w\) followed by the first \(d\). Conversely, for each \(1\le d\le\lfloor N/2\rfloor\), \(\operatorname{suf}_d(w)=\operatorname{pre}_d(w)^R\) by palindromicity, so \(\operatorname{suf}_d(w)\operatorname{pre}_d(w)\) is a palindrome of length \(2d\). It contains \(11\), so is not an ordinary factor; distinct parameters produce different lengths. This proves exactly the displayed disjoint union. If \(w\) is rich, counting gives \(N+\lfloor N/2\rfloor\).

**2. Ordinary Cantor palindromes.** Each \(C_k\) is a palindrome beginning and ending with \(1\), has no internal \(11\), and for \(k\ge1\) has longest consecutive zero run of length exactly \(3^{k-1}\). The first two assertions follow inductively from \(C_{k+1}=C_k0^{3^k}C_k\); the zero-run assertion follows from the inserted central run, longer than any pre-existing run.

We prove that \(C_k\) has exactly \(3^k\) distinct nonempty ordinary palindromes and determine their lengths. The bases are \(\operatorname{Pal}(C_0)=\{1\}\) and \(\operatorname{Pal}(C_1)=\{0,1,101\}\). For \(k\ge1\), let \(U=C_k\), \(V=C_{k-1}\), \(n=|U|=3^k\), and \(r=|V|=n/3\). Inside \(C_{k+1}=U0^nU\) lie the following **three disjoint families of palindromes absent from** \(U\):

* \(0^t\), for \(r<t\le n\), contributing \(n-r\) words: \(U\) has no zero run longer than \(r\).
* \(0^tV0^t\), for \(1\le t\le r\), contributing \(r\) words: the terminal copy of \(V\) in the left \(U=V0^rV\) has at least \(r\) zeros on each side in \(C_{k+1}\). To see that none occurs in \(U\), observe that every occurrence of \(V\) in \(V0^rV\) is its first or last block. Indeed \(V\) begins and ends with \(1\), so an occurrence cannot enter a zero-only gap from just one side, and a length-\(r\) occurrence cannot span both flanking \(1\)'s across the length-\(r\) gap. Neither endpoint occurrence has zeros on both sides in \(U\).
* \(\operatorname{suf}_t(U)0^n\operatorname{pre}_t(U)\), for \(1\le t\le n\), contributing \(n\) words. These are palindromes because \(U=U^R\), and their lengths \(n+2t>n\) preclude occurrence in \(U\).

The first and second families cannot coincide (the second contains \(1\)); both have length at most \(n\) and cannot coincide with the third. Different words within a family have different lengths. Therefore the \(n\) old palindromes persist and \(2n\) new ones appear: at least \(3n\) distinct nonempty palindromes in a word of length \(3n\). The universal bound of at most \(|w|\) nonempty palindromes for a word \(w\) forces **equality**, proving that these three families exhaust all new palindromes. This proves richness for all ranks without relying on finite experiments.

For a fixed \(k\ge1\), put \(m=3^{k-1}\). Inducting on this exhaustive three-family description gives the ordinary length spectrum: \(2\) at length \(1\); \(3\) at odd lengths from \(3\) through \(m\); \(1\) at even lengths from \(2\) through \(m-1\); \(1\) at odd lengths from \(m+2\) through \(3m\); and \(0\) elsewhere. Explicitly, the zero-only family fills the previously missing even lengths as the central zero run grows; the padded \(V\) family supplies the extra odd palindrome at lengths \(m/3+2,m/3+4,\ldots,m\); and the middle-bridge family supplies the longer odd lengths \(m+2,m+4,\ldots,3m\). The base \(k=1\) is immediate from \(101\).

**3. Circular Cantor spectrum.** The conditions of the boundary transfer theorem hold for every \(C_k\). For \(N=3^k\) odd, exactly one new palindrome is added at each even length \(2,4,\ldots,N-1\), and none at odd lengths. Adding this to the ordinary spectrum proves the displayed formula. Since the ordinary count is \(N\) and the new count is \((N-1)/2\), the total is \((3N-1)/2\).

## Verification
A standalone Python 3 checker, `checker.py`, enumerates literal factors and reversals, independently verifies the transfer principle for all admissible binary palindromes through length \(14\), verifies the exact constructive ordinary-palindrome recursion for Cantor ranks \(2\) through \(5\), and compares the entire predicted circular languages and length spectra for ranks \(0\) through \(5\). Execute `python3 checker.py` with the files as embedded. All checks passed in the package workspace. The proof, not the bounded enumeration, establishes all ranks.

## Relationship to prior work
Glen, Justin, Widmer and Zamboni (2008) study palindromic richness and explicitly identify the infinite Cantor word as rich; their general bound on ordinary palindromes is used above. That source does not present this finite cyclic boundary-transfer language or its lengthwise circular classification. Simpson (2014) proves a general \(5N/3\) upper bound on circular palindromes and gives extremal examples; a general upper bound does not imply the present exact spectrum. Schaeffer and Shallit (2015/2016) study palindromic properties of several automatic sequences without classifying this finite Cantor circular language. Relevant preceding finite Cantor linear-palindrome results cover the ordinary factor spectrum but not the additional cyclic boundary words. The transferable uniqueness-of-the-join statement is the distinct mechanism here.

## Limitations
This theorem requires palindromicity and a unique cyclic \(11\) join in its general form. The Cantor specialization treats complete length-\(3^k\) iterates, not arbitrary prefixes, and counts literal distinct factors rather than rotational equivalence classes. It does not address repeated traversal or cyclic words having multiple occurrences of the join pair. The full text of Simpson (2014) could not be inspected; historical-priority assessment is therefore qualified, and no independent mathematical audit has been performed.

## References
1. A. Glen, J. Justin, S. Widmer, L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656 (first publicly submitted 2008-01-10), *European Journal of Combinatorics* 30 (2009), 510–531. https://arxiv.org/abs/0801.1656
2. J. Simpson, *Palindromes in circular words*, *Theoretical Computer Science* 550 (2014), 66–78. DOI 10.1016/j.tcs.2014.07.012. https://doi.org/10.1016/j.tcs.2014.07.012
3. L. Schaeffer, J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (2015), *Electronic Journal of Combinatorics* 23(1) (2016), P1.25. https://arxiv.org/abs/1508.02074
