# All one-perfect linear flag-rank codes: existence, classification, and exact enumeration

## Finding

For any prime power \(q\), a nontrivial linear code of minimum flag-rank distance exactly \(3\) is perfect in the space of upper triangular matrices precisely at the lengths
\[
n=\frac{q^{\alpha}-1}{q-1},\qquad \alpha\ge3,
\]
where \(\alpha\) is its codimension. Every such parameter pair is attained, without an upper restriction on \(\alpha\). All resulting subspaces are classified by a projective parity-check criterion, and the **exact number of distinct labeled linear subspaces** with these properties is
\[
\boxed{\displaystyle
\mathfrak P_{q,\alpha}=
\frac{n!\,(q-1)^n\,(q^{\alpha}-q^2)^{n-1}\,
q^{\alpha(n-1)(n-2)/2}}
{\prod_{j=0}^{\alpha-1}(q^{\alpha}-q^j)}.}
\]
Here \(n\) is the value specified above. Distinct means unequal linear subspaces of the **fixed coordinate space**, not inequivalence classes under metric isometries.

## Assumptions and scope

Let \(\mathbb F_q\) be an arbitrary finite field of prime-power order \(q\ge2\). Write \(U_n=\mathrm U(n,\mathbb F_q)\) for the \(T=n(n+1)/2\)-dimensional space of upper triangular \(n\times n\) matrices. For \(M\in U_n\), let \(M_{[k]}\) be the submatrix in its first \(k\) rows and columns \(k,\ldots,n\). Define
\[
\mathrm{fr}(M)=\sum_{k=1}^n\mathrm{rank}_{\mathbb F_q}(M_{[k]}),
\quad d_{\mathrm{fr}}(M,N)=\mathrm{fr}(M-N).
\]
A linear code \(C\le U_n\) is **perfect with minimum distance three** when its minimum nonzero flag-rank weight is exactly \(3\) and the closed radius-one balls centered at its words partition \(U_n\).

Fix a surjective parity-check map \(H:U_n\to\mathbb F_q^{\alpha}\) with \(C=\ker H\). Denote elementary matrices by \(E_{ij}\), and put
\[
u_i=H(E_{ii})\quad(1\le i\le n),\qquad
v_i=H(E_{i,i+1})\quad(1\le i<n).
\]
The claimed **complete classification** at the required length is: \(C\) is perfect with minimum distance three if and only if the projective points \([u_i]\) are every point of \(\mathrm{PG}(\alpha-1,q)\) exactly once, and
\[
v_i\notin\operatorname{span}_{\mathbb F_q}\{u_i,u_{i+1}\}
\quad (1\le i<n).
\]
All images \(H(E_{ij})\) with \(j\ge i+2\) may be prescribed arbitrarily. A postcomposition of \(H\) with an invertible linear map of the syndrome space does not change \(C\).

## Proof

**1. The complete low-weight obstruction.** If an entry \(M_{ij}\ne0\), then it occurs in every block \(M_{[k]}\) for \(i\le k\le j\). Therefore \(\mathrm{fr}(M)\ge j-i+1\). A matrix of weight at most two consequently has support only on the diagonal and first superdiagonal. With no nonzero superdiagonal entry, the flag-rank weight equals the number of nonzero diagonal entries. With a nonzero entry at \((i,i+1)\), there can be no other nonzero superdiagonal entry and no nonzero diagonal entry outside \(i,i+1\): otherwise at least three distinct corner blocks have positive rank. Conversely, any matrix with a nonzero \((i,i+1)\) entry and arbitrary entries at \((i,i)\), \((i+1,i+1)\), all other entries zero, has exactly two nonzero corner blocks, each of rank one, and hence weight two. This establishes an exhaustive classification of weights one and two.

**2. Parity checks for distance at least three.** The preceding classification implies that \(\ker H\) contains no nonzero matrix of flag-rank weight one or two exactly when: (a) every \(u_i\ne0\); (b) no two \(u_i,u_j\) are proportional; and (c) every \(v_i\) is outside \(\operatorname{span}\{u_i,u_{i+1}\}\). Indeed, each forbidden kernel vector would be a one- or two-diagonal-support dependency or a dependency in \(u_i,v_i,u_{i+1}\), and any such dependency gives one of the classified low-weight matrices. Nothing on higher superdiagonals can create a low-weight vector.

**3. Necessity of the length.** The radius-one ball about zero consists of zero and the \(n(q-1)\) nonzero diagonal multiples \(aE_{ii}\). If \(C\) has codimension \(\alpha\), the disjoint balls fill \(U_n\) exactly when
\[
q^{T-\alpha}(1+n(q-1))=q^T,
\quad\text{or}\quad n=(q^{\alpha}-1)/(q-1).
\]
The low-weight criterion forces \([u_i]\) pairwise distinct. Since this value of \(n\) is the number of points of \(\mathrm{PG}(\alpha-1,q)\), the diagonal images must exhaust that projective space. For \(\alpha\le2\), the condition on \(v_i\) cannot hold: for \(\alpha=2\) each pair of distinct projective columns spans the whole two-dimensional syndrome space; for \(\alpha\le1\) the required minimum distance three is impossible. Thus \(\alpha\ge3\).

**4. Existence for every \(\alpha\ge3\).** Choose one nonzero representative of every point of \(\mathrm{PG}(\alpha-1,q)\), and assign the representatives bijectively to \(u_1,\ldots,u_n\). Choose \(v_i\) outside the two-dimensional span of \(u_i,u_{i+1}\), possible because \(\alpha\ge3\). Assign arbitrary images to all higher-superdiagonal basis elements. The diagonal images span the syndrome space, so \(H\) is surjective. Step 2 ensures minimum distance at least three. Among the included projective points, choose any two independent directions and the projective direction of their sum. A nonzero linear relation supported on these three diagonal positions supplies a nonzero kernel matrix of flag-rank weight exactly three. Hence the minimum distance is exactly three. The \(q^{\alpha}\) syndromes are covered uniquely by the zero vector and diagonal weight-one errors, so the radius-one balls partition \(U_n\).

**5. Exact enumeration.** For a fixed labeled matrix-coordinate system, there are \(n!\) ways to assign the complete projective point set to the ordered diagonal positions and \((q-1)^n\) choices of nonzero representatives. Each of the \(n-1\) first-superdiagonal basis images has exactly \(q^{\alpha}-q^2\) choices outside its forbidden two-space. The \((n-1)(n-2)/2\) higher-superdiagonal basis images are unrestricted, with \(q^{\alpha}\) choices apiece. Each resulting map is surjective, and two surjective maps have identical kernels if and only if they differ by unique postcomposition with a member of \(\mathrm{GL}(\alpha,q)\). The action is free and
\[
|\mathrm{GL}(\alpha,q)|=\prod_{j=0}^{\alpha-1}(q^{\alpha}-q^j).
\]
Dividing the number of maps by this order yields the displayed count, with no overcounting or implicit equivalence quotient.

## Verification

The accompanying standalone Python program directly reconstructs the corner-block ranks for every candidate low-weight matrix in the finite instances \((q,\alpha)=(2,3),(2,4),(3,3),(5,3)\), verifies the constructed syndrome map, and finds a weight-three kernel witness. It independently inspects all \(2^{13}=8192\) binary first-two-diagonal matrices when \((q,\alpha)=(2,3)\), recovering exactly \(1\), \(7\), and \(45\) matrices of respective flag-rank weights zero, one and two. It verifies the integer count
\[
\mathfrak P_{2,3}=4{,}323{,}455{,}642{,}275{,}676{,}160.
\]
The execution record ends in `VERIFY_OK`. These finite checks test the proof's local classification and construction; the unrestricted prime-power theorem follows from the analytic argument above, not from enumeration.

## Relationship to prior work

Alfarano, Neri and Zullo (2023/2024), *Maximum Flag-Rank Distance Codes*, Proposition 4.16 and Proposition 4.19, classified low-weight obstructions for a rank-three parity-check construction, and Construction C / Theorem 4.20 constructed maximum flag-rank-distance codes with codimension \(3\), up to length \(q^2+q+1\). Alfarano, Mushrraf and Zullo (June 11, 2026), *On perfect flag-rank metric codes*, Theorem 5.4 established the numerical condition \(n=(q^{\alpha}-1)/(q-1)\) **conditional on an already existing distance-three code**, and Theorem 5.8 constructed the \(\alpha=3\) perfect case. Both contributions are premises, not new claims here.

The present result completes existence at **all** codimensions \(\alpha\ge3\), provides a kernel-level classification allowing unrestricted images on higher diagonals, and counts every distinct labeled linear code. The numerical condition alone does not construct a code when \(\alpha\ge4\), and the prior rank-three construction does not count all perfect subspaces, even at codimension three.

## Limitations

The theorem concerns **linear** codes of minimum distance exactly three and radius-one perfectness. It neither classifies nonlinear perfect codes nor treats perfect codes of larger decoding radii. The count is of distinct subspaces with coordinates fixed, not isometry classes. The verifier implements selected **prime** fields; the proof covers all prime powers. Prior structural ingredients are fully credited, and an equivalent independently published enumeration not located in the checked sources remains an originality risk. No independent validation has been performed.

## References

1. G. N. Alfarano, U. Mushrraf, F. Zullo, *On perfect flag-rank metric codes*, arXiv:2606.12934, first public June 11, 2026. https://arxiv.org/abs/2606.12934 . Sections 2–5, especially Propositions 3.1–3.2 and Theorems 5.4 and 5.8.
2. G. N. Alfarano, A. Neri, F. Zullo, *Maximum Flag-Rank Distance Codes*, arXiv:2303.16653 (2023); J. Combin. Theory Ser. A 207 (2024), 105908. https://arxiv.org/abs/2303.16653 . Section 4.3.2, especially Propositions 4.16 and 4.19, Construction C, Theorem 4.20.
