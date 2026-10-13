# Sharp finite-horizon amplification of diagonally preconditioned delta-rule erasures

## Finding

Let \(d\ge 2\), \(\kappa\ge1\), and consider the family of exact normalized erasure matrices
\[
\mathcal P_{\kappa,d}=\left\{P(k,D)=I-\frac{k(Dk)^{\mathsf T}}{k^{\mathsf T}Dk}:\ \|k\|_2=1,\ D=\operatorname{diag}(d_1,\ldots,d_d),\ 1\le d_i\le\kappa\right\}.
\]
For **every** integer \(N\ge1\), the sharp worst-case norm of an arbitrary length-\(N\) product is
\[
\boxed{\sup_{P_1,\ldots,P_N\in\mathcal P_{\kappa,d}}\|P_1P_2\cdots P_N\|_2
=\left(\frac{\kappa+1}{2\sqrt\kappa}\right)^N.}
\]
The supremum is attained by alternating two explicit matrices, already in dimension two. Consequently the joint spectral radius is exactly \((\kappa+1)/(2\sqrt\kappa)\). There is a sharp dichotomy: at \(\kappa=1\) every product is nonexpansive; for each \(\kappa>1\), a two-periodic sequence admits exponentially growing states despite each token's current regression residual being erased **exactly**.

## Assumptions and scope

All matrices and vectors are real and computations exact. The key dimension satisfies \(d\ge2\); keys are unit length and may vary between steps. The diagonal metric may also vary arbitrarily from step to step within \([1,\kappa]^d\). The matrix \(P(k,D)\) is an idempotent oblique projector with \(P(k,D)k=0\). It is obtained from the right-preconditioned delta-rule write
\[
S^+=S+\beta(v-Sk)(Dk)^{\mathsf T},\qquad \beta=(k^{\mathsf T}Dk)^{-1},
\]
when \(v=0\), so that \(S^+=SP(k,D)\). With arbitrary target \(v\), the same choice of \(\beta\) makes the *current* residual \(S^+k-v\) zero, but the theorem concerns products of homogeneous factors, not the forced state trajectories with arbitrary nonzero targets. The family fixes the *ratio* of allowed diagonal entries by normalizing their lower bound to one. It does not assume that a particular learned preconditioner controller realizes an arbitrary admissible sequence.

## Proof

**One-factor sharp bound.** Fix a unit key \(k\) and an admissible diagonal \(D\). Put \(\mu=k^{\mathsf T}Dk\in[1,\kappa]\). In the two-dimensional plane spanned by \(k\) and \(Dk\), choose an orthonormal basis beginning with \(k\), writing \(Dk=\mu k+\tau e\) with \(e\perp k\). On this plane the projector has matrix
\[
\begin{pmatrix}0&-\tau/\mu\\0&1\end{pmatrix},
\]
and it acts as the identity on the orthogonal complement. If \(\tau=0\), it is an ordinary nonzero orthogonal projector. In all cases, because \(d\ge2\),
\[
\|P(k,D)\|_2=\sqrt{1+\tau^2/\mu^2}
=\frac{\|Dk\|_2}{k^{\mathsf T}Dk}.
\]
For each \(x\in[1,\kappa]\), \((x-1)(x-\kappa)\le0\), hence \(x^2\le(\kappa+1)x-\kappa\). Weighting this inequality by \(k_i^2\) and summing gives
\[
\|Dk\|_2^2\le(\kappa+1)\mu-\kappa.
\]
The function \(((\kappa+1)\mu-\kappa)/\mu^2\) on \([1,\kappa]\) has its maximum at \(\mu=2\kappa/(\kappa+1)\) (the constant case \(\kappa=1\) is immediate). Its maximum equals \((\kappa+1)^2/(4\kappa)\). Thus every factor has norm at most \(C_\kappa=(\kappa+1)/(2\sqrt\kappa)\), and submultiplicativity yields the asserted upper bound \(C_\kappa^N\) for every product length and every dimension.

**Simultaneous sharpness for all lengths.** Set \(t=\sqrt\kappa\) and in dimension two take
\[
\begin{aligned}
k_1&=(1,t)^{\mathsf T}/\sqrt{1+t^2},&D_1&=\operatorname{diag}(t^2,1),\\
k_2&=(t,1)^{\mathsf T}/\sqrt{1+t^2},&D_2&=\operatorname{diag}(1,t^2).
\end{aligned}
\]
Both metrics lie in the allowed box and \(k_j^{\mathsf T}D_jk_j=2t^2/(1+t^2)\). Direct substitution gives
\[
P_1=\frac12\begin{pmatrix}1&-1/t\\-t&1\end{pmatrix},
\qquad P_2=P_1^{\mathsf T}.
\]
Let \(a=(1,-t)^{\mathsf T}/\sqrt{1+t^2}\), \(b=(t,-1)^{\mathsf T}/\sqrt{1+t^2}\); they are unit vectors, and
\[
P_1=C_\kappa ab^{\mathsf T},\qquad P_2=C_\kappa ba^{\mathsf T}.
\]
For \(N=2r\ge2\), the alternating product equals \(C_\kappa^{2r}aa^{\mathsf T}\); for \(N=2r+1\ge1\), it equals \(C_\kappa^{2r+1}ab^{\mathsf T}\). Its operator norm is exactly \(C_\kappa^N\) in either case. For \(d>2\), pad both keys with zeros and both diagonal matrices with entries one: the factors become a direct sum of these two-dimensional factors and an identity, so their product norms remain \(C_\kappa^N\). The construction also works when \(\kappa=1\), in which case \(P_1=P_2\) is orthogonal.

**Actual unbounded homogeneous memory.** With one output row \(S_0=a^{\mathsf T}\), zero targets, and alternately the two key/metric pairs above, the row is \(S_N=C_\kappa^N a^{\mathsf T}\) for even \(N\) and \(S_N=C_\kappa^N b^{\mathsf T}\) for odd \(N\). Therefore \(\|S_N\|_2=C_\kappa^N\), while for each step \(S_{j}k_j=0\). When \(\kappa>1\), both normalizing gates \(\beta_j=(\kappa+1)/(2\kappa)\) lie strictly between zero and one. In particular, with \(\kappa=2\), both diagonal entries belong to \([1,2]\), the gates equal \(3/4\), and every two steps amplify the appropriate state by \(9/8\). This demonstrates the dichotomy and finishes the proof.

## Verification

Run `python verify.py` using Python 3.9 or later; only the standard library is needed. The checker reconstructs two-dimensional extremizers with exact rational arithmetic for fifteen square condition ratios and eighteen product lengths. It checks idempotence, exact annihilation of the current key, the rank-one identities, and exact equality of squared product norms. It also tests the \(\kappa=2\) example and performs deterministic random finite-product comparisons to the universal bound. The observed output is:

`VERIFY_OK exact_fraction_identities= 630 random_product_norm_checks= 48000 two_step_growth_kappa2= 1.125`

These finite computations are corroborating tests, not a proof of the universally quantified assertion; the argument above proves the norm and finite-horizon bounds in every finite dimension.

## Relationship to prior work

Zhou et al. introduce diagonal right-preconditioning of the delta-rule memory update and prove a *token-local* residual-ratio statement (their Theorem 5.2). That statement does not compare the Euclidean norms of states across different keys: all ratios can vanish in the witness above even as the shared memory grows. No theorem about instability of their specific learned hypergradient trajectory is asserted here.

The identity between the norms of an oblique projection and its complement is classical; Szyld surveys it and earlier proofs. The one-factor bound here is likewise a form of the classical Kantorovich angle inequality. Neither is represented as new. Censor and Elfving study diagonally weighted projections under feasibility-algorithm structural assumptions, including a partition-of-identity weighting in their block iteration. Those results do not imply an unrestricted sharp all-length norm for independently switching right-preconditioners. Kopecká addresses products of orthogonal projections, whose factors are nonexpansive, whereas the present obstruction requires changing nonorthogonal metrics. The additional step established here is the exact *attainable* finite-horizon envelope for this diagonal family, with a single two-token word saturating it at every length.

## Limitations

The result is a worst-case, exact-arithmetic theorem for arbitrary admissible key/metric switching, not a prediction of typical trained sequence-model behavior. The witnesses use deliberately chosen keys and preconditioners; the result does not show that a specified online preconditioner-learning recurrence generates them. It applies to zero target vectors when demonstrating homogeneous state blow-up, and makes no corresponding claim about output accuracy with nonzero targets or about the full loss of any learned model. Numerical overflow and finite-precision effects are outside the theorem. For dimension one, normalized erasure is the zero matrix, and the stated bound is not the correct sharp value.

## References

1. Chenyu Zhou, Hongpei Li, Yuerou Liu, Jianghao Lin, Dongdong Ge, and Yinyu Ye, *OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention*, arXiv:2605.13473v1, first public 2026-05-13, https://arxiv.org/pdf/2605.13473 (especially Sections 4.1–4.3, Theorem 5.2, and Appendix A).
2. Daniel B. Szyld, *The many proofs of an identity on the norm of oblique projections*, Numerical Algorithms 42 (2006), 309–323, https://doi.org/10.1007/s11075-006-9046-2.
3. Yair Censor and Tommy Elfving, *Iterative algorithms with seminorm-induced oblique projections*, Abstract and Applied Analysis 2003:7 (2003), 387–406, https://doi.org/10.1155/S108533750321201X (especially Sections 2–3).
4. Yair Censor and Tommy Elfving, *Block-Iterative Algorithms with Diagonally Scaled Oblique Projections for the Linear Feasibility Problem*, SIAM Journal on Matrix Analysis and Applications 24 (2002), 40–58, https://doi.org/10.1137/S089547980138705X.
5. Eva Kopecká, *When products of projections diverge*, Journal of the London Mathematical Society 102 (2020), 345–367, https://doi.org/10.1112/jlms.12322 (orthogonal projections, a different setting).
