# Scientific review: hypersphere obstruction for Gaussian pollutant-puff identification

## Correctness — PASS

The claim fixes the full physical domain and quantifies over all positive diffusivities, masses and all source locations and emission times preceding both observations. The logarithmic observations at each snapshot are linear in a quadratic-affine coefficient vector. Full column rank of the sensor matrix recovers this vector exactly, and the displayed formulas recover diffusivity, emission time, location and mass uniquely. A vanishing matrix rank forces a nontrivial quadratic radial equation, whose zero set is a sphere or hyperplane; reflecting a source across a hyperplane, or scaling about the sphere center with the prescribed mass/diffusivity transformation, gives an exact indistinguishable parameter pair for every positive observation time. The converse and the single-snapshot obstruction are explicit. The checker independently passed 6,036 finite assertions, including exact rational sphere identities and 1,200 two-time reconstruction cases. No finite test substitutes for the universal proof.

## Originality — PASS (best-knowledge, residual risk)

The closest primary result is Lu, Dragotti and Vetterli (2011), equations (4)–(15) and section 3, whose known-diffusivity inverse has a \(d+1\)-sensor design. The present problem includes diffusivity as an *unknown* and proves the exact \(d+2\)-sensor threshold, a two-snapshot inverse, and sphere/hyperplane all-time nonidentifiability. These differences are in assumptions and logical implications, not nomenclature. Qu et al. (2014), Matthes et al. (2005), and Turbelin et al. (2014) use different continuous-release or known-transport settings. Published related records and accessible earlier findings did not yield an equivalent assertion. Possible general inverse-system theorems and the incompletely accessible Matthes–Gröll–Keller (2006) paper remain genuine priority risks. No failed search is described as a proof of novelty.

## Mathematical value — PASS

A fully sampled temporal trace cannot separate source, diffusion and mass for a poorly placed sensor array, while a single extra *off-sphere* sensor makes two temporal samples sufficient. This is a precise minimal sensor-design law for an inverse environmental transport model, not a parameter renaming, arbitrary finite slice, or numerical exercise. It identifies a counterintuitive structural barrier that persists despite unlimited temporal measurements. The theorem also clarifies exactly which known-diffusion sensor-count claims cannot be carried over to unknown diffusivity.

## Closest literature and limitations

The Lu–Dragotti–Vetterli (2011) author manuscript was inspected through source reconstruction sections, including its explicit known-diffusion coefficient in equation (11). Full-text comparisons were made with Matthes–Gröll–Keller (2005), Qu et al. (2014) and Turbelin–Singh–Issartel (2014); the closest 2006 minimal-sensor contribution was abstract-only. The classification assumes free-space isotropic diffusion, one instantaneous source, fixed correctly calibrated sensors and exact readings, and does not establish noisy estimation performance or applicability to wind-driven, bounded or reactive environments.

Self-review: passed. Independent audit: not yet performed.
