# Universal two-bond-loss entanglement gain on Mersenne honeycomb graph-state tori

## Finding
Let \(k\ge3\) be an integer and \(L=2^k-1\). A periodic honeycomb graph \(H_L\) has two qubit sublattices \(A=\{A_{i,j}\}\) and \(B=\{B_{i,j}\}\), with all indices in \((\mathbb Z/L\mathbb Z)^2\). Place the three bonds
\[
A_{i,j}\!\sim\!B_{i,j},\qquad A_{i,j}\!\sim\!B_{i-1,j},\qquad A_{i,j}\!\sim\!B_{i,j-1}.
\]
On the ideal pure graph state, apply one controlled-\(Z\) gate per bond to \(|+\rangle^{\otimes 2L^2}\). For any set \(F\) of existing bonds, let \(|G_L\setminus F\rangle\) denote the graph state obtained by *omitting* those gates, and define \(S_A(F)\) as the base-two von Neumann entropy of the complete \(A\) sublattice after tracing out all of \(B\).

**Theorem.** If \(F\) contains zero or one bond, or exactly two bonds with four distinct endpoints, then
\[
\boxed{S_A(F)=L^2-L+1+|F|.}
\]
In particular the gain is universally two bits for any two endpoint-disjoint omissions. For illustration, \(L=7\) gives \(S_A(\varnothing)=43\) and \(S_A(F)=45\) for every permitted two-bond fault; \(L=15\) gives \(211\) and \(213\).

The two-bond universality is sharp in two ways. At the smaller Mersenne size \(L=3\), endpoint-disjoint two-bond deletions can have gains zero, one or two. For every permitted \(L\), the *three* mutually disjoint diagonal bonds at coordinates \((0,0),(1,0),(0,1)\) have a rank gain of at most two, so the corresponding unconditional three-bit assertion would be false.

## Assumptions and scope
There are \(2L^2\) qubits, binary controlled-\(Z\) operations, periodic coordinates, the specified three-regular bipartite honeycomb connectivity, ideal stabilizer-state preparation, and no other faults. The bipartition is all \(A\) versus all \(B\), not a spatial boundary region. The two deleted bonds must use distinct \(A\) endpoints *and* distinct \(B\) endpoints. The assertion is exact for every integer \(k\ge3\); it is not a finite-size interpolation.

## Proof
**1. Cut rank.** Let \(M\) be the \(L^2\)-by-\(L^2\) cross-adjacency matrix over \(\mathbb F_2\), with rows indexed by \(A\) and columns by \(B\). The graph-state Schmidt entropy across this cut is \(\operatorname{rank}_{\mathbb F_2}M\) bits, by the standard stabilizer cut-rank identity [1]. Identify coordinate arrays with
\[
R=\mathbb F_2[x,y]/(x^L-1,y^L-1).
\]
Up to a harmless orientation choice, \(M\) is multiplication by \(f=1+x+y\) on \(R\); the transposed map is conjugate to multiplication by \(1+x^{-1}+y^{-1}\). Therefore its cokernel is
\[
Q=R/(f)\cong\mathbb F_2[x]/\bigl(x^L-1,(1+x)^L-1\bigr).
\]
Since \(L=2^k-1\), the roots of \(x^L-1\) are precisely the nonzero elements of \(\mathbb F_{2^k}\), and they are simple because \(L\) is odd. The common roots with \((1+x)^L-1\) are exactly the elements other than zero and one. Thus the greatest common divisor of those two polynomials is
\[
g(x)=\frac{x^L-1}{x+1}=1+x+\cdots+x^{L-1},
\]
and \(\dim_{\mathbb F_2}Q=L-1\). Consequently
\[
\operatorname{rank}M=L^2-L+1.
\]
This undamaged nullity is consistent with the previously known Rule-60/Newman–Moore Mersenne configuration count [2,3]; it is not the novel portion of the theorem.

**2. Two-site rigidity of the cokernel.** Each coordinate unit vector has a nonzero image in \(Q\), since its monomial \(x^iy^j\) is invertible in \(Q\) and the quotient is nonzero. We prove that *distinct* coordinate unit vectors have distinct images. Otherwise translating by one invertible monomial produces
\[
x^uy^v=1\quad\text{in }Q
\]
for integers \(0\le u,v<L\), not both zero. Substituting \(y=1+x\) and evaluating at the nonzero, nonunit elements \(\alpha\) of \(\mathbb F_{2^k}\) implies
\[
\alpha^u(1+\alpha)^v=1\qquad
(\alpha\in\mathbb F_{2^k}\setminus\{0,1\}).
\]
The same equation with \(\alpha\mapsto1+\alpha\), divided by the original, gives
\[
\bigl(\alpha/(1+\alpha)\bigr)^{u-v}=1.
\]
This fractional linear map permutes \(\mathbb F_{2^k}\setminus\{0,1\}\), a set containing a generator of its multiplicative group of order \(L\). Hence \(u\equiv v\pmod L\), and our chosen ranges force \(u=v=t\).

Next replace \(\alpha\) by \(1/\alpha\) in the equation for \(t\), and compare the two equations: \(\alpha^{3t}=1\) for every nonzero \(\alpha\), so \(L\mid3t\). If \(3\nmid L\), necessarily \(t=0\). Otherwise a nonzero \(t\) is \(L/3\) or \(2L/3\). Because \(L\) is odd, in either case \(\bigl[\alpha(1+\alpha)\bigr]^{L/3}=1\) for every \(\alpha\ne0,1\). But the polynomial
\[
P(X)=[X(1+X)]^{L/3}-1
\]
has degree \(2L/3<L-1\) for \(L\ge7\); it cannot vanish at the \(L-1\) distinct nonzero nonunit field elements. This contradiction proves that the only possible pair is \(u=v=0\). Over \(\mathbb F_2\), two nonzero vectors are linearly dependent exactly when they are equal, so *any two distinct coordinate classes in \(Q\) are linearly independent*. The same conclusion holds for the cokernel of \(M^{\mathsf T}\), using inversion \((x,y)\mapsto(x^{-1},y^{-1})\).

**3. Effect of a matching of two deleted bonds.** For any \(F\) of size \(r=1\) or \(r=2\) satisfying the endpoint conditions, write the new binary matrix as
\[
M_F=M+UV^{\mathsf T},
\]
where the columns of \(U\) are the corresponding distinct unit vectors of the \(A\)-space and the columns of \(V\) are the distinct unit vectors of the \(B\)-space. Section 2 shows both that the columns of \(U\) are independent modulo \(\operatorname{im}M\) and that the map \(V^{\mathsf T}\!:\ker M\to\mathbb F_2^r\) is surjective: the latter is dual to the independence of the selected \(B\)-coordinate vectors modulo \(\operatorname{im}M^{\mathsf T}\).

If \(M_Fz=0\), then \(Mz+U(V^{\mathsf T}z)=0\). Projecting into \(\operatorname{coker}M\) forces \(V^{\mathsf T}z=0\), so then \(Mz=0\). Conversely these two equations imply \(M_Fz=0\). Hence
\[
\ker M_F=\ker M\cap\ker(V^{\mathsf T}),\qquad
\dim\ker M_F=(L-1)-r,
\]
and thus \(\operatorname{rank}M_F=L^2-L+1+r\), as asserted.

**4. Sharp boundaries.** At \(L=3\), the two-site classes are not distinct, and the exhaustive two-bond counts in the verification exhibit all three possible rank gains. For three diagonal bonds indexed by \((0,0),(1,0),(0,1)\), their distinct \(A\)-coordinate vectors satisfy
\[
e_{0,0}+e_{1,0}+e_{0,1}=M e_{0,0}
\]
with the stated row/column orientation. Thus the three rank-one changes span only a two-dimensional space modulo \(\operatorname{im}M\). The deleted-three-bond cut rank can increase by at most two, proving that a universal three-bit gain is impossible.

## Verification
The included standard-library Python program `verify.py` performs independent bit-packed binary-matrix ranks for the actual honeycomb adjacency and deletions, rather than using the closed formula as its computation. Its recorded output is `verification_output.txt`. It checks that all \(10{,}437\) endpoint-disjoint bond pairs for \(L=7\) gain exactly two bits; all \(297\) such pairs for \(L=3\) split into \(27\) zero-gain, \(108\) one-gain and \(162\) two-gain cases. It also tests \(200\) deterministic pairs at \(L=15\), \(30\) at \(L=31\), and distinct nonzero quotient characters at \(L=7,15,31,63\), along with independent single-edge checks. The symbolic finite-field and rank argument in the Proof, not these finite experiments, establishes all \(k\ge3\).

## Relationship to prior work
The graph-state entropy/cut-rank identity and generic bounds for edge changes are due to Hein, Eisert and Briegel [1]. For the same \(1+x+y\) Rule-60 algebra, Sfairopoulos et al. [2] and Carmona-Pírez et al. [3] give configuration and Mersenne-periodic ground-state results; in particular the known \(2^{L-1}\) kernel count subsumes the undamaged entropy baseline. Neither inspected work classifies **matching two-bond omissions and all possible endpoint positions** in a bipartite graph state's Schmidt entropy. The nontrivial extra ingredient here is the all-pairs character rigidity in step 2, which is stronger than the kernel dimension alone and yields the two-fault theorem in step 3. Orús et al. [4] study a toric-code state's *geometric entanglement* on honeycomb lattices, a different quantum state and invariant. Cullen and Kok [5] address *concentratable entanglement*; their available abstract does not establish the asserted two-bond theorem. Priority beyond the inspected sources remains subject to specialist scrutiny.

## Limitations
Only the ideal qubit graph states and the full two-color partition are treated. Two faulty bonds must have four distinct endpoints; adjacent pairs, arbitrary third defects, stochastic errors, decoherence, other graph-state families and entanglement operationally distillable under noise are not classified. The exceptional \(L=3\) result is verified exhaustively, but the positive theorem starts at \(L=7\). The calculation does not imply that removing controlled-\(Z\) gates is an LOCC operation across the partition; it is a change to the nonlocal state-preparation circuit. The undamaged rank and generic rank-change method are known; originality attaches to the new position-independent two-fault rigidity and its sharp boundary. Independent peer review and broad historical priority certification have not occurred.

## References
[1] M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, first posted 18 July 2003, arXiv:quant-ph/0307130, https://arxiv.org/abs/quant-ph/0307130.

[2] K. Sfairopoulos, L. Causer, J. F. Mair and J. P. Garrahan, *Boundary conditions dependence of the phase transition in the quantum Newman-Moore model*, arXiv:2301.02826, https://arxiv.org/abs/2301.02826.

[3] J. Carmona-Pírez, A. J. Peguero, V. Dunjko, M. Olshanii and J. Ruhl, *Rule 60 cellular automaton, Mersenne numbers, and the Newman-Moore spin lattice*, arXiv:2407.19898, https://arxiv.org/abs/2407.19898.

[4] R. Orús, T.-C. Wei, O. Buerschaper and M. Van den Nest, *Geometric entanglement in topologically ordered states*, New J. Phys. 16, 013015 (2014), https://doi.org/10.1088/1367-2630/16/1/013015.

[5] A. R. Cullen and P. Kok, *Calculating concentratable entanglement in graph states*, arXiv:2207.11997, https://arxiv.org/abs/2207.11997.
