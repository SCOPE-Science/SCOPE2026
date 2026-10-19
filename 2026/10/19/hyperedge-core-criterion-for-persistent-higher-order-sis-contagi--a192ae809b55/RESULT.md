# Hyperedge-core criterion for persistent higher-order SIS contagion

## Finding

**Theorem (Boolean support and all-rate extinction).** For the finite purely higher-order directed SIS system defined below, let \(T\) be the Boolean hyperedge-activation operator and let \(K\) be its largest fixed point. Every equilibrium support is a fixed point of \(T\); conversely, for every fixed-point support \(S\), an equilibrium with *exactly* support \(S\) exists at every sufficiently high common infection scale, simultaneously across all such supports. If \(K=\varnothing\), infection tends to zero globally at a stated exponential-with-polynomial rate for **every** positive infection scale (with a valid Euler step). If \(K\ne\varnothing\), a nonzero equilibrium exists for all sufficiently high scales. Thus emptiness of a finite, weight-independent, iteratively computable core is necessary and sufficient for global extinction at every transmission scale.

## Assumptions and scope

Let \(V=\{1,\ldots,n\}\) be nonempty and finite. At each target \(i\), let \(\mathcal E_i\) be a finite collection (possibly empty) of pairs \((J,b)\), where \(J\subseteq V\setminus\{i\}\), \(|J|\ge2\), and \(b>0\). Multiple incoming hyperedges are permitted, as are differing hyperedge orders. Assume recovery \(\delta_i>0\) and a common transmission scale \(\tau>0\). Put
\[
 P_i(x)=\sum_{(J,b)\in\mathcal E_i}b\prod_{j\in J}x_j,
 \qquad L_i=\sum_{(J,b)\in\mathcal E_i}b,
 \qquad L=\max_i L_i.
\]

For an Euler step \(h\) satisfying \(0<h<1/\max_i(\delta_i+\tau L_i)\), the update is
\[
 x_i(t+1)=x_i(t)+h\{-\delta_i x_i(t)+\tau[1-x_i(t)]P_i(x(t))\},
 \qquad x(0)\in[0,1]^n.
\]
The restriction is a sufficient positivity/invariance condition and may require decreasing \(h\) when \(\tau\) changes. These are deterministic mean-field infection probabilities, not sample paths of a finite-state stochastic SIS chain. No dyadic transmission is allowed; this restriction is essential.

For \(S\subseteq V\), define
\[
 T(S)=\{i\in V:\exists(J,b)\in\mathcal E_i\text{ with }J\subseteq S\}.
\]
Start at \(V_0=V\), and set \(V_{k+1}=T(V_k)\). These sets decrease and stabilize after at most \(n\) strict deletions, at \(K=T(K)\). Define the finite bound
\[
 \tau_*=\max\bigl(\{2^{|J|}\delta_i/b:(J,b)\in\mathcal E_i,\ i\in V\}\cup\{0\}\bigr).
\]

## Proof

**Invariant cube.** Write the update as \(x'_i=(1-h\delta_i)x_i+h\tau P_i(x)(1-x_i)\). Since \(0\le P_i(x)\le L_i\) for \(x\in[0,1]^n\), both terms are nonnegative, while
\(x'_i\le(1-h\delta_i)x_i+h\tau L_i(1-x_i)\le1\): the last expression is a convex interpolation between numbers \(1-h\delta_i\) and \(h\tau L_i\), each in \([0,1]\). Thus \([0,1]^n\) is forward invariant.

**Equilibrium supports.** At any equilibrium, the factor \(h>0\) cancels and
\[
 x_i=\Phi_i(x):=\frac{\tau P_i(x)}{\delta_i+\tau P_i(x)}.
\]
Strictly positive weights imply \(P_i(x)>0\) if and only if some incoming parent set \(J\) lies entirely in \(S=\{j:x_j>0\}\). Consequently \(S=T(S)\). Conversely fix any \(S=T(S)\) and let \(q_i=1/2\) for \(i\in S\), with \(q_i=0\) elsewhere. If \(i\notin S\), no parent set lies in \(S\), so \(\Phi_i(q)=0\). If \(i\in S\), there is an incoming \((J,b)\) with \(J\subseteq S\), giving \(P_i(q)\ge b2^{-|J|}\), whence \(\tau\ge\tau_*\) gives \(\Phi_i(q)\ge1/2=q_i\). The map \(\Phi\) is continuous and coordinatewise nondecreasing on \([0,1]^n\), because each \(P_i\) has nonnegative coefficients and \(z\mapsto\tau z/(\delta_i+\tau z)\) increases. Therefore \(q,\Phi(q),\Phi^2(q),\ldots\) increases coordinatewise and is bounded by \(\boldsymbol1\); its limit \(x^S\) is a fixed point. By induction all coordinates outside \(S\) remain zero, while each inside stays at least \(1/2\). This is the desired equilibrium, for each fixed \(S\), at the *same* \(\tau\ge\tau_*\). The empty set gives the disease-free equilibrium at all scales.

**Largest support core.** The operator \(T\) is monotone: \(S\subseteq R\) implies \(T(S)\subseteq T(R)\). Since \(V_1\subseteq V_0\), induction yields \(V_{k+1}\subseteq V_k\). Every fixed point \(S=T(S)\) is contained in every \(V_k\), hence in \(K\). Conversely \(K\) is itself fixed. Thus \(K\) is the unique greatest fixed point and equals the union of all equilibrium supports whenever \(\tau\ge\tau_*\).

**Global all-rate extinction for an empty core.** Fix any \(\tau>0\) and a valid \(h\), put \(\rho=\max_i(1-h\delta_i)\in(0,1)\) and \(W_k=V\setminus V_k\). If \(K=\varnothing\), there exists \(m\le n\) with \(V_m=\varnothing\). For \(i\in W_1\), no incoming hyperedges are present, so \(x_i(t)=(1-h\delta_i)^t x_i(0)\le\rho^t\).

Inductively suppose \(x_i(t)\le C_k(1+t)^{k-1}\rho^t\) for all \(i\in W_k\), all integer \(t\ge0\), with \(C_1=1\). If \(i\in W_{k+1}\setminus W_k\), every incoming parent set intersects \(W_k\), otherwise \(i\in T(V_k)=V_{k+1}\). Since all coordinates are at most one,
\[
 P_i(x(t))\le L_i\max_{j\in W_k}x_j(t)\le L C_k(1+t)^{k-1}\rho^t.
\]
For these newly deleted coordinates, \(x_i(t+1)\le \rho x_i(t)+h\tau L C_k(1+t)^{k-1}\rho^t\). Unrolling and bounding \(\sum_{s=0}^{t-1}(1+s)^{k-1}\le t^k\) yields
\[
 x_i(t)\le\rho^t\left[1+\frac{h\tau L C_k}{\rho}t^k\right]\le C_{k+1}(1+t)^k\rho^t,
 \qquad C_{k+1}:=1+\frac{h\tau L}{\rho}C_k.
\]
For \(i\in W_k\), the old bound is at most the new one. Induction proves
\[
 \|x(t)\|_\infty\le C_m(1+t)^{m-1}\rho^t\longrightarrow0.
\]
(The case \(m=1\) uses \(C_1=1\).) If \(K\ne\varnothing\), the preceding support construction applied to \(S=K\) gives a nonzero equilibrium for all \(\tau\ge\tau_*\), disproving global extinction at every scale. This proves the equivalence.

## Verification

Run `python3 verify.py` in the same directory. The script enumerates all \(2^{12}=4096\) directed pure-triadic edge patterns on four labeled vertices, all their Boolean fixed supports, the greatest fixed point, and the explicit half-density subsolution with rationally representable parameter values. It additionally tests the peeling estimate on a five-vertex layered directed network. These finite checks confirm the implementations and sample cases, not the theorem for arbitrary finite \(n\), which follows from the proof.

## Relationship to prior work

Liang, Cui and Liu (arXiv:2408.08602v1, Sections 2, 3 and 6 and Appendix 9.8) derive a discrete-time directed-hypergraph mean-field SIS map and spectral/large-infection sufficient conditions for equilibria under an irreducible pairwise layer. Their Proposition 8 gives a rate-dependent sufficient extinction condition; Proposition 9 gives an all-coordinate-positive endemic equilibrium under an explicit large-rate condition. Neither statement classifies arbitrary **partial** supports or yields a rate-independent, necessary-and-sufficient directed hyperedge-peeling test when the pairwise layer is absent. Their Section 6 permits arbitrary order, as used here. Cui et al. (arXiv:2306.00619v3, Theorems 3, 8) study continuous-time direct-and-indirect spreading with spectral bounds and irreducible monotone systems rather than the present purely higher-order reducible support classification. Prior spectral thresholds for hypergraph epidemics apply to differing interaction assumptions and do not supply this Boolean criterion. The argument uses standard monotone-map reasoning, but the complete support/peeling equivalence is specific to this contagion family.

## Limitations

The result concerns finite deterministic SIS mean-field updates with nonnegative mass-action hyperedge monomials and **no** pairwise terms, spontaneous infection, or self-containing parent sets. It neither gives endemic local attraction, an exact finite-rate invasion threshold, nor extinction for an individual finite-state stochastic SIS realization with absorbing disease-free state. The explicit \(\tau_*\) is sufficient, not generally minimal. Hyperedge-core nonemptiness need not yield an endemic equilibrium at low transmission, and the bound can be loose. It does not classify trajectories when \(K\ne\varnothing\). Related monotone Boolean/autocatalytic-network theory might provide a more general statement; detailed cross-field comparison remains an originality risk.

## References

1. L. Liang, S. Cui, and F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602v1, first posted 2024-08-16, https://arxiv.org/html/2408.08602v1 (Sections 2, 3, 6 and 9.8).
2. S. Cui, F. Liu, H. Jardón-Kojakhmetov, and M. Cao, *General SIS diffusion process with indirect spreading pathways on a hypergraph*, arXiv:2306.00619, first posted 2023-06-01, https://arxiv.org/html/2306.00619v3 (Theorems 3 and 8).
3. D. J. Higham and H. de Kergorlay, *Epidemics on Hypergraphs: Spectral Thresholds for Extinction*, arXiv:2103.07319 (background spectral comparison).
