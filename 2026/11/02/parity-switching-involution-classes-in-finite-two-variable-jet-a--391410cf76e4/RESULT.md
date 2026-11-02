# Parity-switching involution classes in finite two-variable jet automorphism groups

## Finding
For every odd prime power \(q\) and integer \(N\ge3\), put
\[
R_N=\mathbb F_q[x,y]/(x,y)^N,\qquad G_N=\operatorname{Aut}_{\mathbb F_q}(R_N),
\]
and define the integers
\[
D_N=N(N+1)-6,\qquad
E_N=2\sum_{\substack{2\le s<N\\s\ \mathrm{even}}}(s+1).
\]
The elements of \(G_N\) whose order divides two form exactly **three conjugacy classes**, including the identity. Their linear-part types and exact class sizes are:

| Linear part of an involution | Conjugacy-class size |
| --- | ---: |
| \(I_2\) | \(1\) |
| \(-I_2\) | \(q^{E_N}\) |
| \(\operatorname{diag}(1,-1)\) | \(q(q+1)q^{D_N/2}\) |

Consequently the exact number of elements with order dividing two is
\[
\boxed{T_N(q)=1+q^{E_N}+q(q+1)q^{D_N/2}.}
\]
The two nonidentity types alternate in their asymptotic dominance as the jet length grows at fixed \(q\):
\[
\begin{aligned}
\Pr\bigl(L(f)=-I_2\mid f\ne1,\ f^2=1\bigr)&\longrightarrow1
&&\text{along odd }N,\\
\Pr\bigl(L(f)\sim\operatorname{diag}(1,-1)\mid f\ne1,\ f^2=1\bigr)&\longrightarrow1
&&\text{along even }N.
\end{aligned}
\]
More explicitly, for \(N=2r+1\), \(E_N-D_N/2=r+2\), whereas for \(N=2r\), \(E_N-D_N/2=1-r\). The conjugacy classification itself follows from classical tame finite-order linearization; the assessed result is the evaluated class-size formula and the parity switch.

## Assumptions and scope
All automorphisms are unital \(\mathbb F_q\)-algebra automorphisms, and \((x,y)^N\) means the ideal of all monomials of total degree at least \(N\). The group acts by substituting arbitrary polynomials of positive degree less than \(N\) with invertible \(2\times2\) linear part. Because \(q\) is odd, every order-two linear map is diagonalizable with eigenvalues in \(\{1,-1\}\), and division by two is valid. The formulas apply to all odd prime powers, including nonprime finite fields. \(N\ge3\) is stipulated; the \(N=2\) case reduces to \(\operatorname{GL}_2(q)\).

## Proof
**Step 1: split the group and count nonlinear coordinates.** Each substitution's linear part induces a split epimorphism \(L:G_N\to\operatorname{GL}_2(q)\), with kernel \(U_N\), the substitutions tangent to the identity. Every arbitrary assignment of the nonlinear coefficients yields an automorphism, by successive inversion in the maximal-ideal filtration. For every homogeneous total degree \(s\), there are \(s+1\) monomials and two coordinate outputs. Thus
\[
|U_N|=q^{\,2\sum_{s=2}^{N-1}(s+1)}=q^{D_N},
\]
and \(G_N=U_N\rtimes\operatorname{GL}_2(q)\).

**Step 2: parameterize involutions in each linear fiber.** If \(f^2=1\) and \(L(f)=A\), then \(A^2=I_2\). Set
\[
h=\tfrac12\bigl(\operatorname{id}+A^{-1}\circ f\bigr).
\]
Here the sum and the scalar factor act coordinatewise on the ordered pair of substitution polynomials (not on algebra homomorphisms as linear maps). This pair has identity linear part, hence defines an element of \(U_N\). Directly, using \(f^2=A^2=1\),
\[
h\circ f=\tfrac12(f+A^{-1})=A\circ h.
\]
Therefore \(f=h^{-1}Ah\). Conversely every such conjugate is an involution with linear part \(A\). Hence the involutions in the fiber above \(A\) form one orbit under \(U_N\), of size
\[
|U_N:C_{U_N}(A)|.
\]
This explicit averaging argument is a special case of the classical finite-order formal linearization theorem and is not asserted as new.

**Step 3: centralizing coefficient count.** For \(A=-I_2\), a nonlinear monomial of degree \(s\) acquires the scalar \((-1)^s\), whereas each output acquires \(-1\). Thus the coefficients commuting with \(A\) are exactly those in odd degrees \(s\); all even-degree coefficients contribute to the orbit size. The exponent of the latter is \(E_N\), yielding \(q^{E_N}\) involutions above \(-I_2\). For \(A=I_2\), the entire \(U_N\) centralizes it, yielding only the identity.

For \(A=\operatorname{diag}(1,-1)\), the input monomial \(x^a y^b\) has sign \((-1)^b\). Exactly one of the two output coordinates has the same sign. Hence at each degree there are exactly \(s+1\) commuting coefficients out of \(2(s+1)\), giving
\[
|C_{U_N}(A)|=q^{D_N/2},\qquad
|U_N:C_{U_N}(A)|=q^{D_N/2}.
\]
No other linear involution types exist over a field of odd characteristic. The mixed linear involutions form one \(\operatorname{GL}_2(q)\)-conjugacy class, of size
\[
\frac{|\operatorname{GL}_2(q)|}{(q-1)^2}=q(q+1).
\]
The scalar linear classes consist of one matrix each. Combining these with the \(U_N\) orbits gives exactly three \(G_N\)-classes and the stated counts.

**Step 4: derive the alternating asymptotics.** For \(N=2r+1\), direct summation of even degrees gives \(E_N=2r(r+2)\) and \(D_N/2=2r^2+3r-2\), with difference \(r+2\). For \(N=2r\), \(E_N=2(r^2-1)\) and \(D_N/2=2r^2+r-3\), with difference \(1-r\). The ratio of scalar-negative to mixed involutions is therefore
\[
\frac{q^{E_N}}{q(q+1)q^{D_N/2}}=
\begin{cases}
q^{r+2}/[q(q+1)],&N=2r+1,\\
q^{1-r}/[q(q+1)],&N=2r.
\end{cases}
\]
For fixed \(q>1\), this ratio tends to infinity along odd \(N\) and to zero along even \(N\), proving both conditional limits.

## Verification
The standalone \(\texttt{verify.py}\) builds substituted polynomials directly in \(\mathbb F_q[x,y]/(x,y)^N\), checks the defining equation \(f\circ f=\operatorname{id}\) by coefficient comparison, and does **not** implement the orbit-stabilizer formula as its acceptance condition. It exhaustively checks all possible involutive linear parts and all nonlinear quadratic coefficients for \(N=3\), \(q=3,5\), a total of 510206 substitution tests. It separately solves the actual cubic coefficient equations for \(N=4\), \(q=3\), checking each of the three linear types with a modular Gaussian-elimination counter. The observed counts above \(I_2,-I_2,\operatorname{diag}(1,-1)\) at \(q=3,N=4\) are \(1,729,2187\); the mixed type is repeated across \(q(q+1)=12\) linear matrices, giving the total \(26974\). Nine further independent degree-parity identities check \(N=3,\ldots,11\). These finite computations corroborate but cannot replace the unrestricted proof.

## Relationship to prior work
Marshall M. Cohen, *Elements of Finite Order in the Group of Formal Power Series Under Composition* (first public 2018-03-30, arXiv:1804.00059, primary MSC includes 20E45), presents conjugacy and coefficient freedom for **one-variable, characteristic-zero** formal series. O'Farrell and Zaitsev, *Formally-Reversible Maps of C²* (arXiv:1111.6984, 2011), already establish **multivariable finite-order conjugacy to the linear part** in Section 2.2, Lemma 2.1, and this known ingredient is explicitly credited. Their results concern complex formal reversibility rather than finite-field truncation-level involution populations. Caprace and Kassabov, *Tame automorphism groups of polynomial rings with property (T) and infinitely many alternating group quotients* (arXiv:2210.00730, 2022), investigate infinite tame automorphism groups and finite alternating quotients; their inspected theorems do not provide the local jet-group class sizes. The result is the exact two-variable finite-field orbit evaluation and the resulting parity-sensitive limit, not a new general linearization theorem.

## Limitations
Odd characteristic is essential: when \(q\) is even, \(I_2\) and \(-I_2\) coincide and nonsemisimple linear involutions occur, so the displayed formulas do not apply. The classification concerns algebra automorphisms of a local truncated *two-variable* ring, not global polynomial automorphisms or arbitrary complete local rings. The proof establishes exact counts and qualitative fixed-field parity limits, not a uniform limit as \(q\) varies with \(N\). Novelty is assessed relative to inspected sources and indexed mathematical research; a general unpublished or differently indexed finite-jet centralizer enumeration could imply the formulas. Independent validation has not been performed.

## References
1. M. M. Cohen, *Elements of Finite Order in the Group of Formal Power Series Under Composition*, first posted 2018-03-30, https://arxiv.org/abs/1804.00059 .
2. A. G. O'Farrell and D. Zaitsev, *Formally-Reversible Maps of C²*, 2011, https://arxiv.org/abs/1111.6984 , especially Lemma 2.1.
3. P.-E. Caprace and M. Kassabov, *Tame automorphism groups of polynomial rings with property (T) and infinitely many alternating group quotients*, 2022, https://arxiv.org/abs/2210.00730 .
