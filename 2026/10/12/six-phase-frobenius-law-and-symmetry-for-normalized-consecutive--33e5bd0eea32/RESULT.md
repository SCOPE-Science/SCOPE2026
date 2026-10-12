# Six-phase Frobenius law and symmetry for normalized consecutive tetrahedral triples

## Finding

For every integer \(n\ge2\), put \(T_n=n(n+1)(n+2)/6\), \(d_n=\gcd(T_n,T_{n+1},T_{n+2})\), and
\[
S_n=\langle T_n/d_n,T_{n+1}/d_n,T_{n+2}/d_n\rangle.
\]
Every \(S_n\) is symmetric. For \(n=6k+r\), the exact Frobenius number \(F(S_n)\) is:

| \(r\) | permitted \(k\) | \(F(S_{6k+r})\) |
| --- | --- | --- |
| \(0\) | \(k\ge1\) | \(96k^3+76k^2+16k-1\) |
| \(1\) | \(k\ge1\) | \(162k^3+171k^2+45k-1\) |
| \(2\) | \(k\ge0\) | \(96k^3+140k^2+56k+3\) |
| \(3\) | \(k\ge0\) | \(30k^3+59k^2+35k+5\) |
| \(4\) | \(k\ge0\) | \(432k^3+1188k^2+1068k+309\) |
| \(5\) | \(k\ge0\) | \(30k^3+85k^2+75k+19\) |

The genus is \(g(S_n)=(F(S_n)+1)/2\). The embedding dimension is \(2\) precisely for \(n=2,3\), and \(3\) for all \(n\ge4\). In particular, the accumulation points of \(F(S_n)/n^3\) form exactly
\[
\left\{\frac5{36},\frac49,\frac34,2\right\}.
\]

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of the nonnegative integers. The Frobenius number is its largest omitted nonnegative integer; the genus is the number of omitted nonnegative integers. A numerical semigroup with Frobenius number \(F\) is symmetric if for every integer \(z\), exactly one of \(z\in S\) and \(F-z\in S\) holds. There is no upper bound on \(n\). The index begins at \(n=2\), and every displayed normalization is by the exact common gcd of the three tetrahedral numbers. No assertion is made about the unnormalized triple, whose gcd can exceed one.

## Proof

**1. Uniform gluing lemma.** Suppose \(u,v,h,W\) are positive integers with \(\gcd(u,v)=\gcd(h,W)=1\) and \(W\in\langle u,v\rangle\). Put \(S=\langle hu,hv,W\rangle\). Let \(\operatorname{Ap}(S,hu)\) be its Apéry set relative to \(hu\). Then
\[
\operatorname{Ap}(S,hu)=\{ihv+jW:0\le i<u,\ 0\le j<h\}.
\]
Indeed, write any element as \(h(au+bv)+cW\) with \(a,b,c\ge0\). Since \(W\in\langle u,v\rangle\), writing \(c=qh+j\) permits absorption of \(qhW\) into \(h\langle u,v\rangle\); likewise absorb multiples of \(u\) from \(b\) into the \(hu\)-coefficient. Thus every element reduces to an element of the displayed rectangular set plus a nonnegative multiple of \(hu\). These \(hu\) elements are pairwise incongruent modulo \(hu\): first modulo \(h\), the coprimality of \(h,W\) determines \(j\); then modulo \(u\), coprimality of \(u,v\) determines \(i\). Therefore the set is precisely the Apéry set. Its maximum and sum give
\[
F(S)=huv-hu-hv+(h-1)W,
\qquad
 g(S)=\frac{F(S)+1}{2}.
\]
The Apéry criterion also proves symmetry: each residue-pair \((i,j)\) complements to \((u-1-i,h-1-j)\), making the rectangle symmetric about its maximum; equivalently, \(g=(F+1)/2\) is the standard characterization of a symmetric numerical semigroup.

**2. Six exact factorizations.** Let \(n=6k+r\) and denote the normalized consecutive tetrahedral values by \((a,b,c)\). The table gives their factorizations, \(d_n\), a preferred pair \((U,V)\), its gcd \(h\), and a nonnegative expression for the remaining generator \(W\) in \(U/h,V/h\). Rows \(0\) and \(1\) start with \(k\ge1\); the others start with \(k\ge0\).

| \(r\) | \(d_n\) | \(a\) | \(b\) | \(c\) | \(h\) | \((U,V,W)\) and witness |
| --- | --- | --- | --- | --- | --- | --- |
| \(0\) | \(3k+1\) | \(2k(6k+1)\) | \((2k+1)(6k+1)\) | \(2(2k+1)(3k+2)\) | \(6k+1\) | \((a,b,c)\); \(W=2(3k+2)(V/h)\) |
| \(1\) | \(2k+1\) | \((3k+1)(6k+1)\) | \(2(3k+1)(3k+2)\) | \((3k+2)(6k+5)\) | \(3k+1\) | \((a,b,c)\); \(W=(3k+2)(U/h)+2(V/h)\) |
| \(2\) | \(3k+2\) | \(2(2k+1)(3k+1)\) | \((2k+1)(6k+5)\) | \(2(k+1)(6k+5)\) | \(2k+1\) | \((a,b,c)\); \(W=2(k+1)(V/h)\) |
| \(3\) | \(6k+5\) | \((2k+1)(3k+2)\) | \(2(k+1)(3k+2)\) | \((k+1)(6k+7)\) | \(3k+2\) | \((a,b,c)\); \(W=3(k+1)(U/h)+2(V/h)\) |
| \(4\) | \(k+1\) | \(2(3k+2)(6k+5)\) | \((6k+5)(6k+7)\) | \(2(3k+4)(6k+7)\) | \(6k+5\) | \((a,b,c)\); \(W=2(3k+4)(V/h)\) |
| \(5\) | \(6k+7\) | \((k+1)(6k+5)\) | \(2(k+1)(3k+4)\) | \((2k+3)(3k+4)\) | \(3k+4\) | \((c,b,a)\); \(W=(k+1)(U/h)+(2k+1)(V/h)\) |

The entries for \(a,b,c\) follow by substituting \(6k+r\) into \(T_n=n(n+1)(n+2)/6\). Direct Euclidean identities give \(\gcd(U,V)=h\), \(\gcd(U/h,V/h)=1\), and \(\gcd(h,W)=1\) for every row. For example, in row \(4\), \(\gcd(6k+4,6k+7)=\gcd(6k+4,3)=1\), while \(\gcd(6k+5,2(3k+4)(6k+7))=1\). In row \(5\), \(\gcd(2k+2,2k+3)=1\) and \(\gcd(3k+4,(k+1)(6k+5))=1\). The other rows are identical one-step Euclidean reductions: row \(0\) uses differences \(2\) and \(3\) and \(6k+1\equiv1\pmod3\); row \(1\) uses differences \(1\) and \(3\) and \(3k+1\equiv1\pmod3\); row \(2\) uses differences \(1\), \(2\), \(3\); and row \(3\) uses differences \(1\) and \(3\) and \(3k+2\equiv2\pmod3\). In particular the displayed \(d_n\) is the exact gcd, since the displayed factorizations reproduce the original tetrahedral numbers and \(\gcd(a,b,c)=1\). Each final-column identity proves \(W\in\langle U/h,V/h\rangle\) with nonnegative coefficients. Therefore the uniform gluing lemma applies in all six cases.

**3. Exact formula, genus, symmetry.** Substitute each row into \(F=UV/h-U-V+(h-1)W\) and expand. The six resulting cubics are the six entries in the Finding table. The same lemma gives the genus formula and symmetry for every allowed \(k\), hence for all \(n\ge2\).

**4. Embedding dimension.** For \(n=2\), \((a,b,c)=(2,5,10)\); for \(n=3\), \((a,b,c)=(2,4,7)\), so the dimension is two. For \(n=4,5,6\), the triples are respectively \((20,35,56)\), \((5,8,12)\), \((14,21,30)\); each is a minimal three-element generating set. For \(n\ge7\), the strict inequalities \(a<b<c<2a\) follow from \((n+3)(n+4)<2n(n+1)\); therefore none of the three distinct generators is generated by the other two.

**5. Cubic phase spectrum.** Divide the leading terms in the six formulas by \((6k+r)^3\). The resulting limits, as \(k\to\infty\), are \(4/9,3/4,4/9,5/36,2,5/36\), respectively. Every divergent sequence of indices has a subsequence in some fixed residue class. This proves that the four distinct values displayed in the Finding are exactly the accumulation points.

## Verification

Run `python3 verify.py` from the directory containing the bundled verifier; it needs Python 3.9 or later and only the standard library. The independent Dijkstra/Apéry shortest-residue method computes exact Frobenius numbers and genera for every \(2\le n\le140\) and checks the six symbolic formulas, gcd normalization, gluing identities, and symmetry. The expected success line begins `EXACT_REGRESSION_OK`. This is an additional finite check; it is not the basis of the infinite proof.

## Relationship to prior work

OEIS A069761 (submitted April 9, 2002) tabulates Frobenius numbers of **four** consecutive tetrahedral numbers, not this normalized three-generator family. Robles-Pérez and Rosales (arXiv:1706.04378, 2017), especially Sections 3 and 4.3, determine Frobenius numbers and free numerical-semigroup structure for **four** consecutive tetrahedral numbers and supply closely related gcd and telescopic identities. Their published pair-gcd ingredients and the classical gluing method motivate the algebra above, but their stated four-generator theorem does not give the normalized three-generator family, its six cubics, or its phase spectrum. Pascadi (arXiv:1712.02522, 2017) develops general reduction-graph techniques and considers triangular and tetrahedral examples, mainly the established four-term tetrahedral instance. This proof explicitly supplies the additional normalization, six-row witnesses, and Apéry rectangle not asserted in those sources. The general two-generator Frobenius and Apéry-set results are classical and not claimed as new.

## Limitations

The result concerns the gcd-normalized **three** consecutive tetrahedral numbers, not the unnormalized triple, four consecutive tetrahedral numbers, arbitrary figurate-number sequences, or semigroups of higher embedding dimension. The six-phase theorem is an explicit specialization of classical gluing, and the literature overlap risk is that an unindexed equivalent specialization may have appeared elsewhere. The supplied computational check covers \(n\le140\) only; the proof supplies all larger cases. No independent external validation has been performed.

## References

1. V. A. Sapko, OEIS A069761, “Frobenius number of the numerical semigroup generated by four consecutive tetrahedral numbers”, first submission April 9, 2002, https://oeis.org/A069761.
2. A. M. Robles-Pérez and J. C. Rosales, “The Frobenius number for sequences of triangular and tetrahedral numbers”, arXiv:1706.04378 (first posted June 14, 2017), especially Sections 3 and 4.3, https://arxiv.org/abs/1706.04378.
3. A. Pascadi, “A Graphical Approach to Finding the Frobenius Number, Genus and Hilbert Series of a Numerical Semigroup”, arXiv:1712.02522 (first posted December 7, 2017), https://arxiv.org/abs/1712.02522.
4. A. Brauer and J. E. Shockley, “On a problem of Frobenius”, Journal für die reine und angewandte Mathematik, 211 (1962), 215–220 (general gcd reduction/Frobenius formula, cited in reference 2).
