# Sharp isodiametric duality and discontinuous Chebyshev centers of rectangular flat Möbius bands

## Finding

For the rectangular flat Möbius band \(M_{L,w}=(\mathbb R\times[-w,w])/\langle(x,y)\mapsto(x+L,-y)\rangle\), let \(e(u)\) be the intrinsic eccentricity of a point at absolute transverse coordinate \(u\in[0,w]\): the largest distance from it to any point of the band. For \(c=L^2/4\) this profile is
\[
e(u)=\begin{cases}
\sqrt{c+w^2+(1+w^2/c)u^2},&uw\le c,\\
\max\{u+c/u,\sqrt{L^2+(w-u)^2}\},&uw\ge c.
\end{cases}
\]
Consequently the **intrinsic Chebyshev radius**, \(R=\min_u e(u)\), has a transition at \(w_c=7\sqrt{15}L/30\):
\[
R=\begin{cases}
\sqrt{L^2/4+w^2},&w\le w_c,\\
(3\sqrt{w^2+2L^2}-w)/4,&w\ge w_c.
\end{cases}
\]
Below \(w_c\) the center set is the core circle. Above \(w_c\) it is the circle at \(|y|=(w+\sqrt{w^2+2L^2})/4\). At \(w_c\) both circles minimize; the positive center coordinate there is \(\sqrt{15}L/6\). The radius is continuous and equals \(4L/\sqrt{15}\) at the transition; its left and right derivatives in \(w\) at fixed \(L\) are \(7/8\) and \(2/13\).

**Diameter comparison.** The diameter and the sharp diameter–area comparison below are consequences of the earlier full distance law [1], so they are included for comparison, not as independent contributions. For \(r=2w/L\) and area \(S=2wL\),
\[
D=\frac{L(1+r^2)}{2\max\{1,r\}},\qquad
\frac{D^2}{S}=F(r):=\frac{(1+r^2)^2}{4r\max\{1,r\}^2},\qquad F(r)=F(1/r)\ge \frac{4\sqrt3}{9}.
\]
Reciprocity is a symmetry of the dimensionless profile, not an isometry. Equality holds at \(r=1/\sqrt3\) and \(r=\sqrt3\), giving two nonisometric bands at any fixed area. The diameter branch changes at \(r=1\), unlike the Chebyshev center transition at \(r=7/\sqrt{15}\).

## Assumptions and scope

Take \(L,w>0\). All distances are intrinsic in the compact flat length-metric quotient, including its single boundary circle. The two parallel edges of the covering strip project to that boundary. The theorem concerns neither extrinsic embeddings nor optimization over arbitrary Riemannian or Finsler metrics. Translation and reflection let the source be represented by \((0,u)\) with \(0\le u\le w\).

## Proof

**Pointwise eccentricity.** For a target represented by \((t,v)\), \(0\le t\le L\), the two nearest deck images, one for each parity, give the squared distance
\[
\min\{t^2+(v-u)^2,(L-t)^2+(v+u)^2\}.
\]
The minimizing straight segment lies in the convex covering strip. The symmetry \((t,v)\mapsto(L-t,-v)\) preserves the displayed minimum, so maximize using \(0\le v\le w\). At fixed \(v\), the first term increases in \(t\) and the second decreases. Their minimum is largest at the crossing \(t=L/2+2uv/L\) if it falls in \([0,L]\), and otherwise at \(t=L\). Thus the maximum over \(t\) is \(c+u^2+(1+u^2/c)v^2\) for \(uv\le c\), and \(L^2+(v-u)^2\) for \(uv\ge c\). The first expression increases in \(v\); the second is convex in \(v\). When \(uw\le c\), take \(v=w\). When \(uw>c\), take the larger of the values at \(v=c/u\) and \(v=w\). At \(v=c/u\) the value is \((u+c/u)^2\). This proves the profile, including the equality where its pieces meet.

**Chebyshev centers.** If \(w\le L/2\) the first piece suffices and is minimized only at \(u=0\). If \(w>L/2\), put \(u_0=c/w\). The first piece increases to \(u_0\). On the remaining interval write \(A=u+c/u\) and \(B=\sqrt{L^2+(w-u)^2}\). The identity
\[
A^2-B^2=(2u-w-c/u)(w-c/u)
\]
shows that \(B\) is active from \(u_0\) to the positive root \(u_*=(w+\sqrt{w^2+2L^2})/4\) of \(2u^2-wu-c=0\), and \(A\) from \(u_*\) to \(w\). Indeed \(w-c/u>0\) for \(u>u_0\), and evaluating the quadratic at \(L/2\) and \(w\) shows that \(L/2<u_*<w\). The \(B\)-piece decreases to \(u_*\); the \(A\)-piece increases after it because \(u_*>L/2\). There are only two candidate minimizers, \(0\) and \(u_*\), with eccentricities \(R_0=\sqrt{c+w^2}\) and \(R_*=3u_*-w=(3\sqrt{w^2+2L^2}-w)/4\). For \(w\ge L/2\), \(R_0'\ge1/\sqrt2\) and \(R_*'<1/2\), so the difference is strictly increasing. Substitution at \(w=w_c\) gives equality with common value \(4L/\sqrt{15}\), \(u_*=\sqrt{15}L/6\), and slopes \(7/8\), \(2/13\). This decides the minimum and the complete locus, including coexistence. In the quotient the two signed levels of a positive \(|y|\) join into a single circle.

**Recovering the diameter comparison from the prior full law.** In [1] use \(C=L\) and \(H=2w\). The diameter is the upper endpoint of the distance distribution because normalized area has full support and distance is continuous. For horizontal separation \(a\in[0,C/2]\) and a test radius \(d\ge C/2\), put \(b=C-a\) and \(U=\sqrt{d^2-a^2}\). If \(d<b\), only the same-parity shortcut condition \(|y-y'|\le U\) is available, requiring \(U\ge H\) for saturation. If \(d\ge b\), the two thresholds are \(U\) for \(|y-y'|\) and \(V=\sqrt{d^2-b^2}\) for \(|y+y'|\). Since the feasible pair of absolute values is the triangle with sum at most \(H\), the law saturates there exactly when \(U+V\ge H\). The same conditions follow from the integrands in [1]. For \(C/2\le d<C\) the smallest threshold occurs at \(a=C-d\): \(U\) decreases before that point, while \(U+V\) increases afterward since \(b/V\ge a/U\). Thus saturation requires \(\sqrt{2Cd-C^2}\ge H\). For \(d\ge C\) the two terms are available throughout and their smallest sum occurs at \(a=0\), requiring \(d+\sqrt{d^2-C^2}\ge H\). These yield \(D=(C^2+H^2)/(2\max\{C,H\})\), which also follows from maximizing the pointwise profile above. At \(0<r\le1\), four times its normalized square is \(r^{-1}+2r+r^3\); the unique critical minimum solves \(-r^{-2}+2+3r^2=0\), at \(r=1/\sqrt3\). Reciprocity gives the other minimizer and the bound. The two ratios at fixed area have different \(L\) and therefore different systoles: any noncontractible loop has a longitudinal lift displacement of magnitude at least \(L\), achieved by the core.

## Verification

The supplied `verify.py` can be run with Python 3 using the standard library. Its distance samples, explicit maximizing targets, and radius and diameter checks are finite corroboration. The profile and continuum minimization follow from the algebraic proof above.

## Relationship to prior work

The complete area-uniform distance law [1] gives the global support endpoint after the above calculation, but averaging over sources does not give the eccentricity conditional on the source position or identify the minimizing source locus. The exact geodesic dispersion record [2] optimizes a mean squared distance, not that conditional minimax. The related two-point ordering [3] likewise compares distribution functions, not the set of centers. The later catalogue result [4] gives the same pointwise profile, radius and center transition in width/circumference notation and additionally classifies diametral pairs. This is overlap in mathematical content, not evidence of earlier priority. The classical systolic work [5, 6] compares lengths of noncontractible loops and transverse curves with area or volume. Sabitov [7] studies isometric embeddings and immersions; the inspected abstract does not address the intrinsic minimax. No exhaustive historical priority is claimed.

## References

1. [*Distance statistics detect the half-twist of a flat Möbius band*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-distance-statistics-detect-the-half-twist-of-a-flat-m-bius-band--cbaf47596178), Finding and quotient metric derivation, 2026-10-25.
2. [*Exact geodesic dispersion and unique area-constrained optimum of flat Möbius bands*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-geodesic-dispersion-and-unique-area-constrained-optimum-of--8010a90e7384), Finding.
3. [*A complete two-point distance ordering for the flat Möbius band and its matched cylinder*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-complete-two-point-distance-ordering-for-the-flat-m-bius-band--d61dc15f6cd5), Finding.
4. [*A boundary-to-interior farthest-point transition and two center phases on flat Möbius bands*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-boundary-to-interior-farthest-point-transition-and-two-center--7e805c97530c), Finding, 2026-11-22.
5. C. Blatter, [*Zur Riemannschen Geometrie im Grossen auf dem Möbiusband*](https://www.numdam.org/item/CM_1962-1964__15__88_0/), Compositio Mathematica **15**, 88–107.
6. S. Sabourau and Z. Yassine, [*Optimal systolic inequalities on Finsler Möbius bands*](https://arxiv.org/abs/1503.01282), arXiv:1503.01282.
7. I. Kh. Sabitov, [*Isometric immersions and embeddings of a flat Möbius strip in Euclidean spaces*](https://doi.org/10.1070/IM2007v071n05ABEH002376), Izvestiya: Mathematics **71** (2007), 1049–1078.
