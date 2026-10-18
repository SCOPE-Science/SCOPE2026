# Degree-one generation of the rational cohomology of the 27-line complement on the Fermat cubic

## Finding
Let \(S\subset\mathbb P^3_{\mathbb C}\) be the smooth Fermat cubic surface
\[
S:\quad X_0^3+X_1^3+X_2^3+X_3^3=0,
\]
let \(D\) be the reduced union of its \(27\) lines, and put \(U=S\setminus D\). The singular cohomology algebra \(H^*(U;\mathbb Q)\) is **generated in degree one**: the map
\[
\bigwedge{}^2 H^1(U;\mathbb Q)\ \xrightarrow{\ \smile\ }\ H^2(U;\mathbb Q)
\]
is surjective. More precisely,
\[
H^0(U;\mathbb Q)=\mathbb Q,\qquad
H^1(U;\mathbb Q)=\mathbb Q(-1)^{20},\qquad
H^2(U;\mathbb Q)=\mathbb Q(-2)^{91},
\]
and all higher cohomology vanishes. Here \(\mathbb Q(-k)\) denotes the pure Tate Hodge structure of weight \(2k\). Integrally, \(H_i(U;\mathbb Z)\) is torsion-free, with ranks \(1,20,91\) in degrees \(0,1,2\), and is zero otherwise. Thus \(\chi(U)=72\).

The multiplication assertion does not follow merely from the Betti numbers or from the known \(109\)-dimensional space of logarithmic top forms for a general cubic surface: the Fermat surface has eighteen concurrent triples of lines, and the boundary must first be resolved.

## Assumptions and scope
All varieties and cohomology groups are over \(\mathbb C\) unless specified. Cohomology means ordinary singular cohomology of the complex analytic open surface, with rational or integral coefficients as indicated. The assertion is about **the Fermat cubic**, not every smooth cubic surface. It involves no claim about the fundamental group or integral cup-product surjectivity.

Write \(\mathscr R=\{a\in\mathbb C:a^3=-1\}\). The lines have the three coordinate-pairing forms
\[
X_i=aX_j,\quad X_k=bX_\ell,\qquad a,b\in\mathscr R,
\]
for the three partitions \(\{i,j\}\sqcup\{k,\ell\}=\{0,1,2,3\}\). These give \(27\) distinct lines.

## Proof
**1. The boundary incidence and its simple-normal-crossing resolution.** Within each of the three nine-line pairing blocks, three lines with the same first parameter (or the same second parameter) meet at one point where the other coordinate pair vanishes. There are six such triple points per block. Distinct pairing blocks have precisely \(27\) pairwise line intersections per unordered pair of blocks: in a representative comparison the equations reduce to \(ad=cb\), where all four parameters have cube \(-1\), and there are three choices for \((c,d)\) per given \((a,b)\). These cross-block intersection points have all four projective coordinates nonzero, and cannot lie on a line from the third pairing block: this would force a product of two cube roots of \(-1\) to have cube \(-1\), whereas its cube is \(+1\). Hence they are ordinary double points. Altogether \(D\) has \(18\) distinct ordinary triple points and \(81\) distinct ordinary double points; no higher concurrence occurs. The \(27\) lines meet in \(135=81+3\cdot18\) unordered pairs.

Blow up the \(18\) triple points, obtaining \(\pi:\widetilde S\to S\) and the reduced total transform \(\widetilde D\). Its \(45\) rational components are the \(27\) strict transforms and \(18\) exceptional curves. It has precisely \(135=81+3\cdot18\) transverse nodes and no triple crossings. Its connected dual graph \(\Gamma\) therefore satisfies
\[
\dim H^1(\Gamma;\mathbb Q)=135-45+1=91.
\]
The complements \(\widetilde S\setminus\widetilde D\) and \(U\) are isomorphic.

**2. Cohomology groups and Hodge weights.** A smooth cubic surface is the blowup of \(\mathbb P^2\) at six points. Its \(27\) lines have classes \(E_i\) (six), \(F_{ij}=H-E_i-E_j\) (fifteen), and \(G_i=2H-\sum_{j\ne i}E_j\) (six). The six \(E_i\) together with \(F_{12}\) form an integral basis of \(\operatorname{Pic}(S)\) because \(H=F_{12}+E_1+E_2\). Thus the original line classes generate \(H^2(S;\mathbb Z)\) integrally. The \(45\) boundary component classes likewise span \(H^2(\widetilde S;\mathbb Q)\), including the new exceptional directions.

The residue/Gysin sequence for the complement gives \(H^1(U;\mathbb Q)\) as the kernel of the divisor-class map \(\mathbb Q^{27}(-1)\to H^2(S;\mathbb Q)\), hence \(\dim H^1(U)=27-7=20\) and its Hodge structure is pure of weight two. The weight spectral sequence for the simple-normal-crossing boundary \(\widetilde D\) gives weight-four \(H^2(U)\) as \(H^1(\Gamma;\mathbb Q)(-2)\). The weight-three term vanishes because the boundary components are projective lines, while the weight-two term vanishes because the boundary classes span \(H^2(\widetilde S)\). Thus \(H^2(U)=\mathbb Q(-2)^{91}\). No higher cohomology occurs: \(D\sim-9K_S\) is ample, so \(U\) is affine, and a smooth affine complex surface has the homotopy type of a real CW complex of dimension at most two.

For integral homology, the meridian presentation gives a surjection \(\mathbb Z^{27}\to H_1(U;\mathbb Z)\), whose relations are the intersection pairings with \(H^2(S;\mathbb Z)\). Since the line classes contain an integral unimodular basis, these relations form a primitive rank-seven sublattice; hence \(H_1(U;\mathbb Z)\cong\mathbb Z^{20}\). A two-dimensional CW complex has free \(H_2\); its rank is \(91\) from the rational calculation, proving the stated integral groups.

**3. Cup-product surjectivity by a finite exact certificate.** Let \(L_0,\dots,L_{26}\) be the six \(E_i\), fifteen \(F_{ij}\) in lexicographic order, and six \(G_i\). For a vector \(a=(a_i)\in\mathbb Q^{27}\), the condition \(\sum a_i[L_i]=0\) is a seven-equation integer system. An explicit integral basis of its twenty-dimensional kernel is obtained as follows: freely choose the fourteen \(F_{ij}\) coefficients except \(F_{12}\), and the six \(G_i\) coefficients. Set
\[
a_{F_{12}}=-\sum_{(i,j)\ne(1,2)}a_{F_{ij}}-2\sum_i a_{G_i},\qquad
a_{E_i}=\sum_{j\ne i}a_{F_{ij}}+\sum_{k\ne i}a_{G_k}.
\]
At a blown-up triple point where the incident original lines are indexed by \(\{i,j,k\}\), the meridian residue on the exceptional curve is \(a_i+a_j+a_k\). This extends each of the twenty basis vectors to residue vectors on all \(45\) components of \(\widetilde D\).

Orient the \(135\) edges of \(\Gamma\) by increasing vertex index. Let \(\delta\) be its integral \(135\)-by-\(45\) incidence matrix, and let \(W\) be the \(135\)-by-\(190\) integer matrix whose column for basis residues \(a,b\) has at an edge \(i\to j\) the value \(a_i b_j-a_j b_i\). These are exactly the double residues of the wedge products of logarithmic degree-one classes. The graph-cochain description identifies their cohomology classes with the columns of \(W\) modulo \(\operatorname{im}\delta\).

The accompanying **standard-library-only** program `verify_fermat_cubic.py` constructs the line incidence from their equations, reproduces the same crossing pattern over the good primes \(7\) and \(13\), and constructs these matrices from the displayed integral formulas. Exact Gaussian elimination in \(\mathbb F_{101}\) returns
\[
\operatorname{rank}_{101}(\delta)=44,\qquad
\operatorname{rank}_{101}[\delta\mid W]=135.
\]
Since \(135\) is the full number of rows, a nonzero full minor modulo \(101\) is also a nonzero integer minor. Therefore \([\delta\mid W]\) has rank \(135\) over \(\mathbb Q\), implying
\[
\dim\operatorname{im}\!\left(\bigwedge{}^2 H^1(U;\mathbb Q)\to H^2(U;\mathbb Q)\right)
=135-44=91.
\]
This is the dimension of the target; the multiplication map is surjective.

## Verification
Run `python3 verify_fermat_cubic.py`. The checker uses only Python's standard library, enumerates all \(27\) lines and their projective rational points over \(\mathbb F_7\) and \(\mathbb F_{13}\), and checks that the patterns agree. It then constructs an explicit \(20\)-vector integral residue basis from the cubic surface's Picard classes. Finally, it performs exact modular row reduction on the incidence matrix and on the incidence-plus-cup matrix. Its recorded output is:

```
PASS: 27 lines, 81 ordinary crossings, 18 Eckardt triple crossings, 135 meeting pairs (mod 7 and 13).
PASS: mod-101 rank([incidence^T | all 190 cup products])=135;
      rank(incidence^T)=44, hence cup-product image has rational dimension 91.
PASS: H^*(complement; Q) generated in degree one, Betti numbers 1,20,91; Euler 72.
```

The modular full-rank calculation is a rigorous exact certificate for a rational surjectivity statement because the matrices have integer entries and the target dimension is independently proved. The finite-field point incidences are supplementary checks of the explicit characteristic-zero pairing argument in the proof, not a substitute for that argument.

## Relationship to prior work
Sturmfels and Telen, *Positive Geometries from Cubic Surfaces* (first posted May 12, 2026), study the same \(27\)-line complement for general real cubic surfaces. In their Theorem 1.1 and Lemma 5.3 the space of logarithmic top forms has dimension \(109\) in the absence of triple intersections; Section 5 explicitly counts the connected \(27\)-vertex, \(135\)-edge boundary graph. The Fermat cubic is not in their general/no-Eckardt hypothesis. The present theorem calculates the exceptional \(45\)-vertex resolution's \(91\)-dimensional top cohomology and, more importantly, proves that its entire rational cohomology ring is generated by \(H^1\), a multiplication assertion not contained in those stated results.

Brown and Dupont, *Positive Geometries and Canonical Forms via Mixed Hodge Theory*, supply the broader mixed-Hodge and residue framework, but their general correspondence does not by itself give the Fermat cubic's explicit integral residue basis or rank-\(91\) cup-product certificate. Classical descriptions of the Fermat cubic's \(27\) lines and \(18\) Eckardt points supply the geometric configuration; neither such description alone nor the Schläfli intersection graph implies the multiplicative surjectivity. This comparison does not assert exhaustive coverage of unindexed literature.

## Limitations
The integral cohomology groups are determined, but **integral cup-product surjectivity** and the homotopy type are not claimed. No uniform cup-generation theorem is asserted for every cubic surface with an arbitrary number of Eckardt points. The mod-\(101\) rank proves full rank over \(\mathbb Q\), not the Smith normal form of the integral multiplication map. Equivalence to an unindexed treatment of arrangements on cubic surfaces remains a residual literature risk.

## References
1. B. Sturmfels and S. Telen, *Positive Geometries from Cubic Surfaces*, arXiv:2605.11909, originally posted 2026-05-12, specifically Theorem 1.1, Lemma 5.3, and Sections 3–6. https://arxiv.org/html/2605.11909v2
2. F. Brown and C. Dupont, *Positive Geometries and Canonical Forms via Mixed Hodge Theory*, Communications in Mathematical Physics **406** (2025), article 267; arXiv:2501.03202. https://arxiv.org/abs/2501.03202
3. Classical description of the \(27\) lines and Eckardt points on the Fermat cubic surface; see B. Segre, *The Non-Singular Cubic Surfaces*, Oxford University Press, 1942, and D. Huybrechts, *The Geometry of Cubic Hypersurfaces*, Section 4.3.
