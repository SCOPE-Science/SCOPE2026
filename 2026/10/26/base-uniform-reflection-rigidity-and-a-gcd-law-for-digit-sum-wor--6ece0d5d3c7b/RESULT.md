# Base-uniform reflection rigidity and a gcd law for digit-sum words

## Finding

For integers \(b\ge3\) and \(m\ge3\), put \(d=\gcd(b-1,m)\), and define the generalized Thue–Morse word \(t_{b,m}(j)=s_b(j)\bmod m\), where \(s_b\) is the sum of the base-\(b\) digits. Write \(C_{b,m}(n)\) for the number of its distinct contiguous length-\(n\) factors and \(r_{b,m}(n)\) for the number of such factors up to ordinary reversal.

**Theorem.** No length-four factor of \(t_{b,m}\) has its reversal occurring anywhere in the word, so the same is true for every factor of length at least four. Moreover, no two *distinct* length-three factors are reversals of one another. For all \(b,m\ge3\),
\[
\begin{aligned}
r_{b,m}(0)&=1,\\
r_{b,m}(1)&=m,\\
r_{b,m}(2)&=\begin{cases}\dfrac{m(m+1)}2,&d=1,\\ \dfrac{m^2}{4},&d=2,\\ \dfrac{m^2}{d},&d>2,\end{cases}\\
r_{b,m}(3)&=\dfrac{2m^2}{d}-m,\\
r_{b,m}(4)&=\dfrac{3m^2}{d}-2m,\\
r_{b,m}(n)&=C_{b,m}(n)\qquad(n\ge3).
\end{aligned}
\]
The already-published exact factor-complexity formula of Starosta [2, Table 2], including its periodic branch, supplies all the last line's explicit values. The reflection obstruction has a sharp length threshold: when \(d\le2\), length-three palindromes occur but no reversed factor occurs from length four; when \(d>2\), no factor of length at least two has its reversal present. The cutoff-three statement in the first case refers to palindromes, not distinct reversed pairs.

## Assumptions and scope

Indices start at zero, the alphabet is \(\mathbb Z/m\mathbb Z\), and all displayed letter additions are modulo \(m\). Factors are contiguous blocks, not scattered subsequences. Ordinary reversal reverses the order without complementing or permuting the symbols. Quantifiers cover every integer base \(b\ge3\), every modulus \(m\ge3\), and every nonnegative factor length. Both aperiodic cases and the periodic cases \(b\equiv1\pmod m\) are included. The ordinary binary-base family \(b=2\) is outside the newly assessed scope.

## Proof

**Lemma 1 (complete adjacency language).** The exact set of ordered length-two factors is
\[
P=\{(a,c)\in(\mathbb Z/m\mathbb Z)^2:c-a\equiv1\pmod d\},\qquad d=\gcd(b-1,m).
\]
Indeed, increasing a base-\(b\) integer \(q\) by one changes its digit sum by \(1-k(b-1)\), where \(k\) is its number of trailing digits equal to \(b-1\). This forces the congruence. Conversely, for any \(a,c\) satisfying that congruence, choose a nonnegative \(k\) solving \(c-a\equiv1-k(b-1)\pmod m\). Choose \(u\ge0\) with \(s_b(u)\equiv a-k(b-1)\pmod m\), possible by taking an integer whose base-\(b\) expansion contains the required number of ones. Set \(q=b^k(bu+1)-1\). Then \(s_b(q)=s_b(u)+k(b-1)\equiv a\), whereas \(s_b(q+1)=s_b(u)+1\equiv c\), as required. Thus \(|P|=m^2/d\).

**Lemma 2 (local increment structure).** For each \(q\ge0\) and \(0\le j<b\),
\[
t_{b,m}(bq+j)=t_{b,m}(q)+j.
\]
Call an adjacent pair internal if both indices belong to the same length-\(b\) substitution block. Its letter increment is always \(+1\). Every block of four consecutive positions contains at most one boundary between substitution blocks, because \(b\ge3\). Consequently every length-four factor has at least two adjacent increments equal to \(+1\). Its reversal, if present, would have at least two adjacent increments equal to \(-1\). Since \(+1\ne-1\pmod m\) for \(m\ge3\), no actual length-four factor can have two \(-1\) increments. This proves the length-four assertion without finite sampling. If a longer factor and its reversal both occurred, their respective four-letter prefix and suffix would give a reversed length-four pair; hence none does.

Every three-position window similarly has at least one internal adjacency, of increment \(+1\). If two distinct length-three factors were reversals, one factor would need both a \(+1\) and a \(-1\) increment to allow its reversed copy to have an internal \(+1\). The only two such increment patterns are \((+1,-1)\) and \((-1,+1)\), which define palindromes. Therefore any reversed length-three pair must be the same palindrome.

**Lemma 3 (small factor counts).** By Lemma 1 and the block recurrence, the full length-three factor set is the union
\[
\begin{aligned}
U&=\{(a,a+1,c):c-a\equiv2\pmod d\},\\
V&=\{(a,c,c+1):c-a\equiv1\pmod d\},
\end{aligned}
\]
where \(a,c\in\mathbb Z/m\mathbb Z\). The first set comes from a window with two positions at the end of one substitution block; the second from a window with two positions at the beginning of the next. Fully internal three-position windows already belong to the two displayed families. Each family has \(m^2/d\) members, and their intersection consists of exactly the \(m\) arithmetic triples \((a,a+1,a+2)\). Thus \(C_{b,m}(3)=2m^2/d-m\). Exactly \(2m\) length-three palindromes occur when \(d\mid2\), and none when \(d>2\): the palindrome conditions in the two displayed families respectively require \(0\equiv2\pmod d\) and \(-1\equiv1\pmod d\). The two palindrome families do not overlap because \(m\ge3\).

For length four, exactly the following three boundary-window families occur (fully internal factors, when \(b\ge4\), are already included):
\[
\begin{aligned}
F&=\{(a,a+1,a+2,c):c-a\equiv3\pmod d\},\\
G&=\{(a,a+1,c,c+1):c-a\equiv2\pmod d\},\\
H&=\{(a,c,c+1,c+2):c-a\equiv1\pmod d\}.
\end{aligned}
\]
Each family has \(m^2/d\) members; every two, and all three, meet exactly in the \(m\) all-increment-\(+1\) progressions \((a,a+1,a+2,a+3)\). Inclusion-exclusion therefore yields \(C_{b,m}(4)=3m^2/d-2m\). The full-language descriptions are justified by Lemma 1, which realizes every required source adjacency.

**Reversal orbits.** All \(m\) letters occur. By Lemma 2 and the preceding argument, every length-three or longer factor forms a singleton reversal class within the language, so \(r_{b,m}(n)=C_{b,m}(n)\) for \(n\ge3\). At length two, a factor \((a,c)\in P\) has a reversed companion exactly when both \(c-a\equiv1\) and \(a-c\equiv1\pmod d\), equivalently \(d\mid2\). For \(d=1\), all \(m^2\) pairs occur, including \(m\) palindromes, giving \(m(m+1)/2\) reversal classes. For \(d=2\), all admissible pairs have opposite residue parity, so none is a palindrome, each has its reversed companion, and there are \(m^2/4\) classes. For \(d>2\), no admissible pair has its reversal present, so all \(m^2/d\) pairs give distinct classes. This proves every assertion. \(\square\)

## Verification

The self-contained `verify.py` tests the exact adjacency and short-factor sets symbolically for all 104 parameter pairs \(3\le b\le10\), \(3\le m\le15\), checking the gcd formulas and the absence of distinct reverse companions. It independently enumerates actual digit-sum prefixes for selected bases 3 through 6 and moduli 3 through 6; 39 length-two/three/four factor sets agree exactly with the symbolic predictions, and every tested factor of lengths five through eight lacks its reversal. Execute `python3 verify.py` without external packages. The infinite proof is the two-internal-adjacency argument and adjacency-realization lemma, not extrapolation from prefixes.

## Relationship to prior work

Allouche, Campbell, Li, Shallit and Stipulanti [1, Question 62] asked how reflection complexity generalizes beyond the classical Thue–Morse word and reported the base-two, modulus-three case. The present theorem addresses **every base at least three and every modulus at least three**, and reveals a previously unstated \(\gcd(b-1,m)\) trichotomy of short reflection classes, including periodic and aperiodic words.

Starosta [2] previously described the length-two and length-three factor languages and determined all factor-complexity values for arbitrary base and modulus. Those results are acknowledged rather than claimed anew; the new step is the base-uniform absence of distinct reverse factors beyond the sharp cutoff, with resulting reflection orbits and short-length dichotomy. Allouche and Shallit [3] established relevant ordinary-palindrome restrictions in digit-sum sequences. Palindrome avoidance by itself does not exclude two *different* mutually reversed factors, so it does not supply the reflection theorem without the new argument. The base-two all-modulus reflection family has also been recorded separately and is expressly not presented as new here.

## Limitations

The claim is restricted to integer bases \(b\ge3\) and alphabets of size \(m\ge3\). The factor-complexity series is inherited from [2] rather than reproved, while the explicit short counts and reflection comparison are proved here. The theorem does not treat other digit statistics, scattered subsequences, or reflection combined with nontrivial alphabet permutations. Searches cannot exclude unpublished or differently indexed equivalent results; no independent mathematical audit has been performed.

## References

[1] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, first public 2024-06-13, especially Question 62. https://arxiv.org/abs/2406.09302

[2] Š. Starosta, *Generalized Thue-Morse words and palindromic richness*, arXiv:1104.2476 (2011), especially Properties IV–V and Table 2. https://arxiv.org/abs/1104.2476

[3] J.-P. Allouche and J. Shallit, *Sums of Digits, Overlaps, and Palindromes*, Discrete Mathematics & Theoretical Computer Science 4 (2000), 1–10, especially the ordinary-palindrome result. https://dmtcs.episciences.org/282
