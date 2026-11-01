# Rational Fourier-null densities of dyadic simplex measures, with an exact eight-atom law

## Finding
For every integer \(K\ge2\), let \(\mu_K\) be the uniform dyadic simplex self-similar measure in \(\mathbb R^{K-1}\) defined below. The set of integer frequencies annihilated by its Fourier transform has a natural density \(\delta_K\). For odd \(K\), this density is zero, and in fact there are no integer Fourier zeros. For even \(K\), \(\delta_K\) is rational and is obtained by an explicit finite recursion on even integer partitions of \(K\).

For the eight-atom measure in \(\mathbb R^7\), let \(J\) be the first dyadic mask level at which an integer Fourier frequency vanishes, with \(J=\infty\) for no vanishing level. With frequency interpreted as a Haar-uniform seven-dimensional 2-adic integer vector, its first-zero generating function is
\[
\boxed{\sum_{j\ge1}\mathbb P(J=j)z^j
=\frac{35z(32768+512z+304z^2+7z^3)}{(128-z)(64-z)(32-z)(16-z)}.}
\]
Consequently, the exact natural density of annihilated integer Fourier frequencies is
\[
\boxed{\delta_8=\frac{11197}{35433}=0.316004854231930\ldots.}
\]
The same generating function gives every finite-resolution first-zero census, and its initial probabilities are \(35/128\), \(595/16384\), and \(11795/2097152\) for first-zero levels one, two, and three, respectively.

## Assumptions and scope
Fix \(K\ge2\), set \(d=K-1\), and let \(U_1,U_2,\ldots\) be independent random vectors each uniform on the \(K\)-point digit set \(D_K=\{0,e_1,\ldots,e_d\}\subset\mathbb R^d\). Define
\[
\mu_K=\operatorname{Law}\left(\sum_{j=1}^{\infty}2^{-j}U_j\right),\qquad
\widehat\mu_K(m)=\int_{\mathbb R^d}e^{-2\pi i m\cdot x}\,d\mu_K(x).
\]
The zero-frequency value is one. For every nonzero \(m\in\mathbb Z^d\), define its first zero level \(J(m)\) as the least positive integer \(j\) for which
\[
M_{K,j}(m)=\frac1K\left(1+\sum_{i=1}^{d}e^{-2\pi i m_i/2^j}\right)=0,
\]
with \(J(m)=\infty\) if none exists. Put \(Z_K=\{m\in\mathbb Z^d:\widehat\mu_K(m)=0\}\), and define natural density by centered cubes:
\[
\delta_K=\lim_{N\to\infty}
\frac{\#\bigl(Z_K\cap[-N,N]^d\bigr)}{(2N+1)^d}.
\]
This limit is asserted to exist; the ambient dimension varies with \(K\). All exact Fourier-zero statements concern integer frequencies, not arbitrary real frequencies. The generating-function probability is with respect to normalized Haar measure on \(\mathbb Z_2^7\), which agrees with densities of finite congruence classes.

## Proof
**1. Integer Fourier zeros occur at finite mask levels.** Independence gives
\[
\widehat\mu_K(m)=\prod_{j=1}^{\infty}M_{K,j}(m).
\]
For fixed integer \(m\), the bound \(|1-e^{it}|\le |t|\) yields
\[
\sum_{j\ge1}|1-M_{K,j}(m)|\le
\frac{2\pi}{K}\sum_{i=1}^{d}|m_i|\sum_{j\ge1}2^{-j}<\infty.
\]
Since the factors converge to one, a product without zero factors converges to a nonzero value. Thus \(\widehat\mu_K(m)=0\) exactly when some \(M_{K,j}(m)=0\).

**2. Cyclotomic prefix-balance criterion.** Fix \(j\ge1\) and let \(a_0=0\), \(a_i=m_i\). Write \(c_r\) for the number of the \(K\) integers \(a_i\) congruent to \(r\) modulo \(2^j\), where \(0\le r<2^j\). For a primitive \(2^j\)-th root \(\zeta\), the mask vanishes if and only if \(P(\zeta)=0\) for \(P(X)=\sum_{r=0}^{2^j-1}c_rX^r\). Since \(\Phi_{2^j}(X)=X^{2^{j-1}}+1\) and \(\deg P<2^j\), divisibility by this cyclotomic polynomial is equivalent to
\[
\boxed{c_r=c_{r+2^{j-1}}\quad(0\le r<2^{j-1}).}
\]
Therefore every residue class modulo \(2^{j-1}\) must have even multiplicity, split equally between its two possible next binary digits. For odd \(K\), this is impossible at every level, proving the asserted absence of zeros.

**3. Finite even-partition mechanism for all even \(K\).** Let \(K\) be even. A simultaneous translation of the \(K\) integer exponents multiplies their root sum by a unit complex number and does not change its zeros. Accordingly, the distribution of the zero events for \((0,m_1,\ldots,m_{K-1})\), with \(m_i\) independent Haar-uniform elements of \(\mathbb Z_2\), agrees with that for \(K\) independent Haar-uniform 2-adic exponents: subtract one of them from all the others.

At binary prefix depth \(t\), partition the \(K\) exponents by congruence modulo \(2^t\), retaining only the sorted list \(s=(s_1,\ldots,s_b)\) of occupied class sizes. If any class size is odd, no deeper mask can vanish: at a later vanishing level all its refined sub-classes would have even size, impossible because their total is odd. Until this terminal obstruction, every occupied class has even size. Conditioned on an even state \(s\), the new binary digit divides each class of size \(s_i\) independently into counts \(A_i\) and \(s_i-A_i\), where \(A_i\sim\operatorname{Binomial}(s_i,1/2)\). A zero occurs at this next level if and only if \(A_i=s_i/2\) for every class. Its probability is
\[
q(s)=\prod_{i=1}^b\frac{\binom{s_i}{s_i/2}}{2^{s_i}}.
\]
If this immediate success does not occur, and every positive child size is still even, transition to the sorted even child-size partition. Otherwise enter a terminal failure state. Let \(T(s,s')\) be the resulting non-success, live-state transition probability; equivalently it is the sum of \(2^{-K}\prod_i\binom{s_i}{a_i}\) over all valid split vectors \((a_i)\) producing \(s'\), excluding the simultaneously balanced vector.

There are finitely many even partitions of \(K\). All non-self transitions strictly increase the number of blocks, and the self-transition probability at a state with \(b\) blocks is \(2^{b-K}<1\). Thus the recursion
\[
F(s)=q(s)+\sum_{s'}T(s,s')F(s')
\]
has a unique rational solution by descending block count (or by the inverse of \(I-T\)); the initial value \(F((K))\) is the probability of some zero at any finite scale. The first-hit generating function has the precise matrix form
\[
G_K(z)=z\,e_{(K)}^{\mathsf T}(I-zT)^{-1}q.
\]
In particular, \(G_K(1)=F((K))\) is rational. Every state has a positive immediate-hit probability, so because the state set is finite there is a positive minimum of these probabilities. The mass remaining in live states decays geometrically with prefix depth.

For each fixed depth \(L\), the event of a zero at some level at most \(L\) is a union of residue classes modulo \(2^L\), and therefore has precisely its Haar measure as a centered-cube natural density. Any first zero beyond level \(L\) must belong to the live-state residue classes at depth \(L\), whose density tends geometrically to zero. Squeezing between these fixed-depth cylinder sets proves existence of the natural density and identifies it with \(G_K(1)\).

**4. Exact eight-atom transition computation.** For \(K=8\), the only live partitions reachable before the first zero are
\[
A=(8),\quad B=(2,6),\quad D=(2,2,4),\quad E=(2,2,2,2).
\]
Their immediate-hit probabilities and nonzero live transitions are, exactly:

| State | Immediate hit \(q\) | Nonzero entries of \(T\) |
| --- | --- | --- |
| \(A\) | \(35/128\) | \(T_{A,A}=1/128\), \(T_{A,B}=7/32\) |
| \(B\) | \(5/32\) | \(T_{B,B}=1/64\), \(T_{B,D}=15/64\) |
| \(D\) | \(3/32\) | \(T_{D,D}=1/32\), \(T_{D,E}=3/32\) |
| \(E\) | \(1/16\) | \(T_{E,E}=1/16\) |

Each entry follows from independent binomial splitting; all unlisted probability goes to terminal failure. In particular, the balanced \((4,4)\) split from \(A\) is an immediate zero, not a live \((4,4)\) state. The four equations for first-hit generating functions are
\[
\begin{aligned}
G_E&=z(1+G_E)/16,\\
G_D&=z(3+G_D+3G_E)/32,\\
G_B&=z(10+G_B+15G_D)/64,\\
G_A&=z(35+G_A+28G_B)/128.
\end{aligned}
\]
Solving yields \(G_A(z)\) as displayed in the finding. At \(z=1\), the individual eventual-hit probabilities are
\[
F(E)=\frac1{15},\qquad F(D)=\frac{16}{155},\qquad
F(B)=\frac{358}{1953},\qquad F(A)=\frac{11197}{35433}.
\]
Since \(G_A(1)\) equals the lattice density, this proves the exact eight-atom statement.

## Verification
The accompanying standalone Python 3 script `verify_density.py` uses only the standard library. It enumerates all binomial splitting patterns for the four reachable states; compares the resulting rational transition entries and the four rational hitting probabilities to independently stated fractions; checks the two-atom and four-atom boundary cases; and directly enumerates all \(2^7\) and \(4^7\) residue-frequency vectors to certify the first two finite censuses. It also verifies the first four first-hit probabilities against the transition process. Its expected success line is `DYADIC_EIGHT_ATOM_NULL_DENSITY_OK rational=11197/35433 L1=35/128 L2=5075/16384`.

A separate exhaustive direct residue test at modulus eight, not needed for the proof, gave first-hit counts \(573440\), \(76160\), and \(11795\) at levels one, two, and three, summing to \(661395\) of the \(2^{21}\) residue vectors. This independently matches the generating function's first three coefficients. These finite checks do not replace the cyclotomic and infinite-state-tail arguments.

## Relationship to prior work
The primitive prime-power cyclotomic cancellation mechanism is classical; in particular, Lam and Leung's work on vanishing sums of roots of unity contains a substantially more general algebraic classification of allowable cancellations. The self-similar Fourier product is likewise standard in affine-IFS Fourier analysis, including the work of Jorgensen and Pedersen and of Dutkay and Jorgensen. These components are used rather than claimed as new.

The contribution asserted here is the finite even-partition first-hit mechanism establishing rational **natural densities for an entire family** of dyadic simplex measures, and its explicit eight-atom first-hit generating function and density. A classification of possible cyclotomic cancellations alone does not give the density of their union over all dyadic levels: first hits at different scales overlap nontrivially, and surviving even prefix partitions must be counted. Comparisons with accessible related research did not identify a stronger result already furnishing these exact distributional formulas.

## Limitations
The theorem concerns Fourier zeros on \(\mathbb Z^{K-1}\), not arbitrary real frequencies. The general theorem gives a finite rational algorithm, not a closed formula uniform in the number of atoms. A related older article by Strichartz on self-similar Fourier transforms was identified but its full text could not be examined, so previously unlocated equivalent coverage remains a risk. This is a mathematical proof and bounded literature assessment, not an independently validated certification.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, initial public arXiv version dated 1995-11-13, https://arxiv.org/abs/math/9511209 ; *Journal of Algebra* 224 (2000), 91–109.
2. P. E. T. Jorgensen and S. Pedersen, *Harmonic Analysis of Fractal Measures*, initial public arXiv version dated 2006-04-04, https://arxiv.org/abs/math/0604087 .
3. D. E. Dutkay and P. E. T. Jorgensen, *Probability and Fourier duality for affine iterated function systems*, initial arXiv release dated 2008-08-21, https://arxiv.org/abs/0808.2946 .
4. R. S. Strichartz, *Self-Similar Measures and Their Fourier Transforms. III*, *Indiana University Mathematics Journal* 42 (1993), 367–411, https://doi.org/10.1512/iumj.1993.42.42018 . Full text not inspected.
