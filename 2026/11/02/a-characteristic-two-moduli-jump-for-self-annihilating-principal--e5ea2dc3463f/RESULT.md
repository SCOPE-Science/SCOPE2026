# A characteristic-two moduli jump for self-annihilating principal ideals

## Finding
Fix an integer \(d\ge2\) and a field \(k\). For the Artinian monomial complete intersection
\[
A_d(k)=k[x_1,\ldots,x_d]/(x_1^2,\ldots,x_d^2),\qquad \mathfrak m=(x_1,\ldots,x_d),
\]
let \(\mathcal E_d(k)\) be the set of distinct principal ideals \((f)\) with \(f\in\mathfrak m\setminus\mathfrak m^2\), \(f^2=0\), and \(\operatorname{Ann}_{A_d(k)}(f)=(f)\). Thus these are precisely the *self-annihilating* (or self-paired exact-zero-divisor) principal ideals with nonzero linear initial form.

If \(\operatorname{char}k\ne2\), then
\[
\mathcal E_d(k)=\{(x_1),\ldots,(x_d)\}.
\]
If \(\operatorname{char}k=2\), the map
\[
\mathcal E_d(k)\longrightarrow\mathbb P(\mathfrak m/\mathfrak m^2)(k),\qquad
(f)\longmapsto[f\bmod\mathfrak m^2]
\]
has explicit Zariski-local trivializations whose fibers are affine spaces of dimension \(2^{d-1}-d\). The parameter space defined by these charts is consequently a Zariski-locally trivial affine-space fibration over \(\mathbb P^{d-1}_k\), of total dimension \(2^{d-1}-1\). In particular, for every prime power \(q\),
\[
\boxed{\#\mathcal E_d(\mathbb F_q)=
\begin{cases}
d,&q\text{ odd},\\[2pt]
q^{\,2^{d-1}-d}\,(q^d-1)/(q-1),&q\text{ even}.
\end{cases}}
\]
The self-annihilator condition is automatic for *every* \(f\in\mathfrak m\setminus\mathfrak m^2\) satisfying \(f^2=0\).

## Assumptions and scope
All ideals are distinct ideals, not generators modulo nonzero scalar multiplication. The coefficient field is arbitrary in the structural classification; the displayed formula counts ideals over finite fields. The algebra has \(k\)-dimension \(2^d\), with squarefree monomials as a basis. A linear initial form means a nonzero image in \(\mathfrak m/\mathfrak m^2\). No assertion is made about principal ideals generated inside \(\mathfrak m^2\), arbitrary pairs \((f,g)\) of exact zero divisors, or nonreduced moduli schemes.

## Proof
**1. Normalization in characteristic two.** In characteristic two every element of \(\mathfrak m\) has square zero, because each squarefree monomial of positive degree squares to zero and Frobenius is additive. Every invertible linear change of the \(x_i\) therefore respects all relations \(x_i^2=0\) and defines an algebra automorphism. Fix a nonzero initial linear form \(L\); choose complementary linear forms \(y_2,\ldots,y_d\), and write
\[
B=k[y_2,\ldots,y_d]/(y_2^2,\ldots,y_d^2),\quad A_d=B\oplus LB.
\]
Every \(f\) whose initial line is \([L]\) admits a unique expression \(f=La+b\) after choosing the scalar so that the coefficient of \(L\) is one, with \(a\in B^\times\) having constant term one and \(b\in\mathfrak m_B^2\). Multiplying \(f\) by the unit \(a^{-1}\) gives a generator \(L+g\), where \(g=ba^{-1}\in\mathfrak m_B^2\).

The representative is *unique as an ideal*: if \((L+g')=(L+g)\), then \(L+g'=(L+g)(u+Lv)\) for some \(u,v\in B\). Comparing the \(LB\) and \(B\) summands gives \(u+gv=1\) and \(g'=gu\). Since \(g^2=0\), these force \(g'=g\). Conversely every \(g\in\mathfrak m_B^2\) gives such an ideal. Thus the fiber over \([L]\) is canonically parametrized, relative to a chosen complement, by the affine space underlying \(\mathfrak m_B^2\), of dimension \(2^{d-1}-d\). Choosing the complement polynomially on each standard projective chart provides Zariski-local trivializations; their transition maps are regular (via finite nilpotent unit inversion). Here “affine-space fibration” does not assert that the transition functions are affine-linear.

**2. The self-annihilator.** For \(g\in\mathfrak m_B^2\), the substitution \(L\mapsto L+g\), \(y_i\mapsto y_i\) gives an automorphism in characteristic two: its inverse is the same substitution, because \(g\) contains no \(L\). The coordinate element \(L\) has \(\operatorname{Ann}(L)=LB=(L)\), by the decomposition \(A_d=B\oplus LB\). Applying the automorphism gives \(\operatorname{Ann}(L+g)=(L+g)\). This also proves the required annihilator statement for every square-zero element with nonzero initial form.

**3. Odd characteristic.** Suppose \(f^2=0\) and \(f\bmod\mathfrak m^2=\sum_i a_i x_i\ne0\). The quadratic homogeneous part of \(f^2\) is \(2\sum_{i<j}a_i a_j x_ix_j\). Independence of the squarefree quadrics and invertibility of \(2\) force at most one \(a_i\) to be nonzero. After scaling let that coordinate be \(x_i\), and set \(B=k[x_j:j\ne i]/(x_j^2:j\ne i)\). Write \(f=x_i u+v\), with \(u\in B^\times\) and \(v\in\mathfrak m_B^2\). The decomposition \(A_d=B\oplus x_iB\) turns \(f^2=0\) into the separate equations \(v^2=0\) and \(2uv=0\). Since \(2\) and \(u\) are units, \(v=0\), so \((f)=(x_i)\). Conversely \(\operatorname{Ann}(x_i)=(x_i)\) and \(x_i^2=0\); exactly \(d\) ideals occur.

**4. Counting.** In characteristic two, the base has \((q^d-1)/(q-1)\) rational points and every rational fiber has \(q^{2^{d-1}-d}\) elements. Multiply. In odd characteristic the preceding classification has exactly \(d\) elements. This proves all statements for every \(d\ge2\) and every allowed field.

## Verification
The standalone standard-library checker `verify.py` implements arithmetic in \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), constructs the quotient-ring multiplication, enumerates all elements with nonzero linear form, tests \(f^2=0\), computes the image of multiplication by \(f\) as a canonical row-space representative of \((f)\), and checks its dimension \(2^{d-1}\) (which combined with \(f^2=0\) implies \(\operatorname{Ann}(f)=(f)\)). Direct exhaustive instances are \((d,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\); respectively, the distinct-ideal counts are \(3,2,5,2,14,3,84,240\). Execute `python3 verify.py` in an environment with Python 3; no third-party packages are required. Finite checks corroborate but do not replace the uniform proof.

## Relationship to prior work
Dibaei and Gheibi (2011) develop exact-zero-divisor sequences in local rings. Kustin, Striuli and Vraciu (2013), especially their Remark 3.13, explicitly note that a coordinate generator is an exact zero divisor in the three-variable square-zero monomial complete intersection, and establish Hilbert-function restrictions on homogeneous exact pairs. Eddings and Vraciu (2024) investigate the characteristic-zero existence of general linear exact zero divisors. Their stated results and inspected relevant arguments do not provide the classification of distinct linear-leading *self-paired* principal ideals and its characteristic-two affine-fibration and all-finite-field point count. The existence and basic rank facts, in particular the coordinate ideals, are not claimed as new. Literature searches cannot establish absolute historical priority; an implicit or unindexed broader classification remains possible.

## Limitations
The parameterization concerns distinct labelled ideals in the fixed algebra, not ideals modulo the algebra-automorphism group; in characteristic two, automorphisms can identify many members. The local affine-space charts yield a reduced parameterization and do not settle nonreduced Hilbert-scheme structure. The theorem does not classify higher-order initial forms, exact pairs with distinct annihilator generators, or complete intersections whose generator exponents exceed two.

## References
1. M. T. Dibaei and M. Gheibi, *Sequence of Exact Zero-Divisors*, arXiv:1112.2353 (first public version December 11, 2011).
2. A. R. Kustin, J. Striuli and A. Vraciu, *Exact pairs of homogeneous zero divisors*, arXiv:1304.0411 (April 1, 2013), especially Remark 3.13.
3. A. Eddings and A. Vraciu, *Rings for which general linear forms are exact zero divisors*, arXiv:2407.16000 (July 22, 2024).
