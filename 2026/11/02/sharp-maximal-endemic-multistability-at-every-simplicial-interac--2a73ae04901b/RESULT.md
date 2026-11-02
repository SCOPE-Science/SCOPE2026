# Sharp maximal endemic multistability at every simplicial interaction order

## Finding
For every integer \(M\geq2\), consider the continuous-time, homogeneous complete-simplicial SIS mean-field equation
\[
\dot x=x\left[(1-x)\sum_{j=1}^{M}\frac{s_j}{j!}x^{j-1}-1\right],\qquad 0\leq x\leq1,\quad s_j>0.
\]
The recovery rate is normalized to one; \(s_j\) is the positive scaled infection pressure at simplex order \(j\). There are at most \(M\) positive endemic equilibria and at most \(\lceil M/2\rceil\) locally asymptotically stable positive endemic equilibria. Both bounds are simultaneously sharp **for every \(M\)**. Indeed, for every \(\eta>0\), rates can be chosen with \(\left|s_j/j!-1\right|<\eta\) for all \(j\), producing exactly \(M\) distinct hyperbolic endemic equilibria in \((0,1)\), of which exactly \(\lceil M/2\rceil\) attract. This maximal configuration persists throughout a nonempty open set of strictly positive infection-rate vectors.

## Assumptions and scope
The equation is the *deterministic homogeneous mean-field limiting equation*, obtained from the source's complete simplicial complex by retaining every interaction order \(1,\ldots,M\). The source writes its equivalent polynomial form as equation (II.31), with scaled rates \(s_j\) and recovery \(\gamma\); here \(\gamma=1\). This statement does not assert positive stationary endemic distributions for any finite-population stochastic SIS chain, which has an absorbing all-susceptible state. The integer \(M\) is fixed while taking the homogeneous population limit; it is not the population size. All \(s_j\) must be strictly positive, including the pairwise and every intermediate simplex order.

## Proof
**Upper bounds.** Put \(P(x)=\sum_{j=1}^M(s_j/j!)x^{j-1}\) and \(f(x)=(1-x)P(x)-1\), so \(\dot x=xf(x)\). Since the leading coefficient of \(f\) is \(-s_M/M!\neq0\), \(f\) has degree exactly \(M\). Therefore at most \(M\) distinct endemic equilibria occur in \((0,1)\). If \(k\) distinct endemic equilibria are locally asymptotically stable, the scalar vector field is positive immediately to the left and negative immediately to the right of each. Between any two consecutive stable equilibria, continuity therefore forces another distinct equilibrium. Thus there are at least \(2k-1\) distinct endemic roots, and \(k\leq\lceil M/2\rceil\). This argument also covers nonhyperbolic attracting roots.

**Constructive sharpness.** Fix any \(\eta>0\) and choose a positive rational \(\varepsilon<\min\{1/8,\eta/4\}\). Define
\[
K=M-1,\qquad \delta=\frac{\varepsilon}{4(2M)^K},\qquad
Q(x)=\prod_{j=1}^{K}\left(x-\frac{j\delta}{M}\right),\qquad
P(x)=\sum_{j=0}^{K}x^j+\varepsilon Q(x).
\]
Write \(P(x)=\sum_{j=0}^{K}\lambda_jx^j\), then choose \(s_{j+1}=(j+1)!\lambda_j\) for \(0\leq j\leq K\). Since each root of \(Q\) is positive and below \(\delta\), the sum of the absolute values of all coefficients of \(Q\) is \(\prod_{j=1}^K(1+j\delta/M)\leq e^{K\delta}<e^{1/32}<2\). Consequently \(\lvert\lambda_j-1\rvert<2\varepsilon<\min\{1/4,\eta\}\); in particular all infection rates are strictly positive.

The geometric-sum identity yields the exact factorization
\[
f(x)= -x^M+\varepsilon(1-x)Q(x).
\]
Take the \(M\) rational test points
\[
t_j=\frac{(j+1/2)\delta}{M},\qquad j=0,\ldots,K.
\]
They are all in \((0,\delta)\), and \(Q(t_j)\) has sign \((-1)^{K-j}\). Moreover, every factor \(\lvert t_j-k\delta/M\rvert\) is at least \(\delta/(2M)\). Therefore
\[
\frac{\left|\varepsilon(1-t_j)Q(t_j)\right|}{t_j^M}
\geq \frac{\varepsilon(1-\delta)(\delta/(2M))^K}{\delta^M}
=4(1-\delta)>1.
\]
Hence \(f(t_j)\) has the alternating sign \((-1)^{K-j}\). Since \(Q(t_K)>0\), \(f(t_K)>0\), whereas \(f(1)=-1<0\). The intermediate value theorem gives a different root of \(f\) in every one of the \(K\) intervals \((t_j,t_{j+1})\) and one more in \((t_K,1)\). These are \(M\) distinct interior roots. A degree-\(M\) polynomial cannot have further roots, and all \(M\) are simple.

**Attractor count and robustness.** Across each simple root the sign changes. For odd \(M\), the first interior root is attracting and the roots alternate in stability; for even \(M\), the first interior root is repelling and the roots again alternate. In both cases precisely \(\lceil M/2\rceil\) endemic roots are locally asymptotically stable. Their simplicity and location in \((0,1)\) persist by continuity of polynomial roots under sufficiently small perturbations of every rate; all positive rates also remain positive. In particular there is an open positive-rate region realizing the sharp count. For even \(M\) the disease-free equilibrium is also attracting, while for odd \(M\) it is repelling; this distinction does not affect the endemic count.

## Verification
The standalone standard-library script `verify.py` performs exact rational-polynomial calculations for each \(2\leq M\leq12\). It checks positivity and near-unit normalization of every rate, all \(M\) alternating test-point signs, the negative right boundary, and exact agreement with the source equation (II.31), using \(s_j=j!\lambda_{j-1}\). Its concrete rational choice is \(\varepsilon=1/8\) and \(\delta=1/[32(2M)^{M-1}]\); the proof above allows any smaller positive rational \(\varepsilon\). The software checks sample orders only; the displayed uniform inequalities establish the theorem for every \(M\).

Reproduce with `python3 verify.py` (Python 3.9 or later; no third-party packages).

## Relationship to prior work
Kiss–Iacopini–Simon–Georgiou (2023), equations (II.30)–(II.31), derives the all-order complete-simplicial mean-field polynomial and analyzes the 2- and 3-simplex cases in detail. Its discussion explicitly anticipates the possibility of arbitrarily many distinct endemic stationary states at higher order without establishing a realizability theorem or a sharp stable-state count. The present result gives a constructive all-order answer, exact upper bounds, strictly positive rates at every order, and robustness. It does not reprove the stochastic-to-mean-field limiting theorem.

Iacopini–Petri–Barrat–Latora (2018/2019) gives the related general homogeneous mean-field polynomial but explicitly analyzes the triangle case and particular single-higher-order specializations. Ferraz de Arruda–Petri–Rodriguez–Moreno (2021/2023) finds multistability in community-structured hypergraphs under a different group-activation rule; its network-dependent mechanisms do not furnish the claimed complete-structure sharp bound. Liang–Cui–Liu (2024) studies a discrete-time, networked SIS class and sufficient stability conditions, not this continuous-time complete-structure optimal equilibrium count. These are comparisons of the implications of inspected statements, not claims that a search establishes priority.

## Limitations
The conclusion concerns deterministic equilibria in a scalar infinite-population mean-field model; finite stochastic populations eventually reach the absorbing disease-free state. The constructed endemic equilibria can be close together and their parameter neighborhoods can be small, so finite-size observations or noisy parameter fitting need not distinguish all branches. The theorem does not extend unaltered to heterogeneous, temporally varying, or discrete-time networks. Bibliographic searches do not exclude an equivalent unindexed construction; no independent review has been performed.

## References
1. I. Z. Kiss, I. Iacopini, P. L. Simon, N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752v1, first posted 2023-09-22, especially equation (II.31) and Section IV. https://arxiv.org/abs/2309.12752
2. I. Iacopini, G. Petri, A. Barrat, V. Latora, *Simplicial models of social contagion*, arXiv:1810.07031v1, first posted 2018-10-16; Nature Communications 10, 2485 (2019), especially the mean-field and supplementary general-order analyses. https://arxiv.org/abs/1810.07031
3. G. Ferraz de Arruda, G. Petri, P. M. Rodriguez, Y. Moreno, *Multistability, intermittency, and hybrid transitions in social contagion models on hypergraphs*, arXiv:2112.04273v1; Nature Communications 14, 1375 (2023). https://arxiv.org/abs/2112.04273
4. L. Liang, S. Cui, F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602v1, first posted 2024-08-16, particularly Section 6. https://arxiv.org/abs/2408.08602
