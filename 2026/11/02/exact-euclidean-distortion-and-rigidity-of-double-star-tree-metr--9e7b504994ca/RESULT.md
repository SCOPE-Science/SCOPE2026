# Exact Euclidean distortion and rigidity of double-star tree metrics

## Finding

For integers \(m,n\ge 2\), let \(T_{m,n}\) be the unweighted double-star tree formed by joining the centers of two stars having \(m\) and \(n\) leaves. Equip all \(m+n+2\) vertices with shortest-path distances \(d\). Define
\[
r_m=2-\frac2m,\qquad s_n=2-\frac2n,
\]
and, for \(c\ge\max\{r_m,s_n\}\), define
\[
\Phi_{m,n}(c)=r_m+s_n+
\bigl(\sqrt{c-r_m}+\sqrt c+\sqrt{c-s_n}\bigr)^2.
\]
There is exactly one \(c_{m,n}\in(\max\{r_m,s_n\},3)\) with \(\Phi_{m,n}(c_{m,n})=9\). The least bi-Lipschitz distortion into any real Hilbert space is precisely
\[
\boxed{c_2(T_{m,n})=\sqrt{c_{m,n}}.}
\]
Every optimal noncontracting embedding whose Lipschitz constant is \(\sqrt{c_{m,n}}\) is congruent to the explicit configuration in the proof. Its affine span has dimension exactly \(m+n-1\). In particular, every optimal embedding places the two centers and the two leaf centroids on one line in that order; each leaf class forms a regular simplex, and their fluctuation subspaces and the centroid line are mutually orthogonal.

When \(m=n=k\), the equation has the closed solution
\[
\boxed{c_2(T_{k,k})=
\frac{2\sqrt{11-2/k}-\sqrt{5+4/k}}3.}
\]
The distortion increases strictly in either leaf count. Consequently its supremum over all finite double stars is the unattained, sharp dimension-independent constant
\[
\boxed{\sup_{m,n\ge2}c_2(T_{m,n})=
\frac{2\sqrt{11}-\sqrt5}{3}=1.4657272010\ldots.}
\]

## Assumptions and scope

The two central vertices are \(u,v\). Leaves \(a_1,\ldots,a_m\) are adjacent to \(u\), and leaves \(b_1,\ldots,b_n\) are adjacent to \(v\); the centers are adjacent. All graph edges have length \(1\). In particular, same-class leaf distances are \(2\), opposite-class leaf distances are \(3\), and each leaf is at distance \(2\) from the opposite center. The target can be an arbitrary real Hilbert space, with no restriction on ambient dimension. For an injective map \(f\), distortion means
\[
\operatorname{dist}(f)=
\left(\max_{x\ne y}\frac{\|f(x)-f(y)\|}{d(x,y)}\right)
\left(\max_{x\ne y}\frac{d(x,y)}{\|f(x)-f(y)\|}\right).
\]
Scaling allows us to require \(\|f(x)-f(y)\|\ge d(x,y)\) for every pair; then \(\operatorname{dist}(f)\le\sqrt c\) means every squared distance is at most \(c\) times its squared graph distance.

## Proof

**1. The unique scalar root.** Write \(r=r_m\), \(s=s_n\), and \(d_0=\max\{r,s\}\). Since \(1\le r,s<2\), we have
\[
\Phi_{m,n}(d_0)=3d_0+2\sqrt{d_0(d_0-\min\{r,s\})}
<6+2\sqrt2<9.
\]
For fixed \(c>d_0\), the function \(\Phi_{m,n}(c)\) is strictly increasing in \(c\), while
\[
\Phi_{m,n}(3)\ge 4+(2+\sqrt3)^2>9.
\]
(The last inequality follows because \(\Phi\) is decreasing separately in \(r,s\) at fixed \(c\), and \(r,s\le2\).) Thus a unique root \(c\in(d_0,3)\) exists.

**2. A universal lower bound.** Fix any Hilbert-valued, noncontracting embedding satisfying the squared upper-Lipschitz bound \(C\). Denote its leaf vectors by \(x_i,y_j\), its center vectors by \(U,V\), and its leaf centroids by \(\bar x,\bar y\). Put
\[
R=\frac1m\sum_i\|x_i-\bar x\|^2,\qquad
S=\frac1n\sum_j\|y_j-\bar y\|^2.
\]
The exact variance identity and the lower distance bound within each leaf class yield
\[
R=\frac1{m^2}\sum_{i<j}\|x_i-x_j\|^2\ge \frac{2(m-1)}m=r,\qquad S\ge s.
\]
Averaging the squared center-to-leaf distances, each at most \(C\), gives
\[
\|\bar x-U\|\le\sqrt{C-R},\qquad
\|\bar y-V\|\le\sqrt{C-S},\qquad
\|U-V\|\le\sqrt C.
\]
The averaged cross-class distances are each at least \(9\); applying the centroid decomposition and the triangle inequality along \(\bar x,U,V,\bar y\) therefore gives
\[
9\le R+S+\|\bar x-\bar y\|^2
\le R+S+\bigl(\sqrt{C-R}+\sqrt C+\sqrt{C-S}\bigr)^2.
\]
For \(0\le R,S\le C\), the last right side is strictly decreasing in either \(R\) or \(S\) (its derivative with respect to \(R\), away from the endpoint, is \(-[\sqrt C+\sqrt{C-S}]/\sqrt{C-R}<0\), with the endpoint handled by continuity). It is hence no greater than \(\Phi_{m,n}(C)\). As \(\Phi\) is increasing in \(C\) and \(\Phi(c)=9\), we conclude \(C\ge c\), or \(\operatorname{dist}(f)\ge\sqrt c\).

**3. Attaining configuration and the two-distance constraint.** Let \(c=c_{m,n}\). Use a unit vector \(e\) and mutually orthogonal regular-simplex spaces of dimensions \(m-1\) and \(n-1\), both orthogonal to \(e\). In these spaces choose vectors \(p_1,\ldots,p_m\) and \(q_1,\ldots,q_n\) with centroid zero, squared lengths \(r\) and \(s\), and within-class pairwise distances \(2\). One concrete choice is \(p_i=\sqrt2(e_i-m^{-1}\mathbf1)\) in the coordinate zero-sum hyperplane, and analogously for the other class. Set
\[
U=0,\qquad V=\sqrt c\,e,\qquad
x_i=-\sqrt{c-r}\,e+p_i,\qquad
y_j=(\sqrt c+\sqrt{c-s})e+q_j.
\]
All three types of original graph edges (leaf–near center on either side and the center–center edge) have squared embedded length \(c\). Same-class leaf distances are \(2\), and by the defining equation
\[
\|x_i-y_j\|^2=r+s+
(\sqrt{c-r}+\sqrt c+\sqrt{c-s})^2=9
\]
for every opposite-class leaf pair. The remaining two pair types, leaf-to-opposite-center, have squared distances
\[
2c+2\sqrt{c(c-r)},\qquad 2c+2\sqrt{c(c-s)}.
\]
These lie strictly between \(4\) and \(4c\). The upper bounds follow from \(r,s>0\). For the lower bounds, for any \(t\in[1,2)\) put \(c_0(t)=4/(4-t)\). If \(c_0(r)<s\), then \(c>s>c_0(r)\) already. Otherwise \(c_0(r)\ge s\ge1\), so the function \(\Phi\) is defined at \(c_0(r)\) and, because it decreases in the parameter \(s\), one has \(\Phi_{m,n}(c_0(r))\le\Phi(c_0(r);r,1)=4+c_0(r)+2\sqrt r<9\). As \(c_0(r)<2\), this is at most \(6+2\sqrt2<9\). Hence in all cases \(c>c_0(r)\); similarly \(c>c_0(s)\). For \(c<2\), the inequality \(2c+2\sqrt{c(c-t)}\ge4\) is equivalent to \(c\ge c_0(t)\), while for \(c\ge2\) it is immediate. Thus all pair distances are noncontracting and at most \(\sqrt c\) times their original values, and the original edges attain \(\sqrt c\). This proves equality.

**4. Rigidity and affine dimension.** If a normalized embedding attains the lower bound \(C=c\), every preceding inequality is an equality: the strict monotonicity in \(R,S\) gives \(R=r,S=s\), so every pair within each leaf class has distance exactly \(2\). Both averaged center-leaf upper bounds and the center-center upper bound are equalities, giving all original graph edges squared embedded distance \(c\). The centroid triangle inequality is an equality, so \(\bar x,U,V,\bar y\) are collinear in this order, with consecutive lengths \(\sqrt{c-r},\sqrt c,\sqrt{c-s}\). Constancy of each near-center leaf distance forces the centered simplex fluctuations to be orthogonal to the centroid line. Finally, since the mean cross-class squared distance is \(9\) and every cross-class distance is at least \(3\), all cross-class squared distances are exactly \(9\); this forces every inner product between a centered first-class and centered second-class fluctuation to vanish. The two regular simplices are therefore in orthogonal subspaces. Their Gram matrices are uniquely determined by the within-class squared distance \(4\), and the center positions are fixed up to isometry. The affine span is the direct sum of the line and the two simplex subspaces, of dimension \(1+(m-1)+(n-1)=m+n-1\).

**5. Balanced law and limiting sharp constant.** In the balanced case \(r=s=t=2-2/k\), the equation \(2t+(2\sqrt{c-t}+\sqrt c)^2=9\) is solved by setting \(z=\sqrt c\), \(h=\sqrt{9-2t}\), whence \(3z^2+2hz-(h^2+4t)=0\). The positive solution is \(z=[2\sqrt{9+t}-\sqrt{9-2t}]/3\), yielding the stated formula. For fixed \(c\), \(\Phi_{m,n}(c)\) strictly decreases with \(r\) and \(s\); since the unique root is defined by \(\Phi=9\), it strictly increases with either \(r\) or \(s\), hence with either leaf count. Sending both counts to infinity gives the stated sharp supremum.

## Verification

The standalone `verify_double_star.py` uses 75-digit decimal arithmetic and explicitly reconstructs the Hilbert-space coordinates. Running `python verify_double_star.py` verifies \(173\) parameter pairs, \(28{,}223\) explicit vertex pairs, all metric distortion inequalities and extremal pair types, plus the balanced radicals and limiting constant. Its expected final line is `CHECK_OK parameter_cases= 173 explicit_vertex_pairs= 28223`. This is supplementary finite verification; uniqueness and the unrestricted result are proved above without enumeration.

## Relationship to prior work

Choudhury and Nandi [1, Theorem 3.6] determine the quadratic embedding constant of the same double-star tree family by a cubic in parameters. This is a quadratic form of the **unsquared graph distance matrix** used for negative-type questions, not the optimal bi-Lipschitz distortion into Hilbert space of the original metric. Robertson [2, Theorem 4.3] provides exact Hilbert distortion for a different family, complete bipartite graph metrics, and general distorted-negative-type machinery. Babilon et al. [3] prove fixed-dimensional distortion bounds for all trees and construct asymptotically optimal plane embeddings for fans, not sharp unrestricted-dimensional double-star constants. Lee, Naor, and Peres [4] determine tree Hilbert distortion only up to universal factors via Markov convexity. None of these statements implies the exact double-star formula and optimal-embedding rigidity here by a stated result; broader prior coverage under different terminology has not been fully ruled out.

## Limitations

The theorem concerns unweighted double stars with at least two leaves on each side; it does not cover arbitrary weighted trees, single-star degeneracies, fixed low-dimensional Euclidean targets, or general graphs. The root is defined implicitly except on the balanced subfamily. The proof is analytical and self-contained, while numerical checks merely guard its formulas. Historical priority is qualified because older material on low-distortion tree embeddings, especially Linial–Magen–Saks (1998), was not available in full text; no independent audit or external certification has occurred.

## References

1. Projesh Nath Choudhury and Raju Nandi, *Quadratic embedding constants of graphs: Bounds and distance spectra*, arXiv:2306.15589 (first posted 2023-06-27), especially Definition 3.3 and Theorem 3.6. https://arxiv.org/abs/2306.15589
2. Gavin Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space*, arXiv:2309.16070 (first posted 2023-09-27), Theorem 4.3. https://arxiv.org/abs/2309.16070
3. Robert Babilon, Jiří Matoušek, Jana Maxová, and Pavel Valtr, *Low-Distortion Embeddings of Trees*, Journal of Graph Algorithms and Applications 7 (2003), 399–409, especially Theorem 1 and Proposition 1. https://doi.org/10.7155/jgaa.00076
4. James R. Lee, Assaf Naor, and Yuval Peres, *Trees and Markov convexity*, Sections 1–2, an author-hosted full-text paper available at https://web.math.princeton.edu/~naor/homepage%20files/TreeMarkov.pdf
5. Nathan Linial, Avner Magen, and Michael E. Saks, *Low distortion Euclidean embeddings of trees*, Israel Journal of Mathematics 106 (1998), 339–348. Full text was not accessed; bibliographic/abstract-only comparison.
