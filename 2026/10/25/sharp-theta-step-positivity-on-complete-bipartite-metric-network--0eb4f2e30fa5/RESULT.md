# Sharp \(\theta\)-step positivity on complete-bipartite metric networks

## Finding

Let \(p,q\ge1\) be integers with \(m=\max\{p,q\}\ge2\). Realize each edge of \(K_{p,q}\) as a wire of common length \(\ell>0\), with unit thermal diffusivity and continuity/Kirchhoff conditions at vertices. Let \(M\) and \(K\) be the globally assembled continuous piecewise-linear **consistent** mass and stiffness matrices, with all vertices retained as degrees of freedom. For \(t\ge0\) and \(0\le\theta\le1\), let
\[
 T_\theta(t)=(M+\theta tK)^{-1}(M-(1-\theta)tK),\qquad x=t/\ell^2,
 \quad \theta_c(m)=1-\frac1{2m}.
\]
Here \(T_\theta(t)\ge0\) means every entry is nonnegative. Then the complete positivity classification is
\[
\boxed{\begin{aligned}
 T_\theta(t)\ge0\ \Longleftrightarrow\quad &t=0,\\
 &\text{or }\theta=\tfrac13\text{ and }x=\tfrac12,\\
 &\text{or }\tfrac13<\theta<\theta_c(m)\text{ and }\tfrac1{6\theta}\le x\le R_m(\theta),\\
 &\text{or }\theta_c(m)\le\theta\le1\text{ and }x\ge\tfrac1{6\theta},
\end{aligned}}
\]
where, in the finite-window regime, define
\[
 a_m(\theta)=18\theta\bigl(2m(1-\theta)-1\bigr)>0,\quad
 b_m(\theta)=m(15\theta-3)-3,\quad
 R_m(\theta)=\frac{b_m(\theta)+\sqrt{b_m(\theta)^2+4a_m(\theta)m}}{2a_m(\theta)}.
\]
In particular, **no** positive step is positivity preserving for \(0\le\theta<1/3\); at \(\theta=1/3\) exactly one positive step is admissible, and it sends each vertex uniformly to the opposite bipartition. For \(\theta\ge\theta_c(m)\), there is no upper positivity restriction. Every \(T_\theta(t)\) has row sums one; entrywise positivity is therefore also the nodal maximum principle for a single homogeneous step.

For the Crank–Nicolson case \(\theta=1/2\), the sharp lower endpoint is \(x=1/3\). The finite upper endpoint depends only on the **larger** partition size, equals \((1+\sqrt3)/3\) when \(m=2\), and tends to \(2/3\) as \(m\to\infty\).

## Assumptions and scope

Each undirected edge has the exact local matrices
\[
 M_e=\frac\ell6\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
 K_e=\frac1\ell\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
The time-stepping parameter \(\theta\) and step \(t\) are real, and both partition sizes are integers. There are no Dirichlet constraints or mass lumping. The endpoint \(t=0\) always gives the identity. The two-vertex graph \(K_{1,1}\) is excluded because there is no pair of distinct vertices in one bipartition, and the stated sharp lower condition changes. The result concerns one completed step and its iterations with a *fixed* admissible step; it does not assert positivity of the continuous-time consistent-mass semigroup for small positive times.

## Proof

Write \(D\) for the degree diagonal and \(A\) for the adjacency matrix of \(K_{p,q}\). Summation of the local matrices gives
\[
 M=\frac\ell6(2D+A),\qquad K=\frac1\ell(D-A).
\]
The matrix \(M\) is strictly positive definite: each local mass matrix is positive definite and the connected graph has no isolated vertices. Hence \(M+\theta tK\) is invertible for the stated domain. The constant vector is a generalized eigenvector of \((K,M)\) with eigenvalue zero. The vector \(v\), equal to \(+1\) on the \(p\)-part and \(-1\) on the \(q\)-part, has generalized eigenvalue \(12/\ell^2\). Vectors summing to zero separately in either part have generalized eigenvalue \(3/\ell^2\). These mutually \(M\)-orthogonal subspaces exhaust the \(p+q\) dimensions, including the degenerate case of a singleton part.

Put \(\pi_j=1/(2p)\) for a vertex in the \(p\)-part, and \(\pi_j=1/(2q)\) for a vertex in the \(q\)-part. The mass-orthogonal projectors onto the constant and bipartite modes have entries \((\Pi_0)_{ij}=\pi_j\) and \((\Pi_{12})_{ij}=v_i v_j\pi_j\). Define
\[
 r_3=\frac{1-3(1-\theta)x}{1+3\theta x},\qquad
 r_{12}=\frac{1-12(1-\theta)x}{1+12\theta x}.
\]
The exact step is
\[
 T_\theta(t)=r_3 I+(1-r_3)\Pi_0+(r_{12}-r_3)\Pi_{12}.
\]
It follows that, for distinct vertices in opposite parts, \((T_\theta)_{ij}=\pi_j(1-r_{12})=12x\pi_j/(1+12\theta x)>0\) whenever \(x>0\). For distinct vertices in the same part,
\[
 (T_\theta)_{ij}=\pi_j(1+r_{12}-2r_3)
 =\pi_j\frac{6x(6\theta x-1)}{(1+3\theta x)(1+12\theta x)}.
\]
Because \(m\ge2\), such a pair exists. Hence any positive admissible step must satisfy \(\theta>0\) and \(x\ge1/(6\theta)\). Conversely, this condition makes every off-diagonal entry nonnegative.

For a diagonal vertex in a part of size \(s\in\{p,q\}\), direct substitution gives
\[
 (T_\theta)_{ii}=\frac{F_s(\theta,x)}{s(1+3\theta x)(1+12\theta x)},\qquad
 F_s=s+[s(15\theta-3)-3]x+18\theta[1-2s(1-\theta)]x^2.
\]
For \(x\ge1/(6\theta)\), the factor \(g=1+r_{12}-2r_3\) is nonnegative and the same diagonal may also be written \(r_3+g/(2s)\). It is therefore smallest for \(s=m\). Thus all diagonal entries are nonnegative exactly when \(F_m(\theta,x)\ge0\).

At the necessary lower boundary,
\[
 F_m\!\left(\theta,\frac1{6\theta}\right)=\frac{3m(3\theta-1)}{2\theta},\qquad
 \partial_xF_m\!\left(\theta,\frac1{6\theta}\right)=3\bigl(m(9\theta-5)+1\bigr).
\]
For \(0<\theta<1/3\), the first expression is negative, the second negative, and \(F_m\) is concave in \(x\); hence no \(x\) at or above the lower boundary qualifies. At \(\theta=1/3\), the factorization
\[
 F_m(1/3,x)=-(2x-1)\bigl((4m-3)x+m\bigr)
\]
leaves precisely \(x=1/2\). For \(1/3<\theta<\theta_c(m)\), the quadratic is strictly concave, is positive at the lower boundary, and tends to minus infinity, so its unique positive zero is \(R_m(\theta)\). For \(\theta\ge\theta_c(m)\), its quadratic coefficient is nonnegative, its linear coefficient is positive, and its constant is \(m>0\); hence the upper boundary disappears. These exhaust all cases, including \(\theta=0\), which fails at every positive step by the same-part formula. At \(\theta=1/3, x=1/2\), diagonal and within-part entries vanish, while each opposite-part entry equals the reciprocal of the opposite part's size.

Finally, for \(\theta=1/2\), dividing the positive-root equation by \(m\) and letting \(m\to\infty\) gives \(1+(9/2)x-9x^2=0\), whose positive root is \(2/3\). At \(m=2\), the equation is \(2+6x-9x^2=0\), giving \((1+\sqrt3)/3\).

## Verification

The accompanying standard-library script `verify_theta_biclique.py` independently assembles \(M\), \(K\) from their local edge contributions, inverts the step matrix by exact rational Gauss–Jordan elimination, and checks equality with the projector formula, row sums, and the scalar sign test. It passed **2,952 exact-rational matrix cases** with \(1\le p,q\le5\), excluding \(K_{1,1}\), including boundary points and several rational values of \(\theta\). SymPy algebra also independently factored the same-part and diagonal polynomials used in the proof. Finite checks do not establish the all-parameter theorem, which follows from the exact decomposition above.

Replay with `python verify_theta_biclique.py` using Python 3's standard library. The theorem requires no nondeterministic data, random seeds, numerical tolerances, or external scientific software.

## Relationship to prior work

Li and Huang (arXiv:1209.5657, original posting September 25, 2012) establish sufficient lower and upper time-step bounds for a conventional \(\theta\)-finite-element maximum principle on simplicial domains. Their Theorem 3.1 does not give an if-and-only-if classification for a Kirchhoff metric graph, its all-\(\theta\) isolated-step transition, or its largest-part-dependent upper threshold. Jin, Lazarov, Thomée, and Zhou (arXiv:1510.02825) analyze nonnegativity for ordinary and fractional diffusion on polygonal domains, including a general small-step obstruction; their Theorems 4.1–4.3 concern different operators and do not derive this three-eigenmode biclique classification. The closest previously documented exact graph-mesh cases are periodic or Dirichlet interval meshes and metric trees, none of which covers all equilateral complete bipartite graphs together with every \(\theta\). In particular \(K_{2,2}\) and \(\theta=1/2\) coincide with an already studied four-cycle case and are not claimed as separately new.

## Limitations

The result assumes a common edge length, unit diffusivity, no boundary elimination, and exactly the complete bipartite topology. It does not establish thresholds for arbitrary non-bipartite graphs, heterogeneous edge lengths, nonlinear equations, or mass-lumped formulations. A specialized 2015 positivity paper by Chatzipantelidis, Horváth, and Thomée could not be inspected in full; its available description concerns homogeneous Dirichlet finite elements rather than Kirchhoff networks, but its inaccessible detailed results remain a literature-coverage risk. The claim is analytically proved and computationally checked as stated; no independent audit or broader originality certification is asserted.

## References

- X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657 (public preprint, September 25, 2012), https://arxiv.org/abs/1209.5657.
- B. Jin, R. Lazarov, V. Thomée, and Z. Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, arXiv:1510.02825 (public preprint, October 9, 2015), https://arxiv.org/abs/1510.02825.
- P. Chatzipantelidis, Z. Horváth, and V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Computational Methods in Applied Mathematics **15** (2015), 417–437, DOI: 10.1515/cmam-2015-0018 (full text unavailable in this review).
