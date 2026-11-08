---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all n>=4 and arbitrary symmetric nonnegative stochastic edge/diagonal supported P, convexity of the centered operator norm under dihedral conjugation gives a feasible invariant minimizer; the fixed point matrices are P(a,b)=(1-2a-b)I+a(S+S^-1)+bS^n, a,b>=0 and 2a+b<=1. Fourier characters yield lambda_j=1-2a(1-cos(pi*j/n))-b(1-(-1)^j), lambda_0=1. Let u=1-cos(pi/n), v=1-cos(2pi/n), w=2 if n odd and 2-u if n even, d=2v+w-u. Three unavoidable spectral constraints lambda_1<=mu, lambda_2<=mu and -lambda_(n if odd else n-1)<=mu have positive multipliers v/d,(w-u)/d,v/d; they sum to one and cancel both a,b, proving mu>=(w-u)/d globally. Equality forces all active constraints and gives unique invariant optimum a=1/d,b=(v-u)/d, mu=(w-u)/d. Feasibility: v>u>0, w>u, holding r=(v+w-2)/d equals v/d (odd) or (v-u)/d (even), positive. Every odd-mode s_j lies [u,w], so its eigenvalues interpolate between +mu and -mu. Every nonstationary even-mode s_j lies [v,2-u] (odd n) or [v,2] (even n), and its minimum lies mu+lambda_even_min=2v/d or 2(v-2u)/d; the latter is positive since v-2u=2u(1-u)>0 for even n>=4. All other modes are controlled. At odd n the unlazy 1/3-each-edge walk has eigenvalue -1 (bipartite); at even n its SLEM equals 1-2u/3. Taylor expansions u~pi^2/(2n^2), v~2pi^2/n^2 give optimal gap~2pi^2/n^2 and even-parity spectral gap ratio to baseline ->6. Independently formed actual 2n-by-2n matrices, Fourier spectra, and full-mode SciPy LPs for each n=4,...,54; worst absolute deviations were 3.56e-15 (spectrum), 2.23e-16 (LP mu), 1.18e-16 (weights), and 2.23e-16 (heuristic). The infinite claim rests on the analytic inequalities, not these finite tests or a saved VERIFY_OK log.

## originality

PASS

Best-of-knowledge novelty of the evaluated two-edge-orbit, all-size SLEM optimum for Möbius ladders n>=4, including sharp three-active-mode certificate and even/odd heuristic comparison. This is not a new general FMMC method. Boyd/Diaconis/Xiao (2004) already give convex/SDP definition and dual framework; Boyd/Diaconis/Parrilo/Xiao (2005) study reversible-chain symmetry and orbit bounds; the 2007 arXiv/2009 journal symmetry paper proves group averaging and Fourier decomposition, and solves edge-transitive graphs, Cartesian products, wheels, K_(m,n), etc. Its theorem 3.1 cannot be directly applied to n>=4 Möbius ladders because rim and antipodal edges have different four-cycle counts (one and two); n=3 reduces to K_3,3 and is already covered. The Möbius ladder is not C_n Cartesian K_2 (bipartite parity differs). The general two-orbit SDP does not itself specify this three-mode sharp optimum. Exact parameterized formula absent from the inspected relevant portions and targeted full-document searches of primary materials and from bounded independent web/Resultary searches. Discovery of a specialized older paper would change priority; absence from a search alone is not proof.

## value

PASS

Möbius ladders are standard, natural cubic networks containing a cycle and diametral interconnections, with two inequivalent physical edge types and a natural uniform-stationary reversible-walk design question. The exact minimax SLEM for all n>=4 is not a tiny arbitrary instance: a sharp global solution for a full graph family not covered by the one-edge-transitive formula. The parity obstruction makes unlazy equal-edge walks nonconvergent for odd n while explicit laziness restores mixing, and in even n the leading spectral-gap coefficient improves by factor six. The all-size exact weights and uniqueness within the two-orbit invariant class can inform reversible consensus and Markov-chain edge-weight design. This is an independently meaningful graph-spectral invariant, though not an optimal finite-time total-variation mixing theorem or a novel SDP technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
