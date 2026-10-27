# A compact quasinilpotent weighted shift with no two-step rank-one commuting chain

## Finding

For any unilateral weighted shift \(T\) on \(\ell_2(\mathbb N_0;\mathbb C)\) with \(Te_n=w_ne_{n+1}\) and \(w_n\ne0\) for every \(n\), every nonzero bounded operator commuting with \(T\) is injective; hence a non-scalar operator commuting with \(T\) has no eigenvalues and cannot commute with a nonzero rank-one operator. In particular, the compact quasinilpotent shift \(Ke_n=\frac{1}{n+1}e_{n+1}\) admits no chain \(K\leftrightarrow S\leftrightarrow F\) with non-scalar \(S\) and rank-one \(F\), giving a negative answer to the universal existence question in Problem 4.5 of arXiv:2507.14297v2.

## Assumptions and scope

Work on the complex Hilbert space \(\ell_2(\mathbb N_0;\mathbb C)\) with standard basis \((e_n)_{n\ge0}\). All operators are bounded and complex-linear. A chain \(K\leftrightarrow S\leftrightarrow F\) means \(KS=SK\) and \(SF=FS\), with \(S\) non-scalar and \(F\) a nonzero rank-one operator. The result rules out this two-link chain for the specified compact quasinilpotent shift; it does not classify all compact quasinilpotent operators.

## Proof

Define \(K e_n=(n+1)^{-1}e_{n+1}\). For each \(N\ge1\), let \(K_N e_n=(n+1)^{-1}e_{n+1}\) for \(n<N\), and \(K_Ne_n=0\) for \(n\ge N\). Then \(K_N\) has finite rank and
\[
\|K-K_N\|=\sup_{n\ge N}\frac{1}{n+1}=\frac{1}{N+1}\longrightarrow0,
\]
so \(K\) is compact. For every integer \(m\ge1\),
\[
K^m e_n=\frac{1}{(n+1)(n+2)\cdots(n+m)}e_{n+m},
\qquad
\|K^m\|=\frac1{m!}.
\]
The spectral-radius formula gives \(r(K)=\lim_{m\to\infty}\|K^m\|^{1/m}=0\), so \(K\) is quasinilpotent and nonzero.

We prove the commutant lemma for any bounded unilateral weighted shift \(T e_n=w_ne_{n+1}\) with all \(w_n\ne0\). Let \(A\) commute with \(T\), and write \(Ae_0=\sum_{j\ge0}a_je_j\). If \(Ae_0=0\), then \(e_n=(\prod_{j=0}^{n-1}w_j)^{-1}T^ne_0\) implies \(Ae_n=0\) for every \(n\), hence \(A=0\). Otherwise let \(m=\min\{j:a_j\ne0\}\). Put \(\beta_n=\prod_{j=0}^{n-1}w_j\), with \(\beta_0=1\). Commutation yields
\[
Ae_n=\beta_n^{-1}T^nAe_0.
\]
The first nonzero coordinate of \(Ae_n\) is at \(e_{n+m}\), with coefficient
\[
a_m\frac{\prod_{j=m}^{m+n-1}w_j}{\prod_{j=0}^{n-1}w_j}\ne0.
\]
If \(x\ne0\) has first nonzero coordinate \(x_n\), then the \(e_{n+m}\)-coordinate of \(Ax\) is \(x_n\) times this nonzero coefficient: every \(Ae_j\) with \(j>n\) has zero coordinates through \(e_{n+m}\). Thus \(Ax\ne0\). Every nonzero operator commuting with \(T\) is injective.

Now suppose a non-scalar \(S\) commuting with \(K\) had an eigenvalue \(\lambda\). The nonzero operator \(S-\lambda I\) would also commute with \(K\), but would have a nontrivial kernel, contradicting the commutant lemma. Hence \(S\) has no eigenvalues. If a nonzero rank-one operator is written \(F=x\otimes f\), where \(x\ne0\) and \(f\ne0\), the relation \(SF=FS\) gives
\[
f(y)Sx=f(Sy)x\qquad\text{for every }y.
\]
Choosing \(y\) with \(f(y)\ne0\) shows that \(Sx\) is a scalar multiple of \(x\), so \(S\) has an eigenvalue. This contradiction proves that no such chain \(K\leftrightarrow S\leftrightarrow F\) exists.

## Verification

The finite-rank approximation and power-norm formulas above are exact. The infinite-dimensional conclusion follows from the first-nonzero-coordinate argument, not from finite numerical tests. The proof uses no unverified external lemma. The conclusion concerns a rank-one terminal operator and one non-scalar intermediate operator only.

## Relationship to prior work

The paper cited in [1] explicitly poses the universal chain question as Problem 4.5 and gives a positive example for the Volterra operator in Example 4.4, using a nilpotent convolution operator as the intermediate link. The weighted shift here is a different compact quasinilpotent operator, and the commutant argument rules out every non-scalar intermediate, not only nilpotent ones. This counterexample refutes universal existence without contradicting the Volterra example.

## Limitations

This is a counterexample to a universal existence assertion, not a classification of all compact quasinilpotent operators. It does not rule out longer commuting chains from this shift to a rank-one operator, nor chains ending at compact operators of higher rank. The argument addresses only the stated two-link chain and makes no assertion about longer chains.

## References

[1] Tomasz Szczepanski, “On the chain of commuting operators on Banach spaces,” arXiv:2507.14297v2; published version, DOI:10.1112/blms.70471. See Problem 4.5 and Example 4.4.

[2] Marc P. Thomas, “Quasinilpotent Strictly Cyclic Unilateral Weighted Shift Operators on \(\ell^p\) which are not Unicellular,” *Proceedings of the London Mathematical Society* 51 (1985), 127–145. DOI:10.1112/plms/s3-51.1.127.
