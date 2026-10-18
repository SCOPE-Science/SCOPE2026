# Sharp nine-part cutoff and reentrant hub-gain blackout in \(K_{1,m,m}\)

## Finding

On the unit-edge complete tripartite graph \(G_m=K_{1,m,m}=K_1\vee K_{m,m}\), \(m\ge2\), the unique allocation of a freely divisible pinning budget \(B>0\) minimizing \(\operatorname{tr}(L+\operatorname{diag}g)^{-1}\) exhibits an exact phase transition in graph size. For \(2\le m\le8\), the universal vertex always receives positive gain. For every \(m\ge9\), it receives zero gain on one nonempty **closed interval** of budgets, and receives positive gain both below and above that interval.

Write the hub gain as \(x\), the common gain at every other vertex as \(y\), and \(x+2my=B\). Define
\[
P_m(y)=y+2-\frac{4m(m-1)y}{(m+1+y)^2}-\frac{2my}{(2m+1+y)^2}.
\]
The exact support criterion is
\[
x=0\quad\Longleftrightarrow\quad P_m\!\left(\frac{B}{2m}\right)\le0.
\]
For every \(m\ge9\), the rational function \(P_m\) has exactly two distinct positive roots \(r_-(m)<r_+(m)\). The exact switching budgets are \(B_-(m)=2mr_-(m)\) and \(B_+(m)=2mr_+(m)\): the hub is unpinned exactly for \(B\in[B_-(m),B_+(m)]\), including equality.

As the two part sizes grow,
\[
\lim_{m\to\infty}\frac{B_-(m)}m=\frac43,\qquad
\lim_{m\to\infty}\frac{B_+(m)}{m^2}=2.
\]
For example, \(P_9(3)=-9161/40898<0\); thus at budget \(B=54\) on \(K_{1,9,9}\), the unique optimal solution assigns zero gain to the universal vertex. At budgets \(B=1\) and \(B=200\), its optimal gain is strictly positive.

## Assumptions and scope

Every graph edge has unit conductance. Let \(L\) be the combinatorial graph Laplacian of \(K_{1,m,m}\). The admissible gains are arbitrary independent numbers \(g_v\ge0\) with \(\sum_v g_v=B\). Since the graph is connected and \(B>0\), the matrix \(M(g)=L+\operatorname{diag}g\) is positive definite for every feasible allocation. The objective \(J(g)=\operatorname{tr} M(g)^{-1}\) is twice the stationary variance for independent unit-intensity noise in the standard continuous-time consensus model; the factor of two has no effect on minimizers.

This is a continuous-gain allocation theorem, not a fixed-cardinality or fixed-equal-gain leader-selection theorem. No extra per-vertex gain caps or sparse-selection constraints are imposed.

## Proof

**1. Global uniqueness and symmetry.** For any feasible gain vector and any nonzero real diagonal direction \(D\), differentiate the inverse under a small feasible affine perturbation:
\[
\frac{d^2}{dt^2}\operatorname{tr}(M+tD)^{-1}\bigg|_{t=0}
=2\operatorname{tr}(M^{-1}DM^{-1}DM^{-1})
=2\|M^{-1/2}DM^{-1}\|_F^2>0.
\]
Thus the objective is strictly convex along every nontrivial feasible segment and has a unique optimizer. Its invariance under the automorphism group of \(K_{1,m,m}\), which is transitive on all \(2m\) nonhub vertices, forces that optimizer to have common nonhub gain \(y\) and hub gain \(x=B-2my\). This is a conclusion about *all* independent allocations, not an assumption that reduces the feasible set.

**2. Exact scalar objective.** The peripheral subspace orthogonal to the all-ones vector splits into a \((2m-2)\)-dimensional eigenfamily of the pinned Laplacian with eigenvalue \(m+1+y\), and a one-dimensional eigenfamily with eigenvalue \(2m+1+y\). On the orthonormal hub/peripheral-constant subspace, the pinned Laplacian is
\[
\begin{pmatrix}2m+x&-\sqrt{2m}\\-\sqrt{2m}&1+y\end{pmatrix}.
\]
Consequently, on \(0\le y\le B/(2m)\),
\[
F_{m,B}(y)=\frac{2m-2}{m+1+y}+\frac1{2m+1+y}
+\frac{2m+x+1+y}{(2m+x)(1+y)-2m},\quad x=B-2my.
\]
The global optimal value is exactly \(\min_{0\le y\le B/(2m)}F_{m,B}(y)\), with a unique minimizer. This formula also determines the full optimal allocation and value for every \(m,B\), including interior phases (the unique root of \(F_{m,B}'(y)=0\) in the open interval).

**3. Marginal sign and exact support.** At the two endpoints, direct differentiation yields
\[
F_{m,B}'(0)=-1-\frac{4m}{B}-\frac{2m-2}{(m+1)^2}-\frac1{(2m+1)^2}<0,
\]
\[
F_{m,B}'\!\left(\frac{B}{2m}\right)
=\frac{P_m(B/(2m))}{B}.
\]
(The latter follows from \(2my=B\).) Strict convexity implies \(y>0\) always; furthermore its unique minimizer is the upper endpoint \(y=B/(2m)\), hence \(x=0\), precisely when the right-end derivative is nonpositive. Otherwise the unique zero of \(F_{m,B}'\) lies strictly inside the interval, and \(x>0\).

**4. No hub-blackout budget when \(2\le m\le8\).** For fixed \(y>0\), the function \(m(m-1)/(m+1+y)^2\) is increasing in real \(m\ge2\). Also \(2m/(2m+1+y)^2\le1/[4(1+y)]\), by maximizing \(t/(t+1+y)^2\) over \(t>0\). Therefore
\[
P_m(y)\ge y+2-\frac{224y}{(y+9)^2}-\frac{y}{4(1+y)}
=\frac{Q(y)}{4(1+y)(y+9)^2},
\]
where \(Q(y)=4y^4+83y^3-366y^2+139y+648\). To certify positivity without a numerical root claim: on \([0,2]\), the degree-four Bernstein coefficients of \(Q(2t)\) are \((648,1435/2,543,581/2,190)\); on \([2,3]\), those of \(Q(2+t)\) are \((190,559/4,255/2,182,336)\). Each is positive. For \(y\ge3\), write \(z=y-3\ge0\) and observe
\[
Q(3+z)=336+616z+597z^2+131z^3+4z^4>0.
\]
The Bernstein basis polynomials are nonnegative and sum to one, so \(Q(y)>0\) for every \(y>0\). Hence \(P_m(y)>0\) for every \(2\le m\le8\) and \(y>0\).

**5. Exactly two switching budgets for \(m\ge9\).** Multiplication by the positive denominator \((m+1+y)^2(2m+1+y)^2\) turns \(P_m\) into a degree-five polynomial in \(y\) with coefficients in descending order
\[
1,\quad 6(m+1),\quad 9m^2+32m+14,\quad
-2(2m^3-28m^2-29m-8),
\]
\[
-12m^4+34m^3+73m^2+44m+9,\quad
2(m+1)^2(2m+1)^2.
\]
For \(m\ge9\), the penultimate coefficient is strictly negative: substituting \(m=9+u\), \(u\ge0\), into its negative gives \(12u^4+398u^3+4841u^2+25372u+47628\). The other coefficient signs then produce **at most two positive roots**, by Descartes' rule (regardless of the sign of the quadratic coefficient). Meanwhile \(P_m(0)=2>0\), \(P_m(y)\to+\infty\) as \(y\to\infty\), and
\[
P_m(m/3)= -\frac{H(m)}{3(4m+3)^2(7m+3)^2}<0,
\]
where \(H(m)=980m^5-6516m^4-13437m^3-10314m^2-3645m-486\). At \(m=9+u\), \(H\) has positive coefficients \((980,37584,545787,3604311,9693756,4452246)\) in descending powers of \(u\). Thus two distinct positive zeros exist and there are no others. The sign is nonpositive exactly between them, including both zeros.

**6. Scaling of the switching interval.** For fixed \(y>0\), \(P_m(y)\to2-3y\) as \(m\to\infty\), uniformly on compact intervals. The smaller root therefore converges to \(2/3\). For fixed \(z>0\),
\[
\frac1m P_m(mz)\longrightarrow z\left(1-\frac4{(1+z)^2}\right),
\]
whose sign changes from negative to positive at \(z=1\). The larger root satisfies \(r_+(m)/m\to1\). Multiplying by \(2m\) gives the two claimed budget scalings.

## Verification

The standalone file `verification/check.py` symbolically checks the scalar boundary derivatives, quintic coefficients, Bernstein certificates, exact witness, and two asymptotic limits. It also directly constructs the independently pinned graph Laplacian for multiple sizes and budgets, compares full matrix inverse traces with the spectral reduction, and tests sampled nonsymmetric feasible gains. Run with `python verification/check.py` using Python 3, SymPy, NumPy and SciPy. Numerical tests do not establish the infinite-family theorem; the proof above does.

## Relationship to prior work

Lin, Fardad, and Jovanović establish the noisy-leader inverse-trace objective and convex relaxation of *Boolean leader selection* (2013). Fitch and Leonard study optimal finite leader sets with network centrality (2014). Their general formulations and derivative tools motivate this continuous, freely divisible gain-budget problem but do not provide the graph-family size cutoff, two support transitions, or separate linear/quadratic budget scales established here. Exact continuous gain allocation on the triangle-containing \(K_{1,m,m}\) is also distinct from corresponding results for the triangle-free complete bipartite family \(K_{p,q}\); these graphs are not reducible by relabelling. Ordinary general-purpose convexity does not itself give the two-root phase classification.

## Limitations

All graph edges and noise intensities are unit-weight, feedback gains are nonnegative with one unweighted sum constraint, and there are no per-vertex caps. The claimed uniqueness concerns this exact problem only. The theory classifies optimal support and determines all optimal gains via a scalar equation but gives no radical formula for the general quintic switching thresholds. An equivalent unindexed or unstated specialization of broader optimal-design results cannot be ruled out; no claim is made about independent review or formal verification.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, original public preprint 3 February 2013, arXiv:1302.0450. https://arxiv.org/abs/1302.0450
2. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, original public preprint 7 July 2014, arXiv:1407.1569. https://arxiv.org/abs/1407.1569
