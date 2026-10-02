# A d-semistability obstruction for a named quintic pencil

## Finding

Consider \(F=x_0q+tq_5\) in \(\mathbb P^4\times\Delta\), where the disc \(\Delta\) includes \(t=0\), and
\[
q=\sum_{i=0}^4x_i^4+x_0x_1^3+x_0x_2^3,
\qquad q_5=\sum_{i=0}^4x_i^5+x_0^3x_1^2.
\]
Its central fiber is \(H\cup Q\), with \(H=\{x_0=0\}\), \(Q=\{q=0\}\). Both components are smooth and meet transversely in a smooth quartic K3 surface \(S\). Over the central fiber the total-space singular locus is exactly
\[
C=S\cap\{q_5=0\},
\]
a nonempty smooth complete-intersection curve of degree \(20\) and genus \(51\). Furthermore
\[
N_{S/H}\otimes N_{S/Q}=\mathcal O_S(5)\ne\mathcal O_S.
\]
Thus the bare central fiber is not d-semistable and is not the central fiber of a semistable smoothing with smooth total space. A bare-triple Clemens–Schmid calculation cannot be applied to this presentation without modifying the degeneration.

## Assumptions and scope

All geometry is over \(\mathbb C\). The assertion about the total-space singular locus is restricted to its intersection with \(t=0\); no assertion about all singular fibers away from zero is needed. Semistable means a smooth total space with a reduced simple-normal-crossing central fiber. No monodromy weight table or Abel–Jacobi nonsplitting is inferred from this obstruction.

## Proof

The derivatives of \(q\) are
\[
q_{x_0}=4x_0^3+x_1^3+x_2^3,
\quad q_{x_1}=x_1^2(4x_1+3x_0),
\quad q_{x_2}=x_2^2(4x_2+3x_0),
\quad q_{x_3}=4x_3^3,\quad q_{x_4}=4x_4^3.
\]
If \(x_0=0\), their simultaneous vanishing is impossible projectively. If \(x_0\ne0\), scale to \(x_0=1\); then \(x_3=x_4=0\) and \(x_1,x_2\in\{0,-3/4\}\). The remaining derivative is one of \(4,229/64,101/32\), none zero. Thus \(Q\) is smooth.

On \(H\), the equation of \(S\) is \(\sum_{i=1}^4x_i^4=0\). Its gradient never vanishes projectively; adjunction identifies this smooth quartic as a K3 surface. The nonzero gradient along \(H\) also proves transversality with \(Q\).

At \(t=0\),
\[
dF=q\,dx_0+x_0\,dq+q_5\,dt.
\]
Outside \(S\), smoothness of the relevant component makes the spatial differential nonzero. On \(S\), this is \(q_5dt\), proving the asserted central singular locus.

The curve is the intersection in \(\mathbb P^3\) of \(\sum x_i^4=0\) and \(\sum x_i^5=0\). If their gradients were dependent, some \((a,b)\ne(0,0)\) would satisfy
\[
4ax_i^3+5bx_i^4=0\quad\text{for all }i.
\]
For \(b=0\) every coordinate vanishes. Otherwise every nonzero coordinate equals \(c=-4a/(5b)\). If \(k\) coordinates are nonzero, the quartic equation becomes \(kc^4=0\), impossible in characteristic zero. The intersection is therefore smooth of codimension two at all its points. It is nonempty: choose \(\zeta^4=-1\), and the exact point
\[
(1:\zeta:-1:-\zeta)
\]
satisfies both equations. Bézout and adjunction give
\[
\deg C=4\cdot5=20,\qquad K_C=\mathcal O_C(4+5-4)=\mathcal O_C(5),
\qquad 2g-2=5\cdot20=100.
\]
Hence \(g=51\). There is no extra subtraction by one inside the degree formula.

Since \(S\) is a quartic divisor in \(H\) and a hyperplane divisor in \(Q\), the two normal bundles are \(\mathcal O_S(4)\) and \(\mathcal O_S(1)\). Their tensor product is \(\mathcal O_S(5)\). It is nontrivial, for its first Chern class has positive intersection with the hyperplane class: \(5\cdot4=20\). The necessary d-semistability condition for a two-component smooth-total-space semistable degeneration requires this product to be trivial. It fails here.

## Verification

The smoothness cases, exact nonempty point, adjunction calculation and normal-bundle degrees are established symbolically above; no approximate root or numerical residual is needed. The original `artifacts/verify_C_point.py` remains historical corroboration, not the basis for nonemptiness. All current paths refer to the actual package layout, not an `output/` prefix.

## Relationship to prior work

Friedman's d-semistability criterion and the Tyurin-degeneration literature provide the general obstruction. They do not state the explicit Jacobian and singular-curve calculation for this named pencil. The useful boundary is that a smooth transverse pair by itself does not supply a smooth-total-space semistable model. This does not claim a new general smoothing theorem or a disproof of a weight table after semistable reduction.

## Limitations

The result neither constructs semistable reduction nor determines the limiting Hodge filtration, monodromy or proposed weight dimensions. Modifying the total space or central fiber can remove the obstruction; no obstruction to every modified smoothing is asserted. General-fiber smoothness in a whole punctured disc is not established or used here.

## References

- R. Friedman, *Global smoothings of varieties with normal crossings*, necessary d-semistability condition.
- Y. Kawamata and Y. Namikawa, *Logarithmic deformations of normal crossing varieties and smoothing of degenerate Calabi–Yau varieties*, DOI:10.1007/BF01231538.
- C. Doran, A. Harder and A. Thompson, *Mirror symmetry, Tyurin degenerations and fibrations on Calabi–Yau manifolds*, arXiv:1601.08110. https://arxiv.org/html/1601.08110
