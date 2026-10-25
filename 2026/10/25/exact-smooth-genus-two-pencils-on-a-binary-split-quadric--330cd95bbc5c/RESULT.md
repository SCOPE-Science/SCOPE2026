# Exact smooth genus-two pencils on a binary split quadric

## Finding
Let \(Q=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\) and \(V=H^0(Q,\mathcal O_Q(2,3))\), a twelve-dimensional vector space over \(\mathbf F_2\). A *fully smooth pencil* is a two-dimensional \(\mathbf F_2\)-linear subspace \(W\subset V\) whose three nonzero sections each cut out a geometrically smooth curve. Every such member has genus two.

Among the \(2\,794\,155\) two-dimensional subspaces of \(V\), **exactly \(44\,070\)** are fully smooth. Under the complete \(36\)-element group of automorphisms of \(Q\) preserving \(\mathcal O_Q(2,3)\), these pencils form **\(1\,242\)** orbits: one of size \(6\), three of size \(12\), thirty of size \(18\), and \(1\,208\) of size \(36\).

The rational base-locus distribution is exact:

| Number of common \(\mathbf F_2\)-points | Pencils |
|:--:|--:|
| \(0\) | \(6\,066\) |
| \(1\) | \(16\,884\) |
| \(2\) | \(17\,424\) |
| \(3\) | \(3\,696\) |

Consequently, three is the sharp maximum of the number of *rational* base points. There are \(6\,066\) fully smooth pencils without an \(\mathbf F_2\)-rational base point. All the pencils nonetheless have geometric base loci: the intersection product of two divisors of type \((2,3)\) equals \(12\), counting multiplicities.

## Assumptions and scope
All fields, parameter spaces, and counts in this statement are over \(\mathbf F_2\). The curves are embedded divisors on the **split** smooth quadric, not abstract genus-two isomorphism classes. Equivalence is under the automorphism group of the polarized surface \((Q,\mathcal O_Q(2,3))\), namely \(\operatorname{PGL}_2(\mathbf F_2)\times\operatorname{PGL}_2(\mathbf F_2)\); exchanging factors does not preserve the bidegree. The word *smooth* always means smooth after base change to an algebraic closure.

Fix homogeneous coordinates \(([X_0:X_1],[Y_0:Y_1])\), with the coefficient bit \(4i+j\), for \(0\le i\le2\), \(0\le j\le3\), attached to the monomial \(X_0^{2-i}X_1^iY_0^{3-j}Y_1^j\). The integer mask \(1\le m\le4095\) uniquely specifies a nonzero section. The format of `ORBIT_REPRESENTATIVES.csv` uses this convention. A pencil is determined by its three nonzero masks \(\{a,b,a\mathbin{\mathrm{xor}}b\}\).

## Proof
1. On the four standard affine charts of \(Q\), dehomogenize every section. A point is a geometric singularity of the divisor exactly when the local polynomial and both formal first derivatives vanish there. Over an algebraically closed field the resulting ideal has an affine common zero exactly when it is **not** the unit ideal. Buchberger's algorithm over \(\mathbf F_2\), without sampling extension fields, makes this decision exactly. Independently implemented symbolic Gröbner calculations agree for all \(4095\) nonzero masks: precisely \(1116\) masks are geometrically smooth. For any such section, adjunction on \(\mathbf P^1\times\mathbf P^1\) gives \(g=(2-1)(3-1)=2\).

2. For \(a,b\) distinct nonzero masks, the associated two-dimensional \(\mathbf F_2\)-subspace consists of \(\{0,a,b,a\mathbin{\mathrm{xor}}b\}\). Its projective members are all smooth if and only if these three masks lie in the verified smooth set \(\mathcal S\). Enumeration of all distinct pairs and deduplication by their sorted triples gives exactly \(44\,070\) pencils.

3. For each pair of generators, evaluate the two sections at the nine rational points of \(Q\). A rational point belongs to their scheme-theoretic base precisely when both evaluations vanish. Counting the resulting base-point intersections over all verified pencils gives the four displayed totals. In a separate additive-Fourier computation, use the Walsh--Hadamard transform of the characteristic function of the smooth-mask set and of its restrictions to vanish at prescribed rational points. The formula
\[
N_U=\frac{1}{6\cdot2^{12}}\sum_{\chi\in\widehat{\mathbf F_2^{12}}}\widehat{1_{\mathcal S_U}}(\chi)^3
\]
counts fully smooth pencils whose base contains a chosen set \(U\) of rational points. Summing over subsets \(U\) of sizes \(0,1,2,3,4\) gives the binomial moments \((44\,070,62\,820,28\,512,3\,696,0)\). Binomial inversion recovers exactly the distribution above, and the vanishing fourth moment proves that no pencil has four or more rational base points.

4. The two projective linear groups each have six elements. Expand the action of all their \(36\) pairs on the twelve monomials; these are invertible transformations preserving geometric smoothness. Partition the \(44\,070\) pencils into their full orbits, obtaining sizes \(6,12,18,36\) with frequencies \(1,3,30,1208\). The complete catalogue contains the lexicographically minimal triple of masks for each of the \(1242\) orbits, together with orbit size and rational base-point count. Directly summing catalogue orbit sizes gives \(44\,070\) and independently reproduces the four base-point totals.

No step treats a finite sample as an infinite proof: every computation ranges over a specified finite space, and the Jacobian-ideal criterion is equivalent to geometric smoothness over the algebraic closure.

## Verification
The standalone reproducibility files are `gf2_ideal.py`, `enumerate_pencils.py`, `verify_walsh.py`, `ORBIT_REPRESENTATIVES.csv`, `COUNTS.json`, `SMOOTHNESS_OUTPUT.txt`, and `WALSH_OUTPUT.txt`. All principal calculations use Python's built-in integer and set operations and require no nonstandard modules. Run `python enumerate_pencils.py ORBIT_REPRESENTATIVES.csv` and `python verify_walsh.py` in their extracted directory. The first performs the exact ideal tests, enumerates pencils, generates all \(36\) automorphisms, and writes the deterministic catalogue. The second gives an independent Fourier-counting verification conditional on the separately rechecked smoothness set. A separate symbolic Gröbner implementation using SymPy was run for all masks and agreed with the supplied pure-Python ideal calculation.

## Relationship to prior work
Asgarli and Ghioca (2022) study smooth members of linear pencils over finite fields and give existence theorems and explicit cases for hypersurfaces in projective space. The present claim concerns a different polarized surface and supplies exact binary-field arithmetic counts, complete projective orbit sizes, and base-point incidence data; those numbers do not follow from the inspected existence theorems. Zobernig (2021) studies genus-two moduli and \(p\)-rank strata, not pencils of specified bidegree on a split quadric. The prior enumeration of individual embedded genus-two curves, when available, does not itself constitute a classification of three-member pencils or their intersections. A previously unindexed exact computation is a residual publication-priority possibility.

## Limitations
The catalogue classifies embedded linear systems under ruling-preserving projective changes, **not** abstract isomorphism classes of genus-two curves, and does not classify scheme structures of the full degree-twelve geometric base intersections. A base-locus count of zero refers only to \(\mathbf F_2\)-points. Verification is exact but was not independently audited by an external mathematician. The literature comparison is bounded and cannot certify global publication priority.

## References
- Shamil Asgarli and Dragos Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169v1 (14 March 2022), https://arxiv.org/abs/2203.07169 .
- Lukas Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270v1 (14 November 2021), https://arxiv.org/abs/2111.07270 .
