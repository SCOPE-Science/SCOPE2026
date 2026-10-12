# Exact all-component-count mean-square stability of SAGA on identical positive-definite quadratics

## Finding

**Theorem.** Fix an integer \(n\ge 2\), a finite dimension \(d\ge 1\), a symmetric positive-definite \(d\times d\) matrix \(H\), and \(w_\star\in\mathbb R^d\). Apply the original single-index, uniform-sampling, constant-stepsize SAGA algorithm without an additional proximal term to
\[
f_i(w)=\frac12(w-w_\star)^\mathsf TH(w-w_\star),\qquad i=1,\ldots,n.
\]
For **every deterministic initial iterate and every deterministic initial gradient table**, the iterates and stored gradients converge in mean square to their optimal values if and only if
\[
\boxed{\quad 0<\eta\lambda_{\max}(H)<\tau_n,\quad}
\]
where \(\tau_n>1\) is the unique positive root of
\[
P_n(t)=(2n-1)(t-1)(1+(n-1)t)-1=0.
\]
In particular, \(\tau_2=2/\sqrt3\), \(\tau_3=(5+\sqrt{265})/20\), the thresholds decrease strictly in \(n\), and
\[
\tau_n=1+\frac{1}{2n^2}+\frac{1}{4n^3}+O(n^{-4})\quad(n\to\infty).
\]
More strongly, in a scalar eigendirection with \(s=\eta\lambda\ge\tau_n\), **every nonzero deterministic initial iterate-and-table state fails to converge in mean square**. The boundary is excluded.

## Assumptions and scope

At iteration \(k\), draw an independent index \(I_k\), uniformly from \(\{1,\ldots,n\}\). Use the saved **pre-update** component-gradient table to form the SAGA gradient, update the iterate, and *then* replace the sampled component's saved gradient with its newly evaluated gradient at the old iterate. In symbols, set \(x_k=w_k-w_\star\), store \(y_{i,k}=H^{-1}g_{i,k}\), where \(g_{i,k}\) is the gradient saved for component \(i\) (the inverse exists because \(H\succ0\)), and define \(\bar y_k=n^{-1}\sum_i y_{i,k}\). The iteration is
\[
\begin{aligned}
x_{k+1}&=x_k-\eta H\big(x_k-y_{I_k,k}+\bar y_k\big),\\
y_{I_k,k+1}&=x_k,\qquad y_{j,k+1}=y_{j,k}\quad(j\ne I_k).
\end{aligned}
\]
All results concern fixed \(\eta\), exact arithmetic, IID sampling with replacement, finite-dimensional SPD \(H\), and identical component Hessians and minimizers. Arbitrary deterministic saved gradients are allowed, not only tables initialized at \(w_0\). Mean-square convergence means \(\mathbb E\|x_k\|^2\to0\) and \(\mathbb E\sum_i\|g_{i,k}\|^2\to0\); there is no claim about nonidentical component Hessians, adaptive stepsizes, or rates under noise at the minimizer.

## Proof

**1. Scalar spectral reduction and exact moments.** Diagonalize \(H\) orthogonally. Since all component Hessians are the same, each orthogonal eigencoordinate obeys the same scalar random-index recursion with \(s=\eta\lambda>0\):
\[
x'=(1-s)x+s(y_I-m),\qquad y_I'=x,\quad y_j'=y_j\;(j\ne I),
\]
where \(m=n^{-1}\sum_i y_i\) and \(v=n^{-1}\sum_i(y_i-m)^2\). Write \(M=(x^2,xm,m^2,v)^\mathsf T\). Directly averaging over the \(n\) sampled indices gives the **conditional**, rather than merely stationary, exact moment relation \(\mathbb E[M'\mid x,y]=B_{n,s}M\), with
\[
B_{n,s}=\begin{pmatrix}
(1-s)^2&0&0&s^2\\
(1-s)/n&(1-s)(n-1)/n&0&-s/n\\
1/n^2&2(n-1)/n^2&(n-1)^2/n^2&1/n^2\\
(n-1)/n^2&-2(n-1)/n^2&(n-1)/n^2&(n^2-n-1)/n^2
\end{pmatrix}.
\]
For example, the first row follows from \(\mathbb E(y_I-m)=0\) and \(\mathbb E(y_I-m)^2=v\); the last follows by computing \(n^{-1}\sum_i(y_i')^2-(m')^2\). This identity is valid for every scalar state and every real \(s\).

**2. A positive energy with exact sign-changing drift.** Set
\[
Q=n+(n-1)^2s,\qquad K=1+(n-1)s,
\]
and define the quadratic state energy
\[
\begin{aligned}
V_{n,s}(x,y)={}&Qx^2-n(n-1)s^2xm\\
&+\frac{n(n-1)}2s^2Km^2+\frac{n(2n-1)}2s^2Kv.
\end{aligned}
\]
For every integer \(n\ge2\) and every \(s>0\), this is positive definite in the \((n+1)\)-dimensional state \((x,y_1,\ldots,y_n)\). Indeed \(v\ge0\), with \(v=0\) precisely when all table entries equal \(m\). The variance coefficient is strictly positive. The discriminant of the \((x,m)\) quadratic is positive in the positive-definiteness convention:
\[
\begin{aligned}
4Q\Big(\frac{n(n-1)}2s^2K\Big)
-\big(n(n-1)s^2\big)^2
&=n(n-1)s^2\,[2QK-n(n-1)s^2],\\
2QK-n(n-1)s^2
&=2n+2(n-1)(2n-1)s\\
&\quad +(n-1)(2n-1)(n-2)s^2>0.
\end{aligned}
\]
Multiplying the exact moment matrix by the four energy coefficients, and canceling the remaining coefficients of \(xm,m^2,v\), gives the **identity for every state**
\[
\boxed{\;\mathbb E[V_{n,s}(x',y')\mid x,y]-V_{n,s}(x,y)=sP_n(s)x^2.\;}
\]
The algebra is reproduced exactly and independently checked using the embedded `verify.py`.

**3. Determine the unique threshold.** We have \(P_n(0)=-2n<0\), \(P_n(1)=-1\), and \(P_n(2)=4n(n-1)>0\). Moreover \(P_n\) is an upward-opening quadratic with negative constant term. Hence it has exactly one positive zero \(\tau_n\in(1,2)\), and \(P_n(s)<0\) if and only if \(0<s<\tau_n\).

**4. Sufficiency.** In that range, take unconditional expectations of the energy identity and sum over time:
\[
\mathbb EV_k+s(-P_n(s))\sum_{j=0}^{k-1}\mathbb E x_j^2=V_0.
\]
Since \(V\) is nonnegative and \(s(-P_n(s))>0\), the nonnegative sequence \(\mathbb E x_j^2\) is summable; in particular it converges to zero. Independently the mean squared table norm \(e_k=n^{-1}\sum_i\mathbb E y_{i,k}^2\) obeys
\[
e_{k+1}=\Big(1-\frac1n\Big)e_k+\frac1n\mathbb Ex_k^2.
\]
A stable linear scalar filter with vanishing input converges to zero, so \(e_k\to0\). Every scalar iterate and its entire table therefore converge in mean square. Orthogonal diagonalization of finite-dimensional \(H\) and the requirement \(\eta\lambda_{\max}(H)<\tau_n\) prove the matrix result.

**5. Necessity and endpoint.** If \(s\ge\tau_n\), the energy is a nonnegative submartingale in expectation: \(\mathbb EV_{k+1}\ge\mathbb EV_k>0\) from any nonzero deterministic scalar state. Were \(\mathbb Ex_k^2\to0\), the displayed table recurrence would imply \(e_k\to0\), and because \(V\) is a fixed positive quadratic in the iterate and table, \(\mathbb EV_k\to0\), a contradiction. At \(s=\tau_n\) the drift is identically zero, so the same contradiction applies with conserved expected energy. For an arbitrary SPD matrix, initialize a nonzero state supported only on a unit eigenvector of \(\lambda_{\max}(H)\). This establishes failure of the all-initialization property when \(\eta\lambda_{\max}(H)\ge\tau_n\); \(\eta=0\) trivially also fails for general initial states.

**6. Sample-count law.** Writing \(\varepsilon_n=\tau_n-1\) in the threshold equation gives
\[
(2n-1)\varepsilon_n\big[n+(n-1)\varepsilon_n\big]=1.
\]
For fixed positive \(\varepsilon\), the left-hand side strictly increases with integer \(n\ge2\), so \(\varepsilon_n\) strictly decreases. Expanding this equation as \(n\to\infty\) yields \(\varepsilon_n=1/(2n^2)+1/(4n^3)+O(n^{-4})\). Substituting \(n=2\) and \(n=3\) gives the explicit cases stated above.

## Verification

Run `python verify.py` with Python 3 and SymPy installed (the included `requirements.txt` specifies the dependency). The program checks, **symbolically for unconstrained formal \(n,s\)**, the entire four-moment transition matrix, the four energy-drift coefficients, the positive-definiteness factorization, \(\det(I-B_{n,s})\), and the sample-count polynomial comparison. A second, independently implemented direct update enumerator performs 270 exact-rational conditional expectations for \(n\in\{2,3,4,5,7\}\). The actual execution returned `VERIFY_OK symbolic_general_n_s=PASS exact_enumerations=270`.

The symbolic identities are not, by themselves, substitutes for the positivity argument, stochastic telescoping argument, or the all-initial-state necessity proof; those are supplied above. A finite enumeration checks implementation consistency but is not an exhaustive proof for all \(n\).

## Relationship to prior work

Defazio, Bach and Lacoste-Julien (2014) introduce SAGA and supply generally applicable sufficient convergence stepsizes; their main general strongly convex bound is not a necessary-and-sufficient stability condition on the specialized identical-Hessian quadratic family. Bottou, Curtis and Nocedal (2016 preprint; 2018 journal) present SAGA among numerical stochastic variance-reduction methods and explicitly classify the subject first as MSC 65K05. Gazagnadou, Gower and Salmon (2019) optimize sufficient mini-batch and stepsize prescriptions using expected smoothness, not the exact all-initialization scalar second-moment cutoff. The two-component specialization \(\tau_2=2/\sqrt3\) is already accounted for and **is not asserted to be novel**; the mathematical increment is the all-\(n\) law, its asymptotics, and the SPD eigenspace extension with sharp necessity. Standard full-gradient descent on these quadratics has the larger bound \(\eta\lambda_{\max}(H)<2\); the diminishing SAGA margin comes from gradient-table memory even when all component objectives coincide.

## Limitations

The theorem requires identical SPD component Hessians and identical minimizers, independent uniform sampling with replacement, original nonproximal SAGA, and exact arithmetic. It does not address unequal component Hessians, nonuniform sampling, minibatches, asynchronous updates, nonquadratic losses, mean-square linear rates, or almost-sure behavior at the boundary. The cited primary texts and scientific search did not reveal an equivalent published all-\(n\) formula, but an older exact stochastic linear-systems analysis under different terminology could supply one; a negative search result cannot establish exhaustive novelty. The comparison with broader convergence theorems is claim-level, not a general novelty certification.

## References

1. A. Defazio, F. Bach, and S. Lacoste-Julien, *SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives*, arXiv:1407.0202, initial public v1 July 1, 2014. https://arxiv.org/abs/1407.0202
2. L. Bottou, F. E. Curtis, and J. Nocedal, *Optimization Methods for Large-Scale Machine Learning*, arXiv:1606.04838, initial public v1 June 15, 2016; SIAM Review 60 (2018), DOI:10.1137/16M1080173. First stated MSC 65K05. https://arxiv.org/abs/1606.04838
3. N. Gazagnadou, R. M. Gower, and J. Salmon, *Optimal Mini-Batch and Step Sizes for SAGA*, Proceedings of Machine Learning Research 97 (2019), pp. 2142–2150. https://proceedings.mlr.press/v97/gazagnadou19a.html
