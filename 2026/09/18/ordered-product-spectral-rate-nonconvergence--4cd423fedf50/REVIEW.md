# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The source defines
\[
h_L=L^{-1}\langle\log\rho(P_n^{(L)})\rangle
\]
and states both in the main text and Supplemental Eq. (S2) that a non-degenerate top Lyapunov exponent implies \(h_L\to\lambda_1\). The displayed counterexample satisfies the source's smooth-map setting: the map \(F:\mathbb R^4\to\mathbb R^4\) is polynomial and has an explicit period-four orbit.

Along that orbit the derivative is block diagonal. The fiber blocks telescope to
\[
P_n^{(L)}=Q^{n+L}D^LQ^{-n}.
\]
Orthogonal left/right factors preserve singular values, so the fiber singular-value exponents are exactly \(a>b\), while the base rotation contributes only zero exponents. Hence \(\lambda_1=a\) is simple and \(\lambda_2=b\).

For even \(L\), \(Q^L=\pm I\), giving spectral radius \(e^{aL}\). For odd \(L\), the characteristic polynomial of \(Q D^L\) is
\[
z^2+e^{(a+b)L},
\]
so its eigenvalues have modulus \(e^{(a+b)L/2}\). This proves the exact parity formula and nonconvergence. The base block has spectral radius one and therefore never dominates when \(a,b>0\).

The residue-class transversality argument was checked separately. For \(L=kp+r\), periodicity gives \(P_n^{(L)}=A_{n,r}M_n^k\). A simple dominant Floquet multiplier yields
\[
M_n^k=\mu_1^k\frac{v_nw_n^\top}{w_n^\top v_n}+o(|\mu_1|^k)
\]
at exponential scale. Multiplication by \(A_{n,r}\) produces a rank-one dominant term whose unique nonzero eigenvalue is \(\mu_1^kc_{n,r}\). Therefore \(c_{n,r}\ne0\) implies the normalized log spectral radius tends to \(p^{-1}\log|\mu_1|\). The counterexample has exact cancellation for odd residues.

The verification artifact was executed for \(a=2,b=1\), all four phases and \(L=1,\dots,12\). It reports zero floating-point discrepancy from the analytic spectral-rate and singular-rate identities.

## Adversarial checks

A possible escape is that the source intended its convergence statement only for the six numerical trajectories studied. That reading is inconsistent with Supplemental S1.1, which states without a trajectory-specific qualification that \(h_L\to\lambda_1\) for a non-degenerate top exponent, and with the main-text/end-matter explanation invoking Oseledets alignment as the reason both spectral-radius and singular-value rates converge. The source later says its measured \(h_{1024}\) agreement is only an observation for those sequences, but this does not repair the earlier general implication.

Another possible escape is to identify the product's leading eigenvector with its leading singular/covariant direction. The example separates them explicitly: the covariant top direction grows by \(e^{aL}\) but rotates by ninety degrees for odd \(L\), while the product's dominant eigenvalues then form a complex conjugate pair of modulus \(e^{(a+b)L/2}\). A Lyapunov gap therefore does not supply the missing endpoint pairing.

The construction is not merely an arbitrary matrix sequence. It is the exact Jacobian cocycle of a smooth polynomial map on \(\mathbb R^4\) along a genuine period-four orbit.

## Originality

PASS, to the best of our knowledge, with a narrow source-specific claim.

General failure of normalized spectral-radius convergence is established prior mathematics and is excluded from the novelty claim. Aoun and Sert (2021) give an ergodic stationary Markov counterexample. Martínez Ramos (2026) states explicitly that a limsup formula holds generally while a true limit may fail, and proves convergence only under additional strong-irreducibility and mixing hypotheses. These sources materially undercut any claim that the broad phenomenon is new.

The full HTML of arXiv:2609.18017v1 was inspected, including the definition of \(h_L\), the convergence statement, the Oseledets-gap explanation, the periodic-orbit identity \(h_{kp}=\lambda_1\), and the caveat that the measured \(h_{1024}\) agreement is empirical for the reported sequences. Searches using the exact title and arXiv identifier together with `spectral radius`, `Oseledets`, `ordered-product growth rate`, `correction`, and `counterexample` did not locate a public correction or comment addressing this source-specific claim.

The originality claim is therefore only: an explicit smooth deterministic period-four counterexample directly to the unrestricted convergence assertion of arXiv:2609.18017v1, plus the residue-class endpoint-transversality explanation and the resulting warning about frame dependence. Standard Oseledets theory, spectral-radius counterexamples, Floquet theory, and singular-value asymptotics are not claimed as new.

The source preprint is very recent, so an unindexed author revision or discussion is the main residual originality risk. No inaccessible paper emerged as a particularly plausible source of the same source-specific correction. The original Morris limsup theorem was not needed for the proof; its role was checked through the detailed discussion and theorem citation in Martínez Ramos (2026).

## Value

PASS.

The disputed statement is used to motivate \(h_L\) as an interpolation between one-step spectral growth and asymptotic Lyapunov growth and to interpret the Lyapunov gap as an alignment scale that is shorter than the measured separation length \(L^*\). The counterexample shows that this theoretical interpolation is not guaranteed even in the elementary setting of a smooth periodic orbit with a simple top exponent.

The correction is constructive rather than merely negative. It identifies an explicit non-cancellation condition that restores convergence residue class by residue class on periodic orbits and explains why return-time products are special. It also separates the coordinate/frame-sensitive spectral-radius diagnostic from the singular-value finite-time exponent that is controlled by multiplicative ergodic theory.

The source's finite-horizon numerical observations and control results are not declared false. Their reported \(h_L\) curves remain legitimate coordinate-specific diagnostics; what is removed is the claimed general asymptotic guarantee from a Lyapunov gap alone.

## Scope and limitations

The counterexample addresses the general convergence and alignment claims for \(h_L\). It does not recompute the source's Hénon or Ikeda data and does not show that their measured \(h_{1024}\) values are inaccurate. The periodic transversality statement is a sufficient mechanism and is not presented as a complete characterization for arbitrary aperiodic cocycles.
