# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The calculation is a direct deformation of the Gaussian kernel identity in Qin's Lemma 2.1. Replacing the active matrix \(4U^*\) by \(2(1+q)U^*\) and the passive matrix \(2I\) by \((1+\rho)I\) gives
\[
D=\operatorname{diag}\!\left(U/[2(1+q)],I/(1+\rho)\right)
\]
and
\[
\kappa=[4(1+q)^2(1+\rho)^{n-2}]^{-1}.
\]
The Hermitian part is positive for the stated parameters, so the Gaussian integral is legitimate. The symbol modulus is exactly \(e^{-q|\xi|^2-\rho|z'|^2}\).

The sixteen quaternionic products \(U_jV_k\) were checked directly with the displayed matrices. Grouping equal product matrices gives zero total coefficient in each class. Since the deformed \(D_U D_V\) depends on the pair only through \(UV\), Qin's cancellation survives unchanged and yields \(T_fT_g=0\).

The Schatten assertion follows from an explicit singular-value calculation, not from symbol decay. A linear Fock composition operator with contraction singular values \(s_1,\ldots,s_n\) has Schatten \(p\)-sum \(\prod_j(1-s_j^p)^{-1}\). Here the active singular values are always \(1/[2(1+q)]<1\); the passive singular values are \(1/(1+\rho)\). This proves membership in every \(S_p\), \(p>0\), exactly when there are no passive directions or \(\rho>0\). At \(\rho=0\) with \(n>2\), tensor factorization with an infinite-dimensional identity proves noncompactness.

The nondecay and nonradial assertions are witnessed explicitly on two rays of equal Euclidean norm. Infinite rank is established independently of finite-rank Toeplitz theorems: the operators preserve homogeneous degree, while their kernel actions give nonpolynomial finite sums of exponentials for generic active vectors. This also verifies that neither factor is zero.

## Originality

**PASS, to the best of our knowledge.** Qin's arXiv:2609.20555v1 (submitted 17 September 2026) proves the existence of two bounded nonradial Schwartz symbols with zero product for \(n\ge2\). Its displayed construction has full Gaussian decay and its text does not state compactness, trace-class, or Schatten consequences. The present claim isolates a new endpoint of the same matrix mechanism: active decay can be removed completely while the resulting Toeplitz factors remain in every Schatten class. It also identifies the exact \(\rho=0\) versus \(\rho>0\) compactness transition in the passive coordinates.

Searches for the source paper together with "Schatten", "trace class", "compact", "nonvanishing symbol", "quadratic phase", and "zero product" did not locate this endpoint statement or the all-Schatten zero-product pair. Searches of the current SCOPE archive by the source identifier, Toeplitz zero products, Fock space, nonvanishing symbols, and Schatten terminology found no overlapping record.

Relevant prior art was checked in several directions. Bauer--Le (2011) gives earlier Segal--Bargmann zero products and finite-rank results; its full text was not inspected, although its abstract and Qin's detailed description of its examples were. This is the most important residual originality risk. Lin--Lu--Zu (2026) gives a recent Fourier criterion for bounded-symbol Toeplitz representation and applies it to weighted composition operators; only its abstract-level statement was inspected, so its detailed formulas may already encompass the single Gaussian building-block representation. That representation is not claimed as new. Isralowitz--Zhu (2010) treats compact and Schatten Toeplitz operators for positive measure symbols, a structurally different setting.

No claim is made that bounded nondecaying symbols producing compact Toeplitz operators are themselves new in isolation. The contribution claimed here is the explicit nontrivial zero-product pair with nondecaying bounded symbols, all-\(p\) Schatten membership, infinite-rank defect, and the parameter-sharp passive compactness boundary.

## Value

**PASS.** Qin's counterexample shows that rapid decay and smoothness do not restore the zero-product property in dimensions at least two. The endpoint deformation sharpens the mechanism substantially: decay in the two coordinates responsible for cancellation is unnecessary. In dimension two the symbols can stay uniformly macroscopic along sequences tending to infinity while both Toeplitz factors are in every Schatten ideal. In higher dimension the same family exhibits a clean operator-ideal phase transition controlled solely by damping in the unused coordinates. This separates symbol-side decay from operator-side smoothing and gives a reusable quadratic-phase mechanism.

## Scope and limitations

The statement is confined to the explicit family and \(n\ge2\). It does not settle the one-dimensional bounded-symbol problem, classify all compact or Schatten Toeplitz operators with complex symbols, determine the optimal Schatten quasi-norms of the four-term sums, or assert uniqueness of this construction. The originality assessment remains subject to the uninspected portions of the older and recent literature identified above.
