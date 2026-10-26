# Discrete positivity islands for exponential rank-metric kernels over finite fields

## Finding
Let \(q\) be a prime power and \(m\ge n\ge2\). On the additive group \(G=M_{m,n}(\mathbb F_q)\), consider the rank-metric stationary kernel
\[
K_t(X,Y)=t^{\operatorname{rank}(X-Y)},\qquad 0\le t\le1,
\]
where \(0^0=1\). Its complete positive-semidefiniteness set is the disconnected set
\[
\boxed{[0,q^{-(n-1)}]\ \cup\ \{q^{-k}:k=0,1,\ldots,n-2\}.}
\]
The kernel is strictly positive definite on every finite set of distinct matrices precisely when \(0\le t<q^{-(n-1)}\). At each exceptional point \(t=q^{-k}\), including the interval endpoint \(k=n-1\), the full convolution Gram matrix has exact rank
\[
\boxed{\sum_{s=0}^{k}{n\brack s}_q\prod_{i=0}^{s-1}(q^m-q^i)}.
\]
Here \({n\brack s}_q\) is the Gaussian binomial coefficient; empty products equal one. There are \(q^{mn}\) rows and columns in the full Gram matrix. In the damping parametrization \(t=e^{-a}\), finite \(a\ge0\), positive semidefiniteness holds exactly at \(a=0,\log q,\ldots,(n-2)\log q\) and for every \(a\ge(n-1)\log q\). In particular, this rank distance does not have negative type when \(n\ge2\): intermediate positive damping parameters are forbidden.

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary of prime-power cardinality \(q\); all matrix ranks are over this field. The smaller matrix dimension is \(n\), so transpose symmetry covers all rectangular spaces. Positive semidefiniteness means that \(\bigl[K_t(X_i,X_j)\bigr]_{i,j=1}^N\) is positive semidefinite for every positive integer \(N\) and arbitrary matrices \(X_i\in G\); strict positivity means positive definiteness whenever these matrices are pairwise distinct. Only \(0\le t\le1\) is classified. For \(n=1\), separately, all \(t\in[0,1]\) are admissible and strict positivity holds for \(t<1\).

Choose a nontrivial additive character \(\psi\) of \(\mathbb F_q\). Every Fourier character of \(G\) is \(\chi_B(X)=\psi(\operatorname{tr}(B^{\mathsf T}X))\), indexed by \(B\in G\). Unnormalized convolution eigenvalues are \(\lambda_B(t)=\sum_{X\in G} t^{\operatorname{rank} X}\overline{\chi_B(X)}\). By row/column symmetry they depend only on \(s=\operatorname{rank}B\); write \(\lambda_s(t)\).

## Proof
**1. A rank expansion into subgroup indicators.** For each integer \(r\ge0\) and indeterminate \(z\), the Gaussian-binomial Newton identity is
\[
z^r=\sum_{j=0}^r {r\brack j}_q\prod_{i=0}^{j-1}(z-q^i).
\]
To prove it, specialize \(z=q^h\) for any nonnegative integer \(h\). The left side counts all linear maps from an \(r\)-dimensional to an \(h\)-dimensional vector space. The summand of index \(j\) counts the rank-\(j\) maps: choose their kernel, of dimension \(r-j\), then choose an injective map on the quotient. Since the identity holds for infinitely many \(h\), it is a polynomial identity.

For \(X\in G\), write \(r=\dim\ker X=n-\operatorname{rank}X\). Substituting \(z=t^{-1}\), multiplying by \(t^n\), and regrouping the \(j\)-subspaces of the kernel gives, initially for \(t>0\) and then polynomially for \(t=0\),
\[
 t^{\operatorname{rank}X}=\sum_{j=0}^n c_j(t)\sum_{\substack{U\le\mathbb F_q^n\\\dim U=j}}\mathbf 1_{\{XU=0\}},
 \qquad c_j(t)=t^{n-j}\prod_{i=0}^{j-1}(1-q^it).
\]

**2. Fourier diagonalization.** For a fixed \(j\)-dimensional subspace \(U\), the set \(H_U=\{X:XU=0\}\) is an additive subgroup of size \(q^{m(n-j)}\). Its Fourier transform equals that cardinality when every row of the frequency matrix \(B\) belongs to \(U\), and zero otherwise, by character orthogonality. If \(B\) has rank \(s\), there are exactly \({n-s\brack j-s}_q\) such subspaces \(U\), and none if \(j<s\). Therefore all Fourier eigenvalues have the exact expression
\[
\boxed{\lambda_s(t)=\sum_{j=s}^n {n-s\brack j-s}_q\,q^{m(n-j)}t^{n-j}\prod_{i=0}^{j-1}(1-q^it)},\qquad 0\le s\le n.
\]
The associated eigenspace has dimension \({n\brack s}_q\prod_{i=0}^{s-1}(q^m-q^i)\), the number of rank-\(s\) frequency matrices. The usual Fourier diagonalization criterion says that \(K_t\) is positive semidefinite if and only if every \(\lambda_s(t)\) is nonnegative.

**3. Sufficiency and strictness.** For \(0\le t<q^{-(n-1)}\), every factor \(1-q^it\) occurring above is strictly positive; at \(t=0\), only the \(j=n\) term survives. In every case each \(\lambda_s(t)>0\), which establishes strict positive definiteness. If \(t=q^{-k}\) for an integer \(0\le k\le n-1\), then \(c_j(t)>0\) exactly for \(0\le j\le k\), while \(c_j(t)=0\) for \(j\ge k+1\). Hence \(\lambda_s(t)>0\) precisely when \(s\le k\), and it vanishes for \(s>k\). These are positive-semidefinite parameters, with the claimed matrix-rank formula.

**4. Excluding every other parameter.** For \(t>q^{-(n-1)}\), set \(P(t)=\prod_{i=0}^{n-2}(1-q^it)\). The two top frequency ranks in the displayed Fourier formula simplify to
\[
\lambda_n(t)=P(t)(1-q^{n-1}t),\qquad
\lambda_{n-1}(t)=P(t)\bigl(1+(q^m-q^{n-1})t\bigr).
\]
The first factor in parentheses is negative, whereas the second is strictly positive because \(m\ge n\). Whenever \(P(t)\ne0\), the two eigenvalues have opposite signs, forcing a negative eigenvalue. The only remaining points in \((q^{-(n-1)},1]\) are the roots \(t=q^{-k}\), for integers \(0\le k\le n-2\), which were already included. Necessity, all endpoints, and the exact rank statements follow.

## Verification
The fully standalone `verify_rank_kernel.py` uses only the Python standard library. Running `python verify_rank_kernel.py` checks the Fourier formula against exact character sums for binary spaces of shapes \(2\times2\), \(3\times2\), and \(3\times3\), and for the ternary space \(2\times2\), at rational parameters covering the admissible interval, forbidden gaps, special points, and endpoints. It also checks all predicted rank-support boundaries algebraically for field cardinalities \(2,3,4,5\) and smaller dimensions \(2,3,4,5\). The tested character-sum comparisons total 3,957, all exact rational equalities. This code is a finite consistency check; the proof above establishes the assertions for every prime-power field and all dimensions.

## Relationship to prior work
Delsarte's 1978 analysis of the bilinear-forms association scheme gives the general rank-distance character matrix in generalized Krawtchouk form and establishes MacWilliams inequalities. Gadouleau and Yan (2007) derive a functional rank-weight MacWilliams transform. Those results supply the natural harmonic-analysis setting and in principle permit evaluation of individual rank-radial Fourier transforms. The present result is the sharp positivity *parameter set* for a specific natural continuous one-parameter family, with explicit strictness and spectral ranks. Its two-highest-frequency exclusion mechanism and disconnected isolated positivity points are not stated in the inspected works. This comparison does not establish uniqueness against all unindexed literature.

## Limitations
The theorem concerns full additive matrix spaces over finite fields and real \(t\in[0,1]\), not arbitrary rank-invariant functions, symmetric/alternating bilinear form subspaces, or all negative \(t\). The rank assertions concern the complete Gram matrix on all \(q^{mn}\) group elements; its principal submatrices may have different ranks. The historical character-matrix formulas may make related parameter restrictions derivable by other methods; an equivalent earlier explicit sign classification outside the inspected sources remains possible. No independent mathematical audit has been performed.

## References
1. Ph. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory, Series A **25** (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8. In particular, Sections 2–3 and the Appendix.
2. M. Gadouleau and Z. Yan, *MacWilliams Identity for Codes with the Rank Metric*, arXiv:0706.1751 (first posted 12 June 2007), especially Sections II–IV.
