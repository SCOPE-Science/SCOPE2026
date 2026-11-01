# Complete quadratic Walsh sampling spectrum on a split binary quadric

## Finding
For each integer \(m\ge2\), write \(n=2m\), and let
\[
X_m=\left\{x\in\mathbb F_2^{2m}:Q(x)=\sum_{j=1}^m x_{2j-1}x_{2j}=0\ \text{in}\ \mathbb F_2\right\}.
\]
For every subset \(A\subseteq\{1,\ldots,n\}\) of size at most two, let \(\chi_A(x)=(-1)^{\sum_{i\in A}x_i}\). Equip \(X_m\) with uniform probability measure and define the Gram matrix \(G_m=(\mathbb E_{x\in X_m}\chi_A(x)\chi_B(x))_{A,B}\). Its size is \(N_m=1+n+\binom n2=2m^2+m+1\).

Put \(s_\pm=-(n-3)\pm\sqrt{(n-3)^2+8}\), and let \(\rho_1,\rho_2,\rho_3\) be the three real roots, with multiplicities, of
\[
p_n(t)=t^3+\frac{-n^2+7n-14}{2}t^2+(-n^2+n-2)t+8.
\]
Then the **complete Gram spectrum** is \(g_m(\theta)=(2^m+\theta)/(2^m+1)\), applied to the following finite multiset of \(\theta\)-values:

| Parameter \(\theta\) | Multiplicity |
| --- | ---: |
| Each \(\rho_j\) | 1 |
| Each of \(s_+\), \(s_-\) | \(m-1\) |
| Each of \(-s_+\), \(-s_-\) | \(m\) |
| \(4\) | \(m(m-1)\) |
| \(-4\) | \(m(m-2)\) |

Equal numerical levels are combined by adding their multiplicities. At \(m=2\) the Gram matrix has nullity **exactly one**; at every \(m\ge3\) it is positive definite. Thus quadratic Walsh polynomials are uniquely determined by samples on \(X_m\) precisely from six binary variables onward (within the stated range).

For \(m\ge3\), let \(\rho_m\) be the largest root of \(p_{2m}\), and put \(\eta_m=(2m-3)+\sqrt{(2m-3)^2+8}\). The sharp eigenvalue bounds are
\[
\lambda_{\min}(G_m)=\frac{2^m-\eta_m}{2^m+1},\qquad
\lambda_{\max}(G_m)=\frac{2^m+\rho_m}{2^m+1}.
\]
Consequently the exact spectral condition number of the evaluation map is
\[
\boxed{\kappa_2(E_m)^2=\frac{2^m+\rho_m}{2^m-\eta_m}},
\qquad \kappa_2(E_m)=1+O(m^2 2^{-m}).
\]
The eigenvalue multiplicities and sharp bounds hold for every \(m\ge3\), without numerical root approximations.

## Assumptions and scope
All arithmetic in \(Q\), the polar pairing, and the indexing vectors is in \(\mathbb F_2\). Spectrum, complex linear independence, condition number, and matrix eigenvalues are over \(\mathbb C\). The sampling inner product is conditional probability on \(X_m\), not unnormalized counting measure. The distinguished coordinate pairs are \(\{2j-1,2j\}\). The result concerns the entire degree-at-most-two coordinate Walsh band, including the constant and first-degree characters; arbitrary affine changes to coordinates need not preserve this band.

## Proof
**1. The quadratic character sum and normalization.** For a single binary pair,
\[
\sum_{x,y\in\mathbb F_2}(-1)^{xy+ax+by}=2(-1)^{ab}.
\]
Multiplying over the \(m\) independent pairs proves
\[
\sum_{x\in\mathbb F_2^n}(-1)^{Q(x)+u\cdot x}=2^m(-1)^{Q(u)},
\qquad |X_m|=2^{2m-1}+2^{m-1}.
\]
For distinct frequency indices \(A,B\), uniform sampling therefore gives
\[
(G_m)_{AB}=\frac{(-1)^{Q(1_A+1_B)}}{2^m+1},
\]
while the diagonal is one. Here \(1_A\) denotes the binary incidence vector. Set \(D_{AA}=(-1)^{Q(1_A)}\), and let \(P\) send a subset to the result of exchanging the two entries of every distinguished coordinate pair. The polar identity
\(Q(u+v)=Q(u)+Q(v)+u^TJv\), with \(J\) the coordinate-pair swap, gives
\[
D G_m D=\frac{2^m I+PW}{2^m+1},\qquad W_{AB}=(-1)^{|A\cap B|}.
\]
The matrix \(W\) is indexed by all subsets of \(\{1,\ldots,n\}\) of size at most two. Both \(P\) and \(W\) are self-adjoint, and they commute.

**2. Hamming-ball harmonic decomposition.** Under permutations of \(n\) coordinates, the space of functions on subsets of size zero, one, or two splits into: (a) three trivial-representation copies; (b) two copies of the standard zero-sum coordinate representation; (c) one pair-harmonic representation of dimension \(n(n-3)/2\), characterized by zero sums at every vertex.

On the three normalized rank-constant vectors, \(W\) is the real symmetric matrix similar to
\[
K_n=\begin{pmatrix}
1&n&\binom n2\\
1&n-2&\frac{(n-1)(n-4)}2\\
1&n-4&\frac{n^2-9n+16}2
\end{pmatrix}.
\]
Indeed the entry in row rank \(r\), column rank \(s\), is the Krawtchouk count \(\sum_j(-1)^j\binom rj\binom{n-r}{s-j}\), and similarity is by the square roots of the rank sizes \(1,n,\binom n2\). Direct determinant expansion gives \(\det(tI-K_n)=p_n(t)\).

On the two standard copies, choose the normalized incidence intertwiner sending a zero-sum vector \(z\) to the pair function \((z_i+z_j)/\sqrt{n-2}\). The induced symmetric matrix is
\[
S_n=\begin{pmatrix}-2&-2\sqrt{n-2}\\-2\sqrt{n-2}&-2(n-4)\end{pmatrix},
\]
whose eigenvalues are \(s_+\) and \(s_-\). On pair harmonics, the pair--pair block is \(J-2A_{J(n,2)}\), where the Johnson adjacency has eigenvalue \(-2\), so \(W\) acts by \(4\).

**3. Paired-coordinate involution.** The swap permutation \(P\) acts as identity on the three trivial copies. On the standard zero-sum representation its \(+1\) and \(-1\) eigenspaces have dimensions \(m-1\) and \(m\). The permutation has \(m\) fixed two-element subsets, while its traces on the trivial and standard summands of the pair representation are \(1\) and \(-1\). Thus its trace on pair harmonics is \(m\), and its \(+1\) and \(-1\) multiplicities there are respectively \(m(m-1)\) and \(m(m-2)\). Since \(P\) commutes with \(W\), multiplying the eigenvalues of the three blocks by these \(P\)-signs gives every listed \(\theta\), without omitted dimensions.

**4. Rank and boundary.** A multilinear real polynomial of total degree at most two has the same span on the Boolean cube as the stated Walsh band. If it vanishes on \(X_m\), evaluate it first at the zero vector, all singletons, and all two-point supports that are *not* one of the \(m\) distinguished pairs; all such points lie in \(X_m\). These evaluations force every coefficient except the coefficients of \(x_{2j-1}x_{2j}\) to vanish. A point with exactly two distinguished pairs activated also lies in \(X_m\), forcing \(c_i+c_j=0\) for all distinct \(i,j\). For \(m\ge3\), all coefficients vanish; for \(m=2\), this leaves exactly one dimension, generated by \(x_1x_2-x_3x_4\). This proves the all-dimensional rank assertions independently of numeric spectral tests.

**5. Sharp extrema.** For \(n\ge6\), the normalized symmetric rank-constant block \(T\) is congruent by positive diagonal similarity to \(K_n\). For \(c=2(n-3)\), its leading principal minors after adding \(cI\) are
\[
2n-5,\quad 2(n-2)(3n-10),\quad 2(n-5)(n-2)^2(n-1),
\]
all positive. Sylvester's criterion shows every root of \(p_n\) exceeds \(-2(n-3)\), whereas \(s_-<-2(n-3)<-4\) and \(-s_+>s_-\). Hence \(s_-\) is strictly the smallest \(\theta\).

Put \(\eta_n=-s_-=(n-3)+\sqrt{(n-3)^2+8}\). It satisfies \(\eta_n^2-2(n-3)\eta_n-8=0\), and division of \(p_n\) by this quadratic gives
\[
p_n(\eta_n)=-(n-3)\bigl((n^2-10n+28)\eta_n+4n-32\bigr)<0
\]
for every even \(n\ge6\). The largest root \(\rho_n\) thus exceeds \(\eta_n\). It also exceeds \(4\), since \(T\) has diagonal entry \(n-2\ge4\) with a nonzero off-diagonal coupling. Therefore \(\rho_n\) is strictly the largest \(\theta\). Finally \(\eta_n<2^m\) for \(m\ge3\): check \(m=3\) directly, and for \(m\ge4\) use \(\eta_n<4m-6+4/(2m-3)<4m\le2^m\). This proves the positive lower bound and the exact condition-number formula. The entries of \(T\) and the quadratic formula yield \(\rho_n=O(n^2)\), while \(\eta_n=O(n)\), giving the stated asymptotic bound.

## Verification
Run `python3 artifacts/verify.py` with Python 3, NumPy, and SymPy. The checker independently enumerates every point of \(X_m\) for \(m=2,3,4,5\), constructs the unrestricted degree-two character evaluation matrices, compares 5,110 Gram entries exactly after clearing denominators, and compares all 126 eigenvalues and the boundary ranks. It also checks the cubic characteristic polynomials and the nonstandard Sylvester and polynomial-division identities symbolically. These finite tests corroborate, but do not replace, the proofs for arbitrary \(m\).

## Relationship to prior work
The classical bent-function and Hadamard-difference-set character identities motivate the restriction problem. Leopardi (arXiv:1504.02827) studies Cayley graphs from bent functions and Clifford-algebra constructions, not the complete degree-two restricted Walsh Gram spectrum. Earlier work on Boolean-function spectra likewise treats full Walsh transforms and Cayley eigenvalues rather than this band-limited sampling problem. A related published first-Walsh-band theorem on all nonsingular binary quadrics proves degree-one injectivity and a graph transfer law; its stated scope explicitly excludes higher Walsh degrees. The present claim is a complete degree-two spectrum for the distinguished split form, including exact multiplicities, a sharp degree-two rank boundary, and a cubic-controlled condition number, not a restatement of the degree-one result.

## Limitations
Only the split paired-coordinate quadratic form and the specified degree-two coordinate band are covered. Spectra for arbitrary nonsingular quadratic forms in arbitrary fixed coordinates or higher Walsh degrees are not claimed. The 2003 and 2015 sources concern bent-function constructions and Cayley-graph theory; an older equivalent in association-scheme or punctured Reed--Muller literature cannot be entirely excluded without comprehensive historical access. Independent validation has not been performed.

## References
1. A. Grocholewska-Czuryło, *A study of differences between bent functions constructed using Rothaus method and randomly generated bent functions*, Journal of Telecommunications and Information Technology 4 (2003), 19–24, published 2003-12-30, https://www.jtit.pl/jtit/article/view/205/205.
2. P. Leopardi, *Twin bent functions, strongly regular Cayley graphs, and Hurwitz–Radon theory*, arXiv:1504.02827, version 1 publicly posted 2015-04-11; revised full text consulted, https://arxiv.org/abs/1504.02827.
3. A. Bernasconi and B. Codenotti, *Spectral analysis of Boolean functions as a graph eigenvalue problem*, IEEE Transactions on Computers 48 (1999), 345–351, DOI 10.1109/12.755000.
4. *Dual symplectic graphs govern first-Walsh-band sampling on binary quadrics*, published research statement (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dual-symplectic-graphs-govern-first-walsh-band-sampling-on-binar--f73b283fd6aa.
