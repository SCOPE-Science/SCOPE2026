# Exact Ptolemy constant of the cubic two-dimensional Cesàro space
## Finding
Let \(X=\mathrm{ces}_3^{(2)}\) be \(\mathbb R^2\) with
\[
\|(x,y)\|_X=
\left(
|x|^3+\left(\frac{|x|+|y|}{2}\right)^3
\right)^{1/3}.
\]
Let \(\tau>0\) be the unique solution of
\[
3^{4/3}(1+\tau)^2
=
\tau\bigl((1+\tau)^2+8\bigr).
\]
Then the Ptolemy constant of \(X\) is
\[
C_{\mathrm{Pt}}(X)
=
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}
{3^{4/3}+\tau^2}
=
1.29958204360103898476109693949\ldots .
\]
An extremizing Ptolemy triple is
\[
x=(-1,0),\qquad
y=(0,-\tau),\qquad
z=(-1,-\tau).
\]

Numerically,
\[
\tau=2.76673988007870113906853704996\ldots .
\]

## Assumptions and scope
All scalars are real and the dimension is exactly two. The norm is the canonical two-dimensional section of the classical Cesàro sequence space at exponent \(3\). The Ptolemy constant is
\[
C_{\mathrm{Pt}}(X)
=
\sup
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum runs over nonzero pairwise distinct \(x,y,z\in X\).

The theorem determines this invariant only for \(\mathrm{ces}_3^{(2)}\). It does not assert a formula for all exponents or higher-dimensional Cesàro spaces.

## Proof
Set
\[
r_0=3^{-4/3}
\]
and introduce the Euclidean pullback
\[
H(x,y)^2=x^2+r_0y^2.
\]
Because the norm is absolute and homogeneous, for a nonzero vector with \(x\ne0\) it is enough to put
\[
t=\frac{|y|}{|x|}\in[0,\infty)
\]
and study
\[
F(t)
=
\frac{\|(1,t)\|_X^2}{H(1,t)^2}
=
\frac{\left((8+(1+t)^3)/8\right)^{2/3}}
{1+r_0t^2}.
\]
The two endpoint values agree:
\[
F(0)=\left(\frac98\right)^{2/3}
=\frac{3^{4/3}}4,
\qquad
\lim_{t\to\infty}F(t)
=
\frac1{4r_0}
=
\frac{3^{4/3}}4.
\]

For \(t>0\),
\[
\frac12\frac{d}{dt}\log F(t)
=
\frac{(1+t)^2}{8+(1+t)^3}
-
\frac{r_0t}{1+r_0t^2}.
\]
Thus an interior critical point satisfies
\[
r_0
=
R(t)
:=
\frac{(1+t)^2}
{t\bigl((1+t)^2+8\bigr)}.
\]
A direct differentiation gives
\[
R'(t)
=
-\frac{(t+1)(t^3+3t^2-5t+9)}
{t^2(t^2+2t+9)^2}.
\]
The polynomial in the numerator is strictly positive for \(t>0\), since
\[
t^3+3t^2-5t+9
=
t(t-1)^2
+
5\left(t-\frac35\right)^2
+
\frac{36}5.
\]
Therefore \(R\) is strictly decreasing from \(+\infty\) to \(0\), so there is a unique critical point \(\tau>0\). The equation \(R(\tau)=r_0\) is exactly
\[
3^{4/3}(1+\tau)^2
=
\tau\bigl((1+\tau)^2+8\bigr).
\]
The sign of the derivative shows that \(F\) increases on \((0,\tau)\) and decreases on \((\tau,\infty)\). Hence
\[
m:=\inf F
=
\frac{3^{4/3}}4,
\qquad
M:=\sup F
=
F(\tau).
\]
Equivalently,
\[
m\,H(w)^2
\le
\|w\|_X^2
\le
M\,H(w)^2
\qquad
(w\in\mathbb R^2).
\]

The norm \(H\) is Hilbertian and satisfies the Ptolemy inequality. Applying the preceding comparison to every admissible triple gives
\[
C_{\mathrm{Pt}}(X)\le\frac{M}{m}.
\]
Using \(r_0=3^{-4/3}\),
\[
\frac{M}{m}
=
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}
{3^{4/3}+\tau^2}
=:D.
\]

For the reverse inequality take
\[
x=(-1,0),\qquad
y=(0,-\tau),\qquad
z=x+y=(-1,-\tau).
\]
By absoluteness,
\[
\|x-y\|_X=\|z\|_X=\|(1,\tau)\|_X.
\]
Also
\[
x-z=(0,\tau),
\qquad
z-y=(-1,0).
\]
The needed squared norms are
\[
\|(1,\tau)\|_X^2
=
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}4,
\]
\[
\|(1,0)\|_X^2
=
\frac{3^{4/3}}4,
\qquad
\|(0,\tau)\|_X^2
=
\frac{\tau^2}4.
\]
Hence this triple has Ptolemy ratio
\[
\frac{\bigl(8+(1+\tau)^3\bigr)^{2/3}}
{3^{4/3}+\tau^2}
=
D.
\]
The upper and lower bounds coincide, proving the claim.

## Verification
The proof is global. Homogeneity reduces every nonzero direction to \(t=|y|/|x|\), including axis directions through endpoint limits. The critical-point equation has exactly one positive solution because \(R'(t)<0\) for every \(t>0\). Thus no local extremum is omitted.

The numerical checks are
\[
\tau
=
2.76673988007870113906853704996\ldots
\]
and
\[
C_{\mathrm{Pt}}(X)
=
1.29958204360103898476109693949\ldots .
\]
They are not used as proof.

## Relationship to prior work
Zuo's 2012 article defines the two-dimensional Cesàro family for every \(1<p<\infty\) and develops Ptolemy estimates for absolute normalized norms. Its concrete Cesàro calculation is the quadratic case \(\mathrm{ces}_2^{(2)}\), where the relevant Euclidean comparison reaches its extremum at the midpoint. The cubic norm above has an off-midpoint extremal direction governed by \(\tau\), so that quadratic example does not imply the present formula.

Saejung's 2010 treatment computes the von Neumann--Jordan and James constants of the two-dimensional Cesàro space only in the range \(1<p\le2\), so it neither treats the Ptolemy invariant nor reaches \(p=3\). Nikolova and Varošanec's 2013 work treats several other geometric constants of absolute normalized norms and includes Cesàro examples, but the listed constants are James, von Neumann--Jordan, Gao, Zbăganu, and \(A_2\), not the present Ptolemy formula.

A previously recorded exact Euclidean-distortion calculation for the same cubic Cesàro plane was checked only for statement overlap. It is a different invariant and does not itself supply the Ptolemy lower bound; the explicit three-point configuration above is required for equality.

## Limitations
The result is specific to the real two-dimensional exponent-\(3\) Cesàro norm. It does not supply a general \(p\)-formula or higher-dimensional theorem.

The originality comparison is bounded by the searchable and inspected literature. An older equivalent computation under a different normalization or convex-geometric notation remains a residual bibliographic risk, although no such statement was located in the checked sources or exact-formula searches.

## References
1. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107; published 2012-05-17.
2. S. Saejung, “Another look at Cesàro sequence spaces,” *Journal of Mathematical Analysis and Applications* 366 (2010), 530--537, DOI 10.1016/j.jmaa.2010.01.029.
3. L. Nikolova and S. Varošanec, “Geometric constants for Banach spaces with absolute normalized norms which corresponding functions are comparable,” *Journal of Nonlinear and Convex Analysis* 14 (2013), 529--549.
