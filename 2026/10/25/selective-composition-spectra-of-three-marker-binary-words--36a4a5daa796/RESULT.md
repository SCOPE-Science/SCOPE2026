# Selective composition spectra of three-marker binary words

## Finding

Let \(w\) be any binary word containing exactly three occurrences of \(1\). Write it uniquely as
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
For \(j\in\{0,1,2,3\}\), let \(\mathcal S_j(w)\) denote the multiset of compositions of all nonempty contiguous substrings of \(w\) containing exactly \(j\) occurrences of \(1\). Every composition specifies both its number of ones and its number of zeros, and multiplicity is retained. Words are considered equivalent only under reversal (not symbol complementation or cyclic rotation).

**Theorem (exact two-stage reconstruction).** For every choice of the four nonnegative integers above, among all binary words with exactly three ones and with the same \(\mathcal S_0\) and \(\mathcal S_3\) as \(w\), the number of reversal classes is exactly
\[
1+\mathbf 1_{a\ne d}\mathbf 1_{b\ne c}.
\]
They are represented by the two possible orders
\[
0^a1\,0^b1\,0^c1\,0^d\quad\text{and}\quad0^a1\,0^c1\,0^b1\,0^d,
\]
with those representatives belonging to the same reversal class exactly when \(a=d\) or \(b=c\). Moreover, observing \(\mathcal S_1\) distinguishes these classes whenever they differ. Thus \(\mathcal S_0\cup\mathcal S_1\cup\mathcal S_3\) uniquely determines every three-one binary word up to reversal; **the entire two-one composition layer is unnecessary**.

The two-class alternative genuinely occurs: the words `010100100` and `010010100` have identical zero-one-count and three-one-count composition layers but differ in their one-one-count layers and are not reversals.

## Assumptions and scope

The source word has known Hamming weight exactly three; the substring observations are complete, noise-free multisets for the specified exact-one-count layers. Contiguous substrings are linear, not circular, and the source length may be arbitrary at least three. The given layers include compositions of all substring lengths, provided the specified number of ones is present. No reconstruction statement is made for weight four or higher, missing multiplicities, or noisy measurements.

Put
\[
G_t(z)=1+z+\cdots+z^t\quad(t\ge0),
\qquad P_j(z)=\sum_{u:\,u\text{ is a substring occurrence of }w,\,|u|_1=j}z^{|u|_0}.
\]
The coefficient of \(z^\ell\) in \(P_j\) is exactly the multiplicity of the composition containing \(j\) ones and \(\ell\) zeros, so \(P_j\) and \(\mathcal S_j\) convey identical information. An occurrence is counted once per choice of start and end, even if several occurrences spell the same substring.

## Proof

**1. The zero-only layer determines the multiset of all four gaps.** There are four zero runs, of lengths \(a,b,c,d\), including possibly empty end or internal runs. For every integer \(\ell\ge1\), the coefficient \(f_\ell=[z^\ell]P_0(z)\) satisfies
\[
f_\ell=\sum_{g\in(a,b,c,d)}\max(g-\ell+1,0),
\qquad f_\ell-f_{\ell+1}=\#\{g\in(a,b,c,d):g\ge\ell\}.
\]
Thus consecutive differences recover the number of gap lengths at least \(\ell\), and hence the multiplicity of every positive gap length. Exactly four gaps exist, so the number of zero-length gaps also follows. The unordered multiset \(\{\!\{a,b,c,d\}\!\}\) is therefore determined.

**2. The three-one layer determines the two outer gaps as an unordered pair.** Every substring containing all three ones must start in the first zero gap or at the first one, and stop at the third one or in the last zero gap. Consequently
\[
P_3(z)=z^{b+c}G_a(z)G_d(z).
\]
Its least exponent gives \(b+c\). Dividing by that power yields \(H(z)=G_a(z)G_d(z)\), whose degree is \(a+d\). Let \(m=\min(a,d)\). For \(0\le j\le m\), the coefficient of \(z^j\) in \(H\) equals \(j+1\); for any \(j>m\) not exceeding its degree, that equality fails. Therefore
\[
m=\max\{j\in[0,\deg H]\cap\mathbb Z:[z^j]H=j+1\},
\]
and \(\max(a,d)=\deg H-m\). This also covers zero gaps, including \(H=1\). Hence the unordered pair \(\{\!\{a,d\}\!\}\) is known. Subtracting it, with multiplicities, from the gap multiset recovered in Step 1 gives the unordered pair \(\{\!\{b,c\}\!\}\).

**3. Exact ambiguity without the one-one layer.** Select an orientation in which the two outer gaps are \(a,d\). The only candidates are then the two words displayed in the theorem, and the reversals of those candidates account for the opposite orientation. Both candidates have the same \(P_0\), because they merely permute the four zero gaps, and the same \(P_3\), because they have the same outer pair and the same sum of inner gaps. They are reversals of one another if and only if \(a=d\) or \(b=c\); otherwise they are distinct reversal classes. This proves the exact two-class formula, including the boundary cases.

**4. The one-one layer resolves the remaining choice.** A substring with exactly one one must contain one of the three marked ones, extend left into the immediately preceding zero gap, and extend right into the immediately following zero gap. Therefore
\[
P_1(z)=G_a(z)G_b(z)+G_b(z)G_c(z)+G_c(z)G_d(z).
\]
Interchanging the inner gaps changes this polynomial by exactly
\[
\bigl(G_a(z)-G_d(z)\bigr)\bigl(G_b(z)-G_c(z)\bigr).
\]
Because \(G_s=G_t\) holds precisely when \(s=t\), and \(\mathbb Z[z]\) is an integral domain, the difference is nonzero exactly when \(a\ne d\) and \(b\ne c\). Those are precisely the cases in which Step 3 leaves two reversal classes. Therefore the one-one layer selects the correct class, proving the theorem for every permitted quadruple.

## Verification

The included standard-library `verify.py` enumerates every weight-three binary word of each length \(3\le n\le24\), 12,650 words in total. It constructs the partial composition multisets literally from substring occurrences, groups them into equivalence classes under zero-and-three observations, and checks that every fiber contains the stated number of reversal classes. It then checks that adding one-one observations leaves only one class per fiber. The test also checks an explicit two-class example. It independently checks the classical weight-four full-spectrum ambiguous pair as a scope boundary. Running `python verify.py` prints `PASS` lines only when all assertions hold. These experiments corroborate but do not replace the infinite proof above.

## Relationship to prior work

Acharya, Das, Milenkovic, Orlitsky, and Pan introduced the full substring-composition reconstruction problem and characterized full-spectrum equicomposability using bivariate-polynomial factorizations. Their universal length criteria allow ambiguity at many lengths and their length-eight witness has four ones. The theorem here is instead an all-length **selective exact-one-count observation** result for source weight three, and its zero-three two-class count is not obtained merely by knowing a full-spectrum reconstruction procedure.

Ye and Elishco studied reconstruction from partial composition information, especially prefix/suffix observations and subsets restricted by **substring length**. Gupta and Mahdavifar studied algorithms using the full composition spectrum. Those observation channels are materially different: keeping substrings with exactly zero, one and three marked bits while allowing arbitrary lengths is neither a prefix/suffix filter nor a short-length truncation. A published exact binary length-two composition classification similarly concerns a length filter and does not give the gap-orientation statement here.

## Limitations

The result assumes exactly three marked ones, exact multiplicities, and complete observation of the selected layers. It does not claim robustness to missing observations, efficiency in the presence of errors, or reconstruction for arbitrary Hamming weights. It also does not assert that the three retained one-count layers are a smallest sufficient collection; a sharper sufficiency theorem might exist. Priority against unindexed or differently named selective-spectrum results remains an empirical literature-search limitation, not a mathematical uniqueness certificate.

## References

1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439v1 (first posted 2014-03-10); SIAM J. Discrete Math. 29 (2015), 1340–1371, DOI:10.1137/140962486. Open full text: https://people.ece.cornell.edu/acharya/papers/str_rcn_sidma.pdf.
2. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963 (2022), especially Section VIII on length-limited composition observations.
3. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955 (2022).
