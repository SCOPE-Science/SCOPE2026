# Color-permutation homology characters of categorical cycle–clique products

## Finding
Let \(m\ge 3\) and \(n\ge 2\) be integers. Give \(G_{m,n}=C_m\times K_n\) the **categorical** graph product: its vertex set is \((\mathbb Z/m\mathbb Z)\times[n]\), with \((i,a)\) adjacent to \((j,b)\) exactly when \(j-i\equiv\pm1\pmod m\) and \(a\ne b\). Put \(X_{m,n}=\operatorname{Ind}(G_{m,n})\). Relabeling the second coordinate gives a canonical action of \(S_n\). For \(\sigma\in S_n\), write \(f(\sigma)=|\{a\in[n]:\sigma(a)=a\}|\).

**Theorem.** The complete reduced, rational, equivariant Euler character of \(X_{m,n}\) is
\[
\sum_{j\ge0}(-1)^j\operatorname{tr}\!\left(\sigma\mid\widetilde H_j(X_{m,n};\mathbb Q)\right)
=\begin{cases}
-3\bigl(f(\sigma)-1\bigr)^r-(-1)^r\bigl(f(\sigma)-1\bigr),&m=3r,\\
(-1)^{m+1}\bigl(f(\sigma)-1\bigr),&3\nmid m.
\end{cases}
\]
In particular, for **every** \(r\ge1\), the known concentration of reduced homology of \(X_{3r,n}\) in degree \(2r-1\) upgrades this identity to the full actual \(S_n\)-homology character:
\[
\boxed{\operatorname{tr}\!\left(\sigma\mid\widetilde H_{2r-1}(X_{3r,n};\mathbb Q)\right)
=3\bigl(f(\sigma)-1\bigr)^r+(-1)^r\bigl(f(\sigma)-1\bigr).}
\]
All other reduced rational homology groups vanish in this divisible-by-three case. If \(U_n\) is the rational augmentation (standard) \(S_n\)-module, the last character is equivalently the identity \([\widetilde H_{2r-1}]=3[U_n^{\otimes r}]+(-1)^r[U_n]\) in the rational representation ring. This is a representation-ring identity, not an assertion of a direct-sum decomposition when the sign is negative.

Thus, beyond the identity element, the full character depends only on the number of **fixed colors**, not on the remaining cycle lengths of the permutation. For example, at \(m=6\) and \(n=4\), the character values on the conjugacy types \((1^4),(2,1^2),(2^2),(3,1),(4)\) are respectively \(30,4,2,0,2\). The resulting invariant subspace has dimension \(3\), information not determined by the previously known Betti number \(30\).

## Assumptions and scope
The simplicial complex has all independent vertex subsets as faces, including the empty face in its **augmented chain complex**. The group acts by permuting colors simultaneously in every cycle position, not by rotating the base cycle. Homology and traces in the character statements use \(\mathbb Q\). The character computation is intrinsic and applies to all \(m\ge3\), independently of any homotopy classification. Only the passage from the virtual character to an actual single-degree character uses the published pure-degree homotopy theorem for \(m=3r\). No new assertion about torsion or sphere decompositions is made for \(3\nmid m\).

## Proof
**1. Signed face trace.** Fix \(\sigma\in S_n\), and let its color orbits be \(O_1,\ldots,O_c\), of which exactly \(f=f(\sigma)\) are singletons. A face fixed setwise by \(\sigma\) is specified, in each of the \(m\) cycle positions, by a union of these orbits. Its signed contribution to the trace on the *augmented* simplicial chain complex, including the empty face in degree \(-1\), is \(-(-1)^s\), where \(s\) is the total number of chosen color orbits across positions. Indeed, on a nonempty face with \(v\) vertices and \(s\) vertex-orbits, the sign of its induced vertex permutation is \((-1)^{v-s}\), while the chain alternating sign is \((-1)^{v-1}\). Their product is \(-(-1)^s\). The empty face contributes \(-1\), agreeing with the same rule.

Let \(Z_m(\sigma)\) be the sum of \((-1)^s\) over these invariant independent subsets, including the empty subset. The reduced Lefschetz number is consequently \(-Z_m(\sigma)\), exactly by the simplicial Hopf trace formula (or by canceling boundaries in the alternating chain trace).

**2. Row compatibility and cancellations.** If two consecutive positions both contain vertices, the categorical-product adjacency condition forces both row sets to be the **same singleton color**: otherwise some selected colors differ across the two positions and are adjacent. For invariant row sets, such a singleton must be one of the \(f\) fixed colors. Thus a row is either empty \(E\), one singleton fixed color \(S_i\) (\(1\le i\le f\)), or another nonempty invariant row set \(B\). Consecutive states are compatible only when at least one is \(E\), or when both are the same \(S_i\). The sum of \((-1)^{\text{number of chosen color orbits}}\) over **all** nonempty invariant row sets is \(-1\), because \(\sum_{T\subseteq[c]}(-1)^{|T|}=0\). Each \(S_i\) has weight \(-1\), so the aggregate weight of \(B\) is \(f-1\), regardless of the number or lengths of nonsingleton color orbits.

**3. Exact transfer trace.** For \(f\ge1\), take the transfer matrix with row and column states \(E,B,S_1,\ldots,S_f\), entry \(T_{ab}=w(b)\) if states \(a,b\) are compatible, and zero otherwise, with weights \(w(E)=1\), \(w(B)=f-1\), \(w(S_i)=-1\). Since the cycle length is at least three, closing the transfer walk counts each admissible cyclic state assignment once, and
\[Z_m(\sigma)=\operatorname{tr}(T^m).\]
The subspace of vectors supported on the \(S_i\) coordinates with coordinate sum zero is an eigenspace of \(T\) with eigenvalue \(-1\) and dimension \(f-1\). On its three-dimensional complement represented by coordinates \((E,B,S_1=\cdots=S_f)\), the matrix is
\[
M_f=\begin{pmatrix}1&f-1&-f\\1&0&0\\1&0&-1\end{pmatrix},
\qquad \det(tI-M_f)=t^3-(f-1).
\]
Therefore \(Z_m(\sigma)=\operatorname{tr}(M_f^m)+(f-1)(-1)^m\). This also holds for \(f=0\): the genuine transfer matrix is then \(\begin{pmatrix}1&-1\\1&0\end{pmatrix}\), whose characteristic polynomial is \(t^2-t+1\); the formal three-by-three matrix at \(f=0\) has characteristic polynomial \((t+1)(t^2-t+1)\), and subtracting \((-1)^m\) cancels its extra eigenvalue. As the three eigenvalues of \(M_f\) are the three cubic roots of \(f-1\), their \(m\)-th powers sum to \(3(f-1)^r\) when \(m=3r\) and to zero otherwise. In consequence,
\[
Z_m(\sigma)=\begin{cases}
3(f-1)^r+(-1)^r(f-1),&m=3r,\\
(-1)^m(f-1),&3\nmid m.
\end{cases}
\]
Combining with step 1 proves the first displayed theorem formula for **every** permutation and every admissible \((m,n)\).

**4. The actual homology character.** Antolín Camarena and Carnero Bravo's homotopy classification establishes that \(X_{3r,n}\) is homotopy equivalent to a wedge of spheres **all of degree** \(2r-1\); it holds for \(n\ge2\), including the case \(n=2\) by their separate cycle calculation. Consequently its reduced Lefschetz number equals \((-1)^{2r-1}\operatorname{tr}(\sigma\mid\widetilde H_{2r-1})\), which is the negative of that homology trace. Equating it with \(-Z_m(\sigma)\) yields the boxed character formula. Finally, the standard module \(U_n\) has character \(f(\sigma)-1\); tensor products multiply characters, and rational representations of finite groups are determined by their characters. This yields the asserted representation-ring equality. No chain-level equivariance of the published homotopy equivalence is assumed.

## Verification
The included standalone `checker.py` independently enumerates the \(\sigma\)-invariant row subsets of the **original** colored product graph and computes the signed augmented-chain alternating trace via a finite state walk, without substituting the three-by-three matrix. It checks every permutation for \(n=2,3,4\) and all \(m=3,\ldots,9\), totaling \(224\) comparisons; a second check computes the oriented-chain trace directly on original simplices in \(16\) cases. It separately builds full simplicial boundary matrices over \(\mathbb F_2\) for \((m,n)=(3,2),(3,3),(6,2),(6,3)\) and confirms their only reduced Betti numbers are respectively \(2,4,4,14\) in the predicted degrees. These checks are finite corroboration; the proof for all parameters is steps 1–4 and the cited pure-degree homotopy theorem. The finite-field checks do not certify absence of integral torsion.

## Relationship to prior work
Theorem 22 of Antolín Camarena–Carnero Bravo (arXiv:2307.12401, first publicly submitted 2023-07-23) determines the **nonequivariant** homotopy types of these categorical-product independence complexes when the cycle length is divisible by three. The identity-permutation specialization here recovers exactly their sphere rank \(3(n-1)^r+(-1)^r(n-1)\); all nonidentity permutation traces and the representation-ring description are additional data. Their Sections 3.1–3.2 address homotopy equivalences and homology ranks, not the canonical permutation action. The earlier Goyal–Shukla–Singh paper (arXiv:1905.06926) examines products of complete graphs and generalized Mycielskians, not the \(S_n\)-homology of the cycle–clique family. Related published symmetry computations for other graph complexes and for isolated short-cycle cases do not imply this uniform character formula. The main innovation is that orbit-signed cancellation makes the answer depend only on fixed colors rather than the full color cycle type.

## Limitations
The theorem gives the actual rational representation only at cycle lengths divisible by three; for other lengths the formula is an alternating sum of graded representations and **does not determine** the individual homology groups or settle their integral torsion. The result does not classify the simultaneous dihedral action on the cycle coordinate, nor does it provide a canonical integral equivariant cellular splitting. Searches of primary literature and published records are not a proof of bibliographic uniqueness; an equivalent statement may occur in unindexed or otherwise inaccessible work.

## References
1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (2023-07-23); revised version arXiv:2307.12401v2, Theorem 22 and Section 3, https://arxiv.org/abs/2307.12401 .
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019-05-16), especially Section 3, https://arxiv.org/abs/1905.06926 .
3. The simplicial Hopf trace formula and the standard character rule for the augmentation representation are used in their ordinary, finite-dimensional forms; no additional source-dependent lemma is required for the transfer calculation.
