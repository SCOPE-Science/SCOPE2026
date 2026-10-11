# Compact-defect characterization of the essential norm among relative operator seminorms

## Finding

Let \(H\) be an arbitrary infinite-dimensional real or complex Hilbert space. Fix \(G\in\mathcal B(H)\) with \(\|G\|=1\), and for \(T\in\mathcal B(H)\) define the relative seminorm
\[
p_G(T)=\inf_{\delta>0}\sup\{\|Tx\|:\|x\|=1,\ \|Gx\|>1-\delta\}.
\]
Write \(\mathcal K(H)\) for the compact operators and \(\|T\|_{\mathrm{ess}}=\inf_{K\in\mathcal K(H)}\|T-K\|\).

**Theorem.** The following are equivalent:

1. For every \(T\in\mathcal B(H)\), \(p_G(T)=\|T\|_{\mathrm{ess}}\).
2. The positive operator \(B=I-G^*G\) is compact and has trivial kernel.

When these conditions hold, the spectral projection \(P_\varepsilon=\mathbf 1_{[0,\varepsilon)}(B)\) satisfies
\[
p_G(T)=\lim_{\varepsilon\downarrow0}\|TP_\varepsilon\|=\|T\|_{\mathrm{ess}}
\quad\text{for every }T\in\mathcal B(H).
\]
Consequently, \(\ker p_G=\mathcal K(H)\), and the relative seminorm descends precisely to the quotient norm of the Calkin algebra \(\mathcal B(H)/\mathcal K(H)\). Such a norm-one operator \(G\) exists if and only if \(H\) is separable.

## Assumptions and scope

The scalars are real or complex, and \(H\) is infinite-dimensional, not initially assumed separable. Norms and adjoints are those of Hilbert-space bounded linear operators. The set in the defining supremum is nonempty for each \(\delta>0\) because \(\|G\|=1\). The spectral projections use the bounded self-adjoint Borel functional calculus. The equality in the theorem is **simultaneous for every** bounded operator \(T\); no claim is made that the equality for one fixed \(T\) forces the compact-defect condition.

## Proof

**Step 1: spectral localization from the relative seminorm.** Because \(\|G\|=1\), \(B=I-G^*G\) is positive and \(0\le B\le I\). For \(\varepsilon>0\) let \(Q_\varepsilon=\mathbf1_{[\varepsilon,\infty)}(B)\), and set \(P_\varepsilon=I-Q_\varepsilon\). The spectral theorem gives \(B\ge\varepsilon Q_\varepsilon\). If \(\|x\|=1\) and \(\|Gx\|>1-\delta\), with \(0<\delta<1\), then
\[
\varepsilon\|Q_\varepsilon x\|^2
\le\langle Bx,x\rangle
=1-\|Gx\|^2<2\delta-\delta^2.
\]
Hence \(p_G(Q_\varepsilon)=0\) for every \(\varepsilon>0\).

**Step 2: necessity.** Suppose \(p_G(T)=\|T\|_{\mathrm{ess}}\) for every bounded \(T\). Step 1 gives \(\|Q_\varepsilon\|_{\mathrm{ess}}=0\), so \(Q_\varepsilon\) is compact; an orthogonal projection is compact exactly when it has finite rank. In addition,
\[
\|B-BQ_\varepsilon\|=\|BP_\varepsilon\|\le\varepsilon.
\]
Thus \(B\) is a norm limit of finite-rank operators, hence compact. If a unit vector \(x\) belonged to \(\ker B\), then \(\|Gx\|=1\). For the rank-one orthogonal projection \(R_x\) onto the span of \(x\), the defining supremum is at least \(\|R_xx\|=1\) for every \(\delta\), while it cannot exceed \(1\). This gives \(p_G(R_x)=1\) although \(\|R_x\|_{\mathrm{ess}}=0\), a contradiction. Therefore \(\ker B=\{0\}\).

**Step 3: sufficiency and an exact spectral formula.** Suppose instead that \(B\) is positive, compact, and injective. Since \(H\) is infinite-dimensional, the spectral theorem implies that each \(Q_\varepsilon\) has finite rank and \(P_\varepsilon\to0\) strongly as \(\varepsilon\downarrow0\); the latter follows from the strong convergence of the decreasing projections to \(\mathbf1_{\{0\}}(B)=0\). Define
\[
f_\delta(T)=\sup\{\|Tx\|:\|x\|=1,\ \|Gx\|>1-\delta\}.
\]
From Step 1, for fixed \(\varepsilon>0\) and \(0<\delta<1\),
\[
f_\delta(T)\le\|TP_\varepsilon\|+\|T\|\sqrt{(2\delta-\delta^2)/\varepsilon}.
\]
Taking \(\delta\downarrow0\) shows \(p_G(T)\le\|TP_\varepsilon\|\). Conversely, fix \(0<\delta<1\) and choose \(0<\varepsilon<2\delta-\delta^2\). Every unit \(x\in\operatorname{ran}P_\varepsilon\) satisfies
\[
\|Gx\|^2=1-\langle Bx,x\rangle>1-\varepsilon>(1-\delta)^2.
\]
Therefore \(f_\delta(T)\ge\|TP_\varepsilon\|\). As \(\varepsilon\downarrow0\), these projection norms decrease to a limit \(L(T)\); hence \(f_\delta(T)\ge L(T)\) for every \(\delta\), and \(p_G(T)\ge L(T)\). Combining the inequalities yields
\[
p_G(T)=L(T)=\lim_{\varepsilon\downarrow0}\|TP_\varepsilon\|.
\]

**Step 4: identify the quotient norm.** Because \(TQ_\varepsilon\) has finite rank,
\[
\|T\|_{\mathrm{ess}}\le\|T-TQ_\varepsilon\|=\|TP_\varepsilon\|.
\]
For any compact \(K\), strong convergence \(P_\varepsilon\to0\) and self-adjointness of the projections imply \(\|KP_\varepsilon\|=\|P_\varepsilon K^*\|\to0\), uniformly on the relatively compact image \(K^*(B_H)\). Consequently,
\[
\limsup_{\varepsilon\downarrow0}\|TP_\varepsilon\|
\le\|T-K\|+\lim_{\varepsilon\downarrow0}\|KP_\varepsilon\|
=\|T-K\|.
\]
Infimizing over compact \(K\) proves \(L(T)=\|T\|_{\mathrm{ess}}\), as claimed. The kernel identity is immediate because the compact operators form a norm-closed ideal.

**Step 5: existence versus separability.** An injective compact self-adjoint operator has dense range because \(\overline{\operatorname{ran}B}=(\ker B)^{\perp}=H\). The range of a compact operator is separable, so \(H\) must be separable. Conversely, on any separable infinite-dimensional \(H\) with orthonormal basis \((e_n)_{n\ge1}\), define
\[
Be_n=\frac1{n+1}e_n,\qquad Ge_n=\sqrt{1-\frac1{n+1}}\,e_n.
\]
Then \(B=I-G^*G\) is positive compact injective and \(\|G\|=1\), giving an explicit witness. This completes the proof.

## Verification

The argument is analytic. Its independently reproducible checks are: the spectral estimate \(B\ge\varepsilon Q_\varepsilon\); finite rank of \(Q_\varepsilon\) when \(B\) is compact; strong convergence \(P_\varepsilon\to0\) when \(\ker B=0\); and uniform convergence of strongly vanishing uniformly bounded projections on compact sets. The converse explicitly uses the two families of **test operators** \(Q_\varepsilon\) and \(R_x\), covering both compactness and injectivity. The diagonal construction supplies a direct instance. No finite test is invoked as an infinite-dimensional proof.

## Relationship to prior work

Dey and Pal introduced geometric results for the relative \(G\)-seminorm in arXiv:2603.20796v1 (first public submission March 21, 2026). Their Theorem 3.13 treats norm-attaining \(G\) and a spectral gap outside the norm-attainment space; their Theorem 3.14 compares different relative seminorms. Neither theorem identifies a relative seminorm with the **essential operator norm simultaneously for all bounded operators**. Indeed, in the present equality case \(G\) does not attain its norm, because \(\ker(I-G^*G)=0\).

The earlier work of Kadets, Martín, Merí, and Quero, *Generating operators between Banach spaces* (arXiv:2306.02645v1; 2024 journal edition), introduced and analyzed the same relative seminorm. Its generating-operator characterization concerns the opposite equality \(p_G(T)=\|T\|\) for all \(T\), not the quotient equality \(p_G(T)=\|T\|_{\mathrm{ess}}\). A full operator norm and an essential norm differ on every nonzero finite-rank operator. The elementary compact-approximation limit in Step 4 is classical; the structural if-and-only-if characterization of \(G\) is the asserted contribution.

## Limitations

The theorem concerns Hilbert domains and the universal identity for all bounded endomorphisms. It does not classify individual operators \(T\) for which the equality happens when the hypotheses on \(G\) fail, nor does it imply an analogous statement for general Banach spaces without orthogonal spectral projections. The proposed novelty is based on the inspected literature and searches, not a guarantee that no unindexed equivalent exists. No independent audit has been conducted.

## References

1. L. K. Dey and S. Pal, *On the geometry of G-norm*, arXiv:2603.20796v1, submitted March 21, 2026. https://arxiv.org/abs/2603.20796
2. V. Kadets, M. Martín, J. Merí, and A. Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1 (2023); *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 118 (2024), article 90. https://doi.org/10.1007/s13398-024-01582-3
3. C. R. Jayanarayanan and R. R. Rajpopat, *On Bhatia-Šemrl Property, Strong Subdifferentiability and Essential Norm of Operators on Banach Spaces*, arXiv:2512.15208 (2025), contextual comparison of essential versus full operator norm.
