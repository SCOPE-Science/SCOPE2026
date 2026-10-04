# Exact isotropic-dilation window for zero-energy contact in the anisotropic hexagonal minus-R lattice
## Finding
Fix positive shape lengths \(A,B,C\). In the periodic hexagonal metric graph with the negative-\(R\) preferred-orientation coupling of Exner--Pekař, normalize the coupling length to one and set
\[
a=sA,\qquad b=sB,\qquad c=sC,\qquad s>0.
\]
Let
\[
x=A^{-1},\qquad y=B^{-1},\qquad z=C^{-1}.
\]
Define
\[
s_+^2=4(xy+xz+yz)
\]
and
\[
s_-^2=\begin{cases}
4xyz/\max\{x,y,z\},&x+y+z\le 2\max\{x,y,z\},\\
2(xy+xz+yz)-(x^2+y^2+z^2),&x+y+z\ge 2\max\{x,y,z\}.
\end{cases}
\]
At equality in the reciprocal triangle condition, the two formulas for \(s_-\) coincide.

The positive absolutely-continuous spectrum accumulates at zero exactly when
\[
s_-\le s<s_+.
\]
Hence there is no open spectral gap about zero exactly on this half-closed interval. For \(0<s<s_-\) and for \(s\ge s_+\), the spectrum has an open gap about zero. In particular, the lower critical scale is gapless but the upper critical scale is gapped.

The window has a universal shape constraint,
\[
\frac{s_+}{s_-}\ge 2,
\]
with equality if and only if \(A=B=C\). In the reciprocal-nontriangle regime the stronger estimate
\[
\frac{s_+}{s_-}\ge\sqrt5
\]
holds. Thus the equilateral cell is the unique shape with the narrowest multiplicative isotropic-dilation window for zero-energy contact.

## Assumptions and scope
The graph, Bloch phases, negative-\(R\) vertex condition, and coupling-length normalization are those of arXiv:2409.03538v1. The statement concerns uniform dilation of a fixed positive shape \((A,B,C)\); it does not alter the vertex coupling while \(s\) varies. The conclusion is about spectral contact at energy zero and an open neighborhood of zero, not about the high-energy gap distribution or flat-band commensurability.

The source derives the exact Bloch spectral condition and its order-\(k^3\) low-energy coefficient. It gives strict sufficient band conditions for general unequal lengths but does not settle the critical equalities. The endpoint assertions here require the order-\(k^5\) coefficient of the exact spectral determinant.

## Proof
Write the exact determinant condition from Eq. (19) of the source as \(F(k,\theta_1,\theta_2;a,b,c)=0\). Direct Taylor expansion of that exact finite trigonometric expression gives
\[
F=k^3\bigl(G(\theta_1,\theta_2)+k^2H(\theta_1,\theta_2)+O(k^4)\bigr),
\]
uniformly on the compact Bloch torus, where
\[
G=abc-2(a+b+c)-2f,
\qquad
f=a\cos(\theta_2-\theta_1)+b\cos\theta_2+c\cos\theta_1.
\]
This is the source's Eq. (22), multiplied by \(-1\), which leaves its zero set unchanged.

For a fixed shape under \(a=sA\), \(b=sB\), \(c=sC\), divide \(G\) by \(s\). The maximum of \(f/s\) is \(A+B+C\), attained at \((\theta_1,\theta_2)=(0,0)\). The source's minimization lemma gives the two cases
\[
\min \frac{f}{s}=-(A+B+C)+2\min\{A,B,C\}
\]
when \(x+y+z\le2\max\{x,y,z\}\), and
\[
\min \frac{f}{s}=-\frac{ABC}{2}(x^2+y^2+z^2)
\]
when \(x+y+z\ge2\max\{x,y,z\}\). Therefore the two sign-change scales of \(G\) are exactly the displayed \(s_-\) and \(s_+\). For \(s_-<s<s_+\), \(G\) has both signs on the Bloch torus, so for every sufficiently small \(k>0\), continuity in the Bloch phases gives a zero of \(F\). For \(s<s_-\) or \(s>s_+\), \(G\) has a uniform nonzero sign, so no sufficiently small positive \(k\) is spectral.

It remains to resolve the two critical scales, where the cubic coefficient vanishes at an extremizing Bloch phase.

At the upper critical scale, \(abc=4(a+b+c)\) and the only maximum phase is \((0,0)\). Put \(X=a^{-1}\), \(Y=b^{-1}\), \(Z=c^{-1}\), \(e_1=X+Y+Z\), and \(e_3=XYZ\). The critical relation is \(XY+XZ+YZ=1/4\). The fifth-order coefficient at the maximum phase simplifies exactly to
\[
H(0,0)=\frac{e_1-12e_3}{12e_3^2}>0.
\]
Indeed, Cauchy's inequality gives
\[
(X+Y+Z)(XY+XZ+YZ)\ge 9XYZ,
\]
so \(e_1\ge36e_3\). At the same time, \(G=2(a+b+c-f)\ge0\). Near \((0,0)\), continuity keeps \(H\) positive, while away from that phase \(G\) has a positive uniform lower bound. Hence \(F\) has one sign for all sufficiently small \(k>0\): the upper endpoint \(s=s_+\) is gapped.

At the lower critical scale, \(G=2(f_{\min}-f)\le0\), with equality at a minimizing phase. We show that \(H>0\) at such a phase, forcing a sign change of \(F\) between the minimizer and any fixed nonminimizing phase for every sufficiently small \(k>0\).

In the reciprocal-nontriangle case, suppose without loss of generality that \(a=\min\{a,b,c\}\). A minimizing phase is \((\pi,\pi)\), the critical relation is \(bc=4\), and direct simplification of the fifth-order coefficient gives
\[
H(\pi,\pi)=\frac{a}{3}\bigl(b^2+c^2+3a(b+c)\bigr)>0.
\]

In the reciprocal-triangle case, let \(X=a^{-1}\), \(Y=b^{-1}\), \(Z=c^{-1}\). The lower critical relation is
\[
2(XY+XZ+YZ)-(X^2+Y^2+Z^2)=1.
\]
At a minimizing phase the three relevant cosines are
\[
\cos(\theta_2-\theta_1)=\frac{X^2-Y^2-Z^2}{2YZ},
\]
\[
\cos\theta_2=\frac{Y^2-X^2-Z^2}{2XZ},
\qquad
\cos\theta_1=\frac{Z^2-X^2-Y^2}{2XY}.
\]
With \(e_1=X+Y+Z\) and \(e_3=XYZ\), substitution into the exact fifth-order coefficient yields
\[
H_{\min}=\frac{(e_1-6e_3)(e_1^2+1)}{6e_3^2}.
\]
The reciprocal triangle can be parameterized by \(X=p+q\), \(Y=q+r\), \(Z=r+p\) with \(p,q,r\ge0\). The critical relation becomes \(4(pq+pr+qr)=1\). Since
\[
XYZ=(p+q+r)(pq+pr+qr)-pqr,
\]
one obtains
\[
e_1-6e_3=\frac{p+q+r}{2}+6pqr>0.
\]
Thus \(H_{\min}>0\), proving that the lower endpoint \(s=s_-\) is gapless. The source states that when the positive spectrum does not extend to zero, the negative side also leaves a gap there; consequently the positive-side classification above is exactly the classification of open gaps about energy zero.

Finally, the width bound is intrinsic to shape. In the reciprocal-triangle case put \(Q=xy+xz+yz\) and \(R=x^2+y^2+z^2\). Then
\[
s_+^2-4s_-^2=4(R-Q)=2\bigl((x-y)^2+(y-z)^2+(z-x)^2\bigr)\ge0,
\]
with equality exactly at \(x=y=z\). In the reciprocal-nontriangle case assume \(x=\max\{x,y,z\}\), so \(x\ge y+z\). Then
\[
\frac{s_+^2}{s_-^2}=\frac{x(y+z)+yz}{yz}
\ge \frac{(y+z)^2+yz}{yz}
=3+\frac{y}{z}+\frac{z}{y}\ge5.
\]
This proves both multiplicative-width assertions.

## Verification
The algebraic proof is independent of numerical experiments. The accompanying `verify.py` evaluates the exact determinant, the critical-scale formulas, and the predicted sign patterns for representative reciprocal-triangle, reciprocal-nontriangle, and equilateral shapes. It also checks the factor-two and \(\sqrt5\) width inequalities over a deterministic grid. These computations corroborate the formulas but are not used as a substitute for the analytic proof.

## Relationship to prior work
Exner--Pekař derive the exact determinant for the negative-\(R\) hexagonal lattice and its low-energy cubic coefficient. For unequal lengths they state strict inequalities, Eqs. (23)--(24), ensuring that the positive spectrum extends to zero. Their equilateral analysis separately gives the special interval \(\sqrt3\le l<2\sqrt3\), thereby showing that critical endpoints can matter. The present result resolves both critical endpoints for every positive anisotropic shape, organizes the source inequalities into an exact isotropic-dilation phase diagram, and proves a shape-optimality law for the multiplicative window.

Exner--Turek study geometrically dilated honeycomb graphs with \(\delta\)-type coupling. Their model has a different vertex condition and its near-zero gap criteria depend on the \(\delta\)-coupling strength; it does not imply the negative-\(R\) critical endpoint classification. Exner--Tater study the original preferred-orientation \(R\) coupling on equilateral square and hexagonal lattices, rather than the anisotropic negative-\(R\) family considered here.

## Limitations
The theorem concerns isotropic scaling of a fixed shape while the coupling length is held fixed. It does not classify arbitrary paths in the full three-parameter space \((a,b,c)\), does not quantify the size of the opened energy gap away from the transition scales, and does not address high-energy gap asymptotics. At \(s=s_-\), the theorem asserts accumulation of the positive spectrum at zero; it does not claim that the negative band also reaches zero there. No independent audit has been performed.

## References
1. P. Exner and J. Pekař, *Spectral properties of hexagonal lattices with the \(-R\) coupling*, arXiv:2409.03538v1 (first public 2024-09-05), especially Eqs. (19), (22)--(24) and Secs. 4.2--4.3.
2. P. Exner and O. Turek, *Spectrum of a dilated honeycomb network*, arXiv:1405.0694v1; Integral Equations and Operator Theory 81 (2015), 535--557.
3. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664v1; Physics Letters A 382 (2018), 283--287.
