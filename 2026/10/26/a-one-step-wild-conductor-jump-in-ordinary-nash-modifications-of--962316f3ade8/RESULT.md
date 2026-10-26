# A one-step wild conductor jump in ordinary Nash modifications of odd \(A\)-type surface singularities

## Finding
Fix an odd integer \(m\ge3\), and let \(k\) be an algebraically closed field of characteristic different from \(2\). Put
\[
 X_m=\operatorname{Spec} k[x,y,z]/(xy-z^m)
\]
and let \(N_m\to X_m\) be the **ordinary, non-normalized** Nash blowup. At the geometric generic point of its reduced exceptional curve, the local transverse semigroup depends on whether the characteristic divides \(m\):
\[
 S_{\mathrm{wild}}=\langle2,m\rangle\quad(\operatorname{char}k\mid m),\qquad
 S_{\mathrm{tame}}=\langle2,m-2\rangle\quad(\operatorname{char}k\nmid m).
\]
Write \(\delta_{\mathrm{gen}}\) for the length of the quotient of the integral closure by the one-dimensional local ring at the generic exceptional point, over its residue field. Write \(c_{\mathrm{gen}}\) for the valuation exponent of its conductor in the normalization. Then
\[
 (\delta_{\mathrm{gen}},c_{\mathrm{gen}})=
 \begin{cases}
 ((m-1)/2,m-1),&\operatorname{char}k\mid m,\\
 ((m-3)/2,m-3),&\operatorname{char}k\nmid m.
 \end{cases}
\]
Thus the ordinary Nash blowup acquires **exactly one additional generic normalization length and two additional conductor steps** when the characteristic divides \(m\). The normalized Nash blowups in the two cases have the same toric modification. For \(m=3\) the tame generic exceptional point is regular, while the wild generic exceptional point is a cusp.

## Assumptions and scope
All assertions hold for every odd \(m\ge3\) and every algebraically closed \(k\) with \(\operatorname{char}k\ne2\). The wild case is possible only in positive characteristic. The local invariants concern the generic point of the reduced exceptional curve of the **first ordinary Nash blowup**, not isolated singularities of \(X_m\), not its entire exceptional fibre, and not a claim about further iterations. If \(K=k(t)\) is the rational function field of this curve, length is taken over \(K\) after localizing at the exceptional height-one prime.

## Proof
**Jacobian centers.** For \(f=xy-z^m\), the gradient is \((y,x,-m z^{m-1})\). The surface is integral and normal: it is a hypersurface with its sole singular point at the origin and satisfies the codimension-one regularity and Cohen–Macaulay conditions. Since the Nash map for a hypersurface is the projective gradient map, its graph closure is the blowup of the gradient ideal. Hence the Nash center is \(I_w=(x,y)\) when \(\operatorname{char}k\mid m\), and \(I_t=(x,y,z^{m-1})\) otherwise. These ideals are nonzero in the domain.

**An open neighborhood of the generic exceptional point.** On the blowup chart corresponding to generator \(x\), set \(t=y/x\) and restrict to \(t\ne0\). In the wild case, direct elimination in the Rees algebra gives
\[
 B_w=k[t,t^{-1},x,z]/(t x^2-z^m).
\]
In the tame case adjoin \(u=z^{m-1}/x\). The relations \(t x^2=z^m\) and \(xu=z^{m-1}\) imply \(tx=zu\), and elimination gives
\[
 B_t=k[t,t^{-1},u,z]/(u^2-t z^{m-2}),
 \qquad x=zu/t,\quad y=zu.
\]
Conversely these formulas satisfy the graph equations and induce injections into the common function field on the dense locus \(xz\ne0\), so no additional Rees relation is present. In both charts the reduced exceptional curve is \(x=z=0\), respectively \(u=z=0\), with generic parameter \(t\); its residue field is \(K=k(t)\).

**Local normalization and semigroups.** In either chart define \(s\) in its fraction field by \(s^2=tz\). In the wild chart one may take \(s=z^{(m+1)/2}/x\). In the tame chart one may take \(s=u/z^{(m-3)/2}\). Then
\[
 z=s^2/t,\qquad x=s^m/t^{(m+1)/2},\qquad
 u=s^{m-2}/t^{(m-3)/2}\quad\text{(tame)}.
\]
As powers of \(t\) are units, the respective one-dimensional local domains at the generic exceptional prime are
\[
 K[s^2,s^m]_{(s^2,s^m)},\qquad
 K[s^2,s^{m-2}]_{(s^2,s^{m-2})}.
\]
Their integral closures in the common rational fraction field are \(K[s]_{(s)}\). For odd \(r\ge1\), the nonnegative integers absent from \(\langle2,r\rangle\) are precisely \(1,3,\ldots,r-2\). A monomial basis of the quotient of the normalization by the local ring consists of the corresponding powers of \(s\); its length is \((r-1)/2\). The conductor is \(s^{r-1}K[s]_{(s)}\) because every valuation at least \(r-1\) occurs and \(r-2\) does not (if \(r=1\), the conductor is the unit ideal). Substituting \(r=m\) or \(r=m-2\) proves the formulas and the jumps.

**Why normalization does not see the jump.** Within the normal surface coordinate ring, \(z^{m-1}\) is integral over \((x,y)\), since it satisfies \(T^2-(xy)z^{m-2}=0\) and the constant coefficient belongs to \((x,y)^2\). Thus \((x,y)\) and \((x,y,z^{m-1})\) have identical integral closures of all powers; equivalently their normalized Rees algebras, and hence normalized blowups, agree. This special-case proof is consistent with the known characteristic-independence of normalized toric surface Nash fans.

## Verification
The accompanying portable Python program `nash_checker.py` uses exact integer arithmetic. Running `python3 nash_checker.py` verifies the chart monomial identities, conductor thresholds, semigroup gaps and the two-step conductor difference for every odd integer from \(3\) through \(41\). These are finite regression checks, not the proof for arbitrary \(m\); the algebraic argument above proves the universal claim.

## Relationship to prior work
The normalized toric surface Nash construction and its characteristic-independent fan are known, notably from Atanasov–Lopez–Perry–Proudfoot–Thaddeus and Duarte–Jeffries–Núñez-Betancourt. González Pérez–Teissier supply a general monomial blowup construction; González-Sprinberg studies rational double points in characteristic zero, and Duarte–Snoussi study iteration of ordinary toric Nash modifications in characteristic zero. These broader frameworks are prior results. The statement here isolates an exact **generic conductor/normalization-length comparison across wild versus tame characteristics of the same \(A\)-type surface**, which is not a consequence of the normalized fan alone. No novelty is asserted for the formula for a numerical semigroup's gaps or for the general Jacobian blowup representation.

## Limitations
Only the first ordinary Nash modification and generic exceptional codimension-one nonnormality are calculated. No classification of all closed points on the exceptional fibre, of higher Nash blowups, or of every characteristic-two case is asserted. Published frameworks give combinatorial tools from which these specialized local computations can be derived, and possible unpublished or older exact conductor comparisons cannot be excluded. The result has self-review only; no independent audit has occurred.

## References
1. A. Atanasov, C. Lopez, A. Perry, N. Proudfoot, M. Thaddeus, *Resolving toric varieties with Nash blow-ups* (first arXiv version 27 October 2009), arXiv:0910.5028, https://arxiv.org/abs/0910.5028.
2. G. González-Sprinberg, *Résolution de Nash des points doubles rationnels*, Annales de l'Institut Fourier 32 (1982), 111–178, https://doi.org/10.5802/aif.874.
3. P. D. González Pérez and B. Teissier, *Toric Geometry and the Semple-Nash modification*, arXiv:0912.0593 (2009), https://arxiv.org/abs/0912.0593.
4. D. Duarte, J. Jeffries, L. Núñez-Betancourt, *Nash blowups of toric varieties in prime characteristic*, Collectanea Mathematica 75 (2024), 629–637, first online 28 April 2023, https://doi.org/10.1007/s13348-023-00402-y.
5. D. Duarte and J. Snoussi, *Nash blowups of normal toric surfaces: the case of one and two segments*, Beiträge zur Algebra und Geometrie, first online 28 August 2025, https://doi.org/10.1007/s13366-025-00805-x.
