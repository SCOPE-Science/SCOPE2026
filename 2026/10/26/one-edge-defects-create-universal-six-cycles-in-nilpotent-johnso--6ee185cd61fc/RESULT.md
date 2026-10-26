# One-edge defects create universal six-cycles in nilpotent Johnson parity dynamics

## Finding
For each even integer \(n\ge4\) and each even integer \(2\le k\le n-2\), form the Johnson graph \(J(n,k)\), delete **any one edge**, and update binary vertex states synchronously by XOR of the current states at adjacent vertices. Put \(N=\binom nk\) and \(r=\binom{n-2}{k-1}\). Then the following hold.

1. Every state enters a periodic orbit after at most two updates; the entire recurrent subspace has exactly \(16\) elements, independent of \(n,k\) and of the removed edge.
2. The complete primitive-cycle census is exactly **one fixed point** (zero), **one primitive three-cycle**, and **two primitive six-cycles**. No other periods occur.
3. Let \(C_t\) be the number of initial labelled states already periodic after at most \(t\) updates (with \(C_0\) counting initially periodic states). Then
   \[
   C_0=16,\qquad C_1=2^{N-r+2},\qquad C_2=2^N.
   \]
   Consequently exactly \(C_1-16\) states enter recurrence at update 1, and exactly \(2^N-C_1\) at update 2. The maximum two-step transient is attained for \(n\ge6\); for \(n=4,k=2\), the sharp bound is one update.

In sharp contrast, the undeleted Johnson graph sends **every** configuration to zero in at most two updates. Thus deleting a single edge creates universal genuine six-periodic orbits out of a nilpotent binary update.

## Assumptions and scope
The graph is finite, simple and undirected. Its vertices are all \(k\)-element subsets of \(\{1,\ldots,n\}\), two joined when they differ in one element. All operations on configurations and adjacency matrices are over \(\mathbb F_2\). Time is counted from an arbitrary initial state at time zero; entering a cycle means that the state lies on the cycle, not merely that a future iterate does. The edge endpoints \(u,v\) are arbitrary distinct adjacent vertices. The theorem assumes both \(n\) and \(k\) even as stated and makes no claim about the other parity classes.

## Proof
Write \(V=\mathbb F_2^{\binom nk}\) with basis vectors \(e_S\) indexed by \(k\)-subsets. Let \(A\) be the original Johnson adjacency operator and let \(B=A+E\), where \(E=e_ue_v^T+e_ve_u^T\); over characteristic two this deletes the edge \(uv\).

**1. Nilpotence and exact rank of \(A\).** On the exterior algebra of \(W=\mathbb F_2^n\), identify \(V\cong\bigwedge^kW\), let \(w\) be wedging by \(e=e_1+\cdots+e_n\), and let \(\iota\) be contraction by the linear functional \(\ell(e_i)=1\). Directly on the standard wedge basis,
\[
   w\iota=A+(k\bmod2)I=A.
\]
The graded relation is \(\iota w+w\iota=\ell(e)I=(n\bmod2)I=0\). Hence \(A^2=w\iota w\iota=0\). To compute its rank, choose \(f\in W\) with \(\ell(f)=1\); since \(n\) is even, \(e\in\ker\ell\). Split \(\ker\ell=\langle e\rangle\oplus H\), where \(\dim H=n-2\). Every input splits into a wedge without \(f\) and a wedge \(f\wedge z\). The former is killed by contraction; the latter maps under \(w\iota\) to \(e\wedge z\). Therefore
\[
   \operatorname{im}A=e\wedge\bigwedge^{k-1}H,
   \qquad \operatorname{rank}A=\binom{n-2}{k-1}=r.
\]
All formulas include the boundary case \(n=4,k=2\).

**2. A four-dimensional periodic subspace.** Abbreviate \(p=e_u\), \(q=e_v\), \(a=Ap\), \(b=Aq\). Because \(u,v\) are adjacent and the adjacency matrix has zero diagonal, \(a_u=0,a_v=1,b_u=1,b_v=0\). Thus \(a,b\) are independent. If \(\alpha p+\beta q+\gamma a+\delta b=0\), application of \(A\), using \(A^2=0\), gives \(\alpha a+\beta b=0\) and hence \(\alpha=\beta=\gamma=\delta=0\). Consequently
\[
   U=\operatorname{span}_{\mathbb F_2}\{p,q,a,b\}
\]
has dimension four. The perturbed update acts on this basis as
\[
  Bp=q+a,\quad Bq=p+b,\quad Ba=p,\quad Bb=q.
\]
Thus in coordinates \((\alpha,\beta,\gamma,\delta)\),
\[
 B(\alpha,\beta,\gamma,\delta)
 =(\beta+\gamma,\alpha+\delta,\alpha,\beta),
 \quad B^3(\alpha,\beta,\gamma,\delta)
 =(\beta,\alpha,\delta,\gamma).
\]
The restriction of \(B\) to \(U\) is invertible and has \(B^6=I\). Solving \(Bx=x\) gives only the zero vector. Solving \(B^3x=x\) gives \(\alpha=\beta\) and \(\gamma=\delta\), hence exactly four such vectors. Because \(B\) is invertible on \(U\), the remaining \(12\) vectors have exact period six: among the four vectors of period dividing three, three have exact period three. Therefore \(U\) contains one fixed point, one three-cycle and two six-cycles.

**3. All periodic configurations lie in \(U\), reached within two updates.** From \(A^2=0\),
\[
 B^2=AE+EA+E^2.
\]
Every term on the right has image inside \(U\): \(AE\) maps into \(\langle a,b\rangle\), while \(EA\) and \(E^2\) map into \(\langle p,q\rangle\). Therefore \(B^2V\subseteq U\). As \(B\) is invertible on \(U\), also \(B^2U=U\); thus \(B^2V=U\). Every initial configuration reaches \(U\) after at most two updates; no periodic state can lie outside \(U\), because a periodic vector is in the image of every positive power, in particular in \(\operatorname{im}B^2=U\).

**4. Exact transient-depth populations.** Since \(A^2=0\), \(\operatorname{im}A\subseteq\ker A\). For any nonzero vector in \(\operatorname{span}\{p,q\}\), its image under \(A\) is a nonzero linear combination of independent \(a,b\); hence \(\operatorname{span}\{p,q\}\cap\operatorname{im}A=\{0\}\). Because \(A\) is symmetric, the independent coordinate functionals at \(u,v\) increase the rank of the map \(x\mapsto Ax\) by two. Equivalently, the direct-sum decomposition of \(Bx=Ax+x_vp+x_uq\) gives
\[
   \operatorname{rank}B=r+2.
\]
Since \(B\) is bijective on \(U\), the preimage \(B^{-1}(U)\) has dimension \(\dim U+\dim\ker B=4+N-r-2=N-r+2\). Thus \(C_0=|U|=16\), \(C_1=|B^{-1}U|=2^{N-r+2}\), and \(C_2=|V|=2^N\). For \(n=4,k=2\), \(r=2\), so \(C_1=2^N\); for \(n\ge6\), \(r>2\), so \(C_1<2^N\). This proves every assertion. \(\square\)

## Verification
The companion pure-Python program `johnson_edge_verify.py` independently constructs the Johnson graph and removes one actual undirected edge. It checks the exact binary rank of \(A\), nilpotence \(A^2=0\), rank of \(B\) and \(B^2\), the identity \(B^8=B^2\), the complete sixteen-state periodic subspace, and the primitive periods. It exhaustively simulates all \(64\) configurations for \(J(4,2)\setminus uv\) and all \(32{,}768\) configurations for each of \(J(6,2)\setminus uv\) and \(J(6,4)\setminus uv\), independently checking transient-depth counts. It also checks exact matrix ranks for \((n,k)=(8,2),(8,4),(8,6),(10,2),(10,4),(10,6)\) and deterministic randomized trajectories. Recorded output is `verification_output.txt`. This finite verification corroborates but does not replace the preceding proof.

## Relationship to prior work
Peeters' study of binary ranks and minimal polynomials of **unmodified** Johnson adjacency matrices supplies the closest structural antecedent; Section 4.1 includes the rank \(\binom{n-2}{k-1}\) and an order-two nilpotence constraint, but does not study the rank-two edge-deletion perturbation or periods three and six. Work on the automorphism groups of Johnson graphs and the Terwilliger algebra of Johnson incidence geometries concerns different invariants and, in the latter case, a different graph. General parity-automaton studies on regular graphs do not imply this one-edge-defect classification. The proof above is self-contained, not dependent on extrapolating numerical experiments or on novelty inferred solely from search failures.

## Limitations
The theorem concerns a single deleted edge and the specified even-even parity class. It does not classify additions, multiple deletions, other parities, noisy updates, nonlinear thresholding or physical systems. An equivalent historical characterization may exist outside the inspected literature. The graph-theoretic rank antecedent is known; only the edge-perturbed dynamics and its exact orbit/transient census are advanced as the present finding. No independent verification is asserted.

## References
- R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics **15** (2002), 127–149, DOI: 10.1023/A:1013842904024, especially Section 4.1; an earlier research memorandum dates to 1994.
- Q. Kong, B. Lv and K. Wang, *The Terwilliger algebra of the incidence graphs of Johnson geometry*, arXiv:1111.1369v1, publicly submitted 2011-11-06, https://arxiv.org/abs/1111.1369.
- A. Ganesan, *On the automorphism group of a Johnson graph*, arXiv:1412.5055v1, publicly submitted 2014-12-09, https://arxiv.org/abs/1412.5055.
- W. Fish, J. D. Key and E. Mwambene, *Codes from adjacency matrices of uniform subset graphs*, 2017, for related binary coding interpretations rather than edge-deleted orbit structure.
