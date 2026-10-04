# Sharp runtime of the single-hypercube parallel-Hadamard construction
## Finding
Fix \(n\ge 1\). Label the computational basis by \(V=\{0,1\}^n\), and let \(Q_n\) be the \(n\)-dimensional hypercube. In the normalized-adjacency convention, the hypercube interval uses Hamiltonian \(A(Q_n)/n\). A loop-singleton phase layer chooses an arbitrary subset \(S\subseteq V\), places a self-loop at each vertex of \(S\) and no other edges, and evolves for a nonnegative duration. Empty layers are omitted. Consider all phase-sandwich implementations
\[
D_{\mathrm{out}}\,e^{-iA(Q_n)t/n}\,D_{\mathrm{in}}
\]
formed from arbitrary sequences of such phase layers before and after exactly one hypercube interval, with equality to \(H^{\otimes n}\) required only up to a global phase. The exact minimum total elapsed time is
\[
T_n^*=\frac{n\pi}{4}+\pi\min\{n,3\}
=
\begin{cases}
5\pi/4,&n=1,\\
5\pi/2,&n=2,\\
n\pi/4+3\pi,&n\ge3.
\end{cases}
\]
Equivalently, the optimal loop-singleton cost on each side of the hypercube is
\[
L_n=\frac{\pi}{2}\min\{n,3\}.
\]
Thus the \(n=2\) construction of Herrman and Wong with total time \(5\pi/2\) is optimal within this architecture. For \(n\ge3\), the two phase durations \(\pi\) and \(\pi/2\) on each side used by their general hypercube construction are jointly time-optimal.

## Assumptions and scope
The Hamiltonian normalization is exactly \(H=A/\lVert A\rVert\), so \(\lVert A(Q_n)\rVert=n\) and every nonempty loop-singleton layer has norm one. The only non-diagonal interval is one contiguous walk on \(Q_n\). Phase layers may use arbitrary loop masks and may be split into arbitrarily many intervals. All durations are nonnegative, and elapsed time is their ordinary sum. Equality of gates is taken up to a physically irrelevant overall scalar phase.

No claim is made for architectures with two or more non-diagonal intervals, graphs that mix ordinary edges and self-loops in the same interval, weighted adjacency matrices, ancillary vertices, negative-time controls, or a different Hamiltonian normalization.

## Proof
Write
\[
A(Q_n)=\sum_{j=1}^n X_j,
\]
where the commuting matrices \(X_j\) flip the \(j\)-th bit. For \(\theta=t/n\),
\[
U_n(t)=e^{-iA(Q_n)t/n}=
\bigl(\cos\theta\,I-i\sin\theta\,X\bigr)^{\otimes n}.
\]
If two diagonal unitary matrices turn \(U_n(t)\) into \(H^{\otimes n}\) up to a scalar, they cannot change entry magnitudes. An entry of \(U_n(t)\) between vertices at Hamming distance \(d\) has magnitude
\[
|\cos\theta|^{n-d}|\sin\theta|^d.
\]
All entries of \(H^{\otimes n}\) have magnitude \(2^{-n/2}\). Comparing distances \(d=0\) and \(d=1\) therefore forces
\[
|\cos\theta|=|\sin\theta|=2^{-1/2}.
\]
Hence
\[
\theta=\frac{\pi}{4}+\frac{k\pi}{2},\qquad k\in\mathbb Z,
\]
and the smallest positive hypercube duration is \(n\pi/4\).

At any such time let \(q=\sin\theta/\cos\theta\in\{-1,1\}\) and \(\rho=-iq\in\{i,-i\}\). After removing the scalar factor \((\cos\theta)^n\), the hypercube matrix has entries \(\rho^{d(x,y)}\). Since
\[
d(x,y)=h(x)+h(y)-2x\cdot y
\]
and \(\rho^2=-1\), the entrywise ratio between the Walsh-Hadamard matrix and the hypercube matrix factors as
\[
\frac{(-1)^{x\cdot y}}{\rho^{d(x,y)}}
=\rho^{-h(x)}\rho^{-h(y)}.
\]
All hypercube entries are nonzero. Consequently this diagonal factorization is unique up to independent scalar phases on the two sides: if \(a_xb_y\) equals the displayed rank-one ratio for every \(x,y\), then \(a_x/\rho^{-h(x)}\) is independent of \(x\), and similarly for \(b_y\). Thus, up to a scalar rotation, each side must realize the phase set
\[
\{\rho^{-h(v)}:v\in V\}.
\]

Now consider any collection of loop-singleton layers on one side, with durations \(\tau_1,\ldots,\tau_r\) and total duration \(T=\sum_j\tau_j\). A vertex \(v\) accumulates some phase
\[
e^{-is_v},\qquad s_v=\sum_{j:v\in S_j}\tau_j,
\]
so \(0\le s_v\le T\). Therefore, if \(T<2\pi\), all realized phases lie in a single directed circular arc of length at most \(T\), after an arbitrary common rotation. The required Hamming-weight phases are consecutive fourth roots of unity until all four classes have appeared. Their shortest covering-arc lengths are
\[
\frac{\pi}{2},\quad \pi,\quad \frac{3\pi}{2}
\]
for \(n=1\), \(n=2\), and \(n\ge3\), respectively. This proves
\[
T\ge L_n=\frac{\pi}{2}\min\{n,3\}
\]
on each side. The same phase set occurs for both choices \(\rho=\pm i\), so using a later uniform-mixing time never reduces the phase lower bound. Since later admissible hypercube times are larger by integer multiples of \(n\pi/2\), the globally shortest admissible hypercube time is optimal.

The bounds are attained. At \(t=n\pi/4\), choose the scalar representative of the correction phases conveniently. For \(n=1\), one layer of duration \(\pi/2\) suffices on each side. For \(n=2\), two nested layers of duration \(\pi/2\) realize accumulated times \(0,\pi/2,\pi\), giving cost \(\pi\) per side. For \(n\ge3\), one layer of duration \(\pi\) and one of duration \(\pi/2\) realize the four accumulated times \(0,\pi/2,\pi,3\pi/2\), giving cost \(3\pi/2\) per side. Adding the hypercube time proves the formula for \(T_n^*\).

## Verification
The proof is analytic: the lower bound uses entry magnitudes, uniqueness of a rank-one diagonal factorization, and a circular-arc obstruction for loop-singleton phases. The accompanying `verify.py` checks the Hamming-distance phase identity exactly for dimensions \(1\) through \(8\), computes the exact fourth-root covering-arc costs, verifies explicit phase-layer schedules for all three regimes, and confirms the resulting piecewise runtime formula. Running `python3 verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Herrman and Wong introduced the normalized time convention \(A/\lVert A\rVert\), used hypercube uniform mixing at the shortest time \(n\pi/4\), and corrected the resulting phases using looped singletons before and after the cube. Their two-qubit example is further simplified to total time \(5\pi/2\), and their general construction uses phase intervals of durations \(\pi\) and \(\pi/2\) on each side. The present result adds an architecture-sharp lower bound: no rearrangement, splitting, or alternative choice of loop masks can lower those phase costs for \(n=2\) or \(n\ge3\), and the \(n=1\) case has the separate optimum \(5\pi/4\) in the same one-cube architecture.

Wong's earlier isolated-vertex work supplies the looped-versus-loopless phase primitive and gate constructions, but not a phase-synthesis lower bound for a hypercube sandwich. Adisa and Wong later gave length-three constructions for arbitrary single-qubit gates and controlled single-qubit gates; that is a different architecture and does not imply a parallel \(n\)-qubit single-hypercube elapsed-time optimum. Chan's work characterizes instantaneous uniform mixing and complex Hadamard matrices in cube-related adjacency algebras, but does not optimize elapsed time of diagonal phase layers around a dynamic hypercube walk.

## Limitations
Optimality is only for the explicitly stated single-hypercube phase-sandwich architecture. A faster implementation may exist if one permits additional non-diagonal intervals, mixed edge-and-loop graphs, weights, ancillas, or a different energy normalization. The phase-layer lower bound is geometric and exact; the finite checker is corroborative rather than the basis of the infinite-dimensional-in-\(n\) proof. No claim is made that the construction is globally time-optimal among all continuous-time controls implementing \(H^{\otimes n}\).

## References
1. R. Herrman and T. G. Wong, “Simplifying Continuous-Time Quantum Walks on Dynamic Graphs,” arXiv:2106.06015v1 (2021); Quantum Information Processing 21, 54 (2022), DOI 10.1007/s11128-021-03403-7.
2. T. G. Wong, “Isolated Vertices in Continuous-Time Quantum Walks on Dynamic Graphs,” arXiv:1908.00507; Physical Review A 100, 062325 (2019), DOI 10.1103/PhysRevA.100.062325.
3. I. A. Adisa and T. G. Wong, “Implementing Quantum Gates Using Length-3 Dynamic Quantum Walks,” arXiv:2108.01055; Physical Review A 104, 042604 (2021), DOI 10.1103/PhysRevA.104.042604.
4. A. Chan, “Complex Hadamard matrices, instantaneous uniform mixing and cubes,” Algebraic Combinatorics 3 (2020), 757–774, DOI 10.5802/alco.112.
