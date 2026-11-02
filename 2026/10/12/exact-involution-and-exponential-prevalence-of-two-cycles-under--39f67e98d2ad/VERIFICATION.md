---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Checked exactly the submitted N>=1, finite undirected simple graph pairs, scalar J=-j with j>=0, Delta=max of both layer vertex degrees, synchronous binary sign updates, fair stochastic ties. Each intralayer sum lies in [-d_i,d_i]. For j>Delta the cross-layer term -j B_i (or -j A_i) strictly dominates every possible neighbor sum, so update equals (-B,-A) deterministically and F^2=Id for every microstate. Conversely at an all-positive pair of layers, a degree-Delta site has field Delta-j: positive for j<Delta and a fair tie at j=Delta, contradicting state-uniform deterministic identity (includes Delta=0,j=0). Fixed states solve A=-B, exactly 2^N; remaining 4^N-2^N microstates pair into (4^N-2^N)/2 disjoint strict cycles. For a site, A_i=B_i iff it flips, probability 2r(1-r); independent product initialization gives Binomial(N,2r(1-r)), stationary probability q^N with q=r^2+(1-r)^2, homogeneous opposite states r^(2N)+(1-r)^(2N), and strict-two-cycle probability 1-q^N. For r=0,1 cycle chance is zero; for each fixed 0<r<1 it tends to 1 exponentially. Direct proof handles arbitrary N and graph pairs; independent checker enumerated 69 pairs of simple graphs and 4,164 graph-state combinations for N=1,2,3, with exact rational ensemble probabilities at r=0,1/3,1/2,2/3,1 and all-positive threshold witnesses. No finite check is treated as an infinite proof.

## originality

PASS

Qualified best-of-knowledge originality for the precise sharp all-microstate strong-antagonism phase of the synchronous Hughes et al. paired-spin model, not for the elementary sign-bound inequality or the classical eventual period <=2 fact. The complete Hughes 2026 primary text defines the same Eqs.(2)-(5), focuses on k=3,J=-1, and identifies two homogeneous opposed absorbing states and their simulated attraction picture, without analyzing j>Delta, proving an immediate all-state involution, or deriving an all-bias binomial distribution. Goles-Olivos 1980 provides the much broader eventual period-at-most-two theorem for symmetric threshold maps; even if applicable to this signed network, that alone does not imply zero transient, exact fixed/cycle counts, or a degree-sharp identity. Related published Resultary parity automata use an F_2-linear distance-two Hamming graph update, not a sign-threshold antagonistic paired graph. No inspected source was found that asserts or mathematically forces the full model-specific phase. Residual risk is significant because the complete 1980 text was inaccessible and other signed-threshold strong-coupling reductions may be indexed differently; search absence is not priority proof.

## value

PASS

The full strong-inhibition regime is a motivated, natural parameter phase of the just-introduced antagonistic multiplex majority model. Although its sign-dominance proof and subsequent counting are elementary, together they give an all-graph, all-size, sharp complete orbit classification not provided by the motivating baseline metastability simulations. It materially changes interpretation of model extrapolation: above the explicit maximum-degree barrier, every state is already stationary or oscillates, exponentially many exact two-cycle orbits coexist with 2^N absorbing (often non-consensus) fixed states, and under the motivating independent biased ensemble almost all large-N initial states cycle for every interior bias. The exact threshold and binomial survival/cycling probability are natural diagnostic quantities for designing simulations and distinguishing a two-polarized-consensus picture from a fully oscillatory microscopic phase. The result is self-contained and has object-specific value rather than relying on an unproved downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
