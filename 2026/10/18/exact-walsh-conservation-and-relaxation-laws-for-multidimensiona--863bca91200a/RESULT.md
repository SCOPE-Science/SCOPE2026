# Exact Walsh conservation and relaxation laws for multidimensional friend–foe opinion dynamics

## Finding

Consider the noiseless, infinite-population binary-issue friend–foe model defined below, with any number of issues \(n\ge2\), positive issue weights and update rates, and arbitrary admissible friendship/enmity thresholds. Every Walsh-character perturbation of its equal-frequency equilibrium has a **real, nonpositive, explicitly computable growth exponent**. A mode has exponent zero **if and only if its Walsh moment is an exact nonlinear first integral** of the full mean-field ODE. Consequently, the equilibria near equal frequencies form a real-analytic manifold, with precisely one conserved coordinate for each zero mode, and every sufficiently nearby trajectory converges exponentially to the uniquely selected equilibrium on its conservation level set.

When friendship and enmity use one threshold strictly above every similarity of distinct opinion strings, equal frequencies is locally exponentially stable if and only if \(n\ge3\). In that regime its spectral gap is an explicit function of the two smallest issue-update rates. In particular, under equal rates the slowest-decaying perturbations are **two-issue correlations**, not single-issue opinion imbalances. With two issues, the even-versus-odd opinion-pattern imbalance is conserved for *every* admissible threshold and the equal-frequency state is never an isolated attracting equilibrium.

## Assumptions and scope

Set \(G=(\mathbb Z/2\mathbb Z)^n\), \(Q=2^n\), and write \(s\oplus d\) for bitwise addition. An opinion is \(s\in G\), and \(x_s\ge0\), \(\sum_s x_s=1\), is its population frequency. Choose \(w_i>0\) with \(\sum_iw_i=1\), issue-change rates \(\gamma_i>0\), and thresholds \(0\le\alpha_e\le\alpha_f\le1\). The similarity of an opinion displacement \(d\) is
\[
\sigma(d)=\sum_{j:d_j=0}w_j.
\]

A focal individual comparing with a target at displacement \(d\) flips issue \(i\) precisely when \(d_i=1\) and \(\sigma(d)>\alpha_f\) (imitating a friend), or when \(d_i=0\) and \(\sigma(d)<\alpha_e\) (disagreeing with an enemy). The threshold inequalities are strict; equality gives no flip. Define the indicator
\[
K_i(d)=\mathbf1\{d_i=1,\ \sigma(d)>\alpha_f\}+\mathbf1\{d_i=0,\ \sigma(d)<\alpha_e\}.
\]
With one uniformly chosen issue per comparison, the deterministic mean-field equations are
\[
\dot x_s=\frac1n\sum_{i=1}^n\gamma_i\left[x_{s\oplus e_i}\sum_d K_i(d)x_{s\oplus e_i\oplus d}-x_s\sum_d K_i(d)x_{s\oplus d}\right].\tag{1}
\]
This is the model's **noiseless deterministic mean-field system**, not a finite-population absorbing Markov chain. The simplex is forward invariant, and the uniform state \(u_s=Q^{-1}\) is an equilibrium.

For every nonempty \(A\subseteq\{1,\ldots,n\}\), set
\[
\chi_A(s)=(-1)^{\sum_{j\in A}s_j},\qquad M_A(x)=\sum_s\chi_A(s)x_s,
\]
and let \(E_{i,A}=\{d\in G:K_i(d)=1,\ \chi_A(d)=1\}\). The following statements hold for every choice of the above parameters, including thresholds equal to subset-sum similarity values.

**Complete tangent spectrum:** the Jacobian of (1) restricted to the \((Q-1)\)-dimensional probability-simplex tangent space has Walsh eigenvectors \(\chi_A\), each with eigenvalue
\[
\boxed{\lambda_A=-\frac4{nQ}\sum_{i\in A}\gamma_i\lvert E_{i,A}\rvert\le0.}\tag{2}
\]
Thus \(\lambda_A=0\) precisely when \(E_{i,A}=\varnothing\) for every \(i\in A\).

**Exact nonlinear conservation and local selection:** define \(\mathcal Z=\{A\ne\varnothing:\lambda_A=0\}\). Exactly the moments \(M_A\) with \(A\in\mathcal Z\) are constant along *all* trajectories. There exist neighborhoods of \(0\in\mathbb R^{|\mathcal Z|}\) and \(u\) such that the nearby equilibrium set is a real-analytic graph over the values of these conserved moments and every trajectory beginning sufficiently near \(u\) converges exponentially to its graph point. There are exactly \(|\mathcal Z|\) independent local equilibrium directions. No global convergence claim is made.

**Sharp high-similarity regime:** suppose \(\alpha_e=\alpha_f=\alpha\) and
\[
1-\min_i w_i<\alpha\le1.
\]
Then for \(A\ne\varnothing\),
\[
\boxed{\lambda_A=\begin{cases}
-\dfrac{2\gamma_i}{n}(1-2^{1-n}),&A=\{i\},\\[2mm]
-\dfrac{1-2^{2-n}}n\displaystyle\sum_{i\in A}\gamma_i,&|A|\ge2.
\end{cases}}\tag{3}
\]
When \(n\ge3\), the local exponential relaxation gap is
\[
\boxed{\kappa=\min\left\{\frac2n(1-2^{1-n})\gamma_{(1)},\ \frac1n(1-2^{2-n})(\gamma_{(1)}+\gamma_{(2)})\right\},}\tag{4}
\]
where \(\gamma_{(1)}\le\gamma_{(2)}\) are the two smallest update rates. If every rate equals \(\gamma>0\), formula (4) reduces to \(\kappa=2\gamma(1-2^{2-n})/n\), attained by every two-issue Walsh character. If \(n=2\), \(\lambda_{\{1,2\}}=0\) for **all** admissible thresholds, and \(M_{\{1,2\}}=x_{00}+x_{11}-x_{01}-x_{10}\) is exactly conserved.

## Proof

**1. Translation-covariant mean field.** An ordered focal-target pair \((s,s\oplus d)\) generates a flip \(s\to s\oplus e_i\) at mass-action rate \(\gamma_i K_i(d)x_sx_{s\oplus d}/n\). Summing all in- and out-fluxes yields (1). Every transition redistributes mass without creating negative coordinates. At uniform \(x\), the flux through each oriented hypercube edge has equal total in- and out-flow, giving stationarity.

**2. Walsh diagonalization.** Write \(k_i=\sum_dK_i(d)\) and \(\widehat K_i(A)=\sum_dK_i(d)\chi_A(d)\). For a perturbation \(y\) at \(u\), differentiation of the two quadratic flux terms gives
\[
(Jy)_s=\frac1{nQ}\sum_i\gamma_i\left[k_i(y_{s\oplus e_i}-y_s)+\sum_d K_i(d)(y_{s\oplus e_i\oplus d}-y_{s\oplus d})\right].
\]
Translations act on \(\chi_A\) as multiplication by \(\chi_A\) evaluated at the translation. The corresponding eigenvalue is
\[
\frac1{nQ}\sum_i\gamma_i(\chi_A(e_i)-1)(k_i+\widehat K_i(A)).
\]
Since \(\chi_A(e_i)-1\) equals \(-2\) for \(i\in A\) and zero otherwise, and \(k_i+\widehat K_i(A)=2|E_{i,A}|\), this is (2). The nonempty Walsh characters form an orthogonal basis of the simplex tangent space. The constant character represents the ambient total-mass direction and is not part of that tangent space. Positivity of each \(\gamma_i\) proves the precise vanishing condition.

**3. Zero modes are conserved, not merely center eigenvectors.** Multiplying the flux representation of (1) by \(\chi_A(s)\) and summing over \(s\), only flips with \(i\in A\) contribute. For a fixed displacement \(d\), the quadratic sum
\[
B_{A,d}(x)=\sum_s\chi_A(s)x_sx_{s\oplus d}
\]
satisfies \(B_{A,d}=\chi_A(d)B_{A,d}\) by the substitution \(s\mapsto s\oplus d\). Therefore \(B_{A,d}=0\) whenever \(\chi_A(d)=-1\), and
\[
\dot M_A=-\frac2n\sum_{i\in A}\gamma_i\sum_{d\in E_{i,A}}B_{A,d}(x).\tag{5}
\]
If \(\lambda_A=0\), all the index sets \(E_{i,A}\) are empty and (5) vanishes for every \(x\); hence \(M_A\) is a global first integral of the ODE. Conversely, if \(\lambda_A<0\), its derivative has nonzero linearization at \(u\), so \(M_A\) cannot be a first integral on any neighborhood of \(u\).

**4. Nearby equilibrium manifold and convergence.** Use the invertible Walsh transform to parameterize the simplex near \(u\) by its nonconstant moments. Separate coordinates \(z=(M_A)_{A\in\mathcal Z}\) and \(y=(M_A)_{A\notin\mathcal Z,A\ne\varnothing}\). Step 3 gives \(\dot z=0\) *exactly*, while \(\dot y=F(z,y)\) is a polynomial vector field whose derivative with respect to \(y\) at \((0,0)\) is diagonal with strictly negative diagonal \((\lambda_A)_{A\notin\mathcal Z}\). The analytic implicit-function theorem supplies a unique analytic solution \(y=h(z)\) of \(F(z,y)=0\) for small \(z\). For fixed sufficiently small \(z\), the Jacobian near \(h(z)\) remains uniformly Hurwitz; equivalently, a small Euclidean ball about \(h(z)\) satisfies a strictly contracting quadratic Lyapunov inequality. Hence all sufficiently near initial data converge exponentially to \(h(z)\). This proves the local classification without claiming that the whole simplex converges.

**5. High-threshold counts.** Since distinct binary strings have similarity at most \(1-\min w_i<\alpha\), every distinct target is an enemy and an identical target causes no flip. Therefore \(K_i(d)=1\) exactly when \(d_i=0\) and \(d\ne0\). For a singleton \(A=\{i\}\), \(|E_{i,A}|=2^{n-1}-1\). For \(|A|\ge2\) and \(i\in A\), parity balance among the other \(|A|-1\) selected coordinates gives \(|E_{i,A}|=2^{n-2}-1\). Substitution into (2) gives (3). For \(n\ge3\), all numbers are strictly negative, and minimizing over singleton subsets and subsets of size at least two yields (4). For equal rates, the pair mode is strictly slower than singleton modes. For \(n=2\), every possible active flip displacement has exactly one nonzero coordinate: displacement \(00\) never flips because it is identical, and displacement \(11\) never flips because it disagrees on both issues. Therefore \(E_{i,\{1,2\}}=\varnothing\) for every threshold, proving universal parity conservation.

## Verification

The standalone \(\texttt{checker.py}\) uses only Python's rational-arithmetic standard library. It independently constructs the full ordered-pair population fluxes, takes exact symmetric difference quotients (which are exact for this quadratic ODE), and verifies the Walsh eigen-equations without using a preassembled Fourier Jacobian. It also checks conserved moments on a nonuniform rational population and independently checks the closed high-threshold formulas for \(n=2,3,4,5\). Running \(\texttt{python3 checker.py}\) produced: `PASS: 453 exact rational eigenmode/parity assertions; n=2,3,4,5`.

The arbitrary-\(n\) conclusions and the local manifold theorem follow from the written symbolic proof, not from the finite tests. The inequalities used to define thresholds are literal and preserve equality boundaries.

## Relationship to prior work

Mintz, Simonson, Wodarz, Fu and Komarova (arXiv:2603.04939; first publicly posted March 5, 2026) introduce and analyze this weighted binary friend–foe model. Their main text gives the stochastic rules and mean-field equation, numerical equilibrium-symmetry classifications through five issues, and an interpretation through neutral drift and super-symmetry. The result here treats their **unchanged noiseless mean-field dynamics**, and derives an all-issue-count spectral and *nonlinear conservation* classification instead of another finite symmetry table. It does not claim the underlying model, the observation of pluralism, or the general use of Fourier characters as inventions.

Lanchier and Mercer (arXiv:2310.19073; 2023 preprint, 2024 journal publication) analyze a distinct Deffuant attraction–repulsion process on an infinite spatial lattice with continuous rather than binary-vector opinions; its main theorem on discordance does not imply (2)–(5). Conventional Fourier diagonalization of translation-invariant linear operators explains the technique, but by itself does not supply the active-even-parity rates or the identification of *every* center mode with an exact nonlinear first integral.

## Limitations

The classification is local around the interior equal-frequency state; it does not determine global attraction basins, finite-population consensus probabilities, or stochastic absorption times. It assumes shared issue weights, uniform partner selection, one-coordinate flips, strict friend/enemy threshold rules, and positive update rates, with no spontaneous opinion innovations. The high-threshold closed formulas require equal friend and enemy thresholds strictly above all nonidentity similarities. Earlier general group-equivariant kinetics could conceivably encode some special cases; an ancillary PDF supplement of the motivating preprint was not retrievable and was therefore **not** certified as non-covering. Independent scientific review has not been performed.

## References

1. B. Mintz, D. Simonson, D. Wodarz, F. Fu, and N. L. Komarova, *When minor issues matter: symmetries, pluralism, and polarization in similarity-based opinion dynamics*, arXiv:2603.04939 (first public posting 2026-03-05), https://arxiv.org/abs/2603.04939 ; HTML main text https://arxiv.org/html/2603.04939 .
2. N. Lanchier and M. Mercer, *Deffuant opinion dynamics with attraction and repulsion*, arXiv:2310.19073 (first public posting 2023-10-29), https://arxiv.org/abs/2310.19073 ; Electronic Communications in Probability 29 (2024), 45, doi:10.1214/24-ECP615.
