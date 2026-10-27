# Defect-pair Gibbs law for regular finite-field subspace-preserving endomorphisms

## Finding
Let \(q\) be any prime power. For positive integers \(a,b\), let \(P_{a,b}(q)\) denote the multiplicative monoid of all linear endomorphisms of \(\mathbb F_q^{a+b}\) preserving a specified \(a\)-dimensional subspace. Relative to a basis extending that subspace, every element is uniquely
\[
T=\begin{pmatrix}A&B\\0&D\end{pmatrix},\qquad
A\in M_a(\mathbb F_q),\quad B\in M_{a\times b}(\mathbb F_q),\quad D\in M_b(\mathbb F_q).
\]
Write \(I=a-\operatorname{rank}(A)\) and \(J=b-\operatorname{rank}(D)\). Call \(T\) regular when \(TST=T\) for some \(S\in P_{a,b}(q)\).

Define \(\Phi_k(q)=\prod_{h=1}^{k}(1-q^{-h})\), with \(\Phi_0(q)=1\), and
\[
p_{q,n}(k)=\frac{q^{-k^2}\Phi_n(q)^2}{\Phi_k(q)^2\Phi_{n-k}(q)}\quad(0\le k\le n),
\]
with value zero outside this range. Then the complete finite joint defect/regularity spectrum is
\[
\boxed{\Pr\{I=i,J=j,T\text{ regular}\}=p_{q,a}(i)p_{q,b}(j)q^{-ij}.}
\]
In particular the number of regular elements in the defect stratum \((i,j)\) is
\[
\boxed{N_q(a,a-i)N_q(b,b-j)q^{ab-ij},}
\]
where \(N_q(n,r)=\prod_{h=0}^{r-1}(q^n-q^h)^2/\prod_{h=0}^{r-1}(q^r-q^h)\) counts rank-\(r\) square matrices.

For fixed \(q\), put \(\Phi_\infty(q)=\prod_{h\ge1}(1-q^{-h})>0\), \(\pi_q(k)=q^{-k^2}\Phi_\infty(q)/\Phi_k(q)^2\), and
\[
L_q=\sum_{i,j\ge0}\pi_q(i)\pi_q(j)q^{-ij}.
\]
As \(a,b\to\infty\), with no restriction on their relative growth,
\[
\Pr\{T\text{ regular}\}=L_q+O_q(q^{-a}+q^{-b}),
\]
and the conditional law of \((I,J)\) given regularity converges in total variation, with the same rate, to the strictly positive probability measure
\[
\boxed{\mu_q(i,j)=L_q^{-1}\pi_q(i)\pi_q(j)q^{-ij},\quad i,j\ge0.}
\]
Every finite conditional distribution and the limit satisfy negative association of the two coordinates: for nondecreasing real functions \(f,g\) with the relevant finite expectations,
\[\operatorname{Cov}(f(I),g(J)\mid T\text{ regular})\le0.\]
For nonconstant nondecreasing functions on the coordinate supports, the inequality is strict. The asymptotic nonregularity probability is positive, \(1-L_q>0\); for \(q=2\), \(L_2=0.699851322305535\ldots\).

## Assumptions and scope
The result holds over every finite field, including nonprime fields and characteristic two. Dimensions \(a,b\) are positive; the exact formula extends trivially to a zero block dimension. The asymptotic statements require both \(a,b\to\infty\) and fix \(q\). No conclusion is asserted for flags with three or more nontrivial steps or for arbitrary subalgebras of matrix algebras.

## Proof
**Regularity criterion.** The image of \(T\) projects onto \(\operatorname{im}D\) in the quotient by the distinguished subspace \(U\). Thus \(\dim(\operatorname{im}T\cap U)=\operatorname{rank}T-\operatorname{rank}D\). If \(TST=T\) for a map \(S\) preserving \(U\), then the restriction of \(S\) to \(\operatorname{im}T\cap U\) is a right inverse into \(U\), forcing \(\operatorname{im}T\cap U=\operatorname{im}A\). Conversely, when equality holds, choose a right inverse of \(T\) on \(\operatorname{im}T\), sending its intersection with \(U\) into \(U\); extend it to an endomorphism of the ambient space preserving \(U\). This gives \(TST=T\). In block terms, the condition is equivalent to
\[B(\ker D)\subseteq\operatorname{im}A,\]
or equivalently \(\operatorname{rank}T=\operatorname{rank}A+\operatorname{rank}D\). This criterion is already present in the literature; it is not claimed as new.

**Exact counting.** Conditional on fixed \(A,D\) of coranks \(i,j\), the map
\[B\longmapsto(\ker D\xrightarrow{\,B\,}\mathbb F_q^a\twoheadrightarrow\mathbb F_q^a/\operatorname{im}A)\]
is a surjective linear map from an \(ab\)-dimensional coefficient space onto a space of dimension \(ij\). Hence precisely \(q^{ab-ij}\) of the \(q^{ab}\) blocks \(B\) make \(T\) regular. Counting the two independently chosen diagonal blocks by rank gives both boxed exact formulas.

**Limit and rate.** The elementary rank-matrix enumeration gives \(p_{q,n}(k)\) as stated. The infinite products converge because \(\sum_{h\ge1}q^{-h}<\infty\). For \(0\le k\le n\), division by \(\pi_q(k)\) gives \(\Phi_n(q)^2/[\Phi_{n-k}(q)\Phi_\infty(q)]\), whose deviation from one is bounded by \(C_q q^{-(n-k)}\). Also \(\sum_{k\ge0}\pi_q(k)q^k<\infty\), while \(\sum_{k>n}\pi_q(k)=O_q(q^{-n})\). Therefore \(\|p_{q,n}-\pi_q\|_{\mathrm{TV}}=O_q(q^{-n})\). In particular, since each \(p_{q,n}\) sums to one and the difference tends to zero in total variation, \(\sum_{k\ge0}\pi_q(k)=1\). Multiplying two probability laws and weighting by the function \(q^{-ij}\in[0,1]\) cannot increase their unnormalized \(\ell^1\) error. Since the normalization is at least the probability that the first diagonal block is invertible, which is bounded below by \(\Phi_\infty(q)>0\), normalization preserves the claimed rate. Dominated convergence gives the limit \(L_q\). Positivity and nontriviality follow because \(\pi_q(0),\pi_q(1)>0\) and the weight is less than one for \(i,j>0\).

**Negative dependence.** Given regularity and \(I=i\), the conditional weights for \(J=j\) are proportional to \(p_{q,b}(j)q^{-ij}\). For \(i_2>i_1\), the likelihood ratio is a positive constant times \(q^{-(i_2-i_1)j}\), strictly decreasing in \(j\). Thus the conditional expectation of any nondecreasing \(g(J)\) decreases with \(i\). Taking covariance with nondecreasing \(f(I)\) proves the assertion by the elementary rearrangement inequality. Strictness holds when both functions vary on their supports, since each defect stratum has positive mass. Replace \(p_{q,n}\) by \(\pi_q\) for the limit.

## Verification
The standalone Python checker `checks/check_parabolic_regular.py` compares the predicted count **in every defect stratum** with an independent rank test of every block triangular matrix for six small prime-field configurations. In three smaller cases it additionally searches all candidate generalized inverses, verifying \(TST=T\) directly. Its stored deterministic output is `checks/check_output.txt`. The run checks \(6574\) matrices, finds \(5450\) regular matrices, and performs full witness searches for \(163\) matrices. Prime-power extension fields and the infinite limit are proved symbolically, not exhaustively verified computationally.

## Relationship to prior work
Sarkar and Singh's Theorem 4.2 (arXiv:2303.03861, public March 7, 2023) supplies the regular-element image-intersection criterion for subspace-preserving endomorphisms. Fulman and Goldstein's Theorem 1.1 (arXiv:1211.0504) supplies sharp finite-field matrix-nullity convergence rates, including the square-matrix case. Neither examined work gives the parabolic monoid's exact **joint defect/regularity** spectrum, its Gibbs conditional law, or its negative-dependence theorem. The present formula is mathematically derived by combining the known criterion and classical rank counts; priority risk remains for an equivalent result in literature specifically enumerating regular elements of parabolic matrix monoids.

## Limitations
This is not a classification of arbitrary regular representations or of longer flag-preserving matrix monoids. Finite checks do not independently establish all-field identities or asymptotic results; those depend on the displayed proofs. The source review cannot rule out unindexed equivalent enumerations. Independent mathematical audit has not been performed.

## References
1. M. Sarkar and S. N. Singh, *Semigroups of (linear) transformations whose restrictions belong to a given semigroup*, arXiv:2303.03861 (2023), especially Theorem 4.2, https://arxiv.org/abs/2303.03861.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Annals of Probability 43 (2015), 1274–1314, arXiv:1211.0504, https://arxiv.org/abs/1211.0504.
3. N. Sawatraksa and P. Tantong, *Left and Right Regular Elements of Some Subsemigroups of the Linear Transformations Semigroups With Invariant Subspace*, European Journal of Pure and Applied Mathematics 18 (2025), Article 5623, https://doi.org/10.29020/nybg.ejpam.v18i1.5623.
