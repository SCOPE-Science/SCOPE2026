# Uniform coexistence compositions for sparse peripheral opinions in a star voter model

## Finding
Consider a population of \(n\) agents with opinions at the vertices of a star: a hub \(H\) and \(d\) mutually incompatible peripheral opinions. Suppose initially one agent holds each peripheral opinion and the other \(n-d\) hold the hub opinion. For any integers \(d\ge2\), \(n\ge d+1\), and any positive integers \(\ell_1,\ldots,\ell_d\) satisfying \(\sum_i\ell_i=n\), the probability that the final absorbing configuration has no hub agents and precisely \(\ell_i\) agents of peripheral opinion \(i\) is

\[
\Pr\{L=(\ell_1,\ldots,\ell_d)\}
=\frac{(n-d)!(2d-1)!}{(n+d-1)!}.
\]

Thus **every positive terminal composition has exactly the same unconditioned probability**, independent of its balance. In particular, writing \(E\) for the event that *all* \(d\) peripheral opinions survive,

\[
\Pr(E)=\binom{n-1}{d-1}\frac{(n-d)!(2d-1)!}{(n+d-1)!}
=\frac{(2d-1)!(n-1)!}{(d-1)!(n+d-1)!}.
\]

Conditional on \(E\), the terminal count vector is uniform on the \(\binom{n-1}{d-1}\) positive integer compositions of \(n\). For each fixed \(d\), as \(n\to\infty\),

\[
\Pr(E)\sim\frac{(2d-1)!}{(d-1)!}\,n^{-d},\qquad
(L_1/n,\ldots,L_d/n)\mid E\ \xrightarrow{\mathrm{law}}\ \operatorname{Dirichlet}(1,\ldots,1).
\]

For illustration, with \(d=3\) and \(n=7\), each of the fifteen positive terminal compositions has probability \(1/126\), so the joint-survival probability is \(5/42\).

## Assumptions and scope
An unordered pair of distinct agents is selected uniformly from all pairs; if their opinions are adjacent in the star, one of the two (chosen fairly) adopts the other's opinion. Otherwise nothing changes. This is the ordinary EdgeVOG rule on a complete communication graph; its non-idle subsequence is the productive EdgeVOG chain and has the same absorption law. Each opinion disappears permanently when its count first reaches zero. The terminal state consists either of the hub opinion alone or of a subset of mutually incompatible peripheral opinions. The theorem describes terminal states in which **every** initial peripheral opinion survives, not the distribution after one or more peripheral extinctions.

The parameters are arbitrary finite integers \(d\ge2\), \(n\ge d+1\), with exactly one initial agent per peripheral opinion. Terminal peripheral counts are labeled by opinion, rather than treated as unlabeled partitions.

## Proof
Let \(X_i\) count agents holding peripheral opinion \(i\), let \(s=\sum_iX_i\), and write \(Y=n-s\) for the hub count. While \(0<s<n\), every productive interaction joins the hub to a peripheral opinion, and the total number of compatible unordered pairs is \(Ys\). Exactly \(YX_i\) such pairs involve opinion \(i\), and conditional on choosing one such pair either endpoint copies the other with probability \(1/2\). Consequently the embedded productive chain has transition probabilities

\[
\Pr\{X\mapsto X+e_i\mid X\}=
\Pr\{X\mapsto X-e_i\mid X\}=\frac{X_i}{2s}.
\tag{1}
\]

Set \(h(x)=\prod_{i=1}^{d}x_i\). The product is harmonic for (1) in the interior: the two opposite transitions in any coordinate have equal probability and change the product by equal and opposite amounts. Extend \(h=0\) whenever a peripheral opinion becomes extinct. At a terminal all-peripheral configuration, \(h(L)=\prod_iL_i\); at any other terminal configuration, \(h=0\). Since the state space is finite and the chain absorbs almost surely, the bounded harmonic function determines a Doob transform up to absorption, beginning at \(x_0=(1,\ldots,1)\) with \(h(x_0)=1\).

At a state \(x_i\ge1\) for every \(i\), the transformed transition probabilities become

\[
P^h(x,x+e_i)=\frac{x_i+1}{2s},\qquad
P^h(x,x-e_i)=\frac{x_i-1}{2s}.
\tag{2}
\]

These sum to one, and the transformation prohibits peripheral extinction. The total peripheral count moves up with probability \((s+d)/(2s)\) and down with probability \((s-d)/(2s)\), independently of the vector of peripheral counts. At \(s=d\), a down-move has zero probability. Thus the transformed total-size chain is a finite birth-death chain which reaches the absorbing level \(n\) almost surely.

For clarity, conditional on a *given trajectory of total counts* in the transformed chain, the composition at level \(s=d+t\) has the Dirichlet–multinomial law with \(t\) trials and parameters \((2,\ldots,2)\), translated by one in each coordinate. This follows by induction on the number of up and down steps. If \(T_i=X_i-1\), conditional on an upward step, (2) chooses type \(i\) with probability \((T_i+2)/(t+2d)\), which is exactly the Pólya-urn addition rule for Dirichlet–multinomial parameters two. Conditional on a downward step, (2) chooses type \(i\) with probability \(T_i/t\), the uniformly random deletion rule; deleting one of \(t\) exchangeable Pólya-urn draws preserves the Dirichlet–multinomial family with \(t-1\) draws. The conditional probabilities of the up/down decisions depend on \(s\) alone, so conditioning on the total-size path does not change these identities. Initially \(t=0\), giving the base case.

At terminal total \(n\), writing \(t=n-d\) and \(t_i=\ell_i-1\), the transformed terminal distribution is therefore

\[
\begin{aligned}
\Pr^h\{L=\ell\}
&=\frac{t!\,\Gamma(2d)}{\Gamma(t+2d)}
\prod_{i=1}^{d}\frac{\Gamma(t_i+2)}{\Gamma(2)t_i!}\\
&=\frac{(n-d)!(2d-1)!}{(n+d-1)!}\prod_i\ell_i.
\end{aligned}
\tag{3}
\]

The terminal Doob-change-of-measure formula is
\(\Pr^h\{L=\ell\}=\Pr\{L=\ell\}h(\ell)/h(x_0)=\Pr\{L=\ell\}\prod_i\ell_i\). Cancelling the positive product in (3) proves the uniform-per-composition formula. There are exactly \(\binom{n-1}{d-1}\) positive compositions. Summing yields the joint-survival formula. Finally, for fixed \(d\), the factorial ratio gives the stated \(n^{-d}\) asymptotic and uniform lattice points on the positive composition simplex converge under scaling by \(n\) to the uniform simplex law, namely Dirichlet with all parameters one.

## Verification
The standalone `verify.py` constructs the **original productive chain** directly from (1), rather than using the Doob transform or the Dirichlet–multinomial formula. For each pair \((d,n)\), it enumerates all positive transient peripheral-count states below total \(n\) and all positive terminal compositions at total \(n\), sets the probability of subsequently achieving full coexistence to zero after any peripheral count vanishes, and solves the finite absorbing-chain linear systems exactly over rational numbers. It compares each terminal probability individually with the factorial formula.

The program passed thirteen parameter pairs, including \((d,n)=(2,7),(3,8),(4,7),(5,7)\), covering 114 terminal probabilities with exact rational arithmetic. Example results: \((3,7)\) has 15 terminal compositions, each probability \(1/126\); \((4,7)\) has 20, each probability \(1/120\). Finite enumeration is a check of the proof's finite instances, not an argument for the universally quantified theorem. Run `python verify.py` with SymPy installed.

## Relationship to prior work
Berenbrink, Götte, Hoefer, and Koglin (2026) introduced and analyzed ordinary and productive EdgeVOG. Their Section 2.2 establishes a lower bound for the individual probability of survival and a concentration inequality for the number of surviving opinions; their star construction in Section 2.1 uses a gambler's-ruin calculation for the *total* hub support to analyze stabilization time. Neither calculation supplies the exact **joint terminal vector law** here. The definition and pair-selection convention are theirs; those are not claimed as novel.

Öztürk (2011 preprint; later published) studied a bounded-confidence discrete opinion process using master equations and absorption probabilities, including the three-opinion line, which is the two-leaf star. Its numerical and matrix-based polarization calculations motivate caution about generality; the present result concerns the specified highly unbalanced initial configuration and gives a uniform formula for arbitrary star degree. Hardin and Lanchier (2019 preprint) establish consensus bounds in opinion models with confidence thresholds, not this terminal count identity. Standard Doob transforms and Pólya-urn sampling consistency are tools rather than proposed novel principles. A more general preexisting result about multitype birth–death absorption may imply the theorem; no uniqueness or publication priority is asserted.

## Limitations
The formula is specific to complete, homogeneous, fair pairwise communication; to the star compatibility graph; and to exactly one initially supported individual at each peripheral opinion. Unequal interaction rates, general confidence graphs, and larger initial peripheral groups can change the joint exit law. The Dirichlet limit is a conditional law on a rare event: without conditioning, its mass vanishes at order \(n^{-d}\) for fixed \(d\). Results are analytically proved but have not undergone independent scientific review. Novelty comparisons cover the cited accessible material and targeted searches; undiscovered equivalent results remain possible.

## References
1. P. Berenbrink, T. Götte, M. Hoefer, T. Koglin, *The Voter Model with Opinion Graph*, arXiv:2610.16684v1, first submitted 12 October 2026. https://arxiv.org/html/2610.16684v1
2. M. K. Öztürk, *Dynamics of discrete opinions without compromise*, arXiv:1112.4624 (2011 preprint). https://arxiv.org/abs/1112.4624
3. C. Hardin and N. Lanchier, *Probability of consensus in spatial opinion models with confidence threshold*, arXiv:1912.06746 (2019 preprint). https://arxiv.org/abs/1912.06746
