# Independent mathematical audit

## correctness

PASS

Starting from the frozen exact quartic Bloch condition, solving linearly for \(Q=\cos\theta_1+\cos\theta_2\) is legitimate away from \(k=N_n\), and spectral membership is exactly \(|Q(k)|\le2\). With \(k=N_n+x/N_n\) and \(y=\ell x\), direct dominant-balance expansion gives \(Q=(-1)^n(\sin(2\mu)y/2-2\sin(2\mu)/y-2\cos(2\mu))+O(N_n^{-2})\). The limiting quotient is strictly increasing on each half-line; its four simple crossings with \(\pm2\) are exactly the submitted half-angle expressions. The central point is nonspectral, so the two half-line allowed intervals remain separated for large \(n\). Squaring \(k\) doubles the limiting momentum shifts and leaves an \(O(n^{-2})\) energy-edge error. A fresh symbolic leading-order expansion in this audit reproduced the singular \(-2\sin(2\mu)/y\) term; the frozen verifier independently checks the four edges and second-order convergence at several parameter values.

## originality

PASS

The defining Exner--Tater paper gives the exact Bloch polynomial and a coarse high-energy localization/width estimate, but its displayed \(k=N_n+\delta\) expansion is not uniform on the singular \(\delta\asymp N_n^{-1}\) scale: it yields only an outer range and does not see the central gap. The audited scaling retains a reciprocal term of the same leading order and thereby resolves two separated local bands and all four sharp edges. The older endpoint-oriented square-lattice paper treats a different coupling limit. Resultary and exact-formula web searches did not locate a prior two-band scaling theorem.

## value

PASS

The theorem upgrades a coarse high-energy width estimate to the complete local spectral geometry: it identifies the missing central gap, the two-band topology, four sharp edge constants, and parity-independent translated limit. That is a natural spectral refinement of the primary model rather than an arbitrary extra Taylor coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
