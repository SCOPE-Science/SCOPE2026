# Antipodal placement and a three-quarter allocation limit for two imperfect traps on a cycle

## Finding

Let \(n\ge3\) be an integer. A particle starts at vertex \(0\) of the cycle \(C_n\), and independently jumps from each vertex to either neighbor at rate \(D>0\) **per edge**. At vertex \(0\) it is killed at rate \(\kappa_0\ge0\), and at a distinct vertex \(d\in\{1,\ldots,n-1\}\) at rate \(\kappa_d\ge0\). The total reactivity \(K=\kappa_0+\kappa_d>0\) is prescribed. Let \(\tau\) denote the killing time, including the possibility of a jump before killing even though the particle starts at a reactive vertex.

For every placement and allocation, put \(C_d=Dn/[d(n-d)]\). The exact mean lifetime is
\[
\mathbb E_0\tau=\frac n2\,\frac{\kappa_d+2C_d}{\kappa_0\kappa_d+C_dK}.
\]
Among **all** placements \(d\) and nonnegative allocations with total \(K\), the only minimizing placements are \(d=\lfloor n/2\rfloor\) and \(d=\lceil n/2\rceil\) (one position for even \(n\)). For either minimizing placement, writing \(C_*=Dn/\lfloor n^2/4\rfloor\), the **unique** optimal allocation is
\[
\kappa_d^*=\frac{K}{2+\sqrt{4+K/C_*}},\qquad
\kappa_0^*=K-\kappa_d^*,
\]
and the exact global minimum is
\[
\boxed{\min_{d,\kappa_0+\kappa_d=K}\mathbb E_0\tau
=\frac nK\left(\frac12+\frac{1}{\sqrt{4+K\lfloor n^2/4\rfloor/(Dn)}}\right).}
\]
The remote trap is always strictly active, but receives **strictly less than one quarter** of the reactivity. At fixed \(n,D\), its fraction approaches \(1/4\) as \(K\downarrow0\) and \(0\) as \(K\to\infty\). In contrast, its absolute optimal rate grows as \(\sqrt{C_*K}\) in the latter regime. A single trap at the starting site, or two equally reactive traps anywhere, gives \(\mathbb E_0\tau=n/K\). The optimized two-trap lifetime is strictly smaller for every finite \(K>0\) and its ratio to \(n/K\) decreases from \(1\) to \(1/2\) as \(K/D\) increases.

## Assumptions and scope

The graph has precisely \(n\) labeled vertices, with the two usual cycle edges incident to each vertex. At each vertex, independent exponential clocks govern the two directed edge jumps, each of rate \(D\); at a reactive vertex an additional independent killing clock has the stated rate. Rates are measured in inverse time and need not be probabilities per visit. The two potential trap locations are distinct, and the initial state is exactly the local reactive site \(0\). Zero reactivity at either potential site is allowed as an allocation boundary. No assumption of a continuum scaling limit, resetting, other absorbing sites, or spatial averaging of the initial position is made.

## Proof

**Finite expected lifetime and the Poisson equation.** Write \(t_j=\mathbb E_j\tau\). The killed generator is the negative of the strictly positive definite matrix \(H=D L_{C_n}+\kappa_0 e_0e_0^{\mathsf T}+\kappa_d e_de_d^{\mathsf T}\): a vector with zero quadratic form would be constant on the connected cycle and vanish at a positive-rate site, hence would be zero. Therefore \(Ht=\mathbf1\) determines a unique finite vector of expected lifetimes.

**Exact two-point reduction.** On the arc \(0,1,\ldots,d\), the interior Poisson equations \(D(2t_j-t_{j-1}-t_{j+1})=1\) give
\[
t_x=\left(1-\frac xd\right)t_0+\frac xd\,t_d+\frac{x(d-x)}{2D},\qquad 0\le x\le d.
\]
The opposite arc of length \(n-d\) has the analogous interpolation from \(t_0\) to \(t_d\). At either trap vertex, substituting the two adjacent interpolations into \(Ht=\mathbf1\) gives
\[
(\kappa_0+C_d)t_0-C_dt_d=n/2,\qquad
-C_dt_0+(\kappa_d+C_d)t_d=n/2,
\]
where \(C_d=D(1/d+1/(n-d))=Dn/[d(n-d)]\). The determinant is \(\kappa_0\kappa_d+C_dK>0\). Cramer's rule gives the claimed formula for \(t_0=\mathbb E_0\tau\). The calculation also covers an arc of one edge, because its interior quadratic term is then identically zero.

**Allocation at a fixed separation.** Set \(y=\kappa_d\in[0,K]\), \(\kappa_0=K-y\) and \(C=C_d\). Then
\[
T(C,y)=\frac n2\frac{y+2C}{y(K-y)+CK},\qquad
\frac{\partial T}{\partial y}=
\frac n2\frac{y^2+4Cy-CK}{[y(K-y)+CK]^2}.
\]
The derivative numerator is strictly increasing on \([0,K]\), is negative at \(y=0\), and positive at \(y=K\). Thus there is exactly one minimizing allocation, the positive root
\[
y_C=\sqrt{4C^2+CK}-2C
=\frac K{2+\sqrt{4+K/C}}\in(0,K/4).
\]
Substitution, or the stationary relation \(y_C^2+4Cy_C=CK\), yields
\[
T(C,y_C)=\frac nK\left(\frac12+\frac1{\sqrt{4+K/C}}\right).
\]
The minimum is strictly increasing as a function of \(C>0\), since the reciprocal square-root term strictly increases with \(C\).

**Optimal separation and all equality cases.** For an integer \(d\in\{1,\ldots,n-1\}\), \(C_d=Dn/[d(n-d)]\) is minimized exactly at \(d=\lfloor n/2\rfloor\) and \(d=\lceil n/2\rceil\). The strict monotonicity of the optimized mean in \(C\) proves that these, and only these, are globally optimal placements. The unique fixed-separation allocation just found supplies the complete equality classification.

**Comparison and limiting laws.** Putting \(y=0\) or \(y=K/2\) in \(T(C,y)\) gives exactly \(n/K\). More precisely,
\[
T(C,y)-\frac nK=\frac{ny(2y-K)}{2K[y(K-y)+CK]},
\]
so every split assigning a positive minority of the budget to the remote trap improves on both benchmarks. At the optimizer, \(y_C/K=1/(2+\sqrt{4+K/C})\), which is strictly decreasing from \(1/4\) to zero as \(K/C\) increases. Expanding the exact expression, at fixed \(C\), gives \(y_C=K/4-K^2/(64C)+O(K^3)\) as \(K\downarrow0\), while \(y_C=\sqrt{CK}-2C+O(K^{-1/2})\) as \(K\to\infty\). Finally
\[
\frac{T(C,y_C)}{n/K}=\frac12+\frac1{\sqrt{4+K/C}}
\]
is strictly decreasing from \(1\) to \(1/2\). All limits refer to fixed graph and hopping rate, with only the total reactivity varied.

## Verification

`CHECK.py` uses an independent exact rational Gaussian-elimination implementation of the \(n\times n\) killed-generator Poisson equation. Running `python3 CHECK.py` verifies the closed formula against **270 exact rational linear-system solutions**, tests **6,750 seeded alternate placements/rates** against the analytical optimum, checks the one-trap/equal-split identities, and probes the limiting regimes. The outputs support the calculation; neither random sampling nor a finite collection of graph sizes proves the universal optimizer. That conclusion follows from the monotone derivative calculation and exact integer maximization in the proof.

## Relationship to prior work

Aspelmeier, Magnin, Graupner, and Täuber (arXiv:cond-mat/0107434, public first version 2001-07-20) analyze imperfect traps and a **one-trap** decoupled-ring approximation, with late-time survival as the objective. Their single-ring model and its physical motivation do not supply a two-reactive-site fixed-budget mean-time optimizer. Condamin, Tejedor, and Bénichou (arXiv:0806.0453, 2008) derive exact occupation-time and imperfect-target reaction results for finite geometries with an absorbing target; their stated quantity is not the present simultaneous choice of **two** finite killing rates and their separation to minimize the lifetime of a particle started at one trap.

Robledo and Woodhouse (J. Stat. Phys. 19, 129–147, 1978) study multiple trapping and report exactly solvable equally spaced trapping on rings. Evans and Nord (Phys. Rev. A 32, 2926–2943, 1985) develop multi-trap walk-length calculations with **perfect** absorbers. Abad and Kozak (Phys. Rev. E 91, 022106, 2015) analyze a distinct setup with a deep trap and partially reactive remaining sites, including a one-dimensional case. The available abstracts do not establish the above two-imperfect-trap resource optimization. Their full texts were not all accessible in this examination, so equivalence hidden in broader formulas remains a historical-priority risk.

A related publicly indexed result, *All-coupling equidistant maximizer for repulsive point interactions on a loop*, optimizes a Schrödinger **ground-state eigenvalue** for identical repulsive point interactions. Its equal-spacing result does not determine the **source-specific mean lifetime** or the **asymmetric optimal reactivity split** for the killed Markov chain considered here. More generally, standard finite-state resolvent formulas justify computing lifetimes but do not themselves supply the optimized closed form or its sharp allocation and strong/weak-resource laws.

## Limitations

This is a fixed-source, fixed-total-local-killing-rate problem on a homogeneous undirected cycle; it makes no claim about general finite networks, optimizing the principal decay eigenvalue, capture probability before a deadline, or mean time from a uniform initial state. The result is self-contained but its historical priority is provisional: potentially relevant older and broader works were not all available for complete full-text comparison. No independent external scientific audit or certification is asserted.

## References

1. T. Aspelmeier, J. Magnin, W. Graupner, and U. C. Täuber, *Random walks with imperfect trapping in the decoupled-ring approximation*, arXiv:cond-mat/0107434 (first version 2001-07-20), https://arxiv.org/abs/cond-mat/0107434.
2. S. Condamin, V. Tejedor, and O. Bénichou, *Occupation times of random walks in confined geometries: From random trap model to diffusion limited reactions*, arXiv:0806.0453 (2008), https://arxiv.org/abs/0806.0453.
3. A. Robledo and L. Woodhouse, *Multiple trapping of random walkers on periodic lattices*, Journal of Statistical Physics 19, 129–147 (1978), doi:10.1007/BF01012507.
4. J. W. Evans and R. S. Nord, *Random walks on finite lattices with multiple traps: Application to particle-cluster aggregation*, Physical Review A 32, 2926–2943 (1985), doi:10.1103/PhysRevA.32.2926.
5. E. Abad and J. J. Kozak, *Competing reaction processes on a lattice as a paradigm for catalyst deactivation*, Physical Review E 91, 022106 (2015), doi:10.1103/PhysRevE.91.022106.
