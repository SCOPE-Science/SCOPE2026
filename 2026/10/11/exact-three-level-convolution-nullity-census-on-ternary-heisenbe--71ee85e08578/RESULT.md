# Exact three-level convolution nullity census on ternary Heisenberg groups

## Finding
For every integer \(n\geq1\), put \(Q=3^{2n}\), and let \(G\) be the extraspecial exponent-three Heisenberg group of order \(3Q\) defined below. For each unordered three-element subset \(S\subset G\), let
\[
T_S:\mathbb C[G]\longrightarrow\mathbb C[G],\qquad
(T_Sf)(g)=\sum_{s\in S}f(s^{-1}g).
\]
Every such convolution operator is singular. There are precisely three possible complex nullities, with the following exact census over all \(\binom{3Q}{3}\) supports:

| Complex nullity | Number of unordered three-element supports |
| --- | ---: |
| \(2Q\) | \(Q(3Q-1)/2\) |
| \(2Q/3\) | \(3Q(Q-1)^2/2\) |
| \(2Q/9\) | \(3Q^2(Q-1)\) |

These classes admit a complete geometric description in the quotient symplectic vector space. The top nullity occurs exactly when \(S\) is a whole central coset or a coset of a noncentral cyclic subgroup of order three. The middle nullity occurs if the quotient image has exactly two distinct points, if it is an affine line but \(S\) is not a cyclic subgroup coset, or if its three quotient points are affinely independent and their two difference directions are symplectically orthogonal. The bottom nullity occurs exactly when those two independent difference directions have nonzero symplectic pairing. In particular, the middle isotropic-independent case exists only for \(n\geq2\).

## Assumptions and scope
Let \(V=\mathbb F_3^n\oplus\mathbb F_3^n\). For \(v=(x,y)\), \(w=(x',y')\), define
\[
\omega(v,w)=x\cdot y'-y\cdot x'\in\mathbb F_3.
\]
Set \(G=V\times\mathbb F_3\) with multiplication
\[
(v,t)(w,s)=\bigl(v+w,t+s+2\omega(v,w)\bigr).
\]
Here all additions and products in the group formula are in \(\mathbb F_3\); multiplication by \(2\) represents division by \(2\). This group has exponent three, center \(Z=\{(0,t):t\in\mathbb F_3\}\), and quotient projection \(\pi:G\to V\). Each support comprises three **distinct**, unweighted elements, and the rank and kernel are taken over \(\mathbb C\), not in characteristic three.

If \(\pi(S)\) comprises three distinct noncollinear points, choose any \(s_0\in S\) and write the other projected differences as \(A=\pi(s_0^{-1}s_1)\), \(B=\pi(s_0^{-1}s_2)\). Then the last two cases above are distinguished by \(\omega(A,B)=0\) or \(\omega(A,B)\neq0\); this condition is independent of the choice and order of the three points. When \(\pi(S)\) is an affine line, the stated cyclic-coset criterion is intrinsic.

## Proof
**1. Fourier reduction.** Left translation of \(S\) does not change the nullity. Write the translated support as \(\{e,a,b\}\). Let \(d=3^n\), so \(d^2=Q\), and let \(\zeta=e^{2\pi i/3}\). The irreducible complex representations of \(G\) consist of \(Q\) one-dimensional characters \(\chi_\xi\), indexed by \(\xi\in V^*\), together with two representations \(\rho_h\) of dimension \(d\), \(h\in\{1,2\}\), having central character \(\rho_h(0,t)=\zeta^{ht}I\). Indeed, an explicit model on functions \(\phi:\mathbb F_3^n\to\mathbb C\) is
\[
[\rho_h((x,y),t)\phi](u)=\zeta^{h(t+2x\cdot y+y\cdot u)}\phi(u+x).
\]
Direct composition verifies the displayed group multiplication. Shifts and nontrivial diagonal phase operators generate the full matrix algebra, so these representations are irreducible; their distinct central characters make them inequivalent. Every central-trivial irreducible representation factors through the abelian quotient \(V\) and is one-dimensional, and the squared dimensions sum to \(Q+2d^2=3Q=|G|\). Therefore this is the complete irreducible list. The regular representation contains each irreducible representation with multiplicity its dimension. Consequently
\[
\operatorname{nullity}T_S
=\#\{\xi:1+\chi_\xi(a)+\chi_\xi(b)=0\}
+d\sum_{h=1}^{2}\dim\ker\bigl(I+\rho_h(a)+\rho_h(b)\bigr).
\]
For each noncentral element \(g\), the matrix \(\rho_h(g)\) has the three cubic roots of unity as eigenvalues, each repeated \(d/3\) times. Indeed \(g^3=e\), and the character trace of a noncentral element is zero in either nontrivial-central-character representation. For independent isotropic projections \(A,B\), the commuting matrices \(\rho_h(a),\rho_h(b)\) have each joint eigenvalue pair \((\zeta^j,\zeta^k)\) with multiplicity \(d/9\). This follows by Fourier inversion on \(\mathbb F_3^2\): every nonidentity product of their powers remains noncentral and hence has trace zero. Such an independent isotropic pair requires \(n\geq2\), so the displayed multiplicities are integers.

**2. Contributions of linear characters.** The scalar expression \(1+\zeta^j+\zeta^k\) vanishes exactly when \(\{j,k\}=\{1,2\}\). Therefore the linear-character contribution is zero if \(\pi(S)\) has fewer than three distinct points; it equals \(2Q/3\) when the image is a three-point affine line; and it equals \(2Q/9\) when the three projected points are affinely independent. These counts follow by applying the relevant one or two independent linear evaluations on \(V^*\).

**3. Contributions of the higher-dimensional representations.** There are five mutually exhaustive cases.

If \(\pi(S)\) is one point, then \(a,b\) are the two nontrivial central elements. Thus \(I+\rho_h(a)+\rho_h(b)=(1+\zeta^h+\zeta^{2h})I=0\), giving total nullity \(2d^2=2Q\).

If \(\pi(S)\) has two points, choose the normalizing basepoint from the projection fiber containing two support elements. Then exactly one of \(a,b\) is nontrivial central, and the other is noncentral, and exactly one of its three eigenvalues cancels the two scalar terms. Hence each higher-dimensional block has kernel dimension \(d/3\), giving total nullity \(2d(d/3)=2Q/3\).

If the image is an affine line, then \(A\neq0\) and \(B=-A\). The product \(ab\) is central. Writing \(U=\rho_h(a)\) and \(\rho_h(b)=\zeta^{hc}U^{-1}\), the block is \(I+U+\zeta^{hc}U^{-1}\). Its kernel is zero unless \(c=0\), because a sum of three cube roots of unity vanishes only when all three are different. If \(c=0\), namely \(b=a^{-1}\), the two nontrivial eigenvalues of \(U\) give a kernel of dimension \(2d/3\) in each block. Including the linear-character contribution, these cases have nullities respectively \(2Q/3\) and \(2Q\). The latter criterion is precisely that \(S\) be a coset of a noncentral cyclic order-three subgroup.

If the projected differences are independent and \(\omega(A,B)=0\), the blocks commute and the joint-eigenspace observation in Step 1 gives \(2d/9\) kernel dimensions per higher-dimensional representation: exactly the two joint eigenvalue pairs \((\zeta,\zeta^2)\) and \((\zeta^2,\zeta)\) vanish. Combined with \(2Q/9\) linear-character zeros, the total nullity is \(2Q/9+2d(2d/9)=2Q/3\).

Finally, if \(\omega(A,B)\neq0\), then \(U=\rho_h(a)\) and \(W=\rho_h(b)\) satisfy \(UW=\zeta^k WU\) for \(k\in\{1,2\}\) and \(U^3=W^3=I\). The cubic quantum-binomial identity gives \((U+W)^3=U^3+W^3=2I\). Therefore
\[
\bigl(I+U+W\bigr)\bigl(I-(U+W)+(U+W)^2\bigr)=3I,
\]
which proves that both higher-dimensional blocks are invertible. Their kernel contribution is zero and the total nullity is \(2Q/9\). The five cases prove the classification and show that every operator is singular.

**4. Exact counting.** Each projected point has three lifts. The numbers of supports with respectively one, two, and three distinct quotient points are \(Q\), \(9Q(Q-1)\), and \(27\binom Q3\). The quotient has \(Q(Q-1)/6\) affine lines (three points each); for every line there are \(27\) lifted triples, precisely \(9\) of which are cyclic-subgroup cosets. Hence the top-nullity count is
\[
Q+9\frac{Q(Q-1)}6=\frac{Q(3Q-1)}2.
\]
For affinely independent triples, fixing a first point and a nonzero first difference leaves \(Q/3-3\) orthogonal independent second differences and \(2Q/3\) nonorthogonal ones. Dividing ordered triples by \(6\), the numbers of projected isotropic and nonisotropic unordered triangles are
\[
\frac{Q(Q-1)(Q-9)}{18},\qquad \frac{Q^2(Q-1)}9.
\]
Each has \(27\) lifts. Thus the bottom-nullity count is \(27Q^2(Q-1)/9=3Q^2(Q-1)\). The remaining supports, or directly the sum of the two-projection, noncyclic-line, and isotropic-triangle counts, give \(3Q(Q-1)^2/2\) supports of middle nullity. All counts add to \(\binom{3Q}{3}\).

## Verification
The attached standalone C++17 program `heisenberg_check.cpp` constructs exact multiplication tables and three-term convolution matrices. It exhaustively evaluates all \(\binom{27}{3}=2925\) supports when \(n=1\), obtaining 117, 864, and 1944 supports at nullities 18, 6, and 2 respectively. It also checks twelve additional supports in the order-243 group when \(n=2\), including all three nullity classes. Matrix ranks are calculated modulo the prime \(1009\), independently of the representation-theoretic formula. This finite check supports but does not establish the complex-rank theorem; the proof above does.

To reproduce from the directory containing the file, run `g++ -std=c++17 -O2 -Wall -Wextra -pedantic heisenberg_check.cpp -o heisenberg_check` and then `./heisenberg_check`. The program terminates with a nonzero status if a rank comparison or stated finite census fails and prints `VERIFY_OK` on success.

## Relationship to prior work
DeDeo, Martínez, Medrano, Minei, Stark, and Terras studied finite Heisenberg-group graph spectra via representation blocks, especially four-generator symmetric Cayley graphs. Arezoomand and Taeri supplied a general characteristic-polynomial decomposition for Cayley digraphs over finite groups. Gibbons, Hoffman, and Wootters studied discrete Weyl operators and finite-field symplectic phase space. Those results supply the decomposition and commutation foundations, but the explicit three-tap nullity trichotomy, geometric equality conditions, and all-support multiplicities established here are not stated in the inspected results. General block diagonalization alone does not determine the cancellation modes or the symplectic triangle census.

## Limitations
The theorem applies to unweighted supports of exactly three distinct group elements in the extraspecial exponent-three group \(G\), and computes nullity over \(\mathbb C\). It does not classify weighted filters, other primes, or finite Heisenberg groups over nonfield rings. The modular finite checks are not certificates for all dimensions or for complex ranks. Although comparison with the specified primary literature did not identify an equivalent explicit census, equivalent historical formulations remain a possibility and independent mathematical review has not been performed.

## References
1. M. DeDeo, M. Martínez, A. Medrano, M. Minei, H. Stark, and A. Terras, *Spectra of Heisenberg Graphs over Finite Rings: Histograms, Zeta Functions and Butterflies*, authors' preprint, https://mathweb.ucsd.edu/~aterras/heis.pdf ; published version, *Conference Publications* (2003), DOI:10.3934/proc.2003.2003.213.
2. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, *Electronic Journal of Combinatorics* 20 (2013), #P57, DOI:10.37236/3105.
3. K. S. Gibbons, M. J. Hoffman, and W. K. Wootters, *Discrete phase space based on finite fields*, arXiv:quant-ph/0401155 (initial public posting 2004-01-25); *Physical Review A* 70 (2004), 062101.
