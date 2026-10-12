# Rank and nilpotency-index enumerators for partial isometries of finite cycles

## Finding
For every integer \(n\ge4\), the monoid of partial isometries of the cycle graph \(C_n\) has an exact joint distribution of transformation rank and nilpotency index. Write \(0\) for the empty partial map. For \(1\le h\le n\), let
\[
N_{n,h}(X)=\sum_{\substack{\alpha\in\operatorname{PIso}(C_n)\\\alpha^h=0}}X^{\operatorname{rank}(\alpha)}.
\]
For \(h=1\), \(N_{n,1}(X)=1\). For \(h\ge2\), define the \(h\)-state transfer matrix \(T_h(X)\), with states \(0,1,\ldots,h-1\), by assigning weight \(1\) to every transition \(a\to0\), and weight \(X\) to \(a\to a+1\) for \(a<h-1\), with no other transitions. Its weighted adjacency matrix has \((a,0)\)-entry \(1\) and \((a,a+1)\)-entry \(X\), and
\[
B_{t,h}(X)=\operatorname{tr}(T_h(X)^t).
\]
The exact rank enumerator of nilpotents of index at most \(h\) is
\[
\boxed{\displaystyle N_{n,h}(X)=
\sum_{t\mid n}\varphi(t)B_{t,h}(X)^{n/t}+R_n(X)
-(2n-1)-n(n-1)X-\mathbf1_{2\mid n}\frac{n(n-2)}2X^2,}
\]
where \(\varphi\) is Euler's totient and
\[
R_n(X)=\begin{cases}
n(1+2X)^{(n-1)/2},&n\text{ odd},\\[2mm]
\dfrac n2\bigl((1+2X)^{n/2}+(1+2X)^{(n-2)/2}\bigr),&n\text{ even}.
\end{cases}
\]
The polynomial for elements of exact index \(h\) is \(N_{n,h}(X)-N_{n,h-1}(X)\), taking \(N_{n,0}=0\); the empty partial map has index \(1\).

In particular, writing \(N_n(X)=N_{n,n}(X)\), all nilpotent partial isometries are counted by
\[
\boxed{\displaystyle N_n(X)=
\sum_{t\mid n}\varphi(t)\big((1+X)^t-X^t\big)^{n/t}
+R_n(X)-(2n-1)-n(n-1)X
-\mathbf1_{2\mid n}\frac{n(n-2)}2X^2.}
\]
The number of nilpotent elements of maximal possible rank \(n-1\), and separately the number of elements with nilpotency index exactly \(n\), are both \(n\varphi(n)\).

## Assumptions and scope
The graph \(C_n\) has vertex set \(\mathbb Z/n\mathbb Z\) and edges connecting consecutive residues. A partial isometry is a partial injection \(\alpha:A\to\mathbb Z/n\mathbb Z\) preserving graph distance on its domain \(A\). Composition is the usual composition of partial maps and the rank is \(|A|\). The equation \(\alpha^h=0\) means the \(h\)-fold partial composition has empty domain. Here \(n\ge4\) and \(1\le h\le n\). No assumption of prime cycle length or odd parity is made.

All nonempty coefficients count distinct partial maps, not pairs of an ambient permutation and a domain. This distinction is essential at ranks zero and one, and at rank two for even cycles.

## Proof
**1. Ambient dihedral restrictions and their multiplicities.** The fundamental description by Fernandes and Paulista [1, Lemma 1.1] states that every partial isometry of \(C_n\) is the restriction \(g|_A\) of an element \(g\) of the dihedral group \(D_{2n}\) of order \(2n\). For a domain of size at least three, the extension is unique. For a singleton domain, exactly two dihedral elements extend a given partial map. For a two-point domain, extension is unique except when the two vertices are antipodal on an even cycle, in which case there are exactly two extensions. For the empty domain, every dihedral element supplies the same empty map.

**2. Powers become circular forbidden runs.** If \(\alpha=g|_A\), then \(\alpha^h\) is nonempty if and only if some \(v\) satisfies \(v,gv,\ldots,g^{h-1}v\in A\). Along each cycle of \(g\), mark members of \(A\) with ones. Thus \(\alpha^h=0\) precisely when every cyclic word so obtained avoids a circular run of \(h\) consecutive ones. This includes the condition that no entire permutation cycle is selected.

**3. Cyclic transfer matrix.** A legal cyclic binary word of length \(t\) has a zero. Just before reading each successive position, the number of consecutive ones since the preceding zero lies in \(\{0,\ldots,h-1\}\); reading zero resets the state, while reading one increments it. There is a unique periodic state itinerary for each legal word. Conversely, every closed walk of length \(t\) in the transfer graph represents one legal cyclic word; an all-ones word has no closed walk because its state would strictly increase indefinitely. The trace of the weighted adjacency power therefore counts legal words by their number of ones, proving \(B_{t,h}(X)=\operatorname{tr}(T_h(X)^t)\).

**4. Rotations and reflections.** A rotation of order \(t\) has \(n/t\) disjoint cycles of length \(t\), and exactly \(\varphi(t)\) rotations have this order. Independent domain choices on its cycles contribute \(B_{t,h}(X)^{n/t}\). If \(h\ge2\), a reflection's fixed vertices cannot be chosen, while on each of its two-cycles one may choose neither vertex or exactly one of the two; these choices contribute \(1+2X\). An odd cycle has \(n\) reflections, each with one fixed vertex and \((n-1)/2\) two-cycles. An even cycle has \(n/2\) reflections with two fixed vertices and \((n-2)/2\) two-cycles, and \(n/2\) fixed-point-free reflections with \(n/2\) two-cycles. These produce the polynomial \(R_n(X)\).

**5. Correcting repeated extensions.** Summing the previous contributions counts pairs \((g,A)\), not distinct partial isometries. The empty map occurs \(2n\) times, requiring subtraction of \(2n-1\). Every nilpotent singleton map sends its sole domain point to a different point, so there are exactly \(n(n-1)\) such maps, each counted twice; subtract \(n(n-1)X\). On even cycles, exactly the antipodal two-point domains admit two extensions. A nilpotent map from such a domain must have its image in a *different* antipodal pair: if it maps onto its own pair, it is a permutation there and is not nilpotent. There are \(n/2\) source pairs, \(n/2-1\) different target pairs, and two bijections for each ordered pair. Thus \(n(n-2)/2\) nilpotent rank-two maps were counted twice; subtract \(n(n-2)X^2/2\). No other duplicates exist by [1, Lemma 1.1]. These corrections prove the stated formula for every \(h\ge2\). The case \(h=1\) contains only the empty map.

**6. Unbounded nilpotency and the top stratum.** A nilpotent partial injection on \(n\) points has no directed cycle and is a disjoint union of directed paths; its \(n\)-th power is therefore empty. For every divisor \(t\) of \(n\), a proper subset of a \(t\)-cycle contains no \(n\) consecutive visited points; choosing the full \(t\)-cycle produces nonnilpotence. Therefore \(B_{t,n}(X)=(1+X)^t-X^t\), giving the total-nilpotent formula. The highest possible rank is \(n-1\), and rank \(n-1\) forces a single permutation orbit on all \(n\) vertices. The ambient permutation must be an \(n\)-cycle rotation; there are \(\varphi(n)\) of these and \(n\) choices for the omitted domain point. Such a map consists of one directed path on all \(n\) vertices and has nilpotency index \(n\). Conversely, index \(n\) requires a path containing all \(n\) vertices, and hence has this form. Both asserted cardinalities are \(n\varphi(n)\).

## Verification
The standalone `checker.py` forms distinct restrictions of each dihedral permutation for \(3\le n\le10\), computes all partial powers by direct traversal, and checks each coefficient of \(N_{n,h}\) for every \(1\le h\le n\). It separately enumerates *all* distance-preserving partial injections without using the dihedral representation for \(3\le n\le6\), matching the derived monoid exactly. For each \(1\le t\le10\) and \(1\le h\le11\), it independently compares the transfer-matrix trace with direct cyclic-subset enumeration. It checks the top-rank coefficient and prints `VERIFY_OK` on success.

The total-nilpotent rank arrays for \(n=6\) and \(n=7\), including rank zero, are respectively
\[
(1,30,108,108,48,12,0),\qquad(1,42,210,266,210,126,42,0).
\]
Their totals are \(307\) and \(897\). The finite checks corroborate the general proof but do not replace it.

## Relationship to prior work
Fernandes and Paulista [1] prove the dihedral-restriction theorem and compute cardinality, Green's relations, generating rank, and presentations of the *whole* partial-isometry monoid. The present theorem uses their established extension multiplicities but counts only nilpotent elements, refined simultaneously by map rank and exact power at which zero is attained. The original total monoid cardinality does not determine this distribution. Dimitrova, Fernandes, Koppitz and Quinteiro [2] study cardinalities, Green's relations, and ranks of oriented/monotone/order-preserving *submonoids* of the dihedral inverse monoid; [3] studies presentations of these submonoids. Their inspected material does not give the nilpotency filtration calculated here.

## Limitations
The result counts nilpotent partial isometries and their ranks and indices; it does not classify products or ideals generated by these elements. The proof depends on the established dihedral-restriction lemma; it independently proves the enumerative and duplication-correction steps. Exhaustive testing was limited to \(n\le10\), not used as a proof for arbitrary \(n\). The bibliographic comparison cannot exclude every independently derived or unindexed general group-restriction enumerator.

## References
[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (first posted 2022-05-04), subsequently Turkish Journal of Mathematics **47** (2023), 1746–1760, DOI 10.55730/1300-0098.3460. Full text: https://arxiv.org/pdf/2205.02196.

[2] I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *On three submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.01519 (first posted 2023-01-04), subsequently Bulletin of the Malaysian Mathematical Sciences Society. Full text: https://arxiv.org/pdf/2301.01519.

[3] I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Presentations for three remarkable submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.02474 (first posted 2023-01-06), subsequently Semigroup Forum **107** (2023), 315–338. Full text: https://arxiv.org/pdf/2301.02474.
