# Exact Morse-index classification of separated McKean fronts in periodic necklace media

## Finding

The stationary multi-fronts of the periodic-coefficient McKean equation have an **exact finite-dimensional spectral index**. Moreover, every sufficiently separated crossing word has a completely determined index: **the number of letters Q in the word**. Hence, among the \(2^m\) front profiles with an odd number \(m\geq3\) of crossings in prescribed sufficiently separated periods, precisely \(\binom m k\) have \(k\) positive eigenvalues in the natural selfadjoint transmission linearization. Exactly one, the all-P profile, has strictly negative spectral bound. None has a neutral eigenvalue.

The theorem is a **spectral** statement for the scalar periodic-diffusion problem (or the paired-edge-symmetric subspace of the associated necklace graph), not a theorem of nonlinear Lyapunov stability of the discontinuous-reaction semiflow. The existence and exact \(2^m\) count of these fronts is an input from Mori, Ogawa and Sintavanuruk [1, Theorem 5.3]; the spectral classification is the result established here.

## Assumptions and scope

Let \(0<\alpha<1\), \(L_1,L_2>0\), \(L=L_1+L_2\), and let \(p:\mathbb R\to(0,\infty)\) be the \(L\)-periodic coefficient

\[
p(x)=\begin{cases}
1,&kL\leq x<kL+L_1,\\
\alpha^{-1},&kL+L_1\leq x<(k+1)L,
\end{cases}\qquad k\in\mathbb Z.
\]

The equation is \(u_t=(p u_x)_x+f_{\mathrm{MK}}(u,a)\) on the real line, where \(f_{\mathrm{MK}}(u,a)=-u+\mathbf1_{\{u\geq a\}}\) and \(0<a<1\). A stationary front is a bounded weak solution with limits \(u(-\infty)=1\), \(u(+\infty)=0\), and finitely many *simple* threshold crossings \(\rho_1<\cdots<\rho_m\) lying strictly inside constant-coefficient intervals. Weak solutions have continuous \(u\) and \(p u_x\) at coefficient interfaces. All crossings under consideration have nonzero \(u_x\).

Define the strictly positive operator \(B=-(p\partial_x)\partial_x+1\) on \(L^2(\mathbb R)\) through its quadratic form \(\int(p|v_x|^2+|v|^2)dx\) on \(H^1(\mathbb R)\). Let \(G(x,y)\) denote its positive symmetric resolvent kernel, \(B^{-1}\), and define the matching function

\[
V_s(x)=\int_{-\infty}^sG(x,y)\,dy,\qquad b(s)=V_s(s).
\]

By [1, Lemma 3.5], \(b\) is periodic, strictly decreasing on \((0,L_1)\) and strictly increasing on \((L_1,L)\). Write \(a_-=b(L_1)\) and \(a_+=b(0)\). Fix \(a\in(a_-,a_+)\). For each \(\theta\in\{a,1-a\}\), there are exactly two simple phases solving \(b(s)=\theta\): \(s_P(\theta)\in(0,L_1)\), where \(b'<0\), and \(s_Q(\theta)\in(L_1,L)\), where \(b'>0\).

For odd \(m\geq3\), choose integers \(N_1<\cdots<N_m\) whose minimum consecutive separation is \(n\), and choose a word \(w=(w_1,\ldots,w_m)\in\{P,Q\}^m\). Theorem 5.3 of [1] produces a unique front with exactly one crossing in each designated period and no others, with

\[
\rho_i=N_iL+s_{w_i}(\theta_i)+O(\nu^{-n}),\quad
\theta_i=\begin{cases}a,&i\text{ odd},\\1-a,&i\text{ even},\end{cases}
\]

where \(\nu>1\) is the expanding Floquet multiplier of \((p v_x)_x=v\). The constants in the asymptotic estimates may depend on the fixed coefficients, threshold and crossing number, but not the particular choice of distant periods or word.

At any such stationary profile \(u\), define the *transmission linearization* \(\mathcal L_u\) as the selfadjoint operator with quadratic form

\[
\mathfrak q_u[v]=
-\int_{\mathbb R}(p|v_x|^2+|v|^2)\,dx
+\sum_{i=1}^m\frac{|v(\rho_i)|^2}{|u_x(\rho_i)|},
\qquad v\in H^1(\mathbb R).
\]

This is the distributional shape linearization \((p v_x)_x-v+\sum_i |u_x(\rho_i)|^{-1}v(\rho_i)\delta_{\rho_i}\), equivalently a differential operator away from crossings with transmission conditions \([p v_x]_{\rho_i^-}^{\rho_i^+}=-v(\rho_i)/|u_x(\rho_i)|\). Its Morse index is the number of strictly positive eigenvalues with multiplicity.

**Theorem.** For any stationary profile with finitely many simple crossings, form the symmetric matrix

\[
\mathcal K_{ij}=
\frac{G(\rho_i,\rho_j)}{
\sqrt{|u_x(\rho_i)|\,|u_x(\rho_j)|}},\qquad1\leq i,j\leq m.
\]

Then

\[
\operatorname{ind}_+(\mathcal L_u)
=\#\{\text{eigenvalues of }\mathcal K\text{ strictly greater than }1\},
\qquad
\dim\ker\mathcal L_u=\dim\ker(\mathcal K-I).
\]

For each fixed odd \(m\geq3\), there is a finite \(n_m^{\mathrm{spec}}\) such that for all \(n\geq n_m^{\mathrm{spec}}\), every one of the \(2^m\) fronts of [1, Theorem 5.3] satisfies

\[
\boxed{\operatorname{ind}_+(\mathcal L_{u_w})=\#\{i:w_i=Q\},
\qquad\ker\mathcal L_{u_w}=\{0\}.}
\]

In particular, \(\binom m k\) of these fronts have exactly \(k\) positive linearization eigenvalues; exactly one has no nonnegative spectrum, and it is the all-P front.

## Proof

**1. Resolvent and point interactions.** Uniform ellipticity gives \(B\geq I\); \(G\) is symmetric, strictly positive and continuous, and is exponentially decreasing with spatial separation. In the present piecewise constant periodic setting this also follows from the explicit positive growing/decaying Floquet solutions in [1, Sections 3.2 and 3.6]. Since the point evaluations are continuous on \(H^1(\mathbb R)\), the quadratic form above defines a selfadjoint, upper-semibounded operator. Its essential spectrum coincides with that of \(-B\), hence is contained in \(( -\infty,-1]\).

For \(t\geq0\), let \(G_t\) be the kernel of \((B+t)^{-1}\), and set

\[
\mathcal K(t)_{ij}=
\frac{G_t(\rho_i,\rho_j)}{
\sqrt{|u_x(\rho_i)|\,|u_x(\rho_j)|}}.
\]

The eigen-equation \(\mathcal L_u v=t v\) is equivalent to \((B+t)v=\sum_i |u_x(\rho_i)|^{-1}v(\rho_i)\delta_{\rho_i}\). Applying the resolvent and evaluating at the crossing points gives \(z=\mathcal K(t)z\), where \(z_i=v(\rho_i)/\sqrt{|u_x(\rho_i)|}\). Conversely, any nonzero such vector reconstructs the eigenfunction by this resolvent formula; the reconstructions preserve geometric multiplicities. The matrix \(\mathcal K(t)\) is positive definite for distinct crossing points. As \(t\) increases, it decreases *strictly in quadratic-form order*, because the resolvent identity gives

\[
(B+t_1)^{-1}-(B+t_2)^{-1}
=(t_2-t_1)(B+t_1)^{-1}(B+t_2)^{-1}>0
\]

for \(0\leq t_1<t_2\) on nonzero finite linear combinations of the distinct point masses. All eigenvalues of \(\mathcal K(t)\) tend to zero as \(t\to\infty\), by the one-dimensional elliptic resolvent bound. Each ordered eigenvalue initially above 1 therefore crosses 1 exactly once at positive \(t\), including multiplicities at coincident crossings. Eigenvalues initially below 1 never cross. At \(t=0\) the same equivalence gives the kernel dimension. This proves the exact matrix index formula.

**2. Isolated crossing slope.** Differentiate \(b(s)=V_s(s)\) with respect to \(s\) inside a coefficient interval. Since \(\partial_s V_s(x)=G(x,s)\),

\[
b'(s)=\partial_xV_s(s)+G(s,s),\qquad
-\partial_xV_s(s)=G(s,s)-b'(s)>0.
\]

The last inequality follows from strict decrease of the isolated front \(V_s\) through its crossing. The complementary isolated increasing profile \(1-V_s\) has the same positive crossing slope magnitude. Thus the single-crossing Green ratio at a phase \(s\) is

\[
d(s)=\frac{G(s,s)}{G(s,s)-b'(s)},
\quad
0<d(s)<1\text{ when }s=s_P(\theta),
\quad d(s)>1\text{ when }s=s_Q(\theta).
\]

The inequalities are strict because the corresponding roots are simple and \(G(s,s)-b'(s)>0\). This diagonal sign distinction is valid for both downward and upward crossings.

**3. Decoupling of separated interfaces.** Each odd-crossing front with threshold set \(\{\rho_i\}\) has the representation

\[
u_w(x)=\sum_{j=1}^m(-1)^{j-1}V_{\rho_j}(x),
\]

since its forcing indicator equals the corresponding alternating sum of half-line indicators. The source's exponential tail estimates [1, equations (5.6)--(5.10)] give, with \(\sigma_i=(-1)^{i-1}\),

\[
u_w'(\rho_i)=\sigma_i\partial_xV_{\rho_i}(\rho_i)
+O(\nu^{-n}),
\quad
|u_w'(\rho_i)|=
G(s_i^*,s_i^*)-b'(s_i^*)+O(\nu^{-n}),
\]

where \(s_i^*=s_{w_i}(\theta_i)\), using the periodicity and local regularity of \(G(x,x)\) and \(b'\) and the source's crossing-location estimate. The nonzero isolated crossing slopes make the absolute-value step legitimate once the gap is large. Also, for \(i\ne j\), \(|G(\rho_i,\rho_j)|\leq C\nu^{-n}\); hence

\[
\mathcal K(0)=\operatorname{diag}(d(s_1^*),\ldots,d(s_m^*))
+O(\nu^{-n})
\]

in operator norm, uniformly over the finite collection of words and allowed period placements for fixed \(m\). The diagonal entries stay a positive distance from 1 because there are only four possible isolated phases and \(b'\ne0\) at each. Choose \(n_m^{\mathrm{spec}}\) large enough that the operator-norm error is smaller than half this separation. Weyl's eigenvalue inequality then shows that exactly the Q entries lie above 1, none equals 1, and all P entries lie below 1. Apply Step 1 to conclude the stated index and kernel count.

The essential spectrum lies strictly below zero. Thus in the all-P case the *entire* spectrum has a strictly negative upper bound; in every other case a genuine positive eigenvalue exists. Counting the words with \(k\) Q letters gives \(\binom m k\). This completes the proof.

## Verification

The standalone `checker.py` constructs the Floquet solutions for the two constant-coefficient zones via exact transfer-matrix formulas (evaluated in floating point), solves the original nonlinear threshold-matching equations for each crossing word, and builds the Green matrix from those solutions. For \(\alpha=1/4\), \(L_1=0.8\), \(L_2=1.6\), it checked all eight three-crossing words at \(a=1/2\), with index multiplicities \(1,3,3,1\), and all 32 five-crossing words at \(a=0.42\), with index multiplicities \(1,5,10,10,5,1\). Each calculated crossing was transverse, each matching residual below \(10^{-8}\), and no computed Green eigenvalue was within \(0.02\) of 1. The proof above, not these finite computations, establishes the assertion for all admissible parameters, large enough gaps, and odd crossing counts.

To reproduce: run `python checker.py` with Python, NumPy and SciPy installed. The checker evaluates the exact transfer formulas numerically; it is a diagnostic rather than a rigorous interval certificate.

## Relationship to prior work

Mori, Ogawa and Sintavanuruk [1] prove the explicit pinning interval, stable/unstable single-crossing branches, and existence/exact \(2^m\) count of distant multi-fronts. In Sections 1 and 6 they explicitly leave stability of the nonmonotone profiles open. Their theorem supplies the existence and exponential separation needed here, but **does not imply a spectral index of any of the multi-front words** without the new point-interaction argument. The present theorem does not claim their nonlinear stability result for multi-crossing fronts.

Bastiaansen, Doelman and Kaper [2] establish existence and stability patterns for *small-amplitude smooth topographic perturbations* of the cubic Allen--Cahn equation, including asymptotic multi-front eigenvalue signs. They do not consider the fixed, order-one, discontinuous necklace diffusion contrast or the discontinuous McKean reaction, and their small-heterogeneity assumptions do not imply this exact Green-matrix certificate. Their qualitative prediction of a single stable all-P pattern among \(2^m\) is an important precedent, not claimed as new here.

The rank-finite resolvent / point-interaction method is classical. The contribution is its application to this explicitly constructed periodic necklace family, including the exact arbitrary-gap matrix criterion and the complete Q-letter Morse-index count in the large-gap regime.

## Limitations

The result establishes spectral properties only of the specified selfadjoint **transmission** linearization. It does not establish Frechet differentiability of the discontinuous-reaction semiflow in a chosen function space, nonlinear Lyapunov or asymptotic stability, behavior under disturbances that break paired-edge symmetry on the full necklace graph, or an optimal minimum separation. The bound \(n_m^{\mathrm{spec}}\) is existential; no optimal or explicit integer formula is asserted. At short crossing gaps, the Green matrix remains an exact spectral index test but the simple Q-count need not hold. Broader literature priority is not independently certified.

## References

[1] Y. Mori, T. Ogawa and C. Sintavanuruk, *Stationary bistable fronts on a periodic necklace graph: existence, stability and multiplicity*, arXiv:2610.32917v1 (first public submission 23 October 2026), especially Lemma 3.5, Section 3.6, Theorem 5.3 and Section 6. https://arxiv.org/html/2610.32917v1

[2] R. Bastiaansen, A. Doelman and T. J. Kaper, *Multi-front dynamics in spatially inhomogeneous Allen--Cahn equations*, arXiv:2501.16195 (first public submission 27 January 2025), Sections 3, 4 and 6. https://arxiv.org/abs/2501.16195
