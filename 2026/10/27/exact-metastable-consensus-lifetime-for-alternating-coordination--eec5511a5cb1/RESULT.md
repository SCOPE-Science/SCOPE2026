# Exact metastable consensus lifetime for alternating coordination games on a clique

## Finding

Consider the fully overlapping, complete-graph specialization of a two-layer coordination game. At every asynchronous update, one of two opposed coordination payoff matrices is chosen equiprobably, followed by a uniformly chosen player making a strict myopic best response to the current choices of all other players. For a fixed threshold \(0<\eta<1/2\), the first game favors action \(A\) whenever the fraction of \(A\)-neighbors exceeds \(\eta\), and the second whenever that fraction exceeds \(1-\eta\). All participants use the same action on both layers.

For every even population \(N=2r\ge4\) satisfying \((N-1)\eta\notin\mathbb Z\) and \(m=\lfloor(N-1)\eta\rfloor\le r-2\), the chain started with \(r\) players using each action almost surely reaches unanimous \(A\) or unanimous \(B\), each with probability \(1/2\). Its mean consensus time \(\mathbb E_r\tau_N\), measured in individual asynchronous updates, has the exact finite-binomial formula below.

Write \(C_j=\binom Nj\) and, for \(m+2\le k\le r\), define
\[
D_k=\frac{2N}{kC_k}\left(\sum_{j=k}^{r-1}C_j+\frac12 C_r\right),
\qquad
D_{m+1}=\frac{N}{m+1}+\frac{N-m-1}{2(m+1)}D_{m+2}.
\]
Then
\[
\boxed{\mathbb E_r\tau_N=N\sum_{j=1}^{m}\frac1j+\sum_{k=m+1}^{r}D_k.}
\]
This formula is valid without diffusion or mean-field approximations and includes the special boundary update probabilities. For every fixed \(\eta\in(0,1/2)\), as even, tie-free \(N\to\infty\),
\[
\boxed{\lim_{N\to\infty}\frac1N\log\mathbb E_{N/2}\tau_N
=\log 2+\eta\log\eta+(1-\eta)\log(1-\eta)>0.}
\]
The balanced mixed state thus has an exponentially long finite-population lifetime, although consensus occurs almost surely for each finite population.

## Assumptions and scope

The interaction graph on each layer is the same complete graph with \(N\) labeled participants, with complete node overlap. The two payoff matrices, each written with the row player's alternatives \(A,B\) against the column player's \(A,B\), are
\[
M_1=\begin{pmatrix}1&-\eta\\ \eta&0\end{pmatrix},
\qquad
M_2=\begin{pmatrix}1&-(1-\eta)\\1-\eta&0\end{pmatrix}.
\]
These are strict coordination games for \(0<\eta<1/2\), with opposed risk-dominant alternatives. They coincide with the symmetric stag-hunt parameterization of Raducha and San Miguel (arXiv:2212.08877) for separation \(\Delta S=1-2\eta\). Every update chooses one layer with probability \(1/2\) and independently selects one participant uniformly; that participant computes the better action by summing the payoff across all \(N-1\) neighbors on the chosen layer and changes its action if required. The new action is synchronized across layers. Since \((N-1)\eta\notin\mathbb Z\), no best-response tie can arise at either threshold in the finite chain.

Let \(K_t\) count the number choosing \(A\), and \(\tau_N=\inf\{t\ge0:K_t\in\{0,N\}\}\). Holding steps are counted. The exact formula assumes \(N\) even, the tie-free restriction, and \(m\le r-2\); these conditions hold for all sufficiently large tie-free even \(N\) at fixed \(\eta\). The exponential limit is along these allowable population sizes, not a claim about a different tie convention.

## Proof

**Best-response thresholds and lumping.** If a selected participant observes fraction \(z\) of neighbors playing \(A\), the difference between its payoffs from \(A\) and \(B\) is exactly \(z-\eta\) under \(M_1\), and \(z-(1-\eta)\) under \(M_2\). Therefore, when \(K_t=k\), a selected \(B\)-player sees \(k/(N-1)\) neighbors playing \(A\), whereas a selected \(A\)-player sees \((k-1)/(N-1)\). The count \(K_t\) is a birth-and-death chain. Define \(p_k=\Pr(K_{t+1}=k+1\mid K_t=k)\) and \(q_k=\Pr(K_{t+1}=k-1\mid K_t=k)\). Direct conditioning on the chosen player and layer yields
\[
p_k=\frac{N-k}{N}\begin{cases}
0,&k/(N-1)<\eta,\\
\frac12,&\eta<k/(N-1)<1-\eta,\\
1,&k/(N-1)>1-\eta,
\end{cases}
\]
\[
q_k=\frac{k}{N}\begin{cases}
1,&(k-1)/(N-1)<\eta,\\
\frac12,&\eta<(k-1)/(N-1)<1-\eta,\\
0,&(k-1)/(N-1)>1-\eta.
\end{cases}
\]
In particular, \(p_k=0\) for \(0\le k\le m\) and \(q_k=0\) for \(N-m\le k\le N\). Starting from those respective corridors the chain monotonically reaches the corresponding unanimous state; its conditional expected remaining duration from \(k=m\), or from \(k=N-m\), is \(N\sum_{j=1}^{m}1/j\).

**Exact exit-time calculation.** Let \(T_k\) denote the expected time to hit \(\{m,N-m\}\) from \(k\) in the interior. The reflection identity \(p_k=q_{N-k}\) implies \(T_k=T_{N-k}\). Thus, for \(r=N/2\), \(T_{r+1}=T_{r-1}\), and the first-step equation at the center, where \(p_r=q_r=1/4\), gives \(T_r-T_{r-1}=2\). For \(m+1\le k\le r\) set \(d_k=T_k-T_{k-1}\). At all \(m+2\le k\le r\), the interior transition probabilities are \(p_k=(N-k)/(2N)\) and \(q_k=k/(2N)\). Hence
\[
q_kd_k=1+p_kd_{k+1}\quad(m+2\le k<r).
\]
Multiplication by \(C_k\) and \(C_kp_k=C_{k+1}q_{k+1}\) gives, by backward summation from the central condition \(d_r=2\),
\[
d_k=\frac{2N}{kC_k}\left(\sum_{j=k}^{r-1}C_j+\frac12 C_r\right)=D_k.
\]
There is one exceptional interior state, \(k=m+1\), where \(p_{m+1}=(N-m-1)/(2N)\) but \(q_{m+1}=(m+1)/N\), twice the usual inward Ehrenfest probability. The first-step equation therefore gives
\[
d_{m+1}=\frac{N}{m+1}+\frac{N-m-1}{2(m+1)}D_{m+2}=D_{m+1}.
\]
Since \(T_m=0\), summing the increments yields \(T_r=\sum_{k=m+1}^rD_k\). Adding the exact expected duration from either exit corridor by the strong Markov property proves the displayed finite formula. Every state in the interior communicates with an exit corridor by a positive-probability path; a finite-state absorbing-chain argument proves \(\tau_N<\infty\) almost surely. Reflection interchanges \(A\) and \(B\), so from \(K_0=r\) the two absorption probabilities are equal and sum to one.

**Sharp exponential rate.** As \(N\to\infty\) along allowable even sizes, \((m+2)/N\to\eta\), and the binomial entropy estimate gives
\[
\frac1N\log C_{m+2}\longrightarrow
H(\eta):=-\eta\log\eta-(1-\eta)\log(1-\eta).
\]
The central binomial coefficient satisfies \(N^{-1}\log C_r\to\log2\). Since the summand \(D_{m+2}\) includes \(C_r/2\), the exact formula gives the lower exponential bound \(\liminf N^{-1}\log\mathbb E_r\tau_N\ge\log2-H(\eta)\). Conversely, \(C_k\ge C_{m+2}\) for \(m+2\le k\le r\), and each numerator sum is at most \(2^N\). Thus all \(D_k\) and the exceptional \(D_{m+1}\) are bounded by a polynomial in \(N\) times \(2^N/C_{m+2}\). The corridor term is at most \(N(1+\log N)\). This yields the matching upper exponential bound and proves the limit. Positivity follows from strict binary entropy maximization at \(\eta=1/2\).

## Verification

The standalone standard-library program `verify.py` reconstructs the transition rates directly from the two payoff thresholds, computes \(\mathbb E_r\tau_N\) using the finite formula, and independently validates every first-step expected-time equation by exact rational arithmetic. For small populations it additionally enumerates all action profiles and both possible layer choices to check the lumped transition probabilities. It checks action-reversal symmetry and both one-way absorption corridors. Its finite checks are corroborative; the universal and asymptotic assertions are proved above.

For \(\eta=1/5\), \(N=20\), and balanced initial play, \(m=3\) and
\[
\mathbb E_{10}\tau_{20}=\frac{20759}{21}=988.523809\ldots
\]
individual updates. The population-size exponent is
\[
\log2-H(1/5)=0.192744757021757\ldots.
\]
Run `python3 verify.py` from the directory containing the document and program; no network, nonstandard package, or external data are required.

## Relationship to prior work

Raducha and San Miguel, *Evolutionary games on multilayer networks: coordination and equilibrium selection* (arXiv:2212.08877, first submitted 2022-12-17), provide the two-layer payoff family, shared-agent mechanism, and asynchronous best-response update. Their study chiefly examines random regular networks through simulation, identifying mixed outcomes at high overlap. It does not provide the finite complete-graph absorption-time identity or its exact entropy-rate dependence on the separation of the games. The present claim is confined to the complete-graph, full-overlap specialization, not arbitrary random regular networks.

Auletta, Ferraioli, Pasquale and Persiano, *Metastability of Logit Dynamics for Coordination Games* (arXiv:1107.4537), give general metastability results for logit dynamics and examine a nearly lazy Ehrenfest process arising from a different OR game. Their Section 6 provides a useful comparison, but its logit/OR update rule, location of exceptional transitions, and stated bounds do not give the switched-hard-best-response consensus-time formula proved here. Ehrenfest binomial weights and finite birth-and-death recurrences are classical and are not claimed as new ingredients.

Krapivsky and Redner, *Divergence and Consensus in Majority Rule* (arXiv:2103.04248), obtain exponential consensus times for a different two-class majority-rule process. That model selects triples and incorporates homophily, rather than uniformly alternating two opposed coordination payoff matrices for an individual update; its macroscopic state is two-dimensional and its metastable basin differs from the central single-count corridor treated here.

## Limitations

The calculation requires identical complete graphs, total node overlap, strict deterministic best response given the selected layer, equal layer-selection probabilities, asynchronous single-player updates, and the stated even-size/tie-free conditions. It does not prove an identical lifetime for the sparse random-regular graphs emphasized in the motivating simulations, for partially shared nodes, for other update rules, or when best-response ties require a convention. The expectation exponent does not by itself characterize the full distribution of absorption times or prove an exponential limiting law. Literature priority is provisional pending wider specialist review.

## References

1. T. Raducha and M. San Miguel, *Evolutionary games on multilayer networks: coordination and equilibrium selection*, arXiv:2212.08877 (submitted 2022-12-17), https://arxiv.org/abs/2212.08877.
2. V. Auletta, D. Ferraioli, F. Pasquale and G. Persiano, *Metastability of Logit Dynamics for Coordination Games*, arXiv:1107.4537 (2011), https://arxiv.org/abs/1107.4537.
3. P. L. Krapivsky and S. Redner, *Divergence and Consensus in Majority Rule*, arXiv:2103.04248 (2021), https://arxiv.org/abs/2103.04248.
