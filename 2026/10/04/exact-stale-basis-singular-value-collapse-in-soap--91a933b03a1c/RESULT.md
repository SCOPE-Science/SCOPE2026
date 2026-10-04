# Exact stale-basis singular-value collapse in SOAP
## Finding

SOAP applies Adam-like coordinatewise normalization after rotating a matrix gradient into a Shampoo preconditioner eigenbasis. When that basis is stale, even a stationary positive-definite gradient can acquire an exactly quantifiable singular-value collapse.

Let a constant symmetric positive-definite gradient matrix be
\[
G_\kappa
=
\frac12
\begin{bmatrix}
\kappa+1 & \kappa-1\\
\kappa-1 & \kappa+1
\end{bmatrix},
\qquad
\kappa>1.
\]
Its eigenvalues are
\[
\kappa
\qquad\text{and}\qquad
1,
\]
and its eigenbasis is rotated by \(45^\circ\) from the coordinate basis.

Freeze SOAP's preconditioner basis at the identity and let the constant gradient persist. For any
\[
\beta_1,\beta_2\in[0,1),
\qquad
\varepsilon>0,
\]
the first-moment state converges to \(G_\kappa\), the second-moment state converges entrywise to \(G_\kappa\odot G_\kappa\), and the stationary normalized update is
\[
N_{\rm stale}
=
\begin{bmatrix}
p&r\\
r&p
\end{bmatrix},
\]
where
\[
p
=
\frac{\kappa+1}{\kappa+1+2\varepsilon},
\qquad
r
=
\frac{\kappa-1}{\kappa-1+2\varepsilon}.
\]
Because \(p>r>0\), its singular values are exactly
\[
p+r
\qquad\text{and}\qquad
p-r.
\]
Therefore
\[
\kappa_2(N_{\rm stale})
=
\frac{p+r}{p-r}
=
\kappa
+
\frac{\kappa^2-1}{2\varepsilon}.
\]
The small singular value is
\[
\sigma_{\min}(N_{\rm stale})
=
\frac{4\varepsilon}
{
(\kappa+1+2\varepsilon)
(\kappa-1+2\varepsilon)
}.
\]

Now refresh the basis to the exact eigenbasis of \(G_\kappa\). In that basis the gradient is diagonal, so SOAP's stationary update has eigenvalues
\[
\frac{\kappa}{\kappa+\varepsilon}
\qquad\text{and}\qquad
\frac1{1+\varepsilon}.
\]
After rotating back, its spectral condition number is
\[
\kappa_2(N_{\rm fresh})
=
\frac{
\kappa(1+\varepsilon)
}{
\kappa+\varepsilon
}.
\]

Thus
\[
\lim_{\varepsilon\downarrow0}
N_{\rm fresh}
=
I,
\]
while
\[
\lim_{\varepsilon\downarrow0}
N_{\rm stale}
=
\begin{bmatrix}
1&1\\
1&1
\end{bmatrix},
\]
which has rank one. At fixed
\[
\kappa=2
\]
and
\[
\varepsilon=10^{-8},
\]
the exact stale-basis condition number is
\[
150000002,
\]
while the fresh-basis condition number is approximately
\[
1.000000005.
\]

The singular perturbation is not confined to a \(45^\circ\) error. Let the true eigenbasis be rotated by an angle \(\theta\) from a frozen coordinate basis. The off-diagonal entry of the rotated gradient has magnitude
\[
c_\theta
=
\frac{\kappa-1}{2}
|\sin(2\theta)|.
\]
The stationary normalized off-diagonal magnitude is exactly
\[
r_\varepsilon(\theta)
=
\frac{c_\theta}{c_\theta+\varepsilon}.
\]
It reaches one half precisely when
\[
(\kappa-1)|\sin(2\theta)|
=
2\varepsilon.
\]
When
\[
2\varepsilon<\kappa-1,
\]
the smallest positive half-saturation angle is
\[
\theta_{1/2}
=
\frac12
\arcsin
\left(
\frac{2\varepsilon}{\kappa-1}
\right).
\]

For every fixed nonzero
\[
0<|\theta|<\frac{\pi}{2},
\]
taking
\[
\varepsilon\downarrow0
\]
first makes every nonzero rotated entry normalize to magnitude one. The resulting stale-coordinate update has singular values \(2\) and \(0\). By contrast, taking
\[
\theta\to0
\]
first removes the off-diagonal coordinate and then taking
\[
\varepsilon\downarrow0
\]
gives the identity. Hence the small-angle and small-\(\varepsilon\) limits do not commute.

This is an exact stationary-gradient mechanism by which eigenbasis staleness can destroy the singular-value balance that SOAP is intended to obtain from spectral structure.

## Assumptions and scope

The calculation uses Algorithm 3 of the defining SOAP paper: the gradient is rotated into the current preconditioner basis, first and second moments are maintained, the Adam-like elementwise normalization is performed there, and the update is rotated back.

The gradient matrix is held constant while the preconditioner basis is frozen. This isolates basis staleness from landscape drift.

The result concerns the stationary limit of the moment recurrences. Bias correction and initial moment states do not change that limit for
\[
\beta_1,\beta_2\in[0,1).
\]

The denominator convention is
\[
\sqrt{V}+\varepsilon,
\]
as in the source algorithm.

The matrix \(G_\kappa\) is normalized so that its smaller eigenvalue is one. Rescaling the gradient rescales the effective dimensionless size of \(\varepsilon\).

No claim is made that singular-value collapse of one update is by itself sufficient for global optimization divergence.

## Proof

Fix orthogonal matrices
\[
Q_L,Q_R
\]
through a stationary interval and a constant gradient matrix \(G\). Then
\[
G'
=
Q_L^\top GQ_R
\]
is constant.

SOAP's first-moment recurrence converges to \(G\), hence its rotated first moment converges to \(G'\). Its second-moment recurrence in the frozen coordinates converges entrywise to
\[
G'\odot G'.
\]
Consequently the stationary normalized coordinate is
\[
\frac{G'_{ij}}{|G'_{ij}|+\varepsilon}
=
F_\varepsilon(G'_{ij}),
\]
where
\[
F_\varepsilon(z)
=
\frac{z}{|z|+\varepsilon}.
\]
The limiting update is therefore
\[
Q_L
F_\varepsilon(G')
Q_R^\top,
\]
with \(F_\varepsilon\) applied entrywise.

For the \(45^\circ\)-rotated family, use the frozen identity basis. Then the diagonal magnitude is
\[
d=\frac{\kappa+1}{2}
\]
and the off-diagonal magnitude is
\[
c=\frac{\kappa-1}{2}.
\]
Thus
\[
p=\frac{d}{d+\varepsilon},
\qquad
r=\frac{c}{c+\varepsilon}.
\]
The symmetric matrix
\[
\begin{bmatrix}
p&r\\
r&p
\end{bmatrix}
\]
has eigenvalues, and therefore singular values,
\[
p+r
\qquad\text{and}\qquad
p-r.
\]
Direct subtraction gives
\[
p-r
=
\frac{
\varepsilon(d-c)
}{
(d+\varepsilon)(c+\varepsilon)
}
=
\frac{
4\varepsilon
}{
(\kappa+1+2\varepsilon)
(\kappa-1+2\varepsilon)
},
\]
because
\[
d-c=1.
\]
Likewise,
\[
\frac{p+r}{p-r}
=
\frac{
2dc+\varepsilon(d+c)
}{
\varepsilon(d-c)
}
=
\kappa+\frac{\kappa^2-1}{2\varepsilon}.
\]

In the exact eigenbasis the gradient is
\[
\operatorname{diag}(\kappa,1).
\]
Applying \(F_\varepsilon\) entrywise yields
\[
\operatorname{diag}
\left(
\frac{\kappa}{\kappa+\varepsilon},
\frac1{1+\varepsilon}
\right).
\]
Orthogonal rotation back does not change singular values, proving the fresh-basis formula.

For a general angular basis error \(\theta\),
\[
Q_\theta
\operatorname{diag}(\kappa,1)
Q_\theta^\top
\]
has off-diagonal magnitude
\[
c_\theta
=
\frac{\kappa-1}{2}
|\sin(2\theta)|.
\]
Applying \(F_\varepsilon\) gives the stated exact off-diagonal response. Setting it equal to one half gives
\[
c_\theta=\varepsilon,
\]
which is equivalent to the half-saturation equation.

Finally, at every fixed nonzero angle all four entries of the rotated positive-definite matrix are nonzero. Sending \(\varepsilon\) to zero therefore maps the two diagonal entries to \(1\) and the two equal off-diagonal entries to the same sign. That matrix has singular values \(2\) and \(0\). At zero angle, the off-diagonal entries are exactly zero for every positive \(\varepsilon\), so the opposite order of limits gives the identity.

## Verification

The accompanying `verify.py` reconstructs the stationary SOAP map from its elementwise Adam denominator and checks the closed forms against direct singular-value computations over randomized values of \(\kappa\), \(\varepsilon\), and basis angle.

It separately verifies the exact \(45^\circ\) condition-number law, the fresh-basis law, the half-saturation angle, and the noncommuting-limit behavior.

The finite checks are transcription guards. The stationary limit and exact singular-value identities are proved algebraically above.

## Relationship to prior work

Vyas and coauthors introduced SOAP by running Adam in the eigenbasis of Shampoo's Kronecker preconditioner. Their algorithm updates the second moment every step in the current eigenbasis but refreshes the eigenbasis only at a specified preconditioning frequency. The paper reports that less frequent eigendecomposition degrades performance and explicitly treats the coordinate basis as slowly changing.

Khona and coauthors later identified a large-scale SOAP instability caused by a lag between the preconditioner and current gradient statistics. Their experiments show gradient oscillations, loss spikes, and in a larger model divergence under stale statistics; per-step eigenbasis updates using the current gradient are part of their stabilization recipe. They also emphasize the numerical role of SOAP's \(\varepsilon\).

The inspected works establish the importance of basis freshness empirically and algorithmically, but they do not state the stationary \(2\times2\) singular-value collapse derived here, the exact condition number
\[
\kappa+\frac{\kappa^2-1}{2\varepsilon},
\]
or the half-saturation angle
\[
\frac12\arcsin\left(\frac{2\varepsilon}{\kappa-1}\right).
\]

The finding therefore supplies a precise spectral mechanism consistent with the later stale-preconditioner observations without claiming to explain all causes of large-model instability.

## Limitations

A constant gradient is an isolation device; real training gradients change with the parameters and data.

The \(45^\circ\) family is a canonical exact stress test, not a claim that practical eigenbasis errors are always that large.

The singular-value collapse concerns the matrix-shaped update itself. It does not prove loss increase, instability, or divergence for a nonlinear training problem.

For fixed positive \(\varepsilon\), sufficiently tiny basis error is regularized. The singular behavior appears when off-diagonal rotated-gradient magnitude is comparable to or larger than \(\varepsilon\).

## References

1. Nikhil Vyas, Depen Morwani, Rosie Zhao, Mujin Kwun, Itai Shapira, David Brandfonbrener, Lucas Janson, and Sham Kakade, “SOAP: Improving and Stabilizing Shampoo using Adam,” arXiv:2409.11321v1, 2024.
2. Mikail Khona, Aditya Vavre, Boxiang Wang, Deyu Fu, Hao Wu, Mike Chrzanowski, Bryan Catanzaro, Dheevatsa Mudigere, Jeff Pool, Michael Lightstone, Mohammad Shoeybi, Mostofa Patwary, Nima Tajbakhsh, and Tijmen Blankevoort, “SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales,” arXiv:2607.20548v1, 2026.
