# Three Cartier-stable rank strata in a characteristic-seven genus-four cyclic trigonal pencil

## Finding
Let \(k\) be an algebraically closed field of characteristic \(7\), and let \(C_a\) be the smooth projective model of \(y^3=x^5+a x^2+1\). For exactly the smooth parameters \(a\in k\) with \(a^5\ne-1\), the genus is \(4\). The Jacobian's \(a\)-number is always \(2\), while its \(7\)-rank is
\[
 f_7(C_a)=\begin{cases}
 0,&a=0,\\
 1,&a^5=1,\\
 2,&a\ne0\text{ and }a^5\ne1.
 \end{cases}
\]
The third case is understood on the smooth domain \(a^5\ne-1\). Thus the rank-one stratum comprises exactly five distinct geometric parameters, the rank-zero stratum is the single parameter \(a=0\), and all remaining smooth parameters have rank two. All five rank-one parameters lie in one orbit under the explicit fifth-root coordinate scalings; no classification of all geometric isomorphisms is asserted.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(7\); the curves are smooth, projective, geometrically connected normalization models of the indicated affine equations. A Jacobian's \(p\)-rank is the dimension of its maximal étale \(p\)-torsion, equivalently the stable rank of Frobenius on \(H^1(C,\mathcal O_C)\). Its \(a\)-number is \(g-\operatorname{rank}(\mathcal C)\), where \(\mathcal C\) is Cartier on \(H^0(C,\Omega_C^1)\). The curve is a tame degree-three Kummer cover of the line, branched at five simple roots and infinity; Riemann–Hurwitz gives \(g=(3-1)(5-1)/2=4\). The polynomial \(F=x^5+a x^2+1\) is squarefree precisely when \(a^5\ne-1\): a multiple root has \(x^3=a\) and \(x^2=3/a\), forcing \(a^5=-1\); conversely those equations have a solution whenever \(a^5=-1\). The case \(a=0\) is squarefree.

## Proof
A basis of holomorphic differentials is
\[
 \omega_1=\frac{dx}{y^2},\quad \omega_2=\frac{x\,dx}{y^2},\quad
 \omega_3=\frac{x^2\,dx}{y^2},\quad \omega_4=\frac{dx}{y}.
\]
For the first three forms, the seventh powers of the Cartier coefficients are \(M_{ij}=[x^{7(i+1)-(j+1)}]F(x)^4\), with \(0\le i,j\le2\). The last one-dimensional Cartier block has coefficient \([x^6]F(x)^2=0\). Explicit trinomial expansion gives
\[
 M=\begin{pmatrix}4a^3&4&6a^2\\0&5a&4a^3\\1&0&0\end{pmatrix}\quad\text{over }\mathbb F_7[a].
\]
The actual Cartier entries are seventh roots of these coefficients; taking roots does not change rank over the perfect field. The minor using rows one and three and columns one and two equals \(3\), while \(\det M=0\) identically. Thus the Cartier rank is exactly \(2\) and \(a(C_a)=4-2=2\) throughout the smooth family.

To calculate stable Frobenius rank, use the Hasse–Witt transpose of \(M\) and respect Frobenius semilinearity. The transpose of its \(r\)-fold iterate is the product \(M^{(7^{r-1})}\cdots M^{(7)}M\), where \(M^{(q)}\) means applying the \(q\)-power Frobenius to every coefficient. For \(r=2\), the minor in the same indicated positions is
\[
 3a^4(a^{10}-1).
\]
For \(a\ne0\), \(a^{10}\ne1\), this proves the two-step product has full available rank \(2\). Applying Frobenius to this nonvanishing minor shows every adjacent twisted two-step product also has rank \(2\). Since each individual factor has rank \(2\), their images and the adjacent-pair images coincide, so every longer product also has rank \(2\). On the smooth domain, \(a^{10}=1\) is equivalent to \(a^5=1\) (the other possibility \(a^5=-1\) is singular).

When \(a=0\), the matrix \(M\) has \(M^3=0\), and all Frobenius twists equal \(M\) at this parameter; hence the stable rank is zero.

When \(a^5=1\), work in \(\mathbb F_7[a]/(a^5-1)\). The four-step product \(P_4=M^{(343)}M^{(49)}M^{(7)}M\) is
\[
 P_4=\begin{pmatrix}4&4a^2&6a^4\\2a^3&2&3a^2\\2a&2a^3&3\end{pmatrix}.
\]
Its two-by-two minors all vanish, its trace equals \(2\), and \(P_4^2=2P_4\). Thus it has rank one and is not nilpotent. Since \(a^{7^4}=a\) on the fifth-root locus, each successive four-step semilinear block has the same matrix, so the stable rank is exactly one. This proves the classification.

The transformations \(x\mapsto\zeta x\) for \(\zeta^5=1\) preserve the shape of the defining equation and send \(a\) to \(a\zeta^2\). Since multiplication by \(\zeta^2\) is transitive on the fifth roots of unity, the five rank-one parameters form one orbit under these transformations.

## Verification
Running `python3 verify_symbolic.py` computes the Cartier coefficient matrix independently by exact trinomial expansion in \(\mathbb F_7[a]\), verifies the constant-rank minor, determinant, twisted-product minor, four-step product, its minors and trace, and the nilpotent specialization. It prints `SYMBOLIC_CERTIFICATE_OK`.

Running `python3 verify_point_counts.py` independently constructs exact finite fields \(\mathbb F_{7^n}\) for \(1\le n\le4\), exhaustively counts points on all six smooth curves with \(a\in\mathbb F_7\), and derives the first four coefficients of the zeta numerator modulo seven by Newton's identities. Its resulting rank sequence for \(a=0,1,2,3,4,5\) is \(0,1,2,2,2,2\). It prints `INDEPENDENT_POINT_COUNTS_OK`. These finite-field checks corroborate, rather than establish, the theorem over the algebraic closure.

## Relationship to prior work
Obus and Shaska's investigation of superelliptic curves with many automorphisms motivates studying symmetric superelliptic subfamilies. Sutherland provides the general superelliptic Cartier–Manin block-coefficient method, including the genus-four cyclic trigonal case. Achter–Howe explain the Frobenius-semilinear distinction between Cartier–Manin and Hasse–Witt conventions. The present result does **not** claim a new Cartier algorithm or a classification of all genus-four curves. It determines the stable ranks and precise exceptional loci of this specific nonconstant, smooth one-parameter family; none of those cited articles states this three-stratum result as such.

## Limitations
The classification is for coefficient-marked curves in characteristic seven and does not count all isomorphism classes; only the explicit scaling orbit is asserted. The existing general Cartier coefficient formulas already cover the extraction of the matrix, so originality rests on the complete stable-rank stratification and its sharp exceptional loci, not on that routine matrix computation. An unindexed earlier calculation or an inaccessible result may establish the same specialization; independent priority review remains outstanding. Finite point counting is not an independent infinite-field proof.

## References
1. A. Obus and T. Shaska, *Superelliptic curves with many automorphisms and CM Jacobians*, arXiv:2006.12685 (first public 2020-06-23); especially setup and examples of symmetric superelliptic families.
2. A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, arXiv:2004.10189 (first public 2020-04-21); especially the Cartier–Manin block formula and genus-four cyclic trigonal example.
3. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: a warning and a request*, arXiv:1710.10726 (first public 2017-10-30); semilinear-order convention.
4. G. Sohn, *The a-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics **7** (2025), 59–66, DOI:10.23091/japm.2025.059; relevant possible stronger a-number source, full text unavailable in this review.
