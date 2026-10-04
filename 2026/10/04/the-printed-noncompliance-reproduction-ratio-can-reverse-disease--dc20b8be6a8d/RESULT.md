# The printed noncompliance reproduction ratio can reverse disease-free stability
## Finding
For the constant-control current model of Ngo, Parkinson, and Wang, write
\[
q=\mu^*-\mu.
\]
At a disease-free equilibrium \((s,0,0,s^*,0,0)\), linearization of the infected pair \((I,I^*)\) gives the next-generation matrices
\[
F=\beta\begin{pmatrix}
(1-\alpha)^2s&(1-\alpha)s\\
(1-\alpha)s^*&s^*
\end{pmatrix},
\qquad
V=\begin{pmatrix}
\gamma+\eta+\delta+q s^*&-\nu\\
-q s^*&\gamma+\nu+\delta
\end{pmatrix}.
\]
Thus the basic reproduction number for the current model is \(\mathcal R_{\rm true}=\rho(FV^{-1})\). If
\[
D=\gamma+\eta+\nu+\delta+q s^*,
\]
then direct inversion gives
\[
\mathcal R_{\rm true}
=
\frac{\beta\left[
(1-\alpha)^2\left(1+\frac{\alpha q s^*/(1-\alpha)-\eta}{D}\right)s
+\left(1-\frac{\alpha\nu}{D}\right)s^*
\right]}
{\gamma+\delta+\eta\nu/D}.
\]
The current paper's Eq. (2.6) has the same displayed expression except that the numerator contains \(\alpha\mu s^*/(1-\alpha)\) in place of \(\alpha q s^*/(1-\alpha)\). Consequently
\[
\mathcal R_{\rm true}-\mathcal R_{\rm print}
=
\frac{\beta\alpha(1-\alpha)ss^*(\mu^*-2\mu)}
{(\gamma+\delta)D+\eta\nu}.
\]
The mismatch is therefore structural, not merely notational, except on accidental parameter submanifolds such as \(\mu^*=2\mu\) or a boundary state with \(ss^*=0\).

An exact admissible parameter point reverses the threshold classification. Take
\[
b=\delta=\gamma=1,\quad \xi=0,\quad \mu^*=4,\quad \mu=1,\quad
\nu=\frac12,\quad \alpha=\frac12,\quad \eta=0,\quad \beta=\frac{16}{5}.
\]
Then \(q=3\), and the behavioral-endemic disease-free equilibrium from the paper's own formula is
\[
s=\frac{\nu+\delta}{q}=\frac12,
\qquad
s^*=\frac b\delta-s=\frac12.
\]
At this equilibrium the printed formula gives
\[
\mathcal R_{\rm print}=\frac{39}{40}<1,
\]
whereas the actual next-generation spectral radius is
\[
\mathcal R_{\rm true}=\frac{41}{40}>1.
\]
The infected Jacobian block is exactly
\[
F-V=
\begin{pmatrix}
-31/10&13/10\\
23/10&-9/10
\end{pmatrix},
\]
whose determinant is \(-1/5\). Hence one eigenvalue is positive, so the disease-free equilibrium is linearly unstable despite the printed threshold lying below one. Theorem 2.3(ii), if evaluated with Eq. (2.6) as printed, can therefore select the wrong stability side. The next-generation theorem itself is repaired simply by using \(\rho(FV^{-1})\), equivalently the corrected formula above.

## Assumptions and scope
The claim concerns the autonomous constant-control disease-free analysis of arXiv:2509.09075v3. All epidemiological rates used in the general formula are nonnegative with \(\beta,\gamma,\delta>0\), \(0\le\alpha<1\), and \(0\le\mu\le\mu^*\). The exact counterexample also satisfies the paper's physical condition for the behavioral-endemic disease-free equilibrium, because
\[
\frac b\delta\frac{q}{\nu+\delta}=2>1.
\]

The result does not challenge the optimal-control existence theorem, the numerical optimizer, or the disease-free theorem after replacing the printed reproduction number by the actual next-generation spectral radius. It also does not concern the older version of the preprint whose infection term used only one factor of \(1-\alpha\); that earlier model has a different \(F\) matrix.

## Proof
The current model has infected equations
\[
\begin{aligned}
I'&=\beta(1-\alpha)S\bigl((1-\alpha)I+I^*\bigr)
-(\gamma+\eta+\delta)I-qIN^*+\nu I^*,\\
(I^*)'&=\beta S^*\bigl((1-\alpha)I+I^*\bigr)
-\gamma I^*+qIN^*-(\nu+\delta)I^*.
\end{aligned}
\]
At a disease-free equilibrium, \(N^*=s^*\). Separating new infections from other infected-state transfers yields the displayed matrices \(F\) and \(V\). The matrix \(F\) is rank one:
\[
F=\beta
\begin{pmatrix}(1-\alpha)s\\s^*\end{pmatrix}
\begin{pmatrix}1-\alpha&1\end{pmatrix}.
\]
Therefore \(FV^{-1}\) has one zero eigenvalue and its nonzero eigenvalue equals its trace, or equivalently
\[
\mathcal R_{\rm true}
=\beta
\begin{pmatrix}1-\alpha&1\end{pmatrix}
V^{-1}
\begin{pmatrix}(1-\alpha)s\\s^*\end{pmatrix}.
\]
Since
\[
\det V=(\gamma+\delta)D+\eta\nu>0,
\]
direct inversion gives the corrected formula in the finding. Comparing it term-by-term with Eq. (2.6) leaves only the replacement \(\mu\mapsto q=\mu^*-\mu\) inside the \(\alpha\)-dependent transfer term, and subtraction gives the displayed exact difference.

For the rational counterexample, the paper's disease-free formula gives \((s,s^*)=(1/2,1/2)\). Substitution into its printed Eq. (2.6) gives \(39/40\). Direct construction of \(F\) and \(V\) gives
\[
F=\begin{pmatrix}2/5&4/5\\4/5&8/5\end{pmatrix},
\qquad
V=\begin{pmatrix}7/2&-1/2\\-3/2&5/2\end{pmatrix},
\]
and hence \(\rho(FV^{-1})=41/40\). The infected Jacobian is the displayed \(F-V\) with determinant \(-1/5\), so its two real eigenvalues have opposite signs. This proves linear instability independently of any threshold theorem.

## Verification
The bundled `verify.py` uses exact rational arithmetic. It reconstructs the disease-free point, the matrices \(F\) and \(V\), the rank-one next-generation matrix, the two reproduction-number values \(39/40\) and \(41/40\), and the infected Jacobian determinant \(-1/5\). It returns `VERIFY_OK` only if every identity holds.

The universal correction is algebraic and is proved above; the finite exact check is a witness that the sign error can cross the epidemiological threshold rather than merely perturb its numerical value.

## Relationship to prior work
The current version of Ngo--Parkinson--Wang explicitly defines noncompliance transmission through \(q=\mu^*-\mu\) in the state equations and gives the next-generation interpretation of its reproduction number. Its current infection term reduces both susceptibility and infectiousness of the compliant class, creating the squared factor \((1-\alpha)^2\) in the compliant-to-compliant entry of \(F\). The printed Eq. (2.6), however, retains \(\mu\) in one mixed transfer term.

The first public version of the same preprint used a different infection convention, with only one factor of \(1-\alpha\) in the compliant infection term, and its displayed next-generation formula is correspondingly different. The earlier Parkinson--Wang model treats the noncompliance transmission rate directly rather than as a baseline-minus-control quantity; its full next-generation derivation confirms that behavioral transfer enters through the actual transfer rate. These sources support the corrected construction but do not state the current-version threshold-reversal counterexample.

Exact-title, reproduction-number, correction, erratum, and next-generation searches found no public correction of the current Eq. (2.6), and the closest indexed summaries still reproduce the older-version formula rather than identify the current mismatch.

## Limitations
This result is version-specific to the current model equations in arXiv:2509.09075v3. It does not assert that every numerical trajectory or optimal control in the paper is qualitatively wrong. The threshold reversal is demonstrated at one exact admissible parameter point; the general difference formula identifies the full sign and magnitude of the mismatch but does not classify every downstream simulation.

The claim is also limited to local disease invasion at disease-free equilibria. It does not make statements about endemic equilibria, global basins under the corrected threshold, or time-varying-control Floquet thresholds.

## References
1. C. Ngo, C. Parkinson, and W. Wang, “Optimal Control of an SIR Model with Noncompliance as a Social Contagion,” arXiv:2509.09075v3, 2026; first public version arXiv:2509.09075v1, 2025.
2. C. Parkinson and W. Wang, “A Compartmental Model for Epidemiology with Human Behavior and Stochastic Effects,” arXiv:2507.01046v4; Mathematical Biosciences 392 (2026), 109588.
3. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” Mathematical Biosciences 180 (2002), 29--48.
