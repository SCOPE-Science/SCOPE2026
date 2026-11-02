# Scientific review

## Correctness — PASS

The stationary return process is an Erlang renewal process. Its exact two-sided centered point-process spectrum is obtained from the renewal convolution expansion. Subtracting the Poisson plateau reduces the entire question to the scalar function \(\cos(n\theta)/\cos^n\theta-1\), whose derivative is proportional to \(-\sin((n-1)\theta)\). Consecutive strict extrema alternate beyond \(\pm1\), while the final endpoint diverges with the opposite sign, giving the exact root count and simplicity for all integer stages. Boundary limits and the distinct \(n=1\) Poisson case are explicitly handled. A second derivation using the full finite-state generator plus polynomial Sturm checks confirms the formulas numerically and symbolically for finite samples; it is not used as an infinite proof.

## Originality — PASS on inspected evidence, with residual priority risk

The closest primary comparison is Brandes (arXiv:0802.2233v1, 2008), whose full accessible text treats the same sequential directed-cycle transport, establishes the waiting-time transform and general noise relation, and analyzes the equal-rate many-stage limit. Thus neither the Erlang spectral formula nor the model is asserted new. The distinguished result here is the finite-\(n\) Poisson-plateau intersection classification, including sharp count, nondegeneracy, localization brackets and stage-count inversion. Those finite-stage statements were not located in the inspected text. The general renewal spectrum in *Neuronal Dynamics* also does not give the corresponding root-count theorem. An additional paper about finite-state **occupation-observable** spectral peaks is mathematically neighboring but differs from a marked-event counting spectrum and was only partially accessible. Related mathematical root-count results might predate this observation, so originality remains provisional pending independent priority review.

## Mathematical value — PASS

Spectral peak location is frequently sensitive to rate scales, whereas the number of strict crossings of the shot-noise plateau is a discrete, dimensionless signature for the number of hidden sequential stages. This result makes the signature exact, including the unavoidable adjacent-stage ambiguity, for a physically motivated transport cycle. It identifies genuine alternating super- and sub-Poisson frequency bands in a regime where low-frequency counting noise is always suppressed. The count is a natural complete classification of a global feature of the entire frequency spectrum; it is not merely a single numerical value or a reparameterization of the original renewal formula.

## Closest literature and limits

Brandes, *Waiting Times and Noise in Single Particle Transport*, arXiv:0802.2233v1, sections II.1, III.3 and III.3.2, is the strongest same-object primary antecedent. The Gerstner–Kistler–Naud–Paninski renewal chapter supplies the general covariance-spectrum relation. Wang and Yang (2025) addresses Markov-state observables rather than the return-event train; accessible material was limited. The classification requires homogeneous rates and exact renewal return counting, and has not been independently audited or established for heterogeneous cycles.

Self-review: passed. Independent audit: not yet performed.
