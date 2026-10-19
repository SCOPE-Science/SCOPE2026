# A sharp bounded-conditioning rescue for a fixed-face tetrahedral Hodge preconditioner

## Finding

The positive triangle weights of a fixed weakly collapsible subcomplex need not be inherited from the original complex when the goal is **spectral conditioning**, rather than approximation of the up-Laplacian in operator norm. On a four-face tetrahedral sphere with one prescribed omitted face, a simple local addition rule prevents unbounded spectral deterioration and achieves a sharp limiting optimum among **all positive retained-face reweightings**.

More precisely, let \(0<a\leq 1\). Give the four consistently oriented faces of a tetrahedron the strictly positive weights \((a,1,a^{-1},1)\). Omit the fourth face, retain the other three, and form a positive-weight, three-face preconditioner for the full weighted one-up-Laplacian. Let \(\kappa(a;d)\) be the spectral condition number of the three-dimensional positive definite symmetrically preconditioned matrix, when the retained weights are \(d=(d_1,d_2,d_3)\in(0,\infty)^3\).

The inherited weights \(d=(a,1,a^{-1})\) produce exactly
\[
\kappa(a;d)=2+a+a^{-1}.
\]
Instead, the local additive reweighting \(d=(1+a,2,1+a^{-1})\), obtained by adding the omitted face's weight to every retained weight, has
\[
\lim_{a\downarrow0}\kappa(a;d)=3+2\sqrt2.
\]
The constant is **asymptotically best possible among all positive retained-face weights**:
\[
\boxed{\inf_{d\in(0,\infty)^3}\kappa(a;d)=3+2\sqrt2+O(a)\quad(a\downarrow0).}
\]
Consequently the inherited-weight approximation has an unbounded loss relative to optimal reweighting, with the sharp ratio law
\[
\boxed{\lim_{a\downarrow0}a\,\frac{\kappa(a;(a,1,a^{-1}))}{\inf_{d>0}\kappa(a;d)}=3-2\sqrt2.}
\]
The omitted face and the three retained faces are **fixed** throughout; the claim does not optimize the choice of faces.

## Assumptions and scope

Take a single tetrahedron with ordered vertices \(0,1,2,3\). Let \(B_2\in\mathbb R^{6\times4}\) be its signed edge-face incidence matrix with face columns \(b_1,b_2,b_3,b_4\) oriented as the oriented boundary of the tetrahedron, so that \(b_1+b_2+b_3+b_4=0\). The first three columns are linearly independent. Edge weights are one; all four face weights are positive. Define the full one-up-Laplacian
\[
L(a)=B_2\operatorname{diag}(a,1,a^{-1},1)B_2^{\mathsf T}.
\]
The three-face subcomplex obtained by deleting face four is a disk and is weakly collapsible. For positive retained-face weights \(d\), form \(C(d)=[b_1\ b_2\ b_3]\operatorname{diag}(\sqrt{d_1},\sqrt{d_2},\sqrt{d_3})\), so that \(C(d)C(d)^{\mathsf T}\) is the reweighted three-face one-up-Laplacian. Its exact Cholesky-like factors are equivalent for spectral purposes. Set
\[
\kappa(a;d)=\kappa_2\!\left(C(d)^+L(a)(C(d)^+)^{\mathsf T}\right).
\]
Here \((\cdot)^+\) is the Moore--Penrose pseudoinverse; the displayed matrix is a positive definite \(3\times3\) matrix, and \(\kappa_2\) is its largest-to-smallest eigenvalue ratio. All conclusions use exact arithmetic. No assertion is made at \(a=0\), where the original weights cease to be strictly positive.

## Proof

**Step 1: exact reduction.** Let \(B=[b_1\ b_2\ b_3]\). The tetrahedral boundary identity \(b_4=-B\mathbf1\), together with the four weights, yields
\[
L(a)=B M(a)B^{\mathsf T},\qquad
M(a)=\operatorname{diag}(a,1,a^{-1})+\mathbf1\mathbf1^{\mathsf T}.
\]
The retained-face disk has three linearly independent face boundaries (for example, the retained face boundary Gram matrix is \(4I_3-\mathbf1\mathbf1^{\mathsf T}\), with determinant \(16\)). With \(D=\operatorname{diag}(d)\) and \(C=BD^{1/2}\), the identity \(C^+B=D^{-1/2}\) gives the exact spectral representation
\[
C^+L(a)(C^+)^{\mathsf T}=D^{-1/2}M(a)D^{-1/2}.
\]
This justifies optimization over positive face reweightings without altering the retained topology or the nonzero spectral subspace.

**Step 2: inherited weights.** Set \(D_0=\operatorname{diag}(a,1,a^{-1})\). The preconditioned matrix is
\[
D_0^{-1/2}M(a)D_0^{-1/2}=I_3+vv^{\mathsf T},\quad v=(a^{-1/2},1,a^{1/2})^{\mathsf T}.
\]
Its eigenvalues are \(1,1,1+\|v\|_2^2\). Therefore \(\kappa(a;(a,1,a^{-1}))=2+a+a^{-1}\), exactly.

**Step 3: a constructive bounded-conditioning rule.** Set
\[
D_*(a)=\operatorname{diag}(1+a,2,1+a^{-1})=\operatorname{diag}M(a).
\]
The symmetric preconditioned matrix \(P(a)=D_*^{-1/2}M(a)D_*^{-1/2}\) has diagonal entries one and off-diagonal entries
\[
P_{12}=\frac1{\sqrt{2(1+a)}},\qquad
P_{13}=\frac{\sqrt a}{1+a},\qquad
P_{23}=\frac{\sqrt a}{\sqrt{2(1+a)}}.
\]
Writing \(t=a/(1+a)^2\), direct expansion of the determinant gives
\[
\det(\lambda I_3-P(a))=\lambda^3-3\lambda^2+\left(\frac52-t\right)\lambda-\frac12.
\]
As \(a\downarrow0\), this polynomial tends to \((\lambda-1)(\lambda^2-2\lambda+1/2)\). Its three roots \(1-1/\sqrt2\), \(1\), \(1+1/\sqrt2\) are positive and distinct. Continuity gives
\[
\lim_{a\downarrow0}\kappa_2(P(a))
=\frac{1+1/\sqrt2}{1-1/\sqrt2}=3+2\sqrt2.
\]
Because \(t=O(a)\) and the limiting roots are simple, elementary root perturbation (or the implicit function theorem for each root) strengthens this to \(\kappa_2(P(a))=3+2\sqrt2+O(a)\).

**Step 4: optimal lower bound over all positive face weights.** For arbitrary positive \(D=\operatorname{diag}(d)\), take the leading \(2\times2\) principal submatrix of \(D^{-1/2}M(a)D^{-1/2}\). Its correlation coefficient is independent of \(D\):
\[
c(a)=\frac{M_{12}}{\sqrt{M_{11}M_{22}}}=\frac1{\sqrt{2(1+a)}}.
\]
A positive definite \(2\times2\) matrix with positive correlation \(c\) has condition number at least \((1+c)/(1-c)\) under all positive diagonal scalings. Indeed, if its diagonal entries are \(u,v>0\), then its determinant divided by the square of its trace is \((1-c^2)uv/(u+v)^2\le(1-c^2)/4\). The eigenvalue ratio is minimized when \(u=v\), yielding that bound. Eigenvalue interlacing makes the full \(3\times3\) condition number no smaller than that of the principal block. Consequently, **for every** \(d\in(0,\infty)^3\),
\[
\kappa(a;d)\ge\frac{1+c(a)}{1-c(a)}=3+2\sqrt2+O(a).
\]
The constructive upper bound in Step 3 matches the limit and the \(O(a)\) scale. This proves the asymptotic infimum over all reweightings. Finally, the inherited cost is \(a^{-1}+2+a\), so multiplying its ratio to that infimum by \(a\) and taking the limit gives \((3+2\sqrt2)^{-1}=3-2\sqrt2\).

## Verification

The companion file `check.py` uses only Python's standard library. It constructs the signed six-edge/four-face incidence matrix directly from oriented tetrahedron faces, verifies the boundary relation and the three-face Gram determinant, and checks the six-dimensional up-Laplacian factorization using exact rational arithmetic. For eight positive rational values of \(a\), it verifies the rational coefficients of the characteristic polynomial and the inherited-weight spectral law. It also compares three-dimensional symmetric eigenvalue calculations with the interlacing bound and the asserted limiting constants. In total it passes 74 assertions in one execution. These finite checks supplement, but do not replace, the complete analytical argument above. Run `python3 check.py` in the extracted artifact directory.

## Relationship to prior work

Savostianov, Tudisco and Guglielmi [1] develop Cholesky-like preconditioners for simplicial up-Laplacians using weakly collapsible subcomplexes. Their Section 6.1 treats the **fixed-subcomplex** weight question using an operator-norm approximation objective and derives spectral conditioning in terms of a projected incidence subspace. Their heavy-subcomplex algorithm also chooses which faces to retain. The present result concerns the **different spectral-conditioning objective**, permits positive reweighting of a prescribed three-face disk, and computes a sharp limiting infimum and a simple optimal-at-leading-order rule. It does not replace or evaluate their face-selection algorithm.

Qu, Gao, Hinder, Ye and Zhou [2] provide general algorithms and optimization formulations for diagonal preconditioning. Those general methods encompass the diagonal-scaling problem abstractly; the specific tetrahedral Hodge interpretation, inherited-weight divergence and sharp \(3+2\sqrt2\) asymptotic reweighting law are not statements identified in the inspected portions of that literature. The lower-bound proof uses standard interlacing and two-dimensional conditioning inequalities; these classical tools are not claimed as novel.

## Limitations

The sharp result is for one tetrahedral boundary, its fixed three-face disk, and the explicitly graded positive weights \((a,1,a^{-1},1)\) as \(a\downarrow0\). It is not an exact characterization of the best finite-\(a\) reweighting and says nothing about the quality of the heaviest-face selection used by [1]. Indeed, selecting the omitted face is a separate combinatorial decision that may avoid this unfavourable fixed subcomplex. General higher-dimensional complexes, other weight profiles, finite-precision factors and timing improvements are not analyzed. 

## References

[1] A. Savostianov, F. Tudisco and N. Guglielmi, *Cholesky-like Preconditioner for Hodge Laplacians via Heavy Collapsible Subcomplex*, arXiv:2401.15492v1 (first public January 27, 2024), especially Sections 3, 6.1 and Theorem 18. https://arxiv.org/html/2401.15492v1

[2] Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809v1 (first public September 2, 2022), especially Section 1 and general one-sided scaling formulation. https://arxiv.org/abs/2209.00809
