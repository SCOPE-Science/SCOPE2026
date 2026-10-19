# Scientific review: fast habitat-pulse tipping boundary

## Correctness — PASS

The theorem concerns the precise singular regime of a rectangular shock of length \(\varepsilon s\) with fixed \(s\), followed by restoration. The postshock limit is the scalar fast equation at the initial predator density. Its unstable frozen-layer root is \(w=a+1/\phi_0-1\), and its shock fold is the unique solution of \(F(\phi)=v_0\), where \(F(\phi)=(1-a\phi)^2/(4\phi)\). The critical duration is the exact strictly-positive travel-time integral from prey density \(1\) to \(w\). Compact separation from this unstable root gives a robust basin conclusion for sufficiently small \(\varepsilon>0\). The inverse-square-root law follows from an interior quadratic bottleneck with a calculated coefficient. Symbolic and high-precision computations reconstruct the algebra and exact example, while optional finite-\(\varepsilon\) ODE simulations are supplementary. No conclusion is asserted for the singular equality \(s=s_c\) or for finite \(\varepsilon\) uniformly approaching the threshold.

## Originality — PASS (self-review; residual risk)

The central recent paper [1] uses the identical frozen biological flow, establishes bistability and fold geometry, and studies a *linearly ramped* environmental parameter and its critical ramp rate. A materially read public full-text version and appendix do not present the rectangular temporary shock, return to baseline, its amplitude–duration phase boundary, baseline immunity condition, or the displayed exact divergence constant. Earlier press/pulse ecological literature [2,3] demonstrates qualitative timing effects, including simulations and recovery, but uses different settings and does not present this model-specific full classification. The nearest accessible published mathematical results about Allee extinction, periodic intervention, and fold slowing have different dynamical statements and do not imply the present formula as stated. Generic scalar quadrature and geometric singular perturbation theorems remain plausible sources of stronger abstract coverage; originality is not independently certified. The current contribution is the combined sharp classification, not the previously known fact that pulse length can matter.

## Mathematical value — PASS

Temporary habitat deterioration followed by restoration is a distinct, ecologically motivated forcing protocol from indefinite ramping. The result computes the exact minimum damaging duration at every admissible damaging amplitude, identifies a previously unseparated baseline regime with no admissible fast-pulse tipping, and quantifies the bottleneck divergence with its coefficient. Such a complete boundary is a useful analytical benchmark for duration-sensitive resilience; it is neither an arbitrary numerical slice nor a claim of universal ecological applicability.

## Closest sources and scientific limits

[1] Hennessy, Popović, and Sattar (2026), arXiv:2610.12319v1: source model, frozen bistability and fold; linear-ramp dynamics rather than temporary shock.

[2] Ratajczak et al. (2017), DOI:10.1002/ecm.1249: ecological press/pulse strength-duration effects; openly inspected abstract, full paper not materially inspected.

[3] Karakoç et al. (2017), DOI:10.1186/s12898-017-0123-2: materially inspected full public HTML of a different predator–prey/resource model under pulses and presses.

There remains a possible generic fast–slow theorem or uninspected specialist result subsuming the specific formula, and the outcome on the equality boundary or for joint small-parameter limits is unproved. All conclusions are local to the stated deterministic model, initial state, and fast-pulse regime.

Self-review: passed. Independent audit: not yet performed.
