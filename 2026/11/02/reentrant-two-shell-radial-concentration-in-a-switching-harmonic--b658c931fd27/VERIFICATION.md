---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two-sided stationary stochastic convolution exists: along a stationary switching path the on occupation time grows asymptotically as half the elapsed time, making its squared kernel integrable. Sharing future switching and Brownian noise gives contraction by exp(−κ∫J), yielding uniqueness (different initial switching states can be coupled to meet). In dimensionless time κt let w=κV/D−1, with V the conditional coordinate variance. On/off velocities of w are −2w and 2; the zero-flux densities satisfy p_off=w p_on, and on-state balance gives (w p_on)'=(α/2)(1−w)p_on. Thus the normalized total density of w is β^β(1+w)w^(β−1)exp(−βw)/(2Γ(β)); the state densities satisfy the invariant balance with vanishing boundary flux. Equivalently βw is the equal mixture of unit-rate gamma laws of shapes β and β+1, and λ=(1+w)⁻¹ has the printed density. Coupling all d by one shared w and nested independent standard Gaussians gives S_d=√(1+w)·√(ΣG_i²/d)→√(1+w) almost surely. Changing variables w=s²−1 gives g_α; it diverges integrably at 1 exactly for α<2. For u=s²>1 the sign of g′ is minus the sign of Q(u)=αu²−(2α+1)u+3. Its vertex is strictly above 1 and Q(1)=2−α. Below 2, two roots greater than 1 occur exactly when Δ=4α²−8α+1>0, with derivative signs −,+,−; at a double root the density is still strictly decreasing. At 2 the lower root equals 1 and the upper root is 3/2, and above 2 exactly one root exceeds 1. Thus the interior peak survives at and beyond 2, but is no longer paired with a divergent boundary peak; the two windows describe coexistence, not two disappearances of the interior maximum itself. For finite d, below √(1−1/d) the conditional chi derivatives are positive. On compact sets in log radius x>0, the law of log S_d is the convolution of the density of log√(1+w) with k_d(z)=C_d exp(−d I(z)), I(z)=(e^(2z)−1)/2−z and C_d=O(√d). Here I has its unique minimum 0 at zero. Outside every fixed neighborhood of zero, both k_d and k_d′=d(1−e^(2z))k_d decay uniformly exponentially in d, up to polynomial factors. Splitting the log-scale mixing density by a smooth cutoff around the compact set reduces the near part to C¹ approximate-identity convergence and bounds the far convolution and its derivative by those exponential estimates times its L¹ norm, despite the integrable boundary singularity. Transforming back gives the claimed local C¹ convergence. The derivative signs at 0.9 and three fixed radii straddling the limiting critical points are eventually +,−,+,−. The density is real analytic on s>0 (integrate s^(d−1) times an exponential in s² with bounded scale parameter), so the compact-interval interior extrema forced by those signs are strict. The spatial density is a mixture of strictly decreasing Gaussian spatial profiles, with strictly negative radial derivative for every positive radius. The proof therefore establishes at least two peaks at every sufficiently large d for fixed α in an open window, not exact finite-d mode counts or uniform dimension thresholds.

## originality

PASS

The known exact Gaussian mixture and its arbitrary-dimensional spatial profile are the input, and the limiting random scale follows directly by conditional concentration. The supported distinct claim is the two disjoint windows of boundary/interior coexistence for the Euclidean radial density together with rigorous persistence of strict extrema at large finite dimension. The strongest compared literature and catalog records give other observables, dynamics or mode statements, not this classification and persistence. This is a bounded statement-level assessment, not priority for the mixture or for two-shell phenomenology generally.

## value

PASS

The Euclidean norm is the natural radial observable of the isotropic diffusion, not an arbitrary transformation chosen after fitting a mode. The result distinguishes central spatial concentration from an observable radial histogram, gives the exact two disconnected ranges rather than a plot or finite-dimensional anecdote, and proves that the radial effect is not an artifact of the limit. Strict separated extrema for all sufficiently large dimensions require more than the known mixture identity or a weak law for the radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
