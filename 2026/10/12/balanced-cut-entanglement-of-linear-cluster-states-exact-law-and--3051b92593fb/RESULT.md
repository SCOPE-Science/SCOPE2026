# Balanced-cut entanglement of linear cluster states: exact law and Gaussian limit

## Finding

The complete balanced-bipartition entanglement law of an even-length one-dimensional cluster state is a coefficient of an explicit four-state transfer matrix. Its typical entanglement has a Gaussian limit with a nontrivial extensive mean, whereas fully maximally entangled balanced cuts are exponentially rare.

**Theorem.** For every integer \(m\ge2\), put \(n=2m\) and prepare the \(n\)-qubit open-path graph state \(|P_n\rangle\). Select a subset \(A\subseteq\{1,\ldots,n\}\) uniformly among the \(\binom{n}{m}\) choices of cardinality \(m\); define \(S(\rho)=-\operatorname{tr}(\rho\ln\rho)\) in nats and let \(R_n=S(\operatorname{tr}_{A^c}|P_n\rangle\langle P_n|)/\ln 2\) be its bipartite von Neumann entanglement entropy **in bits**. Define the ordered state labels \((a,s)=(0,0),(0,1),(1,0),(1,1)\), a row vector \(w(z)=(1,0,z,0)\), and

\[
T(z,t)=\begin{pmatrix}
1&0&0&zt\\
1&0&z&0\\
0&t&z&0\\
1&0&z&0
\end{pmatrix}.
\]

Then the complete finite-size distribution is determined by

\[
\boxed{\displaystyle \mathbb E[t^{R_{2m}}]=\frac{[z^m]w(z)T(z,t)^{2m-1}\mathbf 1}{\binom{2m}{m}}.}
\]

Here \([z^m]\) denotes coefficient extraction, \(\mathbf1\) is the all-ones column vector, and the equality holds as an identity of polynomials in \(t\). The two endpoint probabilities are exactly

\[
\boxed{\displaystyle \Pr(R_{2m}=1)=\frac2{\binom{2m}{m}},\qquad
\Pr(R_{2m}=m)=\frac{2^m}{\binom{2m}{m}}\sim\sqrt{\pi m}\,2^{-m}.}
\]

As \(m\to\infty\),

\[
\boxed{\displaystyle \mathbb E R_{2m}=\frac{2m}{3}+O(1),\qquad
\operatorname{Var}(R_{2m})=\frac{4m}{27}+O(1),\qquad
\frac{R_{2m}-2m/3}{\sqrt{4m/27}}\Longrightarrow N(0,1).}
\]

In particular, a typical uniformly balanced, possibly disconnected partition has extensive entropy occupying asymptotically two thirds of its maximal \(m\)-bit capacity. This is distinct from entanglement across a *contiguous* cut of the same path state, which is at most one bit.

## Assumptions and scope

The graph is the simple open path with edges \(\{i,i+1\}\), \(1\le i<n\), not a cycle. The state is pure and noiseless:

\[
|P_n\rangle=2^{-n/2}\sum_{x\in\{0,1\}^n}(-1)^{\sum_{i=1}^{n-1}x_ix_{i+1}}|x\rangle.
\]

The bipartition is chosen uniformly among all subsets of exactly half the sites, with complements counted separately. The entropy uses natural logarithms before division by \(\ln 2\); the reported entropy is in bits. All asymptotics are along even \(n\), and the theorem does not assert that this law governs random-circuit entanglement growth.

## Proof

**1. Binary cut rank gives the entropy.** For a fixed \(A\), separate controlled-phase factors wholly inside \(A\) and \(A^c\) into local unitaries. The remaining coefficient matrix in computational bases is the binary character matrix \(2^{-n/2}(-1)^{u^\top Bv}\), where \(B\) is the \(A\)-to-\(A^c\) adjacency matrix over \(\mathbb F_2\). Orthogonality of characters shows that the reduced density operator has exactly \(2^r\) equal nonzero eigenvalues, each \(2^{-r}\), with \(r=\operatorname{rank}_{\mathbb F_2}B\). Therefore \(R_n=r\) exactly, for all cuts.

**2. The rank is the crossing-forest matching number.** The cut edges form a subgraph of the path, hence a bipartite forest with color classes \(A\) and \(A^c\). A nonzero \(r\)-minor implies a matching of size \(r\), so matrix rank is at most the maximum matching size \(\nu\). Conversely choose a maximum matching and retain its covered vertices on each side. The induced square submatrix has a perfect matching; in a forest such a perfect matching is unique, because the symmetric difference of two perfect matchings would contain an alternating cycle. The determinant's Leibniz sum is therefore a single nonzero term (including in characteristic two), proving \(r=\nu\).

**3. A four-state transfer counts every balanced cut.** Encode site membership by \(a_i=\mathbf 1\{i\in A\}\). Edge \(i\) crosses the cut precisely when \(a_i\ne a_{i+1}\). The standard left-to-right greedy matching of a path selects the crossing edge whenever it does not touch the immediately preceding selected edge. With \(s_0=0\), write this selection as

\[
s_i=\mathbf1\{a_i\ne a_{i+1}\}(1-s_{i-1}),\quad 1\le i<n.
\]

This greedy matching is maximum: selecting the leftmost available edge never reduces optimal cardinality, by exchanging it with the edge incident to its first vertex in any optimum matching; iterate on the remaining suffix. Consequently \(R_n=\sum_{i=1}^{n-1}s_i\). Store the last membership bit \(a_i\) and previous greedy selection \(s_{i-1}\). A transition with new membership \(b\) contributes \(z^b t^{s_i}\) and updates to \((b,s_i)\); this is precisely the displayed \(T\). The initial bit contributes \(w(z)\). Summation over all bits gives \(w(z)T(z,t)^{n-1}\mathbf1\), whose \(z^m\) coefficient counts exactly the balanced subsets. Division by \(\binom{n}{m}\) proves the polynomial formula and all its coefficients without approximation.

**4. The endpoint probabilities are exact.** A cut has \(R_{2m}=m\) precisely when its crossing forest has a perfect matching of the full path. The path has only one perfect matching, using edges \(\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\). Those \(m\) edges must all cross the cut; independently assigning their two endpoints to opposite sides yields exactly \(2^m\) balanced membership strings. For \(m\ge2\), a crossing forest has maximum matching size one only if it has one edge or a pair of consecutive edges. Two consecutive crossings place a single bit opposite all other bits and are not balanced. One crossing must occur exactly in the middle, giving the two strings \(0^m1^m\) and \(1^m0^m\). Stirling's formula yields the stated maximal-entropy probability asymptotic.

**5. The Gaussian law from the dominant transfer eigenvalue.** Direct expansion gives the exact characteristic polynomial

\[
\det(\lambda I-T(z,t))=\lambda\bigl[\lambda^3-(1+z)\lambda^2+z(1-2t)\lambda+tz(z+1)\bigr].
\]

At \((z,t)=(1,1)\), the eigenvalues are \(2,1,-1,0\). The transfer is nonnegative and primitive there; for positive \(t\) near one it has a unique analytic dominant eigenvalue \(\lambda(z,t)\) near \((z,t)=(1,1)\). At \(z=1\) its explicit value is

\[
\lambda(1,t)=\frac{1+\sqrt{1+8t}}{2}.
\]

Complementation of all membership bits yields the identity \(F_n(z,t)=z^nF_n(z^{-1},t)\) for \(F_n=wT^{n-1}\mathbf1\). Hence the central coefficient saddle for \([z^{n/2}]F_n\) remains exactly at \(z=1\) for all positive \(t\) close to one. To justify uniform saddle extraction, use Fourier integration on \(|z|=1\): away from \(z=1\), the spectral radius is strictly smaller than \(\lambda(1,t)\). Indeed equality in the entrywise modulus comparison would force the unit-phase factor for the \((0,0)\) self-loop (weight one) to equal that of the \((1,0)\) self-loop (weight \(z\)); hence \(z=1\). At the saddle, implicit differentiation of the characteristic cubic in logarithmic variables \(x=\log z\), \(u=\log t\) gives

\[
\left.\nabla\log\lambda(e^x,e^u)\right|_{0,0}
=\left(\frac12,\frac13\right),\qquad
\left.\nabla^2\log\lambda(e^x,e^u)\right|_{0,0}
=\begin{pmatrix}1/4&0\\0&2/27\end{pmatrix}.
\]

The positive \(x\)-curvature \(1/4\) gives a nondegenerate Gaussian coefficient saddle; the strict spectral gap away from it provides exponentially small tails. Standard analytic Gaussian integration, uniform for complex \(u\) near zero, therefore gives an analytic nonvanishing prefactor \(C(u)\), with \(C(0)=1\), satisfying

\[
\mathbb E[e^{uR_n}]=C(u)\left(\frac{1+\sqrt{1+8e^u}}4\right)^n\bigl(1+O(n^{-1})\bigr),
\qquad n\ \text{even}.
\]

The error is locally uniform and analytic in \(u\); differentiating its logarithm yields the first two cumulants. The exponent \(\psi(u)=\log((1+\sqrt{1+8e^u})/4)\) satisfies \(\psi'(0)=1/3\) and \(\psi''(0)=2/27\). Finally, putting \(u=is/\sqrt{2n/27}\) in the centered characteristic function, its Taylor expansion gives convergence to \(e^{-s^2/2}\) for every real \(s\). Lévy's theorem proves the stated central limit theorem.

## Verification

The standalone `verify.py` requires only the Python standard library. It independently computes cut-adjacency ranks by binary elimination for all membership strings of path lengths \(2\) through \(14\), compares their complete distributions with the four-state transfer enumeration, and confirms the exact endpoint counts. It additionally certifies the displayed characteristic-polynomial identity by evaluation on a sufficient exact integer interpolation grid and checks the rational cumulant Hessian from the implicit derivatives. It prints `VERIFY_OK` on completion. These finite computations check the algebra and small sizes, while the full finite-size theorem and limit law are justified by the preceding proofs, not by extrapolation.

## Relationship to prior work

Rao et al. (arXiv:2605.11076, 2026) study graph-state circuit primitives and show that **contiguous block-cut** entanglement profiles relate to circuit entanglement velocity. Their height function uses cuts \(\{1,\ldots,x\}\), not all balanced, disconnected subsets. The present theorem instead describes the complete equal-size partition distribution of the *isolated* open-path graph state; it does not infer velocities.

More directly, Facchi, Florio, and Pascazio (Physical Review A 74, 042331, 2006) explicitly plotted the balanced-bipartition participation-number histograms of one-dimensional cluster states for finite small system sizes (their Fig. 1, including \(n=12\)). Their histogram object agrees with the present entropy law under the exact transformation \(N_{AB}=2^{R_n}\). The result here is the all-size coefficient formula, exact extreme frequencies, and a proved large-size Gaussian law, not the proposal of the statistic, the identification of cluster states, or the plotted finite cases. Hajdušek and Murao (arXiv:1207.5877) provide established graph-state entanglement/matching methods in a different entanglement setting. The binary cut-rank identity and path matching recurrence are standard ingredients and are not presented as separate novel results.

## Limitations

No claim is made about noisy cluster states, periodic chains, other graph families, arbitrary partition sizes, or dynamical entanglement speeds. Analytic results apply to even length and uniform balanced subsets; they are not numerical fits. The earlier cluster-state finite histogram literature makes an unlocated equivalent all-size derivation a remaining priority possibility, rather than something that can be ruled out by search alone. This result has had no independent external audit.

## References

1. C. Rao, H. Sahu, A. Bhattacharya, S. A. Rather, M. Flory, and Z. Raissi, *Graph-State Circuit Blocks control Entanglement and Scrambling Velocities*, arXiv:2605.11076v1 (public 2026-05-11), https://arxiv.org/abs/2605.11076. Related public replication dataset DOI:10.57903/UJ/EJAAFN (published 2026-05-04).
2. P. Facchi, G. Florio, and S. Pascazio, *Probability-density-function characterization of multipartite entanglement*, Phys. Rev. A 74, 042331 (2006), DOI:10.1103/PhysRevA.74.042331; lawful open full text: https://home.ba.infn.it/~facchi/papers/59%20entrandom.pdf.
3. M. Hajdušek and M. Murao, *Direct evaluation of pure graph state entanglement*, arXiv:1207.5877 (2012), https://arxiv.org/abs/1207.5877.
