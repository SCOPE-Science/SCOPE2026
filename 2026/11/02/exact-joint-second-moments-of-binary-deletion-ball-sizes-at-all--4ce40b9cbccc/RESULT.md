# Exact joint second moments of binary deletion-ball sizes at all radii

## Finding

Let \(X_n\) be a uniformly random binary word of length \(n\), and let \(B_d(x)\) be the number of **distinct** length-\(n-d\) subsequences obtainable by exactly \(d\) deletions. Define the deletion enumerator
\[
P_x(z)=\sum_{d=0}^{n} B_d(x)z^d.
\]
The complete all-length, all-pairs second-moment generating function is
\[
\boxed{\sum_{n\ge0}u^n\,\mathbb E\bigl[P_{X_n}(z)P_{X_n}(w)\bigr]
=\frac{(2-uzw)R(u,z,w)}{(1-uzw)(2-uzw-2uw)(2-uzw-2uz)S(u,z,w)},}
\]
where
\[
\begin{aligned}
R(u,z,w)={}&8-4u(z+w)-8uzw+4u^2zw(z+w)\\
 &+2u^2z^2w^2-u^3z^2w^2(z+w+4),\\
S(u,z,w)={}&4-4u-2u(z+w)-2uzw+u^2zw(z+w).
\end{aligned}
\]
The coefficient of \(u^nz^dw^e\) is exactly \(\mathbb E[B_d(X_n)B_e(X_n)]\) for every \(n\ge0\) and all \(0\le d,e\le n\); no asymptotic or fixed-radius restriction is needed.

Two natural consequences illustrate the information this identity contains. For every \(n\ge3\),
\[
\boxed{\mathbb E B_3(X_n)=\frac{(n+1)(n^2-n+6)}{48},\qquad
\operatorname{Var}(B_3(X_n))=\frac{(n-3)(n-2)(3n^3-12n^2-13n+94)}{768}.}
\]
In particular, its standard deviation is asymptotic to \(n^{5/2}/16\) while its mean is asymptotic to \(n^3/48\).

Writing \(T_n=\sum_{d=0}^{n}B_d(X_n)\) for the number of distinct subsequences of all lengths, **including the empty word**, yields
\[
\boxed{\sum_{n\ge0}u^n\mathbb E T_n^2=
\frac{(2-u)(u^2-u+2)}{(1-u)(2-3u)(u^2-5u+2)}.}
\]
Consequently, with \(\rho=(5+\sqrt{17})/4\),
\[
\boxed{\operatorname{Var}(T_n)\sim\left(2+\frac8{\sqrt{17}}\right)\rho^n.}
\]
In contrast, the known mean is \(\mathbb E T_n=2(3/2)^n-1\). Thus the squared coefficient of variation grows exponentially, with exponential base \((5+\sqrt{17})/9>1\).

## Assumptions and scope

Words are finite binary strings with independent fair bits. Deleting exactly \(d\) positions leaves a word of length \(n-d\), and repeated outputs are counted once. We set \(B_d(x)=0\) outside \(0\le d\le n\); in particular \(B_0(x)=B_n(x)=1\). The empty input word is included at \(n=0\). All generating-function identities are formal power series over \(\mathbb Q[z,w][[u]]\), so no analytic convergence assumption is required for coefficient extraction.

## Proof

**Canonical deletion masks.** For a fixed target subsequence, use its *leftmost* embedding in the original word, taking the earliest admissible input position for each target symbol. Scan the source from right to left, maintaining the symbol of the nearest position retained to the right; denote the absence of a retained symbol by \(\bot\). A retained symbol \(b\) replaces the state with \(b\). A deleted symbol \(b\) leaves the state unchanged and is permitted precisely when the state is \(\bot\) or is different from \(b\). Indeed, if the next retained symbol to the right were equal to \(b\), replacing that later retained occurrence by this earlier occurrence would contradict leftmost embedding. Conversely, the absence of any such replacement at each deleted position proves leftmost embedding by a right-to-left exchange argument. Hence exactly one permitted mask represents every distinct subsequence, with each deletion marked by \(z\).

**Transfer matrices.** Index three states by \((\bot,0,1)\). Let \(H_b\) be the \(3\times3\) matrix with a \(1\) in row \(b\) of every column and zeros elsewhere. Let \(D_b\) be diagonal with entry \(1\) at state \(\bot\) and at the symbol different from \(b\), and \(0\) at state \(b\). Put \(M_b(z)=H_b+zD_b\). With \(e_{\bot}\) the initial-state vector and \(\mathbf1\) the vector of ones, the canonical-mask bijection gives
\[
P_{x_1\cdots x_n}(z)=\mathbf1^\mathsf{T}M_{x_1}(z)\cdots M_{x_n}(z)e_{\bot}.
\]
For independently fair bits, form the \(9\times9\) pair transfer
\[
K(z,w)=\tfrac12\sum_{b=0}^{1}M_b(z)\otimes M_b(w).
\]
Writing \(e=e_{\bot}\otimes e_{\bot}\), we obtain the exact resolvent expression
\[
\sum_{n\ge0}u^n\mathbb E[P_{X_n}(z)P_{X_n}(w)]
=(\mathbf1\otimes\mathbf1)^\mathsf{T}(I-uK(z,w))^{-1}e.
\]
It remains to establish that this rational resolvent equals the displayed fully factored form.

**Exact polynomial certificate.** Call the displayed numerator \(N(u,z,w)=(2-uzw)R\) and the displayed denominator \(Q(u,z,w)=(1-uzw)(2-uzw-2uw)(2-uzw-2uz)S\). They have \(u\)-degree at most \(4\) and \(5\), respectively, with nonzero constant coefficient \(16\). By Cramer's rule, the resolvent equals \(A(u,z,w)/D(u,z,w)\), where \(A=(\mathbf1\otimes\mathbf1)^\mathsf T\operatorname{adj}(I-uK)e\) has \(u\)-degree at most \(8\), and \(D=\det(I-uK)\) has \(u\)-degree at most \(9\) and constant term \(1\). Thus the polynomial \(QA-ND\) has \(u\)-degree at most \(13\). The standalone exact-rational verifier `verify_joint_moments.py` computes all coefficients of \(u^n z^d w^e\) of \(Q\sum_{j\ge0}u^j(\mathbf1\otimes\mathbf1)^\mathsf T K^j e-N\) through \(n=13\), using a sparse symbolic polynomial representation. All vanish exactly. Since \(D\) is invertible as a formal series and \(QA-ND\) is a polynomial of degree at most \(13\), all its coefficients vanish. This certifies the claimed **infinite** generating-function identity, not just a finite experimental fit.

**Corollaries.** Extracting the coefficient of \(z^3w^3\) yields
\[
\sum_{n\ge0}u^n\mathbb E[B_3(X_n)^2]
=\frac{u^3(16-54u+112u^2-117u^3+68u^4-24u^5+4u^6)}{16(1-u)^7}.
\]
Extracting one marginal gives \(\sum_{n\ge0}u^n\mathbb E B_3(X_n)=u^3(8-17u+14u^2-4u^3)/(8(1-u)^4)\). Taking coefficients of these two rational expressions and subtracting the squared mean gives the displayed variance formula for every \(n\ge3\); `verify_variance3.py` checks the exact polynomial identities, not only selected numerical cases. Setting \(z=w=1\) yields the total-subsequence generating function. Its unique smallest-modulus pole is \(r=(5-\sqrt{17})/2\), with multiplicative coefficient \(2+8/\sqrt{17}\), and \(1/r=(5+\sqrt{17})/4>9/4\). The remaining poles contribute strictly smaller exponential terms; subtraction of \((2(3/2)^n-1)^2\) leaves the stated variance asymptotic.

## Verification

The package includes independent executable source files `verify_joint_moments.py` and `verify_variance3.py`, requiring only Python's standard library. The first performs an exact rational symbolic degree-13 certificate for all powers and all pairs of deletion radii and independently compares the canonical mask algorithm against **all** ordinary deletion-mask outputs for every binary word through length \(8\). The second checks the separately derived exact three-deletion rational moment expressions and independently enumerates all binary words through length \(13\), with direct deletion-mask checks through length \(11\). The captured successful outputs are included in `verification_output.txt`. These bounded direct enumerations supplement, but do not replace, the formal-series proof.

## Relationship to prior work

Collins (2013) evaluates the mean count of distinct subsequences, including \(\mathbb E T_n=2(3/2)^n-1\). Biers-Ariel, Godbole and Kelley (2017/2018) treat expectations for biased or dependent random sources. Li, Wang and Fu (first public January 10, 2026) give deterministic deletion-ball bounds and run-structure extremizers. Liron and Langberg (2012) give further deterministic run-constrained bounds. The 2008 study of Mercier, Khabbazian and Bhargava provides formulas for single-word deletion-ball sizes at fixed small radii; a complete accessible full text was not available for comparison. The present claim is different: an all-radius bivariate moment enumerator simultaneously fixing the covariance of arbitrary deletion-ball sizes, together with explicit three-deletion variance and total-count second-moment consequences. Neither mean-only results nor individual fixed-word size formulas by themselves imply this evaluated second-moment identity.

## Limitations

This theorem is restricted to uniformly random binary source words. It does not establish corresponding rational formulas for biased or larger-alphabet sources, nor a limiting probability distribution for the normalized number of subsequences. The arithmetic and symbolic certificates verify the stated identities. Publication priority is subject to the possibility of an unindexed equivalent result, particularly because the full 2008 paper by Mercier and collaborators was not accessible; its abstract and its characterization in subsequent primary work were examined.

## References

1. Han Li, Xiang Wang, Fang-Wei Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493, first submitted January 10, 2026. https://arxiv.org/html/2601.06493v2
2. Michael J. Collins, *The Number of Distinct Subsequences of a Random Binary String*, arXiv:1310.7288, October 28, 2013. https://arxiv.org/abs/1310.7288
3. Liron and Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644, February 2012. https://arxiv.org/abs/1202.1644
4. Yonah Biers-Ariel, Anant Godbole, Elizabeth Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661; *Discrete Mathematics & Theoretical Computer Science* 19:2 (2018). https://arxiv.org/abs/1704.08661
5. H. Mercier, M. Khabbazian, V. K. Bhargava, *On the Number of Subsequences When Deleting Symbols From a String*, *IEEE Transactions on Information Theory* (2008), doi:10.1109/TIT.2008.924730. https://doi.org/10.1109/TIT.2008.924730
