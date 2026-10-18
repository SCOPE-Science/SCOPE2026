# Rational Eckardt-contact splitting spectrum on smooth binary cubic surfaces

## Finding

Let \(S\subset\mathbf P^3_{\mathbf F_2}\) range over **geometrically smooth** cubic hypersurfaces. A rational Eckardt point is a point \(P\in S(\mathbf F_2)\) through which pass three distinct **geometric** lines contained in \(S\); the lines need not be individually rational. Put \(N(S)=\#S(\mathbf F_2)\) and \(e(S)=\#\{\text{rational Eckardt points}\}\). Then the exact set of possible rational Eckardt numbers is

\[
\{0,1,2,3,4,7,15\}.
\]

The complete weighted distribution is \(189952,115920,10080,2800,3360,420,28\), respectively. It has 17 nonempty \((N,e)\)-strata, given below. In the finite coefficient space of \(2^{20}-1=1048575\) nonzero homogeneous cubics, exactly \(322560\) define smooth surfaces, comprising 36 projective classes under \(\operatorname{PGL}_4(\mathbf F_2)\). These ambient counts are included as enumeration consistency checks, **not** presented as the novel part of the classification.

The **contact-field refinement** has exactly 21 nonempty strata. At a rational Eckardt point, the three lines are either one degree-three Frobenius orbit, one rational line and one quadratic conjugate pair, or three rational lines. Denote the respective numbers by \(e_3,e_{1+2},e_{1+1+1}\), so \(e=e_3+e_{1+2}+e_{1+1+1}\). In particular, there are precisely 28 smooth equations with \((N,e)=(15,15)\), constituting one projective orbit, and precisely 420 with \((N,e)=(7,7)\), also one orbit. In the latter orbit, the contact types are \((e_3,e_{1+2},e_{1+1+1})=(1,6,0)\), whereas all 15 rational Eckardt points of the former have three rational lines.

The complete rational-point/Eckardt-count distribution is:

| \(N\) | \(e\) | Defining equations | Projective classes |
|---:|---:|---:|---:|
| 1 | 1 | 840 | 1 |
| 3 | 1 | 10,080 | 1 |
| 3 | 3 | 1,540 | 2 |
| 5 | 0 | 44,352 | 3 |
| 5 | 1 | 35,280 | 4 |
| 5 | 2 | 5,040 | 1 |
| 7 | 0 | 80,640 | 4 |
| 7 | 1 | 48,720 | 6 |
| 7 | 7 | 420 | 1 |
| 9 | 0 | 64,960 | 5 |
| 9 | 1 | 10,920 | 2 |
| 9 | 2 | 5,040 | 1 |
| 9 | 4 | 1,680 | 1 |
| 11 | 1 | 10,080 | 1 |
| 11 | 3 | 1,260 | 1 |
| 13 | 4 | 1,680 | 1 |
| 15 | 15 | 28 | 1 |

The further decomposition by Frobenius splitting of each rational tritangent section is:

| \(N\) | \(e\) | \(e_3\) | \(e_{1+2}\) | \(e_{1+1+1}\) | Equations | Classes |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 | 840 | 1 |
| 3 | 1 | 1 | 0 | 0 | 10,080 | 1 |
| 3 | 3 | 0 | 3 | 0 | 420 | 1 |
| 3 | 3 | 3 | 0 | 0 | 1,120 | 1 |
| 5 | 0 | 0 | 0 | 0 | 44,352 | 3 |
| 5 | 1 | 0 | 1 | 0 | 10,080 | 1 |
| 5 | 1 | 1 | 0 | 0 | 25,200 | 3 |
| 5 | 2 | 0 | 2 | 0 | 5,040 | 1 |
| 7 | 0 | 0 | 0 | 0 | 80,640 | 4 |
| 7 | 1 | 0 | 1 | 0 | 35,280 | 4 |
| 7 | 1 | 1 | 0 | 0 | 13,440 | 2 |
| 7 | 7 | 0 | 6 | 1 | 420 | 1 |
| 9 | 0 | 0 | 0 | 0 | 64,960 | 5 |
| 9 | 1 | 0 | 1 | 0 | 10,080 | 1 |
| 9 | 1 | 1 | 0 | 0 | 840 | 1 |
| 9 | 2 | 0 | 1 | 1 | 5,040 | 1 |
| 9 | 4 | 0 | 3 | 1 | 1,680 | 1 |
| 11 | 1 | 0 | 0 | 1 | 10,080 | 1 |
| 11 | 3 | 0 | 1 | 2 | 1,260 | 1 |
| 13 | 4 | 0 | 0 | 4 | 1,680 | 1 |
| 15 | 15 | 0 | 0 | 15 | 28 | 1 |

## Assumptions and scope

All arithmetic is over \(\mathbf F_2\), and geometric smoothness and geometric line components are evaluated after base change to an algebraic closure. A defining equation is a nonzero homogeneous polynomial of degree three in four variables; in characteristic two its scalar-projective normalization is unique. Projective equivalence means change of coordinates by the entire \(\operatorname{PGL}_4(\mathbf F_2)=\operatorname{GL}_4(\mathbf F_2)\). Counts of equations and counts of projective classes are not counts of abstract varieties up to arbitrary field-isomorphism. At a rational Eckardt point, contact-type labels are Frobenius orbit lengths of the three **distinct** geometric lines, not rational points of those lines.

The claim is the joint arithmetic/contact classification. Known facts about cubic-surface point counts, the geometric 27-line arrangement, and the extremal space-filling cubic serve as context and checks; no general \(\mathbf F_{2^m}\) distribution is asserted.

## Proof

**Complete coefficient-space reduction.** Order the twenty degree-three monomials by ascending exponents \((a,b,c,d)\), with the last exponent determined by \(a+b+c+d=3\), as implemented in `code/cubic_orbits.cpp`. Every nonzero 20-bit coefficient mask represents one cubic. The twelve elementary transvections \(x_i\mapsto x_i+x_j\) for \(i\ne j\) generate \(\operatorname{GL}_4(\mathbf F_2)\). Breadth-first closure visits each mask and gives 141 projective orbits among all 1,048,575 equations. Their orbit sizes sum to 1,048,575; an independent Burnside computation across all 20,160 matrices gives the same 141 nonzero orbits (142 if zero is included).

**Geometric smoothness.** For each orbit representative \(F\), Euler's identity in characteristic two is \(F=\sum_i x_i\,\partial_iF\). Hence projective singularities are exactly the nonzero common zeros of the four quadratic partial derivatives. On each of the four affine charts \(x_i=1\), a Gröbner-basis calculation over \(\mathbf F_2\) checks whether their ideal is the unit ideal. By the algebraic-closure Nullstellensatz, the four unit-ideal conditions are equivalent to geometric smoothness. Exactly 36 orbits pass; their sizes sum to 322,560 equations. The procedure does not rely on a finite-extension cutoff.

**Eckardt criterion and line descent.** For a rational smooth point \(P\), put \(H=T_PS\). Choose rational vectors \(U,V\) for which \(P,U,V\) span \(H\). Since \(F(P)=0\) and \(P\) is tangent, the restricted cubic has the exact shape

\[
F(sP+tU+vV)=s\,Q_2(t,v)+C_3(t,v),
\quad C_3=a t^3+b t^2v+c tv^2+d v^3.
\]

There are three distinct geometric lines through \(P\) on the tangent-plane section if and only if \(Q_2=0\) identically and \(C_3\) is squarefree as a binary cubic. In characteristic two its discriminant is \((ad+bc)^2\), so the exact test is \(ad+bc=1\). When it passes, the number of distinct \(\mathbf F_2\)-roots of \(C_3\) in \(\mathbf P^1(\mathbf F_2)\) is 0, 1, or 3, yielding Frobenius types \(3\), \(1+2\), and \(1+1+1\), respectively. Every rational point of every smooth orbit representative is tested. The computed orbit sizes, point counts, and contact types give the two tables above and the 36-line class table in `data/smooth_orbits.csv`.

**The all-rational extremum.** Any cubic vanishing at all 15 points of \(\mathbf P^3(\mathbf F_2)\) has the unique form

\[
F_B=\sum_{0\le i<j\le3} b_{ij}(x_i^2x_j+x_ix_j^2),
\qquad b_{ij}\in\mathbf F_2.
\]

Indeed evaluation on each coordinate point kills all pure cubes, and evaluation on each sum of two basis vectors forces the two cross-coefficients to agree. Write \(B\) for the alternating matrix \((b_{ij})\). The gradient is \(B\,x^{[2]}\), so \(F_B\) is geometrically smooth exactly when \(B\) is nonsingular. There are \(|\operatorname{GL}_4(\mathbf F_2)|/|\operatorname{Sp}_4(\mathbf F_2)|=20160/720=28\) such forms, constituting one projective orbit. For each rational \(P\), the tangent plane is its symplectic orthogonal \(P^\perp\), and the restriction factors into three **distinct rational** lines through \(P\), because the induced alternating form on \(P^\perp/\langle P\rangle\) is nondegenerate. Thus every rational point is Eckardt. A representative is

\[
x_0^2x_3+x_0x_3^2+x_1^2x_2+x_1x_2^2=0.
\]

The 7-Eckardt orbit has representative obtained by adding \(x_3^3\) to that equation. Its 420 equations, 7 rational points, and contact splitting \((1,6,0)\) are independently confirmed by symbolic substitution.

## Verification

The exact public artifacts are `code/cubic_orbits.cpp`, `code/burnside.cpp`, `code/smooth_check.py`, `code/independent_contacts.py`, `code/independent_lines.py`, `code/reproduce.py`, and the paired `data/` output files. Execute `python3 code/reproduce.py` from the extracted package root (requires C++17 compiler and Python 3 with SymPy). This compiles both C++ calculations, checks the 141-orbit list byte-for-byte, checks the Burnside fixed-space sum, reruns all four affine Gröbner checks for all 141 orbit representatives, recomputes rational Eckardt points by an independently written symbolic tangent-section procedure, and tests the number of three-rational-line Eckardt points directly by polynomial line containment. It compares the regenerated tables against stored expected datasets. Exact reproduction succeeded on the package source paths before packaging.

The independent Burnside calculation obtains the fixed-point sum 2,862,720 over the 20,160 matrices, hence 142 orbits including the zero polynomial. The rational-line incidence check covers all 258 rational points among the 36 smooth orbit representatives; the three-rational-line counts agree exactly. The 21 joint contact strata and 17 coarse strata sum to 322,560 equations and 36 classes. The expected smooth-representative records and contact records are fully included. All contact and smoothness decisions are exact finite algebra, not extrapolations from bounded extensions.

## Relationship to prior work

Dolgachev and Duncan (2017) classify geometric Eckardt collections and automorphisms of smooth cubic surfaces in positive characteristic, including the characteristic-two exceptional forms. Their geometric lists do not specify the weighted arithmetic distribution of rational Eckardt points or of Frobenius splitting types across binary cubic equations. Kadyrsizova et al. (2020) characterize the Frobenius splitting of characteristic-two cubic surfaces and triangle-free tritangent arrangements, again without this rational-point/contact joint distribution. Das (2020) computes finite-field Frobenius classes on the 27 lines, rational-point counts, and the counts of Frobenius-stable tritangent trios. A Frobenius-stable tritangent trio need not consist of concurrent lines: incidence convergence into an Eckardt point is additional geometry not implied by the line permutation class alone. Betten's 2018 finite-field classification concerns cubic surfaces **with all 27 lines rational**; its \(q=2\) row contains no cases and cannot tabulate the present objects. These broader results are acknowledged; ambient smooth-curve counts, known geometric Eckardt restrictions and the symplectic extremal example are **not** claims of priority here.

In particular, the same rational-point count \(N=9\) occurs with four rational Eckardt counts \(e=0,1,2,4\), which demonstrates that the rational-point marginal alone does not imply the accepted refinement. The full 21-stratum contact-field distribution is the specific contribution.

## Limitations

The projective classification is only over \(\mathbf F_2\), with no assertion of uniformity over larger fields. While the finite computation and a separate symplectic extremal argument establish the stated numerical claims, no independent external expert audit has been performed. A previously unindexed finite-geometry catalogue or unpublished computation could contain an equivalent joint contact table; this remains a priority risk. Frobenius permutations on 27 lines and published geometric Eckardt classifications were compared as stronger potential antecedents; none of the inspected passages gives the full 21-stratum joint distribution. No statement about arbitrary abstract field-isomorphism classes is intended.

## References

- I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167, first public version 2017-12-04; especially §§1.2, 5 and 13, Table 5. https://arxiv.org/abs/1712.01167
- Z. Kadyrsizova, J. Kenkel, J. Page, J. Singh, K. E. Smith, A. Vraciu and E. E. Witt, *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018, 2020-07-23; especially §5. https://arxiv.org/abs/2007.12018
- R. Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183, 2020-02-25; especially Theorem 1.1 and Tables 1–3. https://arxiv.org/abs/2002.11183
- A. Betten, *Classifying Cubic Surfaces over Finite Fields Using Orbiter*, ICMS 2018, DOI:10.1007/978-3-319-96418-8_7, especially Table 1 and pp. 58–61. https://doi.org/10.1007/978-3-319-96418-8_7
