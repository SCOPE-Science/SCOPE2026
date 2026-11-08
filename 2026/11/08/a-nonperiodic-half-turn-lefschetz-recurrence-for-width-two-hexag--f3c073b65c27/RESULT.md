# A nonperiodic half-turn Lefschetz recurrence for width-two hexagonal strips

## Finding
For each integer \(n\ge1\), let \(H_n\) be the three-rail hexagonal strip defined below, and let \(\tau_n\) rotate the strip through a half-turn. For its simplicial independence complex \(X_n=\operatorname{Ind}(H_n)\), put
\[
 e_n=\widetilde\chi\bigl(|X_n|^{\langle\tau_n\rangle}\bigr).
\]
Then the complete generating function of the **geometric fixed-point** reduced Euler characteristics is
\[
\boxed{\sum_{n\ge1}e_nz^n=\frac{z^2(z-1)}{1+z+z^4}.}
\]
Equivalently, \(e_1=0\), \(e_2=-1\), \(e_3=2\), \(e_4=-2\), and
\[
\boxed{e_n=-e_{n-1}-e_{n-4}\quad(n\ge5).}
\]
The first fifteen terms are \(0,-1,2,-2,2,-1,-1,3,-5,6,-5,2,3,-9,14\). The series is nonperiodic and its coefficients have exponentially growing absolute value along a subsequence. Furthermore \(e_n\) equals the reduced rational Lefschetz number of the half-turn on the **full** independence-complex homology:
\[
 e_n=\sum_{d\ge0}(-1)^d\operatorname{tr}\!\left((\tau_n)_*\mid\widetilde H_d(X_n;\mathbb Q)\right).
\]
No concentration of fixed-point homology in a single degree is assumed or asserted.

## Assumptions and scope
The simple undirected graph \(H_n\) has vertices \((r,j)\), where the allowed column indices in the three rows \(r=0,1,2\) respectively are \(1\le j\le2n+1\), \(1\le j\le2n+2\), and \(1\le j\le2n+1\). It contains each horizontal edge \((r,j)(r,j+1)\); additionally, for each odd \(j\in\{1,3,\dots,2n+1\}\), it has edges \((0,j)(1,j+1)\) and \((1,j)(2,j)\). These are the width-two linear hexagonal-grid graphs studied in [1], not square Cartesian grids and not the two-row hexagonal chains.

Define \(\tau_n\) on vertices by
\[
\tau_n(0,j)=(2,2n+2-j),\qquad
\tau_n(2,j)=(0,2n+2-j),\qquad
\tau_n(1,j)=(1,2n+3-j).
\]
It preserves graph edges, has order two, and has no fixed original vertex. The geometric fixed-point space \(|X_n|^{\langle\tau_n\rangle}\) consists of fixed points of the induced action on the geometric realization, **not** just simplices of fixed original vertices. Reduced Euler characteristic uses \(\widetilde\chi(\varnothing)=-1\). The formal power series are considered over \(\mathbb Q[[z]]\).

## Proof
**1. Geometric orbit complex and signed face formula.** Let an involution \(g\) act on a finite graph \(G\). Discard each two-element or fixed singleton vertex orbit containing a graph edge. Let \(Q_g\) have the remaining orbits as its vertices, with two distinct orbits adjacent if some original graph edge joins their members. An invariant independent set in \(G\) is uniquely the union of mutually compatible orbit vertices of \(Q_g\). A point of \(|\operatorname{Ind}(G)|\) fixed by \(g\) has equal barycentric weights along each vertex orbit, so rescaling the orbit weights yields a PL homeomorphism
\[
|\operatorname{Ind}(G)|^{\langle g\rangle}\cong_{\rm PL}|\operatorname{Ind}(Q_g)|.
\]
For \(I(Q;t)=\sum_{S\text{ independent}}t^{|S|}\), including the empty set, \(\widetilde\chi(\operatorname{Ind}(Q))=-I(Q;-1)\). The simplicial Hopf trace identity on augmented chains also shows this is the reduced Lefschetz number: a \(g\)-invariant oriented simplex with \(k\) two-element orbits has sign \((-1)^k\), while its alternating chain parity is \((-1)^{2k-1}=-1\); thus the combined contribution of its \(k\) orbits is \(-(-1)^k\). This argument also covers the empty face.

**2. Explicit quotient graph.** Applying Step 1 to \(H_n\) and \(\tau_n\) gives \(Q_n\) with vertices
\[
 A_1,\ldots,A_{2n+1},\qquad M_1,\ldots,M_n.
\]
Here \(A_j=\{(0,j),(2,2n+2-j)\}\), and \(M_i=\{(1,i),(1,2n+3-i)\}\). The middle-row orbit \(\{(1,n+1),(1,n+2)\}\) is excluded because its vertices are adjacent. The graph \(Q_n\) has the two paths \(A_1-\cdots-A_{2n+1}\) and \(M_1-\cdots-M_n\), together with one cross edge at every \(M_i\):
\[
 M_iA_{2n+2-i}\ (i\text{ odd}),\qquad M_iA_{i-1}\ (i\text{ even}).
\]
This is obtained by checking the two families of nonhorizontal edges and folding the three horizontal paths. In particular, it specifies all orbit compatibility conditions without referring to the original complex.

**3. An eight-state exact transfer.** For \(1\le i\le n\), set \(U_i=A_i\), \(V_i=A_{2n+2-i}\), and \(W_i=M_i\). Put \(C=A_{n+1}\). The only cross-rail edges are \(V_iW_i\) at odd \(i\), and \(U_{i-1}W_i\) at even \(i\). All three rails have nearest-neighbor edges, and the cap \(C\) is adjacent to \(U_n,V_n\). A layer configuration is a triple \(q=(u,v,w)\in\{0,1\}^3\), with \(|q|=u+v+w\), and \(p\wedge q=0\) meaning no shared occupied rail.

Use row vectors \(s\), \(t\) indexed by these eight triples and two \(8\times8\) integer matrices \(A,B\), indexed by consecutive layer states \(p,q\):
\[
 s_q=\begin{cases}(-1)^{|q|},&v_qw_q=0,\\0,&v_qw_q=1,\end{cases}\qquad
 t_q=\begin{cases}1,&u_q+v_q>0,\\0,&u_q=v_q=0.\end{cases}
\]
The cap factor \(t_q\) is \(1\) when \(C\) cannot be chosen and \(1+(-1)=0\) otherwise. For odd destination layer define
\[
 A_{pq}=\begin{cases}(-1)^{|q|},&p\wedge q=0\text{ and }v_qw_q=0,\\0,&\text{otherwise};\end{cases}
\]
for even destination layer define
\[
 B_{pq}=\begin{cases}(-1)^{|q|},&p\wedge q=0\text{ and }u_pw_q=0,\\0,&\text{otherwise}.\end{cases}
\]
All vertex signs are included once in the initial vector or destination layer. Writing \(I_n=I(Q_n;-1)\) and \(T=BA\), exact enumeration of layers gives
\[
I_{2k+1}=sT^kt\quad(k\ge0),\qquad
I_{2k+2}=sT^kBt\quad(k\ge0).
\]

**4. An exact integer-matrix identity and rational reduction.** With the preceding explicit eight-state matrices, direct integer multiplication gives
\[
\boxed{T^8-T^7+2T^6+T^4=0.}
\]
The complete computation is reproduced by the standalone pure-Python verification program [4]. Put \(D(w)=1-w+2w^2+w^4\). By the matrix identity \(T^4(T^4-T^3+2T^2+I_8)=0\), where \(I_8\) is the identity matrix, the coefficients of \(D(w)\sum_{k\ge0}sT^ktw^k\) vanish from degree eight onwards; likewise for \(sT^kBt\). Indeed, the coefficient at degree \(k\ge4\) is \(sT^{k-4}(T^4-T^3+2T^2+I_8)t\). Computing the eight initial coefficients exactly gives the **complete** numerator identities
\[
\sum_{k\ge0}sT^kt\,w^k=\frac{-2w-w^3}{D(w)},\qquad
\sum_{k\ge0}sT^kBt\,w^k=\frac{1+w+w^2}{D(w)}.
\]
Substituting \(w=z^2\), multiplying the odd-index series by \(z\) and the even-index series by \(z^2\), and factoring
\[
D(z^2)=(1-z+z^4)(1+z+z^4),
\]
we obtain
\[
\sum_{n\ge1}I_nz^n=\frac{z^2(1-z)}{1+z+z^4}.
\]
Step 1 gives \(e_n=-I_n\), proving the claimed generating function and recurrence for every integer \(n\ge1\).

**5. Nonperiodicity and exponential growth.** The denominator \(1+z+z^4\) has no zeros on the unit circle: if \(|z|=1\) and \(1+z+z^4=0\), three unit vectors form an equilateral triple, forcing \(z\) to be a primitive cube root of unity and thus \(z^4=z\), contradicting \(1+2z=0\). Its roots have product \(1\), so since no root has modulus one, at least one has modulus less than one. Neither \(z=0\) nor \(z=1\) is a denominator root, so there is no cancellation by the numerator \(z^2(z-1)\). Thus the power series has radius of convergence strictly less than one; Cauchy-Hadamard yields \(\limsup_{n\to\infty}|e_n|^{1/n}>1\). In particular the integer sequence is unbounded and nonperiodic.

## Verification
The standalone Python 3 program `verify_halfturn.py` checks the **actual finite integer matrices**, the identity \(T^8-T^7+2T^6+T^4=0\), and the eight initial numerator coefficients that make the transfer derivation an all-parameter exact calculation. It also constructs original hexagonal strips, verifies the involution preserves every edge, reconstructs quotient graphs independently for \(1\le n\le15\), and compares exact independent-set signed sums against the transfer. For \(1\le n\le5\), it separately enumerates invariant independent faces in the **original graph** instead of relying on the quotient derivation. It tests \(239\) transfer values against the recurrence. Running `python3 verify_halfturn.py` reproduces `HALFTURN_FIXED_EULER_OK` and the recorded check output in `verification_output.txt`.

The matrix identity and initial coefficients are finite exact arithmetic, not a numeric guess from the first terms. The exhaustive small cases independently check the combinatorial model but do not independently prove the formula for arbitrary \(n\); Step 4 does that.

## Relationship to prior work
Chandrakar and Singh [1] determine non-equivariant homotopy types of linear hexagonal-strip independence complexes, including the width-two family. Their results do not determine how half-turn rotations act on homology or the topology of geometric fixed spaces. A nonequivariant wedge classification or Betti table alone cannot specify the Lefschetz character.

A published calculation [2] gives **reflection characters** for the *two-row* linear hexagonal chain \(H_{1\times1\times n}\), whereas the present graph is the *three-row* width-two family \(H_{1\times2\times n}\) and the symmetry is its half-turn. The results have different graph parameters and different scalar sequences. A published calculation [3] of a 56-periodic reflection character concerns independence complexes of rectangular **square** grids \(P_6\square P_n\); the present hexagonal strip is not a Cartesian-product square grid. The half-turn Lefschetz calculation [5] for \(3\times n\) **matching complexes** likewise concerns a different simplicial complex and has a different transfer. Exact searches for geometric fixed Euler characteristics, half-turn traces, hexagonal width-two graphs, and generating functions did not locate equivalent coverage; this is not proof of absolute novelty.

## Limitations
The theorem establishes an alternating **rational homology trace** and the geometric fixed-space reduced Euler characteristic, but not the individual fixed-space Betti numbers or its integral homotopy type. It does not classify other hexagonal widths or arbitrary dihedral actions. The exact transfer proof relies on a small finite integer-matrix computation, supplied in executable and mathematically explicit form. An unindexed or unpublished equivalent result remains possible; independent mathematical audit has not been performed.

## References
[1] Himanshu Chandrakar and Anurag Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318v1 (first publicly submitted 2025-12-24). https://arxiv.org/pdf/2512.21318

[2] *Reflection characters of linear hexagonal-chain independence complexes*, published calculation (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-reflection-characters-of-linear-hexagonal-chain-independence-com--db3e42fb7a57

[3] *A 56-periodic reflection Lefschetz character for six-row grid independence complexes*, published calculation (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-56-periodic-reflection-lefschetz-character-for-six-row-grid-in--8dd06c5248ba

[4] `verify_halfturn.py` and `verification_output.txt`, supplied with this research result; pure Python 3, no external data or packages.

[5] *Half-turn Lefschetz characters and full symmetry quotients of \(3\times n\) grid matching complexes*, published calculation (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-half-turn-lefschetz-characters-and-full-symmetry-quotients-of-3--e4fab66f9a1a
