# Sharp register–activation tradeoff for selectable phase-kickback catalyst banks
## Finding
Let \(n\ge 2\) and put \(N=2^n-1\). A binary-selectable eigenphase-kickback bank consists of \(r\) offline \(n\)-qubit eigenstate catalysts \(|\psi_{k_1}\rangle,\ldots,|\psi_{k_r}\rangle\) of the same primitive-polynomial Clifford \(U_f\). In one online use, each associated controlled \(U_f\) is either applied once or omitted. Thus a selected subset \(S\subseteq[r]\) implements the residue
\[
\sigma(S)=\sum_{i\in S} k_i \pmod N.
\]
If all \(N\) residues are reachable and each target has a realization using at most \(h\) active kickbacks, then
\[
\sum_{j=0}^h \binom{r}{j}\ge N.
\]
In particular, every universal bank has \(r\ge n\). If \(r=n\), then necessarily \(h\ge n-1\). Both bounds are sharp for the source bank \(k_i\equiv a2^i\pmod N\), where \(a\) is coprime to \(N\): every residue has a representation with at most \(n-1\) active kickbacks.

Therefore, within this independent single-use on/off architecture, the variable-angle construction uses the minimum possible \(n\) eigenstate registers, hence the minimum \(n^2\) eigenstate-catalyst qubits, and among register-minimal universal banks it also has the minimum possible worst-case number \(n-1\) of controlled-\(U_f\) invocations.

## Assumptions and scope
The statement is about the exact architecture in which a fixed bank of eigenstate catalysts is prepared offline and each bank element contributes either zero or one copy of its eigenphase online. Repeated powers of \(U_f\), target-dependent controlled powers, coherent arithmetic on the exponent, measurements that change the online operation, and more general catalytic embeddings are outside the model.

This restriction matters. A later construction uses a single universal eigenstate catalyst together with a target-dependent controlled \(U_f^{d'}\), achieving an \(O(\log(1/\epsilon))\)-qubit universal catalyst. That method changes the online operation and is not a counterexample to the selectable-bank bound.

## Proof
For each subset \(S\subseteq[r]\), phase kickback adds the eigenphases, so the implemented residue is \(\sigma(S)\). If every target can be implemented using at most \(h\) active bank elements, all \(N\) residues must lie in the image of the subsets of size at most \(h\). There are exactly
\[
\sum_{j=0}^h \binom{r}{j}
\]
such subsets. Collisions of subset sums can only reduce the image size, proving the inequality.

Taking \(h=r\) gives \(2^r\ge 2^n-1\). For integral \(r\) and \(n\ge2\), \(r\le n-1\) would imply \(2^r\le2^{n-1}<2^n-1\), so \(r\ge n\).

Now set \(r=n\). If \(h\le n-2\), then
\[
\sum_{j=0}^h\binom{n}{j}
\le 2^n-\binom{n}{n-1}-\binom{n}{n}
=2^n-n-1
<2^n-1=N.
\]
Hence \(h\ge n-1\).

For sharpness, take the source family \(k_i\equiv a2^i\pmod N\), \(i=0,\ldots,n-1\), with \(\gcd(a,N)=1\). Given any residue \(b\), choose the unique \(m\in\{0,1,\ldots,N-1\}\) satisfying \(am\equiv b\pmod N\). Because \(m\le N-1=2^n-2\), its \(n\)-bit expansion is never the all-ones word, so its Hamming weight is at most \(n-1\). Selecting precisely the powers of two occurring in that expansion implements \(b\) with at most \(n-1\) active kickbacks. Thus both lower bounds are attained.

Each \(|\psi_k\rangle\) in the construction occupies \(n\) qubits. Therefore \(r\ge n\) implies at least \(n^2\) eigenstate-catalyst qubits inside this bank architecture, attained by the source construction.

## Verification
The proof is counting-theoretic and does not rely on finite enumeration. A standalone checker in `artifacts/verify.py` exhaustively verifies the source bank for \(2\le n\le12\): it confirms complete residue coverage, worst-case minimum activation count \(n-1\), and the two binomial inequalities used in the proof. These finite checks are corroborative only.

The primary source was inspected at its phase-kickback construction, resource estimate, and discussion. It explicitly prepares \(n\) eigenstate catalysts, selectively applies the corresponding phase kickbacks, reports \(n^2\) catalyst-state size for that method, and later notes an \(O(n)\)-size arbitrary-rotation improvement. The later Kim–Laakkonen paper was inspected at its arbitrary-angle catalysis construction: it uses a single eigenstate catalyst and a target-dependent controlled power \(U_f^{d'}\), which falls outside the on/off bank model.

## Relationship to prior work
Kim's 2026 paper gives the sufficient bank \(|\psi_{a2^t}\rangle\) for \(t\in[n]\), says that the variable-angle variant appears to need \(n\) copies, and reports the resulting quadratic catalyst size. It does not state a lower bound for arbitrary selectable eigenphase banks.

Kim and Laakkonen subsequently reduce the universal catalyst to \(O(\log(1/\epsilon))\) qubits by replacing subset selection of fixed controlled-\(U_f\) kickbacks with a target-dependent controlled \(U_f^{d'}\). Their construction therefore gives broader resource performance but does not cover the architecture-restricted lower bound here. The earlier catalytic-embedding framework is more general still and does not specialize to this sharp subset-count tradeoff.

## Limitations
The result is not a lower bound on arbitrary catalytic rotation synthesis, arbitrary constant-\(T\)-depth circuits, or arbitrary implementations of controlled powers of \(U_f\). It does not prove an \(\Omega(n^2)\) lower bound on \(T\)-count. It only characterizes the number of registers and active fixed kickbacks in the stated independent single-use selectable-bank model.

The originality search can miss very recent or differently indexed observations. The main residual risk is an equivalent counting remark stated informally under subset-sum or phase-gradient terminology.

## References
1. Isaac H. Kim, “Catalytic z-rotations in constant T-depth,” Quantum 10, 2191 (2026), DOI 10.22331/q-2026-08-13-2191; arXiv:2506.15147. First public preprint: 2025-06-18.
2. Isaac H. Kim and Tuomas Laakkonen, “Any Clifford+T circuit can be controlled with constant T-depth overhead,” arXiv:2512.24982v1 (2025).
3. M. Amy, M. Crawford, A. N. Glaudell, M. L. Macasieb, S. S. Mendelson, and N. J. Ross, “Catalytic Embeddings of Quantum Circuits,” arXiv:2305.07720v1 (2023).
