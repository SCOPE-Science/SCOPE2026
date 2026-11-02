# Exact binary three-deck ambiguity at Hamming weight three

## Finding

For every integer \(n\ge3\), among binary words of length \(n\) with exactly three ones, every three-deck equivalence class has at most two elements. All nontrivial classes are described explicitly, and their exact number has a rational generating function.

Write a word uniquely as
\[
 w=0^a1\,0^b1\,0^c1\,0^d,\quad a,b,c,d\in\mathbb Z_{\ge0},\quad a+b+c+d=n-3.
\]
Its three-deck is the vector of counts of the eight length-three scattered subsequences, with multiplicity. A distinct word has precisely the same deck if and only if
\[
 b\ne c,\quad 3\mid(c-b),\quad a-t\ge0,\quad d+t\ge0,\qquad t=(c-b)/3,
\]
in which case that unique partner has gap tuple
\[
 (a-t,c,b,d+t).
\]
Let \(P_n\) count unordered pairs of distinct three-deck-equivalent words in this constant-weight set, or equivalently the number of two-element equivalence classes. Then
\[
 \sum_{n\ge3}P_nz^n=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)},\qquad
 P_n=\sum_{t=1}^{\lfloor(n-3)/4\rfloor}\ \sum_{b=0}^{\lfloor(n-3-4t)/2\rfloor}(n-2-4t-2b).
\]
Consequently the exact maximum codebook size for this restricted three-deck reconstruction channel is
\[
 A_{3,3}(n)=\binom n3-P_n,\qquad
 P_n=\frac{n^3}{48}+O(n^2),\qquad
 \frac{A_{3,3}(n)}{\binom n3}\longrightarrow\frac78.
\]
The first nontrivial pair occurs at length seven: `0110001` and `1000110` (previously recorded as a finite example in the integer-sequence literature).

## Assumptions and scope

The alphabet is \(\{0,1\}\), words have exactly three occurrences of \(1\), lengths satisfy \(n\ge3\), and a scattered subsequence counts strictly increasing triples of positions. Two words are indistinguishable if their counts agree for each of the eight three-letter binary patterns. The codebook may contain only weight-three words; the statement does not describe all binary three-deck classes of unrestricted Hamming weight. At fixed \(n\ge3\), the length-three deck determines all shorter decks by double counting extensions of a shorter subsequence, so the result also applies to the usual equivalence defined using lengths at most three.

## Proof

For a gap tuple \((a,b,c,d)\), direct position counting gives
\[
\begin{array}{ll}
N_{011}=3a+b,&N_{101}=2b+2c,\\
N_{110}=c+3d,&N_{001}=\binom a2+\binom{a+b}2+\binom{a+b+c}2.
\end{array}
\]
The other mixed-pattern entries are
\[
\begin{aligned}
N_{010}&=a(b+c+d)+(a+b)(c+d)+(a+b+c)d,\\
N_{100}&=\binom{b+c+d}2+\binom{c+d}2+\binom d2.
\end{aligned}
\]
Also \(N_{000}=\binom{n-3}3\), \(N_{111}=1\), with binomial coefficients interpreted as zero when the upper index is too small.

Suppose another gap tuple \((a',b',c',d')\) has the same three-deck. Equality of \(N_{011}\) implies \(b'-b=3(a-a')\), so some integer \(t\) satisfies \(a'=a-t\), \(b'=b+3t\). Equality of \(N_{101}\) gives \(c'=c-3t\), and equality of \(N_{110}\) gives \(d'=d+t\). All other gap tuples sharing these three entries therefore lie on the one-dimensional integral line
\[
 (a',b',c',d')=(a-t,b+3t,c-3t,d+t).
\]
Substituting into the formula for \(N_{001}\) and simplifying gives the exact difference
\[
 N_{001}(a',b',c',d')-N_{001}(a,b,c,d)=t(b-c+3t).
\]
Thus \(t=0\) or \(t=(c-b)/3\). The first is the original word. In the second case \(b'=c\), \(c'=b\), so a distinct partner exists precisely under the stated integer and nonnegative-gap constraints. Conversely, at this second root direct substitution shows that the remaining mixed entries change respectively by
\[
 \Delta N_{010}=-2t(b-c+3t)=0,\qquad
 \Delta N_{100}=t(b-c+3t)=0.
\]
The remaining entries are already fixed, proving the partner is deck-equivalent. There are only the two possible roots, hence no equivalence class has more than two elements. The transformation is an involution: interchanging \(b\) and \(c\) changes \(t\) to \(-t\).

Orient each nontrivial pair by taking the representative with \(c>b\). Write
\[
 t=(c-b)/3\ge1,\quad a=t+A,\quad c=b+3t,\quad d=D,
\]
where \(A,b,D\) are arbitrary nonnegative integers. The number of zeros is
\[
 n-3=4t+2b+A+D.
\]
Each such quadruple represents exactly one unordered collision pair. Taking the ordinary generating function gives
\[
 \sum_{n\ge3}P_nz^n=z^3\Bigl(\sum_{t\ge1}z^{4t}\Bigr)
  \Bigl(\sum_{b\ge0}z^{2b}\Bigr)
  \Bigl(\sum_{A\ge0}z^A\Bigr)
  \Bigl(\sum_{D\ge0}z^D\Bigr)
 =\frac{z^7}{(1-z^4)(1-z^2)(1-z)^2}.
\]
For fixed \(n,t,b\), the number of pairs \((A,D)\) is \(n-2-4t-2b\), proving the coefficient formula. Since all fibers have size one or two, selecting one representative from each gives the maximum constant-weight-three codebook size \(\binom n3-P_n\); choosing two from one fiber would violate distinguishability. Near \(z=1\), the generating function equals \((8(1-z)^4)^{-1}+O((1-z)^{-3})\). The other poles are of order at most two, so coefficient extraction yields \(P_n=n^3/48+O(n^2)\). Using \(\binom n3=n^3/6+O(n^2)\) gives the limiting ratio \(7/8\). This argument applies to all integers \(n\ge3\), not merely to the verified finite range.

## Verification

Run `python3 verify_deck3.py` using Python 3 standard library. The verifier enumerates every binary word with exactly three ones for each \(n\in\{3,\ldots,16\}\), constructs each three-deck directly from position triples, groups identical decks, and checks all class sizes, all involution partners, all collision counts and the exact codebook formula. It passes with the result recorded in `verify_deck3_output.txt`. An independent symbolic substitution check of the four key polynomial deck entries also gave exactly the differences printed in the proof. Such finite checks are consistency tests; the all-length statement follows from the algebraic proof above.

## Relationship to prior work

Nilforoushan and Parvaresh (first public version September 19, 2026) analyze the general \(k\)-deck channel, degrees of freedom and the asymptotic growth \(D_{2,3}(n)=\Theta(n^9)\). Their paper develops full-length-three deck identities but does not provide this complete restricted-weight fiber classification or its rational enumerator. Chrisnata and coauthors enumerate unrestricted deck counts at finite lengths, without the all-length weight-three formula. Lejeune, Rigo and Rosenfeld study binomial-equivalence classes, especially two-binomial equivalence and general growth questions. The integer-sequence entry A258585 explicitly records a colliding length-seven pair, so that finite example is not claimed as new. The present result concerns the exact structure and optimal codebook size for every length in the constant-weight-three stratum.

## Limitations

No conclusion is drawn about deck classes with other weights, robustness to missing or noisy read multiplicities, or the unrestricted capacity \(D_{2,3}(n)\). Priority is assessed from accessible primary text, literature records and exact-deck comparisons; earlier unindexed or inaccessible focused results could still subsume the claim. The verification is computationally exhaustive only for lengths three through sixteen; the infinite classification has an independent symbolic proof. No independent mathematical audit has been performed.

## References

1. Arman Nilforoushan and Farzad Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106, first public September 19, 2026. https://arxiv.org/abs/2609.23106
2. Johan Chrisnata, Han Mao Kiah, Sankeerth Rao Karingula, Alexander Vardy, Eitan Yaakobi and Hanwen Yao, *On the number of distinct k-decks: Enumeration and bounds*, Advances in Mathematics of Communications 17 (2023), 960–978, DOI 10.3934/amc.2021032. https://www.aimsciences.org/article/doi/10.3934/amc.2021032
3. Marie Lejeune, Michel Rigo and Matthieu Rosenfeld, *On the binomial equivalence classes of finite words*, 2020, arXiv:2001.11732. https://arxiv.org/abs/2001.11732
4. OEIS A258585, number of three-binomial equivalence classes of binary words of length \(n\); contains the previously known length-seven collision. https://oeis.org/A258585
