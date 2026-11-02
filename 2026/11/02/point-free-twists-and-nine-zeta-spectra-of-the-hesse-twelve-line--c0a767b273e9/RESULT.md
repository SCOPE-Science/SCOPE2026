# Point-free twists and nine zeta spectra of the Hesse twelve-line curve

## Finding

Let \(k=\mathbb F_q\) have characteristic \(p>3\), and let \(C\subset\mathbb P^2_k\) be an arbitrary smooth plane cubic. Let \(D_C\) be the **reduced union of the twelve geometric inflection (Hesse) lines** of \(C\), regarded as a curve over \(k\). Its arithmetic genus is \(55\). The Frobenius action on its nine geometric flexes is affine on \(V=\mathbb F_3^2\): \(g(v)=Av+b\), with \(A\in\mathrm{GL}_2(\mathbb F_3)\), \(b\in V\), and \(\det A\equiv q\pmod3\).

The following ten spectral templates exhaust the actions of all \(432\) affine transformations on the four intrinsic finite configurations. The table states the number of affine elements in each template, not the number of distinct plane cubics over a fixed field. An entry \(1^a2^b\) means \(a\) Frobenius orbits of size one and \(b\) of size two. Columns \(F\) and \(B\) denote the branches above quadruple and double points, respectively.

| Type | Affine elements | Determinant | Nine flexes \(P\) | Twelve lines \(L\) | 36 flex branches \(F\) | 24 double branches \(B\) | \(\#D(\mathbb F_q)\) |
|---:|---:|---:|---|---|---|---|---:|
| 1 | 72 | 1 | \(1 2 6\) | \(1 2 3 6\) | \(1 2 3 6^{5}\) | \(2^{3} 6^{3}\) | \(q+2\) |
| 2 | 9 | 1 | \(1 2^{4}\) | \(1^{4} 2^{4}\) | \(1^{4} 2^{16}\) | \(2^{12}\) | \(4q+5\) |
| 3 | 54 | 1 | \(1 4^{2}\) | \(2^{2} 4^{2}\) | \(2^{2} 4^{8}\) | \(4^{6}\) | \(1\) |
| 4 | 108 | 2 | \(1 8\) | \(4 8\) | \(4 8^{4}\) | \(8^{3}\) | \(1\) |
| 5 | 36 | 2 | \(1^{3} 2^{3}\) | \(1^{4} 2^{4}\) | \(1^{6} 2^{15}\) | \(1^{6} 2^{9}\) | \(4q-1\) |
| 6 | 24 | 1 | \(1^{3} 3^{2}\) | \(1^{3} 3^{3}\) | \(1^{3} 3^{11}\) | \(1^{6} 3^{6}\) | \(3q\) |
| 7 | 1 | 1 | \(1^{9}\) | \(1^{12}\) | \(1^{36}\) | \(1^{24}\) | \(12q-27\) |
| 8 | 72 | 2 | \(3 6\) | \(1 2 3 6\) | \(3^{2} 6^{5}\) | \(2^{3} 3^{2} 6^{2}\) | \(q+2\) |
| 9 | 8 | 1 | \(3^{3}\) | \(1^{3} 3^{3}\) | \(3^{12}\) | \(1^{6} 3^{6}\) | \(3q\) |
| 10 | 48 | 1 | \(3^{3}\) | \(3^{4}\) | \(3^{12}\) | \(3^{8}\) | \(0\) |

Let \(p_d,\ell_d,f_d,b_d\) denote the numbers of length-\(d\) orbits in the four respective columns. **The complete rational zeta function** is

\[
Z(D_C,T)=\prod_{d\ge1}\frac{(1-T^d)^{f_d+b_d-2\ell_d-p_d}}{(1-q^dT^d)^{\ell_d}}.
\]

The ten orbit spectra yield **exactly nine distinct rational zeta functions**: types 6 and 9 have identical zeta functions despite having different rational quadruple-point counts. Every point count over any finite extension follows by replacing each fixed-object count with the sum of orbit lengths dividing that extension degree.

Write \(E\) for the elliptic curve obtained by choosing any \(k\)-point \(O\in C(k)\), and let \(\xi\in E(k)\) represent the degree-zero line-bundle class \([\mathcal O_C(1)-3O]\). Then the curve \(D_C\) is **point-free over \(k\)** if and only if both conditions hold:

1. Frobenius on \(E[3]\) is nontrivially unipotent (one Jordan block of eigenvalue one);
2. \(\xi\notin3E(k)\).

This is precisely type 10. In that case \(Z(D_C,T)=(1-T^3)^9/(1-q^3T^3)^4\), the curve has no points over \(\mathbb F_q\) or \(\mathbb F_{q^2}\), and all twelve lines and nine flexes become rational over \(\mathbb F_{q^3}\). In particular, every smooth plane cubic of characteristic \(>3\) has at least one flex over \(\mathbb F_{q^3}\), as inspection of the flex-orbit column also shows.

A concrete point-free example exists over \(\mathbb F_7\):

\[
C_0:\quad XY^2+Y^2Z-2YZ^2-X^2Z+XZ^2-2Z^3=0.
\]

It has six rational points as a smooth cubic, no rational flex, no rational Hesse line, and \(D_{C_0}(\mathbb F_7)=\varnothing\). Two other cubics over \(\mathbb F_7\),

\[
C_1:\ XY^2+YZ^2-X^2Z=0,\qquad
C_2:\ Y^2Z-X^3-XZ^2-3Z^3=0,
\]

have the **same** Hesse-line-union zeta function and each has \(21\) rational points on that union; nevertheless their numbers of rational quadruple points are \(0\) and \(3\). Thus the zeta function alone does not determine the arithmetic singularity stratification of this natural genus-\(55\) curve.

## Assumptions and scope

All statements concern the reduced scheme of the twelve inflection lines in characteristic \(p>3\). The original cubic is smooth, with an arbitrary degree-three plane embedding; a rational flex is not assumed. The field \(k\) may be any finite field of the stated characteristic, including those without a primitive cube root of unity. In the ten-row classification, a row is a group-theoretically possible affine Frobenius action subject to \(\det A\equiv q\pmod3\); the theorem does not assert that every row occurs over every small field.

Over an algebraic closure the curve has twelve projective-line components, nine ordinary quadruple points, and twelve ordinary double points. In the affine-plane labeling of flexes by \(V\), the twelve geometric lines are exactly the cosets of the four one-dimensional subspaces of \(V\). Distinct directions intersect at flexes, while the three lines in each direction meet pairwise at three further double points (the vertices of one Hesse triangle). Thus there are \(36\) branches above quadruple points and \(24\) above double points.

## Proof

**Geometric reduction.** The Hesse pencil of a smooth cubic gives its nine flexes, twelve inflection lines, and four triangular singular members [1, §2, pp. 3–6]. Any two lines of different affine directions meet at a flex, and the three parallel affine cosets of a direction form one projective triangle, whose three vertices are ordinary double points. The cited explicit equations and [1, Remark 3.1] give the classical intersection scheme. Independently, the exact determinant-norm census of all \(\binom{12}{3}=220\) line triples is \(0^{36},1^{28},3^{81},9^{72},27^3\); thus no previously nonconcurrent triple becomes concurrent in any characteristic \(>3\). The nine quadruple points contribute \(9\cdot\binom42=54\) pairs of intersecting lines; the twelve double points contribute another \(12\), exhausting \(\binom{12}2=66\). The arithmetic genus follows either from the degree-twelve plane curve formula or from \(9\cdot6+12-12+1=55\).

**Galois description.** Choosing a geometric flex identifies the nine flexes with the torsor under \(E[3]\cong V\), and choosing a rational point \(O\in C(k)\) identifies the plane embedding class with \(\xi\). A point \(R\) is a flex precisely when \(3(R-O)=\xi\). For a geometric solution \(Q\), Frobenius on \(Q+V\) is \(v\mapsto Av+b\), with \(b=\operatorname{Frob}(Q)-Q\). The Weil pairing gives \(\det A=q\bmod3\). Therefore every geometric line, intersection point, and branch is acted on by the same affine map.

**Finite configurations.** The set \(P\) is the nine vectors. The set \(L\) is the twelve three-point affine lines. The set \(F\) consists of the \(36\) pairs \((v,\ell)\) with \(v\in\ell\); these are branches over flex quadruple points. The \(12\) double vertices are equivariantly indexed by \(L\): in a parallel class of three lines, a vertex is determined by the omitted third line. The set \(B\) of \(24\) branches over these vertices is the set of ordered pairs of distinct parallel lines. All identifications respect the full affine action.

**Zeta calculation.** The normalization \(N\) of \(D_C\) is the disjoint union of the twelve geometric lines. The singular support is \(P\sqcup L\), with normalization preimage \(F\sqcup B\). For every positive integer \(n\), normalization is an isomorphism away from these finite schemes, so

\[
\#D_C(\mathbb F_{q^n})=(q^n+1)\#L^{g^n}-\#F^{g^n}-\#B^{g^n}+\#P^{g^n}+\#L^{g^n}.
\]

Here \(\#S^{g^n}=\sum_{d\mid n}d\,s_d\) for a finite Frobenius set with \(s_d\) cycles of length \(d\). Taking exponential generating functions gives the displayed zeta product. Exactly \(48\) matrices over \(\mathbb F_3\) are invertible; allowing nine translations produces \(432\) elements. The attached integer-only enumeration checks all of them, and the ten spectral templates account for respectively \(72,9,54,108,36,24,1,72,8,48\) transformations. The determinant-one and determinant-two contributions each total \(216\). Comparing zeta signatures shows that only templates 6 and 9 coincide, leaving nine distinct functions.

**Point-free criterion.** A rational smooth point of \(D_C\) lies on a unique geometric line, hence on a rational line. A rational quadruple point is a rational flex; a rational double vertex determines its omitted third line and hence also gives a rational line. Thus \(D_C(k)=\varnothing\) exactly when the affine action has neither a fixed vector nor a fixed affine line. If \(A-I\) is invertible, \(g\) has a fixed vector. If \(A=I\) with no fixed vector, the nonzero translation \(b\) fixes affine lines parallel to itself. If \(A\) has eigenvalues \(1,-1\), the quotient by its eigenline of eigenvalue \(1\) has affine action \(t\mapsto-t+c\), which has a fixed coset and therefore a fixed line. The only remaining possibility is a nonidentity unipotent \(A\). Its unique invariant direction is \(W=\ker(A-I)=\operatorname{im}(A-I)\), and the induced action on \(V/W\) is translation by \(b+W\). It has no invariant affine line exactly when \(b\notin W\), equivalently when \(\xi\notin3E(k)\). This proves necessity and sufficiency without reliance on the enumeration.

**Concrete realizations.** Over \(\mathbb F_7\), take \(E:y^2=x^3+x+3\), with \(\#E(\mathbb F_7)=6\), and \(P=(6,1)\), which has order three. The very ample system \(|2O+P|\) is represented by the functions \(1,x,(y+1)/(x-6)\). Eliminating \(y\) gives \(C_0\) as above. Since \(P\notin3E(\mathbb F_7)\), and the rational \(3\)-torsion has exactly three elements, the Weil pairing forces nontrivial unipotent Frobenius, so its Hesse union is point-free. The two other displayed cubics come, respectively, from \(E:y^2=x^3+2\), with full rational \(3\)-torsion and the nondivisible class \(P=(0,3)\), and the standard \(|3O|\) embedding of \(y^2=x^3+x+3\). Their signatures are types 9 and 6. A direct polynomial Hessian calculation over all \(57\) rational projective points and all \(57\) rational projective lines confirms the flex counts \(0,0,3\) and Hesse-line counts \(0,3,3\) for \(C_0,C_1,C_2\).

## Verification

Run `python3 verify_hesse.py` using Python 3; no packages are required. The script constructs all affine point/line actions, all flex and double branches, and all \(432\) exact permutations. It checks the ten cycle signatures, nine zeta signatures, determinant balance, and point-free orbit criterion. An independent Eisenstein-integer triple-determinant norm calculation excludes additional triple concurrence in all characteristics \(>3\). Separately, it constructs the twelve explicit split Hesse lines over \(\mathbb F_7\) and verifies the nine quadruple and twelve double intersections. A third independent routine builds Hessians by integer polynomial operations and evaluates all rational projective points and lines for the three displayed cubics, checking smoothness, rational cubic points, flexes, and Hesse lines. See `verify_output.txt`; the terminal line is `VERIFY_OK`.

## Relationship to prior work

Artebani and Dolgachev [1] give the Hesse pencil, explicit triangular line members, the affine-plane combinatorics, and the classical Hesse group. These are premises, not new claims here. Their inspected §§2–3 do not state the ten full arithmetic branch-orbit spectra, nine rational zeta functions, or the nondivisible-embedding point-free criterion and explicit realization. The earlier question [2] about a flex over a cubic field illustrates an adjacent arithmetic motivation; it is not used as a proof and does not cover the Hesse-line-union zeta classification. Standard normalization identities explain the formal zeta correction, but do not themselves supply the explicit affine action spectra or the rational empty-locus criterion.

## Limitations

This result excludes characteristics two and three, and treats only the reduced Hesse line union, not the potentially nonreduced singularity scheme or the ambient elliptic curve's zeta function. The ten templates are exhaustive for abstract affine Frobenius actions, not asserted individually realizable for every fixed \(q\). The geometric ingredients are classical, so implicit appearances of the computed arithmetic tables in older treatments remain a historical-priority risk. No independent mathematical validation is claimed.

## References

[1] M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590 (first public version 19 November 2006), especially §§2–3 and Remark 3.1; published in *L'Enseignement Mathématique* 55 (2009), 235–273, DOI:10.4171/LEM/55-3-3. https://arxiv.org/pdf/math/0611590

[2] D. Koshelev, *Does every nonsingular cubic curve over a finite field have a flex over the cubic extension?*, Mathematics Stack Exchange question and discussion, 18–20 March 2020. https://math.stackexchange.com/questions/3585175/
