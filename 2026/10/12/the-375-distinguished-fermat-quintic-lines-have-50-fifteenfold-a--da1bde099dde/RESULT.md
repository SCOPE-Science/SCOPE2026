# The 375 distinguished Fermat-quintic lines have 50 fifteenfold and 1875 double intersection points

## Finding
Let \(X\subset\mathbb P^4_{\mathbb C}\) be the Fermat quintic threefold
\[
X=\{x_0^5+x_1^5+x_2^5+x_3^5+x_4^5=0\}.
\]
Consider the distinguished set \(\mathcal L\) of \(375\) lines lying in two distinct irreducible components of the Fano scheme of lines on \(X\), as described by Albano--Katz and Pauli. Their **ambient projective intersection geometry** is as follows:

1. Exactly \(50\) points lie on \(15\) members of \(\mathcal L\) each, and exactly \(1875\) further points lie on \(2\) members each; there are no other points common to two distinct members. The two strata have respectively two and four nonzero homogeneous coordinates.
2. The simple graph \(G\) on \(\mathcal L\), joining distinct lines when they intersect in \(\mathbb P^4\), has \(375\) vertices, \(7125=5250+1875\) edges and constant degree \(38\). Every line meets \(28\) others at its two coordinate-pair endpoints and \(10\) others at four-coordinate points.
3. An edge of the first type has exactly \(13\) common neighbors, while an edge of the second type has exactly \(1\) common neighbor. Consequently the clique number of \(G\) is \(15\), and its precisely \(50\) maximal cliques of size \(15\) are the sets of lines through the fifty-coordinate-pair points.
4. These \(50\) cliques canonically recover the \(50\) Fano-curve components: each line belongs to exactly two cliques, and the graph with clique-vertices and line-edges is the fivefold independent-set blow-up \(KG(5,2)[\overline{K}_5]\) of the Petersen graph \(KG(5,2)\).

The edge counts concern *intersections of line images in projective space*, not intersections of parameter curves inside the Fano scheme. They are distinct incidence notions.

## Assumptions and scope
All intersections are set-theoretic over \(\mathbb C\); no scheme-theoretic intersection multiplicities or deformation contributions are asserted. Fix a primitive fifth root of unity \(\zeta\). For an omitted coordinate \(e\), partition the other four indices into two unordered pairs \(\{a,b\}\) and \(\{c,d\}\) with \(a<b\), \(c<d\). For \(r,s\in\mathbb Z/5\mathbb Z\) define a line parametrically by
\[
(x_a,x_b,x_c,x_d,x_e)=(u,-\zeta^r u,v,-\zeta^s v,0).
\]
Coordinates in this display are indexed by their subscripts; this is not an instruction that indices occur in numerical order. The number of resulting distinct lines is \(5\cdot3\cdot5^2=375\), and each lies on \(X\) because its two pairs of fifth powers cancel. This is exactly the distinguished finite crossing set in the cited Fano-curve description.

## Proof
**Classification of intersection supports.** Every point on a member of \(\mathcal L\) has either two nonzero coordinates (one parameter vanishes) or four (both parameters nonzero). A point supported on a pair \(\{a,b\}\) has \(x_a^5+x_b^5=0\). There are \(\binom{5}{2}\cdot5=50\) such points. Any special line through one of them uses that support pair, chooses its omitted index in the other three coordinates, and chooses one of five possible fifth-root ratios on the remaining coordinate pair. Hence exactly \(3\cdot5=15\) distinct special lines pass through each such point. Each special line has exactly two such endpoints.

Now fix a point \(P\) with four nonzero coordinates, omitting \(e\). A special line through it pairs the four coordinates into two pairs with *opposite fifth powers*. A second, distinct pairing is possible precisely when the four fifth powers consist of two copies of one value and two of its negative. There are three unordered partitions of the four indices into these two sign classes. For each partition, rescaling to make a chosen nonzero coordinate \(1\) leaves five choices for each of the other three coordinates, producing \(5^3\) points. Thus there are exactly \(5\cdot3\cdot5^3=1875\) four-support intersection points, and each belongs to exactly two special lines (the two matchings between the opposite-sign classes). For any other four-support point the pairing is unique, so it is not an intersection point. Two special lines cannot share more than one point without coinciding; distinct lines also have no common five-support or three-support point. This proves the full list of points and multiplicities.

**Graph degrees and the family-graph structure.** Each line meets \(14\) other special lines at either endpoint, giving \(28\). Its four-coordinate point with parameter ratio \(v/u\) lies on a second special line exactly when \((v/u)^5=1\) or \((v/u)^5=-1\), giving ten more distinct neighbors. Thus the degree is \(38\), and the total edge count is
\[
50\binom{15}{2}+1875\binom{2}{2}=5250+1875=7125.
\]
For a two-support point, the coordinate-pair support \(\{a,b\}\) and its fifth-root ratio specify one of the fifty Fano-curve cones whose generator lines pass through this vertex. Two such vertices determine a distinguished line exactly when their support pairs are disjoint, in which case the fifth root labels may be chosen independently. As the ten two-element support sets have the Petersen disjointness graph \(KG(5,2)\), splitting each support set into its five labelled choices gives the stated blow-up. Each distinguished line lies in exactly two such Fano components, corresponding to its two endpoints.

**Intrinsic clique recovery.** An exact finite incidence reduction makes the two edge types distinguishable without coordinates: for any two intersecting special lines, count their common-neighbor lines. The counts are \(13\) when they share a two-coordinate endpoint and \(1\) when they meet at a four-coordinate point. To reproduce this computation, encode each line as two oriented labelled pairs \((a,b,r)\) representing \(x_b=-\zeta^r x_a\). Distinct lines meet at a two-coordinate point iff they share a labelled pair. Otherwise they can meet only if they omit the same coordinate and have different pairings; then their four ratio constraints form an alternating four-cycle, which has a nonzero solution exactly when the signed fifth-root exponents around the cycle sum to zero modulo \(5\). The included `verify.py` enumerates all \(\binom{375}{2}=70125\) pairs using these exact integer congruences, classifies the common-neighbor counts and checks that a two-coordinate edge has as its whole common-neighbor set the other \(13\) members of its unique fifteen-line pencil.

Any clique of order at least \(4\) has an edge with at least two common neighbors; such an edge must be of the two-coordinate type. The whole clique therefore lies in its fifteen-line pencil. Each pencil is a clique, so the clique number is \(15\) and all \(15\)-cliques are exactly these \(50\) pencils. The Fano-component reconstruction follows. These finite checks cover the entire explicitly defined \(375\)-vertex object; no inference from random sampling is involved.

## Verification
The standalone standard-library verifier `verify.py` builds all \(375\) lines and checks all \(70125\) pairs by exact modular fifth-root constraints; it independently compares every meet/nonmeet decision with a \(5\times4\) rank calculation over \(\mathbb F_{11}\). That finite-field comparison is a secondary consistency check; the proof of the characteristic-zero statement is the binomial support-and-ratio classification above, not a finite-field extrapolation. The verifier also checks the \(50\) incidence pencils, blow-up graph, common-neighbor numbers, connectivity, and unique maximum-clique structure. Run `python3 verify.py` from the directory containing the file; no external packages are required.

## Relationship to prior work
Albano--Katz's description of the Fermat-quintic line families and their intersections in the Fano scheme, used in Pauli's section 6, supplies the \(50\) irreducible family components and \(375\) special lines. The present result counts instead the intersections **of those distinct projective lines with one another**. The additional \(1875\) four-coordinate double intersections, regular ambient-intersection graph, two edge common-neighbor types and intrinsic clique reconstruction are not supplied by the cited family/deformation counts. Katz--Morrison analyze enumerative geometry of a mirror quotient, not this graph of distinguished lines in the original quintic.

## Limitations
This is a finite, fixed-hypersurface incidence theorem over \(\mathbb C\), not a statement for a general quintic, for the full infinite family of Fermat-quintic lines, or for the scheme structure of the Fano locus. Neither curve-intersection numbers on the threefold nor effects on virtual counts are inferred. An older specialized incidence computation under different terminology remains a plausible bibliographic overlap risk; the concrete source comparisons are recorded separately.

## References
1. S. Pauli, *Quadratic types and the dynamic Euler number of lines on a quintic threefold*, arXiv:2006.12089 (first public 2020-06-22), especially section 6. https://arxiv.org/abs/2006.12089
2. A. Albano and S. Katz, *Lines on the Fermat quintic threefold and the infinitesimal generalized Hodge conjecture*, Trans. Amer. Math. Soc. **324** (1991), 353–368, DOI 10.1090/S0002-9947-1991-1024767-6.
3. S. Katz and D. R. Morrison, *Enumerative geometry of the mirror quintic*, arXiv:2204.01669 (2022), different quotient-geometric setting.
