# Two exceptional Lee–Yang zeros in heterogeneous antiferromagnetic Ising stars

## Finding

**Theorem (antiferromagnetic star zero geometry).** Let \(m\geq1\) and let \(q_1,\ldots,q_m\) be arbitrary real numbers greater than \(1\), with no homogeneity or genericity assumptions. Consider the Lee–Yang polynomial of the Ising star with \(m\) leaves,
\[
Z_m(z)=\prod_{i=1}^{m}(1+q_i z)+z\prod_{i=1}^{m}(q_i+z).
\]
Set \(a_i=q_i^{-1}\in(0,1)\) and \(P_m=\prod_i a_i\).

1. All \(m+1\) zeros are simple. Exactly \(m-1\) lie on the unit circle; the other two are negative, real and reciprocal, of the form \(-x_m\) and \(-x_m^{-1}\), with \(0<x_m<P_m<1\). The inner exceptional modulus is the **unique** solution \(x\in(0,\min_i a_i)\) of
   \[
   x=\prod_{i=1}^m\frac{a_i-x}{1-a_i x}.
   \]
   The circle zero \(-1\) occurs exactly when \(m\) is even.

2. If a family of such stars satisfies \(a_i\leq a_*<1\), then, for every \(m\geq1\),
   \[
   0<1-\frac{x_m}{P_m}\leq\frac{m a_*^{m-1}}{1-a_*^{m+1}}.
   \]
   Thus \(x_m/P_m\longrightarrow1\) as \(m\to\infty\), uniformly over all admissible heterogeneous couplings. In particular the two exceptional zero moduli are asymptotic to \(P_m\) and \(P_m^{-1}\).

3. Put \(c_*=(1-a_*)/(1+a_*)\). Whenever \(m c_*>1\), let \(N_m([\alpha,\beta))\) count the unit-circle zeros with arguments in \([\alpha,\beta)\), for \(-\pi\leq\alpha<\beta\leq\pi\). Then
   \[
   \left|\frac{N_m([\alpha,\beta))}{m+1}-\frac{1}{2\pi m}\sum_{i=1}^m\int_\alpha^\beta\frac{1-a_i^2}{1+a_i^2+2a_i\cos\theta}\,d\theta\right|\leq\frac3{m+1}.
   \]
   Hence if \(m^{-1}\sum_i\delta_{a_i}\) converges weakly to a probability measure \(\mu\) on \([0,a_*]\), the normalized empirical measure of **all** \(m+1\) zeros converges weakly in the complex plane to the probability measure on the unit circle with angular density
   \[
   \rho_\mu(\theta)=\frac1{2\pi}\int_{[0,a_*]}\frac{1-a^2}{1+a^2+2a\cos\theta}\,d\mu(a).
   \]
   The two exceptional zeros do not contribute to this weak limit because their total weight is \(2/(m+1)\).

The three assertions together describe the finite zero geometry, the exponential location of its exceptions, and the limiting circular bulk for a canonical inhomogeneous antiferromagnetic tree.

## Assumptions and scope

The star has one central spin and \(m\) leaves; every edge interaction is **strictly antiferromagnetic**. The parameter \(q_i=e^{-2J_i}\) uses inverse temperature absorbed into \(J_i<0\); the external field fugacity is uniform at every vertex. The displayed polynomial differs from the physical partition function only by a strictly positive factor independent of \(z\). There are no vertex-dependent fields, additional interactions, thermodynamic boundary conditions, or restrictions on how the couplings vary across a finite star.

The zero count and simplicity require only \(q_i>1\). The uniform outlier approximation and limiting empirical law additionally require one common \(a_*<1\); weak convergence of the empirical \(a_i\) is needed only to identify a unique limiting bulk density. A single arbitrary star requires no such convergence assumption.

## Proof

**1. Spin-sum reduction and reciprocity.** With \(q_i\) the cross-spin weight, conditioning on whether the center belongs to the selected spin set gives the two products in \(Z_m\). Write \(Q=\prod_iq_i=P_m^{-1}\). Division by \(Q\) gives the polynomial
\[
F_m(z):=Q^{-1}Z_m(z)=\prod_i(z+a_i)+z\prod_i(1+a_i z).
\]
It has degree \(m+1\) and satisfies \(z^{m+1}F_m(1/z)=F_m(z)\). Indeed, reversing the first product produces the second and conversely. In particular, all nonzero roots occur in reciprocal pairs. Also \(F_m(0)=P_m>0\).

**2. Count every unit-circle zero.** Define the finite Blaschke product
\[
B_m(z)=\prod_{i=1}^m\frac{z+a_i}{1+a_i z}.
\]
For \(|z|=1\), every factor has modulus one, and none of the denominators vanishes. Thus \(F_m(z)=0\) exactly when \(B_m(z)=-z\). For \(-\pi\leq\theta\leq\pi\), choose the continuous phase \(\psi_a(\theta)\) of \((e^{i\theta}+a)/(1+a e^{i\theta})\), normalized by \(\psi_a(0)=0\), \(\psi_a(\pm\pi)=\pm\pi\). Direct differentiation gives
\[
\psi_a'(\theta)=\frac{1-a^2}{1+a^2+2a\cos\theta}>0,\qquad
\psi_a''(\theta)=\frac{2a(1-a^2)\sin\theta}{(1+a^2+2a\cos\theta)^2}>0
\quad(0<\theta<\pi).
\]
Set \(\Delta_m(\theta)=\sum_i\psi_{a_i}(\theta)-\theta\). The equation on the circle is \(\Delta_m(\theta)\in(2\mathbb Z+1)\pi\). On \((0,\pi)\), \(\Delta_m\) is strictly convex, starts at \(0\), ends at \((m-1)\pi\), and satisfies \(\Delta_m(\theta)>-\theta>-\pi\). Therefore it meets each positive odd multiple of \(\pi\) below its terminal value exactly once; if the terminal value is itself odd, it is met only at \(\theta=\pi\). Negative angles supply conjugate roots, with \(-1\) counted once rather than twice. There are exactly \(m-1\) distinct unit roots. At each crossing, \(\Delta_m'(\theta)>0\), so each zero is simple (equivalently the angular derivative of \(B_m(e^{i\theta})+e^{i\theta}\) is nonzero). At \(\theta=\pi\), the same follows from \(\sum_i(1+a_i)/(1-a_i)-1>0\) when \(m\) is even. The argument also covers \(m=1\), when there are no unit-circle roots.

**3. Identify the two noncircular roots.** For \(0<x<\min_i a_i\), the function
\[
g(x)=B_m(-x)=\prod_i\frac{a_i-x}{1-a_i x}
\]
is strictly positive and strictly decreasing: each factor has derivative \(-(1-a_i^2)/(1-a_i x)^2<0\). It decreases from \(P_m\) at \(x=0\) to \(0\) at \(x=\min_i a_i\). Hence \(g(x)=x\) has exactly one solution \(x_m\) in this interval, and \(x_m=g(x_m)<P_m<1\). The polynomial therefore has a simple zero at \(-x_m\), and reciprocal symmetry supplies a distinct simple zero at \(-x_m^{-1}\). Counting degrees together with Step 2 excludes any further zeros and proves simplicity globally.

**4. Bound the escaping pair.** At the root, put \(u_m=x_m/P_m\in(0,1)\). Then
\[
u_m=\prod_i\frac{1-x_m/a_i}{1-a_i x_m}
=\prod_i(1-t_i),\qquad
t_i=\frac{x_m(1-a_i^2)}{a_i(1-a_i x_m)}\in(0,1).
\]
Using \(1-\prod_i(1-t_i)\leq\sum_i t_i\), \(x_m<P_m\), \(P_m/a_i\leq a_*^{m-1}\), and \(1-a_i x_m\geq1-a_*^{m+1}\), gives the claimed bound. The right side tends to zero because \(a_*<1\). No Taylor expansion or unproved asymptotic hypothesis is needed.

**5. Count circular roots in arcs and take the limit.** For all \(\theta\),
\[
\psi_a'(\theta)\geq\frac{1-a}{1+a}\geq c_*.
\]
Thus \(\Delta_m'(\theta)\geq m c_*-1>0\) whenever the stated condition holds. In the half-open argument interval \([-\pi,\pi)\), the unit roots are exactly the crossings of the equally spaced levels \((2k+1)\pi\). Their number in \([\alpha,\beta)\) therefore differs by at most one from \((\Delta_m(\beta)-\Delta_m(\alpha))/(2\pi)\). Substituting the derivative identity and normalizing by \(m+1\) yields the bound \(3/(m+1)\), since both the interval length fraction and the average integrated phase fraction are at most one. Under weak empirical convergence, the averaged Poisson kernels converge when integrated over any fixed arc; the limiting density is continuous. The arc discrepancy tends to zero, proving weak convergence of the circle-root submeasure. Finally the total mass of the two exceptional roots is \(2/(m+1)\), which vanishes against every bounded continuous test function on \(\mathbb C\). This gives weak convergence of the full empirical zero measures.

## Verification

A standalone Python checker in `verify.py` uses exact rational arithmetic for the partition coefficients and independent spin enumeration for small stars. It checks reciprocity, explicit negative-root intervals and bounds, the angular root equations, and the finite arc-discrepancy inequality on deterministic parameter families. Run `python3 verify.py` from the containing directory. Its output records the finite test counts. These tests are corroboration, not substitutes for the above proofs for every \(m\) and all real couplings.

For example, \((q_1,q_2,q_3)=(2,3,5)\) yields the exact polynomial \(1+40z+62z^2+40z^3+z^4\). Its two noncircular zeros are negative reciprocals, while its remaining two zeros are unit-modulus conjugates.

## Relationship to prior work

Chio, He, Ji and Roeder study Lee–Yang zeros on **ferromagnetic** Cayley trees using expanding Blaschke products; their coupling assumption is \(0<t<1\). Peters and Regts prove zero-free regions for bounded-degree graphs, including antiferromagnetic interactions, rather than a per-star zero census. Bencs, Buys, Guerini and Peters formulate antiferromagnetic tree recursions and prove density/nowhere-density statements for classes of Cayley and spherically symmetric trees. Sedik and collaborators study antiferromagnetic square lattices and fully connected mean-field polynomials. These established reductions and results are credited. The present claim is the all-heterogeneity **one-level star** count, simple reciprocal real exceptions, uniform multiplicative outlier approximation, and explicit finite circular discrepancy; no new claim is made for the elementary partition-polynomial identity or for the isolated use of Blaschke factors.

There is a bipartite spin-flip duality sending these antiferromagnetic stars to ferromagnetic stars with a reversed field fugacity at the center. This is **not** the homogeneous-field ferromagnetic problem: in particular, the ferromagnetic Lee–Yang circle theorem does not imply the absence or location of the two outliers under a staggered field. The limiting circular density has the same Poisson-kernel form that arises for the corresponding ferromagnetic reciprocal-parameter family; that algebraic coincidence by itself is not asserted as original.

## Limitations

The graph must be a star, all edge interactions must be strictly antiferromagnetic, and the field must be uniform. Nothing is proved about other antiferromagnetic trees, mixed-sign interactions, phase transitions in bounded-degree lattices, or root multiplicities at the excluded zero-coupling boundary \(q_i=1\). The uniform bulk and outlier approximations require \(a_i\leq a_*<1\). The explicit finite upper bound may be numerically vacuous for small \(m\), though it is asymptotically effective. Related finite-Blaschke fixed-point theory may encompass the qualitative circle-root count; the star-specific parameter bound and full quantitative statement must be compared separately when evaluating priority.

## References

- I. Chio, C. He, A. L. Ji, R. K. W. Roeder, *Limiting Measure of Lee–Yang Zeros for the Cayley Tree*, arXiv:1806.00403v1 (first public version 2018-06-01), https://arxiv.org/abs/1806.00403 .
- H. Peters and G. Regts, *Location of Zeros for the Partition Function of the Ising Model on Bounded Degree Graphs*, arXiv:1810.01699v1 (2018-10-03), https://arxiv.org/abs/1810.01699 .
- F. Bencs, P. Buys, L. Guerini, H. Peters, *Lee–Yang Zeros of the Antiferromagnetic Ising Model*, arXiv:1907.07479v1 (2019-07-17), https://arxiv.org/abs/1907.07479 .
- M. Sedik, J. M. Bhat, A. Dhar, B. S. Shastry, *Yang–Lee Zeros of Certain Antiferromagnetic Models*, arXiv:2309.14562v1 (2023-09-25), https://arxiv.org/abs/2309.14562 .
