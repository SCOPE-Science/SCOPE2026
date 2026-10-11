# A twelve-branch pressure certificate for the Minkowski correlation dimension

## Finding

Let
\[
(K_sg)(x)
=
\sum_{a=1}^{\infty}
4^{-a}(a+x)^{2s}
g\!\left(\frac1{a+x}\right),
\qquad x\in[0,1],
\]
be the positive transfer operator for the Minkowski question-mark measure used in the recent correlation-dimension theorem. Let \(D_2\) be the unique zero of
\[
P(s)=\log r(K_s).
\]
Then
\[
D_2<\frac{847}{1000}.
\]

If
\[
\eta_*
=
\sup\left\{\eta:
|m(it)|=O(|t|^{-\eta})
\right\},
\]
then the source's general comparison
\[
\eta_*\le\frac{D_2}{2}
\]
gives the rigorous numerical obstruction
\[
\eta_*<0.4235.
\]

The source reports the numerical value
\[
D_2/2=0.4223047\ldots,
\]
but does not turn that computation into a certified inequality. The finite certificate below supplies such a proof with a simple positive linear test function and only twelve transfer branches.

## Assumptions and scope

The operator \(K_s\), pressure \(P(s)\), correlation dimension \(D_2\), and Fourier exponent \(\eta_*\) are exactly those in arXiv:2609.39181v1.

The source proves that \(D_2\in(0,1)\) is the unique zero of \(P\) and that \(P\) is strictly increasing. It also proves the correlation/Fourier comparison
\[
\eta_*\le D_2/2.
\]

The result here is an upper certificate. It does not claim the exact value of \(D_2\), does not certify every digit of the source's numerical estimate, and does not improve the known lower bounds for Fourier decay.

## Proof

Set
\[
s_0=\frac{847}{1000}
\]
and choose
\[
g(x)=1+\frac{127}{120}x.
\]
For the first twelve branches define
\[
(K^{(12)}_{s_0}g)(x)
=
\sum_{a=1}^{12}
4^{-a}(a+x)^{2s_0}
g\!\left(\frac1{a+x}\right).
\]
Because \(g(y)=1+(127/120)y\), this is the explicit scalar function
\[
(K^{(12)}_{s_0}g)(x)
=
\sum_{a=1}^{12}4^{-a}
\left[
(a+x)^{2s_0}
+
\frac{127}{120}(a+x)^{2s_0-1}
\right].
\]

The accompanying verifier partitions \([0,1]\) into \(2000\) closed intervals of length \(1/2000\). On every cell it evaluates the preceding expression using outward interval arithmetic. The smallest certified lower endpoint of
\[
(K^{(12)}_{s_0}g)(x)-g(x)
\]
over all cells is
\[
0.000051512874937209574\ldots,
\]
which is strictly larger than
\[
\frac1{25000}=0.00004.
\]
Thus, exhaustively over the whole continuum,
\[
(K^{(12)}_{s_0}g)(x)-g(x)>\frac1{25000}.
\]
This is a finite interval certificate for a uniform inequality, not an extrapolation from sampled point values.

Every omitted transfer branch is positive. Hence
\[
K_{s_0}g
\ge
K^{(12)}_{s_0}g
>
g+\frac1{25000}.
\]
Also
\[
1\le g(x)\le1+\frac{127}{120}=rac{247}{120}.
\]
Therefore
\[
K_{s_0}g
\ge
\left(
1+
\frac{1/25000}{247/120}
\right)g
=
\left(1+\frac{3}{154375}\right)g.
\]

Since \(K_{s_0}\) is positive, induction gives
\[
K_{s_0}^ng
\ge
\left(1+\frac{3}{154375}\right)^n g.
\]
Taking operator norms and then \(n\)-th roots yields
\[
r(K_{s_0})
\ge
1+\frac{3}{154375}>1.
\]
Consequently
\[
P(s_0)>0.
\]
The source proves that \(P\) has the unique zero \(D_2\) and is strictly increasing, so
\[
D_2<s_0=0.847.
\]
Finally,
\[
\eta_*\le D_2/2<0.4235.
\]

## Verification

The primary paper was inspected at Proposition 1 and its proof. The following source facts were independently checked: the exact transfer operator, the identity
\[
P(s)=\log r(K_s),
\]
the uniqueness of the zero \(D_2\), strict increase of \(P\), and the Fourier comparison \(\eta_*\le D_2/2\).

The standalone verifier uses `mpmath` version `1.3.0` interval arithmetic. It evaluates every one of the \(2000\) cells and fails immediately unless the outward lower enclosure exceeds \(1/25000\). The replay reports the minimum lower endpoint
\[
5.1512874937209574\times10^{-5}
\]
on cell \(1005\), leaving a positive margin over the target floor.

No assertion about the infinite operator is inferred from a truncated numerical approximation: positivity of the omitted transfer branches supplies the rigorous passage from the twelve-branch lower bound to the full operator.

## Relationship to prior work

The recent paper proves existence of the correlation dimension and characterizes it as the unique pressure zero. It then reports
\[
D_2/2=0.4223047\ldots
\]
as a numerical evaluation and notes that this is sharper than the older obstruction obtained from half the Hausdorff dimension,
\[
0.4373581525\ldots.
\]
The present result supplies a fully reproducible inequality
\[
D_2<0.847
\]
and therefore a rigorous Fourier-decay obstruction below \(0.4235\).

Earlier work on the Minkowski question-mark measure develops moments, regularity, Hausdorff dimension, and Fourier-transform questions, but the inspected literature does not provide this explicit pressure subeigenfunction certificate. Searches for the source identifier, the correlation-dimension pressure, the value \(0.847\), and certified Fourier-decay bounds did not locate an implication-equivalent statement.

## Limitations

The bound
\[
D_2<0.847
\]
is not expected to be numerically optimal; it is chosen to give a short, robust certificate close to the source's reported value.

The proof relies on outward interval arithmetic for one finite elementary inequality. The verifier is included so the certificate can be replayed independently, but no claim is made that this is the only possible analytic certification route.

The result is one-sided. It neither supplies a comparably tight lower bound for \(D_2\) nor proves the exact Fourier-decay exponent of the Minkowski measure.

## References

1. G. Alkauskas, *The Minkowski ?(x) function and Salem's problem. II*, arXiv:2609.39181v1, 2026.
2. G. Alkauskas, *The Minkowski question mark function: explicit series for the dyadic period function and moments*, Mathematics of Computation 79 (2010), 383--418; arXiv:0805.1717.
3. C.-A. Guérin and M. Holschneider, *On equivalent definitions of the correlation dimension for a probability measure*, Journal of Statistical Physics 86 (1997), 707--720.
4. P. Mattila, *Fourier Analysis and Hausdorff Dimension*, Cambridge University Press, 2015.
5. T. Jordan and T. Sahlsten, *Fourier transforms of Gibbs measures for the Gauss map*, Mathematische Annalen 364 (2016), 983--1023.
