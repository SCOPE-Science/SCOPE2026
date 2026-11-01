# A missing-edge parity transition in hypercube XOR dynamics

## Finding

Let \(Q_d\) be the graph on the binary words of length \(d\), with edges joining words at Hamming distance one. Delete **one** graph edge and perform synchronous neighbor-sum updates over any finite field \(\mathbb F_q\) with \(q\) a power of two. Set \(n=2^d\) and \(m=2^{d-1}\). For \(d\ge2\), the resulting linear update \(B_d\) has the following complete dynamical classification, independent of the deleted edge.

When \(d\) is even, its rational canonical/Jordan decomposition is
\[
 B_d\sim C\big((X^2+X+1)^2\big)\oplus J_2(0)^{\oplus(m-2)},
\]
where \(C(g)\) is the four-dimensional companion matrix of the monic polynomial \(g\). Its periodic states have primitive periods exactly \(1,3,6\). The numbers of distinct primitive cycles are
\[
 C_1=1,\qquad C_3=\frac{q^2-1}{3},\qquad C_6=\frac{q^4-q^2}{6}.
\]
For the first time \(T(x)\) that the orbit of \(x\) enters its eventual periodic cycle, the exact populations are
\[
 \#\{T=0\}=q^4,\quad
 \#\{T=1\}=q^{m+2}-q^4,\quad
 \#\{T=2\}=q^n-q^{m+2}.
\]
No larger \(T\) occurs. The case \(d=2\) is reversible, so its two positive-time shells are empty; for even \(d\ge4\) the maximum \(T\) equals two.

When \(d\) is odd (hence \(d\ge3\)), the decomposition is
\[
 B_d\sim J_1(0)^{\oplus2}\oplus J_4(1)\oplus J_2(1)^{\oplus(m-3)}.
\]
The eventual primitive periods are exactly \(1,2,4\), and their numbers of distinct cycles are
\[
 C_1=q^{m-2},\qquad
 C_2=\frac{q^{n-4}-q^{m-2}}2,\qquad
 C_4=\frac{q^{n-2}-q^{n-4}}4.
\]
Every state is periodic initially or after **one** update, with
\[
 \#\{T=0\}=q^{n-2},\qquad
 \#\{T=1\}=q^n-q^{n-2}.
\]
In particular, uniformly random initial conditions have \(\Pr(T=1)=1-q^{-2}\), independent of odd dimension.

## Assumptions and scope

The states form the vector space \(V=\mathbb F_q^{2^d}\), and time is discrete and synchronous. There are no self-loops, and exactly one ordinary graph edge is deleted. Choose its endpoints \(u,v\) and identify them with standard basis vectors of \(V\). If \(A\) is the original hypercube adjacency matrix, then deletion in characteristic two gives \(B=A+uv^{\mathsf T}+vu^{\mathsf T}\). The graph automorphism group is edge-transitive, so the same classification holds for every edge. The term *periodic* includes a fixed point; \(T=0\) means periodic from the initial state. The displayed cycle counts are counts of distinct orbits, not populations of states.

The finite-field extensions are covered because every rank identity and invariant-subspace calculation below holds over any field of characteristic two. The rational canonical companion notation remains valid even if its quadratic factor splits over the particular field.

## Proof

**The unperturbed operator.** Write \(A=S_1+\cdots+S_d\), with \(S_j\) the commuting involution that flips coordinate \(j\). Squaring in characteristic two yields \(A^2=\delta I\), where \(\delta=d\bmod2\). If \(d\) is even, \(A\) is square-zero; if odd, \(N=A+I\) is square-zero. In either case the indicated square-zero operator has rank exactly \(m\): split off the first coordinate, obtaining the block matrix \(\begin{psmallmatrix}H&I\\I&H\end{psmallmatrix}\) with \(H^2=I\). Its kernel consists exactly of pairs \((x,Hx)\), giving nullity \(m\).

**A four-dimensional local module.** Put \(p=Au\), \(r=Av\). Because the endpoints are adjacent, \(u,v,p,r\) are linearly independent for \(d\ge2\): each endpoint has another neighbor appearing exclusively in its own neighbor-indicator vector. Let \(W=\operatorname{span}\{u,v,p,r\}\). The hypercube has no triangles, so its endpoints have no common neighbor. Directly from the update,
\[
 Bu=v+p,\qquad Bv=u+r,\qquad Bp=(1+\delta)u,\qquad Br=(1+\delta)v.
\]
Consequently \(W\) is invariant under \(B\). Because \(B-A\) has image inside \(W\), the induced map on \(V/W\) is the one induced by \(A\).

**Even dimensions.** For \(\delta=0\), the above four equations show that \(B|_W\) is invertible, has characteristic polynomial \((X^2+X+1)^2\), and its third power swaps \(u\leftrightarrow v\) and \(p\leftrightarrow r\). Thus \((B|_W)^6=I\), whereas \((B|_W)^3\ne I\) and \(\ker(B|_W+I)=0\). Its minimal polynomial is \((X^2+X+1)^2\), giving the stated single companion block. Because \(\operatorname{Im}A=\ker A\) has dimension \(m\), and \(W\cap\ker A=\operatorname{span}\{p,r\}\), the induced map on \(V/W\) has rank \(m-2\) and square zero. Since \(B(W)=W\), it follows that \(\operatorname{rank}B=m+2\) and \(\operatorname{Im}B^2=W\), of rank four. Hence the complementary nilpotent component has dimension \(n-4\), rank \(m-2\), and square zero. All of its \(m-2\) Jordan blocks therefore have length two. The fixed spaces inside \(W\) for powers one, three and six have respective dimensions \(0,2,4\). Subtracting the resulting state populations yields the three primitive-period cycle counts. The dimensions of the kernels of the nilpotent powers are \(0,m-2,n-4\), giving the asserted \(T\)-shell populations by the Fitting decomposition.

**Odd dimensions.** For \(\delta=1\), \(Bp=Br=0\). Since \(A\) is invertible and \(B-A\) has rank two, \(\dim\ker B\le2\), so \(\ker B=\operatorname{span}\{p,r\}\). Here \(p^{\mathsf T}p=r^{\mathsf T}r=1\) and \(p^{\mathsf T}r=0\). Symmetry of \(B\) gives \(\operatorname{Im}B=(\ker B)^\perp\), hence \(V=\ker B\oplus\operatorname{Im}B\), and \(B\) is invertible on its \((n-2)\)-dimensional image. Set \(s=u+r=Bv\) and \(t=v+p=Bu\). The two-dimensional subspace \(U=\operatorname{span}\{s,t\}\subseteq\operatorname{Im}B\) is exchanged by \(B\).

To determine the unipotent blocks, first put \(N=A+I\), for which \(\operatorname{Im}N=\ker N\) has dimension \(m\). The span of \(u,v\) meets \(\operatorname{Im}N\) trivially: an element in the intersection would lie in \(\ker N\), but \(Nu=u+p\) and \(Nv=v+r\) are independent. Thus \((B+I)x=0\) requires both \(Nx=0\) and \(x_u=x_v=0\). Those two coordinate conditions are independent on \(\ker N\), as their annihilating vectors \(u,v\) are independent modulo \((\ker N)^\perp=\operatorname{Im}N\). Consequently \(\dim\ker(B+I)=m-2\).

On the periodic subspace \(\operatorname{Im}B\), let \(E=B^2+I=(B+I)^2\). Expanding \(B=A+uv^{\mathsf T}+vu^{\mathsf T}\), and using \(p^{\mathsf T}x=r^{\mathsf T}x=0\) for \(x\in\operatorname{Im}B\), yields
\[
 Ex=(u^{\mathsf T}x)(u+r)+(v^{\mathsf T}x)(v+p).
\]
The coordinate functionals \(u^{\mathsf T}\) and \(v^{\mathsf T}\) are independent on \(\operatorname{Im}B\), since \(u,v\) are independent modulo \(\ker B=\operatorname{span}\{p,r\}\). Therefore \(E(\operatorname{Im}B)=U\) has rank two. Since \(B\) exchanges \(s,t\), \((B+I)U\) has dimension one and \((B+I)^2U=0\). On \(\operatorname{Im}B\), the ranks of \((B+I)^2\) and \((B+I)^3\) are thus two and one, while \((B+I)^4=0\). This forces precisely one length-four unipotent block and all other unipotent blocks of length at most two. There are \(m-2\) unipotent blocks altogether, and their combined dimension is \(n-2=2m-2\), so the remaining \(m-3\) blocks all have length two. The other two eigenvectors form \(J_1(0)^{\oplus2}\).

The periodic fixed-space dimensions of \(B,B^2,B^4\) are respectively \(m-2,n-4,n-2\); applying the standard exact-period divisor subtraction gives the displayed primitive-orbit counts. Since the zero eigenvalue is semisimple with nullity two, every nonperiodic point has \(T=1\), proving the last shell formula.

## Verification

The standalone script `verify.py` builds adjacency matrices independently from their graph edges and carries out Gaussian elimination over \(\mathbb F_2\), matrix-power identities, and exhaustive state iteration. It checks the algebraic rank and fixed-space formulas in dimensions two through eight (up to 256 vertices), exhausts all 65,808 binary initial configurations in dimensions two through four, and exhausts 65,792 initial configurations over \(\mathbb F_4\) in dimensions two and three. The replayed output is `verification_output.txt` and terminates with `EDGE_DELETED_HYPERCUBE_ALL_CHECKS_PASSED`. All such finite checks are corroboration; the proof above establishes the all-dimension theorem.

## Relationship to prior work

Brunnet and Chaté (2004) study synchronous hypercube cellular automata with nonlinear totalistic threshold rules and large-dimensional collective behavior; their model does not delete an edge or determine these modular-linear Jordan blocks. Lettieri, Stevens and Thomas (2006) explain the minimal-polynomial analysis of linear cellular automata, especially periodic one-dimensional Rules 90 and 150. Their framework motivates the dynamical invariants, but the cyclic one-dimensional update matrices do not directly yield the rank-two defective-hypercube classification. Wu and coauthors (2017) study the real spectral-radius effects of deleting multiple hypercube edges, rather than characteristic-two dynamics for one deleted edge.

The ordinary hypercube identity \(A^2=(d\bmod2)I\) already implies zero after at most two updates in even dimension, and invertibility with period at most two in odd dimension. In contrast, deleting one edge creates primitive six-cycles when \(d\) is even and destroys reversibility while creating primitive four-cycles when \(d\) is odd. A particularly close prior two-site self-feedback result gives the **same even-dimensional rational canonical form** as the deleted-edge update, hence the same even-dimensional orbit and transient populations. In odd dimension it gives the same *invertible* Jordan component but a length-two nilpotent zero block rather than the present two length-one zero blocks. Thus the genuinely distinguishing statement here is the complete one-bond fault classification—especially the odd-dimensional semisimple-zero transition and sharp one-step transient—in contrast to two adjacent diagonal feedback sites. The coincidence in the even case is acknowledged, not claimed as a new abstract Jordan type.

## Limitations

The claim concerns exactly one deleted edge, fields of characteristic two, and synchronous neighbor-sum dynamics. It does not classify arbitrary edge sets, nonbinary characteristics, asynchronous schedules, or noisy systems. The bibliographic comparison cannot rule out unindexed or inaccessible mathematically equivalent results; no independent audit has been performed.

## References

- L. G. Brunnet and H. Chaté, “Cellular automata on high-dimensional hypercubes,” *Physical Review E* **69** (2004), 057201, published 2004-05-18, DOI: `10.1103/PhysRevE.69.057201`.
- S. Lettieri, J. G. Stevens and D. M. Thomas, “Characteristic and minimal polynomials of linear cellular automata,” *Rocky Mountain Journal of Mathematics* **36** (2006), 1077–1092, DOI: `10.1216/rmjm/1181069447`.
- Y. Wu, T. Zhang, S. Chen and T. Wang, “The minimum spectral radius of an edge-removed network: A hypercube perspective,” *Discrete Dynamics in Nature and Society* (2017), article 1382980, DOI: `10.1155/2017/1382980`.
