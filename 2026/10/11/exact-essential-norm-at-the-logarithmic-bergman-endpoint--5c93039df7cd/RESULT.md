# Exact essential norm at the logarithmic Bergman endpoint

## Finding

Let \(\mathbb D\) be the unit disk and \(dA(z)=dx\,dy/\pi\). Define \(A^2_{\log^2}\) by the norm
\[
\|f\|_{A^2_{\log^2}}^2=\int_{\mathbb D}|f(z)|^2\left(\log\frac{e}{1-|z|^2}\right)^2dA(z).
\]
On the Taylor series \(f(z)=\sum_{n\ge0}a_nz^n\), consider the Hilbert matrix operator
\[
(Hf)(z)=\sum_{m\ge0}\left(\sum_{n\ge0}\frac{a_n}{m+n+1}\right)z^m.
\]
Its exact essential norm between the stated Hilbert spaces is
\[
\boxed{\|H:A^2_{\log^2}\longrightarrow A^2\|_{\mathrm{ess}}=2.}
\]
Here the essential norm is the distance, in the operator norm, to all compact operators between these two spaces. In particular, every finite-rank approximation to \(H\) has error at least \(2\), and for every \(\varepsilon>0\) there exists a finite-rank approximation with error at most \(2+\varepsilon\).

## Assumptions and scope

The logarithm is natural, area is normalized by \(1/\pi\), and the logarithmic weight is exactly \((\log(e/(1-|z|^2)))^2\), with no extra renormalization. The result concerns the classical coefficient Hilbert matrix from this weighted Bergman Hilbert space to the unweighted Bergman Hilbert space, **not** its operator norm or spectral set on a single Hilbert space. No positivity or reality assumption is imposed on Taylor coefficients. The compact-operator ideal is taken over complex Hilbert spaces.

## Proof

**Exact coefficient normalization.** Orthogonality of monomials yields
\[
\|f\|_{A^2_{\log^2}}^2=\sum_{n\ge0}v_n|a_n|^2,\qquad
v_n=\int_0^1t^n\bigl(1-\log(1-t)\bigr)^2\,dt.
\]
Write \(h_k=\sum_{j=1}^k1/j\) and \(h_k^{(2)}=\sum_{j=1}^k1/j^2\). Differentiating the beta integral \(\int_0^1t^n(1-t)^{q-1}\,dt=n!/[q(q+1)\cdots(q+n)]\) twice at \(q=1\) gives
\[
\boxed{v_n=\frac{(1+h_{n+1})^2+h_{n+1}^{(2)}}{n+1}.}
\]
Consequently \(v_n=(\log n)^2n^{-1}(1+O((\log n)^{-1}))\) as \(n\to\infty\). The unweighted Bergman norm is \(\|g\|_{A^2}^2=\sum_{m\ge0}|\widehat g(m)|^2/(m+1)\). Conjugating by the corresponding diagonal unitaries identifies \(H\) with the matrix on ordinary \(\ell^2(\mathbb N_0)\)
\[
B_{mn}=\frac{1}{(m+n+1)\sqrt{m+1}\sqrt{v_n}},\qquad m,n\ge0.
\]
The coefficient defining each output coordinate is absolutely convergent by Cauchy--Schwarz, since \(\sum_{n\ge3}1/(n(\log n)^2)<\infty\).

**A compact-equivalent triangular model.** Define the positive triangular matrix
\[
D_{mn}=\begin{cases}\dfrac{1}{\sqrt{mn}\log n},&n\ge m\ge3,\\0,&\text{otherwise.}\end{cases}
\]
We prove \(B-D\) is Hilbert--Schmidt. For \(n\ge m\ge3\), define \(q_n=\log n/\sqrt{nv_n}\); then \(q_n=1+O(1/\log n)\) and
\[
\frac{B_{mn}}{D_{mn}}=q_n\sqrt{\frac{m}{m+1}}\frac{n}{m+n+1}.
\]
Hence, with an absolute constant \(C\),
\[
|B_{mn}-D_{mn}|^2\le \frac{C}{mn(\log n)^2}\left(\frac1{(\log n)^2}+\frac1{m^2}+\frac{m^2}{n^2}\right).
\]
The three double series converge: summing first over \(3\le m\le n\), they are bounded respectively by constant multiples of
\[
\sum_{n\ge3}\frac{\log n}{n(\log n)^4},\quad
\sum_{n\ge3}\frac1{n(\log n)^2},\quad
\sum_{n\ge3}\frac1{n(\log n)^2}.
\]
For \(m>n\ge3\), the asymptotic of \(v_n\) implies
\[
B_{mn}^2\le C\frac{n}{m^3(\log n)^2},
\]
whose double sum converges because \(\sum_{m>n}m^{-3}=O(n^{-2})\). The finitely many rows or columns with index below \(3\) are square-summable: their tails are respectively \(O(1/[n(\log n)^2])\) and \(O(m^{-3})\) after squaring. Thus \(B-D\in\mathcal S_2\), in particular it is compact. It follows that \(\|B\|_{\mathrm{ess}}=\|D\|_{\mathrm{ess}}\).

**Essential-norm upper bound.** Let \(Q_N\) project onto coordinates indexed by \(n\ge N\ge3\). The difference \(D-Q_NDQ_N\) has finite rank. On this tail, apply Schur's test with the positive vector \(u_n=1/\sqrt{n\log n}\). Every row ratio satisfies
\[
\frac{1}{u_m}\sum_{n\ge N}D_{mn}u_n
=\sqrt{\log m}\sum_{n\ge m}\frac1{n(\log n)^{3/2}}
\le2+\frac1{m\log m}\le2+\frac1{N\log N},
\]
using comparison of the decreasing summand with its integral. Every column ratio satisfies
\[
\frac{1}{u_n}\sum_{m\ge N}D_{mn}u_m
=\frac1{\sqrt{\log n}}\sum_{m=N}^n\frac1{m\sqrt{\log m}}
\le2+\frac1{N\log N}.
\]
Therefore \(\|Q_NDQ_N\|\le2+1/(N\log N)\), and \(\|D\|_{\mathrm{ess}}\le2\).

**Essential-norm lower bound.** Fix \(L>0\) and take \(R\to\infty\). Set \(M=\lceil e^R\rceil\) and \(T=\lfloor\exp(Re^L)\rfloor\). Use the finitely supported nonnegative vector
\[
b_n=\frac{\mathbf1_{\{M\le n\le T\}}}{\sqrt{n\log n}}.
\]
Integral comparison gives \(\|b\|_2^2=L+o_R(1)\). For every \(M\le m\le T\), the decreasing-summand integral lower bound yields
\[
(Db)_m=\frac1{\sqrt m}\sum_{n=m}^T\frac1{n(\log n)^{3/2}}
\ge\frac{2}{\sqrt{m\log m}}\left(1-\sqrt{\frac{\log m}{\log(T+1)}}\right).
\]
Squaring and summing over the same range, then converting the Riemann sum by \(u=\log\log x-\log R\), gives
\[
\liminf_{R\to\infty}\|Db\|_2^2\ge 4\int_0^L(1-e^{(u-L)/2})^2du
=4\bigl(L-3+4e^{-L/2}-e^{-L}\bigr).
\]
For fixed \(L\), these normalized finitely supported vectors escape to infinity and are weakly null; every compact operator sends them to zero in norm. Hence
\[
\|D\|_{\mathrm{ess}}\ge2\sqrt{1-\frac3L+\frac{4e^{-L/2}-e^{-L}}L}.
\]
Letting \(L\to\infty\) proves \(\|D\|_{\mathrm{ess}}\ge2\). Combined with the upper bound and compact equivalence, this proves the asserted equality.

## Verification

The computation of \(v_n\) follows by two derivatives of a finite rational beta-product, not by numerical integration. The Hilbert--Schmidt assertion is backed by the three displayed convergent numerical series and the off-triangular estimates, rather than a finite matrix cutoff. The Schur bounds are analytic inequalities and the lower bound uses an explicit family of weakly-null vectors; no finite-dimensional singular-value extrapolation is used. Run the supplementary arithmetic spot-check with `python3 artifacts/verify.py`; it verifies the beta-product coefficients, the finite-block estimates, and the closed-form lower-bound integrals but is not a substitute for the infinite-dimensional proof.

## Relationship to prior work

Norrbo's 2026 theorem proves boundedness at the logarithmic endpoint but supplies no essential-norm constant. Ye and Feng (2023) give norm bounds above that endpoint. Lindström, Miihkinen, and Norrbo (2022) compute essential norms for generalized Hilbert operators acting within the same weighted analytic space, including standard Bergman spaces, not for the asymmetric endpoint map here. The present result uses an explicit compact reduction to a critical discrete Copson tail to determine the missing exact number. The 2022 theorem's bounded-operator assumptions and same-space conclusions do not imply this cross-space essential norm.

## Limitations

The value is specific to the stated logarithmic weight and area normalization; multiplying the source norm by an arbitrary constant changes the number. The proof identifies the essential norm, not the potentially larger full operator norm or point spectrum. The argument does not give a rate for optimal approximation numbers beyond their convergence to the essential norm. Full texts of two nearby operator-norm studies were not available for complete comparison; see the attached literature assessment.

## References

1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1 (first publicly posted 2026-09-23), Theorem 3.5 and Section 4. https://arxiv.org/pdf/2610.00252
2. M. Lindström, S. Miihkinen, D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, Adv. Math. 408 (2022), 108598. DOI:10.1016/j.aim.2022.108598. https://www.diva-portal.org/smash/get/diva2:1689957/FULLTEXT01.pdf
3. S. Ye, G. Feng, *Norm of the Hilbert Matrix on Logarithmically Weighted Bergman Spaces*, Complex Anal. Oper. Theory 17 (2023), article 97. DOI:10.1007/s11785-023-01403-2.
4. H. Hu, S. Ye, *Norm of the Hilbert matrix on the logarithmically weighted Bergman spaces*, Acta Mathematica Scientia Series A, publication entry dated 2026-03-25, bibliographic record https://portal.mardi4nfdi.de/wiki/Norm_of_the_Hilbert_matrix_on_the_logarithmically_weighted_Bergman_spaces.
