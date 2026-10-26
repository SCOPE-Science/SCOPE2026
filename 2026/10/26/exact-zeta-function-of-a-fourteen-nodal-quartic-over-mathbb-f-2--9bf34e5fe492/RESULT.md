# Exact zeta function of a fourteen-nodal quartic over \(\mathbb F_2\)

## Finding
Let \(X\subset\mathbb P^3_{\mathbb F_2}\) be the reduced projective surface
\[
X:\quad w^4+w^2x^2+x^3y+y^3z+z^3x=0.
\]
The surface is geometrically integral, normal, and has precisely fourteen geometric ordinary double points. Frobenius permutes these nodes in four cycles of lengths \(2,3,3,6\).

Its **exact Hasse–Weil zeta function** is
\[
Z(X/\mathbb F_2,T)=\frac{1}{(1-T)(1-4T)(1-2T)(1+2T)(1-8T^3+64T^6)}.
\]
For every integer \(n\ge1\), writing \(q=2^n\), the closed-point formula is equivalently
\[
\#X(\mathbb F_q)=1+q^2+q\left(1+(-1)^n+3\mathbf1_{3\mid n}-6\mathbf1_{6\mid n}-9\mathbf1_{9\mid n}+18\mathbf1_{18\mid n}\right).
\]
If \(Y\to X\) is the minimal resolution, then \(Y\) is a supersingular K3 surface and its second-cohomology Frobenius determinant is
\[
\det(1-FT\mid H^2_{\mathrm{\acute et}}(Y_{\overline{\mathbb F}_2},\mathbb Q_\ell))=
\Phi_1(2T)^5\Phi_2(2T)^3\Phi_3(2T)^3\Phi_6(2T)\Phi_{18}(2T)
\]
for every prime \(\ell\ne2\), with the usual cyclotomic polynomials \(\Phi_d\). In particular, all eigenvalues on \(H^2\) are twice roots of unity, and the zeta function determines every extension-field point count.

## Assumptions and scope
The equation and all point counts refer to this literal \(\mathbb F_2\)-model, not an unspecified twist or an abstract isomorphism class. The zeta function is that of the **singular quartic** \(X\), not that of the smooth resolution \(Y\); both are explicitly distinguished. Singularities are geometric points over an algebraic closure, and their orbit lengths are for the absolute Frobenius \(u\mapsto u^2\). Standard purity, the cohomological trace formula, the Weil absolute-value bound and the K3 second Betti number \(22\) are used in the last step. The geometric fourteen-node model and the fact that its minimal resolution is supersingular K3 belong to the cited literature; the arithmetic factorization, descent cycles, and all-extension count are the claimed contribution.

## Proof
**Geometric singularities and their descent.** On the chart \(x=1\), write
\[
F=w^4+w^2+y+y^3z+z^3.
\]
All partial derivatives in the \(w\)-direction vanish. The critical-point equations in \(y,z\) are \(1+y^2z=0\) and \(y^3+z^2=0\), hence \(y^7=1\) and \(z=y^5\). The projective partial derivatives have no common zero on \(x=0\). At each of the seven base critical points \((y,z)=(\epsilon,\epsilon^5)\), the equation for \(w\) becomes \(w^4+w^2=\epsilon\), which has two distinct geometric roots, each of multiplicity two. Thus there are exactly fourteen geometric singular points, with no other singular points. The quadratic term of the local equation has a nonzero \(w\)-square coefficient and a nonzero \(yz\)-polar coefficient \(\epsilon^2\); its projectivized quadratic tangent cone is a smooth conic. All fourteen points are therefore ordinary double points. The finite singular set and hypersurface Cohen–Macaulay property give normality; a reducible hypersurface in projective three-space would have positive-dimensional singular intersection, so the surface is geometrically integral.

Every \(\epsilon\) lies in \(\mathbb F_8\). In \(\mathbb F_8\), the equation for \(w\) is equivalent to an Artin–Schreier equation whose splitting is decided by \(\operatorname{Tr}_{\mathbb F_8/\mathbb F_2}(\epsilon)\). The root \(\epsilon=1\) has trace one; of the six primitive seventh roots, three have trace zero and three have trace one. Frobenius consequently has a single length-two orbit above \(\epsilon=1\), two length-three orbits above the trace-zero three-cycle, and one length-six orbit above the trace-one three-cycle. This proves the stated multiset \(\{2,3,3,6\}\). The exact independent algebraic-field check in `verify.py` reconstructs these orbits directly in \(\mathbb F_{64}\).

**Reduction of finite-field counts to a complete finite sum.** Fix \(m\ge1\) and let \(q=2^m\). Above \(x=0\), every \([y:z]\in\mathbb P^1(\mathbb F_q)\) lifts to exactly one \(\mathbb F_q\)-point, since raising to the fourth power is a bijection. Above \(x=1\), the equation has two or zero roots according as the absolute trace of \(y+y^3z+z^3\) is zero or one. Therefore
\[
\#X(\mathbb F_q)=q^2+q+1+S_m,\qquad
S_m=\sum_{y,z\in\mathbb F_q}(-1)^{\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(y+y^3z+z^3)}.
\]
The sums for \(1\le m\le12\) were exhaustively computed by the self-contained `count.c` using explicit binary irreducible polynomials of degrees \(1\) through \(12\). Polynomial irreducibility, independent small-field direct point enumeration, the node cycles, the Newton recurrence and factor identity are checked in `verify.py`. The exact resulting \(S_m\) sequence is
\[
(-2,4,16,16,-32,-128,-128,256,-3584,1024,-2048,-8192).
\]
These are **finite exhaustive computations**, not an extrapolation to all extensions.

**The geometric bridge from twelve sums to all extensions.** Let \(Y\to X\) be the minimal resolution. Fourteen ordinary nodes imply that \(Y\) is a K3 surface (also established in the cited Catanese–Schütt theorem). Each node defined over \(\mathbb F_{2^d}\) is replaced by a projective line over its residue field, so
\[
\#Y(\mathbb F_{2^m})=\#X(\mathbb F_{2^m})+2^m\left(2\mathbf1_{2\mid m}+6\mathbf1_{3\mid m}+6\mathbf1_{6\mid m}\right).
\]
Put \(s_m=(\#Y(\mathbb F_{2^m})-1-4^m)/2^m\). The twelve exact sums yield
\[
(s_1,\ldots,s_{12})=(0,4,9,4,0,13,0,4,0,4,0,13).
\]
Write \(P(u)=\prod_{j=1}^{22}(1-\lambda_j u)\) with \(\lambda_j\) the eigenvalues of Frobenius on \(H^2(Y)\) divided by \(2\). The Weil bounds and real rational characteristic polynomial imply that the \(\lambda_j\) occur in reciprocal-conjugate pairs (with roots of absolute value one), giving \(c_{22-j}=e c_j\), where \(c_j=[u^j]P(u)\) and \(e\in\{1,-1\}\). Newton's identities
\[
 c_0=1,\qquad kc_k=-\sum_{i=1}^k s_i c_{k-i}
\]
give the first thirteen coefficients
\[
(c_0,\ldots,c_{12})=(1,0,-2,-3,1,6,3,-3,-6,0,3,0,-3).
\]
In particular \(c_{12}=-3=-c_{10}\ne0\), forcing \(e=-1\). Reciprocity now supplies the remaining ten coefficients uniquely, and direct polynomial multiplication factors the completed degree-twenty-two determinant as
\[
P(u)=\Phi_1(u)^5\Phi_2(u)^3\Phi_3(u)^3\Phi_6(u)\Phi_{18}(u).
\]
This step uses the global degree and functional equation of K3 cohomology; hence it upgrades finite exact counts into an infinite theorem rather than treating sampled fields as an infinite proof.

Finally, replacing each of the four Frobenius node orbits by exceptional projective lines gives
\[
Z(X,T)=Z(Y,T)(1-(2T)^2)(1-(2T)^3)^2(1-(2T)^6).
\]
Since \((1-u^2)(1-u^3)^2(1-u^6)=\Phi_1(u)^4\Phi_2(u)^2\Phi_3(u)^3\Phi_6(u)\), cancellation proves the displayed zeta function. The explicit point-count formula follows from the Ramanujan sum
\[
 c_{18}(m)=3\mathbf1_{3\mid m}-6\mathbf1_{6\mid m}-9\mathbf1_{9\mid m}+18\mathbf1_{18\mid m}.
\]

## Verification
Run `python3 verify.py` in the same directory as `count.c` using Python 3 and a C11 compiler such as `cc`. It verifies irreducibility of all twelve binary field polynomials, tests multiplicative field identities, reconstructs the fourteen nodes and their complete Frobenius orbits over \(\mathbb F_{64}\), checks the first four field counts by direct projective enumeration independent of the character-sum method, exhaustively evaluates all twelve double character sums, reconstructs the K3 determinant from Newton's identities, and confirms both cyclotomic factorizations and all-extension formula against the twelve exact counts. The local run returned `VERIFY_OK`.

For instance, exact counts for \(m=1,2,3,4,6,12\) are \(5,25,89,289,4033,16773121\), respectively. An extra distinct degree-thirteen field computation returned \(\#X(\mathbb F_{8192})=67108865\), consistent with the derived formula; this last check is corroboration, not used to determine the polynomial.

## Relationship to prior work
Catanese's two 2021 accounts (the 2106.06643 appendix and 2106.09988 Section 2.3, both attributing the construction to Schütt) supply the quartic construction from the Klein plane quartic and the description of its seven plane critical points. Catanese and Schütt's 2021 preprint establishes the sharp fourteen-node theorem and supersingular K3 resolution. These geometric inputs are **prior results**, not claimed here. Their relevant source sections give neither the four arithmetic Frobenius orbit lengths of this explicit \(\mathbb F_2\)-model nor its full zeta polynomial. The present assertion is an arithmetic refinement, determined by exact finite-field character sums together with the global cohomological functional equation, not a restatement of the supersingularity assertion. Comparison to other similarly named Klein curves must distinguish this singular quartic surface from the genus-three Klein plane curve itself.

## Limitations
The claim is for this single model and its specified minimal resolution. It does not determine the zeta functions of all fourteen-nodal quartics, nor the integral Galois module of its Néron–Severi group or its Artin invariant. Historical or unindexed source computations could conceivably contain equivalent arithmetic information. Independent scholarly verification has not been performed. The C11 exhaustive enumerations are finite arithmetic certificates; their source and field-polynomial checks are part of the package.

## References
1. F. Catanese, *The number of singular points of quartic surfaces (char=2)*, arXiv:2106.06643, first public version June 11, 2021, especially Section 2.1 Step IV and Appendix (Schütt construction). https://arxiv.org/abs/2106.06643
2. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, first public version June 18, 2021, Sections 2.1 and 2.3. https://arxiv.org/abs/2106.09988
3. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078, first public version October 6, 2021, Theorem 1 and Sections 3 and 7. https://arxiv.org/abs/2110.03078
4. Standard cohomological facts used: K3 surfaces have second Betti number \(22\), purity and the Weil absolute values give Frobenius reciprocal symmetry; the Lefschetz trace formula and Newton identities connect point counts to the characteristic polynomial.
