# Exact unbordered-conjugate spectrum of binary words containing three ones

## Finding
For each integer \(n\geq3\), consider all binary words \(w\) of length \(n\) with exactly three ones. A word is *unbordered* if it has no nonempty proper prefix equal to a suffix. Write \(U(w)\) for the number of its \(n\) cyclic shift **positions** at which the shifted word is unbordered. Let \(C_j(n)=\#\{w:U(w)=j\}\).

If \((a,b,c)\) are the three cyclic numbers of zeros between consecutive ones, then
\[
U(w)=[a\ne b]+[b\ne c]+[c\ne a],
\]
where \([P]\) is one when \(P\) holds and zero otherwise. Thus only \(0\), \(2\), and \(3\) unbordered cyclic shifts occur. Define \(\delta_n=[3\mid n]\). The **complete all-length enumeration** is
\[
\begin{aligned}
C_0(n)&=\frac{n}{3}\delta_n,\\
C_2(n)&=n\left(\left\lfloor\frac{n-3}{2}\right\rfloor+1-\delta_n\right),\\
C_3(n)&=\binom{n}{3}-C_0(n)-C_2(n),
\end{aligned}
\]
with \(C_j(n)=0\) for every other integer \(j\). Consequently \(C_3(n)/\binom n3\to1\) as \(n\to\infty\). For example, at length \(9\) the respective counts for \(j=0,2,3\) are \(3,27,54\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the three occurrences of \(1\) are counted with multiplicity, and all nonnegative zero-gap lengths, including zero, are allowed. A cyclic shift is indexed by an integer from \(0\) to \(n-1\); periodic words may repeat as strings but still have \(n\) indexed shifts. All formulas hold for every integer \(n\ge3\), including \(n=3\). Counts are of linear words, not rotation classes or words modulo symbol exchange.

## Proof
**Step 1: an unbordered-rotation lemma.** For any nonnegative integers \(a,b,c\), consider
\[
v=1\,0^a1\,0^b1\,0^c.
\]
This word is unbordered exactly when \(a<c\). If \(c=0\) it begins and ends in \(1\), and is bordered; the inequality also fails. For \(c>0\), if \(a\ge c\), its initial and final \(c+1\) letters are both \(1 0^c\), giving a proper border. Conversely, if \(a<c\) and a proper border exists, that border must start at the second or third occurrence of \(1\) in the suffix, since every prefix begins with \(1\). A border beginning with the final \(1\) would require \(a\ge c\), impossible. A border beginning with the middle \(1\) would require matching the first two inter-one gaps \(a=b\). Its length is \(b+c+2\). But \(a=b<c\) forces the corresponding prefix to contain the third \(1\), whereas the suffix beginning at the middle \(1\) contains only two ones, another contradiction. Thus no border exists.

Reversing words preserves borderedness, so the reversal of the preceding lemma gives: a rotation of the form \(0^a1\,0^b1\,0^c1\) is unbordered precisely when \(a>c\).

**Step 2: gap comparison.** Any unbordered binary rotation must begin and end with different letters; otherwise its single-letter prefix is a border. Each cyclic junction from \(0\) to \(1\) contributes a potential rotation beginning at that \(1\); each junction from \(1\) to \(0\) contributes a potential rotation beginning at the first \(0\). The two lemmas say that, for each adjacent pair of cyclic gaps, exactly one of these candidate rotations is unbordered if the two gaps differ, and neither is unbordered if they are equal. All remaining shifts begin and end in the same letter and are bordered. Therefore \(U(w)=[a\ne b]+[b\ne c]+[c\ne a]\). Three cyclic values have either zero, two, or three unequal adjacent pairs.

**Step 3: counting.** Put \(m=n-3\). There are \(\binom{m+2}{2}=\binom{n-1}{2}\) ordered nonnegative triples \((a,b,c)\) with sum \(m\). If all gaps are equal, there is precisely one triple if \(3\mid n\) and none otherwise. If exactly two gaps are equal, choose the location of the unequal gap in three ways, choose the common value \(t\) in \(0\le t\le\lfloor m/2\rfloor\), and omit the single all-equal possibility. This gives \(3(\lfloor m/2\rfloor+1-\delta_n)\) triples. All remaining gap triples have three distinct values.

For every gap triple choose a marked starting position among the \(n\) positions and place a \(1\) there, followed by the three specified cyclic gaps. Conversely, each length-\(n\) three-one word has exactly three choices of marked \(1\). Thus \(3C_j(n)=nT_j(n)\), where \(T_j(n)\) counts the ordered gap triples having \(j\) unequal cyclic neighbor pairs. Substitution proves all three formulas, including the periodic all-equal case. Finally \(C_2(n)=O(n^2)\) and \(C_0(n)=O(n)\), whereas \(\binom{n}{3}=\Theta(n^3)\), proving the limiting proportion.

## Verification
Run `python3 verify.py` with Python 3 and no nonstandard dependencies. It compares direct cyclic-rotation border tests with the gap classification for every three-one binary word at lengths \(3\) through \(23\), a total of \(10{,}626\) inputs; separately, it exhausts ordered zero-gap triples through length \(120\), checking all counting identities with exact integer arithmetic. The expected output begins `ALL_CHECKS_PASS`. This finite testing is independent corroboration, not the proof for arbitrary lengths.

## Relationship to prior work
Harju and Nowotka introduced and studied the binary border-correlation function and fixed-weight border counts; their results motivate asking for the full distribution of the **number** of unbordered conjugates conditional on a prescribed sparse letter count. Their 2008 follow-up examines which binary border-correlation patterns occur over larger alphabets, not the multiplicity of three-one binary words in each count stratum. Holub and Müller's 2015 preprint gives an inductive characterization of *all* binary words with exactly two unbordered conjugates, a strictly broader structural class; specializing that characterization alone does not state the three-one length-dependent multiplicities \(C_0(n),C_2(n),C_3(n)\) or this direct gap proof. Clokie, Gabric and Shallit's 2019 paper derives general maximum/existence and expected-number results, which do not determine the fixed-weight distribution. The present contribution is the complete all-length joint histogram in the first sparse weight where three unbordered rotations can occur, not a new characterization of all fully bordered words.

## Limitations
The theorem is restricted to binary words with exactly three ones and to counts of indexed cyclic shifts. It does not establish the corresponding distributions for higher weights or alphabet sizes. A general earlier characterization of the two-unbordered case is known; the novelty claim concerns the explicit complete sparse-layer distribution. Exact priority cannot be established by a finite literature search, and two relevant older papers could not be completely inspected from accessible full text.

## References
1. T. Harju and D. Nowotka, “Border correlation of binary words,” *Journal of Combinatorial Theory A* **108** (2004), 331–341. DOI: 10.1016/j.jcta.2004.07.009.
2. T. Harju and D. Nowotka, “Counting bordered and primitive words with a fixed weight,” *Theoretical Computer Science* **340** (2005). DOI: 10.1016/j.tcs.2005.03.040.
3. T. Harju and D. Nowotka, “Bordered Conjugates of Words over Large Alphabets,” *Electronic Journal of Combinatorics* **15** (2008), #N41. DOI: 10.37236/916.
4. Š. Holub and M. Müller, “Fully bordered words,” arXiv:1504.02222, first posted 2015-04-09.
5. T. Clokie, D. Gabric and J. Shallit, “Circularly squarefree words and unbordered conjugates: a new approach,” arXiv:1904.08187 (2019).
