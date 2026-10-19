# A quadratic-time correlation profile for Gauss-map survival near zero

## Finding
Let \(T:[0,1]\to[0,1]\) be the Gauss map, with \(T(0)=0\) and \(T(x)=1/x-\lfloor1/x\rfloor\) for \(x>0\). For an integer \(k\ge2\), put \(I_k=[0,1/k]\) and define the \(n\)-observation survivor mass
\[
M_n(k)=\operatorname{Leb}\{x\in[0,1]:T^jx\in I_k\text{ for every }0\le j<n\},\qquad n\ge1.
\]
Set
\[
p_k=\sum_{j=k}^{\infty}j^{-2},\quad q_k=\sum_{j=k}^{\infty}j^{-3},\quad
\Lambda_k=p_k-\frac{2q_k^2}{p_k}.
\]
For every fixed real \(C>0\), **uniformly over integers** \(1\le n\le Ck^2\) as \(k\to\infty\),
\[
\boxed{M_n(k)=\frac{1}{k}\Lambda_k^{n-1}\big(1+O_C(k^{-2})\big).}
\]
In particular, for **every integer sequence** \(n_k\ge1\) satisfying \(n_k/k^2\to\tau\in[0,\infty)\),
\[
\boxed{\lim_{k\to\infty}\frac{M_{n_k}(k)}{k^{-1}p_k^{n_k-1}}=e^{-\tau/2}.}
\]
The two Hurwitz-zeta tails are explicitly computable: \(p_k=\zeta(2,k)\) and \(q_k=\zeta(3,k)\). The second limit is a genuine quadratic-time correction to the product-of-branch-Jacobians approximation, not an assertion about a stationary distribution.

## Assumptions and scope
The measure is ordinary Lebesgue measure and the hole is \((1/k,1]\). The number of observations includes time zero. The theorem requires \(k\to\infty\), while \(n\) may grow with \(k\) up to a fixed multiple of \(k^2\). There are no mixing, finite-alphabet, or generic-initial-data hypotheses. The map's rational points and inverse-branch boundaries can be included or discarded without affecting measure.

## Proof
Write \(\alpha=1/k\), let \(g_j(y)=1/(j+y)\) for \(j\ge k\), and consider the positive transfer operator on continuous functions on \(I_k\):
\[
(\mathcal L_k f)(y)=\sum_{j=k}^{\infty}\frac{f(g_j(y))}{(j+y)^2}.
\]
Every \(g_j(I_k)\subset I_k\), and, up to countably many endpoints, these are precisely the inverse branches that stay in \(I_k\). Repeated one-dimensional change of variables therefore gives the **exact identity**
\[
M_n(k)=\int_0^{\alpha}(\mathcal L_k^{n-1}\mathbf 1)(y)\,dy.
\tag{1}
\]
Define \(c_k=2q_k/p_k\) and the positive affine test function \(h_k(y)=1-c_ky\). Since \(q_k\le p_k/k\), \(c_k\le2/k\) and \(h_k(y)\ge1-2/k^2>0\) for \(k\ge2\). Moreover \(\Lambda_k=p_k-c_kq_k\ge p_k(1-2/k^2)>0\).

For \(s>1\) write \(S_s(y)=\sum_{j=k}^{\infty}(j+y)^{-s}\), and let \(r_k=\sum_{j=k}^{\infty}j^{-4}\), \(s_k=\sum_{j=k}^{\infty}j^{-5}\). Taylor's theorem with alternating derivative signs, for \(0\le y\le\alpha\), gives
\[
S_2(y)=p_k-2q_ky+R_2(y),\quad 0\le R_2(y)\le3r_ky^2,
\]
\[
S_3(y)=q_k-3r_ky+R_3(y),\quad 0\le R_3(y)\le6s_ky^2.
\]
Direct substitution, using \(c_kp_k=2q_k\), yields
\[
\mathcal L_k h_k-\Lambda_kh_k
=R_2(y)+3c_kr_ky-c_kR_3(y)-c_k^2q_ky.
\tag{2}
\]
The elementary integral test implies \(p_k\asymp k^{-1}\), \(q_k=O(k^{-2})\), \(r_k=O(k^{-3})\), and \(s_k=O(k^{-4})\). Thus the right side of (2) is \(O(k^{-5})\), **uniformly on the entire interval**. Since \(\Lambda_kh_k\asymp k^{-1}\), the positive operator satisfies
\[
(1-\epsilon_k)\Lambda_kh_k\le\mathcal L_kh_k\le(1+\epsilon_k)\Lambda_kh_k,
\quad\epsilon_k=O(k^{-4}).
\]
Induction by positivity gives the same inequalities with factors \((1\pm\epsilon_k)^m\) for \(\mathcal L_k^m h_k\). Also \(h_k=1+O(k^{-2})\) uniformly, so sandwiching \(\mathbf1\) between constant multiples of \(h_k\) and integrating (1) proves
\[
M_n(k)=\alpha\Lambda_k^{n-1}\big(1+O(k^{-2}+nk^{-4})\big),
\]
uniformly whenever \(n=O(k^2)\). This is the first asserted formula.

Finally, integral comparison yields
\[
p_k=\frac1k+O(k^{-2}),\qquad q_k=\frac1{2k^2}+O(k^{-3}),
\]
so that \(q_k/p_k=1/(2k)+O(k^{-2})\) and
\[
\frac{\Lambda_k}{p_k}=1-2\left(\frac{q_k}{p_k}\right)^2
=1-\frac1{2k^2}+O(k^{-3}).
\]
Consequently \((n_k-1)\log(\Lambda_k/p_k)\to-\tau/2\). Combining with the first formula proves the second. All estimates are deterministic, and no finite computation is used to prove a quantified asymptotic.

## Verification
The standalone `verify.py` tests 507 exact-rational two-branch cylinder identities, nine independent transfer-integral/digamma agreements, 81 sampled approximate-eigenfunction residual inequalities, nine corresponding zeta-tail correction diagnostics, and four quadratic-time limits, together with nine positivity checks: **619 checks** passed. In particular the exact mass identity for two observations is
\[
M_2(k)=\psi(k+1/k)-\psi(k),
\]
where \(\psi\) is the digamma function, and it agrees with direct quadrature of \(\mathcal L_k\mathbf 1\). The proof above, not this finite diagnostic suite, establishes the full quantified theorem. Execute with `python verify.py`, using Python 3 and `mpmath`.

## Relationship to prior work
Liu and Liao study the same Gauss map and the same family of holes near the endpoint \(1\), giving symbolic descriptions and Hausdorff-dimension plateaus for **infinite-time** survivor sets. Their dimension-pressure statements do not give the Lebesgue mass after finitely many observations, uniformly in a diverging observation horizon and a simultaneously shrinking allowed interval. Nisoli's work studies the **unrestricted** Gauss–Kuzmin–Wirsing transfer operator and certifies its global spectral data, not the restricted, moving-cutoff operator \(\mathcal L_k\). The general transfer-operator method and classical Gauss-map identities are background; the asserted quantitative contribution is the uniform \(n=O(k^2)\) survival expansion and its explicit nontrivial scaling profile.

## Limitations
The relative approximation is proved for \(n\le Ck^2\) with fixed \(C\), not for arbitrary growing \(n/k^2\). It is restricted to the reciprocal thresholds \(1/k\) and Lebesgue initial mass, and does not claim a full asymptotic expansion of the true Perron eigenvalue of \(\mathcal L_k\), a Hausdorff-dimension formula, or an asymptotic for infinite-time survivor mass. Possible equivalent formulations in older spectral perturbation literature are not excluded by the bibliographic comparison.

## References
1. C. Liu and L. Liao, *Survivor Set of Gauss Map with a Hole at 1*, arXiv:2610.14534v1 (first posted 2026-10-10), https://arxiv.org/html/2610.14534v1 .
2. I. Nisoli, *Certified spectral approximation of transfer operators and the Gauss map*, arXiv:2602.19435v1 (first posted 2026-02-23), https://arxiv.org/html/2602.19435v1 .
