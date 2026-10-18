# Exact two-summing constants of complete-bipartite discrete gradients

## Finding
For all integers \(a,b\ge 1\), put \(n=a+b\), \(E=\ell_2^n(\mathbb R)\), and let \(e_1,\ldots,e_n\) be its standard unit vectors. In the real free 2-convex Banach lattice \(\operatorname{FBL}^{(2)}[E]\), form the positive lattice polynomial
\[
F_{a,b}=\bigvee_{1\le i\le a<j\le n}\bigl|\delta_{e_i}-\delta_{e_j}\bigr|.
\]
Its norm has the exact closed form
\[
\boxed{\|F_{a,b}\|=
\frac{a-1}{\sqrt a}+\frac{b-1}{\sqrt b}
+\sqrt{\frac1a+\frac1b}.}
\]
Equivalently, let \(D_{a,b}:\ell_2^{a+b}(\mathbb R)\to\ell_\infty^{ab}(\mathbb R)\) send a vector \(u\) to its complete-bipartite edge differences \((u_i-u_j)_{i\le a<j}\). Then its absolutely 2-summing norm equals the displayed quantity: \(\pi_2(D_{a,b})=\|F_{a,b}\|\).

In particular, \(\pi_2(D_{1,b})=(b-1+\sqrt{b+1})/\sqrt b\), \(\pi_2(D_{2,2})=1+\sqrt2\), and \(\pi_2(D_{m,m})=2\sqrt m+(\sqrt2-2)/\sqrt m\). Every value is attained by an explicitly defined family of exactly \(ab\) test vectors; no limiting argument is required.

## Assumptions and scope
All spaces and operators are real. Integers \(a,b\) are positive, and the edges have unit incidence coefficients. In the functional realization of the free lattice, \(\delta_{e_i}(u)=u_i\) for \(u\in E^*\simeq\ell_2^n\), so \(F_{a,b}\) is represented by the homogeneous function
\[
f_{a,b}(u)=\max_{1\le i\le a<j\le n}|u_i-u_j|.
\]
The normalization of the free 2-convex lattice is that of Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky, formula (1.1):
\[
\|F_{a,b}\|^2=
\sup_{N\ge1}\ \sup_{\substack{u_1,\ldots,u_N\in\mathbb R^n\\
\sum_{t=1}^N u_tu_t^{\mathsf T}\preceq I_n}}
\sum_{t=1}^N f_{a,b}(u_t)^2.
\tag{1}
\]
Here \(\preceq\) denotes positive-semidefinite order. The constraint is precisely the weak 2-summability constraint on the Euclidean dual, not a bound on the individual lengths of the \(u_t\). Formula (1) is also the definition of the absolutely 2-summing norm of \(D_{a,b}\), squared.

## Proof
Write \(A=\{1,\ldots,a\}\), \(B=\{a+1,\ldots,n\}\), and \(h_{ij}=e_i-e_j\) for every cross-edge. Define orthogonal projections \(P_A\) and \(P_B\) onto the respective coordinate-zero-sum subspaces, extended by zero on the other coordinate block. Define
\[
w=\frac1a\mathbf1_A-\frac1b\mathbf1_B,
\qquad c=\|w\|_2^2=\frac1a+\frac1b,
\qquad P_C=\frac{ww^{\mathsf T}}c.
\]
The three projection ranges are pairwise orthogonal, their dimensions are \(a-1\), \(b-1\), and \(1\), and
\[
P_A+P_B+P_C=I_n-\frac1n\mathbf1\mathbf1^{\mathsf T}\preceq I_n.
\tag{2}
\]
In the singleton-block cases the corresponding zero-dimensional projection is zero. Every cross-edge has the same squared projected lengths:
\[
\|P_Ah_{ij}\|_2^2=\frac{a-1}{a},\qquad
\|P_Bh_{ij}\|_2^2=\frac{b-1}{b},\qquad
\|P_Ch_{ij}\|_2^2=c.
\tag{3}
\]
Set
\[
S=\frac{a-1}{\sqrt a}+\frac{b-1}{\sqrt b}+\sqrt c.
\]
For each nonzero projection range, give it a strictly positive weight
\[
\lambda_A=\frac S{\sqrt a}\quad(a>1),\qquad
\lambda_B=\frac S{\sqrt b}\quad(b>1),\qquad
\lambda_C=S\sqrt c.
\]
The entries associated with zero-dimensional ranges are simply omitted. Equation (3) gives, for every edge,
\[
\sum_{H\in\{A,B,C\}}\frac{\|P_Hh_{ij}\|_2^2}{\lambda_H}=1,
\tag{4}
\]
where the sum is over the nonzero ranges. Orthogonality and weighted Cauchy–Schwarz now imply, for every \(u\in\mathbb R^n\),
\[
|\langle h_{ij},u\rangle|^2
\le \sum_H\lambda_H\|P_Hu\|_2^2.
\]
Take the edge maximum and then sum over an arbitrary admissible family in (1). We obtain
\[
\sum_t f_{a,b}(u_t)^2
\le\sum_H\lambda_H\operatorname{tr}\left(P_H\sum_t u_tu_t^{\mathsf T}\right)
\le \sum_H\lambda_H\operatorname{rank}(P_H)
=S^2.
\tag{5}
\]
This proves the upper bound for *every* finite test family, not merely symmetric families.

For attainment, the averaged edge covariance identity is
\[
\frac1{ab}\sum_{i\in A,j\in B}h_{ij}h_{ij}^{\mathsf T}
=\frac1aP_A+\frac1bP_B+cP_C.
\tag{6}
\]
To verify (6) without invoking representation theory, its left-hand side has diagonal blocks \(I_A/a\), \(I_B/b\) and off-diagonal blocks \(-\mathbf1_A\mathbf1_B^{\mathsf T}/(ab)\). On the right, the \(A\)-block of \(P_A/a\) is \(I_A/a-\mathbf1_A\mathbf1_A^{\mathsf T}/a^2\); the \(A\)-block of \(cP_C=ww^{\mathsf T}\) adds precisely \(\mathbf1_A\mathbf1_A^{\mathsf T}/a^2\). The \(B\) diagonal and both off-diagonal blocks agree by the same direct expansion. For each cross-edge define
\[
g_{ij}=\sum_H\frac{P_Hh_{ij}}{\lambda_H},
\qquad v_{ij}=\frac S{\sqrt{ab}}g_{ij}.
\tag{7}
\]
By (4), \(\langle h_{ij},g_{ij}\rangle=1\); hence \(f_{a,b}(v_{ij})\ge S/\sqrt{ab}\). Equation (6), the orthogonality of the projections, and the chosen weights give exactly
\[
\sum_{i\in A,j\in B}v_{ij}v_{ij}^{\mathsf T}
=\frac{S^2}{ab}\sum_{i,j}\sum_H\frac{P_Hh_{ij}h_{ij}^{\mathsf T}P_H}{\lambda_H^2}
=\sum_H P_H\preceq I_n.
\tag{8}
\]
Indeed, the coefficients on the three orthogonal blocks are respectively \(S^2/(a\lambda_A^2)=1\), \(S^2/(b\lambda_B^2)=1\), and \(S^2c/\lambda_C^2=1\); zero-dimensional blocks contribute nothing. Thus this family is admissible in (1), and
\[
\|F_{a,b}\|^2\ge\sum_{i,j}f_{a,b}(v_{ij})^2\ge ab\,\frac{S^2}{ab}=S^2.
\]
Combined with (5), this proves the asserted formula, including \(a=1\) or \(b=1\). Equality holds in every step, so the explicit vectors (7) give a finite exact norming certificate. \(\square\)

## Verification
The self-contained Python 3 program `verify_biclique.py` reconstructs the projections with rational matrices and checks (2), (6), their orthogonality, and the explicit norming family (7) for all \(1\le a,b\le8\). It then checks the computed edge values and covariance (8) to floating tolerance only where square roots arise. Run it using `python3 verify_biclique.py` from the directory containing this file. These tests exercise boundary cases, imbalanced blocks, and balanced blocks; they are diagnostics, not a substitute for the analytic proof for arbitrary \(a,b\).

## Relationship to prior work
Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky give the general free \(p\)-convex norm formula and investigate nonlinear summing norms, thereby implying the variational characterization (1). The exact complete-bipartite evaluation of that variational formula, the three-subspace optimal weighting, and its explicit \(ab\)-vector norming certificate are the claims established here; the general representation itself is not claimed to be new. Oikhberg, Taylor, Tradacete and Troitsky study functional realizations and induced operators in free \(p\)-convex lattices, but the examined material does not provide this graph-gradient norm. Work on Lipschitz \(p\)-summing maps concerns distinct metric-map formulations and does not directly furnish the equality above.

## Limitations
The result is restricted to real scalars, the Euclidean generating space, \(p=2\), and complete bipartite edge sets with unit coefficients. It does not assert a matching expression for other graph families, exponents, or complex scalars. The numerical verifier checks only a finite parameter range. Existing literature may contain equivalent formulas under a different operator-ideal or frame-optimization vocabulary; absence from searched sources is not a proof of novelty. An independent scientific audit has not been performed.

## References
1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510v1 (first posted 2021-01-10), especially the free \(p\)-convex norm formula (1.1) and Sections 6–7. https://arxiv.org/abs/2101.03510 ; https://doi.org/10.1007/s13398-021-01155-8
2. T. Oikhberg, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices*, Journal of the European Mathematical Society, https://doi.org/10.4171/JEMS/1552.
3. M. A. Saleh Saleh, *Computations of Lipschitz summing norms and applications*, Colloquium Mathematicum, https://doi.org/10.4064/cm8096-3-2020 (comparison of metric-map, rather than linear Hilbert-to-\(\ell_\infty\), summing norms).
