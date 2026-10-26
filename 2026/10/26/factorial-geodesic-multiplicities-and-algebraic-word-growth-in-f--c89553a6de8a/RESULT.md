# Factorial geodesic multiplicities and algebraic word growth in free inverse monoids

## Finding

Fix an integer \(r\geq1\), and let \(\mathrm{FIM}_r\) be the free inverse monoid with the standard symmetric alphabet of \(2r\) letters. An element is represented by its Munn tree \((T;s,t)\), with finite connected Cayley subtree \(T\) and distinguished initial and terminal vertices \(s,t\) (normalization takes \(s=1\)). Let \(P=P_T(s,t)\) be the unique simple path between them; denote vertex degrees in \(T\) and \(P\) by \(\deg_T\) and \(\deg_P\), respectively.

**Theorem A (multiplicity for one element).** The minimum word length of \((T;s,t)\) is \(2|E(T)|-d_T(s,t)\), and the **exact number of distinct words** attaining that length and representing that element is

\[
W(T;s,t)=\prod_{v\in P}\bigl(\deg_T(v)-\deg_P(v)\bigr)!\prod_{v\in V(T)\setminus P}\bigl(\deg_T(v)-1\bigr)!.
\]

The empty tree has value \(W=1\). For the Green \(\mathcal R\)-class determined by \(T\), the number of shortest words representing *any element of that class* is

\[
\sum_{t\in V(T):\,d_T(s,t)=\operatorname{ecc}_T(s)}W(T;s,t).
\]

The \(\mathcal L\)-class formula is the same on the Munn tree of the inverse element. For a \(\mathcal D\)-class, represented by the unrooted edge-labelled Cayley subtree \(T\) up to left translation, the count is

\[
\sum_{\substack{(s,t)\in V(T)^2\\ d_T(s,t)=\operatorname{diam}(T)}} W(T;s,t).
\]

All shortest lengths in these formulas are the corresponding element, eccentricity, or diameter minima; these minima are not claimed as new.

**Theorem B (algebraic series counting words, not elements).** Put \(q=2r\), \(p=q-1\), and write \((a)_{\underline j}=a!/(a-j)!\). Let \(F_r(z)\in\mathbb Z[[z]]\) be the unique series with constant coefficient one satisfying

\[
F_r(z)=\sum_{j=0}^{p}(p)_{\underline j}\bigl(zF_r(z)\bigr)^j,
\quad
E_{r,a}(z)=\sum_{j=0}^{a}(a)_{\underline j}\bigl(zF_r(z)\bigr)^j
\quad(0\le a\le q).
\]

Let \(h_{r,n}\) denote the number of **words of length \(n\) that are shortest representatives of their own elements**. Their ordinary generating series is

\[
\boxed{
\sum_{n\ge0}h_{r,n}u^n
=E_{r,q}(u^2)+\frac{q u\,E_{r,p}(u^2)^2}{1-pu\,E_{r,p-1}(u^2)}.
}
\]

In particular this series is algebraic over \(\mathbb Q(u)\) for every \(r\ge1\). For rank two its coefficients through degree eight are

\[
1,4,16,60,228,840,3132,11496,42528.
\]

## Assumptions and scope

A word corresponds to a walk in the Cayley graph of the free group on the standard symmetric alphabet. Its Munn tree is the finite edge-labelled subtree containing the starting vertex \(1\), all vertices the walk visits, and its terminal vertex. Two words represent the same free-inverse-monoid element precisely when these Munn data agree. A distinct word means a distinct ordered alphabet string, not merely a different traversal presentation or endpoint. A Green-class geodesic means a word of minimum length among representatives of **all** elements in that fixed Green class. This result is valid for every finite-rank free inverse monoid with no restriction to rank two.

## Proof

**1. Parity lower bound and structural rigidity.** Remove any edge \(e\) from \(T\). Every walk from \(s\) to \(t\) crosses its cut an odd number of times if \(e\in P\), and an even number otherwise. A representing walk must cover every edge. Hence each path edge is crossed at least once and each nonpath edge at least twice, yielding length at least \(|E(P)|+2(|E(T)|-|E(P)|)=2|E(T)|-d_T(s,t)\). A depth-first traversal of all off-path branches, advancing strictly along \(P\), attains equality.

Equality forces exactly one traversal of each path edge and exactly two traversals of each off-path edge. Consequently no return to an earlier trunk vertex is possible and each off-path subtree must be completed before its parent traversal continues. At every path vertex \(v\), the off-path child subtrees are therefore traversed in an arbitrary linear order: there are \((\deg_T(v)-\deg_P(v))!\) choices. At each vertex \(v\notin P\), the one edge leading toward the trunk is fixed and the remaining \(\deg_T(v)-1\) child subtrees may likewise be ordered arbitrarily. Multiplying yields \(W(T;s,t)\). Every ordering generates a walk with the required Munn tree and terminal vertex. Distinct orderings give distinct words, because in a free-group Cayley tree different outgoing edges bear distinct alphabet labels and the first changed ordering changes the letter sequence. This proves Theorem A for an element.

**2. Green-class sums.** In a free inverse monoid, the \(\mathcal R\)-class retains the initial-rooted tree and varies its terminal vertex over \(V(T)\). The minimum length is attained exactly at vertices farthest from \(s\); summing the disjoint word sets of the associated elements proves the \(\mathcal R\) formula. Inversion reverses words and interchanges \(\mathcal R\) and \(\mathcal L\), proving the \(\mathcal L\) assertion. For \(\mathcal D\), the finite Cayley subtree is retained up to left translation while both distinguished vertices vary. The minimum occurs precisely at ordered diametral pairs. Distinct ordered vertex pairs yield distinct normalized Munn elements: a nontrivial left translation cannot preserve a finite nonempty subtree of a free-group Cayley graph. Thus the sum over ordered pairs counts each geodesic once.

**3. Ordered branch excursions.** Use \(z\) to mark a single edge that is traversed out and back, hence contributing two letters to the walk. Upon arriving at a vertex via its parent edge, there are exactly \(p=2r-1\) available directions for children. Choosing and **ordering** \(j\) distinct child directions contributes \((p)_{\underline j}\); each child leads to one edge-pair and an independent recursively explored subtree. Therefore its excursion-generating series satisfies

\[
F_r(z)=\sum_{j=0}^{p}(p)_{\underline j}(zF_r(z))^j.
\]

This recursive equation determines a unique formal power series with constant term one: every nonconstant occurrence of \(F_r\) is multiplied by \(z\), so coefficient \(z^k\) is determined by lower coefficients. At a trunk vertex having \(a\) directions not occupied by trunk edges, all ordered off-trunk excursions contribute \(E_{r,a}(z)\).

**4. Separate zero and positive trunk length.** If the trunk has length zero, its unique vertex has \(q\) permissible outgoing directions, giving \(E_{r,q}(u^2)\). If its length \(t\ge1\), there are \(q p^{t-1}\) choices of freely reduced trunk word, and its two endpoints each admit \(p\) side directions while its \(t-1\) internal vertices each admit \(p-1\). Therefore all geodesic words with exactly \(t\) trunk edges contribute

\[
q p^{t-1}u^t E_{r,p}(u^2)^2 E_{r,p-1}(u^2)^{t-1}.
\]

Summing over \(t\ge1\) gives the displayed rational expression in the auxiliary algebraic series \(F_r\). The decomposition is unique for each geodesic word, since its visited Munn tree and terminal vertex recover the trunk and every ordered excursion. In particular the formula counts **all geodesic words**, rather than one canonical word per element. Algebraicity follows because \(F_r\) satisfies a polynomial equation and \(H_r\) belongs to \(\mathbb Q(u,F_r(u^2))\).

## Verification

Run `python3 verify.py` in this directory with Python 3's standard library. It exhaustively enumerates all 87,381 words over four letters with length at most eight, builds their Munn trees by free reduction, and independently counts shortest representatives of all observed \(\mathcal H\), \(\mathcal R\), \(\mathcal L\), and \(\mathcal D\) classes. The enumerator compares the observed multiplicities and minima against factorial and diameter formulas for every observed class. A separate formal-power-series expansion computes the predicted word counts and compares every coefficient through degree eight against the direct exhaustive data. Additional independent word enumeration checks ranks one through length twelve and three through length six, providing boundary checks outside rank two. Representative output:

```
VERIFY_OK enumerated_words=87381 H=54590 R=35558 L=35558 D=12176 rank=2 max_length=8
RANK2_GEODESIC_SERIES [1, 4, 16, 60, 228, 840, 3132, 11496, 42528]
AUXILIARY_VERIFY_OK 1 12 [1, 2, 4, 6, 10, 12, 18, 20, 28, 30, 40, 42, 54]
AUXILIARY_VERIFY_OK 3 6 [1, 6, 36, 210, 1230, 7140, 41550]
```

The verifier confirms a finite bounded range; the universal quantification is supported by the mathematical proof above, not inferred from testing.

## Relationship to prior work

Munn's 1974 representation by finite birooted trees is foundational. Kambites, Nyberg-Brodda, Szakács and Webb (2024 preprint; journal 2026), *The growth of free inverse monoids*, Lemma 3.2, determine the minimum length from trunk and branch edges and their subsequent formulas count **Munn-tree elements** by length using Fuss–Catalan numbers. This proof relies on their minimum-length principle but counts the generally multiple **shortest words** representing each fixed element and derives a different weighted series. Bodart, Carvalho and Monteiro (2026), *Green languages and growth of free inverse monoids*, study Green-geodesic languages, their descriptions, formal-language complexity and growth tightness. Their structural characterizations motivate the class-wise refinement; the examined statements do not give these class-specific factorial multiplicities or the ordinary generating series for every geodesic word. Earlier normal-form work constructs individual representatives, not their full geodesic multiplicity. Mitchell's 1974 note, *Counting word-trees*, concerns the number of word-trees according to its abstract; its inaccessible full text is a residual overlap risk.

## Limitations

This counts words, not the number of distinct elements of a given length; the two growth sequences differ in general. The formulas use the standard symmetric generating set of a **free** inverse monoid. They are not asserted for quotients, inverse monoids with relations, or other generating sets. The algebraic series formula does not by itself identify an explicit dominant singularity or give asymptotic constants. A source-equivalence search cannot guarantee absolute novelty, especially for older word-tree enumeration literature.

## References

1. C. Bodart, A. Carvalho, A.-C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251 (first posted 2026-09-28), https://arxiv.org/abs/2609.35251 .
2. M. Kambites, C.-F. Nyberg-Brodda, N. Szakács, R. Webb, *The growth of free inverse monoids*, arXiv:2407.10489 (first posted 2024-07-15), https://arxiv.org/abs/2407.10489 ; Journal of the Institute of Mathematics of Jussieu, DOI:10.1017/S1474748026101789.
3. W. D. Munn, *Free inverse semigroups*, Proc. London Math. Soc. (1974), DOI:10.1112/plms/s3-29.3.385.
4. J. M. O. Mitchell, *Counting word-trees*, Glasgow Math. J. 15 (1974), 148–149, DOI:10.1017/S0017089500002317.
5. L. A. Bokut, Y. Chen, X. Zhao, *Gröbner–Shirshov bases for free inverse semigroups*, arXiv:0804.0959, https://arxiv.org/abs/0804.0959 .
