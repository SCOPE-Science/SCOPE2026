# D-optimal minimum-horizon control of priced weighted stars

## Finding
Let \(m\ge1\), \(B>0\), and let \(c_1,\ldots,c_m>0\) be given spoke prices. A weighted star has hub \(0\), leaves \(1,\ldots,m\), and nonnegative spoke conductances \(w_i\), subject to \(\sum_{i=1}^m c_iw_i=B\). Let \(L(w)\) be its symmetric graph Laplacian, put \(P(w)=I-\eta L(w)\), and fix \(0<\eta\le \min_i c_i/B\). Thus \(P(w)\) is nonnegative and row-stochastic at every feasible allocation. Place one scalar control input at the hub: \(z_{t+1}=P(w)z_t+e_0u_t\). At the minimum possible full-controllability horizon \(T=m+1\), define
\[
 C_T(w)=[e_0,P(w)e_0,\ldots,P(w)^m e_0],\qquad
 W_T(w)=C_T(w)C_T(w)^{\mathsf T}.
\]
The D-optimal design maximizes \(\det W_T(w)\), the squared volume factor of the unit-input-energy reachable ellipsoid.

**Theorem (all positive prices).** Write \(d=m(m+1)/2\). For every feasible \(w\),
\[
 \det W_T(w)=\eta^{2d}\left(\prod_{i=1}^m w_i\right)^2
 \prod_{1\le i<j\le m}(w_j-w_i)^2.
\]
The determinant is positive precisely when all conductances are positive and pairwise distinct. Every maximizer is strictly positive with distinct conductances, and it assigns larger conductances to no more expensive spokes: if \(c_i>c_j\), then \(w_i<w_j\). For a prescribed ordering \(c_1\ge\cdots\ge c_m\), there is exactly one maximizer satisfying \(0<w_1<\cdots<w_m\). It is the unique ordered solution of the following system, including its budget equation:
\[
 \boxed{\quad
 \frac1{w_i}+\sum_{j\ne i}\frac1{w_i-w_j}
 =\frac{d}{B}c_i\quad(1\le i\le m),
 \qquad\sum_{i=1}^m c_iw_i=B.\quad}
\]
If prices tie, swapping the associated leaf labels gives all other maximizers. Consequently the theorem completely specifies the global optimum for every price vector, without a combinatorial search over weight orderings.

**Equal-price closed form.** If \(c_i=c>0\) for all leaves, let \(0<z_1<\cdots<z_m\) be the roots of the classical generalized Laguerre polynomial \(L_m^{(1)}\). Then, up to leaf permutation, the unique optimal multiset is
\[
 \boxed{\quad w_i=\frac{B}{c\,m(m+1)}z_i.\quad}
\]
Its exact maximum Gramian determinant is
\[
 \boxed{\quad
 \max\det W_T=\left(\frac{\eta B}{c\,m(m+1)}\right)^{m(m+1)}
 ((m+1)!)^2\prod_{j=1}^{m}j^j(j+1)^{j-1}.\quad}
\]
For \(m=2\) with prices \(c_1\ge c_2\), put
\[
 t=\frac{c_1+c_2+\sqrt{c_1^2+c_1c_2+c_2^2}}{c_2}.
\]
Then the unique ordered optimum has \(w_1=B/(c_1+c_2t)\), \(w_2=tw_1\). In particular, for \(c_1=c_2=B=\eta=1\), the optimal weights are \((3-\sqrt3)/6\) and \((3+\sqrt3)/6\), and \(\max\det W_3=1/108\).

## Assumptions and scope
All networks are undirected stars with one controllable hub, real nonnegative symmetric spoke weights, positive linear price coefficients, and a strictly positive exact budget. The finite horizon is exactly the number \(m+1\) of network vertices. The bound on \(\eta\) ensures a valid stochastic update for **every** feasible allocation; the determinant theorem itself remains algebraically true for any nonzero real \(\eta\). The control input is a scalar of fixed unit normalization at the hub. If a control horizon has fewer than \(m+1\) steps, the controllability matrix has fewer than \(m+1\) columns and the full-state Gramian is singular for every weight allocation.

## Proof
**1. Exact controllability determinant.** Let \(b=e_0\) and \(v^{(k)}=L(w)^kb\). For each leaf \(i\),
\[
 v_i^{(k+1)}=w_i v_i^{(k)}-w_i v_0^{(k)},\qquad
 v_i^{(0)}=0.
\]
The scalar \(v_0^{(k)}\) is common to all leaves. Induction shows that for \(1\le k\le m\), \(v_i^{(k)}\) is the negative of a monic degree-\(k\) polynomial in \(w_i\), with zero constant term and all lower-degree coefficients independent of the leaf index. Expanding the determinant of \([b,Lb,\ldots,L^mb]\) along the first column and subtracting appropriate earlier columns leaves a Vandermonde matrix. Consequently
\[
 \det[b,Lb,\ldots,L^mb]
 =(-1)^m\left(\prod_iw_i\right)\prod_{i<j}(w_j-w_i).
\]
The binomial expansion of \(P^kb=(I-\eta L)^kb\) is a triangular column transformation of this Krylov matrix with diagonal entries \(1,-\eta,(-\eta)^2,\ldots,(-\eta)^m\). Its determinant has absolute factor \(\eta^d\). Since \(W_T=C_TC_T^{\mathsf T}\), squaring yields the claimed exact Gramian determinant, including all boundary cases.

**2. Optimal ordering and existence.** A positive, distinct, feasible vector exists, hence the maximum is strictly positive. The feasible closed polytope is compact. A zero weight or a collision of weights forces the determinant to zero, so every maximizer is interior with distinct weights. Suppose \(c_i<c_j\) but \(w_i<w_j\). Swapping these two weights reduces total cost by \((c_j-c_i)(w_j-w_i)>0\) and leaves the absolute determinant factor unchanged. Scaling all swapped weights upward to exhaust the budget strictly increases the determinant because it is homogeneous of positive degree \(2d\). Hence an optimum has the reverse price/weight order.

**3. Complete price-sensitive optimizer.** Fix \(c_1\ge\cdots\ge c_m\) and the chamber \(0<w_1<\cdots<w_m\). Maximizing the determinant is equivalent to maximizing
\[
 \Phi(w)=\sum_i\log w_i+\sum_{i<j}\log(w_j-w_i)
\]
subject to \(\sum_i c_iw_i=B\). Every logarithm is strictly concave on its positive linear argument, and \(\sum_i\log w_i\) has strictly negative-definite Hessian. Thus \(\Phi\) is strictly concave on this convex chamber. It tends to \(-\infty\) at all chamber boundaries within the budget simplex, so the maximum exists uniquely inside. The Lagrange equations are
\[
 \frac1{w_i}+\sum_{j\ne i}\frac1{w_i-w_j}=\lambda c_i.
\]
Multiply by \(w_i\), sum over \(i\), and pair the terms corresponding to unordered pairs of leaves; each such pair contributes exactly one. This yields \(\lambda B=m+\binom m2=d\), proving the displayed price-sensitive equations and their sufficiency and uniqueness. Equal-price label permutations are the only ambiguity.

**4. Equal prices and special polynomials.** Define the monic Laguerre polynomial \(p_m(x)=(-1)^m m!L_m^{(1)}(x)\). Its \(m\) roots are positive and distinct; it satisfies
\[
 xp_m''+(2-x)p_m'+mp_m=0,
 \qquad\sum_{i=1}^m z_i=m(m+1).
\]
At each root \(z_i\), the logarithmic derivative identity \(p_m''(z_i)/p_m'(z_i)=2\sum_{j\ne i}(z_i-z_j)^{-1}\), together with the differential equation, gives
\[
 \frac1{z_i}+\sum_{j\ne i}\frac1{z_i-z_j}=\frac12.
\]
Scaling \(z_i\) by \(B/[c\,m(m+1)]\) therefore satisfies the price-sensitive equations, and strict concavity makes it the unique optimum up to leaf permutation. The Laguerre root product is \(\prod_i z_i=(m+1)!\), while its monic discriminant is
\[
 \prod_{i<j}(z_j-z_i)^2=\prod_{j=1}^m j^j(j+1)^{j-1}.
\]
Here is an explicit resultant derivation. Write \(\mathcal R_m=\operatorname{Res}(p_m,p_{m-1})\). The recurrence evaluated at the roots of \(p_{m-1}\) gives
\[
 \mathcal R_m=[-m(m-1)]^{m-1}\mathcal R_{m-1},\qquad\mathcal R_1=1.
\]
At every root \(z_i\) of \(p_m\), the derivative identity gives \(p_m'(z_i)=m(m+1)p_{m-1}(z_i)/z_i\). Hence
\[
 |\operatorname{Res}(p_m,p_m')|
 =\frac{[m(m+1)]^m}{(m+1)!}
   \prod_{k=2}^m[k(k-1)]^{k-1}
 =\prod_{j=1}^m j^j(j+1)^{j-1}.
\]
The discriminant of a monic polynomial with simple real roots is the positive absolute value of this resultant, which proves the asserted product. Substitution into the exact Gramian determinant yields the closed maximum. For \(m=2\), substituting \(t=w_2/w_1>1\) reduces the weighted objective to a positive constant times \(t(t-1)/(c_1+c_2t)^3\); its unique critical point gives the stated quadratic-root formula.

## Verification
Run the included, standard-library-only `verify.py` with Python 3. It builds weighted-star stochastic matrices with exact rational arithmetic, constructs their minimum-horizon reachability Gramians, and checks the determinant formula for \(m=1,\ldots,6\). It also recomputes monic Laguerre polynomials by recurrence and checks their discriminants exactly through degree seven, plus four distinct two-leaf price instances against their stationarity equations. A successful execution prints `VERIFY_OK`. These bounded checks are supplementary; the universal claims follow from the analytical arguments above.

## Relationship to prior work
Sundaram and Hadjicostis gave general structured controllability criteria, including a four-dimensional Vandermonde-factor determinant for an independent-parameter directed example. The present matrix imposes symmetric undirected Laplacian coupling and optimizes the *magnitude* of a finite-horizon Gramian determinant under arbitrary positive edge prices, which that example does not address. Pasqualetti, Zampieri and Bullo explained the Gramian determinant's reachable-volume interpretation but did not solve this all-size priced-star conductance-design problem. The classical Stieltjes interpretation of Laguerre roots supplies a known electrostatic identity, not a previously asserted network design result. Gautschi optimized the **condition number** of Vandermonde matrices, a distinct objective; his nonnegative-node optimum can place a node at zero, while the determinant optimum here must have strictly positive, distinct conductances. These distinctions do not prove global historical priority.

## Limitations
D-optimality concerns the determinant of the finite-horizon Gramian, not its smallest eigenvalue, condition number, trace inverse, infinite-horizon energy, or actual control actions under actuator saturation. The minimum horizon and hub-input normalization are essential to the stated volume interpretation. The all-price optimum is given by an exact, uniquely soluble nonlinear system rather than elementary radicals for arbitrary \(m\); the Laguerre formula is restricted to equal prices. Independent validation and a comprehensive historical-priority review have not been performed.

## References
1. Shreyas Sundaram and Christoforos N. Hadjicostis, “Structural Controllability and Observability of Linear Systems Over Finite Fields With Applications to Multi-Agent Systems,” *IEEE Transactions on Automatic Control* 58 (2013), 60–73, DOI: 10.1109/TAC.2012.2204155.
2. Fabio Pasqualetti, Sandro Zampieri, and Francesco Bullo, “Controllability Metrics, Limitations and Algorithms for Complex Networks,” arXiv:1308.1201 (first posted 2013-08-06).
3. F. Alberto Grünbaum, “Electrostatic interpretation for the zeros of certain polynomials and the Darboux process,” *Journal of Computational and Applied Mathematics* 133 (2001), 397–412, DOI: 10.1016/S0377-0427(00)00661-0.
4. Walter Gautschi, “Optimally Conditioned Vandermonde Matrices,” *Numerische Mathematik* 24 (1975), 1–12.
