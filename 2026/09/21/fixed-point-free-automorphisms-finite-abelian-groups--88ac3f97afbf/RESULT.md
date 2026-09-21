# Exact counts of fixed-point-free automorphisms of finite abelian groups

Let \(\theta(G,d)\) denote the number of automorphisms of a finite group \(G\) having exactly \(d\) fixed points. This note gives a closed formula for \(\theta(A,1)\) for every finite abelian group \(A\).

## Theorem

Write the primary decomposition as
\[
A=\bigoplus_p A_p,\qquad
A_p\cong\bigoplus_{r\ge 1}(\mathbf Z/p^r\mathbf Z)^{m_{p,r}},
\]
where only finitely many multiplicities \(m_{p,r}\) are nonzero. For \(m\ge 0\), define
\[
D_m(p)=\#\{X\in \operatorname{GL}_m(\mathbf F_p):\det(X-I)\ne 0\},
\qquad D_0(p)=1.
\]
Then
\[
\boxed{
\theta(A,1)
=|\operatorname{Aut}(A)|
\prod_p\prod_{r:m_{p,r}>0}
\frac{D_{m_{p,r}}(p)}{|\operatorname{GL}_{m_{p,r}}(\mathbf F_p)|}.}
\]
Moreover,
\[
\boxed{
D_m(p)=|\operatorname{GL}_m(\mathbf F_p)|
\sum_{j=0}^m
\frac{(-1)^j p^{\binom j2}}{|\operatorname{GL}_j(\mathbf F_p)|},}
\]
with \(|\operatorname{GL}_0(\mathbf F_p)|=1\).

For a single \(p\)-primary group, let \(\lambda\) be the partition whose part \(r\) occurs \(m_r\) times, and let \(\lambda'\) be the conjugate partition. Using the standard order formula for the automorphism group gives the equivalent closed form
\[
\boxed{
\theta(A_p,1)
=p^{\sum_j(\lambda'_j)^2-\sum_r m_r^2}
\prod_{r:m_r>0}D_{m_r}(p).}
\]

## Proof

It is enough first to treat a finite abelian \(p\)-group
\[
P\cong\bigoplus_{i=1}^n \mathbf Z/p^{e_i}\mathbf Z,
\qquad 1\le e_1\le\cdots\le e_n.
\]
Hillar and Rhea give a matrix model for \(\operatorname{End}(P)\): an endomorphism is represented by an integer matrix \(M=(m_{ij})\) satisfying
\[
p^{e_i-e_j}\mid m_{ij}\quad\text{whenever }i\ge j,
\]
and the represented endomorphism is an automorphism exactly when \(M\bmod p\) is invertible.

Group equal exponents together. If an exponent \(r\) occurs \(m_r\) times, then modulo \(p\) every matrix representing an endomorphism is block upper triangular, with one diagonal block \(B_r\in M_{m_r}(\mathbf F_p)\) for each occurring exponent \(r\). Therefore an automorphism has each \(B_r\in\operatorname{GL}_{m_r}(\mathbf F_p)\).

The map
\[
\rho:\operatorname{Aut}(P)\longrightarrow
\prod_{r:m_r>0}\operatorname{GL}_{m_r}(\mathbf F_p),
\qquad \varphi\longmapsto(B_r)_r,
\]
is a well-defined surjective homomorphism. It is well defined because two matrices representing the same endomorphism differ, in row \(i\), by entries divisible by \(p^{e_i}\), hence have the same reduction modulo \(p\). It is surjective because any tuple of invertible diagonal blocks can be lifted to a block-diagonal representing matrix.

For finite \(P\), an automorphism \(\varphi\) is fixed-point-free if and only if \(\varphi-I\) is an automorphism. In the matrix model, \(\varphi-I\) is represented by \(M-I\), whose reduction modulo \(p\) has diagonal blocks \(B_r-I\). Hence
\[
\varphi\text{ is fixed-point-free}
\iff
\det(B_r-I)\ne0\quad\text{for every }r.
\]
All fibers of the surjective group homomorphism \(\rho\) have the same cardinality. Consequently,
\[
\theta(P,1)
=|\ker\rho|\prod_r D_{m_r}(p),
\qquad
|\operatorname{Aut}(P)|
=|\ker\rho|\prod_r|\operatorname{GL}_{m_r}(\mathbf F_p)|,
\]
which proves the product-ratio formula for \(P\).

The familiar automorphism-count formula
\[
|\operatorname{Aut}(P)|
=p^{\sum_j(\lambda'_j)^2}
\prod_r\prod_{i=1}^{m_r}(1-p^{-i})
\]
can be rewritten as
\[
|\operatorname{Aut}(P)|
=p^{\sum_j(\lambda'_j)^2-\sum_r m_r^2}
\prod_r |\operatorname{GL}_{m_r}(\mathbf F_p)|,
\]
and substitution gives the stated closed \(p\)-primary formula.

It remains to evaluate \(D_m(p)\). For \(X\in\operatorname{GL}_m(\mathbf F_p)\), the indicator that \(\operatorname{Fix}(X)=0\) is obtained by Möbius inversion in the lattice of subspaces of \(\mathbf F_p^m\). A \(j\)-dimensional subspace has Möbius value
\[
(-1)^j p^{\binom j2}.
\]
For a fixed \(j\)-dimensional subspace \(W\), the number of invertible matrices fixing \(W\) pointwise is
\[
p^{j(m-j)}|\operatorname{GL}_{m-j}(\mathbf F_p)|.
\]
Multiplying by the Gaussian binomial coefficient counting choices of \(W\) simplifies to
\[
{m\brack j}_p p^{j(m-j)}|\operatorname{GL}_{m-j}(\mathbf F_p)|
=\frac{|\operatorname{GL}_m(\mathbf F_p)|}{|\operatorname{GL}_j(\mathbf F_p)|}.
\]
Summing the Möbius contributions gives the displayed formula for \(D_m(p)\).

Finally, Sylow subgroups of a finite abelian group are characteristic, so
\[
\operatorname{Aut}(A)\cong\prod_p\operatorname{Aut}(A_p).
\]
An automorphism of \(A\) is fixed-point-free exactly when every primary component is fixed-point-free. The counts therefore multiply over \(p\), completing the proof.

## Distinct-exponent corollary

Suppose
\[
A=\bigoplus_{i=1}^n \mathbf Z/p^{a_i}\mathbf Z,
\qquad 1\le a_1<a_2<\cdots<a_n.
\]
Every occurring exponent has multiplicity one, so \(D_1(p)=p-2\). Also
\[
\sum_j(\lambda'_j)^2
=\sum_{i=1}^n(2n-2i+1)a_i.
\]
Hence
\[
\boxed{
\theta(A,1)
=p^{\sum_{i=1}^n(2n-2i+1)a_i-n}(p-2)^n.}
\]
For \(n=2\) this is
\[
p^{3a_1+a_2-2}(p-2)^2,
\]
exactly the formula proved by Hayat, López-Aguayo and Abbas. Their 2018 paper ends by asking for the theta values of direct sums with pairwise distinct exponents; the displayed formula determines the fixed-point-free case \(d=1\) for every rank.

## Consequences

The proportion of fixed-point-free automorphisms of an abelian \(p\)-group depends only on the multiplicities of its cyclic exponents:
\[
\frac{\theta(A_p,1)}{|\operatorname{Aut}(A_p)|}
=\prod_r\frac{D_{m_r}(p)}{|\operatorname{GL}_{m_r}(\mathbf F_p)|}.
\]
It is independent of the numerical exponent values \(r\).

For odd \(p\), every \(D_m(p)\) with \(m\ge1\) is positive (for example, a nonidentity scalar matrix is fixed-point-free), so every finite abelian group of odd order admits a fixed-point-free automorphism. For \(p=2\), \(D_1(2)=0\), while \(D_m(2)>0\) for every \(m\ge2\). Thus an abelian \(2\)-group admits a fixed-point-free automorphism exactly when no cyclic exponent occurs with multiplicity one. This recovers Gross's 1968 existence criterion while additionally giving the exact count.

## Verification

The accompanying script checks the finite-field derangement formula by brute force for small \(p,m\), and independently enumerates all endomorphism matrices for several small abelian \(p\)-groups. It agrees with the theorem for, among others,
\[
C_2^2,\ C_4^2,\ C_2\oplus C_4,\ C_2^2\oplus C_4,\ C_3\oplus C_9,\ C_3^2\oplus C_9.
\]
The general theorem does not rely on these finite checks.

## Limitations

The formula counts only the fixed-point-free stratum \(\theta(A,1)\). It does not determine \(\theta(A,d)\) for \(d>1\), where the size of the fixed subgroup depends on finer integral data than the semisimple diagonal blocks modulo \(p\). Thus the full 2018 distinct-exponent theta-value problem remains open beyond \(d=1\).

Originality is asserted only to the best of our knowledge. The ingredients—matrix models for automorphisms of finite abelian groups, the criterion that \(\varphi-I\) be invertible, and finite-field derangement counting—are standard. No prior source was located that combines them into the exact product formula above or the all-rank distinct-exponent formula, but an implicit or differently phrased antecedent remains possible.

## References

1. C. J. Hillar and D. L. Rhea, *Automorphisms of finite Abelian groups*, Amer. Math. Monthly **114** (2007), 917–923. https://doi.org/10.1080/00029890.2007.11920485 ; preprint: https://arxiv.org/abs/math/0605185
2. U. Hayat, D. López-Aguayo and A. Abbas, *Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group*, Symmetry **10** (2018), 238. https://doi.org/10.3390/sym10070238
3. J. Checco, R. Darling, S. Longfield and K. Wisdom, *On the Fixed Points of Abelian Group Automorphisms*, Rose-Hulman Undergraduate Mathematics Journal **11** (2010), Article 3. https://scholar.rose-hulman.edu/rhumj/vol11/iss2/3/
4. F. Gross, *Some Remarks on Groups Admitting a Fixed-Point-Free Automorphism*, Canadian J. Math. **20** (1968), 1300–1307. https://doi.org/10.4153/CJM-1968-128-5
5. P. Senden, *The Reidemeister spectrum of finite abelian groups*, Proc. Edinburgh Math. Soc. **66** (2023), 1014–1033. https://doi.org/10.1017/S0013091523000500
