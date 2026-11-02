# Three-point index stability in elementary abelian groups and exact binary–ternary subfactor counts

## Finding

**Theorem (complete three-point index-stability classification).** Let \(p\) be prime, \(d\ge1\), and \(G=(\mathbb F_p)^d\) under addition. For a three-element subset \(A\subset G\), write \(D=A-A\), and call a nonempty subset \(B\subset G\) an **\(A\)-subfactor** when its translates \(A+b\), for \(b\in B\), are pairwise disjoint and the family is inclusion-maximal with that property. Say \(G\) is **three-index-stable** if, for every three-element \(A\), all its \(A\)-subfactors have the same cardinality. Then

\[
G\text{ is three-index-stable}\quad\Longleftrightarrow\quad p\in\{2,3\}\ \text{or}\ (d=1\text{ and }p\in\{5,7,11\}).
\]

In the two infinite positive-characteristic families, **every subfactor is classified and counted** as follows.

- If \(p=2\) and \(d\ge2\), the difference subgroup \(H=\langle A-A\rangle\) has four elements. Every \(A\)-subfactor is a transversal of the \(H\)-cosets: its size is \(2^{d-2}\), and there are exactly \(4^{2^{d-2}}\) such subsets.
- If \(p=3\) and \(A\) is collinear (three points of an affine line), \(H=\langle A-A\rangle\) has three elements. The subfactors are the transversals of its cosets: size \(3^{d-1}\), count \(3^{3^{d-1}}\).
- If \(p=3\), \(d\ge2\), and \(A=\{x,x+a,x+b\}\) is noncollinear, set \(H=\langle a,b\rangle\) and \(L=\langle a+b\rangle\). A subfactor consists of **one whole \(L\)-coset inside each \(H\)-coset**, chosen independently: size \(3^{d-1}\), count \(3^{3^{d-2}}\).

For \(d=1\) and \(p\in\{5,7,11\}\), the possible common size depends on \(|A-A|\). Precisely: \(p=5\) always has size \(1\); \(p=7\) has size \(2\) for difference-set size \(5\), and size \(1\) for difference-set size \(7\); \(p=11\) has size \(3\) for difference-set size \(5\), and size \(2\) for difference-set size \(7\). The code accompanying this result gives an exhaustive finite certificate for these exceptional prime orders.

## Assumptions and scope

Groups are finite elementary abelian \(p\)-groups of positive rank. Every three-element support is considered, not only supports in one fixed affine orbit. If \(|G|<3\), the defining universal statement is vacuous (only \(p=2,d=1\)). The term *index-stable* is the common subfactor-cardinality condition of the cited literature; in an abelian group the left/right notions coincide. Counts above are of actual subsets \(B\), not translation classes or sets normalized to contain zero.

For any finite abelian group, disjointness of the translates \(A+b\) is equivalent to \((B-B)\cap D=\{0\}\). An independent \(B\) is maximal exactly when \(B+D=G\). Indeed, an outside point can be added precisely if its difference from every point of \(B\) avoids \(D\). We use these two exact conditions throughout.

## Proof

**1. Binary characteristic.** Let \(p=2\). Three distinct points are affinely independent; translating yields \(A=\{0,a,b\}\) with independent \(a,b\). Then \(D=\{0,a,b,a+b\}=H\), a four-element subspace. The condition \((B-B)\cap H=\{0\}\) means at most one element of \(B\) in each \(H\)-coset; maximality means exactly one. There are \(2^{d-2}\) cosets, each with four independent choices. This proves both the common cardinality and the subfactor count.

**2. Ternary characteristic.** Let \(p=3\). If \(A\) is collinear, it is a full affine line and \(D=H\) is its one-dimensional direction subgroup; the same transversal argument proves the collinear formula. If \(A=\{0,a,b\}\) with independent \(a,b\), then

\[
D=\{0,\pm a,\pm b,\pm(a-b)\}=H\setminus\{\pm(a+b)\}.
\]

The only allowed differences between two distinct elements in a fixed \(H\)-coset are \(\pm(a+b)\). Thus every compatible subset of that coset lies in one coset of \(L=\langle a+b\rangle\), and filling that \(L\)-coset retains compatibility. Since \(D\subset H\), different \(H\)-cosets do not interact. Maximality therefore requires one **complete** \(L\)-coset in each \(H\)-coset. There are \(3^{d-2}\) outer cosets and three independent choices in each, proving the ternary formula. In either affine type, the subfactor cardinality is \(3^{d-1}\), hence three-index stability.

**3. Cyclic exceptional primes.** For \(d=1\) and \(p\in\{5,7,11\}\), translate the support to \(A=\{0,a,b\}\), with \(1\le a<b<p\). The accompanying exact checker loops over **every** such support and **every** nonempty subset of \(\mathbb Z/p\mathbb Z\), retaining precisely those satisfying \((B-B)\cap D=\{0\}\) and \(B+D=\mathbb Z/p\mathbb Z\). The output is

\[
\begin{array}{c|c}
p & (|D|,\text{all subfactor sizes})\\\hline
5&(5,\{1\})\\
7&(5,\{2\}),(7,\{1\})\\
11&(5,\{3\}),(7,\{2\}).
\end{array}
\]

The ranges \(\binom{p-1}{2}\) and \(2^p-1\) are finite and completely covered; no sampling or extrapolation is used. This certifies the only remaining positive cyclic cases.

**4. Rank-two negative witnesses for \(p=5,7,11\).** Work in \(H=\mathbb F_p^2\) with \(A=\{(0,0),(1,0),(0,1)\}\). Its difference set is

\[
D=\{(0,0),\pm(1,0),\pm(0,1),\pm(1,-1)\}.
\]

Define \(\ell(x,y)=y-2x\) and \(B_0=\ell^{-1}(S)\), with \(S=\{0\}\) if \(p=5,7\), and \(S=\{0,5\}\) if \(p=11\). All nonzero elements of \(D\) have nonzero images in \(\mathbb F_p\), and \(\ell(D)=\{0,\pm1,\pm2,\pm3\}\). For each indicated \(S\), one checks \((S-S)\cap\ell(D)=\{0\}\) and \(S+\ell(D)=\mathbb F_p\). Because \(B_0\) consists of complete fibers of \(\ell\), these two checks imply \((B_0-B_0)\cap D=\{0\}\) and \(B_0+D=H\). Thus \(B_0\) is maximal, with size \(5,7,22\), respectively.

Take the second packing \(B_1\) by scanning \(H\) in lexicographic order and adding each point not yet in \(B_1+D\). This process always produces a maximal packing. Explicit finite evaluation in the included checker gives \(|B_1|=7,13,31\), respectively, and prints the coordinates of **every** selected element; the checker also recomputes both defining conditions for both witnesses, independently of the greedy construction. Thus \(B_0\) and \(B_1\) have different sizes. In every dimension \(d>2\), take their Cartesian products with a complementary \((d-2)\)-space. Since \(D\) lies in the original plane, these products remain maximal and have different sizes.

**5. All primes \(p\ge13\).** In a cyclic order-\(p\) subgroup choose \(A=\{0,e,3e\}\); its difference set consists of the seven consecutive residues \(\{0,\pm e,\pm2e,\pm3e\}\). A cyclic set \(B\) of size at least two is an \(A\)-subfactor precisely when **each successive positive cyclic gap** lies in \(\{4,5,6,7\}\): gaps at least four ensure disjointness; gaps at most seven ensure that every remaining point lies within three steps of a chosen point. Every integer \(k\ge2\) with \(4k\le p\le7k\) occurs: start with \(k\) gaps equal to four and distribute the extra \(p-4k\) units, at most three per gap.

For \(p=13\), both \(k=2,3\) work; for \(p=17,19\), both \(k=3,4\) work. For every prime \(p\ge23\), set \(k=\lfloor p/5\rfloor\); both \(k\) and \(k+1\) satisfy \(4j\le p\le7j\). Hence two maximal packing cardinalities occur in the cyclic subgroup, and, after adjoining a full complement, in \(\mathbb F_p^d\) for any \(d\ge1\). Together with step 4 this proves every negative case, completing the equivalence.

## Verification

Run `python3 verify.py` from this package. The script uses Python's standard library and exact integer arithmetic. It exhausts all anchored three-element supports and nonempty packing subsets in cyclic orders \(5,7,11\); checks the finite rank-two witnesses and their maximality for \(p=5,7,11\); exhausts all packing subsets for the smallest binary and ternary spaces; and reconstructs distinct gap witnesses for eleven primes from \(13\) through \(53\). Expected final output: `VERIFY_OK`. The included `verification_output.txt` is an actual recorded run, not a replacement for executing the code. The cases beyond these finite tests are proved symbolically in steps 1, 2, 4 (product lifting), and 5.

## Relationship to prior work

Hooshmand (2026, arXiv:2607.08805, first version 2026-07-09) develops \(k\)-index stability, determines the two-point cyclic cases, and poses the extension to three-point supports as an explicit research direction. Hooshmand and Yousefian Arani (2023, arXiv:2310.03438) develop exhaustive subfactor methods and classify groups stable for *all* subset sizes. Their paper already records the failure of stability for \(C_5\times C_5\) and supplies a three-point instability witness for \(C_7\times C_7\); these individual observations are **not claimed as new**. Their all-subset characterization does not imply three-index instability for a group failing at larger subset sizes, and does not state the present exact elementary-abelian three-point classification or the subfactor counts in characteristics two and three. The present theorem settles the three-point problem over **every elementary abelian prime-power group**, together with exact lists/counts of all positive-family subfactors. More general results on maximal independent sets of Cayley graphs could conceivably imply components of this proof; full historical priority remains to be assessed independently.

## Limitations

The classification is for elementary abelian groups and supports of size exactly three; it makes no assertion about cyclic prime powers of nonprime order, other finite abelian groups, nonabelian groups, or supports of sizes four and above. The cyclic orders \(5,7,11\) use a complete, finite search certificate rather than a parameter-uniform structural proof. The results for \(C_5^2\) and \(C_7^2\) overlap known instability examples; the claimed contribution is the complete all-prime/rank dichotomy and the exact binary–ternary subfactor descriptions. No independent audit is claimed.

## References

1. M. H. Hooshmand, *Subindices and subfactors of \(\mathbb Z_n\) and \(k\)-index stability of finite groups*, arXiv:2607.08805 (first submission 2026-07-09; revised September 2026), https://arxiv.org/abs/2607.08805.
2. M. H. Hooshmand and M. M. Yousefian Arani, *Computational aspects of subindices and subfactors with characterization of finite index stable groups*, arXiv:2310.03438 (2023-10-05), https://arxiv.org/abs/2310.03438.
3. M. H. Hooshmand et al., *Subindices and subfactors of finite groups*, *Communications in Algebra* **51** (2023), https://doi.org/10.1080/00927872.2023.2168685. This reference supplies background definitions; the publicly accessible abstract was consulted, not its entire publisher full text.
