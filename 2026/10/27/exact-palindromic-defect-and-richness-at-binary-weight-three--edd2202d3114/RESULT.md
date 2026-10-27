# Exact palindromic defect and richness at binary weight three

## Finding
For every quadruple of nonnegative integers \(a,b,c,d\), consider the finite binary word
\[
w=0^a1\,0^b1\,0^c1\,0^d.
\]
Let \(\operatorname{Pal}(w)\) denote the set of *distinct contiguous palindromic factors*, including the empty word, and define its palindromic defect as
\[
\mathcal D(w)=|w|+1-|\operatorname{Pal}(w)|.
\]
Then the exact all-parameter law is
\[
\boxed{\mathcal D(w)=
 \begin{cases}
 0,&b=c,\\
 \max\{0,\min(a,d)-\max(b,c)\},&b\ne c.
 \end{cases}}
\]
Consequently, a word with three ones is non-rich precisely when its two inner zero gaps are unequal and **each outer gap is strictly longer than both inner gaps**. Every binary word with at most two ones is rich (has defect zero).

For every length \(n\ge 3\), the maximum defect among binary words of length \(n\) with exactly three ones is
\[
\boxed{\max_w\mathcal D(w)=\max\{0,\lfloor(n-6)/2\rfloor\}.}
\]
For \(n\ge8\), all maximizers are exactly the words with \(\{b,c\}=\{0,1\}\) and \(\{a,d\}=\{\lfloor(n-4)/2\rfloor,\lceil(n-4)/2\rceil\}\); either ordering of the two pairs is allowed. Thus the first non-rich binary words with only three ones occur at length eight, and there are precisely two such words: `00101100` and `00110100`. The existence and description of the shortest non-rich binary words at length eight was established previously; the new claim is the uniform sparse-weight defect law and its complete restricted extremal profile.

## Assumptions and scope
A factor means a *contiguous substring*, not a scattered subsequence. The alphabet is exactly \(\{0,1\}\); zero exponents are allowed, so adjacent ones and empty outer gaps are included. All counts distinguish factor strings, not their different occurrences. Words may be nonprimitive or palindromic. The formula applies to *all* nonnegative integral quadruples. The extremum is taken only within the class containing exactly three ones; no assertion about unrestricted maximum defect is made.

## Proof
Put
\[
\begin{aligned}
M&=\max(a,b,c,d),\\
H&=\max\{\min(a,b),\min(b,c),\min(c,d)\},\\
U&=\min(a,c),\qquad V=\min(b,d),\qquad Q=\min(a,d).
\end{aligned}
\]
Every palindrome has an equal number of ones on both sides of its center. Group the *distinct palindromic factors* by their number of ones.

* With no ones, precisely \(0,0^2,\ldots,0^M\) occur, giving \(M\) nonempty palindromes.
* With one one, each palindrome is \(0^k1 0^k\). It can be centered at the first, second or third one and occurs if and only if \(0\le k\le H\). This gives \(H+1\) distinct factors.
* With two ones, the two ones must be consecutive among the three occurrences. One family is \(0^k1 0^b1 0^k\) with \(0\le k\le U\); the other is \(0^k1 0^c1 0^k\) with \(0\le k\le V\). Each family has \(U+1\) or \(V+1\) members. They are disjoint when \(b\ne c\); when \(b=c\), their intersection has exactly \(\min(U,V)+1\) members.
* A factor containing all three ones can be a palindrome only when \(b=c\). In that case all and only \(0^k1 0^b1 0^b1 0^k\), for \(0\le k\le Q\), occur, giving \(Q+1\) members.

In particular the total number \(P\) of *nonempty* distinct palindromic factors is exactly
\[
P=M+H+U+V+3+\mathbf1_{b=c}\bigl(Q-\min(U,V)\bigr).
\]
This identity accounts for the otherwise easily overlooked duplicate two-one palindromes when the inner gaps are equal. Since \(|w|=a+b+c+d+3\),
\[
\mathcal D(w)=a+b+c+d-M-H-U-V
 -\mathbf1_{b=c}\bigl(Q-\min(U,V)\bigr). \tag{1}
\]

We prove the required min-max identity without assuming any order among the four gaps:
\[
a+b+c+d-M-H-U-V=\max\{0,\min(a,d)-\max(b,c)\}.\tag{2}
\]
For every positive integer \(t\), write \(A=[a\ge t]\), \(B=[b\ge t]\), \(C=[c\ge t]\), \(E=[d\ge t]\), with each bracket denoting a Boolean value in \(\{0,1\}\). The level-\(t\) contribution to the left side of (2) is
\[
A+B+C+E-\mathbf1_{A\lor B\lor C\lor E}
-\mathbf1_{(A\land B)\lor(B\land C)\lor(C\land E)}
-AC-BE.\tag{3}
\]
For an occupied subset of size zero or one, (3) is zero. For a two-element subset it vanishes for each adjacent pair \(AB,BC,CE\) and each opposite pair \(AC,BE\), but equals one for the sole remaining pair \(AE\). For a three-element subset there is at least one adjacent pair and exactly one opposite pair, giving \(3-1-1-1=0\); for all four elements it is \(4-1-1-1-1=0\). Therefore (3) is exactly \(AE(1-B)(1-C)\). Summing all levels counts integers \(t\) with \(\max(b,c)<t\le\min(a,d)\), proving (2).

If \(b\ne c\), the indicator in (1) is zero and (2) immediately proves the asserted formula. If \(b=c=q\), then
\[
\min(U,V)=\min(a,d,q),\qquad
Q-\min(U,V)=\max\{0,Q-q\}.
\]
This is precisely the right side of (2), so the two terms cancel in (1), giving defect zero. This completes the exact classification.

For at most two ones, the zero-, one- and two-one palindromes of \(0^a1\,0^b1\,0^c\) number respectively \(\max(a,b,c)\), \(\max(\min(a,b),\min(b,c))+1\), and \(\min(a,c)+1\). A three-variable version of the same level argument shows the sum is \(a+b+c+2\), the full word length; hence its defect is zero. Deleting a one covers the cases of zero or one one directly.

For the extremum, put \(m=n-3=a+b+c+d\). If \(\mathcal D(w)>0\), then \(b\ne c\), \(h=\max(b,c)\ge1\), and \(b+c\ge1\). Thus
\[
\mathcal D(w)=\min(a,d)-h
\le \left\lfloor\frac{m-(b+c)}2\right\rfloor-h
\le\left\lfloor\frac{m-1}2\right\rfloor-1
=\left\lfloor\frac{n-6}2\right\rfloor.
\]
For \(n\ge8\), equality requires \(\{b,c\}=\{0,1\}\) and an optimally balanced pair of outer gaps with sum \(m-1=n-4\). The stated maximizers attain equality. For \(3\le n<8\), positive defect would require \(a,d\ge2\) and \(b+c\ge1\), forcing \(n\ge8\). This establishes the complete extremal formula and its equality cases.

## Verification
The standalone `verify.py` enumerates palindromic factors independently from substrings. Running `python3 verify.py` gives:

`PASS: 16 Boolean levels; 6561 three-marker words; 1015 zero-to-two-marker words; exact maxima at lengths 3..22.`

The finite checks are corroboration, **not** proof of the all-integer statement. The exhaustive proof above uses the explicit factor taxonomy, the sixteen-pattern level identity, and sharp outer-gap balancing. No external lemma is required for the parameter formula.

## Relationship to prior work
Glen, Justin, Widmer and Zamboni introduced and developed the rich-word viewpoint and complete-return characterization; their 2008 arXiv version predates the present class calculation. The related 2008 study of Blondin Massé, Brlek, Frosini, Labbé and Rinaldi proves that the first binary words of defect one have length eight and lists all four of them under letter complementation, including the two with three ones. Consequently the *length-eight example itself is not claimed as new*. Their general minimum-length law for given defect does not supply the all-parameter formula with a fixed number of ones or the restricted extremizers. Guo, Shallit and Shur study counts of rich words and related palindrome structures, but their available abstract does not assert the sparse-weight defect identity. The exact fixed-weight formula and sharp sparse extremizers have not been found in the inspected material; this is a qualified priority comparison, not proof of absence from all literature.

## Limitations
The theorem concerns only words with at most three ones, with zero as the other symbol. A global interchange of the letters transfers it to words with at most three zeros. It does not extend without new arguments to four ones, arbitrary alphabets or cyclic factors. The first defective length-eight examples are explicitly prior art. The relevant original rich-word papers were inspected through accessible text and sections; one author-hosted PDF could not be re-rendered during retrieval, and the full text of the 2015 palindromes/antipalindromes preprint was not obtained. These access limits leave residual priority uncertainty. Independent mathematical audit has not been performed.

## References
1. A. Glen, J. Justin, S. Widmer and L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656, first publicly posted 2008-01-10; subsequently *European Journal of Combinatorics* 30 (2009), 510–531. https://arxiv.org/abs/0801.1656
2. A. Blondin Massé, S. Brlek, A. Frosini, S. Labbé and S. Rinaldi, *Reconstructing Words from a Fixed Palindromic Length Sequence*, IFIP TCS 2008, pp. 101–114; preprint arXiv:0806.3710. https://www.researchgate.net/publication/225759529_Reconstructing_words_from_a_fixed_palindromic_length_sequence
3. C. Guo, J. Shallit and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112, 2015. https://arxiv.org/abs/1503.09112
