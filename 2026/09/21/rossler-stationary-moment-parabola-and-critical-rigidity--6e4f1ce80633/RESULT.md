# A heightwise stationary-flux law for the Rössler system

Consider the classical Rössler system
\[
\dot x=-y-z,\qquad
\dot y=x+ay,\qquad
\dot z=b+z(x-c),
\]
with \(a,b,c>0\). Let \(\mu\) be a compactly supported invariant probability measure and let
\[
\nu=z_\#\mu
\]
be its \(z\)-marginal.

## Result

For any version
\[
q(z)=\mathbb E_\mu[x\mid z],
\]
one has
\[
\boxed{\nu(\{0\})=0}
\]
and
\[
\boxed{\mathbb E_\mu[x\mid z]=c-\frac{b}{z}}
\qquad \nu\text{-a.e.}
\]

Thus the stationary \(x\)-flux is fixed exactly at almost every occupied height, not merely after averaging over the whole invariant measure.

As an integrated consequence,
\[
b\int\frac1z\,d\mu
=c-\int x\,d\mu.
\]
The familiar first-moment balance
\[
\int x\,d\mu=a\int z\,d\mu
\]
then recovers the previously published harmonic-height identity. That integrated identity is prior work and is not claimed here.

## Proof

Let \(q(z)\) be a conditional expectation of \(x\) given \(z\). For every smooth compactly supported test function \(\psi\), invariance gives
\[
0=\int L\psi(z)\,d\mu
=\int \psi'(z)\,[b+z(x-c)]\,d\mu.
\]
Conditioning on \(z\),
\[
0=\int \psi'(z)\,[b+z(q(z)-c)]\,d\nu(z).
\]

Define the compactly supported signed measure
\[
d\eta(z)=[b+z(q(z)-c)]\,d\nu(z).
\]
The last identity says that the distributional derivative of \(\eta\) is zero. A distribution on the real line with zero derivative is constant. Since \(\eta\) has compact support, that constant must be zero. Therefore
\[
[b+z(q(z)-c)]\,\nu(dz)=0.
\]
At \(z=0\) the coefficient is \(b>0\), so
\[
\nu(\{0\})=0.
\]
For \(\nu\)-almost every remaining \(z\),
\[
q(z)=c-\frac bz.
\]

Because \(x\) is bounded on the compact support, \(q\) is essentially bounded. The formula therefore also shows directly that \(1/z\) is integrable with respect to \(\nu\), and integrating the conditional identity gives the displayed harmonic consequence.

## Prior coverage and originality boundary

A published 20 September 2026 result already established the exact mean/variance parabola for compact invariant measures of the positive-parameter Rössler flow, the covariance identities, the compact-recurrence discriminant threshold, the harmonic-height identity, and uniqueness of the stationary probability measure at the saddle-node boundary. Those statements are prior work and are not re-claimed here.

The surviving contribution is the heightwise conditional law. The earlier integrated identity constrains only one scalar average and does not imply the conditional relation. The distributional stationary-flux argument above supplies the additional test-function information needed to identify the conditional mean at almost every height.

## Limitations

The theorem assumes \(a,b,c>0\) and compact support. It is a stationary conditional-expectation identity, not a pointwise relation along individual trajectories. It does not classify invariant measures or attractors.

## References

1. O. E. Rössler, “An equation for continuous chaos,” *Physics Letters A* 57 (1976), 397–398.
2. “Exact compact-recurrence threshold and invariant-measure laws for the Rössler system,” published 20 September 2026, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-rossler-compact-recurrence-threshold-and-measure-laws--6e87f2d3c811
3. J. J. Bramburger and G. Fantuzzi, “Data-driven discovery of invariant measures,” *Proceedings of the Royal Society A* 480 (2024), 20230627.
