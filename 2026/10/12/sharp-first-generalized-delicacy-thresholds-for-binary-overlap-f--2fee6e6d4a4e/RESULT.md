# Sharp first generalized-delicacy thresholds for binary overlap-free words
## Finding
For a binary overlap-free word, call it \(k\)-delicate when changing any set of between \(1\) and \(k\) positions creates an overlap. Let
\[
L_k=\min\{|w|:w\text{ is a finite }k\text{-delicate binary overlap-free word}\}.
\]
Then the first two nontrivial generalized-delicacy thresholds are
\[
L_2=13,\qquad L_3=14.
\]

There are exactly four shortest \(2\)-delicate words:
`0100110010110`, `0110100110010`, `1001011001101`, and `1011001101001`. They form one orbit under reversal and binary complementation, and each has overlap-free isolation distance exactly \(3\).

There are exactly two shortest \(3\)-delicate words:
`00101100110100` and `11010011001011`. They are complementary palindromes, form one orbit under reversal and complementation, and each has overlap-free isolation distance exactly \(4\).

## Assumptions and scope
An overlap is a factor of the form \(xYxYx\), where \(x\) is one letter and \(Y\) is possibly empty. A binary word is overlap-free when it contains no such factor.

For a fixed length \(n\), let \(\mathcal O_n\) be the set of overlap-free binary words of length \(n\), and define the isolation distance
\[
\delta(w)=\min\{d_H(w,v):v\in\mathcal O_n,\ v\ne w\}.
\]
Because the alphabet is binary, changing a prescribed set of positions means flipping exactly those bits. Consequently a word is \(k\)-delicate exactly when \(\delta(w)\ge k+1\). The result concerns only \(k=2\) and \(k=3\), the first two cases beyond ordinary delicacy; it does not settle existence for every \(k\).

## Proof
The equivalence between generalized delicacy and Hamming isolation reduces the claim to an exact finite census of \(\mathcal O_n\).

For every \(1\le n\le14\), all overlap-free words were generated and their distances to every other word in \(\mathcal O_n\) were computed. Through length \(12\), the maximum isolation distance is at most \(2\). At length \(13\), the distance histogram is
\[
44\text{ words at distance }1,\quad 12\text{ at distance }2,\quad 4\text{ at distance }3.
\]
Thus no \(2\)-delicate binary overlap-free word has length below \(13\), while the four displayed words are exactly the length-\(13\) examples. Hence \(L_2=13\).

Through length \(13\), the maximum isolation distance is at most \(3\). At length \(14\), the distance histogram is
\[
44\text{ words at distance }1,\quad 14\text{ at distance }2,\quad 2\text{ at distance }3,\quad 2\text{ at distance }4.
\]
Therefore no \(3\)-delicate word has length below \(14\), and the two displayed words are exactly the length-\(14\) examples. Hence \(L_3=14\).

The orbit statements follow by direct reversal and complementation of the complete extremizer lists.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses two independent finite enumeration routes. The first grows overlap-free prefixes and checks only overlaps ending at the newly appended bit. The second scans all \(2^n\) binary words and tests every possible factor from scratch. The two complete sets agree for every \(1\le n\le14\).

It then recomputes every pairwise Hamming isolation distance, checks the full distance histograms stored in `certificate.json`, identifies the exact four and two extremizer lists, and verifies the reversal/complement orbit statements. No random sampling or timeout-dependent inference is used.

## Relationship to prior work
Przybocki introduced \(k\)-delicacy as a generalization of delicacy and explicitly asked whether finite \(k\)-delicate overlap-free binary words exist for every \(k\). The same paper completely classifies ordinary delicate overlap-free words, corresponding to \(k=1\), but gives no finite length minima for \(k\ge2\).

The present result determines, with complete equality-case classification, the first two generalized levels beyond that published classification. The statement is stronger than merely exhibiting witnesses: it proves the exact minimum lengths and all shortest witnesses.

Targeted searches for finite \(2\)-delicate and \(3\)-delicate overlap-free words, shortest generalized-delicacy witnesses, Hamming-isolation formulations, the exact witness strings, and later references to the source question did not locate a published statement implying these two thresholds. A 2024 paper on Hamming-isometric words studies whether occurrences of a fixed factor can be avoided along shortest Hamming transformations; that is a different object and does not constrain Hamming isolation inside the overlap-free language.

## Limitations
Only the first two nontrivial values \(L_2\) and \(L_3\) are claimed. The all-\(k\) existence question remains outside this result.

The lower bounds are exhaustive finite proofs through lengths \(12\) and \(13\), respectively. They do not supply a structural formula for \(L_k\) at larger \(k\). An unindexed computation or unpublished note could contain the same small thresholds; no such source was found in the targeted originality checks.

## References
1. B. Przybocki, “Lengths of Irreducible and Delicate Words,” arXiv:2108.06646, first public version 2021-08-15; Electronic Journal of Combinatorics 29(3), 2022, P3.7, DOI 10.37236/10669.
2. M. Anselmo, M. Flores, and M. Madonia, “Computing the index of non-isometric k-ary words with Hamming and Lee distance,” Computability 13(3–4), 2024, DOI 10.3233/COM-230441.
