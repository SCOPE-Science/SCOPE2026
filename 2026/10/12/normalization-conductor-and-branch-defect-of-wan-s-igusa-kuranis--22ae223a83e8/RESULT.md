# Normalization conductor and branch defect of Wan's Igusa Kuranishi germ
## Finding
Let
\[
R=\mathbb C[a,b,c,d,e,f]/(ab,bc,ca,de,ef,fd).
\]
Wan identifies the semiuniversal analytic deformation germ of the polystable tangent bundle in the Igusa example, with the threefold fixed, with the germ at the origin of \(\operatorname{Spec}R\). The normalization of the homogeneous affine model is
\[
\widetilde R\cong\prod_{x\in\{a,b,c\},\,y\in\{d,e,f\}}\mathbb C[x,y].
\]
Thus the normalization is the disjoint union of nine affine planes.

The conductor is exactly
\[
\mathfrak c=(ad,ae,af,bd,be,bf,cd,ce,cf)\subset R.
\]
Modulo \(\mathfrak c\), every product of two distinct variables vanishes. Hence the conductor subscheme downstairs is the reduced union of the six coordinate axes, which is also the singular locus. On a normalized component \(\operatorname{Spec}\mathbb C[x,y]\), the extended conductor is \((xy)\), so its inverse image is the union of the two coordinate axes of that plane.

The normalization fiber has one point away from the six axes, three points over each nonzero point of a conductor axis, and nine points over the origin. With the standard grading,
\[
H_{\widetilde R/R}(t)=\frac{8+4t}{1-t}.
\]
Thus the one-dimensional normalization-defect module has multiplicity \(12\): its degree-zero piece has dimension \(8\), while every positive graded piece has dimension \(12\).

## Assumptions and scope
All rings are over \(\mathbb C\). The statement concerns Wan's fixed-threefold semiuniversal deformation germ before quotienting by automorphisms or by any coarse-moduli equivalence. The homogeneous affine model represents the analytic germ at its vertex; normalization is finite, and localization/completion at the vertex gives the corresponding germ statement.

The conductor is
\[
\mathfrak c=\{r\in R:r\widetilde R\subset R\}.
\]
The multiplicity \(12\) is the Hilbert multiplicity of the one-dimensional graded module \(\widetilde R/R\), not the Hilbert--Samuel multiplicity \(9\) of \(R\).

## Proof
Write
\[
A=\mathbb C[a,b,c]/(ab,bc,ca),\qquad A'=\mathbb C[d,e,f]/(de,ef,fd),
\]
so \(R\cong A\otimes_{\mathbb C}A'\). The minimal primes of \(A\) are \((a,b)\), \((a,c)\), and \((b,c)\), and similarly for \(A'\). Hence the nine minimal-prime quotients of \(R\) are \(\mathbb C[x,y]\), where \(x\in\{a,b,c\}\) and \(y\in\{d,e,f\}\). Each is normal, so the normalization of the reduced ring is their product.

Under the embedding into this product, an element is a \(3\times3\) family \((f_{xy}(x,y))\). The image of \(R\) consists exactly of families for which, for fixed \(x\), the restrictions \(f_{xy}(x,0)\) are independent of \(y\), and for fixed \(y\), the restrictions \(f_{xy}(0,y)\) are independent of \(x\). Indeed every surviving monomial uses at most one variable from each triple, so every element is a common constant plus three first-axis terms, three second-axis terms, and nine independent terms divisible by the relevant \(xy\).

If \(r=(f_{xy})\) lies in the conductor, multiply it in \(\widetilde R\) by the idempotent supported on one normalized plane. The product must still satisfy the boundary compatibilities, while all neighboring components are zero. Therefore
\[
f_{xy}(x,0)=f_{xy}(0,y)=0,
\]
so \(f_{xy}\) is divisible by \(xy\). This holds on all nine planes. Conversely, if every component is divisible by its \(xy\), then multiplication by an arbitrary element of the normalization preserves zero boundary restrictions, so the product lies in \(R\). This proves the conductor formula.

The original six quadratic generators together with the nine conductor generators are all fifteen squarefree products of two distinct variables among \(a,b,c,d,e,f\). Their quotient is therefore the reduced union of the six coordinate axes. On the \((x,y)\)-plane, the conductor extends to \((xy)\). Branch incidence gives normalization-fiber sizes \(1\), \(3\), and \(9\) off the conductor, on a nonzero conductor axis, and at the origin respectively.

Each normalized plane contributes \((1-t)^{-2}\), hence
\[
H_{\widetilde R}(t)=\frac{9}{(1-t)^2}.
\]
The three-axis ring has Hilbert series \((1+2t)/(1-t)\), so
\[
H_R(t)=\frac{(1+2t)^2}{(1-t)^2}.
\]
Subtracting yields
\[
H_{\widetilde R/R}(t)=\frac{8-4t-4t^2}{(1-t)^2}=\frac{8+4t}{1-t}.
\]

## Verification
The accompanying `verify_normalization_conductor.py` checks the component and conductor combinatorics with exact integer arithmetic. It confirms the nine normalized components, the fifteen pairwise squarefree quadratic generators after adjoining the conductor, the normalization-fiber counts, and the Hilbert functions through degree \(19\). The stored replay ends in `VERIFY_OK`.

The finite replay is only a consistency check. The infinite conductor equality and Hilbert-series identity are proved symbolically above.

## Relationship to prior work
Wan's preprint determines the exact semiuniversal deformation germ and states that it is the product of two three-axis germs, hence reduced with nine two-dimensional irreducible components. A published structural profile of the same ring computes Cohen--Macaulay type \(4\), the minimal graded resolution, Hilbert--Samuel multiplicity \(9\), the six-axis singular locus, and the \(K_{3,3}\) projectivized tangent cone. The inspected public statements do not give the normalization, conductor ideal, normalization fiber counts, or Hilbert series of the normalization-defect module.

Targeted database searches used the exact ideal, the arXiv identifier, normalization/conductor terminology, branch-count language, and the defect-series formulation. The closest result is the structural profile of the same Wan germ; other returned normalization/conductor results concern different varieties and do not imply this calculation.

## Limitations
The statement does not address automorphism quotients or coarse moduli. The normalization and conductor computation is short once the exact monomial germ is known; its value is the canonical branch-gluing description and quantitative defect module, not a new general theorem about normalization.

The primary arXiv abstract and independently indexed Introduction/Theorem 1.5 material were inspectable, while the primary full-text HTML/PDF route was inaccessible during source inspection. A previously published exact-source review records full inspection of Theorem 1.5 and Sections 5.2--5.4. Because the primary full text was not directly re-read here, an equivalent statement hidden later in that paper remains a residual originality risk.

## References
1. X. Wan, *Rigid and obstructed tangent bundles on Calabi--Yau threefolds*, arXiv:2609.27271v1, first public 2026-09-23.
2. Published database record `2026/10/4/SCOPE-wan-s-igusa-kuranishi-cone-is-cohen-macaulay-of-type-4--efa99c3892a3`, structural profile of the same deformation germ.
