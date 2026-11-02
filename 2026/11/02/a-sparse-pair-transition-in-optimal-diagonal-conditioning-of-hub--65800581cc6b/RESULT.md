# A sparse-pair transition in optimal diagonal conditioning of hub matrices

## Finding

Consider a positive-definite correlation matrix formed from \(m\ge2\) disjoint pairs of leaves and one hub. Every diagonal entry is \(1\), every hub–leaf entry is \(a>0\), each paired-leaf entry is \(b\in(0,1)\), and all other off-diagonal entries are zero. Suppose \(2ma^2<1+b\). Write
\[
 c^2=2ma^2,\qquad v=1+b,\qquad \theta=\frac{4b^2}{1+b}.
\]
Among **all** positive diagonal congruence scalings, without any symmetry restriction, the spectral condition number has a unique minimizer up to a common positive scalar. It has the form
\[
D_*=\operatorname{diag}(\sqrt{t_*},1,\ldots,1),\qquad
 t_*=\begin{cases}
 \dfrac{2b(1-b)}{2b-c^2},&c^2\le\theta,\\[2mm]
 1+b,&c^2\ge\theta.
 \end{cases}
\]
The formula agrees on the boundary. The exact best condition number is
\[
\kappa_*=
\begin{cases}
 \dfrac{\frac{2b(1-b)}{2b-c^2}+2b}{1-b},&c^2\le\theta,\\[3mm]
 \dfrac{\sqrt{1+b}+c}{\sqrt{1+b}-c},&c^2\ge\theta.
\end{cases}
\]
Consequently the unit-diagonal Jacobi scaling is globally optimal **if and only if** \(ma^2=b^2\). This is a sharp, dimension-dependent criterion, not an assumption that diagonal equilibration is generically optimal.

## Assumptions and scope

Index the real symmetric matrix \(A\) by \(0\) and \((j,+),(j,-)\) for \(1\le j\le m\). Its nonzero entries are \(A_{ii}=1\), \(A_{0,(j,\pm)}=A_{(j,\pm),0}=a\), and \(A_{(j,+),(j,-)}=A_{(j,-),(j,+)}=b\). All unspecified off-diagonal entries vanish. The parameter domain is \(m\in\mathbb Z\), \(m\ge2\), \(0<b<1\), \(a>0\), and \(2ma^2<1+b\). The objective is \(\kappa_2(DAD)=\lambda_{\max}(DAD)/\lambda_{\min}(DAD)\) over every diagonal \(D\) with strictly positive entries. Uniqueness is modulo replacing \(D\) by \(sD\) for \(s>0\). No claim is made for general nonsymmetric matrices, indefinite matrices, or block-diagonal (non-diagonal) preconditioners.

## Proof

**Spectral decomposition.** Put \(c=\sqrt{2m}\,a\) and \(v=1+b\). The subspace antisymmetric within each leaf pair has eigenvalue \(1-b\), multiplicity \(m\). The differences of constant-on-pair vectors have eigenvalue \(v\), multiplicity \(m-1\). The remaining two-dimensional block is \(\begin{psmallmatrix}1&c\\c&v\end{psmallmatrix}\), so the stated assumptions are exactly those needed for positive definiteness.

**Unrestricted-to-orbit reduction.** For \(K\ge1\), the existence of a scaling \(D\) of condition number at most \(K\) is equivalent to the existence of a positive diagonal \(S\) with \(S\preceq A\preceq KS\). Indeed, given \(D\), choose \(S=\lambda_{\min}(DAD)D^{-2}\), and conversely choose \(D=S^{-1/2}\). The set of such \(S\) is convex and invariant under all permutations of leaf pairs and swaps inside pairs. Averaging therefore produces an orbit-constant feasible \(S\), and hence an orbit-constant optimal \(D\). After dividing by a common scalar, every such \(D\) is \(D(t)=\operatorname{diag}(\sqrt t,1,\ldots,1)\), with \(t>0\).

**Exact scalar minimization.** The eigenvalues of \(D(t)AD(t)\) are \(1-b\), \(v\), and
\[
\lambda_\pm(t)=\frac{t+v\pm\sqrt{(t-v)^2+4c^2t}}{2},
\]
with the preceding fixed eigenvalue multiplicities. Since \(\lambda_+(t)>v>\lambda_-(t)>0\), the condition number is \(\lambda_+(t)/\min\{\lambda_-(t),1-b\}\). Both \(\lambda_+(t)\) and \(\lambda_-(t)\) increase strictly in \(t\): the derivative formula reduces strictness to \(4c^2(v-c^2)>0\). The quotient \(\lambda_+(t)/\lambda_-(t)\) has its unique minimum at \(t=v\): its determinant is \(t(v-c^2)\), and its trace divided by the square root of the determinant is \((t+v)/\sqrt{t(v-c^2)}\), uniquely minimized by arithmetic–geometric mean equality at \(t=v\).

At \(t=v\), \(\lambda_-(v)=v-c\sqrt v\). When \(c^2\ge4b^2/v\), this is at most \(1-b\). The pair quotient decreases until \(v\) and increases afterward, while any later transition to the fixed minimum \(1-b\) leaves the quotient increasing. Thus \(t_*=v\). When \(c^2<4b^2/v\), the increasing eigenvalue \(\lambda_-(t)\) crosses \(1-b\) at the unique \(t_c=2b(1-b)/(2b-c^2)<v\). Below that point the pair quotient decreases; above it \(\lambda_+(t)/(1-b)\) increases. Thus \(t_*=t_c\). The boundary has \(t_c=v\). Substituting yields both formulae for \(\kappa_*\).

**Uniqueness without a symmetry assumption.** Let \(K=\kappa_*\) and let \(S\) be any diagonal feasible matrix with \(S\preceq A\preceq KS\). Averaging its orbit yields \(\bar S\), which is feasible and must have generalized eigenvalues attaining both endpoints \(1\) and \(K\), by minimality of \(K\). Because \(A\) has nonnegative entries and its positive off-diagonal graph is connected, the top generalized eigenvector \(u\) of \((A,\bar S)\) is strictly positive. Each matrix \(KS_g-A\), for the automorphic images \(S_g\), is positive semidefinite. Their average annihilates \(u\), hence every \(KS_g-A\) annihilates \(u\). Componentwise \((KS_g)_{ii}=(Au)_i/u_i\), independent of \(g\). Consequently \(S=\bar S\) is orbit-constant. The scalar minimizer above is unique, proving unrestricted uniqueness up to common scaling.

**Jacobi frontier.** The unit-diagonal matrix \(A\) has Jacobi scaling \(I\). The second branch has \(t_*=1+b>1\); the first has \(t_*=1\) exactly when \(c^2=2b^2\), or \(ma^2=b^2\). For \(0<b<1\), this equality is always within the first branch, since \(2b^2<4b^2/(1+b)\). This proves the claimed equivalence.

## Verification

The standalone program `verify.py` reconstructs the complete matrix and its analytic spectrum for \(m=2,\ldots,8\), tests 126 deterministic admissible parameter sets, 12 alternate orbit scalings for each case, and 35 independently initialized unrestricted numerical optimizations. It records 1,799 numerical assertions. Computation corroborates, but does not replace, the all-parameter proof above. To replay: `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work

The general diagonal-condition-number problem and convex formulations are classical; see van der Sluis (1969), Shapiro (1985), and Braatz–Morari (1994). The present result is a graph-structured closed form with a sharp sparsity-sensitive transition and a dimension-dependent exceptional Jacobi-optimality locus. Its leaf interaction matrix consists of disjoint two-by-two correlated blocks, not a dense equicorrelation block. The known Jacobi optimality for bipartite or property-A matrices does not apply because every paired leaf and the hub form a triangle.

## Limitations

The result assumes a common positive hub–leaf correlation, a common positive paired-leaf correlation, and strict positive definiteness. It does not characterize arbitrary irregular pair couplings, negative paired correlations, nor fully general block transformations. The proof does not assert that earlier general scaling optimality criteria cannot be specialized to recover the formula; the priority of this particular explicit family has not been independently settled.

## References

1. A. van der Sluis, “Condition Numbers and Equilibration of Matrices,” *Numerische Mathematik* **14** (1969), 14–23. DOI: https://doi.org/10.1007/BF02165096 . Open full text: https://user.it.uu.se/~maney676/Courses/NLA/Projects/2014/VanderSluis1963.pdf .
2. A. Shapiro, “Optimal Block Diagonal \(l_2\)-Scaling of Matrices,” *SIAM Journal on Numerical Analysis* **22** (1985), 81–94. DOI: https://doi.org/10.1137/0722005 .
3. R. D. Braatz and M. Morari, “Minimizing the Euclidean Condition Number,” *SIAM Journal on Control and Optimization* **32** (1994), 1763–1768. DOI: https://doi.org/10.1137/S0363012992238680 .
4. L. Yu. Kolotilina, “Optimally conditioned block matrices,” *Linear Algebra and its Applications* **340** (2002), 55–67. DOI: https://doi.org/10.1016/S0024-3795(01)00412-8 .
