# Exact endpoint norms and Euler-product scaling for the first Grassmann Fourier projection

## Finding
For every prime power \(q\ge2\), integers \(n\ge2\) and \(1\le k\le\lfloor n/2\rfloor\), the first nonconstant Grassmann harmonic projector has an exact endpoint norm controlled by the proportion of mutually disjoint subspaces. Put
\[
X=\operatorname{Gr}_{q}(n,k),\quad
B=\binom{n}{k}_{q},\quad
v=[n]_q=\frac{q^n-1}{q-1},\quad
R=[k]_q=\frac{q^k-1}{q-1}.
\]
Then the orthogonal projection \(E_1\) onto the mean-zero span of projective-point incidences satisfies
\[
\boxed{\|E_1\|_{\ell^1(X)\to\ell^1(X)}=\|E_1\|_{\ell^\infty(X)\to\ell^\infty(X)}
=\frac{2R(v-1)}{v-R}\,\frac{q^{k^2}\binom{n-k}{k}_{q}}{B}.}
\]
Its complementary projection has the exact norm
\[
\boxed{\|I-E_1\|=1+\|E_1\|-\frac{2(v-1)}{B},}
\]
with the same value on both endpoints. For fixed \(q\) and \(s\in\mathbb Z_{\ge0}\), writing \(n=2k+s\),
\[
\boxed{\lim_{k\to\infty}\frac{\|E_1\|}{q^k}
=\frac{2}{q-1}\prod_{r=s+1}^{\infty}(1-q^{-r}).}
\]
All products converge to strictly positive constants.

## Assumptions and scope
The field has \(q\) elements, where \(q\) is an arbitrary prime power. Each element of \(X\) is a \(k\)-dimensional linear subspace of \(\mathbb F_q^n\). The norms are of the indicated matrix acting on complex-valued functions on \(X\); using counting or normalized counting in both domain and codomain yields the same operator norms. Write \([j]_q=(q^j-1)/(q-1)\), with \([0]_q=0\).

For each one-dimensional subspace \(p\) of \(\mathbb F_q^n\), let \(h_p(U)=\mathbf1_{\{p\subset U\}}\). Define \(W_1=\operatorname{span}_{\mathbb C}\{h_p-R/v:p\}\) and \(E_1\) as the orthogonal projection onto \(W_1\). The space \(W_1\) has dimension \(v-1\) and is the first nonconstant spherical harmonic component in the usual Grassmann scheme ordering [2,3].

## Proof
**Incidence Gram calculation.** Let \(H\) be the \(B\)-by-\(v\) point-subspace incidence matrix. Its row sums are \(R\). Every projective point lies in exactly \(BR/v\) members of \(X\), and every ordered pair of distinct projective points lies in exactly \(BR(R-1)/(v(v-1))\) members. Thus, for \(T=H(I_v-v^{-1}J_v)\),
\[
T^*T=\frac{BR(v-R)}{v(v-1)}(I_v-v^{-1}J_v).
\]
Since the displayed coefficient is strictly positive, \(T\) has rank \(v-1\), and
\[
E_1=\frac{v(v-1)}{BR(v-R)}TT^*.
\]
For \(U,V\in X\), \((HH^*)_{UV}=[\dim(U\cap V)]_q\), so
\[
\boxed{E_1(U,V)=\frac{v(v-1)}{BR(v-R)}
\left([\dim(U\cap V)]_q-\frac{R^2}{v}\right).}
\]
In particular the rows sum to zero and each diagonal is \((v-1)/B\).

**The sign boundary.** Because \(n\ge2k\), one has \(v\ge[2k]_q=R(q^k+1)\); also \(R<q^k+1\) for all \(q\ge2\). Therefore \(0<R^2/v<1\). Consequently the kernel is strictly negative if and only if \(U\cap V=\{0\}\), and is strictly positive otherwise (including the diagonal). The number of \(k\)-subspaces disjoint from a fixed \(k\)-space is
\[
D_{n,k,q}=q^{k^2}\binom{n-k}{k}_{q}.
\]
Indeed, choose the projection of the candidate disjoint space onto a fixed complement of the reference \(k\)-space; this is an arbitrary \(k\)-space in the complement, together with an arbitrary linear map of it into the reference space. The latter maps give exactly \(q^{k^2}\) lifts. The magnitude of each negative kernel entry is \((v-1)R/(B(v-R))\). Because every row sums to zero, its absolute sum is twice its total negative mass. It follows that
\[
\|E_1\|_{\infty\to\infty}=
\frac{2R(v-1)}{v-R}\frac{D_{n,k,q}}B.
\]
By symmetry of \(E_1\) and transitivity on \(X\), the same holds for the column-sum \(\ell^1\) norm. For the complement, its off-diagonal entries are the negatives of those of \(E_1\); the diagonal contribution changes from \((v-1)/B\) to \(1-(v-1)/B\), so its norm is \(1+\|E_1\|-2(v-1)/B\).

**Balanced-rank asymptotics.** Set \(n=2k+s\) for a fixed \(s\ge0\). The exact Gaussian-binomial identity is
\[
\frac{D_{n,k,q}}B
=\frac{\prod_{r=s+1}^{k+s}(1-q^{-r})}
{\prod_{r=k+s+1}^{2k+s}(1-q^{-r})}.
\]
As \(k\to\infty\), the numerator converges to \(\prod_{r=s+1}^{\infty}(1-q^{-r})\) and the denominator tends to \(1\). At the same time \(R/q^k\to1/(q-1)\) and \((v-1)/(v-R)\to1\), proving the claimed limit.

## Verification
The accompanying standalone `verify_grassmann.py` independently checks both the full absolute-intersection sum and the simplified formula using exact rational arithmetic for 500 parameter triples with \(q\in\{2,3,4,5,7\}\), \(2\le n\le20\), and \(1\le k\le\lfloor n/2\rfloor\). It also enumerates actual row-reduced-echelon subspaces and directly sums kernel magnitudes in 15 small prime-field examples. The program prints `VERIFY_OK q_binomial_cases=500 explicit_rref_cases=15 fields=2,3` on successful completion. These finite tests supplement, but do not establish, the all-parameter proof.

## Relationship to prior work
Scarabotti–Tolli [1] establish the finite-homogeneous-space harmonic-analysis setting and its spherical-function decompositions, with primary MSC 43A95, but do not evaluate this Grassmann endpoint norm. Srinivasan [2] explicitly constructs a common orthogonal eigenbasis for the Grassmann scheme, while Filmus–Ihringer [3] identify its first-degree incidence harmonic component in the course of classifying Boolean degree-one functions. Neither inspected work states the absolute row-sum identity, complement norm, or balanced-rank infinite-product endpoint coefficient. The claim does not assert novelty for the representation decomposition, incidence dimensions, or the classical disjoint-subspace count individually.

## Limitations
The theorem treats only the canonical first nonconstant Grassmann harmonic component, not higher primitive idempotents or intermediate \(L^p\) norms. The finite checker cannot certify statements for all field sizes or dimensions. Older literature on Grassmann association schemes and \(q\)-Hahn polynomials may contain an equivalent endpoint norm in another normalization; independent literature review remains appropriate. No independent audit has been performed.

## References
[1] F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1 (first public 19 January 2007), primary MSC 43A95; https://arxiv.org/abs/math/0701533.

[2] M. K. Srinivasan, *The Goldman–Rota identity and the Grassmann scheme*, arXiv:1304.6244v1 (23 April 2013); https://arxiv.org/abs/1304.6244.

[3] Y. Filmus and F. Ihringer, *Boolean degree 1 functions on some classical association schemes*, arXiv:1801.06034v1 (18 January 2018); https://arxiv.org/abs/1801.06034.
