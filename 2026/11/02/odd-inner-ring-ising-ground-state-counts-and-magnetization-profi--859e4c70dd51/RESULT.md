# Odd-inner-ring Ising ground-state counts and magnetization profiles on generalized Petersen graphs

## Finding

Let \(n=4r+2\), where \(r\ge1\), and let \(G=GP(n,2)\) be the simple generalized Petersen graph with vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). For every \(J>0\), give every vertex a classical Ising spin \(\sigma_x\in\{-1,+1\}\) and define the zero-field antiferromagnetic Hamiltonian

\[
H(\sigma)=J\sum_{xy\in E(G)}\sigma_x\sigma_y.
\]

Put \(m=n/2=2r+1\) and denote the Fibonacci numbers by \(F_0=0\), \(F_1=1\), \(F_{m+2}=F_{m+1}+F_m\). Then the exact minimum energy and the number of *labelled* minimizing spin assignments are

\[
\boxed{\min_{\sigma}H(\sigma)=-2(n-1)J,\qquad
\#\{\sigma:H(\sigma)=-2(n-1)J\}=2m^2F_m.}
\]

Equivalently, the largest graph cut has \(5n/2-1\) edges, and precisely \(m^2F_m\) unordered bipartitions attain that cut size. **More strongly, the complete ground-state magnetization distribution is explicit.** Let \(M=\sum_x\sigma_x\) and define the coefficient

\[
A_m=
\begin{cases}
0,&m=3,\\
m\,[t^{(m-5)/2}](1-3t+t^2)^{-2},&m\ge5\text{ odd}.
\end{cases}
\]

Then

\[
\boxed{\#\{\sigma:H(\sigma)=\min H,\ M(\sigma)=M\}=
\begin{cases}
A_m,&M=+4\text{ or }-4,\\
2m^2F_m-2A_m,&M=0,\\
0,&\text{otherwise}.
\end{cases}}
\]

Thus **no ground state has magnetization outside \(\{0,\pm4\}\)**, despite the growing number of spins. The formula covers every \(n\equiv2\pmod4\) with \(n\ge6\), including the 12-vertex Dürer graph at \(n=6\). For \(n=6,10,14,18\), the labelled ground-state counts are \(36,250,1274,5508\), with \(M=+4\) multiplicities \(0,5,42,225\) respectively.

## Assumptions and scope

The graph is simple, with \(2n\) labelled vertices and exactly \(3n\) edges. Each edge has identical positive exchange \(J\); there is no field, disorder or boundary defect. Unordered cut bipartitions identify a spin configuration and its global spin reversal, whereas the ground-state count distinguishes them. The restriction \(n\equiv2\pmod4\) is essential: it makes the two inner cycles odd; a different previously studied law holds when \(4\mid n\).

## Proof

**1. A frustration lower bound.** Let \(e_o,e_s,e_i\) count edges whose endpoint spins are equal among outer, spoke, and inner edges, respectively; write \(f=e_o+e_s+e_i\). For every index \(i\), the five-edge cycle

\[
u_i,u_{i+1},u_{i+2},v_{i+2},v_i,u_i
\]

has an odd number of equal-spin edges and therefore at least one. Summing over its \(n\) cyclic translates counts each outer or spoke edge twice and each inner edge once. Hence \(n\le2e_o+2e_s+e_i=2f-e_i\). Since the inner graph has two disjoint cycles of odd length \(m=n/2\), at least one inner edge is frustrated on each, whence \(e_i\ge2\). Consequently \(f\ge m+1\). Since \(H/J=2f-3n\), every spin assignment satisfies \(H\ge-2(n-1)J\).

**2. A finite transfer matrix for exact multiplicities.** Encode spins by bits, with equal bits meaning equal spins. For an index \(i\), use the three-bit state \(s_i=(a_i,b_i,b_{i-1})\), where \(a_i\) and \(b_i\) are the outer and inner bits. In the lexicographic basis \(\{0,1\}^3\), define an \(8\times8\) polynomial matrix \(T(z)\) by

\[
T(z)_{(a,b,c),(a',b',c')}=
\begin{cases}
z^{[a=a']+[c=b']+[a=b]},&c'=b,\\
0,&c'\ne b.
\end{cases}
\]

Here \([P]\) is \(1\) when proposition \(P\) holds and \(0\) otherwise. Each closed walk \(s_0,\ldots,s_{n-1},s_n=s_0\) corresponds bijectively to one labelled spin assignment; the exponent sums each of the three kinds of graph edges exactly once. Thus

\[
Z_n(z):=\operatorname{tr}T(z)^n
=\sum_{\sigma}z^{f(\sigma)}.
\]

It follows that the number of ground states equals the coefficient of \(z^{m+1}\) in \(Z_{2m}(z)\), provided that coefficient is nonzero.

**3. Exact determinant extraction.** Define the formal determinant

\[
E(y,z)=\det\bigl(I_8-yz^{-1}T(z)^2\bigr).
\]

A direct finite \(8\times8\) determinant expansion, reproducible in `checker.py`, shows that all negative powers of \(z\) cancel and that

\[
\begin{aligned}
E(y,z)&=E_0(y)+zE_1(y)+O(z^2),\\
E_0(y)&=(1-3y^2+y^4)^2,\\
E_1(y)&=-2y(y-1)^2(y^4+8y^3+15y^2+8y+1).
\end{aligned}
\]

The determinant trace identity yields the exact formal-power-series equation

\[
-y\frac{\partial}{\partial y}\log E(y,z)
=\sum_{\ell\ge1}y^\ell z^{-\ell}Z_{2\ell}(z).
\]

Write the left side as \(R_0(y)+zR_1(y)+O(z^2)\). Then

\[
R_0(y)=-y\frac{E_0'(y)}{E_0(y)},\qquad
R_1(y)=-y\frac{d}{dy}\left(\frac{E_1(y)}{E_0(y)}\right).
\]

As \(E_0(y)\) is even, so is \(R_0(y)\); hence its coefficients of odd powers of \(y\) vanish. Let \(D=y\,d/dy\) and \(f(y)=y/(1-y-y^2)=\sum_{\ell\ge1}F_\ell y^\ell\). The elementary rational-function identity

\[
\frac{R_1(y)-R_1(-y)}2
=D^2f(y)-D^2f(-y)
=2\sum_{\substack{\ell\ge1\\\ell\ \mathrm{odd}}}\ell^2 F_\ell y^\ell
\]

is verified by substituting the displayed \(E_0,E_1\), differentiating, and clearing denominators; the checker reconstructs these operations exactly over \(\mathbb Z[y]\). For odd \(m\ge3\), the coefficient of \(y^m z\) in the trace identity is therefore \(2m^2F_m\). That is,

\[
[z^{m+1}]Z_{2m}(z)=2m^2F_m>0.
\]

The lower bound from Step 1 makes this the first possible nonzero coefficient, so its value proves both the exact energy and the exact labelled ground-state count. Dividing by two accounts for global spin reversal and proves the maximum-cut statements.

**4. Complete ground-state magnetization counts.** Introduce a second indeterminate \(w\) and replace every nonzero entry of the preceding transfer matrix by

\[
T(z,w)_{(a,b,c),(a',b',c')}=
 w^{a+b}z^{[a=a']+[c=b']+[a=b]}\quad(c'=b).
\]

Here bit \(1\) represents spin \(+1\), so the power of \(w\) counts positive spins. Write \(Z_{2m}(z,w)=\operatorname{tr}T(z,w)^{2m}\). The generating monomial for a spin assignment with magnetization \(M\) is \(w^{2m+M/2}\). Define a normalized formal determinant

\[
\widetilde E(Y,z,w)=\det\left(I_8-\frac{Y}{z w^2}T(z,w)^2\right)
=\widetilde E_0(Y,w)+z\widetilde E_1(Y,w)+O(z^2).
\]

A direct eight-state symbolic expansion gives \(\widetilde E_0=(1-3Y^2+Y^4)^2\), independent of \(w\). Since \(m\) is odd, only the odd-in-\(Y\) part of the next coefficient can contribute to the first allowed ground-state weight. The exact identity is

\[
\frac{\widetilde E_1(Y,w)-\widetilde E_1(-Y,w)}2
=-2Y^7+(2-w^2-w^{-2})Y^5-2Y.
\]

Every term in the normalized \(Y^m z\) coefficient of the logarithmic derivative \(-Y\partial_Y\log\widetilde E\) therefore has \(w\)-degree only \(0,+2,-2\), proving the asserted magnetization support. Each coefficient at \(w^{+2}\) and \(w^{-2}\) is exactly

\[
[Y^m]\;Y\frac{d}{dY}
\left(\frac{Y^5}{(1-3Y^2+Y^4)^2}\right)
=m\,[t^{(m-5)/2}](1-3t+t^2)^{-2}=A_m.
\]

This holds for every odd \(m\ge3\) with the negative-index coefficient interpreted as zero. Subtraction from the already proved total \(2m^2F_m\) gives the \(M=0\) multiplicity. The packaged checker independently verifies the weighted determinant identity exactly and checks the resulting magnetization counts through \(n=50\).

## Verification

The standalone `checker.py` constructs the eight transfer states from first principles. It checks both the unweighted and magnetization-weighted determinant identities symbolically over integer polynomial rings and verifies the odd Fibonacci rational-function identity without numerical approximation. It separately enumerates spin assignments on the actual graph for \(n=6\) and \(n=8\), and compares their exact minima and multiplicities with the transfer calculation. It additionally checks the min-plus transfer counts for all even \(n\) from \(6\) through \(202\) and the full magnetization profile for 12 sizes \(n=6,10,\ldots,50\). Execute `python3 checker.py` in an environment satisfying `requirements.txt`.

These finite tests are corroboration only: the arbitrary-size proof is the cycle inequality combined with the exact determinant and generating-function identities.

## Relationship to prior work

Jacobsen and Salas (first publicly submitted March 21, 2013) develop a general Potts-model partition-function transfer matrix for \(G(nk,k)\), including the Ising specialization. This implies algorithmic recovery of every finite-size coefficient, but the examined Ising section gives no closed formula for the lowest nonzero coefficient for \(G(4r+2,2)\), no quadratic-Fibonacci degeneracy law, and no magnetization-resolved ground-state distribution. The zero-field Potts partition function cannot by itself recover the latter because it does not track spin magnetization. The present claim is the explicit evaluation of the nontrivial coefficient **and its magnetization refinement**, not the existence of a transfer matrix or the general zero-field partition function.

Strečka, Karlová and Madaras (2015) give the exact 20-spin dodecahedral instance \(GP(10,2)\), including the already known total degeneracy \(250\) and its \(M=0,\pm4\) counts \(240,5,5\); this specific instance is not claimed as new. Sehrawat and Bhattacharjya (2019) study the maximum *over signings* of frustration indices, with bounds for \(\gcd(n,k)\ge2\). That optimization is different from counting maximum cuts for the fixed all-antiferromagnetic signing and does not yield the stated multiplicity. The case \(4\mid n\) has a separately established Lucas-law classification and is expressly excluded from the present claim. The \(n=10\) specialization has been previously computed for the regular dodecahedron; the new subject is the complete unbounded parity-class law, including the magnetization profile at all larger sizes.

## Limitations

No assertion is made for odd \(n\), for \(4\mid n\), for \(n<6\), for unequal couplings, external fields, finite temperature, or quantum-spin dynamics. The explicit closed form is extracted from a previously known kind of Potts/Ising transfer formalism, so priority should be assessed for this coefficient evaluation rather than the transfer framework. Historical searches may miss a specialized equivalent enumeration. There has been no independent scientific audit.

## References

1. J. L. Jacobsen and J. Salas, *A generalized Beraha conjecture for non-planar graphs*, arXiv:1303.5210v1 (first public submission March 21, 2013), https://arxiv.org/abs/1303.5210; full-text comparison: https://arxiv.org/html/1303.5210v2, especially Sections 2, 3, and 5.3.
2. J. Strečka, K. Karlová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449 (first submitted February 16, 2015), https://arxiv.org/abs/1502.04449, especially Table 5 for the 20-spin dodecahedron.
3. D. Sehrawat and B. Bhattacharjya, *Maximum Frustration in Signed Generalized Petersen Graphs*, arXiv:1905.05548v1 (May 14, 2019), https://arxiv.org/html/1905.05548v1, especially Section 4.
