# Exact stabilizer-order distribution in two-heavy canonical and terminal weighted projective spaces
## Finding
For every integer \(r\ge2\), let
\[
X_{r,a,b}=\mathbb P(1^r,a,b),\qquad 1\le a\le b,
\]
and define the summatory totient function
\[
\Phi(n)=\sum_{m=1}^n\varphi(m),\qquad \Phi(0)=0.
\]
For every integer \(g\ge1\), the number of canonical pairs \((a,b)\) with \(\gcd(a,b)=g\) is
\[
N_{\mathrm{can}}(r,g)=3\Phi\!\left(\left\lfloor\frac r g\right\rfloor\right),
\]
while the number of terminal pairs is
\[
N_{\mathrm{term}}(r,g)=3\Phi\!\left(\left\lfloor\frac{r-1}g\right\rfloor\right).
\]
The quotient description of weighted projective space shows that \(\gcd(a,b)\) is the generic stabilizer order along the line on which the \(r\) coordinates of weight \(1\) vanish. Hence the formulas give the complete distribution of generic stabilizer orders on that heavy-coordinate stratum.

## Assumptions and scope
The family is the well-formed weighted projective space \(\mathbb P(1^r,a,b)\) over characteristic zero, with \(r\ge2\) and \(1\le a\le b\). Put \(d=b-a\). For this family the canonical and terminal regions are
\[
0\le d\le r,\qquad 1\le a\le r+d
\]
and
\[
0\le d<r,\qquad 1\le a<r+d,
\]
respectively.

Along the open part of the heavy-coordinate line, both heavy coordinates are nonzero and all unit-weight coordinates vanish. A scalar fixes such a point exactly when its \(a\)-th and \(b\)-th powers are both \(1\), so the generic stabilizer is \(\mu_{\gcd(a,b)}\). When \(g>1\), this group acts nontrivially on the \(r\) transverse unit-weight directions; since \(r\ge2\), the coarse space is singular along that line. When \(g=1\), no positive-dimensional singular stratum remains there.

## Proof
Because
\[
\gcd(a,b)=\gcd(a,b-a)=\gcd(a,d),
\]
the condition \(\gcd(a,b)=g\) is equivalent to
\[
a=gc,\qquad d=ge,\qquad \gcd(c,e)=1,
\]
with \(c\ge1\) and \(e\ge0\).

First consider the canonical region. Set
\[
R=\left\lfloor\frac r g\right\rfloor.
\]
The inequalities \(d\le r\) and \(a\le r+d\) become
\[
0\le e\le R,\qquad 1\le c\le R+e.
\]
Thus \(N_{\mathrm{can}}(r,g)\) is the number of coprime pairs \((c,e)\) in this triangular region.

For \(e=0\), coprimality forces \(c=1\), contributing one pair. For \(1\le e\le R\), split the allowed \(c\)-values into
\[
1\le c\le e
\]
and
\[
e<c\le R+e.
\]
The first range contributes \(\varphi(e)\). In the second range write \(c=e+u\), where \(1\le u\le R\). Then
\[
\gcd(c,e)=\gcd(u,e),
\]
so the contribution from all second ranges is the number of ordered coprime pairs \((u,e)\) in the square \(1\le u,e\le R\). That number is
\[
1+2\sum_{m=2}^R\varphi(m)=2\Phi(R)-1.
\]
Hence
\[
N_{\mathrm{can}}(r,g)
=1+\Phi(R)+\bigl(2\Phi(R)-1\bigr)
=3\Phi(R).
\]

For terminal pairs, the strict inequalities give
\[
ge<r,\qquad gc<r+ge.
\]
With
\[
R'=\left\lfloor\frac{r-1}g\right\rfloor,
\]
these are exactly
\[
0\le e\le R',\qquad 1\le c\le R'+e,
\]
again with \(\gcd(c,e)=1\). The same count therefore gives
\[
N_{\mathrm{term}}(r,g)=3\Phi(R').
\]
This proves both formulas.

## Verification
The accompanying script `verify_stabilizer_totient_distribution.py` exhaustively enumerates all canonical and terminal pairs for \(2\le r\le200\), groups them by \(\gcd(a,b)\), and compares the exact counts with the two formulas above. It also checks that summing the distribution over all \(g\) recovers the known totals \(3r(r+1)/2\) and \(3r(r-1)/2\). Its terminal output is `VERIFY_OK`.

## Relationship to prior work
Weighted projective spaces admit the standard quotient description by a weighted \(\mathbb C^\times\)-action, from which the stabilizer along a coordinate stratum is read off as the gcd of the corresponding weights. Kasprzyk gives general terminal and canonical criteria for weighted projective spaces and fixed-dimensional classifications. The earlier exact count for the subcase \(\gcd(a,b)=1\) gives the zero-dimensional-singular-locus census, but does not supply the distribution for every stabilizer order.

The present argument uses a scaling reduction by \(g\) and an exact coprime-pair count in a triangular region. Targeted searches did not locate the resulting all-dimensional formulas \(3\Phi(\lfloor r/g\rfloor)\) and \(3\Phi(\lfloor(r-1)/g\rfloor)\).

## Limitations
The result is restricted to the two-heavy family \(\mathbb P(1^r,a,b)\). It records the generic stabilizer order on the heavy-coordinate line, not the complete local analytic type of every point on that line. The finite replay through \(r=200\) is only a regression check; the proof above is all-dimensional.

## References
- I. Dolgachev, *Weighted projective varieties*, Lecture Notes in Mathematics 956 (1982), 34–71.
- A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029 (first public version 2013-04-10).
