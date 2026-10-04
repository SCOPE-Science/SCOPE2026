# Exact binary two-multispectrum code size and singleton classification
## Finding
For a binary word \(x=x_1\cdots x_n\in\{0,1\}^n\), let \(M_2(x)\) be the multiset of all adjacent pairs \(x_ix_{i+1}\), \(1\le i<n\). Write \(Q_n\) for the number of distinct possible multispectra \(M_2(x)\). A binary length-\(n\) reconstruction code for read length two is exactly a set containing at most one word from each multispectrum class, so its maximum size is \(Q_n\).

For every \(n\ge2\),
\[
Q_{2m}=3m^2-m+2,
\qquad
Q_{2m+1}=3m^2+2m+2.
\]
Thus the optimum code size is \(\frac34n^2+O(n)\), whereas the unrestricted composition count used as a general upper bound for length-two multispectra is cubic in \(n\).

The same analysis gives the exact singleton classes. A word is uniquely determined among all binary words of the same length by \(M_2(x)\) if and only if it has at most one transition, or it is one of the two alternating words of even length at least four. Hence the number of individually reconstructible words is
\[
2n+2\mathbf 1_{\{n\ge4\text{ even}\}}.
\]
For \(n=2\), all four words are already in the at-most-one-transition family.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the word length satisfies \(n\ge2\), the read length is exactly two, and multiplicities of adjacent pairs are retained. The observed object is the linear, not cyclic, multispectrum: there are exactly \(n-1\) adjacent-pair observations.

For a word \(x\), let \(c_{ab}(x)\) be the multiplicity of the pair \(ab\in\{00,01,10,11\}\) in \(M_2(x)\). The profile is therefore the quadruple
\[
(c_{00},c_{01},c_{10},c_{11}).
\]

## Proof
Put \(N=n-1\). Telescoping the binary symbols along the word gives
\[
c_{01}-c_{10}\in\{-1,0,1\}.
\]
More precisely, the difference is \(1\) when the word starts in \(0\) and ends in \(1\), it is \(-1\) for the reverse endpoint orientation, and it is \(0\) when the endpoints agree.

Conversely, every nonnegative quadruple with total \(N\), transition-count difference in \(\{-1,0,1\}\), and at least one transition when both symbols are to occur is realizable. This follows directly from the run representation. If \(c_{01}=c_{10}=k\ge1\), one may start and end in \(0\), use \(k+1\) zero-runs and \(k\) one-runs, and distribute the \(c_{00}\) and \(c_{11}\) equal-adjacency counts as extra symbols among those positive runs. If \(c_{01}=k+1\) and \(c_{10}=k\), start in \(0\), end in \(1\), and use \(k+1\) runs of each symbol; the opposite imbalance is symmetric. When both transition counts vanish, the only realizable profiles are the two constant words.

It remains to count these feasible profiles. The balanced case contributes
\[
2+\sum_{k=1}^{\lfloor N/2\rfloor}(N-2k+1),
\]
where the initial \(2\) accounts for the two constant profiles. Each of the two endpoint-imbalanced cases contributes
\[
\sum_{k=0}^{\lfloor(N-1)/2\rfloor}(N-2k).
\]
For \(n=2m\), their sum is
\[
2m^2+m(m-1)+2=3m^2-m+2.
\]
For \(n=2m+1\), it is
\[
2m(m+1)+m^2+2=3m^2+2m+2.
\]
A reconstruction code can contain at most one representative from each profile, and choosing one representative from every feasible profile attains the bound, proving the exact code size.

For the singleton classification, consider first \(c_{01}=k+1\), \(c_{10}=k\). The endpoint orientation is forced and there are \(k+1\) runs of each symbol. The loop counts \(c_{00}\) and \(c_{11}\) may be distributed independently among these runs, so the class contains exactly
\[
\binom{c_{00}+k}{k}\binom{c_{11}+k}{k}
\]
words. This equals one exactly when either \(k=0\), giving a word with one transition, or both loop counts vanish, giving an alternating word. The opposite endpoint orientation is symmetric. If \(c_{01}=c_{10}=k\ge1\), both equal-endpoint orientations are feasible and give distinct words, so the class is not a singleton. When both transition counts vanish, the two realizable profiles are the two constant words. This proves the stated classification and count.

## Verification
The accompanying `verify.py` independently enumerates every binary word for \(2\le n\le16\), groups words by their literal adjacent-pair multispectra, checks the feasible-profile characterization, verifies the closed form for \(Q_n\), verifies the exact run-composition class-size formula for every observed profile, and checks the singleton classification word-for-word. It examines \(131068\) words in the exhaustive range. A separate arithmetic pass checks the feasible-profile count formula through \(n=200\).

The finite computation is corroborative; the proof above establishes the theorem for all \(n\ge2\).

## Relationship to prior work
Gabrys and Milenkovic define the same linear \(L\)-multispectrum and the same notion of an \(L\)-reconstruction code. Their general counting argument bounds the number of realizable multispectra by the number of unrestricted \(2^L\)-compositions, and their main constructions concern logarithmic read lengths. The present result resolves the shortest nontrivial read length \(L=2\) exactly, where endpoint flow constraints make the number of realizable profiles quadratic rather than the cubic unrestricted-composition bound.

Jacquet, Knessl, and Szpankowski count first-order Markov types after explicitly passing to cyclic strings. In their binary example the frequency matrix is balanced, so the two cross-transition counts must be equal. The linear multispectrum problem here is different: free endpoints permit cross-transition imbalance \(-1\), \(0\), or \(1\), and the zero-transition case has an additional connectivity restriction. Their cyclic binary formula therefore does not state the linear reconstruction-code optimum or the singleton classification above.

The mathematical ownership is combinatorics on words; closely related string-reconstruction literature is classified under MSC 68R15.

## Limitations
The theorem is binary and specific to read length two. It does not claim an exact formula for larger alphabets, larger read lengths, noisy or incomplete spectra, cyclic spectra, or efficient ranking and unranking of an optimal representative codebook. The literature search did not identify a prior statement of this exact linear formula, but an elementary result can occur in unindexed notes or under Markov-type terminology; that residual originality risk remains.

## References
1. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (2018); IEEE Transactions on Information Theory 65(12), 7682--7696 (2019), DOI:10.1109/TIT.2019.2935973.
2. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768.
3. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, SIAM Journal on Discrete Mathematics 29(3), 1340--1371 (2015), DOI:10.1137/140962486. This adjacent reconstruction literature is indexed under MSC 68R15.
