# A sharp critical-window total-variation law for probabilistic parking preferences

## Finding

For every integer \(n\ge2\), choose preferences of \(n\) successive cars independently and uniformly from \(\{1,\ldots,n\}\). A car takes its preferred spot if empty; otherwise, with probability \(p\) it searches rightward for the nearest vacancy, and with probability \(1-p\) it searches leftward for the nearest vacancy. An unsuccessful search means the car does not park. Condition on all cars successfully parking, let \(Q_{n,p}\) be the distribution of the last car's original preference, and let \(U_n\) be uniform on \(\{1,\ldots,n\}\). All coins and preferences are independent before conditioning. The total-variation distance is \(\|Q-U\|_{\mathrm{TV}}=\tfrac12\sum_j|Q(j)-U(j)|\).

**Theorem (critical crossover and matched outer scale).** If \(p_n\in[0,1]\) and \(\sqrt n(p_n-\tfrac12)\to c\in\mathbb R\), then
\[
\lim_{n\to\infty}n\,\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}
=\frac{1+\sqrt{1+32c^2/\pi}}2.
\]
In particular, the sharp constant at unbiased coin tossing is \(\lim_{n\to\infty}n\|Q_{n,1/2}-U_n\|_{\mathrm{TV}}=1\). In the outer regime \(\sqrt n|p_n-\tfrac12|\to\infty\), one has
\[
\lim_{n\to\infty}\frac{\sqrt n}{|2p_n-1|}\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}=\sqrt{2/\pi}.
\]
The claims hold for arbitrary parameter sequences satisfying their conditions, including fixed biased parameters in the outer regime.

## Assumptions and scope

The parking rule selects the search direction *once*, only when the initially preferred space is occupied. Cars cannot jump over a vacancy in the chosen direction, and a car fails if no vacant space lies in that direction. The conditioning event has probability \((n+1)^{n-1}/n^n\), independently of \(p\), as established previously. Neither extra parking spaces nor a different coin-flip protocol is covered. All limits are for integer \(n\to\infty\). The paper by Durmić, Han, Harris, Ribeiro and Yin supplies the finite preference law used below; that finite law is not claimed as new.

## Proof

**1. Exact decomposition.** Define, for \(1\le j\le n\),
\[
t_{n,j}=\frac{\binom{n-1}{j-1}j^{j-2}(n+1-j)^{n-j-1}}{(n+1)^{n-1}},\qquad
A_{n,j}=\sum_{k=1}^{j}t_{n,k},\quad A_{n,0}=0.
\]
At a factor whose base is \(1\), interpret the corresponding tree-count power as \(1\). The established last-preference counting formula (Durmić et al., Theorem 3 and its proof) may be written
\[
Q_{n,p}(j)=(1-p)A_{n,j-1}+t_{n,j}+p\bigl(A_{n,n}-A_{n,j}\bigr).
\]
Indeed the unoccupied final spot among the first \(n-1\) cars is either left of, equal to, or right of the final preference; the respective final parking probabilities are \(1-p\), \(1\), and \(p\). The established Abel count gives
\[
t_{n,j}=t_{n,n+1-j},\qquad A_{n,n}=\frac2{n+1}.
\]
Set \(\Delta_{n,j}=2/(n+1)-A_{n,j-1}-A_{n,j}\). Direct algebra now gives
\[
Q_{n,p}(j)-\frac1n
=\underbrace{\frac{t_{n,j}}2-\frac1{n(n+1)}}_{b_{n,j}}
+(p-\tfrac12)\Delta_{n,j}.
\tag{1}
\]
Reflection gives \(\Delta_{n,n+1-j}=-\Delta_{n,j}\). For \(j\le n/2\), an exact cancellation using symmetry yields
\[
\Delta_{n,j}=\sum_{k=j}^{n-j}t_{n,k}\ge0;
\tag{2}
\]
for \(j>(n+1)/2\), use the reflected negative value, and the odd central value is zero.

**2. Tree-count kernel asymptotics.** Put \(C=(2\pi)^{-1/2}\) and \(g(x)=C[x(1-x)]^{-3/2}\) for \(0<x<1\). Standard two-sided Stirling inequalities, applied to the factorials in the definition, yield a universal \(K<\infty\) such that
\[
0\le t_{n,j}\le K\frac{\sqrt{n+1}}{[j(n+1-j)]^{3/2}}
\quad(1\le j\le n),
\tag{3}
\]
and, uniformly when \(j/n\) ranges over compact subintervals of \((0,1)\),
\[
n^{5/2}t_{n,j}-g(j/n)\longrightarrow0.
\tag{4}
\]
There are no unproved probabilistic local-limit inputs here: (3) and (4) follow by rewriting the factorial ratio as
\[
\frac{(n-1)!}{(n+1)^{n-1}}
\frac{j^{j-2}}{(j-1)!}
\frac{(n+1-j)^{n-j-1}}{(n-j)!}
\]
and using Stirling. At the boundary, the convention for base \(1\) makes the same uniform upper estimate valid after enlarging \(K\).

By (2)--(4), uniformly for \(j/n\) in any compact subset of \((0,1)\),
\[
n^{3/2}\Delta_{n,j}\longrightarrow H(j/n),\qquad
H(x)=\frac{4(1-2x)}{\sqrt{2\pi x(1-x)}}.
\tag{5}
\]
For \(x<1/2\), this is the Riemann-sum limit \(\int_x^{1-x}g(u)\,du\); for \(x>1/2\), apply reflection. Also, (2) and (3) give the uniform endpoint estimate
\[
|\Delta_{n,j}|\le\frac{K'}{n\sqrt{\min(j,n+1-j)}}.
\tag{6}
\]
For any fixed \(0<\varepsilon<1/2\), the bulk contains asymptotically no mass of the rescaled nonnegative kernel: using (4),
\[
n\sum_{\varepsilon n<j<(1-\varepsilon)n}t_{n,j}\to0.
\]
Symmetry and \(\sum_jt_{n,j}=2/(n+1)\) therefore imply the **two boundary masses**
\[
n\sum_{j\le\varepsilon n}t_{n,j}\to1,\qquad
n\sum_{j\ge(1-\varepsilon)n}t_{n,j}\to1.
\tag{7}
\]
The integer inequalities in these sums are interpreted with floors or ceilings; endpoint choices do not affect the limits.

**3. Critical window and boundary contribution.** Assume \(d_n=\sqrt n(p_n-1/2)\to c\). From (1), (4), (5), uniformly on compact bulk intervals,
\[
n^2\bigl(Q_{n,p_n}(j)-1/n\bigr)\to -1+cH(j/n).
\]
Thus the bulk contribution to \(n\sum_j|Q_{n,p_n}(j)-1/n|\) tends to \(\int_{\varepsilon}^{1-\varepsilon}|-1+cH(x)|\,dx\). On either endpoint block, the deviation differs from the nonnegative term \(t_{n,j}/2\) by \(-1/[n(n+1)]+(p_n-1/2)\Delta_{n,j}\). By (6), its total absolute scaled contribution is bounded by \(O(\varepsilon)+O_c(\sqrt\varepsilon)\). Indeed, for the left block,
\[
n\sum_{j\le\varepsilon n}\left|\frac1{n(n+1)}-(p_n-1/2)\Delta_{n,j}\right|
\le O(\varepsilon)+O_c(\sqrt\varepsilon),
\]
and reflection gives the other block. By (7), each endpoint contributes \(1/2\) to the limiting *unhalved* scaled absolute sum. Letting \(\varepsilon\downarrow0\) proves
\[
\lim_n n\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}
=\frac12+\frac12\int_0^1|1-cH(x)|\,dx.
\tag{8}
\]
The integrable endpoint singularities of \(H\) are controlled by (6). Substitute \(x=(1-\cos\theta)/2\). Since \(H(x)=8(2\pi)^{-1/2}\cot\theta\),
\[
\int_0^1|1-cH(x)|dx
=\frac12\int_0^\pi|\sin\theta-8c(2\pi)^{-1/2}\cos\theta|d\theta
=\sqrt{1+32c^2/\pi}.
\]
The final equality follows because the absolute integral of a sinusoid over any interval of length \(\pi\) is twice its amplitude. This establishes the critical-window formula.

**4. Matching the outer regime.** Again (5)--(6), now with an integrable dominating function, imply
\[
\sqrt n\sum_{j=1}^n|\Delta_{n,j}|\to\int_0^1|H(x)|dx=\frac8{\sqrt{2\pi}}.
\tag{9}
\]
By (1) and the triangle inequality, the difference between \(\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}\) and \(\frac12|p_n-1/2|\sum_j|\Delta_{n,j}|\) is at most \(\|Q_{n,1/2}-U_n\|_{\mathrm{TV}}\le1/(n+1)\); the last bound follows by summing the positive and negative pieces of \(b_{n,j}\) in (1). If \(\sqrt n|p_n-1/2|\to\infty\), this error is negligible after multiplication by \(\sqrt n/|2p_n-1|\). Formula (9) proves the outer-scale assertion.

## Verification

The included `check.py` evaluates the exact tree-count kernel, its reflection and cancellation identities, and the complete finite preference distribution using exact rational arithmetic. It also independently enumerates every preference vector and every random search branch for small parking lots, checking the conditional law against the counting formula. The program reports 790 exact assertions passed (for the recorded run), plus optional floating-point asymptotic diagnostics at increasing sizes. The diagnostics approach \(1\), \(\sqrt{2/\pi}\), and \((1+\sqrt{1+32/\pi})/2\), respectively. Exact finite tests do not prove any infinite-size limit; those follow from the Stirling estimate and mass decomposition above.

Reproduction: `python3 check.py`. The exact tests use only the Python standard library; optional large-size diagnostics use NumPy and SciPy.

## Relationship to prior work

Tian and Treviño introduced the forward/backward random-direction parking model and established the overall success count. Durmić, Han, Harris, Ribeiro and Yin derived the exact conditional last-preference formula, its symmetry, and the rates \(\Theta(1/n)\) at \(p=1/2\) and \(\Theta(1/\sqrt n)\) for fixed \(p\ne1/2\). These exact laws and order bounds are **inputs, not new findings**. Bellin's classical-parking TV estimate concerns \(p=1\) and does not supply the displayed sharp constant or its varying-bias crossover. Harris, Ribeiro and Yin subsequently studied general \((m,n)\)-parking and different asymptotics when the occupancy fraction stays strictly below one; the analyzed inequalities do not state the present \(m=n\) critical-window limit.

The additional result here is the **sharp crossover profile** for \(p-1/2\) of order \(n^{-1/2}\), including its exact constant and matching outer asymptotic. The profile arises from two endpoint atoms and a signed continuous bulk perturbation; its square-root form is not obtained by merely substituting into the previously known \(\Theta\)-estimates.

## Limitations

The result concerns only the last original preference conditional on **complete success** under the specified one-coin direction protocol. It does not establish joint laws of multiple preferences, exact finite-size TV formulas, or behavior under other parking dynamics. No assertion of historical priority beyond the inspected primary literature and query results is made. The exact kernel is prior work, and independent mathematical validation has not been performed.

## References

1. M. Tian and E. Treviño, *Generalizing Parking Functions with Randomness*, arXiv:2111.12850v1 (2021), section 2. https://arxiv.org/abs/2111.12850
2. I. Durmić, A. Han, P. E. Harris, R. Ribeiro, and M. Yin, *Probabilistic Parking Functions*, arXiv:2211.00536v1 (2022); Electronic Journal of Combinatorics 30(3), P3.18 (2023), Theorems 3, 5, 6 and equations (2.20), (2.35). https://arxiv.org/abs/2211.00536
3. E. Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, arXiv:2108.08661v1 (2021), Theorem 1. https://arxiv.org/abs/2108.08661
4. P. E. Harris, R. Ribeiro, and M. Yin, *Probabilistic (m,n)-Parking Functions*, arXiv:2502.00269v1 (2025), section 3. https://arxiv.org/abs/2502.00269
