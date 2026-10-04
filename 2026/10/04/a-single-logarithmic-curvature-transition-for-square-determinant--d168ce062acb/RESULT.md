# A single logarithmic-curvature transition for square determinantal degrees
## Finding
For integers \(n\ge 2\) and \(1\le r\le n\), let \(D_{n,r}\) be the projective degree of the variety of complex \(n\times n\) matrices of rank at most \(r\), with \(D_{n,n}=1\). The Harris--Tu degree formula, reproduced explicitly by Friedland--Krattenthaler, is
\[
D_{n,r}=\prod_{j=0}^{n-r-1}\frac{(n+j)!\,j!}{(r+j)!\,(n-r+j)!}.
\]
For every interior rank \(2\le r\le n-1\), the neighboring-rank logarithmic curvature has the closed form
\[
\frac{D_{n,r-1}D_{n,r+1}}{D_{n,r}^{2}}
=
\frac{r(2n-r)}{4\bigl(2(n-r)-1\bigr)\bigl(2(n-r)+1\bigr)}.
\]
Consequently \(D_{n,r}^{2}\ge D_{n,r-1}D_{n,r+1}\) exactly when
\[
17(n-r)^2\ge n^2+4,
\]
and the inequality reverses exactly when \(17(n-r)^2<n^2+4\). Thus, as rank increases, the square determinantal degree sequence has a single sharp transition from log-concavity to log-convexity, at
\[
r\approx \left(1-\frac{1}{\sqrt{17}}\right)n.
\]
Neutral curvature occurs exactly when
\[
n^2-17(n-r)^2=-4,
\]
so equality ranks are governed by a negative Pell equation. The first three positive solutions are \((n,n-r,r)=(8,2,6)\), \((536,130,406)\), and \((35368,8578,26790)\).

## Assumptions and scope
The base field is \(\mathbb C\). The variety is the projectivization of the generic square determinantal locus cut out by the \((r+1)\times(r+1)\) minors. The statement concerns only projective degrees as the rank bound varies for fixed matrix size \(n\). It does not claim log-concavity of Hilbert functions, of coefficients of a fixed Hilbert series, or of the ordinary plane-partition function by volume.

## Proof
Put \(s=n-r\). From the degree product, cancellation between adjacent ranks gives
\[
R_{n,r}:=\frac{D_{n,r+1}}{D_{n,r}}
=
\frac{r!\,(2s-2)!\,(2s-1)!}{(s-1)!^2\,(r+2s-1)!}.
\]
Indeed, for the common factors with \(0\le j\le s-2\), the quotient is \((s+j)/(r+j+1)\); multiplying these and then cancelling the final \(j=s-1\) factor in \(D_{n,r}\) yields the displayed expression.

For \(2\le r\le n-1\), replacing \((r,s)\) by \((r-1,s+1)\) in the same formula and dividing gives
\[
\frac{R_{n,r}}{R_{n,r-1}}
=
\frac{r(r+2s)}{4(2s-1)(2s+1)}.
\]
Since \(R_{n,r}/R_{n,r-1}=D_{n,r-1}D_{n,r+1}/D_{n,r}^2\) and \(r+2s=2n-r\), this proves the curvature formula.

Finally,
\[
\frac{D_{n,r-1}D_{n,r+1}}{D_{n,r}^{2}}\le1
\iff
r(r+2s)\le4(4s^2-1).
\]
Using \(r=n-s\), the left side of the last comparison becomes \(n^2-s^2\), so the inequality is equivalent to \(n^2+4\le17s^2\), that is \(17(n-r)^2\ge n^2+4\). Equality is therefore equivalent to \(n^2-17s^2=-4\). Because the threshold in \(r\) is monotone, there can be only one change of sign in the logarithmic curvature for each fixed \(n\). Dividing the threshold by \(n\) gives the limiting transition fraction \(1-1/\sqrt{17}\).

## Verification
The standalone exact-arithmetic checker `verify_determinantal_curvature.py` reconstructs the Harris--Tu product for every \(2\le n\le40\), verifies all adjacent-rank ratios and curvature identities there, and stress-tests the one-switch sign criterion through \(n=1000\). It also finds the first three neutral-curvature Pell solutions in the window \(n-r<10000\) and directly checks the first equality \(D_{8,6}^2=D_{8,5}D_{8,7}\). The finite computation is regression evidence only; the proof above is symbolic and uniform.

## Relationship to prior work
Friedland and Krattenthaler reproduce the Harris--Tu product formula for degrees of generic determinantal varieties and note its boxed-plane-partition interpretation. Their paper studies parity and related real-linear-space consequences, not the adjacent-rank logarithmic curvature derived here. The foundational Harris--Tu article is the cited source of the degree formula; its repository copy was not machine-accessible in this check, so no claim is made about unsearched wording inside that article beyond what is explicitly attributed and reproduced by Friedland--Krattenthaler. Searches for determinantal-degree log-concavity, rankwise unimodality, boxed-plane-partition shape log-concavity, and the Pell equality above did not locate a statement implying this single-transition theorem.

## Limitations
The result is for square generic determinantal varieties. Rectangular, symmetric, and skew-symmetric rank loci have different degree products and are not covered. The Pell equation identifies equality cases but no complete parametrization of all its positive solutions is asserted here. Literature search cannot prove absolute novelty; the strongest residual risk is an older combinatorial treatment of MacMahon box counts phrased in shape parameters rather than determinantal degrees.

## References
1. S. Friedland and C. Krattenthaler, *2-adic valuations of certain ratios of products of factorials and applications*, arXiv:math/0508498, first submitted 2005-08-25. Formula (1.2) reproduces the degree of the generic determinantal variety and attributes it to Harris--Tu; the introduction also records the boxed-plane-partition interpretation.
2. J. Harris and L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, Topology 23 (1984), 71--84, DOI 10.1016/0040-9383(84)90026-0. Foundational source cited by Friedland--Krattenthaler for the determinantal degree formulas.
