# A sharp second-moment blind spot in anonymous two-habitat occupancy

## Finding
Consider two independent, stationary, continuous-time habitat-occupancy chains. Patch \(i\) is recolonized at rate \(c_i>0\) when empty and becomes empty at rate \(e_i>0\) when occupied. Only the aggregate occupied-patch count \(N(t)\in\{0,1,2\}\), not either patch label, is recorded. Put \(\lambda_i=c_i+e_i\) and \(p_i=c_i/\lambda_i\). The exact stationary mean \(m=\mathbb E N(t)\) and complete autocovariance function \(C(t)=\operatorname{Cov}(N(0),N(t))\), for all \(t\ge0\), identify the unordered pair of parameter pairs \(\{(c_1,e_1),(c_2,e_2)\}\) **except** when \(\lambda_1\ne\lambda_2\), \(p_1+p_2=1\), and \(p_1\ne p_2\). In this exceptional family there are exactly two inequivalent parameter assignments with identical first- and second-order temporal moments. The single additional third-order stationary moment
\[
H(t_0)=\mathbb E\big[(N(0)-m)^2(N(t_0)-m)\big],\qquad t_0>0,
\]
separates those two assignments, so \((m,C(\cdot),H(t_0))\) identifies all rates up to exchange of the habitat labels for **every** positive choice of rates. The exceptional ambiguity is genuine and sharp.

## Assumptions and scope
The two sites are independent, homogeneous in time, and initially in their unique stationary laws; all four transition rates are strictly positive, so \(0<p_i<1\). Their states are exactly observed only through \(N(t)\). Identification refers to *population-level exact moment functions* rather than finite-data statistical recovery. Time is continuous, \(t\ge0\), and the fixed extra lag \(t_0\) is any strictly positive real. Permutation of the two unobserved habitat labels is not distinguishable and is disregarded.

## Proof
For each site, the two-state transition formula gives
\[
\mathbb E[Z_i(t)-p_i\mid Z_i(0)]=(Z_i(0)-p_i)e^{-\lambda_i t},
\qquad \operatorname{Var}(Z_i(0))=v_i=p_i(1-p_i)>0.
\]
Independence and stationarity therefore give the exact identities
\[
m=p_1+p_2,\quad C(t)=v_1e^{-\lambda_1t}+v_2e^{-\lambda_2t},\quad
H(t)=v_1(1-2p_1)e^{-\lambda_1t}+v_2(1-2p_2)e^{-\lambda_2t}.
\tag{1}
\]
Indeed, with centered \(Y_i=Z_i-p_i\), terms in \(\mathbb E[(Y_1(0)+Y_2(0))^2(Y_1(t)+Y_2(t))]\) containing an unpaired centered variable from the other independent site vanish. Its surviving single-site term is \(e^{-\lambda_i t}\mathbb E[Y_i(0)^3]=e^{-\lambda_i t}v_i(1-2p_i)\).

Because all \(v_i>0\), uniqueness of finite exponential sums with distinct real exponents (or partial fractions of their Laplace transforms) recovers the distinct \(\lambda_i\) and their attached weights \(v_i\) from \(C(\cdot)\). If the two rates coincide at \(\lambda\), the covariance is \(We^{-\lambda t}\), where \(W=v_1+v_2\). In that case \(m\) and \(W\) recover \(p_1,p_2\) as the unordered roots of
\[
X^2-mX+\frac{W-m+m^2}{2}=0.
\]
As \(\lambda_1=\lambda_2=\lambda\), both rate pairs then follow from \(c_i=\lambda p_i\), \(e_i=\lambda(1-p_i)\).

Suppose next that \(\lambda_1\ne\lambda_2\). Attach each recovered weight \(v_i\) to the corresponding recovered \(\lambda_i\). The equation \(p_i(1-p_i)=v_i\) leaves exactly the alternatives \(p_i=\frac12\pm a_i\), where \(a_i=\sqrt{\frac14-v_i}\ge0\). The four signed sums \(1\pm a_1\pm a_2\) have a collision between *different actual parameter assignments* only when \(a_1=a_2>0\) and the signs are opposite. Then \(p_1+p_2=1\), \(p_1\ne p_2\), and swapping the two probabilities **without swapping the distinct recovered rate labels** gives the unique second assignment. Conversely these two assignments have the same \(m\) and \(C(t)\) by (1), proving necessity, sufficiency and the twofold size of the blind spot.

In that exceptional class, write \(p_2=1-p_1\), \(v=p_1(1-p_1)>0\). Then (1) reduces to
\[
H(t_0)=v(1-2p_1)\big(e^{-\lambda_1t_0}-e^{-\lambda_2t_0}\big).
\]
Every factor on the right is nonzero for \(t_0>0\); the other admissible assignment negates its sign. Thus any one such third-order moment selects the correct assignment. This completes identification in all cases.

For a concrete sharp witness, choose \((\lambda_1,\lambda_2)=(2,5)\) and \((p_1,p_2)=(1/4,3/4)\). The rates are \((c_1,e_1)=(1/2,3/2)\), \((c_2,e_2)=(15/4,5/4)\). Keeping \(\lambda_1,\lambda_2\) fixed but exchanging \(p_1,p_2\) yields instead \((3/2,1/2)\) and \((5/4,15/4)\), not obtainable by exchanging whole habitat labels. Both have \(m=1\) and
\[
C(t)=\frac3{16}(e^{-2t}+e^{-5t}),
\]
whereas their \(H(t)\) values are opposite and nonzero for every \(t>0\): \(\pm\frac3{32}(e^{-2t}-e^{-5t})\).

## Verification
The accompanying standalone \(\texttt{CHECK.py}\) uses exact rational arithmetic to expand the two-patch, two-time joint law and check (1) for 90 parameter combinations, its stationary zero-state mass, the explicit twofold counterexample, 16 equal-rate reconstruction instances, and four third-order sign separations. Run \(\texttt{python3 CHECK.py}\) using Python's standard library. These finite checks independently test the identities; the proof above, rather than the experiments, supplies all-parameter identification and sharpness.

## Relationship to prior work
Royle and Kéry (2007) provide the ecological motivation for separating habitat occupancy, recolonization and extinction in dynamic site-occupancy models. Rydén (1996) and Larget (1998) consider identifiability of much more general aggregated Markov processes from their *observable laws*. Bernstein and Sheldon (2016) prove second-order identification and estimation for aggregated populations of independent individuals sharing a **common** Markov transition matrix (see their model statement and Proposition 1). Here the two patches may have distinct transition generators, and the question is deliberately limited to the exact information in the mean and all autocovariances, with one explicitly characterized exceptional twofold ambiguity and a minimal additional third-order resolution. Identifiability from a full observed law alone does not imply this specific moment hierarchy. The mathematical ingredients of exponential-mixture uniqueness and Bernoulli cumulants are classical; no claim is made for their invention.

## Limitations
Neither finite sample statistical consistency nor robustness to observation error, correlated patches, nonstationary rates, more than two patches, or discrete sampling at only finitely many lags is asserted. The inverse reconstruction may be badly conditioned when relaxation rates approach one another or occupancy probabilities approach one half. General aggregated-Markov equivalence research is a substantial prior-coverage risk: in particular, complete text of the closest broad works by Rydén and Larget was not available for a decisive appendix-level exclusion of an equivalent special-case formula.

## References
- Royle, J. A., and Kéry, M. (2007). A Bayesian state-space formulation of dynamic occupancy models. *Ecology* 88, 1813–1823. DOI: 10.1890/06-0669.1. First published July 1, 2007.
- Rydén, T. (1996). On identifiability and order of continuous-time aggregated Markov chains, Markov-modulated Poisson processes, and phase-type distributions. *Journal of Applied Probability* 33, 640–653. DOI: 10.2307/3215346.
- Larget, B. (1998). A canonical representation for aggregated Markov processes. *Journal of Applied Probability* 35, 313–324. DOI: 10.1239/jap/1032192850.
- Bernstein, G., and Sheldon, D. (2016). Consistently estimating Markov chains with noisy aggregate data. *Proceedings of AISTATS*, PMLR 51, 1142–1150. https://proceedings.mlr.press/v51/bernstein16.pdf.
