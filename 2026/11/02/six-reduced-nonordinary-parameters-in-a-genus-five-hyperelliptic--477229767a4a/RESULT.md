# Six reduced nonordinary parameters in a genus-five hyperelliptic pencil in characteristic thirteen

## Finding

Let \(k\) be an algebraically closed field of characteristic \(13\). For every \(t\in k\setminus\{2,-2\}\), let \(C_t\) be the smooth projective curve with affine model
\[
C_t:\quad y^2=(x^4-1)(x^8+t x^4+1).
\]
Define the cubic polynomials in \(\mathbb F_{13}[t]\)
\[
P(t)=(t-6)(t^2+3t+6),\qquad
Q(t)=(t+6)(t^2+5t-4).
\]
Then the geometric \(13\)-rank \(f_{13}\) of the Jacobian and its \(a\)-number satisfy, for **every** smooth geometric parameter,
\[
(f_{13}(C_t),a(C_t))=
\begin{cases}
(3,2),&P(t)Q(t)=0,\\
(5,0),&P(t)Q(t)\ne0.
\end{cases}
\]
In particular, the reduced nonordinary parameter divisor has exactly **six distinct geometric points**, all defined over \(\mathbb F_{13^2}\), and precisely two of them are \(\mathbb F_{13}\)-rational. With \(\eta^2=2\) in \(\mathbb F_{13^2}\), the exceptional parameters are
\[
t=6,\ 5+9\eta,\ 5-9\eta,\ 7,\ 4+7\eta,\ 4-7\eta.
\]
Every nonordinary member has exactly the same rank drop of two; neither \(a=1\) nor \(13\)-ranks \(0,1,2,4\) occur. The Hasse--Witt determinant has multiplicity two at each of these six smooth fibers.

## Assumptions and scope

The parameter space is the punctured affine line \(U=\mathbb A^1_k\setminus\{2,-2\}\). The polynomial defining the double cover has twelve distinct roots when \(t\in U\), so \(C_t\) is hyperelliptic of genus \(5\). The \(13\)-rank means \(\dim_{\mathbb F_{13}}\operatorname{Jac}(C_t)[13](k)\); the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_{13},\operatorname{Jac}(C_t))\), equivalently the dimension of the kernel of Cartier on regular one-forms. The statements concern geometric parameters rather than isomorphism classes of curves.

## Proof

Put \(z=x^4\) and \(F(z)=(z-1)(z^2+tz+1)\), and write
\[
F(z)^6=\sum_{j=0}^{18}b_j(t)z^j
\quad (b_j\in\mathbb F_{13}[t]).
\]
The anti-reciprocity \(z^3F(1/z)=-F(z)\) implies \(b_j=b_{18-j}\). In the standard hyperelliptic Hasse--Witt normalization, with indices \(1\le i,j\le5\), the coefficient matrix is \((c_{13i-j})\), where \(c_{4j}=b_j\) and all other \(c_\ell\) vanish. Consequently
\[
M_t=\begin{pmatrix}
b_3&0&0&0&b_2\\
0&b_6&0&0&0\\
0&0&b_9&0&0\\
0&0&0&b_6&0\\
b_2&0&0&0&b_3
\end{pmatrix}.
\]
The formulas are valid in characteristic \(13\) over every perfect extension; a possible Frobenius root/transpose convention for the Cartier matrix does not affect its rank.

Exact coefficient convolution in \(\mathbb F_{13}[t,z]\) yields
\[
\begin{aligned}
b_6&=(t+2)^3P(t), & b_9&=6(t+2)^3Q(t),\\
b_3+b_2&=-6(t+2)^3,& b_3-b_2&=-6Q(t).
\end{aligned}
\]
The basis vectors \(e_1+e_5\), \(e_1-e_5\), \(e_2\), \(e_3\), \(e_4\) are defined over \(\mathbb F_{13}\) and diagonalize this coefficient matrix, with eigenvalues
\[
-6(t+2)^3,\quad -6Q(t),\quad (t+2)^3P(t),\quad
6(t+2)^3Q(t),\quad (t+2)^3P(t).
\]
Since the eigenvectors are defined over the prime field, **the same basis diagonalizes all Frobenius twists**. For each one-dimensional semilinear eigensummand, a nonzero scalar gives an invertible semilinear map and a zero scalar gives the zero map. Thus the rank of the stabilized Frobenius iterate equals the number of nonzero displayed eigenvalues. This identifies the geometric \(13\)-rank, not merely the one-step Hasse--Witt rank.

The two cubics have no common geometric root. Indeed, their factors are the distinct rational linear roots \(6\) and \(7\), together with the separable irreducible quadratics whose discriminants are respectively \(11\) and \(2\), both nonsquares in \(\mathbb F_{13}\). Direct evaluation excludes the forbidden parameters \(\pm2\) and verifies that the two quadratic factors have different roots. It follows that, on \(U\), either both copies of the \(P\)-eigenvalue vanish, or both \(Q\)-eigenvalues vanish, or none vanish. Accordingly the rank is \(3\) in the first two cases and \(5\) otherwise.

The one-step Cartier rank is the same matrix rank, so \(a(C_t)=5-\operatorname{rank}M_t\), proving the stated pair of invariants. Finally, exact multiplication gives
\[
\det M_t=8(t+2)^{12}P(t)^2Q(t)^2\qquad\text{in }\mathbb F_{13}[t].
\]
Since \(t=-2\) lies outside the smooth parameter space and \(P Q\) is squarefree, every smooth determinant zero has multiplicity exactly two, while the reduced nonordinary divisor has degree six.

## Verification

Run `python3 verify.py` with a standard Python 3 installation. The standalone program constructs the entire polynomial \(F(z)^6\) by coefficient convolution in \(\mathbb F_{13}[t,z]\), checks the four displayed factorizations and determinant identity, constructs the complete \(5\times5\) matrix, and checks its rank for all \(167\) smooth parameters over \(\mathbb F_{169}\). It uses the presentation \(\mathbb F_{169}=\mathbb F_{13}[\eta]/(\eta^2-2)\) and verifies the six exceptional points and their two Frobenius-orbit patterns. Output begins `VERIFY_OK`. The proof of the all-geometric-parameter statement is the symbolic polynomial and semilinear argument above; a finite-field census alone would not suffice.

## Relationship to prior work

Ohashi and Kudo, *On superspecial hyperelliptic curves of genus 5 whose automorphism groups contain \((\mathbb Z/2\mathbb Z)^3\)* (2026), Section 4.2, define precisely this family up to their explicit coordinate change. Their Proposition 4.6 gives a prime-to-characteristic isogeny decomposition into five elliptic curves and their Corollary 4.7 constrains superspeciality. They do not provide the present complete characteristic-thirteen ordinary/\(13\)-rank-three stratification, the two cubic equations for its smooth nonordinary parameters, or their precise multiplicities. The matrix formula itself is classical (Yui). Bouchet, Davis, Groen, Porat and York (2025) study \(p\)-rank strata in hyperelliptic moduli broadly; their computational sampling and conjectures do not give this explicit pencil's divisor. The isogeny decomposition explains why paired rank drops are plausible but does not identify the exact parameters.

## Limitations

The classification is confined to characteristic thirteen and to this particular one-dimensional family. It counts **parameter values**, not geometric isomorphism classes: multiple parameters could define isomorphic curves. No claim is made about higher Cartier iterates beyond the rank needed for the \(p\)-rank, Newton polygons, full Ekedahl--Oort types, or the geometry of all genus-five hyperelliptic curves. Historical priority has been checked against identified sources but not independently certified; an unindexed equivalent computation remains possible.

## References

1. R. Ohashi and M. Kudo, *On superspecial hyperelliptic curves of genus 5 whose automorphism groups contain \((\mathbb Z/2\mathbb Z)^3\)*, arXiv:2603.21569 (first public 2026-03-23), Sections 2--4.2 and 6. https://arxiv.org/abs/2603.21569
2. T. Bouchet, E. Davis, S. R. Groen, Z. Porat and B. York, *Heuristics for (ir)reducibility of \(p\)-rank strata of the moduli space of hyperelliptic curves*, arXiv:2506.06457 (2025). https://arxiv.org/abs/2506.06457
3. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, Journal of Algebra 52 (1978), 378--410, DOI:10.1016/0021-8693(78)90247-8.
