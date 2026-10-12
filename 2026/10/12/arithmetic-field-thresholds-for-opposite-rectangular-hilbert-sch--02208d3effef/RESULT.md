# Arithmetic field thresholds for opposite rectangular Hilbert-scheme torus edges

## Finding
Let \(K\) be any field of characteristic zero, and let \(d\ge3\) be an integer. Write
\[
M_d=(x^2,y^d),\qquad N_d=(x^d,y^2)\subset K[x,y].
\]
Both are colength-\(2d\) torus fixed points of \(\operatorname{Hilb}^{2d}(\mathbb A^2_K)\). An edge *over* \(K\) means a one-dimensional coordinate-torus orbit containing a \(K\)-rational ideal, with precisely these two monomial fixed-point limits.

**Field criterion.** Such an edge exists if and only if \(K\) contains
\[
\zeta+\zeta^{-1}
\]
for some nonidentity \(d\)-th root of unity \(\zeta\) in an algebraic closure of \(K\).

**Rationality dichotomy.** Over \(\mathbb Q\), the edge exists exactly when
\[
\boxed{\,2\mid d\quad\text{or}\quad 3\mid d\,}.
\]
Over \(\mathbb R\), it exists for every \(d\ge3\). Hence every \(d\) coprime to \(6\) gives a rational-versus-real edge discrepancy, generalizing the previously known case \(d=5\).

**Sharp arithmetic threshold.** Let \(\delta(d)\) be the minimum of \([K:\mathbb Q]\) among number fields \(K\) admitting an edge between \(M_d\) and \(N_d\). If \(d\) is even, then \(\delta(d)=1\). If \(d\) is odd, and \(p\) is the smallest prime divisor of \(d\), then
\[
\boxed{\delta(d)=\frac{p-1}{2}}.
\]
The bound is attained over the maximal real cyclotomic subfield
\[
K=\mathbb Q(\zeta_p+\zeta_p^{-1}).
\]
Thus the sharp minimal degree depends only on the smallest prime divisor for odd \(d\); for example, odd multiples of \(5\) not divisible by \(3\) admit quadratic models, while powers of an odd prime \(p\) require degree at least \((p-1)/2\).

## Assumptions and scope
The characteristic-zero hypothesis is essential to the repeated-root exclusion below. The claim concerns the coordinate \((\mathbb G_m)^2\)-action on the affine Hilbert scheme of points, not arbitrary connectedness or abstract rational points of Hilbert schemes. The two ideals are distinct because \(d\ge3\).

For a nonalgebraically closed field, a geometric component or an edge over its algebraic closure does **not** imply the existence of an edge over the original field: a \(K\)-rational intermediate ideal is required. The word “edge” is used with that condition throughout.

## Proof
**1. Reduction to standard homogeneous ideals.** Suppose an edge exists, represented by an ideal \(I\subset K[x,y]\). The two-initial-ideal characterization of one-dimensional torus orbits (Hering–Maclagan, Proposition 2.5) implies that \(I\) is homogeneous for positive integer weights \(\deg x=u\), \(\deg y=v\), and has initial ideals \(M_d,N_d\) under opposite term orders.

The standard monomials of \(M_d\) are \(x^iy^j\) with \(0\le i<2\) and \(0\le j<d\); those of \(N_d\) are \(x^iy^j\) with \(0\le i<d\) and \(0\le j<2\). These monomial sets must have the same weighted Hilbert function as \(I\). Comparing the greatest occurring weighted degrees gives
\[
u+(d-1)v=(d-1)u+v.
\]
As \(d\ge3\), we have \(u=v\). Hence \(I\) is homogeneous for the **usual** total degree.

The degree-two component \(I_2\) is one-dimensional because the degree-two components of both initial ideals are one-dimensional. Choose a generator
\[
f=A x^2+Bxy+C y^2\quad(A,C\in K^*).
\]
Both pure coefficients are nonzero: under \(x>y\), the leading monomial in degree two must be \(x^2\), whereas under \(y>x\) it must be \(y^2\). The initial ideal \(M_d\) contains \(y^d\) as a minimal generator. Since \(y^d\) is the *smallest* monomial of degree \(d\) under \(x>y\), its homogeneous lift must be exactly \(y^d\), and therefore \(y^d\in I\). Similarly \(x^d\in I\) using the opposite term order and \(N_d\).

Because \(C\neq0\), the homogeneous polynomials \(f\) and \(x^d\) form a regular sequence, hence \(K[x,y]/(f,x^d)\) has length \(2d\). The inclusion \((f,x^d)\subseteq I\) and \(\dim_K K[x,y]/I=2d\) force
\[
I=(f,x^d),\qquad y^d\in(f,x^d).
\]
Conversely, any such \(f\) with \(A,C\neq0\) and \(y^d\in(f,x^d)\) defines an ideal of length \(2d\), whose initial ideals are exactly \((x^2,y^d)\) and \((x^d,y^2)\) in the two opposite lexicographic orders. Its torus orbit is one-dimensional because \(f\) is nonmonomial with two pure quadratic terms.

**2. Root-of-unity obstruction.** Use formal dehomogenization of homogeneous forms, not localization of the Artinian quotient: set \(t=y/x\) only as a symbol representing the ratio of formal monomials and put \(g(t)=A+Bt+Ct^2\). The degree-\(d\) vector space \(K[x,y]_d/fK[x,y]_{d-2}\) identifies with the two-dimensional algebra \(R=K[t]/(g)\) via \(x^d t^j\leftrightarrow x^{d-j}y^j\), after reducing representatives to degree at most one in \(t\). Under this identification, \(y^d\in(f,x^d)\) is equivalent to
\[
t^d\in K\cdot1\subset R.
\]
The constant is nonzero because \(A\neq0\) makes \(t\) invertible in \(R\). The quadratic polynomial \(g\) cannot have a repeated root \(\alpha\), since then \(\alpha\neq0\) and modulo \((t-\alpha)^2\) the nonconstant term of \(t^d\) is \(d\alpha^{d-1}(t-\alpha)\neq0\) in characteristic zero.

Thus \(g\) has distinct nonzero roots \(\alpha,\beta\), with \(\alpha^d=\beta^d\). Their ratio \(\zeta=\alpha/\beta\) is a nonidentity \(d\)-th root of unity. Its trace belongs to \(K\):
\[
\zeta+\zeta^{-1}
=\frac{(\alpha+\beta)^2}{\alpha\beta}-2\in K.
\]
This proves necessity.

For sufficiency, suppose \(\tau=\zeta+\zeta^{-1}\in K\) for some nonidentity \(d\)-th root \(\zeta\). If \(\zeta\ne-1\), take
\[
g(t)=t^2-\tau t+1,
\quad
I=(y^2-\tau xy+x^2,x^d).
\]
The distinct roots of \(g\) are \(\zeta,\zeta^{-1}\), both with \(d\)-th power \(1\), so \(y^d\in I\). If \(\zeta=-1\), necessarily \(d\) is even, and \(I=(y^2-x^2,x^d)\) works instead. Step 1 gives the required edge.

**3. Rational and real fields.** If \(K=\mathbb Q\), the trace \(\tau\) is a rational algebraic integer, hence an integer. Every complex root of unity has trace in \([-2,2]\). Excluding the identity, the possibilities \(\tau=-2,-1,0,1\) correspond to orders \(2,3,4,6\). An order dividing \(d\) exists if and only if \(2\mid d\) or \(3\mid d\). Conversely, the explicit ideals
\[
(y^2-x^2,x^d)\quad(2\mid d),
\qquad
(y^2+xy+x^2,x^d)\quad(3\mid d)
\]
realize the edge over \(\mathbb Q\). For \(\mathbb R\), any \(\zeta=e^{2\pi i/d}\) has real trace \(2\cos(2\pi/d)\), giving a real intermediate ideal for every \(d\ge3\).

**4. Minimum number-field degree.** The even case is settled by Step 3. Let \(d\) be odd and \(p\) its smallest prime divisor. For every number field \(K\) admitting an edge, Step 2 produces a nonidentity root \(\zeta\) of some odd order \(m\mid d\). Since \(m\ge3\), the algebraic number \(\zeta+\zeta^{-1}\) generates the real cyclotomic subfield of degree \(\varphi(m)/2\). Consequently
\[
[K:\mathbb Q]\ge\frac{\varphi(m)}2\ge\frac{p-1}{2},
\]
because every prime factor of \(m\) is at least \(p\). Equality is achieved by choosing a primitive \(p\)-th root \(\zeta_p\) and the explicit intermediate ideal over \(K=\mathbb Q(\zeta_p+\zeta_p^{-1})\) in Step 2. This finishes the proof.

## Verification
Run `python3 artifacts/check.py` with Python 3 standard library. It checks polynomial reductions for the explicit rational quadratic constructions for all \(3\le d\le300\), the two opposed Gröbner-leading-generator patterns by symbolic algebra for representative degrees (optional SymPy cross-check described in the script), and the arithmetic degree bound for all \(3\le d\le2000\) by totient/divisor enumeration. No finite census is used to establish the for-all-\(d\) theorem, which follows entirely from the preceding argument.

## Relationship to prior work
Hering–Maclagan (2011), Proposition 2.5, proves the homogeneous-orbit criterion needed for the reduction. Its Example 2.11 **already establishes** exactly the special case \(d=5\), with a real edge but no rational edge. That example is prior art, not a new instance.

Silversmith (2019), Theorem 5.11, identifies the **complex** edge scheme for arbitrary opposite rectangular monomial ideals with a divisor of pairs of roots on \(\mathbb P^1\), and indexes complex components by binary necklaces. Thus the existence and geometric structure over \(\mathbb C\) are prior art, and the present proof does not claim them as new. The separate arithmetic conclusions classify \(K\)-rational existence, determine the precise \(\mathbb Q\)-versus-\(\mathbb R\) discrepancy for every \(d\), and give the optimal number-field degree. These conclusions are not among the complex-field statements in that theorem.

Zajaczkowska (2018), Chapter 5, constructs quadratic complex realizations of rank-two tropical ideals using roots of unity. That construction supplies further geometric precedent but does not formulate the rational-versus-real edge criterion or any minimum number-field degree.

Maclagan–Silversmith (2021 preprint; revised 2023), Example 2.3, revisits the \(d=5\) discrepancy and explicitly notes a **sufficient** condition over an arbitrary field: a degree-\(2\) factor of \(x^d+c y^d\). That known sufficient direction overlaps with the explicit constructions here; the additional necessary field trace obstruction and sharp all-parameter degree formula are the arithmetic content of this result.

## Limitations
The result is restricted to opposite \(2\times d\) monomial rectangles, characteristic zero, and the coordinate-torus edge relation on the affine plane's length-\(2d\) Hilbert scheme. It does not classify arbitrary torus edges, higher rectangles, or positive-characteristic behavior. The case \(d=5\) and the complex geometric edge schemes are known. An unindexed arithmetic formulation in earlier sources remains a possible originality risk; absence from a search index is not proof of novelty. No independent audit has been performed.

## References
Milena Hering and Diane Maclagan, *The T-graph of a multigraded Hilbert scheme*, arXiv:1110.1861v1, first posted 9 October 2011; *Experimental Mathematics* 21 (2012), 280–297, DOI 10.1080/10586458.2012.659569, Proposition 2.5 and Example 2.11.

Rob Silversmith, *The matroid stratification of the Hilbert scheme of points on \(\mathbb P^1\)*, arXiv:1911.03569, first posted 8 November 2019; *Manuscripta Mathematica* 167 (2022), 173–195, Theorem 5.11.

Diane Maclagan and Rob Silversmith, *The spine of the \(T\)-graph of the Hilbert scheme of points in the plane*, arXiv:2111.00819, first posted 1 November 2021; Example 2.3.

Magdalena Anna Zajaczkowska, *Tropical Ideals with Hilbert Function Two*, PhD thesis, University of Warwick, March 2018, Chapter 5, archived at https://wrap.warwick.ac.uk/115228/.
