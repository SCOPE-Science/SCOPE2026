# Minimum genus of trisections on a \(\Lambda_2\)-polarized K3 surface

## Finding

Let \(X\) be a complex K3 surface with full Néron–Severi lattice \(\operatorname{NS}(X)=\Lambda_2=U\oplus\langle-4\rangle\), equipped with an elliptic fibration whose fiber class is \(F\) and whose section is \(O\). Choose \(G\) orthogonal to \(F,O\) with \(G^2=-4\). Every irreducible curve \(C\subset X\) satisfying \(F\cdot C=3\) has arithmetic genus \(p_a(C)\ge8\). The bound is sharp: \(D=6F+3O+G\) is nef and basepoint-free, \(D^2=14\), and a general member of \(|D|\) is a smooth genus-eight trisection. Hence the minimum geometric genus of a smooth degree-three multisection is exactly \(8\).

## Assumptions and scope

The statement assumes that the *full* Néron–Severi lattice is exactly \(\Lambda_2\), with the displayed hyperbolic-plane summand realized by the fiber and section. The intersection products are \(F^2=0\), \(O^2=-2\), \(F\cdot O=1\), \(F\cdot G=O\cdot G=0\), and \(G^2=-4\). A trisection means an irreducible curve \(C\) with \(F\cdot C=3\). The lower bound is on arithmetic genus for integral curves, so it also bounds the genus of every smooth trisection.

## Proof

**No reducible fibers and a family of sections.** A vertical irreducible component has intersection zero with \(F\), hence class \(aF+cG\) and square \(-4c^2\). A component of a reducible fiber would be a \((-2)\)-curve by adjunction, which is impossible in this lattice. Thus all fibers are irreducible. For every integer \(w\), put \(S_w=2w^2F+O+wG\). Then \(S_w^2=-2\) and \(F\cdot S_w=1\). Riemann–Roch on a K3 surface makes either \(S_w\) or \(-S_w\) effective; nefness of \(F\) rules out \(-S_w\). An effective divisor of fiber degree one has one section as its horizontal component and can differ from it only by whole fibers; its square \(-2\) forces there to be no fiber component. Therefore \(S_w\) is an irreducible section.

**Lower bound.** Write an irreducible trisection as \(C=aF+3O+cG\), with integers \(a,c\). Adjunction gives
\[
C^2=6a-18-4c^2,\qquad p_a(C)=1+\frac{C^2}{2}=3a-8-2c^2,
\]
so \(a=(p_a(C)+8+2c^2)/3\). Since \(C\) and \(S_w\) are distinct irreducible curves, \(C\cdot S_w\ge0\). The intersection matrix gives
\[
C\cdot S_w=a+6w^2-6-4cw
=\frac{p_a(C)-10}{3}+6\left(w-\frac c3\right)^2.
\]
Choose an integer \(w\) nearest to \(c/3\), so \(|w-c/3|\le1/3\). Then
\[
0\le C\cdot S_w\le\frac{p_a(C)-10}{3}+\frac23
=\frac{p_a(C)-8}{3},
\]
which forces \(p_a(C)\ge8\).

**Sharpness.** Let \(D=6F+3O+G\). Then \(F\cdot D=3\), \(O\cdot D=0\), and \(D^2=14\). To show that \(D\) is nef, take an irreducible curve \(\Gamma\). If \(F\cdot\Gamma=0\), it is a fiber and \(D\cdot\Gamma=3\). If \(\Gamma^2\ge0\) and \(F\cdot\Gamma>0\), the positive-cone criterion gives \(D\cdot\Gamma>0\). Otherwise \(\Gamma^2=-2\); write \(\Gamma=aF+vO+wG\), where \(v=F\cdot\Gamma\ge1\). The root equation gives \(a=v+(2w^2-1)/v\), hence
\[
v(D\cdot\Gamma)=3v^2+6w^2-3-4vw
=(v^2-1)+2(v-w)^2+4w^2-2\ge0.
\]
For \(w=0\), the right side is \(3v^2-3\ge0\); for \(|w|\ge1\), it is positive. Thus \(D\) is nef and big.

The only fixed-component obstruction in the standard basepoint-free criterion for a nef and big K3 divisor would require an isotropic class \(E=uF+vO+wG\) with \(D\cdot E=1\). That equation gives \(u=(1+4w)/3\). If \(w=0\), this is not integral. If \(w\ne0\), then \(u^2/4=(1+4w)^2/36<2w^2\), contradicting \(E^2=0\), which requires \(v(u-v)=2w^2\le u^2/4\). The obstruction is absent, so \(|D|\) is basepoint-free. Since \(D^2>0\), a general member is smooth and irreducible. Adjunction gives genus \(1+D^2/2=8\), and its intersection with \(F\) is \(3\). This attains the lower bound.

## Verification

The lower bound follows from the displayed intersection matrix and the explicit family of sections \(S_w\); the nearest-integer estimate is exact. The sharpness argument checks nefness against vertical curves, classes of nonnegative square, and every \((-2)\)-class, then applies the standard K3 basepoint-free criterion. No finite search or numerical approximation is involved.

## Relationship to prior work

The recent paper *Rank jumps and multisections of elliptic fibrations on K3 surfaces* studies the family \(\Lambda_d=U\oplus\langle-2d\rangle\), including the exclusion of smooth genus-zero and genus-one multisections for \(d\le3\). The inspected statement does not give a lower bound for all degree-three multisections on \(\Lambda_2\), nor the sharp genus-eight construction. This result concerns the minimum genus of trisections rather than the existence of rational or genus-one multisections.

## Limitations

The result is specific to the exact lattice \(\Lambda_2\) and the given elliptic fibration. It need not persist after specialization to a K3 surface with a larger Néron–Severi lattice, where additional vertical roots or sections may occur. It does not classify multisections of other degrees or all genera above \(8\).

## References

- *Rank jumps and multisections of elliptic fibrations on K3 surfaces*, arXiv:2505.15159 (first version submitted 21 May 2025).
- B. Saint-Donat, “Projective models of K3 surfaces,” *American Journal of Mathematics* 96 (1974), 602–639.