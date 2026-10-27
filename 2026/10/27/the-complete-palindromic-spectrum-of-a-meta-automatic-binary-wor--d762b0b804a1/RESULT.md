# The complete palindromic spectrum of a meta-automatic binary word

## Finding

Let \(\varphi\) be the \(4\)-uniform morphism on \(\{0,1,2,3\}\) given by
\[
\varphi(0)=\mathtt{0112},\quad
\varphi(1)=\mathtt{1230},\quad
\varphi(2)=\mathtt{2301},\quad
\varphi(3)=\mathtt{3023},
\]
and define the binary coding \(\pi(0)=\pi(2)=0\), \(\pi(1)=\pi(3)=1\).
Let \(u=\pi(\varphi^{\omega}(0))\), the meta-automatic word \(\mathcal M_1\) of Campbell and Cloitre [1]. For each integer \(n\ge1\), let \(P(n)\) be the number of **distinct** length-\(n\) palindromic contiguous factors of \(u\). Then
\[
P(n)=\begin{cases}
2,&1\le n\le9\text{ or }n\in\{14,16\},\\
3,&n\in\{10,12\},\\
0,&\text{all other positive integers }n.
\end{cases}
\]
Consequently, \(u\) has **exactly 28 distinct nonempty palindromic factors**. Its longest palindromes have length \(16\), and they are exactly `1010010110100101` and `1010101001010101`.

Write \(u_{[0,N)}\) for the length-\(N\) prefix and define the palindromic defect of a finite word \(w\) by \(\operatorname{Def}(w)=|w|+1-\#\operatorname{Pal}(w)\), where the empty word counts as one palindrome. The precise stabilization law is
\[
\operatorname{Def}(u_{[0,N)})=N-28\qquad\text{for all }N\ge196.
\]
The threshold \(196\) is sharp: the prefix of length \(195\) contains only \(27\) distinct nonempty palindromes, whereas the prefix of length \(196\) contains all \(28\).

## Assumptions and scope

A factor means an ordinary contiguous finite substring. The fixed point is one-sided, indexed from zero, and well-defined because \(\varphi(0)\) begins with \(0\). The theorem concerns the particular binary coding above, not arbitrary codings or all meta-automatic sequences. Length zero is excluded from \(P\); if extended, \(P(0)=1\).

## Proof

**Step 1: All adjacent state pairs.** Let \(F=\varphi^{\omega}(0)\). Directly computing \(\varphi^4(0)\), a finite word of length \(256\), gives the set
\[
T=\{\mathtt{01},\mathtt{02},\mathtt{03},\mathtt{11},\mathtt{12},
\mathtt{13},\mathtt{21},\mathtt{22},\mathtt{23},\mathtt{30}\}
\]
of adjacent two-letter factors. This set is closed under taking adjacent two-letter factors of \(\varphi(xy)\) whenever \(xy\in T\). The closure is an exact check on ten words of length eight, performed in `verify_palindromes.py`. For the induction, any adjacent pair in \(\varphi^{j+1}(0)\) comes from the image of some adjacent pair in \(\varphi^j(0)\), because every letter image is nonempty. Thus, starting with \(j=4\), no additional pair can appear. Every element of \(T\) actually occurs already in \(\varphi^4(0)\), so \(T\) is precisely the full two-letter factor set of \(F\).

**Step 2: A finite cover of *every* short binary factor.** Since \(\varphi^3\) has constant block length \(64\), the identity \(F=\varphi^3(F)\) partitions \(u=\pi(F)\) into consecutive \(64\)-symbol blocks \(\pi(\varphi^3(F_i))\). Any factor of length \(1\le n\le18\) lies within one block or crosses a single boundary, hence lies in
\[
\pi(\varphi^3(xy))\qquad\text{for some }xy\in T.
\]
Conversely, because every \(xy\in T\) occurs in \(F\), the entire length-\(128\) word \(\pi(\varphi^3(xy))\) occurs in \(u\). Therefore the union of factors of the ten specified length-\(128\) strings gives **exactly** the factors of each length \(n\le18\), not a sample or an approximation.

**Step 3: Exact palindromic factors of lengths through 18.** Test each substring of each of those ten explicit strings against its reversal. The numbers for lengths \(1,2,\ldots,18\), in order, are
\[
(2,2,2,2,2,2,2,2,2,3,0,3,0,2,0,2,0,0).
\]
This small finite comparison is implemented and cross-checked in the standalone standard-library checker `verify_palindromes.py`; the complete list of all 28 distinct palindromes and their first occurrence intervals is in `palindromes.tsv`. In particular, there are no length-\(11\) or length-\(18\) palindromes.

**Step 4: The infinite bound.** Every odd palindrome of length at least \(11\) contains a central palindrome of length \(11\), while every even palindrome of length at least \(18\) contains a central palindrome of length \(18\). Step 3 rules both out. Thus no additional palindromes exist at greater lengths. The two length-\(16\) palindromes from the finite list exist in \(u\), so the maximum length is exactly \(16\), and the full global census contains exactly \(28\) nonempty palindromes.

**Step 5: Sharp prefix defect.** The first appearance intervals recorded in `palindromes.tsv` all lie within the length-\(196\) prefix \(u_{[0,196)}\). The palindrome `1010101001010101` first occurs at zero-based index \(180\), occupying positions \(180\) through \(195\), so it is absent from \(u_{[0,195)}\). The other \(27\) palindromes are already present there. By Step 4, no further palindrome can appear afterward. Counting the empty palindrome gives \(\#\operatorname{Pal}(u_{[0,N)})=29\) for every \(N\ge196\), proving the defect formula and sharpness.

## Verification

Run `python3 verify_palindromes.py` with Python's standard library. Its deterministic output is stored in `verification_output.json`. The program (i) checks the exact adjacent-pair set and substitution closure, (ii) enumerates the ten short-factor-cover words, (iii) tests their palindrome spectrum and both absent critical lengths, (iv) confirms all 28 first appearances in the length-256 prefix, and (v) independently checks the first 4096 coded symbols against the original nested recurrence from OEIS A392736 [2]. It also directly enumerates palindrome sets in a 4096-symbol prefix as an independent finite cross-check. The infinite exhaustiveness follows from the factor-cover and central-subpalindrome arguments in the proof, not from the finite prefix test alone.

## Relationship to prior work

Campbell and Cloitre [1] define the word, prove its four-state base-four DFAO and uniform-morphism representation, and analyze ordinary factor complexity. Their inspected treatment does not determine its palindrome factor spectrum or its prefix palindromic defect. OEIS A392736 [2] records the word and recurrence without this exact invariant. Schaeffer and Shallit [3] give general decision methods for palindromic factors in automatic sequences and calculations for other named sequences; those results do not imply the stated explicit spectrum. Allouche, Baake, Cassaigne, and Damanik [4] develop the general study of palindrome complexity, not the stated word-specific classification.

## Limitations

The exact classification is specific to \(u\); it makes no claim about the palindromic spectra of \(\mathcal M_2\) or unrelated primitive morphisms. The finite computation is exhaustive **only because** the ten-pair cover is proved globally and any longer palindrome forces a prohibited shorter one. It does not constitute an unqualified enumeration of all factors at arbitrary lengths. Historical priority against unindexed or unpublished analyses cannot be guaranteed by bibliographic search alone. No independent external mathematical audit has been performed.

## References

[1] John M. Campbell and Benoît Cloitre, *Meta-automatic Sequences*, arXiv:2602.23395 (first arXiv posting 2026-02-25), especially Theorem 13, Corollary 16, and Section 5. https://arxiv.org/html/2602.23395

[2] *OEIS A392736*, 4-automatic binary sequence with an irreducible nested recurrence. Historical entry supplied by January 21, 2026. https://oeis.org/A392736 ; https://oeis.org/history?seq=A392736

[3] Luke Schaeffer and Jeffrey Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (2015). https://arxiv.org/abs/1508.02074

[4] Jean-Paul Allouche, Michael Baake, Julien Cassaigne, and David Damanik, *Palindrome complexity*, Theoretical Computer Science 292 (2003), 9–31; arXiv:math/0106121. https://arxiv.org/abs/math/0106121
