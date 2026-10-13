# Singularity strata and the unique nearly-free member of an explicit four-conic family

## Finding
Consider the reduced degree-eight plane curve \(\mathcal A_t\subset\mathbb P^2_{\mathbb C}\) formed by four conics
\[
\begin{aligned}
q_0&=x^2+y^2-z^2,\\
q_1&=2x^2+y^2+2xz,\\
q_2&=x^2+y^2+2xz,\\
q_{3,t}&=4x^2+6y^2+4xz-tz^2,
\end{aligned}
\qquad f_t=q_0q_1q_2q_{3,t}.
\]
For all \(t\in\mathbb C\setminus\{-1\}\), all four conics are smooth and pairwise distinct. The complete singularity stratification of \(\mathcal A_t\) is

| Parameter | Complete singularity configuration | Global Tjurina information |
| --- | --- | --- |
| \(t\notin\{-1,0,2,7/2,8\}\) | \(2A_7+16A_1\) | \(\tau=30\) |
| \(t=0\) | two triple points with pairwise branch contacts \((4,2,2)\), plus \(8A_1\) | \(\mu=36,\ \tau<36\) |
| \(t=2\) | \(2A_7+2A_3+12A_1\) | \(\tau=32\) |
| \(t=7/2\) | \(2A_7+2D_4+10A_1\) | \(\tau=32\) |
| \(t=8\) | \(4A_7+8A_1\) | \(\tau=36\) |

**Among the smooth-four-conic members of this family, \(\mathcal A_t\) is nearly free if and only if \(t=8\).** The specialization \(t=8\) has minimal Jacobian-syzygy degree \(\operatorname{mdr}(f_8)=3\). In particular the fourth conic with the coefficient \(-9z^2\) printed in Pokora's Example 2.6 instead lies in the generic stratum \(2A_7+16A_1\); substituting \(-8z^2\) recovers the intended \(4A_7+8A_1\) nearly-free example. The paper's intended abstract singularity configuration is therefore prior, while the parameter stratification and uniqueness assertion are the refinement here.

## Assumptions and scope
All geometry is over \(\mathbb C\), and all singularity types denote analytic types of the **reduced union** of the four conics. A node is \(A_1\), an order-two tangency of smooth branches is \(A_3\), an order-four tangency is \(A_7\), and an ordinary transverse triple point is \(D_4\). At the two special triple germs for \(t=0\), the three smooth local branches have pairwise intersection multiplicities \(4,2,2\); this configuration is not assigned an ADE label. For \(t=-1\), the fourth conic is singular, and is outside the claimed smooth-conic domain.

The minimal degree \(\operatorname{mdr}(f_t)\) is the minimum degree of a nonzero homogeneous triple \((a,b,c)\) satisfying \(a(f_t)_x+b(f_t)_y+c(f_t)_z=0\). The global Tjurina number is the sum of the local Tjurina numbers. The nearly-free characterization used below is the standard Tjurina-number/syzygy characterization for reduced plane curves of degree eight, not a definition of near freeness by numerical coincidence alone.

## Proof
**1. Smoothness and fixed incidences.** The symmetric matrices of the four quadratics have determinants \(-1,-1,-1,-24(t+1)\), so precisely \(t=-1\) makes the fourth conic singular. The first two conics meet at \([-1:0:1]\) with multiplicity four; \(q_1\) and \(q_2\) meet at \([0:0:1]\) with multiplicity four. These yield two persistent \(A_7\) points. The pair \((q_0,q_2)\) has four transverse intersections: two on \(z=0\) and two with \(z=1\), \(x=-1/2\), \(y^2=3/4\).

**2. Exhaustive elimination for the moving conic.** On the affine chart \(z=1\), eliminate \(y\) between \(q_{3,t}\) and each of \(q_0,q_1,q_2\). Up to a nonzero constant, the exact resultants are
\[
\begin{aligned}
R_0^2&=(t+2x^2-4x-6)^2,\\
R_1^2&=(t+8x^2+8x)^2,\\
R_2^2&=(t+2x^2+8x)^2.
\end{aligned}
\]
The respective quadratic discriminants are \(8(8-t)\), \(32(2-t)\), and \(8(8-t)\). A multiple quadratic root creates a tangency: at \(t=2\), the \((q_1,q_{3,t})\)-pair has two order-two contacts; at \(t=8\), the \((q_0,q_{3,t})\)- and \((q_2,q_{3,t})\)-pairs each have an order-four contact on \(y=0\). The remaining collisions arise when the moving conic passes through a fixed pairwise intersection. Substitution gives exactly \(t=0\), at both persistent \(A_7\) points, and \(t=7/2\), at the two affine \((q_0,q_2)\)-nodes. At \(t=7/2\) the three local tangents are distinct, so the two triple points are \(D_4\). At \(t=0\), power-series expansions of the three smooth branches show pairwise contact orders \((4,2,2)\) at each triple point. A direct check on \(z=0\) excludes additional intersections with the moving conic there. These tests exhaust every pair among four smooth conics and show that no other exceptional parameter exists.

**3. Counting all remaining nodes.** Each of the six pairs of distinct conics has total intersection multiplicity four by Bézout, for a total of \(24\). At generic parameters the two persistent \(A_7\) points contribute four each and leave sixteen transverse nodes. At \(t=2\), two extra contacts contribute two each and leave twelve nodes; at \(t=8\), four contacts of multiplicity four leave eight nodes. At \(t=7/2\), each triple \(D_4\) contributes three pair-incidences and leaves ten nodes. At \(t=0\), each triple has pair-incidence sum \(4+2+2=8\), leaving eight nodes. The identified local contacts and the exhaustiveness of step 2 ensure these are distinct geometric points rather than just multiplicity totals.

**4. Tjurina numbers and near freeness.** The ADE fibers have local Tjurina numbers equal to their Milnor numbers: \(\tau(A_1)=1\), \(\tau(A_3)=3\), \(\tau(A_7)=7\), \(\tau(D_4)=4\). This gives the table values. At \(t=0\), each three-branch germ has \(\delta=8\), hence \(\mu=2\delta-3+1=14\). The contact pattern \((4,2,2)\) prevents weighted homogeneity: three reduced smooth branches of a weighted homogeneous germ cannot have two different positive pairwise contact orders. By the local Saito criterion each such germ has \(\tau<\mu\). Thus \(\tau(\mathcal A_0)<2(14)+8=36\).

For any nearly-free reduced octic the standard degree-eight numerical relation with minimal Jacobian degree \(r\) is \(\tau=48-r(7-r)\), where \(1\leq r\leq4\); in particular \(\tau\geq36\). Consequently every fiber except possibly \(t=8\) is excluded. For \(t=8\), put
\[
\begin{aligned}
a&=-(x^3-x^2z+xy^2-3xz^2-y^2z),\\
b&=0,\\
c&=(2x+z)(x^2+xz+y^2-z^2).
\end{aligned}
\]
Exact polynomial expansion gives \(a(f_8)_x+c(f_8)_z=0\). The degree-one and degree-two Jacobian syzygy coefficient matrices have full column rank after reduction modulo the prime \(1000003\); hence they have full rank over \(\mathbb Q\), and also over \(\mathbb C\). A degree-zero syzygy would yield a degree-one syzygy by multiplication, so \(\operatorname{mdr}(f_8)=3\). Together with \(\tau=36=48-3(7-3)\), the numerical characterization proves that \(\mathcal A_8\) is nearly free.

## Verification
The standalone `verify.py` uses SymPy and exact rational and finite-field arithmetic. It checks conic determinants, all six pairwise elimination resultants, moving-conic discriminants, the special triple points and their branch-contact orders, the cubic Jacobian syzygy, and injectivity of the degree-one and degree-two syzygy maps modulo \(1000003\). Its asserted pair-incidence totals are \(24\) for each stratum. Run `python verify.py` with SymPy version \(1.12\) or newer. Algebraic computation supports the proof; the exhaustive algebraic classification and the local analytic arguments above explain why sampled computations alone are insufficient.

## Relationship to prior work
Pokora, Example 2.6, supplies the four-conic construction, displays the coefficient \(-9z^2\) and asserts a nearly-free configuration with four \(A_7\) points and eight nodes. That asserted abstract configuration and the general numerical near-free criterion are prior work. The new information is that the displayed member is instead generic, the coefficient restoring the intended example is precisely \(-8z^2\), and the complete deformation stratification identifies **all** exceptional fibers and the unique nearly-free one. General conic-arrangement constraints in Zieliński's related work do not give this family-specific stratification. These distinctions are about mathematical statements and implications, not merely differences of wording.

## Limitations
The result concerns only the displayed one-parameter family and only its four-smooth-conic locus; it does not classify all degree-eight conic arrangements or characterize arbitrary deformations. No independent audit has been performed. Potential independent or unindexed corrections to the printed example have not been ruled out by bibliographic searching.

## References
1. Piotr Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, arXiv:2303.08584 (first public 2023-03-15), Example 2.6; *Annali dell'Università di Ferrara* 70 (2024), 593–606, doi:10.1007/s11565-023-00481-6.
2. Alexandru Dimca, *Freeness versus maximal global Tjurina number for plane curves*, arXiv:1508.04954; *Math. Proc. Cambridge Philos. Soc.* 163 (2017), 161–172.
3. Marcin Zieliński, *On plane conic arrangements with A5 and A7 singularities*, *Rend. Circ. Mat. Palermo* (2) 73 (2024), 57–63, doi:10.1007/s12215-023-00890-8.
