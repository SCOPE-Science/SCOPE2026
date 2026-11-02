# Paired omitted-bond cancellation in three-dimensional toroidal cluster states

## Finding

For every integer \(a\ge3\), let \(L=2^a\) and let \(G=C_4\square C_4\square C_L\). Prepare the ideal \(16L\)-qubit graph state and partition its vertices by checkerboard parity. Its bipartite entanglement entropy in bits, and every positive-order Rényi entropy, equals
\[
S_0=8L-16.
\]
Choose **any** edge \(e\) in either of the two length-four coordinate directions, and let \(e'\) be its translate by four steps along the length-\(L\) direction. The two edges have disjoint endpoints. If \(S(F)\) denotes the checkerboard entanglement after omitting the controlled-\(Z\) gates on edges in \(F\), then
\[
\boxed{S(\{e\})=S(\{e'\})=S_0+1,\qquad S(\{e,e'\})=S_0.}
\]
In fact all nonzero Schmidt probabilities are equal for each of these graph states. Thus either missing bond alone *increases* entanglement by a bit, but the two correlated missing bonds together return it **exactly** to its original value. The cancellation is valid for all allowed circumferences and for every location and orientation of such a bond.

## Assumptions and scope

All three cycles are simple, unweighted, periodic cycles, and \(L\) is a power of two at least eight. The two omitted bonds are related by translation by four sites in the longest direction, and are parallel to one of the length-four directions. The measured invariant is the entropy across the fixed even/odd checkerboard cut of an ideal pure *qubit graph state*, not maximum Schmidt measure or an energy spectrum. The adjacency and rank computations below take place over \(\mathbb F_2\), not over the real numbers.

## Proof

**Binary graph-state reduction.** For any bipartite simple graph with off-diagonal binary adjacency block \(B\), its pure graph-state checkerboard entanglement is \(\operatorname{rank}_{\mathbb F_2}B\): the phase-matrix character orthogonality gives exactly \(2^{\operatorname{rank}B}\) equal nonzero Schmidt weights. Removing one cross-partition edge toggles its single \(1\) entry in \(B\).

**Base rank and nontrivial kernels.** Write \(M\) for the full binary adjacency matrix and \(T_i\) for translation by one unit in coordinate \(i\). Then \(M=\sum_{i=1}^3(T_i+T_i^{-1})\). In the truncated group algebra \(\mathbb F_2[u_1,u_2,u_3]/(u_1^4,u_2^4,u_3^L)\), with \(u_i=T_i+I\), the summand in coordinate \(i\) is multiplication by \(u_i^2/(1+u_i)\). Each summand is similar, by the nullities of its powers, to multiplication by \(u_i^2\). A tensor-product similarity transforms \(M\) to multiplication by \((u_1+u_2+u_3)^2\). Since \(L\) is a power of two, replacing \(u_3\) by \(z=u_1+u_2+u_3\) is a ring automorphism, and multiplication by \(z^2\) consists of \(32\) Jordan blocks of length \(L/2\). Consequently \(\operatorname{rank}M=16L-32\), and the checkerboard block has rank \(r=8L-16\). Both \(B\) and \(B^{\mathsf T}\) have kernel dimension \(16\).

**Each isolated edge raises the rank by one.** Even translations act transitively on each checkerboard color class. Since \(\ker B\) and \(\ker B^{\mathsf T}\) are nonzero and are translation-invariant, some vector in each kernel has entry one at *every specified* coordinate after a suitable translation. Therefore the coordinate vector of any even site lies outside \(\operatorname{im} B\), and the coordinate vector of any odd site lies outside \(\operatorname{im}B^{\mathsf T}\). Toggling an even–odd edge adds a rank-one matrix \(p q^{\mathsf T}\) whose left and right vectors are both outside the respective images. Elementary row and column reductions show that its rank is \(r+1\). This applies to \(e\) and \(e'\).

**Paired-edge cancellation.** Regard \(p,p'\) as the even endpoint basis vectors and \(q,q'\) as the odd endpoint basis vectors, where \(p'=Tp\) and \(q'=Tq\) for translation \(T=T_3^4\). Since \(T_1^4=T_2^4=I\), in characteristic two
\[
M^2=T_3^2+T_3^{-2},\qquad T+I=M^2T_3^2.
\]
Define the odd-vector \(c=MT_3^2p\) and even-vector \(b=MT_3^2q\). The displayed identity yields
\[
Bc=p+p',\qquad B^{\mathsf T}b=q+q'.
\]
Three scalar products vanish:
\[
b^{\mathsf T}p=0,\qquad (q')^{\mathsf T}c=0,\qquad b^{\mathsf T}Bc=q^{\mathsf T}M^3p=0.
\]
For the first two, a nearest-neighbor step cannot connect an original endpoint at layer \(z\) to a vertex at layer \(z+2\) when \(L\ge8\). For the last, \(M^3=M(T_3^2+T_3^{-2})\), and neither two-step vertical translate of \(p\) is adjacent to \(q\), because the chosen edge runs in a length-four direction. These arguments are independent of its location and the sign of its short-direction orientation.

Let \(B'\) be the cross-adjacency block after deleting both edges. Addition and deletion are identical over \(\mathbb F_2\), so
\[
\begin{aligned}
B'&=B+pq^{\mathsf T}+p'(q')^{\mathsf T}\\
&=B+p(q+q')^{\mathsf T}+(p+p')(q')^{\mathsf T}\\
&=B+p b^{\mathsf T}B+Bc(q')^{\mathsf T}\\
&=(I+p b^{\mathsf T})\,B\,(I+c(q')^{\mathsf T}).
\end{aligned}
\]
The final factorization uses \(b^{\mathsf T}Bc=0\). Its left and right factors are **invertible rank-one shears**: since \(b^{\mathsf T}p=(q')^{\mathsf T}c=0\), each is its own inverse in characteristic two. Hence \(\operatorname{rank}B'=\operatorname{rank}B=r\), proving the paired-bond equality. The earlier rank-one argument proves the two isolated-bond equalities. All statements follow for every \(a\ge3\).

## Verification

The standalone standard-library \(checker.py\) directly constructs the finite checkerboard adjacency block, toggles actual bond entries, and performs exact bit-vector elimination over \(\mathbb F_2\). It verifies \(L=8,16,32\), all even base layers and both signs of bonds in both short directions: \(112\) geometrically distinct bond pairs, \(339\) exact rank comparisons including base ranks. Each single deletion increases the rank by one, and each paired deletion returns it to baseline. The recorded output is in \(verification_output.txt\). These examples do not substitute for the all-parameter proof above.

## Relationship to prior work

The graph-state cross-adjacency rank criterion is due to Hein, Eisert and Briegel, and the 2006 graph-state review develops its entanglement consequences. Earlier general modular Jordan theory by Norman and later Barry describes Kronecker sums and products; that theory is background for the base-rank calculation, **not** the novelty claimed here. Vadali and Turner's multidimensional parity-automaton study likewise treats unperturbed nearest-neighbor binary dynamics. Existing two-dimensional checkerboard formulas and single-bond effects are not claimed as new. The specific result assessed as new is the exact two-*correlated*-bond cancellation under a nontrivial long-direction translation, established here by explicit invertible shears rather than by generic Jordan-block enumeration.

## Limitations

The cancellation concerns the specified family \(C_4\square C_4\square C_{2^a}\), ideal graph states and two specifically correlated omitted bonds. It does not classify all pairs of missing edges, arbitrary three-dimensional periodic dimensions, noise, quantum Hamiltonian dynamics or entropy across other partitions. Other omitted-bond placements can instead increase entanglement by one or two bits. The theorem is a mathematical claim with same-author verification only; historical priority requires independent scrutiny.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (2003-07-18), https://arxiv.org/abs/quant-ph/0307130.
2. M. Hein et al., *Entanglement in Graph States and its Applications*, arXiv:quant-ph/0602096 (2006-02-11), https://arxiv.org/abs/quant-ph/0602096.
3. C. W. Norman, *On Jordan bases for the tensor product and Kronecker sum and their elementary divisors over fields of prime characteristic*, Linear and Multilinear Algebra 56 (2008), DOI 10.1080/03081080701395640.
4. M. J. J. Barry, *A New Algorithm for Decomposing Modular Tensor Products*, Bull. Austral. Math. Soc. 104 (2021), https://doi.org/10.1017/S0004972720001379.
5. A. Vadali and A. Turner, *Cycle-lengths of Multi-Dimensional σ Automata*, arXiv:2502.10898 (2025-02-15), https://arxiv.org/abs/2502.10898.
