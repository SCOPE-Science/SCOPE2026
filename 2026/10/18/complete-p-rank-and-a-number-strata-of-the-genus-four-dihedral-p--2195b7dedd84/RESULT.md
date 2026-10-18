# Complete \(p\)-rank and \(a\)-number strata of the genus-four dihedral pencil in characteristic \(41\)

## Finding
Let \(k=\overline{\mathbf F}_{41}\). For \(s\in k\) with \(s^2\ne4\), consider the smooth genus-four hyperelliptic curve
\[
H_s:\quad y^2=x^{10}+s x^5+1.
\]
Its geometric isomorphism class is indexed by \(v=s^2\); the two choices of square root define isomorphic curves. Define the following two polynomials in \(\mathbf F_{41}[v]\):
\[
C(v)=v^3-17v^2+v+2,\qquad
T(v)=v^6+20v^5+14v^4-3v^3+15v^2-14v-19.
\]
The complete geometric stratification of the Jacobian is
\[
\big(f(H_s),a(H_s)\big)=
\begin{cases}
(0,4),&v=26,\\
(2,2),&v=28\ \text{or}\ C(v)=0\ \text{or}\ T(v)=0,\\
(4,0),&\text{otherwise},
\end{cases}
\qquad v\ne4,
\]
where \(f\) is the geometric \(41\)-rank and \(a\) is the \(a\)-number. Both \(C\) and \(T\) are separable and irreducible over \(\mathbf F_{41}\). Thus there are exactly ten distinct geometric isomorphism classes with \((f,a)=(2,2)\), arranged into Frobenius orbits of degrees \(1,3,6\); the unique \((0,4)\) class has \(v=26\), a rational coarse-moduli coordinate. The \((0,4)\) isomorphism class is previously included in the published superspecial enumeration; the intermediate-rank classification is the new portion.

## Assumptions and scope
All curves and isomorphism classes are geometric over \(k\). The characteristic is exactly \(41\), and the singular parameters \(s=\pm2\) (equivalently \(v=4\)) are excluded. The polynomial \(x^{10}+s x^5+1\) is square-free when \(s^2\ne4\), because its derivative is \(5x^4(2x^5+s)\); the constant term is nonzero, and a repeated nonzero root would require \(s^2=4\). Degree ten therefore gives genus four.

The known isomorphism criterion for this dihedral family identifies precisely \(s\) and \(-s\), so \(v=s^2\) is the geometric coarse parameter (Ohashi--Kudo, Proposition 3.3.4, via \(\lambda+\lambda^{-1}=v-2\)). The enlarged automorphism point \(v=0\) is ordinary. All nonordinary members have the dihedral full automorphism group of order \(20\). A rational coarse-moduli coordinate is *not* asserted to mean that this displayed equation admits \(s\in\mathbf F_{41}\).

## Proof
Let \(e=(41-1)/2=20\), and write
\[
(x^{10}+s x^5+1)^{20}=\sum_{m=0}^{200}\gamma_m x^m.
\]
On the basis \(x^{j-1}dx/y\) for \(j=1,2,3,4\), the Cartier--Manin matrix has entries \(\gamma_{41i-j}\), where \(i,j\in\{1,2,3,4\}\). All nonzero exponents \(m\) are multiples of five. Since \(41\equiv1\pmod5\), \(41i-j\equiv i-j\pmod5\); as \(1\le i,j\le4\), only diagonal entries survive. Palindromicity of \(x^{10}+s x^5+1\) gives
\[
M_s=\operatorname{diag}(A(s^2),B(s^2),B(s^2),A(s^2)),
\]
where
\[
A(s^2)=[U^8](U^2+sU+1)^{20},\qquad
B(s^2)=[U^{16}](U^2+sU+1)^{20}.
\]
Only even powers of \(s\) occur. Exact multinomial expansion in characteristic \(41\) gives the factorizations
\[
\begin{aligned}
A(v)&=18(v+15)(v^3-17v^2+v+2),\\
B(v)&=7(v+13)(v+15)(v^6+20v^5+14v^4-3v^3+15v^2-14v-19).
\end{aligned}
\]
The factors \(v+13\), \(v+15\), \(C\), and \(T\) are distinct, separable, irreducible over \(\mathbf F_{41}\); in particular \(\gcd(A,B)=v+15\) up to unit. The exact finite-field computations are independently reproducible by the accompanying `verify.py`, which constructs each coefficient directly, verifies the displayed products and gcd, and uses the finite-field Frobenius criterion for irreducibility.

For a diagonal Cartier--Manin matrix, its semilinear iterates retain precisely the same nonzero diagonal positions: a nonzero scalar and its Frobenius powers cannot become zero. Consequently the stable rank, equal to the Jacobian \(p\)-rank, equals \(\operatorname{rank}M_s\). The \(a\)-number is \(4-\operatorname{rank}M_s\). If \(v=26=-15\), both \(A\) and \(B\) vanish, giving \((0,4)\). If exactly one vanishes, the rank is two, giving \((2,2)\). Else rank is four, giving \((4,0)\). Neither coefficient vanishes at \(v=4\): both evaluate to \(1\), so excluding the two singular parameters deletes no exceptional point.

Every root \(v\in k\) has a square root \(s\in k\), while the isomorphism criterion identifies the two signs and no additional values. The distinct roots give \(1+1+3+6=11\) nonordinary geometric isomorphism classes. As the four factors have irreducible degrees \(1,1,3,6\) over \(\mathbf F_{41}\), the Frobenius orbit-degree assertions follow. Finally \(v=26\) and \(v=28\) are nonsquares in \(\mathbf F_{41}\), while the higher-degree roots are not in the prime field; hence no member with displayed coefficient \(s\in\mathbf F_{41}\) is nonordinary.

## Verification
Run `python3 verify.py` with Python 3 and SymPy. It constructs the two Cartier polynomials as finite multinomial sums modulo \(41\), independently verifies palindromicity and coefficient parity, checks products, gcd and squarefreeness, applies explicit finite-field Frobenius irreducibility tests, and checks the excluded boundary, rational-parameter specialization and orbit-degree counts. The successful run prints `VERIFY_OK`. These computations supply finite, exact algebraic certificates; the completeness of the geometric classification also uses the parameter-uniform Cartier matrix and the published isomorphism criterion.

## Relationship to prior work
Cavalieri--Pries, *Mass formula for non-ordinary curves in one dimensional families* (arXiv:2308.14891v1, first public 2023-08-28), studies the nonordinary locus and its mass in natural one-dimensional cyclic and hyperelliptic families, including degree-ten palindromic models. It motivates exact descriptions beyond aggregate intersection numbers. Ohashi--Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group* (arXiv:2312.16858v1, first public 2023-12-28), Section 3.3 and Table 2, establishes Cartier criteria, geometric isomorphism testing, and the existence of precisely one superspecial dihedral isomorphism class at characteristic \(41\). Those results already cover the superspecial case and the general matrix method. The statement here supplies the additional ten intermediate-rank classes, their defining irreducible polynomials and field-orbit degrees, and a complete exact stratification. No claim of novelty is made for the preexisting superspecial count.

## Limitations
The result applies only to this one-parameter genus-four dihedral family in characteristic \(41\), not all genus-four hyperelliptic curves, all primes, or all Newton/Ekedahl--Oort strata. It determines the \(p\)-rank and \(a\)-number, not the full isomorphism type of the \(41\)-divisible group. It concerns geometric isomorphism classes and Frobenius action on coarse moduli; it does not establish minimal fields of definition of each displayed normalized equation. Bibliographic priority remains subject to unindexed equivalent computations or later versions of nearby papers.

## References
1. Renzo Cavalieri and Rachel Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891v1 (28 August 2023), https://arxiv.org/abs/2308.14891.
2. Ryo Ohashi and Momonari Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858v1 (28 December 2023), https://arxiv.org/abs/2312.16858. In particular Proposition 3.3.4, Corollary 3.3.5 and Table 2.
