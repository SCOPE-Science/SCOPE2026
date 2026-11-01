# Adjacency-fractured Jordan dynamics of doubly punctured Boolean hypercubes

## Finding

For every integer \(d\ge2\), delete any two distinct vertices \(u,v\) from the ordinary \(d\)-dimensional Boolean hypercube \(Q_d\), and let \(h\in\{1,\ldots,d\}\) be their Hamming distance. Let \(B\) be the adjacency matrix of the remaining induced graph, acting by synchronous neighbor-sum on \(\mathbb F_q^{2^d-2}\), where \(q\) is any power of two. Write \(N=2^d\); \(J_s(\lambda)\) denotes the \(s\)-by-\(s\) Jordan block with eigenvalue \(\lambda\). The **complete similarity classification**, depending only on the dimension parity and whether the two removed vertices are adjacent, is

\[
B\sim\begin{cases}
J_2(1)\oplus J_2(0)^{\oplus(N/2-2)}, & d\text{ even},\ h=1,\\
J_3(0)^{\oplus2}\oplus J_2(0)^{\oplus(N/2-4)}, & d\ge4\text{ even},\ h\ge2,\\
J_1(0)^{\oplus2}, &d=2,\ h=2,\\
J_4(1)\oplus J_2(1)^{\oplus(N/2-3)}, &d\text{ odd},\ h=1,\\
J_1(0)^{\oplus2}\oplus J_2(1)^{\oplus(N/2-2)}, &d\text{ odd},\ h\ge2.
\end{cases}
\]

A zero exponent means that the corresponding direct summand is absent. In particular, the **dimension-parity/adjacency transition** is sharp. For even dimensions, adjacent deletions produce a two-dimensional recurrent two-periodic factor, whereas all nonadjacent deletions eventually extinguish every state. For odd dimensions, adjacent deletions make the entire system reversible and create primitive four-cycles, whereas nonadjacent deletions have only fixed points/two-cycles and one-step transients.

The Jordan forms yield exact entry-time and primitive-period populations for every field size \(q\). Write \(M_{t,p}\) for the number of labelled configurations whose first periodic entry is exactly after \(t\) updates and whose eventual primitive period is \(p\). Then:

* If \(d\) is even and \(h=1\), put \(m=N/2-2\) and \(L_0=1\), \(L_1=q^m-1\), \(L_2=q^{2m}-q^m\). The only nonzero entries are \(M_{t,1}=qL_t\) and \(M_{t,2}=(q^2-q)L_t\) for \(0\le t\le2\).
* If \(d\ge4\) is even and \(h\ge2\), every state eventually reaches zero, and \((M_{0,1},M_{1,1},M_{2,1},M_{3,1})=(1,q^{N/2-2}-1,q^{N-4}-q^{N/2-2},q^{N-2}-q^{N-4})\).
* If \(d=2\) and \(h=2\), \((M_{0,1},M_{1,1})=(1,q^2-1)\).
* If \(d\) is odd and \(h=1\), every state is immediately periodic, and \((M_{0,1},M_{0,2},M_{0,4})=(q^{N/2-2},q^{N-4}-q^{N/2-2},q^{N-2}-q^{N-4})\).
* If \(d\) is odd and \(h\ge2\), put \(H_1=q^{N/2-2}\), \(H_2=q^{N-4}-H_1\). The only nonzero entries are \(M_{0,p}=H_p\) and \(M_{1,p}=(q^2-1)H_p\) for \(p\in\{1,2\}\).

Primitive orbit counts are \(M_{0,p}/p\), and the formulas above enumerate all configurations by first-entry time and eventual primitive period. (For the even-adjacent case, primitive orbit counts use its recurrent factor: \(q\) fixed points and \((q^2-q)/2\) distinct two-cycles.)

## Assumptions and scope

All graphs are ordinary simple undirected hypercubes: vertices are binary words of length \(d\), adjacent iff the words differ in exactly one coordinate. The two vertices are removed with their incident edges, not identified, and no self-loops are added. Field characteristic is exactly two; \(q=2^f\) with arbitrary positive integer \(f\). The update is linear and synchronous, with no additive forcing and no self-feedback. The time \(t=0\) means that the initial vector is already on a periodic orbit. Hamming distance is the only relevant orbit-of-pairs invariant under hypercube graph automorphisms.

## Proof

**1. Cube involution and its half-rank square-zero part.** Let \(A\) be the full cube adjacency matrix and \(\delta=d\pmod2\), viewed inside the ground field. Because distinct coordinates commute and pairs of unequal flips occur twice,
\[
A^2=\delta I_N.
\]
Consequently \(C=A+\delta I_N\) satisfies \(C^2=0\). On splitting the hypercube along any coordinate, its block form is
\[
C=\begin{pmatrix}D+\delta I&I\\I&D+\delta I\end{pmatrix},
\]
where \(D\) is the \((d-1)\)-cube adjacency. Since \((D+\delta I)^2=I\), the kernel is \(\{(x,(D+\delta I)x):x\in\mathbb F_q^{N/2}\}\). Thus
\[
\operatorname{rank}C=N/2,\qquad \ker C=\operatorname{im}C=:K.
\]
Symmetry gives \(K^\perp=K\) for the standard nondegenerate coordinate bilinear form.

**2. Rank of the two-deletion compression.** Let \(E=\operatorname{span}(e_u,e_v)\), \(T\) its complementary coordinate subspace, and \(P\) coordinate restriction to \(T\). For \(d\ge3\), the two columns \(Ce_u,Ce_v\) are linearly independent: their supports are distinct cube (possibly self-augmented) neighborhoods, and neither is zero. The same holds at \(d=2,h=1\). Hence \(E\cap K=\{0\}\). Since \(K^\perp=K\), the coordinate projection \(K\to E\) is surjective: otherwise a nonzero vector in \(E\) would annihilate \(K\) and belong to \(E\cap K\). It follows that \(C(T)=C(\mathbb F_q^N)=K\). Since the restriction \(P:K\to T\) is injective, the compressed matrix \(PCP^T\) has rank exactly \(N/2\). Accordingly,
\[
\operatorname{rank}(B+\delta I_{N-2})=N/2
\]
for every case except \(d=2,h=2\). In that exceptional case the two surviving vertices have distance two and \(B=0_2\).

**3. Rank-two feedback.** Let \(a=P A e_u\), \(b=P A e_v\) be the two deleted-vertex neighbor columns, and put \(e=1\) when \(h=1\), otherwise \(e=0\). The compression of \(A^2=\delta I\) gives the exact matrix identity
\[
B^2=\delta I_{N-2}+R,\qquad R=aa^T+bb^T.
\]
For all cases outside \(d=2,h=2\), \(a,b\) are independent and \(\operatorname{rank}R=2\). Their Gram matrix is
\[
\begin{pmatrix}a^Ta&a^Tb\\b^Ta&b^Tb\end{pmatrix}
=(\delta+e)I_2.
\]
Indeed, each truncated neighborhood has \(d-e\) members, and any two different cube vertices have either zero or two common neighbors; both counts reduce modulo two as asserted. The additional identities
\[
Ba=eb,\qquad Bb=ea
\]
follow directly by truncating the columns of \(A^2=\delta I_N\). Consequently \(R^2=(\delta+e)R\), with all ranks and exponents determined by \(\delta,e\).

**4. Resolve each of the four regimes.** If \(\delta=0,e=1\), then \(R^2=R\), and \(B\) swaps \(a,b\) on \(\operatorname{im}R\), giving \(J_2(1)\) in characteristic two; on \(\ker R\), \(B^2=0\). The rank from Step 2 gives precisely \(N/2-2\) remaining blocks \(J_2(0)\).

If \(\delta=0,e=0\), then \(R^2=0\), \(Ba=Bb=0\), so \(B^3=0\) and \(\operatorname{rank}B^2=2\). Thus two \(J_3(0)\) blocks occur and, using \(\operatorname{rank}B=N/2\), every remaining block is \(J_2(0)\). This requires \(d\ge4\), with the smaller exceptional case already resolved.

If \(\delta=1,e=1\), then \(R^2=0\) and \((B+I)^2=R\). As \((B+I)a=(B+I)b=a+b\), the image of \((B+I)^3\) has dimension one, and its fourth power vanishes. Therefore exactly one block is \(J_4(1)\); the rank from Step 2 gives the remaining \(J_2(1)\) blocks.

If \(\delta=1,e=0\), then \(R^2=R\). On \(\operatorname{im}R=\operatorname{span}(a,b)\), the matrix \(B\) is zero, producing \(J_1(0)^{\oplus2}\); on \(\ker R\), \((B+I)^2=0\). The rank of \(B+I\) forces all remaining blocks to have size exactly two and eigenvalue one. This exhausts the total dimension in every case.

**5. Counts and orbit lengths.** A zero-eigenvalue block \(J_s(0)\) has \(q^{\min(t,s)}\) points in the kernel of its \(t\)-th power; entry-time strata are differences between consecutive such totals. A \(J_2(1)\) block in characteristic two has periods one and two; a \(J_4(1)\) block has periods one, two and four. Product decomposition into nilpotent and invertible generalized eigenspaces makes the entry-time and eventual-period counts independent. Subtract fixed-point populations \(\#\operatorname{Fix}(B^p)\) for increasing powers of two to recover the primitive-period populations, yielding every formula in the Finding. No finite enumeration is used as a substitute for the arbitrary-dimensional rank/Jordan proof.

## Verification

The included `verify_twopuncture.py` independently constructs each induced-graph adjacency matrix over \(\mathbb F_2\), multiplies bitset matrices, and checks the nullities of its first five powers and those of its one-shift against the proposed Jordan forms for all dimension/distance pairs with \(2\le d\le8\). It additionally enumerates every initial state for \(2\le d\le4\) by direct vertexwise propagation and compares its first periodic-entry time and primitive period with the symbolic formulas. Recorded run: `TWO_PUNCTURE_JORDAN_ALL_CHECKS_PASSED`; 35 dimension-distance pairs, 3,514 matrix vertices summed across cases, and 65,736 full state histories. Finite checks corroborate, but do not replace, the proof for all dimensions and characteristic-two fields.

## Relationship to prior work

Dalfó, van Dam and Fiol studied real spectra under closely related graph perturbations; their real-spectral cospectrality statements do not specify the characteristic-two elementary divisors or dynamical orbit populations. Kim, Reiner and Schoenzeit studied real adjacency spectra of singly and antipodally punctured hypercubes; reduction of real spectral data does not recover Jordan blocks over characteristic two. Sutner's additive-cellular-automaton decomposition supplies the broader linear-dynamics perspective; the opening sections inspected do not give this two-defect classification. The present theorem concerns adjacency (not graph Laplacian) dynamics for all pairs of deleted vertices, all dimension parities and every characteristic-two finite field.

## Limitations

The result is restricted to synchronous linear neighbor-sum updates in characteristic two and exactly two deleted vertices of the ordinary cube. It does not classify real adjacency spectra, characteristic-odd dynamics, arbitrary vertex subsets, or nonlinear threshold rules. Full historical originality cannot be guaranteed by searches: an unindexed equivalence may exist, particularly in the characteristic-two graph-module literature. All numerical evidence is finite; the general statement relies on the five-step algebraic proof.

## References

1. C. Dalfó, E. R. van Dam, M. A. Fiol, *On Perturbations of Almost Distance-Regular Graphs*, arXiv:1202.3313, first arXiv version dated 2012-02-15 (following an earlier 2011 journal appearance). https://arxiv.org/abs/1202.3313
2. J. Kim, V. Reiner, D. Schoenzeit, *Note on adjacency spectra for twice punctured hypercubes*, arXiv:2608.27887 (2026). https://arxiv.org/abs/2608.27887
3. K. Sutner, *Decomposition of Additive Cellular Automata*, Complex Systems 13 (2001), 245–270. https://content.wolfram.com/sites/13/2018/02/13-3-4.pdf
4. P. Caballero-Gil et al., *Linear Cellular Automata as Discrete Models for Generating Cryptographic Sequences*, arXiv:1005.0086 (2010). https://arxiv.org/abs/1005.0086
