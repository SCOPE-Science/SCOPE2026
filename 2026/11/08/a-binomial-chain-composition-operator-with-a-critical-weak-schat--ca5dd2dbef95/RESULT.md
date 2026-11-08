# A binomial-chain composition operator with a critical weak-Schatten self-commutator

## Finding
Let \(n=2^k j\) be the unique factorization of each positive integer into a power of two and an odd integer \(j\). On the analytic coefficient Hilbert space \(H^2(\beta)\), set \(\beta_0=1\), \(\beta_{2^k j}=\binom{j+k}{k}^{-2}\), and \(\|f\|_\beta^2=\sum_{n\ge0}\beta_n|\widehat f(n)|^2\). The monomial composition operator \(C f=f(z^2)\) is a norm-one, noncompact, subnormal operator. Its positive self-commutator \(D=C^*C-CC^*\) is compact, and has exactly the eigenvalues
\[
 d_{j,k}=\frac{j\bigl(j(2k+1)+2k(k+1)\bigr)}{(j+k)^2(j+k+1)^2},\quad j\ge1\text{ odd},\quad k\ge0,
\]
with multiplicities in the multiset sense, plus a zero eigenvalue for the constants. For \(N_D(t)=\#\{n:s_n(D)>t\}\),
\[
 \lim_{t\downarrow0}t^2N_D(t)=\frac1{30},\qquad
 \lim_{n\to\infty}\sqrt n\,s_n(D)=\frac1{\sqrt{30}}.
\]
Consequently \(D\in\mathcal S_p\) if and only if \(p>2\), and \(D\in\mathcal S_{2,\infty}\setminus\mathcal S_2\). The constant \(1/30\) is sharp.

## Assumptions and scope
The space and operator are complex. Indices \(n\) run over nonnegative integers, \(j\) over positive odd integers, \(k\) over nonnegative integers. The convention is \(\mathcal S_{2,\infty}\) for weak Schatten two. The coefficient weights are positive, at most one, and satisfy \(\lim_{n\to\infty}\beta_n^{1/n}=1\): indeed \(\beta_n^{-1}\le (2n)^{2\log_2 n}\) for \(n\ge2\). Hence all members are analytic throughout the open unit disk. No standard Hardy-space equivalence, universal composition-operator boundedness, or sharp constant for other symbols is claimed.

## Proof
Put \(u_n=z^n/\sqrt{\beta_n}\). These form an orthonormal basis. The constant vector is fixed. The positive indices split into disjoint dyadic orbits \(\{j,2j,4j,\ldots\}\), one for each odd \(j\). On the orbit indexed by \(j\), composition is a forward unilateral weighted shift, with
\[
 Cu_{2^kj}=r_{j,k}u_{2^{k+1}j},\qquad r_{j,k}=\sqrt{\beta_{2^{k+1}j}/\beta_{2^kj}}=\frac{k+1}{j+k+1}.
\]
Every weight is positive and below one, so \(\|C\|=1\). Along the orbit \(j=1\), \(r_{1,k}\to1\). Therefore \(C\) is not compact and has essential norm one.

For every positive integer \(j\), let \(X_j,Y_j\) be independent variables on \([0,1]\) with density \(j(1-x)^{j-1}\). Their product has moments
\[
 \mathbb E[(X_jY_j)^k]=\left(\frac{k!j!}{(j+k)!}\right)^2.
\]
These are exactly the squared products of the first \(k\) shift weights. A rotationally invariant measure on the disk with squared radial coordinate distributed as \(X_jY_j\) makes the monomials orthogonal with these squared norms. Multiplication by the coordinate is a normal extension of each orbit shift. Their orthogonal sum (together with the constant identity) gives a normal extension of \(C\), proving subnormality.

The self-commutator is diagonal in this basis. At the starting vector of each orbit its eigenvalue is \(r_{j,0}^2\); at position \(k\ge1\) it is \(r_{j,k}^2-r_{j,k-1}^2\). Set \(r_{j,-1}=0\), so the displayed formula follows by elementary rational simplification, and it is strictly positive. The difference-of-squares representation gives the uniform bound
\[
 0<d_{j,k}\le\frac{2j}{(j+k)(j+k+1)}\le\frac2{j+k}.
\]
For every positive threshold only finitely many pairs satisfy \(d_{j,k}>t\). Thus \(D\) is positive compact.

It remains to prove the precise spectral distribution. Write \(x=tj\) and \(y=tk\). Uniformly on compact subsets of the positive quadrant avoiding the origin,
\[
 \frac{d_{j,k}}{t}\longrightarrow F(x,y)=\frac{2xy}{(x+y)^3}.
\]
The bound \(d_{j,k}\le 2/(j+k)\) confines every counted lattice point to \(x+y<2\). A small square around the origin contributes at most its area times the lattice density; its scaled contribution tends to zero as its side decreases. The level curve \(F(x,y)=1\) has planar measure zero. Hence ordinary two-dimensional Riemann sums, with mesh \(2t\) in the odd-\(j\) direction and \(t\) in the \(k\) direction, yield
\[
 \lim_{t\downarrow0}t^2N_D(t)=\frac12\operatorname{area}\{(x,y):x>0,y>0,F(x,y)>1\}.
\]
Set \(y=sx\). Since \(dy\,dx=x\,ds\,dx\), the condition becomes \(x<h(s)=2s/(1+s)^3\), and the limit equals
\[
 \frac14\int_0^\infty h(s)^2\,ds
 =\int_0^\infty\frac{s^2}{(1+s)^6}\,ds
 =B(3,3)=\frac{2!2!}{5!}=\frac1{30}.
\]
Inverting this strict singular-value counting law gives \(s_n(D)\sim(30n)^{-1/2}\). The Schatten assertions follow from comparison with the \(p/2\)-power harmonic series; the endpoint weak ideal follows from boundedness of \(\sqrt n\,s_n(D)\). All quantifiers and constants above are exact.

## Verification
Run `python checker.py` with standard Python 3. The checker tests 3,829 exact rational identities, inequalities and moment ratios across sampled orbit parameters, and counts eigenvalues above four exact reciprocal thresholds by integer arithmetic. It prints `DYADIC_BINOMIAL_CHECK_OK 3829 exact assertions`. In particular, \(t^2N_D(t)\) is close to \(1/30\) at the tested thresholds. The proof of the infinite counting limit is the preceding Riemann-sum argument, not any finite count.

## Relationship to prior work
Cruz-Zamorano, Dellepiane and Seco (2026, arXiv:2610.40148v1) investigate which coefficient weights preserve compact and Schatten membership of composition operators. Their theorems concern compactness/Schatten membership of \(C_\varphi\) itself and equivalence between classes for different weights, not singular values of its self-commutator. Classical treatments of essential normality for unweighted Hardy composition operators concern a different coefficient space. Weighted-shift theory supplies standard subnormality tools; the exact two-dimensional binomial-orbit spectral coefficient is the new calculation here.

## Limitations
The result concerns this explicit weight and the symbol \(z^2\), not all weights or symbols. The constant for the singular distribution is analytical; finite checker output only corroborates it. Earlier general results for weighted shifts and self-commutators could imply a reformulation of this specific calculation; literature coverage is not independent priority certification. Nothing is asserted about a full independent audit.

## References
- F. J. Cruz-Zamorano, E. Dellepiane and D. Seco, *Compact and Hilbert-Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1 (first submitted 2026-10-29), especially Sections 1, 5 and 6.
- A. L. Shields, *Weighted shift operators and analytic function theory*, Mathematical Surveys 13, American Mathematical Society, 1974.
- P. S. Bourdon, D. Levi, S. K. Narayan and J. H. Shapiro, *Which linear-fractional composition operators are essentially normal?*, J. Math. Anal. Appl. 280 (2003), 30–53.
- M. Katz, *Essentially Normal Composition Operators on \(H^2\)*, arXiv:1503.06165 (2015).
