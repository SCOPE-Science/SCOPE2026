# Review of an exact selective-sweep aging law

## Correctness
**PASS.** The Poisson score-tail measure \(t e^{-m/t}\) gives existence and a Gumbel score. A Mecke density factors into an independent exponential location and Gumbel score, yielding the claimed distribution of \(e^{-Y_s}\). The exact mass of new competitors capable of overtaking by \(t\) is \((t-s)e^{-Y_s}\), proving the conditional exponential reign and two-time aging formula. An independently parametrized two-point Mecke crossing calculation yields switch intensity \(1/(2t)\), hence local finiteness and the expected count. The previously unexamined higher-slope wedge is an independent marked Poisson process with rate \(e^{-y}dh\,v e^{-v}dv\); its successive exploration gives iid gamma fitness increments and the logarithmic almost-sure sweep-frequency law. Poisson-intensity scaling makes log-time switch locations stationary; their void law rules out a Poisson process. The 17 reproducibility assertions pass, but are not substitutes for the proof.

## Originality
**PASS, qualified historical priority.** The motivating Fontes--Schinazi preprint defines precisely this envelope and obtains candidate-point convergence and fixed-time/finite-dimensional leader behavior. It does not report the conditional lifetime, gamma replacement chain, almost-sure sweep frequency, persistence, switch-count or non-Poisson law proved here. Boettcher--Robe--Sibani instead treat another log-Poisson record mechanism, and Groeneboom's linear-score homogeneous-quadrant hull is not the present logarithmic score after coordinate transformation. Related general upper-envelope machinery could imply portions of the statement implicitly; independent priority review is outstanding.

## Mathematical value
**PASS.** The exact two-time persistence, gamma fitness increment law and almost-sure frequency resolve natural temporal observables missing from the selective-sweep point-process description. In particular, the process has logarithmic mean growth yet is non-Poisson, while conditional reigns are exponential but unconditional mean remaining reign is infinite. This distinguishes mutation-candidate Poisson points from actual changes of dominant genotypes and is pertinent to aging and sweep-frequency predictions.

## Limitations and risks
No finite-population path-level convergence is inferred, and no arbitrary mark laws are covered. The result relies on the given exponential-mark Poisson limit and exact linear score. General point-process or convex-hull formulas might provide stronger historical coverage. Numerical checks are finite approximations.

Self-review: passed. Independent audit: not yet performed.
