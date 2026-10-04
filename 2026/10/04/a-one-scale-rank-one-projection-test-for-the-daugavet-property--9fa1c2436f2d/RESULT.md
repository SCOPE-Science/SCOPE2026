# A one-scale rank-one projection test for the Daugavet property
## Finding
Let \(X\) be a real Banach space with \(\dim X>1\), and fix \(\sigma\in\{-1,1\}\). Then \(X\) has the Daugavet property if and only if every rank-one projection \(P\in\mathcal L(X)\) satisfies
\[
\|I+\sigma P\|=1+\|P\|.
\]
Moreover, this one-scale identity forces the full positive ray
\[
\|I+\sigma tP\|=1+t\|P\|\qquad(t>0)
\]
for every rank-one projection \(P\).

## Assumptions and scope
The scalar field is \(\mathbb R\), and \(\dim X>1\). A rank-one projection means a bounded rank-one operator \(P\) with \(P^2=P\). The conclusion is asserted separately for either fixed sign \(\sigma=1\) or fixed sign \(\sigma=-1\). The one-dimensional exception is necessary for the positive-sign formulation: on \(\mathbb R\), the only nonzero rank-one projection is \(I\), for which \(\|I+I\|=2=1+\|I\|\), although \(\mathbb R\) does not have the Daugavet property.

## Proof
The forward implication is immediate. If \(X\) has the Daugavet property, then \(\|I+S\|=1+\|S\|\) for every rank-one operator \(S\). Taking \(S=\sigma P\) gives the required projection identity.

For the converse, assume that for every rank-one projection \(P\),
\[
\|I+\sigma P\|=1+\|P\|.
\]
First, the equality propagates from scale \(1\) to every \(t>0\). If \(0<t\le1\), then
\[
I+\sigma P=(I+\sigma tP)+\sigma(1-t)P,
\]
so
\[
1+\|P\|\le \|I+\sigma tP\|+(1-t)\|P\|,
\]
which gives \(\|I+\sigma tP\|\ge1+t\|P\|\). The reverse inequality is the triangle inequality, hence equality holds. If \(t\ge1\), then
\[
I+\sigma P=t^-1(I+\sigma tP)+(1-t^-1)I.
\]
Therefore
\[
1+\|P\|\le t^-1\|I+\sigma tP\|+1-t^-1,
\]
and again \(\|I+\sigma tP\|\ge1+t\|P\|\), with the opposite inequality trivial. Thus the full ray identity holds.

Now let \(T\) be an arbitrary rank-one operator. Write \(T=f\otimes x\), meaning \(Tz=f(z)x\), and set \(a=f(x)\). Then \(T^2=aT\). If \(a=0\), then \(T^2=0\) and
\[
\|I+\sigma T^2\|=1=1+\|T^2\|.
\]
If \(a\ne0\), define \(P=T/a\). Since \(T^2=aT\), one has \(P^2=P\), so \(P\) is a rank-one projection, and
\[
T^2=a^2P.
\]
Because \(a^2>0\), the ray identity with \(t=a^2\) yields
\[
\|I+\sigma T^2\|=1+\|T^2\|.
\]
Hence \(X\) has the \(\sigma\)-square Daugavet property. Langemets proved in 2026 that, for real Banach spaces of dimension greater than one, either signed square Daugavet property characterizes the Daugavet property. Therefore \(X\) has the Daugavet property.

## Verification
The argument uses only the operator identity \((f\otimes x)^2=f(x)(f\otimes x)\), two triangle-inequality interpolations that propagate equality from scale \(1\) to every positive scale, and Langemets's signed-square characterization. The sign and scalar restrictions were checked explicitly: over \(\mathbb R\), the coefficient \(a^2\) is always nonnegative, which is exactly what the ray argument needs. No finite experiment or computation is used.

## Relationship to prior work
Langemets proved that, in real dimension greater than one, each of the two identities \(\|I+T^2\|=1+\|T^2\|\) and \(\|I-T^2\|=1+\|T^2\|\), required for every rank-one operator \(T\), characterizes the Daugavet property. The present observation reduces either test further: it is enough to check the corresponding norm identity only on rank-one idempotents and only at the single scalar value \(1\).

This also sharpens the older notion of a space with bad projections, which asks only \(\|I-P\|\ge2\) for every rank-one projection \(P\). That weaker property is known not to be equivalent to the Daugavet property. The exact identity \(\|I-P\|=1+\|P\|\), by contrast, is equivalent to the Daugavet property in real dimension greater than one.

## Limitations
The proof is real-scalar. For complex spaces, a square of a rank-one operator can produce a non-real scalar multiple of a projection, so a fixed-sign one-ray test does not directly cover all squares. The result does not claim that the weaker bad-projection inequality \(\|I-P\|\ge2\) characterizes the Daugavet property; it does not. The originality assessment is literature-based rather than a proof of absolute novelty, and short projection reformulations may be under-indexed.

## References
1. Johann Langemets, “Characterizing the Daugavet property by squares of rank-one operators,” arXiv:2609.27693v1, first submitted 2026-09-23. Primary MSC 46B20.
2. Yevgen Ivakhno and Vladimir Kadets, “Unconditional sums of spaces with bad projections,” Visn. Khark. Univ. Ser. Mat. Prykl. Mat. Mekh. 645 (2004), no. 54, 30–35.
3. Vladimir M. Kadets, Roman V. Shvidkoy, Gleb G. Sirotkin, and Dirk Werner, “Banach spaces with the Daugavet property,” Trans. Amer. Math. Soc. 352 (2000), 855–873.
