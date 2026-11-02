# Unique budget-optimal spectral gaps on alternating-price cycles

## Finding
Fix an integer \(m\ge2\), prices \(p,q>0\), and conductance budget \(B>0\). Label the vertices of the undirected cycle \(C_{2m}\) as \(A_j,B_j\), \(j\in\mathbb Z/m\mathbb Z\). Each edge \(A_jB_j\) costs \(p\) per unit conductance and each edge \(B_jA_{j+1}\) costs \(q\). All \(2m\) edge conductances may be chosen **independently**, are nonnegative, and have total price at most \(B\). Let \(L\) be the resulting weighted combinatorial Laplacian and \(\lambda_2(L)\) its second-smallest eigenvalue.

Write \(g=\cos(\pi/m)\) and \(h=\sin^2(\pi/m)\). There is **exactly one optimal full edge-conductance vector**. It assigns the respective common values
\[
 a_* =\frac{B(qg+\sqrt{pq})}{m[2pqg+(p+q)\sqrt{pq}]},\qquad
 b_* =\frac{B(pg+\sqrt{pq})}{m[2pqg+(p+q)\sqrt{pq}]}
\]
to the \(A_jB_j\) and \(B_jA_{j+1}\) edges, and has exact gap
\[
 \boxed{\lambda_{2,*}=\frac{2B\sin^2(\pi/m)}{m[p+q+2\sqrt{pq}\cos(\pi/m)]}.}
\]
In particular, both edge classes remain strictly positive for every finite positive price ratio, and the unique optimum has
\[
 \frac{a_*}{b_*}=\frac{q\cos(\pi/m)+\sqrt{pq}}{p\cos(\pi/m)+\sqrt{pq}}.
\]
For the four-cycle \(m=2\), this ratio equals one for **all** positive prices; as \(m\to\infty\), the ratio converges to \(\sqrt{q/p}\). Among designs that use a common conductance on every edge, the exact optimal-gain ratio is
\[
 \frac{\lambda_{2,*}}{\lambda_{2,\mathrm{equal}}}
 =\frac{(p+q)[1+\cos(\pi/m)]}{p+q+2\sqrt{pq}\cos(\pi/m)}.
\]
This is strictly greater than one if \(m>2\) and \(p\ne q\), and tends to \(2(p+q)/(\sqrt p+\sqrt q)^2\) as \(m\to\infty\); that limiting factor can approach two for large price contrast.

## Assumptions and scope
The graph is exactly the undirected even cycle specified above, with no chords or independent self-loops; the quantity optimized is continuous-time algebraic connectivity of the **combinatorial**, not normalized, weighted Laplacian. Every individual edge is an independent nonnegative design variable. Prices and total budget are strictly positive, and \(m\) is an arbitrary integer at least two. No per-vertex conductance, degree, or probability cap is imposed. The budget is exhausted at the optimum because positive scaling strictly increases \(\lambda_2\) for a connected design.

## Proof
**1. Rotation averaging and the two-band spectrum.** Since \(\lambda_2(L)=\min_{x\perp\mathbf1,\|x\|=1}x^TLx\) is concave in \(L\), averaging any feasible design under the \(m\) rotations \(j\mapsto j+1\) preserves cost and cannot decrease the objective. An optimal rotation-invariant design therefore exists. Write \(a,b\ge0\) for its two alternating edge weights; its price is \(m(pa+qb)\). The Bloch matrix at \(\theta=2\pi k/m\) is
\[
 H_\theta=\begin{pmatrix}
 a+b&-a-be^{-i\theta}\\
 -a-be^{i\theta}&a+b
 \end{pmatrix}.
\]
Its eigenvalues are \(a+b\pm\sqrt{a^2+b^2+2ab\cos\theta}\). The zero mode occurs only in the lower band at \(\theta=0\). The least positive eigenvalue is the lower band for \(\theta=2\pi/m\) (and its conjugate), namely
\[
 \lambda_2(a,b)=(a+b)-\sqrt{g^2(a+b)^2+h(a-b)^2}.
\]
The same formula holds when \(m=2\), in which case it equals \(2\min\{a,b\}\).

**2. A sharp global norm inequality.** Set \(s=a+b\), \(d=a-b\), \(P=p+q\), \(Q=p-q\), and \(D=P+2g\sqrt{pq}\). The vector
\[
 v=\frac1D\big(Pg+2\sqrt{pq},\,-\sqrt h\,Q\big)
\]
has Euclidean norm exactly one, as follows by expansion using \(P^2-Q^2=4pq\) and \(g^2+h=1\). Cauchy--Schwarz gives
\[
 \sqrt{g^2s^2+hd^2}\ \ge\
 (gs,\sqrt h\,d)\cdot v
 =s-\frac{2h(pa+qb)}{D}.
\]
Therefore \(\lambda_2(a,b)\le 2h(pa+qb)/D\le2hB/(mD)\). For \(m>2\), equality in the norm bound requires
\[
 \frac{d}{s}=-\frac{g(p-q)}{g(p+q)+2\sqrt{pq}},
\]
which, together with the exhausted budget, uniquely gives \(a_*,b_*\). For \(m=2\), the bound becomes \(\lambda_2=2\min\{a,b\}\le2(pa+qb)/(p+q)\) with equality only at \(a=b\); the same formulas follow. Thus the displayed weights are the unique **rotation-invariant** optimum and yield the stated exact value.

**3. No asymmetric optimal design exists.** Let \(w\) be any unrestricted optimum and \(\overline L\) its rotational average. By step 2 the average is precisely the Laplacian of \(a_*,b_*\). Let \(\Pi=I-\mathbf1\mathbf1^T/(2m)\) and \(t=\lambda_{2,*}\). Feasibility and optimality imply \(L(w)-t\Pi\succeq0\), and also \(\overline L-t\Pi\succeq0\). Every \(z\) in the complexified \(t\)-eigenspace of \(\overline L\) has \(z^*(\overline L-t\Pi)z=0\). Since the average is formed from positive-semidefinite conjugates of \(L(w)-t\Pi\), each such quadratic form vanishes for every conjugate, in particular for the original. Hence \(L(w)z=tz\).

For \(m\ge3\), take the lower-band Bloch vector at \(\theta=2\pi/m\), with components \(z_{A_j}=e^{i\theta j}\) and \(z_{B_j}=re^{i\theta j}\), where
\[
 r=\frac{a_*+b_*e^{i\theta}}{|a_*+b_*e^{i\theta}|}.
\]
Subtracting the eigenvalue equations for \(L(w)\) and \(\overline L\) at \(B_j\) gives
\[
 (a_j-a_*)(r-1)+(b_j-b_*)(r-e^{i\theta})=0.
\]
The coefficients multiplying the two **real** deviations are linearly independent over \(\mathbb R\): the three distinct points \(1,r,e^{i\theta}\) lie on the unit circle, and no straight line meets that circle in three distinct points. Distinctness follows from \(a_*,b_*>0\) and \(0<\theta<\pi\). Thus \(a_j=a_*\), \(b_j=b_*\) for every \(j\).

For \(m=2\), \(a_*=b_*\) and the Fiedler eigenspace of the symmetric four-cycle is spanned by the vectors \((1,0,-1,0)\) and \((0,1,0,-1)\), in vertex order \(A_0,B_0,A_1,B_1\). The eigenvalue equations for the first vector force the conductances at each \(B\)-vertex to agree; those for the second force the conductances at each \(A\)-vertex to agree. All four conductances must therefore coincide. This proves the full unrestricted uniqueness claim.

**4. Baseline and limits.** Equal edge conductances exhaust the budget at \(a=b=B/[m(p+q)]\) and give \(\lambda_{2,\mathrm{equal}}=2B[1-g]/[m(p+q)]\). Dividing and simplifying yields the stated gain ratio. Positivity follows from \(p+q>2\sqrt{pq}\) whenever \(p\ne q\) and \(g>0\). Taking \(g\to1\) proves both the square-root allocation limit and the gain limit. Since \(1-g\sim\pi^2/(2m^2)\), the optimized gap has asymptotic \(2B\pi^2/[m^3(\sqrt p+\sqrt q)^2]\).

## Verification
The accompanying `verify.py` checks the Laplacian spectrum against the formula for 78 parameter cases; compares 1,950 independently allocated feasible asymmetric random designs; makes 36 independent constrained-optimization upper-bound comparisons; and performs 108 bounded scalar-optimization comparisons. A separate exact symbolic check gives, for \(m=3\), \(p=1\), \(q=4\), and \(B=1\), the exact conductances \(a_*=2/21\), \(b_*=5/84\), and spectrum \(\{0,1/14,1/14,5/21,5/21,13/42\}\). These computations corroborate the proof but are not used to infer an infinite-family conclusion.

## Relationship to prior work
Ghosh and Boyd (2006) establish the concavity and group-averaging framework for Laplacian eigenvalue optimization, but the material inspected does not give this alternating-price cycle allocation or unrestricted uniqueness statement. Wan and colleagues (2008) study structural properties of optimal algebraic-connectivity edge designs, especially trees and eigenvalue multiplicity, but the inspected full-text sections do not state the alternating cycle price rule. Related work on distributed spectral optimization concerns other constraints and numerical methods. The present contribution is the combined explicit positive-price formula, finite-size interpolation, and all-edge uniqueness on an infinite cycle family, not the generic semidefinite programming framework or Fourier diagonalization alone.

## Limitations
The theorem does not address odd cycles, nonalternating edge prices, discrete-time SLEM optimization, normalized Laplacians, per-node caps, or other graph families. No independence or publication-priority assertion is made; specialized earlier coverage of this exact price-constrained periodic design remains possible. Numerical tests are finite corroboration only.

## References
1. A. Ghosh and S. Boyd, "Upper bounds on algebraic connectivity via convex optimization," *Linear Algebra and its Applications* 418 (2006), 693--707. DOI: 10.1016/j.laa.2006.03.006. Publicly available May 5, 2006.
2. Y. Wan et al., "On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity," *Proceedings of the 47th IEEE Conference on Decision and Control* (2008), 805--810. DOI: 10.1109/CDC.2008.4738734.
3. L. Kempton, G. Herrmann, and M. di Bernardo, "Self-organization of weighted networks for optimal synchronizability," arXiv:1505.07279 (May 27, 2015).
