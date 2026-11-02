# Exact minimal-unique-factor spectrum of four-run binary words

## Finding
A *minimal unique factor* (MUF, also called a minimal unique substring) of a finite word is a nonempty contiguous factor that occurs exactly once, while every proper nonempty contiguous factor occurs at least twice. Overlapping occurrences are counted separately.

**Classification theorem.** Let \(a,b,c,d\) be arbitrary positive integers and put
\[W=0^a1^b0^c1^d.\]
The entire set of distinct minimal unique factors of \(W\) consists of the following five possible factors, included exactly under their stated conditions:

1. \(10\), always;
2. \(0^{\max(a,c)}\), exactly when \(a\ne c\);
3. \(1^{\max(b,d)}\), exactly when \(b\ne d\);
4. \(0^{\min(a,c)+1}1\), exactly when \(|a-c|\ge2\);
5. \(01^{\min(b,d)+1}\), exactly when \(|b-d|\ge2\).

The five factors are pairwise different. Therefore
\[|\operatorname{MUF}(W)|=1+\mathbf1_{a\ne c}+\mathbf1_{b\ne d}+\mathbf1_{|a-c|\ge2}+\mathbf1_{|b-d|\ge2}.\]
The bit-complemented orientation \(1^a0^b1^c0^d\) has the complemented factor set and identical count.

**Complete length-and-count distribution.** Mark a word's length by \(z\), and its number of minimal unique factors by \(t\). Summing over *both* orientations and all positive run lengths gives the rational bivariate generating function
\[\boxed{F(z,t)=\sum_{\substack{W\text{ binary}\\\operatorname{runs}(W)=4}}z^{|W|}t^{|\operatorname{MUF}(W)|}
=2t\left(\frac{z^2+2tz^3+\dfrac{2t^2z^4}{1-z}}{1-z^2}\right)^2.}\]
Thus the coefficient \([z^nt^k]F\) counts four-run binary words of length \(n\) with exactly \(k\) minimal unique factors.

For each length \(n\ge4\), the largest attainable number is exactly \(\min\{5,n-3\}\). Five are first attainable at length eight, and the extremizers are precisely the words with \(|a-c|\ge2\) and \(|b-d|\ge2\) (or their complements). Their length generating function is
\[\sum_{n\ge8}E_nz^n=\frac{8z^8}{(1-z)^2(1-z^2)^2}.\]
Writing \(j=\lfloor(n-8)/2\rfloor\), for \(n\ge8\) the number of extremizers is explicitly
\[E_n=\begin{cases}
\dfrac43(j+1)(j+2)(2j+3),&n\text{ even},\\[2mm]
\dfrac83(j+1)(j+2)(j+3),&n\text{ odd}.
\end{cases}\]
Moreover \(E_n/(2\binom{n-1}{3})\to1\) as \(n\to\infty\).

## Assumptions and scope
Only nonempty contiguous factors are considered, not scattered subsequences. All four run lengths are positive, ensuring exactly four alternating binary runs. The zero and one alphabet is fixed and labeled; both initial-symbol orientations are included only in the generating functions and length counts, not simultaneously in the displayed five-factor list. Minimality is with respect to all proper nonempty factors; checking the length-one-shorter prefix and suffix suffices because each other proper factor lies in one of those.

## Proof
Let \(\operatorname{occ}_W(u)\) denote the number of starting positions of factor \(u\) in \(W\), allowing overlaps. For a present factor of length at least two, minimal uniqueness is equivalent to
\[\operatorname{occ}_W(u)=1,\qquad
\operatorname{occ}_W(u[1..|u|-1])\ge2,\qquad
\operatorname{occ}_W(u[2..|u|])\ge2.\]

**Unique decreasing boundary.** The digram \(10\) occurs at exactly the second-to-third run boundary. Its one-letter factors \(1\) and \(0\) each occur at least twice, so \(10\) is minimally unique. Any longer factor containing \(10\) has \(10\) as a proper factor and hence cannot be minimally unique. It remains to study factors avoiding \(10\). These are exactly pure powers of one letter or factors \(0^i1^j\) with \(i,j\ge1\).

**Pure powers.** The number of occurrences of \(0^i\) is
\[\max(a-i+1,0)+\max(c-i+1,0).\]
This equals one only for \(i=\max(a,c)\) with \(a\ne c\). Such a run has length at least two and its proper prefix of length \(i-1\) occurs twice inside the same longer run; the same is true of the suffix. Hence it is minimally unique. Replacing \((a,c,0)\) by \((b,d,1)\) gives the second pure-power family.

**Increasing boundaries.** Each factor \(0^i1^j\) with both exponents positive can occur only at either of the two \(01\) boundaries; at each boundary it occurs at most once. Thus
\[\operatorname{occ}_W(0^i1^j)=\mathbf1_{i\le a,\ j\le b}+\mathbf1_{i\le c,\ j\le d}.\]
In particular \(01\) occurs twice and is not unique.

If \(i,j\ge2\) and \(0^i1^j\) were minimally unique, its prefix \(0^i1^{j-1}\) and suffix \(0^{i-1}1^j\) would each have to occur twice. Being mixed factors, this forces respectively \(i\le\min(a,c)\) and \(j\le\min(b,d)\), which would also make the full factor occur twice; contradiction.

Suppose \(i\ge2,j=1\). Repetition of the mixed suffix \(0^{i-1}1\) forces \(i-1\le\min(a,c)\). Uniqueness of the full factor forces \(i>\min(a,c)\); hence \(i=\min(a,c)+1\). Its pure-zero prefix occurs at least twice if and only if the longer zero run has at least \(i+1\) letters, equivalently \(|a-c|\ge2\). Exactly this condition yields the fourth listed factor. Interchanging the roles of exponents and letters, the case \(i=1,j\ge2\) gives the fifth factor under \(|b-d|\ge2\). This exhausts all factors, proving the classification.

**Generating function and sharp maximum.** Let \(\delta(x,y)\) equal \(0,1,2\) according as \(|x-y|=0,1,\ge2\). The count just proved is \(1+\delta(a,c)+\delta(b,d)\). Pairwise sums over two positive run lengths are independent; their joint length/count enumerator is
\[P(z,t)=\sum_{x,y\ge1}z^{x+y}t^{\delta(x,y)}
=\frac{z^2}{1-z^2}+\frac{2tz^3}{1-z^2}+\frac{2t^2z^4}{(1-z)(1-z^2)}.\]
Here the three terms count equal lengths, lengths differing by one, and lengths differing by at least two. The fixed \(10\) contributes \(t\), and the two starting-symbol orientations contribute the factor \(2\), so \(F(z,t)=2tP(z,t)^2\), as asserted.

A pair contributing \(\delta\in\{0,1,2\}\) has total length at least \(2+\delta\). Consequently \(n\ge4+\delta(a,c)+\delta(b,d)\), giving \(|\operatorname{MUF}(W)|\le\min\{5,n-3\}\). For lengths four through seven equality is achieved by run pairs of respective gap types \((0,0),(1,0),(2,0),(2,1)\); for every \(n\ge8\), use one pair with run lengths \((1,n-5)\) and the other with \((1,3)\). For the five-factor case both pairs have gaps at least two. Their pair enumerator is \(2z^4/((1-z)(1-z^2))\), yielding the stated \(E_n\) generating function. Expanding \((1-z^2)^{-2}\) and \((1-z)^{-2}\) gives the displayed parity formulas. Finally \(E_n\sim n^3/3\) while the total number of four-run binary words is \(2\binom{n-1}{3}\sim n^3/3\), proving the density statement.

## Verification
The accompanying standalone standard-library program `verify.py` constructs literal occurrence tables for all \(7^4=2401\) quadruples \(1\le a,b,c,d\le7\), checks the complete factor sets rather than only their sizes, and compares the rational-generating-function coefficients to direct word enumeration for lengths four through twenty-two. It also verifies the extremal parity formula. The observed result is `VERIFY_OK complete_quadruples=2401 literal_mus=9457 length_coefficients=95 max_length=22 maximum=5 first_attainment=8`.

These finite calculations are checks on the algebra and boundary cases. The unrestricted conclusions depend on the preceding proof, not on extrapolation from enumeration.

## Relationship to prior work
Mieno, Inenaga, Bannai and Takeda (MFCS 2016) establish the general bound of at most \(2r-1\) minimal unique substrings for a string with \(r\) runs and a method for computing them from run-length encoding. For four runs this gives an upper bound of seven, whereas the theorem above gives a sharp upper bound of five in the alternating binary family, classifies every attaining parameter choice, and enumerates their lengths. Their longest-unique-run lemma already covers the two pure-power factors; the distinct new calculation is the exact interaction of the two repeated \(01\) boundaries and its joint length/count distribution.

Mieno and collaborators (2019 preprint and 2021 Algorithmica article) study general sliding-window changes and enumeration algorithms for minimal unique substrings, not this fixed-family coefficient formula. Later compact representations and BWT-based enumeration concern algorithmic access to minimal unique substrings of arbitrary input. A general-purpose algorithm can recover individual instances, but the inspected results do not state the present uniform factor classification or rational bivariate enumeration. This literature comparison is limited to the material actually inspected.

## Limitations
The theorem concerns exactly four alternating binary runs, not arbitrary run counts, arbitrary alphabets, minimal absent factors, or scattered subsequences. The family is deliberately the first binary case with two occurrences of \(01\) and one of \(10\), so its exact exceptional-run behavior is meaningful but specialized. The generic RLE algorithms in earlier literature remain more general algorithmically. An unlocated equivalent specialization or enumeration is possible. Independent external verification has not been performed.

## References
1. T. Mieno, Y. Kuhara, T. Akagi, Y. Fujishige, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window*, arXiv:1909.02804 (first public September 6, 2019), https://arxiv.org/abs/1909.02804.
2. T. Mieno, S. Inenaga, H. Bannai, M. Takeda, *Shortest Unique Substring Queries on Run-Length Encoded Strings*, MFCS 2016, DOI:10.4230/LIPIcs.MFCS.2016.69, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.69.
3. T. Mieno, Y. Fujishige, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Computing Minimal Unique Substrings for a Sliding Window*, Algorithmica 84 (2022), 670–693; first online August 20, 2021, DOI:10.1007/s00453-021-00864-1.
4. T. Mieno, D. Köppl, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Space-Efficient Algorithms for Computing Minimal/Shortest Unique Substrings*, arXiv:1905.12854 (2019), https://arxiv.org/abs/1905.12854.
5. T. Nishimoto, Y. Tabei, *R-enum: Enumeration of Characteristic Substrings in BWT-runs Bounded Space*, arXiv:2004.01493 (2020), https://arxiv.org/abs/2004.01493.
