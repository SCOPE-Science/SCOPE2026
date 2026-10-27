# Exact dyadic restoration periods for odd-cycle symplectic shears

## Finding
For every odd integer \(n\ge3\), let \(S\) be the cyclic permutation matrix of size \(n\), \(B=S+S^{-1}\), and
\[
T_n=\begin{pmatrix}I_n&B\\ I_n&I_n+B\end{pmatrix}\in\operatorname{Sp}_{2n}(\mathbb Z).
\]
For every integer \(s\ge1\), let \(P_n(s)\) be the least positive \(t\) such that \(T_n^t\equiv I_{2n}\pmod{2^s}\). Then the **exact global permutation order** on \((\mathbb Z/2^s\mathbb Z)^{2n}\) is
\[
\boxed{P_n(s)=\begin{cases}2n,&s=1,\\4n,&s=2\text{ or }s=3,\\n\,2^{s-1},&s\ge4.\end{cases}}
\]
In particular the modulus-four and modulus-eight orders coincide, although increasing every subsequent dyadic modulus doubles the order. The formula holds for every odd circumference, including all odd composite values.

## Assumptions and scope
The matrix \(S\) is the permutation \((Sv)_j=v_{j-1}\), with indices modulo \(n\). The block map acts on two copies of the cyclic spatial lattice by an upper shear with coupling \(B\) followed by a lower shear with identity coupling. Because \(B=B^{\mathsf T}\), both shears are integral symplectic and their product is \(T_n\). The precise shear convention matters: this is not the equal-shear map \(\bigl(\begin{smallmatrix}I&C\\ C&I+C^2\end{smallmatrix}\bigr)\). The conclusion concerns the order of the full permutation, not the primitive period of every point. The modulus is a power of two, and \(n\) is odd.

## Proof
**1. Exact order modulo two.** Work first over \(\mathbb F_2\). Since \(n\) is odd, \(x^n-1\) is separable over \(\mathbb F_2\). After extending scalars to a splitting field, the cyclic shift \(S\) has as eigenvalues all the distinct \(n\)-th roots \(\lambda\). On the corresponding two-dimensional block, the characteristic polynomial of \(T_n\) is
\[
X^2+(\lambda+\lambda^{-1})X+1=(X+\lambda)(X+\lambda^{-1}).
\]
For \(\lambda\ne1\), these roots are distinct, so that block is diagonalizable and its order divides \(n\). A primitive \(n\)-th root occurs, making the global order divisible by \(n\). For \(\lambda=1\), the block is \(\bigl(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\bigr)\), of exact order two. Hence the order modulo two is exactly \(2n\).

**2. A uniform congruence modulo four.** Set \(R=\mathbb Z[z,z^{-1}]/(z^n-1)\), let \(b=z+z^{-1}\), and identify \(T_n\) with the two-by-two matrix \(T\) over \(R\) obtained by replacing \(B\) with \(b\). Define integer polynomials \(U_0(w)=0\), \(U_1(w)=1\), and \(U_{m+1}(w)=wU_m(w)-U_{m-1}(w)\). The Cayley–Hamilton identity \(T^2-(b+2)T+I=0\) gives
\[
T^m=U_m(b+2)T-U_{m-1}(b+2)I.
\]
The Laurent identity
\[
U_m(z+z^{-1})=\sum_{j=0}^{m-1}z^{m-1-2j}
\]
holds over the integers. Write \(\Sigma=1+z+\cdots+z^{n-1}\). Since \(n\) is odd, the successive exponents differ by an invertible residue modulo \(n\). Thus, exactly in \(R\),
\[
U_{2n}(b)=2\Sigma,\qquad U_{2n-1}(b)=2\Sigma-1.
\]
The parity of \(U_{2n-1}\) implies \(U'_{2n-1}(w)\equiv0\pmod2\). The doubling identity \(U_{2n}(w)=U_n(w)(U_{n+1}(w)-U_{n-1}(w))\) implies, in characteristic two, \(U_{2n}(w)=wU_n(w)^2\), hence \(U'_{2n}(w)=U_n(w)^2\). Moreover \(U_n(b)\equiv\Sigma\pmod2\), and \(\Sigma^2\equiv\Sigma\pmod2\), because \(n\) is odd. Polynomial Taylor expansion modulo four therefore yields
\[
U_{2n}(b+2)\equiv2\Sigma+2\Sigma^2\equiv0\pmod4,
\qquad U_{2n-1}(b+2)\equiv2\Sigma-1\pmod4.
\]
Consequently,
\[
\boxed{T^{2n}\equiv I+2\Sigma I\pmod4.}
\]
Because \(\Sigma\not\equiv0\pmod2\), the order modulo four is not \(2n\). Squaring the displayed congruence and using the idempotence of \(\Sigma\) modulo two shows \(T^{4n}\equiv I\pmod8\). Therefore the exact orders modulo four and eight are both \(4n\).

**3. Sharp lifting past modulus eight.** Evaluate the quotient ring at \(z=1\), so \(b=2\), to obtain the integral two-by-two matrix
\[
H=\begin{pmatrix}1&2\\1&3\end{pmatrix},\qquad H^4-I=8\begin{pmatrix}5&14\\7&19\end{pmatrix}.
\]
Since \(n\) is odd, \(H^{4n}\not\equiv I\pmod{16}\). Thus \(T^{4n}=I+8E\), where at least one coefficient of \(E\) is odd, in the faithful Laurent-circulant representation. Whenever \(Q=I+2^kE\) with \(k\ge3\) and \(E\not\equiv0\pmod2\),
\[
Q^2-I=2^{k+1}(E+2^{k-1}E^2)
\]
has exact coefficientwise two-adic valuation \(k+1\). Repeated squaring raises the exact valuation by one each time. Since the order modulo eight is \(4n\), the kernels of the consecutive reductions of matrix groups are two-groups, and a proper odd factor cannot disappear, this proves \(P_n(s)=4n\,2^{s-3}\) for every \(s\ge3\), completing the stated formula.

## Verification
The self-contained `verify.py` performs arithmetic in the faithful quotient \((\mathbb Z/2^s\mathbb Z)[z]/(z^n-1)\) without floating-point calculations. For every odd \(n\) from \(3\) to \(25\) and every \(1\le s\le10\), it checks the predicted identity exponent and every prime-divisor reduction. It separately checks the exact congruence modulo four, the modulus-eight plateau, and nontriviality modulo sixteen. Run `python3 verify.py`; the expected output begins with `VERIFY_OK` and reports 416 checks. The infinite-family proof is the algebraic argument above, not the finite sample.

## Relationship to prior work
Nance's 2011 treatment of discretized Arnold cat maps and higher-dimensional constructions supplies historical finite-torus motivation but no corresponding graph-cyclic all-odd-order theorem. Manolas and Floratos study a different, **equal-shear** symplectic circulant family \(M(C)=\bigl(\begin{smallmatrix}I&C\\ C&I+C^2\end{smallmatrix}\bigr)\), derive numerical period spectra, and discuss dyadic scaling. Their finite-volume conclusions do not directly imply the period of the **unequal-shear** map in this note: our characteristic trace is \(2+B\), rather than \(2+C^2\). A published exact classification for the complete-graph equal-shear family is likewise not an odd-cycle unequal-shear classification. The shear construction and the classical integer-polynomial recurrence are background tools; what is claimed here is the exact all-odd-size dyadic-order law for the stated map.

## Limitations
No assertion is made about even spatial sizes, odd prime-power moduli, individual orbit-length distributions, or the continuous-torus Lyapunov spectrum. An explicit closed all-size formula for one symplectic shear family does not settle the period problem for arbitrary circulant coupled cat maps. The originality comparison is limited to the identified and materially inspected sources; historical priority still requires independent checking.

## References
1. J. Nance, *Periods of the discretized Arnold Cat Map and its extension to n dimensions*, arXiv:1111.2984, first public November 13, 2011. https://arxiv.org/abs/1111.2984
2. K. Manolas and E. Floratos, *Coupled Arnol'd cat maps on circulant graphs*, arXiv:2605.00965, first public May 1, 2026, especially Sections 3–5. https://arxiv.org/abs/2605.00965
3. F. J. Dyson and H. Falk, *Period of a discrete cat mapping*, American Mathematical Monthly 99 (1992), 603–614, DOI:10.1080/00029890.1992.11995900.
4. *Exact powers-of-two torus orders for all-to-all coupled cat maps*, public mathematical result, 2026; its equal-shear complete-graph theorem provides a closely related but non-covering comparison.
