# Two sharp dimension barriers for fourth-order Gauss positivity on Boolean cubes

## Finding
Let \(Q_d\) be the binary \(d\)-cube with unit edge conductances, \(L_d=dI-A_d\) its combinatorial Laplacian, and
\[
T_d(h)=(12I-6hL_d+h^2L_d^2)(12I+6hL_d+h^2L_d^2)^{-1},\qquad h\ge0.
\]
This is the completed step of the two-stage, fourth-order Gauss–Legendre method for \(\dot u=-L_du\). Then:

1. For \(d=1,2\), \(T_d(h)\) is entrywise nonnegative at every \(h\ge0\), and strictly positive at every \(h>0\).
2. For each \(3\le d\le6\), some \(\epsilon_d>0\) makes \(T_d(h)\) strictly positive for \(0<h<\epsilon_d\); nevertheless, for sufficiently large \(h\), every entry joining adjacent vertices is **negative**.
3. For each \(d\ge7\), every entry between vertices at Hamming distance seven is **negative for all sufficiently small positive** \(h\), and every adjacent-vertex entry is negative for all sufficiently large \(h\). More precisely, for any distance-seven pair, \(T_d(h)_{uv}=-\frac{35}{12}h^7+O_d(h^8)\) as \(h\downarrow0\).

Thus the family has sharp boundaries at dimensions three (loss at sufficiently large steps) and seven (loss arbitrarily near zero), despite positive-definiteness and conservation for every step.

For the first nontrivial cube \(Q_3\), the entire entrywise-nonnegative timestep set is **exactly** \([0,\alpha]\), where \(\alpha=8.58376346373336\ldots\) is the unique positive root of
\[
p(h)=h^4-6h^3-20h^2-18h-6.
\]
At \(h=\alpha\), precisely the adjacent off-diagonal entries vanish. For \(h>\alpha\), precisely those entries are negative; the other off-diagonal entries and every diagonal entry remain positive.

## Assumptions and scope
The vertices of \(Q_d\) are binary strings of length \(d\), and edges flip exactly one bit. All edge conductances equal one; there are no boundary conditions or spatial rescalings. \(d\) is a positive integer, \(h\) is real and nonnegative. Entrywise positivity concerns the **completed** numerical map, not the internal Runge–Kutta stages. A matrix is called strictly positive if all its entries are positive, a different property from positive-definiteness. The exact heat semigroup \(e^{-hL_d}\) is strictly positive for every \(h>0\).

## Proof
**1. Scalar and spectral setup.** Write
\[
r(z)=\frac{12+6z+z^2}{12-6z+z^2};\quad T_d(h)=r(-hL_d).
\]
The Walsh character indexed by a set of \(k\) coordinates has Laplacian eigenvalue \(2k\). Hence, for vertices at distance \(j\),
\[
(T_d(h))_{uv}=2^{-d}\sum_{k=0}^d K_k(j)r(-2kh),\quad
K_k(j)=\sum_{a=\max(0,k-d+j)}^{\min(j,k)}(-1)^a\binom ja\binom{d-j}{k-a}.
\]
All denominators are positive for \(h\ge0\). For each real \(x\ge0\), \(r(-x)=[(x-3)^2+3]/[(x+3)^2+3]\in(0,1]\). Therefore all eigenvalues of \(T_d(h)\) are positive, its diagonal entries are positive, and \(T_d(h)\mathbf1=\mathbf1\). Thus only off-diagonal signs matter.

**2. Small-step dimension seven.** Direct expansion gives
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{144}+0z^6-\frac{z^7}{1728}+O(z^8).
\]
Put \(Q=A_d-dI=-L_d\). For vertices at distance \(j\), the first nonzero coefficient of \((r(hQ))_{uv}\), for \(1\le j\le6\), is respectively
\[
\begin{array}{c|cccccc}j&1&2&3&4&5&6\\\hline
\text{first term}&h&h^2&h^3&h^4&\tfrac56h^5&\tfrac{35d}{12}h^7\end{array}.
\]
Indeed the number of length-\(j\) geodesics is \(j!\); at distance six the order-six coefficient is zero and the first nonzero contribution at order seven is \(-\frac1{1728}(Q^7)_{uv}\). Bipartiteness rules out seven adjacency moves between even-distance vertices; exactly one diagonal stay along a six-step geodesic contributes, so \((Q^7)_{uv}=-7d\cdot 6!\). All displayed leading terms are strictly positive. For each fixed \(d\le6\), finitely many distance classes and positive diagonal entries therefore give a common positive small-step interval.

For \(d\ge7\), select two vertices at distance seven. Every power \(Q^m\) with \(m<7\) has zero entry between them, whereas \((Q^7)_{uv}=7!\). The coefficient \(-1/1728\) gives \(-7!h^7/1728=-35h^7/12\), strictly negative for all sufficiently small positive steps. This proves the sharp small-step dimension boundary.

**3. Eventual edge negativity.** The standard heat-kernel identity \(L_d^\dagger=\int_0^\infty(e^{-tL_d}-2^{-d}J)\,dt\), where \(J\) is the all-ones matrix, gives for neighboring vertices
\[
(L_d^\dagger)_{uv}=2^{-d-1}\int_0^1\frac{(1-s)(1+s)^{d-1}-1}{s}\,ds.
\]
At \(d=3\), this equals \(2^{-4}(1-\tfrac12-\tfrac13)=1/96>0\). At any fixed \(s\in(0,1)\), the numerator increases strictly with \(d\), so the integral is strictly positive for every \(d\ge3\). On the positive-eigenvalue subspace,
\[
r(-h\lambda)=1-\frac{12}{h\lambda}+O_\lambda(h^{-2})\qquad(h\to\infty),
\]
while \(r(0)=1\). The spectral decomposition thus yields \(T_d(h)=I-12L_d^\dagger/h+O_d(h^{-2})\). Every neighboring off-diagonal entry is consequently negative at sufficiently large \(h\) whenever \(d\ge3\).

**4. Unconditional dimensions one and two.** For \(Q_1\), the only nontrivial spectral eigenvalue is \(2\), and \(0<r(-2h)<1\) for \(h>0\). For \(Q_2\), every adjacent entry equals \(3h/(4h^2+6h+3)\) and the opposite-vertex entry equals
\[
\frac{9h^2(h+1)}{(h^2+3h+3)(4h^2+6h+3)}.
\]
These are positive for all \(h>0\); the diagonal is positive by the spectral argument. The \(h=0\) map is the identity.

**5. Exact eight-vertex horizon.** With \(D=(h^2+3h+3)(3h^2+3h+1)(4h^2+6h+3)>0\), the three off-diagonal distance classes in \(Q_3\) are
\[
\begin{aligned}
T_3(h;1)&=-\frac{3h(h^4-6h^3-20h^2-18h-6)}{2D},\\
T_3(h;2)&=\frac{3h^2(7h^3+18h^2+18h+6)}{2D},\\
T_3(h;3)&=\frac{3h^3(11h^2+18h+6)}{2D}.
\end{aligned}
\]
The last two are positive for every \(h>0\). The polynomial \(p\) has exactly one positive root by Descartes' rule of signs, \(p(0)<0\), and \(p(h)\to+\infty\). Its sign determines all adjacent entries, proving the exact claim.

## Verification
The accompanying standalone script `artifacts/verify_gauss_hypercubes.py` symbolically recomputes Padé coefficients, Walsh distance entries, the distance-one and distance-seven thresholds, the pseudoinverse identity for eight dimensions, the exact \(Q_2\) and \(Q_3\) formulas, and five independent full \(8\times8\) rational matrix inversions. It prints `VERIFY_OK` upon success. The infinite-dimensional dimension statements are established by Steps 2 and 3, not inferred from these finite checks.

## Relationship to prior work
Zappavigna–Colaneri–Kirkland–Shorten established that the diagonal Padé \([2/2]\) discretization can lose positivity for arbitrarily small steps; their 2012 paper exhibits the same negative seventh Taylor coefficient using a nilpotent eight-state shift. This **general mechanism is known and is not newly claimed here**. Their examples do not state the present hypercube small/large dimension classification, Green-function edge sign, or exact \(Q_3\) quartic horizon. General absolute-monotonicity theory likewise establishes lack of universal positivity guarantees, not the exact graph-family classification. The previously available exact formulas for strongly regular graphs and complete multipartite graphs do not specialize to \(Q_3\), whose nonadjacent vertices fall into two different distance classes. A published finite-state Markov example provides a distinct conservative eight-state pure-birth witness; it does not contain the hypercube horizon or family phase diagram. No broader published claim found in the sources inspected logically implies all parts of the stated conjunction. The known mechanism is acknowledged rather than presented as independently new.

## Limitations
For \(d=4,5,6\), this result establishes small-step positivity and eventual negativity but **does not classify every intermediate timestep**. For \(d\ge7\), it proves negative entries for sufficiently small and sufficiently large steps, not negativity for every positive step. The assertion is for unweighted cubes and exact arithmetic, not arbitrary weighted Hamming graphs or floating-point implementations. No claim of method-wide positivity or independent review is made. A specialized source not captured by the literature searches could have overlapping cube-specific results.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” MTNS (2010), public repository deposit 2010-10-15: https://mural.maynoothuniversity.ie/id/eprint/2195/.
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially Negative News About Positive Systems,” 2012 preprint, public repository deposit 2012-06-19: https://mural.maynoothuniversity.ie/id/eprint/3761/; journal version *Linear Algebra and its Applications* 436 (2012), 3425–3442, doi:10.1016/j.laa.2011.12.021.
3. J. A. van de Griend, J. F. B. M. Kraaijevanger, “Absolute monotonicity of rational functions occurring in the numerical solution of initial value problems,” *Numerische Mathematik* 49 (1986), 413–424, doi:10.1007/BF01389539.
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” public research record (2026): https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
