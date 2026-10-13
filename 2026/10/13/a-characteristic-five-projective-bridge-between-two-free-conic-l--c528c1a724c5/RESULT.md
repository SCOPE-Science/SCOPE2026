# A characteristic-five projective bridge between two free conic–line arrangements

## Finding

Take the two rational conic–line arrangements called \(\mathcal{CL}_{10}\) and \(\mathcal{CL}_{4}\) in Pokora's 2023 classification. For the fixed primitive integral equations below, the **reduced geometric support** of \(\mathcal{CL}_{10}\) preserves seven distinct lines, one smooth conic, and its complete characteristic-zero component-incidence structure over the algebraic closure of \(\mathbb F_p\), for **every prime \(p\ge 7\)**. It has exactly twelve ordinary singular points, with \((n_2,n_3,n_4)=(5,4,3)\). Every one of the twelve points is \(\mathbb F_p\)-rational.

At the sole exceptional prime \(p=5\), two different pairs of labeled lines coalesce. The **reduced support** then consists of one smooth conic and five distinct lines, with exactly six ordinary \(\mathbb F_5\)-rational singularities, \((n_2,n_3,n_4)=(2,2,2)\). More strongly, this reduced support is projectively equivalent over \(\mathbb F_5\) to the reduction of the *different* arrangement \(\mathcal{CL}_4\) from the same classification. An explicit transformation establishes that equivalence, not merely equality of singularity counts.

These assertions classify every prime \(p\ge5\) for this fixed integral model. The product of all seven labeled line factors at \(p=5\) is **nonreduced**; all statements about six singularities or projective equivalence concern its reduced support, not the scheme defined by that nonreduced product.

## Assumptions and scope

Let \((X,Y,Z)\) be homogeneous coordinates and let the degree-two component of \(\mathcal{CL}_{10}\) be
\[
q_{10}=-4X^2+12Y^2-4YZ-5Z^2.
\]
Write the seven line forms, in order, as
\[
\begin{aligned}
\ell_0&=X,&\ell_1&=2X+2Y+Z,&\ell_2&=-2X+2Y+Z,\\
\ell_3&=-3X+4Y,&\ell_4&=3X+4Y,\\
\ell_5&=-4X+2Y+5Z,&\ell_6&=4X+2Y+5Z.
\end{aligned}
\]
For each prime \(p\ge5\), let \(D_{10,p}^{\mathrm{red}}\subset\mathbb P^2_{\overline{\mathbb F}_p}\) denote the union of the distinct geometric components of the reduction of \(q_{10}\prod_{i=0}^{6}\ell_i\).

For the comparison arrangement define
\[
q_4=U^2+V^2-W^2
\]
and its five lines by \(V=0\), \(-U+V-W=0\), \(U+V-W=0\), \(-U-V-W=0\), and \(U-V-W=0\). Their product with \(q_4\) is Pokora's \(\mathcal{CL}_4\), up to rational scalar multiples of individual factors.

An *ordinary multiplicity-\(m\) point* is one at which exactly \(m\) smooth local components have pairwise distinct tangent directions. All counts concern the geometric reduced support, not Tjurina scheme lengths or freeness in positive characteristic.

## Proof

**1. Smoothness and distinctness.** The symmetric integral matrix for \(q_{10}\) is
\[
B_{10}=\begin{pmatrix}-4&0&0\\0&12&-2\\0&-2&-5\end{pmatrix},\qquad\det B_{10}=256.
\]
Thus the conic is smooth for each \(p\ge5\). Taking each unordered triple of the seven line coefficient vectors, the complete set of \(\binom73=35\) determinants has five zeros; every one of the remaining thirty nonzero determinants has prime divisors only in \(\{2,3,5\}\). Since for each pair of lines there is a third with nonzero determinant, seven pairwise distinct lines survive at every \(p\ge7\), and a triple that was not concurrent cannot become concurrent there.

**2. Exact intersection support in characteristic zero.** The twelve projective points of the complete singular support, represented by primitive integral triples, are
\[
\begin{gathered}
(0,0,1),\ (0,1,-2),\ (0,5,-2),\ (0,5,6),\\
(4,-7,6),\ (4,-3,-2),\ (4,-3,14),\ (4,3,-14),\\
(4,3,2),\ (4,7,-6),\ (20,-15,22),\ (20,15,-22).
\end{gathered}
\]
For the seven lines take the respective integral kernel bases \((u_i,v_i)\):
\[
\begin{gathered}
((0,1,0),(0,0,1)),\ ((1,-1,0),(0,1,-2)),\ ((1,1,0),(0,1,-2)),\\
((4,3,0),(0,0,1)),\ ((4,-3,0),(0,0,1)),\\
((1,2,0),(0,-5,2)),\ ((1,-2,0),(0,-5,2)).
\end{gathered}
\]
For \(q_{10}(su_i+tv_i)=A_i s^2+B_i st+C_i t^2\), the seven discriminants \(B_i^2-4A_iC_i\) are exactly
\[
(256,1024,1024,1024,1024,9216,9216).
\]
They are nonzero squares supported on primes \(2,3\), so each line meets the conic in **two distinct rational points in every characteristic \(p\ge5\)**. Taking the twenty-one line-pair intersections and these fourteen conic-line intersections produces precisely the twelve triples listed above. Direct evaluation of all eight component equations at these points gives the multiplicity census \((5,4,3)\), where every conic--line intersection is transverse. The pair-count check \(5+3\cdot4+6\cdot3=35=\binom72+2\cdot7\) accounts for all component pairs.

**3. Uniform stability beyond five.** For each of the \(\binom{12}{2}=66\) unordered pairs of distinct primitive point representatives above, form their vector cross product and the gcd of its three integer coordinates. These 66 gcds lie in
\[
\{1,4,5,8,16,20,24,32,40,48\}.
\]
Consequently, no two of the twelve points coalesce modulo a prime \(p\ge7\). Every line intersection and both conic intersections per line are accounted for in this set, proving not just a finite-sample observation but the complete incidence-stability theorem for **all** primes \(p\ge7\). Transversality follows from the nonvanishing binary discriminants. The twelve displayed integral projective points reduce to \(\mathbb F_p\)-points for every such prime, proving their rationality.

**4. The exceptional characteristic.** At \(p=5\), lines \(\ell_3\) and \(\ell_5\) coincide projectively, as do \(\ell_4\) and \(\ell_6\). No other lines coincide. Direct exhaustive enumeration of the \(31\) points of \(\mathbb P^2(\mathbb F_5)\) gives exactly six singular-support points, namely
\[
\begin{array}{c|c}
\text{point}&\text{number of smooth branches}\\\hline
(0,0,1)&4\\
(0,1,3)&4\\
(1,2,3)&3\\
(1,3,2)&3\\
(1,2,4)&2\\
(1,3,1)&2
\end{array}
\]
(the order of the last four entries is immaterial). The five distinct reduced lines have ten intersections in total, and each meets the conic in two distinct \(\mathbb F_5\)-points. Therefore enumeration exhausts all geometric intersections even over \(\overline{\mathbb F}_5\); the weighted pair count is \(2+3\cdot2+6\cdot2=20=\binom52+2\cdot5\). The gradient of the conic is not proportional to any incident line at these six points, so every singularity is ordinary.

**5. A projective identification with \(\mathcal{CL}_4\).** In column coordinates define
\[
\begin{pmatrix}X\\Y\\Z\end{pmatrix}
=M\begin{pmatrix}U\\V\\W\end{pmatrix},\qquad
M=\begin{pmatrix}0&1&0\\3&0&2\\1&0&3\end{pmatrix}.
\]
The determinant is \(-7\equiv3\pmod5\), so the map belongs to \(\mathrm{PGL}_3(\mathbb F_5)\). The exact congruence \(M^{\mathsf T}B_{10}M\equiv\operatorname{diag}(1,1,-1)\pmod5\) gives \(q_{10}(M(U,V,W))=q_4(U,V,W)\) modulo five. In addition, the pullbacks \(M^{\mathsf T}\ell_i\) of the five distinct reduced \(\mathcal{CL}_{10}\) line covectors comprise **exactly** the five \(\mathcal{CL}_4\) line covectors up to units in \(\mathbb F_5\). Hence the whole reduced curves, rather than just their multiplicity profiles, are projectively equivalent.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. From the displayed integer coefficient vectors it recomputes the complete line-triple determinant support, derives the two conic intersections per line by exact integer square roots, recovers the twelve projective intersection points, confirms all sixty-six cross-content obstructions and the generic incidence multiplicities, and verifies the conic discriminants. It then enumerates the entire finite projective plane over \(\mathbb F_5\), tests transversality, and checks the projective transformation at all \(125\) coordinate triples. Run `python3 verify.py`; success prints a single line beginning `VERIFY_OK`. All universal prime assertions are deduced from exact integer factor support, not from finite-field sampling.

## Relationship to prior work

Pokora's 2023 preprint supplies the original \(\mathcal{CL}_{4}\) and \(\mathcal{CL}_{10}\) equations and their characteristic-zero freeness and weak combinatorics. The present finding neither reproves those free-arrangement classifications as new results nor assumes characteristic-zero freeness survives reduction. The new content is the universal arithmetic boundary at characteristic five, the complete reduced-support incidence classification on either side, and an explicit projective identification of the exceptional fiber with a separately constructed named arrangement. Related conic-line work on plus-one generation addresses different configurations and does not yield this specialization statement.

## Limitations

The analysis is specific to the stated primitive integral forms and primes at least five. It does not classify reductions in characteristics two or three, positive-characteristic freeness, the singular scheme or Tjurina number of the nonreduced characteristic-five product, or the lifting/moduli behavior of all arrangements having these weak incidence counts. Published or unpublished modular calculations omitted from accessible searches could still provide overlapping prior coverage; the projective equivalence was checked explicitly, not assumed from the shared multiplicity profile.

## References

1. P. Pokora, *Freeness of arrangements of lines and one conic with ordinary quasi-homogeneous singularities*, arXiv:2312.13052v1 (publicly posted 20 December 2023); original examples \(\mathcal{CL}_4\) and \(\mathcal{CL}_{10}\). https://arxiv.org/abs/2312.13052
2. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228 (2023). https://arxiv.org/abs/2309.15228
