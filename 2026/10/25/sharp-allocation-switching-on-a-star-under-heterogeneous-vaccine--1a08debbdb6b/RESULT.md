# Sharp allocation switching on a star under heterogeneous vaccine efficiency

## Finding
Let \(m\ge2\) be an integer, \(\mu>0\), \(s\in(0,1]\), \(\kappa>0\), and \(0<B\le s/\max\{1,\kappa\}\). For a geographic star with one center and \(m\) leaves, let the nonnegative vaccination resources obey \(v_0+\sum_{i=1}^m v_i=B\). Their effects on initially susceptible fractions are \(s-\kappa v_0\) at the center and \(s-v_i\) at leaf \(i\). With homogeneous local transmission rate \(\beta>0\), recovery rate \(\gamma>0\), symmetric edge mobility rate \(\alpha>0\), and \(\mu=\alpha/\beta\), minimize the largest eigenvalue of the epidemic growth matrix
\[
M(v)=\alpha L+\beta\operatorname{diag}(s-\kappa v_0,s-v_1,\ldots,s-v_m)-\gamma I,
\]
where \(L\) is the negative-semidefinite graph Laplacian of the star (one on every center–leaf off-diagonal and negative vertex degree on the diagonal).

The unique global minimizer has an equal allocation to every leaf. Define
\[
D_\kappa=(\sqrt\kappa-1)(m+\kappa^{-1/2}),\qquad
x_* =\min\left\{B,\max\left\{0,\frac{B+m\mu D_\kappa}{\kappa m+1}\right\}\right\}.
\]
Then \(v_0=x_*\) and \(v_i=(B-x_*)/m\) for every leaf.

For \(\kappa>1\), all resources go to the center exactly when \(B\le \mu D_\kappa/\kappa\); above that threshold the optimal strategy vaccinates every vertex. For \(0<\kappa<1\), all resources go equally to the leaves exactly when \(B\le-m\mu D_\kappa\); above that threshold every vertex is vaccinated. A transition within the physical budget interval exists only if the displayed critical budget is below \(s/\max\{1,\kappa\}\). For \(\kappa=1\) the optimal allocation is uniform for every positive budget.

In the interior regime \(0<x_*<B\), the minimized epidemic growth rate is exactly affine in the vaccination budget:
\[
\boxed{\lambda_*(B)=\beta\left[s-\frac{\kappa B+\mu m(\sqrt\kappa-1)^2}{\kappa m+1}\right]-\gamma.}
\]
This is an exact, nonperturbative phase diagram at any strictly positive mobility, not a small-budget approximation.

## Assumptions and scope
The model describes the early linearized infection growth rate, not eventual epidemic size. All locations have equal initial susceptible fraction \(s\); the center converts one resource unit into \(\kappa\) times the susceptible reduction delivered at each leaf. The total resource \(B\) is fixed and divisible; no delivery caps other than keeping the susceptible fractions nonnegative are active. The conservative condition \(B\le s/\max\{1,\kappa\}\) makes **every** nonnegative budget allocation biologically admissible, so no constraints are silently relaxed. Mobility and local transmission are positive. Recovery subtracts a common scalar and cannot change which allocation minimizes the largest eigenvalue. For budgets outside this interval, node-level caps may change the optimizer, and that problem is not included.

## Proof
Write \(\lambda_{\max}(M(v))=\beta[s+\Lambda(v)]-\gamma\), where
\[
\Lambda(v)=\lambda_{\max}\!\left(\mu L-\operatorname{diag}(\kappa v_0,v_1,\ldots,v_m)\right).
\]
The matrix inside the eigenvalue is symmetric, irreducible, and Metzler. Its largest eigenvalue is simple and has a strictly positive unit eigenvector. As a function of \(v\), the largest eigenvalue is convex because it is the supremum of affine Rayleigh quotients. In fact it is **strictly convex on the budget hyperplane**: along a nonzero feasible line direction \(h\), the diagonal perturbation is \(H=-\operatorname{diag}(\kappa h_0,h_1,\ldots,h_m)\). The standard symmetric simple-eigenvalue second-derivative formula is
\[
\Lambda''=2\sum_{j=2}^{m+1}\frac{|u_j^{\mathsf T}Hu_1|^2}{\Lambda-\lambda_j}\ge0.
\]
Equality requires \(Hu_1\) to be proportional to the positive vector \(u_1\), hence requires \(H\) to be a scalar matrix. But this and \(h_0+\sum_i h_i=0\) force \(h=0\). Thus the minimizer exists and is unique. Permuting leaves preserves the matrix up to a permutation similarity and preserves the budget, so uniqueness forces all leaf allocations to be equal.

Put \(x=v_0\) and \(y=(B-x)/m\), with \(0\le x\le B\). The \(m-1\) leaf-difference eigenvectors have eigenvalue \(A=-y-\mu\). The remaining invariant two-dimensional subspace of vectors constant over the leaves has symmetric matrix
\[
\begin{pmatrix}C&\sqrt m\,\mu\\\sqrt m\,\mu&A\end{pmatrix},\qquad
C=-\kappa x-m\mu.
\]
Its larger eigenvalue strictly exceeds \(A\) because \(\mu>0\). Therefore
\[
F(x)=\Lambda(x,y,\ldots,y)=\frac{A+C+\sqrt{(A-C)^2+4m\mu^2}}2.
\]
Set \(\Delta=A-C=\kappa x-(B-x)/m+(m-1)\mu\) and \(t=\kappa+1/m\). Direct differentiation gives
\[
F'(x)=\frac{1/m-\kappa}{2}+\frac{t\Delta}{2\sqrt{\Delta^2+4m\mu^2}},\qquad
F''(x)=\frac{2m\mu^2t^2}{(\Delta^2+4m\mu^2)^{3/2}}>0.
\]
The unique unconstrained stationary point is determined by
\[
\frac{\Delta}{\sqrt{\Delta^2+4m\mu^2}}=\frac{\kappa m-1}{\kappa m+1},
\]
which is equivalent, with the correct sign retained, to \(\Delta=\mu(\kappa m-1)/\sqrt\kappa\). Solving this linear relation gives the unclipped allocation \((B+m\mu D_\kappa)/(\kappa m+1)\). Strict convexity means clipping it to \([0,B]\) gives the **unique** constrained optimum. The stated critical budgets follow from the conditions that the stationary point is at or beyond an endpoint.

For an interior optimum, \(\sqrt{\Delta^2+4m\mu^2}=\mu(\kappa m+1)/\sqrt\kappa\). Substitute this and the stationary allocation into \(F\) to obtain
\[
F(x_*)=-\frac{\kappa B+\mu m(\sqrt\kappa-1)^2}{\kappa m+1},
\]
which establishes the affine branch. The endpoint branches, if needed for the full optimal objective, are exactly
\[
F(B)=-\frac{\kappa B+(m+1)\mu}{2}
+\frac{\sqrt{[\kappa B+(m-1)\mu]^2+4m\mu^2}}2,
\]
\[
F(0)=-\frac{B/m+(m+1)\mu}{2}
+\frac{\sqrt{[(m-1)\mu-B/m]^2+4m\mu^2}}2.
\]
These are used only in the parameter regimes selecting their respective endpoints.

## Verification
The accompanying standalone Python 3 program `verify.py` independently diagonalizes full star matrices by symmetric Jacobi rotations, tests all allocation classes and critical inequalities, compares 61 symmetric alternatives and sampled asymmetric allocations, and verifies exact-rational cases. On execution it reports `VERIFY_OK 20706 assertions`.

For example, with \(m=3\), \(\kappa=4\), \(\mu=1/5\), \(B=1/5\), and \(s=1\), the critical budget is \(7/40\). The unique optimum gives \(v_0=23/130\) and \(v_1=v_2=v_3=1/130\), and the reduced maximal eigenvalue is exactly \(-7/65\). For \(m=2\), \(\kappa=1/4\), \(\mu=1/10\), \(B=1/2\), and \(s=1\), the critical budget is \(2/5\), the optimum has \(v_0=1/15\), each leaf receives \(13/60\), and the reduced maximum is exactly \(-7/60\). The proof, not finite computation, establishes the result for all stated real parameters and all star sizes.

## Relationship to prior work
The symmetric graph-Laplacian epidemic matrix and geographic diffusion model are established in Bustamante-Castañeda, Caputo, Cruz-Pacheco, Knippel and Mouatamide (arXiv:1906.07449). That study evaluates isolation of individual nodes and some fixed pairs, rather than all divisible fixed-budget allocations with unequal delivery efficiency. Badaoui, Caputo, Cruz-Pacheco and Knippel (Axioms 13 (2024), 769) analyze vaccination through eigenvalue perturbation and graph examples, including stars, mostly under homogeneous susceptibility responses. The exact heterogeneous-efficiency star optimum, both sharp allocation-switching thresholds, uniqueness, and the affine post-switch budget law are not statements of their inspected analyses.

Preciado, Zargham, Enyioha, Jadbabaie and Pappas (arXiv:1303.3984) develop a general convex optimization framework for heterogeneous SIS vaccination in contact networks, with cost minimization subject to a stability rate. That is a related spectral-resource method, not the same Laplacian-mobility fixed-budget optimization or an explicit star phase diagram; it could nevertheless inspire a different derivation. The convexity and eigenvalue-sensitivity ingredients themselves are classical and are not claimed to be new.

## Limitations
This result is about initial linear growth under a specific symmetric, homogeneous-metapopulation SIR linearization and linear site-dependent vaccine delivery effectiveness. It does not address nonlinear cumulative cases, unstable vaccine responses, uneven baseline susceptibles, asymmetric mobility, continuous delivery over time, or node-specific dose caps that bind outside the specified budget range. The mathematical priority assessment is provisional; an unexamined general eigenvalue-allocation theorem may subsume this specialized explicit phase diagram. Independent scientific verification has not been performed.

## References
1. F. Bustamante-Castañeda, J.-G. Caputo, G. Cruz-Pacheco, A. Knippel, and F. Mouatamide, *Epidemic model on a network: analysis and applications to COVID-19*, arXiv:1906.07449 (first public version 2019-06-18); https://arxiv.org/abs/1906.07449 .
2. M. Badaoui, J.-G. Caputo, G. Cruz-Pacheco, and A. Knippel, *Mitigating an Epidemic on a Geographic Network Using Vaccination*, Axioms **13** (2024), 769; https://doi.org/10.3390/axioms13110769 .
3. V. M. Preciado, M. Zargham, C. Enyioha, A. Jadbabaie, and G. Pappas, *Optimal Vaccine Allocation to Control Epidemic Outbreaks in Arbitrary Networks*, arXiv:1303.3984 (2013); https://arxiv.org/abs/1303.3984 .
