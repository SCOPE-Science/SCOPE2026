# No-outbreak blocks remove the atom assumption and force uniform mixing

## Finding
For the multi-season epidemic Markov chain of Britton and Pugliese, fix an integer \(r\ge 2\). Let the seasonal pairs \((\delta_k,\tau_k)\) be iid with \(0\le\delta_k\le1\) and \(\tau_k\ge0\), and put
\[
\beta=\mathbb P(\tau_k<1).
\]
If \(\beta>0\), then the atom at \(\delta=1\) used in Proposition 2.1 is unnecessary, as is any density assumption. With \(m=r-1\), the \(m\)-season transition kernel obeys a global minorization
\[
P^m(x,A)\ge \beta^m\nu(A)
\]
for every state \(x\) and measurable set \(A\), for a probability law \(\nu\) independent of \(x\). Therefore the chain has a unique stationary law \(\pi\) and, using \(d_{\mathrm{TV}}(\mu,\eta)=\sup_A|\mu(A)-\eta(A)|\),
\[
d_{\mathrm{TV}}(\mu P^n,\eta P^n)
\le
(1-\beta^m)^{\lfloor n/m\rfloor}d_{\mathrm{TV}}(\mu,\eta)
\]
for all probability laws \(\mu,\eta\) and all integers \(n\ge0\). In particular,
\[
d_{\mathrm{TV}}(P^n(x,\cdot),\pi)
\le
(1-\beta^m)^{\lfloor n/m\rfloor}.
\]
Thus a run of low-transmissibility seasons is a common regeneration block that removes all dependence on the incoming immunity state.

## Assumptions and scope
The state before season \(k\) is \(X_k=(\mathbf p^{(k)},\boldsymbol\iota^{(k)})\), where \(\mathbf p^{(k)}=(p_1^{(k)},\ldots,p_r^{(k)})\) records time since last infection and \(\boldsymbol\iota^{(k)}=(\iota_1^{(k)},\ldots,\iota_{r-1}^{(k)})\) records immunity, with \(\iota_1^{(k)}=1\). The source model assumes iid seasonal marks \((\delta_k,\tau_k)\); dependence between \(\delta_k\) and \(\tau_k\) within one season is allowed and remains allowed here.

Only \(\beta=\mathbb P(\tau<1)>0\) is required. The result does not require a point mass at complete genetic drift, continuity of the mark law, or independence of drift and transmissibility within a season. The theorem concerns the Markov chain exactly as defined in the source, including the finite-memory rule that immunity is completely lost after \(r\) seasons.

## Proof
For every immunity class, \(0\le\iota_j\le1\) and \(0\le\delta\le1\), so
\[
0\le 1-(1-\delta)\iota_j\le1.
\]
The source's effective reproduction number therefore satisfies
\[
R_e
=
\tau\sum_{j=1}^r p_j\bigl(1-(1-\delta)\iota_j\bigr)
\le \tau.
\]
Hence every season with \(\tau<1\) has \(R_e<1\), and the source final-size rule gives no outbreak: \(z_j=0\) for all \(j\).

During a no-outbreak season the population update reduces to
\[
p_1'=0,
\qquad
p_j'=p_{j-1}\quad(2\le j<r),
\qquad
p_r'=p_r+p_{r-1}.
\]
After exactly \(m=r-1\) consecutive no-outbreak seasons, repeated shifting therefore gives
\[
\mathbf p=(0,\ldots,0,1)
\]
regardless of the incoming population vector.

The immunity update is
\[
\iota_1'=1,
\qquad
\iota_j'=(1-\delta)\iota_{j-1}\quad(2\le j\le r-1).
\]
Label the drifts in an \(m\)-season block by \(\Delta_1,\ldots,\Delta_m\). At the end of the block,
\[
\iota_j
=
\prod_{\ell=m-j+2}^m(1-\Delta_\ell),
\qquad 2\le j\le r-1,
\]
which depends only on marks inside the block and not on the incoming state. For \(r=2\), there are no such products and the immunity vector is simply \(\iota_1=1\).

Let
\[
E=\{\tau_1<1,\ldots,\tau_m<1\}.
\]
The seasonal pairs are iid, so \(\mathbb P(E)=\beta^m\). On \(E\), the terminal state is a measurable function only of the block's seasonal marks. Let \(\nu\) be its conditional law given \(E\). For every initial state \(x\),
\[
P^m(x,A)
\ge
\mathbb P_x(E, X_m\in A)
=
\beta^m\nu(A).
\]
This is a global Doeblin minorization with \(\alpha=\beta^m\).

If \(0<\alpha<1\), write
\[
P^m(x,\cdot)=\alpha\nu(\cdot)+(1-\alpha)Q_x(\cdot)
\]
for a Markov kernel \(Q\). Then for any probability laws \(\mu,\eta\),
\[
d_{\mathrm{TV}}(\mu P^m,\eta P^m)
\le
(1-\alpha)d_{\mathrm{TV}}(\mu,\eta).
\]
The space of probability measures is complete in total variation, so the contraction has a unique fixed probability law \(\pi_m\) for \(P^m\). Moreover \(\pi_mP\) is also fixed by \(P^m\); uniqueness gives \(\pi_mP=\pi_m\). Thus \(\pi=\pi_m\) is the unique stationary law for \(P\). If \(\alpha=1\), all states have the same \(m\)-step law and the same conclusion is immediate.

Writing \(n=qm+s\) with \(0\le s<m\), applying the contraction \(q\) times and using nonexpansiveness of a Markov kernel in total variation yields
\[
d_{\mathrm{TV}}(\mu P^n,\eta P^n)
\le
(1-\alpha)^q d_{\mathrm{TV}}(\mu,\eta),
\]
which is the stated bound.

## Verification
The proof is symbolic and uses only the displayed transition rules from the source. The included `verify.py` independently checks, with exact rational arithmetic, that for several values of \(r\) two different incoming population/immunity states coalesce after \(r-1\) common no-outbreak updates and that the resulting immunity vector matches the product formula above. The computation is a consistency check; the theorem for arbitrary \(r\) is established by the preceding algebra, not by finite enumeration.

## Relationship to prior work
Britton and Pugliese prove qualitative convergence in Proposition 2.1 under a continuous-density assumption plus an atom at \(\delta=1\). Their proof uses repeated complete-drift seasons to reach a single immunity-free state. Immediately after the proposition they explicitly note that the atom assumption may possibly be removable, while separately observing that it is unnecessary when \(r=2\).

The result here proves that removal for every \(r\ge2\). The key distinction is to use a common *random* terminal state after \(r-1\) low-transmissibility seasons rather than forcing a deterministic immunity-free state. Standard global-minorization theory explains why such a minorization yields uniform geometric convergence; the model-specific contribution is the \(r-1\)-season coalescence mechanism and the explicit constant \(\beta^{r-1}\).

Searches of the source title and identifier together with `Doeblin`, `uniform ergodicity`, `geometric mixing`, `atom assumption`, `no-outbreak block`, and \(r-1\) did not locate this statement. Searches of the published mathematical-finding database for the same model and equivalent regeneration/minorization formulations likewise found no covering result.

## Limitations
The bound is sufficient and need not be the optimal mixing rate. It uses only blocks in which every transmissibility is below one; other state-dependent paths may couple faster. The theorem assumes iid seasonal pairs exactly as in the source. It does not cover the source's brief discussion of dependence *between* seasons without further argument. No claim is made about statistical estimation of \(\beta\) from epidemic data.

## References
1. T. Britton and A. Pugliese, *A multi-season epidemic model with random genetic drift and transmissibility*, Journal of Mathematical Biology 91, 80 (2025), DOI 10.1007/s00285-025-02308-8; preprint arXiv:2505.17933.
2. *Convergence rates of Metropolis–Hastings algorithms*, WIREs Computational Statistics (2024), DOI 10.1002/wics.70002, for the standard implication from global minorization to uniform ergodicity.
