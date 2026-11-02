# Universal hub coupling makes SIR metapopulation thresholds independent of peripheral mobility

## Finding

Consider an SIR metapopulation in which one central location may have a higher transmission rate while all other locations share a common rate. Equal symmetric flux into the central location makes the **full reproduction number** insensitive to arbitrary nonnegative symmetric mobility among the peripheral locations. The conclusion holds for all numbers of locations and every permissible central flux, not merely for a specific star, star–cycle, or complete graph.

Fix an integer \(M\ge3\), put \(k=M-1\), and let the outward flux from every peripheral location into the center be \(p\) with \(0<p\le1/k\). The center's return flux into each peripheral location is also \(p\). All peripheral transmission rates equal \(\beta_0>0\), while the center's rate is \(\zeta\beta_0\), \(\zeta\ge1\). Recovery is \(\gamma>0\), and \(r=\beta_0/\gamma\).

Set
\[
T=(1-p)^2+kp^2+\zeta\bigl(kp^2+(1-kp)^2\bigr).
\]
Then the basic reproduction number is exactly
\[
\boxed{\mathcal R_0=\frac r2\left[T+\sqrt{T^2-4\zeta(1-Mp)^2}\right].}
\]
Every peripheral-to-peripheral mobility coefficient cancels from this expression. If \(\zeta>1\), the unique optimal central flux is \(p=1/M\), and the minimum reproduction number is \(r(k+\zeta)/M\); if \(\zeta=1\), \(\mathcal R_0=r\) for every permitted mobility.

There is also an exact complete threshold classification. For \(0<r<1\), write \(q=\zeta-1\) and \(q_c=M(1-r)/r\). When \(q>q_c\) the reproduction number always exceeds one. When \(q=q_c\), it equals one only at \(p=1/M\) and exceeds one elsewhere. When \(q<q_c\), define the positive quantity
\[
H=\frac{M(1-r)-rq}{r\bigl(M\zeta(1-r)-q\bigr)}.
\]
Then
\[
\mathcal R_0\lessgtr1\quad\Longleftrightarrow\quad(1-Mp)^2\lessgtr H,
\]
with equality on either side precisely when equality holds on the other side. In particular, \(\zeta\le1/r\) forces strict subcriticality for every \(p>0\) in the specified range. For \(r\ge1\), no such mobility is strictly subcritical.

## Assumptions and scope

The \(M\) demographic patches have equal resident populations \(N>0\). Their mobility matrix \(\Phi=(\phi_{ij})\) is real, nonnegative, symmetric and row-stochastic. Its final row and column satisfy \(\phi_{iM}=\phi_{Mi}=p\) for every \(i<M\); consequently \(\phi_{MM}=1-kp\). Self-retention is permitted, and peripheral links, including their absence, may be arbitrary as long as symmetry, nonnegativity and stochasticity hold. Since \(\Phi\) is also column-stochastic, the number present at each location is \(N\).

In the SIR-network formulation, linearization at the disease-free state gives the next-generation operator
\[
K=\frac1\gamma\Phi\,\operatorname{diag}(\beta_0,\dots,\beta_0,\zeta\beta_0)\,\Phi
 =r\Phi D\Phi,
\qquad D=\operatorname{diag}(1,\dots,1,\zeta).
\]
This is the model's standard next-generation matrix, not a claim about other movement, residence-time, unequal-population, heterogeneous-recovery or SEIR conventions. All comparisons of criticality refer to the spectral invasion threshold \(\rho(K)\), not to a global nonlinear stability assertion at equality.

## Proof

**1. Orthogonal invariant splitting.** Let \(f=k^{-1/2}(1,\ldots,1,0)^\top\) and let \(e\) be the last standard basis vector. Put \(E=\operatorname{span}\{f,e\}\) and \(F=\{x\in\mathbb R^M:x_M=0,\ \sum_{i<M}x_i=0\}\). These are orthogonal complementary invariant subspaces for both \(D\) and \(\Phi\). Indeed, every peripheral row of \(\Phi\) has peripheral row sum \(1-p\), and every peripheral-to-center entry equals \(p\). Symmetry makes the corresponding column sums equal. The restriction of \(\Phi\) to \(E\) in the ordered orthonormal basis \((f,e)\) is
\[
A=\begin{pmatrix}1-p&\sqrt{k}p\\\sqrt{k}p&1-kp\end{pmatrix},
\qquad D\vert_E=\begin{pmatrix}1&0\\0&\zeta\end{pmatrix}.
\]
On \(F\), \(D\) is the identity and \(\Phi\) restricts to a real symmetric contraction \(C\): because \(\Phi\) is symmetric and stochastic, all its eigenvalues are in \([-1,1]\). Therefore
\[
K\vert_E=rA\begin{pmatrix}1&0\\0&\zeta\end{pmatrix}A,
\qquad K\vert_F=rC^2,
\]
and every eigenvalue of \(K\vert_F\) lies in \([0,r]\).

**2. The two-dimensional block is dominant.** Let \(\mathbf1\) denote the all-ones vector. Since \(\Phi\mathbf1=\mathbf1\) and \(\mathbf1\in E\), its Rayleigh quotient for the real symmetric positive semidefinite matrix \(K\) is
\[
\frac{\mathbf1^\top K\mathbf1}{\mathbf1^\top\mathbf1}=r\frac{k+\zeta}{M}\ge r.
\]
For \(\zeta>1\) the inequality is strict, so the largest eigenvalue of \(K\) belongs to \(E\), not \(F\). For \(\zeta=1\), \(K=r\Phi^2\) has maximum eigenvalue exactly \(r\), because \(\Phi\mathbf1=\mathbf1\). Thus no peripheral eigenmode can alter the dominant eigenvalue.

**3. Closed formula.** The trace and determinant of \(A\,\operatorname{diag}(1,\zeta)\,A\) are respectively
\[
T=(1-p)^2+kp^2+\zeta\bigl(kp^2+(1-kp)^2\bigr),\qquad
\zeta(\det A)^2=\zeta(1-Mp)^2.
\]
The larger root of its quadratic characteristic polynomial is the displayed formula. This establishes both the all-size result and its independence from every coefficient of \(C\).

**4. Exact minimum.** Introduce the orthonormal eigenbasis of \(A\) consisting of the normalized all-ones vector and its orthogonal complement within \(E\). Their eigenvalues are \(1\) and \(d=1-Mp\). Writing \(q=\zeta-1\), the resulting two-dimensional matrix is, up to a harmless sign change in its second coordinate,
\[
\frac1rK\vert_E=
\begin{pmatrix}1&0\\0&d^2\end{pmatrix}
+\frac qM\begin{pmatrix}1\\\sqrt{k}d\end{pmatrix}
\begin{pmatrix}1&\sqrt{k}d\end{pmatrix}.
\]
Its top eigenvalue is at least \(1+q/M\), with equality at \(d=0\). If \(q>0\) and \(d\ne0\), the nonzero off-diagonal entry precludes equality in the Rayleigh estimate for the first basis vector. Thus the minimum is unique at \(p=1/M\) when \(\zeta>1\); at \(q=0\) the unit eigenvalue is present for every \(p\).

**5. All strict and equality boundaries.** First let \(0<r<1\). Because \(\lvert d\rvert<1\) for \(M\ge3\) and \(0<p\le1/k\), the matrix \(I-r\operatorname{diag}(1,d^2)\) is positive definite. A rank-one Schur complement (or matrix determinant lemma with positivity of the background) shows that its rank-one downdate remains positive definite exactly when
\[
\frac{rq}{M}\left(\frac1{1-r}+\frac{kd^2}{1-rd^2}\right)<1.
\]
This condition is equivalent to \(\lambda_{\max}(K\vert_E)<1\). Since every peripheral eigenvalue is at most \(r<1\), it is also equivalent to \(\mathcal R_0<1\). At \(d=0\), the inequality becomes \(q<q_c=M(1-r)/r\). If \(q>q_c\), it fails everywhere; if \(q=q_c\), it is an equality only at \(d=0\). For \(q<q_c\), elementary rearrangement gives
\[
d^2<\frac{M(1-r)-rq}{r\bigl(M\zeta(1-r)-q\bigr)}=H.
\]
The denominator is positive on this range: setting \(t=1/r>1\) gives
\[
M\zeta(t-1)-q=[M(t-1)-q]+Mq(t-1)>0.
\]
(For \(q=0\) the expression remains positive.) The rank-one update criterion has the same weak/equality/strict comparisons with one because the leading eigenvalue is continuous and monotone in \(d^2\). If \(\zeta\le1/r\), then \(q\le(1-r)/r\); the preceding inequality holds strictly for every permissible \(d^2<1\), since its left side is strictly smaller than its value at \(d^2=1\), which is \(rq\le1-r\). Finally, when \(r\ge1\), the all-ones Rayleigh bound gives \(\mathcal R_0\ge r\ge1\). This covers every parameter boundary.

## Verification

The complete proof uses the block decomposition and rank-one positive-definiteness test, not finite experiments. The accompanying `verify.py` reproduces three independent diagnostics: (i) \(575\) random real-symmetric flux matrices with inhomogeneous peripheral entries and direct numerical eigensolvers; (ii) \(42\) exact-rational characteristic-polynomial factorization checks and \(9\) exact critical boundary checks; and (iii) \(1863\) additional spectral classifications. It also checks three different peripheral mixing patterns sharing the exact algebraic reproduction number \((53+\sqrt{2377})/120\) at \(M=5\), \(p=1/6\), \(r=3/5\), \(\zeta=3\). Run with `python3 verify.py` with NumPy and SymPy installed.

## Relationship to prior work

Das and Stolerman, *Epidemic thresholds and disease dynamics in metapopulations: the role of network geometry and human mobility* (arXiv:2308.01998v1, first made public August 3, 2023; journal DOI 10.1137/23M1579522), derive threshold formulas for star, complete and selected composite graphs, and state four equal-hub-flux extensions as conjectures in their preprint. The present statement covers all of them, including arbitrarily weighted symmetric peripheral networks, by a single invariant two-dimensional block. It further provides the exact reproduction number and the complete criticality classification, including equality.

The earlier Stolerman–Coombs–Boatto SIR-network result (DOI 10.1137/140996148) treats a fully connected exchange pattern. It does not directly state invariance under arbitrary weighted peripheral mobility. A literature comparison found no full-text theorem implying this general invariant-block conclusion; equivalence under another terminology is a residual priority risk. Differences in non-leading spectral modes, spatial infection trajectories and transient peaks are not claimed to disappear.

## Limitations

The equality of residence populations, symmetry and stochasticity of the mobility matrix, identical peripheral infection rates, common recovery rate, and uniform center-periphery coupling are indispensable hypotheses of this theorem; unequal peripheral transmission rates or asymmetric residence fluxes generally break the invariant splitting. The theorem is about \(\rho(K)\) and associated linear invasion thresholds, not about nonlinear final epidemic sizes, stochastic outbreak probabilities, trajectory synchrony, or critical nonlinear asymptotic stability. The original source's threshold terminology and strict inequalities are retained; at \(\mathcal R_0=1\) only criticality of the next-generation operator is asserted. No independent validation has been conducted.

## References

1. H. K. Das and L. M. Stolerman, *Epidemic thresholds and disease dynamics in metapopulations: the role of network geometry and human mobility*, arXiv:2308.01998v1 (2023), https://arxiv.org/abs/2308.01998 ; peer-reviewed version *Epidemic Thresholds and Disease Dynamics in Metapopulations: The Role of Network Structure and Human Mobility*, SIAM Journal on Applied Dynamical Systems (2024), https://doi.org/10.1137/23M1579522.
2. L. M. Stolerman, D. Coombs and S. Boatto, *SIR-Network Model and Its Application to Dengue Fever*, SIAM Journal on Applied Mathematics (2015), https://doi.org/10.1137/140996148.
