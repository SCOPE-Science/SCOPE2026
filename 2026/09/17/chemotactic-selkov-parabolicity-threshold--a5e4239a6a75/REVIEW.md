# Same-model review

## Finding reviewed

**Ultraviolet instability is loss of parabolicity in the chemotactic Selkov model.**

The claim is source-specific: for the Karmakar--Basu chemotactic Selkov PDE
(arXiv:2609.01159), the reciprocal-chemotaxis threshold
\[
D_1D_2-\frac{\xi_1\xi_2b^2}{a+b^2}=0
\]
is exactly the loss-of-normal-ellipticity boundary of the principal diffusion
matrix at the positive homogeneous equilibrium. On the negative-determinant
side, one linear dispersion branch grows like \(c|k|^2\), so the linearized
periodic Cauchy problem is not bounded \(H^s\to H^s\) at any positive time.

## Correctness review

**PASS.**

The source equations were checked directly from the full arXiv HTML. At the
positive equilibrium
\[
(\phi_*,\psi_*)=\left(b,\frac{b}{a+b^2}\right),
\]
linearizing the second-order terms gives
\[
\mathcal D_*=
\begin{pmatrix}
D_1 & \xi_1b\\
\xi_2b/(a+b^2) & D_2
\end{pmatrix}.
\]
Its determinant is exactly
\[
Q=D_1D_2-\frac{\xi_1\xi_2b^2}{a+b^2},
\]
the same coefficient multiplying \(k^4\) in the source dispersion
determinant and the same quantity whose vanishing appears in the denominator of
the selected-wave-number expression.

For \(Q<0\), the positive trace \(D_1+D_2\) and negative determinant force one
diffusion eigenvalue to be negative. The Fourier generator is
\(R-|k|^2\mathcal D_*\); therefore its corresponding eigenvalue is
\(-\nu_-|k|^2+O(1)\) with \(-\nu_->0\). Single-mode data then have amplification
\(e^{c|k|^2t+O(t)}\), which is unbounded uniformly in \(k\) in every Sobolev
norm. This proves the stated linear Hadamard ill-posedness.

The nonlinear principal matrix
\[
\mathcal D(\phi,\psi)=
\begin{pmatrix}D_1&\xi_1\phi\\ \xi_2\psi&D_2\end{pmatrix}
\]
has the same fixed positive trace and determinant
\(D_1D_2-\xi_1\xi_2\phi\psi\), giving the stated pointwise normal-ellipticity
region for positive states.

Adversarial checks:
- The argument does not require the reaction equilibrium to be ODE-stable; the
  high-frequency conclusion is controlled by the principal symbol.
- The claim at \(Q=0\) is only degeneracy, not Sobolev ill-posedness.
- For \(\xi_1\xi_2<0\), determinant positivity indeed holds for all positive
  states; even if the diffusion eigenvalues become complex, their real parts
  are positive because their sum is \(D_1+D_2>0\).
- The result does not confuse finite-wave-number Turing instability for \(Q>0\)
  with the \(Q<0\) ultraviolet branch.

## Originality review

**PASS, to the best of our knowledge.**

The principal source was inspected in full-text HTML, including its model
equations, Fourier stability matrix, dispersion determinant, selected-wave-number
formula, and discussion of the reciprocal strong-chemotaxis high-wave-number
instability. The source explicitly observes that sufficiently strong reciprocal
chemotaxis makes arbitrarily large wave numbers unstable, but it presents this
as a chemotaxis-induced instability/pattern-forming phenomenon and does not
identify the threshold as loss of normal ellipticity or state the resulting
Sobolev ill-posedness.

Searches included:
- exact title and arXiv identifier 2609.01159 with "parabolicity",
  "ellipticity", and "ill-posed";
- "Selkov chemotaxis" with "normal ellipticity", "cross-diffusion",
  "high-wavenumber", and "ill-posed";
- general cross-diffusion searches for normal ellipticity, determinant
  conditions, forward-backward parabolicity, and short-wave instability.

These searches found standard literature explaining that normal ellipticity is
a well-posedness condition for cross-diffusion systems, including work that
requires positivity of the diffusion-tensor determinant, but no prior
source-specific statement for the Karmakar--Basu model equating its reciprocal
threshold with the parabolicity boundary or deriving the \(H^s\) ill-posedness.

No inaccessible paper was identified as especially likely to contain this exact
source-specific result. The source preprint is very recent, so ordinary
indexing/citation lag remains a nonzero originality risk.

The generic normal-ellipticity criterion and backward-parabolic
high-frequency mechanism are standard and are not claimed as new.

## Value review

**PASS.**

The result changes the mathematical interpretation of one of the source
paper's headline regimes. The divergence of the preferred wave number is not
merely an extreme wavelength-selection effect: it occurs exactly as the
continuum PDE loses normal ellipticity, and beyond the threshold the linear
growth rate is unbounded at high wave number. This matters for continuum
well-posedness, interpretation of numerical patterns, and model design.

The nonlinear state-space criterion
\[
D_1D_2>\xi_1\xi_2\phi\psi
\]
also provides a reusable diagnostic for simulations and future analytical work
on the model.

## Limitations

The theorem does not classify generalized solutions in the forward-backward
regime, does not establish global nonlinear well-posedness in the normally
elliptic region, and does not settle the exact degenerate boundary \(Q=0\).
It does not invalidate finite-wave-number Turing results obtained while
\(Q>0\).

**Same-model review: passed. Cross-model review: not yet performed.**
