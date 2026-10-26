# Exact single-sensor observability resonances of a singly weighted cycle

## Finding

Consider every integer \(n\ge5\). Label the vertices \(0,1,\ldots,n-1\), give edges \(\{i,i+1\}\), for \(0\le i<n-1\), unit conductance, and give the closing edge \(\{0,n-1\}\) a conductance \(w>0\). Let \(L_w\) be the weighted Laplacian. Observe the consensus dynamics \(\dot z=-L_w z\) at the single vertex \(1\), so that \(y=z_1\).

**Theorem.** The pair \((-L_w,e_1^{\mathsf T})\) is observable if and only if all of the following hold:

1. \(6\nmid n\);
2. \(w\ne1\);
3. \(w\ne\tfrac12-\cos(2\pi k/(n-3))\) for every integer \(1\le k\le\lfloor(n-4)/2\rfloor\) for which the right-hand side is positive.

Equivalently, for \(6\mid n\) the sensor is blind at **every** positive closing-edge weight. At every other cycle length it is blind precisely at the uniform weight and a finite, explicitly listed set of positive resonant weights. For example, \(n=7\) has the additional resonance \(w=1/2\); \(n=8\) has additional resonances \(w=(3-\sqrt5)/4\) and \(w=(3+\sqrt5)/4\). The sharp classification is unchanged by replacing observability with controllability using a single input at vertex \(1\), because \(L_w\) is symmetric.

## Assumptions and scope

The system is finite dimensional, continuous time, real, linear, and noise free. The output is the exact state at vertex \(1\), one unit edge inward from an endpoint of the exceptional closing edge. The two endpoints of that edge are vertices \(0,n-1\); all other edges have identical positive weight normalized to \(1\). The closing-edge weight lies in \((0,\infty)\). Observability means that distinct initial states produce distinct full output trajectories, equivalently that no nonzero eigenvector of \(L_w\) has zero entry at vertex \(1\) (symmetric Popov–Belevitch–Hautus test). No assertion is made for arbitrary sensor positions or for multiple perturbed edges.

## Proof

**1. Parity decomposition.** Write \(b=e_0-e_{n-1}\). The exact Laplacian is
\[
L_w=L(P_n)+wbb^{\mathsf T},
\]
where \(P_n\) is the unit path with vertices \(0,\ldots,n-1\). Reflection \((Ru)_i=u_{n-1-i}\) commutes with \(L_w\), and \(Rb=-b\). Path eigenvectors and eigenvalues may be chosen as
\[
q_j(i)=\cos\!\left(\frac{\pi j(i+1/2)}n\right),\qquad
\lambda_j=2-2\cos\!\left(\frac{\pi j}n\right),\quad 0\le j<n.
\]
These eigenvalues are strictly increasing; \(Rq_j=(-1)^jq_j\). All even-indexed modes \(q_{2r}\) remain eigenvectors of \(L_w\) with the same eigenvalues. The odd-parity restriction is a real symmetric irreducible Jacobi matrix, differing from its \(w=0\) form only in the first diagonal entry, which is \(1+2w\).

**2. No cross-parity coincidence when \(w\ne1\).** The ordered odd-parity eigenvalues at \(w=0\) are \(\lambda_1,\lambda_3,\ldots\). Every eigenvector of the odd Jacobi matrix has nonzero first coordinate, by the three-term recurrence; hence each eigenvalue is strictly increasing with \(w\), by the simple-eigenvalue derivative formula for a positive rank-one diagonal perturbation. Standard rank-one strict interlacing places its \(r\)-th eigenvalue strictly between \(\lambda_{2r-1}\) and \(\lambda_{2r+1}\) whenever the latter exists. At \(w=1\), the graph is the uniform cycle: the \(r\)-th odd-parity eigenvalue equals \(\lambda_{2r}\) for every matching even mode, with one unmatched top odd-parity eigenvalue \(4\) when \(n\) is even. Consequently the strictly increasing odd branch meets its possible even-parity neighbor only at \(w=1\); it cannot reach the next even eigenvalue by interlacing. Within each parity all eigenvalues are simple. Thus \(L_w\) has simple spectrum for \(w\ne1\). At \(w=1\), a nonzero cycle eigenvalue has multiplicity two, so one scalar measurement cannot observe the entire state.

**3. Even-parity blind modes.** At the measured vertex, the surviving even modes satisfy
\[
q_{2r}(1)=\cos\!\left(\frac{3\pi r}{n}\right),
\quad 1\le r\le\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
This quantity vanishes exactly when \(6r=n(2s+1)\) for an integer \(s\ge0\). If \(n\) is odd, parity makes the equality impossible. If \(n=2m\), it reads \(3r=m(2s+1)\) with \(1\le r<m\). When \(3\nmid m\), the odd factor is at least \(3\) and forces \(r\ge m\), impossible; when \(3\mid m\), the choice \(r=m/3\) works. Therefore a weight-independent even-mode obstruction exists exactly for \(6\mid n\).

**4. Odd-parity blind modes.** Set \(h=\lfloor n/2\rfloor\), and represent an antisymmetric eigenvector by its first \(h\) coordinates \(v_0,\ldots,v_{h-1}\). They satisfy an irreducible tridiagonal eigen-equation whose first two rows, when \(h\ge3\), are
\[
(1+2w)v_0-v_1=\lambda v_0,\qquad
-v_0+2v_1-v_2=\lambda v_1.
\]
If \(v_1=0\), these rows and irreducibility force \(v_0=-v_2\ne0\) and \(\lambda=1+2w\). The tail \(v_2,\ldots,v_{h-1}\) then obeys
\[
-v_{r-1}+2v_r-v_{r+1}=\lambda v_r
\]
with the left boundary \(v_1=0\). At the right end, reflection gives \(v_h=0\) for odd \(n\) and \(v_h=-v_{h-1}\) for even \(n\). With \(\lambda=2-2\cos\theta\), its nonzero solutions are proportional to \(v_r=\sin((r-1)\theta)\) for \(r\ge2\). The right boundary quantizes the angle exactly as
\[
\theta=\frac{2\pi k}{n-3},\qquad
1\le k\le\left\lfloor\frac{n-4}{2}\right\rfloor.
\]
For odd \(n\), this is the Dirichlet condition \(\sin((h-1)\theta)=0\); for even \(n\), it is \(\sin((h-1)\theta)=-\sin((h-2)\theta)\). Each allowed angle lies strictly between \(0\) and \(\pi\), making the tail a genuine nonzero eigenvector. Using \(\lambda=1+2w\), the exceptional weight is exactly
\[
w=\frac12-\cos\!\left(\frac{2\pi k}{n-3}\right).
\]
Only positive weights belong to the stated domain. Conversely, any allowed positive value gives a nonzero antisymmetric eigenvector: take the stated tail, set \(v_1=0\), \(v_0=-v_2\), and reflect with a minus sign. This also covers \(n=5\), whose index range is empty and whose two-dimensional antisymmetric Jacobi matrix has no eigenvector with zero second coordinate.

Combining steps 2–4 and the PBH criterion proves both necessity and sufficiency. Symmetry of \(L_w\) gives the matching controllability statement.

## Verification

The accompanying `check_observability.py` constructs the exact weighted Laplacian, diagonalizes it numerically, and compares the theorem's exclusion predicate with simple-spectrum PBH observability for \(n=5,\ldots,36\). The fixed-seed suite tests 816 length-weight combinations, including all positive predicted resonances and random off-resonance weights; the executed suite returned `CASES 816 MISMATCHES 0`. Exact symbolic determinant factorizations of the finite observability matrix for \(n=5,\ldots,10\) were also checked during derivation. These finite checks illustrate rather than replace the all-size proof above.

## Relationship to prior work

Parlangeli and Notarstefano's path/cycle observability classification (first arXiv release 2011-09-16, arXiv:1109.3556v1; subsequently IEEE Transactions on Automatic Control) treats uniform path and cycle Laplacians and the gcd criteria for sensor sets. In particular a uniform cycle needs at least two sensors. The present theorem treats a different, one-parameter **nonuniform undirected cycle** and isolates both weight-independent failures and the exact positive resonant weight set for a fixed single sensor. Xiang et al. (2013) study directed/weighted heterogeneous leader-follower networks, but their explicit cycle theorem concerns a *directed* cycle under a different model. Wang et al. (2012) address generic network structural controllability after adding links, not the precise PBH eigenvector condition for a single weighted undirected link. These general papers do not imply the displayed exception formula from their inspected statements. The recurrence, perturbation arguments, and PBH criterion themselves are classical; the proposed contribution is the explicit combined classification for this natural defect-and-sensor geometry.

## Limitations

The exact theorem assumes a single altered edge and a fixed sensor one vertex in from that edge; other sensor locations have different resonances. The classification concerns binary exact observability and does not bound observability Gramian conditioning, reconstruction noise amplification, finite-horizon robustness, or optimal sensor placement. The literature comparison does not claim exhaustive worldwide coverage: a specialized weighted-cycle result not recovered in the checked sources could cover part or all of this theorem. The proof is analytic and not dependent on finite numerical tests.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (first publicly posted 2011-09-16), https://arxiv.org/abs/1109.3556 ; DOI:10.1109/TAC.2011.2168912.
2. L. Xiang, J. J. H. Zhu, F. Chen, and G. Chen, *Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics*, Mathematical Problems in Engineering (2013), DOI:10.1155/2013/405034, https://doi.org/10.1155/2013/405034.
3. W.-X. Wang, X. Ni, Y.-C. Lai, and C. Grebogi, *Optimizing controllability of complex networks by minimum structural perturbations*, Physical Review E **85**, 026115 (2012), DOI:10.1103/PhysRevE.85.026115, https://doi.org/10.1103/PhysRevE.85.026115.
