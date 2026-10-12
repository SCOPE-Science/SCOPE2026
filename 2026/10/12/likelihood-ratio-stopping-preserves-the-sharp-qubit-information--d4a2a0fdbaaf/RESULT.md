# Likelihood-ratio stopping preserves the sharp qubit information–disturbance frontier
## Finding
Fix \(0<p<1/2\), put \(q=1-p\), and consider the nondestructive qubit measurement with Kraus operators \(V_+=\operatorname{diag}(\sqrt q,\sqrt p)\) and \(V_-=\operatorname{diag}(\sqrt p,\sqrt q)\), the sharpness family used by Janssens. For any integer \(m\ge1\), repeat this same measurement and stop at the first time the outcome score \(S_n=N_+(n)-N_-(n)\) reaches \(+m\) or \(-m\), declaring the sign reached. After forgetting the full stopped record but retaining its declared sign, the resulting two-outcome instrument is exactly the same sharp family with renormalized error parameter \[p_m=\frac{p^m}{p^m+q^m},\qquad \frac{p_m}{1-p_m}=\left(\frac pq\right)^m.\] Equivalently it has effective Kraus operators \(W_+=\operatorname{diag}(\sqrt{1-p_m},\sqrt{p_m})\) and \(W_-=\operatorname{diag}(\sqrt{p_m},\sqrt{1-p_m})\). Hence its measurement infidelity is exactly \(p_m\), its residual coherence multiplier is \(2\sqrt{p_m(1-p_m)}\), and its maximal disturbance is \(1/2-\sqrt{p_m(1-p_m)}\); therefore the adaptive stopped measurement again attains both sharp Janssens information–disturbance/decoherence bounds for every \(m\). The mean number of elementary measurements is \[\mathbb E\tau_m=\frac{m}{q-p}\,\frac{q^m-p^m}{q^m+p^m}.\] Thus this extremal nondestructive family is closed under symmetric likelihood-ratio stopping, with log-odds multiplied exactly by the stopping threshold.

The closure is exact, not asymptotic. In particular, lowering the effective infidelity from \(p\) to \(p_m\) by sequential likelihood-ratio stopping does not move the final two-outcome instrument into the interior of the source's sharp information–disturbance region: after coarse-graining the stopped record, the instrument lies on the same boundary curve.

## Assumptions and scope
Let the measured system be a qubit with computational basis \(\{|+\rangle,|-\rangle\}\), and let \(0<p<1/2\), \(q=1-p\). One elementary nondestructive measurement has Kraus operators
\[
V_+=\operatorname{{diag}}(\sqrt q,\sqrt p),\qquad
V_-=\operatorname{{diag}}(\sqrt p,\sqrt q).
\]
These are precisely the two diagonal operators used in the source to attain its sharp bounds. The elementary outcomes are encoded as \(+1\) and \(-1\). Starting from \(S_0=0\), define \(S_n\) as their cumulative sum and
\[
\tau_m=\inf\{n\ge1:|S_n|=m\},\qquad m\in\mathbb N.
\]
The final classical outcome is \(\operatorname{{sgn}}S_{\tau_m}\). The full path is otherwise discarded. Because the score is a finite-state absorbing random walk between \(-m\) and \(+m\), \(\tau_m<\infty\) almost surely.

The claim concerns this ideal, symmetric two-outcome nondestructive instrument. It does not assert that arbitrary experimental QND readouts, asymmetric detector models, destructive errors, or arbitrary sequential quantum tests reduce to this family.

## Proof
For an input eigenstate \(|+\rangle\), each elementary score increment is \(+1\) with probability \(q\) and \(-1\) with probability \(p\). Put \(r=p/q\). The standard two-boundary difference equation for the probability of hitting \(-m\) before \(+m\) gives
\[
\delta_m=\frac{r^m}{1+r^m}=\frac{p^m}{p^m+q^m}.
\]
By symmetry the same error probability holds for input \(|-\rangle\), so the stopped binary measurement has measurement infidelity \(p_m=\delta_m\).

Now consider a stopped outcome record \(\omega=(\omega_1,\ldots,\omega_n)\). Since the elementary Kraus operators commute and are diagonal, its product Kraus operator depends on the counts \(N_+\) and \(N_-\). If the record terminates at \(+m\), then \(N_+-N_-=m\), and
\[
K_\omega=(pq)^{N_-/2}\operatorname{{diag}}(q^{m/2},p^{m/2}).
\]
Thus every Kraus operator of every path ending at \(+m\) is a nonnegative scalar multiple of the same diagonal operator. Consequently the whole completely positive map for the declared outcome \(+\) has Kraus rank one. Its diagonal effect probabilities are the two hitting probabilities \(1-p_m\) and \(p_m\), so its positive Kraus representative is exactly
\[
W_+=\operatorname{{diag}}(\sqrt{1-p_m},\sqrt{p_m}).
\]
The same argument at the other boundary gives
\[
W_-=\operatorname{{diag}}(\sqrt{p_m},\sqrt{1-p_m}).
\]
This proves exact closure of the instrument family and immediately yields the odds law
\[
\frac{p_m}{1-p_m}=\left(\frac p{1-p}\right)^m.
\]

Discarding the final classical outcome gives the dephasing channel
\[
\rho\longmapsto
\begin{pmatrix}
\rho_{++} & 2\sqrt{p_m(1-p_m)}\,\rho_{+-}\\
2\sqrt{p_m(1-p_m)}\,\rho_{-+} & \rho_{--}
\end{pmatrix}.
\]
Hence the maximum surviving coherence in the source's normalization is \(\sqrt{p_m(1-p_m)}\), attained on an equatorial pure state, and the maximal trace-distance disturbance is
\[
\Delta_m=\frac12-\sqrt{p_m(1-p_m)}.
\]
These are equalities in the source's sharp decoherence and measurement-disturbance bounds at infidelity \(p_m\).

Finally, under input \(|+\rangle\), the stopped score satisfies \(\mathbb E S_{\tau_m}=m(1-2p_m)\). Since the increment mean is \(q-p\), the bounded-interval stopping equation (equivalently, the elementary gambler's-ruin recurrence for the mean duration) gives
\[
\mathbb E\tau_m=\frac{m(1-2p_m)}{q-p}
=\frac{m}{q-p}\frac{q^m-p^m}{q^m+p^m}.
\]
The same value holds for input \(|-\rangle\).

## Verification
The proof is analytic. The accompanying `verify.py` independently solves the finite gambler's-ruin linear systems over exact rational arithmetic for several rational values of \(p\) and thresholds \(m\), rather than inserting the closed forms. It verifies the hitting-error formula, the mean stopping-time formula, and—when \(\sqrt{p(1-p)}\) is rational—the stopped-record coherence recurrence and its equality with \(2\sqrt{p_m(1-p_m)}\). Running `python3 verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Janssens proves sharp state-independent measurement-disturbance and decoherence inequalities and gives the elementary diagonal qubit instrument above as an explicit one-shot equality family. The inspected source discusses nondestructive measurements and their repeatability, but does not derive the likelihood-ratio stopping closure or the odds-exponentiation law.

Hume, Rosenband, and Wineland experimentally implement repeated QND readout and explicitly use Bayesian products of per-cycle likelihoods, stopping once a likelihood-ratio threshold is exceeded. Their full arXiv text establishes the practical relevance of adaptive likelihood stopping and reports its efficiency advantage over a fixed number of cycles. It does not formulate the ideal diagonal Kraus model above or identify exact preservation of a sharp information-disturbance frontier.

Later sequential-quantum-hypothesis-testing literature develops stopping-time methods for monitored quantum systems in broader dynamical settings. That broader program does not by itself imply the exact rank-one coarse-graining and parameter renormalization proved here for this particular extremal nondestructive instrument.

## Limitations
The equality uses the symmetry and commuting diagonal form of the elementary instrument, and the stopping boundaries are symmetric integer score boundaries. Detector asymmetry, outcome-dependent back-action outside this diagonal model, state transitions during readout, or unequal likelihood increments generally destroy the simple \(p_m\) formula. No claim is made about optimal expected stopping time among all physically allowed quantum instruments; the result identifies an exact closure and saturation property of this specific sharp family.

A literature search cannot prove uniqueness of the statement. The main residual originality risk is that the same closure law may have appeared under sequential weak-measurement, Bayesian QND, or likelihood-ratio terminology not surfaced by the targeted searches.

## References
1. B. Janssens, “Unifying Decoherence and the Heisenberg Principle,” arXiv:quant-ph/0606093, first public 10 June 2006; *Letters in Mathematical Physics* 107 (2017), 1557–1579, DOI: 10.1007/s11005-017-0953-z. The publication lists primary MSC \(81P40\).
2. D. B. Hume, T. Rosenband, and D. J. Wineland, “High-Fidelity, Adaptive Qubit Measurements through Repetitive Information Transfer,” arXiv:0705.1870, first public 14 May 2007; *Physical Review Letters* 99 (2007), 120502, DOI: 10.1103/PhysRevLett.99.120502.
3. G. Gasbarri, M. Bilkis, E. Roda-Salichs, and J. Calsamiglia, “Sequential hypothesis testing for continuously-monitored quantum systems,” *Quantum* 8 (2024), 1289, arXiv:2307.14954, DOI: 10.22331/q-2024-03-20-1289.
