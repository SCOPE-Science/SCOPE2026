# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. For fixed \(n\), if \(0<\alpha<\beta\), then \(p_n^{(\alpha)}<p_n^{(\beta)}\), and monotonicity of normalized positive moments gives \(A_n^{(\alpha)}\le A_n^{(\beta)}\), hence \(\Phi_\alpha\le\Phi_\beta\). The compressed-block probe is also valid: its block mass is \(r_n\), its support endpoint satisfies \(\log R_n=L_n-r_n^\gamma\), and previous and next block contributions are asymptotically negligible. The normalized moment therefore has the factor \(\exp(-r_n^{\gamma-\alpha}/p_n+o(1))\), giving exactly \(0\), \(e^{-1}\), or \(1\) according as \(\alpha<\gamma\), \(\alpha=\gamma\), or \(\alpha>\gamma\). Choosing \(\gamma\) strictly between two parameters proves strict kernel inclusion. The Hardy--Littlewood obstruction for every interior parameter follows from Huang's \(f,g\) pair and the corresponding moment estimates.

Originality: PASS. Huang's complete 11-page primary paper was inspected. It defines the entire \(\alpha\in(0,1]\) family but specializes to \(\alpha=1\) for a non-strongly-symmetric norm and \(\alpha=1/2\) for a non-Hardy--Littlewood-solid kernel; it does not state monotone nesting, strictness, or the threshold probes. A highly relevant same-day published result on the general critical scale \(L_n(1-p_n)\) was also inspected in full: it proves a different phase diagram, including the \(\alpha>1\) fully symmetric regime and order-theoretic behavior for \(\alpha<1\), but it does not imply strict separation among distinct parameters in \(0<\alpha<1\) or construct \(h_\gamma\) with the \(0/e^{-1}/1\) response. No earlier exact strict-filtration theorem was found.

Scientific value: PASS. The result shows that Huang's continuum of parameters is not redundant: it yields a strictly ordered continuum of distinct logarithmically solid kernels inside one fixed Marcinkiewicz space, with explicit probes that measure the concentration exponent separating any two parameters. That is a natural structural refinement of a new counterexample family.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
