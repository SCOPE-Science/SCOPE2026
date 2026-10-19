# IID four-branch coding and sharp information-growth bounds for a quadratic random map

## Finding
A position-dependent mixture of two quadratic maps can have a uniform invariant state even though its branch dynamics are nonlinear. In the two-parameter example of Góra, Li, Boyarsky and Proppe, the joint observable consisting of the selected quadratic map and the spatial half-branch is exactly independent and identically distributed (IID) at **all** times. Moreover, the mutual information of its first \(n\) labels with the initial continuous coordinate is exactly \(n\Lambda\), and the rate has optimal strict parameter-independent bounds
\[\log 2<\Lambda<2\log2-\tfrac12.\]
The full four-symbol law is uniform precisely when \(b_1+b_2=4\); otherwise the map-choice weights are biased.

## Assumptions and scope
Take real parameters \(0<b_1<2<b_2<4\). On \(0\le y\le1/2\), define
\[f_i(y)=(4-2b_i)y^2+b_iy,\quad r_i(y)=f_i'(y)=b_i+4(2-b_i)y.\]
Both \(f_i\) map the half interval increasingly and bijectively onto \([0,1]\). Write \(y(x)=x\) on \([0,1/2)\), \(y(x)=x-1/2\) on \([1/2,1]\), and \(\tau_i(x)=f_i(y(x))\). Values at the half-integer discontinuity do not affect the stated probability laws. Set
\[k_1=\frac{b_2-2}{2(b_2-b_1)},\qquad k_2=\frac{2-b_1}{2(b_2-b_1)},\qquad w_i=2k_i.\]
For each step sample \(S_t\in\{1,2\}\) using fresh randomness and conditional probabilities \(p_i(x)=k_i r_i(y(x))\), then put \(X_{t+1}=\tau_{S_t}(X_t)\). Assume \(X_0\) is Lebesgue-uniform on \([0,1]\), independent of fresh selection randomness. Define \(B_t=\lfloor2X_t\rfloor\), with endpoint one assigned arbitrarily, and \(C_t=(B_t,S_t)\). Entropies and mutual information are Shannon quantities in natural-log units. The derivative integrals in this result are stationary averages, not assertions about each path's Lyapunov exponent.

## Proof
**(1) Joint inverse-branch law.** Direct simplification gives \(k_1r_1(y)+k_2r_2(y)=1\), so the probabilities are legal. Each \(r_i>0\) and \(\int_0^{1/2}r_i(y)\,dy=f_i(1/2)-f_i(0)=1\). For an arbitrary Borel set \(E\subset[0,1]\), for each \(j\in\{0,1\}\) and \(i\in\{1,2\}\), the change of variables \(z=f_i(y)\) yields
\[\Pr(B_t=j,S_t=i,X_{t+1}\in E)=\int_{f_i^{-1}(E)} k_i r_i(y)\,dy=k_i|E|,\]
provided \(X_t\) is uniform. Thus \(X_{t+1}\) is again uniform, and is independent of \(C_t\); the four label probabilities are \(k_i\), regardless of \(j\). The Markov property and fresh stepwise randomness now inductively give independence of \(C_t\) from every previous label and the IID law of \((C_t)_{t\ge0}\). In particular the map labels have probabilities \(w_i=2k_i\), and the half-branch labels are independent fair bits. The four weights are equal if and only if \(k_1=k_2\), equivalently \(b_1+b_2=4\).

**(2) Exact block information.** The entropy of the IID block is
\[H(C_0,\ldots,C_{n-1})=n(\log2+H(w)),\quad H(w)=-\sum_iw_i\log w_i.\]
Condition on \(X_0\) and all earlier labels. The current half-branch \(B_t\) is determined because the earlier map selections determine \(X_t\); the only remaining randomness is the Bernoulli map choice. Hence the conditional entropy chain rule and stationarity show
\[H(C_0,\ldots,C_{n-1}\mid X_0)=n\int_0^1 h(p_1(x))\,dx,\]
where \(h(u)=-u\log u-(1-u)\log(1-u)\). Using \(p_i=k_ir_i\) and the half-interval integral of \(r_i\),
\[\int_0^1h(p_1(x))\,dx=-\sum_iw_i\log k_i-\sum_iw_i\int_0^{1/2}r_i(y)\log r_i(y)\,dy\]
\[=\log2+H(w)-\Lambda.\]
Subtracting conditional entropy from unconditional entropy proves the exact identity \(I(X_0;C_0,\ldots,C_{n-1})=n\Lambda\) for every integer \(n\ge1\).

**(3) Closed rate and sharp extrema.** Define \(F(t)=\tfrac12t^2\log t-\tfrac14t^2\). Then
\[J(b)=\int_0^{1/2}\bigl(b+4(2-b)y\bigr)\log\bigl(b+4(2-b)y\bigr)\,dy\]
\[=\frac{F(4-b)-F(b)}{4(2-b)}\quad(b\ne2),\qquad J(2)=\log2,\qquad\Lambda=\sum_iw_iJ(b_i).\]
Each \(r_i\) integrates to one on \([0,1/2]\), so it is a probability density relative to the reference density \(2\) on that interval. Consequently
\[J(b)-\log2=\int_0^{1/2}r_b(y)\log\frac{r_b(y)}2\,dy=D(r_b(y)dy\|2dy).\]
Strict positivity follows from strict convexity unless \(b=2\); here both parameters differ from two. For the upper bound write \(r_b(y)=2+(b-2)(1-4y)\). Since \(1-4y\) is uniform on \([-1,1]\) under normalized Lebesgue measure and \(t\mapsto t\log(t/2)\) is strictly convex, its average increases strictly as the amplitude \(|b-2|\) increases in \((0,2)\) (a mean-preserving-spread comparison, or differentiation and pairing \(y\) with \(1/2-y\)). Therefore \(D(r_b\|2)<D(r_0\|2)=\log2-1/2\), obtaining the strict upper bound after averaging with positive \(w_i\). Both endpoints are sharp limits: choose \(b_1=2-\epsilon,b_2=2+\epsilon\) for the lower limit and \(b_1=\epsilon,b_2=4-\epsilon\) for the upper, then let \(\epsilon\downarrow0\).

## Verification
The standalone `verify.py` checks the key rational identity, normalization integrals, the closed-form derivative integral at multiple rational parameter pairs, the strict rate bounds, and the independently numerically integrated Shannon entropy identity. It prints `VERIFY_OK`. The proof of infinite-time IID and exact information for every horizon is analytic; finitely many numerical checks are not substitutes for it.

## Relationship to prior work
Góra, Li, Boyarsky and Proppe introduced exactly this quadratic pair, the position-dependent linear switching rule, and its uniform stationary density (Section 5, equations (13)–(15), arXiv:1404.7455v1). These are taken as premises and independently checked above; they are **not** claimed to be new. Their article does not state an IID four-label coding, an exact finite-horizon mutual-information law, or the sharp global rate interval. General inverse-branch Jacobian and entropy identities are well-known mechanisms; the contribution here is the complete explicit specialization, all-horizon IID and information profile, and optimized bounds for the source's nonlinear two-parameter family.

## Limitations
The law is stationary and uses a fresh position-dependent random choice at each step; arbitrary fixed initial coordinates need not produce IID labels. The map boundaries are only defined up to null sets. The label process does not assert that the continuous state process is IID. The sharp bounds are strict at all admissible parameter pairs and attained only as limiting parameters approach the excluded boundary. The information calculation does not establish uniqueness of all invariant measures, convergence from every initial distribution, or a sample-path Lyapunov theorem. Unindexed prior derivations of the specialized information identity remain possible.

## References
1. P. Góra, Z. Li, A. Boyarsky and H. Proppe, *Toward A Mathematical Holographic Principle*, arXiv:1404.7455v1 (first posted 29 April 2014), particularly Section 5 and equations (13)–(15), https://arxiv.org/abs/1404.7455.
2. W. Bahsoun, C. Bose and A. Quas, *Deterministic representation for position dependent random maps* (2008); general skew-product representation background, not an identical explicit four-symbol theorem.
