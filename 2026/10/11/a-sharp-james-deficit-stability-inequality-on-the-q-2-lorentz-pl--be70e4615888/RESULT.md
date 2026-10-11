# A sharp James-deficit stability inequality on the \(q=2\) Lorentz plane
## Finding
For \(0<\omega<1\), let \(X_\omega=(\mathbb R^2,N_\omega)\) be the real two-dimensional Lorentz space
\[
N_\omega(u,v)=\left(\max\{|u|,|v|\}^2+\omega\min\{|u|,|v|\}^2\right)^{1/2}.
\]
For \(z=(z_1,z_2)\), put
\[
D(z)=|z_1^2-z_2^2|,
\qquad
m(z)=\min\{|z_1|,|z_2|\}.
\]
For \(x,y\in S_{X_\omega}\), let
\[
F_\omega(x,y)=\min\{N_\omega(x+y),N_\omega(x-y)\}
\]
and let \(\sigma(x,y)=1\) when \(\langle x,y\rangle\ge0\), while \(\sigma(x,y)=-1\) otherwise. Then
\[
\frac{4}{1+\omega}-F_\omega(x,y)^2
\ge
\frac{1-\omega}{1+\omega}\bigl(D(x)+D(y)\bigr)
+2|\langle x,y\rangle|
+(1-\omega)m\!\left(x-\sigma(x,y)y\right)^2.
\]
The inequality is sharp on a full one-parameter family: equality holds for every
\[
x=(a,b),\qquad y=(a,-b),\qquad a\ge b\ge0,\qquad a^2+\omega b^2=1,
\]
and for all pairs obtained from these by the signed-coordinate symmetries, vector sign changes, and order reversal. In particular, the classical value
\[
J(X_\omega)=\frac{2}{\sqrt{1+\omega}}
\]
is recovered, with equality only at the diagonal James-extremal orbit. Quantitatively, if
\[
F_\omega(x,y)\ge J(X_\omega)-\varepsilon,
\]
then
\[
D(x)+D(y)\le\frac{4\sqrt{1+\omega}}{1-\omega}\,\varepsilon,
\qquad
|\langle x,y\rangle|\le\frac{2}{\sqrt{1+\omega}}\,\varepsilon,
\]
and
\[
m\!\left(x-\sigma(x,y)y\right)^2
\le
\frac{4}{(1-\omega)\sqrt{1+\omega}}\,\varepsilon.
\]

## Assumptions and scope
The scalar field is real and \(0<\omega<1\). The norm is
\[
N_\omega(u,v)=\left(\max\{|u|,|v|\}^2+\omega\min\{|u|,|v|\}^2\right)^{1/2}.
\]
For \(z=(z_1,z_2)\), define
\[
D(z)=|z_1^2-z_2^2|,
\qquad
m(z)=\min\{|z_1|,|z_2|\}.
\]
The result is a quantitative refinement of the classical James-constant calculation at Lorentz exponent \(q=2\). It controls three independent geometric defects: imbalance from a diagonal ray, failure of Euclidean orthogonality, and failure of the Euclidean-shorter James chord to lie on a coordinate axis.

## Proof
Let \(z=(z_1,z_2)\in S_{X_\omega}\), and write
\[
M=\max\{|z_1|,|z_2|\},
\qquad
m=\min\{|z_1|,|z_2|\}.
\]
The unit-sphere equation is
\[
M^2+\omega m^2=1.
\]
Since
\[
D(z)=M^2-m^2,
\]
we obtain
\[
m^2=\frac{1-D(z)}{1+\omega}.
\]
Therefore
\[
\|z\|_2^2=M^2+m^2
=\frac{2}{1+\omega}
-\frac{1-\omega}{1+\omega}D(z).
\]
This identity records exactly the Euclidean radial deficit from the two diagonal rays.

Now take \(x,y\in S_{X_\omega}\), put
\[
p=\langle x,y\rangle,
\]
and let \(\sigma=1\) when \(p\ge0\), while \(\sigma=-1\) when \(p<0\). Then \(x-\sigma y\) is a Euclidean-shorter chord:
\[
\|x-\sigma y\|_2^2
=
\|x\|_2^2+\|y\|_2^2-2|p|.
\]
Also, for every \(z\in\mathbb R^2\),
\[
N_\omega(z)^2
=
\|z\|_2^2-(1-\omega)m(z)^2.
\]
Since
\[
F_\omega(x,y)^2
\le
N_\omega(x-\sigma y)^2,
\]
we have
\[
\frac{4}{1+\omega}-F_\omega(x,y)^2
\ge
\frac{4}{1+\omega}
-
N_\omega(x-\sigma y)^2.
\]
Substituting the preceding two identities gives exactly
\[
\frac{4}{1+\omega}-F_\omega(x,y)^2
\ge
\frac{1-\omega}{1+\omega}\bigl(D(x)+D(y)\bigr)
+2|p|
+(1-\omega)m(x-\sigma y)^2.
\]

Every term on the right is nonnegative, so
\[
F_\omega(x,y)\le\frac{2}{\sqrt{1+\omega}}.
\]
The diagonal pair
\[
x=\frac{(1,1)}{\sqrt{1+\omega}},
\qquad
y=\frac{(1,-1)}{\sqrt{1+\omega}}
\]
has both James chord norms equal to \(2/\sqrt{1+\omega}\), recovering the classical value.

For sharpness of the stability inequality, let
\[
x=(a,b),\qquad y=(a,-b),
\qquad
a\ge b\ge0,
\qquad
a^2+\omega b^2=1.
\]
Then
\[
F_\omega(x,y)=2b,
\qquad
D(x)=D(y)=a^2-b^2,
\qquad
\langle x,y\rangle=a^2-b^2,
\]
and
\[
m(x-y)=0.
\]
Because
\[
a^2-b^2=1-(1+\omega)b^2,
\]
both sides of the claimed inequality equal
\[
\frac{4}{1+\omega}\bigl(1-(1+\omega)b^2\bigr).
\]
Thus equality holds along the whole displayed one-parameter family.

Finally, if
\[
F_\omega(x,y)\ge J(X_\omega)-\varepsilon,
\]
then, because \(F_\omega(x,y)\le J(X_\omega)\),
\[
J(X_\omega)^2-F_\omega(x,y)^2
\le
2J(X_\omega)\varepsilon
=
\frac{4}{\sqrt{1+\omega}}\varepsilon.
\]
Bounding each nonnegative defect term separately yields the three quantitative near-extremizer estimates.

The right-hand side of the stability inequality vanishes exactly when
\[
D(x)=D(y)=0,
\qquad
\langle x,y\rangle=0,
\qquad
m(x-\sigma y)=0.
\]
Thus both vectors lie on diagonal rays and are Euclidean orthogonal, which gives precisely the signed-coordinate orbit of the displayed diagonal James pair.

## Verification
The proof is symbolic and exhaustive. Its two critical identities are
\[
\|z\|_2^2
=
\frac{2}{1+\omega}
-
\frac{1-\omega}{1+\omega}D(z)
\qquad
(z\in S_{X_\omega})
\]
and
\[
N_\omega(z)^2
=
\|z\|_2^2-(1-\omega)m(z)^2.
\]
The first follows by solving the unit-sphere equation for the smaller squared coordinate. The second is simply the definition rewritten in Euclidean form.

A direct algebraic substitution on the sign-reflected family verifies equality for every admissible parameter, not only at the James extremizer. Randomized numerical stress tests over several values of \(\omega\) were used only to look for a counterexample; they are not part of the proof.

## Relationship to prior work
Kato and Maligranda computed the James constant of the two-dimensional Lorentz spaces \(d^{(2)}(\omega,q)\) for \(q\ge2\). A later survey states their theorem in the form
\[
J(d^{(2)}(\omega,q))
=
2(1+\omega)^{-1/q}.
\]
At \(q=2\), this is the scalar value used above.

Kato, Maligranda, and Takahashi independently give the same \(q=2\) geometry on the classical subfamily \(\ell_{p,2}\). Their Example 3 proves the James and Jordan--von Neumann values by the Euclidean comparison
\[
\|z\|_2
\le
\left(\frac{2}{1+\omega}\right)^{1/2}N_\omega(z)
\]
and exhibits the diagonal pair. Their full text does not state a quantitative James-deficit inequality or near-extremizer control.

The 2014 Lorentz survey gives a general pointwise reduction for James constants of symmetric absolute norms and reproduces the exact Lorentz value, but its inspected text contains no quantitative stability, deficit, near-extremizer, or extremizer theorem. Targeted searches for those formulations did not locate an equivalent statement.

## Limitations
The theorem is restricted to the real two-dimensional Lorentz family at exponent \(q=2\). It gives a sharp attained lower bound for the James deficit and explicit near-extremizer controls, but it does not claim that the displayed three defect terms provide an optimal metric distance to the extremizer orbit.

The original 2001 Journal of Mathematical Analysis and Applications article was verified bibliographically and through its theorem as reproduced in the later survey, but a trustworthy full-text copy of that exact article was not obtained in the checked access routes. The complete 2001 Studia Mathematica article and the complete 2014 survey were inspected. A differently phrased quantitative refinement in unindexed literature remains a residual risk.

## References
1. M. Kato and L. Maligranda, “On James and Jordan--von Neumann Constants of Lorentz Sequence Spaces,” *Journal of Mathematical Analysis and Applications* 258 (2001), 457--465, DOI 10.1006/jmaa.2000.7367; published 2001-06-15.
2. M. Kato, L. Maligranda, and Y. Takahashi, “On James and Jordan--von Neumann constants and the normal structure coefficient of Banach spaces,” *Studia Mathematica* 144 (2001), 275--295, DOI 10.4064/sm144-3-5; MSC 46B20, 46E30, 46A45, 46B25.
3. K.-S. Saito, K.-I. Mitani, and R. Tanaka, “Recent development on James constant of 2-dimensional Lorentz sequence spaces,” *RIMS Kôkyûroku* 1906 (2014), 40--47.
