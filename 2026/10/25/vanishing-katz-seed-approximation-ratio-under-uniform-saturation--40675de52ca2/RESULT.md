# Vanishing Katz-seed approximation ratio under uniform saturation and feedback

## Finding
For every integer \(k\ge 4\), there is a strongly connected nonnegative weighted digraph with \(k+3\) vertices in which choosing one initial seed by maximum outgoing Katz centrality for discount \(1/2\) achieves at most
\[
\frac{4}{k}+\frac{k+1}{50k^4}
\]
times the best single-seed discounted influence under a unit-clipped general information propagation (GIP) process. This bound vanishes as \(k\to\infty\). The phenomenon does not require a positive activation threshold: uniform upper saturation and recurrent high-gain walks suffice. The claim concerns the Katz choice itself, not algorithms that optimize or locally improve that choice.

## Assumptions and scope
Fix any integer \(k\ge4\). The vertex set is \(V_k=\{a_0,a_1,b,\ell_1,\ldots,\ell_k\}\), and the **only** nonzero arc weights, in source-to-target orientation, are
\[
W_{a_0a_1}=W_{a_1a_0}=w=2-\frac{1}{4k},\qquad
W_{a_0b}=W_{\ell_i a_0}=\varepsilon=\frac{1}{100k^3},\qquad
W_{b\ell_i}=1\quad(1\le i\le k).
\]
Each vertex can reach each other vertex, since the cycle on \(a_0,a_1\) connects to \(b\) and to every leaf, and every leaf points back to \(a_0\). Thus the weighted directed network is strongly connected with strictly positive weights on its arcs. All non-arc entries are zero.

The unique initial seed \(v\) has state \(x_v(0)=1\), and all other coordinates have state zero. At every integer \(t\ge1\), the process updates synchronously as
\[
x_j(t)=\min\left\{1,\sum_{i\in V_k}W_{ij}x_i(t-1)\right\},\qquad
S(v)=\sum_{t=1}^{\infty}2^{-t}\sum_{j\in V_k}x_j(t).
\]
This is equation (7) of Tian--Lambiotte's general bounded-linear GIP system with \(l_{j,t}=0\), \(h_{j,t}=1\) for \(t\ge1\), and permissible initial states \(l_{j,0}=h_{j,0}=1\) for every vertex. The model is a specialization of the *general* GIP equation, not of the paper's narrower later choice of parametric, time-dependent thresholds. All sums \(S(v)\) converge because every state belongs to \([0,1]\).

The outgoing Katz/EIC influence of a seed is
\[
c_v=\sum_{t=1}^{\infty}2^{-t}\sum_{j\in V_k}(W^t)_{vj}
=\left[\bigl(I-\tfrac12W\bigr)^{-1}\mathbf 1-\mathbf 1\right]_v.
\]
The spectral-radius condition required for this resolvent is verified below. Because every initial seed amplitude is one, maximizing \(c_v\) is exactly the single-seed EIC criterion studied in the cited source. Orientation matters: it is the outgoing resolvent row sum, not the incoming Katz score.

## Proof
Let \(\alpha=w/2=1-1/(8k)\) and \(e=\varepsilon/2=1/(200k^3)\). The nonnegative irreducible matrix \(W/2\) has Perron root \(\lambda>0\). The right eigenvector equations, using the leaf symmetry, are
\[
\lambda u_{a_0}=\alpha u_{a_1}+e u_b,\quad
\lambda u_{a_1}=\alpha u_{a_0},\quad
\lambda u_b=\frac{k}{2}u_\ell,\quad
\lambda u_\ell=e u_{a_0}.
\]
Consequently \(\lambda^3-\alpha^2\lambda-ke^2/2=0\). The polynomial has exactly one positive root, by a single change of sign in its ordered coefficients (or by its single positive local-minimum structure). Furthermore,
\[
1-\alpha^2-\frac{k e^2}{2}
=\frac{1}{4k}-\frac{1}{64k^2}-\frac{1}{80000k^5}
>\frac{1}{8k}>0
\]
for \(k\ge4\). Therefore \(\lambda<1\), so the outgoing Katz series converges.

The Katz scores satisfy the exact positive walk recursions
\[
\begin{aligned}
c_{a_0}&=\alpha(1+c_{a_1})+e(1+c_b),\\
c_{a_1}&=\alpha(1+c_{a_0}),\\
c_b&=\frac{k}{2}(1+c_\ell),\\
c_\ell&=e(1+c_{a_0}).
\end{aligned}
\]
Solving these gives
\[
c_{a_0}=\frac{\alpha+\alpha^2+e(1+k/2)+ke^2/2}{1-\alpha^2-ke^2/2}.
\]
For all \(k\ge4\), the numerator is smaller than \(3\), and the denominator exceeds \(1/(8k)\). Hence \(c_{a_0}<24k\), and
\[
c_b=\frac{k}{2}\bigl(1+e(1+c_{a_0})\bigr)
<\frac{k}{2}\left(1+\frac{1+24k}{200k^3}\right)<k,
\qquad
c_\ell=e(1+c_{a_0})<1.
\]
On the other hand, every walk alternating along the two-way \(a_0,a_1\) pair contributes to the Katz score from either starting vertex. In particular,
\[
c_{a_0},c_{a_1}\ge \sum_{t\ge1}\alpha^t=\frac{\alpha}{1-\alpha}=8k-1>k.
\]
Thus **every** outgoing Katz maximizer lies in the two-vertex set \(\{a_0,a_1\}\), regardless of how ties are broken.

If the only initial seed is either \(a_0\) or \(a_1\), the unit cap yields \(x_{a_0}(t),x_{a_1}(t)\le1\). Because only \(a_0\) sends to \(b\), we have \(x_b(t)\le\varepsilon\) for every \(t\ge1\). Each \(\ell_i\) is reached only from \(b\), so \(x_{\ell_i}(t)\le\varepsilon\) for every \(t\ge1\) (in fact zero at \(t=1\)). Therefore every Katz-maximizing seed satisfies
\[
S(v)\le\sum_{t\ge1}2^{-t}\bigl[2+(k+1)\varepsilon\bigr]
=2+(k+1)\varepsilon.
\]
Alternatively, if the initial seed is \(b\), every \(\ell_i\) has state exactly one at \(t=1\), since \(W_{b\ell_i}=1\). In particular \(S(b)\ge k/2\), and the true one-seed optimum obeys \(S_{\mathrm{opt}}\ge S(b)\). Combining the bounds gives, simultaneously for all Katz-maximizing seeds,
\[
\frac{S(v)}{S_{\mathrm{opt}}}\le\frac{2+(k+1)/(100k^3)}{k/2}
=\frac4k+\frac{k+1}{50k^4}\longrightarrow0.
\]
This establishes the claimed absence of any uniform positive Katz approximation ratio on the specified family. \(\square\)

## Verification
The self-contained script `check.py` uses exact rational arithmetic. Executing `python3 check.py` independently checks the Katz recursions, strict score separation, the rational inequalities above and exact 48-step clipped trajectories for \(k=4,8,16,32\). The finite trajectories are checks rather than a replacement for the all-integer and infinite-time proof: the latter follows entirely from the uniform state bounds and algebraic inequalities. The largest of the four displayed theoretical ratio bounds falls from approximately \(1.00039\) at \(k=4\) to approximately \(0.125\) at \(k=32\).

## Relationship to prior work
Tian and Lambiotte (arXiv:2112.01465, first public version 2 December 2021), equations (2), (7) and (16), and Theorem 6, define the discounted nonlinear GIP objective and show that outgoing Katz-based selection is **exact** for its linear EIC endpoint. Their Sections V.2.1--V.2.2 compare Katz initialization numerically with nonlinear influence-optimization methods. Those statements do not provide a positive approximation guarantee for the capped nonlinear case, nor an analytical zero-ratio counterfamily. The present construction gives a sharp qualitative separation: arbitrarily high discounted linear walk reinforcement on two mutually linked nodes contributes little after unit saturation, while a one-step broadcast from \(b\) produces influence proportional to \(k\).

Bilmes and Bai (arXiv:1701.08939) develop general submodularity properties of multilayer nonnegative weighted systems with concave activations (including saturation). Those general structural facts concern diminishing marginal returns, not performance of the **Katz-centrality heuristic** versus direct nonlinear influence maximization. The result is not a claim of new submodularity or new convergence theory.

## Limitations
The approximation bound is specific to one seed, discount \(1/2\), the explicit weighted and strongly connected directed family, and the uniform, nonpersistent, synchronous capped GIP process. Edge weights vary with graph size; the strong two-cycle has weights close to two, so this is not a statement about row-stochastic or bounded-weight-below-one networks. The theorem does not assess the paper's customized direct-search algorithm, probabilistic independent cascades, positive lower activation thresholds, or continuous-time models. The analytic family demonstrates possible worst-case failure, not its empirical prevalence. Broader influence-heuristic literature may contain an equivalent worst-case phenomenon in another parameterization; this remains a bibliographic risk pending independent specialist assessment.

## References
1. Yu Tian and Renaud Lambiotte, *Unifying information propagation models on networks and influence maximization*, arXiv:2112.01465 (v1, 2021-12-02; full text v3, 2022), https://arxiv.org/html/2112.01465v3.
2. Jeffrey Bilmes and Wenruo Bai, *Deep Submodular Functions*, arXiv:1701.08939v1 (2017-01-31), https://arxiv.org/html/1701.08939v1.
