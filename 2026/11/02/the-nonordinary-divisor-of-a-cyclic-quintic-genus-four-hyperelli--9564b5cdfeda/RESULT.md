# The nonordinary divisor of a cyclic-quintic genus-four hyperelliptic family in characteristics \(3\) and \(7\)

## Finding
Let \(k\) be algebraically closed of characteristic \(\ell\in\{3,7\}\) and let \(U=\mathbf A^1_k\setminus\{0,1\}\). For each \(\lambda\in U(k)\), denote by \(C_\lambda\) the smooth projective model of
\[
 y^2=(x^5-1)(x^5-\lambda).
\]
Every \(C_\lambda\) has genus \(4\). Let \(f_\ell(C_\lambda)\) be the geometric \(\ell\)-rank of its Jacobian, and let \(a(C_\lambda)=\dim_k\operatorname{Hom}(\alpha_\ell,\operatorname{Jac}(C_\lambda)[\ell])\) be its \(a\)-number. With respect to the basis \(x^{j-1}dx/y\), \(1\le j\le4\), the Cartier–Manin determinant, normalized by the coefficient convention below, is
\[
\det M_3=-\lambda(\lambda+1)^2,\qquad
\det M_7=3\lambda^3(\lambda+1)^2(\lambda^2+3\lambda+1)^2.
\]
The complete geometric strata on \(U\) are
\[
(f_3,a)=\begin{cases}(0,2)&\lambda=-1,\\(4,0)&\lambda\ne-1,\end{cases}
\]
and
\[
(f_7,a)=\begin{cases}(0,2)&(\lambda+1)(\lambda^2+3\lambda+1)=0,\\(4,0)&\text{otherwise.}\end{cases}
\]
In particular, in either characteristic, **no smooth family member has intermediate geometric rank** \(1\), \(2\), or \(3\). The scheme-theoretic nonordinary Cartier determinant divisor on \(U\) equals \(2[-1]\) for \(\ell=3\), and \(2[-1]+2[\lambda_+]+2[\lambda_-]\) for \(\ell=7\), where \(\lambda_\pm\) are the distinct roots of \(\lambda^2+3\lambda+1\). These statements concern marked parameter values, not distinct isomorphism classes.

More generally, for any odd prime \(\ell\ne5\) with \(\ell\equiv2\) or \(3\pmod5\), the geometric \(\ell\)-rank of this family is always either \(0\) or \(4\); no explicit exceptional-divisor formula is claimed here for primes other than \(3\) and \(7\).

## Assumptions and scope
Work over an algebraically closed field \(k\) of the stated characteristic, with the parameter restricted to \(U\). The degree-ten polynomial \((x^5-1)(x^5-\lambda)\) is squarefree when \(\ell\ne2,5\) and \(\lambda\ne0,1\): each quintic has five simple roots, and their roots are disjoint. The genus is consequently \((10-2)/2=4\). The order-five action \(x\mapsto\zeta x\) explains the sparse Cartier matrix. The singular boundary parameters \(0\) and \(1\) are excluded throughout; factors of the determinants at these parameters are not counted in the smooth-family divisors.

## Proof
Write \(F(x)=(x^5-1)(x^5-\lambda)=x^{10}-(1+\lambda)x^5+\lambda\), and expand
\[
F(x)^{(\ell-1)/2}=\sum_{m\ge0}c_m x^m.
\]
For the regular differential basis \(\omega_j=x^{j-1}dx/y\), \(j=1,2,3,4\), the standard hyperelliptic coefficient formula gives the \(4\times4\) Cartier–Manin matrix
\[
M_\ell=(c_{\ell i-j})_{1\le i,j\le4},
\]
with \(c_n=0\) for negative or absent degrees. As \(F\) lies in \(k[x^5]\), any nonzero entry must satisfy \(j\equiv\ell i\pmod5\). For \(\ell\equiv2\) or \(3\pmod5\), multiplication by \(\ell\) permutes \(1,2,3,4\) as one four-cycle. Thus each row and column of \(M_\ell\) has at most one nonzero position, and all these positions make one directed cycle. If all its four weights are nonzero, \(M_\ell\) is invertible. If any is zero, the fourfold semilinear Frobenius product
\[
 M_\ell M_\ell^{(\ell)}M_\ell^{(\ell^2)}M_\ell^{(\ell^3)}
\]
is zero: every diagonal weight in the fourth iterate contains all four weights with positive Frobenius exponents. The stable Frobenius rank, hence the geometric Jacobian \(\ell\)-rank, is therefore respectively \(4\) or \(0\). The same statement holds in all odd characteristics congruent to \(2\) or \(3\) modulo \(5\).

For \(\ell=3\), \(F(x)\) itself is the relevant power, and the matrix is
\[
 M_3=\begin{pmatrix}
0&0&\lambda&0\\
-(\lambda+1)&0&0&0\\
0&0&0&-(\lambda+1)\\
0&1&0&0
\end{pmatrix}.
\]
The determinant is \(-\lambda(\lambda+1)^2\). On \(U\), the unique zero is \(\lambda=-1\), where exactly two of its four nonzero-pattern entries vanish and the matrix rank is \(2\). Otherwise it has rank \(4\). Since the \(a\)-number equals \(4-\operatorname{rank}(M_3)\), this proves the characteristic-three classification and its divisor multiplicity.

For \(\ell=7\), use \(F(x)^3\) and collect powers of \(t=x^5\). Direct expansion gives
\[
 M_7=\begin{pmatrix}
0&-3\lambda^2(\lambda+1)&0&0\\
0&0&0&3\lambda(\lambda^2+3\lambda+1)\\
3(\lambda^2+3\lambda+1)&0&0&0\\
0&0&-3(\lambda+1)&0
\end{pmatrix}.
\]
The signed product of the cycle weights is
\[
-81\lambda^3(\lambda+1)^2(\lambda^2+3\lambda+1)^2
=3\lambda^3(\lambda+1)^2(\lambda^2+3\lambda+1)^2
\]
in characteristic \(7\). On \(U\), the quadratic \(\lambda^2+3\lambda+1\) has discriminant \(5\ne0\); neither its roots nor \(-1\) equal \(0\) or \(1\), and \(-1\) is not a quadratic root. Each exceptional parameter therefore makes exactly two pattern entries zero, leaving matrix rank \(2\) and \(a=2\). Else all four entries are nonzero and \((f_7,a)=(4,0)\). The factors are squared and pairwise coprime on \(U\), proving the full effective Hasse divisor with multiplicity two at all three geometric points.

The quadratic \(\lambda^2+3\lambda+1\) is irreducible over \(\mathbf F_7\) because \(5\) is a nonsquare. Thus among marked smooth parameters defined over \(\mathbf F_{7^r}\), the rank-zero locus contains one point if \(r\) is odd and three if \(r\) is even. These arithmetic counts do not identify distinct geometric curve-isomorphism classes.

## Verification
Run the self-contained Python 3 script `python3 verify_cyclic5.py`. It expands \(F^{(\ell-1)/2}\) by exact polynomial arithmetic over \(\mathbf F_\ell[\lambda]\), forms all \(16\) matrix entries via coefficient extraction, and computes each determinant from the full permutation formula, independently of the stated factorization. It then enumerates every smooth parameter in \(\mathbf F_3\) and \(\mathbf F_{49}\), calculating ordinary matrix rank and the four-step Frobenius-stable rank by exact finite-field elimination. Its successful final output is `CYCLIC5_EXACT_DETERMINANTS_AND_STABLE_RANKS_OK`. This finite enumeration is a check of the symbolic proof, not a proof by itself for all algebraically closed fields.

## Relationship to prior work
Hidalgo described the genus-\((r-1)\) hyperelliptic quotient \(y^2=(x^r-1)(x^r-\alpha^r)\) of generalized Fermat curves over the complex numbers (Theorem 1(5)(ii)); taking \(r=5\) motivates the present family. This earlier classification is about algebraic quotient models, not its arithmetic reduction strata. Li–Mantovan–Pries–Tang analyze Newton polygons of special cyclic-cover families; the order-five four-point inertia pattern here is \((1,1,4,4)\), unlike their special family with four-point order-five inertia \((1,3,3,3)\). Kudo–Nakagawa–Takagi give general hyperelliptic automorphism classifications and investigate a different \(C_6\)-symmetric genus-four family for superspeciality. Their cited results do not supply this marked \(C_5\) family's complete \(3\)- and \(7\)-rank jumping loci or Hasse divisor multiplicities. Kudo–Harashita–Senda also discuss the characteristic-three supersingular genus-four curve \(v^{10}=u(1-u)\), whose square-completion gives a model geometrically isomorphic to the exceptional member \(C_{-1}:y^2=x^{10}-1\); the existence and rank-zero status of that individual special member are **not** claimed as new. The new claim instead identifies the unique exceptional marked parameter, its \(a\)-number, Hasse multiplicity and the characteristic-seven complete divisor. Yui's coefficient formula, also documented in Sage's finite-field hyperelliptic manual, is used as an established tool and is not claimed as new.

## Limitations
No supersingularity, Newton-polygon, Ekedahl–Oort classification beyond the stated rank and \(a\)-number, or characterization up to geometric isomorphism is asserted. In particular, \(\ell\)-rank zero alone is not a proof of supersingularity. The analytic quotient construction motivating the family is not asserted to extend unchanged to every residue characteristic; the equations are interpreted directly over \(k\). An unindexed equivalent historical arithmetic computation remains possible. Independent external validation has not been performed.

## References
1. R. A. Hidalgo, *Smooth quotients of generalized Fermat curves*, arXiv:2202.12663v1 (first posted 2022-02-25), Theorem 1(5)(ii) and Section 4.2. https://arxiv.org/abs/2202.12663
2. W. Li, E. Mantovan, R. Pries, Y. Tang, *Newton Polygons Arising for Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914 (2018), family tables and cyclic-cover strata. https://arxiv.org/abs/1805.06914
3. M. Kudo, T. Nakagawa, T. Takagi, *Efficient Search for Superspecial Hyperelliptic Curves of Genus Four with Automorphism Group Containing \(C_6\)*, *Mathematics in Computer Science* 17 (2023), 21, doi:10.1007/s11786-023-00571-w. https://doi.org/10.1007/s11786-023-00571-w
4. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, coefficient formula; see also the Sage reference manual, `HyperellipticCurve_finite_field.Cartier_matrix`. https://sagemath.gitlab.io/documentation/html/en/reference/arithmetic_curves/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.html
5. M. Kudo, S. Harashita, H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, *Research in Number Theory* 6 (2020), 44, doi:10.1007/s40993-020-00217-x, especially the characteristic-three example. https://doi.org/10.1007/s40993-020-00217-x
