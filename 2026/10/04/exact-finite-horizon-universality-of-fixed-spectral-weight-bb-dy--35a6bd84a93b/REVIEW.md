# Same-model review

## Correctness

PASS. The primary full text proves that the spectral map
\[
\mathcal S_W(u,v)=(W^{1/2}u,W^{1/2}v)
\]
is a bijection of the compatible cone and satisfies
\[
\mathcal S_WT_W=T_I\mathcal S_W.
\]
The proposed matched norm is exactly the pullback of the Euclidean product norm through this map. Therefore every corresponding orbit has the same normalized \(k\)-step gain for every \(k\), and taking the supremum over the cone preserves equality because the map is onto. The contraction-horizon and sharp-prefactor conclusions follow directly from equality of the whole gain sequence.

The source realization lemma was also inspected. It shows that every cone state is an actual consecutive-gradient state after an admissible warm-up, so no nonrealizable states enter the worst-case envelope.

## Originality

PASS. The primary paper states equality of homogeneous growth radii and gives only a condition-number sandwich for finite-horizon gains in a common Euclidean norm. A companion paper gives a common endpoint Lyapunov law, and the earlier sharp-rate paper transfers sharp asymptotic thresholds by spectral conjugacy. None of the inspected statements identifies exact horizon-by-horizon worst-case gain equality in the weight-matched norm or its exact finite-step contraction-horizon and best-prefactor consequences.

Targeted published-research searches over matched norms, transient profiles, finite-horizon gains, spectral conjugacy, BB1, BB2, and weighted delayed Rayleigh rules returned no equivalent statement. A residual risk remains because isometric pullback under linear conjugacy is a standard abstract principle; no optimization-specific statement applying it to this new compatible BB cone was found.

## Value

PASS. The primary convergence proof is itself organized around uniform finite-step contraction, while its spectral-weight transfer introduces a condition-number factor in Euclidean norm. The result isolates which part is intrinsic: after transporting the norm with the exact conjugacy, BB1, BB2, and every fixed positive spectral-weight rule share the complete sharp transient profile, not only the asymptotic exponent. This directly fixes the sharp contraction horizon and best prefactor in the matched metric and clarifies that any remaining weight dependence is metric-dependent rather than a loss in the conjugate dynamics.

Same-model review: passed. Independent audit: not yet performed.
