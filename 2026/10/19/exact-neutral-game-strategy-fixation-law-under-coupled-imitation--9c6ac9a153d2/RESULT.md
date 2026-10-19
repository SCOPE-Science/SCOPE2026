# Exact neutral game–strategy fixation law under coupled imitation

## Finding

Fix any integer \(N\ge2\), a finite population of \(N\) individuals, initial strategy labels \(S_i(0)\) and game labels \(G_i(0)\), and two copy-propensity parameters \(0<p_s,p_g\le1\). In each discrete step choose a focal individual and a model individual uniformly and independently from the population. The focal individual copies the model's strategy with probability \(p_s/2\) and independently copies the model's game label with probability \(p_g/2\). This is the exact zero-selection-strength specialization of the independent game/strategy Fermi imitation mechanism in Sadekar et al. [1], since its imitation probability is then \(1/2\). Game labels can be arbitrary distinct payoff matrices; no mutation or new game is introduced.

Both attributes fix to population-wide consensus almost surely. Write \(S_\infty\) and \(G_\infty\) for their respective surviving labels. For any initial strategy label \(s\) and game label \(g\), let
\[
 r_s=\frac1N\#\{i:S_i(0)=s\},\qquad
 q_g=\frac1N\#\{i:G_i(0)=g\},\qquad
 h_{sg}=\frac1N\#\{i:(S_i(0),G_i(0))=(s,g)\}.
\]
Then their *complete joint terminal law* is
\[
\boxed{\Pr(S_\infty=s,G_\infty=g)=(1-\theta)r_s q_g+\theta h_{sg},\qquad
\theta=\frac{p_s p_g}{N(p_s+p_g-p_s p_g)+p_s p_g}.}
\]
The same terminal law holds if the model is chosen uniformly among the other \(N-1\) agents instead of among all \(N\) agents. Thus fixation pairs are exactly a mixture of independently sampled initial strategy/game labels and a jointly sampled initial pair. Moreover \(0<\theta\le1/(N+1)\), with the upper bound attained precisely for \(p_s=p_g=1\). If \(h_{sg}=r_s q_g\) for all pairs, the terminal attributes are independent, despite sharing every focal/model interaction.

With the self-allowed sampling convention, for the time-dependent proportions \(R_s(t)\) and \(Q_g(t)\),
\[
 \mathbb E[R_s(t)Q_g(t)]
 =r_s q_g+\theta\bigl(1-(1-\lambda)^t\bigr)(h_{sg}-r_s q_g),
\qquad
 \lambda=\frac{N(p_s+p_g-p_s p_g)+p_s p_g}{2N^2}.
\]
For sampling distinct individuals, replace \(\lambda\) by \(\lambda N/(N-1)\); \(\theta\) is unchanged.

## Assumptions and scope

All assertions are for finite \(N\ge2\), deterministic initial labels with finite support, strict positive copy propensities \(p_s,p_g\le1\), independent random copying decisions conditional on the same selected focal/model pair, and selection strength identically zero. The result concerns *eventual absorption*, not the quasi-stationary laws used for nonzero selection in [1], and it does not assert any formula for payoff-dependent positive-strength imitation, general graphs, mutation, or independently sampled model individuals for the two different attributes. Self-allowed and self-excluded pair sampling are both covered and explicitly differentiated for finite-time rates.

## Proof

**Absorption.** A step in which focal \(i\) copies *both* attributes of designated individual \(1\) has positive probability \((p_sp_g/4)/N^2\) under independent uniform focal/model sampling. Prescribing this event in turn for each \(i=2,\ldots,N\) produces a joint-consensus configuration in at most \(N-1\) steps. The probability is uniformly positive over all initial states. Repeating fixed-length blocks proves almost-sure finite absorption. With distinct-model sampling the corresponding probability per prescribed event is \((p_sp_g/4)/[N(N-1)]\), so the conclusion is unchanged.

**Two-indicator moment closure.** For any fixed labels \(s,g\), put \(X_i=\mathbf1_{\{S_i=s\}}\), \(Y_i=\mathbf1_{\{G_i=g\}}\), \(x=N^{-1}\sum_iX_i\), \(y=N^{-1}\sum_iY_i\), \(z=N^{-1}\sum_iX_iY_i\), and \(d=z-xy\). Let \(a=p_s/2\), \(b=p_g/2\). When \(i\) and \(j\) are the selected focal and model, and \(U,V\) are independent Bernoulli random variables of means \(a,b\),
\[
 \Delta X_i=U(X_j-X_i),\qquad \Delta Y_i=V(Y_j-Y_i).
\]
Uniform *independent* selection of \(i,j\) gives
\[
\begin{aligned}
 \mathbb E[\Delta x\mid\mathcal F_t]&=0, &
 \mathbb E[\Delta y\mid\mathcal F_t]&=0,\\
 \mathbb E[\Delta(xy)\mid\mathcal F_t]&=\frac{2ab}{N^2}d, &
 \mathbb E[\Delta z\mid\mathcal F_t]&=-\frac{a+b-2ab}{N}d.
\end{aligned}
\]
The second line follows by expanding \((x+\Delta x)(y+\Delta y)\) and \((X_i+\Delta X_i)(Y_i+\Delta Y_i)\), using
\[
 \frac1{N^2}\sum_{i,j}(X_j-X_i)(Y_j-Y_i)=2(z-xy),\qquad
 \frac1{N^2}\sum_{i,j}Y_i(X_j-X_i)=xy-z.
\]
Consequently
\[
 \mathbb E[\Delta d\mid\mathcal F_t]=-\lambda d,
 \qquad \lambda=\frac{a+b-2ab+2ab/N}{N}.
\]
Set \(\theta=(2ab/N^2)/\lambda\). The process \(xy+\theta d\) is a bounded martingale. At absorption \(d=0\) and \(xy=\mathbf1_{\{S_\infty=s,G_\infty=g\}}\). Bounded convergence yields
\[
 \Pr(S_\infty=s,G_\infty=g)=r_s q_g+\theta(h_{sg}-r_s q_g),
\]
and simplification of \(\theta\) gives the displayed formula. Iterating \(\mathbb E[d_{t+1}]=(1-\lambda)\mathbb E[d_t]\) and summing the increments of \(\mathbb E[xy]\) gives the transient identity.

**Distinct-model robustness.** For ordered \(i\ne j\), replace the pair average by \(1/[N(N-1)]\sum_{i\ne j}\). The two conditional increments become
\[
 \mathbb E[\Delta(xy)\mid\mathcal F_t]=\frac{2ab}{N(N-1)}d,
 \qquad \mathbb E[\Delta z\mid\mathcal F_t]=-\frac{a+b-2ab}{N-1}d.
\]
Their ratio determining \(\theta\) is unchanged, while \(\lambda\) is multiplied by \(N/(N-1)\).

**Sharpness.** Let \(D=N(a+b-2ab)+2ab\). Direct differentiation gives
\[
 \frac{\partial\theta}{\partial a}=\frac{2Nb^2}{D^2}>0,
 \qquad \frac{\partial\theta}{\partial b}=\frac{2Na^2}{D^2}>0.
\]
Since \(a,b\le1/2\), the exact maximum is \(\theta(1/2,1/2)=1/(N+1)\). Nonzero initial contingency-table covariance makes this bound operational: in the two-person example with labels \((S,G)=(0,0),(1,1)\) and \(p_s=p_g=1\), \(\Pr(S_\infty=1,G_\infty=1)=1/3\), versus independent-founder value \(1/4\).

## Verification

The standalone standard-library Python program `neutral_coupled_traits_checker.py` represents each of the four binary joint label categories as an exact count state and forms all transition probabilities as `fractions.Fraction` rationals. It checks the displayed harmonic function on **1,230 exact count-state/parameter/sampling combinations**, spanning population sizes \(N=2,3,4,5,6\). A second, independently constructed absorbing-chain Gaussian-elimination calculation exactly solves and compares **88 nonabsorbing states** for \(N=2,3\). The checked examples include \(1/6\) and \(1/3\) terminal \((1,1)\) probabilities for two opposite versus two matching binary initial pairs. The algebraic proof above, rather than finite testing, establishes the theorem for all \(N\), labels, and admitted copy propensities. Reproduce using `python3 neutral_coupled_traits_checker.py`.

## Relationship to prior work

Sadekar, Civilini, Gómez-Gardeñes, Latora, and Battiston [1] introduce the coevolving game/strategy mechanism, specify independent imitation probabilities in their Eq. (11), and numerically observe strong associations of surviving strategies and games under payoff selection. Their analysis does not give the exact finite-population **joint fixation table at zero selection** proved here. This neutral benchmark separates finite-population ancestry-induced coupling from payoff-driven associations. The two-layer voter model of Vega-Oliveros et al. [2] instead makes opinion updating *dependent on current tolerance* and uses separate neighbors, so its consensus-time results cannot supply this independent two-trait terminal mixture. General two-locus neutral Moran and recombination methods [3] provide related ancestral-process machinery but are formulated for distinct reproduction/recombination generators and sampling likelihoods, not the precise independent Fermi co-imitation mechanism and its explicit fixed-initial-data fixation table. No claim is made that the martingale technique or neutral genealogy ideas are new.

## Limitations

This is a **neutral**, finite-population result and is not evidence of payoff-selected cooperation, nor a statement about nonzero Fermi strength or structured networks. For the two-attribute result, both copy propensities must be strictly positive; if one is zero its trait need not fix. The mixture coefficient is at most \(1/(N+1)\) in this mechanism and therefore tends to zero for large \(N\), but the displayed formula is not an asymptotic claim about the nonneutral model. Specialist literature on dual-locus fixation or coupled voter genealogies could supply an equivalent reduction not identified in the examined materials.

## References

[1] O. Sadekar, A. Civilini, J. Gómez-Gardeñes, V. Latora, F. Battiston, *Evolutionary game selection creates cooperative environments*, arXiv:2311.11128, first posted 2023-11-18, https://arxiv.org/abs/2311.11128; later *Physical Review E* 110, 014306 (2024). Eq. (11) and Secs. II–IV.

[2] D. A. Vega-Oliveros, H. L. C. Grande, F. Iannelli, F. Vazquez, *Bi-layer voter model: Modeling intolerant/tolerant positions and bots in opinion dynamics*, arXiv:2201.02218 (2022), https://arxiv.org/abs/2201.02218, especially Secs. II–III.

[3] J. A. Kamm, J. P. Spence, J. Chan, Y. S. Song, *Two-Locus Likelihoods Under Variable Population Size and Fine-Scale Recombination Rate Estimation*, *Genetics* 203, 1381–1399 (2016), https://doi.org/10.1534/genetics.115.184820; related thesis treatment https://doczz.net/doc/8239490/one-and-two-locus-likelihoods-under-complex, Ch. 4.
