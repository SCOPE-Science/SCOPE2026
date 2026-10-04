# Exact type-class Wasserstein transport and the sharp \(n^{-1/2}\) almost-i.i.d. scale
## Finding
Let \(\mathcal X\) be a finite alphabet of size \(N\), let \(n\ge 1\), and let \(t\) be an \(n\)-type, so that \(m_x:=nt_x\) is an integer for each \(x\in\mathcal X\). Write \(T_{t,n}\subseteq\mathcal X^n\) for the type class, \(U_{t,n}\) for its uniform law, and \(P_{t,n}:=t^{\otimes n}\). Equip \(\mathcal X^n\) with Hamming distance. If \(Y\sim P_{t,n}\) and \(M_x\) is the number of occurrences of \(x\) in \(Y\), then
\[
W_1(U_{t,n},P_{t,n})=\frac12\,\mathbb E\!\left[\sum_{x\in\mathcal X}|M_x-m_x|\right].
\]
In particular,
\[
\frac1nW_1(U_{t,n},P_{t,n})
\le \frac1{2\sqrt n}\sum_{x\in\mathcal X}\sqrt{t_x(1-t_x)}
\le \frac{\sqrt{N-1}}{2\sqrt n}.
\]
This replaces the bound \(\sqrt{(N-1)\log(n+1)/(2n)}\) in Proposition 23 of Girardi--De Palma--Lami and in Proposition 22 of Girardi--Lee--Hayashi--Lami by a log-free rate.

For a fixed rational probability vector \(t\), along integers \(n\) for which \(nt\) is integral,
\[
\frac{W_1(U_{t,n},P_{t,n})}{\sqrt n}
\longrightarrow
\frac1{\sqrt{2\pi}}\sum_{x\in\mathcal X}\sqrt{t_x(1-t_x)}.
\]
For the balanced binary type and even \(n\), the identity becomes the closed form
\[
W_1(U_{1/2,n},(1/2,1/2)^{\otimes n})
=\frac{n}{2^{n+1}}{n\choose n/2}.
\]

There is also a quantum consequence. For states \(\{\rho_x:x\in\mathcal X\}\) on one finite-dimensional system, define
\[
\bar\rho_t:=\sum_x t_x\rho_x,
\qquad
\Omega_{t,n}:=\frac1{|T_{t,n}|}\sum_{x^n\in T_{t,n}}\rho_{x_1}\otimes\cdots\otimes\rho_{x_n}.
\]
Single-site data processing for quantum \(W_1\) gives
\[
\|\Omega_{t,n}-\bar\rho_t^{\otimes n}\|_{W_1}
\le W_1(U_{t,n},P_{t,n}),
\]
so all bounds above transfer verbatim. If the \(\rho_x\) are mutually orthogonal pure states, the quantum distance equals the classical Hamming-Wasserstein distance. Hence normalized order \(n^{-1/2}\) is optimal uniformly over state families, although the recent \(\sqrt{\log n/n}\) estimate is not.

## Assumptions and scope
The exact transport identity uses only a finite alphabet, an exact type \(t\), and the ordinary Hamming cost in which changing one coordinate costs one. The asymptotic constant is stated for a fixed rational \(t\) along admissible block lengths; zero coordinates cause no difficulty and simply contribute zero. The quantum corollary uses the quantum Wasserstein distance of order one employed in the cited almost-i.i.d. papers and its data-processing inequality for single-system channels. It does not claim equality for nonorthogonal signal states.

## Proof
For a string \(y\in\mathcal X^n\) with count vector \(k=(k_x)\), the minimum Hamming distance from \(y\) to the target type class is
\[
d_H(y,T_{t,n})=\sum_{x:k_x>m_x}(k_x-m_x)
=\frac12\sum_x|k_x-m_x|.
\]
Indeed, every changed coordinate can decrease the count discrepancy by at most one surplus and one deficit, while changing exactly one surplus occurrence into one deficit symbol attains this number of changes.

Every coupling \(\Gamma\) of \(P_{t,n}\) and \(U_{t,n}\) therefore satisfies
\[
\mathbb E_\Gamma d_H(X,Y)\ge \mathbb E_{P_{t,n}}d_H(Y,T_{t,n})
=\frac12\mathbb E\|M-nt\|_1.
\]
For the reverse inequality, condition on \(Y=y\). Choose uniformly the required number of positions carrying surplus symbols, and reassign those selected positions uniformly among all assignments that fill the exact deficits. This changes exactly \(d_H(y,T_{t,n})\) coordinates. The repair kernel is equivariant under coordinate permutations. Since \(P_{t,n}\) is exchangeable, its repaired output is exchangeable; since it is supported on the single orbit \(T_{t,n}\), it must be uniform there. This is a coupling with the lower-bound cost, proving the exact identity.

For the finite bound, Cauchy--Schwarz gives
\[
\mathbb E|M_x-nt_x|\le\sqrt{\operatorname{Var}(M_x)}
=\sqrt{nt_x(1-t_x)}.
\]
Summing and dividing by \(2n\) gives the first inequality. A second Cauchy--Schwarz step yields
\[
\left(\sum_x\sqrt{t_x(1-t_x)}\right)^2
\le N\sum_x t_x(1-t_x)
=N\left(1-\sum_x t_x^2\right)\le N-1.
\]

For fixed rational \(t\), the multinomial central limit theorem gives
\[
\frac{M-nt}{\sqrt n}\Rightarrow Z,
\]
where \(Z_x\) is centered Gaussian with variance \(t_x(1-t_x)\). The coordinates are uniformly integrable because their second moments are fixed, so expectations of absolute values converge. Therefore
\[
\frac1{2\sqrt n}\mathbb E\|M-nt\|_1
\to\frac12\sum_x\mathbb E|Z_x|
=\frac1{\sqrt{2\pi}}\sum_x\sqrt{t_x(1-t_x)}.
\]
For the balanced binary law, \(\frac12\|M-nt\|_1=|B-n/2|\) with \(B\sim\operatorname{Bin}(n,1/2)\), and the standard adjacent-binomial cancellation gives \(\mathbb E|B-n/2|=n{n\choose n/2}/2^{n+1}\).

For the quantum statement, apply at every coordinate the same classical-to-quantum preparation channel \(x\mapsto\rho_x\). Its product maps \(U_{t,n}\) to \(\Omega_{t,n}\) and \(P_{t,n}\) to \(\bar\rho_t^{\otimes n}\). The single-system data-processing property of quantum \(W_1\), iterated over coordinates, gives the displayed contraction. For mutually orthogonal pure signal states, both outputs are diagonal in a product basis and quantum \(W_1\) reduces to classical Hamming-Wasserstein distance, giving equality and proving sharpness of the \(n^{-1/2}\) normalized order.

## Verification
The bundled script `artifacts/verify.py` independently computes small type classes, solves the full discrete optimal-transport linear program, and checks the optimum against \(\frac12\mathbb E\|M-nt\|_1\) for binary and ternary examples. It also checks the balanced-binary closed form and the two finite upper bounds. These finite computations corroborate the construction; the all-blocklength result is established by the analytic coupling proof above.

## Relationship to prior work
Girardi, De Palma, and Lami introduced Wasserstein almost-i.i.d. sources and, in Proposition 23 of arXiv:2605.15114, bounded the normalized distance between a uniform type class and the corresponding i.i.d. product by \(\sqrt{(N-1)\log(n+1)/(2n)}\). Their proof uses a transportation-cost inequality and a standard lower bound on type-class cardinality; Remark 26 only sketches the heuristic that typical types lie at Hamming distance of order \(\sqrt n\). The exact optimal coupling and exact multinomial-deviation identity above are not stated there.

Girardi, Lee, Hayashi, and Lami reuse that estimate as Proposition 22 of arXiv:2609.17309 in their proof for arbitrarily varying null hypotheses. Their equations (3.56)--(3.59) pass from the classical type law to the corresponding symmetrized quantum state by single-system classical-to-quantum data processing. Substituting the present exact identity removes the logarithmic loss at that step and provides the sharp fixed-type asymptotic constant.

The older constant-composition distribution-matching literature studies the same type-class combinatorics but measures approximation by informational divergence and rate loss rather than Hamming-Wasserstein transport. The foundational quantum \(W_1\) work of De Palma, Marvian, Trevisan, and Lloyd establishes that diagonal quantum states recover classical Hamming-Wasserstein distance, which supplies the orthogonal-state equality case used here.

## Limitations
The fixed-type asymptotic constant is proved only along admissible block lengths for a fixed rational \(t\); no second-order correction is claimed. The quantum bound can be strict for nonorthogonal signal states, and no attempt is made to characterize equality in that general case. The result sharpens the quantitative type-class approximation used in recent almost-i.i.d. arguments; it does not change the already-established asymptotic Stein exponent, for which any vanishing normalized Wasserstein error suffices. Literature searches cannot exclude every older formulation under remote terminology, so an alias risk remains for the purely classical optimal-transport identity.

## References
1. F. Girardi, G. De Palma, and L. Lami, *New approaches to almost i.i.d. information theory*, arXiv:2605.15114v2 (first public 2026-05-14), especially Proposition 23 and Remark 26.
2. F. Girardi, K.-Y. Lee, M. Hayashi, and L. Lami, *Generalised quantum Stein's lemma more robust than ever*, arXiv:2609.17309v1 (2026-09-15), especially Proposition 22 and equations (3.56)--(3.59).
3. G. De Palma, M. Marvian, D. Trevisan, and S. Lloyd, *The Quantum Wasserstein Distance of Order 1*, IEEE Transactions on Information Theory 67 (2021), 6627--6643; arXiv:2009.04469.
4. P. Schulte and G. Böcherer, *Constant Composition Distribution Matching*, IEEE Transactions on Information Theory 62 (2016), 430--434; arXiv:1503.05133.
