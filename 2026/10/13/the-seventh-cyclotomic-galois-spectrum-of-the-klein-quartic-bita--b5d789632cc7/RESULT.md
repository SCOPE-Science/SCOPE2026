# The seventh-cyclotomic Galois spectrum of the Klein quartic bitangents

## Finding
Let \(C/\mathbb Q\) be the plane Klein quartic \(X^3Y+Y^3Z+Z^3X=0\), and count a hyperflex tangent as a bitangent (so a contact divisor of the form \(2P+2Q\) allows \(P=Q\)). The 28 geometric bitangent lines have **minimal common field of definition** \(K=\mathbb Q(\zeta_7)\), of degree six. As a \(\operatorname{Gal}(K/\mathbb Q)\)-set they consist of one orbit of length one, one orbit of length three, and four orbits of length six. Thus exactly one is individually \(\mathbb Q\)-rational, three have minimal field the real cubic subfield \(K^+=\mathbb Q(\zeta_7+\zeta_7^{-1})\), and the other 24 each require \(K\).

For every **odd prime** \(p\ne7\), \(C\) has smooth reduction and all 28 geometric bitangents reduce to distinct bitangents. The number \(N_p\) of individual bitangent lines defined over \(\mathbb F_p\) is exactly
\[
N_p=\begin{cases}
28,&p\equiv1\pmod7,\\
4,&p\equiv6\pmod7,\\
1,&p\equiv2,3,4,5\pmod7.
\end{cases}
\]
The natural densities of primes in these three cases are \(1/6\), \(1/6\), and \(2/3\), respectively. This counts lines, not \(\mathbb F_p\)-points of the curve or tangency points.

## Assumptions and scope
Put \(\zeta=\zeta_7\) for a primitive seventh root of unity, \(R=\mathbb Z[\zeta]\), and \(\Phi_7(t)=1+t+\cdots+t^6\). We use column coordinates for points, row coordinates for line equations, and the usual cyclotomic embeddings \(\sigma_k(\zeta)=\zeta^k\) for \(k=1,\ldots,6\). If a line has row \((a,b,c)\), the projective transformation \(M\) pulls its equation back to \((a,b,c)M\). The theorem concerns the specified rational integral model; it does not identify bitangent fields of arbitrary twists or of the alternative Ciani pencil models. Characteristic two and seven are excluded from the good-reduction assertion.

## Proof
**1. The exact 28-line orbit.** Define
\[
u=\zeta-\zeta^6,\qquad v=\zeta^2-\zeta^5,\qquad w=\zeta^4-\zeta^3,
\]
and matrices
\[
S=\begin{pmatrix}\zeta&0&0\\0&\zeta^4&0\\0&0&\zeta^2\end{pmatrix},\quad
T=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\quad
U=\begin{pmatrix}u&v&w\\v&w&u\\w&u&v\end{pmatrix}.
\]
A direct calculation in \(R=\mathbb Z[t]/(\Phi_7(t))\) gives
\[
F(S\mathbf x)=F(\mathbf x),\quad F(T\mathbf x)=F(\mathbf x),\quad F(U\mathbf x)=49F(\mathbf x),
\]
where \(F=X^3Y+Y^3Z+Z^3X\). Also \(\det U=7(1+2\zeta+2\zeta^2+2\zeta^4)\) has nonzero norm \(7^9\); hence these are automorphisms over \(K\) and remain invertible away from seven. The initial line \(L_0:X+Y+Z=0\) is a bitangent because
\[
F(X,Y,-X-Y)=-(X^2+XY+Y^2)^2.
\]
Form the smallest set \(\mathcal B\) of projective line rows containing \((1,1,1)\) and stable under right multiplication by \(S,T,U\). Exact arithmetic in \(R\) gives **28 distinct rows**, all uniquely normalized \((1,b,c)\) with \(b,c\in R\). One member is \((1,\zeta^3,\zeta)\). The exhaustive closure is reproduced by `verify_klein.py`; neither numerical coordinates nor a black-box symmetry classification are assumed. Because the curve is smooth in characteristic zero and a smooth plane quartic in characteristic different from two has 28 geometric bitangents, \(\mathcal B\) is the complete bitangent set.

**2. The exact Galois representation.** Apply each of \(\sigma_k\), \(1\le k\le6\), to every coefficient of the normalized rows and normalize again. The exact fixed-line counts are
\[
\#\mathcal B^{\sigma_1}=28,\quad
\#\mathcal B^{\sigma_2}=\#\mathcal B^{\sigma_3}
=\#\mathcal B^{\sigma_4}=\#\mathcal B^{\sigma_5}=1,\quad
\#\mathcal B^{\sigma_6}=4.
\]
The corresponding complete orbit sizes are \(1,3,6,6,6,6\); for the length-three orbit complex conjugation fixes every row. Its field is exactly \(K^+\). The line \((1,\zeta^3,\zeta)\) has field of definition exactly \(K\), since its coefficient ratio contains \(\zeta\). All the other coefficients lie in \(K\), proving minimality of the *common* field.

**3. Uniform reduction at every odd prime other than seven.** The three partial derivatives are
\[
F_X=3X^2Y+Z^3,\quad F_Y=X^3+3Y^2Z,\quad F_Z=Y^3+3Z^2X.
\]
A common projective zero of these derivatives cannot have a zero coordinate. Multiplication of the equations after all coordinates are nonzero implies \(1=-27\), hence \(28=0\) in the field. Therefore the quartic is smooth at every odd prime different from seven.

The displayed integral orbit rows might conceivably collide after reduction, even at a smooth prime; this requires an independent test. For every one of the \(\binom{28}{2}=378\) unordered pairs, write \(d=b_i-b_j\) and \(e=c_i-c_j\) in \(R\). If the lines coincide at some geometric point over a prime of residue characteristic \(p\), then \(\Phi_7,d,e\) have a common root over an algebraic closure of \(\mathbb F_p\). The exact norms \(\operatorname{Res}(\Phi_7,d)\) and \(\operatorname{Res}(\Phi_7,e)\), with norm of zero taken as zero, have gcd-distribution
\[
\begin{array}{c|rrrrrrrrr}
\gcd\text{ of absolute norms}&1&7&29&43&49&64&203&448&497\\\hline
\text{pairs}&21&84&42&42&21&42&42&42&42.
\end{array}
\]
Thus the only *candidate* primes are \(2,7,29,43,71\). For each candidate and pair, the exact polynomial gcd \(\gcd(\overline\Phi_7,\overline d,\overline e)\) over \(\mathbb F_p[t]\) has positive degree for 84 pairs at \(p=2\), 231 pairs at \(p=7\), and **no pairs** at \(p=29,43,71\). Hence the 28 lines remain pairwise geometrically distinct for every odd \(p\ne7\). All 28 are still bitangents because the quartic pullback identities hold after reduction, with \(49\) invertible, and the initial restriction is still a square; distinctness and the characteristic-odd 28-bitangent theorem establish completeness.

**4. Frobenius fixed points and densities.** For \(p\ne7\), the cyclotomic field \(K\) is unramified at \(p\); arithmetic Frobenius induces \(\zeta\mapsto\zeta^p\). Since no two geometric lines coalesce, a reduced line is \(\mathbb F_p\)-rational precisely when its normalized row is fixed by this Frobenius element. The six fixed-counts in Step 2 give the three-case formula. Dirichlet's theorem on primes in reduced residue classes modulo seven yields the asserted densities.

## Verification
The standalone `verify_klein.py` uses exact arithmetic in \(\mathbb Q[t]/(\Phi_7)\), polynomial expansion of the three pullbacks, exact orbit enumeration, 378 pairwise resultant and residue-field gcd tests, and all six Galois fixed counts. It asserts each conclusion before returning `VERIFY_OK`. A separate direct enumeration inside that same executable factors the restricted binary quartic over \(\mathbb F_p\) for every rational projective line at eight primes \(p=3,5,11,13,17,19,23,29\), obtaining \(1,1,1,4,1,1,1,28\) bitangent lines. This finite census corroborates but does not replace the universal algebraic arguments of Steps 1–4. Reproduce with `python verify_klein.py` using Python 3 and SymPy.

## Relationship to prior work
Janasz–Pokora–Zieliński, *On arrangements of smooth plane quartics and their bitangents* (arXiv:2308.16514, first public 2023-08-31), establish the **geometric** 28-line configuration and its 252 double and 21 quadruple intersection points. Their Table 2 gives explicit bitangents for a Klein quartic model in a Ciani pencil over a quadratic number field; their paper states that it works over complex numbers. Those geometric counts and equations are not claimed as new here. Bethea–Brazelton, *Bitangents to symmetric quartics* (arXiv:2410.09242, 2024), give the geometric automorphism-group action on all 28 Klein bitangents and report **four real bitangents**; their supplementary tables give numerical line coefficients. Their automorphism orbits (transitive under a 168-element geometric group) are logically different from the six cyclotomic Galois orbits of the rational model proved here. In particular the known count of four real bitangents is **not** claimed as an original component; the theorem supplies the exact arithmetic splitting field, field degrees, and every-good-prime Frobenius count, not obtained by stating the complex incidence or geometric group action. The classical 28-bitangent theorem and cyclotomic Frobenius law are used as inputs.

## Limitations
No claim is made about the geometry or bitangent count in characteristics two or seven, any other rational twist of the Klein quartic, or the rationality of tangency *points*. The theorem gives a complete algebraic derivation for the specified model. Prior-work searches do not exclude unindexed older explicit Galois computations; historical Klein-quartic literature may contain equivalent arithmetic descriptions. The auxiliary finite-field tests are checks, not the proof for infinitely many primes.

## References
1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514v1 (2023-08-31), Section 3.1, Proposition 3.1, Table 2. https://arxiv.org/abs/2308.16514
2. C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242v1 (2024-10-11), Theorem 1.1 and Section 4.1. https://arxiv.org/abs/2410.09242
3. C. Bethea, T. Brazelton, *Equations for bitangents to symmetric quartics*, supplementary numerical data, Section 1. https://tbrazel.github.io/supplementary/lines.pdf
4. Classical smooth-plane-quartic/odd-theta-characteristic correspondence and the cyclotomic Frobenius theorem (standard inputs).
