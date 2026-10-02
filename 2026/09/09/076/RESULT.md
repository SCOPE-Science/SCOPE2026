# Emptiness of the first sub-174/55 homogeneous 10-point system L(136;43^10)

## Context

For ten general points in the projective plane, Ciliberto--Miranda prove expected dimension for homogeneous systems when \(d/m\ge174/55\), while Dumnicki proves the homogeneous Harbourne--Hirschowitz statement for multiplicity at most 42. Petrakiev proves emptiness below \(2280/721\), slightly below \(\sqrt{10}\).

At multiplicity \(m=43\), degree \(d=136\) is the unique integer with

\[
43\sqrt{10}<136<43\cdot\frac{174}{55}.
\]

Thus \(L(136;43^{10})\) is the first homogeneous cell beyond the published multiplicity-42 finite range inside this narrow ten-point interpolation strip.

## Result

The homogeneous system \(L(136;43^{10})\) on the blowup of the projective plane at ten general points has virtual dimension \(-8\) and is empty.

There are

\[
\binom{138}{2}=9453
\]

degree-at-most-136 affine monomials, while each multiplicity-43 point contributes

\[
\binom{44}{2}=946
\]

jet conditions, for 9460 rows in the interpolation matrix.

## Proof

Take the ten distinct rational affine points with x-coordinates \(0,1,\ldots,9\) and y-coordinates

\[
0,2,5,11,7,13,17,23,29,31.
\]

Form the \(9460\times9453\) integer interpolation matrix whose row indexed by a point and \((a,b)\), \(a+b\le42\), evaluates the derivative \(\partial_x^a\partial_y^b\) of each monomial.

Exact Gaussian elimination modulo 251 gives a pivot in every one of the 9453 columns. Therefore a \(9453\times9453\) minor is nonzero modulo 251, hence is a nonzero integer. The same specialization has full column rank over the rationals, so its degree-136 section space is zero.

Dimension of a kernel is upper semicontinuous in the point coordinates. Consequently vanishing at this specialization implies vanishing for general ten-tuples in characteristic zero. Hence \(L(136;43^{10})\) is empty.

A fresh independent reconstruction of the full \(9460\times9453\) matrix at this first specialization and elimination through all 9453 columns reproduced full column rank.

## Reproducibility correction

The original auxiliary shifted-specialization source allocated its falling-factorial table with stride \(m\) while iterating through index \(m\). That out-of-bounds access made its saved secondary run unsuitable as evidence. The corrected source uses stride \(m+1\). The stale shifted log is removed.

This correction does not affect the theorem: the first specialization alone proves emptiness, and that full rank was independently reproduced.

## Limitations

Only the single cell \(L(136;43^{10})\) is decided here. The remainder of the strip \(\sqrt{10}<d/m<174/55\) is not classified.

## References

- C. Ciliberto and R. Miranda, *Homogeneous interpolation on ten points*, J. Algebraic Geometry 20 (2011), arXiv:0812.0032.
- M. Dumnicki, *Cutting diagram method for systems of plane curves with base points*, Ann. Polon. Math. 90 (2007).
- I. Petrakiev, *Homogeneous Interpolation and Some Continued Fractions*, Trans. Amer. Math. Soc. Ser. B 1 (2014), arXiv:1211.6380.
