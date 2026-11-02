# Sharp cut and circulation projection constants of rectangular rook graphs

## Finding

For integers \(m,n\ge 2\), let \(G_{m,n}=K_m\square K_n\), the Cartesian product of two unweighted complete graphs. Give its real oriented edge space \(E=\mathbb R^{E(G_{m,n})}\) the coordinate \(\ell_1\) norm. Put \(C=\operatorname{im}D^{\mathsf T}\) (the cut space) and \(Z=\ker D\) (the circulation space), where \(D\) is any signed vertex-edge incidence matrix. Write \(\lambda(C)\) and \(\lambda(Z)\) for the infima of operator norms over all linear projections from \(E\) onto those respective fixed subspaces.

Define
\[
A=(m-1)(n+2),\quad B=(n-1)(m+2),\quad S=A+B=2mn+m+n-4.
\]
Then both infima are attained, and their exact values are
\[
\boxed{\lambda(C)=\frac{2(m^2+mn-3m+n^2-3n+3)}{m(m-1)+n(n-1)}}
\]
and
\[
\boxed{\lambda(Z)=5-\frac{2(m+n+2)}{mn}-\frac{2AB}{mnS}.}
\]
The unique \(S_m\times S_n\)-equivariant minimizing cut projection is parametrized by
\[
\theta_C=\frac{m^2-2m+n}{m(m-1)+n(n-1)},
\]
and the unique equivariant minimizing circulation projection by
\[
s_Z=\frac{(m-1)(n+2)}{2mn+m+n-4}.
\]
The Euclidean orthogonal projection onto \(C\) has minimum \(\ell_1\) norm **if and only if** \(m=n\). The orthogonal projection onto \(Z\) has minimum norm **if and only if** either \(m=n\), or \((m,n)=(2,4)\) or \((4,2)\). In particular, when \(m\ne n\), **no** pair of complementary projections onto \(C\) and \(Z\) can attain both separate minima. This does not assert uniqueness among nonsymmetric minimizers.

For example, on \(K_2\square K_3\) the constants are exactly \(\lambda(C)=7/4\) and \(\lambda(Z)=64/39\), whereas for \(K_q\square K_q\), they reduce to \(3(q-1)/q\) and \(4-5/q-2/q^2\).

## Assumptions and scope

All spaces, operators and coefficients are real; all graph edges have unit weight; all norms are coordinate \(\ell_1\) operator norms. Orient every edge arbitrarily once and use the corresponding signed action of automorphisms on edge coordinates. There are two edge families: \(h\)-edges changing the first coordinate and \(v\)-edges changing the second. The formulas hold for all integers \(m,n\ge2\), including the four-cycle \((m,n)=(2,2)\). No weighted or higher-dimensional product theorem is asserted.

Let \(D_h,D_v\) be the incidence restrictions and \(G_h=D_h^{\mathsf T}\), \(G_v=D_v^{\mathsf T}\) their gradients. On \(\mathbb R^m\otimes\mathbb R^n\), let \(P_m=I_m-J_m/m\), \(P_n=I_n-J_n/n\) and
\[
\Pi_{10}=P_m\otimes J_n/n,\quad
\Pi_{01}=J_m/m\otimes P_n,\quad
\Pi_{11}=P_m\otimes P_n.
\]
For a flow \(u=(u_h,u_v)\), write \(d_h=D_hu_h\) and \(d_v=D_vu_v\). We have
\[
D_hG_h=mP_m\otimes I_n,\qquad D_vG_v=nI_m\otimes P_n.
\]
The component \(d_h\) lies in \(\operatorname{ran}(\Pi_{10}+\Pi_{11})\); \(d_v\) lies in \(\operatorname{ran}(\Pi_{01}+\Pi_{11})\).

## Proof

**1. Every invariant projection belongs to an explicit one-parameter family.** A permutation of the vertices of \(K_r\) acts by signed permutations on its oriented edge space. Every equivariant map from this edge space to \(\mathbb R^r\) is a scalar multiple of incidence: fixing an unordered edge and then exchanging its endpoints forces the image of its oriented basis vector to be proportional to the difference of the two endpoint indicators. Also, every permutation-equivariant endomorphism of \(\mathbb R^r\) is a linear combination of \(I_r\) and \(J_r\). Consequently, any \(S_m\times S_n\)-equivariant linear map from the edge space of \(G_{m,n}\) to the mean-zero vertex space has four scalar coefficients: one on each of \(\Pi_{10}d_h\), \(\Pi_{01}d_v\), \(\Pi_{11}d_h\), \(\Pi_{11}d_v\). If its gradient is a projection onto \(C\), the requirement that it act identically on every gradient imposes three independent constraints, leaving exactly the family \(P_\theta\):
\[
P_\theta u=(G_h f_\theta,G_v f_\theta),\qquad
f_\theta=\frac{\Pi_{10}d_h}{m}+\frac{\Pi_{01}d_v}{n}
 +\frac{\theta\Pi_{11}d_h}{m}+\frac{(1-\theta)\Pi_{11}d_v}{n}.
\]
These are indeed projections onto \(C\), for every real \(\theta\).

For a projection \(Q\) onto \(Z\), the complement \(R=I-Q\) annihilates \(Z\) and hence factors through the total divergence \(d_h+d_v\). Since \(D:E\to\mathbf 1^\perp\) is surjective, invariant such \(R\) correspond to invariant right inverses of \(D\). The same equivariant-map argument and three constraints give exactly \(Q_s=I-R_s\), where
\[
R_su=\left(G_h\left[\frac{\Pi_{10}d_h}{m}+\frac{s\Pi_{11}(d_h+d_v)}m\right],
 G_v\left[\frac{\Pi_{01}d_v}{n}+\frac{(1-s)\Pi_{11}(d_h+d_v)}n\right]\right).
\]
Directly \(DR_su=d_h+d_v\), \(R_s\) is the identity on its range, and \(Q_s\) is a projection onto \(Z\). For an arbitrary projection onto either fixed subspace, averaging its conjugates over \(S_m\times S_n\) preserves the projection property (identity on the target and image in that target) and does not increase its norm. Thus global minimization reduces to these one-parameter families. This statement remains valid when \(m=n\); possible coordinate interchange merely adds symmetry.

**2. Exact cut-projection minimum.** Fix a unit \(h\)-edge from first coordinate \(a\) to \(b\), at second coordinate \(c\), and let \(v=\mathbf 1_b-\mathbf 1_a\). Its \(P_\theta\) potential is \(v\otimes w\) with
\[
w_c=\frac{1+(n-1)\theta}{mn},\qquad
w_j=\frac{1-\theta}{mn}\quad(j\ne c).
\]
Using \(\|G_{K_m}v\|_1=2(m-1)\), the sum of absolute coordinates in its projected edge column is
\[
H_P(\theta)=\frac{2(m-1)}{mn}\bigl(|1+(n-1)\theta|+(n-1)|1-\theta|\bigr)+\frac{2(n-1)}m|\theta|.
\]
A symmetric calculation for a unit \(v\)-edge gives
\[
V_P(\theta)=\frac{2(n-1)}{mn}\bigl(|1+(m-1)(1-\theta)|+(m-1)|\theta|\bigr)
+\frac{2(m-1)}n|1-\theta|.
\]
For \(0\le\theta\le1\), these are the affine functions
\[
h_P(\theta)=\frac{2(m-1)}m+\frac{2(n-1)}m\theta,
\qquad v_P(\theta)=\frac{2(n-1)}n+\frac{2(m-1)}n(1-\theta).
\]
For every real \(\theta\), the triangle inequality in the displayed absolute-value formulas gives \(H_P\ge h_P\) and \(V_P\ge v_P\). The first affine function increases strictly and the second decreases strictly. Their unique intersection lies in \((0,1)\) and equals \(\theta_C\) above. Since \(\|P_\theta\|_{1\to1}=\max(H_P,V_P)\), the intersection attains the global minimum and gives the formula for \(\lambda(C)\).

**3. Exact circulation-projection minimum.** For the same unit \(h\)-edge, set \(w_c=[1+(n-1)s]/(mn)\) and \(w_j=(1-s)/(mn)\) otherwise. The \(h\)-edge part of \(R_s\) is the first-coordinate gradient of \(v\otimes w\); its \(v\)-edge part is \((1-s)/n\) times the second-coordinate gradient of \(v\otimes(\mathbf 1_c-\mathbf 1/n)\). Therefore the \(Q_s=I-R_s\) column has norm
\[
H_Q(s)=|1-2w_c|+2(m-2)|w_c|+2(m-1)(n-1)|w_j|+\frac{2(n-1)}n|1-s|.
\]
For \(0\le s\le1\), \(0\le 2w_c\le1\), so this simplifies to
\[
h_Q(s)=5-\frac{2(m+n+2)}{mn}-\frac{2(n-1)(m+2)}{mn}s.
\]
Interchanging the two coordinates replaces \((m,n,s)\) by \((n,m,1-s)\), giving the other edge-column norm
\[
v_Q(s)=5-\frac{2(m+n+2)}{mn}-\frac{2(m-1)(n+2)}{mn}(1-s)
\]
on the same interval. For arbitrary real \(s\), the columnwise absolute-value expressions dominate these affine continuations; hence their maximum is a global lower bound. Since \(h_Q\) decreases strictly and \(v_Q\) increases strictly, their unique intersection \(s_Z=A/S\in(0,1)\) is the global minimizer. Substitution gives the exact formula for \(\lambda(Z)\).

**4. Orthogonal optimality and incompatibility.** The orthogonal projector onto \(C\) corresponds to \(\theta_0=m/(m+n)\); its complement onto \(Z\) corresponds to \(s_0=m/(m+n)\). Direct subtraction yields
\[
\theta_C-\theta_0=
\frac{(m-n)(mn-m-n)}{(m+n)[m(m-1)+n(n-1)]},
\]
\[
s_Z-s_0=-\frac{(m-n)(mn-m-n-2)}{(m+n)(2mn+m+n-4)}.
\]
Since \(m,n\ge2\), \(mn-m-n=0\) only at \((2,2)\), so the first expression vanishes exactly when \(m=n\). The second expression also vanishes at \((m-1)(n-1)=3\), namely \((2,4)\) and \((4,2)\). Finally, any complementary pair of projections with respective ranges \(C,Z\) is necessarily the unique projection along the orthogonal decomposition \(E=C\oplus Z\); hence such a pair can be individually optimal only in the square case. This completes the proof.

## Verification

The standalone Python 3 checker `check.py` uses only standard-library rational arithmetic. Execute `python3 check.py`. It reconstructs all edge columns from the displayed tensor formulas for every \(2\le m,n\le7\), checks both exact formulas against full column sums, checks divergence-free circulation columns, and tests projection identities and cycle generators on smaller cases. It does not use floating-point approximations. The proof, not finite testing, establishes the unbounded parameter ranges.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582v1, public May 21, 2023), develop the invariant-projection framework. In their Section 2.6, Theorem 43 proves uniqueness of the invariant circulation projection for homogeneous Hamming graphs having the same alphabet size on every axis. That statement does not settle the two unequal-coordinate edge orbits or identify the two distinct, nonorthogonal norm minimizers here. The present formulas specialize to the homogeneous two-coordinate endpoint but exhibit symmetry breaking and a separate \((2,4)\) cycle-projection exception. Their earlier paper *Lipschitz free spaces on finite metric spaces* (arXiv:1807.03814v1) provides general historical context for averaging in graph-free spaces and focuses on recursive diamond and Laakso constructions, not the formulas here.

## Limitations

Only the coordinate-\(\ell_1\) norms, real scalars, two-factor complete-graph Cartesian products, and projections onto the specified cut/circulation subspaces are classified. The proof determines unique equivariant minimizers; it does not classify all nonsymmetric minimizers. No claim is made about nonuniform edge weights, other \(\ell_p\) norms, or products of three or more distinct complete graphs. Historical priority under other terminology (transportation-cost spaces, electrical-current projections, rook-graph incidence operators) has not been independently certified.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (2023), especially Section 2.6 and Theorem 43; https://arxiv.org/abs/2305.12582.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (2018); https://arxiv.org/abs/1807.03814.
