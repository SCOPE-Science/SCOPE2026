# Abelian three-antipower avoidance in Dyck words of height two

## Finding
For every integer \(n\ge1\), the complete family of height-at-most-two Dyck words of semilength \(n\) without an abelian three-antipower consists of exactly these words, subject to the conditions shown:

1. \((01)^n\), for every \(n\ge1\).
2. \((0011)^{n/2}\), when \(n\) is even.
3. \(00(10)^{n-2}11\), when \(n\ge4\) and \(3\nmid n\).
4. \(01\,00(10)^{n-3}11\) and \(00(10)^{n-3}11\,01\), when \(n\ge5\) and \(n\equiv2\pmod3\).

The families are disjoint. Hence the exact number is
\[
T_n=1+\mathbf1_{2\mid n}+\mathbf1_{\{n\ge4,\ 3\nmid n\}}+2\mathbf1_{\{n\ge5,\ n\equiv2\pmod3\}}.
\]
In particular, the enumeration becomes periodic modulo six beyond its initial boundary terms.

## Assumptions and scope
A Dyck word is a binary word with equally many zeros and ones such that every prefix has at least as many zeros as ones; its height is the maximum of the running excess of zeros over ones. A *factor* is a contiguous substring. An *abelian three-antipower* is a factor of the form \(UVW\) with \(|U|=|V|=|W|\ge1\) whose three Parikh vectors are pairwise distinct. For binary factors of equal length, different Parikh vectors mean different counts of zeros. Only maximal height at most two is assumed; no restriction on the number of primitive excursions is imposed. The statement holds for all positive semilengths, not merely the checked finite range.

## Proof
**1. Height code.** For a height-at-most-two Dyck word \(w\) of length \(2n\), let \(H(t)\) be its height after \(t\) letters and define \(x_j=H(2j)/2\) for \(0\le j\le n\). Every odd-position height equals one. Thus \(x_j\in\{0,1\}\), with \(x_0=x_n=0\). Conversely, every such bit sequence determines a unique Dyck word: for \(0\le j<n\), the \(j\)-th two-letter block is the binary pair consisting of \(x_j\) followed by \(1-x_{j+1}\). Indeed its intermediate height is one, while its even endpoints have heights \(2x_j\) and \(2x_{j+1}\).

**2. Exact progression obstruction.** For a factor of length \(p\) starting after position \(t\), its number of zeros is \((p+H(t+p)-H(t))/2\). For odd \(p\), this quantity has only two possible values across the three equal-length blocks, because each endpoint has height either one (odd position) or zero/two (even position). Hence odd block lengths cannot give abelian three-antipowers. For even \(p=2s\), an odd starting position likewise gives three equal zero counts. At an even starting position \(t=2j\), the zero counts for the three successive blocks are
\[
s+x_{j+s}-x_j,\quad s+x_{j+2s}-x_{j+s},\quad s+x_{j+3s}-x_{j+2s}.
\]
For four bits, the three consecutive differences are pairwise distinct exactly when the first and last bits agree and the four bits are not all equal. To see this, a pairwise-distinct triple of differences in \(\{-1,0,1\}\) must comprise all three values, so it sums to zero and the endpoints agree. Conversely if the endpoints agree, the difference triple sums to zero; if it is not identically zero, it must be a permutation of \((-1,0,1)\). Therefore avoidance is equivalent to the *four-point progression rigidity* property:
\[
\forall j\ge0,\ \forall s\ge1\quad
j+3s\le n\ \land\ x_j=x_{j+3s}
\Longrightarrow x_j=x_{j+s}=x_{j+2s}=x_{j+3s}.
\tag{P}
\]

**3. Classifying rigid binary codes.** Consider maximal constant runs of the code \(x_0x_1\cdots x_n\), beginning and ending with a run of zeros. Any internal run of length two creates the forbidden four-term progression of step one \(ABBA\) (with \(A\ne B\)). If an internal run has length one, then both adjacent runs must also have length one: otherwise a step-one progression \(AABA\) or \(ABAA\) violates (P). Repeating this argument propagates length-one runs through the entire code, leaving a fully alternating sequence. Since its endpoints are zero, this case is \((01)^{n/2}0\) in the height code, with even \(n\).

Otherwise all internal runs have length at least three. The following crossing observation rules out five or more runs and bounds any three-run code. Suppose three consecutive maximal runs are \(A^aB^bA^c\), where \(a,c\ge1\) and \(b\ge3\). If \(a+c\ge4\), the possible distances between positions in the two outer \(A\)-runs include each of \(b+1,b+2,b+3\); one of those distances equals \(3s\) for an integer \(s\ge1\) satisfying \(s\le b\). Choose positions in the outer runs at that distance. Were neither interior point of their four-term progression inside the middle \(B\)-run, these two interior points would straddle it, so their mutual separation would be at least \(b+1\), contradicting \(s\le b\). Thus the progression has equal outer bits but a nonconstant interior, violating (P).

There cannot be five or more runs: then the third run is internal and has length at least three, while the first three runs are \(A^aB^bA^c\) with \(a\ge1\), \(b\ge3\), \(c\ge3\), contradicting the crossing observation. Consequently the code is either constantly zero, fully alternating, or has exactly three runs \(0^a1^b0^c\). In the latter case \(b\ge3\) and the crossing observation imposes \(a+c\le3\). Therefore \((a,c)\) is one of \((1,1),(1,2),(2,1)\). For a three-run code, any progression violating (P) has its endpoints in the distinct outer zero-runs: if both lie inside one constant run they cannot violate (P), and endpoints within the central one-run also cannot. The outer-run endpoint distance is only \(n\) when \((a,c)=(1,1)\), and ranges over \(n-1,n\) when \(a+c=3\). Hence (P) holds precisely when \(3\nmid n\) in the first case, or \(n\equiv2\pmod3\) in the latter two. The minimum central-run length \(b\ge3\) gives \(n\ge4\) and \(n\ge5\), respectively.

**4. Translation and enumeration.** The all-zero code corresponds to \((01)^n\), the alternating code to \((0011)^{n/2}\), and the three-run codes to the remaining three displayed word templates. The cases are disjoint because their codes have different run structures or outer-run lengths. The displayed formula follows by counting them. This proves necessity and sufficiency for every \(n\ge1\).

## Verification
The companion script `verify_height2_antipower.py` performs independently written direct factor counting, a separate four-point progression test, and a separate predicted-family generator. It enumerates every height-at-most-two Dyck word for all \(1\le n\le15\), checking 32,767 words, and directly tests each proposed survivor for every \(16\le n\le150\). Run `python3 verify_height2_antipower.py`. Expected concluding line: `HEIGHT_TWO_ABELIAN_ANTIPOWER_PASS lengths=1..15 total= 32767 constructive_lengths=16..150`. These finite checks are consistency tests; the preceding argument proves the general theorem.

## Relationship to prior work
Fici, Postic, and Silva (2018) investigate abelian anti-powers in infinite words, notably morphic constructions and paperfolding. The survey by Fici and Puzynina (2022) discusses abelian repetitions and anti-powers. Mol, Rampersad, and Shallit (2023) study Dyck words with other repetition-avoidance conditions. The present result concerns a different joint restriction: *finite* Dyck words of maximum height two avoiding abelian three-antipowers, including an exact complete classification by semilength. The four-point progression translation is essential to this restriction. The result does not imply any general classification of unrestricted-height Dyck words or all abelian antipowers of arbitrary order.

## Limitations
The classification applies only to Dyck words of height at most two and to abelian three-antipowers, not to higher nesting height or avoidance of larger numbers of blocks. Finite tests do not replace the all-length proof. Literature comparison is based on available sources, and independent validation has not been performed.

## References
- G. Fici, M. Postic, M. Silva, *Abelian Anti-Powers in Infinite Words* (2018), arXiv:1810.12275. First public version 2018-10-29.
- G. Fici and S. Puzynina, *Abelian Combinatorics on Words: A Survey* (2022), arXiv:2207.09937.
- L. Mol, N. Rampersad, and J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences* (2023), arXiv:2301.06145.
