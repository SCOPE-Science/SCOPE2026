# A Hurwitz barrier to memory-induced instability in a distributed-order SEIRS model
## Finding
Consider a linearization with the same distributed-order Caputo operator in every coordinate,
\[
{}^C\mathcal D_t^{(\omega)}u=Ju,
\]
with characteristic symbol
\[
\Psi_\omega(s)=\int_{\alpha_1}^{\alpha_2}
\omega(\alpha)T_c^{\alpha-1}s^\alpha\,d\alpha,
\]
where \(0<\alpha_1\le\alpha_2\le1\), \(T_c>0\), and \(\omega\ge0\) is normalized.

If \(J\) is Hurwitz, then
\[
\det\!\left(\Psi_\omega(s)I-J\right)\ne0
\]
for every \(s\) with \(\operatorname{Re}s\ge0\). Thus all characteristic roots lie in the open left half-plane for every admissible memory density and every admissible support contained in \((0,1]\). In particular, changing only the common distributed-order memory cannot destabilize a Hurwitz equilibrium or generate a Hopf-type stability loss.

For the endemic equilibrium used in the baseline simulations of Ali (2026), the model parameters are
\[
r=0.02,\quad q=0.40,\quad p=0.05,\quad \epsilon=0.10,\quad
\sigma=0.20,\quad \gamma=0.10,\quad \mu=0.01,\quad \beta=0.35,
\]
with
\[
f(N)=0.005+1.5\times10^{-5}N,\qquad K=1000.
\]
Independent reconstruction gives
\[
(X^*,H^*,Y^*,Z^*)\approx
(362.377257655,84.479329039,131.439986279,324.659184500),
\]
consistent with the equilibrium reported in the source. The ordinary Jacobian at this point has characteristic polynomial
\[
P(z)=z^4+a_1z^3+a_2z^2+a_3z+a_4,
\]
with
\[
a_1\approx0.5786699091,\quad
a_2\approx0.08810770448,\quad
a_3\approx0.004035626673,\quad
a_4\approx0.00003990077566.
\]
The two nontrivial quartic Routh-Hurwitz margins are
\[
a_1a_2-a_3\approx0.04694965067>0
\]
and
\[
a_1a_2a_3-a_3^2-a_1^2a_4
\approx0.0001761101341>0.
\]
Together with \(a_i>0\), these inequalities certify that \(J\) is Hurwitz. Therefore the source's baseline endemic equilibrium is locally asymptotically stable for every common nonnegative distributed-order density supported in \((0,1]\), not only for the memory intervals and density shapes tested numerically.

## Assumptions and scope
The theorem uses the source's common scalar distributed-order operator: the same \(\Psi_\omega\) multiplies the identity matrix in the linearized resolvent. The memory density is nonnegative and normalized, its support lies in \((0,1]\), and the principal branch of \(s^\alpha\) is used. These are the assumptions under which the source formulates its characteristic symbol and numerical memory experiments.

The source itself notes that an extension with distinct memory densities for different compartments is natural. The present argument does not cover that extension because the characteristic matrix would no longer have the scalar form \(\Psi_\omega(s)I-J\).

The all-memory conclusion is also conditional on the fixed epidemiological parameter vector having a Hurwitz Jacobian. If transmission, immunity-loss, demographic, or other epidemiological parameters are changed, then \(J\) changes and a stability transition is not excluded by this result.

## Proof
Let \(s\ne0\) satisfy \(\operatorname{Re}s\ge0\), and write the principal argument as
\[
s=\rho e^{i\theta},\qquad -\frac{\pi}{2}\le\theta\le\frac{\pi}{2}.
\]
For every \(0<\alpha\le1\),
\[
s^\alpha=\rho^\alpha e^{i\alpha\theta},
\]
so
\[
\operatorname{Re}(s^\alpha)
=\rho^\alpha\cos(\alpha\theta)\ge0.
\]
Since \(T_c^{\alpha-1}>0\) and \(\omega(\alpha)\ge0\),
\[
\operatorname{Re}\Psi_\omega(s)
=
\int_{\alpha_1}^{\alpha_2}
\omega(\alpha)T_c^{\alpha-1}
\rho^\alpha\cos(\alpha\theta)\,d\alpha
\ge0.
\]
Thus \(\Psi_\omega\) maps the closed right half-plane into the closed right half-plane.

If
\[
\det(\Psi_\omega(s)I-J)=0,
\]
then the scalar \(\Psi_\omega(s)\) is an eigenvalue of \(J\). A Hurwitz matrix has every eigenvalue strictly in the open left half-plane, contradicting
\[
\operatorname{Re}\Psi_\omega(s)\ge0.
\]
At \(s=0\), one has \(\Psi_\omega(0)=0\); a Hurwitz matrix is nonsingular, so
\[
\det(-J)\ne0.
\]
Therefore no characteristic root lies in the closed right half-plane. The distributed-order root criterion used in the motivating paper then yields local asymptotic stability.

For the baseline SEIRS equilibrium, the equilibrium can be reconstructed without time integration. With
\[
N=X+H+Y+Z,\qquad f(N)=0.005+1.5\times10^{-5}N,
\]
the endemic equilibrium identities imply
\[
Y=\frac{(r-f(N))N}{\mu},
\]
\[
H=\frac{\gamma+\mu+f(N)}{\sigma}Y,
\]
and
\[
X=N\frac{(\sigma+f(N))(\gamma+\mu+f(N))}{\beta\sigma}.
\]
Setting
\[
Z=N-X-H-Y
\]
and imposing the \(Z\)-equilibrium equation reduces the baseline equilibrium to a single scalar equation in \(N\). Bisection on \(902<N<903\) gives the coordinates stated above.

Evaluating the exact Jacobian formula at that reconstructed equilibrium produces the displayed quartic. For a monic quartic
\[
z^4+a_1z^3+a_2z^2+a_3z+a_4,
\]
the Routh-Hurwitz criterion requires \(a_i>0\),
\[
a_1a_2>a_3,
\]
and
\[
a_1a_2a_3>a_3^2+a_1^2a_4.
\]
The displayed positive margins verify all conditions.

## Verification
The bundled script `verification/verify.py` reconstructs the baseline endemic equilibrium from a one-dimensional bisection, evaluates the analytic four-dimensional Jacobian, computes its characteristic coefficients from traces and a determinant, and checks the quartic Routh-Hurwitz inequalities. It also checks the four equilibrium residuals. The script uses only the Python standard library and prints `VERIFY_OK` when all checks pass.

The universal memory statement is analytic; no finite sampling of memory densities is used to prove it.

## Relationship to prior work
Ali (2026) derives the same scalar distributed-order characteristic structure
\[
\det(\Psi_\omega(s)I-J)=0
\]
and develops general conditions for purely imaginary characteristic roots. For its baseline endemic equilibrium, however, the paper reports only a numerical search over selected memory intervals and density shapes and concludes that no oscillatory transition was detected within the investigated parameter ranges.

Saberi Najafi, Refahi Sheikhani, and Ansari (2011) establish the general root-location criterion for linear distributed-order systems: asymptotic stability is equivalent to all roots of
\[
\det(B(s)I-A)=0
\]
lying in the open left half-plane. Their theorem supplies the general stability framework used here, but the inspected text does not state the positive-real half-plane lemma above, does not give the Hurwitz-implies-all-\((0,1]\)-memory corollary, and does not analyze the SEIRS Jacobian.

Rivero, Rogosin, Tenreiro Machado, and Trujillo (2013) review distributed-order fractional stability and cite the 2011 framework, but the inspected distributed-order section likewise does not provide this source-specific all-memory certification.

The new content is therefore not the general distributed-order characteristic equation. It is the exact positive-real obstruction together with a Routh-Hurwitz certification of the 2026 SEIRS baseline, which upgrades a finite numerical memory scan to a theorem covering every admissible common density and support in \((0,1]\).

## Limitations
The result does not say that distributed-order memory can never affect stability. If \(J\) has eigenvalues outside the open left half-plane, fractional or distributed-order memory may change stability relative to the classical model. The result only states that common memory of order at most one cannot destabilize an already Hurwitz equilibrium.

No global stability of the endemic equilibrium is claimed. The proof concerns local linearized stability through the source's distributed-order root criterion. It also does not cover compartment-specific memory operators or fractional orders exceeding one.

The numerical Routh-Hurwitz certificate is for the source's published baseline parameter vector. Other epidemiological parameter choices require a fresh Jacobian check.

## References
1. I. Ali, “Stability and Transient Dynamics of a Distributed-Order Fractional SEIRS Epidemic Model with Temporary Immunity,” Mathematics 14 (2026), 3186. DOI: 10.3390/math14173186.
2. H. Saberi Najafi, A. Refahi Sheikhani, A. Ansari, “Stability Analysis of Distributed Order Fractional Differential Equations,” Abstract and Applied Analysis 2011 (2011), 175323. DOI: 10.1155/2011/175323.
3. M. Rivero, S. V. Rogosin, J. A. Tenreiro Machado, J. J. Trujillo, “Stability of Fractional Order Systems,” Mathematical Problems in Engineering 2013 (2013), 356215. DOI: 10.1155/2013/356215.
