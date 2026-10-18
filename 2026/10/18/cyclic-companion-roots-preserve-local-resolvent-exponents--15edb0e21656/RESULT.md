# Cyclic companion roots preserve local resolvent exponents

## Finding

Let \(X\) be a nonzero complex Banach space, let \(B\in\mathcal B(X)\) be quasinilpotent, and suppose its resolvent has **uniform superpolynomial logarithmic growth** at zero:
\[
\lim_{\zeta\to0}\frac{\log(1/|\zeta|)}{\log\|(\zeta I-B)^{-1}\|}=0. \tag{U}
\]
For each integer \(m\ge2\), and any \(1\le q\le\infty\), give \(E=X^m\) the finite \(\ell_q\)-sum norm and define the cyclic companion
\[
T(x_0,x_1,\ldots,x_{m-1})=(x_1,\ldots,x_{m-1},Bx_0).
\]
For a quasinilpotent operator \(A\), write
\[
k_A(y)=\limsup_{z\to0}\frac{\log\|(zI-A)^{-1}y\|}{\log\|(zI-A)^{-1}\|}\quad(y\ne0),\qquad
\Lambda(A)=\{k_A(y):y\ne0\}.
\]
Then \(T\) is quasinilpotent and **every nonzero vector has the exact pointwise exponent**
\[
\boxed{k_T(x_0,\ldots,x_{m-1})=\max_{j:x_j\ne0}k_B(x_j).} \tag{1}
\]
In particular, \(\Lambda(T)=\Lambda(B)\). Moreover, for every \(0\le\tau\le1\), the exponent sublevel subspace \(M_\tau(A)=\{0\}\cup\{y\ne0:k_A(y)\le\tau\}\) satisfies
\[
\boxed{M_\tau(T)=\underbrace{M_\tau(B)\oplus\cdots\oplus M_\tau(B)}_{m\ \mathrm{summands}}.} \tag{2}
\]

This transfer has a concrete compactness contrast. Fix \(1\le p<\infty\) and \(m\ge2\). On \(\ell_p(\mathbb N_0)\), define a backward weighted shift \(S\) by \(Se_0=0\), \(Se_n=w_ne_{n-1}\) for \(n\ge1\), where
\[
w_{mn+j}=1\quad(n\ge0,\ 1\le j<m),\qquad
w_{mn}=e^{-n^2}\quad(n\ge1).
\]
Then \(S\) is a noncompact quasinilpotent contraction with
\[
\boxed{\Lambda(S)=[0,1],\qquad S^m\text{ compact},\qquad S^r\text{ noncompact for }1\le r<m.} \tag{3}
\]
Thus its image in the Calkin algebra has exact nilpotency index \(m\), independently of its maximal resolvent power set. In particular, a full power set does **not** require monotone, summable, or compact shift weights.

## Assumptions and scope

The complex scalar field is used for Fourier averaging over roots of unity. The integer \(m\) is finite and at least two. The growth condition (U) is an assumption for the transfer principle, **not** a property claimed for all nonnilpotent quasinilpotent operators. The example uses the standard infinite-dimensional complex \(\ell_p\) space, \(1\le p<\infty\). A compact weighted backward shift with all positive weights satisfies (U), as verified below. Results about arbitrary nonmonotone weights outside this cyclic-root class are not claimed.

## Proof

**1. Algebraic cyclic-root identity.** Under the block decomposition of \(E\), direct multiplication gives
\[
T^m=\operatorname{diag}(B,\ldots,B).
\]
Consequently \(\sigma(T)^m=\sigma(B)=\{0\}\), so \(T\) is quasinilpotent. Put \(R_B(\zeta)=(\zeta I-B)^{-1}\) and \(\zeta=z^m\). The polynomial factorization \((zI-T)\sum_{h=0}^{m-1}z^{m-1-h}T^h=z^mI-T^m\) yields the exact resolvent identity
\[
R_T(z)=\left(\sum_{h=0}^{m-1}z^{m-1-h}T^h\right)
\operatorname{diag}\bigl(R_B(\zeta),\ldots,R_B(\zeta)\bigr). \tag{4}
\]
For \(0<|z|\le1\), this gives \(\|R_T(z)\|\le C_m\|R_B(\zeta)\|\), where \(C_m=\sum_{h=0}^{m-1}\|T\|^h\). Conversely, applying (4) to an input supported in the last block and taking the first output coordinate gives exactly \(R_B(\zeta)\) on that block. Therefore
\[
\|R_B(\zeta)\|\le\|R_T(z)\|\le C_m\|R_B(\zeta)\|. \tag{5}
\]
In particular their logarithms differ by at most \(\log C_m\). Since \(B\) is quasinilpotent, both resolvent norms tend to infinity as their arguments approach zero. Condition (U) makes every fixed power of \(|z|\) negligible on this logarithmic scale.

**2. Upper exponent bound.** For each fixed \(x=(x_j)\ne0\), (4), boundedness of the finitely many \(T^h\), and the finite direct-sum inequalities imply
\[
\|R_T(z)x\|\le C_m\sum_{j=0}^{m-1}\|R_B(z^m)x_j\|. \tag{6}
\]
Ignore the zero coordinates. Since the sum is finite, dividing its logarithm by the denominator in (5) and taking the limsup gives
\[
k_T(x)\le\max_{j:x_j\ne0}k_B(x_j). \tag{7}
\]
Additive constants disappear because the resolvent logarithms tend to infinity; the substitution \(\zeta=z^m\) ranges over every sufficiently small nonzero complex \(\zeta\).

**3. Fourier extraction and the reverse bound.** Denote the first coordinate projection by \(P_0\). For each \(m\)-th root of unity \(\omega\), formula (4) has first block
\[
P_0R_T(\omega z)x
=\sum_{j=0}^{m-1}(\omega z)^{m-1-j}R_B(\zeta)x_j. \tag{8}
\]
(There is no wrapped contribution in the first block from a power \(T^h\) with \(0\le h<m\).) Fourier inversion on the finite cyclic group gives, for every \(j\),
\[
z^{m-1-j}R_B(\zeta)x_j
=\frac1m\sum_{\omega^m=1}\omega^{-(m-1-j)}P_0R_T(\omega z)x.
\]
Thus
\[
\max_{\omega^m=1}\|R_T(\omega z)x\|\ge
|z|^{m-1-j}\|R_B(\zeta)x_j\|. \tag{9}
\]
By (5) the denominators at all the finitely many roots are \(\log\|R_B(\zeta)\|+O(1)\), uniformly. Condition (U) says \((m-1)|\log|z||=o(\log\|R_B(\zeta)\|)\). Taking the limsup over \(\zeta\to0\), then choosing the best root for each \(\zeta\), proves \(k_T(x)\ge k_B(x_j)\) for each nonzero coordinate. This and (7) prove (1). Equations for the power set and exponent sublevel spaces follow immediately; a finite maximum of values already attained in \(\Lambda(B)\) is itself one of those values.

**4. Explicit noncompact weighted shifts.** Let \(B\) on \(X=\ell_p(\mathbb N_0)\) have \(Be_0=0\) and \(Be_n=e^{-n^2}e_{n-1}\) for \(n\ge1\). Then \(B\) is compact. Since its weights decrease,
\[
\|B^k\|=\exp\left(-\sum_{j=1}^{k}j^2\right),
\]
so \(B\) is quasinilpotent. For each fixed integer \(N\ge0\), the zeroth coordinate of \(R_B(\zeta)e_N\) gives
\[
\|R_B(\zeta)\|\ge
\exp\left(-\sum_{j=1}^{N}j^2\right)|\zeta|^{-N-1}. \tag{10}
\]
As \(N\) can be arbitrarily large, this proves (U). Ignatev's July 2026 theorem for strictly decreasing, positive, power-summable backward-shift weights gives \(\Lambda(B)=[0,1]\). The companion \(T\) with \(E=(\ell_p)^m\) is identified isometrically with the single-space backward shift \(S\) by listing coordinates in the order \(e_{mn+j}\). Formula (1) gives \(\Lambda(S)=[0,1]\). Because \(T^m\) is a finite direct sum of the compact operator \(B\), it is compact. For \(1\le r<m\), the restriction of \(T^r\) from block \(r\) to block zero is the identity on infinite-dimensional \(X\). Hence \(T^r\) is not compact. The explicit weights have norm one and give quasinilpotence by the already proved identity for \(T^m\). This proves (3).

**5. Boundary of the growth hypothesis.** With \(B=0\) on any nonzero \(X\), condition (U) fails. Here \(\Lambda(B)=\{1\}\), whereas the cyclic companion is nilpotent of order \(m\), with \(\Lambda(T)=\{1/m,2/m,\ldots,1\}\): an input in block \(j\) has a resolvent pole of order \(j+1\), while the operator resolvent has pole order \(m\). Thus removing (U) outright makes the transfer statement false.

## Verification

The factorization (4), block coefficient identity (8), and discrete Fourier extraction (9) can be independently reproduced by `python checker.py`, which uses Python's standard library and tests finite nilpotent matrix truncations. In the present execution it passed 1148 finite algebra/Fourier assertions, including zero-base boundary cases. These tests check algebra and signs only; they do not establish the asymptotic statements (U), (1), or the infinite-dimensional compactness conclusions. Those follow from the displayed analytic arguments and the explicitly cited published backward-shift theorem. The sole invoked non-elementary external result in the example is the full power-set classification for the decreasing-weight shift.

## Relationship to prior work

Douglas–Yang introduced the local resolvent exponent and its invariant sublevel spaces. Ji–Zhang established right-closedness and abstract realizations. Hu–Ji classified several monotone-weight shifts, and Hu–Ji–Liang studied general Banach-space realizations. Ignatev's Theorem 4 proves \(\Lambda(B)=[0,1]\) for decreasing, power-summable backward shifts; its concluding remark explicitly raises relaxing monotonicity. The new statement is a pointwise cyclic-companion transfer, not an assertion that Ignatev's theorem itself applies to the interspersed weights. In the example infinitely many weights are exactly one, so neither decay to zero nor power summability nor monotonicity holds. The exact Calkin nilpotency index and all exponent filtration spaces are likewise not consequences of the cited abstract existence results alone. Earlier formulations of the transfer identity under matrix-resolvent or companion-operator terminology cannot be excluded solely by the searches described in the review.

## Limitations

The transfer theorem assumes (U) and complex scalars; it does not settle arbitrary nonmonotone weighted shifts or quasinilpotent Banach operators without (U). The explicit construction is power-compact but not compact; it is not claimed to be injective or strongly cyclic. The operator-power-set statement relies on the stated published decreasing-weight classification. The finite checker cannot establish any infinite-dimensional assertion. A separate independent mathematical audit and publication-priority review have not been performed.

## References

1. E. Ignatev, *The power set of a quasinilpotent backward weighted shift*, arXiv:2607.16743 (first public arXiv version July 18, 2026), Theorem 4 and concluding remark. https://arxiv.org/abs/2607.16743
2. C. L. Hu, Y. Q. Ji, D. H. Liang, *On the Power Set of Quasinilpotent Operators in Banach Spaces*, arXiv:2607.01614 (first version July 2, 2026), Sections 1–4. https://arxiv.org/abs/2607.01614
3. C. Hu and Y. Ji, *Power Set of Some Quasinilpotent Weighted Shifts on* \(\ell_p\), arXiv:2306.00387 (2023), Sections 2–4. https://arxiv.org/abs/2306.00387
4. Y. Ji and Y. Zhang, *On the Power Set of Quasinilpotent Operators*, arXiv:2305.09963 (2023). https://arxiv.org/abs/2305.09963
