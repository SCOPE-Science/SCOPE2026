# Parity-resonant optimal bipartitions of a singly defective noisy GHZ state

## Finding
Let \(n\ge 2\). Apply independent qubit replacement-depolarizing channels with Bloch visibility \(s\in(0,1)\) to \(n-1\) qubits of the balanced \(n\)-qubit GHZ state, and one such channel with visibility \(d\in(0,1)\) to the remaining, distinguished qubit. Among **all** nontrivial bipartitions, the largest ordinary entanglement negativity is exactly
\[
\mathcal N_{\max}(n;s,d)=\frac{P}{2}\left[e^{(n-1)g(s)+g(d)}-2\cosh\!\left(\frac{\delta_n(s,d)}2\right)\right]_+,
\]
where \([z]_+=\max\{z,0\}\) and
\[
\begin{aligned}
 a(v)&=(1+v)/2,\qquad b(v)=(1-v)/2,\\
 L(v)&=\log\frac{1+v}{1-v},\qquad g(v)=\log\frac{2v}{\sqrt{1-v^2}},\\
 P&=[a(s)b(s)]^{(n-1)/2}\sqrt{a(d)b(d)},\\
 \delta_n(s,d)&=\min_{0\le k\le n-2}\left|(n-1-2k)L(s)-L(d)\right|.
\end{aligned}
\]
When the maximum is positive, **all and only** maximizing unoriented cuts consist of the defective qubit and \(k\) ordinary qubits on one side, with \(k\) attaining the above minimum. For each such \(k\) there are \(\binom{n-1}{k}\) maximizing cuts. The minimizer is unique except on the explicit switch surfaces
\[
 d=\tanh\!\bigl(j\operatorname{atanh}s\bigr),
 \qquad 1\le j\le n-2,\quad j\equiv n\pmod 2,
\]
where two adjacent values of \(k\) tie. This determines the complete finite-size parity staircase of optimizing cut imbalances. Using the established Dür--Cirac criterion for the canonical GHZ-diagonal family, the output is fully separable exactly when the displayed maximum vanishes.

There is an exact critical finite-size window. Set
\[
 s_*=\frac1{\sqrt5},\qquad \kappa=\frac{5\sqrt5}{4},\qquad L_*=\log\frac{1+s_*}{1-s_*}.
\]
Fix \(d\in(0,1)\), \(u\in\mathbb R\), and a parity class \(p\in\{0,1\}\) for \(n-1\) modulo \(2\). Let \(s_n=s_*+u/n\), and let \(\mathcal R_p=\{p,p+2,p+4,\ldots\}\), where \(p=0\) for odd \(n\) and \(p=1\) for even \(n\). Define
\[
 \delta_p(d)=\min_{r\in\mathcal R_p}|rL_*-L(d)|.
\]
Then, along \(n\to\infty\) with the stated parity,
\[
 \lim_{n\to\infty}\frac{2\mathcal N_{\max}(n;s_n,d)}{P_n}
 =\left[e^{\kappa u+g(d)}-2\cosh\!\left(\frac{\delta_p(d)}2\right)\right]_+.
\]
Consequently, writing
\[
 u_p(d)=\frac{\log\left(2\cosh(\delta_p(d)/2)\right)-g(d)}{\kappa},
\]
the states are fully separable for all sufficiently large \(n\) of the specified parity if \(u<u_p(d)\), and have an NPT bipartition for all sufficiently large such \(n\) if \(u>u_p(d)\). No finite-size conclusion at equality \(u=u_p(d)\) is claimed. For each parity the function \(u_p(d)\) has an infinite discrete family of genuine derivative kinks at
\[
 d_j=\tanh(j\operatorname{atanh}s_*),\qquad j\ge1,\quad j\equiv n\pmod2,
\]
which accumulate only at \(d=1\). For any fixed \(d\in(0,1)\), the limiting bulk visibility separating eventually fully separable and eventually NPT states is \(s_*\), independent of the defect; the defect changes the sharp order-\(1/n\) correction and its parity-resonant structure.

## Assumptions and scope
The input is \(|G_n\rangle=(|0\rangle^{\otimes n}+|1\rangle^{\otimes n})/\sqrt2\). Each channel is the completely positive trace-preserving map \(\mathcal D_v(X)=vX+(1-v)\operatorname{Tr}(X)I/2\) for \(0<v<1\). The distinguished qubit may be placed last without loss of generality. For any nonempty proper subset \(S\) of qubits, ordinary negativity means \(\mathcal N_S=(\|\rho^{T_S}\|_1-1)/2\). Unoriented cuts \(S|S^c\) are identified, and thus are uniquely oriented here by requiring the distinguished qubit to lie in \(S\). The output is \(\rho=\mathcal D_s^{\otimes(n-1)}\otimes\mathcal D_d(|G_n\rangle\langle G_n|)\). The critical statement fixes \(d,u,p\) and takes \(n\) through one parity. \(P_n\) denotes the specified value of \(P\) at \(s=s_n\).

## Proof
**Exact channel output.** Put \(a_i=a(v_i)\), \(b_i=b(v_i)\), where \(v_i=s\) except \(v_n=d\). The channel sends \(|0\rangle\langle0|\) to \(a_i|0\rangle\langle0|+b_i|1\rangle\langle1|\), sends \(|1\rangle\langle1|\) to its bit-flipped analogue, and multiplies \(|0\rangle\langle1|\) by \(v_i\). Hence the output is diagonal except for the conjugate corner entries \(\langle 0^n|\rho|1^n\rangle=\langle1^n|\rho|0^n\rangle=s^{n-1}d/2\). For a bit string \(z\), its diagonal probability is
\[
 \rho_{z,z}=\frac12\left(\prod_{i:z_i=0}a_i\prod_{i:z_i=1}b_i+\prod_{i:z_i=0}b_i\prod_{i:z_i=1}a_i\right)=\rho_{\bar z,\bar z}.
\]

**Every partial-transpose eigenvalue.** Orient a cut with the distinguished qubit in \(S\), and let \(k=|S|-1\) count ordinary qubits in \(S\), so \(0\le k\le n-2\). Taking partial transpose on \(S\) sends the two original off-diagonal corner entries to the unique block indexed by the bit string \(z\) whose ones form \(S\) and its complement \(\bar z\). Every other eigenvalue is a nonnegative diagonal probability. This block is
\[
 \begin{pmatrix}
 P\cosh((rL(s)-L(d))/2)&s^{n-1}d/2\\
 s^{n-1}d/2&P\cosh((rL(s)-L(d))/2)
 \end{pmatrix},\qquad r=n-1-2k,
\]
whose smaller eigenvalue is the common diagonal minus \(s^{n-1}d/2\). Because \(s^{n-1}d=P\exp((n-1)g(s)+g(d))\), the claimed exact negativity for that cut follows. In particular there is at most one negative eigenvalue; the formula includes the zero-negativity boundary without a strictness error.

**Global cut optimization and multiplicities.** For positive \(P\), the only cut-dependent quantity is \(\cosh(|rL(s)-L(d)|/2)\), strictly increasing in the displayed absolute discrepancy. Thus the maximizing positive-negativity cuts minimize the discrepancy over the finite parity-spaced set \(r\in\{n-1,n-3,\ldots,-(n-3)\}\). Since \(L(d)>0\), a negative \(r\) cannot outperform the corresponding available nonnegative \(r\) (zero when the parity is even, one when odd); hence the maximizer is the nearest permitted nonnegative parity-lattice point to \(L(d)/L(s)\), clipped at the finite upper endpoint. There is a tie exactly at a midpoint \(L(d)=jL(s)\) between adjacent permitted points \(j-1\) and \(j+1\), with \(1\le j\le n-2\) and \(j\equiv n\pmod2\). Solving for \(d\) gives the stated hyperbolic-tangent surfaces. Choosing \(k\) ordinary qubits gives \(\binom{n-1}{k}\) distinct unoriented cuts. If the maximum is zero, every cut has zero negativity and no uniqueness claim is made. The output lies in the canonical GHZ-diagonal family with paired diagonal probabilities and only one nontrivial coherence pair. Dür and Cirac's PPT-versus-full-separability theorem for precisely that family applies: all cut negativities vanish if and only if this state is fully separable.

**Critical scaling.** The function \(g\) satisfies \(g(s_*)=0\), and differentiation gives \(g'(s_*)=\kappa\). Therefore \((n-1)g(s_*+u/n)\to\kappa u\). Likewise \(L(s_*+u/n)\to L_*\). Because fixed \(d<1\) gives a finite value of \(L(d)\), all nearest permitted \(r\) remain bounded as \(n\to\infty\), so the finite lattice minimum converges to the minimum on \(\mathcal R_p\). Substituting in the exact finite formula and using continuity of the positive-part operation proves the normalized limit. Its inside bracket has a strictly positive or negative limit exactly for \(u>u_p(d)\) or \(u<u_p(d)\), yielding the eventual NPT or full-separability assertions. At equality only a zero leading term is established.

**Resonance kinks and bulk threshold.** The distance \(\delta_p(d)\) to the nonnegative even or positive odd lattice is piecewise linear as a function of \(L(d)\), with a corner at every odd or even positive midpoint \(jL_*\), respectively. There its one-sided derivatives with respect to \(d\) have opposite signs, whereas \(\sinh(\delta_p(d)/2)>0\), so \(\log(2\cosh(\delta_p(d)/2))\) has a nonzero derivative jump. Subtracting the smooth \(g(d)\) cannot remove this kink. The midpoint locations are exactly \(d_j\), tending to \(1\). Finally for any fixed \(d\in(0,1)\), if \(s<s_*\) then \((n-1)g(s)+g(d)\to-\infty\) and the exact bracket is eventually negative, while if \(s>s_*\) it tends to \(+\infty\) and the bounded nearest-lattice correction cannot offset it. Thus the limiting bulk threshold is \(s_*\).

## Verification
The accompanying `verify.py` independently constructs the full density matrix from the **single-qubit channel's action on four matrix units** and evaluates actual partial-transpose eigenvalues for all oriented cuts in twenty small systems, testing the analytic formula on 228 bipartitions. It also checks twelve critical-window sequences over both parities and four exact resonant double-optimum examples, including perturbations to either side. Run `python3 verify.py` with Python 3 and NumPy installed. A successful execution prints `VERIFY_OK channel_states=20 partial_transposes=228 critical_parities=2 critical_sequences=12 resonance_cases=4`. These finite calculations check normalization and signs but do not prove the all-dimensional statements; those follow from the preceding derivation and cited separability theorem.

## Relationship to prior work
Dür and Cirac (1999 preprint) establish the GHZ-diagonal partial-transpose and full-separability framework. Simon and Kempe (2001 preprint) compute the cut eigenvalues for **identical** local depolarizing channels, recover the bulk visibility \(1/\sqrt5\), and show the importance of balanced cuts in the homogeneous case. Aolita and collaborators (2008 preprints) likewise analyze homogeneous independent reservoirs and the ordering and decay of cut negativities. Han and Kye (2021), and Burduli, Moerland and Schupp (2026), treat broad GHZ-diagonal separability and PPT geometry. The present statement concerns a **different operation**, one exceptional local visibility, and derives the exact global maximizer, explicit defect-strength staircase, tie multiplicities, and parity-dependent finite-size threshold function. The general cited PPT criteria imply the positivity test once a cut is specified; they do not themselves give these cut-optimization and defect-resonance formulas. No priority claim beyond this specifically compared scope is made.

## Limitations
The channels are independent, isotropic and strictly inside the visibility interval \((0,1)\), and the input is the balanced GHZ state. The theorem is not a classification of arbitrary heterogeneous noise on every qubit, arbitrary input GHZ amplitudes, arbitrary measurement protocols, genuine multipartite entanglement, or distillation rates. An NPT cut proves entanglement but not genuine multipartite entanglement. The full-separability equivalence relies on the cited specialized GHZ-diagonal theorem rather than a newly proved general separability criterion. At the critical equality \(u=u_p(d)\), higher-order finite-size corrections are not resolved. At finite size, exactly resonant double optima need \(d=\tanh(j\operatorname{atanh}s)\); fixed \(d=d_j\) with \(s_n=s_*+u/n\) and nonzero \(u\) need not remain exactly degenerate. No independent literature-priority assessment has been performed.

## References
1. W. Dür and J. I. Cirac, *Classification of multi-qubit mixed states: separability and distillability properties*, arXiv:quant-ph/9911044v1, publicly posted 1999-11-10, https://arxiv.org/pdf/quant-ph/9911044.
2. C. Simon and J. Kempe, *Robustness of Multi-Party Entanglement*, arXiv:quant-ph/0109102v1, publicly posted 2001-09-20, https://arxiv.org/pdf/quant-ph/0109102.
3. L. Aolita et al., *Scaling laws for the decay of multiqubit entanglement*, arXiv:0801.1305v1, publicly posted 2008-01-08, https://arxiv.org/pdf/0801.1305.
4. L. Aolita et al., *Scalability of GHZ and random-state entanglement in the presence of decoherence*, arXiv:0812.4203v1, publicly posted 2008-12-22, https://arxiv.org/pdf/0812.4203.
5. K. H. Han and S.-H. Kye, *Polytope structures for Greenberger-Horne-Zeilinger diagonal states*, arXiv:2104.07871v1, publicly posted 2021-04-16, https://arxiv.org/pdf/2104.07871.
6. L. Burduli, J. Moerland and P. Schupp, *Multipartite GHZ diagonal states and their entanglement properties*, arXiv:2609.28351v1, publicly posted 2026-09-23, https://arxiv.org/html/2609.28351v1.
