# Resolution and local monodromy of a free Fermat–Cremona arrangement

## Finding
For every integer \(m\ge 2\), consider the reduced complex projective plane curve
\[
B_m=V\!\left((x^m y^m+y^m z^m+x^m z^m)(x^m+y^m)(y^m+z^m)\right)\subset\mathbb P^2_{\mathbb C}.
\]
Its singular locus consists of precisely three coordinate vertices and \(m^2\) additional ordinary nodes. The vertex \(p_y=[0:1:0]\) is an ordinary \(m\)-fold point. Each of the other vertices, \(p_x=[1:0:0]\) and \(p_z=[0:0:1]\), has \(2m\) smooth branches, divided into \(m\) pairs. The two branches within each pair have intersection multiplicity \(m+1\); every other pair of distinct branches intersects with multiplicity one.

At either of these two distinguished vertices the reduced embedded resolution has one central exceptional curve of multiplicity \(2m\) and, attached at \(m\) distinct points, \(m\) chains each of length \(m\), with successive multiplicities \(2m+2,2m+4,\ldots,4m\). Write \(h\) for local geometric Milnor monodromy and \(F_p\) for its Milnor fiber. Its first-homology characteristic polynomial is exactly
\[
\det\bigl(I-t h_*\mid H_1(F_p,\mathbb Q)\bigr)
=(1-t)(1-t^{2m})^{m-2}(1-t^{4m})^m.
\]
The local numerical invariants are
\[
\delta_p=3m^2-m,\qquad \mu_p=6m^2-4m+1,\qquad
\tau_p=5m^2-2m,\qquad \mu_p-\tau_p=(m-1)^2.
\]
For the entire arrangement the total Milnor number and Tjurina number are, respectively,
\[
\mu(B_m)=14m^2-10m+3,\qquad
\tau(B_m)=12m^2-6m+1,
\]
so the complete non-quasihomogeneity defect is \(2(m-1)^2\). The two local Tjurina values and freeness already follow from the primary source; the contribution here is the uniform complete branch/resolution/monodromy description and its exact comparison with those values.

## Assumptions and scope
All curves, analytic germs, Milnor fibers and local monodromy are over \(\mathbb C\), in characteristic zero. All assertions quantify over **every** integer \(m\ge2\). Each monodromy polynomial is for the reduced local plane-curve germ at the specified vertex, not the global Alexander polynomial of the projective complement. The multiplicities on exceptional curves are those of the total transform of the local defining equation; the order of branches within a pair is immaterial.

The nonlinear factor \(Q=x^m y^m+y^m z^m+x^m z^m\) is irreducible. For example, at a linear prime dividing \(y^m+z^m\), the reciprocal polynomial \((y^m+z^m)+y^m z^m s^m\) is Eisenstein over the corresponding discrete valuation ring. The two line-pencils have distinct simple factors and share no component with \(Q\); hence the displayed defining equation is reduced.

## Proof
**1. Exhaust the singular locus.** In the algebraic torus where \(xyz\ne0\), a singular point of \(Q=0\) would satisfy \(y^m+z^m=x^m+z^m=x^m+y^m=0\), which is impossible in characteristic zero. On a coordinate axis, \(Q\) vanishes only at the vertices. At \(p_y\) neither line-pencil factor vanishes. The restriction of \(Q\) to either of the degree-\(m\) line-pencil curves is \(-y^{2m}\); therefore their only intersections with \(Q\) are the respective coordinate vertices. The two distinct line pencils intersect precisely when \(x^m=z^m=-y^m\ne0\), giving \(m^2\) distinct points. These are transverse intersections of one line from each pencil, and \(Q=-y^{2m}\ne0\) there, so all are ordinary nodes. No further singularities exist.

**2. Identify branches and their contacts.** At \(p_x\), use \(x=1\) and set \(U=y^m+z^m\). The other pencil factor \(1+y^m\) is a unit, so the reduced germ is
\[
U(U+y^m z^m)=0.
\]
For each root \(\rho^m=-1\), the first factor defines the line \(y=\rho z\). Put \(y=z(\rho+w)\) in the second factor. After dividing by \(z^m\), its equation becomes
\[
(\rho+w)^m+1+z^m(\rho+w)^m=0.
\]
The derivative in \(w\) at the origin is \(m\rho^{m-1}\ne0\), so the implicit-function theorem gives precisely one smooth branch
\[
y=\rho z+\frac{1}{m\rho^{m-1}}z^{m+1}+O(z^{m+2}).
\]
It meets its paired line with intersection multiplicity \(m+1\). Branches corresponding to distinct roots have distinct tangent lines and meet transversely. Thus there are \(2m\) smooth branches with exactly \(m\) enhanced contacts. Symmetry exchanging \(x\) and \(z\) proves the same statement at \(p_z\). Therefore
\[
\delta_p=\binom{2m}{2}+m\cdot m=3m^2-m,
\qquad \mu_p=2\delta_p-2m+1=6m^2-4m+1.
\]
At \(p_y\), the line factors are units and the equation is \(x^m+z^m+x^mz^m=0\). Its reduced tangent cone consists of \(m\) distinct lines, hence it is an ordinary \(m\)-fold point with \(\mu=\tau=(m-1)^2\). In fact, multiplying one local coordinate by the analytic unit \((1+z^m)^{1/m}\) identifies this germ with \(x^m+z^m=0\).

**3. Construct the complete embedded resolution at either nonordinary vertex.** Blow up the vertex once. The first exceptional curve \(E_0\) has total-transform multiplicity \(2m\). The \(m\) distinct tangent directions give \(m\) points on \(E_0\); at each point the two smooth strict-transform branches have contact \(m\) and meet \(E_0\) transversely. In local coordinates the pair is analytically of the form \(v=0\) and \(v=s^m u(s)\), where \(u(0)\ne0\), with \(E_0\) given by \(s=0\).

For each such pair, perform \(m\) successive point blowups along the common tangent. In the chart \(v=s^k v_k\), the strict-transform pair has contact \(m-k\) until its members meet the final exceptional curve at different points when \(k=m\). At the \(k\)-th blowup the center lies on a single exceptional curve of multiplicity \(2m+2(k-1)\) and on two smooth branches of multiplicity one; consequently the new exceptional multiplicity is \(2m+2k\). The previous exceptional intersects the new one away from the two branch points. These operations yield simple normal crossings, and no further blowups are required.

The central exceptional curve meets exactly the \(m\) first curves of the tails, so \(\chi(E_0^\circ)=2-m\). Each intermediate tail component meets its two neighboring exceptional curves and no strict branch, giving Euler characteristic zero. Each last tail component meets the preceding exceptional curve and two distinct strict branches, giving \(\chi(E_{j,m}^\circ)=-1\). By A'Campo's resolution formula, the Lefschetz zeta function of local Milnor monodromy is
\[
\zeta_h(t)=(1-t^{2m})^{m-2}(1-t^{4m})^m.
\]
Since the reduced plane-curve Milnor fiber is connected, its \(H_0\) is one-dimensional with trivial monodromy; multiplying the zeta function by \(1-t\) gives the stated first-homology characteristic polynomial. Its degree is \(1+2m(m-2)+4m^2=6m^2-4m+1\), independently confirming the Milnor number computed from branches.

**4. Determine the Tjurina defect without assuming a local formula.** Set \(X=x^m\), \(Y=y^m\), \(Z=z^m\) and \(H=(XY+YZ+XZ)(X+Y)(Y+Z)\). Two syzygies of its pullback \(f=H(x^m,y^m,z^m)\) are
\[
R_1=\bigl(z^{m-1}(x^m+y^m),0,-x^{m-1}(y^m+z^m)\bigr)
\]
and
\[
R_2=\bigl(xy^{m-1}(2x^m+3y^m),
 -(2Q+y^{2m}),zy^{m-1}(2z^m+3y^m)\bigr).
\]
Direct polynomial identities give \(R_1\cdot\nabla f=R_2\cdot\nabla f=0\) and
\[
\det\begin{pmatrix}x&y&z\\R_1\\R_2\end{pmatrix}=-4f.
\]
Saito's criterion proves freeness with exponents \((2m-1,2m)\), in agreement with the primary source. The total Tjurina number is therefore
\[
(4m-1)^2-(2m-1)(2m)=12m^2-6m+1.
\]
The \(m^2\) nodes each have Tjurina number one, and the ordinary \(m\)-fold vertex has \((m-1)^2\). The other vertices have equal Tjurina numbers by the symmetry \(x\leftrightarrow z\), so each contributes
\[
\frac{12m^2-6m+1-m^2-(m-1)^2}{2}=5m^2-2m.
\]
Subtracting from the proved local Milnor number gives the defect \((m-1)^2\) at each. Adding all four singularity types gives the total Milnor and Tjurina numbers as claimed.

**5. Global consistency.** The nonlinear component has normalization genus \((m-1)(m-2)/2\) by its three ordinary \(m\)-fold points. The sum of local delta invariants on the full reduced curve is \((15m^2-5m)/2\). Together with \(2m+1\) irreducible components, the reducible-curve genus formula yields the arithmetic genus \((4m-1)(4m-2)/2\), another independent consistency check.

## Verification
Run `python verification/verify.py` with Python 3 and SymPy at least version 1.12. The standalone checker verifies the two universal polynomial syzygy identities and the universal determinant identity \(\det=-4f\) exactly; it also checks direct pullbacks for three small degrees and the resolution/multiplicity/genus formulas for sample parameters. A fresh run returned `VERIFY_OK symbolic_syzygies=2 saito_det=-4F direct_m=2,3,4 local_branches=2m matched_contact=m+1 local_delta=3m2-m local_mu=6m2-4m+1 local_tau=5m2-2m resolution=E0(2m)+m_tails(2m+2k) local_monodromy=(1-t)(1-t^(2m))^(m-2)(1-t^(4m))^m`.

The analytic branch argument, exhaustiveness of the singular locus, the blowup charts and the use of A'Campo's theorem prove the statement uniformly; checking finitely many parameter values is not used as an infinite proof. The checker does not claim to construct complex Milnor fibers or certify the topological application of A'Campo's theorem by computation.

## Relationship to prior work
Dimca–Ilardi–Pokora–Sticlaru, Theorem 1.8, provide this exact polynomial and prove it free with the stated exponents. Their Example 6.3 describes the singularities of the nonlinear constituent, and Remark 4.8 notes the nonquasihomogeneous enlarged vertices and extracts the local Tjurina value from freeness. These facts are **not** new claims here. Their explicit description supplies key inputs, but their relevant analysis does not present the complete embedded resolution, its multiplicity graph, the local first-homology monodromy polynomial, or the full singularity basket of the first Theorem 1.8 arrangement. A'Campo's general monodromy formula is established prior work; the new computation is its application to this exact family after resolving the paired high-contact branches.

The closest other monodromy calculations found concern different plane-curve germs and do not provide these chain multiplicities or the displayed polynomial. Historical or unindexed treatments could still contain an equivalent computation.

## Limitations
No claim is made about analytic equivalence classes beyond the stated branch-contact and resolution data, about global complement Alexander polynomials, or about characteristic-positive analogues. The standard A'Campo formula is invoked for the monodromy step rather than reproved. Local Tjurina numbers and the freeness of the family were known; the distinct contribution is the explicitly computed local resolution and topological monodromy uniform in \(m\). Originality remains subject to possible previously unindexed literature.

## References
1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, first arXiv version 2023-01-03, arXiv:2301.01117v1; *Results in Mathematics* 79 (2024), article 11, DOI:10.1007/s00025-023-02036-9. See Theorem 1.8, Section 4.4, Remark 4.8 and Example 6.3.
2. N. A'Campo, *La fonction zêta d'une monodromie*, *Commentarii Mathematici Helvetici* 50 (1975), 233–248, DOI:10.1007/BF02565748. Applied only for the classical exceptional-divisor Euler-characteristic formula.
