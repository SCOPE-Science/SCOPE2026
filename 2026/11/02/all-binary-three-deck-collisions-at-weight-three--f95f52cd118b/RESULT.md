# All binary three-deck collisions at weight three

## Finding

For each integer \(z\ge0\), consider all binary words containing exactly three \(1\)'s and \(z\) zeros. The *three-deck* of a word is the multiset of all length-three scattered subsequences, counted with multiplicity. A scattered subsequence chooses increasing but not necessarily consecutive positions.

**Theorem.** Write each such word uniquely as
\[
 w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0},\quad a+b+c+d=z.
\]
Two different words have equal three-decks if and only if, after possibly exchanging them, their zero-gap vectors are
\[
 (t+u,b,b+3t,d)\quad\text{and}\quad (u,b+3t,b,d+t),
 \qquad t\ge1,\quad u,b,d\ge0.
\]
All variables here are integers. Hence every class has size one or two. Let \(P_z\) be the number of two-word classes. Then
\[
\sum_{z\ge0}P_zX^z=\frac{X^4}{(1-X)^2(1-X^2)(1-X^4)}.
\]
The exact number \(D_{3,3}(n)\) of distinct length-three decks among length-\(n\) binary words of Hamming weight three, for every \(n=z+3\ge3\), is
\[
 D_{3,3}(z+3)=\binom{z+3}{3}-P_z.
\]
The number of singleton classes is \(\binom{z+3}{3}-2P_z\). In particular, the first two-word class in the weight-three slice occurs at \(z=4\), i.e. length seven, consistently with previously published small-length collision examples; that first occurrence is not claimed as new.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\). The deck records multiplicities, not merely which scattered subsequences occur. Exactly three ones occur, while the number \(z\) of zeros is unrestricted. The symbols \(a,b,c,d,t,u\) are integers, with all nonnegativity conditions displayed above. Both endpoints and zero-length gaps are permitted. The parameter \(D_{3,3}(n)\) uses its first subscript for *deck length* and its second for *Hamming weight*, and is not the unrestricted-alphabet statistic \(D_{q,k}(n)\) of some references.

For length \(n\ge3\), equality of the length-three deck also determines all shorter scattered-subsequence counts: for any length-\(j\) pattern, summing the multiplicities of the length-three patterns containing it, with the appropriate deletion multiplicities, gives the original count multiplied by \(\binom{n-j}{3-j}\). Thus length-three-deck equality coincides with three-binomial equivalence at these fixed lengths.

## Proof

Let \(\binom{w}{v}\) denote the number of scattered occurrences of \(v\) inside \(w\). Define four integer statistics
\[
 z=a+b+c+d,\quad U=\binom w{011}=3a+b,\quad V=\binom w{110}=c+3d,
\quad Q=\binom w{001}=\binom a2+\binom{a+b}2+\binom{a+b+c}2.
\]
The first two equalities count a zero before a pair of ones, and a zero after a pair of ones, respectively. The last sums choices of two preceding zeros over the three ones.

**Deck compression is exact.** Let \(T=\binom w{01}=3a+2b+c\). Direct substitution gives \(2T=U+3z-V\), so \(T\) is fixed by \((z,U,V)\). The three deck entries with exactly two ones are
\[
 \binom w{011}=U,\qquad \binom w{110}=V,\qquad
 \binom w{101}=3z-U-V.
\]
The three with exactly one one are
\[
 \binom w{001}=Q,\qquad
 \binom w{010}=(z-1)T-2Q,\qquad
 \binom w{100}=3\binom z2-Q-\binom w{010}.
\]
For the middle equality, let \(p_1=a\), \(p_2=a+b\), \(p_3=a+b+c\) be the numbers of zeros before the consecutive ones. Then
\(\binom w{010}=\sum_{i=1}^3p_i(z-p_i)\), while
\(T=\sum_i p_i\) and \(2Q=\sum_i(p_i^2-p_i)\). Finally,
\(\binom w{000}=\binom z3\) and \(\binom w{111}=1\). These equations recover the entire deck from \((z,U,V,Q)\); conversely those four statistics are determined by the deck, with \(z\) fixed by its ambient word length. Thus the deck is equal precisely when all four statistics agree.

**All possible collision moves.** Let two gap vectors have equal \(z,U,V\). Their coordinate differences necessarily have the form
\[
 (\Delta a,\Delta b,\Delta c,\Delta d)=(-t,3t,-3t,t)
\]
for some integer \(t\). Indeed, the three linear equalities are
\(\Delta a+\Delta b+\Delta c+\Delta d=0\),
\(3\Delta a+\Delta b=0\), and
\(\Delta c+3\Delta d=0\); solving them over the integers gives exactly the displayed line. Under that change the three zero prefixes change by \((-t,2t,-t)\), so expansion of the displayed quadratic expression yields
\[
 Q'-Q=t(b-c+3t).
\]
For distinct words \(t\ne0\), equality of \(Q\) therefore forces \(3t=c-b\); this value is unique. The candidate partner gap vector is
\[
 (a-t,c,b,d+t)
 \quad\text{with}\quad t=(c-b)/3,
\]
provided all its entries are nonnegative. Reversing the candidate change uses \(-t\), giving a genuine involution. Thus the equivalence class contains at most two words, and the condition is sufficient because it fixes all deck statistics.

**Orient and enumerate doubletons.** In every distinct pair exactly one member has \(b<c\). For it, \(t=(c-b)/3\ge1\), and the partner requires \(a\ge t\). Set \(u=a-t\ge0\); then the two vectors are precisely
\[
 (t+u,b,b+3t,d)\quad\text{and}\quad(u,b+3t,b,d+t).
\]
Conversely each independent choice \(t\ge1\), \(u,b,d\ge0\) gives one valid unordered pair, and exactly one because \(b<c\) singles out its representative. The number of zeros is \(z=4t+u+2b+d\). Therefore
\[
 \begin{aligned}
 \sum_{z\ge0}P_zX^z
 &=\left(\sum_{t\ge1}X^{4t}\right)
   \left(\sum_{u\ge0}X^u\right)
   \left(\sum_{b\ge0}X^{2b}\right)
   \left(\sum_{d\ge0}X^d\right)\\
 &=\frac{X^4}{(1-X)^2(1-X^2)(1-X^4)}.
 \end{aligned}
\]
There are \(\binom{z+3}{3}\) words of weight three by stars and bars (or choosing three one-positions). Each doubleton merges exactly two words into one deck, so the number of distinct decks is \(\binom{z+3}{3}-P_z\). This proves all assertions. \(\square\)

## Verification

The included `verify.py` independently builds complete length-three subsequence-count vectors using an iterative dynamic program and exhaustively groups all binary words with exactly three ones for every \(z\in\{0,\ldots,15\}\). For each grouped deck it compares every class to the explicit partner involution, checks the singleton/doubleton dichotomy, and checks the rational-series coefficient count and distinct-deck identity. Output from the embedded code is `VERIFY_OK zeros=0..15 words=3876 classes=3590 doubletons=286 signature_class_partner_and_gf=TRUE`.

This finite computation checks the proof and detects small counterexamples; it is not substituted for the infinite algebraic argument above. The proof uses only elementary counting and an exact linear/quadratic Diophantine calculation.

## Relationship to prior work

Lejeune, Rigo and Rosenfeld (2020, arXiv:2001.11732) study finite binomial equivalence classes, focusing on explicit algorithms for two-binomial equivalence; their definitions apply here but do not give this weight-three, three-binomial fiber formula. Chrisnata et al., *On the number of distinct \(k\)-decks: Enumeration and bounds* (2019 conference; 2021 early-access journal, DOI below), study deck counting and enumerate small parameters; their prior length-seven collisions and general trellis approach are acknowledged, not recast as new. Rigo, Stipulanti and Whiteland (2022, arXiv:2201.04603) study binomial complexity in infinite words and morphisms rather than the present finite fixed-weight fibers.

Nilforoushan and Parvaresh (2026, arXiv:2609.23106, especially Lemma 7.1 and Sections 4–7) give a general four-parameter compression of binary three-decks and sharp global asymptotic counts. That broader compression is established prior work: the new assertion is the **complete integer-fiber classification and rational enumerator for exactly three ones**, not compression itself. A general affine constraint does not count realizable integral fibers or establish their maximum size of two.

## Limitations

This result is restricted to binary Hamming weight exactly three and length-three scattered-subsequence multiplicity decks. It does not classify weights four or more or determine the unrestricted total number of three-decks. It is not a statement about contiguous-substring spectra, ordinary deletion-correction codes or distinct subsequences without multiplicities. Literature comparison does not guarantee absence of an unlocated equivalent characterization. The full text of the closest 2021 journal version was not independently inspectable; its accessible abstract, table and material publicly available sections were examined, alongside the distinct earlier conference record. An independent scientific assessment has not yet been performed.

## References

1. M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732 (first posted 2020-01-31), https://arxiv.org/abs/2001.11732.
2. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the number of distinct k-decks: Enumeration and bounds*, ISCIT 2019 and *Advances in Mathematics of Communications* 17 (2023), 960–978 (online 2021-08-30), https://doi.org/10.3934/amc.2021032.
3. M. Rigo, M. Stipulanti and M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603 (first posted 2022-01-12), https://arxiv.org/abs/2201.04603.
4. A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106 (first posted 2026-09-19), https://arxiv.org/abs/2609.23106.
