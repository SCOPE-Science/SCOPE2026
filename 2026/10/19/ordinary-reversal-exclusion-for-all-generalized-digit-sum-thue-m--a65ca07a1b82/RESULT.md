# Ordinary reversal exclusion for all generalized digit-sum Thue–Morse words

## Finding
Let \(b\ge2\), \(m\ge3\), and let \(t_{b,m}(n)=s_b(n)\bmod m\) for every integer \(n\ge0\), where \(s_b(n)\) is the sum of the base-\(b\) digits of \(n\). If \(u\) is any contiguous length-four factor of this infinite word, its ordinary reversal \(u^R\) is **not** a factor. Hence the same exclusion holds for every factor of length \(n\ge4\). For length three, a factor and a different factor cannot be ordinary reversals of one another. Consequently its ordinary reflection complexity and ordinary factor complexity coincide for every \(n\ge3\):

\[
 r_{t_{b,m}}(n)=\rho_{t_{b,m}}(n),\qquad b\ge2,\quad m\ge3,\quad n\ge3.
\]

Here \(\rho\) counts distinct length-\(n\) factors and \(r\) counts equivalence classes of those factors under the relation \(u\sim v\) if \(u=v\) or \(u=v^R\). This is a universal threshold: it cannot be uniformly moved below four for exclusion of **all** reflected factors, since \(t_{2,3}\) contains the palindrome \(121\).

## Assumptions and scope
The alphabet is the additive cyclic group \(\mathbb Z/m\mathbb Z\). Reversal changes the order of letters without relabeling them. The theorem applies to every base \(b\ge2\), including bases with \(b\equiv1\pmod m\) where the sequence is periodic, and every modulus \(m\ge3\), including composite moduli. It makes no assertion for \(m\in\{1,2\}\): ordinary Thue–Morse at \(m=2\) has arbitrarily long reversible factors.

For the digit-sum word, the substitution identity is
\[
 t_{b,m}(bj+i)=t_{b,m}(j)+i\pmod m,
 \quad j\ge0,\quad 0\le i<b.
\]
Thus every aligned block of length \(b\) has successive differences \(+1\bmod m\). Call a gap between the last position of one such block and the first position of the next a boundary gap. Inside any aligned block all gaps have difference \(+1\).

## Proof
**Lemma 1 (short windows).** In a window with \(h\) consecutive adjacent gaps, at most \(\lceil h/b\rceil\) gaps cross aligned block boundaries. For \(h=2\) and every \(b\ge2\), there is at most one boundary gap; for \(h=3\) and \(b\ge3\), there is at most one boundary gap.

Indeed boundary gaps are spaced exactly \(b\) gaps apart. The asserted cases follow immediately.

**Lemma 2 (three letters).** For every \(b\ge2\), \(m\ge3\), if a length-three factor \(u=u_0u_1u_2\) and its reversal both occur, then \(u_0=u_2\).

Write its successive differences as \((d_1,d_2)=(u_1-u_0,u_2-u_1)\), modulo \(m\). Lemma 1 says that at least one of these is \(+1\). For the reversed triple, the corresponding differences are \((-d_2,-d_1)\), and again at least one is \(+1\). Thus among \(d_1,d_2\) there is both a \(+1\) and a \(-1\). As \(+1\ne-1\) for \(m\ge3\), these are the two differences, so their sum vanishes: \(u_2=u_0\). The two words are then equal.

**Lemma 3 (four letters, bases at least three).** Fix \(b\ge3\), \(m\ge3\). Every four-letter factor has at least two adjacent differences equal to \(+1\), because among its three gaps at most one is a boundary gap (Lemma 1). If its reversal were also a factor, the latter would likewise have at least two differences \(+1\). But reversing a factor negates and reverses its three differences, so the original would need at least two differences equal to \(-1\). Since \(+1\ne-1\), three gaps cannot simultaneously contain at least two of each. Contradiction.

**Lemma 4 (four letters, base two).** Fix \(m\ge3\) and abbreviate \(a_j=t_{2,m}(j)\). The digit-sum identity shows that every four-letter factor is one of two parity types:
\[
 E(a,b)=(a,a+1,b,b+1),\quad(a,b)=(a_j,a_{j+1}),
\]
\[
 O(a,b,c)=(a+1,b,b+1,c),\quad(a,b,c)=(a_j,a_{j+1},a_{j+2}).
\]
All coordinates are interpreted modulo \(m\). No triple \((a_j,a_{j+1},a_{j+2})\) consists of three equal letters: among any three consecutive indices there is an aligned pair \((a_{2k},a_{2k+1})=(a_k,a_k+1)\), whose entries differ.

If \(E(a,b)^R=(b+1,b,a+1,a)\) were of type \(E\), its first adjacent pair would require \(b=b+2\pmod m\), impossible. If it were of type \(O\), coordinate comparison forces the three coarse symbols of that odd starting window to equal \(a=b\), violating the preceding triple property. Similarly \(O(a,b,c)^R=(c,b+1,b,a+1)\) cannot be of type \(O\), since its middle pair would require \(b=b+2\); if it were of type \(E\), coordinate comparison would force \(a=b=c\), again impossible. Thus no reversed four-letter factor occurs.

The assertion for length four follows from Lemmas 3–4. If a longer factor and its reversal both occurred, then its leading four-letter subfactor would have its reversal as the trailing four-letter subfactor of the reversed occurrence, contradicting the length-four result. For \(n\ge4\), no reversal relates two occurring factors, so all reflection classes are singletons. For \(n=3\), Lemma 2 excludes a pair of *distinct* reversed factors, also making all reflection classes singletons. This proves \(r=\rho\) for all \(n\ge3\).

The length-three palindrome \(121\) appears in \(t_{2,3}\) at zero-based positions \(2,3,4\), so length four is the best possible universal threshold for the stronger assertion that even identical reversed factors are absent. \(\square\)

## Verification
A standalone Python 3 checker, `check_factors.py`, checks exact four-factor sets derived from morphism block-pair closure for every \(3\le b\le16\), \(3\le m\le19\), and separately checks generated prefixes for \(b=2\), \(3\le m\le29\), through length \(65536\). It prints `VERIFY_OK`. These computations check small cases and help detect errors; the preceding proof, not the finite checks, establishes the infinite quantified statement.

## Relationship to prior work
Allouche and Shallit (2000) study these very digit-sum words and show that arbitrarily long ordinary palindromes occur precisely when \(m\le2\). This by itself does not exclude *different* factors related by reversal, nor provide the universal length-four cutoff. Starosta (2011/2012) establishes closure under the larger dihedral family of **twisted** antimorphisms and determines ordinary factor complexity, but closure under \(a\mapsto x-a\) followed by reversal is not ordinary reversal closure. Rampersad and Shallit (2003) construct reversal-avoiding words, rather than identifying the complete \((b,m)\)-family here. Allouche, Campbell, Li, Shallit and Stipulanti (2025, arXiv:2406.09302v4, Question 62) specifically exhibit the ordinary-reflection identity for \(t_{2,3}\) and suggest it for moduli above four. The result here proves this equality simultaneously for every \(b\ge2,m\ge3\), including the previously omitted modulus four.

## Limitations
No formula for the ordinary factor complexity \(\rho_{t_{b,m}}\) is newly asserted; the finding identifies it with reflection complexity in the stated range. It does not address reflected factors with a nontrivial relabeling of alphabet symbols; those are known to occur under dihedral antimorphisms. The literature comparison is not an assertion of global uniqueness; earlier equivalent statements not indexed or not accessible remain a risk. The proof uses the usual digit-sum generating sequence and does not apply to arbitrary codings or perturbed substitutions.

## References
1. J.-P. Allouche and J. Shallit, *Sums of Digits, Overlaps, and Palindromes*, Discrete Mathematics & Theoretical Computer Science 4 (2000), 1–10, DOI 10.46298/dmtcs.282, https://dmtcs.episciences.org/282.
2. Š. Starosta, *Generalized Thue-Morse words and palindromic richness*, arXiv:1104.2476 (first public 2011-04-13); Kybernetika 48 (2012), 361–370, https://arxiv.org/abs/1104.2476.
3. N. Rampersad and J. Shallit, *Words avoiding reversed subwords*, arXiv:math/0311121 (2003), https://arxiv.org/abs/math/0311121.
4. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302v4 (2025), Question 62, https://arxiv.org/abs/2406.09302.
