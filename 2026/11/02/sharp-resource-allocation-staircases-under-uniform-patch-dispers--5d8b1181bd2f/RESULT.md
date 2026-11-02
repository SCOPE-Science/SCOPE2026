# Sharp resource-allocation staircases under uniform patch dispersal

## Finding

Suppose a fixed habitat-investment budget is divided among heterogeneous patches. Larval recruitment follows an all-to-all, symmetric dispersal rule with a tunable emigration fraction. Maximizing the low-density next-generation Perron root produces an exact transition from guaranteed single-patch concentration at lower movement to a unique square-root active-set allocation at higher movement. Patches join the optimum at explicit, ordered emigration thresholds; very inefficient patches may never receive resources even at maximal emigration.

Let \(n\ge2\), \(B>0\), and \(c_1\ge\cdots\ge c_n>0\). An investment vector \(h\in[0,\infty)^n\) satisfies \(\sum_i h_i=B\). Patch \(i\) produces \(c_i h_i\) low-density recruits. For \(0\le\theta\le1\), let
\[
P_{ii}=1-\theta,\qquad P_{ij}=\frac{\theta}{n-1}\quad(i\ne j),\qquad
M(h)=P\,\operatorname{diag}(c_1h_1,\ldots,c_nh_n).
\]
The quantity optimized is precisely \(\rho(M(h))\), the Perron spectral radius of this nonnegative recruitment matrix; it is **not** an asserted nonlinear extinction probability.

Define \(\theta_c=(n-1)/n\). If \(0\le\theta<\theta_c\), every maximizer invests the entire budget in a **single** patch of maximal efficiency; the optimum value is \((1-\theta)c_1B\). At \(\theta=\theta_c\), **every** allocation supported only on maximal-efficiency patches is optimal, with value \(c_1B/n\).

If \(\theta_c<\theta\le1\), define
\[
\beta=\frac{\theta}{n-1},\qquad
s=\frac{n\theta}{n-1}-1>0,\qquad
\delta=\frac{s}{\beta}=n-\frac{n-1}{\theta},\qquad
u_i=\sqrt{c_i}.
\]
There is a **unique** maximizing vector, described by a cutoff \(z>0\). It has active indices precisely \(\{i:u_i>z\}\), and, writing \(m\) for their number,
\[
z=\frac{m-\delta}{\sum_{i=1}^{m}u_i^{-1}},\qquad
Q=\sum_{i=1}^{m}\left(u_i^{-1}-zu_i^{-2}\right),
\]
\[
\boxed{\quad
h_i^*=\frac{B\left(u_i^{-1}-zu_i^{-2}\right)}{Q}\;\;(i\le m),\qquad h_i^*=0\;\;(i>m),\qquad
\rho_{\max}=\frac{Bs z}{Q}.
\quad}
\]
The cutoff is the unique solution of
\[
\sum_{i=1}^{n}\left(1-\frac{z}{u_i}\right)_+=\delta;
\]
this formula handles repeated efficiencies and activation equalities without ambiguity. For any \(j=2,\ldots,n\), patch \(j\) is active **if and only if**
\[
\boxed{\quad\delta>\delta_{j-1}:=\sum_{i=1}^{j-1}\left(1-\sqrt{\frac{c_j}{c_i}}\right).\quad}
\]
These thresholds are nondecreasing. If \(\delta_{j-1}\ge1\), patch \(j\) remains unused for every \(\theta\le1\). The strict inequality matters: at an activation threshold the newly joining patch still has zero optimal investment.

For \(n=4\), \((c_1,c_2,c_3,c_4)=(16,9,4,1)\), the optimum uses only patch 1 up to \(\theta=4/5\), patches 1 and 2 for \(4/5<\theta\le18/19\), and patches 1, 2 and 3 for \(18/19<\theta\le1\). Patch 4 never activates. At \(\theta=1\), the unique optimum is
\[
\boxed{\quad h^*=\frac{B}{47}(21,20,6,0),\qquad \rho_{\max}=\frac{96B}{47}.\quad}
\]

## Assumptions and scope

The habitat budget is divisible continuously with no per-patch upper bound; production is linear in invested habitat; source efficiency coefficients are fixed, strictly positive, and sorted merely for indexing. Dispersal destinations are sampled uniformly among the other patches. \(P\) is column-stochastic, so \(M=P\operatorname{diag}(ch)\) represents **offspring production followed by dispersal**. A patch with zero investment is assigned zero source reproduction even if it receives propagules. The theorem applies to the Perron root of this linearization, without making nonlinear persistence claims. No stochastic finite-population extinction times or habitat geometry are modeled.

## Proof

**1. Symmetrization and the concentration side.** Put \(x_i=c_i h_i\), \(D=\operatorname{diag}(x_i)\) and \(v=(\sqrt{x_i})_i\). The nonzero eigenvalues of \(PD\) equal those of the symmetric \(S=D^{1/2}PD^{1/2}\), including zero multiplicities after continuity; directly, the two matrices have the same characteristic polynomial by \(\det(\lambda I-AB)=\det(\lambda I-BA)\). Writing \(\beta=\theta/(n-1)\) and \(a=1-n\theta/(n-1)\),
\[
S=aD+\beta vv^\mathsf{T}.
\]
When \(\theta\le\theta_c\), \(a\ge0\) and \(S\) is positive semidefinite; therefore
\[
\rho(PD)=\lambda_{\max}(S)\le\operatorname{tr}S
=(1-\theta)\sum_i x_i\le (1-\theta)c_1B.
\]
For \(\theta<\theta_c\), any allocation with at least two positive \(x_i\) makes \(S\) rank at least two, so the first inequality is strict. A single highest-efficiency patch attains equality. At \(\theta_c\), \(S=vv^\mathsf{T}/n\) has rank one and \(\rho=\sum_i c_i h_i/n\), yielding exactly the stated maximizing face.

**2. A secular equation above the mixing threshold.** For \(\theta>\theta_c\), \(a=-s<0\), so \(S=-sD+\beta vv^\mathsf{T}\). For any \(\lambda>0\), the matrix determinant lemma gives the positive-eigenvalue condition
\[
F_h(\lambda):=\beta\sum_{i=1}^{n}\frac{c_i h_i}{\lambda+s c_i h_i}=1.
\]
For \(h\ge0\), this function decreases strictly in \(\lambda>0\) whenever any \(h_i>0\). The symmetric matrix has at most one positive eigenvalue, which (if present) equals the nonnegative Perron root. If \(\theta=1\) and exactly one \(h_i>0\), then the Perron root is zero, while allocations with at least two active sites have a positive Perron root; hence such a singleton cannot maximize. For \(\theta<1\) a singleton has positive Perron root.

**3. A strictly concave fixed-eigenvalue problem.** Fix \(\lambda>0\). The function \(h\mapsto F_h(\lambda)\) on \(\{h\ge0:\sum_i h_i=B\}\) is **strictly concave**: its \(i\)-th summand has derivative \(\beta\lambda c_i/(\lambda+s c_i h_i)^2\) and strictly negative second derivative. Thus its unique maximizer satisfies the Karush–Kuhn–Tucker conditions with a common positive multiplier \(\kappa\): for active indices,
\[
\frac{\beta\lambda c_i}{(\lambda+s c_i h_i)^2}=\kappa,
\]
and for inactive indices the left derivative at zero is at most \(\kappa\). Defining \(z=\sqrt{\kappa\lambda/\beta}\), these are exactly
\[
h_i=\frac{\lambda}{sz}\left(u_i^{-1}-zu_i^{-2}\right)_+,
\qquad\text{with active set }\{u_i>z\}.
\]
The budget fixes \(\lambda/(sz)=B/Q\). Substituting the KKT form in \(F_h(\lambda)=1\) yields
\[
1=\frac{\beta}{s}\sum_i\left(1-\frac{z}{u_i}\right)_+,
\]
so \(\sum_i(1-z/u_i)_+=\delta=s/\beta\). The left side is continuous and strictly decreasing as \(z\) ranges from \(0\) to \(u_1\), from value \(n\) to zero. Since \(0<\delta\le1<n\), it determines exactly one \(z\in(0,u_1)\), hence exactly one nonnegative proposed \(h^*\) and \(\lambda=Bs z/Q>0\).

**4. Global optimality and uniqueness.** The proposed \(h^*\) satisfies the KKT conditions, so for its positive \(\lambda^*\), strict concavity yields \(F_h(\lambda^*)<F_{h^*}(\lambda^*)=1\) for every other feasible \(h\). Any \(h\) with a positive Perron root therefore has \(\rho(PD)<\lambda^*\), by strict decrease of its secular function. Feasible vectors with Perron root zero are also strictly inferior. Thus the optimizer is unique and its value is \(\lambda^*\), including the \(\theta=1\) boundary.

**5. Patch-entry staircase.** Patch \(j\) activates precisely when \(z<u_j\). Evaluating the cutoff equation at \(z=u_j\) gives the explicit threshold \(\delta_{j-1}=\sum_{i<j}(1-u_j/u_i)\); strict monotonicity then yields the stated equivalence. Consecutive thresholds differ by \((u_j-u_{j+1})\sum_{i\le j}u_i^{-1}\ge0\). The exact four-patch thresholds follow from \(\delta_1=1/4\), \(\delta_2=5/6\) and \(\delta_3=23/12>1\), with \(\delta=4-3/\theta\). At \(\theta=1\), \(\delta=1\) and the cutoff is \(z=24/13\); normalization gives \(h^*=B(21,20,6,0)/47\). Substituting this \(h\) in the eigenvalue formula gives \(96B/47\). This completes the proof.

## Verification

Run `python verify.py` after installing Python 3, NumPy and SymPy. The code reconstructs the four-patch thresholds, uses exact rational arithmetic to test the exact optimum and its eigenvalue, then compares the analytical optimum against 18,375 randomly generated feasible competitors over varied patch counts, efficiencies and movement fractions. These finite tests are **not** used to infer universal optimality; Steps 1–5 are the proof.

## Relationship to prior work

Kirkland, Li and Schreiber (2006) derive ecological population/dispersal theory on patchy landscapes and examine varying dispersal strategies with **fixed patch fecundities**. Their setting motivates the column-stochastic recruitment matrix but does not optimize the fecundities subject to a heterogeneous habitat budget. Haight and Travis (published online 2007) study allocating habitat resources for persistence in a stochastic individual-based simulation model. Their objective, decision variables and simulation-based selection differ from an analytic maximum Perron root under all-to-all movement; their conclusions do not imply the square-root entry threshold formulas.

Delmas, Dronnier and Zitt (2023), Theorem 4.2, is the strongest structural analogue: it completely solves a **different constrained spectral allocation problem** for a homogeneous assortative/disassortative mixing kernel. Its effective nonvaccinated group masses have coordinate caps \(0\le\xi_i\le\mu_i\), with a fixed **unweighted sum** \(\sum_i\xi_i\), producing horizontal capped allocation profiles in the disassortative case. Here \(x_i=c_i h_i\) obeys the **heterogeneously weighted** constraint \(\sum_i x_i/c_i=B\), with **no coordinate caps**. Their horizontal rule is not the current square-root staircase except in special equal-efficiency limits; the exact heterogeneous threshold classification is not stated there. Their general spectral concavity theory is consistent with (but does not provide) this allocation formula. The point is not priority for the generic rank-one secular formula, positive-eigenvalue inertia, or KKT conditions, all of which are standard.

Searches of pertinent research records and published literature identified no matching statement of the complete heterogeneously weighted all-to-all phase diagram. That negative observation cannot prove historical uniqueness; in particular, specialized matrix-allocation or economic resource-investment work may contain a more general result.

## Limitations

The theorem concerns continuous budget allocation and linearized total recruitment, not habitat fragmentation, realized reserve persistence, resilience to environmental variability or discrete site-purchase decisions. It assumes no per-site size caps, no establishment density feedback, no dispersal mortality, and symmetric uniform destination choices. Increasing spectral growth need not maximize a finite-population survival probability. Historical originality is provisional pending a wider systematic matrix-allocation literature review. The all-to-all model has a special rank-one structure; the staircase is not claimed for arbitrary dispersal matrices.

## References

1. S. Kirkland, C.-K. Li and S. J. Schreiber (2006). *On the Evolution of Dispersal in Patchy Landscapes*. SIAM Journal on Applied Mathematics 66, 1366–1382. DOI: 10.1137/050628933. Electronically published 2006-04-21. Open paper: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2022/09/050628933.pdf
2. R. G. Haight and L. E. Travis (2007 online; 2008 volume). *Reserve Design to Maximize Species Persistence*. Environmental Modeling & Assessment 13, 243–253. DOI: 10.1007/s10666-007-9088-4. Online 2007-03-15. Open paper: https://research.fs.usda.gov/treesearch/download/13955.pdf
3. J.-F. Delmas, D. Dronnier and P.-A. Zitt (2023). *Optimal vaccination: various (counter) intuitive examples*. Journal of Mathematical Biology 86, article 26. DOI: 10.1007/s00285-022-01858-5. Open article: https://link.springer.com/article/10.1007/s00285-022-01858-5
