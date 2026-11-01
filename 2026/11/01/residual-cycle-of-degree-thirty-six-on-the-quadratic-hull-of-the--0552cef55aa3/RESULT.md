# Residual cycle of degree thirty-six on the quadratic hull of the triple osculating binary decic

## Finding
Let \(V=\mathbb C^2\), let \(T=T^3c_{10}\subset\mathbb P(\operatorname{Sym}^{10}V)\) be the fourth-dimensional locus of binary decics with a root of multiplicity at least seven, and let \(X\) be the **scheme-theoretic quadratic hull**, defined by all quadrics vanishing on \(T\). Then \(T\) occurs in the fundamental cycle of \(X\) with **scheme-theoretic multiplicity one**. Therefore the effective residual top-dimensional cycle
\[
R=[X]-[T]\in A_4(\mathbb P^{10})
\]
has **exact degree**
\[
\boxed{\deg R=36.}
\]
This is a weighted cycle degree; no assertion is made about the irreducibility, reducedness, number, or individual degrees of its residual components. In particular, a generic complementary linear space has residual intersection number 36, counted with multiplicities.

## Assumptions and scope
The ground field is \(\mathbb C\). Write a decic as
\[
f(x,y)=\sum_{i=0}^{10}a_i x^{10-i}y^i.
\]
The quadratic hull is defined **as a scheme**, not merely as a set. Its six defining quadrics are the five coefficients of \((f,f)_8\) and the single coefficient of \((f,f)_{10}\). For \(m\in\{4,5\}\), put
\[
q_j^{(m)}=[x^{20-4m-j}y^j]
\sum_{k=0}^{2m}(-1)^k\binom{2m}{k}
(\partial_x^{2m-k}\partial_y^k f)(\partial_x^k\partial_y^{2m-k}f).
\]
The index ranges are \(j=0,1,2,3,4\) for \(m=4\), and \(j=0\) for \(m=5\). Nonzero scalar normalization of a transvectant does not change its zero scheme or the ranks below.

## Proof
**1. Source complete intersection and degree.** Theorem 1.1 and Proposition 6.1 of Massri (arXiv:2610.28499v1) apply with \((p,r)=(3,10)\): the boundary equality is
\[
3=\binom{10-2\cdot3-1}{2}=\binom32.
\]
The six displayed quadrics form a regular sequence in \(\mathbb P^{10}\). Hence \(X\) is a Cohen–Macaulay complete intersection of pure dimension \(10-6=4\), with
\[
\deg X=2^6=64.
\]
There are no embedded associated components contributing to its four-dimensional fundamental cycle.

**2. The osculating component and its degree.** The incidence parametrization
\[
\mathbb P^1\times\mathbb P^3\longrightarrow T,
\quad ([\ell],[h])\longmapsto[\ell^7 h]
\]
is generically one-to-one: a degree-ten form cannot have two distinct roots each of multiplicity at least seven. The pullback of a hyperplane is \(\mathcal O(7,1)\). Therefore
\[
\deg T=\int_{\mathbb P^1\times\mathbb P^3}(7H_1+H_2)^4
=4\cdot7=28.
\]
This is a fourfold and lies in \(X\), so it is an irreducible component of the support of \(X\).

**3. An exact regular point on the osculating component.** Take
\[
f_0=x^7(x^3+x^2y+xy^2+y^3),
\]
so its coefficient vector is \(a_0=a_1=a_2=a_3=1\) and \(a_4=\cdots=a_{10}=0\). This form is on \(T\), has a unique sevenfold root \([x]\), and the cubic residual factor is not divisible by \(x\). The parameter map for \(T\) is locally immersive here: the three independent changes of the residual cubic modulo scaling give the \(a_1,a_2,a_3\) directions in the chart \(a_0=1\), and moving the sevenfold root gives a nonzero \(a_4\) direction (its coefficient comes from the \(y^3\) term). Thus \(T\) is smooth of projective dimension four at \([f_0]\), with normal coordinate directions \(a_5,\ldots,a_{10}\).

For each six-tuple equation \((m,j)\in\{(4,0),(4,1),(4,2),(4,3),(4,4),(5,0)\}\), differentiate with respect to \(a_5,\ldots,a_{10}\) at \(f_0\). If \((u)_{\underline h}=u!/(u-h)!\) for \(0\le h\le u\) and zero otherwise, its entry in column \(v\) is
\[
J_{(m,j),v}=2\sum_{u=0}^3\;\sum_{k=0}^{2m}
(-1)^k\binom{2m}{k}(10-u)_{\underline{2m-k}}
(u)_{\underline{k}}(10-v)_{\underline{k}}
(v)_{\underline{2m-k}}\,\mathbf1_{u+v=2m+j}.
\]
Dividing each row by its positive integral gcd yields the **exact** integer matrix
\[
B=\begin{pmatrix}
-5&8&-18&60&0&0\\
0&-3&10&-42&270&0\\
0&0&9&-4&-108&2700\\
0&0&0&5&-21&135\\
0&0&0&0&-3&10\\
0&0&-3&8&-36&360
\end{pmatrix},\qquad \det B=-1890000\ne0.
\]
The row gcds before normalization, in that order, are
\[
(2438553600,4877107200,2438553600,9754214400,14631321600,73156608000).
\]
The six equations vanish at \(f_0\): in each transvectant of order at least eight the total number of \(y\)-derivatives is at least eight, whereas each nonzero term of \(f_0\) has \(y\)-degree at most three. The nonzero determinant therefore gives Jacobian rank six. By the Jacobian criterion, \(X\) is regular of dimension four at \([f_0]\).

**4. Multiplicity and residual cycle.** Since \(T\subset X\) is a four-dimensional irreducible component and \(X\) is nonsingular at one point of \(T\), its generic point has length one in the fundamental cycle \([X]\). The remaining components form an effective four-cycle \(R\). Additivity of projective degree gives
\[
\deg R=\deg X-\deg T=64-28=36.
\]

## Verification
Run the supplied standalone script with `python3 checker.py`. It computes the six transvectant derivatives by integer falling factorials, checks that each quadric vanishes at \(f_0\), reconstructs all six primitive Jacobian rows, calculates the determinant by exact rational elimination, and checks the degree subtraction. Expected output: `VERIFY_OK: six quadrics, exact nonzero Jacobian determinant, residual degree 36`. The script uses only Python's standard library. The numerical Jacobian calculation is a **complete finite certificate for the claimed local rank**, while the source complete-intersection theorem and the above intersection-theoretic argument supply the global reasoning.

## Relationship to prior work
Massri's Theorem 1.1 and Proposition 6.1 establish the complete-intersection property and degree 64. His Section 6 proves reducibility at the boundary by observing that the degree 28 of the osculating component cannot divide 64. That argument alone does not determine whether the osculating component appears with multiplicity one or higher (or give the weighted residual degree). The explicit rank-six witness settles that missing multiplicity and gives residual degree 36. The paper points to a related, revised 2026 preprint arXiv:1202.5531v4 for the same reducibility example; its latest full text could not be inspected in this comparison, which remains a residual historical-priority risk. The older 2012 text at the base arXiv identifier is not treated as the 2026 revision.

## Limitations
The assertion is solely about the **four-dimensional fundamental cycle** in characteristic zero and for this particular \((p,r)\). It does not identify residual prime ideals, irreducible components, degrees of individual residual components, intersections between components, nilpotent structure away from the osculating component, or a general formula at other boundary parameters. The arithmetic certificate uses the monomial basis specified above and does not imply any independent mathematical audit or universal computer proof. The 2026 revision arXiv:1202.5531v4 remains a specific uninspected source.

## References
- C. Massri, *Quadratic hulls of osculating varieties of rational normal curves*, arXiv:2610.28499v1 (initial public version, 2026-10-20), especially Theorem 1.1 and Sections 2 and 6. https://arxiv.org/abs/2610.28499
- C. Massri, *Irreducibility of quadratic hulls of osculating varieties of closed orbits*, arXiv:1202.5531v4 (2026 revision, cited by the preceding paper); current complete text not inspected. https://arxiv.org/abs/1202.5531
- J. Weyman, *The equations of strata for binary forms*, J. Algebra **122** (1989), 244–249 (degree of coincident-root loci; the needed degree is also derived here).
