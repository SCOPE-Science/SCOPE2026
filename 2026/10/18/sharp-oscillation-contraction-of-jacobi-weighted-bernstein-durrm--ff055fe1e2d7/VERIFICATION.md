---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The claimed domain is integer n>=1, a,b>0, bounded Borel real observables and fixed-parameter n->infinity; the operator is a beta-binomial Markov transition, not the ordinary Bernstein point-evaluation polynomial. For x<z, binomial weights are TP2 in (x,k) and beta densities q_{a+k,b+n-k} are TP2 in (k,y), so composing them gives a monotone-likelihood-ratio family with one density crossing. Stochastic monotonicity of every conditional beta CDF and Bin(n,x) then bounds F_x-F_z by F_0-F_1 pointwise, proving both the Dobrushin oscillation supremum and endpoint optimizer. The two beta endpoint densities have likelihood ratio proportional to (y/(1-y))^n, with unique crossing c_n=R_n^{1/n}/(1+R_n^{1/n}), R_n=B(n+a,b)/B(a,n+b). Integration gives the two incomplete-beta differences. Gamma ratios yield c_n=1/2+((a-b)log n+logGamma(b)-logGamma(a))/(4n)+o(1/n); one-sided Laplace bounds near this moving endpoint yield each overlap tail asymptotic to 2^{1-a-b}n^{(a+b)/2-1}2^{-n}/sqrt(Gamma(a)Gamma(b)), so their sum gives the announced prefactor. Reversibility and conditional beta factorial moments give lambda_1=n/(n+a+b), already a known spectral eigenvalue, not an originality claim. Independent SciPy beta-function checks at four parameter choices, including n=1,2,8,100, satisfy endpoint total-variation and overlap identities to numerical tolerance. Script reads confirm that 527 reported tests are finite; they cannot prove all n,a,b or historical novelty. No assertion of uniform asymptotics as a or b tend to zero, or of multistep mixing.

## originality

PASS

Jacobi L2 eigenvalues, positive approximation and shape variation do not logically imply a sharp operator oscillation/Dobrushin norm. Independent primary-section comparison found a distinct mathematical optimization over two Markov input locations, a beta-tail overlap, and its gamma-dependent n->infinity coefficient. The 1995 Adell–de la Cal abstract concerns TV between measures for convergence of Bernstein–Durrmeyer to a Szász kernel, not an identified exact x-vs-z Dobrushin coefficient; unread full text remains a priority risk. Failed searches are not novelty proof.

## value

PASS

For this natural Markov averaging kernel, the sharp oscillation contraction coefficient is the exact worst-case one-step propagation of bounded-observable error. Proving boundary extremizers for all asymmetric Jacobi beta parameters is a structural statement; its gamma-weight prefactor quantifies an exponentially small overlap, sharply separating a different Banach-space norm from the known polynomial L2 spectral gap. The invariant is canonical, parameterized, nontrivial, and not a renaming of the spectral eigenvalue; no claim is made about iteration or arbitrary dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
