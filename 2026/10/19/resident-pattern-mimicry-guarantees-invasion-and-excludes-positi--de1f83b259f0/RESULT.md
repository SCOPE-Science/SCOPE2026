# Resident-pattern mimicry guarantees invasion and excludes positive coexistence in two patches

## Finding

**Theorem (two-patch resident-profile mimicry).** For strictly positive \(P_1,P_2,d,e,m_1,m_2\), let \(Q=(Q_1,Q_2)\) be the unique strictly positive stationary population for
\[
\dot z_i=d\left(\frac{z_j}{P_j}-\frac{z_i}{P_i}\right)+z_i(m_i-z_i),\qquad\{i,j\}=\{1,2\}.
\]
Suppose \(Q_1/P_1\ne Q_2/P_2\). Consider two species with identical local growth and competition but distinct movement targets:
\[
\begin{aligned}
\dot u_i&=d\left(\frac{u_j}{P_j}-\frac{u_i}{P_i}\right)+u_i(m_i-u_i-v_i),\\
\dot v_i&=e\left(\frac{v_j}{Q_j}-\frac{v_i}{Q_i}\right)+v_i(m_i-u_i-v_i),\qquad\{i,j\}=\{1,2\}.
\end{aligned}
\]
Then, simultaneously for **every** \(e>0\):

1. At the resident-only state \((Q,0)\), the rare invader has exactly one positive real growth eigenvalue, so \((Q,0)\) is linearly unstable.
2. The invader-only scalar system has a unique positive stationary profile \(V\). The state \((0,V)\) is locally exponentially asymptotically stable against both resident and invader perturbations.
3. There exists **no equilibrium with both species positive in both patches**. Irreducibility implies that a nonnegative equilibrium with both species present is automatically strictly positive in every patch, so there is no equilibrium supporting both species.

The theorem asserts a local invasion/exclusion classification and absence of coexistence equilibria. It does **not** assert global attraction to \((0,V)\) from every positive initial state.

## Assumptions and scope

All six listed parameters are strictly positive; \(i\in\{1,2\}\), \(j=3-i\), and population coordinates are nonnegative. Movement is a conservative two-patch flux with a target weight: \(d(z_j/P_j-z_i/P_i)\) for the resident, \(e(z_j/Q_j-z_i/Q_i)\) for the invader. The actual vector \(Q\), not merely a proportional profile, is used as the invader target (rescaling the target can be absorbed into \(e\)). Local carrying-resource terms are identical for both species in each patch. The nonbalance condition excludes the case where the resident already follows its own movement target and implies that \(P\) and \(Q\) are linearly independent.

The model is a finite-patch analogue of directed diffusion and stationary-profile imitation; it is not asserted to be a spatial discretization preserving every PDE property.

## Proof

**Scalar existence, uniqueness, and stability.** For any fixed strictly positive target \(R=(R_1,R_2)\), dispersal coefficient \(\eta>0\), and positive local growth rates \(m_i\), consider the cooperative two-patch logistic equation
\[
\dot z_i=\eta(z_j/R_j-z_i/R_i)+z_i(m_i-z_i).
\]
The positive vectors \(\epsilon R\) and \(MR\) are strict sub- and supersolutions for sufficiently small \(\epsilon>0\) and large \(M\); monotone trajectories between them yield a positive stationary vector \(Z\). Uniqueness follows from scaling: if \(Z,W\) are different positive equilibria and \(c=\max_i Z_i/W_i>1\), at a maximizing index the conservative migration part of \(Z\) is at most \(c\) times that of \(W\), whereas \(Z_i(m_i-Z_i)<cW_i(m_i-W_i)\), an impossibility. By symmetry every two equilibria coincide. The Jacobian \(J\) at \(Z\) is irreducible Metzler and satisfies \(JZ=(-Z_1^2,-Z_2^2)<0\); its spectral bound is negative. This proves the scalar stability required at both boundary states.

**The resident is invadable for every invader movement intensity.** Put
\[
a=d\left(\frac{Q_1}{P_1}-\frac{Q_2}{P_2}\right)\ne0.
\]
The resident stationary equations imply
\[
m_1-Q_1=\frac{a}{Q_1},\qquad m_2-Q_2=-\frac{a}{Q_2}.
\]
The invader's transverse Jacobian at \((Q,0)\) therefore equals
\[
L_v=\begin{pmatrix}(a-e)/Q_1&e/Q_2\\e/Q_1&(-a-e)/Q_2\end{pmatrix},\qquad
\det L_v=-\frac{a^2}{Q_1Q_2}<0.
\]
It has one strictly positive and one strictly negative real eigenvalue independent of the size of \(e>0\). The resident's tangential logistic Jacobian is Hurwitz by the scalar argument. Thus the boundary state is unstable and invasion is possible from sufficiently small invader populations.

**The invader-only state resists resident invasion.** The same scalar argument yields a unique positive invader-only equilibrium \(V\). Relabel patches if necessary so that \(a>0\), and write \(V_i=Q_it_i\), \(D=t_1-t_2\). The stationarity equations are
\[
\begin{aligned}
e(t_2-t_1)+Q_1t_1\bigl(m_1-Q_1t_1\bigr)&=0,\\
e(t_1-t_2)+Q_2t_2\bigl(m_2-Q_2t_2\bigr)&=0.
\end{aligned}
\]
If \(t_1\le t_2\), the first equation forces \(t_1\ge m_1/Q_1>1\), while the second forces \(t_2\le m_2/Q_2<1\), a contradiction. Hence \(D>0\). Subtraction of the corresponding expressions for \(eD\) gives
\[
aD=Q_1^2t_1(t_1-1)+Q_2^2t_2(t_2-1).
\]
If \(t_1\le1\), then \(0<t_2<t_1\le1\), making its right side negative and its left positive. Therefore \(t_1>1\).

Set \(\delta_i=m_i-Q_it_i\). From invader stationarity,
\[
\delta_1=\frac{eD}{Q_1t_1}>0,\qquad\delta_2=-\frac{eD}{Q_2t_2}<0.
\]
The resident's transverse Jacobian at \((0,V)\) is
\[
L_u=\begin{pmatrix}\delta_1-d/P_1&d/P_2\\d/P_1&\delta_2-d/P_2\end{pmatrix}.
\]
Direct determinant algebra and the first invader stationarity equation give
\[
\begin{aligned}
\det L_u
&=\frac{eD}{Q_1Q_2t_1t_2}\left[d\left(\frac{Q_1t_1}{P_1}-\frac{Q_2t_2}{P_2}\right)-eD\right]\\
&=\frac{eD}{Q_1Q_2t_1t_2}\left[Q_1^2t_1(t_1-1)+\frac{dQ_2}{P_2}D\right]>0.
\end{aligned}
\]
Because its lower-right diagonal entry \(\delta_2-d/P_2\) is negative, the positive determinant and positive off-diagonal entries force its upper-left diagonal entry also to be negative. Therefore \(\operatorname{tr} L_u<0\), and both resident transverse eigenvalues have negative real parts. The scalar invader block is Hurwitz, completing local exponential stability of \((0,V)\).

**No positive coexistence stationary state.** Suppose both vectors \(u,v\) were strictly positive at equilibrium, and let \(g_i=m_i-u_i-v_i\). Summing each species' two equilibrium equations cancels its conservative migration terms:
\[
u_1g_1+u_2g_2=0,\qquad v_1g_1+v_2g_2=0.
\]
If \(g\ne0\), both positive two-vectors orthogonal to \(g\) must be proportional, so \(u=\theta(u+v)\) and \(v=(1-\theta)(u+v)\) for a constant \(0<\theta<1\). Writing \(T=u+v\), the resident equation divided by \(\theta\) gives the resident-only scalar stationary equation for \(T\), hence \(T=Q\). The invader equation divided by \(1-\theta\) then has zero dispersal because the target is \(Q\), forcing \(g=0\), a contradiction. If instead \(g=0\), each dispersal flux must separately vanish, so \(u=\alpha P\), \(v=\beta Q\) for \(\alpha,\beta>0\), and \(m=\alpha P+\beta Q\). But by the resident stationary identities,
\[
\alpha=\frac{\det(m,Q)}{\det(P,Q)}
=-\frac{d}{P_1P_2}\left(\frac{Q_2}{Q_1}+\frac{Q_1}{Q_2}\right)<0,
\]
which is impossible. A nonnegative steady state with one species nontrivial in only one patch is also impossible because positive cross-patch movement immediately generates that species in its other patch. Thus no coexistence equilibrium exists.

**Exact rational witness.** Choose
\[
P=(1,1),\quad d=\frac14,\quad m=\left(\frac{17}{8},\frac34\right),\quad Q=(2,1),\quad e=\frac{15}{26}.
\]
The resident equilibrium is indeed \(Q\), the invader-only equilibrium is \(V=(27/13,45/52)\), and
\[
L_v=\begin{pmatrix}-17/104&15/26\\15/52&-43/52\end{pmatrix},\quad\det L_v=-\frac1{32},
\]
\[
L_u=\begin{pmatrix}-21/104&1/4\\1/4&-19/52\end{pmatrix},\quad\det L_u=\frac{61}{5408}>0,\quad\operatorname{tr}L_u=-\frac{59}{104}<0.
\]
The explicit certificate is checked using rational arithmetic in `verify.py`.

## Verification

Run `python3 verify.py` using the Python standard library. It checks the exact witness's resident and invader stationarity, the exact two transverse matrices, determinant and trace identities, local sign classification, and the zero-source-drift identity. The general theorem is certified by the displayed inequalities, not by finite enumeration. A separate parameter sampling diagnostic is intentionally excluded because it cannot prove the universal quantified statements.

## Relationship to prior work

Braverman and Lawson [1] formulate mimicking the resident stationary profile for directed diffusion. Their Theorem 3.4 proves invader success under an additional strictly favorable resource condition; Section 5 poses identical-resource invasion and exclusion as an open question and explicitly invites discrete analogues. The present two-patch theorem treats identical resources and every positive invader movement rate, proving local invadability, local attractiveness of the invader boundary state, and absence of coexistence equilibria; it does **not** resolve their infinite-dimensional PDE conjecture or prove global exclusion.

Lou's two-patch ideal-free-distribution survey [2, Theorem 2.3] already describes a complete phase diagram for two-patch competition with locally normalized growth \(1-(u_i+v_i)/K_i\). That is closely related but is not the stated patch-heterogeneous intrinsic-rate system \(m_i-u_i-v_i\); its theorem is not claimed anew. Chen, Shi, Shuai and Wu [3] prove global dynamics for a patch Lotka–Volterra model with a **common dispersal matrix** for both species; here the movement matrices differ in their target profiles. When the local intrinsic rates are equal, an important special case overlaps classical ideal-free two-patch competition results; the new statement extends over arbitrary unequal patch rates under the distinct resident and mimic target kernels. We do not claim novelty for generic two-patch competition principles, ideal-free evolutionary stability, or invasion eigenvalue methods. Qi–Su–Wang (2024) and Chen–Liu–Wu (2022) concern related river-patch competition models, but their complete theorems were not accessible; equivalence remains a literature risk.

## Limitations

The proof is restricted to two patches, shared local crowding coefficients and equal local resource terms for the two species. The target \(Q\) is exactly the resident-only stationary profile. Extending the claim to three or more patches, unequal competition or growth rates, nonlinear migration, or the motivating PDE requires new arguments. The theorem proves equilibrium exclusion and local stability, **not** global convergence, uniform persistence, stochastic invasion success, or empirical ecological outcomes. Its originality relative to less-indexed early two-patch strategy literature and two plausibly related river-patch papers requires independent examination.

## References

[1] E. Braverman and J. Lawson, *Trimming to Coexistence: How Dispersal Strategies Should Be Accounted for in Resource Management*, arXiv:2512.10898v1 (first public 2025-12-11), Sections 3.3, 5 and proof of Theorem 3.4. https://arxiv.org/pdf/2512.10898v1

[2] Y. Lou, *Ideal Free Distribution in Two Patches*, Journal of Nonlinear Modeling and Analysis (2019), especially Section 2, Theorems 2.1–2.3. https://epe.lac-bac.gc.ca/100/201/300/jrn_nonlinear_modeling_analysis/2019/v01n02.pdf

[3] S. Chen, J. Shi, Z. Shuai and Y. Wu, *Global dynamics of a Lotka–Volterra competition patch model*, Nonlinearity 35 (2022), 817–842, model (1.3) and assumptions (A1)–(A3). https://jxshix.people.wm.edu/shi/2022-Chen-Shi-Shuai-Wu-NON.pdf

[4] Y. Qi, L. Su and M. Wang, *Population dynamics of two competing species in an advective heterogeneous two-patch environment*, DCDS-B 29 (2024), 2549–2581. https://doi.org/10.3934/dcdsb.2023192 (abstract inspected; full text not obtained).

[5] S. Chen, J. Liu and Y. Wu, *Invasion analysis of a two-species Lotka–Volterra competition model in an advective patchy environment*, Studies in Applied Mathematics 149 (2022), 762–797. https://doi.org/10.1111/sapm.12520 (abstract inspected; full text not obtained).
