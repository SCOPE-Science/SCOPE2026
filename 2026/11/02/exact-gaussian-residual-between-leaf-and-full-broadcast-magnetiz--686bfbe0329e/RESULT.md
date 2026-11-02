# Exact Gaussian residual between leaf and full broadcast magnetizations

## Finding
Let \(T_n\) be a uniform random recursive tree with vertices \(1,\ldots,n\): vertex \(j\ge2\) independently chooses a uniformly random parent among \(1,\ldots,j-1\). The root has spin \(B_1=+1\). Each new child independently copies its parent's spin with probability \(1-q\) and reverses it with probability \(q\), where \(0\le q<1\). Write
\[
t=1-2q\in(-1,1],\quad X_n=\sum_{v=1}^{n}B_v,\quad
Y_n=\sum_{v\text{ a leaf of }T_n}B_v,\quad
Z_n=Y_n-\frac{t}{1+t}X_n.
\]
Here a leaf means a vertex with no children, and the sum \(Y_n\) is defined using the tree at time \(n\), not the set of vertices that were leaves at birth.

**Theorem.** For every such fixed \(t\) and all integers \(n\ge3\),
\[
\mathbb E Z_n=0,\qquad
\mathbb E Z_n^2=\frac{3-t^2}{6(1+t)^2}\,n.
\tag{1}
\]
Moreover, with \(\sigma_t^2=(3-t^2)/(6(1+t)^2)>0\),
\[
\frac{Z_n}{\sqrt n}\ \xrightarrow{\ d\ }\ N(0,\sigma_t^2).
\tag{2}
\]
If \(1/2<t\le1\), there is an almost-sure and \(L^2\) limit \(W_t=\lim_{n\to\infty}n^{-t}X_n\), and the stronger joint convergence holds:
\[
\left(n^{-t}X_n,\ n^{-1/2}Z_n\right)
\xrightarrow{\ d\ }(W_t,G_t),\qquad
G_t\sim N(0,\sigma_t^2),\quad G_t\perp W_t.
\tag{3}
\]
Thus leaf magnetization has a \(\sqrt n\)-scale Gaussian fluctuation *after its known leading full-magnetization mode has been subtracted*, even when that mode itself has a larger, non-Gaussian scale. At the threshold \(t=1/2\), (1) implies \(Z_n/\sqrt{n\log n}\to0\) in \(L^2\), while \(\mathbb E X_n^2=nH_n\).

## Assumptions and scope
All probabilities jointly average over independent recursive parent choices and independent edge-copying signs. The initial root spin is fixed to \(+1\); a fair random initial spin only multiplies both magnetizations by a common independent sign and leaves (1) and (2) unchanged. The parameter \(q\) is fixed as \(n\) grows. The endpoint \(q=1\) is excluded because the coefficient \(t/(1+t)\) is singular. Equations (1) and (2) hold also for predominant reversals, \(q>1/2\). Equation (3) only asserts independence in the superdiffusive regime \(t>1/2\).

## Proof
Let \(\mathcal F_n\) contain the tree and spins observed after \(n\) arrivals. Given \(\mathcal F_n\), choose \(U\) uniformly in the existing vertices and independently choose \(\zeta\in\{-1,+1\}\) with \(\mathbb E\zeta=t\). Let \(I\) be the indicator that \(U\) is currently a leaf. The new spin is \(\zeta B_U\), so the exact updates are
\[
\Delta X_n=\zeta B_U,\qquad
\Delta Y_n=(\zeta-I)B_U,\qquad
\Delta Z_n=\left(\frac{\zeta}{1+t}-I\right)B_U.
\tag{4}
\]
In particular, \(\mathbb E[\Delta Z_n\mid\mathcal F_n]=-Z_n/n\). Thus \(M_n=(n-1)Z_n\), \(n\ge2\), is a mean-zero martingale: at \(n=2\), \(Z_2=(\zeta-t)/(1+t)\), whose expectation vanishes. Also, for \(L_n\), the number of leaves,
\[
\mathbb E L_n=n/2\quad(n\ge2),
\qquad
\mathbb E[(\Delta Z_n)^2\mid\mathcal F_n]
=\frac1{(1+t)^2}+\frac{1-t}{1+t}\frac{L_n}{n}.
\tag{5}
\]
Indeed, \(L_2=1\), and \(L_{n+1}=L_n+1-I\) gives \(\mathbb E[L_{n+1}\mid\mathcal F_n]=L_n+1-L_n/n\). Squaring \(Z_{n+1}=Z_n+\Delta Z_n\) now yields
\[
\mathbb E Z_{n+1}^2
=\left(1-\frac2n\right)\mathbb E Z_n^2
+\underbrace{\left(\frac1{(1+t)^2}+\frac{1-t}{2(1+t)}\right)}_{K_t=(3-t^2)/(2(1+t)^2)}
\quad(n\ge2).
\tag{6}
\]
At \(n=2\) the multiplier of the old second moment is zero; hence \(\mathbb E Z_3^2=K_t\). Equation (6) gives \(\mathbb E Z_n^2=K_t n/3\) by induction for every \(n\ge3\), proving (1). This calculation does not rely on a limiting approximation.

For the central limit theorem, the increments of \(M_n\) are
\[
M_{j+1}-M_j=Z_j+j\Delta Z_j,
\qquad
\mathbb E[(M_{j+1}-M_j)^2\mid\mathcal F_j]
=j^2\left[\frac1{(1+t)^2}
+\frac{1-t}{1+t}\frac{L_j}{j}
-\left(\frac{Z_j}{j}\right)^2\right].
\tag{7}
\]
The parent choices are independent. Altering one parent choice can change the terminal leaf count at only its two possible parent vertices, so the bounded-differences variance bound gives \(\operatorname{Var}(L_j)=O(j)\). Combined with \(\mathbb E L_j=j/2\), this shows \(L_j/j\to1/2\) in \(L^2\). Equation (1) also gives \(\mathbb E(Z_j/j)^2=O(1/j)\). Weighted averaging in (7) therefore establishes
\[
\frac1{n^3}\sum_{j=2}^{n-1}
\mathbb E[(M_{j+1}-M_j)^2\mid\mathcal F_j]
\ \xrightarrow{\mathbb P}\ \frac{K_t}{3}=\sigma_t^2.
\tag{8}
\]
For fixed \(t>-1\), \(|Z_j|\le C_tj\) and \(|\Delta Z_j|\le C_t\), so the largest martingale increment divided by \(n^{3/2}\) is deterministically \(O_t(n^{-1/2})\). The martingale Lindeberg condition follows. The martingale central limit theorem, (8), and \(Z_n=M_n/(n-1)\) prove (2).

For the joint claim, write
\[
\mu_n=\prod_{j=1}^{n-1}\left(1+\frac tj\right)
=\frac{\Gamma(n+t)}{\Gamma(1+t)\Gamma(n)}.
\]
The process \(X_n/\mu_n\) is a martingale, with its successive conditional-variance contributions bounded by \(\mu_{n+1}^{-2}\). If \(t>1/2\), the sum of these contributions is finite, so this martingale converges almost surely and in \(L^2\). Since \(\mu_n/n^t\to1/\Gamma(1+t)\), this proves the existence of \(W_t\). Furthermore, the martingale CLT above is stable with respect to the entire fixed-time history: conditioning on any \(\mathcal F_m\) removes only finitely many increments and does not change (8), while subsequent increments satisfy the same Lindeberg condition. Approximation of bounded \(\mathcal F_\infty\)-measurable random variables by their \(\mathcal F_m\)-conditional expectations upgrades this to stable normal convergence. As \(W_t\) is \(\mathcal F_\infty\)-measurable, (3) follows. Finally, from (1), \(\mathbb E[(n^{-t}Z_n)^2]=\sigma_t^2 n^{1-2t}\to0\) when \(t>1/2\). At \(t=1/2\), the exact recurrence \(\mathbb E X_{n+1}^2=(1+1/n)\mathbb E X_n^2+1\), starting at one, yields \(\mathbb E X_n^2=nH_n\); (1) gives the claimed smaller residual scale.

## Verification
The standalone `checker.py` enumerates every parent-choice sequence and every nonzero-probability edge-sign sequence, for \(2\le n\le7\) and seven exact rational values \(t\in\{-3/4,-1/2,0,1/3,1/2,3/4,1\}\). Independently of the preceding moment recursion, it computes tree/spin outcomes, their exact rational weights, (1), the leaf/full mean identity, and the full one-step conditional drift and square identity by explicit next-step enumeration. It reports **5,622 exact rational assertions passed**. These calculations are checks of finite identities, not evidence replacing the martingale central limit proof or proving priority.

## Relationship to prior work
Addario-Berry, Devroye, Lugosi and Velona (2020; [1]) introduce and analyze broadcasting and leaf-only majority on recursive trees. Desmarais, Holmgren and Wagner (2023; [2], Theorems 2.1 and 2.4) give separate leading laws for total and leaf color counts, and in the superdiffusive regime identify their shared leading random amplitude. In the uniform-attachment case those results already imply the leading ratio \(Y_n/X_n\sim t/(1+t)\) in the appropriate normalized sense; this is **not** claimed as new. Their separate leading laws do not supply the exact every-size residual variance (1) or the \(\sqrt n\)-Gaussian correction independent of the dominant random amplitude in (3). Althaus, Hartung and Steiner (2024; [3]) examine majority reconstruction through recursive walks and urns, but not this corrected leaf observable. General multitype urn limit theory [4] is a possible route to (2) and remains a background-source priority risk; the exact finite identity (1) does not follow from a limit theorem alone.

## Limitations
The proof depends on uniform recursive attachment and independent binary transmission with fixed \(q<1\). It does not establish the same coefficient for degree-biased preferential attachment or multi-parent graphs. The Gaussian limit is for the *linear residual* and is not a claim about classification-error probabilities or independence of leaf and full votes at finite \(n\). The joint independence statement is restricted to \(t>1/2\), not the diffusive regime. Historical priority and independent mathematical validation have not been established.

## References
[1] L. Addario-Berry, L. Devroye, G. Lugosi, V. Velona, *Broadcasting on random recursive trees*, arXiv:2006.11787, first posted 2020-06-21. https://arxiv.org/abs/2006.11787

[2] C. Desmarais, C. Holmgren, S. Wagner, *Broadcasting-induced colorings of preferential attachment trees*, Random Structures & Algorithms 63 (2023), 364–405; online 2023-02-23. https://doi.org/10.1002/rsa.21142

[3] E. Althaus, L. Hartung, R. Steiner, *A Random Walk Approach to Broadcasting on Random Recursive Trees*, arXiv:2405.04385, first posted 2024-05-07. https://arxiv.org/abs/2405.04385

[4] S. Janson, *Functional limit theorems for multitype branching processes and generalized Pólya urns*, Stochastic Processes and their Applications 110 (2004), 177–245. https://doi.org/10.1016/j.spa.2003.12.002
