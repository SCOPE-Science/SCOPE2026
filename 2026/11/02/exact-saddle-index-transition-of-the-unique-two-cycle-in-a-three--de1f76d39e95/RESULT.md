# Exact saddle-index transition of the unique two-cycle in a three-dimensional Hénon map

## Finding
For the real three-dimensional polynomial diffeomorphism
\[
F_{a,b}(x,y,z)=(a-y^2-bz,\ x,\ y),\qquad 0<b<1,\quad a\in\mathbb R,
\]
define
\[
a_{\mathrm{birth}}(b)=\frac{3b^2-2b-1}{4},\qquad
 a_{\mathrm{flip}}(b)=\frac{5b^2-6b+3}{4}.
\]
There are no primitive two-cycles when \(a\le a_{\mathrm{birth}}\). For every \(a>a_{\mathrm{birth}}\), there is exactly one primitive two-cycle, counted as an unordered pair of points, in all of \(\mathbb R^3\). It has exactly one multiplier outside the closed unit disk when \(a_{\mathrm{birth}}<a<a_{\mathrm{flip}}\), exactly two such multipliers when \(a>a_{\mathrm{flip}}\), and at the intervening threshold has one simple unit multiplier \(-1\), one multiplier greater than \(1\), and one multiplier in \((-1,0)\). Thus the unique two-cycle is never an attracting cycle. The threshold is a spectral flip crossing; existence or stability of a nearby primitive four-cycle is not asserted.

## Assumptions and scope
All quantities and cycles are real. The parameters satisfy \(0<b<1\) and \(a\in\mathbb R\). A primitive two-cycle means an orbit of least period exactly two. Its multipliers are the eigenvalues of the two-step derivative at either cyclic point; unstable dimension is the number of multipliers of modulus strictly greater than one, counted with algebraic multiplicity. The family is a global diffeomorphism for \(b\neq0\), since its Jacobian determinant is \(-b\). There are no boundedness assumptions on cycle coordinates.

## Proof
1. **Complete algebraic census.** The shift structure forces every two-periodic state to alternate between \(P=(u,v,u)\) and \(Q=(v,u,v)\). The equations \(F(P)=Q\) and \(F(Q)=P\) are
\[
 u=a-u^2-bv,\qquad v=a-v^2-bu.
\]
Their difference yields \((u-v)(1+u+v-b)=0\). A *primitive* cycle has \(u\ne v\), hence \(u+v=b-1\). The remaining equation reduces to
\[
u^2-(b-1)u+b(b-1)-a=0.
\]
Its discriminant is \(\Delta=4a-3b^2+2b+1=4(a-a_{\mathrm{birth}})\). When \(\Delta\le0\), no distinct real roots exist; when \(\Delta>0\), the only two ordered roots are
\[
 u=\frac{b-1+\sqrt{\Delta}}2,\qquad v=\frac{b-1-\sqrt{\Delta}}2.
\]
Swapping \(u,v\) merely changes the starting point. Both transition equations hold exactly, so the cycle exists and is unique up to rotation.

2. **Exact monodromy.** At a point whose second coordinate is \(t\), the derivative is
\[
J(t)=\begin{pmatrix}0&-2t&-b\\1&0&0\\0&1&0\end{pmatrix}.
\]
Thus, with the two successive values \(v,u\), a two-step derivative is
\[
M=J(u)J(v)=\begin{pmatrix}-2u&-b&0\\0&-2v&-b\\1&0&0\end{pmatrix},
\]
with characteristic polynomial
\[
 p_{a,b}(\lambda)=\lambda^3+2(b-1)\lambda^2
 +4[b(b-1)-a]\lambda-b^2.
\]
Since \(p_{a,b}(1)=-4(a-a_{\mathrm{birth}})<0\), this monodromy always has a real eigenvalue greater than one (as \(p(\lambda)\to+\infty\) for \(\lambda\to+\infty\)). The cycle is therefore never attracting.

3. **Initial unstable dimension.** At the limiting parameter \(a=a_{\mathrm{birth}}\), the characteristic polynomial factors as
\[
p_{a_{\mathrm{birth}},b}(\lambda)
 =(\lambda-1)\bigl[\lambda^2+(2b-1)\lambda+b^2\bigr].
\]
The quadratic has both roots strictly inside the unit disk: its constant coefficient is \(b^2<1\), and its evaluations at \(1\) and \(-1\) are \(b^2+2b>0\) and \(b^2-2b+2>0\), respectively. The usual quadratic Schur test (or direct root analysis) therefore applies. The simple root \(1\) moves beyond \(1\) immediately as \(a\) increases (its derivative with respect to \(\lambda\) at birth is \(b^2+2b>0\)). Consequently the cycle has one unstable direction just above birth.

4. **All possible unit-circle crossings.** A real multiplier at \(1\) would require \(a=a_{\mathrm{birth}}\) and so does not occur for primitive cycles. A real multiplier at \(-1\) requires
\[
p_{a,b}(-1)=4(a-a_{\mathrm{flip}})=0.
\]
For a nonreal conjugate pair on the unit circle, its product is \(1\); because \(\det M=b^2\), the third eigenvalue must be \(b^2\). Comparing the linear and quadratic coefficients then gives
\[
\cos\theta=1-b-\frac{b^2}{2},\qquad
 a_{\mathrm{pair}}=\frac{b^4+2b^3+2b^2-4b-1}{4}.
\]
But \(a_{\mathrm{pair}}-a_{\mathrm{birth}}=b(b+2)(b^2-1)/4<0\) throughout \(0<b<1\). Hence no conjugate unit pair can arise in the two-cycle existence region. The number of unstable multipliers is constant on each of the two open intervals separated by \(a_{\mathrm{flip}}\).

5. **Sharp index change.** Since
\[
a_{\mathrm{flip}}-a_{\mathrm{birth}}=\frac{b^2-2b+2}{2}>0,
\]
the threshold lies strictly above the birth parameter. At \(a=a_{\mathrm{flip}}\),
\[
p_{a_{\mathrm{flip}},b}(\lambda)
 =(\lambda+1)\bigl[\lambda^2+(2b-3)\lambda-b^2\bigr].
\]
The quadratic has a positive root greater than one and a negative root between \(-1\) and \(0\), as seen by evaluating it at \(0,1,-1\), with positive leading coefficient. The multiplier \(-1\) is simple because
\[
\partial_\lambda p_{a_{\mathrm{flip}},b}(-1)=4-2b-b^2>0.
\]
Implicit differentiation yields \(d\lambda/da=-4/(4-2b-b^2)<0\) there, so it exits the unit disk as \(a\) increases. Thus the unstable dimension is exactly one before the crossing and exactly two after it. These are the only changes, completing the global classification. \(\square\)

## Verification
Run `python verify.py` with Python and SymPy. The reproducibility script checks the exact orbit equations, monodromy determinant and characteristic polynomial, both factorizations, all parameter-ordering identities, and 50 representative numerical root-count computations for rational parameter pairs. The analytical argument above establishes the result for the uncountable parameter range; finite verification is not used as a proof of global eigenvalue counts.

## Relationship to prior work
Muni and Banerjee [1] explicitly study this same three-dimensional generalized Hénon map, especially stable and saddle period-four and period-eight mode-locked orbits, and the dependence of manifold geometry on periodic multipliers. Muni [2] studies hyperchaos and the absorption of unstable invariant objects in the same family. The present claim isolates the *primitive period-two* branch, counts it globally, and gives its precise one-to-two unstable-index threshold, neither asserted in the inspected parts of [1] or [2]. Zheng and collaborators [3] use the sign-reversed parameter convention for the same map and establish instability of period-two points emerging at a fixed-point flip; that near-onset instability is prior work, whereas their theorem does not state the entire spectral phase diagram here. The work of Hampton and Meiss [4] treats a more general three-dimensional quadratic diffeomorphism with differing normal form; its local resonance and bifurcation analysis does not by itself supply the global branch-specific count and index threshold.

## Limitations
The analysis excludes \(b=0\), \(b=1\), and parameter regimes outside \(0<b<1\). It does not classify primitive periods greater than two, basins, attractors, hyperchaotic sets, or a period-four branch at the unit multiplier \(-1\). The exact index crossing alone is not a nonlinear bifurcation nondegeneracy proof. Publication priority is conditional on further comparison with potentially unindexed or inaccessible earlier work, including Richter's foundational 2002 generalization and the full 2017 Zhao–Li–Wang–Feng text; the latter was accessible at abstract/figure-description level only.

## References
[1] S. S. Muni and S. Banerjee, *Bifurcations of mode-locked periodic orbits in three-dimensional maps*, arXiv:2304.10210 (first posted 20 April 2023), Section IV. https://arxiv.org/abs/2304.10210

[2] S. S. Muni, *Pathways to hyperchaos in a three-dimensional quadratic map*, arXiv:2406.08317 (first posted 12 June 2024), Section 2. https://arxiv.org/abs/2406.08317

[3] Y. Zheng et al., *Bifurcations and chaos in a three-dimensional generalized Hénon map*, Advances in Difference Equations (2018), Theorem 4. https://doi.org/10.1186/s13662-018-1622-y

[4] A. E. Hampton and J. D. Meiss, *Visualizing attractors of the three-dimensional generalized Hénon map*, arXiv:2206.07855 (2022). https://arxiv.org/abs/2206.07855

[5] H. Richter, *The generalized Hénon maps: examples for higher-dimensional chaos*, International Journal of Bifurcation and Chaos 12 (2002), 1371–1384, DOI:10.1142/S0218127402005121.
