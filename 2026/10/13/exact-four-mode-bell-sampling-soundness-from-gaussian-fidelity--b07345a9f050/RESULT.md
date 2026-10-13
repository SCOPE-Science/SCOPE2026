# Exact four-mode Bell-sampling soundness from Gaussian fidelity
## Finding
For every normalized positive-parity pure state \(\psi\) of four complex fermionic modes, define its fermionic Gaussian fidelity by
\[
F_{\mathrm G}(\psi)=\max_{g\in\mathcal G_4^+}|\langle g,\psi\rangle|^2,
\]
and let \(r_4(\psi)\) be the rejection probability of the two-copy Bell-sampling Gaussianity test whose accepting subspace is \(\ker\Lambda_4\), where
\[
\Lambda_4=\sum_{a=1}^{8}c_a\otimes c_a.
\]
Then the rejection probability is exactly
\[
\boxed{r_4(\psi)=\frac12F_{\mathrm G}(\psi)\bigl(1-F_{\mathrm G}(\psi)\bigr).}
\]

Writing the Gaussian trace distance as
\[
d_{\mathrm G}(\psi)=\sqrt{1-F_{\mathrm G}(\psi)},
\]
the four-mode positive-parity normal form gives \(F_{\mathrm G}(\psi)\in[1/2,1]\), hence \(d_{\mathrm G}(\psi)\in[0,1/\sqrt2]\). Therefore, for every \(0<\varepsilon\le1/\sqrt2\),
\[
\min_{d_{\mathrm G}(\psi)\ge\varepsilon}r_4(\psi)
=\frac12\varepsilon^2(1-\varepsilon^2).
\]
If the Bell test is repeated independently for \(R\) rounds and the protocol accepts iff every round accepts, the exact worst-case false-acceptance probability on the promise class \(d_{\mathrm G}(\psi)\ge\varepsilon\) is
\[
\left(1-\frac12\varepsilon^2(1-\varepsilon^2)\right)^R.
\]
Thus, for \(0<\delta<1\), the minimum number of Bell-test rounds that guarantees false-acceptance probability at most \(\delta\) is
\[
R_{\min}(\varepsilon,\delta)
=\left\lceil
\frac{\ln\delta}{\ln\left(1-\frac12\varepsilon^2(1-\varepsilon^2)\right)}
\right\rceil.
\]
Each round consumes two copies. For small \(\varepsilon\), the sharp round count is asymptotic to \(2\varepsilon^{-2}\ln(1/\delta)\).

## Assumptions and scope
The statement is restricted to normalized pure states in the positive-parity subspace of four complex fermionic modes. The Bell test is the standard two-copy test obtained by simultaneously measuring the commuting observables associated with the Majorana bridge operator and accepting exactly the zero-eigenvalue sector of \(\Lambda_4\). The Gaussian fidelity is maximized over positive-parity pure fermionic Gaussian states.

No assertion is made here for mixed states, for more than four modes, or for tolerant testing between two nonzero distance thresholds. For \(\varepsilon>1/\sqrt2\), the negative promise class is empty in the four-mode positive-parity setting.

## Proof
Dias and Koenig show that every normalized positive-parity pure four-mode state is Gaussian-unitarily equivalent to a two-term canonical state
\[
|\psi_f\rangle=\sqrt f\,|0000\rangle+\sqrt{1-f}\,|1111\rangle,
\qquad \frac12\le f\le1,
\]
with \(f=F_{\mathrm G}(\psi)\). The Bell test and the Gaussian fidelity are invariant under positive-parity Gaussian unitaries, so it suffices to evaluate the rejection probability on \(|\psi_f\rangle\).

Expand two copies:
\[
|\psi_f\rangle^{\otimes2}
=f|0,0\rangle
+\sqrt{f(1-f)}\bigl(|0,F\rangle+|F,0\rangle\bigr)
+(1-f)|F,F\rangle,
\]
where \(|0\rangle=|0000\rangle\) and \(|F\rangle=|1111\rangle\). The first and last terms are tensor squares of Gaussian states, so they lie in \(\ker\Lambda_4\). They also lie in total-occupation sectors different from the cross term. Hence only
\[
|e\rangle=|0,F\rangle+|F,0\rangle
\]
can contribute to rejection.

In the invariant sector generated from \(|0,F\rangle\), identify a basis vector with the subset \(S\subseteq\{1,2,3,4\}\) of modes occupying the first copy. In this basis, direct fermionic sign bookkeeping gives
\[
\Lambda_4=2\sum_{j=1}^{4}(-1)^{j-1}X_j.
\]
A diagonal sign gauge removes the factors \((-1)^{j-1}\); because the product of these four signs is \(+1\), the two endpoint vectors corresponding to \(S=\varnothing\) and \(S=\{1,2,3,4\}\) acquire the same gauge phase. Thus the needed kernel projection is the zero-eigenspace projection of the ordinary four-dimensional hypercube adjacency operator \(2\sum_jX_j\).

Its Walsh characters indexed by \(T\subseteq\{1,2,3,4\}\) have eigenvalue \(2(4-2|T|)\). The zero eigenspace is therefore the span of the six normalized characters with \(|T|=2\). For each such character, the overlap with the endpoint sum \(|e\rangle\) equals \(1/2\), because both endpoints have character value \(+1\). Therefore
\[
\|P_{\ker\Lambda_4}e\|^2=6\left(\frac12\right)^2=\frac32,
\qquad
\|e\|^2=2,
\]
and hence
\[
\|(I-P_{\ker\Lambda_4})e\|^2=\frac12.
\]
Multiplying by the squared cross-term coefficient gives
\[
r_4(\psi_f)=f(1-f)\cdot\frac12.
\]
Substituting \(f=F_{\mathrm G}(\psi)\) proves the exact identity.

Now put \(x=d_{\mathrm G}(\psi)^2=1-F_{\mathrm G}(\psi)\). Since \(x\in[0,1/2]\),
\[
r_4=\frac12x(1-x).
\]
This function is increasing on \([0,1/2]\), so the minimum subject to \(x\ge\varepsilon^2\) is attained at \(x=\varepsilon^2\), yielding the sharp one-round floor. The canonical state with \(f=1-\varepsilon^2\) attains equality. Independence of repeated rounds then gives the exact false-acceptance probability and the displayed ceiling formula for \(R_{\min}\).

## Verification
The standalone script `artifacts/verify.py` checks the nontrivial finite-dimensional kernel calculation exactly over rational arithmetic. It constructs the six zero-eigenvalue Walsh characters of the four-cube, verifies that the endpoint sum has squared kernel projection \(3/2\), and hence squared rejecting projection \(1/2\). It also verifies the resulting rejection formula at several rational fidelities and checks the monotonicity identity used for the sharp distance threshold.

These finite checks corroborate the analytic proof; they are not used as a substitute for the all-state argument, whose essential global input is the four-mode Gaussian normal form.

## Relationship to prior work
West and Larocca prove a mode-independent Bell-sampling Gaussianity tester for pure fermionic states and establish the general lower bound \(r_n(\psi)\ge \varepsilon^2/8\) for states at Gaussian trace distance at least \(\varepsilon\). Their argument is intentionally uniform in the mode number and does not state the exact four-mode rejection law above.

Dias and Koenig provide the four-mode Gaussian-fidelity normal form that reduces every positive-parity pure four-mode state to \(\sqrt f|0000\rangle+\sqrt{1-f}|1111\rangle\) with \(f=F_{\mathrm G}\). Their work studies simulation and Gaussian fidelity, not the Bell-test rejection probability.

Tarabunga analyzes the full bridge-operator spectrum and gives Bell-sampling Gaussianity tests with polynomial sample complexity. The inspected article text and indexed searches do not state an exact four-mode relation between the zero-sector rejection probability and Gaussian fidelity. Lyu and Bu use a different three-copy convolution-based Gaussianity test, while Haug, Turkeshi, and Sierant develop covariance-based witnesses and testers with mode-dependent bounds.

The present result is the four-mode synthesis of the Gaussian-fidelity normal form with the Bell-test kernel geometry. It converts the general soundness bound into an exact, attained finite-mode curve.

## Limitations
The equality is proved only for positive-parity pure states of exactly four complex modes. It does not imply an exact formula in higher mode number, where the component orthogonal to the Gaussian tangent space has many occupation sectors and the bridge-kernel weight need not be determined by the single scalar \(F_{\mathrm G}\).

The repeated-round formula assumes independent copies and the all-rounds-accept decision rule. It does not claim optimal finite-sample constants among arbitrary collective tests, despite the asymptotic optimality results known for the general Gaussianity-testing problem.

## References
1. M. West and M. Larocca, *Fermionic Gaussianity can be tested with mode-independent sample-complexity*, arXiv:2610.02050v1 (2026).
2. B. Dias and R. Koenig, *Classical simulation of non-Gaussian fermionic circuits*, Quantum 8, 1350 (2024); arXiv:2307.12912.
3. P. S. Tarabunga, *Fermionic non-Gaussianity via Bell sampling: monotones and efficient quantum algorithms*, PRX Quantum 7, 033065 (2026); arXiv:2606.05066.
4. X. Lyu and K. Bu, *Fermionic Gaussian Testing and Non-Gaussian Measures via Convolution*, arXiv:2409.08180 (2024).
5. T. Haug, X. Turkeshi, and P. Sierant, *Practical Tests and Witnesses of Fermionic non-Gaussianity*, arXiv:2605.26218 (2026).
