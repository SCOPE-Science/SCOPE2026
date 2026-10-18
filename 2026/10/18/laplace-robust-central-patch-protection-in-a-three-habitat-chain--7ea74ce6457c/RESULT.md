# Laplace-robust central-patch protection in a three-habitat chain

## Finding

A single permanent reduction of local extinction hazard in the middle of a three-habitat chain outperforms the same reduction at an end in **every exponentially discounted persistence objective**, with strictness at every nonzero recolonization rate. A complete reversal holds when the distinguished patch is made less safe instead.

Write \(T_{\mathrm{mid}}\) and \(T_{\mathrm{end}}\) for global extinction times under these placements. For \(z\ge0\), put
\[
F_v(z)=\mathbb E\!\left[\int_0^{T_v}e^{-zt}\,dt\right].
\]
Then, for \(q>0\), \(\lambda>0\), and every \(z\ge0\),
\[
\operatorname{sgn}\bigl(F_{\mathrm{mid}}(z)-F_{\mathrm{end}}(z)\bigr)=\operatorname{sgn}(1-q).
\]
Equality holds for \(q=1\) or \(\lambda=0\). In particular, for \(0<q<1\), \(\mathbb E[T_{\mathrm{mid}}]>\mathbb E[T_{\mathrm{end}}]\) and \(\mathbb E[e^{-zT_{\mathrm{mid}}}]<\mathbb E[e^{-zT_{\mathrm{end}}}]\) for every \(z>0\).

## Assumptions and scope

The habitat graph is the undirected path \(1-2-3\). Each patch is vacant or occupied. At an occupied patch, the local extinction hazard is \(1\), except at one distinguished patch where it is \(q>0\). From any occupied neighbor, recolonization of a vacant patch occurs independently at rate \(\lambda\ge0\), so two occupied neighbors give the sum of two rates. State \(000\) is absorbing, and initially the state is \(111\). There are no catastrophes, simultaneous transitions, patch-area effects, density dependence, or environmental temporal changes. Protection is permanent rather than a time-dependent policy. The unit baseline hazard entails no loss of generality for equal baseline hazards \(\mu>0\): divide all rates, including the discount rate, by \(\mu\), and scale time by \(\mu\).

## Proof

Index the seven nonempty occupancy subsets by the binary masks \(1,2,3,4,5,6,7\), where the central vertex has bit \(2\). Let \(Q_v\) denote their transient generator, with local-death transitions \(S\to S\setminus\{i\}\) at rates \(q\) or \(1\), and recolonization transitions \(S\to S\cup\{i\}\) at rate \(\lambda\) times the number of occupied neighbors. Rate exiting to empty state contributes only to the negative diagonal of \(Q_v\). Write \(M_v(z)=zI-Q_v\), \(D_v(z)=\det M_v(z)\), and let \(N_v(z)\) be its determinant after replacing column seven by the all-ones column.

The standard finite-state Markov resolvent and Cramer's rule give
\[
F_v(z)=e_7^{\mathsf T}(zI-Q_v)^{-1}\mathbf 1=\frac{N_v(z)}{D_v(z)}.
\]
Every state can reach absorption by successive local-extinction events of positive probability. Therefore the transient generator is stable. For each \(z\ge0\), both \(M_v(z)\) are nonsingular \(M\)-matrices, and \(D_{\mathrm{mid}}(z)D_{\mathrm{end}}(z)>0\).

The exact integer-polynomial identity proved by the accompanying self-contained checker is
\[
N_{\mathrm{mid}}D_{\mathrm{end}}-N_{\mathrm{end}}D_{\mathrm{mid}}
=\lambda q(1-q)H(\lambda,q,z),
\]
where \(H\) has exactly \(159\) nonzero monomials, each with a strictly positive integer coefficient. Its total degree is \(8\), its smallest coefficient is \(2\), and its largest is \(19670\). The checker constructs all four determinants directly from the seven-state generator, uses exact integer polynomial arithmetic, divides by the displayed factors with an exact remainder test, checks positivity of **every** remaining coefficient, and independently checks rational resolvents by Gaussian elimination. Thus \(H(\lambda,q,z)>0\) for \(\lambda>0\), \(q>0\), \(z\ge0\). This proves the sign classification. If \(\lambda=0\), the three patch lifetimes are independent exponential random variables with rate multiset \(\{1,1,q\}\); changing their positions cannot change the time of final extinction. If \(q=1\), the generators coincide.

For \(z>0\), integration by parts for the absorption time gives \(F_v(z)=(1-\mathbb E[e^{-zT_v}])/z\). At \(z=0\) it gives \(F_v(0)=\mathbb E[T_v]\). These yield all claimed consequences.

## Verification

Run `python3 check_exact.py` using Python 3.10 or later; it needs no third-party packages. It constructs an exact multivariate coefficient dictionary for the generator determinant identity, independently checks four rational Gaussian-elimination solutions, and reports the coefficient count, extrema, and degree. The test is an **exact finite symbolic certificate** for a polynomial identity valid for all parameters, not a simulation or a truncated parameter scan. In the case \(\lambda=1\), \(q=1/2\), the computed expected times are \(851/182\) for central protection and \(1599/370\) for end protection; at \(z=1\), the discounted values are \(1307/1480\) and \(48135/54809\), respectively.

## Relationship to prior work

Chadès et al. (2011) study time-dependent node management and survey policies for finite susceptible–infected–susceptible network motifs. Their rules for managing a line begin at an end, but their objective, action sequence, and discrete-time controlled process differ from the permanent local-hazard intervention and all-discount extinction-time ordering here. Etienne and Heesterbeek (2001) give qualitative metapopulation management advice favoring well-connected patches when local risks are nearly equal; any mean-persistence preference contained there is not claimed as new. The present exact claim concerns a simultaneously valid continuum of exponential-discount objectives, which is not implied by a mean-time preference. Ross and Pollett (2010) optimize expected extinction times in a calibrated Levins-type model, not this seven-state heterogeneous path resolvent. Eriksson et al. (2014) analyze rescue effects with many patches and stochastic within-patch recruitment, not this finite-path placement comparison.

## Limitations

The result is specifically a three-patch homogeneous-edge contact process, initially fully occupied. It does not establish usual stochastic dominance of extinction times at every deterministic horizon, variance ordering, hazard ordering, or optimality on larger/other graphs. The literature comparison cannot rule out an equivalent formulation in the full text of Etienne and Heesterbeek (2001), which was not accessible for inspection, or in unindexed specialized work. It should not be construed as a statement about the empirical magnitude of any conservation intervention.

## References

1. I. Chadès, T. G. Martin, S. Nicol, M. A. Burgman, H. P. Possingham, and Y. M. Buckley, *General rules for managing and surveying networks of pests, diseases, and endangered species*, PNAS 108 (2011), 8323–8328, DOI: 10.1073/pnas.1016846108, first online 2011-05-02.
2. R. S. Etienne and J. A. P. Heesterbeek, *Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model*, American Naturalist 158 (2001), 389–407, DOI: 10.1086/321986.
3. J. V. Ross and P. K. Pollett, *Simple rules for ranking and optimally managing metapopulations*, Ecological Modelling 221 (2010), 2515–2520, DOI: 10.1016/j.ecolmodel.2010.02.016.
4. A. Eriksson, F. Elías-Wolff, B. Mehlig, and A. Manica, *The emergence of the rescue effect from the interaction of local stochastic dynamics within a metapopulation*, arXiv:1401.6524v1 (2014-01-25).
