# Two marked cells suffice for two-round orbit recovery in binary Latin three-nets

## Finding
Let \(V=\mathbb F_2^d\), where \(d\ge1\), and put \(X=V\times V\). Give \(X\) three **named, reflexive** equivalence relations
\[
E_0((x,y),(x',y'))\iff x=x',\quad
E_1((x,y),(x',y'))\iff y=y',\quad
E_2((x,y),(x',y'))\iff x+y=x'+y'.
\]
Thus \(X\) is the cell set of the Latin square for addition on \(V\), with the row, column, and symbol equivalences kept distinct. Individually colour any two distinct cells \(A,B\), and give all others one common colour. At each synchronous counting-refinement round, retain the old colour and count, for each of the three relations, every previous-colour class within the corresponding equivalence class (including the vertex itself).

Translate the two cells so that \(A=(0,0)\) and \(B=(u,v)\ne(0,0)\). Let \(H=\langle u,v\rangle_{\mathbb F_2}\), \(r=\dim H\in\{1,2\}\), and \(h=|H|=2^r\). Define the *partial coordinate profile* of \((x,y)\) by
\[
\kappa(x,y)=(\rho_H(x),\rho_H(y),\rho_H(x+y)),\qquad
\rho_H(z)=\begin{cases}z,&z\in H,\\ \bot,&z\notin H.\end{cases}
\]
**The stable counting-refinement classes are exactly the fibres of \(\kappa\), and they already appear by round two.** These fibres are exactly the orbits of the automorphism group fixing \(A\) and \(B\) individually.

The exact class census is: \(h^2\) singleton classes (both coordinates in \(H\)); when \(d>r\), another \(3h\) classes each of size \(2^d-h\); when \(d\ge r+2\), one final class of size \((2^d-h)(2^d-2h)\). Hence the total number of stable classes is
\[
N(d,r)=h^2+3h\,\mathbf1_{\{d>r\}}+\mathbf1_{\{d\ge r+2\}}.
\]
In particular the stable class counts are \(4,10,11\) for \(r=1\) at \(d=1,2,\ge3\), and \(16,28,29\) for \(r=2\) at \(d=2,3,\ge4\), respectively. The **exact first orbit-recovery round** is one if \(d=1\), or if \((d,r)=(2,1)\); it is two in all other permitted cases.

## Assumptions and scope
All vector spaces and operations are over the two-element field. The relation names are preserved by automorphisms; swapping row, column, and symbol names is not allowed. The two marked cells receive different singleton colours. No order or multiplication predicate on \(V\) is present. The assertion concerns automorphism-orbit recovery *inside this structure*, not identification among all finite relational structures or higher-variable canonization. For \(d=1\) the cell set has four elements; \(r=2\) requires \(d\ge2\).

## Proof
**1. Normalize and determine the stabilizer.** Independent coordinate translations send any chosen first cell to \((0,0)\), preserving all three relations. Because \(E_0\) and \(E_1\) are named, every automorphism is of the form \((x,y)\mapsto(f(x),g(y))\) with \(f,g\) bijections of \(V\). Preservation of \(E_2\) says that \(f(x)+g(y)\) depends only on \(x+y\). Taking \(y=0\) and \(x=0\) implies \(f(x)=\phi(x)+a\) and \(g(y)=\phi(y)+b\) for one additive bijection \(\phi\). Over \(\mathbb F_2\), \(\phi\in\mathrm{GL}(d,2)\). Fixing \((0,0)\) forces \(a=b=0\), and fixing \((u,v)\) forces \(\phi(u)=u\), \(\phi(v)=v\), hence \(\phi\) fixes \(H\) pointwise.

Two ordered pairs \((x,y)\) and \((x',y')\) are in the same orbit under this pointwise stabilizer exactly when their linear relations modulo \(H\) agree, including any values of linear combinations that lie in \(H\). There are only three possibilities: both \(x,y\in H\); exactly one of \(x,y,x+y\) lies in \(H\); or none lies in \(H\). The first case has \(h^2\) pointwise-fixed cells. In the second case the one coordinate combination in \(H\) can be any specific \(t\in H\), giving \(3h\) classes if the quotient \(V/H\) is nonzero. In the third case the two images of \(x,y\) in \(V/H\) are linearly independent, so it exists only if \(\dim(V/H)\ge2\); all such pairs form one orbit by extending a linear isomorphism between finite independent systems. This proves the \(\kappa\)-orbit characterization. It also gives the class sizes directly: \(1\), \(2^d-h\), and \((2^d-h)(2^d-2h)\), respectively.

**2. Round-one singleton witnesses.** The two marked cells remain singleton-coloured forever. If a cell is the unique intersection of an \(E_i\)-class through one marker and an \(E_j\)-class through the other marker with \(i\ne j\), it gets a singleton colour after one round: the two differently named relation-count signatures identify both defining constraints. The following lists give singleton witnesses whose three coordinate projections \(x,y,x+y\), separately, cover every value of \(H\).

If \(r=2\), so that \(u,v\) are independent, these eight cells suffice:
\[
(0,0),\ (u,v),\ (0,v),\ (0,u+v),\ (u,0),\ (u+v,0),\ (u,u),\ (v,v).
\]
The six nonmarked cells are intersections of differently directed marker equivalence classes. The displayed eight cells collectively realize all four values \(0,u,v,u+v\) as each of \(x\), \(y\), and \(x+y\).

If \(r=1\), precisely one of \(u=0\), \(v=0\), \(u=v\) holds. Relabelling the **proof's three coordinate roles** (not the structure's relation symbols), it is enough to inspect \((u,v)=(w,0)\) with \(w\ne0\). The four singleton witnesses are
\[
(0,0),\ (w,0),\ (0,w),\ (w,w).
\]
The two unmarked cells each lie at the intersection of a marker row and a differently directed marker symbol class. These four cells realize both values \(0,w\) in each of the three coordinate projections. The other two cases have the same witness property by the explicit coordinate interchanges \((x,y)\mapsto(y,x)\) and \((x,y)\mapsto(x,x+y)\), together with corresponding permutations of the three *proof roles*. These relabellings are used only to reduce the case analysis, not as automorphisms preserving the named signature.

**3. Round two reads the complete profile.** Fix a relation index \(i\in\{0,1,2\}\) and a value \(t\in H\). Step 2 supplies a cell \(w_{i,t}\) of its own round-one colour with \(i\)-th projection equal to \(t\). For any \(z\in X\), the number of \(E_i\)-related cells having that singleton colour is exactly one when the \(i\)-th projection of \(z\) equals \(t\), and zero otherwise. Because the relations are reflexive, this statement includes \(z=w_{i,t}\). Hence round two determines for each of \(x,y,x+y\) whether it belongs to \(H\), and its precise value if so. It therefore determines \(\kappa\). Conversely, automorphisms fixing both marker colours preserve every refinement round, so no two points in one \(\kappa\)-orbit can split. This proves equality at round two and at stabilization.

**4. Sharp depth.** A distinct pair of markers leaves more than one orbit at round zero, so zero rounds never suffice. When \(d=1\), the four cells are all singleton after one round. If \((d,r)=(2,1)\), the ten possible \(\kappa\)-profiles have distinct first-round relation signatures (inspect the two values of \(H\) and the single nonzero coset of \(V/H\)); thus round one suffices.

For \(r=2\) in every \(d\ge2\), the two cells \((v,u+v)\) and \((u+v,u)\) have different \(\kappa\)-profiles, but neither is on any of the six marker equivalence classes, so their round-one colours coincide. For \(r=1\), \(d\ge3\), normalize \(B=(w,0)\) and choose \(s,t\in V\) independent modulo \(H=\{0,w\}\). The cells \((s,w)\) and \((s,t)\) have different \(\kappa\)-profiles but are both unrelated to either marker in any of the three named relations; their first-round colours coincide. The other two \(r=1\) marker placements are symmetric under the coordinate-role interchanges above. Therefore two rounds are necessary in all remaining cases.

## Verification
The companion programs `support/verify_refinement.py` and `support/verify_stabilizers.py` are executable with Python 3 standard library only. The first constructs the entire binary Latin three-net and separately refines the three named equivalence relations for dimensions \(1\) through \(5\), testing 27 marker configurations and 8,172 vertex instances. It checks equality of the final partition with the predicted \(\kappa\)-fibres, class counts, and exact first recovery round. The second independently enumerates invertible binary linear maps for dimensions \(1\) through \(3\), calculates pointwise stabilizer orbits without using the refinement algorithm, and checks singleton-witness availability. It tests 15 marker configurations. Recorded outputs are provided in `support/refinement_output.txt` and `support/stabilizers_output.txt`. These finite checks corroborate but do not replace the proof for all dimensions.

## Relationship to prior work
The cell encoding and autotopism viewpoint are standard for Latin squares (Stones–Vojtěchovský–Wanless, 2012). Two-variable counting logic with equivalence predicates is an established setting (Pratt-Hartmann, 2015). Kiefer–Schweitzer–Selman (2015) characterize a different, global notion: a structure identified up to isomorphism among all structures by counting logic; neither their identification theorem nor their orbit consequences imply the present statement about two individually marked cells in a family that is not being claimed identifiable. Scheidt–Schweikardt (2025) characterize a general relational refinement procedure, without this orbit-counting theorem. The specific contribution here is that two individualizations yield exact stabilizer orbits of the binary addition-table three-net in at most two counting rounds, with sharp round thresholds and orbit-size formulas.

## Limitations
No assertion is made for nonbinary fields, non-elementary-abelian groups, unnamed/merged relations, or the ordinary uncoloured Latin-square graph. The result does not establish a graph-isomorphism/canonization bound on arbitrary input structures. The literature checks available here do not rule out an earlier specialized presentation of the same theorem, or a direct deduction from a previously tabulated coherent configuration. Independent audit has not been performed.

## References
- D. S. Stones, P. Vojtěchovský, and I. M. Wanless, *Cycle structure of autotopisms of quasigroups and Latin squares*, Journal of Combinatorial Designs 20 (2012), 227–263. DOI: 10.1002/jcd.20309; arXiv:1509.05655 (later available preprint).
- I. Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, Mathematical Logic Quarterly 61 (2015), 474–515. DOI: 10.1002/malq.201400102.
- S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, MFCS 2015, 319–330. arXiv:1503.08792; DOI: 10.1007/978-3-662-48057-1_25.
- B. Scheidt and N. Schweikardt, *Color Refinement for Relational Structures*, MFCS 2025, article 88. DOI: 10.4230/LIPIcs.MFCS.2025.88.
