---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

In the finite-report information-theoretic benchmark (Eq. 21 of Ham–Zhao–Jasin–Yang), take positive report masses g_j summing to 1, nonnegative conditional KL gains d_1>=...>=d_m, I=I_R^(h)>=0, J=I+sum_j g_j d_j>0, positive c_AI,c_H, N>0 and T>=0. By the source Proposition 4.8 the concave frontier Psi(s) is affine on each [W_(q-1),W_q] and gives the exact information/cost segment between the AI-first breakpoint modes (I+D_q,c_AI+c_H W_q). Every feasible original triple maps to an LP combination of at most two adjacent AI modes plus a direct-human mode with identical information/cost. Conversely any finite-mode mixture aggregates to a feasible original triple with at least its LP information by concavity of Psi, so both optima coincide. Scale any positive-information solution to equality at T>0, include idle mass, and use the planar lower convex envelope L at x=T/N to obtain Gamma_h(T,N)=N L(T/N); T=0 gives cost zero. Every mode has information <=J and direct human attains J, giving infeasibility precisely at T>NJ. Every lower-hull point admits at most two non-idle endpoint modes. Strictly positive c_AI makes full AI-then-human at (J,c_AI+c_H) dominated by (J,c_H). In the nondegenerate regime 0<I<J, 0<c_AI<c_H, strict improvement over the pure AI/human chord is equivalent to some s>0 with Psi(s)/s>c_H(J-I)/(c_H-c_AI). This holds exactly when d_1 exceeds that threshold, proving c_AI/c_H<1-(J-I)/d_1. On each hull segment a x+b, N L(T/N)=aT+bN, so the outer positive-data-cost maximum is convex piecewise affine, with changes at transformed vertices N=T_h/K and crossings of simultaneously active affine pieces; integer neighbors plus the feasible lower boundary give the exact discrete minimum. Exact rational finite tests independently corroborated 694 nonzero-target inner LP instances, 316 nondegenerate selective-threshold instances, and 160 two-direction outer examples. These are checks, not unrestricted proofs.

## originality

PASS

Best-of-knowledge comparison finds that the initiating paper supplies the sorted fractional-knapsack frontier and labels Eq. (21) a convex program (Proposition 4.10); it does not state in the materially inspected definition/results/proof sections the explicit finite hull identity, universal two-mode support for this program, strict pure-source-chord criterion, or transformed-hull finite outer minimization. Classical LP/Caratheodory and perspective geometry are acknowledged as standard ingredients rather than claimed as newly invented. The nearest weak/strong-rating allocation paper uses an unbiased-mean estimation objective, not this report-dependent sequential KL threshold. Resultary searches returned the canonical published entry for this same assigned finding, not an independent earlier theorem dominating it. The novelty conclusion remains best-of-knowledge because the source-specific observation could appear in a differently indexed optimization treatment and the full other-rater paper was not materially read.

## value

PASS

The object is the primary paper’s own cost-information benchmark for validity-constrained sequential AI/human testing, not an arbitrary numerical slice. The exact finite-hull expression removes generic inner convex solves for all finite report alphabets, exposes at-most-two active sensing modes for the expected-count optimum and gives a sharp, interpretable condition for whether post-report escalation actually outperforms randomizing between pure AI and direct-human sensing. The transformed hull/crossing description similarly reduces the full two-direction integer lower-bound computation to a finite candidate set. These are reproducible design invariants a future investigator could use to analyze or implement this central benchmark. The proof uses standard LP facts, but its exact source-specific application and decision threshold supply mathematical motivation beyond merely restating convexity. No claim is made to improving the underlying testing-error lower bound or the adaptive policy itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
