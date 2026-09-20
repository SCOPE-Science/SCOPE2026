# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The contraction identity follows algebraically from the published equations: use \(\dot z=b(1-2\cos y)\) to eliminate \(\cos y\) from \(-a\cos y\sin z\), and use \(d(\cos z)/dt=-\dot z\sin z\). The invariant-measure consequence follows because the integral of a smooth coboundary against an invariant probability measure is zero.

For the central orbit, the source paper itself gives the normal variational equation \(X''+a\sin(z_0-bt)X'+X=0\). The periodic Liouville substitution stated in `RESULT.md` gives the displayed two-harmonic Hill equation. Abel's formula gives transverse monodromy determinant one exactly. A standalone verifier checks both symbolic reductions and computes the \(b=1/2\) band edge from the original NVE and the transformed Hill equation independently; the traces agree to about \(10^{-14}\), and phase shifts in \(z_0\) leave the trace unchanged to the same scale.

Adversarial checks considered sign errors in the coboundary term, the Liouville gauge, and the period. With \(\theta=z_0-bt\), \(d(\cos\theta)/dt=b\sin\theta\), so the gauge \(\exp[-a\cos\theta/(2b)]\) has the correct sign; the orbit period is \(2\pi/|b|\). The reported numerical edge is explicitly labeled non-rigorous and is not used as a premise for the exact identities.

## Originality

**PASS, with a narrow source-specific claim.** The full HTML of arXiv:2609.19958v1 was inspected around the model definition, reversibility, divergence, global bifurcation discussion, and the differential-Galois normal variational equation. The paper gives \(\operatorname{div}v=-a\cos y\sin z\), the reversing involution, the central periodic orbit, and its NVE, but does not present the contraction coboundary, a Floquet/Whittaker–Hill stability analysis of that orbit, or a monodromy threshold near \(a=1.6\). Text searches in the paper for `Floquet` and `Whittaker` returned no matches.

No matching prior SCOPE record was identified for arXiv:2609.19958 or for the same contraction/Floquet claim family.

Generic prior art is substantial: Posch–Hoover (1997) and Sprott (2015) establish that time-reversible flows can support dissipative attractor/repeller pairs, and periodic-damping oscillators are routinely analyzed by Floquet/Hill methods. Those general facts are excluded from the novelty claim. Literature checked around the source model, periodic damping, reversible contraction, and Floquet stability did not reveal a source-specific prior statement of the exact cohomology or the \(a\approx1.590316803\) central-orbit edge.

Some generic periodic-damping literature was inspected only through abstracts or bibliographic pages. That creates residual risk for any broad claim about the Hill reduction, so no such broad claim is made. Because arXiv:2609.19958v1 is very recent, an unindexed comment or later author revision could also overlap the source-specific observation.

## Value

**PASS.** The exact cohomology converts a two-variable contraction observable into a one-variable thermostat-phase order parameter and gives an immediate symmetry test for zero versus nonzero Lyapunov sum. The Floquet reduction then turns the paper's qualitative statement that the central regular branch survives to roughly \(a=1.6\) into a sharply localized local stability mechanism: the exact central orbit reaches a \(-1\) band edge at \(a\approx1.590316803\) for \(b=1/2\). The result also clarifies that a reversing-symmetric periodic orbit cannot be an asymptotic sink, even though nearby trajectories can appear regular.

## Limitations

The band-edge value is floating-point rather than interval-certified. The local Floquet transition is not a proof of a global chaotic bifurcation. The analysis does not classify the later regular windows or the full \((a,b)\) stability chart. General reversible-dynamics and periodic-damping theory are prior art and are not claimed as new.
