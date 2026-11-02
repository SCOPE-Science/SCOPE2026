# A three-torus chart for the planar-conic quartic of Example 7.1

## Finding

Over \(\mathbb C\), let \(B\subset\mathbb P^3\) be the quartic of Alves da Silva–Figueroa–Moraga, Example 7.1, with homogeneous coordinates \([t:x:y:z]\) and equation
\[
F=(ty+x^2-z^2)^2-4x^2(x^2+y^2-z^2)=0.
\]
The open subset
\[
U=\{[t:x:y:z]\mid x\ne0,\ y\ne0,\ F\ne0,\ ty+x^2-z^2+2\mathrm i xz\ne0\}
\]
of \(\mathbb P^3\setminus B\) is **isomorphic to \((\mathbb C^\times)^3\)**. Consequently the log Calabi–Yau pair \((\mathbb P^3,B)\) is of **cluster type**. Here \(\mathrm i^2=-1\).

## Assumptions and scope

The base field is \(\mathbb C\). The polynomial \(F\) is homogeneous of degree four. The cited Example 7.1 establishes that this reduced quartic defines a log Calabi–Yau pair (index one, coregularity zero) whose singular locus is a plane conic and whose points have multiplicity at most two. The finding concerns this **specific** quartic, not every quartic singular along a plane conic.

Write \(T=t/x\), \(Y=y/x\), \(Z=z/x\) on the chart \(x\ne0\), and let \(F_1=F(T,1,Y,Z)\). The torus-chart assertion is an exact isomorphism of complex algebraic varieties, not just a rational parametrization.

## Proof

Set
\[
 u=\frac{TY+1-Z^2}{2},\qquad a=u+\mathrm i Z,\qquad b=u-\mathrm i Z,\qquad w=\frac{F_1}{4}.
\]
A direct expansion gives the identity
\[
 w=u^2+Z^2-Y^2-1=ab-Y^2-1.
\]
On \(U\), the functions \(Y,a,w\) are invertible. Conversely, let \((a,Y,w)\in(\mathbb C^\times)^3\) be arbitrary and define
\[
 b=\frac{w+Y^2+1}{a},\qquad
 Z=\frac{a-b}{2\mathrm i},\qquad
 T=\frac{a+b-1+Z^2}{Y}.
\]
These are regular Laurent expressions on the whole three-torus. For the point \([T:1:Y:Z]\), one has \(u=(a+b)/2\), \(F_1=4w\ne0\), and \(a=u+\mathrm i Z\ne0\), so this construction lands in \(U\). Both compositions are the identity: the first recovers \(a,Y,w\); the second recovers \(T,Y,Z\). Thus the displayed regular morphisms are inverse isomorphisms,
\[
 U\simeq\operatorname{Spec}\mathbb C[a^{\pm1},Y^{\pm1},w^{\pm1}]=(\mathbb C^\times)^3.
\]
The set \(U\) is nonempty, since the formulas are defined for every triple of nonzero complex coordinates, and is Zariski open in \(\mathbb P^3\setminus B\) by its four nonvanishing conditions. Projective three-space is a \(\mathbb Q\)-factorial Fano threefold. Theorem 2.9 of the cited work therefore applies to its already-established log Calabi–Yau pair and converts the full-dimensional torus in the complement into the cluster-type conclusion.

## Verification

The accompanying `verify.py` performs exact symbolic Laurent computations with SymPy. It checks \(F_1=4w\), recovery of \(a\) and \(b\), the factorization \(w=ab-Y^2-1\), and both reverse coordinate identities on the affine chart. Running `python verify.py` with SymPy available printed `VERIFY_OK: forward and inverse formulas are mutual rational identities; F=4W`. The algebraic proof above is complete without this computation.

## Relationship to prior work

Alves da Silva, Figueroa and Moraga introduce **exactly this quartic** in Example 7.1 and prove its singularity and log Calabi–Yau properties. Their introduction and Section 7 identify Example 7.1 as outside the coverage of their stated cluster-type detection criteria; they do not give this torus embedding or assert cluster type for the example. Their Theorem 2.9 supplies the criterion invoked only *after* constructing the new explicit chart. Moraga's subsequent survey, Section 6, repeats that the general classification of quartic torus complements remains open, without resolving this named example. The general classification remains outside the present claim.

## Limitations

Only the given Example 7.1 quartic is treated; no result is claimed for their different Example 7.2 or for all irreducible quartics with planar singular curves. The explicit open torus need not be unique, and the complement outside \(U\) is not classified. Literature searches did not reveal a previous statement of this particular chart or conclusion, but this does not establish absolute literature priority. No independent mathematical audit has been performed.

## References

1. E. Alves da Silva, F. Figueroa, J. Moraga, *Algebraic tori in the complement of quartic surfaces*, arXiv:2411.03506, first submitted 2024-11-05; especially Theorem 2.9, Theorem 6.1, and Example 7.1. https://arxiv.org/abs/2411.03506
2. E. Alves da Silva, F. Figueroa, J. Moraga, *Algebraic tori in the complement of quartic surfaces*, J. London Math. Soc. 113 (2026), e70427, DOI:10.1112/jlms.70427, especially Section 7. https://doi.org/10.1112/jlms.70427
3. J. Moraga, *Cluster type varieties*, arXiv:2602.23584, Section 6, especially Theorems 6.6–6.7 and Problem 6.8. https://arxiv.org/abs/2602.23584
