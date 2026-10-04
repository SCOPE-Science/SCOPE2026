# Same-model review of: A positive-parameter counterexample to a coexistence shortcut in a prey-taxis model

## Correctness
**PASS.** The equilibrium reduction was reconstructed from the source rather than inferred from a numerical plot. The exact parameter tuple satisfies the printed hypotheses \(r>\beta_1\eta\), \(\gamma_1>\beta_2\), and \(\beta<C_1\). It yields \(L=-11/10\), \(L_0=0\), \(U=9/10\), and
\[
f(u)=-u^2-\frac{u}{5}-\frac{341}{100}<0\qquad (u>0).
\]
Hence no root lies in \((L_0,U)\). The source's proof explicitly identifies admissible coexistence equilibria with roots in that interval. Exact arithmetic is replayed by `verify.py`.

## Originality
**PASS.** Direct inspection of Liu and Tan's Section 3 shows the precise statement/proof mismatch: the theorem and its ecological shortcut use \(L\), whereas the positivity derivation and proof use \(L_0=\max\{0,L\}\). DOI-, theorem-, alias-, endpoint-, and conclusion-targeted published-finding corpus searches did not locate a covering statement. The closest published records concern different predator–prey, reaction–diffusion, or memory models and do not imply this counterexample. A related 2025 memory-diffusion/fear article was accessible only at abstract level; this is a residual access risk, but its distinct model does not create a decisive unresolved comparison.

## Value
**PASS.** The issue changes the predicted number of positive coexistence equilibria for an admissible positive-parameter regime. Since later local stability and bifurcation calculations presuppose such an equilibrium, a reliable existence classification is mathematically consequential. The result supplies a sharp diagnostic and the necessary endpoint correction for the sign-change step while avoiding claims about unrelated parameter regimes.

## Closest literature and limitations
The closest inspected literature treats different memory-based predator–prey or cognitive-taxis systems. This finding is intentionally limited to the printed weak-Allee coexistence shortcut and the lower endpoint used in its proof. It does not claim a complete replacement for all of Theorem 3.1(b), nor does it reassess the source's numerical bifurcation examples.

Same-model review: passed. Independent audit: not yet performed.
