# Scientific assessment

## Correctness — PASS

The exact domain is \(D,\tau,\mu,\beta_s>0\) with \(\gamma\ge0\). Differentiating the OU susceptibility, then integrating by parts, gives a weighted increasing-hazard integral with exactly one sign change. The strictly decreasing ratio of its late and early Laplace contributions proves at most one stationary switching rate; its endpoint derivative decides existence and gives the global optimum. The correlation-time likelihood-ratio ordering proves strict monotonicity of the moment threshold; the limiting exponential and Gaussian rescalings yield its sharp endpoints. A scaled limiting derivative and two-sided root brackets establish the \(\tau^{-1}\) optimizer law. A standalone SciPy verification program passed 908 finite checks, and those checks are explicitly not substituted for an infinite-parameter proof.

## Originality — PASS (best-knowledge)

The closest primary source is Reon Hayashi's 2026 OU Ising–Kuramoto model, arXiv:2609.35838v1, which supplies the susceptibility and a sufficient condition for a finite switching optimum. The new statement proves global uniqueness, a necessary-and-sufficient criterion, a unique parameter-dependent maximum allowed memory duration for a positive optimum, and singular short-memory scaling. Tönjes (2010), Zhang–Strogatz (2021), and older on–off coupling literature address different switching/noise mechanisms. Actual searches of mathematical findings and accessible earlier claims did not identify complete stronger coverage, but the broad positive-Laplace-kernel theory is a residual possibility. The Chen–Qiu–Huang 2009 and Maggi–Paoluzzi 2019 sources were compared only at abstract level; this limitation is not presented as a full-text noncoverage finding.

## Value — PASS

The new memory-duration phase boundary is a natural unresolved control-timescale question for the source's reported finite optimum. For fixed \(0<\mu/\beta_s<D\), switching is optimal at a strictly positive rate only below a unique memory time. For \(D=1\), \(\mu/\beta_s=1/2\), that boundary is \(\tau_c\approx4.22146244\), and the short-memory optimal switching cost diverges like \((1+\sqrt2)/\tau\). These explain a genuine qualitative design change beyond finite parameter examples.

## Limitations and scientific risk

The theorem is for linear first-harmonic susceptibility of the stated OU model, not nonlinear synchronization stability, non-OU kernels, or discrete switching costs. More general published transform principles could imply a portion of the proof; priority has not been independently certified. Missing full texts are recorded rather than presumed checked.

Self-review: passed. Independent audit: not yet performed.
