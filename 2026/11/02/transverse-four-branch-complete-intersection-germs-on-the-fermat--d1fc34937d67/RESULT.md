# Transverse four-branch complete-intersection germs on the Fermat cubic fourfold second-type locus
## Finding
Let \(X=V(\sum_{i=0}^5x_i^3)\subset\mathbf P^5_{\mathbb C}\), let \(F(X)\) be its smooth four-dimensional Fano variety of lines, and let \(S\subset F(X)\) be the **reduced** locus of second-type lines. The reduced singular locus of \(S\), previously identified as \(180\) Fermat elliptic curves meeting in \(405\) special points, has the following precise scheme-theoretic and local structure.

At any point of exactly one of those elliptic curves, the completed local ring of \(S\) is \(\mathbb C[[t,u,v]]/(uv)\). At each of their \(405\) fourfold intersection points, it is
\[
\widehat{\mathcal O}_{S,L}\cong\mathbb C[[C,D,G,H]]/(CG,DH).
\]
The four two-dimensional branches at a fourfold point are smooth, with independent coordinate tangent planes; its four singular curves are the four coordinate axes. Moreover, **the intrinsic singular scheme** of \(S\), defined by \(\operatorname{Fitt}_2\Omega^1_S\), is reduced everywhere and equals the reduced union of those \(180\) elliptic curves. The Hilbert–Samuel multiplicity of \(S\) is \(2\) along a general elliptic singular curve and \(4\) at each of its \(405\) fourfold intersection points. These assertions refine, rather than reprove as new, the earlier set-theoretic component and incidence counts.

## Assumptions and scope
Work over \(\mathbb C\). A line is of second type when its Gauss-map restriction has degree two. The reduced scheme \(S\) is the union of the \(45\) smooth Fermat cubic surfaces and \(10\) smooth products of two Fermat plane elliptic cubics described by Gounelas–Kouvidakis. Every such surface parameterizes lines joining points supported on two disjoint coordinate blocks, respectively \(2+4\) and \(3+3\). By the previous set-theoretic classification of the singular locus, a generic singular line has exactly one identically zero ambient coordinate (actual support sizes \(2+3\)), and a fourfold singular line has exactly two (actual support sizes \(2+2\)); no other singular lines occur. Completed local rings are taken at complex closed points.

## Proof
### 1. The fourfold points and the Fano coordinate chart
By permuting the six ambient coordinates and applying cube-root diagonal automorphisms, every two-zero line is equivalent to the line spanned by
\[
p=(1,-1,0,0,0,0),\qquad q=(0,0,1,-1,0,0).
\]
Near this line, write the spanning vectors of a nearby projective line as
\[
\begin{aligned}
p'&=p+A(1,1,0,0,0,0)+B(0,0,1,1,0,0)+Ce_4+De_5,\\
q'&=q+E(1,1,0,0,0,0)+F(0,0,1,1,0,0)+Ge_4+He_5.
\end{aligned}
\]
The condition that the entire line \(sp'+tq'\) lie on \(X\) is vanishing of the coefficients of \(s^3,s^2t,st^2,t^3\), namely
\[
\begin{aligned}
P_{30}&=2A^3+6A+2B^3+C^3+D^3,\\
P_{21}&=6A^2E+6E+6B^2F+3C^2G+3D^2H,\\
P_{12}&=6AE^2+6BF^2+6B+3CG^2+3DH^2,\\
P_{03}&=2E^3+2F^3+6F+G^3+H^3.
\end{aligned}
\]
The Jacobian of these four polynomials with respect to \((A,E,B,F)\) is diagonal with diagonal entries \(6\) at the origin; its determinant is \(1296\neq0\). The formal implicit-function theorem therefore makes \((C,D,G,H)\) a regular formal parameter system on the smooth Fano fourfold near this line, uniquely determining \((A,E,B,F)\).

### 2. Identifying the four reduced surface branches exactly
The component classification yields exactly four smooth reduced surface components through this line. The cubic-surface component with Eckardt endpoint on coordinates \(0,1\) has \((C,D)=(0,0)\); the one with Eckardt endpoint on \(2,3\) has \((G,H)=(0,0)\). The two product-of-cubics components split the remaining two coordinates as \(\{0,1,4\}|\{2,3,5\}\) or \(\{0,1,5\}|\{2,3,4\}\), and have equations \((D,G)=(0,0)\) and \((C,H)=(0,0)\), respectively. These are exact equations in the formal Fano coordinates, not merely linearized constraints: each condition prescribes the corresponding disjoint coordinate supports, and conversely every line on that support split lies on the appropriate reduced component. All four support-defined families are smooth of dimension two and each occurs once.

Thus the completed ideal of their *reduced* union in \(\mathbb C[[C,D,G,H]]\) is
\[
(C,D)\cap(G,H)\cap(D,G)\cap(C,H)=(CG,DH).
\]
This proves the asserted local-ring model. It is a codimension-two complete intersection with four smooth branches in distinct tangent planes. Its Hilbert–Samuel multiplicity is the product of the two initial quadratic orders, hence \(4\).

### 3. Ordinary points of the elliptic singular curves
At a line with a single zero coordinate, choose its disjoint nonzero support blocks as an Eckardt pair \(P\) and a triple \(Q\), and call the unused coordinate \(z\). Exactly two smooth components contain it: the cubic-surface component corresponding to the fixed pair \(P\), and the product component for the splitting \((P\cup\{z\})|Q\). Their common locus is exactly the smooth Fermat plane cubic obtained by varying the point on \(Q\), with the Eckardt endpoint fixed.

At such a line, the tangent space of the smooth fourfold \(F(X)\) has four independent deformations: moving the fixed Eckardt endpoint into \(z\), moving the triple endpoint into \(z\), moving the Eckardt endpoint transversely into the \(Q\)-block, and moving the \(Q\)-endpoint along its Fermat cubic. This follows directly by linearizing the four cubic coefficients of a line on \(X\); the two \(z\)-deformations are independent because the defining equation is cubic in \(z\). The tangent planes of the two surface components are spanned, respectively, by (\(Q\)-elliptic, \(Q\)-endpoint-into-\(z\)) and (\(Q\)-elliptic, Eckardt-endpoint-into-\(z\)). Their intersection is the tangent line to the smooth elliptic common curve and their span has dimension three. Formal straightening of two smooth surfaces meeting cleanly along a smooth curve now identifies their reduced union with
\[
\mathbb C[[t,u,v,w]]/(w,uv)\cong\mathbb C[[t,u,v]]/(uv).
\]
This gives multiplicity \(2\). Everywhere else \(S\) is contained in exactly one of its smooth components, so \(S\) is smooth there.

### 4. The intrinsic singular scheme is reduced
At a fourfold point, the Jacobian matrix of \((CG,DH)\) with respect to \((C,D,G,H)\) is
\[
\begin{pmatrix}G&0&C&0\\0&H&0&D\end{pmatrix}.
\]
The singular subscheme of the two-dimensional complete intersection is defined by the \(2\times2\) minors, together with the defining equations. Its ideal in the regular ambient ring is
\[
(CG,DH,CD,CH,DG,GH),
\]
which is the squarefree ideal of the four coordinate axes, hence radical. At an ordinary double-curve point the intrinsic singular ideal in \(\mathbb C[[t,u,v]]/(uv)\) is \((u,v)\), again radical and defining the smooth common curve. Away from the singular curves the singular ideal is the unit ideal. Since reduction may be checked locally, \(\operatorname{Fitt}_2\Omega^1_S\) is globally radical and its subscheme is precisely the previously classified reduced union of \(180\) elliptic curves. At each fourfold point the four curve branches have independent tangent directions.

## Verification
Run `python verify_local.py` with Python 3 and SymPy. It re-expands the four coefficients \(P_{ij}\), checks their implicit-function Jacobian determinant \(1296\), checks the exact intersection-of-four-primes identity \((CG,DH)\), verifies radicality of the singular ideal and multiplicity \(4\), and rechecks the finite component/incidence arithmetic. An actual local run printed `FERMAT_SECOND_TYPE_LOCAL_AND_INCIDENCE_EXACT_OK`. The infinite conclusions follow from the formal implicit-function argument, exact support classification, clean-intersection argument, and commutative algebra—not from finite enumeration.

## Relationship to prior work
Gounelas and Kouvidakis (2023) identified the entire reduced second-type locus and its \(45+10\) smooth irreducible components. A separate earlier published result identified its reduced *set-theoretic* singular locus as \(180\) Fermat elliptic curves with \(405\) intersection points, and explicitly left the local analytic equations and transversality undetermined. The present result supplies those missing local germs and the **scheme-theoretic** radicality of the intrinsic singular ideal. Set-theoretic incidence and smoothness of separate components do not imply these assertions: distinct smooth components can be tangent or can induce a nonreduced singular scheme.

## Limitations
This treats only \(S=F_2(X)_{\mathrm{red}}\) over the complex numbers and the *intrinsic* singular scheme \(\operatorname{Fitt}_2\Omega^1_S\). It does not assert a new description of the potentially different original defining determinantal scheme or of the Hilbert schemes of pairs of lines. It does not determine arbitrary global Hilbert polynomials or intersection-theoretic cycles. Historical literature searches do not certify absolute novelty; earlier unindexed treatments may exist. No independent mathematical audit has been performed.

## References
1. F. Gounelas and A. Kouvidakis, *The Fermat cubic and monodromy of lines*, arXiv:2302.09562v1 (first public 19 February 2023), especially §3, https://arxiv.org/abs/2302.09562.
2. *Higher triple lines are the reduced second-type singular locus on the Fermat cubic fourfold*, public mathematical research result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-higher-triple-lines-are-the-reduced-second-type-singular-locus-o--690e72184126.
3. Y. Zhang, *Hilbert Scheme of a Pair of Skew Lines on Cubic Hypersurfaces*, arXiv:2501.01682v1 (3 January 2025), https://arxiv.org/abs/2501.01682.
4. F. Gounelas, *The universal cover of the second-type locus of a cubic*, arXiv:2608.08909 (9 August 2026), https://arxiv.org/abs/2608.08909.
