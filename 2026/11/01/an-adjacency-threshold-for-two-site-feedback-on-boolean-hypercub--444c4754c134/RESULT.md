# An adjacency threshold for two-site feedback on Boolean hypercube automata

## Finding

Let \(d\ge3\) be an integer, \(n=2^d\), and \(h=n/2\). Label the vertices of the Boolean hypercube \(Q_d\) by bit strings of length \(d\). Choose two distinct vertices \(u,v\). At every synchronous update, each binary site takes the XOR of its neighbors, with the old state additionally XORed at exactly the two designated sites \(u,v\). Thus the matrix is \(B=A+e_ue_u^{\mathsf T}+e_ve_v^{\mathsf T}\) over \(\mathbb F_2\), where \(A\) is the ordinary hypercube adjacency matrix.

Put \(g(z)=z^2+z+1\). Write \(J_s(\lambda)\) for a Jordan block of length \(s\), and \(C(g^2)\) for the four-dimensional companion block with invariant factor \(g(z)^2\). The complete rational/Jordan classification is

\[
\begin{array}{c|c|l}
 d\bmod2 & \operatorname{dist}(u,v)&\text{rational/Jordan blocks of }B\\\hline
0&1&C(g^2)\ \oplus\ J_2(0)^{\oplus(h-2)}\\
0&\ge2&J_1(1)^{\oplus2}\ \oplus\ J_3(0)^{\oplus2}\ \oplus\ J_2(0)^{\oplus(h-4)}\\
1&1&J_2(0)\ \oplus\ J_4(1)\ \oplus\ J_2(1)^{\oplus(h-3)}\\
1&\ge2&C(g)^{\oplus2}\ \oplus\ J_2(1)^{\oplus(h-2)}.
\end{array}
\]

The last row means two separate two-dimensional irreducible companion blocks. All multiplicities above are nonnegative under the stated \(d\ge3\) restriction (in the even nonadjacent row \(d\ge4\)). **Every pair of nonadjacent vertices, at every distance two through \(d\), has the same dynamical similarity type.**

For odd \(d\), the update is reversible if and only if the two feedback vertices are **nonadjacent**. In that case its exact order is six. Adjacent feedback vertices instead create a single nilpotent block of length two and a periodic component of exact order four. For even \(d\), adjacent feedback gives a period-six component and a sharp transient bound two, while nonadjacent feedback gives only fixed-point attractors and a sharp transient bound three.

The exact cumulative first-periodic-entry count is
\[
 \#\{x:T(x)\le t\}=2^{k+\sum_{\ell\in\mathcal L}\min(t,\ell)},\qquad t\in\mathbb Z_{\ge0},
\]
where \(k\) is the dimension of the invertible component and \(\mathcal L\) is the displayed multiset of zero-eigenvalue Jordan lengths. In the four rows these pairs \((k,\mathcal L)\) are respectively
\[
(4,\{2^{[h-2]}\}),\quad
(2,\{3,3,2^{[h-4]}\}),\quad
(n-2,\{2\}),\quad(n,\varnothing).
\]
Here \(2^{[m]}\) denotes \(m\) copies of block length two, **not** exponentiation. The exact shell population for \(t\ge1\) is the difference between the cumulative counts at \(t\) and \(t-1\).

Primitive orbit counts follow from the periodic fixed-space dimensions. For even \(d\) and adjacent feedback, the periodic component has \(1\) fixed point, one primitive three-cycle, and two primitive six-cycles. For even \(d\) and nonadjacent feedback, exactly four fixed points occur and there are no longer periodic orbits. For odd \(d\) and adjacent feedback, only periods \(1,2,4\) occur, with respective primitive orbit counts
\[
2^{h-2},\qquad\frac{2^{n-4}-2^{h-2}}2,\qquad\frac{2^{n-2}-2^{n-4}}4.
\]
For odd \(d\) and nonadjacent feedback, the primitive orbit counts for periods \(1,2,3,6\) are, respectively,
\[
2^{h-2},\quad\frac{2^{n-4}-2^{h-2}}2,\quad
\frac{2^{h+2}-2^{h-2}}3,\quad
\frac{2^n-2^{n-4}-2^{h+2}+2^{h-2}}6.
\]

## Assumptions and scope

All arithmetic is in the binary field \(\mathbb F_2\). All vertices are labeled and all configurations are counted separately. A trajectory's first-periodic-entry time is \(T(x)=\min\{t\ge0:B^t x\text{ is on a periodic orbit}\}\). A primitive orbit is a set of distinct states with least positive period equal to its specified length. The theorem is for every integer \(d\ge3\) and every pair of distinct vertices. Dimension two is deliberately excluded because antipodal sites have identical neighbor columns, changing the structural calculation.

## Proof

**Step 1: square-zero backbone.** Let \(S_i\) flip coordinate \(i\) of the cube and put \(\varepsilon=d\bmod2\). Then \(A=\sum_{i=1}^dS_i\), hence \(A^2=\varepsilon I\). In the binary group algebra write \(y_i=S_i+I\). Each \(y_i\) squares to zero and \(N=A+\varepsilon I=\sum_i y_i\). An invertible linear substitution of the square-zero generators sends \(\sum_i y_i\) to \(y_1\), proving \(N^2=0\) and \(\operatorname{rank}N=h\). Thus \(N\) has exactly \(h\) blocks of length two at eigenvalue zero.

**Step 2: four-dimensional local space.** Put \(p=e_u\), \(q=e_v\), \(b=Ap\), and \(c=Aq\). For every \(d\ge3\), these four vectors are independent: supports of the two neighborhood columns have distinct vertices outside \(\{u,v\}\), including for distance two because at least one coordinate is not among the two differing coordinates. Their span \(U\) is invariant under \(A\), \(B\), and \(E=pp^{\mathsf T}+qq^{\mathsf T}\). With \(\delta=1\) precisely when \(u,v\) are adjacent, the action on the ordered basis \((p,q,b,c)\) is the matrix
\[
M_{\varepsilon,\delta}=\begin{pmatrix}
1&0&\varepsilon&\delta\\0&1&\delta&\varepsilon\\
1&0&0&0\\0&1&0&0
\end{pmatrix}.
\]
The quotient by \(U\) carries the action induced by \(A\), because the perturbation \(E\) has image in \(U\).

**Step 3: even dimension, adjacent sites.** Now \(A^2=0\), and \(U\) is nondegenerate under the standard dot product: its Gram matrix has determinant one when \(\delta=1\). Symmetry of \(A\) and the inclusion \(p,q\in U\) give the invariant orthogonal direct sum \(V=U\oplus U^{\perp}\). On the complement \(B=A\), containing \(h-2\) blocks \(J_2(0)\). Direct multiplication of \(M_{0,1}\) gives characteristic polynomial \(g^2\), with \(g(M_{0,1})\ne0\) and \(g(M_{0,1})^2=0\); hence its sole invariant factor is \(g^2\). This proves the first row and the periodic component's order six.

**Step 4: odd dimension, nonadjacent sites.** Here \(A^2=I\), \(\delta=0\), and the Gram matrix of \(U\) in the displayed basis is the identity. Again \(V=U\oplus U^{\perp}\) and \(B=A\) on the complement. On \(U\), \(M_{1,0}\) splits into two copies of the companion matrix of \(g\). On the complement \(A+I\) has \(h-2\) square-zero blocks of length two, proving the last row. Since both an order-three irreducible component and an order-two unipotent component occur, the exact order is six.

**Step 5: even dimension, nonadjacent sites.** Put \(P=(p,q)\), \(R=AP=(b,c)\). Since \(P^{\mathsf T}AP=0\), for \(x=P^{\mathsf T}w\) and \(y=P^{\mathsf T}Aw\) one obtains
\[
B^2w=P(x+y)+Rx,\qquad B^3w=(P+R)(x+y),\qquad B^4w=B^3w.
\]
Independence of \(p,q,b,c\) means that the four coordinates \((x,y)\) range freely over \(\mathbb F_2^4\), so these powers have ranks four and two, respectively. Also \(\ker B=\ker A\cap\ker P^{\mathsf T}\): the \(P\)-coordinates of an element in the image of \(A\) must vanish, because \(\operatorname{span}(p,q)\cap\ker A=0\). On \(\ker A=\operatorname{im}A\), the two functionals \(P^{\mathsf T}\) are independent because \(Ap,Aq\) are independent. Thus \(\operatorname{rank}B=h+2\). The stabilized rank two, together with rank sequence \((h+2,4,2,2,\ldots)\), yields precisely two \(J_1(1)\), two \(J_3(0)\), and \(h-4\) blocks \(J_2(0)\).

**Step 6: odd dimension, adjacent sites.** Set \(N=A+I\), \(C=B+I=N+E\), \(P=(p,q)\), \(R=NP\), and \(H=P^{\mathsf T}NP=\begin{pmatrix}1&1\\1&1\end{pmatrix}\), so \(H^2=0\). For \(x=P^{\mathsf T}w\), \(y=P^{\mathsf T}Nw\), one computes
\[
\begin{aligned}
C^2w&=P(x+y)+Rx,\\
C^3w&=P(Hx+x+y)+R(x+y),\\
C^4w&=P(Hy+x+y)+R(Hx+x+y).
\end{aligned}
\]
Because the four vectors \(p,q,Np,Nq\) are independent, \((x,y)\) ranges through all four binary coordinates. The displayed maps have ranks \(4,3,2\): for the fourth power the \(P\)-coefficient equals \((I+H)\) times the \(R\)-coefficient, whereas the latter ranges freely over two coordinates. The characteristic polynomial of \(M_{1,1}\) is \(z^2(z+1)^2\), and its zero-primary part is a single \(J_2(0)\); the quotient \(V/U\) has only eigenvalue one. Thus the total zero-primary dimension is two, and \(\operatorname{rank}B=n-1\), \(\operatorname{rank}B^2=n-2\). Furthermore, \(\ker C=\ker N\cap\ker P^{\mathsf T}\) and the two coordinate functionals are independent on \(\ker N=\operatorname{im}N\). Hence \(\operatorname{rank}C=h+2\). Removing the two dimensions on which \(C\) is invertible from its rank sequence \((h+2,4,3,2,2,\ldots)\) leaves one block \(J_4(0)\) and \(h-3\) blocks \(J_2(0)\) for \(C\) on the eigenvalue-one primary space. Undoing the shift gives the third row.

**Step 7: population formulas.** In Fitting decomposition, an arbitrary state is periodic exactly when its nilpotent coordinates vanish. A nilpotent block of length \(\ell\) contributes \(2^{\min(t,\ell)}\) choices whose \(t\)-th iterate is zero; the invertible component contributes \(2^k\) choices. This proves the transient census. For an invertible block \(J_s(1)\), the dimensions of fixed spaces of powers follow from \((I+N)^{2^j}=I+N^{2^j}\); each \(C(g)\) gives order three and \(C(g^2)\) gives order six. Möbius inversion on the possible periods yields each primitive orbit count displayed above.

## Verification

Run `python3 verify.py` using only the standard Python library. The checker directly constructs the synchronous update on labeled hypercubes, performs binary Gaussian elimination on image vectors, verifies ranks of all relevant powers and fixed-space dimensions for every pair-distance class in dimensions three through eight, and independently exhausts all labeled initial configurations for all pair-distances in dimensions three and four. The exact self-contained output is in `verification_output.txt`. These finite tests corroborate the infinite-dimensional proof; they are not used as a substitute for it.

## Relationship to prior work

Brunnet and Chaté (2004) investigate synchronous totalistic threshold-type automata on high-dimensional hypercubes; their full four-page paper uses interval conditions on the integer neighbor sum and numerical collective-behavior classification, not binary neighbor parity with two exceptional self-feedback sites. Lettieri, Stevens, and Thomas (2006) develop minimal-polynomial methods and finite-field dynamics for one-dimensional cyclic Rule 90 and Rule 150. Those methods inform the algebraic approach but do not state the four-way two-defect hypercube classification. A separately available one-site feedback classification concerns only a rank-one perturbation: its Jordan forms alone do not imply the adjacency versus nonadjacency dichotomy or the present rank-two invariant-space calculation. A public mathematical research-index search returned a result about distance-two *unperturbed* hypercube parity dynamics; that model changes the edge set globally, rather than inserting two local loops, and neither result implies the other. These are implication comparisons, not a claim that absence from a search proves historical uniqueness.

## Limitations

The result is restricted to binary fields and dimensions at least three; dimension two requires a distinct treatment. It classifies the full linear dynamics up to similarity, not spatial patterns of individual periodic configurations. Historical work not indexed by the checked sources may contain equivalent rank-two perturbation formulas. No independent mathematical validation has been performed.

## References

- L. G. Brunnet and H. Chaté, “Cellular automata on high-dimensional hypercubes,” *Physical Review E* **69** (2004), 057201. DOI: 10.1103/PhysRevE.69.057201; first publicly documented 2004-05-18.
- S. Lettieri, J. G. Stevens, and D. M. Thomas, “Characteristic and Minimal Polynomials of Linear Cellular Automata,” *Rocky Mountain Journal of Mathematics* **36** (2006), 1077–1092. DOI: 10.1216/rmjm/1181069447.
