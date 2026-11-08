---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Differentiate log Psi(s) including B'(s): Psi'/Psi = -q(s/c)/(c(1+s/c)^2), and omega1=-Psi'(1/h)/h; differentiating q gives q'(x)=(x+1)(ax-b)/x^2 with unique global minimizer x=b/a and q→+infinity at both endpoints. Hence 0/1/2 simple positive roots depending on Theta and precise sign intervals for all h. Strictly increasing Psi on [s_-,s_+] rules out a nonnegative inverse Laplace kernel; positivity of Psi rules out an all-nonpositive kernel under existence/integrability premise from prior Scarpi theory. Any positive SOE transform F(s)=sum p_j/(s+lambda_j) is decreasing, so endpoint triangle inequality gives error >=(Psi(s_+)-Psi(s_-))/2, and F_lambda=M*lambda/(s+lambda) attains the limit. Taylor near the nondegenerate minimum yields square-root opening. Independent high-precision root bracket and derivative/omega probes for a=0.2,b=0.8,c=10 reproduce Theta≈-0.2133276725 and the negative first lag. Correct limits: no assertion about later CQ coefficients, signed SOEs, or the source's discrete block compression.

## originality

PASS

Yuan–Zegeling introduced the exact exponential Scarpi symbol, backwards-Euler CQ weights and adaptive history compression. Previous variable-order kernel literature addresses existence/approximation and failure of monotonicity of related derivative kernels. The accessible abstract and mathematical related sources do not identify the explicit Theta phase diagram, unique sign-loss interval and sharp positive-Laplace-SOE minimax floor; main 2026 arXiv preprint full text was inaccessible in this run. An extremely relevant 2026 Scarpi approximated-kernel paper could not be read after lawful OA and authorized institutional attempts (VPN disconnected). Best-of-knowledge pass explicitly qualified by those access risks, no whole-document negative assertions.

## value

PASS

Gives a sharp operational boundary where the actual first CQ history weight becomes negative for a physically natural exponentially transitioning order, proves continuous sign-changing memory and establishes an unavoidable quantified obstruction for a precise useful nonnegative-SOE approximation class. Separating this from signed discrete history compression is mathematically essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
