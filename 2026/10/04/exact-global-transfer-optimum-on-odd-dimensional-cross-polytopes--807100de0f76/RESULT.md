# Exact global transfer optimum on odd-dimensional cross-polytopes

## Finding

Let
\[
N=4k+2\ge6,
\]
and let \(G_N\) be the \(N/2\)-cross-polytope graph, equivalently the cocktail-party graph obtained from \(K_N\) by deleting a perfect matching. Choose one deleted matched pair
\[
(u,\bar u).
\]
For the uniform adjacency Hamiltonian define the transfer probability
\[
P_N(t)=
\left|
\langle\bar u|e^{-itA(G_N)}|u\rangle
\right|^2.
\]

Then the global optimum is
\[
\boxed{
\max_{t\in\mathbb R}P_N(t)
=
\cos^2\!\left(\frac{\pi}{N}\right)
}.
\]
It is attained at
\[
\boxed{
t=\frac{\pi}{2}\pm\frac{\pi}{N}\pmod{\pi}.
}
\]

The source evaluates the same transfer at
\[
t=\frac{\pi}{2}
\]
and obtains
\[
P_N\!\left(\frac{\pi}{2}\right)
=
\left(1-\frac{2}{N}\right)^2.
\]
For every
\[
N=4k+2\ge6,
\]
this is strictly below the global optimum:
\[
\left(1-\frac{2}{N}\right)^2
<
\cos^2\!\left(\frac{\pi}{N}\right).
\]

The timing correction changes the asymptotic error scale. At the source time,
\[
1-P_N\!\left(\frac{\pi}{2}\right)
=
\frac4N-\frac4{N^2},
\]
whereas at the true optimum,
\[
1-\max_tP_N(t)
=
\sin^2\!\left(\frac{\pi}{N}\right)
\sim
\frac{\pi^2}{N^2}.
\]
Thus the best transfer on the non-perfect parity class is quadratically closer to perfect transfer than the source-time evaluation suggests.

## Assumptions and scope

The Hamiltonian is exactly the uniform single-excitation adjacency Hamiltonian used in the source: all present graph edges have hopping strength \(1\), all on-site terms vanish, and the missing edges are the antipodal perfect matching.

The result concerns the parity class
\[
N=4k+2.
\]
For
\[
N=4k,
\]
the source already proves perfect state transfer at
\[
t=\frac{\pi}{2}\pmod{\pi}.
\]

The quantity \(P_N(t)\) is explicitly the squared transition amplitude. This avoids a notational ambiguity in the source, whose initial “fidelity” definition is an amplitude modulus while its later displayed formula is a squared modulus.

## Proof

Write
\[
N=2m,
\]
where \(m\ge3\) is odd. The cocktail-party adjacency matrix has eigenvalues
\[
N-2,\qquad -2,\qquad 0.
\]
Using the spectral projectors, or equivalently the source factorization into the complete-graph and matching Hamiltonians, the amplitude between paired nonadjacent vertices is
\[
A_N(t)
=
-\frac12
+
\left(\frac12-\frac1N\right)e^{2it}
+
\frac1N e^{-i(N-2)t}.
\]

A direct trigonometric expansion gives
\[
1-|A_N(t)|^2
=
\frac{m-1}{m}\cos^2t
+
\frac1m\cos^2((m-1)t)
+
\frac{m-1}{m^2}\sin^2(mt).
\]
The right side is \(\pi\)-periodic. Write
\[
t=\frac{\pi}{2}+\varepsilon,
\qquad
-\frac{\pi}{2}\le\varepsilon\le\frac{\pi}{2}.
\]
Since \(m\) is odd,
\[
\cos^2t=\sin^2\varepsilon,
\qquad
\cos^2((m-1)t)=\cos^2((m-1)\varepsilon).
\]
Dropping the final nonnegative term yields
\[
1-|A_N(t)|^2
\ge
\frac1m g_m(\varepsilon),
\]
where
\[
g_m(\varepsilon)
=
(m-1)\sin^2\varepsilon
+
\cos^2((m-1)\varepsilon).
\]

Differentiate:
\[
g_m'(\varepsilon)
=
-2(m-1)\cos(m\varepsilon)\sin((m-2)\varepsilon).
\]
Hence every interior critical point belongs to one of two families.

If
\[
\cos(m\varepsilon)=0,
\]
then
\[
\cos^2((m-1)\varepsilon)=\sin^2\varepsilon,
\]
so
\[
g_m(\varepsilon)=m\sin^2\varepsilon.
\]
The smallest value in this family occurs at
\[
|\varepsilon|=\frac{\pi}{2m}
\]
and equals
\[
m\sin^2\!\left(\frac{\pi}{2m}\right).
\]

If
\[
\sin((m-2)\varepsilon)=0,
\]
then
\[
\cos^2((m-1)\varepsilon)=\cos^2\varepsilon,
\]
so
\[
g_m(\varepsilon)
=
1+(m-2)\sin^2\varepsilon
\ge1.
\]
The interval endpoints give \(g_m=m\). Since
\[
m\sin^2\!\left(\frac{\pi}{2m}\right)<1
\]
for every \(m\ge3\), the global minimum is
\[
\min_\varepsilon g_m(\varepsilon)
=
m\sin^2\!\left(\frac{\pi}{2m}\right).
\]
Therefore
\[
1-|A_N(t)|^2
\ge
\sin^2\!\left(\frac{\pi}{2m}\right)
=
\sin^2\!\left(\frac{\pi}{N}\right).
\]

At
\[
t=\frac{\pi}{2}\pm\frac{\pi}{2m}
=
\frac{\pi}{2}\pm\frac{\pi}{N},
\]
the dropped term also vanishes because
\[
\sin(mt)=0.
\]
Thus equality is achieved, proving
\[
\max_tP_N(t)=\cos^2\!\left(\frac{\pi}{N}\right).
\]

## Verification

`verify_cross_polytope_optimum.py` constructs \(G_N\) directly as \(K_N\) minus the antipodal matching and diagonalizes its adjacency matrix.

For
\[
N=6,10,14,18,22,30,50,
\]
it checks the exact-amplitude formula against direct matrix evolution, verifies the source-time value, verifies the predicted optimal times, and compares the optimum with a dense full-period search.

The script also checks the identity for
\[
1-|A_N(t)|^2
\]
at deterministic sample times.

The numerical replay is supplementary. The global maximization is proved analytically above.

## Relationship to prior work

Tsomokos, Plenio, de Vega, and Huelga identify the cross-polytope graph as a highly connected state-transfer network. They prove perfect transfer for
\[
N=4k
\]
and, for
\[
N=4k+2,
\]
evaluate the transfer at
\[
t=\frac{\pi}{2}
\]
to obtain the squared transition amplitude
\[
\left(1-\frac2N\right)^2,
\]
which they describe as approaching perfect transfer for large \(N\). Their analytical section does not maximize the non-perfect parity class over time.

Angeles-Canul, Norton, Opperman, Paribello, Russell, and Tamon later place cocktail-party graphs inside the mathematical perfect-state-transfer literature and recover the parity condition for perfect transfer. Their treatment concerns the existence of perfect state transfer and does not state the global sub-perfect transfer probability for the excluded parity class.

Later work on discrete-time walks establishes pretty-good transfer on cocktail-party graphs in a different dynamical model. Those results do not imply the continuous-time adjacency optimum derived here.

Targeted searches for the graph aliases “cross polytope,” “cocktail party,” and “hyperoctahedral,” together with maximum transfer probability, near-perfect transfer, and the candidate trigonometric value, did not locate the displayed finite-\(N\) optimum.

## Limitations

The result uses the unweighted adjacency Hamiltonian. Adding local potentials, edge weights, decoherence, or a Laplacian Hamiltonian changes the problem.

The theorem concerns transfer between the unique antipodal nonadjacent partner of a vertex. It does not classify maxima between arbitrary vertex pairs.

The result gives the exact one-shot maximum probability, not a robustness bound under static disorder.

A residual literature risk remains because cocktail-party graphs are highly symmetric and the same maximization may have appeared under a different graph-theoretic name or as an unstated corollary of a general spectral formula.

## References

1. D. I. Tsomokos, M. B. Plenio, I. de Vega, and S. F. Huelga, “State Transfer in Highly Connected Networks and a Quantum Babinet Principle,” arXiv:0808.2261, first public 16 August 2008; *Physical Review A* 78 (2008), 062310, DOI: 10.1103/PhysRevA.78.062310.
2. R. J. Angeles-Canul, R. M. Norton, M. C. Opperman, C. C. Paribello, M. C. Russell, and C. Tamon, “Perfect state transfer, integral circulants and join of graphs,” arXiv:0907.2148, first public 13 July 2009; *Quantum Information & Computation* 10 (2010), 325–342.
3. A. Chan and H. Zhan, “Pretty good state transfer in discrete-time quantum walks,” arXiv:2105.03762; *Journal of Physics A: Mathematical and Theoretical* 56 (2023), 165305.
