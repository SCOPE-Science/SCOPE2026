# Integral incidence degeneration of the Cefalù Kummer configuration

## Finding

Put \(F=\sum_{0\le i<j\le3}X_i^2X_j^2-\sum_{i=0}^3X_i^4\in\mathbb Z[X_0,X_1,X_2,X_3]\), and let \(\mathscr X=V(F)\subset\mathbb P^3_{\mathbb Z}\). This is the primitive integral equation of Catanese's Cefalù quartic. For each \(i\in\{0,1,2,3\}\), define the closed subscheme \(N_i\) of \(\mathbb P^3_{\mathbb Z}\) by
\[
X_i=0,\qquad X_j^2=X_k^2\quad(j,k\ne i).
\]
Let \(N=\coprod_iN_i\), and let \(T=\coprod_iT_i\subset(\mathbb P^3_{\mathbb Z})^\vee\) be the identically defined scheme of marked polar hyperplanes in dual coordinates. Define \(I\subset N\times_{\mathbb Z}T\) by the universal incidence equation \(\sum_{i=0}^3X_iY_i=0\). Write \(\mu_2=\operatorname{Spec}\mathbb Z[z]/(z^2-1)\).

**Theorem.** The schemes \(N\) and \(T\) are finite flat of degree \(16\) over \(\mathbb Z\), each a disjoint union of four copies of \(\mu_2^2\). The incidence scheme has the following complete decomposition (each isomorphism is noncanonical):
\[
\boxed{I\ \simeq\ \coprod_{i\ne j}\mu_{2,\mathbb Z}^3\ \coprod\ \coprod_{i=0}^3\mu_{2,\mathbb F_3}^2.}
\]
The twelve terms with \(i\ne j\) are finite flat of degree \(8\) over \(\mathbb Z\), hence comprise the horizontal degree-\(96\) closure of the classical incidence. The four remaining terms are supported entirely in characteristic \(3\), each with length \(4\). In particular:

* Over any algebraically closed field of characteristic other than \(2,3\), there are \(16\) distinct marked points, \(16\) distinct planes, and exactly \(96\) reduced incidences: six points per plane.
* In characteristic \(3\), the points and planes remain individually distinct; exactly \(16\) new reduced incidences appear, giving \(112\) incidences and seven points per plane. The new pairs form the diagonal under the coordinate-identification of the two marked schemes.
* In characteristic \(2\), each marked scheme has exactly four geometric support points, each with completed local algebra \(k[[u,v]]/(u^2,v^2)\) of length \(4\). The incidence scheme has twelve support points, each with completed local algebra \(k[[u,v,w]]/(u^2,v^2,w^2)\) of length \(8\). A fixed geometric marked plane meets the marked point scheme in three length-\(2\) curvilinear schemes, one on each of the three other coordinate components, for total length \(6\).

The actual special fibers of \(\mathscr X\) at the exceptional primes are **nonreduced double smooth quadrics**. Explicitly, over characteristic \(2\),
\[
F=\left(\sum_i X_i^2+\sum_{i<j}X_iX_j\right)^2,
\]
while over characteristic \(3\),
\[
F=-\left(\sum_i X_i^2\right)^2.
\]
The named schemes \(N\) and \(T\) are *schematic closures of the ordinary-characteristic marked configurations*, not the full singular or actual trope schemes of these nonreduced special fibers. The fact that the quartic becomes a square in the two excluded characteristics was already noted by Catanese; the new assertion concerns the **complete integral marked incidence scheme**, including its flat and vertical components.

## Assumptions and scope

All coordinates, subschemes, and bilinear incidence equations are taken over \(\mathbb Z\) with the fixed primitive model above. Indices \(i,j\) always range over \(\{0,1,2,3\}\). The genus-two Jacobian interpretation of a smooth Kummer K3 resolution is asserted only on the original characteristic-not-\(2,3\) locus and is not used for the exceptional fibers. Base changes to algebraic closures are explicitly indicated when enumerating geometric supports.

For generic fibers in characteristic different from \(2,3\), Catanese identifies the sixteen ordinary nodes as the signed permutations of \([1:1:1:0]\), and their polar planes as the sixteen tropes. Thus \(N\) and \(T\) are integral closures of those *marked finite configurations*. No claim is made that \(N\) is the Jacobian singular scheme of \(\mathscr X\) at primes \(2\) or \(3\).

## Proof

**1. The flat closures.** Fix a missing index \(i\), and order its complement as \(\{h,k,l\}\). Since \(X_h^2=X_k^2=X_l^2\), the three nonmissing coordinates cannot vanish at any point of \(N_i\), including scheme-theoretically after arbitrary base change. The affine chart \(X_h=1\) therefore covers all of \(N_i\). Putting \(u=X_k/X_h\), \(v=X_l/X_h\) gives
\[
N_i\simeq\operatorname{Spec}\mathbb Z[u,v]/(u^2-1,v^2-1)\simeq\mu_2^2.
\]
The four components have disjoint supports over every geometric fiber (their missing coordinate is uniquely determined), hence are pairwise disjoint as closed subschemes. Their coordinate rings are free of rank \(4\) over \(\mathbb Z\). The identical argument applies to \(T_i\), proving both finite-flat assertions. Inverting \(6\), each component consists of the four sign choices of the three nonzero coordinates, so these flat schemes are precisely the schematic closures of the marked configurations, not merely some finite models with the correct generic support. The defining equations also give \(F|_{N_i}=0\): three equal squares yield the equality \(3a^2-3a^2=0\).

**2. Incidences with distinct missing indices.** If \(i\ne j\), the coordinate supports of \(N_i\) and \(T_j\) overlap in exactly two indices, say \(k,l\). All their nonmissing coordinate functions are units of square one. The incidence equation is
\[
X_kY_k+X_lY_l=(X_kY_k)(1+t)=0,
\qquad t=(X_lY_l)/(X_kY_k),\qquad t^2=1.
\]
In the coordinate ring of \(N_i\times T_j\simeq\mu_2^4\), the character \(t\) is nontrivial and is part of a \(\mathbb Z/2\)-basis of its character group: it uses an independent sign variable from one of the two factors. Replacing the four sign generators by \(t\) and three complementary characters is an integral group-ring automorphism. Consequently
\[
I_{ij}=I\cap(N_i\times T_j)\simeq
\operatorname{Spec}\mathbb Z[t,u,v,w]/(t^2-1,u^2-1,v^2-1,w^2-1,1+t)
\simeq\mu_2^3.
\]
Each of the twelve ordered pairs \(i\ne j\) contributes a finite flat rank-\(8\) component.

**3. Incidences with equal missing indices.** If \(i=j\), choose the same first nonmissing coordinate to normalize both schemes. Their product has sign coordinates \(u,v,U,V\), all squaring to one, and the incidence equation is \(1+uU+vV=0\). Replace generators by \(u,v,r=uU,s=vV\). Then
\[
\begin{aligned}
\mathcal O(I_{ii})&=\mathbb Z[u,v,r,s]/(u^2-1,v^2-1,r^2-1,s^2-1,1+r+s)\\
&\simeq\mathbb Z[u,v]/(3,u^2-1,v^2-1).
\end{aligned}
\]
Indeed, \(s=-1-r\) and \(s^2=r^2=1\) give \(1+2r=0\), while multiplying by \(r\) gives \(r+2=0\); substitution yields \(3=0\). Conversely, modulo \(3\), setting \(r=s=1\) satisfies all the relations. Thus \(I_{ii}\simeq\mu_{2,\mathbb F_3}^2\), a reduced four-point scheme over an algebraic closure of \(\mathbb F_3\). These four components are disjoint from one another and from those in Step 2 because \(N\) and \(T\) were disjoint unions. This proves the global scheme decomposition exactly, including the absence of other vertical components or embedded structure.

**4. Geometric fibers and local algebras.** In characteristic different from \(2\), \(\mu_2\) is étale of degree two. Thus the twelve flat terms give \(12\cdot8=96\) reduced incidences, and the four characteristic-three terms give another \(4\cdot4=16\), exactly at that prime. For a given signed plane, each of the other three missing-coordinate groups contributes two nodes; when the characteristic is \(3\) the same missing-coordinate group contributes additionally its own signed node. This gives six or seven points per plane as asserted.

In characteristic \(2\), \(z^2-1=(z-1)^2\). Hence each \(N_i\) and \(T_i\) has a single support point with local algebra \(k[u,v]/(u^2,v^2)\). Each flat incidence term \(\mu_2^3\) has a single support point and local algebra \(k[u,v,w]/(u^2,v^2,w^2)\). At a fixed *geometric* plane in \(T_j\), the incidence equation on any \(N_i\) with \(i\ne j\) eliminates one of its two square-zero coordinates and leaves \(k[e]/(e^2)\), length \(2\); on \(N_j\) it is the constant unit \(1\) at the sole support. This proves the full characteristic-two fiber and the fixed-plane intersection lengths.

**5. The quartic at the exceptional primes.** The integral identity
\[
2F=\left(\sum_iX_i^2\right)^2-3\sum_iX_i^4
\]
gives the characteristic-three factorization, while reduction of \(F\) modulo two gives the characteristic-two square displayed above. In characteristic \(2\) the polar matrix of \(\sum_iX_i^2+\sum_{i<j}X_iX_j\) is \(J+I\), with \(J\) the four-by-four all-ones matrix; since \((J+I)^2=I\) in characteristic \(2\), that quadratic form is nonsingular. In characteristic \(3\), the gradient of \(\sum_iX_i^2\) is \((2X_i)_i\), so this quadric is also smooth. This observation explains why the marked configurations in Steps 1–4 must not be confused with the full singular schemes of the nonreduced quartic fibers.

## Verification

The included standalone program `verify_incidence.py` runs using only the Python standard library. Execute `python verify_incidence.py`. It expands both exceptional-prime polynomial square identities coefficient by coefficient, checks the characteristic-two polar matrix, enumerates all sixteen integral sign representatives and their \(16\times16\) scalar-product table, verifies the \(96\) generic and \(112\) characteristic-three incidences and the precise diagonal extra pairs, and checks the determinant \(\pm3\) of multiplication by \(1+r+s\) on \(\mathbb Z[(\mathbb Z/2)^2]\). Its successful terminal marker is `CEFALU_INTEGRAL_INCIDENCE_96_HORIZONTAL_16_VERTICAL_CHAR3_AND_CHAR2_THICKENING_PASS`.

These finite checks support, but do not replace, the scheme-theoretic isomorphisms in Steps 1–4, which prove the assertions over the entire base \(\mathbb Z\).

## Relationship to prior work

Catanese's *Kummer quartic surfaces, strict self-duality, and more* (arXiv:2101.10501, first posted 2021-01-26), Theorem 1 and its proof, supplies the defining polynomial, sixteen generic nodes, their polar planes, the classical \((16_6)\) incidence, and explicitly observes that the quartic equation becomes a square in characteristics \(2\) and \(3\). Those facts are **not** claimed as new. The result here is the exact closed **integral incidence scheme** for the canonical closures of these marked points and planes: twelve flat components, four vertical characteristic-three components, and the length-eight characteristic-two incidences.

Dolgachev's *K3 surfaces of Kummer type in characteristic two* (2024) constructs genuine characteristic-two K3 surfaces with abstract Kummer configurations through quadric and congruence geometry. These are not the nonreduced special fiber of the fixed Cefalù equation, nor do they determine its marked incidence closure. Kondō and Schröer's *Kummer surfaces associated with group schemes* (2019/2021) constructs normal characteristic-two quotient surfaces via \(\mu_2\)-actions on products of cuspidal curves, likewise a different surface and incidence problem.

## Limitations

This theorem is model-dependent: it concerns the given primitive integral embedding and the canonical schematic closures of its sixteen distinguished generic points and sixteen polar planes. It does not claim that the nonreduced special-fiber quadrics are Kummer surfaces, or that their actual singular/trope schemes equal the marked closures. The decomposition does not construct a simultaneous resolution, and it is not a classification of all integral models of Kummer surfaces. Priority over possible unindexed equivalent incidence calculations has not been independently established.

## References

1. F. Catanese, *Kummer quartic surfaces, strict self-duality, and more*, arXiv:2101.10501, initial public version 2021-01-26, especially Theorem 1, Remark 14, and Section 4. https://arxiv.org/abs/2101.10501
2. I. V. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, Bulletin of the London Mathematical Society 56 (2024), 1903–1919, DOI 10.1112/blms.13033. https://doi.org/10.1112/blms.13033
3. S. Kondō and S. Schröer, *Kummer surfaces associated with group schemes*, arXiv:1912.12015 (2019); Manuscripta Mathematica 166 (2021), 323–342. https://arxiv.org/abs/1912.12015
