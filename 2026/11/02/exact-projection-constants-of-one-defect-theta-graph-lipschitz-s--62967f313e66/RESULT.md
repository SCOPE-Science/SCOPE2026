# Exact projection constants of one-defect theta-graph Lipschitz spaces

## Finding

Let \(p,a,b\) be integers with \(p,a,b\ge2\). Form the simple unweighted graph \(\Theta_{p;a,b}\) by joining two distinct poles with \(p\) internally vertex-disjoint paths of length \(a\) and one further internally vertex-disjoint path of length \(b\). Give its vertex set the unweighted shortest-path metric, and let \(L=\operatorname{Lip}_0(V(\Theta_{p;a,b}))\) be the real Banach space of Lipschitz functions vanishing at either chosen pole. The choice of pole does not affect the isometry class.

Put
\[
 r=\frac ba,\quad
 C=2-\frac2a+r,\quad
 h=p-2+\frac2a-pr,\quad
 B=p\left(1+\frac{a-2}{b}\right),
\]
\[
 H=3-\frac2p-\frac{2(p-1)}{ap},\qquad
 J=2+\frac{a-2}{b}.
\]
Then the **absolute linear projection constant** of \(L\) is exactly
\[
 \boxed{\lambda(L)=
 \begin{cases}
 C,& h\ge0,\\[2pt]
 H,& h<0\ \text{and}\ H\ge J,\\[2pt]
 1+\dfrac{B(C-1)}{B-h},&h<0\ \text{and}\ H<J.
 \end{cases}}
\]
Here the absolute projection constant is the supremum of the minimum projection norm over all isometric superspaces; it equals the minimum norm of a projection from \(\ell_\infty^{|E|}\) onto the edge-gradient copy of \(L\).

There are three sharp geometric regimes. For \(h\ge0\), the optimal cycle-space retraction uses only the exceptional path for its correction. For \(h<0\) and \(H\ge J\), it uses only the \(p\) repeated paths: the value \(H\) is **independent of \(b\)**, despite the additional path becoming arbitrarily long. Else it uses every path. The long-path saturation regime occurs at finite \(b\) precisely when \(a(p-2)>2(p-1)\), beginning at
\[
 b\ge\frac{ap(a-2)}{a(p-2)-2(p-1)}.
\]
For the equal-length case \(b=a\), the formula specializes to
\[
 \lambda(L)=1+\frac{p}{p+1}\left(2-\frac2a\right).
\]
For \(a=b=2\), this is \(2-1/(p+1)\), the known first-level multibranch diamond value, included only for calibration.

## Assumptions and scope

All graphs are finite, simple, unweighted, with the stated numbers of paths and lengths; the field is \(\mathbb R\). Projections are **linear**, and target superspaces and projection operators are otherwise unrestricted. The \(\ell_\infty\) ambient edge copy is defined using the canonical orientation of each entire path from the first pole to the second. If \(D\) is the oriented incidence matrix, define \(Z=\ker D\subset\ell_1(E)\) and \(C_E=Z^\perp=\operatorname{im}D^{\mathsf T}\subset\ell_\infty(E)\). The edge-gradient map is an isometry \(L\cong C_E\), because the Lipschitz norm for a shortest-path graph is the largest absolute edge difference.

## Proof

**Step 1: from absolute projection constant to a complementary cycle projection.** Because finite-dimensional \(\ell_\infty(E)\) is \(1\)-injective, the absolute projection constant of its subspace \(C_E\) equals the relative constant \(\lambda(C_E,\ell_\infty(E))\). For any projection \(P:\ell_1(E)\to Z\), the adjoint \((I-P)^*\) projects \(\ell_\infty(E)\) onto \(Z^\perp=C_E\), with norm \(\|I-P\|_{1\to1}\). Conversely, the adjoint of every projection onto \(C_E\) has kernel \(Z\), so its complementary operator projects onto \(Z\). Therefore
\[
 \lambda(L)=\min_{P^2=P,\ \operatorname{ran}P=Z}\|I-P\|_{1\to1}.
\]
This is **not** the ordinary minimum \(\|P\|\), a distinct invariant for which general hyperplane methods exist.

**Step 2: exact symmetry reduction.** Orient every path consistently from the first pole to the second. By flow conservation at internal vertices, each vector in \(Z\) has a constant coefficient on each path. The path coefficients \(z_1,\ldots,z_{p+1}\) satisfy \(\sum_i z_i=0\). Coordinate permutations of the edges within each path are \(\ell_1(E)\)-isometries fixing \(Z\) pointwise, even though they need not be graph automorphisms. The additional symmetric group permutes the first \(p\) paths. Averaging any minimizing projection over this finite group does not increase \(\|I-P\|\) and keeps it a projection onto \(Z\). A group-invariant projection must first average coordinates along each path, and then apply a linear projection onto the hyperplane \(\sum_i z_i=0\). Every such hyperplane projection is \(u\mapsto u-\gamma\sum_i u_i\), where \(\sum_i\gamma_i=1\). Symmetry forces \(\gamma_1=\cdots=\gamma_p=x\) and \(\gamma_{p+1}=1-px\), for some real \(x\).

For an input basis vector on path \(j\) of length \(\ell_j\), the resulting flow projection is constant on path \(i\) with coefficient \((\delta_{ij}-\gamma_i)/\ell_j\). Hence the \(\ell_1\)-norm of the corresponding column of \(I-P\) is exactly
\[
 |1-(1-\gamma_j)/\ell_j|
 +(\ell_j-1)|1-\gamma_j|/\ell_j
 +\sum_{i\ne j}\ell_i|\gamma_i|/\ell_j.
\]
The operator norm is the maximum of the two orbitwise column norms.

**Step 3: restriction of the one-dimensional optimization.** If \(x<0\), the columns from a repeated path have norm at least their norm at \(x=0\): as \(x\) decreases, the own-path contribution \(|1-t|+(a-1)|t|\) with \(t=(1-x)/a\ge1/a\) is nondecreasing, while all off-path absolute contributions increase. If \(x>1/p\), the norms of both types of columns are nondecreasing as \(x\) increases. For exceptional-path columns this follows by writing the own-path contribution as \(|1-t|+(b-1)t\), where \(t=px/b\ge1/b\). For repeated-path columns, the derivative on \([1/p,1]\) equals \(p-2+2/a+pr>0\), and for \(x\ge1\) all contributions are increasing. Therefore some global minimum has \(0\le x\le1/p\).

On this interval the repeated-path column norm is exactly \(C+h x\), and the exceptional-path column norm is exactly \(1+B x\). Thus
\[
 \lambda(L)=\min_{0\le x\le1/p}\max\{C+h x,\ 1+B x\}.
\]
Notice \(C>1\) and \(B>0\). If \(h\ge0\), both affine functions are nondecreasing, and \(x=0\) attains \(C\). If \(h<0\), the first decreases and the second increases. Their crossing occurs at \(x_0=(C-1)/(B-h)>0\). If \(x_0<1/p\), the minimum is \(1+B(C-1)/(B-h)\). If \(x_0\ge1/p\), the minimum occurs at \(x=1/p\) and equals \(C+h/p=H\). Since \(1+B/p=J\), the last case is precisely \(H\ge J\). This proves all branches, including their common boundary values.

**Step 4: saturation and calibration.** The inequality \(H\ge J\) is equivalent to \(a(p-2)>2(p-1)\) and \(b\ge ap(a-2)/[a(p-2)-2(p-1)]\); the strict first inequality is needed because \(a-2\ge0\) and \(b<\infty\). In that regime the coefficient on the exceptional path vanishes at the optimizer. When \(b=a\), equality of path lengths allows averaging over all \(p+1\) paths, and the optimizer is \(x=1/(p+1)\), giving the displayed equal-length formula. No unproved limiting or extrapolation step is used.

## Verification

The standalone script `check_theta_projection.py` evaluates the exact candidate with rational arithmetic in 6,336 parameter triples (including all three regimes), verifies 82,368 additional rational test points and explicit full edge-column norms, and independently solves eight unrestricted finite-dimensional projection linear programs without imposing symmetry. All checks passed when replayed from the file included with this result. These calculations test finite instances only. The global symmetrization, hyperplane representation, absolute-value inequalities, and minimax calculation above supply the proof for all allowed integer parameters.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii (2020) establish exact projection constants of Lipschitz spaces over multibranch diamond graphs. Their first level gives \(a=b=2\) and is explicitly excluded from the novelty claim; the present result determines all uniform subdivisions and one exceptional path, with an additional sharp long-path saturation phenomenon. Their 2023 paper develops invariant cycle-space projections and treats primarily discrete tori and Hamming graphs; its general averaging framework is used here, but the one-defect theta calculation and piecewise formula do not occur in the inspected text. The related work of Basso (2021) connects Lipschitz extension and projection constants but does not specify the values for this graph family. Hyperplane formulas for \(\min\|P\|\) do not directly imply the asserted \(\min\|I-P\|\) over the enlarged edge space. The bibliography and close-comparison limitations are recorded in REVIEW.md.

## Limitations

No claim is made for arbitrary unequal lengths of all \(p+1\) paths, for weighted edges, for complex scalars, or for nonlinear projections. The formula is for the absolute **linear** projection constant of the real \(\operatorname{Lip}_0\) space, not a Lipschitz extension modulus for arbitrary target Banach spaces. Independent validation and exhaustive historical-priority certification have not been performed. Earlier results under different terminology may still exist.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949 (first posted 2020-07-15), especially §§1, 6. https://arxiv.org/abs/2007.07949
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first posted 2023-05-21), especially §§1.4, 2. https://arxiv.org/html/2305.12582v1
3. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first posted 2021-04-29), especially §§1–3. https://arxiv.org/abs/2104.14238
4. S. Foucart, *Computation of Minimal Projections and Extensions*, Numer. Funct. Anal. Optim. 37 (2016), 159–185; the hyperplane-\(\ell_1\) formula mentioned in §3.2 concerns a different projection objective. https://foucart.github.io/publi/CompMinExt.pdf
