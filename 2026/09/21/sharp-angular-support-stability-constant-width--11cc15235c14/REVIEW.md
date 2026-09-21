# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

After translating the Steiner point to the origin, constant width removes all nonconstant even support-function harmonics and Steiner centering removes the first harmonics. The standard support-function area identity therefore gives
\[
D=\frac{\pi}{2}\sum_{n\ge3,\ n\ {\rm odd}}(n^2-1)(a_n^2+b_n^2).
\]
Hausdorff distance to the Steiner disk is exactly the sup norm of the remaining support-function part. Weighted Cauchy--Schwarz then reduces the theorem to
\[
\sum_{n\ge3,\ n\ {\rm odd}}\frac1{n^2-1}=\frac14,
\]
which telescopes.

The sharpness family was checked separately. Its curvature-radius function is
\[
h_N+h_N''=\frac w2-c_N\sum_{k=1}^N\cos((2k+1)\theta),
\]
and with \(c_N=w/(4N)\) it stays at least \(w/4\), so every member is smooth and strictly convex. Its exact ratio is \(2\pi(N+1)/N\), proving optimality.

For the symmetry refinement, q-fold symmetry restricts frequencies to multiples of q. If q is even, the included half-turn plus constant width forces a disk. For odd q, the admissible modes are \(q(2k+1)\), and
\[
\sum_{k\ge0}\frac1{q^2(2k+1)^2-1}
=\frac{\pi}{4q}\tan\frac{\pi}{2q},
\]
so the sharp coefficient is \(2q\cot(\pi/(2q))\). Truncated admissible-mode families with sufficiently small common amplitude preserve positive curvature and approach the stated constant.

The nonsmooth case is covered by the \(H^1\) support-function identities, or equivalently by circular mollification of the support function, which preserves convexity, constant width and Steiner centering.

The proof was also checked in its stronger two-direction form. For angular separation \(d\),
\[
\sum_{n\ge3,\ n\ {\rm odd}}\frac{2-2\cos(nd)}{n^2-1}
=
\frac{1-\cos d}{2}+\left(\frac\pi2-d\right)\sin d.
\]
A separate finite-mode extremizing family aligns each coefficient with the difference of the two evaluation vectors, and a shrinking amplitude keeps the curvature radius positive. Hence the angular kernel is sharp for every fixed \(d\), not only at the antipodal Hausdorff endpoint.

## Originality

PASS, to the best of our knowledge.

Groemer (1988) is the closest older source. For normalized width one, Theorem 1(b) and Corollary 1 imply
\[
\pi/4-A(K)\ge4\,d_H(K,D)^2
\]
for a suitably chosen diameter-one disk D. The inspected paper does not state a canonical Steiner-disk estimate with coefficient \(2\pi\).

Alvino--Ferone--Nitsch (2009) give a sharp general planar profile for a different Hausdorff asymmetry optimized over comparison disks. Gao (2011) gives Fourier stability estimates for general convex curves relative to the Steiner disk. Cufí--Gallego--Reventós (2018) use the \(L^2\) distance of support functions to the Steiner disk and also study constant width. A 2025 Journal of Geometry paper explicitly records the constant-width odd-harmonic Fourier reduction and the corresponding area identity, but applies them to Linderholm's circumscribed-right-triangle problem. Zhao (2026) was checked as a current general parametric-stability comparison.

Searches using constant width, Steiner disk/disc, Hausdorff distance, isoperimetric/area deficit, support function, Fourier harmonics, angular support differences, rotational symmetry, and the candidate constants did not locate the sharp angular kernel, its \(2\pi\) antipodal consequence, or the \(2q\cot(\pi/(2q))\) hierarchy.

A material residual risk is Deyan Zhang (2019), DOI 10.1016/j.jmaa.2019.04.047. The accessible abstract says that several upper and lower isoperimetric-deficit bounds are proved, but the full theorem text was not inspected. Because that paper is close in subject, an equivalent specialized constant-width consequence there would affect originality. No available statement found during review gives concrete evidence that it contains the present theorem.

## Value

PASS.

The result gives an exact sharp angular modulus for the Steiner-centered support function in terms of the area deficit. Its antipodal specialization sharpens the classical circular-side constant-width stability coefficient from 4 to the best possible \(2\pi\), fixes the comparison disk canonically, and the symmetry refinement yields a second sharp spectral hierarchy. Explicit smooth families establish sharpness for every fixed angular separation.

## Limitations

- Planar Euclidean convex bodies only.
- The comparison disk is the Steiner disk.
- Sharpness is asymptotic through smooth noncircular bodies approaching the disk; no noncircular equality case is claimed.
- Only cyclic rotational symmetry is quantified in the refinement.
- The full text of Zhang (2019) was not inspected, leaving a stated priority risk.
