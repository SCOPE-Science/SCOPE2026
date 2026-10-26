# Minimal unique factors of binary words with two marked symbols: exact spectrum

## Finding

A *minimal unique substring* (MUS) of a finite string is a nonempty contiguous factor that occurs at exactly one starting position, while every proper contiguous factor occurs at least twice. Occurrences, not merely different factor values, are counted. Take the labeled binary alphabet \(\{0,1\}\) and consider every word with exactly two occurrences of \(1\):
\[
w=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0}.
\]
Put \(M=\max(a,b,c)\), and let \(\eta=1\) exactly when \(M>0\) and precisely one of \(a,b,c\) equals \(M\), and \(\eta=0\) otherwise. The complete MUS set consists of the following **at most four distinct factors**, each present precisely when its indicated condition holds:

1. \(0^M\), if \(\eta=1\).
2. \(0^{\min(a,b)+1}1\), if \(a\ne b\) and not \(\bigl(\eta=1\ \text{and}\ M=\min(a,b)+1\bigr)\).
3. \(1\,0^{\min(b,c)+1}\), if \(b\ne c\) and not \(\bigl(\eta=1\ \text{and}\ M=\min(b,c)+1\bigr)\).
4. \(1\,0^b1\), if \(a\ge b\) and \(c\ge b\).

In particular \(1\le|\operatorname{MUS}(w)|\le4\) for every such word. The maximum is attained **if and only if**
\[
 b<\min(a,c)\quad\text{and}\quad a\ne c.
\]
It is attained already at length five, by \(01100\) and \(00110\), whose MUS sets are both \(\{00,01,10,11\}\).

For each \(j\in\{1,2,3,4\}\) and \(N\ge0\), let \(c_j(N)\) count the triples \((a,b,c)\) with \(a+b+c=N\) whose corresponding word has exactly \(j\) MUSs. Then **the complete all-length distribution** is
\[
\begin{aligned}
F_1(z)&=\sum_{N\ge0}c_1(N)z^N=\frac{1+z+z^2-z^3}{(1-z^2)(1-z^3)},\\[2pt]
F_2(z)&=\sum_{N\ge0}c_2(N)z^N=\frac{2z(1+z^2)}{(1-z^2)(1-z^3)},\\[2pt]
F_3(z)&=\sum_{N\ge0}c_3(N)z^N=\frac{z^2(4-z+z^2)}{(1-z)(1-z^2)(1-z^3)},\\[2pt]
F_4(z)&=\sum_{N\ge0}c_4(N)z^N=\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}.
\end{aligned}
\]
These sum to \((1-z)^{-3}\), since the number of length-\(N+2\) binary words with exactly two ones is \(\binom{N+2}{2}\). Consequently, under the uniform distribution on these words,
\[
\lim_{N\to\infty}\frac{c_4(N)}{\binom{N+2}{2}}=\frac13,
\qquad
\lim_{N\to\infty}\frac{c_3(N)}{\binom{N+2}{2}}=\frac23,
\]
whereas the combined proportion with one or two MUSs tends to zero.

## Assumptions and scope

The word is **linear**, has finite length \(N+2\ge2\), and contains **exactly two** copies of the labeled symbol \(1\). Any of the zero-gap lengths \(a,b,c\) may be zero. The definition uses **ordinary exact contiguous occurrences** within the word, not circular occurrences, scattered subsequences, approximate matching, or minimal absent factors. The empty factor is not counted as a MUS; it is regarded as occurring at all \(N+3\) boundaries, ensuring that a uniquely occurring single character is minimal. A proper factor of a unique factor cannot be absent, so the two maximal proper factors suffice to test minimality. The classification makes no assertion for words of higher Hamming weight.

## Proof

**Step 1: factors with no ones.** A nonempty all-zero factor \(0^r\) can occur exactly once only when \(r=M>0\) and the longest zero run among the three runs is unique. If \(r<M\), the longest zero run itself contains at least two occurrences of \(0^r\). If \(r=M\) and at least two runs have length \(M\), the factor repeats. Conversely, in the unique-maximum case, \(0^M\) occurs once, and all its nonempty shorter zero factors occur at least twice (as does the empty factor). Thus category 1 is exact. This is the specialized unique-run observation also implicit in the general MUS literature.

**Step 2: factors with exactly one one.** A factor containing exactly one occurrence of \(1\) has the form \(0^r1\,0^s\), and it can occur at most once around each of the two ones of \(w\). Its occurrence around the first one requires \(r\le a\) and \(s\le b\); occurrence around the second requires \(r\le b\) and \(s\le c\). If it occurs uniquely around one of these ones, it violates at least one of the other one's two inequalities. A minimal such unique factor must therefore have only **one nonzero flank**: if \(r>0\) and \(s>0\), the shortened factor obtained by discarding the irrelevant flank remains unique. For the left-flank type, the shortest value that distinguishes the preceding zero-run lengths \(a,b\) is \(r=\min(a,b)+1\), and it exists precisely when \(a\ne b\). An analogous argument gives \(s=\min(b,c)+1\) for the right-flank type, existing precisely when \(b\ne c\). In each case the candidate loses uniqueness after removing its one zero at the distinguishing end; removing its \(1\) leaves an all-zero factor. The latter is itself unique exactly in the excluded case where that zero factor is the uniquely longest zero run, as proved in Step 1. No other one-one factor can be minimal unique. This proves categories 2 and 3, including their exceptional exclusions.

**Step 3: factors with both ones.** Every factor containing both occurrences of \(1\) occurs exactly once. Such a factor is minimal unique only if it begins at the first \(1\) and ends at the second \(1\), since otherwise deleting an outer zero leaves a factor containing both ones and still occurring once. Its only possible form is therefore \(1\,0^b1\). Its two maximal proper factors \(1\,0^b\) and \(0^b1\) repeat if and only if \(c\ge b\) and \(a\ge b\), respectively (this includes \(b=0\)). Thus category 4 is exact. Factors with three or more ones do not occur. The four categories have different endpoint patterns and hence cannot coincide. Their cardinality is exactly the sum of the four indicated zero-one conditions, giving the sharp upper bound four.

**Step 4: equality at four.** If the four categories are all present, category 4 forces \(a,c\ge b\), while categories 2 and 3 then force the strict inequalities \(a,c>b\). Category 1 forces a unique maximum, so \(a\ne c\). Conversely, if \(b<\min(a,c)\) and \(a\ne c\), the maximum is attained uniquely by one of the outer gaps, and it is at least \(b+2\). Hence neither one-one candidate is excluded for containing the unique all-zero MUS, and all four categories occur. Choosing \((a,b,c)=(1,0,2)\) proves sharpness at the first possible length. For \(N<3\) no triple can meet the equality condition.

**Step 5: enumerating each cardinality.** Let \(N=a+b+c\), and abbreviate
\[
S(z)=\sum_{t\ge1}\sum_{0\le u<t}z^{2t+u}
=\frac1{1-z}\left(\frac{z^2}{1-z^2}-\frac{z^3}{1-z^3}\right).
\]
A direct case split of the four-category test shows that exactly one MUS occurs precisely for (i) \(a=b=c\), (ii) \(a=b>c\), (iii) \(b=c>a\), or (iv) \(a=c\) with \(b=a+1\). The corresponding generating function is
\[
F_1(z)=\frac{1+z}{1-z^3}+2S(z)=\frac{1+z+z^2-z^3}{(1-z^2)(1-z^3)}.
\]
Exactly two MUSs occur precisely for (i) \(a=b\) with \(c=b+1\), (ii) \(b=c\) with \(a=b+1\), or (iii) the four disjoint families
\[
(a,b,c)\in\{(t,t+1,u),(u,t+1,t),(t+1,t,u),(u,t,t+1)\},
\quad t\ge1,\ 0\le u<t.
\]
The corresponding generating function is
\[
F_2(z)=\frac{2z}{1-z^3}+4zS(z)=\frac{2z(1+z^2)}{(1-z^2)(1-z^3)}.
\]
For four MUSs, the criterion in Step 4 is counted by writing \(a=b+1+x\), \(c=b+1+y\), where \(x,y\ge0\) and \(x\ne y\). Therefore
\[
F_4(z)=\frac{z^2}{1-z^3}\left(\frac1{(1-z)^2}-\frac1{1-z^2}\right)
=\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}.
\]
The four cardinalities exhaust all triples, so \(F_3(z)=(1-z)^{-3}-F_1(z)-F_2(z)-F_4(z)\), which simplifies to the displayed third formula. Finally, the denominator expansion \((1-z^j)^{-1}\sim(j(1-z))^{-1}\) as \(z\uparrow1\) shows that \(F_4(z)\) and \(F_3(z)\) have leading singular coefficients \(1/3\) and \(2/3\) relative to \((1-z)^{-3}\). Each is a rational generating function with other poles of order at most two on the unit circle; equivalently by elementary coefficient extraction their coefficients have respective leading terms \(N^2/6\) and \(N^2/3\). This proves the density limits.

## Verification

The standalone `mus_checker.py` computes occurrence multiplicities directly for every substring of every binary word \(0^a1\,0^b1\,0^c\) with \(0\le a+b+c\le35\), independently computes the four-factor formula, and checks equality of the complete MUS **sets**, not just counts. It also verifies the four generating functions coefficient by coefficient through degree \(35\), the four-MUS characterization, and the length-five witnesses. The checker uses Python's standard library alone and reports \(8436\) tested gap triples. Run it with `python3 mus_checker.py` from the directory containing this result. The finite checks test the proof but do not replace its all-length arguments.

## Relationship to prior work

Ilie and Smyth (2011) introduced the study of minimum unique substrings and their duality with maximal repeats; this work does not claim the definition or generic MUS computation. Mieno, Inenaga, Bannai and Takeda (2016) give a general algorithm for MUS/SUS processing of run-length encoded strings, prove the upper bound \(2m-1\) for \(m\) runs (Lemma 7), and show that a uniquely longest run yields a MUS (Lemma 8). Their general bounds and algorithms do not state or directly imply the sharp constant four and complete enumerative spectrum for the specifically constrained two-one binary family. This finding specializes to an entirely explicit sparse-family classification, including exceptions caused by already-unique zero runs, and counts the four possible cardinalities for all lengths. Results on minimal **absent** factors and on shortest unique substrings have different predicates and do not yield these formulas by identification.

## Limitations

This is a classification for binary Hamming weight exactly two, not an optimal general-alphabet or all-weight bound. It counts distinct minimal unique factors, equivalently their unique occurrence intervals, and not all uniquely occurring factors or shortest-unique factors covering each position. The formulas have not been independently refereed or audited. An older equivalent special-case classification may exist outside the literature inspected; one foundational 2011 full text was inaccessible during the priority check, so the novelty assessment remains conditional on that access limitation. The published 2016 paper was inspected at the level of its full text and relevant proofs.

## References

1. L. Ilie and W. F. Smyth, *Minimum Unique Substrings and Maximum Repeats*, Fundamenta Informaticae 110 (2011), 183–195, DOI: 10.3233/FI-2011-536. Publisher first-online date recorded as 2011-01-01.
2. T. Mieno, S. Inenaga, H. Bannai and M. Takeda, *Shortest Unique Substring Queries on Run-Length Encoded Strings*, MFCS 2016, LIPIcs 58, Article 69, DOI: 10.4230/LIPIcs.MFCS.2016.69 (2016-08-19), especially Lemmas 7–8 and Section 4.
3. T. Mieno et al., *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window*, arXiv:1909.02804 (2019). A sliding-window development concerning general strings rather than the present fixed-Hamming-weight enumeration.
