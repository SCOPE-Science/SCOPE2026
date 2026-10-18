# Quadratic rigidity at a rank-two singular Euclidean four-simplex

## Finding
Let the labeled right Euclidean four-simplex be
\[
S_0=\operatorname{conv}\{0,e_1/\sqrt2,e_2/\sqrt2,e_3/\sqrt2,e_4/\sqrt2\}\subset\mathbb R^4.
\]
For a nearby labeled four-simplex, assemble its ten squared edge lengths into a vector \(x\in\mathbb R^{10}\), in lexicographic edge order, and let \(F(x)\in\mathbb R^{10}\) consist of the squared areas of its ten triangular faces in lexicographic triangle order. At \(S_0\), the differential \(DF(x^0)\) has rank exactly eight, so there are two independent nontrivial infinitesimal variations that preserve every triangular face area to first order. Nevertheless, the fiber \(F^{-1}(F(x^0))\) is locally the single point \(x^0\). More precisely, there exist \(c>0\) and \(\rho>0\) such that every realizable squared-edge vector with \(\|x-x^0\|_2<\rho\) satisfies
\[
\|F(x)-F(x^0)\|_2\ge c\|x-x^0\|_2^2.
\]
The exponent \(2\) in this lower growth law is optimal: no exponent smaller than \(2\) can replace it with a positive uniform constant near \(x^0\). Equivalently, the inverse stability exponent \(1/2\) is sharp. Hence no nontrivial continuous deformation through \(S_0\) preserves all ten labeled triangle areas, despite its two-dimensional infinitesimal kernel.

## Assumptions and scope
The vertices are distinctly labeled \(0,1,2,3,4\). Euclidean congruence includes reflections; there is no quotient by relabeling. Each squared edge length is \(x_{ij}=\|v_i-v_j\|^2\) for \(0\le i<j\le4\). The coordinate order is
\[
(01,02,03,04,12,13,14,23,24,34).
\]
The triangular face order is
\[
(012,013,014,023,024,034,123,124,134,234).
\]
At the indicated simplex, \(x^0_{0i}=1/2\) and \(x^0_{ij}=1\) when \(1\le i<j\le4\). Its Gram matrix based at vertex \(0\) is \(I_4/2\). Since positive definiteness is open, all sufficiently small perturbations of the ten coordinates are realized by nondegenerate Euclidean four-simplices. In fact, given \(x\), the Gram matrix is \(G_{ii}=x_{0i}\) and \(G_{ij}=(x_{0i}+x_{0j}-x_{ij})/2\) for \(i\ne j\). The result concerns this local Euclidean domain, not arbitrary pseudo-Euclidean simplices or global uniqueness of every fiber.

## Proof
For three distinct labels \(i<j<k\), abbreviate \(u=x_{ij}\), \(v=x_{ik}\), and \(w=x_{jk}\). Heron's identity in squared-distance form yields the exact polynomial
\[
F_{ijk}(x)=\frac{2(uv+vw+wu)-u^2-v^2-w^2}{16}.
\]
At \(x=x^0\), the six faces containing vertex \(0\) have squared area \(1/16\), and the four faces not containing vertex \(0\) have squared area \(3/16\). This is a degree-two polynomial map defined on an open neighborhood of \(x^0\).

Write \(J=DF(x^0)\). In the stated edge order define
\[
U=(0,0,0,0,0,1,-1,-1,1,0)^T,
\qquad V=(0,0,0,0,1,0,-1,-1,0,1)^T.
\]
In the stated triangle order define
\[
A=(0,1,-1,-1,1,0,0,0,0,0)^T,
\qquad B=(1,0,-1,-1,0,1,0,0,0,0)^T.
\]
Direct differentiation of the displayed polynomial shows \(JU=JV=0\) and \(A^TJ=B^TJ=0\). The submatrix of \(J\) with zero-based row indices \((0,1,2,3,6,7,8,9)\) and column indices \((0,1,2,3,4,5,6,7)\) has determinant \(-1/4194304\). Therefore \(\operatorname{rank}J=8\); \(U,V\) form a basis of its kernel, and \(A,B\) form a basis of its left kernel.

The critical nonlinear obstruction is exact, not asymptotic. For all real \(s,t\), the two left-kernel projections satisfy
\[
\begin{aligned}
A^T(F(x^0+sU+tV)-F(x^0))&=\frac{t(2s+t)}8,\\
B^T(F(x^0+sU+tV)-F(x^0))&=\frac{s(s+2t)}8.
\end{aligned}
\]
A sum-of-squares identity gives
\[
\left(\frac{t(2s+t)}8\right)^2+
\left(\frac{s(s+2t)}8\right)^2
=\frac{(s^2+t^2)^2}{192}+
\frac{(s^2+3st+t^2)^2}{96}
\ge\frac{(s^2+t^2)^2}{192}.
\]
Thus the projected homogeneous quadratic map has no nonzero real zero and has a uniform quadratic lower bound on the two-dimensional kernel.

For clarity, this quadratic obstruction implies the asserted **full** local stability, even when perturbations are not in the kernel. Decompose each displacement \(h=x-x^0=z+w\) with \(z\in\ker J\) and \(w\) in a fixed complementary subspace. Let \(H(h)=F(x^0+h)-F(x^0)-Jh\); it is a homogeneous quadratic map. Suppose no positive constant \(c\) gave the claimed bound. Then there would be a sequence of nonzero \(h_\nu\to0\) with \(\|F(x^0+h_\nu)-F(x^0)\|_2=o(\|h_\nu\|_2^2)\). Because \(J\) is injective on the chosen complement, the equality \(Jw_\nu=\Delta F_\nu-H(h_\nu)\) implies \(w_\nu=O(\|h_\nu\|_2^2)\). Thus \(\|z_\nu\|_2/\|h_\nu\|_2\to1\). Applying \(A^T,B^T\) eliminates \(Jw_\nu\); the two resulting expressions equal the kernel quadratics plus \(O(\|h_\nu\|_2^3)\), since the cross terms involving \(w_\nu\) are cubic or higher. But the sum-of-squares lower bound makes the combined kernel quadratic of order at least \(\|z_\nu\|_2^2\), contradicting the assumed little-oh bound. This proves the positive-constant quadratic lower estimate and therefore isolation of the exact fiber.

Finally choose the realizable path \(x(s)=x^0+sU\) with sufficiently small nonzero \(s\). Positive definiteness of its Gram matrix follows by continuity from \(I_4/2\). Along it, \(J U=0\), hence the exact quadratic formula gives \(F(x(s))-F(x^0)=s^2H(U)\), and \(B^TH(U)=1/8\ne0\). Therefore the area-data change has exact order \(s^2\) whereas the squared-edge change has order \(|s|\). This rules out every stronger inverse Hölder exponent above \(1/2\), or equivalently every smaller lower-growth exponent below \(2\).

## Verification
Run `python checker.py` after installing the dependency listed in `requirements.txt`. The checker independently constructs the ten Heron polynomials, recomputes the base values and full Jacobian, verifies the nonzero rank-eight minor and both nullspace bases, evaluates the two projected quadratic expressions symbolically, and checks the exact sum-of-squares identity. It also verifies positive definiteness at two nonzero rational points along the infinitesimal kernel and confirms exact quadratic scaling there. These finite checks independently reproduce the algebraic certificates; the sequential compactness argument above, not finite sampling, proves the local estimate for every sufficiently small perturbation.

## Relationship to prior work
Mohar and Rivin establish algebraic independence of codimension-two face volumes from edge-length data by the nonzero Jacobian at a **regular** simplex, and exhibit a family with nonunique area data (arXiv:0901.3284, 2009, especially the Jacobian and singular-example sections). Their result does not imply local nonsingularity everywhere, nor this rank-two singular right simplex and its obstructing quadratic map. Gaifullin studies polynomial algebraic relations and generic finite fibers for triangular-face areas (arXiv:1310.3417, originally 2013); a generic finite-fiber conclusion does not resolve an explicitly singular Jacobian at this nongeneric shape. Zhang poses the Euclidean continuous rigidity question and constructs **pseudo-Euclidean**, not Euclidean, flexible examples (arXiv:2307.15817, first made public July 28, 2023). The finding above gives one fully solved nongeneric Euclidean test case with two infinitesimal flexes that cannot be integrated, and supplies sharp local inverse stability. It neither settles Zhang's question for all Euclidean four-simplices nor contradicts known discrete nonuniqueness examples.

## Limitations
Local uniqueness is proved only for the indicated labeled right four-simplex, and after similarity normalization its congruent copies. No global classification of other four-simplices with the same face-area data is claimed; a distant noncongruent simplex might have the same ten areas. The existence of positive constants \(c,\rho\), rather than their globally optimal numerical values, is proved. The quadratic lower-growth exponent is optimal, not the unspecified coefficient \(c\). This is a mathematical proof with exact symbolic reproduction but no independent formal or external audit; unseen prior equivalent treatments cannot be excluded absolutely.

## References
- L. Zhang, *Simplices with fixed volumes of codimension 2 faces in a continuous deformation*, arXiv:2307.15817, first submitted 2023-07-28. Sections 1–3 and the Euclidean-versus-pseudo-Euclidean discussion.
- B. Mohar and I. Rivin, *Simplices and spectra of graphs, continued*, arXiv:0901.3284, first submitted 2009-01-20. Jacobian-spectrum argument and nonuniqueness family.
- A. A. Gaifullin, *Volume of a simplex as a multivalued algebraic function of the areas of its two-faces*, arXiv:1310.3417, first submitted 2013-10-12. Introduction and Theorems 1.1–1.4.
