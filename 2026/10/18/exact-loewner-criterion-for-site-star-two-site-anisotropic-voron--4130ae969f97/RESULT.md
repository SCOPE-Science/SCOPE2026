# Exact Loewner criterion for site-star two-site anisotropic Voronoi cells

## Finding
For every integer \(d\ge1\), distinct sites \(p,q\in\mathbb R^d\) and symmetric positive-definite matrices \(A,B\in\mathbb R^{d\times d}\), define the two closed anisotropic Voronoi cells
\[
C_p=\big\{x:(x-p)^\mathsf{T}A(x-p)\le(x-q)^\mathsf{T}B(x-q)\big\},\qquad
C_q=\big\{x:(x-q)^\mathsf{T}B(x-q)\le(x-p)^\mathsf{T}A(x-p)\big\}.
\]
Then the following conditions are equivalent:

1. \(C_p\) is star-shaped with respect to \(p\).
2. \(C_p\) is convex.
3. \(A-B\) is positive semidefinite in the Loewner order.

In particular, both cells are star-shaped with respect to their respective generating sites exactly when \(A=B\). For unequal site metrics, at least one of the two sites cannot see its entire cell. This conclusion holds in every dimension, including the one-dimensional case.

## Assumptions and scope
The ambient domain is the *entire* Euclidean space, not a clipped observation window. The distance comparison uses site-dependent quadratic forms, and ties are included in both closed cells. Each generating site belongs to its own cell because the sites are distinct and the metrics are positive definite. A set \(S\) is star-shaped at \(z\) when the segment \([z,x]\subset S\) for every \(x\in S\).

## Proof
Translate \(p\) to the origin and put \(v=q-p\ne0\), \(H=A-B\), \(b=Bv\) and \(c=v^\mathsf{T}Bv>0\). The sign comparison is exactly
\[
g(y)=y^\mathsf{T}Hy+2b^\mathsf{T}y-c,\qquad C_p-p=\{y:g(y)\le0\}.
\]
We have \(g(0)=-c<0\) and \(g(v)=v^\mathsf{T}Av>0\). If \(H\succeq0\), the function \(g\) is convex; thus its sublevel set is convex and contains the origin. This proves (3) implies (2) implies (1).

For necessity suppose the cell is star-shaped about the origin but \(H\not\succeq0\). Define the nonempty open double cone
\[
N=\{u\in\mathbb R^d:u^\mathsf{T}Hu<0\}.
\]
For every \(u\in N\), the quadratic \(t\mapsto g(tu)\) tends to minus infinity at both ends of the real line. Hence sufficiently remote points \(\pm Tu\) lie in the cell. The site-star property applied to both segments from the origin forces \(g(tu)\le0\) for *every* real \(t\). In particular \(g(v)>0\) forces \(v\notin N\).

There are two exhaustive possibilities for a symmetric \(H\) with a negative eigenvalue.

**Indefinite case.** If \(H\) has both negative and positive eigenvalues, every null vector \(u\) satisfying \(u^\mathsf{T}Hu=0\) belongs to the closure of \(N\) (perturb it toward a negative eigenvector; if necessary choose a perturbation sign). Continuity gives \(g(tu)\le0\) for every real \(t\). Since \(g(tu)=2t b^\mathsf{T}u-c\), we must have \(b^\mathsf{T}u=0\) for every null vector. Such null vectors span \(\mathbb R^d\): for any negative eigenvector \(e_-\) and positive eigenvector \(e_+\) with eigenvalues \(-\mu\) and \(\lambda\), the two null vectors \(\sqrt\lambda e_-\pm\sqrt\mu e_+\) span their plane. Varying the eigenvectors covers all positive and negative eigenspaces; kernel vectors are themselves null. Therefore \(b=0\), contradicting \(c=v^\mathsf{T}b>0\).

**Negative-semidefinite case.** If \(H\preceq0\) and \(H\ne0\), the already proved condition \(g(y)\le0\) on \(N\) and continuity force \(b\) to annihilate \(\ker H\): every kernel vector is a limit of elements of \(N\), and the linear term must vanish along its full line. Thus \(b\in(\ker H)^\perp\). Since \(v^\mathsf{T}b=c>0\), the vector \(v\) has nonzero projection onto the negative eigenspaces of \(H\). Therefore \(v^\mathsf{T}Hv<0\), i.e. \(v\in N\), contradicting \(g(v)=v^\mathsf{T}Av>0\). This exhausts the possibilities and proves (1) implies (3).

The same equivalence applies to \(C_q\) after interchanging the two sites and their metrics. Thus both cells are site-star exactly when both \(A-B\succeq0\) and \(B-A\succeq0\), which is equivalent to \(A=B\).

For a precise description of failure when \(H\not\succeq0\), the contradiction establishes that there exists \(u\) with \(a=u^\mathsf{T}Hu<0\) for which \(g(tu)>0\) at some positive \(t\). Along that ray \(g(tu)=at^2+2bt-c\), here with scalar \(b=u^\mathsf{T}Bv\); necessarily \(b>0\) and \(b^2+ac>0\). Its two positive roots are
\[
t_-=\frac{b-\sqrt{b^2+ac}}{-a},\qquad
 t_+=\frac{b+\sqrt{b^2+ac}}{-a}.
\]
The points with \(0\le t\le t_-\) and \(t\ge t_+\) belong to the cell, while the interval \(t_-<t<t_+\) lies outside. Scaling \(u\) to unit length changes the root parameters but not this radial obstruction.

## Verification
The complete proof above is analytical, with no finite-experiment-to-universal inference. The included `verify.py` uses exact rational arithmetic to check the nontrivial explicit witness \(p=(0,0)\), \(q=(1,0)\), \(A=\operatorname{diag}(2,1)\), \(B=\operatorname{diag}(1,2)\), and \(u=(10,11)\). Along the ray, \(g(tu)=-21t^2+20t-1\); the exact values at \(t=0,\tfrac12,1\) are respectively \(-1,\tfrac{15}{4},-2\). Thus the endpoints are in \(C_p\), but the midpoint is outside it, explicitly certifying failure of site-star convexity when the Loewner condition is violated. The program also checks a positive-semidefinite example on rational pairs as a numerical regression, not as proof of universal convexity.

To replay locally, run `python verify.py` with Python 3; no third-party packages or external datasets are needed.

## Relationship to prior work
Venkovic and Anzt's 2026 paper introduces formulas for Minkowski tensors of planar site-dependent anisotropic Voronoi cells **conditional on site-star-convexity**. The present statement gives an exact test for that hypothesis in the two-site, global quadratic-metric case. It neither computes those tensors nor proves star-convexity for multisite cells. Labelle and Shewchuk's earlier anisotropic Voronoi analysis provides visibility conditions for general site arrangements rather than the above necessary-and-sufficient two-site metric-order criterion. Cañas and Gortler study sufficient orphan-freeness/connectedness conditions, not the asserted precise site-star equivalence. Search comparisons were made at the level of mathematical implications and not merely title matching.

## Limitations
The geometry of clipped regions can differ: star-shapedness inside a bounded computational window does not force the global Loewner inequality. The result does not address variable point-dependent metrics, nonquadratic Finsler costs, nonconstant weights, or more than two sites. The construction of a failing ray is existential for an arbitrary indefinite matrix but has explicit roots once a witnessing direction is found. A self-review is not an independent validation; related quadratic-geometry statements may exist outside the inspected literature.

## References
1. N. Venkovic and H. Anzt, *Minkowski Tensors of Planar Anisotropic Voronoi Diagrams*, arXiv:2610.08656v1 (2026-10-06), https://arxiv.org/abs/2610.08656.
2. F. Labelle and J. R. Shewchuk, *Anisotropic Voronoi Diagrams and Guaranteed-Quality Anisotropic Mesh Generation*, SoCG (2003), https://people.eecs.berkeley.edu/~jrs/papers/aniso.pdf.
3. G. D. Cañas and S. J. Gortler, *Orphan-Free Anisotropic Voronoi Diagrams*, https://www.eecs.harvard.edu/~sjg/papers/avd.pdf.
