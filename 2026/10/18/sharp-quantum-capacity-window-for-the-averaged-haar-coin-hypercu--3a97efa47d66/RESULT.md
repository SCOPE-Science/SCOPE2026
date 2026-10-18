# Sharp quantum-capacity window for the averaged Haar-coin hypercube walk

## Finding

For each integer \(d\geq1\), identify the vertices of the \(d\)-dimensional hypercube with \(d\) qubits, and let \(X_j\) flip the \(j\)-th vertex bit. The one-step *averaged vertex channel* of the independently Haar-resampled coin walk is
\[
\mathcal M_d(\rho)=\frac1d\sum_{j=1}^d X_j\rho X_j.
\]
For every integer \(t\geq0\), put \(\mathcal N_{d,t}=\mathcal M_d^t\) and let \(P_{d,t}\) be the probability law of the position of the ordinary coordinate-flip walk on \(\mathbb F_2^d\) after \(t\) independent uniform coordinate choices, started at zero. Let \(Q\) be the *unassisted quantum capacity in qubits per independent use* of the \(t\)-step channel. Then
\[
\boxed{Q(\mathcal N_{d,t})=d-H_2(P_{d,t})},
\]
where \(H_2\) is base-two Shannon entropy. If \(\pi_{d,t}\) denotes the uniform probability measure on the parity class of vectors of Hamming weight congruent to \(t\) modulo two, this is equivalently
\[
\boxed{Q(\mathcal N_{d,t})-1=
\frac{D(P_{d,t}\Vert\pi_{d,t})}{\ln 2}},
\]
where \(D\) uses natural logarithms. Thus \(Q\geq1\) at *every* iteration. At every positive iteration it equals one for \(d=1,2\), and strictly exceeds one for finite iterations when \(d\geq3\); for every fixed \(d\), it converges to one as \(t\to\infty\).

The main new asymptotic assertion is a sharp entropy/capacity profile. For every fixed \(c\in\mathbb R\), at
\[
t_d(c)=\left\lfloor\frac d4\ln d+cd\right\rfloor
\]
(which is nonnegative for all sufficiently large \(d\)),
\[
\boxed{\lim_{d\to\infty}
\left[Q(\mathcal N_{d,t_d(c)})-1\right]
=\frac{e^{-4c}}{2\ln2}.}
\]
Consequently, for any fixed target excess capacity \(\delta>0\), the first integer time \(T_d(\delta)\) such that \(Q(\mathcal N_{d,t})\leq1+\delta\) obeys
\[
\boxed{T_d(\delta)=\frac d4\ln d
-\frac d4\ln(2\delta\ln2)+o(d).}
\]
This quantifies the precise \(O(d)\) transition window about \(\frac d4\ln d\), above the protected one-qubit capacity floor.

## Assumptions and scope

The channel is the coin-averaged **vertex-only** channel; the coin is freshly and independently Haar randomized at each step and then discarded. The calculation concerns the averaged completely positive trace-preserving map, not an individual realized sequence of coins or the retained coin-and-vertex system. The vertices have Hilbert-space dimension \(2^d\), and the capacity unit is qubits per independent use of the already composed channel \(\mathcal N_{d,t}\), not qubits per elementary walk step. The Fourier/Hadamard transform converts the commuting coordinate flips into commuting phase flips. Entropies measured in bits carry subscript \(2\); un-subscripted \(\ln\) denotes natural logarithm. The time parameter \(t\) is integer; the scaling \(d\to\infty\) keeps \(c\) fixed.

## Proof

**1. Error law and degradability.** Conjugating by the tensor Hadamard \(H^{\otimes d}\) converts each \(X_j\) into \(Z_j\), so
\[
\mathcal N_{d,t}(\rho)=\sum_{x\in\mathbb F_2^d}
P_{d,t}(x) Z^x\rho Z^x,
\qquad Z^x=\bigotimes_{j=1}^d Z_j^{x_j},
\]
up to conjugation by known Hadamards, which does not change capacity. Its Stinespring map can be taken as
\[
V|\psi\rangle=\sum_x\sqrt{P_{d,t}(x)}\,
Z^x|\psi\rangle\otimes|x\rangle.
\]
The complementary channel depends only on the diagonal of its input in the computational basis: it is the measure-and-prepare map
\[
\mathcal N_{d,t}^c(\rho)=
\sum_{z\in\mathbb F_2^d}\langle z|\rho|z\rangle
|\phi_z\rangle\langle\phi_z|,
\quad
|\phi_z\rangle=\sum_x\sqrt{P_{d,t}(x)}(-1)^{x\cdot z}|x\rangle.
\]
Since \(\mathcal N_{d,t}\) preserves computational-basis diagonals, the complement is recovered from its output by the same measure-and-prepare operation; hence it is **degradable**. The established single-letter capacity theorem for degradable channels gives \(Q=\max_\rho[S(\mathcal N(\rho))-S(\mathcal N^c(\rho))]\). Coherent information is concave on degradable channels. Conjugation of the input by any Pauli operator preserves it (the channel and its complement change by output unitaries), so averaging over the Pauli group shows that \(I/2^d\) is a maximizer. At that input, the output entropy is \(d\). The environment's Gram matrix is diagonal, because \(2^{-d}\operatorname{tr}((Z^x)^\dagger Z^y)=\mathbf1_{x=y}\), so its nonzero spectrum is \(P_{d,t}\). Thus \(Q=d-H_2(P_{d,t})\). This uses established quantum-capacity principles, not a new general dephasing-channel formula.

**2. The protected qubit and parity.** Every elementary flip changes Hamming parity; hence \(P_{d,t}\) is supported on exactly one parity class. In particular, \(H_2(P_{d,t})\leq d-1\) and \(Q\geq1\). More concretely, in the Fourier basis the two-dimensional code spanned by the antipodal basis vectors \(|0\cdots0\rangle\) and \(|1\cdots1\rangle\) undergoes a known logical phase \(Z_{\rm L}^{t}\) under *every* Kraus operator, so one logical qubit is recoverable exactly. For \(d=1\) the channel is unitary, and for \(d=2\) the one-step error law is uniform on its parity class and remains so. If \(d\geq3\), the nontrivial Fourier coefficient \((1-2/d)^t\) is nonzero at every finite \(t\), so \(P_{d,t}\ne\pi_{d,t}\), giving strictly positive divergence. For fixed \(d\), all Fourier coefficients indexed by nonempty proper subsets decay in magnitude, so \(P_{d,t}-\pi_{d,t}\to0\) and \(Q\to1\). Finally \(H_2(P_{d,t})=d-1-D(P_{d,t}\Vert\pi_{d,t})/\ln 2\), proving the divergence identity.

**3. Fourier likelihood ratio at the critical time.** Let \(\chi_A(x)=(-1)^{\sum_{j\in A}x_j}\). The Fourier transform of the walk is exactly
\[
\mathbb E_{P_{d,t}}\chi_A=(1-2|A|/d)^t.
\]
For \(t\geq1\), on the parity class with its uniform law \(\pi_{d,t}\), the likelihood \(L_{d,t}=P_{d,t}/\pi_{d,t}\) therefore has the orthogonal expansion
\[
L_{d,t}=\sum_{0\leq k<d/2}
(1-2k/d)^t\,E_{d,k},
\quad
E_{d,k}(x)=\sum_{|A|=k}\chi_A(x).
\]
The equality follows from pairing each character indexed by \(A\) with its complement, using parity and the identity \((1-2(d-k)/d)^t=(-1)^t(1-2k/d)^t\); the possible middle term vanishes. For \(k,\ell<d/2\), the \(E_{d,k}\) are mutually orthogonal in \(L^2(\pi_{d,t})\) and \(\|E_{d,k}\|_2^2=\binom dk\).

Set \(t=t_d(c)\), \(\sigma=e^{-2c}\), and \(Z_d=d^{-1/2}\sum_j(-1)^{x_j}\) under \(\pi_{d,t}\). The parity constraint fixes the last sign after \(d-1\) independent signs; thus \(Z_d\) converges in law to a standard Gaussian \(Z\). The generating-function identity
\[
\sum_{k=0}^d E_{d,k}(x)(u/\sqrt d)^k
=\prod_{j=1}^d(1+u(-1)^{x_j}/\sqrt d)
\]
and the logarithmic expansion for fixed \(u\) show, at every fixed \(k\), that
\[
d^{-k/2}E_{d,k}\ \Longrightarrow\ H_k(Z)/k!,
\]
where \(H_k\) are probabilists' Hermite polynomials. For fixed \(k\), \(d^{k/2}(1-2k/d)^{t_d(c)}\to\sigma^k\). The tail is uniformly negligible in \(L^2(\pi_{d,t})\) since
\[
\sum_{K<k<d/2}\binom dk(1-2k/d)^{2t_d(c)}
\leq\sum_{k>K}\frac{(d e^{-4t_d(c)/d})^k}{k!},
\]
and the parameter of the exponential series tends to \(\sigma^2\). First truncating at fixed \(K\) and then letting \(K\to\infty\) gives
\[
L_{d,t_d(c)}\ \Longrightarrow\
\sum_{k\geq0}\sigma^k H_k(Z)/k!
=\exp(\sigma Z-\sigma^2/2).
\]
The same tail bound gives \(\sup_d\mathbb E_{\pi_{d,t_d(c)}}L_{d,t_d(c)}^2<\infty\) for all sufficiently large \(d\), which makes \(L\ln L\) uniformly integrable. Therefore
\[
\begin{aligned}
\lim_d D(P_{d,t_d(c)}\Vert\pi_{d,t_d(c)})
&=\mathbb E[e^{\sigma Z-\sigma^2/2}(\sigma Z-\sigma^2/2)]\\
&=\sigma^2/2=e^{-4c}/2.
\end{aligned}
\]
Dividing by \(\ln2\) proves the capacity-window formula.

**4. Inverting the profile.** Composition with one more channel cannot increase unassisted capacity, so \(Q(\mathcal N_{d,t})\) is nonincreasing in \(t\). The limiting excess-capacity profile \(f(c)=e^{-4c}/(2\ln2)\) is continuous, strictly decreasing, with range \((0,\infty)\). For every \(\delta>0\), comparison of the first crossing time with the times \(t_d(c)\) immediately on either side of the unique root \(f(c)=\delta\) yields the asserted \(T_d(\delta)\) asymptotic.

## Verification

The accompanying standalone `verify.py` independently evolves Hamming-weight probabilities by a birth–death recursion, enumerates exact integer coordinate-flip word counts for small registers, checks every Boolean character eigenvalue in those small cases, reconstructs Choi matrices from Kraus operators, and compares finite-dimensional capacities with the predicted Gaussian-window coefficient. The packaged verification requires Python 3, NumPy and SciPy; run `python verify.py` beside `requirements.txt`. These checks are finite corroboration. The continuum limit, quantum-capacity optimization, and all-dimension claims are established in the proof above, not by numerical extrapolation.

## Relationship to prior work

Quillen (2026), originally public July 6, derives the one-step Haar-averaged vertex channel and its hypercube Fourier eigenvalues (Eqs. 58 and 64), and recognizes persistent coherence between antipodal Fourier states. Those operator identities and the existence of conserved coherence are prior results, not claimed as new. Devetak and Shor (2005) establish the single-letter capacity principle for generalized dephasing channels, while Pirandola et al. (2017) determine general dephasing-channel communication benchmarks; the expression \(d-H_2(P)\) is an application of established information theory. The new assessed assertion is the precise entropy/capacity critical profile and its operational first-crossing law **for this periodic coordinate-flip channel**, not a generic capacity formula.

Diaconis, Graham and Morrison (1990) prove a transition-window total-variation profile for a closely related *lazy* hypercube walk, using saddle-point asymptotics. Total-variation convergence alone does not determine a relative-entropy limit: rare likelihood-ratio spikes can have negligible variation mass but nonvanishing entropy contribution. The present proof explicitly supplies the needed \(L^2\) control and treats the parity-periodic nonlazy channel. The full 1990 manuscript was not accessible during comparison, so its stronger intermediate estimates might already imply this entropy constant after additional argument; this is a genuine residual publication-priority risk. Voit (1996) likewise compares discrete-time and continuous-time hypercube distributions in total variation. No priority or independent certification is claimed.

## Limitations

The theorem is specific to the averaged, independently rerandomized hypercube vertex channel, not a single random coin realization, arbitrary graph, a non-Haar coin distribution, or the retained coin subsystem. The channel capacity is an asymptotic coding quantity across independent uses of the *entire* \(t\)-step map. The \(O(d)\) profile is proved only for fixed \(c\), not uniformly over arbitrary sequences of scaled times. A known one-qubit encoding is exhibited, but no finite-block optimal encoder is constructed for the generally nonintegral excess capacity. General degradable-channel formulas and earlier classical mixing analyses are not new, and comparison with inaccessible original material leaves residual originality uncertainty.

## References

1. A. C. Quillen, *Quantum random walks on d-regular graphs with Haar-random coin operators*, arXiv:2607.04584 (first public July 6, 2026); Phys. Rev. A 114, 042410 (2026), doi:10.1103/rmmp-xdqy. Relevant: Eqs. 58, 64 and Sec. IV B.
2. I. Devetak and P. W. Shor, *The capacity of a quantum channel for simultaneous transmission of classical and quantum information*, Commun. Math. Phys. 256, 287–303 (2005), arXiv:quant-ph/0311131. Relevant: Appendix B, Eq. 18.
3. J. Yard, I. Devetak and P. Hayden, *Capacity Theorems for Quantum Multiple Access Channels*, IEEE Trans. Inf. Theory 54, 3091–3113 (2008), arXiv:quant-ph/0501045; coherent-information concavity for degradable channels.
4. S. Pirandola, R. Laurenza, C. Ottaviani and L. Banchi, *Fundamental limits of repeaterless quantum communications*, Nat. Commun. 8, 15043 (2017), doi:10.1038/ncomms15043. Relevant: generalized dephasing-channel bounds, Eqs. 40–41.
5. P. Diaconis, R. L. Graham and J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Struct. Alg. 1, 51–72 (1990), doi:10.1002/rsa.3240010105. Closely related lazy-walk total-variation crossover.
6. M. Voit, *Asymptotic distributions for the Ehrenfest urn and related random walks*, J. Appl. Prob. 33, 340–356 (1996), doi:10.2307/3215058. Discrete/continuous walk variation comparison.
