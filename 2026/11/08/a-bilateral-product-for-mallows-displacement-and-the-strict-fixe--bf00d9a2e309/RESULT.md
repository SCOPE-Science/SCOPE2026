# A bilateral product for Mallows displacement and the strict fixed-point parity bias

## Finding

Fix \(Q>1\), put \(q=Q^{-1}\in(0,1)\), and let \(\Sigma\) be the balanced two-sided Mallows permutation of \(\mathbb Z\) with parameter \(q\). Write \(D=\Sigma(0)\). Its bilateral probability generating function admits the product evaluation

\[
\mathbb E[z^D]=\frac{(q;q)_\infty^2}{(qz;q)_\infty(q/z;q)_\infty},\qquad q<|z|<q^{-1}.
\]

Equivalently, if \(G_j^+,G_j^-\), for \(j\ge1\), are mutually independent geometric random variables on \(\{0,1,2,\ldots\}\) with \(\Pr(G_j^\pm=k)=(1-q^j)q^{jk}\), then

\[
D\ \overset{\mathrm d}=\ \sum_{j\ge1}(G_j^+-G_j^-),
\]

where both sums are almost surely finite.

Let \(c_o(Q)\) and \(c_e(Q)\) denote the limiting expected numbers of fixed points in Mallows permutations of odd and even orders, respectively, as defined by He, Müller and Verstraaten. Their identification with \(\Pr(D\text{ even})\) and \(\Pr(D\text{ odd})\), respectively, is known. The new product evaluation gives

\[
\boxed{\ c_o(Q)-c_e(Q)=\prod_{j=1}^{\infty}\left(\frac{1-Q^{-j}}{1+Q^{-j}}\right)^2>0\ },
\qquad
c_o(Q)=\frac{1+\Delta(Q)}2,\quad c_e(Q)=\frac{1-\Delta(Q)}2,
\]

where \(\Delta(Q)\) denotes the displayed product. Consequently, for *every* \(Q>1\),

\[
 c_o(Q)>\frac12>c_e(Q),
\]

and \(c_o\) is strictly increasing, while \(c_e\) is strictly decreasing, on the whole interval \((1,\infty)\). These two inequalities and strict monotonicity settle the specific questions posed in Section 10 of He, Müller and Verstraaten's paper.

## Assumptions and scope

The model is the translation-invariant, balanced two-sided infinite Mallows measure with \(0<q<1\), in the convention that a permutation has weight proportional to \(q^{\operatorname{inv}}\). The finite-permutation parameter is its reciprocal \(Q>1\). The definitions of \(c_o(Q),c_e(Q)\) and their identification with displacement parity are imported from Theorem 1.6 in the cited 2022 preprint/2023 article; the proof below does not independently reprove convergence of finite cycle counts.

The shifted factorial is \((a;q)_n=\prod_{j=0}^{n-1}(1-aq^j)\), with \((a;q)_0=1\), and \((a;q)_\infty=\prod_{j=0}^\infty(1-aq^j)\). For fixed \(0<q<1\), \((q;q)_\infty>0\). The complex variable \(z\) is nonzero and satisfies \(q<|z|<1/q\). The parity statement requires the particular value \(z=-1\), which lies in this annulus.

## Proof

**1. Exact displacement input and absolute convergence.** Theorem 5.1 of Gnedin and Olshanski gives, for every integer \(d\),

\[
\Pr(D=d)=(1-q)(q;q)_\infty\!\sum_{\substack{r,\ell\ge0\\r-\ell=d}}
\frac{q^{r\ell+r+\ell}}{(q;q)_r(q;q)_\ell}.
\tag{1}
\]

This identity is taken as previously established literature, not as a new result. For \(q<|z|<q^{-1}\), the double series weighted by \(z^{r-\ell}\) is absolutely summable: \((q;q)_r,(q;q)_\ell\ge(q;q)_\infty>0\), and \(q^{r\ell}\le1\), so its absolute value is dominated by a constant times

\[
\sum_{r,\ell\ge0}(q|z|)^r(q/|z|)^\ell<\infty.
\]

Thus rearrangement is legitimate.

**2. Elementary product-series identity.** For \(|t|<1\),

\[
\sum_{n=0}^{\infty}\frac{(a;q)_n}{(q;q)_n}t^n
=\frac{(at;q)_\infty}{(t;q)_\infty}.
\tag{2}
\]

For completeness, put \(H(t)=(at;q)_\infty/(t;q)_\infty\). It is analytic at \(t=0\), satisfies \((1-t)H(t)=(1-at)H(qt)\), and has \(H(0)=1\). Comparing coefficients, \((1-q^n)[t^n]H=(1-aq^{n-1})[t^{n-1}]H\), proving (2) by induction. Taking \(a=0\) yields \(\sum_{n\ge0}t^n/(q;q)_n=1/(t;q)_\infty\).

**3. Sum the known law.** Multiply (1) by \(z^d\) and sum over \(d\). First sum over \(r\), then apply (2) with \(a=qz\) and \(t=q/z\):

\[
\begin{aligned}
\mathbb E[z^D]
&=(1-q)(q;q)_\infty
\sum_{\ell\ge0}\frac{(q/z)^\ell}{(q;q)_\ell}
\sum_{r\ge0}\frac{(zq^{\ell+1})^r}{(q;q)_r}\\
&=\frac{(1-q)(q;q)_\infty}{(zq;q)_\infty}
\sum_{\ell\ge0}\frac{(zq;q)_\ell}{(q;q)_\ell}(q/z)^\ell\\
&=\frac{(1-q)(q;q)_\infty}{(zq;q)_\infty}
\frac{(q^2;q)_\infty}{(q/z;q)_\infty}\\
&=\frac{(q;q)_\infty^2}{(zq;q)_\infty(q/z;q)_\infty}.
\end{aligned}
\tag{3}
\]

Here \((1-q)(q^2;q)_\infty=(q;q)_\infty\). This proves the claimed bilateral product on the full annulus.

**4. Independent-geometric representation.** Each geometric variable has generating function \((1-q^j)/(1-q^jz)\). Because

\[
\sum_{j\ge1}\mathbb E[G_j^++G_j^-]
=2\sum_{j\ge1}\frac{q^j}{1-q^j}<\infty,
\]

both nonnegative random sums are finite almost surely. Their difference has generating function equal to the right-hand side of (3). Equality of its Laurent coefficients on the annulus (or uniqueness of characteristic functions on the unit circle) proves the distributional identity.

**5. Parity and strict parameter dependence.** Substitution \(z=-1\) in (3) gives

\[
\mathbb E[(-1)^D]
=\left(\frac{(q;q)_\infty}{(-q;q)_\infty}\right)^2
=\prod_{j=1}^\infty\left(\frac{1-q^j}{1+q^j}\right)^2
=:\delta(q).
\tag{4}
\]

Since \(\sum_j q^j<\infty\), this convergent product is strictly positive; every factor is smaller than one, so \(0<\delta(q)<1\). For each fixed \(j\ge1\), \((1-q^j)/(1+q^j)\) is strictly decreasing in \(q\in(0,1)\). Comparing the first factor and using monotonicity of all remaining positive factors gives that the *infinite* product is strictly decreasing in \(q\). Since \(q=Q^{-1}\) decreases when \(Q\) increases, \(\Delta(Q)=\delta(Q^{-1})\) is strictly increasing for \(Q>1\). Finally,

\[
\Pr(D\text{ even})-\Pr(D\text{ odd})=\mathbb E[(-1)^D]=\Delta(Q),
\quad
\Pr(D\text{ even})+\Pr(D\text{ odd})=1.
\]

The known identifications of these probabilities with \(c_o,c_e\) complete the proof. The endpoint limits \(\Delta(Q)\to0\) as \(Q\downarrow1\) and \(\Delta(Q)\to1\) as \(Q\to\infty\) agree with the previously known limiting behavior.

## Verification

The accompanying standalone script `verify.py` uses only the Python standard library and rational arithmetic. It sums the exact earlier displacement weights over finite index rectangles at four rational values of \(q\), computes a finite partial product, and checks their agreement inside explicit omitted-mass, normalization, and product-tail bounds. Its checks passed on the packaged code. They are finite diagnostics only; (1)–(4) and their stated convergence supply the proof for all real parameters.

## Relationship to prior work

Gnedin and Olshanski [1, Theorem 5.1] proved the *complete displacement probability mass function* (1), including its q-hypergeometric/q-Bessel representation. The present result starts from that exact formula, rather than claiming a new displacement distribution. What is added is its bilateral generating-function factorization (3), the independent-geometric decomposition, and especially the positive Euler product (4) with strict monotonicity.

He, Müller and Verstraaten [2, Theorem 1.6] had already identified the limiting odd/even fixed-point expectations with displacement parity and established their endpoint limits. In [2, Section 10], the authors explicitly left the inequalities \(c_o(Q)>1/2>c_e(Q)\) and strict monotonicity open. These assertions do not appear in the inspected primary sources. The 2023/2025 logical-limit-law study [3] cites the cycle limit laws but addresses properties in logical languages, not this evaluated parity bias. Formula (2) is the classical q-binomial theorem; its use to sum the existing distribution is the substantive algebraic reduction, not a claimed new q-series theorem.

## Limitations

The conclusion is for fixed \(Q>1\) and for the specific balanced two-sided infinite Mallows law; the finite-size convergence statements on which the constants depend remain those of [2]. It does not treat fixed-point variance or higher-cycle constants, and it does not prove the separate monotonicity questions about \(m_1\) and \(\mu_2\) in [2]. The underlying probability law predates this work, and completeness of historical priority beyond the inspected literature requires independent review. An accessible abstract, but not a full relevant chapter, was obtained for Verstraaten's 2023 dissertation; the same authors' published research article was inspected in full for the closest stated question.

## References

[1] A. Gnedin and G. Olshanski, *The two-sided infinite extension of the Mallows model for random permutations*, arXiv:1103.1498, 2011 (published *Advances in Applied Mathematics* 48, 2012), Theorem 5.1, https://arxiv.org/abs/1103.1498.

[2] J. He, T. Müller, and T. W. Verstraaten, *Cycles in Mallows random permutations*, first publicly posted 2022-01-27, arXiv:2201.11610; published *Random Structures & Algorithms* 63 (2023), Theorem 1.6 and Section 10, https://arxiv.org/abs/2201.11610; https://doi.org/10.1002/rsa.21169.

[3] T. Müller, F. Skerman, and T. W. Verstraaten, *Logical limit laws for Mallows random permutations*, arXiv:2302.10148, https://arxiv.org/abs/2302.10148.
