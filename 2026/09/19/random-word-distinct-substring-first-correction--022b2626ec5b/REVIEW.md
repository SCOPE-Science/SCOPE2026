# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS.** Gheorghiciuc--Ward's uniform fixed-level estimate applies with the number of windows \(N_k=n-k+1\) and has a summable error over all lengths. The exact increment of the occupancy deficit controls replacement of \(N_k\) by \(n\) with total error \(O_d((\log n)^2)\); replacing the binomial term by the exponential occupancy profile contributes bounded total error. Reindexing the geometric profile gives the periodic phase. The Mellin transform \(\Gamma(1-s)/(s(1+s))\) was independently checked numerically with a cancellation-stable integral, and its lattice poles give the stated Fourier coefficients and phase mean. The elementary collision sandwich is also correct because two distinct length-\(k\) windows match with probability exactly \(d^{-k}\), including overlapping windows.
- Originality: **PASS.** Best-of-knowledge originality passes for the all-length second-order periodic correction, its explicit Fourier series, and the finite collision sandwich. The coefficient-one first-order heuristic and the fixed-length occupancy profile are prior input.
- Scientific value: **PASS.** The result resolves the complete linear-order correction to a natural all-length random-string statistic, identifies the digital phase and its Fourier spectrum, and quantifies an unusually small binary oscillation. The exact phase is potentially reusable in expectation comparisons and is more informative than the known first-order coefficient.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
The earlier same-model scientific assessment remains preserved in `AUDIT.json` and is not relabeled as independent evidence.
