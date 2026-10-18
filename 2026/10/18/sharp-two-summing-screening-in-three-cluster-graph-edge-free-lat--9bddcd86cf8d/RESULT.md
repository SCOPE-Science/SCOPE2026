# Sharp two-summing screening in three-cluster graph-edge free lattices

## Finding

For integers \(a\ge2\) and \(b\ge1\), let \(G=K_{a,a,b}\), with two vertex classes \(A_1,A_2\) of size \(a\) and a third class \(B\) of size \(b\). In the real free two-convex Banach lattice over Euclidean space \(\ell_2^{2a+b}(\mathbb R)\), consider the natural positive element
\[
F_G=\bigvee_{\{u,v\}\in E(G)}\left|\delta_{e_u-e_v}\right|.
\]
It acts on a Euclidean dual vector \(z\) as \(F_G(z)=\max_{\{u,v\}\in E(G)}|z_u-z_v|\). Write
\[
H_{a,b}=\frac{b-1}{\sqrt b}+\sqrt{\frac1b+\frac1{2a}},\qquad
\Phi_{a,b}(s)=\frac{2(a-1)\sqrt{1+s}+\sqrt{1+3s}}{\sqrt{2a}}+H_{a,b}\sqrt{1-s}.
\]
**Theorem.** Its exact free-lattice norm, equivalently the absolutely two-summing norm of the graph edge-difference operator, is
\[
\boxed{\|F_G\|=\pi_2(D_G)=\max_{0\le s\le1}\Phi_{a,b}(s).}
\]
The unique maximizing parameter is \(s_*=0\) if and only if \(b\ge2a+2\). If \(1\le b\le2a+1\), the maximizer lies strictly between zero and one and is the unique solution of
\[
\boxed{\frac{H_{a,b}}{\sqrt{1-s_*}}=
\frac{2(a-1)}{\sqrt{2a(1+s_*)}}+
\frac3{\sqrt{2a(1+3s_*)}}.}
\]
For \(b\ge2a+2\), all edges between \(A_1\) and \(A_2\) can be omitted without changing the norm:
\[
\boxed{\|F_G\|=\|F_{K_{2a,b}}\|=
\frac{2a-1}{\sqrt{2a}}+
\frac{b-1}{\sqrt b}+
\sqrt{\frac1{2a}+\frac1b}.}
\]
For \(b\le2a+1\), the strict inequality \(\|F_G\|>\|F_{K_{2a,b}}\|\) holds. The elements themselves are not equal: for a vector equal to \(1\) on \(A_1\), \(-1\) on \(A_2\) and zero on \(B\), their values are \(2\) and \(1\), respectively. Thus the equal-norm phenomenon is a genuine screening of additional, pointwise active lattice generators.

## Assumptions and scope

All scalars are real. The vertex space is \(E=\ell_2^{n}(\mathbb R)\), where \(n=2a+b\), with its standard Hilbert norm and orthonormal coordinate vectors \(e_v\). The graph is simple, unweighted, and complete tripartite; its edge orientation is arbitrary. For a vertex vector \(x\), write \(\delta_x(z)=\langle x,z\rangle\) on \(E^*\simeq E\). The lattice symbol \(\bigvee\) is pointwise supremum. The free two-convex lattice norm is the explicit norm of Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky: for a positively homogeneous lattice function \(f\),
\[
\|f\|_{\operatorname{FBL}^{(2)}}=
\sup\left\{\left(\sum_{j=1}^N|f(z_j)|^2\right)^{1/2}:N\ge1,\ z_j\in E^*,\ \sup_{\|x\|_2\le1}\sum_{j=1}^N|\langle z_j,x\rangle|^2\le1\right\}.
\]
There is no restriction on the number of test vectors. The operator \(D_G:E\to\ell_\infty^{E(G)}\) has components \((D_Gx)_{uv}=x_u-x_v\). Its absolutely two-summing norm is denoted \(\pi_2(D_G)\). For an edge \(e=\{u,v\}\), put \(r_e=e_u-e_v\).

## Proof

**1. Exact spectral reduction without assuming symmetry.** For any finite set \(z_1,\ldots,z_N\) in the defining norm, let \(Z\) be the matrix with columns \(z_j\). The weak-two constraint is \(ZZ^{\mathsf T}\preceq I\). For each test vector, the maximization in \(F_G(z_j)\) selects an edge and a sign. Taking the dual of the Euclidean norm on the resulting list of scalar values gives coefficients \(\alpha_j\) with \(\sum_j\alpha_j^2=1\). For fixed choices and coefficients the unrestricted supremum over \(ZZ^{\mathsf T}\preceq I\) equals the nuclear norm of the matrix whose columns are \(\alpha_j r_{e_j}\), by the singular-value decomposition and the duality between operator and nuclear norms. Writing \(\mu_e=\sum_{j:e_j=e}\alpha_j^2\), the square of this matrix's singular values is the spectrum of \(L_\mu=\sum_e\mu_e r_er_e^{\mathsf T}\). Every probability vector \(\mu\) on the edge set is realized by choosing one test-vector column per edge. Compactness then gives the identity
\[
\|F_G\|=\pi_2(D_G)
=\max_{\mu_e\ge0,\ \sum_e\mu_e=1}\operatorname{tr}\sqrt{L_\mu}.
\tag{1}
\]
In particular, the supremum includes every nonsymmetric edge weighting and is attained; it is not a fixed unweighted graph-Laplacian energy.

**2. Reduction to two edge orbits.** The map \(L\mapsto\operatorname{tr}\sqrt L\) is concave on positive-semidefinite matrices. Conjugation by a coordinate permutation preserves its value. Averaging an arbitrary feasible weight vector over automorphisms of \(G\) therefore does not decrease (1). The edge set has two orbits: the \(a^2\) edges between \(A_1\) and \(A_2\), and the \(2ab\) edges between \(A_1\cup A_2\) and \(B\). An averaged optimizer places weight \(s/a^2\) on every edge of the first orbit, and \((1-s)/(2ab)\) on every edge of the second, for some \(s\in[0,1]\).

**3. Exact Laplacian spectrum.** On the zero-sum subspaces within \(A_1\) and \(A_2\) (combined dimension \(2(a-1)\)), within \(B\) (dimension \(b-1\)), on the difference of the two \(A\)-class means (dimension one), and on the contrast of the combined \(A\) class against \(B\) (dimension one), direct weighted-Laplacian multiplication yields, respectively,
\[
\begin{array}{c|c}
\text{eigenvalue of }L_\mu&\text{multiplicity}\\\hline
\dfrac{1+s}{2a}&2(a-1)\\
\dfrac{1-s}{b}&b-1\\
\dfrac{1+3s}{2a}&1\\
\dfrac{(2a+b)(1-s)}{2ab}&1.
\end{array}
\]
There is one additional zero eigenvalue (the constant vectors); the \(b-1\) row is absent when \(b=1\). Taking the sum of nonnegative square roots establishes \(\operatorname{tr}\sqrt{L_\mu}=\Phi_{a,b}(s)\), proving the one-dimensional exact norm formula.

**4. Strict concavity and the sharp integer cutoff.** The function \(\Phi_{a,b}\) is strictly concave on \([0,1]\): its first nonconstant square-root term alone is strictly concave and all the others are concave. Its one-sided derivative tends to \(-\infty\) at \(s=1\), since \(H_{a,b}>0\). Thus there is exactly one maximizer, equal to zero if \(\Phi_{a,b}'(0)\le0\), and otherwise the unique interior root of the displayed first-order equation. Differentiating gives
\[
2\Phi_{a,b}'(0)=\frac{2a+1}{\sqrt{2a}}-H_{a,b}.
\tag{2}
\]
Put \(m=2a\ge4\), so \(H_{a,b}=(b-1)/\sqrt b+\sqrt{1/b+1/m}\). This is strictly increasing as a function of positive real \(b\), because
\[
\frac{\mathrm dH_{a,b}}{\mathrm db}
=\frac{b+1}{2b^{3/2}}-\frac1{2b^2\sqrt{1/b+1/m}}
\ge\frac1{2\sqrt b}>0.
\]
At \(b=m+1\), the inequality \(H_{a,m+1}<(m+1)/\sqrt m\) is equivalent to
\[
m+\sqrt{2+1/m}<(m+1)\sqrt{1+1/m}.
\]
The left side is at most \(m+3/2\), whereas the square of the right side exceeds \((m+3/2)^2\) by \(3/4+1/m>0\). At \(b=m+2\), the reverse strict inequality \(H_{a,m+2}>(m+1)/\sqrt m\) follows from
\[
\sqrt{2+2/m}>(m+1)(\sqrt{1+2/m}-1),
\]
because the right-hand side is at most \(1+1/m\) by concavity of the square root, while the left-hand side exceeds \(1+1/m\) for all \(m>1\). Strict monotonicity then proves that (2) is positive exactly for integer \(b\le2a+1\), negative exactly for \(b\ge2a+2\), and never zero at an integer parameter. The claimed threshold and uniqueness follow.

**5. Screening and nontriviality.** When \(s=0\), the sole positive-weight orbit is the complete-bipartite graph \(K_{2a,b}\). Formula (1), or the same spectral calculation with one edge orbit, gives the displayed bipartite norm. When \(s_*>0\), strict concavity implies \(\Phi_{a,b}(s_*)>\Phi_{a,b}(0)\). Finally the witness \(z=1\) on \(A_1\), \(z=-1\) on \(A_2\), \(z=0\) on \(B\) proves the two positive lattice elements are pointwise distinct, notwithstanding their equality of norms in the screened regime. This completes the proof.

## Verification

The standalone `verify.py` implements the defining weighted graph Laplacian rather than copying the spectral diagonalization. It checks 36 configurations using exact rational eigenspectra, 13 cases of unrestricted numerical optimization over all nonnegative edge weights, and 15 explicitly constructed polar-factor test families admissible in the original free-lattice norm. The checker prints these counts and requires Python 3 with NumPy, SymPy and SciPy. Invoke `python3 verify.py` in the same directory. Finite numerical comparisons and exact finite cases corroborate, but do not prove, the universal theorem, which follows from the preceding norm duality, concavity, exact spectral decomposition and scalar inequalities.

## Relationship to prior work

The explicit free two-convex Banach-lattice norm, including its relation to summing maps, originates with Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky (arXiv:2101.03510). The exact bipartite edge-difference norm and graph-level spectral estimates were known for simpler objects; neither yields the weighted three-orbit-to-two-orbit strictness boundary without solving the new trace-square-root optimization. The Laplacian-energy-like invariant of Chen and Hao concerns the square-root trace for a fixed unweighted graph, rather than maximization over probability distributions of edge weights. A published calculation for the same symmetric edge polytope of \(K_{a,a,b}\) optimizes the **logarithm of a determinant**, obtains a Löwner ellipsoid and screens the first edge orbit for \(b\ge2a+1\). It does **not** cover the current two-summing/free-lattice objective, for which the cutoff is \(b\ge2a+2\). The consecutive, differing integer cutoffs provide a direct distinction between the two invariants, not a renaming of the ellipsoid result.

## Limitations

The assertion concerns real scalars, exponent two, the Euclidean generator, exactly three complete-partite classes with two equal sizes, and the edge-generator lattice supremum. No assertion is made about other free-lattice exponents, complex scalars, arbitrary unequal class triples, all graphs, or uniqueness of the unrestricted optimal edge-weight distribution (only uniqueness of the averaged orbit-mass parameter is claimed). An equivalent characterization in other graph-design or operator-ideal literature remains possible despite the inspected comparisons. The exact tests are finite, and the floating-point unrestricted optimizations are corroboration only. No independent mathematical or bibliographic audit has been performed.

## References

- H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510v1, initially posted 2021-01-10, https://arxiv.org/abs/2101.03510.
- X. Chen and G. Hao, *Remarks on “Comparison between the Laplacian energy-like invariant and the Kirchhoff index”*, Electronic Journal of Linear Algebra 38 (2022), https://doi.org/10.13001/ela.2022.6383.
- *Exact Löwner ellipsoid and sharp screening transition for \(K_{a,a,b}\) symmetric edge polytopes*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoid-and-sharp-screening-transition-for-k-a-a--2ec3472028bb.
