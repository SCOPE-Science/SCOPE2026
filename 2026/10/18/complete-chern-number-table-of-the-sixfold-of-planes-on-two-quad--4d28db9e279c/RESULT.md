# Complete Chern-number table of the sixfold of planes on two quadrics

## Finding

Let \(X\subset\mathbb P^8_\mathbb C\) be a smooth complete intersection of two sufficiently general quadrics. Its Fano scheme \(F=F_2(X)\) of projective planes is a smooth projective sixfold. Write \(H=c_1(\det\mathcal U^\vee)|_F\), where \(\mathcal U\) is the tautological rank-three bundle on \(G=\operatorname{Gr}(3,9)\), and \(c_i=c_i(T_F)\). Then \(c_1=H=-K_F\); all eleven top-dimensional monomials in \(H,c_2,\ldots,c_6\) have the following intersection numbers:

| Characteristic number | Value |
|:--|--:|
| \(\int_F H^6\) | 3904 |
| \(\int_F c_2H^4\) | 3072 |
| \(\int_F c_3H^3\) | 1664 |
| \(\int_F c_4H^2\) | 896 |
| \(\int_F c_5H\) | 384 |
| \(\int_F c_6\) | 256 |
| \(\int_F c_2^2H^2\) | 2880 |
| \(\int_F c_2c_3H\) | 1728 |
| \(\int_F c_2^3\) | 5248 |
| \(\int_F c_2c_4\) | 1792 |
| \(\int_F c_3^2\) | 1088 |

In particular, the anticanonical volume is \(3904\), and the topological Euler characteristic is \(256\). The Euler characteristic also follows from previously known cohomological results; it is included for completeness and is **not** claimed as a new invariant.

## Assumptions and scope

The base field is \(\mathbb C\), and the defining pair of quadrics is general enough for the expected-dimensional smooth Fano scheme. Here \(G\) parametrizes three-dimensional vector subspaces, equivalent to projective planes. The complete set of weighted Chern monomials of dimension \(6\) is obtained from the eleven partitions of \(6\), replacing all \(c_1\) factors with \(H\). The result is numerical for this polarized sixfold, not a formula for arbitrary intersections of quadrics or a determination of the entire Chow ring.

## Proof

1. A plane in \(\mathbb P^8\) lies on each quadric exactly when each quadratic form restricts to zero on the corresponding rank-three subspace. Hence \(F\) is the common zero locus of a general section of
\[\mathcal E=(\operatorname{Sym}^2\mathcal U^\vee)^{\oplus2}\]
on \(G\). The bundle is globally generated, with \(\dim G=18\), \(\operatorname{rk}\mathcal E=12\), and expected \(\dim F=6\). Generic Bertini/transversality gives smoothness. Its nonzero top intersection below also ensures nonemptiness.

2. The regular-embedding normal sequence gives
\[c(T_F)=\left.\frac{c(T_G)}{c(\mathcal E)}\right|_F,\qquad [F]=c_{12}(\mathcal E)\cap[G].\]
Moreover, \(K_G=-9H\) and \(c_1(\mathcal E)=8H\), so adjunction yields \(K_F=-H\). This identifies the Plücker class with the anticanonical class.

3. Here is a completely explicit finite coefficient formula, sufficient to reproduce every number. For any nine pairwise distinct nonzero formal torus weights \(t_1,\ldots,t_9\), sum over the \(\binom{9}{3}=84\) three-element subsets \(I\), with complement \(J\). At the \(I\)-fixed point put
\[h_I=-\sum_{i\in I}t_i,\quad
A_I(z)=\frac{\prod_{i\in I,j\in J}(1+(t_j-t_i)z)}{\prod_{i\le j,\ i,j\in I}(1-(t_i+t_j)z)^2},\]
where the lower product is over the six unordered pairs with repetition. Write \(a_{I,k}=[z^k]A_I(z)\). For any monomial \(P(H,c_2,\ldots,c_6)\) of total weighted degree six, equivariant localization gives
\[\int_F P=\sum_{|I|=3}\frac{\left(\prod_{i\le j,\ i,j\in I}(t_i+t_j)^2\right)P(h_I,a_{I,2},\ldots,a_{I,6})}{\prod_{i\in I,j\notin I}(t_j-t_i)}.\]
All signs match the weights of \(\mathcal U^\vee\) and \(T_G\). Because the integrands have exactly the dimension of \(G\) after multiplying by \(c_{12}(\mathcal E)\), the sums are constants independent of the distinct torus weights. Computing the degree-six truncations in this finite formula yields exactly the eleven values displayed above; every step uses rational arithmetic.

4. As an independent check of the leading entry, the Grassmannian coefficient-extraction formula gives
\[\int_F H^6=[x^8y^7z^6]\Bigl(\prod_{a\le b,\ a,b\in\{x,y,z\}}(a+b)^2\Bigr)(x+y+z)^6(x-y)(x-z)(y-z)=3904.\]
This agrees with localization and establishes the claimed anticanonical volume independently of torus-weight selection. The \(256\) in the final Chern entry is the topological Euler characteristic by Chern–Gauss–Bonnet.

## Verification

The accompanying `verify.py` performs all 84 localization summands with exact fractions for two unrelated nine-weight lists, checks all eleven results, and independently checks the degree \(3904\) by Grassmannian coefficient extraction. It prints `VERIFY_OK` upon success. Numerical evaluation is exhaustive (84 fixed points), unlike a finite sample of theorems. The algebraic localization and normal-sequence identities prove that the exact computed values apply to every smooth member of the indicated general family.

## Relationship to prior work

Ji and Suzuki (2026) prove motivic formulas for \(F_0(X)\) and \(F_1(X)\), and for **relative** Fano schemes on a quadric pencil, rather than these intrinsic tangent characteristic numbers of \(F_2(X)\). Belmans et al. (2024) and Chen–Vilonen–Xue calculate the cohomological/Hodge information for Fano schemes of intersections of two quadrics. In particular, the Euler number \(256\) is covered by prior cohomology; Hodge numbers do not determine the ten remaining polarized and intrinsic Chern intersection numbers. The underlying tautological-bundle and localization formulas are standard, but no previously tabulated complete eleven-entry table for this particular sixfold was located in the inspected works and targeted searches.

## Limitations

The complete numerical Chern table, not the ambient bundle formula, is the claimed contribution. Hodge numbers, topological Euler characteristic, smoothness, and the basic Fano scheme construction are established background. A universal characteristic-class formula may yield the table by specialization; numerical novelty does not establish historical priority. The calculation does not establish additional structural facts about the Chow ring, integral cohomology, or moduli of special non-general quadric pairs. The 2024 paper's entire full text and older specialized computational literature were not exhaustively inspected.

## References

- Lena Ji and Fumiaki Suzuki, *Motivic classes of Fano schemes of lines on intersections of two quadrics*, arXiv:2609.36233v1 (28 September 2026), especially Section 1 and Theorems 1.1–1.3.
- Pieter Belmans et al., *On decompositions for Fano schemes of intersections of two quadrics*, arXiv:2403.12517 (2024), Introduction and Hodge-number results.
- Tsao-Hsien Chen, Kari Vilonen and Ting Xue, *On the cohomology of Fano varieties and the Springer correspondence*, arXiv:1602.03052 (2016).
- Atiyah–Bott/Berline–Vergne equivariant localization formula; standard tautological normal-sequence and splitting-principle formulas.
