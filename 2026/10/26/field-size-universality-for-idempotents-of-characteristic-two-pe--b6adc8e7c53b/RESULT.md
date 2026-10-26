# Field-size universality for idempotents of characteristic-two perfect evolution algebras

## Finding
Let \(n\geq 1\) and \(q=2^m\) with \(m\geq1\). Choose uniformly at random an invertible \(n\times n\) matrix \(M\) over \(\mathbb F_q\), and give \(\mathbb F_q^n\) the evolution-algebra product determined by \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=\sum_j M_{ij}e_j\). Let \(I(M)\) be the number of *nonzero* idempotent elements, that is, solutions of \(x^2=x\) with \(x\ne0\).

**Distribution theorem.** For every \(q=2^m\), the law of \(I(M)\) is independent of \(m\). More precisely, it is the law of \(2^D-1\), where \(D=\dim_{\mathbb F_2}\ker(G-I)\) for uniform \(G\in\mathrm{GL}_n(\mathbb F_2)\). Thus the only possible values are \(2^d-1\) for \(0\le d\le n\). With \(g_t=|\mathrm{GL}_t(\mathbb F_2)|\), \(g_0=1\), and Gaussian coefficients \({a\brack b}_2\), the exact probabilities are
\[
\Pr(I(M)=2^d-1)=\frac{{n\brack d}_2}{g_n}\sum_{j=0}^{n-d}(-1)^j2^{\binom j2}{n-d\brack j}_2\,2^{(d+j)(n-d-j)}g_{n-d-j}.
\]
In particular, for \(n=2\), the probabilities of \(0,1,3\) nonzero idempotents are exactly \(1/3,1/2,1/6\) for **every** even prime-power field. For \(n=3\), the probabilities for \(0,1,3,7\) nonzero idempotents are \(2/7,7/12,1/8,1/168\), respectively. For fixed \(n=3\), the no-idempotent probability therefore remains \(2/7\) along \(q=2^m\to\infty\).

**Consequence for a recent asymptotic formulation.** The unrestricted-prime-power reading of the fixed-point-distribution consequence asserted after Conjecture 2 of Kaygorodov--Martín González--Viruel (2026) is false: for \(n=3\), the fixed-point-free probability of a uniform permutation on seven letters is \(103/280\), not \(2/7\). This does **not** disprove the conjecture's main characteristic-zero generic Galois-group assertion, or make any claim about odd characteristic.

For completeness, as \(n\to\infty\), the probability that there is no nonzero idempotent tends to
\[
\prod_{j=1}^{\infty}(1-2^{-j})=0.288788095\ldots.
\]

## Assumptions and scope
An evolution algebra is a commutative, generally nonassociative algebra with a natural basis in which products of distinct basis elements are zero. A structure matrix is **perfect** precisely when invertible, and randomness means the uniform measure on *labeled invertible structure matrices*, not on isomorphism classes. We count idempotent **elements** \(x\) satisfying \(x^2=x\), not algebras sometimes themselves called idempotent or perfect. The field is specifically \(\mathbb F_{2^m}\); there is no assertion about odd characteristic. The Gaussian coefficient is \({a\brack b}_2=\prod_{i=0}^{b-1}(2^a-2^i)/(2^b-2^i)\) for \(0\le b\le a\), otherwise zero; \(g_t=\prod_{i=0}^{t-1}(2^t-2^i)\).

## Proof
Write \(x=(x_1,\dots,x_n)^T\), and set \(x^{[2]}=(x_1^2,\dots,x_n^2)^T\). The idempotent equations are \(M^T x^{[2]}=x\). Since transposition and inversion are bijections of \(\mathrm{GL}_n(\mathbb F_q)\), the matrix \(A=(M^T)^{-1}\) is uniform, and the equations become \(x^{[2]}=Ax\). The solution set \(W_A\) is a vector space over the fixed field of squaring, namely \(\mathbb F_2\).

**Independence lemma.** Every \(\mathbb F_2\)-independent collection of vectors in \(W_A\) is linearly independent over \(\mathbb F_q\). Indeed, if not, choose a smallest \(\mathbb F_q\)-dependent subcollection \(v_1,\ldots,v_k\) and write \(v_k=\sum_{i<k}c_iv_i\). Applying coordinatewise squaring and also applying \(A\) to this relation gives \(\sum_{i<k}(c_i^2-c_i)v_i^{[2]}=0\). The \(v_i^{[2]}\) are \(\mathbb F_q\)-independent because field Frobenius is an automorphism and the \(v_i\) are independent. Hence every \(c_i^2=c_i\), so \(c_i\in\mathbb F_2\), contradicting the original \(\mathbb F_2\)-independence. In particular, \(D_A=\dim_{\mathbb F_2}W_A\le n\), and \(I(M)=2^{D_A}-1\).

For \(0\le k\le n\), put \(F_k(d)=\prod_{i=0}^{k-1}(2^d-2^i)\) (empty product \(F_0=1\)). This counts ordered independent \(k\)-frames in an \(\mathbb F_2\)-space of dimension \(d\). By the lemma, each such solution frame \(X=(v_1,\ldots,v_k)\) is an \(\mathbb F_q\)-frame. For every such \(X\), its squared image \(X^{[2]}\) is also an \(\mathbb F_q\)-frame. The number of matrices \(A\in\mathrm{GL}_n(\mathbb F_q)\) satisfying \(AX=X^{[2]}\) is exactly
\[
\frac{|\mathrm{GL}_n(\mathbb F_q)|}{\prod_{i=0}^{k-1}(q^n-q^i)},
\]
by transitivity on ordered frames. As there are \(\prod_{i=0}^{k-1}(q^n-q^i)\) frames, double counting \((A,X)\) gives \(\mathbb E_A[F_k(D_A)]=1\) for every \(0\le k\le n\).

For uniform \(G\in\mathrm{GL}_n(\mathbb F_2)\), the same frame count, now with \(GX=X\), yields \(\mathbb E_G[F_k(D_G)]=1\). The \((n+1)\)-by-\((n+1)\) matrix \((F_k(d))_{0\le k,d\le n}\) is upper triangular, with nonzero diagonal \(F_d(d)=g_d\). Hence the \(n+1\) moments determine the full distribution on \(d\in\{0,\ldots,n\}\) uniquely; consequently \(D_A\) and \(D_G\) have identical laws. This proves field-size universality.

To obtain the exact formula, fix a \(d\)-dimensional subspace \(U\subseteq\mathbb F_2^n\). A matrix fixing \(U\) pointwise has a block form \(\bigl(\begin{smallmatrix}I_d&B\\0&C\end{smallmatrix}\bigr)\), with \(B\) arbitrary and \(C\in\mathrm{GL}_{n-d}(\mathbb F_2)\); therefore there are \(2^{d(n-d)}g_{n-d}\) such matrices. Möbius inversion in the lattice of subspaces containing \(U\), whose interval Möbius function for codimension \(j\) is \((-1)^j2^{\binom j2}\), gives the number whose **exact** fixed space is \(U\):
\[
\sum_{j=0}^{n-d}(-1)^j2^{\binom j2}{n-d\brack j}_2\,2^{(d+j)(n-d-j)}g_{n-d-j}.
\]
There are \({n\brack d}_2\) possible spaces \(U\). Dividing by \(g_n\) gives the claimed distribution. The \(n=2,3\) fractions follow by substitution; for the symmetric group comparison, the number of derangements of seven letters is \(1854\), hence \(1854/7!=103/280\), while \(48/168=2/7\) for \(\mathrm{GL}_3(\mathbb F_2)\).

Finally, the indicator of \(D_G=0\) has the subspace inclusion--exclusion representation \(\sum_{j=0}^{D_G}(-1)^j2^{\binom j2}{D_G\brack j}_2\). Since a fixed \(j\)-frame has expectation \(1\), and \(g_j{D_G\brack j}_2=F_j(D_G)\), we obtain \(\Pr(D_G=0)=\sum_{j=0}^n(-1)^j2^{\binom j2}/g_j\). The limit follows by absolute convergence and Euler's standard binary product identity, giving \(\prod_{j\ge1}(1-2^{-j})\).

## Verification
A standalone standard-library Python checker, `verify.py`, implements arithmetic in \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\) from polynomial multiplication, enumerates every invertible structure matrix, tests every putative idempotent vector, and independently computes the subspace-Möbius probability formula. It exhaustively verifies \((n,q)=(1,2),(1,4),(2,2),(2,4),(2,8),(3,2)\), including \(3528\) invertible matrices at \((2,8)\). It also checks normalized formulas for all dimensions through \(n=12\). Run using `python verify.py` (Python 3, no packages). The output ends `VERIFY_OK`. Finite tests are corroboration, not proof of the arbitrary-dimension statement.

## Relationship to prior work
Kaygorodov, Martín González and Viruel, *Evolution algebras: a survey of results and a list of open problems* (arXiv:2610.22248, posted 15 October 2026), Remark 23, prove that the **mean** number of nonzero idempotents for a uniformly random invertible structure matrix over every finite field is one. Our theorem determines the complete distribution, shows its independence of \(q=2^m\), and exhibits an exceptional characteristic-two asymptotic regime. That source's Conjecture 2 concerns the generic characteristic-zero Galois group; only the conjecture's proposed unrestricted field-size consequence is contradicted here, not its main characteristic-zero statement.

Dempwolff, Fisher and Herman (2000) provide a normal-form theorem for semilinear maps over finite fields. General fixed-space counts for matrices over \(\mathbb F_2\) are classical. Neither fact is claimed as new; the identified contribution is the exact statistical transfer to idempotent solutions for random perfect evolution algebras over **every** binary extension field and its sharp contrast with the proposed symmetric-group law. Wei and Zou (2023) count isomorphism classes of perfect evolution algebras, a different sampling question. Existing special constructions of idempotent-free perfect evolution algebras establish existence, not the distribution.

## Limitations
Results are for uniform labeled structure matrices over finite fields of characteristic two; they do not count isomorphism classes and do not extend to characteristic three or other odd primes. The main characteristic-zero generic Galois-group conjecture is not disproved. More general semilinear group formulas might imply the field-size universality indirectly; published equivalent observations may exist outside the inspected literature. The independent mathematical audit has not been performed; the numerical checker covers finite examples only.

## References
1. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first posted 2026-10-15), especially Remark 23 and Conjecture 2. https://arxiv.org/abs/2610.22248
2. U. Dempwolff, J. C. Fisher, and A. Herman, *Semilinear transformations over finite fields are Frobenius maps*, Glasgow Mathematical Journal 42 (2000), 289–295. https://doi.org/10.1017/S0017089500020164
3. Y. Wei and Y. M. Zou, *Isomorphism classes of idempotent evolution algebras*, Linear Algebra and its Applications (2023), arXiv:2310.12368. https://arxiv.org/abs/2310.12368
