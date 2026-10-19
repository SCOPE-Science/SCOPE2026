# Sharp two-harmonic Morse–Smale window and an eight-point singularity transition

## Finding

For every integer \(N\geq1\), let \(K=(k_{ij})\) be a real symmetric, nonsingular matrix satisfying \(k_{ii}\geq\sum_{j\ne i}|k_{ij}|\) for every row. Write \(\lambda=\lambda_{\max}(K)\), fix \(c\geq0\), and put
\[
g_c(s)=\sin s+c\sin^3s,
\qquad
F_{c,h,K}(z)=z+hK\bigl(g_c(z_1),\ldots,g_c(z_N)\bigr)^{\mathsf T}\pmod{2\pi}.
\]
Define the piecewise-exact shape factor
\[
q(c)=\begin{cases}
1,&0\leq c\leq1/6,\\
\displaystyle\frac{2(1+3c)^{3/2}}{9\sqrt c},&c>1/6.
\end{cases}
\]
**Theorem.** Precisely for \(0<h<1/[\lambda q(c)]\), the family is a Morse–Smale diffeomorphism. It has exactly \(2^N\) hyperbolic fixed points \(\{0,\pi\}^N\), with \(\binom Nr\) having unstable dimension \(r\); every orbit converges to one of these fixed points, and the unique sink \((\pi,\ldots,\pi)\) has full Lebesgue basin. For every \(h\geq1/[\lambda q(c)]\), the map is **not a local diffeomorphism**. Thus this is the exact interval of Morse–Smale diffeomorphism parameters, not merely a sufficient small-step condition.

For the three-edge unit-weight star, take
\[
K_*=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix},
\qquad \lambda_{\max}(K_*)=4,
\qquad h_*(c)=\frac1{4q(c)}.
\]
At its first singular step \(h=h_*(c)\), the *entire* singular-Jacobian locus undergoes the following sharp splitting:
\[
\{z:\det DF_{c,h_*(c),K_*}(z)=0\}
=\begin{cases}
\{(\pi,\pi,\pi)\},&0\leq c\leq1/6,\\
\{s_+(c),s_-(c)\}^3,&c>1/6,
\end{cases}
\]
where
\[
u_c=\sqrt{\frac{1+3c}{9c}},\qquad
s_+(c)=\arccos(-u_c),\qquad
s_-(c)=2\pi-\arccos(-u_c).
\]
The second case consists of **eight distinct nonfixed points**. Every critical Jacobian has rank exactly two. The sink is still regular and hyperbolic at this singular step whenever \(c>1/6\), whereas the singular point is the sink when \(c\leq1/6\). The transition at \(c=1/6\) also changes the order of contact of the minimum derivative from quadratic to quartic.

## Assumptions and scope

The torus is \(\mathbb T^N=(\mathbb R/2\pi\mathbb Z)^N\); all maps are smooth. Diagonal dominance is the signed inequality displayed above (not only absolute diagonal dominance). Gershgorin's theorem and nonsingularity imply \(K\) is positive definite, so \(\lambda>0\). Every statement holds uniformly in finite dimension \(N\), every admissible \(K\), all \(c\geq0\), and every indicated \(h>0\); no perturbative restriction on \(c\) is imposed. The eight-point assertion concerns precisely \(K_*\), not every diagonally dominant matrix. A Morse–Smale map here means a smooth diffeomorphism with a finite hyperbolic nonwandering set and transverse stable/unstable intersections.

The potential is
\[
V_c(z)=\sum_{i=1}^N\left[(1+c)\cos z_i-\frac c3\cos^3z_i\right],
\qquad \nabla V_c(z)=-g_c(z),
\]
where \(g_c(z)\) is applied coordinatewise. Its only critical configurations are \(\{0,\pi\}^N\).

## Proof

**1. Exact scalar optimization.** Differentiate:
\[
g'_c(s)=\cos s\bigl(1+3c\sin^2s\bigr).
\]
It has the sign of \(\cos s\). For \(u=|\cos s|\in[0,1]\), the absolute derivative is
\[
f_c(u)=u(1+3c-3cu^2).
\]
This is maximized at \(u=1\) when \(c\leq1/6\), and uniquely at \(u_c=\sqrt{(1+3c)/(9c)}\in(0,1)\) when \(c>1/6\). Substitution yields \(q(c)=\|g'_c\|_\infty=\max(-g'_c)\) exactly. Moreover, \(|g_c(s)|\leq M_c=1+c\), with equality at \(s=\pi/2\) and \(3\pi/2\). The scalar derivatives are never zero at \(0\) or \(\pi\): \(g'_c(0)=1\) and \(g'_c(\pi)=-1\).

**2. Diffeomorphism, Lyapunov descent, and hyperbolic fixed points.** Put \(D(z)=\operatorname{diag}(g'_c(z_i))\). Then
\[
DF(z)=I+hKD(z),
\]
which is similar to the symmetric matrix \(I+hK^{1/2}D(z)K^{1/2}\). Its eigenvalues lie in \([1-h\lambda q(c),1+h\lambda q(c)]\). Hence when \(h\lambda q(c)<1\), every derivative has positive determinant. The torus map is a local diffeomorphism homotopic to the identity, has degree one, and so is a global diffeomorphism.

Since \(\|D^2V_c\|\leq q(c)\), Taylor's theorem on the real lift and the inequality \(\|Kv\|^2\leq\lambda v^{\mathsf T}Kv\) give
\[
V_c(F(z))-V_c(z)
\leq-h\left(1-\frac{h\lambda q(c)}2\right)
             g_c(z)^{\mathsf T}K g_c(z).
\]
This is strictly negative unless \(g_c(z)=0\). Consequently every periodic point is fixed; every nonfixed point is wandering, and the nonwandering set is precisely \(\{0,\pi\}^N\). The same inequality and compactness imply \(g_c(F^nz)\to0\). Since consecutive increments on the torus tend to zero and the critical set is finite and separated, each orbit converges to one of the fixed points.

At a fixed configuration, \(D(z)\) is diagonal with entries \(+1\) at zero and \(-1\) at \(\pi\). By congruence, \(K^{1/2}D(z)K^{1/2}\) has the same positive and negative inertia. Its eigenvalues are nonzero; the multipliers \(1+h\mu\) lie in \((0,2)\) and differ from one. Hence the unstable dimension is exactly the number of zero coordinates. Only \((\pi,\ldots,\pi)\) is a sink.

**3. Forward-invariant negative-derivative slabs.** Fix coordinate \(i\) and define
\[
S_i=\{z:\ z_i\in[\pi/2,3\pi/2]\pmod{2\pi}\}.
\]
For \(s\in[\pi/2,3\pi/2]\), the scalar \(f_i(s)=s+hk_{ii}g_c(s)\) is strictly increasing since \(1+hk_{ii}g'_c(s)>0\). Its endpoint values are \(\pi/2+hk_{ii}M_c\) and \(3\pi/2-hk_{ii}M_c\). The remaining coupling in coordinate \(i\) has absolute value at most \(hM_c\sum_{j\ne i}|k_{ij}|\leq hk_{ii}M_c\). Therefore each slab \(S_i\) is forward invariant. On this slab \(g'_c(z_i)\leq0\).

**4. Stable/unstable transversality.** Suppose two invariant manifolds have a nontransverse intersection, with associated two-sided orbit \(z_n\). The standard adjoint criterion then produces a nonzero covector sequence tending to zero at both temporal ends and satisfying
\[
\eta_n=\bigl(I+hD(z_n)K\bigr)\eta_{n+1}.
\]
Let \(\rho=\max_{i,n}|\eta_{i,n}|>0\), attained at time \(j\). For indices attaining \(\rho\) at \(j\), choose signs \(s_i=\eta_{i,j}/\rho\). Signed diagonal dominance implies \(s_i(K\eta_j)_i\geq0\). Some attaining index \(i\) has this expression strictly positive: otherwise strict triangle-inequality considerations force all connections to nonattaining indices to vanish, and the corresponding positive-definite principal submatrix of \(K\) would annihilate the nonzero attaining vector.

At this \(i\), with \(s=s_i\), the adjoint equation at \(j-1\) gives
\[
s\eta_{i,j-1}=\rho+h g'_c(z_{i,j-1})s(K\eta_j)_i\leq\rho.
\]
Thus \(g'_c(z_{i,j-1})\leq0\), placing the orbit in \(S_i\) at \(j-1\); forward invariance keeps it there. At time \(j\), the positive coefficient \(1+hk_{ii}g'_c(z_{i,j})\) and \(g'_c(z_{i,j})\leq0\) yield
\[
\rho=(1+hk_{ii}g'_c(z_{i,j}))s\eta_{i,j+1}
+h g'_c(z_{i,j})\sum_{\ell\ne i}k_{i\ell}s\eta_{\ell,j+1}
\leq\rho\left[1+h g'_c(z_{i,j})\left(k_{ii}-\sum_{\ell\ne i}|k_{i\ell}|\right)\right]\leq\rho.
\]
Equality forces \(s\eta_{i,j+1}=\rho\); repeating the same estimate forces this equality for all future times, contradicting decay. All intersections are therefore transverse. A finite hyperbolic nonwandering set together with this property makes the diffeomorphism Morse–Smale. The stable manifolds of all nonsinks have dimension smaller than \(N\), hence zero Lebesgue measure; convergence from step 2 gives full measure to the sink basin.

**5. Sharp maximal step.** For any \(h\lambda q(c)\geq1\), continuity of \(g'_c(s)\) on \([\pi/2,\pi]\) supplies some \(s\) with \(g'_c(s)=-1/(h\lambda)\). At the diagonal configuration \(z=s\mathbf1\), the matrix \(DF(z)=I+h g'_c(s)K\) has a zero eigenvalue along a \(\lambda\)-eigenvector. Thus the map is not a local diffeomorphism for **every** \(h\geq1/[\lambda q(c)]\); the claimed open interval is exact.

**6. The singularity splitting for the three-edge star.** Here \(K_*=I+\mathbf1\mathbf1^{\mathsf T}\) has spectrum \((4,1,1)\), with the \(4\)-eigenspace spanned by the vector of ones. At \(h_*(c)=1/(4q(c))\), all matrices \(D(z)+q(c)I\) are positive semidefinite, and for any real vector \(v\),
\[
 v^{\mathsf T}\bigl[4q(c)I+K_*^{1/2}D(z)K_*^{1/2}\bigr]v
=q(c)v^{\mathsf T}(4I-K_*)v
+(K_*^{1/2}v)^{\mathsf T}[D(z)+q(c)I](K_*^{1/2}v).
\]
Each term is nonnegative. Their sum vanishes for a nonzero \(v\) if and only if \(v\) is proportional to \(\mathbf1\) and all three diagonal entries of \(D(z)\) equal \(-q(c)\). Thus the Jacobian is singular precisely when every coordinate realizes the minimum of \(g'_c\). At each such point it is exactly \(I-K_*/4\) and has rank two.

The scalar minimizer is uniquely \(s=\pi\) if \(c\leq1/6\). If \(c>1/6\), the two distinct minimizers are \(s_+(c)\) and \(s_-(c)\). This proves the one-point/eight-point dichotomy. For \(c>1/6\), \(q(c)>1\) and at the sink the Jacobian is \(I-K_*/[4q(c)]\), with eigenvalues \(1-1/q(c)\) and \(1-1/[4q(c)]\) (the latter twice); it remains regular and attracting. At the transition itself, Taylor expansion gives
\[
g'_c(\pi+t)+1=\left(\frac12-3c\right)t^2+O(t^4)\quad(c<1/6),
\qquad
 g'_{1/6}(\pi+t)+1=\frac38 t^4+O(t^6),
\]
showing the stated quadratic-to-quartic contact change. \(\square\)

## Verification

A standalone standard-library Python script `verify.py` executes **37,958** finite tests for the exact rational cubic maximizer, the critical star Jacobian eigenvalues, the quartic derivative contact, sampled global scalar bounds and the Lyapunov/slab inequalities for two representative diagonally dominant matrices and eight harmonic coefficients. Run with `python3 verify.py`; it prints `VERIFY_OK 37958`. The verification is finite corroboration only: the global quantifiers, transversality, and exact singular locus follow from the analytic proof above.

In particular, the rational witness \(c=1\) has \(u_c=2/3\), \(q(c)=16/9\) and \(h_*(c)=9/64\). All eight critical Jacobians are \(I-K_*/4\), whose eigenvalues are exactly \(0,3/4,3/4\), while the sink remains hyperbolic.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (arXiv:2610.10993v1, first public October 7, 2026) establish an exact Morse–Smale interval for the **pure sine** law and a separate general-odd-law *gradient/Lyapunov/invertibility* framework. Their Theorems 3.2 and 4.1 are antecedents; in particular the descent and local-diffeomorphism aspects here are specializations of their general gradient estimates and are **not independently claimed new**. Their full Theorem 4.1 and proof use the specific \(\cos\)-derivative and \(\sin\)-endpoint values; the present proof extends the maximum-covector transversality mechanism to a nonperturbative two-harmonic family for every \(c\geq0\), and identifies its sharp shape factor and its one-to-eight interior Jacobian singularity transition. The source's structural-stability corollary covers only unspecified small perturbations of a fixed sine map; it does not imply the all-\(c\), sharp-\(h\) statements.

The earlier three-oscillator sinusoidal analysis (arXiv:2503.13230v1) studies sine-coupled synchronisation and does not have the non-sinusoidal parameter or its \(c=1/6\) singularity change. The new claim does not assert an independently new general adjoint-transversality lemma: it proves a new scope of applicability of that known method.

## Limitations

The general theorem requires positive signed diagonal dominance, nonsingularity, identical coordinate laws, and \(c\geq0\). It does not classify non-diffeomorphic dynamics above the exact step ceiling, nor does it assert transversality for arbitrary odd laws without the derivative-sign and endpoint geometry. The eight-point classification is specific to the indicated three-edge star matrix; reducible diagonally dominant matrices can have different critical loci. Neither independent verification nor a complete exhaustion of unpublished mathematical results has been performed. An equivalent specialization in wider gradient-map or monotone dynamical-system theory remains a priority risk.

## References

1. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (October 7, 2026), especially Theorems 3.2, 4.1 and Lemmas 4.2–4.3. https://arxiv.org/html/2610.10993v1
2. *Lyapunov functions for Morse-Smale synchronisation diffeomorphisms*, arXiv:2503.13230v1 (March 17, 2025). https://arxiv.org/html/2503.13230v1
3. *A Lyapunov function for a Synchronisation diffeomorphism of three clocks*, arXiv:2502.15371v1 (February 21, 2025). https://arxiv.org/html/2502.15371v1
