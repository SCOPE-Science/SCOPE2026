# Exact exponent transition for complex Hilbert joint numerical indices

## Finding

Let \(H\) be a complex Hilbert space, let \(k\ge1\) be an integer, and assume \(\dim H\ge k+1\). For \(1\le p<\infty\), define the \(p\)-joint operator norm and numerical radius of \(\mathbf T=(T_1,\ldots,T_k)\in\mathcal B(H)^k\) by
\[
 \|\mathbf T\|_p=\sup_{\|x\|=1}\left(\sum_{j=1}^k\|T_jx\|^p\right)^{1/p},\qquad
 w_p(\mathbf T)=\sup_{\|x\|=1}\left(\sum_{j=1}^k|\langle T_jx,x\rangle|^p\right)^{1/p}.
\]
With \(n_{(p,k)}(H)=\inf_{\|\mathbf T\|_p=1}w_p(\mathbf T)\), the exact constant is
\[
 \boxed{n_{(p,k)}(H)=\frac{1}{2k^{1/\max\{p,2\}}}=\begin{cases}
 (2\sqrt{k})^{-1},&1\le p\le2,\\
 (2k^{1/p})^{-1},&2\le p<\infty.
 \end{cases}}
\]
The same explicit tuple of commuting rank-one square-zero operators is optimal for every exponent. In that tuple, a maximizing vector has equal magnitudes in all output coordinates for \(p<2\), while one output coordinate suffices for \(p>2\). In particular, the optimal index is constant over the entire range \(1\le p\le2\), despite the change in the underlying joint norms.

## Assumptions and scope

All operators are bounded and complex linear. The dimension may be finite or infinite but is at least \(k+1\). The exponent is finite and at least one. No conclusion is claimed for smaller dimension or for general Banach spaces or real Hilbert spaces. The convention for the Hilbert inner product is linear in its first argument. The index takes the infimum over **all** operator tuples, not just the witness class.

## Proof

**1. Scalar numerical-radius estimate.** For any \(S\in\mathcal B(H)\), its numerical radius \(w(S)=\sup_{\|x\|=1}|\langle Sx,x\rangle|\) satisfies \(\|S\|\le2w(S)\). To see this without a nonstandard lemma, for unit vectors \(x,y\), polarization gives
\[
 4\langle Sx,y\rangle=\sum_{r=0}^{3}i^r\langle S(x+i^r y),x+i^r y\rangle.
\]
The sum of the four squared norms on the right is \(8\), so \(|\langle Sx,y\rangle|\le2w(S)\); take suprema.

**2. Sharp lower bound for \(1\le p\le2\).** Let \(q\) denote the conjugate exponent, with \(q=\infty\) when \(p=1\). For every sign vector \(\varepsilon\in\{-1,1\}^k\), coefficient \(\ell_p\)-\(\ell_q\) duality, followed by step 1, yields
\[
 w_p(\mathbf T)\ge k^{-1/q}w\!\left(\sum_j\varepsilon_jT_j\right)
 \ge\frac{k^{-1/q}}2\left\|\sum_j\varepsilon_jT_j\right\|.
\]
For any unit \(x\), exact averaging over all \(2^k\) sign vectors annihilates mixed terms:
\[
 2^{-k}\sum_{\varepsilon\in\{-1,1\}^k}
 \left\|\sum_j\varepsilon_jT_jx\right\|^2
 =\sum_j\|T_jx\|^2.
\]
Hence the largest signed-combination norm is at least \(\|\mathbf T\|_2\). It follows that
\[
 w_p(\mathbf T)\ge\tfrac12 k^{-1/q}\|\mathbf T\|_2.
\]
The elementary \(k\)-coordinate comparison \(\|\mathbf T\|_p\le k^{1/p-1/2}\|\mathbf T\|_2\) now gives
\[
 w_p(\mathbf T)\ge\tfrac12 k^{-(1-1/p)}k^{-(1/p-1/2)}\|\mathbf T\|_p
 =\frac{\|\mathbf T\|_p}{2\sqrt{k}}.
\]
This includes \(p=1\), since the coefficient vector of signs has \(\ell_\infty\) norm one.

**3. Sharp lower bound for \(2\le p<\infty\).** Write \(M=\max_j\|T_j\|\). Then \(\|\mathbf T\|_p\le k^{1/p}M\) and \(w_p(\mathbf T)\ge\max_j w(T_j)\ge M/2\). Therefore
\[
 w_p(\mathbf T)\ge\frac{\|\mathbf T\|_p}{2k^{1/p}}.
\]

**4. One sharp family for all exponents.** Choose orthonormal vectors \(e_0,e_1,\ldots,e_k\), and define \(T_jx=\langle x,e_0\rangle e_j\). They obey \(T_iT_j=0\), and
\[
 \|\mathbf T\|_p=k^{1/p}.
\]
Writing any unit vector as \(x=a e_0+\sum_{j=1}^k b_je_j+y\) with \(y\) perpendicular to this \((k+1)\)-dimensional span, we have
\[
 \left(\sum_j|\langle T_jx,x\rangle|^p\right)^{1/p}=|a|\|b\|_{\ell_p^k},\qquad |a|^2+\|b\|_2^2\le1.
\]
The sharp comparison \(\|b\|_{\ell_p^k}\le k^{\max\{1/p-1/2,0\}}\|b\|_2\) and \(|a|\|b\|_2\le1/2\) give
\[
 w_p(\mathbf T)=\tfrac12k^{\max\{1/p-1/2,0\}}.
\]
For \(p<2\), attain equality with \(|a|=1/\sqrt2\) and \(|b_j|=1/\sqrt{2k}\) for all \(j\). For \(p>2\), take \(|a|=|b_1|=1/\sqrt2\) and all other \(b_j=0\); at \(p=2\), every \(b\) of Euclidean norm \(1/\sqrt2\) works. Dividing by \(\|\mathbf T\|_p\) attains each lower bound above. This proves the statement, including \(k=1\).

## Verification

The identity underlying the low-exponent estimate is a finite sign-orthogonality identity, not a probabilistic approximation. The exact extremizing tuple is described for every admissible dimension, exponent, and tuple length. Run `python3 verify.py` to check algebraic exponent identities, exact signed-combination second moments on deterministic integral complex vectors, polarization identities, and numerical stress tests of the explicit maximizers. Finite tests support but do not replace the preceding unrestricted analytic proof.

## Relationship to prior work

Mal's 2022 preprint (2023 journal Theorem 3.11) establishes the Euclidean case \(p=2\) for \(k<\dim H\), and the case \(p>2\) for two operators. Those are recovered here, not attributed as new. Mal's general lower bound \(n_{(p,k)}(X)\ge n(X)k^{-1/p}\) is sharp here for \(p\ge2\), but is strictly weaker for \(p<2\) and \(k>1\). The essential new portion is the low-exponent plateau together with the all-tuple-length phase diagram and its sharp witnesses.

Moslehian, Sattari, and Shebrawi give foundational \(p\)-joint radius bounds, including a signed-combination Hölder estimate (2017, Theorem 3.1). The new sharp lower bound combines that familiar estimate with an exact sign-second-moment argument and a dimension-independent norm comparison. Their stated results do not give the sharp low-exponent index or its attaining family. Other results for restricted common-source tuples concern \(p=2\) and do not establish this unrestricted exponent law.

## Limitations

The dimension hypothesis ensures the existence of \(k\) orthogonal outputs perpendicular to one common source. The exact index when \(\dim H\le k\) is not determined here. No equality classification is claimed for arbitrary minimizing tuples; only the exhibited witness is analyzed. Potentially equivalent inequalities in literature not indexed by joint numerical-index terminology remain a bibliographic risk. Independent scientific validation has not been performed.

## References

1. A. Mal, *On joint numerical radius of operators and joint numerical index of a Banach space*, arXiv:2212.06500v1, first public 2022-12-13; *Operators and Matrices* 17 (2023), 839–856, DOI:10.7153/oam-2023-17-56, especially Theorems 3.1 and 3.11. https://arxiv.org/abs/2212.06500 and https://files.ele-math.com/articles/oam-17-56.pdf.
2. M. S. Moslehian, M. Sattari and K. Shebrawi, *Extensions of Euclidean operator radius inequalities*, *Mathematica Scandinavica* 120 (2017), 129–144, DOI:10.7146/math.scand.a-25509, particularly Proposition 2.4 and Theorem 3.1. https://journals.msp.org/mscand/article/download/328/327/359.
3. R. Drnovšek and V. Müller, *On joint numerical radius II*, *Linear and Multilinear Algebra* 62 (2014), 1197–1204, DOI:10.1080/03081087.2013.816303. Identified through Mal's proof and bibliographic metadata; full text not inspected.
4. E. O. Çevik and P. Bhunia, *Joint numerical radius for n-tuples of operators*, *The Journal of Analysis* (2026), DOI:10.1007/s41478-026-01118-5. Available abstract covers monotonicity and operator-radius inequalities; the full text was not inspected.
