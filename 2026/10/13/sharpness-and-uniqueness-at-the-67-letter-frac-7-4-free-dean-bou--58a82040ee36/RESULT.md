# Sharpness and uniqueness at the 67-letter \(\frac{7}{4}\)-free Dean boundary
## Finding
Work on the alphabet \(\{0,1,2,3\}\) with inverse pairs \(0\leftrightarrow2\) and \(1\leftrightarrow3\). A Dean word is a reduced square-free word. For a finite Dean word \(w\), let \(D_3(w)\) be its set of minimal absent words of length \(3\), and let \(d_3(w)=|D_3(w)|\).

Among all \(\frac{7}{4}\)-free Dean words satisfying \(d_3(w)\ge3\), the maximum length is exactly
\[
67.
\]
Moreover, there are exactly eight length-\(67\) extremizers, forming one orbit under the eight alphabet permutations that commute with inversion. A representative is
\[
\mathtt{0121032123012103230123210301210321230121030123210323012103212301210}.
\]
It is a palindrome and
\[
D_3(w)=\{\mathtt{010},\mathtt{101},\mathtt{303}\}.
\]
Thus the published bound \(|w|<68\) for this class is sharp, and its extremal orbit is unique.

## Assumptions and scope
A word is \(\frac{7}{4}\)-free when it has no factor of exponent at least \(\frac{7}{4}\). For a factor of length \(L\) and period \(p\), this forbidden condition is \(4L\ge7p\).

A length-\(3\) word \(abc\) is minimal absent from \(w\) exactly when \(abc\) is absent while both \(ab\) and \(bc\) occur. The quantity \(d_3\) used here is therefore the one in Badkobeh--Harju--Ochem--Rosenfeld.

The symmetry statement uses only alphabet permutations preserving the inverse relation. There are eight such permutations. Reversal is not needed to merge further cases because the displayed representative is itself palindromic.

## Proof
First, the displayed word is reduced and \(\frac{7}{4}\)-free. The verifier checks every factor and every candidate period \(p\) satisfying \(4L\ge7p\). It also directly computes the occurring pairs and triples and obtains exactly the three minimal absent triples \(\mathtt{010}\), \(\mathtt{101}\), and \(\mathtt{303}\). Hence the maximum is at least \(67\).

For the upper bound and uniqueness, normalize by symmetry. Every Dean word of length at least \(2\) begins with an ordered pair \(xy\) in which \(y\) is neither \(x\) nor its inverse. There are eight such ordered pairs. For each one, there is exactly one inversion-preserving alphabet permutation sending it to \(01\). Therefore words beginning with \(01\) give exactly one representative of every symmetry orbit.

The exhaustive extension search starts from \(01\). When a letter is appended, any newly created forbidden repetition must be a suffix. For every suffix length \(L\), the search tests every period
\[
1\le p\le\left\lfloor\frac{4L}{7}\right\rfloor
\]
and rejects the extension exactly when that suffix has period \(p\). This condition is necessary and sufficient for creating a factor of exponent at least \(\frac{7}{4}\), so no admissible word is pruned and no forbidden word survives.

At length \(67\), the normalized census contains \(414112\) words, and exactly one has \(d_3\ge3\): the displayed representative. Its orbit has size eight because an inversion-preserving permutation fixing its initial pair \(01\) is the identity. Hence there are exactly eight global length-\(67\) extremizers.

At length \(68\), the normalized census contains \(486776\) words. Every one contains all eight reduced pairs, and their \(d_3\)-distribution is
\[
397780\text{ with }d_3=0,\qquad
83006\text{ with }d_3=1,\qquad
5990\text{ with }d_3=2.
\]
Thus none has \(d_3\ge3\). Finally, once all reduced pairs occur, extending a word can only add length-\(3\) factors; it cannot create a new minimal absent triple. Therefore \(d_3\) is nonincreasing under all further extensions from a length-\(68\) prefix. No longer \(\frac{7}{4}\)-free Dean word can have \(d_3\ge3\). This proves the exact maximum and the uniqueness statement.

## Verification
Run `python3 verify.py` beside `verify.cpp` and `certificate.json`. The wrapper compiles the exact C++ enumerator and compares its output with the embedded certificate.

The enumerator independently performs the normalized length-\(67\) and length-\(68\) censuses. It also scans every factor of the final witness directly for forbidden exponents, recomputes \(D_3\), verifies palindromicity, generates all eight inversion-preserving alphabet symmetries, and checks that the resulting orbit has size eight.

The decisive length-\(68\) census is exhaustive rather than a sampled experiment. The extension monotonicity argument then converts that finite census into the all-longer-length upper bound.

## Relationship to prior work
Badkobeh, Harju, Ochem, and Rosenfeld introduced the avoided-factor quantities \(D_l(w)\) and \(d_l(w)\) for Dean words and studied their interaction with repetition thresholds. Their Lemma 19 states that if \(w\) is a \(\frac{7}{4}\)-free Dean word with \(d_3(w)\ge3\), then \(|w|<68\). The paper does not give a length-\(67\) witness or classify equality cases for that finite bound.

The same paper constructs infinite \(\frac{7}{4}^+\)-free Dean words with four avoided triples, but that is a different strict-threshold statement: \(\frac{7}{4}^+\)-free permits exponent exactly \(\frac{7}{4}\), whereas the present claim forbids it.

A later paper by Ochem studies \(\frac{7}{4}^+\)-free ternary words avoiding \(010\) and directedness. It cites the Dean-word paper but does not address the sharpness or equality cases of Lemma 19.

Searches using the exact threshold, the phrase “Lemma 19”, the length \(67\), the minimal-absent-triple formulation, and the full witness string did not locate a published statement implying the sharpness or unique-orbit classification.

## Limitations
The classification concerns the condition \(d_3(w)\ge3\) at the exact \(\frac{7}{4}\)-free threshold. It does not classify extremal words for \(d_3=0,1,2\), nor does it address the strict \(\frac{7}{4}^+\)-free language.

The originality search cannot exclude an unindexed computation or unpublished enumeration. The mathematical claim itself is certified by exhaustive finite search plus the extension monotonicity argument.

## References
1. G. Badkobeh, T. Harju, P. Ochem, and M. Rosenfeld, “Avoiding Square-Free Words on Free Groups,” arXiv:2104.06837, first public version 2021-04-14; *Theoretical Computer Science* 922 (2022), 206--217, DOI 10.1016/j.tcs.2022.04.025.
2. P. Ochem, “On ternary Dejean words avoiding 010,” *Notes on Number Theory and Discrete Mathematics* 29(3) (2023), 545--548, DOI 10.7546/nntdm.2023.29.3.545-548.
