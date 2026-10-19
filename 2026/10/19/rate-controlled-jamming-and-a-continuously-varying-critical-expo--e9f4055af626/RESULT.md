# Rate-controlled jamming and a continuously varying critical exponent on a complete tripartite graph

## Finding

Fix real numbers \(a,c,\lambda>0\) with \(2a+c=1\). For each positive integer \(N\), let \(G_N\) be the complete tripartite graph with vertex parts \(A_N,B_N,C_N\) satisfying
\[
|A_N|/N\to a,\qquad |B_N|/N\to a,\qquad |C_N|/N\to c.
\]
Every edge between the first two parts is assigned an independent exponential clock of rate \(\lambda/N\); every edge incident to the third part has rate \(1/N\). Process all clocks in increasing time order, accepting an edge precisely when neither endpoint has previously been covered. Let \(U_N\) be the final number of uncovered vertices. Then, in probability and in mean,
\[
\frac{U_N}{N}\longrightarrow J_\lambda(a,c),
\]
where, for \(0<\lambda<2\),
\[
J_\lambda(a,c)=
\begin{cases}
0,&c\le(2-\lambda)a,\\
c\left(1-\frac{(2-\lambda)a}{c}\right)^{\frac{2}{2-\lambda}},&c>(2-\lambda)a;
\end{cases}
\]
for \(\lambda=2\),
\[
J_2(a,c)=c\exp\!\left(-\frac{2a}{c}\right);
\]
and for \(\lambda>2\),
\[
J_\lambda(a,c)=c\left(1+\frac{(\lambda-2)a}{c}\right)^{-\frac{2}{\lambda-2}}.
\]

In the region \(0<\lambda<2\), the surviving population has a continuously varying onset exponent \(\beta(\lambda)=2/(2-\lambda)\). In particular, with \(a\) fixed and \(c_*=(2-\lambda)a\), as \(c\downarrow c_*\) from above (using an arbitrary common macroscopic scale before normalization),
\[
J_\lambda(a,c)=c^{1-\beta(\lambda)}(c-c_*)^{\beta(\lambda)}
\sim c_*^{1-\beta(\lambda)}(c-c_*)^{\beta(\lambda)}.
\]
At the endpoint \(\lambda=2\), the small-\(c\) response is instead \(c\exp(-2a/c)\), which is flat to all algebraic orders as \(c\downarrow0\).

For the concrete family \(K_{3m,3m,4m}\) (which admits a perfect matching), the asymptotic uncovered fractions are \(0\) for \(\lambda\le2/3\), \(1/40\) for \(\lambda=1\), and \(32/245\) for \(\lambda=3\). The rate bias therefore changes macroscopic kinetic jamming without changing the underlying graph's matching feasibility.

## Assumptions and scope

Only positive, fixed \(a,c,\lambda\) are considered. The two first vertex classes need not be exactly equal at finite \(N\), but their normalized sizes must have the same limit. All edge-clock variables are independent, continuous, and exponential at the stated rates; there are no clocks within a part. The process is irreversible and proceeds until no available edge remains. Changing the overall common rate merely changes the time parametrization. Statements involving a variable \(c\) at fixed \(a\) refer to the unnormalized density law \(J_\lambda\), which is homogeneous of degree one; the normalization \(2a+c=1\) is restored by dividing by the total initial density.

## Proof

**1. Finite-count Markov description.** Let \((X_N(t),Y_N(t),Z_N(t))\) be the numbers of uncovered vertices in the three parts. By exponential memorylessness, the only jumps, with their respective instantaneous rates, are
\[
(-1,-1,0):\ \lambda X_NY_N/N,\qquad
(-1,0,-1):\ X_NZ_N/N,\qquad
(0,-1,-1):\ Y_NZ_N/N.
\]
Indeed every currently available edge has not yet rung, because an edge rejected earlier would already have at least one covered endpoint. The process stops exactly when the remaining vertices are contained in a single part. In particular, its terminal uncovered count is the sum of the terminal class counts.

**2. Fluid limit on each finite time interval.** Set \((x_N,y_N,z_N)=(X_N,Y_N,Z_N)/N\). Their drift is the polynomial vector field
\[
F(x,y,z)=(-\lambda xy-xz,-\lambda xy-yz,-z(x+y)).
\]
On the compact cube \([0,1]^3\), this field is Lipschitz. The scaled martingale part has jumps of magnitude at most \(\sqrt2/N\) and predictable quadratic variation bounded by \(K_\lambda T/N\) on \([0,T]\), with \(K_\lambda\) independent of \(N\). Doob's inequality followed by Gronwall's inequality gives uniform-in-time convergence in probability on every fixed \([0,T]\) to the unique nonnegative solution of the indicated ODE, started at \((a,a,c)\).

**3. Symmetry and an exact first integral.** The difference \(d=x-y\) obeys \(\dot d=-zd\). Since \(d(0)=0\), \(x=y\) always. Rename their common value \(u\), and rename the third density \(v\). They solve
\[
\dot u=-u(\lambda u+v),\qquad \dot v=-2uv,\qquad (u(0),v(0))=(a,c).
\]
Both are positive at finite times. Put \(p=\lambda/2\). Division of the differential equations yields
\[
\frac{du}{dv}=\frac{pu}{v}+\frac12.
\]
For \(p\ne1\) direct differentiation shows
\[
\frac{u}{v^p}-\frac{v^{1-p}}{2(1-p)}
=\frac{a}{c^p}-\frac{c^{1-p}}{2(1-p)}.
\]
For \(p=1\) the first integral is \(u/v-(\log v)/2=a/c-(\log c)/2\).

**4. Determine the terminal fluid value.** Since \(\dot u\le-\lambda u^2\), \(u(t)\to0\). Also \(v(t)\) is decreasing and therefore converges to some \(v_*\ge0\). If \(p<1\), the first integral has a positive root at \(u=0\) exactly when \(c>2(1-p)a\); its root is
\[
v_*=c\left(1-\frac{2(1-p)a}{c}\right)^{1/(1-p)}.
\]
When that inequality fails the trajectory can only have \(v_*=0\). If \(p>1\), the same integral has the strictly positive root
\[
v_*=c\left(1+\frac{2(p-1)a}{c}\right)^{-1/(p-1)}.
\]
If \(p=1\), the logarithmic first integral gives \(v_*=c\exp(-2a/c)\). All roots are unique because, along the strictly decreasing solution \(v(t)\), the displayed expression for \(u(v)\) stays positive until its first zero. Substituting \(p=\lambda/2\) produces the stated \(J_\lambda\).

**5. Pass from finite times to the jammed finite graph.** Let \(U_N\) denote the terminal count. At any deterministic time \(T\), irreversible coverage gives
\[
U_N\le X_N(T)+Y_N(T)+Z_N(T).
\]
Every later edge incident to class \(C_N\) consumes one vertex from either \(A_N\) or \(B_N\), so the terminal count also satisfies
\[
U_N\ge Z_N(\infty)\ge Z_N(T)-X_N(T)-Y_N(T).
\]
Take \(N\to\infty\) at fixed \(T\), using step 2, then \(T\to\infty\), using step 4 and \(u(T)\to0\). The deterministic upper and lower limits both equal \(v_*\), proving convergence in probability. Since \(0\le U_N/N\le1\), bounded convergence yields convergence of expectations.

**6. Critical behavior and matching feasibility.** The positive-root formula for \(0<\lambda<2\) is exactly \(c^{1-\beta}(c-c_*)^\beta\), proving the claimed exponent. At \(\lambda=2\), every derivative of its continuous extension by zero at \(c=0\) vanishes because an exponential dominates any power. The example has \(a=3/10\), \(c=2/5\), so \(c_*= (2-\lambda)3/10\), and the threshold is \(\lambda=2/3\). At \(\lambda=3\), \(J_3=(2/5)(1+3/4)^{-2}=32/245\). The largest part of \(K_{3m,3m,4m}\) has size \(4m\le5m\), half its even order \(10m\); the standard complete-multipartite matching criterion therefore gives a perfect matching.

## Verification

The accompanying `check_weighted_jamming.py` uses only the Python standard library. Run `python3 check_weighted_jamming.py` in the same directory. It compares exact rational expected terminal counts obtained from a labeled-edge recursion against a separate three-count Markov recursion for 104 small graph-and-rate instances; checks the nonstandard first integrals algebraically at rational arguments; checks the equal-rate reduction; and performs seeded Monte Carlo comparisons at five rates on graphs of order 5000. The exact graph checks test the finite generator. The finite simulations only diagnose errors and are not substitutes for the infinite-system argument in the proof.

## Relationship to prior work

Ben-Avraham and Redner (1986) analyzed multi-species pair annihilation and reported a mean-field three-species solution. Hilhorst, Deloubrière, Washenberger and Täuber (2004, first public preprint 9 March) studied equal reaction rates, and the subsequent Hilhorst, Washenberger and Täuber (2004, first public preprint 3 September) examined reaction-rate matrices preserving a transitive symmetry of all species and spatial segregation. The present rate matrix has only the first-two-species swap symmetry, not a transitive three-species symmetry, and the observable here is the finite dense-graph terminal coverage for unequal initial species populations. The equal-rate specialization \(\lambda=1\) reproduces the already familiar tripartite product rule and is **not** asserted novel. The distinct claim is the sharp continuously tunable rate-controlled onset and its essential-singularity endpoint for positive unequal edge rates. Earlier mean-field annihilation literature remains a possible route to an equivalent formula and is an explicitly acknowledged bibliographic risk.

## Limitations

The theorem does not give a central-limit law, rate of convergence, finite-size critical scaling, or any result for fixed \(\lambda=0\). It does not apply to sparse graphs, geometric finite-dimensional diffusion, adversarial edge priorities, or arbitrary rate matrices. The limiting process takes \(N\to\infty\) for fixed positive rates and fixed positive macroscopic part fractions; exchanging these limits can change the outcome. Its scientific novelty has not received independent validation, and accessible primary research does not rule out every equivalent earlier formulation.

## References

1. D. ben-Avraham and S. Redner, *Kinetics of n-species annihilation: Mean-field and diffusion-controlled limits*, Physical Review A 34 (1986), 501–509, DOI: 10.1103/PhysRevA.34.501.
2. H. J. Hilhorst, O. Deloubrière, M. J. Washenberger, and U. C. Täuber, *Segregation in diffusion-limited multispecies pair annihilation*, arXiv:cond-mat/0403246v1 (public 2004-03-09), Journal of Physics A 37 (2004), 7063–7093.
3. H. J. Hilhorst, M. J. Washenberger, and U. C. Täuber, *Symmetry and species segregation in diffusion-limited pair annihilation*, arXiv:cond-mat/0409079v1 (public 2004-09-03), Journal of Statistical Mechanics (2004), P10002.
4. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, DOI: 10.1137/0402034.
