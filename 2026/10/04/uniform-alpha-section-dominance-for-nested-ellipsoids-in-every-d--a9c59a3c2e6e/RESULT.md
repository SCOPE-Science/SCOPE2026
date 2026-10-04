# Uniform \(\alpha\)-section dominance for nested ellipsoids in every dimension
## Finding
Let \(d\ge2\), and let \(A\subseteq B\subset\mathbb R^d\) be nondegenerate ellipsoids. There is an oriented normal direction which works simultaneously for every \(\alpha\in(0,1/2]\): the unique hyperplane orthogonal to that direction whose chosen halfspace contains the fraction \(\alpha\) of \(A\) contains a fraction \(\beta(\alpha)\ge\alpha\) of \(B\).

A stronger normalized statement is available. After an invertible affine change of coordinates sending \(A\) to the Euclidean unit ball \(D\), write
\[
B=c+T D,
\]
where \(T\) is invertible. Then every unit vector \(u\) satisfying \(c\cdot u\ge0\) works simultaneously for all \(\alpha\in(0,1/2]\).

## Assumptions and scope
An \(\alpha\)-section is understood through an oriented hyperplane and its chosen closed halfspace: the chosen halfspace contains exactly the fraction \(\alpha\) of the body's \(d\)-dimensional volume. Ellipsoids are compact affine images of the Euclidean unit ball with nonempty interior. The theorem is affine invariant because invertible affine maps preserve hyperplanes, nesting, and volume fractions.

The result concerns nested ellipsoids only. It does not settle the unrestricted higher-dimensional problem for arbitrary nested convex bodies.

## Proof
Let \(D=\{x\in\mathbb R^d:\|x\|\le1\}\). By affine invariance it is enough to prove the normalized statement with \(A=D\) and \(B=c+TD\). For a unit vector \(u\), put
\[
s=\|T^{\mathsf T}u\|>0.
\]
The support function of \(B\) in direction \(u\) is
\[
h_B(u)=c\cdot u+s.
\]
Because \(D\subseteq B\), support-function monotonicity gives
\[
c\cdot u+s=h_B(u)\ge h_D(u)=1. \tag{1}
\]
Choose any unit vector \(u\) with \(c\cdot u\ge0\); such a vector always exists, and if \(c=0\) every unit vector qualifies.

For \(z\in[-1,1]\), define the normalized unit-ball cap function
\[
C_d(z)=\frac{\operatorname{vol}_d\{x\in D:u\cdot x\ge z\}}{\operatorname{vol}_d(D)}.
\]
Rotational symmetry makes this independent of the chosen unit \(u\). The function \(C_d\) is continuous and strictly decreasing, with \(C_d(0)=1/2\). Hence for every \(\alpha\in(0,1/2]\) there is a unique \(t=t_{d,\alpha}\in[0,1)\) satisfying \(C_d(t)=\alpha\). The oriented hyperplane \(u\cdot x=t\) therefore cuts the chosen fraction \(\alpha\) from \(D\).

Under the parametrization \(x=c+Ty\) of \(B\), the same halfspace becomes
\[
(T^{\mathsf T}u)\cdot y\ge t-c\cdot u.
\]
Consequently its fraction of \(B\) is
\[
\beta(\alpha)=C_d\!\left(\frac{t-c\cdot u}{s}\right), \tag{2}
\]
with the evident endpoint interpretation if the normalized threshold lies outside \([-1,1]\).

It remains to compare the two normalized thresholds. From \(t\in[0,1]\), \(c\cdot u\ge0\), and (1),
\[
(c\cdot u)+ts
=t\bigl((c\cdot u)+s\bigr)+(1-t)(c\cdot u)
\ge t.
\]
Thus
\[
\frac{t-c\cdot u}{s}\le t.
\]
Since \(C_d\) is decreasing, (2) gives
\[
\beta(\alpha)\ge C_d(t)=\alpha.
\]
The same fixed \(u\) works for every \(\alpha\in(0,1/2]\). Undoing the affine normalization transports this fixed parallel family of hyperplanes back to the original pair \(A\subseteq B\), completing the proof.

## Verification
The proof uses only affine invariance of volume fractions, the elementary support function of an ellipsoid, and monotonicity of the unit-ball cap function. The decisive scalar implication is
\[
c_0\ge0,\qquad c_0+s\ge1,\qquad 0\le t\le1
\quad\Longrightarrow\quad
\frac{t-c_0}{s}\le t.
\]
It is an identity-plus-positivity argument because
\[
c_0+ts-t=t(c_0+s-1)+(1-t)c_0\ge0.
\]
The bundled verifier checks this identity exactly over a rational stress grid. No finite computation is used as a substitute for the general proof.

## Relationship to prior work
Fruchard and Magazinov proved that for nested planar convex bodies \(A\subseteq B\) and every \(\alpha\in(0,1/2)\), some \(\alpha\)-section of \(A\) is a \(\beta\)-section of \(B\) with \(\beta\ge\alpha\), and their abstract states that the question remains open when the word “planar” is dropped. Chevallier, Fruchard, and Vîlcu formulate the closely related arbitrary-dimensional nested-body conjecture in their full treatment of \(\alpha\)-sections and record the planar result. Their literature survey also discusses ellipsoids in the one-body floating-body setting, not this two-body nested dominance statement.

Kincses studies simultaneous prescribed \(\alpha\)-sections for well-separated families of strictly convex bodies. Nested ellipsoids are not a well-separated family, and prescribed equality for separated bodies does not imply the one-sided nested inequality proved here.

The present theorem is therefore a special-class result in the higher-dimensional direction, strengthened by the fact that one normal direction works for every \(\alpha\) simultaneously.

## Limitations
The theorem does not address arbitrary nested convex bodies, fair partitions into many pieces in higher dimension, or uniqueness of the working direction. It also makes no claim that all directions work when the normalized outer ellipsoid is off-center; the proved sufficient family is \(c\cdot u\ge0\). The literature search cannot exclude an unindexed elementary observation about nested ellipsoids, so that remains the principal originality risk.

## References
1. A. Fruchard and A. Magazinov, “Fair partitioning by straight lines,” arXiv:1509.02090, first public version 7 September 2015; later in *Convexity and Discrete Geometry Including Graph Theory*, DOI 10.1007/978-3-319-28186-5_14.
2. N. Chevallier, A. Fruchard, and C. Vîlcu, “Envelopes of \(\alpha\)-sections,” arXiv:1509.02084, first public version 7 September 2015; HAL hal-01194697.
3. J. Kincses, “The topological type of the \(\alpha\)-sections of convex sets,” *Advances in Mathematics* 217 (2008), 2159–2169, DOI 10.1016/j.aim.2007.09.015.
