# A cut-permutation law for the first non-exponential SIS extinction-time fluctuation

## Finding

**Theorem.** Let \(G=(V,E)\) be any fixed finite connected simple undirected graph with \(n=|V|\ge2\). In the continuous-time susceptible-infected-susceptible process, infected vertices recover at rate \(1\), independently; each edge with one infected and one susceptible endpoint causes infection at rate \(\lambda>0\). Initially every vertex is infected. Write \(T_G(\lambda)\) for the time until there are no infected vertices.

For each permutation \(\pi=(v_1,\ldots,v_n)\) of \(V\), put \(S_j=V\setminus\{v_1,\ldots,v_j\}\), and \(c_j(\pi)=|\partial_G S_j|\) for \(1\le j<n\), where \(\partial_G S\) consists of edges with exactly one endpoint in \(S\). Define the strictly positive finite invariants

\[
R_G=\sum_{\pi\in\mathfrak S(V)}\prod_{j=1}^{n-1}\frac1{c_j(\pi)},
\qquad
C_G=2\sum_{\pi\in\mathfrak S(V)}\left(\prod_{j=1}^{n-1}\frac1{c_j(\pi)}\right)\left(\sum_{j=1}^{n-1}\frac1{c_j(\pi)}\right).
\]

Then, for fixed \(G\) as \(\lambda\to\infty\),

\[
\mathbb E T_G(\lambda)=\frac{\lambda^{n-1}}{R_G}\bigl(1+O_G(\lambda^{-1})\bigr),
\qquad
1-\frac{\operatorname{Var}(T_G(\lambda))}{(\mathbb E T_G(\lambda))^2}
=\frac{C_G}{\lambda^n}+O_G(\lambda^{-n-1}).
\]

The correction is nonzero and positive for every connected graph. For complete graphs, \(R_{K_n}=n/(n-1)!\) and \(C_{K_n}=4H_{n-1}/(n-1)!\), where \(H_m=\sum_{j=1}^m1/j\). In particular, the four-vertex path and four-vertex star both have \(R_G=8\), but their fluctuation coefficients are, respectively, \(C_{P_4}=38\) and \(C_{K_{1,3}}=112/3\). Thus two graphs can have identical leading mean extinction times but distinguishable leading deviations from an exponential extinction-time law.

## Assumptions and scope

The graph is **fixed** as \(\lambda\to\infty\); the result is not uniform in \(n\). All rates are specified in continuous time, recovery is independent and exponential, and extinction is absorbing. All graph cuts are strictly positive because \(G\) is connected and each \(S_j\) is a nonempty proper subset. The reported variance ratio is a *squared coefficient of variation*, not a statement about the variance alone. No independence assumption is imposed among extinction times from other initial states.

## Proof

**1. Regenerative decomposition.** From the fully infected state \(V\), the first recovery occurs after a holding time \(W\sim\mathrm{Exp}(n)\), and its vertex is uniform on \(V\) independently of \(W\). Starting with the resulting \(n-1\) infected vertices, let \(L\) be the time until the process first reaches either \(V\) again (a failed excursion) or the empty set (a successful excursion). Put \(I=1\) in the latter event, \(p=\mathbb E I\), \(\ell=\mathbb E L\), \(c=\mathbb E(LI)\), and \(\mu=1/n+\ell\). The regeneration occurs at \(V\); consequently, with \(Y=W+L\) and an independent fresh extinction time \(T'\),

\[
T\overset d=Y+(1-I)T'.
\]

Since \(p>0\) and the finite absorbing process has finite moments, first and second moments give \(\mathbb E T=\mu/p\) and

\[
\frac{\operatorname{Var}T}{(\mathbb ET)^2}
=\frac{p\,\mathbb E Y^2}{\mu^2}+\frac{2\mathbb E[Y(1-I)]}{\mu}-1.
\]

Using \(\mathbb E(WI)=p/n\), \(\mathbb E Y^2=2/n^2+2\ell/n+\mathbb E L^2\), and \(\mu=1/n+\ell\), rearrangement yields the **exact identity**

\[
1-\frac{\operatorname{Var}T}{(\mathbb ET)^2}
=\frac{2c}{\mu}-\frac{p\mathbb E L^2}{\mu^2}. \tag{1}
\]

**2. Uniform excursion bounds.** In every nonempty, nonfull infected configuration \(S\), its infection rate is \(\lambda|\partial_G S|\ge\lambda\) and its recovery rate is at most \(n\). Hence its next transition is an infection with probability at least \(\lambda/(\lambda+n)\). From any such state, at most \(n-1\) consecutive infections suffice to reach \(V\). The probability of this event is uniformly at least \((\lambda/(\lambda+n))^{n-1}\), which stays bounded away from zero when \(\lambda\ge1\). Dividing transitions into blocks of length \(n-1\) therefore yields a uniform geometric tail bound on the number of jumps before the excursion ends. Every holding time has rate at least \(\lambda\), so its first two moments and the geometric tail give

\[
\ell=O_G(\lambda^{-1}),\quad \mathbb E L^2=O_G(\lambda^{-2}),\quad \mu=1/n+O_G(\lambda^{-1}). \tag{2}
\]

**3. Successful excursions and cuts.** A successful excursion with no infections consists of exactly \(n-1\) subsequent single-vertex recoveries after the initial recovery from \(V\). Label the full \(n\)-vertex deletion ordering by \(\pi\). At infected set \(S_j\), the total jump rate is \(n-j+\lambda c_j(\pi)\). Conditional on initial recovery vertex (probability \(1/n\)), the probability of the specified remaining deletion ordering is the product of these inverse total rates. Thus the total probability of infection-free successful excursions is

\[
\frac1n\sum_{\pi}\prod_{j=1}^{n-1}\frac1{n-j+\lambda c_j(\pi)}
=\frac{R_G}{n\lambda^{n-1}}+O_G(\lambda^{-n}). \tag{3}
\]

Any successful excursion containing at least one infection must contain at least \(n\) recovery jumps *after* the initial departure from \(V\). Each recovery event before absorption in a nonfull state has probability at most \(n/\lambda\) at its jump, and the uniform geometric jump-tail bound in step 2 controls all possible detours. Summing over such paths gives their total probability \(O_G(\lambda^{-n})\); their contribution to \(\mathbb E(LI)\) is \(O_G(\lambda^{-n-1})\), using the conditional holding times and the same geometric tail estimate. Therefore

\[
p=\frac{R_G}{n\lambda^{n-1}}+O_G(\lambda^{-n}). \tag{4}
\]

For a prescribed infection-free successful deletion sequence \(\pi\), conditional holding times between jumps have means \((n-j+\lambda c_j)^{-1}\). Multiplying the sum of these means by the probability of that sequence and summing over \(\pi\) gives

\[
c=\frac1{n\lambda^n}\sum_\pi\left(\prod_{j=1}^{n-1}\frac1{c_j(\pi)}\right)
\left(\sum_{j=1}^{n-1}\frac1{c_j(\pi)}\right)+O_G(\lambda^{-n-1})
=\frac{C_G}{2n\lambda^n}+O_G(\lambda^{-n-1}). \tag{5}
\]

**4. Conclusion.** Substitute (2), (4), and (5) into the exact identity (1). The second term in (1) is \(O_G(\lambda^{-n-1})\), while the first is \(C_G\lambda^{-n}+O_G(\lambda^{-n-1})\). Also \(\mathbb ET=\mu/p\), yielding the claimed mean. Every summand of \(C_G\) is positive, proving sharpness of the exponent \(n\).

**5. Explicit graph evaluations.** In \(K_n\), a cut with \(i\) infected vertices has size \(i(n-i)\). Consequently \(R_{K_n}=n!/((n-1)!)^2=n/(n-1)!\), and \(\sum_{i=1}^{n-1}1/[i(n-i)]=2H_{n-1}/n\), hence \(C_{K_n}=4H_{n-1}/(n-1)!\). Direct rational permutation enumeration gives \((R,C)=(8,38)\) for \(P_4\) and \((8,112/3)\) for \(K_{1,3}\).

## Verification

The included `check.py` uses only the Python standard library. It calculates \(R_G\) and \(C_G\) by exact rational permutation enumeration, builds the exact transient generator for every nonempty SIS state on the seven test graphs, solves the first- and second-moment linear systems with rational arithmetic, and compares scaled variance deficits at infection rates \(10,20,40\). It separately verifies the closed complete-graph expression for orders \(2\) through \(6\). Execute `python3 check.py`. The checker reports `PASS`; these finite experiments are checks, **not** the proof of the all-graph theorem.

## Relationship to prior work

The finite-graph SIS and its survival-time expectations were studied by Van de Bovenkamp and Van Mieghem (2015), including complete-graph calculations and survival-time exponential approximations. Schapira and Valesin (2015 preprint) establish exponential extinction-time behavior in graph-size asymptotic regimes. Neither inspected full text states the **fixed-graph, high-\(\lambda\)** cut-permutation coefficient for the variance-to-mean-squared deficit. The general regeneration approach and finite-state perturbation tools are established methods; the identified cut-weighted first correction is the claim here, not the general existence of asymptotic expansions.

## Limitations

This is a theorem for finite fixed graphs under homogeneous Markov SIS recovery and infection rates. It does not cover non-Markov infectious lifetimes, heterogeneous edge rates, graphs whose size grows with \(\lambda\), or convergence in total variation. The degree of historical originality remains subject to broader independent literature review; a general finite-state Markov-chain singular perturbation theorem could, in principle, imply this as a specialized coefficient after additional calculation. No independent audit has been performed.

## References

- R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, Physical Review E 92 (2015), 032806. DOI: https://doi.org/10.1103/PhysRevE.92.032806.
- B. Schapira and D. Valesin, *Extinction time for the contact process on general graphs*, arXiv:1509.04133 (first posted 2015-09-14). https://arxiv.org/abs/1509.04133.
