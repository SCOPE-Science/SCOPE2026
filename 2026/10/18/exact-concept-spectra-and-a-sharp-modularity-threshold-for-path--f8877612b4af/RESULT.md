# Exact concept spectra and a sharp modularity threshold for path-power neighborhood contexts

## Finding

For integers \(n\ge2\) and \(0\le k<n\), let \(K_{n,k}\) be the formal context with separate object and attribute copies of \([n]=\{1,\ldots,n\}\), with incidence \(iIj\) exactly when \(|i-j|\le k\). This is the reflexive adjacency matrix of the \(k\)-th power of an \(n\)-vertex path (and includes the equality context at \(k=0\)). Write \(L_{n,k}\) for its concept lattice ordered by extents and \(C(n,k)=|L_{n,k}|\).

**Exact extent classification.** Denote integer intervals by \([a,b]=\{a,a+1,\ldots,b\}\). Every concept extent is one of
\[
[n],\qquad [a,b]\quad(1\le a\le n-k,\ k+1\le b\le n,\ 0\le b-a\le2k),
\]
and additionally \(\varnothing\) when \(n\ge2k+2\). Distinct admissible endpoint pairs give distinct intervals. When \(n\le2k+1\), the separately listed whole extent \([n]\) is already one member of the interval family.

**Exact census and spectrum.**
\[
C(n,k)=\begin{cases}
(n-k)^2,&n\le2k+1,\\
(2k+1)n-3k^2-2k+2,&n\ge2k+2.
\end{cases}
\]
When \(n\ge2k+2\), the number of extents of each size \(t\) is \(1\) at \(t=0,n\), is zero for \(2k+2\le t<n\), and for \(1\le t\le2k+1\) is
\[
e_t=n-2k-1+\min\{t,2k+2-t\}.
\]
For \(n\le2k+1\), the size enumerator is exactly
\[
\sum_{a=1}^{n-k}\sum_{b=k+1}^{n}z^{b-a+1}.
\]
Every concept extent is the intersection of at most two column extents, including the empty intersection for the top; the bound of two is necessary when \(n\ge k+2\).

**Lattice phase transition.** If \(1\le k<n\), then \(L_{n,k}\) is distributive, and in fact isomorphic to the product of two chains with \(n-k\) elements, exactly when \(n\le2k+2\). For \(n\ge2k+3\) it fails the modular law. At \(k=0\), the lattice is the height-two lattice with \(n\) atoms; it is modular for all \(n\ge2\) and distributive only when \(n=2\). Thus \(n\le2k+2\) is the sharp distributive/modular cutoff for positive radii.

**Exact radius maximizing concept diversity.** For fixed \(n\ge4\), the unique maximizing integer radius is
\[
k_*(n)=\left\lfloor\frac{2n+1}{6}\right\rfloor,
\]
and
\[
\max_{0\le k<n}C(n,k)
=n+2+\left\lfloor\frac{(n-1)^2}{3}\right\rfloor.
\]
In particular, maximal concept count grows as \(n^2/3+O(n)\), at radius asymptotic to \(n/3\), whereas the complete relation has only one concept. At \(n=2,3\), the respective maxima are \(4,5\), both attained at \(k=0\).

## Assumptions and scope

Both sorts have exactly \(n\) labeled elements, and self-incidence is included. No cyclic wraparound is allowed. We count all concepts including top and bottom. A concept extent is a subset of objects of the form \(B'=\{i:\forall j\in B,\ |i-j|\le k\}\), for a set \(B\) of attributes; every such extent corresponds to exactly one concept. An intersection over no columns is the whole object set. The statements concern the precise finite context specified above, not all interval graphs or cycle powers.

## Proof

**1. Derivation and completeness.** A column \(j\) has extent \([\max(1,j-k),\min(n,j+k)]\). For nonempty \(B\), put \(u=\min B\) and \(v=\max B\). The intersection of its column extents is
\[
B'=[\max(1,v-k),\min(n,u+k)]
\]
if the left endpoint does not exceed the right, and is empty otherwise. Any nonempty such intersection \([a,b]\) has \(1\le a\le n-k\), \(k+1\le b\le n\), and \(b-a\le2k\); the latter follows from \(u\le v\), with endpoint clipping only making the inequality weaker. Also \(a\le b\).

Conversely, consider \(a,b\) satisfying these restrictions. If \(a>1\) and \(b<n\), choose \(B=\{b-k,a+k\}\). Both indices belong to \([n]\) and \(b-k\le a+k\) precisely because \(b-a\le2k\); the intersection is \([a,b]\). If \(a=1\) and \(b<n\), choose the singleton \(B=\{b-k\}\); here \(1\le b-k\le k+1\). If \(a>1\) and \(b=n\), choose \(B=\{a+k\}\); here \(n-k\le a+k\le n\). If \((a,b)=(1,n)\), the empty attribute set gives the entire object set. Finally, \(B=\{1,n\}\) gives the empty extent exactly when \(n\ge2k+2\), and none gives it when \(n\le2k+1\) because every two radius-\(k\) end windows overlap. Thus the classification is complete. The two extreme attributes witness necessity of two columns whenever \(n\ge k+2\): their intersection is a proper subset of each and is not the neighborhood of any singleton attribute (a singleton column has at least \(k+1\) objects).

**2. Census.** When \(n\le2k+1\), every pair in the rectangle \(1\le a\le n-k\), \(k+1\le b\le n\) obeys \(a\le b\le a+2k\). There are \((n-k)^2\) distinct extents, including the whole set; there is no empty extent.

When \(n\ge2k+2\), that rectangle has \((n-k)^2\) pairs. Put \(h=n-2k\). Exactly \(\binom h2\) pairs fail \(a\le b\), and another \(\binom h2\) fail \(b-a\le2k\). The two failure sets are disjoint. Adding the whole-set and empty extents gives
\[
C(n,k)=(n-k)^2-h(h-1)+2=(2k+1)n-3k^2-2k+2.
\]
For \(t=b-a+1\) with \(1\le t\le2k+1\), the allowed left endpoints lie between \(\max(1,k+2-t)\) and \(\min(n-k,n-t+1)\), inclusive. Their number simplifies to the stated \(e_t\). The dense enumerator follows immediately from the rectangle description.

**3. Lattice structure.** Identify a nonempty extent \([a,b]\) with its endpoint pair; inclusion corresponds to \((a,b)\preceq(c,d)\) if and only if \(a\ge c\) and \(b\le d\). For \(n\le2k+1\), every pair in the endpoint rectangle is allowed, giving a product of two chains. When \(n=2k+2\), the only two missing rectangle pairs are \((n-k,k+1)\) and \((1,n)\); assigning these respectively to the empty extent and whole extent extends the same order isomorphism to the full rectangle. Thus \(L_{n,k}\) is distributive for \(1\le k\) and \(n\le2k+2\).

For \(k\ge1\) and \(n\ge2k+3\), the singleton extents \(X=\{k+1\}\), \(Y=\{k+3\}\) and the two-element extent \(Z=\{k+1,k+2\}\) exist and satisfy \(X\subset Z\). Their meet is intersection, and \(X\vee Y=\{k+1,k+2,k+3\}\) because that three-element interval is an extent. Consequently
\[
X\vee(Y\wedge Z)=X\ne Z=(X\vee Y)\wedge Z,
\]
so the modular law fails. For \(k=0\), the only extents are the empty set, whole set, and the singleton sets. This is modular, but has a nondistributive three-atom diamond for \(n\ge3\).

**4. Optimizing the radius.** In the range \(n\ge2k+2\), write
\[
C(n,k)=n+2+\frac{(n-1)^2}{3}-3\left(k-\frac{n-1}{3}\right)^2.
\]
In the complementary range, \(C(n,k)=(n-k)^2\) decreases with \(k\). At the boundary the sparse value exceeds the first dense value: writing \(n=2s\), the values are \((s+1)^2\) and \(s^2\); writing \(n=2s+1\), they are \(s^2+4s\) and \((s+1)^2\) (the comparison is strict for \(s\ge1\)). Thus the maximum is in the sparse region. For \(n\ge4\), the unique integer nearest \((n-1)/3\) is \(\lfloor(2n+1)/6\rfloor\), and it lies in the sparse range. Completing the square and checking the three residues modulo three gives the exact maximum formula; the two smaller orders are inspected directly.

## Verification

A standalone Python 3 standard-library verifier is included as `verify.py`. It independently intersects all column-neighborhood bit masks over every attribute subset, compares the resulting extents with the endpoint classification, verifies the extent-size polynomial and concept counts, and checks the dense product-chain order. It exhaustively handles all \(105\) pairs \((n,k)\) with \(1\le n\le14\), representing \(425986\) attribute subsets. It additionally tests the optimal radius for \(2\le n\le10\) and all modular and distributive identities for \(2\le n\le8\). The expected output ends in `all_equalities=PASS`. These finite tests are evidence of consistency, not proofs of the all-parameter statements.

## Relationship to prior work

Rawson, Myers, Green, Robinson, and Joslyn (2023), Theorem 3.1, establishes the general equivalence between concept lattices and intersection-closed hypergraphs. That representation principle is used here and is not presented as new. Their results do not supply the endpoint normal form, formulas, or sharp optimal radius for reflexive path-power neighborhoods.

Macêdo Filho, Dantas, Machado, and Figueiredo (2012/2013) characterize **induced bicliques of the original graph** \(P_n^k\) to study biclique-coloring. Formal concepts here instead correspond to complete bicliques in the two-sorted incidence relation with reflexive diagonal, or equivalently to intersections of closed neighborhoods. These notions are different, so their coloring and induced-biclique classification does not imply the present concept census. Koyda and Stumme (2021) analyze Boolean substructures in general formal contexts, including their influence on concept counts, rather than these path-power incidence lattices.

## Limitations

The theorem concerns only finite reflexive path-power contexts; removing diagonal incidence, replacing a path by a cycle, or switching to induced graph bicliques changes the problem. The formulas require exact uniform radius and labeled path order. A literature search has not established global publication priority; an equivalent specialization in work on interval matrices or maximal bicliques may exist. Neither finite verification nor database nonmatches establishes originality or independent certification.

## References

1. M. G. Rawson, A. Myers, R. Green, M. Robinson, C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first public 2023-07-21, Sections 2–4 and Theorem 3.1. https://arxiv.org/abs/2307.11681
2. H. B. Macêdo Filho, S. Dantas, R. C. S. Machado, C. M. H. Figueiredo, *Biclique-colouring verification complexity and biclique-colouring power graphs*, arXiv:1203.2543, first public 2012-03-12, Sections 3–4 (version 2, 2013). https://arxiv.org/html/1203.2543v2
3. M. Koyda, G. Stumme, *Boolean Substructures in Formal Concept Analysis*, arXiv:2104.07159, first public 2021-04-14, Sections 2–3 and 6. https://arxiv.org/abs/2104.07159
