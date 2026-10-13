# Exact star-conditioned elliptope–cut gaps for a leaf-clique objective

## Finding

Fix an integer \(n\ge2\) and a parameter \(0\le\varepsilon\le\tfrac12\). On vertices \(\{0,1,\ldots,n\}\), where \(0\) is the hub, put
\[
F(X)=\frac12\sum_{1\le i<j\le n}(1-X_{ij}),\qquad
\mathcal E_{n,\varepsilon}=\{X\in\mathbb S^{n+1}_{+}: X_{ii}=1,\ X_{0i}\ge1-2\varepsilon\ (1\le i\le n)\}.
\]
Let \(R_0\) maximize \(F\) over \(\mathcal E_{n,\varepsilon}\). Let \(R_\triangle\) maximize it over the same set strengthened by **all** metric triangle and perimeter inequalities in \(d_{ij}=(1-X_{ij})/2\). Let \(C\) maximize it over the intersection of the same hub constraints with the cut polytope
\[
\operatorname{Cut}_{n+1}=\operatorname{conv}\{ss^{\mathsf T}:s\in\{-1,1\}^{n+1}\}.
\]
The three optimal values are exactly
\[
\boxed{R_0(n,\varepsilon)=n^2\varepsilon(1-\varepsilon)},
\]
\[
\boxed{R_\triangle(n,\varepsilon)=
\begin{cases}
n(n-1)\varepsilon,&n\ge2,\quad 0\le\varepsilon\le1/n,\\
2,&n=3,\quad 1/3\le\varepsilon\le1/2,\\
n^2\varepsilon(1-\varepsilon),&n\ge4,\quad1/n\le\varepsilon\le1/2,
\end{cases}}
\]
and, writing \(t=n\varepsilon\), \(k=\lfloor t\rfloor\), and \(\alpha=t-k\),
\[
\boxed{C(n,\varepsilon)=(1-\alpha)k(n-k)+\alpha(k+1)(n-k-1)}.
\]
The formulas agree at their shared endpoints. Their sharp **additive** triangle-strengthened gap is
\[
\boxed{R_\triangle-C=
\begin{cases}
0,&n\le3\text{ or }\varepsilon\le1/n,\\
\alpha(1-\alpha),&n\ge4,\quad\varepsilon\ge1/n.
\end{cases}}
\]
In particular, the bound \(0\le R_\triangle-C\le1/4\) holds for all allowed parameters, and the upper value is attained for every \(n\ge4\), for example at \(\varepsilon=3/(2n)\). The smallest total vertex count with a positive gap is five. These are support-function comparisons of *convex* sets under the indicated marginal constraints; they are not claims about the integer optimum when each hub constraint is imposed on an individual deterministic cut.

## Assumptions and scope

Every matrix is real and symmetric; \(X\succeq0\) means positive semidefinite; \(X_{ii}=1\) is imposed on all \(n+1\) vertices. The only positively weighted objective edges join distinct leaves (unit weights); the hub edges serve as correlation constraints, not objective edges. The same tolerance is imposed individually on all hub–leaf entries. The cut-polytope comparator permits a **distribution of cuts** for which \(\mathbb P\{s_i\ne s_0\}\le\varepsilon\) separately for every leaf. By contrast, a deterministic cut subject to those inequalities would have zero objective for \(\varepsilon<1\); no such comparison is asserted here.

The triangle strengthening includes, for all distinct \(i,j,k\), the inequalities \(d_{ij}\le d_{ik}+d_{kj}\) and \(d_{ij}+d_{ik}+d_{jk}\le2\). No stronger pentagonal, hypermetric, or higher-order cuts are assumed. The theorem holds for every integer \(n\ge2\) and every real \(\varepsilon\in[0,1/2]\), not only rational parameters or tested sizes.

## Proof

**1. Symmetrization and the positive-semidefinite envelope.** The feasible sets are convex and invariant under all permutations of leaves, and \(F\) is permutation invariant. Averaging any feasible matrix over these permutations preserves feasibility and its objective. Thus each optimum has a representative with common hub–leaf correlation \(a=1-2p\) and common leaf–leaf correlation \(b=1-2q\), where \(0\le p\le\varepsilon\). In hub/leaf blocks this matrix is
\[
X=\begin{pmatrix}1&a\boldsymbol1^{\mathsf T}\\a\boldsymbol1&(1-b)I_n+b\boldsymbol1\boldsymbol1^{\mathsf T}\end{pmatrix}.
\]
Its Schur complement with respect to the upper-left entry has eigenvalues \(1-b\) (multiplicity \(n-1\)) and \(1+(n-1)b-na^2\) (multiplicity one). Consequently, for \(0\le p\le1/2\), the largest feasible \(q\) is
\[
q_{\rm psd}(p)=\frac{2n}{n-1}p(1-p).
\]
It lies in \([0,1]\) for all such \(p\) and is nondecreasing. The objective is \(\binom n2q\), giving \(R_0=n^2\varepsilon(1-\varepsilon)\). To attain it, choose a hub unit vector \(u_0\), residual unit vectors \(v_1,\ldots,v_n\perp u_0\) with \(v_i\cdot v_j=-1/(n-1)\) for \(i\ne j\) (regular simplex), and set \(u_i=a u_0+\sqrt{1-a^2}\,v_i\) with \(a=1-2\varepsilon\). Their Gram matrix attains the envelope.

**2. Exact triangle strengthening.** With the same symmetric coordinates, every triangle containing the hub imposes \(q\le2p\), while any three leaves (when \(n\ge3\)) impose \(3q\le2\). The remaining symmetric triangle/perimeter conditions are automatic because \(p\le1/2\) and \(0\le q\le1\). Hence the largest possible \(q\) at fixed \(p\) is
\[
q_\triangle(p)=\min\left\{2p,\ \frac{2n}{n-1}p(1-p),\ \frac23\ (n\ge3)\right\}.
\]
All terms are nondecreasing on \([0,1/2]\); hence the maximum occurs at \(p=\varepsilon\). The first two meet at \(p=1/n\). For \(n\ge4\) the third bound is redundant, as \(q_{\rm psd}(p)\le n/[2(n-1)]\le2/3\). For \(n=3\), the third bound becomes active at \(p=1/3\) and remains active thereafter. For \(n=2\), the first branch extends to \(p=1/2\). Substitution gives the displayed formula for \(R_\triangle\). It is achieved by a valid positive-semidefinite symmetric matrix with \(a=1-2p\) and \(b=1-2q_\triangle(p)\). More concretely, below \(p=1/n\) it is a mixture of the all-aligned cut and the \(n\) single-flipped-leaf cuts; above this threshold for \(n\ge4\) the regular-simplex Gram construction from Step 1 satisfies the triangle inequalities. For \(n=3\) above \(1/3\), the equal mixture of three single-flipped-leaf cuts attains \(F=2\) within every larger tolerance.

**3. Exact cut-polytope slice.** In a cut distribution, fix the hub sign to \(+1\) without loss of generality and let \(S\subseteq\{1,\ldots,n\}\) be the random subset with sign \(-1\). Put \(K=|S|\); the hub bounds imply \(\mathbb EK\le n\varepsilon=t\). The clique cut size is exactly \(g(K)=K(n-K)\). The continuous piecewise-linear interpolation \(G\) of the discrete values \(g(k)=k(n-k)\) at integer arguments is concave and nondecreasing on \([0,n/2]\). Because \(g(K)=G(K)\), Jensen's inequality gives
\[
\mathbb E g(K)\le G(\mathbb EK)\le G(t)
=(1-\alpha)g(k)+\alpha g(k+1).
\]
The bound is attained by taking \(K=k\) with probability \(1-\alpha\), \(K=k+1\) with probability \(\alpha\), and conditionally choosing a uniformly random subset of that size. Then each individual leaf is flipped with probability exactly \(\mathbb EK/n=\varepsilon\). This proves \(C=G(t)\), including \(\varepsilon=0\), \(\varepsilon=1/2\), and all integer thresholds.

**4. Defect and sharpness.** Direct expansion of the chord interpolation yields the exact identity
\[
t(n-t)-G(t)=\alpha(1-\alpha).
\]
In the initial range \(t\le1\), \(R_\triangle=n(n-1)\varepsilon=G(t)\). For \(n=2\), this covers the entire parameter interval. For \(n=3\), both \(R_\triangle\) and \(G(t)\) are \(2\) once \(t\ge1\). For \(n\ge4\) and \(t\ge1\), Step 2 gives \(R_\triangle=t(n-t)\), and the displayed identity gives the gap. The elementary bound \(\alpha(1-\alpha)\le1/4\) is attained at \(t=3/2\), permitted whenever \(n\ge4\). Thus all transitions and the first possible positive-gap dimension are exact.

## Verification

The accompanying standalone Python script `verify.py` uses only the standard library for its main exact-rational tests. Run `python3 verify.py`; the expected output begins `VERIFY_OK` and reports 7,804 rational checks spanning \(2\le n\le24\), rational tolerances including all tested phase boundaries, exact Schur-complement and triangle feasibility, gap identities, discrete chord certificates, and small cut enumerations. An optional independent finite-dimensional LP test may be run with `python3 verify.py --lp` when NumPy and SciPy are installed; it checks 95 cut-polytope programs on \(2\le n\le6\). Both commands completed successfully when the files were prepared. These computations support but do not replace the proof for every real parameter and unbounded integer \(n\).

## Relationship to prior work

Mallach and Cohadari prove that exact \(\pm1\) correlations on a spanning tree force rank-one integrality of a MaxCut SDP correlation matrix; this theorem investigates **positive tolerances** on a star and an exact objective comparison among the bare elliptope, its triangle strengthening, and the cut-polytope slice. Avis, Devroye, and Deza compare the elliptope, metric polytope, and cut polytope by volume and record that their metric/cut relationships first separate at five vertices; that general distinction is prior knowledge, whereas the all-size hub-conditioned support values and exact \(\alpha(1-\alpha)\) profile are the present parameterized statement. Oliveira Filho and Vallentin study worst-case MaxCut SDP integrality ratios as a function of Gram rank, not this fixed hub-marginal slice. Campos, Misener, and Parpas study partial Lasserre strengthening; Makarychev, Pittu, and Vakilian impose **deterministic cardinality** constraints, as opposed to the present marginal constraints on cut mixtures. The known fixed-cardinality clique count \(k(n-k)\) is used here as an elementary ingredient, not presented as a separate discovery.

## Limitations

The result is specific to a unit-weight clique on the leaves, uniform hub-correlation tolerances, the full complete-graph correlation matrix, and all metric triangle inequalities. It does not establish a general integrality-gap bound for arbitrary weighted MaxCut instances, unequal hub tolerances, arbitrary spanning trees, deterministic branch constraints, or stronger cut families. In particular the comparator is \(\operatorname{Cut}_{n+1}\) **intersected with moment constraints**, not the convex hull of deterministic cuts individually obeying the same numeric constraints. No claim about computational speedup or new universal global MaxCut integrality ratios is made. Equivalent parameterized reductions in older cut-polytope literature cannot be entirely excluded without a comprehensive historical audit.

## References

1. S. Mallach and C. J. Cohadari, *On Spanning-Tree Integrality and a new Branching Rule for the Maximum Cut Problem*, Optimization Online, publicly posted 2026-09-17. https://optimization-online.org/wp-content/uploads/2026/09/ST_Preprint.pdf
2. D. Avis, L. Devroye, A. Deza, *On the volumes of the elliptope, metric polytope, and cut polytope*, arXiv:2604.16735 (2026). https://arxiv.org/pdf/2604.16735
3. F. M. de Oliveira Filho and F. Vallentin, *On the Integrality Gap of the Maximum-Cut Semidefinite Programming Relaxation in Fixed Dimension*, arXiv:1808.02346 (2018/2020). https://arxiv.org/pdf/1808.02346
4. J. S. Campos, R. Misener, P. Parpas, *Partial Lasserre relaxation for sparse Max-Cut*, Optimization and Engineering (2022/2023). https://link.springer.com/article/10.1007/s11081-022-09763-y
5. Y. Makarychev, M. R. Pittu, A. Vakilian, *Max-Cut with Multiple Cardinality Constraints*, arXiv:2507.12607 (2025). https://arxiv.org/pdf/2507.12607
