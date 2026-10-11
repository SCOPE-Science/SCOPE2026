# Zbăganu rigidity on the quadratic Lorentz plane
## Finding
Let \(0<\omega<1\), and let \(X_\omega=(\mathbb R^2,N_\omega)\) be the real quadratic Lorentz plane
\[
N_\omega(u,v)=\left(\max\{|u|,|v|\}^2+\omega\min\{|u|,|v|\}^2\right)^{1/2}.
\]
Then its Zbăganu constant is
\[
C_Z(X_\omega)=\frac{2}{1+\omega}.
\]
Moreover, a nonzero pair \((x,y)\) attains this value if and only if, up to signed-coordinate symmetries, exchanging \(x\) and \(y\), and changing either vector sign, there is an \(r>0\) such that
\[
x=r(1,1),\qquad y=r(1,-1).
\]
Equivalently, the Zbăganu extremizers are exactly the pairs of equal Euclidean length that lie on the two diagonal directions and are Euclidean orthogonal. Thus on this classical Lorentz family the Zbăganu constant coincides with the known value \(2/(1+\omega)\) of the Jordan--von Neumann and Ptolemy constants, but its maximizing geometry is rigid.

## Assumptions and scope
The scalar field is real and \(0<\omega<1\). For \(z=(z_1,z_2)\), write
\[
E(z)=\sqrt{z_1^2+z_2^2}.
\]
The Zbăganu constant is
\[
C_Z(X_\omega)=
\sup_{\substack{x,y\in X_\omega\\(x,y)\ne(0,0)}}
\frac{N_\omega(x+y)N_\omega(x-y)}
{N_\omega(x)^2+N_\omega(y)^2}.
\]
No normalization of \(x\) and \(y\) is imposed; the quotient is invariant under common nonzero scaling.

## Proof
For every \(z=(u,v)\),
\[
N_\omega(z)^2
=
E(z)^2-(1-\omega)\min\{|u|,|v|\}^2.
\]
Consequently
\[
\frac{1+\omega}{2}E(z)^2
\le
N_\omega(z)^2
\le
E(z)^2.
\]
The lower equality holds exactly when
\[
|u|=|v|,
\]
and, for nonzero \(z\), the upper equality holds exactly when one coordinate is zero.

Put
\[
p=x+y,\qquad q=x-y.
\]
Then
\[
N_\omega(p)N_\omega(q)
\le
E(p)E(q).
\]
By the arithmetic--geometric mean inequality and the Euclidean parallelogram identity,
\[
E(p)E(q)
\le
\frac{E(p)^2+E(q)^2}{2}
=
E(x)^2+E(y)^2.
\]
Using the lower norm comparison on \(x\) and \(y\),
\[
E(x)^2+E(y)^2
\le
\frac{2}{1+\omega}
\left(N_\omega(x)^2+N_\omega(y)^2\right).
\]
Hence
\[
C_Z(X_\omega)\le\frac{2}{1+\omega}.
\]

For the reverse inequality take
\[
x=(1,1),\qquad y=(1,-1).
\]
Then
\[
N_\omega(x)^2=N_\omega(y)^2=1+\omega,
\]
while
\[
x+y=(2,0),\qquad x-y=(0,2),
\]
so
\[
N_\omega(x+y)=N_\omega(x-y)=2.
\]
The quotient is therefore
\[
\frac{4}{2(1+\omega)}=\frac{2}{1+\omega}.
\]

It remains to classify equality. Suppose the Zbăganu quotient equals \(2/(1+\omega)\). Since this value is strictly larger than \(1\), neither \(p\) nor \(q\) is zero. Equality must hold in every step of the upper-bound chain.

Equality in
\[
N_\omega(p)\le E(p),
\qquad
N_\omega(q)\le E(q)
\]
forces \(p\) and \(q\) to lie on coordinate axes. Equality in the arithmetic--geometric mean step forces
\[
E(p)=E(q).
\]
Equality in the lower comparisons for \(x\) and \(y\) forces
\[
|x_1|=|x_2|,
\qquad
|y_1|=|y_2|.
\]
The two nonzero axis vectors \(p\) and \(q\) cannot lie on the same coordinate axis, because then \(x=(p+q)/2\) and \(y=(p-q)/2\) would also lie on that axis and could not satisfy the diagonal equalities. Thus \(p\) and \(q\) lie on different coordinate axes. Since their Euclidean lengths are equal, after signed-coordinate symmetries and order reversal we may write
\[
p=(2r,0),\qquad q=(0,2r)
\]
with \(r>0\). Therefore
\[
x=\frac{p+q}{2}=r(1,1),
\qquad
y=\frac{p-q}{2}=r(1,-1).
\]
Conversely every pair in this symmetry orbit gives the sharp quotient, completing the classification.

## Verification
The proof has three inequalities, and all equality conditions are explicit:

1. \(N_\omega(z)\le E(z)\), with nonzero equality exactly on coordinate axes.
2. \(E(p)E(q)\le(E(p)^2+E(q)^2)/2\), with equality exactly when \(E(p)=E(q)\).
3. \(E(z)^2\le2N_\omega(z)^2/(1+\omega)\), with equality exactly on the diagonal rays.

Tracing these conditions simultaneously gives the complete extremizer orbit. No numerical optimization, finite sampling, or external certificate is used as proof.

## Relationship to prior work
Llorens-Fuster, Mazcuñán-Navarro, and Reich introduced a systematic treatment of the Ptolemy and Zbăganu constants, proved general inequalities, and calculated exact values for several spaces. The accessible publisher material confirms the Zbăganu definition, its fixed-point motivation, and the presence of several exact examples, but the full article body was not available through the checked access route; this remains the principal bibliographic risk.

Zuo's 2011 open article studies a different James-type geometric constant for absolute normalized norms. Its complete text includes a Lorentz-sequence-space example for exponents \(r\ge2\), so it is a close same-object comparison, but it does not discuss the Zbăganu constant.

Targeted searches for the quadratic Lorentz norm together with Zbăganu terminology, the candidate value \(2/(1+\omega)\), and maximizing-pair language found no equivalent statement. The known coincidence of the Jordan--von Neumann and Ptolemy values with \(2/(1+\omega)\) does not by itself classify maximizers of the multiplicative Zbăganu quotient; the equality tracing above is an additional statement.

## Limitations
The theorem concerns only the real two-dimensional Lorentz family at exponent \(2\). It does not assert an analogous Zbăganu formula for \(d^{(2)}(\omega,q)\) when \(q\ne2\), nor does it classify near-extremizers quantitatively.

The complete body of the 2010 principal Zbăganu article was not inspectable in the checked route after open-access attempts; the accessible publisher preview was inspected and the unresolved coverage risk is recorded rather than treated as evidence of noncoverage.

## References
1. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” *Nonlinear Analysis* 72 (2010), 3984--3993, DOI 10.1016/j.na.2010.01.030; published 2010-06-01; primary MSC 46B20.
2. Z. Zuo, “A geometrical constant and normal normal structure in Banach Spaces,” *Journal of Inequalities and Applications* 2011, Article 16, DOI 10.1186/1029-242X-2011-16; published 2011-06-23.
