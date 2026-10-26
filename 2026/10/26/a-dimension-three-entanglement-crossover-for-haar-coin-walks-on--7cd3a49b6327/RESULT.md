# A dimension-three entanglement crossover for Haar-coin walks on hypercubes

## Finding

For every integer \(d\ge2\), consider the \(d\)-dimensional hypercube \(Q_d\) and its coined quantum walk driven by an independent Haar-distributed \(U(d)\) coin at each time. Start at one vertex with an arbitrary deterministic unit coin vector. Write \(\rho_C(t)\) for the reduced coin density matrix after \(t\) unitary steps, for a **single realized sequence** of coins, and \(P_t=\operatorname{Tr}(\rho_C(t)^2)\) for its purity. Then

\[
\boxed{\mathbb E P_1=\frac{2}{d+1},\qquad \mathbb E P_2=\frac{d+5}{(d+1)^2},\qquad \mathbb E(P_2-P_1)=\frac{3-d}{(d+1)^2}.}
\]

Thus the ensemble-mean *linear coin–position entanglement*, \(\mathbb E[1-P_t]\), **decreases** at the second step when \(d=2\), is **unchanged** when \(d=3\), and **increases** when \(d\ge4\). These identities hold for every deterministic initial pure coin state, not only coordinate or uniform coin states.

For comparison, the density operator obtained by averaging over the random coins has reduced coin state \(I_d/d\) after each positive step. The purity of that averaged coin state is \(1/d\), whereas

\[
\boxed{\mathbb E P_2-\frac1d=\frac{3d-1}{d(d+1)^2}>0.}
\]

This gives the exact nonlinear purity information lost by averaging the quantum channel before computing entanglement. In particular, the two-step mean purity approaches the minimal attainable purity \(1/d\) with excess of order \(d^{-2}\).

## Assumptions and scope

Let the vertex Hilbert space have orthonormal basis \(\{|x\rangle:x\in\{0,1\}^d\}\) and the coin space basis \(\{|a\rangle:1\le a\le d\}\). Write \(e_a\) for a bit string with a single unit bit in coordinate \(a\). The unitary conditional shift is

\[
S=\sum_{a=1}^d |a\rangle\langle a|\otimes X_a,\qquad X_a|x\rangle=|x\oplus e_a\rangle.
\]

Let \(U_1,U_2\) be independent Haar random matrices in \(U(d)\), both shared uniformly across vertices at their respective time steps. Starting from \(|c\rangle\otimes|0\rangle\) with \(\langle c|c\rangle=1\) and \(c\) deterministic, apply \(S(U_1\otimes I)\), then \(S(U_2\otimes I)\). No intermediate measurement, environmental decoherence, or separate random coins at different vertices are present. Expectations are over these two Haar matrices only. The claim is for every \(d\ge2\); the single-coin \(d=1\) case has no nontrivial coin–position entanglement and is excluded.

## Proof

**First step.** Haar invariance makes \(u:=U_1c\) a uniformly distributed unit vector in \(\mathbb C^d\). After the shift, the pure state is \(\sum_a u_a|a\rangle\otimes|e_a\rangle\). Because the vertices \(e_a\) are distinct, the reduced coin matrix is diagonal with entries \(|u_a|^2\). The complex-sphere moments satisfy

\[
\mathbb E|u_a|^4=\frac{2}{d(d+1)},\qquad
\mathbb E(|u_a|^2|u_b|^2)=\frac{1}{d(d+1)}\quad(a\ne b).
\]

Consequently \(\mathbb E P_1=d\,2/[d(d+1)]=2/(d+1)\).

**Second-step amplitudes.** Set \(V=U_2\). The component at coin value \(b\) and vertex \(x\) equals

\[
\psi_{b,x}=\sum_{a=1}^d V_{ba}u_a\,\mathbf1_{\{x=e_a\oplus e_b\}}.
\]

Write \(\rho=\rho_C(2)\). For each \(b\), its diagonal element is \(\rho_{bb}=\sum_a |V_{ba}|^2|u_a|^2\). Conditional on \(u\), Haar-row second moments yield

\[
\mathbb E_V[\rho_{bb}^2\mid u]
=\frac{1+\sum_a |u_a|^4}{d(d+1)}.
\]

Summing over \(b\) and averaging over \(u\) therefore gives

\[
\mathbb E\sum_b\rho_{bb}^2=\frac{d+3}{(d+1)^2}.
\]

For \(b\ne b'\), two distinct path pairs—and *only* two—lead to the same terminal vertex in the two coin sectors: both paths return to the starting vertex, or both end at \(e_b\oplus e_{b'}\). Thus

\[
\rho_{bb'}=
V_{bb}\overline{V_{b'b'}}u_b\overline{u_{b'}}
+V_{bb'}\overline{V_{b'b}}u_{b'}\overline{u_b}.
\]

Haar invariance under independent coordinate phases makes the expectation of the cross term in \(|\rho_{bb'}|^2\) vanish. The standard two-entry Haar moment for distinct row and column indices is

\[
\mathbb E_V\big(|V_{bb}|^2|V_{b'b'}|^2\big)
=\mathbb E_V\big(|V_{bb'}|^2|V_{b'b}|^2\big)
=\frac{1}{d^2-1}.
\]

Together with the cross-coordinate sphere moment, this gives

\[
\mathbb E|\rho_{bb'}|^2
=\frac{2}{d(d+1)(d^2-1)},
\qquad
\mathbb E\sum_{b\ne b'}|\rho_{bb'}|^2=\frac{2}{(d+1)^2}.
\]

Since \(P_2=\sum_{b,b'}|\rho_{bb'}|^2\), adding the diagonal and off-diagonal contributions proves \(\mathbb E P_2=(d+5)/(d+1)^2\). Subtraction proves the strict dimension-three crossover.

**Averaged state comparison.** At either positive time, the final independent Haar matrix completely depolarizes the coin before the conditional shift; tracing the position after the shift leaves the coin diagonal with mean weights \(1/d\). Hence \(\mathbb E\rho_C(t)=I_d/d\) for \(t=1,2\). Taking the nonlinear purity *after* this expectation would give \(1/d\), rather than the proven average purity. Simple subtraction proves the displayed positive excess.

## Verification

The standalone program `verify.py` independently implements the coined walk by indexing all terminal hypercube vertices, constructs both reduced coin matrices, and checks their purities against the exact formulas. It derives the Haar-integral terms independently in a separate exact-sum function, checks the crossover and minimal-purity inequalities, and samples \(4500\) independent Haar-coin pairs for every dimension \(2\le d\le9\). Using a fixed random seed, all 40 programmed assertions passed (36,000 sampled pairs); the largest sampled deviations were within five empirical standard errors of the exact values. These numerical tests support, but do not replace, the preceding all-dimension moment proof. Run with `python verify.py` using NumPy.

## Relationship to prior work

Quillen (2026) introduces precisely the time-independent-across-vertices, time-i.i.d. Haar coin walk and derives its **linear averaged quantum channel**, including the depolarized coin and the hypercube example (notably Eq. (57)). The new claim instead computes the **nonlinear** mean purity of the reduced coin of each **unaveraged pure-state realization**. The averaged channel alone cannot supply that mean because purity is quadratic in the density matrix.

Vieira, Amorim and Rigolin (2013) and Fang *et al.* (2023) study coin–position entanglement under temporally disordered or deliberately chosen coins, primarily in one-dimensional two-state walks and at long times or through optimal coin protocols. They do not assert the hypercube-wide two-step Haar moment formula or its dimension-three sign transition. These literatures establish the physical motivation for using coin–position entanglement rather than introducing it here.

The proof uses standard Haar second- and fourth-moment identities, and the result should not be interpreted as discovering those identities. Exhaustive priority beyond inspected works has not been independently established.

## Limitations

The result covers only the first two steps, a localized pure initial position, fully independent Haar coins at each step, and the hypercube's coordinate-flip shift. It concerns **mean linear entropy**, not mean von Neumann or Rényi entropy; replacing the mean of purity by a logarithm of its mean is not justified. It does not claim monotone entanglement growth at later times or for each individual sample, nor any asymptotic mixing law or concentration bound. More general graph shifts can have additional collisions, changing the formula.

## References

1. A. C. Quillen, *Quantum random walks on \(d\)-regular graphs with Haar-random coin operators*, Physical Review A **114**, 042410 (2026), DOI: 10.1103/rmmp-xdqy; earliest public version arXiv:2607.04584v1 (2026-07-06).
2. R. Vieira, E. P. M. Amorim and G. Rigolin, *Dynamically Disordered Quantum Walk as a Maximal Entanglement Generator*, Physical Review Letters **111**, 180503 (2013), arXiv:1305.4191.
3. X.-X. Fang, K. An, B.-T. Zhang, B. C. Sanders and H. Lu, *Maximal coin-position entanglement generation in a quantum walk for the third step and beyond regardless of the initial state*, Physical Review A **107**, 012433 (2023), arXiv:2209.01727.
4. T. A. Brun, H. A. Carteret and A. Ambainis, *Quantum random walks with decoherent coins*, Physical Review A **67**, 032304 (2003).
