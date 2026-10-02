# Heightwise stationary laws for the Rabinovich–Fabrikant flow

Consider
\[
\dot x=y(z-1+x^2)+\gamma x,\qquad
\dot y=x(3z+1-x^2)+\gamma y,\qquad
\dot z=-2z(\alpha+xy),
\]
with \(\alpha,\gamma>0\). Put
\[
R=x^2+y^2.
\]

## Result

Let \(\mu\) be a compactly supported invariant probability measure. Its restriction to \(z<0\) is zero, and its restriction to \(z=0\) is supported at the origin. Write any nonzero positive component as an invariant probability \(\nu\) with \(\nu\{z>0\}=1\).

Then the stationary balance holds at almost every occupied height:
\[
\boxed{\mathbb E_\nu[xy\mid z]=-\alpha}
\qquad \nu\text{-a.s.}
\]
Consequently,
\[
\boxed{\mathbb E_\nu[R\mid z]
=2\alpha+\mathbb E_\nu[(x+y)^2\mid z]}
\qquad \nu\text{-a.s.}
\]

There is also an exact logarithmic-radial identity:
\[
\boxed{\int \frac{xyz}{R}\,d\nu=-\frac{\gamma}{4}},
\]
and hence
\[
\boxed{\int z\frac{(x+y)^2}{R}\,d\nu
=\int z\,d\nu-\frac{\gamma}{2}}.
\]
The ratio is defined arbitrarily on \(R=0\), which is a \(\nu\)-null set.

These formulas refine, but do not re-claim, the previously published global recurrence identities
\[
\int xy\,d\nu=-\alpha
\]
and
\[
\int z\,d\nu
=\frac{\gamma}{2}
+\frac{\gamma}{4\alpha}\int (x+y)^2\,d\nu.
\]

## Proof

The exact Lie derivatives are
\[
\dot R=2\gamma R+8xyz
\]
and
\[
\frac{d}{dt}(R+4z)=2\gamma R-8\alpha z.
\]
The sign of \(z\) is invariant. On \(z<0\), the second derivative above is strictly positive, so an invariant probability cannot give positive mass to that half-space. On \(z=0\), \(\dot R=2\gamma R\), so invariant probability mass there is supported at \(R=0\), namely the origin.

Now let \(\nu\{z>0\}=1\). Fix a bounded continuous \(\varphi\). Choose smooth cutoffs \(\chi_\varepsilon\) vanishing near zero and converging pointwise to one on \((0,\infty)\), and choose a smooth scalar observable \(q_\varepsilon\) whose derivative on the compact \(z\)-range of the support is
\[
q_\varepsilon'(z)=\frac{\varphi(z)\chi_\varepsilon(z)}{z}.
\]
Invariance gives
\[
0=\int Lq_\varepsilon\,d\nu
=-2\int \varphi(z)\chi_\varepsilon(z)(\alpha+xy)\,d\nu.
\]
Compact support gives domination, so
\[
\int \varphi(z)(\alpha+xy)\,d\nu=0
\]
for every bounded continuous \(\varphi\). This is exactly
\[
\mathbb E_\nu[xy\mid z]=-\alpha.
\]
Since
\[
R+2xy=(x+y)^2,
\]
the conditional radial identity follows.

To obtain the logarithmic identity, first note that \(R=0\) is the invariant \(z\)-axis. If \(\nu\) charged its positive part, the normalized restriction would be invariant, but there \(\dot z=-2\alpha z\), which is incompatible with an invariant probability supported on \(z>0\). Thus \(\nu\{R=0\}=0\).

Apply invariance to smooth cutoff approximations of \(\log R\). On \(R>0\),
\[
L\log R=2\gamma+\frac{8xyz}{R}.
\]
Because
\[
\frac{|xy|}{R}\le\frac12
\]
and the support is compact, dominated convergence gives
\[
\int\frac{xyz}{R}\,d\nu=-\frac{\gamma}{4}.
\]
Finally,
\[
z\frac{(x+y)^2}{R}=z+2\frac{xyz}{R},
\]
which yields the last identity.

## Prior coverage and originality boundary

A published 20 September 2026 result already established the global off-plane balance \(\int xy=-\alpha\), the exact mean-height defect, sign selection for recurrent components, and the corresponding periodic-orbit consequences. Those statements are prior work and are not claimed here.

The contribution retained here is the heightwise conditional law, its conditional radial refinement, and the logarithmic-radial stationary identity. A global average such as \(\int xy=-\alpha\) does not imply the conditional identity: the cutoff-generator argument with arbitrary test functions of \(z\) is the additional step.

## Limitations

The statements require \(\alpha,\gamma>0\) and compact support. They are stationary identities, not pointwise trajectory identities. They do not assert existence or uniqueness of a nontrivial invariant probability or attractor, and they do not classify unbounded dynamics.

## References

1. M. I. Rabinovich and A. L. Fabrikant, “Stochastic self-modulation of waves in nonequilibrium media,” *Soviet Physics JETP* 50 (1979), 311–317.
2. “Recurrence sign selection and mean-height law for the Rabinovich--Fabrikant system,” published 20 September 2026, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-rabinovich-fabrikant-recurrence-sign-selection--047ddc1ae9fc
