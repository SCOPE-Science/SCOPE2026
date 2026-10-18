# The first correction to triple-product collisions of monic polynomials

## Finding

For a prime power \(q\), let \(\mathcal M_d(q)\) be the monic polynomials of degree exactly \(d\) in \(\mathbb F_q[T]\). For every **fixed integer** \(d\ge1\), define
\[
E_{3,d}(q)=\#\left\{(f_1,f_2,f_3,g_1,g_2,g_3)\in\mathcal M_d(q)^6:\ f_1f_2f_3=g_1g_2g_3\right\}.
\]
As \(q\to\infty\) through prime powers,
\[
\boxed{E_{3,d}(q)=\frac{(d+1)(d+2)(d^2+3d+4)}8q^{3d}-\frac{3d(d+1)(d+2)(3d+1)}8q^{3d-1}+O_d(q^{3d-2}).}
\]
Both displayed coefficients are exact for every \(d\). The negative second coefficient is a first arithmetic correction to the \(3\times3\) Birkhoff lattice-point count in the main term.

## Assumptions and scope

All six factors are ordered, monic, and have the **same exact degree** \(d\). The polynomial variable is \(T\), while \(q\) is any prime power. The limit fixes \(d\) and lets \(q\) grow. The \(O_d\) constant may depend on \(d\). For \(d=0\), the exact count equals \(1\) (not needed for the theorem). No irreducibility or squarefreeness condition is imposed.

## Proof

**1. A six-variable Euler product.** Introduce indeterminates \(\boldsymbol x=(x_1,x_2,x_3)\) and \(\boldsymbol y=(y_1,y_2,y_3)\), and let \(h_m(\boldsymbol x)\) be the degree-\(m\) complete homogeneous symmetric polynomial, with \(h_0=1\). Define the local formal series
\[
L(\boldsymbol x,\boldsymbol y)=\sum_{m\ge0}h_m(\boldsymbol x)h_m(\boldsymbol y).
\]
For each monic irreducible polynomial \(P\) of degree \(r\), its exponents in the left and right triples must each sum to the same number \(m\). Its degree contributions therefore give the local factor \(L(x_1^r,x_2^r,x_3^r;y_1^r,y_2^r,y_3^r)\). Thus unique factorization proves the formal power-series identity
\[
G(\boldsymbol x,\boldsymbol y;q)=\prod_{r\ge1}L(\boldsymbol x^{r},\boldsymbol y^{r})^{I_r(q)},\qquad I_r(q)=\frac1r\sum_{a\mid r}\mu(a)q^{r/a}.
\]
Here the bold exponent \(r\) means applying that exponent to every variable. The coefficient of \(x_1^d x_2^d x_3^d y_1^d y_2^d y_3^d\) in \(G\) is exactly \(E_{3,d}(q)\).

**2. The first two degrees in the finite-field parameter.** Write \(p_m(\boldsymbol x)=x_1^m+x_2^m+x_3^m\) and \(e_2(\boldsymbol x)=x_1x_2+x_1x_3+x_2x_3\), similarly for \(\boldsymbol y\). Factor out
\[
Z(\boldsymbol x,\boldsymbol y;q)=\prod_{1\le i,j\le3}(1-qx_i y_j)^{-1}.
\]
All terms in \(\log G\), \(\log Z\), and \(\log(G/Z)\) have equal total \(\boldsymbol x\)- and \(\boldsymbol y\)-degree. Call this common degree \(m\). The degree-\(1\) logarithmic pieces coincide. Since \(I_2(q)=(q^2-q)/2\), the degree-\(2\) piece of \(\log(G/Z)\) is
\[
q\left(h_2(\boldsymbol x)h_2(\boldsymbol y)-\tfrac12p_1(\boldsymbol x)^2p_1(\boldsymbol y)^2\right)-\frac q2p_2(\boldsymbol x)p_2(\boldsymbol y)
=-q e_2(\boldsymbol x)e_2(\boldsymbol y).
\]
The equality follows on substituting \(h_2=(p_1^2+p_2)/2\).

For every \(m\ge3\), each monomial in the degree-\(m\) piece of \(\log(G/Z)\) has coefficient of degree at most \(m-2\) in \(q\). Indeed, terms from \(I_r(q)\log L(\boldsymbol x^r,\boldsymbol y^r)\) have \(r\mid m\). When \(r=1\) their coefficient degree is at most \(1\le m-2\); when \(1<r<m\), it is at most \(r\le m/2\le m-2\). Finally, the degree-\(m\) contribution of \(r=m\) cancels the \(q^m p_m(\boldsymbol x)p_m(\boldsymbol y)/m\) contribution from \(\log Z\), leaving \(I_m(q)-q^m/m\), of degree at most \(\lfloor m/2\rfloor\le m-2\). Formal exponentiation therefore yields
\[
G=Z\bigl(1-qe_2(\boldsymbol x)e_2(\boldsymbol y)+R\bigr),
\]
where every homogeneous piece of \(R\), of common degree \(m\), has coefficient of \(q\)-degree at most \(m-2\) (and no constant or degree-\(1\) piece). Products involving the quadratic correction twice have deficit at least \(2\), which is included in this bound.

**3. Extracting the dominant lattice-point counts.** Expanding the nine geometric factors of \(Z\) gives
\[
Z=\sum_{(a_{ij})\in\mathbb Z_{\ge0}^{3\times3}}q^{\sum a_{ij}}\prod_i x_i^{\sum_j a_{ij}}\prod_j y_j^{\sum_i a_{ij}}.
\]
Set \(M_d\) equal to the number of \(3\times3\) nonnegative-integer matrices with all row and column sums \(d\). Set \(N_d\) equal to the number with both row and column sums \((d,d-1,d-1)\). A factor \(x_i x_j y_k y_\ell\) from \(e_2(\boldsymbol x)e_2(\boldsymbol y)\) decreases two distinct row targets and two distinct column targets by one. By row/column symmetry, each of the \(\binom32^2=9\) choices contributes \(N_d\). Coefficient extraction now gives
\[
E_{3,d}(q)=M_d q^{3d}-9N_d q^{3d-1}+O_d(q^{3d-2}).
\]
The finite number of relevant monomials for fixed \(d\) makes the error statement uniform over all prime powers \(q\).

**4. Elementary evaluation of the two counts.** To enumerate \(M_d\), choose first-row entries \(a,b,c\ge0\) summing to \(d\). The middle row must sum to \(d\) and stay under column capacities \((d-a,d-b,d-c)\). By inclusion-exclusion, its count is
\[
\binom{d+2}{2}-\binom{a+1}{2}-\binom{b+1}{2}-\binom{c+1}{2}.
\]
Two capacity violations cannot occur simultaneously. Summing over all first rows, and using \(\sum_{a+b+c=d}\binom{a+1}{2}=\binom{d+3}{4}\), gives
\[
M_d=\binom{d+2}{2}^{\!2}-3\binom{d+3}{4}
=\frac{(d+1)(d+2)(d^2+3d+4)}8.
\]
For \(N_d\), choose the first row \((a,b,c)\) summing to \(d\); the other two rows each sum to \(d-1\) and the columns have capacities \((d-a,d-1-b,d-1-c)\). The number of choices of the middle row is
\[
\binom{d+1}{2}-\binom a2-\binom{b+1}{2}-\binom{c+1}{2}.
\]
If \(b=d\) or \(c=d\), a capacity is negative and this displayed expression correctly gives zero. Double violations otherwise remain impossible. Consequently,
\[
N_d=\binom{d+2}{2}\binom{d+1}{2}-\binom{d+2}{4}-2\binom{d+3}{4}
=\frac{d(d+1)(d+2)(3d+1)}{24}.
\]
Substituting these evaluations into the coefficient formula proves the theorem for all fixed \(d\ge1\) and all prime-power field sizes in the stated limit.

## Verification

Execute `python3 verify.py` with Python 3. The code enumerates the two finite contingency-matrix counts independently for degrees \(1\) through \(10\), constructs monic polynomial triples over explicit prime fields, and checks their exact collision counts. In degree \(1\), the exact identity
\[
E_{3,1}(q)=6q^3-9q^2+4q
\]
provides an additional cross-check: categorize common products into three distinct roots, one double root, and one triple root. The finite calculations corroborate the formulas but are not used in place of the universal formal-series proof. No symbolic or computational check of all degrees is claimed.

## Relationship to prior work

Afifurrahman [1] proves an exact four-tuple equal-product formula with two factors on each side (Theorem 2.2). The present problem has three factors on each side, and its explicit first lower-order coefficient does not follow from that four-tuple statement. Andrade, Bary-Soroker, and Rudnick [2] treat fixed total degree and general divisor functions, including an unshifted **leading** moment statement, but do not supply this six-factor, separately fixed-degree lower-order coefficient. Afifurrahman and Corrigan [3] study related integer multiplicative-equation moments, with different counting base and asymptotic parameter. The nonnegative \(3\times3\) matrix main-term object is a classical Birkhoff-polytope lattice-point count also studied in [4], but the field-size correction arises from the prime-polynomial Euler product rather than the Ehrhart count alone. This relationship is a comparison of mathematical statements, not a claim of exhaustive priority clearance.

## Limitations

The error constant depends on the fixed degree \(d\); no uniformity in growing \(d\) is established. The formula supplies only the first two powers of \(q\), not a full exact polynomial in \(q\) for general \(d\). Generalizations to more than three factors are not claimed. Earlier equivalent computations, including work not accessible or indexed in searched resources, may exist and should be checked independently before external publication.

## References

[1] Muhammad Afifurrahman, *Statistics of divisor functions over function fields*, arXiv:2610.11240v1 (first posted 2026-10-08), Theorem 2.2 and Sections 1–2. https://arxiv.org/html/2610.11240v1

[2] J. C. Andrade, L. Bary-Soroker, Z. Rudnick, *Shifted convolution and the Titchmarsh divisor problem over \(\mathbb F_q[t]\)*, arXiv:1407.2076 (first posted 2014-07-08), Introduction, equation (1.18). https://arxiv.org/abs/1407.2076

[3] M. Afifurrahman and C. C. Corrigan, *Moments of restricted divisor functions*, arXiv:2501.15372v3, Theorem 1.1. https://arxiv.org/html/2501.15372v3

[4] Xinru Jiang, Guoce Xin, Chen Zhang, Yueming Zhong, *Exact Ehrhart Series of Birkhoff Polytopes via Constant Terms and Finite-Field Evaluation*, arXiv:2609.25863v1 (2026-09-22). https://arxiv.org/abs/2609.25863
