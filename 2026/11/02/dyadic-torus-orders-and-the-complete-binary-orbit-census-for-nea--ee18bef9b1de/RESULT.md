# Dyadic torus orders and the complete binary orbit census for nearest-neighbor coupled cat maps

## Finding
For every integer \(k\ge2\), let \(n=2^k\) and let \(P\) be the cyclic shift on \(n\) sites. Put \(C=P+P^{-1}\) and form the integral symplectic cat-map matrix
\[
L=\begin{pmatrix}0&I_n\\ I_n&C\end{pmatrix},\qquad M=L^2=\begin{pmatrix}I_n&C\\C&I_n+C^2\end{pmatrix}.
\]
For every integer \(s\ge1\), the induced permutation on the finite torus \((\mathbb Z/2^s\mathbb Z)^{2n}\) has **exact global order**
\[
\operatorname{ord}_{2^s}(M)=2^{k+s-2}=\frac n2\,2^{s-1}.
\]
Exactly \(2^{4s}\) phase configurations are fixed points at resolution \(2^s\).

For the binary torus \(s=1\), all primitive cycle lengths are precisely \(1,2,4,\ldots,2^{k-1}\). With \(f_j=2^{2\min(2^{j+1},n)}\) for \(j\ge0\), and \(f_{-1}=0\), the number of primitive cycles of length \(2^j\), \(0\le j\le k-1\), is
\[
a_j=\frac{f_j-f_{j-1}}{2^j}.
\]
Equivalently \(a_0=16\) and, for \(1\le j\le k-1\),
\[
a_j=\frac{2^{4\cdot2^j}-2^{4\cdot2^{j-1}}}{2^j}.
\]
Thus the binary Artin–Mazur zeta function equals
\[
\zeta_M(z)=\prod_{j=0}^{k-1}(1-z^{2^j})^{-a_j},
\]
and exactly a fraction \(1-2^{-n}\) of binary configurations have the maximal primitive period \(n/2\).

## Assumptions and scope
The underlying graph is the simple unweighted nearest-neighbor cycle on \(n=2^k\ge4\) vertices. The shift \(P\) satisfies \(P^n=I_n\), and the adjacency matrix is \(P+P^{-1}\) over integers before reduction. Both position and momentum have \(n\) coordinates, each reduced modulo \(2^s\). Matrix \(L\) is invertible over integers since \(L^{-1}=\begin{pmatrix}-C&I_n\\I_n&0\end{pmatrix}\); hence \(M\) permutes every finite phase grid. Statements concern the full matrix order and exact individual binary orbits, not only typical states or numerically estimated periods. Here \(k\) and \(s\) are arbitrary positive integers with \(k\ge2\), \(s\ge1\).

## Proof
**1. Binary nilpotent structure and exact order.** Work over \(\mathbb F_2\) and identify circulants with \(R=\mathbb F_2[z]/(z^n-1)\). Because \(n\) is a power of two, \(z^n-1=(z+1)^n\) in this ring, while
\[
C=z+z^{-1}=z^{-1}(z+1)^2.
\]
Consequently \(C\) has nilpotency index \(t=n/2\): \(C^t=0\), but \(C^{t-1}\ne0\). With \(X=CL=M-I_{2n}\), the matrices \(C\) (acting diagonally on the two blocks) and \(L\) commute. Frobenius gives
\[
M^{2^j}-I_{2n}=(I_{2n}+X)^{2^j}-I_{2n}=X^{2^j}=C^{2^j}L^{2^j}\pmod2.
\]
Since \(L\) is invertible, \(M^{2^j}=I\) first occurs at \(2^j=t\). Its binary order is exactly \(t=2^{k-1}\).

**2. Binary fixed-space ranks and orbit census.** Multiplication by \(C^h=z^{-h}(z+1)^{2h}\) on \(R\) has nullity \(\min(2h,n)\). In the two-component phase space, invertibility of \(L^h\) gives
\[
\dim_{\mathbb F_2}\ker(M^h-I_{2n})=2\min(2h,n)
\]
for each dyadic \(h=2^j\). The fixed-point count is therefore \(f_j\). Every binary orbit has a power-of-two length dividing \(t\), so subtracting the previous fixed-point count yields \(2^j a_j=f_j-f_{j-1}\). For the maximal period, subtract \(f_{k-2}=2^n\) from the total \(2^{2n}\), obtaining the fraction \(1-2^{-n}\). The product for the dynamical zeta function follows from the periodic-orbit Euler product.

**3. A nontrivial dyadic lift (the critical nonstandard step).** From now on take the integral matrices before reduction, and let \(t=n/2\). The binomial coefficients of \((P+P^{-1})^t\) modulo four give
\[
C^t\equiv2(I_n+P^t)\pmod4.
\]
Indeed all intermediate binomial coefficients are divisible by four, except the middle one, congruent to two modulo four. Similarly,
\[
M^t=(I_{2n}+X)^t\equiv I_{2n}+X^t+2X^{t/2}\pmod4.
\]
Define \(E_1=(M^t-I_{2n})/2\), an integral matrix, and reduce it modulo two to \(E\). Put \(J=I_n+P^t\) and \(D=C^{t/2}\) over \(\mathbb F_2\), using the same letters for their two-block diagonal actions. Since
\[
L^t=(L^2)^{t/2}=(I_{2n}+CL)^{t/2}=I_{2n}+DL^{t/2}\pmod2,
\]
and \(JD=J^2=D^2=0\), the preceding congruences imply
\[
E=J I_{2n}+D L^{t/2},\qquad E^2=0\pmod2.
\]
Crucially \(E\ne0\). To prove this rather than infer it from finite experiments, note the off-diagonal block identity
\[
(L^{2^r})_{12}=C^{2^r-1}\pmod2\quad(r\ge0).
\]
It holds for \(r=0\). If it holds for \(r\), squaring the \(2\times2\) block matrix multiplies its off-diagonal block by its trace, which is \(C^{2^r}\) over characteristic two, giving the induction. Thus the upper-right block of \(E\) is \(C^{t/2}C^{t/2-1}=C^{t-1}\ne0\).

It follows that \(M^t=I_{2n}+2E_1\) has exact matrix two-adic valuation one, and
\[
M^{2t}=I_{2n}+4(E_1+E_1^2)
\]
has exact valuation two, because \(E_1+E_1^2\equiv E\ne0\pmod2\). More generally, if \(U=I_{2n}+2^r H\) for \(r\ge2\) and \(H\not\equiv0\pmod2\), then
\[
U^2=I_{2n}+2^{r+1}(H+2^{r-1}H^2),
\]
where the last parenthesis remains nonzero modulo two. Inductively \(M^{t2^{s-1}}=I\pmod{2^s}\), while for \(s\ge2\), \(M^{t2^{s-2}}\ne I\pmod{2^s}\); the binary case was handled in Step 1. Since the proposed order is a power of two, these two facts force the exact order stated.

**4. Fixed points at any dyadic resolution.** Since \(M-I_{2n}=CL\) and \(L\) is invertible, its kernel over \(\mathbb Z/2^s\mathbb Z\) is isomorphic to the kernel of diagonal \(C\) on two copies. The equation \(Cx=0\) on the cycle says \(x_{i+2}=-x_i\). As \(n\) is a multiple of four, any independent choices of \(x_0,x_1\) extend consistently, giving exactly \(2^{2s}\) possible \(n\)-vectors in each copy. There are therefore exactly \(2^{4s}\) fixed phase configurations. This completes all claims.

## Verification
The standalone Python 3 script `artifacts/verify_cat_cycle.py` constructs the full integer-modulus matrix, confirms its order for \(n\in\{4,8,16,32\}\) and \(1\le s\le6\), checks the binary nullity formula, and exhaustively enumerates all orbits for \(n=4\) and \(n=8\). It passed 64 independent comparisons and found the exact cycle counts \(\{1:16,2:120\}\) and \(\{1:16,2:120,4:16320\}\), respectively. Its finite checks corroborate but do not prove the arbitrary-size and arbitrary-resolution theorem; the proof above establishes those cases.

## Relationship to prior work
Manolas and Floratos [1], Sections 3–4.1, introduce precisely the same symplectic two-block family with symmetric circulant couplings and give Fibonacci-polynomial recurrences, numerical period spectra and a dyadic-resolution scaling law in the studied examples. The theorem here specializes to the natural nearest-neighbor cycle at powers-of-two sizes and determines the previously unspecified base order, fixed-point counts at all resolutions, and the complete binary cycle census and zeta. Its dyadic scaling by itself is **not** claimed as new: the explicit contribution is the complete closed arithmetic classification for this infinite family. Axenides, Floratos and Nicolis [2] construct the parent coupled cat-map lattice and analyze period spectra, but their inspected corresponding discussion does not state this exact family-wide orbit census. More general cyclic linear automorphism theory provides tools for fixed-point counting, without by itself supplying the specific two-adic computation above.

## Limitations
The classification assumes simple cycles of sizes exact powers of two, unweighted nearest-neighbor coupling, and torus resolution a power of two. The full cycle census and zeta formula are for the binary torus only; the order and number of fixed points are established for all dyadic resolutions. It does not classify primitive orbit counts at higher dyadic resolutions, graph sizes that are not powers of two, or weighted couplings. Priority comparisons are based on the inspected sources, not an exhaustive guarantee against unpublished or unindexed work. This is a mathematical derivation with finite programmatic checks, not independent external certification.

## References
[1] K. Manolas and E. Floratos, "Coupled Arnol’d cat maps on circulant graphs," arXiv:2605.00965v1, first posted 2026-05-01; version 2 inspected: https://arxiv.org/html/2605.00965v2 (especially Sections 3–4.1).
[2] M. Axenides, E. Floratos, and S. Nicolis, "Arnol’d cat map lattices," arXiv:2208.03267, inspected version 3: https://arxiv.org/html/2208.03267v3 (especially Sections 3 and 6).
