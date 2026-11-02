# A sharp dimension threshold and logarithmic transient peak for Boolean heat flow on Lipschitz-free spaces

## Finding

Let \(Q_n=\{0,1\}^n\) have Hamming distance and distinguished vertex \(o=0\), and let \(\mathcal F(Q_n)\) be its real Lipschitz-free Banach space. For strictly positive coordinate rates \(a_1,\ldots,a_n\), let \(T_t\), \(t\geq0\), denote the linear noise semigroup on zero-total-mass measures: independently flip coordinate \(i\) with probability \((1-e^{-a_it})/2\). Set \(r_i=e^{-a_it}\). Its exact distance from the identity is

\[
\boxed{\|I-T_t\|_{\mathcal F(Q_n)\to\mathcal F(Q_n)}=\max_{1\leq i\leq n}\left\{1+r_i-2r_i\prod_{j\ne i}\frac{1+r_j}{2}\right\}.}
\]

For \(n=1\), this is \(1-r_1\); for \(n=2\), it is \(1-r_1r_2\). In every dimension \(n\geq3\), and for **every** strictly positive rate vector, the norm exceeds \(1\) at all sufficiently large finite times, then converges down to \(1\) as \(t\to\infty\). Thus dimension three is the exact threshold for a transient overshoot, even though \(T_t\) is a contraction for all \(t\geq0\).

For equal rates \(a_i=1\), let \(\rho=e^{-t}\). Then

\[
\|I-T_t\|=1+\rho-2\rho\left(\frac{1+\rho}{2}\right)^{n-1}.
\]

For each \(n\geq3\), this function has exactly one global peak at \(t_n=-\log\rho_n\), where \(\rho_n\in(0,1)\) is the unique solution of

\[
(1+n\rho_n)\left(\frac{1+\rho_n}{2}\right)^{n-2}=1.
\]

Writing \(M_n=\|I-T_{t_n}\|\), its sharp large-dimension law is

\[
\boxed{t_n=\frac{2\log n}{n}+O\!\left(\frac{(\log n)^2}{n^2}\right),\qquad M_n=2-\frac{2\log n+2}{n}+O\!\left(\frac{(\log n)^2}{n^2}\right).}
\]

The precise entry into the overshoot region is \(t> -\log(2^{1-1/(n-1)}-1)\). This theorem gives both the complete anisotropic finite-dimensional operator norm and the temporal geometry of its isotropic peak.

## Assumptions and scope

All scalars are real. The metric is the unweighted shortest-path Hamming metric. The rates \(a_i\) are strictly positive, so \(r_i\in(0,1)\) at finite positive time. The semigroup is defined on the zero-mass molecular realization of \(\mathcal F(Q_n)\); equivalently it is adjoint to the independent-coordinate Markov noise semigroup acting on Lipschitz functions modulo constants. Its generator on functions is

\[
(Lf)(x)=\frac12\sum_{i=1}^n a_i\bigl(f(x\oplus e_i)-f(x)\bigr),
\]

so that the degree-one Walsh eigenvalue in coordinate \(i\) is \(e^{-a_it}\). The norm is the Lipschitz-free transport norm, **not** the \(\ell_1\) or \(\ell_2\) operator norm on vertex functions. No extension to weighted Hamming distances or arbitrary metric graphs is asserted.

## Proof

**1. Edge molecules determine the operator norm.** Write \(m_{x,y}=\delta_x-\delta_y\). Every pair of cube vertices is joined by a shortest path of unit coordinate edges. Consequently its normalized molecule \(m_{x,y}/d(x,y)\) is a convex average of oriented edge molecules. Since these molecules generate the unit ball of \(\mathcal F(Q_n)\), the norm of any linear operator on this finite-dimensional space is the maximum norm of its images of unit edge molecules. Translation symmetry of \(T_t\) reduces this to one edge in each coordinate direction.

**2. The parallel-edge subspace has an exact \(\ell_1\) norm.** Fix a coordinate \(i\). For each \(u\in\{0,1\}^{n-1}\), let \(e_{i,u}\) be the oriented molecule from \((0,u)\) to \((1,u)\), with the coordinate \(i\) understood as the first slot in this notation. Then for every real coefficient family,

\[
\left\|\sum_{u}c_ue_{i,u}\right\|_{\mathcal F(Q_n)}=\sum_u|c_u|.
\]

The upper bound is the triangle inequality. For the lower bound, assign values \(f(0,u)=1\) and \(f(1,u)=0\) when \(c_u\geq0\), and reverse these values when \(c_u<0\). Since the function takes only values \(0\) and \(1\), it is \(1\)-Lipschitz on all cube edges and therefore on all cube pairs. Subtracting a constant makes it vanish at the basepoint without changing its molecular pairing. Its pairing is exactly \(\sum_u|c_u|\).

**3. Exact heat convolution.** Let \(p_{-i,t}(u)\) be the product Bernoulli probability of the flips outside coordinate \(i\):

\[
p_{-i,t}(u)=\prod_{j\ne i}\left(\frac{1-r_j}{2}\right)^{u_j}\left(\frac{1+r_j}{2}\right)^{1-u_j}.
\]

Convolving the initial edge molecule with all flips and grouping the flips of coordinate \(i\) gives

\[
T_te_{i,0}=r_i\sum_u p_{-i,t}(u)e_{i,u}.
\]

Thus, by step 2,

\[
\|(I-T_t)e_{i,0}\|=\left|1-r_ip_{-i,t}(0)\right|+r_i\sum_{u\ne0}p_{-i,t}(u)
=1+r_i-2r_i\prod_{j\ne i}\frac{1+r_j}{2},
\]

because \(0\leq r_ip_{-i,t}(0)\leq1\). Taking the maximum over directions, justified in step 1, establishes the exact formula for all \(n\geq1\), rates and times.

**4. Sharp dimension threshold.** For \(n=1\), the empty product gives \(1-r_1\); for \(n=2\), the two direction values both simplify to \(1-r_1r_2\). Both remain below \(1\) at finite time. For \(n\geq3\), each direction value exceeds \(1\) precisely when \(\prod_{j\ne i}(1+r_j)/2<1/2\). With strictly positive rates that product tends to \(2^{-(n-1)}<1/2\), while \(r_i>0\) at each finite time. Hence the norm eventually exceeds \(1\), and the formula also gives its limit \(1\) at infinity. The semigroup is contractive because it averages coordinate translations, each an isometry on the free space.

**5. Unique isotropic peak and asymptotics.** With all rates one, put \(h_n(\rho)=1+\rho-2\rho((1+\rho)/2)^{n-1}\). Direct differentiation yields

\[
h_n'(\rho)=1-(1+n\rho)\left(\frac{1+\rho}{2}\right)^{n-2}.
\]

For \(n\geq3\), the subtracted factor is strictly increasing, lies below \(1\) at \(\rho=0\), and exceeds \(1\) at \(\rho=1\). There is therefore a unique maximizing \(\rho_n\in(0,1)\). The equation \(h_n(\rho)=1\), for \(\rho>0\), is equivalent to \(((1+\rho)/2)^{n-1}=1/2\), giving the asserted threshold time.

To obtain the peak asymptotics put \(\varepsilon_n=1-\rho_n\). Taking logarithms of the critical-point equation gives

\[
(n-2)\log\left(1-\frac{\varepsilon_n}{2}\right)+\log(n+1-n\varepsilon_n)=0.
\]

Monotonicity first bounds \(\varepsilon_n=O((\log n)/n)\); expanding the two logarithms with uniform Taylor remainders then yields

\[
\varepsilon_n=\frac{2\log n}{n}+O\!\left(\frac{(\log n)^2}{n^2}\right).
\]

Therefore \(t_n=-\log(1-\varepsilon_n)\) has the stated expansion. The critical equation also gives the **exact** identity

\[
M_n=1+\rho_n-\frac{\rho_n(1+\rho_n)}{1+n\rho_n}.
\]

Substitution of the expansion for \(\rho_n\) yields \(M_n=2-(2\log n+2)/n+O((\log n)^2/n^2)\), completing the proof.

## Verification

The accompanying `verification_check.py` uses only the Python standard library. It exhausts all integral \(1\)-Lipschitz dual potentials on the cube for dimensions one through three, for rational heterogeneous noise parameters; total unimodularity of the edge-incidence matrix ensures integral extremizers. It then verifies exact rational parallel-edge shadow identities and explicit sign witnesses for dimensions one through nine, with heterogeneous rates. Output: `PASS 48 exhaustive integral Lipschitz-dual comparisons` and `PASS 360 exact rational anisotropic edge-shadow identities`.

As an additional numerical diagnostic, independent transport linear programs checked 30 isotropic and 40 heterogeneous cases through dimension five, all agreeing with the formula; these independent LP comparisons are not needed for the proof. Finite computations do not establish the infinite-dimensional-parameter quantifiers or the asymptotic result; those are proved analytically above.

## Relationship to prior work

Eskenazis (2023) developed discrete heat-flow methods for geometric problems on Hamming cubes, including metric type and embedding inequalities. Its heat-process definitions supply context, but its inspected statements and relevant semigroup sections do not calculate the free-space distance \(\|I-T_t\|\). Cúth and Doucha (2021) constructed norm-one projections from group actions on Lipschitz-free spaces; those group-invariant projections are distinct from finite-time heat operators.

A published result titled *Coordinate-shadow norm formula for Walsh projections on Hamming Lipschitz-free spaces* establishes exact norms of **idempotent Walsh spectral projections**. Its parallel-edge gradient mechanism is closely related to proof step 2 and is explicitly acknowledged. A heat multiplier has eigenvalues \(e^{-t\sum_{i\in S}a_i}\), rather than zero-one projection eigenvalues. The published statement does not give its finite-time operator-distance norm, the dimension-three overshoot threshold, its unique peak, or the logarithmic high-dimensional peak law. The related argument can be adapted, so conceptual closeness is a genuine originality risk rather than evidence of independence.

## Limitations

All calculations concern real free spaces of unweighted Boolean Hamming cubes and independent-coordinate noise; arbitrary graph Markov kernels, weighted graph metrics, and general \(p\)-free spaces are not covered. No claim is made about originality of the underlying noise kernel or the standard duality between earthmover norms and Lipschitz functions. The novelty claim is restricted to the exact **transient free-space operator-distance profile and its sharp phase/peak behavior**. Earlier equivalent formulations, particularly in Wasserstein semigroup stability or Dobrushin-type operator literature, remain possible.

## References

1. A. Eskenazis, *Some geometric applications of the discrete heat flow*, arXiv:2310.01868v1 (first public 2023-10-03). https://arxiv.org/html/2310.01868v1.
2. M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519v1 (first public 2021-04-23). https://arxiv.org/html/2104.11519v1.
3. *Coordinate-shadow norm formula for Walsh projections on Hamming Lipschitz-free spaces*, published mathematical record (2026-10-11). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-coordinate-shadow-norm-formula-for-walsh-projections-on-hamming--6d24f15eba8d.
