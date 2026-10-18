# Mathematical review: annular Fourier dark-ring trajectories

## Correctness — PASS

The transform identity follows from the radial Fourier–Bessel integral. For \(E(x)=x^2(J_0(x)^2+J_1(x)^2)\), the exact identity \(E'(x)=2xJ_0(x)^2\) and the root equation imply \(|J_0(x)|>q|J_0(qx)|\), so every positive root has a nonzero derivative with the sign of \(J_0(x)\). Opposite endpoint signs and the common crossing orientation give exactly one root per \(J_0\) gap and no earlier root. The stronger identity \((qx_n(q))'=x_n(q)J_0(x_n(q))/[J_0(x_n(q))-q^2J_0(qx_n(q))]>0\) makes the inner argument pass through exactly the first \(n-1\) positive \(J_0\) zeros. Differentiation at these crossings gives the claimed nonzero curvatures; implicit-function arguments give the endpoint asymptotics. The finite tests described in VERIFICATION.md are not substituted for the infinite argument.

## Originality — PASS, with reservations

Pálmai–Apagyi (arXiv:1002.0976, 2010) establish interlacing for ordinary Bessel zeros, but do not treat zeros of \(J_1(x)-qJ_1(qx)\) as a moving parameter family. Khonina's 2013 optical analysis identifies filled-disk and thin-ring first-zero limits, without the every-ring turning-point census. Guo–Müller–Wang–Wang (arXiv:1907.03669) analyze the different \(J_\nu Y_\nu-Y_\nu J_\nu\) annulus boundary-eigenvalue determinant. Searches of the mathematical-record database and relevant terminology produced no result proving the \(n-1\) stationary-point law. This supports an originality assessment of the exact trajectory census, but old unindexed optics tables or special-function papers could contain equivalent formulas; no independent priority determination has been made.

## Value — PASS

The circular-annulus Fourier transform is a basic model of an obstructed aperture. Locating all of its dark rings for every obstruction ratio and proving that the \(n\)-th ring turns exactly \(n-1\) times is a natural complete classification, not an isolated low-order calculation. The result separates the strictly monotone first ring from the increasingly oscillatory higher rings, proves no radial double zeros arise in the family, and gives implicit exact optimization radii and endpoint limits.

## Limitations and closest literature

The result is limited to real positive radial Fourier zeros of uniform planar annuli. Complex zeros, phase masks, and vector diffraction are outside its scope. Related analytic inputs are Pálmai and Apagyi (2010), NIST DLMF §10.21, Khonina (2013), and Guo et al. (2019). The old optical literature is a residual originality risk even after searching and comparing the accessible related texts.

Self-review: passed. Independent audit: not yet performed.
