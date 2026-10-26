# Ten-step Frobenius invisibility on the characteristic-two Klein cubic

## Finding
Let \(X\) be the smooth threefold over \(\mathbb F_2\) defined by
\[
X=V\!\left(\sum_{i\in\mathbb Z/5\mathbb Z}x_i^2x_{i+1}\right)\subset\mathbb P^4_{\mathbb F_2}.
\]
For its geometric Frobenius \(\Phi\) on \(H^3_{\mathrm{et}}(X_{\overline{\mathbb F}_2},\mathbb Q_\ell)\), with any prime \(\ell\ne2,11\), the degree-ten characteristic polynomial is
\[
\det(U-\Phi\mid H^3)=U^{10}+2^{15},\qquad
\det(1-T\Phi\mid H^3)=1+2^{15}T^{10}.
\]
Consequently the exact Hasse--Weil zeta function is
\[
Z(X,T)=\frac{1+2^{15}T^{10}}{(1-T)(1-2T)(1-4T)(1-8T)}.
\]
For every positive integer \(n\), write \(q=2^n\). Then
\[
\#X(\mathbb F_q)=1+q+q^2+q^3-
\begin{cases}
0,&10\nmid n,\\
10(-2^{15})^{n/10},&10\mid n.
\end{cases}
\]
In particular the counts agree exactly with \(\#\mathbb P^3(\mathbb F_{2^n})\) for all nine extension degrees \(1\le n\le9\), while
\[
\#X(\mathbb F_{2^{10}})=1075119105,
\]
which is \(327680\) greater than the projective-space count.

## Assumptions and scope
The equation, coordinate ordering, and descent model over the prime field \(\mathbb F_2\) are fixed. The zeta function concerns the cubic threefold itself, **not** the Fano surface of its lines, any quotient, or an arbitrary Galois twist. All cohomological calculations use \(\ell\)-adic etale cohomology with \(\ell\ne2,11\). The point-count identity holds for every positive integer extension degree, without a computational cutoff.

## Proof
**Smoothness.** Write \(F=\sum_i x_i^2x_{i+1}\) with indices modulo five. In characteristic two, \(\partial F/\partial x_i=x_{i-1}^2\). All five partial derivatives vanish only when all homogeneous coordinates are zero, so \(X\) is smooth.

**The ten-dimensional middle cohomology.** Weak Lefschetz and Poincare duality imply that only the third Betti number can differ from that of \(\mathbb P^3\). The tangent sequence of the smooth cubic hypersurface gives
\[
c(T_X)=\frac{(1+H)^5}{1+3H},\qquad c_3(T_X)=-2H^3.
\]
Since \(\int_X H^3=3\), the etale Gauss--Bonnet formula gives Euler characteristic \(-6\). The even Betti numbers are one in degrees \(0,2,4,6\), hence \(4-b_3=-6\), so \(b_3=10\). Frobenius acts by \(1,2,4,8\) on these four one-dimensional even groups.

**An order-eleven character basis.** Choose a primitive eleventh root of unity \(\zeta\) in the algebraic closure. The diagonal transformation
\[
g:[x_0:\cdots:x_4]\longmapsto
[\zeta x_0:\zeta^9x_1:\zeta^4x_2:\zeta^3x_3:\zeta^5x_4]
\]
preserves the cubic because the five weights \((1,9,4,3,5)\) obey \(2w_i+w_{i+1}\equiv0\pmod{11}\). They are pairwise distinct, so every nonidentity power of \(g\) fixes precisely the five coordinate points on \(X\). The fixed points are isolated and nondegenerate (no nontrivial tangent direction has eigenvalue one), and the action has order prime to the characteristic. The tame Lefschetz fixed-point formula therefore gives
\[
5=1+1+1+1-\operatorname{Tr}(g^j\mid H^3),\qquad
\operatorname{Tr}(g^j\mid H^3)=-1\quad(1\le j\le10).
\]
Together with \(\dim H^3=10\), Fourier inversion on the cyclic group of order eleven shows that the trivial character has multiplicity zero and **each nontrivial character has multiplicity one**. Indeed the multiplicities are \((10-10)/11=0\) and \((10+1)/11=1\), respectively. Thus after extending coefficient scalars to a field containing \(\zeta\), the third cohomology is a direct sum of ten distinct one-dimensional character spaces.

**Frobenius gives a single ten-cycle.** On the defining diagonal automorphism, arithmetic Galois conjugation sends \(g\) to \(g^2\). Correspondingly, geometric Frobenius permutes its nontrivial character spaces by multiplication by \(2\) or its inverse modulo eleven (depending on cohomological convention). The order of \(2\) modulo eleven is exactly ten, so these ten spaces form **one** Frobenius cycle. Therefore the characteristic polynomial of Frobenius on \(H^3\) has the shape \(U^{10}-c\), and its determinant is \(-c\).

**Determine the constant by duality.** The alternating cup product
\[
H^3\times H^3\longrightarrow H^6\cong\mathbb Q_\ell(-3)
\]
is perfect and Frobenius-equivariant. Thus Frobenius is a symplectic similitude of multiplier \(2^3\) on a ten-dimensional space. The determinant of such a similitude is the fifth power of its multiplier, namely \(2^{15}\). Hence \(-c=2^{15}\), so \(c=-2^{15}\). This proves \(\det(U-\Phi)=U^{10}+2^{15}\), equivalently \(\det(1-T\Phi)=1+2^{15}T^{10}\).

**Zeta function and every extension.** The cohomological trace formula now gives the displayed rational zeta function. The ten eigenvalues have tenth power \(-2^{15}\). Their power sum is zero unless \(10\mid n\); for \(n=10m\) it equals \(10(-2^{15})^m\). Subtracting this middle-cohomology trace from the four even-cohomology contributions proves the point-count formula for all \(n\ge1\).

## Verification
The accompanying standalone `verify_counts.cpp` exhaustively enumerates all \(\mathbb F_{2^n}\)-rational points for \(1\le n\le7\), using explicit degree-\(n\) binary field models and canonical projective representatives. It independently returns the counts
\[
15,\ 85,\ 585,\ 4369,\ 33825,\ 266305,\ 2113665,
\]
matching \(1+2^n+2^{2n}+2^{3n}\) in all seven cases. The independent `verify_symmetry.py` checks all five weight congruences, that the residue of two has multiplicative order ten modulo eleven, that the character multiplicities and determinant sign are as stated, and the closed counting formula. The finite enumerations corroborate the theorem; they do not replace its cohomological proof for infinitely many extensions.

For a compiler supporting C++17, run `g++ -O3 -std=c++17 verify_counts.cpp -o verify_counts && ./verify_counts`; run `python3 verify_symmetry.py` separately. Both programs terminate with `VERIFY_OK` after all assertions pass.

## Relationship to prior work
The complex Klein cubic, its order-eleven automorphism, and its Fano surface have an established literature (Roulleau; Gonzalez-Aguilera--Liendo). Ciurca studies the characteristic-two Hermitian Klein cubic and explicitly obtains the trace \(-1\) of its order-eleven automorphism on middle cohomology. Those geometric and character-theoretic ingredients are not claimed as new. Roulleau's finite-field zeta-function work focuses on Fano surfaces in characteristic different from two. The additional assertion here is the **prime-field arithmetic Frobenius cycle**, its constant determined by symplectic duality, and the resulting explicit zeta function and all-extension point counts for this fixed \(\mathbb F_2\) model. A general theorem on twists of Hermitian cubics might subsume the numerical result; no such exact specialization was located in the inspected material.

## Limitations
No independent mathematical audit has been carried out. The argument does not determine the zeta function of the Fano surface, nor the arithmetic of other twists. Exhaustive computations stop at extension degree seven; the universal formulas instead rest on the complete cohomological argument. Published Hermitian-variety and twisting results may give stronger general coverage not identified in the targeted comparison, and a search cannot establish uniqueness or novelty.

## References
1. X. Roulleau, *The Fano surface of the Klein cubic threefold*, arXiv:1001.4853v1 (first publicly posted 2010-01-27), https://arxiv.org/pdf/1001.4853 .
2. V. Gonzalez-Aguilera and A. Liendo, *Automorphisms of prime order of smooth cubic n-folds*, arXiv:1002.4136, https://arxiv.org/pdf/1002.4136 .
3. X. Roulleau, *The zeta functions of the Fano surfaces of cubic threefolds*, arXiv:1304.4076, https://arxiv.org/pdf/1304.4076 .
4. T. Ciurca, *Prym Varieties and Cubic Threefolds over Z*, University of Bath thesis (2025), Chapter 4, especially the Klein-cubic order-eleven cohomological trace in the characteristic-two argument, https://purehost.bath.ac.uk/ws/portalfiles/portal/373426370/Prym_varieties_and_cubic_threefolds_over_Z.pdf .
