# Sharp branching-capacity growth and a finite-depth correction for discrete tree Hardy operators

## Finding

Let \(b\ge2\) be an integer and let \(\mathcal T_{b,N}\) be the complete rooted \(b\)-ary tree of height \(N\ge1\). Associate each nonroot vertex with the edge leading into it. On counting-measure sequence spaces, define the ancestor summation map
\[
 (H_{b,N}g)(v)=\sum_{\substack{w\preceq v\\w\ne o}}g(w),\qquad v\ne o,
\]
where \(o\) is the root and \(w\preceq v\) means that \(w\) lies on the path from \(o\) to \(v\). For every fixed real \(1<p<\infty\),
\[
 \boxed{\lim_{N\to\infty}b^{-(N+1)/p}\|H_{b,N}\|_{\ell^p\to\ell^p}
 =\big[(b-1)(b^{1/(p-1)}-1)^{p-1}\big]^{-1/p}.}
\]
At the Hilbert exponent the first finite-height correction is also explicit:
\[
 \boxed{\|H_{b,N}\|_{2\to2}
 =\frac{b^{(N+1)/2}}{b-1}
 \left[1-\big(N(b-1)-1\big)b^{-(N+1)}
 +O_b(N^2b^{-2(N+1)})\right].}
\]
Equivalently, for the root-Dirichlet graph Laplacian \(L_{b,N}=D^*D\), with \((Df)(v)=f(v)-f(\operatorname{parent}(v))\) and \(f(o)=0\), its smallest eigenvalue is
\[
 \boxed{\lambda_{b,N}=(b-1)^2b^{-(N+1)}
 \left[1+\big(2N(b-1)-2\big)b^{-(N+1)}
 +O_b(N^2b^{-2(N+1)})\right].}
\]
The minimal eigenvalue has multiplicity exactly \(b\) on the full nonroot tree: each root-child branch provides one copy. The asymptotic constants depend on fixed \(b\) (and, in the first formula, fixed \(p\)); the claims do not assert uniformity as either parameter varies.

## Assumptions and scope

All sequence spaces use unweighted counting measure on the \(b+b^2+\cdots+b^N\) nonroot vertices. The operator includes the current vertex in its ancestor sum but excludes the root. For \(N\ge1\), its inverse is the parent-difference operator \(D\). The notation \(O_b(\cdot)\) means a constant that may depend on \(b\) but not on \(N\). The three displayed asymptotics concern \(N\to\infty\), with \(b\) fixed, and \(p\) fixed where applicable.

## Proof

**Sharp limit for every fixed \(1<p<\infty\).** For \(1\le i\le N\), put \(E_i=\sum_{|v|=i}|g(v)|^p\) and \(S_j=\sum_{i=1}^j b^{-i/(p-1)}\). The extension of all level-\(i\) values along their descendants to level \(j\ge i\) has \(\ell^p\) norm \(b^{(j-i)/p}E_i^{1/p}\). Minkowski followed by Hölder therefore gives
\[
 \left(\sum_{|v|=j}|(H_{b,N}g)(v)|^p\right)^{1/p}
 \le b^{j/p}\sum_{i=1}^j b^{-i/p}E_i^{1/p}
 \le b^{j/p}S_j^{(p-1)/p}\left(\sum_{i=1}^jE_i\right)^{1/p}.
\]
Consequently,
\[
 \|H_{b,N}\|_{p\to p}^p\le \sum_{j=1}^N b^j S_j^{p-1}.
\]
For the matching lower bound, choose \(g(v)=b^{-|v|/(p-1)}\). Then \(\|g\|_p^p=S_N\), and every output at depth \(j\) equals \(S_j\), so
\[
 \|H_{b,N}\|_{p\to p}^p\ge
 \frac{\sum_{j=1}^N b^j S_j^p}{S_N}.
\]
Since \(S_j\uparrow S_\infty=1/(b^{1/(p-1)}-1)\) and \(\sum_{j=1}^N b^j\sim b^{N+1}/(b-1)\), geometric-tail summation shows that both bounds, divided by \(b^{N+1}\), tend to \(S_\infty^{p-1}/(b-1)\). Taking \(p\)-th roots proves the first formula.

**Hilbert-space correction.** On functions vanishing at the root, \(D=H_{b,N}^{-1}\). Thus \(\|H_{b,N}\|_{2\to2}=\lambda_{b,N}^{-1/2}\), where \(\lambda_{b,N}\) is the minimum of the spectrum of \(D^*D\). Deleting the root separates \(D^*D\) into \(b\) identical blocks, one on each root-child branch. On any branch the inverse is strictly entrywise positive, because \((D^*D)^{-1}=HH^*\) there and any two vertices share their initial nonroot ancestor. Perron–Frobenius therefore makes the lowest eigenvalue simple *within each block*, with a strictly positive eigenvector invariant under all branch automorphisms. It is consequently radial: let \(u_j\) be its value at depth \(j\).

For \(1\le j<N\), and at the leaf level, respectively, the exact eigenvalue equations are
\[
 (b+1-\lambda)u_j-u_{j-1}-bu_{j+1}=0,\quad u_0=0,
 \qquad (1-\lambda)u_N-u_{N-1}=0.
\]
The admissible radial trial function \(u_j=1-b^{-j}\) gives \(\lambda=O_b(b^{-(N+1)})\) by the Rayleigh principle: its branch energy is \((b-1)(1-b^{-N})/b\), while its squared mass is \(\sum_{j=1}^N b^{j-1}(1-b^{-j})^2\asymp_b b^N\). In particular, for large \(N\) the characteristic roots \(r_+>r_->0\) of
\[
 br^2-(b+1-\lambda)r+1=0
\]
are real and approach \(1\) and \(1/b\), respectively. Since \(u_0=0\), the positive radial eigenvector is proportional to \(u_j=r_+^j-r_-^j\).

Put \(q=b^{-(N+1)}\) and \(t=1-r_+\). The characteristic equation and the leaf condition give *exactly*
\[
 r_+r_-=b^{-1},\qquad
 t\big((1-t)^{2N+1}+bq\big)=(b-1)q,\qquad
 \lambda=\frac{t(b-1-bt)}{1-t}.
\]
The Rayleigh bound and this last identity imply \(t=O_b(q)\). As \(Nq\to0\), Taylor expansion of the exact secular equation, with remainder uniformly \(O_b(N^2q^3)\) in \(t\), gives
\[
 t=(b-1)q+ig((2N+1)(b-1)^2-b(b-1)\big)q^2
 +O_b(N^2q^3).
\]
Substitution into the expression for \(\lambda\) yields
\[
 \lambda=(b-1)^2q\big[1+(2N(b-1)-2)q+O_b(N^2q^2)\big].
\]
Expanding its reciprocal square root proves both remaining formulas. Because the full operator is a direct sum of \(b\) identical root-child blocks, the smallest eigenvalue there has multiplicity \(b\), not one.

## Verification

The accompanying standalone `verify_tree_hardy.py` requires only Python 3's standard library and reports 195 finite numerical consistency assertions. It independently constructs finite ancestor-sum matrices, evaluates the exact secular relation with high-precision decimal arithmetic, and checks upper and lower \(\ell^p\) bounds for several branching factors, depths and exponents. The proof of the limits, positivity, block multiplicity and error terms is analytical; no finite computation is asserted to prove the asymptotic theorem.

## Relationship to prior work

Evans, Harris and Lang [1] studied continuous metric-tree Hardy integration, including boundedness and approximation-number limits as approximation rank increases on a fixed tree. The present operator instead acts on finite **counting-measure vertices**, with height increasing and fixed branching factor; its exact normalization and first finite-height correction do not follow from the inspected statements of [1]. Wang [2] supplied variational formulas and two-sided estimates for discrete mixed \(p\)-Laplacian eigenvalues on trees; the weighted homogeneous-tree example in that paper uses geometrically decaying vertex masses and does not state the unweighted growing-tree norm equivalent or its Hilbert correction. The earlier birth–death-tree Dirichlet study [3] is relevant but was accessible only at the abstract level, so its full statements were not ruled out.

There are algebraic similarities between different tree summation kernels. Such similarities can involve diagonal weights whose condition numbers grow exponentially with tree height; they therefore do not identify the singular norms under fixed counting measure. No claim of historical priority is made beyond the material compared.

## Limitations

The first formula requires fixed \(1<p<\infty\). The second-order statement is proved only for \(p=2\); a corresponding sharp second-order expansion for other \(p\) is not established. There is no assertion of simultaneous uniform asymptotics in \(b,p,N\). The accessible literature comparison cannot exclude a historically equivalent formulation in an unexamined source, especially [3]. The numerical script is a reproducibility check, not a proof certificate. Independent mathematical and historical verification has not been performed.

## References

[1] W. D. Evans, D. J. Harris and J. Lang, *The approximation numbers of Hardy-type operators on trees*, arXiv:math/0003215 (first submitted 2000-03-30), https://arxiv.org/abs/math/0003215.

[2] L. Wang, *Mixed eigenvalues of p-Laplacian on trees*, arXiv:1512.04770 (first submitted 2015-12-15), https://arxiv.org/abs/1512.04770.

[3] L. Wang and Y. Zhang, *The first Dirichlet eigenvalue of birth–death process on trees*, Statistics & Probability Letters (2013), DOI:10.1016/j.spl.2013.05.001. Full text not inspected.
