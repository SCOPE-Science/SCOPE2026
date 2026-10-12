# The unique invariant two-graph measure has the graphic matroid as its dependence matroid
## Finding
For the universal homogeneous parity \(3\)-hypergraph \(\mathcal G_3\), let \(\mu\) be the unique invariant Keisler measure in one variable. With distinct parameters \(a_1,\ldots,a_n\), define \(X_{ij}(d)=\mathbf 1[R(d,a_i,a_j)]\). Then \((X_{ij})\) is uniform on an affine translate of the binary cut space of \(K_n\). Hence for \(F\subseteq E(K_n)\), if \(H=([n],F)\) has \(c(H)\) components, the marginal on \(F\) has affine dimension and Shannon entropy exactly \(n-c(H)\). The variables indexed by \(F\) are jointly independent fair bits exactly when \(H\) is a forest; equivalently their dependence matroid is \(M(K_n)\).

For every cycle \(C=(v_1,\ldots,v_m,v_1)\), the unique cycle dependence is
\[
\bigoplus_{r=1}^{m}X_{v_rv_{r+1}}=
\bigoplus_{r=2}^{m-1}R(a_{v_1},a_{v_r},a_{v_{r+1}}),
\]
where \(v_{m+1}=v_1\).
## Assumptions and scope
The parameters are pairwise distinct and \(n\ge2\). Only singleton-variable pair-incidence coordinates are classified. The measure is the unique invariant measure of Braunfeld--Jahel--Marimon.
## Proof
Choose a graphing \(g\) of the induced two-graph on the parameters. If \(t_i\in\mathbb F_2\) records the graphing edge from a new point \(d\) to \(a_i\), then the two-graph parity rule gives
\[
X_{ij}=g_{ij}+t_i+t_j\pmod2.
\]
The kernel of \(t\mapsto(t_i+t_j)_{i<j}\) is the two-element space of constant vectors, so the complete incidence patterns form an affine cut space of dimension \(n-1\). Braunfeld--Jahel--Marimon, Corollary 5.4, gives mass \(2^{-(n-1)}\) to every complete type over \(n\) distinct parameters, hence this affine space is sampled uniformly.

Restricting to \(F\) gives the binary incidence map of \(H=([n],F)\). Its kernel consists of vectors constant on each connected component, so its rank is \(n-c(H)\). Thus the marginal is uniform on an affine subspace of that dimension. Full independence holds exactly when \(|F|=n-c(H)\), which is exactly the forest criterion. Summing the displayed edge formula around a cycle cancels every \(t_i\), and triangulating from \(v_1\) gives the intrinsic cycle-parity formula above.
## Verification
`verify.py` checks the parity equations, support size, two-to-one graphing parametrization, and binary incidence-rank formula through \(n=7\), returning `VERIFY_OK 8448 exact assertions`.
## Relationship to prior work
Braunfeld--Jahel--Marimon prove uniqueness and equal complete-type masses for universal homogeneous parity hypergraphs. Their Remark 5.6 gives the triangle dependence and explicitly notes that more complex intersections remain to be understood. The theorem here supplies the full finite dependence calculus for the parity \(3\)-hypergraph. Classical two-graph theory identifies two-graphs with Seidel switching classes, supplying the graphing representation but not this invariant-measure dependence law.
## Limitations
The result does not classify laws with several new variables or parity \(k\)-hypergraphs for \(k>3\). The graphic-matroid synthesis was not found in the checked literature, but it is a short consequence of the source theorem plus standard switching linear algebra, so uncatalogued folklore remains a residual originality risk.
## References
1. Samuel Braunfeld, Colin Jahel, Paolo Marimon, *When invariance implies exchangeability (and applications to invariant Keisler measures)*, arXiv:2408.08370, first submitted 2024-08-15; Corollary 5.4 and Remark 5.6.
2. C. L. Mallows and N. J. A. Sloane, *Two-Graphs, Switching Classes and Euler Graphs are Equal in Number*, SIAM J. Appl. Math. 28 (1975), 876--880, DOI:10.1137/0128070.
