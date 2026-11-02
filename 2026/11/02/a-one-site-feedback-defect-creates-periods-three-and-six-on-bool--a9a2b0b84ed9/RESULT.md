# A one-site feedback defect creates periods three and six on Boolean hypercubes

## Finding

Let \(d\ge2\), let \(Q_d\) be the labelled \(d\)-dimensional Boolean hypercube, and let \(r=2^d\), \(h=r/2\). On configurations in \(\mathbb F_2^{V(Q_d)}\), apply the synchronous neighbor-XOR rule at every vertex except the all-zero vertex, where the vertex's **own** bit is additionally XORed into its next state. If \(F\) is this update and \(T(x)\) is the first time the trajectory of \(x\) enters a periodic orbit, the following dichotomy is exact.

**Even \(d\):** The update has one one-dimensional fixed component and a nilpotent component with Jordan blocks \(J_3(0)\oplus J_2(0)^{\oplus(h-2)}\). Its only periodic configurations are zero and the nonzero fixed configuration supported at the distinguished vertex and its \(d\) neighbors. The complete first-entry census is

\[
\#\{T=0\}=2,\qquad
\#\{T=1\}=2^h-2,\qquad
\#\{T=2\}=2^{r-1}-2^h,\qquad
\#\{T=3\}=2^{r-1}.
\]

**Odd \(d\) (necessarily \(d\ge3\)):** The update is bijective; its entire state space is periodic, with every primitive period in \(\{1,2,3,6\}\) attained. The periodic rational canonical decomposition consists of one irreducible two-dimensional factor \(z^2+z+1\) and \(h-1\) two-dimensional Jordan blocks \(J_2(1)\). The exact **numbers of distinct primitive temporal orbits**, without quotienting by graph symmetry, are

\[
\begin{aligned}
C_1&=2^{h-1},\\
C_2&=\frac{2^{r-2}-2^{h-1}}{2},\\
C_3&=2^{h-1},\\
C_6&=\frac{2^r-2^{r-2}-2^{h+1}+2^{h-1}}{6}.
\end{aligned}
\]

The three states supported respectively on the distinguished vertex, on that vertex together with its neighbors, and on its neighbors alone form an explicit primitive three-cycle. In the unmodified hypercube neighbor-XOR dynamics, even-dimensional systems reach zero within two updates, whereas odd-dimensional systems have only periods one and two. Thus **one local self-feedback bit** creates a persistent nonzero attractor and a third transient layer in even dimension, but creates primitive periods three and six in odd dimension.

## Assumptions and scope

Vertices are bit vectors in \(\{0,1\}^d\), with an edge for each single-coordinate flip. Every state is a vector over \(\mathbb F_2\). All updates are simultaneous. There are no self-loops in the original cube; the only modified update is at \(o=(0,\ldots,0)\). Let \(A\) be the binary adjacency matrix, \(e\) the basis vector at \(o\), and \(P=ee^{\mathsf T}\). The update is \(F=A+P\). The time \(T\) includes \(T=0\) for initially periodic configurations. The orbit numbers \(C_j\) count labelled distinct orbits, not individual configurations. All assertions quantify over every integer \(d\ge2\), with parity-conditioned formulas as stated.

## Proof

Put \(\delta=d\bmod2\) and \(H=A+\delta I\). If \(S_i\) flips the \(i\)-th cube coordinate, then \(A=\sum_{i=1}^d S_i\). The operators \(S_i\) commute, satisfy \(S_i^2=I\), and are over characteristic two; hence

\[
A^2=\delta I,\qquad H^2=0.
\]

Partition vertices by their first coordinate, and put \(C=A(Q_{d-1})+\delta I\). Then

\[
H=\begin{pmatrix}C&I\\I&C\end{pmatrix},\qquad C^2=I.
\]

Thus \(\ker H=\{(v,Cv):v\in\mathbb F_2^h\}\), giving \(\operatorname{rank}H=h\), and therefore \(\operatorname{im}H=\ker H\). The matrix \(H\) is symmetric. Also \(He\ne0\), since the distinguished vertex has neighbors, so \(e\notin\operatorname{im}H=\ker H\). Symmetry implies the functional \(e^{\mathsf T}\) is nonzero on \(\ker H\). Choose \(v\in\ker H\) with \(e^{\mathsf T}v=1\). The rank-one update \(D=H+P=F+\delta I\) sends \(v\) to \(e\), and every vector in \(\operatorname{im}H\) remains in \(\operatorname{im}D\) by modifying its preimage by a multiple of \(v\). Because \(e\notin\operatorname{im}H\),

\[
\operatorname{rank}D=h+1.
\]

Write \(w=He\). Since \(H^2=0\),

\[
D^2=HP+PH+P,\qquad
D^2x=(e^{\mathsf T}x)w+(e^{\mathsf T}Hx+e^{\mathsf T}x)e.
\]

The vectors \(e,w\) are independent, as are the coordinate functionals \(e^{\mathsf T},e^{\mathsf T}H\); consequently \(\operatorname{im}D^2=W=\operatorname{span}\{e,w\}\) and \(\operatorname{rank}D^2=2\). Since \(e^{\mathsf T}He=\delta\), the restriction of \(D\) to the invariant plane \(W\), in ordered basis \((e,w)\), is

\[
[D|_W]=\begin{pmatrix}1&\delta\\1&0\end{pmatrix}.
\]

If \(d\) is even, \(D=F\), the displayed matrix is an idempotent of rank one, and \(\operatorname{rank}F^3=\operatorname{rank}F^4=1\) with \(F^3=F^4\). Its image is the fixed line spanned by \(e+Ae\); the complementary nilpotent subspace has dimension \(r-1\). After subtracting the one invertible dimension, the successive ranks of the nilpotent part at exponents one, two, three are \(h,1,0\). Hence there is exactly one block of size three and \(h-2\) blocks of size two. The dimensions of \(\ker F^t\) inside the nilpotent space, including zero, are \(0,h-1,r-2,r-1\) for \(t=0,1,2,3\). Adjoining the fixed line yields the cumulative entry counts \(2,2^h,2^{r-1},2^r\); successive differences give the four claimed shells.

If \(d\) is odd, \(D=F+I\), and \([D|_W]\) has irreducible polynomial \(z^2+z+1\) and order three. Since \(D^2\) maps onto \(W\) and is invertible on \(W\), there is a \(D\)-invariant direct sum \(\mathbb F_2^r=W\oplus\ker D^2\). On the second summand \(D^2=0\), and its dimension and rank are \(r-2\) and \(\operatorname{rank}D-2=h-1\), respectively. Therefore it consists of precisely \(h-1\) size-two nilpotent Jordan blocks of \(D\); shifting back gives \(h-1\) copies of \(J_2(1)\) for \(F\). On \(W\), \(F=D+I\) also has polynomial \(z^2+z+1\) and order three. On the complementary summand, \(F=I+D\) has order two. Therefore \(F\) is bijective with order six. The counts of points fixed by \(F^k\) for \(k=1,2,3,6\) are, respectively,

\[
2^{h-1},\quad 2^{r-2},\quad 2^{h+1},\quad 2^r.
\]

Subtract shorter-period points by divisibility and divide by the primitive period to obtain the stated \(C_1,C_2,C_3,C_6\). All four are positive because \(d\ge3\) and \(h\ge4\). Explicitly, \(e\mapsto e+Ae\mapsto Ae\mapsto e\). This proves all claims.

## Verification

The standalone bit-matrix checker in `VERIFY.py` constructs the update matrix directly from cube-coordinate flips, computes ranks via binary elimination, and compares powers against the claimed identities for every dimension \(2\le d\le8\). It separately advances full configurations and exhaustively checks every state for \(d=2,3,4\); the resulting distributions are \((2,2,4,8)\) for first-entry times zero through three at \(d=2\), \((8,56,24,168)\) states of periods one, two, three, six at \(d=3\), and \((2,254,32512,32768)\) first-entry counts at \(d=4\). The recorded execution in `VERIFY_OUTPUT.txt` concludes `HYPERCUBE_ONE_SITE_VERIFY_OK`. These finite checks corroborate, but do not replace, the general proof above.

## Relationship to prior work

Brunnet and Chaté (2004) study synchronous cellular automata on Boolean hypercubes with uniform nonlinear threshold-type rules, focusing on macroscopic collective behavior rather than parity updates with one vertex defect. Lettieri, Stevens and Thomas (2006) characterize linear Rule 90 and Rule 150 automata under one-dimensional boundary conditions, establishing general minimal-polynomial techniques but not the non-translation-invariant defective-cube dynamics here. Martin, Odlyzko and Wolfram (1984) develop earlier algebraic theory of finite additive cellular automata. Those established methodologies are credited, not claimed as new. A public result on **distance-two** cube parity dynamics has no distinguished-site defect and describes dynamics with only periods one or two, whereas the present **distance-one** defective update has explicit primitive periods three and six. Likewise, earlier graph-specific parity-census results on rings, wheels and rectangular tori do not imply this cube/defect classification.

## Limitations

The theorem applies specifically to the binary field, to one self-feedback defect, and to the standard hypercube; it does not claim robustness under arbitrary vertex defects or couplings, classify geometrically distinct orbits up to cube automorphisms, or address nonlinear threshold rules. The comparison with all prior or unpublished research cannot be exhaustive, and independent validation is not claimed.

## References

- L. G. Brunnet and H. Chaté, *Cellular automata on high-dimensional hypercubes*, Physical Review E 69 (2004), 057201, published May 18, 2004; DOI: 10.1103/PhysRevE.69.057201.
- S. Lettieri, J. G. Stevens, and D. M. Thomas, *Characteristic and minimal polynomials of linear cellular automata*, Rocky Mountain Journal of Mathematics 36 (2006), 1077–1092; DOI: 10.1216/rmjm/1181069447.
- O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics 93 (1984), 219–258; DOI: 10.1007/BF01223745.
- Public mathematical record `f288ef2fe8b4`, *A mod-four orbit census for parity automata on distance-two Boolean cubes* (2026). Examined for implication and differing adjacency/defect hypotheses.
