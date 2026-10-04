# Hard Lefschetz rigidity for \(\mathbb P(1^r,a,b)\)
## Finding
For every integer \(r\ge2\) and integers \(1\le a\le b\), let
\[
\mathcal X_{r,a,b}=\mathbb P(1^r,a,b)=[(\mathbb A^{r+2}\setminus\{0\})/\mathbb G_m]
\]
be the smooth weighted projective stack with weights \(1,\ldots,1,a,b\). Then the Fernandez Hard Lefschetz age-symmetry condition
\[
\operatorname{age}(F)=\operatorname{age}(I(F))
\]
for every inertia component \(F\) holds if and only if
\[
(a,b)\in\{(1,1),(1,2),(2,2)\}.
\]
Thus in this infinite family, once the complex dimension is at least three, orbifold Hard Lefschetz is completely rigid: no stabilizer of order greater than two can occur.

## Assumptions and scope
The base field is \(\mathbb C\), and \(r\ge2\), so \(\dim_{\mathbb C}\mathcal X_{r,a,b}=r+1\ge3\). The statement concerns the smooth Deligne--Mumford weighted projective stack, not only its coarse moduli space. The Hard Lefschetz condition is the age symmetry introduced by Fernandez: the involution \(I\) on the inertia stack sends a sector represented by an isotropy element \(\lambda\) to the sector represented by \(\lambda^{-1}\), and the required equality is sectorwise equality of the corresponding ages.

For a nontrivial isotropy element \(\lambda=e^{2\pi i\theta}\), with \(0<\theta<1\), the quotient presentation gives
\[
\operatorname{age}(\lambda)=r\theta+\{a\theta\}+\{b\theta\},
\]
where \(\{\cdot\}\) denotes fractional part. This is the specialization of the standard weighted-projective twisted-sector degree-shifting calculation: the \(r\) unit-weight coordinates contribute \(r\theta\), a heavy coordinate contributes its fractional weight unless it is fixed, and the quotient direction has trivial isotropy action and contributes zero.

## Proof
Jiang's degree-shifting identity gives
\[
\operatorname{age}(\lambda)+\operatorname{age}(\lambda^{-1})=
\operatorname{codim}_{\mathbb C}(\mathcal X^{\lambda}).
\]
Hence the Hard Lefschetz condition is equivalent to saying that every nontrivial sector has age one half of its complex codimension.

First suppose \(a=b\). If \(a=b=1\), there are no nontrivial sectors. If \(a=b>1\), take the primitive \(b\)-th root \(\lambda=e^{2\pi i/b}\). It fixes the two heavy coordinates and no unit-weight coordinate, so its sector has codimension \(r\), while
\[
\operatorname{age}(\lambda)=\frac r b,
\qquad
\operatorname{age}(\lambda^{-1})=\frac{r(b-1)}b.
\]
Equality holds exactly when \(b=2\). Thus the equal-weight cases are precisely \((1,1)\) and \((2,2)\).

Now suppose \(a<b\). Take again the primitive \(b\)-th root \(\lambda=e^{2\pi i/b}\). Because \(0<a<b\), only the coordinate of weight \(b\) is fixed among the two heavy coordinates, so this twisted sector is a point and has codimension \(r+1\). Its age is
\[
\operatorname{age}(\lambda)=\frac{r+a}{b}.
\]
Age symmetry therefore forces
\[
2(r+a)=b(r+1).
\]
If \(a\ge2\), then
\[
b-a=\frac{2r-a(r-1)}{r+1}\le\frac2{r+1}<1.
\]
But \(b-a\) is a positive integer, a contradiction. Hence \(a=1\), and the displayed equation immediately gives \(b=2\). Therefore the only unequal solution is \((1,2)\).

Conversely, \((1,1)\) has no nontrivial isotropy. For \((1,2)\), the only nontrivial isotropy element is \(-1\); its fixed sector has codimension \(r+1\) and age \((r+1)/2\). For \((2,2)\), the only nontrivial isotropy element is again \(-1\); its fixed sector has codimension \(r\) and age \(r/2\). In both cases the age equals half the codimension, so the Hard Lefschetz condition holds.

## Verification
The standalone script `artifacts/verify_hard_lefschetz.py` evaluates every nontrivial inertia element using exact integer arithmetic. It exhaustively checks all triples with \(2\le r\le80\) and \(1\le a\le b\le80\), finding exactly the three predicted weight pairs for every \(r\). It separately checks the primitive-root obstruction for equal heavy weights and the Diophantine equation forced by the primitive largest-weight sector over much larger finite ranges. Running the script prints `VERIFY_OK`.

The finite computation is a regression check only. The infinite classification is proved by the primitive-sector argument above.

## Relationship to prior work
Jiang computed the twisted sectors and degree-shifting numbers for arbitrary weighted projective spaces, providing the general local input used here. Fernandez proved that orbifold Hard Lefschetz is equivalent to invariance of age under inversion of inertia sectors and explicitly remarked that it would be interesting to understand how common this condition is. Coates--Iritani--Tseng later highlighted the contrast between \(\mathbb P(1,1,2)\), which satisfies Hard Lefschetz, and \(\mathbb P(1,1,1,3)\), which does not.

The present result gives a closed classification for the natural infinite two-heavy family \(\mathbb P(1^r,a,b)\) in all complex dimensions at least three. The inspected sources give the general decision mechanism and isolated examples, but not this family-level classification.

## Limitations
The theorem is restricted to the two-heavy weight pattern and to \(r\ge2\). The dimension-two case \(r=1\) behaves differently and is intentionally excluded. No claim is made about arbitrary weighted projective stacks with three or more non-unit weights, nor about stronger variants of Hard Lefschetz used for partial resolutions or general \(K\)-equivalences.

## References
1. Yunfeng Jiang, *The Chen-Ruan Cohomology of Weighted Projective Spaces*, arXiv:math/0304140, first posted 10 April 2003.
2. Javier Fernandez, *Hodge structures for orbifold cohomology*, arXiv:math/0311026, first posted 3 November 2003; Proc. Amer. Math. Soc. 134 (2006), 2511--2520.
3. Tom Coates, Hiroshi Iritani, Hsian-Hua Tseng, *Wall-Crossings in Toric Gromov--Witten Theory I: Crepant Examples*, arXiv:math/0611550; Geometry & Topology 13 (2009), 2675--2744.
