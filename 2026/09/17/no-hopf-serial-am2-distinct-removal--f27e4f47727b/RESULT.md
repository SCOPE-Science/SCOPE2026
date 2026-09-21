# No-Hopf theorem for the serial AM2 model with distinct removal rates

## Result

Consider the eight-dimensional serial AM2 system of Hmidhi and Fekih-Salem,
arXiv:2604.18903, with state ordered as
\[
(S_1^1,X_1^1),\ (S_2^1,X_2^1),\ (S_1^2,X_1^2),\ (S_2^2,X_2^2),
\]
positive dilution rates \(D_1,D_2\), stoichiometric coefficients \(k_i>0\),
and biomass removal factor \(\alpha\in(0,1)\). The growth functions need only be
\(C^1\) and nonnegative for the argument below; the paper's hypotheses (H1)--(H2)
are therefore more than sufficient.

**Theorem.** No equilibrium of this model can have a nonzero purely imaginary
eigenvalue pair. Consequently, the model admits no local Hopf bifurcation from
an equilibrium as any operating parameter is varied within the stated model
class.

Moreover, at every positive-biomass diagonal block of the second reactor,
positive determinant automatically implies negative trace. In particular, the
extra trace condition in Table 3 and Proposition 5 of arXiv:2604.18903 is
redundant. The trace-indeterminate coexistence equilibria singled out in Remark 1
cannot lose stability through Hopf bifurcation.

This resolves the Hopf part of the open oscillation question stated in the
source paper. It does **not** exclude periodic orbits created by a global
mechanism.

## Structural block decomposition

With the variable ordering above, the Jacobian is block lower triangular with
four \(2\times2\) diagonal blocks. The first-reactor acidogenic pair is
autonomous; the first-reactor methanogenic pair is driven by it; the
second-reactor acidogenic pair is driven by the first reactor; and the
second-reactor methanogenic pair is driven by the preceding pairs. Hence the
spectrum of the full Jacobian is exactly the union of the spectra of these four
diagonal blocks.

For either species in the first reactor, the relevant diagonal block at
substrate \(s\), biomass \(x\), growth rate \(\mu\), and stoichiometric
coefficient \(k\) is
\[
A_1=
\begin{pmatrix}
-D_1-k\mu'(s)x & -k\mu(s)\\
\mu'(s)x & \mu(s)-\alpha D_1
\end{pmatrix}.
\]

If \(x=0\), this block is triangular and has two real eigenvalues. If \(x>0\),
the equilibrium equation gives \(\mu(s)=\alpha D_1\), so
\[
\operatorname{tr}A_1=-D_1-k\mu'(s)x,\qquad
\det A_1=k\alpha D_1\,\mu'(s)x.
\]
Thus \(\det A_1>0\) forces \(\mu'(s)>0\), and then
\(\operatorname{tr}A_1<-D_1<0\). If the trace could vanish, the determinant
would instead be negative. Therefore a first-reactor diagonal block cannot
carry a purely imaginary pair.

## Second-reactor determinant--trace obstruction

For either species in the second reactor, let \(x_0\ge0\) be the corresponding
upstream biomass and let \(x\ge0\) be the local biomass. The diagonal block is
\[
A_2=
\begin{pmatrix}
-D_2-k\mu'(s)x & -k\mu(s)\\
\mu'(s)x & \mu(s)-\alpha D_2
\end{pmatrix}.
\]

Again \(x=0\) makes the block triangular with real eigenvalues. Suppose
\(x>0\). The second-reactor biomass balance is
\[
0=\alpha D_2(x_0-x)+\mu(s)x.
\]
Writing
\[
r=\frac{x_0}{x},\qquad
\delta=\alpha D_2r,\qquad
q=-k\mu'(s)x,
\]
the equilibrium relation gives
\[
\mu(s)=\alpha D_2(1-r),\qquad 0\le r\le1,
\]
and the block invariants reduce exactly to
\[
\boxed{\operatorname{tr}A_2=q-D_2-\delta},
\qquad
\boxed{\det A_2=D_2(\delta-\alpha q)}.
\]

Two consequences are immediate.

First, if \(\det A_2>0\), then
\[
q<\frac{\delta}{\alpha}=D_2r,
\]
and hence
\[
\operatorname{tr}A_2
< D_2r-D_2-\alpha D_2r
=-D_2\bigl(1-r+\alpha r\bigr)<0.
\]
For the source model \(0<\alpha<1\), this even yields the uniform estimate
\[
\operatorname{tr}A_2<-\alpha D_2.
\]

Second, if \(\operatorname{tr}A_2=0\), then \(q=D_2+\delta\), so
\[
\det A_2
=\alpha D_2^2\bigl((1-\alpha)r-1\bigr)
\le -\alpha^2D_2^2<0.
\]
Thus a zero trace is separated from the Hopf condition by a strictly negative
determinant.

Because the full Jacobian is block lower triangular, no coupling terms outside
these diagonal blocks can create an additional eigenvalue pair. This proves the
theorem.

## Consequence for the open stability cases in arXiv:2604.18903

For the methanogenic block \(J_3^3\) used in the source paper's analysis of
\(\mathcal E_{01}^{11}\) and \(\mathcal E_{11}^{11}\), the paper obtains
\[
\det J_3^3
=D_2X_2^{2*}\left(g_2'(X_2^{2*})-f_2'(X_2^{2*})\right)
\]
and imposes both \(\det J_3^3>0\) and \(\operatorname{tr}J_3^3<0\) for local
exponential stability. Remark 1 then identifies a regime with positive
determinant but apparently undetermined trace and leaves stability and possible
oscillation open.

The determinant--trace obstruction above shows instead that
\[
\det J_3^3>0\quad\Longrightarrow\quad
\operatorname{tr}J_3^3<0.
\]
Therefore the stability criterion for these equilibria simplifies: once the
other diagonal blocks satisfy the source paper's stated stability conditions,
the methanogenic block is stable exactly when its determinant is positive.
Accordingly, in the multiple-root ordering of Proposition 5, the
determinant-positive odd-indexed roots are locally exponentially stable rather
than trace-indeterminate; the even-indexed roots remain unstable, and the final
root remains stable as already established in the source.

This also shows that the paper's proposed search for Hopf parameters in these
equilibria cannot succeed: at every trace-zero point of the relevant block the
determinant is strictly negative.

## Scope and limitations

The theorem is a **local equilibrium bifurcation obstruction**. It rules out
ordinary Hopf bifurcation from every equilibrium of the serial AM2 system (1)
under the stated model structure. It does not establish global convergence and
does not rule out periodic orbits generated by global bifurcations or other
nonlocal mechanisms.

The proof uses the feed-forward block-triangular architecture of this specific
AM2 cascade and the second-reactor biomass balance. It does not apply
automatically to chemostat models with feedback between trophic blocks,
flocculation, mutualism, predator--prey coupling, delay, or other mechanisms
that destroy this triangular structure. Such related chemostat models are known
to admit Hopf bifurcations, so the obstruction is structural rather than a
generic consequence of distinct removal rates.

No numerical continuation is required for the result.

## Relation to prior literature

The source preprint explicitly states that coexistence equilibria in the second
bioreactor may require an additional trace condition and that identifying Hopf
bifurcations and limit cycles remains open. The earlier equal-removal-rate
serial-AM2 analysis gives complete equilibrium stability in the reducible case,
but does not state the determinant--trace identity above for the distinct-rate
eight-dimensional model.

Literature searches for the exact preprint identifier and title, serial-AM2
Hopf/limit-cycle formulations, determinant/trace formulations, and related AM2
bifurcation work found no prior statement of this no-Hopf theorem or of the
redundancy of the trace condition. Nearby literature does contain genuine Hopf
bifurcations in structurally different chemostat models, including flocculation
models with distinct removal rates and three-tier anaerobic food-web models;
those results do not cover the feed-forward serial AM2 system considered here.

Originality is therefore asserted only **to the best of our knowledge**. The
block-triangular eigenvalue fact and \(2\times2\) trace/determinant criterion are
standard; the contribution is their source-specific combination with the
second-reactor equilibrium identity to close the open AM2 stability/Hopf case.

## References

1. T. Hmidhi and R. Fekih-Salem, *AM2 model with a series configuration of
   interconnected chemostats and distinct removal rates*, arXiv:2604.18903,
   2026. https://arxiv.org/abs/2604.18903
2. T. Hmidhi, R. Fekih-Salem and J. Harmand, *Analysis of Anaerobic Digestion
   Model With Two Serial Interconnected Chemostats*, Bulletin of Mathematical
   Biology 87, 95 (2025), DOI 10.1007/s11538-025-01475-5.
   https://doi.org/10.1007/s11538-025-01475-5
3. R. Fekih-Salem and T. Sari, *Properties of the Chemostat Model with
   Aggregated Biomass and Distinct Removal Rates*, SIAM Journal on Applied
   Dynamical Systems 18 (2019), 481--509, DOI 10.1137/18M1171801.
   https://doi.org/10.1137/18M1171801
4. S. Nouaoura, N. Abdellatif, R. Fekih-Salem and T. Sari, *Mathematical
   Analysis of a Three-Tiered Model of Anaerobic Digestion*, SIAM Journal on
   Applied Mathematics 81 (2021), DOI 10.1137/20M1353897.
   https://doi.org/10.1137/20M1353897
