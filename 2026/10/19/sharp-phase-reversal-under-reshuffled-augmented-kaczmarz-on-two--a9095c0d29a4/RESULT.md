# Sharp phase reversal under reshuffled augmented Kaczmarz on two inconsistent rows

## Finding

**Theorem (phase-resolved stationary risk and exact crossover).** Let \(b_1\neq b_2\) be real observations of the same unknown scalar, with two inconsistent unit-row equations \(x=b_i\). Write \(\bar b=(b_1+b_2)/2\) for the least-squares minimizer and \(\sigma^2=(b_1-b_2)^2/4>0\). Run the augmented Kaczmarz least-squares update of Morshed [1] at a *constant* penalty \(\rho>0\), with an arbitrary finite deterministic initial pair \((x_0,z_0)\). Put \(p=\rho/(1+\rho)\in(0,1)\).

For with-replacement independent uniform row choices, the limiting expected squared primal error is
\[
V_{\mathrm{iid}}=\sigma^2\frac{2-p}{4-3p}.
\]
Under **fresh independent uniform permutations of the two rows in every two-update epoch**, let \(V_0\) and \(V_1\) denote the limits of \(\mathbb E(x_{2k}-\bar b)^2\) and \(\mathbb E(x_{2k+1}-\bar b)^2\), respectively. Then
\[
\begin{aligned}
V_0&=\sigma^2\frac{p(8-28p+32p^2-11p^3)}{H(p)},\\
V_1&=\sigma^2\frac{p(8-12p+4p^2+p^3)}{H(p)},\\
H(p)&=(2-p)(4-3p)(5p^2-8p+4)>0.
\end{aligned}
\]
The phase-specific comparison is **sharp**:
\[
V_0<V_{\mathrm{iid}}\quad\text{for every }0<p<1,
\]
while
\[
\begin{cases}
V_1<V_{\mathrm{iid}},&0<p<3-\sqrt5,\\
V_1=V_{\mathrm{iid}},&p=3-\sqrt5,\\
V_1>V_{\mathrm{iid}},&3-\sqrt5<p<1.
\end{cases}
\]
At small penalty, \(V_0\sim V_1\sim\sigma^2p/4\), whereas \(V_{\mathrm{iid}}\to\sigma^2/2\). Thus random reshuffling improves the limiting risk at each **epoch boundary**, but can strictly worsen the limiting risk at each **intermediate step**; a global iteration-by-iteration variance ordering is false even for two identical system rows.

## Assumptions and scope

The data are exactly two, real, distinct scalar right-hand sides, and both rows of the linear system are equal to one. Row probabilities are \(1/2\) under sampling with replacement. Random reshuffling uses one of the permutations \((1,2)\) and \((2,1)\), each with probability \(1/2\), independently between epochs. There is no measurement noise beyond this data inconsistency and no external randomness in initialization. Fixed \(\rho>0\) is a constant-penalty specialization of the augmented update in [1], not the paper's optional increasing-penalty variant. All error limits are expectations over the row-selection process. They are not almost-sure comparison statements.

## Proof

Write \(y_k=x_k-\bar b\), \(\xi_i=b_i-\bar b\), \(q=1-p\). Equation (18) and Algorithm 2 of [1] yield, for unit rows and constant penalty,
\[
z_{k+1}=p(y_k-\xi_{i_k})+qz_k,\qquad y_{k+1}=y_k-z_{k+1}.
\]
Therefore with \(w_k=(y_k,z_k)^{\mathsf T}\),
\[
w_{k+1}=Mw_k+C\xi_{i_k},\qquad
M=\begin{pmatrix}q&-q\\p&q\end{pmatrix},\qquad
C=\begin{pmatrix}p\\-p\end{pmatrix}.
\]
The eigenvalues of \(M\) are \(q\pm i\sqrt{pq}\), each of modulus \(\sqrt q<1\). Thus initial-condition contributions decay and all subsequent second-moment limits exist. In the with-replacement experiment the input has zero mean, variance \(\sigma^2\), and is independent at each time. Direct substitution into \(S=MSM^{\mathsf T}+\sigma^2CC^{\mathsf T}\) gives the positive-definite solution
\[
S_{\mathrm{iid}}=\frac{\sigma^2}{4-3p}
\begin{pmatrix}2-p&-p\\-p&2p\end{pmatrix},
\]
whose upper-left entry is \(V_{\mathrm{iid}}\).

For reshuffling, in epoch \(k\), the two noise inputs are \((\xi_{i_{2k}},\xi_{i_{2k+1}})=(s_k,-s_k)\) where independent signs \(s_k\) each have mean zero and variance \(\sigma^2\). Hence
\[
w_{2k+2}=M^2w_{2k}+D s_k,\qquad
D=(M-I)C=\begin{pmatrix}p(1-2p)\\2p^2\end{pmatrix}.
\]
The epoch-boundary covariance \(S_0\) uniquely solves
\[
S_0=M^2S_0(M^2)^{\mathsf T}+\sigma^2DD^{\mathsf T}.
\]
Solving its three symmetric scalar equations yields
\[
S_0=\frac{\sigma^2}{H(p)}
\begin{pmatrix}
p(8-28p+32p^2-11p^3)&-2p^2(2p-1)(2-p)\\
-2p^2(2p-1)(2-p)&4p^2(p^2-2p+2)
\end{pmatrix}.
\]
At the intermediate phase,
\[
S_1=MS_0M^{\mathsf T}+\sigma^2CC^{\mathsf T},
\]
whose upper-left entry is exactly \(V_1\). Let \(H(p)>0\) be the denominator above. Elementary subtraction and factorization give
\[
\begin{aligned}
V_{\mathrm{iid}}-V_0
 &=\sigma^2\frac{4(1-p)(1-(1-p)^2+4(1-p)^3)}{H(p)},\\
V_{\mathrm{iid}}-V_1
 &=\sigma^2\frac{4(1-p)^2(p^2-6p+4)}{H(p)}.
\end{aligned}
\]
The first difference is strictly positive because \((1-p)^2<1\). The second has exactly one root inside \((0,1)\), namely \(3-\sqrt5\), and changes from positive to negative there. Taking \(p\downarrow0\) in the explicit expressions proves the small-penalty limits. This completes the proof.

## Verification

Run `python verify.py` with Python 3 and SymPy. The verifier derives both Lyapunov covariance matrices from the update equations, checks each rational expression exactly, checks the factorized difference formulas, and tests their signs at rational sample penalties. It does not substitute finite testing for the all-parameter proof. A reconstruction from the original source equations, independent of any simulation, is given in this document.

## Relationship to prior work

Morshed [1], public on 2022-05-17, gives the penalty and augmented Kaczmarz recurrences and studies convergence for consistent systems. Our setting is deliberately inconsistent with a fixed penalty and with-versus-without-replacement random row selection; neither the two-phase covariance nor its crossover appears in the inspected original algorithm and convergence discussion.

Domingo-Enrich [2], public on 2022-06-01, analyzes stationary variance for stochastic gradient methods **including heavy-ball momentum** under random reshuffling, using a *random initial epoch phase* to turn cyclostationary forcing into a stationary process. Section 5, especially equations (26)--(29), computes **time/phase-averaged** stationary variance from a spectral density. This is important prior coverage of the general variance mechanism; the present two-phase inequality and exact reversal threshold are different because a phase average does not determine the two phase-specific variances or their individual orderings. The random reshuffling phase information is essential here.

Mohammadi, Razaviyayn and Jovanović [3], public on 2022-09-24, analyze noise amplification of heavy-ball dynamics with white forcing. Their linear stochastic framework is strong prior coverage of the with-replacement variance component, not of the phase-dependent two-row without-replacement effect.

## Limitations

The result is exact only for two conflicting observations on identical unit rows, in exact arithmetic and at a fixed penalty. The algorithm is run beyond the consistent-system assumptions of [1]; no extension of those convergence theorems is claimed. Exact stationary second moments do not imply sample-path ordering or any expected-error ordering at finite iteration counts. The comparison uses a common hyperparameter \(p\) and the same two observations for both sampling schemes. The broad spectral framework of [2] remains the most substantial priority risk for alternative equivalent representations of these phase-specific conclusions, and independent literature assessment is still needed.

## References

[1] M. S. Morshed, *Penalty & Augmented Kaczmarz Methods For Linear Systems & Linear Feasibility Problems*, arXiv:2205.08085, first public 2022-05-17, https://arxiv.org/abs/2205.08085.

[2] C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632v1, 2022-06-01, https://arxiv.org/html/2206.00632v1.

[3] B. Mohammadi, M. Razaviyayn, M. R. Jovanović, *Tradeoffs between convergence rate and noise amplification for momentum-based accelerated optimization algorithms*, arXiv:2209.11920, first public 2022-09-24, https://arxiv.org/abs/2209.11920.
