# Exact band and flat-band spectrum of the equilateral Kirchhoff loop chain
## Finding
Consider the infinite metric graph with vertices indexed by \(j\in\mathbb Z\), one unit backbone edge from vertex \(j\) to vertex \(j+1\), and one unit loop attached at every vertex. On every edge let the operator be \(-d^2/dx^2\), with continuity and zero sum of outgoing derivatives at every vertex. This is the all-zero-phase, \(\delta=0\) specialization of the translation-invariant quasi-\(\delta\) loop-chain family studied by Balmaseda, Di Cosmo and Pérez-Pardo.

Its complete spectrum is
\[
\sigma(H)=\{k^2:k\ge0,\ \cos k\ge0\}\cup\{((2j+1)\pi)^2:j\ge0\}.
\]
For \(k>0\) with \(k\notin\pi\mathbb Z\), the Bloch dispersion relation is exactly
\[
\cos\theta=2\cos k-1,
\]
so the dispersive band part is present exactly when \(\cos k\ge0\). In addition, every energy \((n\pi)^2\), \(n\ge1\), is an eigenvalue of infinite multiplicity. If \(n\) is even, a compact eigenfunction can be supported on one loop. If \(n\) is odd, a compact eigenfunction can instead be supported on one backbone edge and the two loops at its endpoints, with the backbone sine amplitude equal to \(1\) and each loop sine amplitude equal to \(-1/2\).

Consequently each momentum interval on which \(\cos k<0\) is empty of dispersive spectrum but is pierced at its center by an odd Dirichlet flat band. The odd flat bands are therefore genuine gap eigenvalues, while the even flat bands sit at dispersive band edges.

## Assumptions and scope
The graph is exactly the equilateral unit-interval loop chain appearing in the source's Section 4, and the boundary condition is its special case with all phase parameters and \(\delta\) equal to zero. The statement concerns the nonnegative standard Kirchhoff Laplacian and uses the source's unit edge length. No claim is made here for unequal edge lengths, nonzero quasi-\(\delta\) parameters, magnetic phases, or added periodic potentials.

The spectral formula includes the threshold \(0\). For positive energy write \(E=k^2\) with \(k>0\). The term “flat band” refers to an energy that occurs in every Floquet fiber and consequently gives an infinite-multiplicity eigenvalue on the infinite graph.

## Proof
Let \(u_j\) denote the common value of a nonresonant eigenfunction at vertex \(j\), and assume first that \(k\notin\pi\mathbb Z\). On a unit backbone edge joining values \(u_j\) and \(u_{j+1}\), the outgoing derivative at vertex \(j\), divided by \(k\), is
\[
\frac{u_{j+1}-u_j\cos k}{\sin k}.
\]
The two endpoints of the unit loop both have value \(u_j\). Solving the edge equation on that loop shows that the sum of its two outgoing derivatives is
\[
2k u_j\tan(k/2).
\]
Kirchhoff balance at vertex \(j\) therefore gives
\[
\frac{u_{j+1}+u_{j-1}-2u_j\cos k}{\sin k}+2u_j\tan(k/2)=0.
\]
Using \(\sin k\tan(k/2)=1-\cos k\), this reduces to the constant-coefficient recurrence
\[
u_{j+1}+u_{j-1}=2(2\cos k-1)u_j.
\]
For a Bloch sequence \(u_j=e^{ij\theta}u_0\), the recurrence is equivalent to
\[
\cos\theta=2\cos k-1.
\]
The Floquet transform of the periodic graph is a direct integral over real \(\theta\), so a nonresonant energy belongs to the spectrum exactly when the right-hand side lies in \([-1,1]\). This is equivalent to \(0\le\cos k\le1\), hence to \(\cos k\ge0\).

It remains to analyze the resonances \(k=n\pi\). Take zero vertex values and write the sine amplitude on the backbone edge from \(j\) to \(j+1\) as \(a_j\), and the sine amplitude on the loop at vertex \(j\) as \(b_j\). Direct evaluation of outgoing derivatives gives the exact vertex equation
\[
a_j-(-1)^n a_{j-1}+(1-(-1)^n)b_j=0.
\]
If \(n\) is even, this becomes \(a_j-a_{j-1}=0\). Taking every \(a_j=0\) and one nonzero \(b_j\) produces a one-loop eigenfunction. Translating it gives infinitely many mutually orthogonal eigenfunctions.

If \(n\) is odd, the vertex equation is
\[
a_j+a_{j-1}+2b_j=0.
\]
Choose one backbone coefficient, say \(a_0=1\), and all other \(a_j=0\). Then \(b_0=b_1=-1/2\) and every other \(b_j=0\). This is a compact eigenfunction supported on one backbone edge and its two endpoint loops. Translations with sufficiently separated supports give infinitely many linearly independent eigenfunctions. Thus every \((n\pi)^2\) has infinite multiplicity.

There are no further spectral points. Away from \(\pi\mathbb Z\), the Floquet condition above is necessary and sufficient. At \(\pi\mathbb Z\), the resonant analysis accounts for the additional fiber eigenvalues. Since the Kirchhoff Laplacian is nonnegative, there is no negative spectrum. Combining the nonresonant bands, their closure, and the resonant flat bands yields the displayed complete formula.

## Verification
The accompanying `verify.py` checks the reduction of the vertex equation to the Bloch discriminant numerically at nonresonant samples, verifies the equivalence between \(|2\cos k-1|\le1\) and \(\cos k\ge0\), and verifies the even- and odd-parity resonant derivative balances exactly at the coefficient level. These computations are checks of the algebra; the proof above, not finite sampling, establishes the infinite statement.

A separate source-level check was made against the primary article's explicit all-zero-parameter system. The article itself warns that satisfying those algebraic boundary equations only produces candidates for generalized eigenfunctions and does not by itself establish spectral membership. The Floquet reduction above supplies that missing membership test for this standard equilateral case.

## Relationship to prior work
Balmaseda, Di Cosmo and Pérez-Pardo derive the translation-invariant quasi-\(\delta\) boundary equations for this loop chain and display the all-zero-parameter specialization, but they explicitly caution that the resulting algebraic solutions are only candidates for generalized eigenfunctions because not every parameter value need belong to the spectrum. Their paper therefore does not state the complete band set above.

Kuchment's general periodic-quantum-graph theory proves that periodic point spectrum is generated by compactly supported eigenfunctions, and Exner's review emphasizes the generic occurrence of infinitely degenerate Dirichlet eigenvalues on periodic graphs containing commensurate loops. Those results explain why flat bands are natural here, but they do not give the specific discriminant \(2\cos k-1\), the exact band set, or the odd-resonance three-edge compact mode for this graph. Düll, Schneider and Taraca analyze a different “necklace” geometry in which two arcs connect successive vertices; that topology is not the pendant-loop chain treated here.

## Limitations
The result is specialized to unit lengths and standard Kirchhoff coupling. The same calculation can be started for unequal backbone and loop lengths, but commensurability and resonance bookkeeping then change and are not asserted here. Likewise, the formula does not cover the nonzero phase and nonzero \(\delta\) members of the source's quasi-\(\delta\) family.

The literature search found no statement of this exact complete spectrum, but absence from the searched sources is not a proof of universal novelty. The main residual risk is an older or differently named treatment of the same pendant-loop periodic graph in which the same elementary Floquet discriminant and resonant modes were written down.

## References
1. A. Balmaseda, F. Di Cosmo, J. M. Pérez-Pardo, “On \(\mathbb Z\)-Invariant Self-Adjoint Extensions of the Laplacian on Quantum Circuits,” *Symmetry* 11 (2019), 1047. arXiv:1908.04214v1. DOI: 10.3390/sym11081047.
2. P. Kuchment, “Quantum Graphs II: Some spectral properties of quantum and combinatorial graphs,” *J. Phys. A* 38 (2005), 4887–4900. arXiv:math-ph/0411003. DOI: 10.1088/0305-4470/38/22/013.
3. P. Exner, “Topologically Induced Spectral Behavior: The Example of Quantum Graphs,” review article, 2020, mp_arc 20-24.
4. W.-P. Düll, G. Schneider, R. Taraca, “On the Korteweg–de Vries approximation for a Boussinesq equation posed on the infinite necklace graph,” *Math. Methods Appl. Sci.* 47 (2024), 9796–9813. DOI: 10.1002/mma.10095.
