# Independent mathematical audit

## correctness

PASS

PASS. The specified deterministic Mime+SGD control variate for a quadratic f_i(y)=1/2 y^T H_i y-q_i^T y reduces exactly to g_i(y)=H_i(y-x)+c, where c is the broadcast full gradient. The first two local iterates average as x−kηc+binom(k,2)η² Hbar c for k=1,2, identical to two centralized GD steps. At k=3 the noncommuting-matrix expansion leaves only −η³[(1/m)Σ_i H_i²−Hbar²]c=−η³[(1/m)Σ_i(H_i−Hbar)²]c. Each H_i symmetric, so c^T(average−center)=−η³/m Σ_i||(H_i−Hbar)c||²≤0 (for η>0). The assertion is gradient-aligned, not an unconditional improvement in objective. Direct exact rational 2x2 noncommuting test agrees; a scalar two-client example yields central 64/125 and Mime 51/100 after step 3, defect −1/500. All equalities are polynomial identities valid regardless of convexity beyond the source's symmetric-quadratic hypothesis. No finite experiment was mistaken for proof.

## originality

PASS

Best-of-knowledge PASS for the **specific first nonzero average defect at step three and its exact Hessian-variance coefficient**, not for Mime, its control variate, generic client drift, or Hessian-similarity theory. Karimireddy et al. define precisely the used corrected gradient and prove generic perturbation/communication convergence, but the inspected Algorithm 1, Theorem I and Hessian-similarity appendices do not state the exact K=1,2 cancellation or the K=3 coefficient. Resultary and targeted alias queries returned related curvature and federated-method claims, not an implication-equivalent expansion. A later different-name expansion remains possible.

## value

PASS

PASS, though narrow. The exact first onset time of averaged curvature drift is a motivated mechanism question for a named control-variate algorithm: a practitioner can choose 1–2 local steps without this deterministic quadratic average bias, while a third step introduces a computable PSD matrix acting on the broadcast gradient. It is a structural finite-step identity, not a generic stochastic convergence theorem or a new algorithm. The equality cases and direction distinguish it from mere Taylor expansion without a phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
