# Graph-diameter lower bounds for ambient Clifford fourth-moment designs
## Finding
Let \(G=(V,E)\) be a connected interaction graph on \(n\) qubits. A depth-\(L\) graph-local circuit is a product of \(L\) layers, each layer consisting of pairwise-disjoint two-qubit unitaries acting on edges of \(G\). The gates themselves need not be Clifford. For \(v\in V\), let \(B_G(v,L)\) be the radius-\(L\) graph ball and define
\[
b_G(L)=\min_{v\in V}|B_G(v,L)|.
\]
For every probability ensemble \(\mathcal E_L\) of such circuits,
\[
\left\|\Phi_{\mathcal E_L}^{(4)}-\Phi_{\mu_{\mathrm{Cl}_n}}^{(4)}\right\|_\diamond
\ge
1-\frac{4^{b_G(L)}-1}{4^n-1}.
\]
In fact, for every fixed vertex \(v\),
\[
\left\|\Phi_{\mathcal E_L}^{(4)}-\Phi_{\mu_{\mathrm{Cl}_n}}^{(4)}\right\|_\diamond
\ge
1-\frac{4^{|B_G(v,L)|}-1}{4^n-1}.
\]
Therefore an \(\varepsilon\)-approximate Clifford 4-design in this diamond-norm sense must satisfy
\[
b_G(L)\ge
\left\lceil
\log_4\!\left(1+(1-\varepsilon)(4^n-1)\right)
\right\rceil.
\]
For every \(\varepsilon<3/4\), the right-hand side equals \(n\). Hence every radius-\(L\) ball must contain all vertices and
\[
L\ge \operatorname{diam}(G).
\]
Thus the source's one-dimensional lower bound is the path-graph case of an exact architecture-sensitive obstruction. For example, the depth lower bound is at least \(n-1\) on a path, at least \(\lfloor n/2\rfloor\) on a cycle, and at least the graph diameter on any other connected architecture.

## Assumptions and scope
The target moment is the Haar fourth moment of the \(n\)-qubit Clifford group. The approximation metric is the diamond norm between fourth-moment channels. The circuit model uses only two-qubit gates on graph edges, organized into pairwise-disjoint parallel layers; gates may be arbitrary ambient unitaries. No ancillas are needed for the theorem, and no statement is made for ancilla buses whose interactions are not represented in \(G\), intermediate measurements, feed-forward, non-edge interactions, or other circuit models.

The graph is finite and connected. The exact ball-volume inequality is valid for every integer \(L\ge0\). The diameter corollary uses the strict error condition \(\varepsilon<3/4\). No claim is made that the diameter lower bound is tight for general graphs, nor that the same formula holds for the Haar measure on the full unitary group or for lower Clifford moments.

## Proof
Fix \(v\in V\) and put \(S=B_G(v,L)\), with \(s=|S|\). Under a single graph-local layer, the Heisenberg support of any operator can expand by at most one graph edge. Induction over the \(L\) layers therefore gives
\[
\operatorname{supp}(U Z_v U^\dagger)\subseteq S
\]
for every circuit \(U\) in the ensemble.

West, Cerezo, and Larocca use the fourth-order Clifford commutant projector
\[
Q_n=4^{-n}\sum_{P\in\mathcal P_n}P^{\otimes4}.
\]
For an arbitrary spatial bipartition \(V=S\sqcup S^c\), Pauli factorization gives
\[
Q_n=Q_S\otimes Q_{S^c}.
\]
Take the same probe as in their Clifford argument, now centered at \(v\):
\[
A=Z_v\otimes I^{\otimes3}.
\]
Let
\[
\Pi_S=I_S^{\otimes4}\otimes Q_{S^c}.
\]
Because \(U Z_vU^\dagger\) is supported on \(S\), the conjugated range of \(Q_n\) produced by the probe lies inside the range of \(\Pi_S\). This is exactly the projector hypothesis of the source's invariant-projector diamond-distance theorem.

It remains to evaluate the target acceptance probability. A uniformly random Clifford conjugates \(Z_v\) uniformly over the \(4^n-1\) nonidentity Pauli classes. If the resulting Pauli is supported entirely in \(S\), then \(\Pi_S\) accepts with probability one. If it has a nonidentity component on \(S^c\), choose a Pauli on \(S^c\) that anticommutes with that component. The same anticommutation cancellation used in the source's Eq. (34) shows that the acceptance probability is zero. Exactly \(4^s-1\) nonidentity Pauli classes are supported entirely in \(S\). Hence the target acceptance probability is
\[
\frac{4^s-1}{4^n-1}.
\]
The source theorem therefore yields
\[
\left\|\Phi_{\mathcal E_L}^{(4)}-\Phi_{\mu_{\mathrm{Cl}_n}}^{(4)}\right\|_\diamond
\ge 1-\frac{4^s-1}{4^n-1}.
\]
Since this holds for every \(v\), choosing a vertex with minimum ball size proves the first displayed bound.

If the diamond distance is at most \(\varepsilon\), rearrangement gives
\[
4^{b_G(L)}\ge 1+(1-\varepsilon)(4^n-1),
\]
which yields the logarithmic lower bound. When \(\varepsilon<3/4\),
\[
1+(1-\varepsilon)(4^n-1)>4^{n-1},
\]
so the integer \(b_G(L)\) must equal \(n\). Thus every vertex sees all of \(V\) within graph distance \(L\), implying \(L\ge\operatorname{diam}(G)\).

## Verification
The proof is analytic for all finite connected graphs. The packaged checker verifies the algebraic inversion of the diamond-distance bound, the \(3/4\) integer threshold, the path specialization \(|B(v,L)|=L+1\) at an endpoint, and representative path, cycle, grid, star, and complete-graph ball calculations. These finite checks are sanity checks only and are not used as a proof of the general statement.

## Relationship to prior work
West, Cerezo, and Larocca prove the invariant-projector diamond-distance theorem used above and specialize it to depth-\(L\) nearest-neighbor circuits on a one-dimensional line. Their Clifford Corollary 3 obtains
\[
1-\frac{4^{L+1}-1}{4^n-1}
\]
by probing an endpoint Pauli whose one-dimensional lightcone contains at most \(L+1\) qubits. Their paper states its circuit no-go results for local nearest-neighbor one-dimensional circuits and does not state the arbitrary-interaction-graph ball-volume or diameter formulation proved here.

Mittal and Hunter-Jones study local random quantum circuits on arbitrary connected architectures, but their target is Haar measure on the full unitary group rather than the Clifford-group fourth moment. Their architecture-general design upper bounds therefore do not imply the present Clifford-specific obstruction. Earlier subgroup-restricted shallow-design lower bounds cited by West, Cerezo, and Larocca likewise treat one-dimensional locality rather than the graph-ball formula above.

## Limitations
The result concerns the fourth Clifford moment only. It does not prove optimal construction depth on a general graph, does not address errors \(\varepsilon\ge3/4\) beyond the exact ball-volume inequality, and does not incorporate communication resources outside the specified interaction graph. A stronger lower bound may follow from more detailed graph structure than radius-\(L\) ball cardinality; no such strengthening is claimed here.

## References
1. Maxwell West, M. Cerezo, and Martin Larocca, "Ambient unitaries don't enable shallow group designs," arXiv:2608.13528v1, first public 2026-08-13. See Theorem 1 and Clifford Corollary 3, especially Eqs. (28)--(35).
2. Shivan Mittal and Nicholas Hunter-Jones, "Local random quantum circuits form approximate designs on arbitrary architectures," arXiv:2310.19355.
