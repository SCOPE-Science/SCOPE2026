# Axis-compatible scaling and the ring-escape obstruction for Gamma-bounded axisymmetric Navier--Stokes blowup

## Context

Let \(v\) be an axisymmetric vector field in cylindrical coordinates
\((r,\theta,z)\), and put \(\Gamma=r v_\theta\).  The motivating extraction
problem asks whether a finite-time blowup with
\(\sup_t\|\Gamma(t)\|_\infty<\infty\) necessarily yields a nontrivial
axisymmetric ancient limit after axis-centered rescaling.

This record isolates a genuine geometric obstruction in the common
peak-normalized construction.  It does **not** claim a Navier--Stokes
blowup example or a regularity theorem.

## Definitions

For a space-time center \(x_0=(x_{0,h},z_0)\) and scale \(\lambda>0\), write
\[
v^\lambda(y,s)=\lambda v(x_0+\lambda y,T_*+\lambda^2s).
\]
For peak points \(x_k\) at times \(t_k\), put
\(M_k=|v(x_k,t_k)|\to\infty\), \(\mu_k=M_k^{-1}\), and let
\(r_k=|x_{k,h}|\) be the distance of the peak from the symmetry axis.  If the
renormalization is centered at the projection of \(x_k\) to the axis, the
normalized peak has horizontal distance
\[
d_k=\frac{r_k}{\mu_k}=r_kM_k.
\]

## Result

1. **On-axis compatibility.**  If the spatial center lies on the symmetry
   axis, the affine rescaling intertwines rotations about that axis.  Hence an
   axisymmetric field remains axisymmetric, and its swirl variable is exactly
   scale invariant:
   \[
   \Gamma^\lambda(y,s)=\rho\,(v^\lambda)_\theta(y,s)
   =\Gamma(x_0+\lambda y,T_*+\lambda^2s).
   \]

2. **Off-axis caution.**  An off-axis translation does not, in general,
   intertwine the global rotation action and therefore does not preserve
   axisymmetry.  No universal statement of the form
   “off-axis \(\Gamma^\lambda\to0\)” follows from the bound on the original
   \(\Gamma\): after translation, cylindrical directions relative to the new
   origin mix the original radial and azimuthal components.  Special fields
   (for example a constant axial field) can remain rotationally symmetric
   after an off-axis recentering, so an “if and only if for every particular
   field” formulation is also too strong.

3. **Ring escape.**  For axis-projected amplitude renormalization, the
   normalized peak is at distance \(d_k\).  If \(d_k\to\infty\), it leaves
   every fixed compact set; a local compactness limit can then no longer
   inherit the normalization \(|u_k(y_k,0)|=1\) from those peaks.  If
   \(\sup_k d_k<\infty\), the peak locations stay in a fixed ball and this
   particular geometric obstruction disappears, although the analytic
   compactness estimates still have to be proved separately.

4. **Backward time for a model Type-II rate.**  If
   \(M_k=(T_*-t_k)^{-\alpha}\) with \(\alpha>1/2\), then
   \[
   \frac{T_*-t_k}{\mu_k^2}=(T_*-t_k)^{1-2\alpha}\longrightarrow\infty.
   \]
   Thus the model amplitude scaling has arbitrarily long backward time; the
   obstruction in item 3 is spatial, not temporal.

5. **The Gamma bound gives no kinematic bound on \(d_k\).**  For arbitrary
   \(r_k>0\) and \(M_k>0\), choose a smooth compactly supported axisymmetric
   divergence-free *poloidal* bump \(W\), supported near \(r=1\), with
   \(W_\theta=0\) and \(\max|W|=1\), and set
   \[
   v^{(k)}(r,z)=M_k W(r/r_k,z/r_k).
   \]
   Then \(\Gamma\equiv0\), while the maximum amplitude is \(M_k\) at radius
   comparable to \(r_k\).  Hence a bound on \(\Gamma\) alone does not impose a
   purely kinematic upper bound on \(r_kM_k\).

Consequently, any peak-normalized **axis-projected** extraction that intends to
retain the chosen peak on compact sets needs a non-escape estimate such as
\(\limsup r_kM_k<\infty\), or a different mechanism restoring nontriviality.

## Proof / evidence

For an on-axis center, \(R(x_0+\lambda y)=x_0+\lambda Ry\) for every rotation
\(R\) about the symmetry axis.  If the center is off the axis, the difference
between the two sides is \(Rx_0-x_0\), which is generally nonzero.  This is
the precise symmetry statement; it does not imply a scalar off-axis
\(\Gamma\)-limit.

For item 1, on-axis scaling gives \(r_x=\lambda\rho\) and
\((v^\lambda)_\theta=\lambda v_\theta\), so
\(\rho(v^\lambda)_\theta=(\lambda\rho)v_\theta=\Gamma\).

Item 3 is the identity \(d_k=r_k/\mu_k\).  Item 4 is the displayed exponent
calculation.  For item 5, the cylindrical divergence operator scales by the
common factor \(M_k/r_k\), so a divergence-free prototype remains
divergence-free; choosing \(W_\theta=0\) makes \(\Gamma\) vanish identically.

The accompanying script checks the on-axis identity, the rotation-center
geometry, the Type-II exponent, and representative ring-escape sequences.

## Limitations

The compactly supported bumps are kinematic test fields, not
Navier--Stokes solutions.  This record does not prove that an actual blowup
realizes \(d_k\to\infty\), does not disprove any global regularity statement,
and does not by itself establish the analytic compactness required when
\(d_k\) is bounded.  It diagnoses one obstruction to a specific
axis-projected peak-normalization method.

## Reproducibility

Run `python3 artifacts/scaling_check.py` (requires SymPy).

## References

- Caffarelli--Kohn--Nirenberg partial regularity and epsilon regularity.
- Chen--Strain--Tsai--Yau on axisymmetric Navier--Stokes blow-up rates.
- Gallagher--Koch--Planchon and Kenig--Koch on critical-element/profile
  compactness methods for Navier--Stokes.
