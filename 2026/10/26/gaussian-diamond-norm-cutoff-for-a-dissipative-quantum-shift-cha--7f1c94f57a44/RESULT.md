# Gaussian diamond-norm cutoff for a dissipative quantum shift chain

## Finding

Let \(N\geq1\), \(0<g<1\), and \(a=1-g\). The \(N\)-qubit channel introduced in [1] is
\[
\mathcal T_N=\operatorname{Ad}_{R_N}\circ\bigl(a\operatorname{Id}+g\mathcal E_N\bigr),\qquad
\mathcal E_N(X)=\frac{I_2}{2}\otimes\operatorname{Tr}_{N}X,
\]
where \(R_N=r^{\otimes N}\), \(r=\exp(-i\pi\sigma_x/4)\), and \(\operatorname{Tr}_{N}\) traces out the last qubit. Write \(\mathcal D_N(X)=\operatorname{Tr}(X)I_{2^N}/2^N\) and
\[
d_N(t)=\tfrac12\bigl\|\mathcal T_N^{\,t}-\mathcal D_N\bigr\|_{\diamond}
\]
for integer \(t\geq0\). The diamond norm includes optimization over arbitrarily entangled ancillary inputs.

**Theorem (sharp operational cutoff).** For every integer \(1\leq L\leq N\), every \(t\geq0\), and \(K_t\sim\operatorname{Binomial}(t,g)\),
\[
\boxed{\Pr(K_t\leq N-L)-2^{-L}\ \leq\ d_N(t)\ \leq\ \Pr(K_t\leq N-1).}
\]
Consequently, for each fixed real \(s\), with
\[
t_N(s)=\left\lfloor\frac{N+s\sqrt{N(1-g)}}{g}\right\rfloor,
\]
\[
\boxed{\lim_{N\to\infty}d_N\bigl(t_N(s)\bigr)=\mathsf G(-s),}
\]
where \(\mathsf G\) is the standard normal cumulative distribution function. In particular, for each fixed \(0<\varepsilon<1\), the first integer \(t\) with \(d_N(t)\leq\varepsilon\) satisfies
\[
\boxed{t_{\mathrm{mix},N}(\varepsilon)=\frac Ng-\frac{\mathsf G^{-1}(\varepsilon)}{g}\sqrt{N(1-g)}+o(\sqrt N).}
\]
Thus the operational mixing cutoff is centered at \(N/g\) with a sharp \(\sqrt{N(1-g)}/g\) window, despite the channel's \(N\)-independent set of nonstationary multiplier moduli. At \(g=1\), exact depolarization occurs after \(N\) cycles; at \(g=0\), the channel does not converge to depolarization.

## Assumptions and scope

The statement concerns the discrete full-cycle channel \(\mathcal T_N\) above, with independent application of the same mixture on successive cycles, maximally mixed inserted spins, a homogeneous global rotation, and any initial \(N\)-qubit state (including arbitrary entanglement with a reference). No locality, product-state, or separability restriction is imposed on the diamond-norm upper bound. The probability law is the ordinary binomial law, not a postselected distribution. The asymptotic profile assumes \(g\) fixed independently of \(N\) in \((0,1)\); no claim is made for joint limits in which \(g\) approaches either endpoint with \(N\).

## Proof

**1. Exact channel-power representation.** For \(0\leq k\leq N\), direct composition of partial traces gives
\[
\mathcal E_N^k(X)=\left(\frac{I_2}{2}\right)^{\!\otimes k}\otimes\operatorname{Tr}_{N-k+1,\ldots,N}X,
\]
where the right-hand factor is understood to be the scalar trace at \(k=N\). Hence \(\mathcal E_N^k=\mathcal D_N\) for every \(k\geq N\). Since \(r(I_2/2)r^\dagger=I_2/2\) and the same \(r\) acts on every site, \(\mathcal E_N\) commutes with \(\operatorname{Ad}_{R_N}\). The binomial theorem therefore gives, for every integer \(t\geq0\),
\[
\mathcal T_N^{\,t}=\operatorname{Ad}_{R_N^t}\circ
\sum_{k=0}^{t}{t\choose k}a^{t-k}g^k\mathcal E_N^k
=\operatorname{Ad}_{R_N^t}\circ\mathbb E[\mathcal E_N^{K_t}].
\]
Because \(\mathcal D_N\) is rotation invariant, composing by \(\operatorname{Ad}_{R_N^t}\) does not alter its diamond distance to the displayed mixture.

**2. Uniform upper bound, including ancillas.** In the difference \(\mathbb E[\mathcal E_N^{K_t}]-\mathcal D_N\), every term with \(K_t\geq N\) vanishes identically. Any two quantum channels have diamond-norm distance at most \(2\). By convexity and the triangle inequality,
\[
d_N(t)\leq\sum_{k=0}^{N-1}\Pr(K_t=k)=\Pr(K_t\leq N-1).
\]
This is a completely bounded estimate valid against every ancilla.

**3. Matching lower bound without any ancilla.** Use \(\rho_0=(|0\rangle\langle0|)^{\otimes N}\) and undo the known final rotation \(R_N^t\) at readout. Measure the projector \(P_L=I_{2^{N-L}}\otimes(|0\rangle\langle0|)^{\otimes L}\). Whenever \(K_t\leq N-L\), the rightmost \(L\) qubits retain their original \(|0\rangle\) values, so the probability of \(P_L\) is one. The other branches contribute nonnegatively, and \(\operatorname{Tr}[P_L\mathcal D_N(\rho_0)]=2^{-L}\). The trace-distance variational principle yields
\[
d_N(t)\geq\Pr(K_t\leq N-L)-2^{-L}.
\]
Combining with Step 2 proves the finite-size sandwich.

**4. Sharp Gaussian limit.** For fixed \(s\in\mathbb R\), the integer \(t_N(s)\) satisfies
\[
\mathbb E K_{t_N(s)}=N+s\sqrt{N(1-g)}+O(1),\quad
\operatorname{Var}(K_{t_N(s)})=N(1-g)+O(\sqrt N).
\]
Choose \(L_N=\max(1,\lfloor N^{1/4}\rfloor)\). Then \(L_N\to\infty\) and \(L_N=o(\sqrt N)\), while \(2^{-L_N}\to0\). The binomial central limit theorem implies both \(\Pr(K_{t_N(s)}\leq N-L_N)\) and \(\Pr(K_{t_N(s)}\leq N-1)\) converge to \(\mathsf G(-s)\). The finite-size sandwich forces the stated diamond-norm profile.

**5. Mixing-time inversion and endpoints.** The function \(t\mapsto d_N(t)\) is nonincreasing: \(\mathcal T_N\mathcal D_N=\mathcal D_N\), and postcomposition by a channel contracts the diamond norm. Sandwiching a fixed tolerance \(\varepsilon\in(0,1)\) between profile parameters on either side of \(-\mathsf G^{-1}(\varepsilon)\) gives the mixing-time expansion. If \(g=1\), the power equals a rotation followed by \(\mathcal E_N^t\), which is \(\mathcal D_N\) from \(t=N\) onward and is not \(\mathcal D_N\) before then; if \(g=0\), the powers are unitary rotations and cannot approach \(\mathcal D_N\).

## Verification

The standalone file `verify_cutoff.py` checks finite matrix powers against the binomial mixture, the commutation of the shift with the homogeneous rotation, saturation of the shift after \(N\) updates, and both finite-size probability bounds for computational-basis inputs. It also numerically compares binomial tails with the normal limit. Execute `python verify_cutoff.py` with NumPy and SciPy installed. A successful run reports 2732 finite assertions. These checks corroborate the identities but cannot establish the infinite-size result; Steps 1–5 provide that proof.

## Relationship to prior work

Xie et al. [1] defined the exact channel, analyzed its nonnormal Floquet eigenoperators and residual atlas, and gave a binomial propagation formula for local spin observables (their Eq. S43). These are foundational inputs, not new claims here. Their main text and supplemental Section S2 do not state a worst-case quantum-channel diamond-norm mixing profile or the sharp mixing-time coefficient. The present result is an operational global distinguishability statement across all inputs and ancillas, rather than a local-operator residual estimate.

Kastoryano, Reeb, and Wolf [2] developed quantum cutoff theory and bounds for commuting Liouvillians and tensor-power evolutions. Their theorems do not imply the stated Gaussian profile for this nonnormal, non-tensor-power shift channel. Levin and Tankala [3] studied different classical shift-register Markov chains (with reversible bit-update moves and an XOR-feedback register permutation). They provide relevant cutoff context, but their dynamics and conclusions are not this channel or a diamond-norm profile. The probabilistic proof shares classical coupling and binomial-limit tools; the application to this entire quantum channel and sharp diamond-norm profile is the evaluated contribution.

## Limitations

The result is specific to homogeneous maximally mixed reinjection, independent Bernoulli shift decisions, and a rotation commuting with that reinjection. It does not address the paper's chiral XY model, arbitrary coherent errors, nonunital boundary inputs, entanglement-breaking times, or reservoir realizations that correlate successive shift decisions. Its novelty assessment is not an independent priority certification; a more general existing quantum cutoff theorem might subsume the specialization.

## References

[1] Y. Xie, H. Shi, Z. Ma, W. Chu, and X.-G. Gong, *Asymptotic Pseudospectra in Dissipative Floquet Quantum Systems: Geometric Structures and Observable Dynamics*, arXiv:2609.37523 (first public version 2026-09-29). https://arxiv.org/abs/2609.37523

[2] M. J. Kastoryano, D. Reeb, and M. M. Wolf, *A Cutoff Phenomenon for Quantum Markov Chains*, arXiv:1111.2123 (2011). https://arxiv.org/abs/1111.2123

[3] D. A. Levin and C. Tankala, *Fast mixing of a randomized shift-register Markov chain*, arXiv:2109.05387 (2021). https://arxiv.org/abs/2109.05387
