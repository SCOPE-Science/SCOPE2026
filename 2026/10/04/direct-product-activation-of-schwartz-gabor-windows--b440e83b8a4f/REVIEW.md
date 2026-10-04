# Review of Direct-product activation of Schwartz Gabor windows

## Correctness

PASS. For symplectic direct products, the symplectic form splits factorwise. Therefore the adjoint lattice splits exactly:
\[
(\Lambda_1\oplus\Lambda_2)^\circ
=
\Lambda_1^\circ\oplus\Lambda_2^\circ.
\]
Intersecting with the original lattice gives the corresponding exact splitting of the integral symplectic subgroup. Finite group indices multiply, so their positive square roots, the symplectic integrality indices, multiply as well.

For a \(k\)-fold power, the two indices are therefore \(\nu^k\) and \(r^k\), while the signal dimension is \(kd\). Substituting these quantities into the primary source's exact minimum-window formula gives
\[
q_{\min}^{\mathcal S}
=
\left\lceil(r^k+kd)/\nu^k\right\rceil.
\]
The one-window condition is exactly
\[
\nu^k-r^k\ge kd.
\]
Strict density gives \(\nu>r\), and the factorization
\[
\nu^k-r^k=(\nu-r)\sum_{j=0}^{k-1}\nu^{k-1-j}r^j
\]
shows exponential growth, proving finite-power activation. The source example with \((d,\nu,r)=(2,2,1)\) checks exactly to window counts \(2,2,1\).

## Originality

PASS. The full 2026 primary source was inspected through the definitions of the symplectic integrality indices, the exact Schwartz one-window criterion, the exact multiwindow formula, and its examples. Searches of the full text found no direct-product, direct-sum, or tensor-product statement for the lattice classification. The paper does not state the power law
\[
q_{\min}^{\mathcal S}(\Lambda^{\oplus k})
=
\left\lceil(r^k+kd)/\nu^k\right\rceil
\]
or the resulting activation phenomenon.

The 2025 Enstad--Thiel--Vilalta article was inspected in full text. It contains tensor-product structure for rational noncommutative tori and a sufficient Schwartz-frame criterion, but it does not state a Gabor-lattice product-power theorem or exact product-power minimum-window law. The 2024 Gjertsen--Luef article discusses multivariate Gabor structure and cites general tensor-product frame theory, but does not contain the symplectic-index activation claim.

Candidate-specific published-finding searches covered direct products, tensor powers, symplectic index gaps, Feichtinger/Schwartz windows, and minimum regular-window counts. No returned item covered the claim.

A residual risk remains that an elementary corollary of the new classification may have been noted informally after the preprint appeared, since the direct-product index calculation is short once the classification is known.

## Value

PASS. The source emphasizes that ordinary density alone can badly misrepresent the existence of well-localized Gabor windows because the symplectic index gap can remain too small. The accepted result identifies a contrasting amplification law: under independent phase-space products, the arithmetic integrality indices multiply while the regularity threshold dimension only adds.

This creates a genuine activation phenomenon. A lattice may require multiple regular windows and fail every one-window Schwartz construction in its native dimension, yet a finite direct power admits a single Schwartz window. The exact formula also tracks the minimum number of regular windows through every product power. For the source's basic obstructed two-dimensional example, the first activation occurs sharply at the third power. This supplies a structural consequence of the new classification rather than a routine restatement of a threshold.

Same-model review: passed. Independent audit: not yet performed.
