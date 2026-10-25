# Palindromic richness and exact census of Dyck words with one elevated excursion

## Finding
For integers \(a\ge1\) and \(u,v\ge0\), let
\[
W_{a,u,v}=(01)^u\,0(01)^a1\,(01)^v.
\]
This is a binary Dyck word of semilength \(n=u+v+a+1\), of height at most two, with exactly one irreducible excursion reaching height two. Call a word *rich* when it has as many distinct nonempty palindromic contiguous factors as its length.

**Classification.** The word \(W_{a,u,v}\) is rich exactly when
\[
\min(u,v)<a\quad\text{or}\quad u=v=a.
\]
Its complete palindromic-factor count is
\[
P(W_{a,u,v})=M_0+M_1+\min(2u+1,2a)+\min(2v+1,2a),
\]
where \(M_0=\max\{a,u+\mathbf1_{2\mid u},v+\mathbf1_{2\nmid v}\}\) and \(M_1=\max\{a,u+\mathbf1_{2\nmid u},v+\mathbf1_{2\mid v}\}\).

Let \(R_n\) count the rich words in this one-elevated-excursion family at semilength \(n\). For every \(n\ge2\), setting \(t=\lfloor(n-1)/3\rfloor\) gives
\[
R_n=t(t+1)+\frac{(n-t-1)(n-t)}2+\mathbf1_{3\mid(n-1)}.
\]

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), with \(0\) an opening step and \(1\) a closing step. A Dyck word has nonnegative prefix excess of zeros over ones and zero total excess. An irreducible Dyck excursion is a nonempty Dyck factor returning to level zero only at its end. The unique height-two excursion in this family is \(0(01)^a1\), and the remaining excursions are \(01\). The parameters \(a,u,v\) range independently as stated. The empty Dyck word and words having no height-two excursion are outside the enumerated family.

## Proof
Write \(W=(01)^u0(01)^a1(01)^v\). There is exactly one occurrence each of \(00\) and \(11\): the initial doubled zero and final doubled one of the elevated excursion. A palindrome containing \(00\) must have it at its symmetry center, since otherwise reflection would create a second occurrence of \(00\). The same holds for \(11\). A palindrome cannot contain both doubled pairs, because they cannot both occupy the same symmetry center. All remaining palindromes avoid equal adjacent letters and therefore must be odd-length alternating palindromes. Indeed, an even alternating word cannot be a palindrome.

The maximal alternating blocks cut at the two doubled pairs have lengths \(2u+1\), \(2a\), and \(2v+1\). The first starts and ends with zero, the middle is \((01)^a\), and the third starts and ends with one. An odd alternating block of length \(2s+1\) contributes alternating-palindrome lengths up to \(2s+1\) about its central letter and up to \(2s-1\) about the other letter; an alternating block of even length \(2s\) contributes lengths up to \(2s-1\) about both letters. Thus the number of distinct alternating palindromes centered at zero, respectively one, equals
\[
M_0=\max\{a,u+\mathbf1_{2\mid u},v+\mathbf1_{2\nmid v}\},\qquad
M_1=\max\{a,u+\mathbf1_{2\nmid u},v+\mathbf1_{2\mid v}\}.
\]
(For example, the zero-centered palindromes are exactly \(0,010,01010,\ldots\) through the longest available zero-centered length; this establishes distinctness and completeness.)

The even palindromes centered at the unique \(00\) extend symmetrically for exactly \(\min(2u+1,2a)\) pairs: to its left the alternating arm has length \(2u\), and to its right the arm up to the unique \(11\) has length \(2a-1\); the doubled center itself contributes one pair. The corresponding count for the unique \(11\) is \(\min(2v+1,2a)\). Each centered palindrome has a different even length, and neither group overlaps an odd alternating palindrome or the other group. This proves the displayed exact formula for \(P(W)\).

For richness compare that formula with \(|W|=2(u+v+a+1)\). By reversal and complementation, interchanging \(u\) and \(v\) preserves the number of palindromes; suppose \(u\le v\). If \(u<a\), then the two maxima sum to \(2a\) when \(v<a\), to \(2a+1\) when \(v=a\), and to \(2v+1\) when \(v>a\). In all three cases the exact formula gives \(P(W)=|W|\). If \(u=v=a\), each maximum equals \(a+1\), again giving equality. If \(u=a<v\), the maxima sum to \(2v+1\), one less than needed for equality. Finally, if \(a<u\le v\), their sum is at most \(2v+2\), whereas equality would require \(2(u+v-a+1)\), at least \(2v+4\). These cases exhaust the domain and prove the classification.

At semilength \(n\), fix \(a\) and put \(s=n-a-1=u+v\). There are \(s+1\) parameter pairs in total. Those with both \(u,v\ge a\) number \(\max(0,s-2a+1)\); among these, precisely \(u=v=a\) is allowed when \(s=2a\). Hence the count for this \(a\) is
\[
\min(n-a,2a)+\mathbf1_{n=3a+1}.
\]
Sum over \(1\le a\le n-1\), splitting at \(t=\lfloor(n-1)/3\rfloor\): the first range contributes \(\sum_{a=1}^{t}2a=t(t+1)\), the remaining range contributes \(\sum_{j=1}^{n-t-1}j=(n-t-1)(n-t)/2\), and the indicator contributes once exactly if \(3\mid(n-1)\). This completes the enumeration.

## Verification
The included Python 3 verifier independently constructs words and all distinct palindromic factors by contiguous substring enumeration. It compares the direct count against the explicit four-term expression for all \(10{,}164\) triples with \(1\le a\le21\) and \(0\le u,v\le21\), checks richness equivalence for each, and independently enumerates every semilength \(2\le n\le40\) against the closed count. Expected output: `RICH_SINGLE_EXCURSION_PASS triples= 10164 n=2..40`. These tests are finite corroboration, not the proof for arbitrary parameters.

## Relationship to prior work
The classical theory of rich words characterizes the maximal distinct-palindrome count. Currie, Mol and Rampersad (2019) study repetition thresholds of rich infinite binary words, including restrictions based on avoiding high powers. Their main structural theorem requires a rich infinite word avoiding \(14/5\)-powers and does not supply this finite Dyck-height-two exact classification. The present computation exploits the two unique doubled-letter centers rather than repetition-threshold arguments. The general return-word characterization and rich morphism literature provide background, not an equivalent formula identified here.

## Limitations
The enumeration applies only to Dyck words with exactly one excursion attaining height two, not all Dyck words of height at most two or unrestricted Dyck paths. It is a complete theorem for that natural subclass. Originality against all unindexed sources has not been established; the outcome has undergone self-review but no independent mathematical audit.

## References
1. J. D. Currie, L. Mol and N. Rampersad, *The repetition threshold for binary rich words*, arXiv:1908.03169 (first public 2019-08-08), https://arxiv.org/abs/1908.03169.
2. M. Bucci, A. De Luca, A. Glen and L. Q. Zamboni, *A new characteristic property of rich words*, arXiv:0807.2303, https://arxiv.org/abs/0807.2303.
