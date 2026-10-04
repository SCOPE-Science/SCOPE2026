# Exact synthesis-range replacement for Lipschitz \(p\)-approximate Schauder frames
## Finding
Let \(1\le p<\infty\), let \(X\) be a real or complex Banach space, and let \(M\subset X\) be nonempty. For every Lipschitz \(p\)-approximate Schauder frame \((\{f_n\},\{\tau_n\})\) for \(M\) in the sense of Krishna--Johnson, its synthesis operator \(\theta_\tau:\ell^p\to X\) always satisfies \[\operatorname{span}(M)\subseteq\operatorname{Ran}(\theta_\tau)\subseteq\overline{\operatorname{span}}(M),\] and hence \(\overline{\operatorname{Ran}(\theta_\tau)}=\overline{\operatorname{span}}(M)\). Surjectivity onto the ambient \(X\) is therefore not automatic. In particular, if \(\dim X>1\) and \(0\ne u\in X\), the singleton \(M=\{u\}\) admits a Lipschitz \(1\)-Schauder frame whose synthesis range is exactly \(\operatorname{span}\{u\}\ne X\). This is a counterexample to the synthesis-surjectivity assertion in Theorem 2.5(iv) of arXiv:2211.10652v1, retained as Theorem 2.1(iv) in the published article; the displayed range sandwich is the valid universal replacement.

The replacement is sharp at the level of universal conclusions: the definition forces every point of \(M\) into the synthesis range, while the requirement \(\tau_n\in M\) forces every synthesized vector into the closed linear span of \(M\). Neither inclusion can in general be upgraded to equality with the ambient space.

## Assumptions and scope
Use Definition 2.1 of Krishna--Johnson. Thus \(M\) is a nonempty subset of a Banach space \(X\), \(1\le p<\infty\), \(\theta_f:M\to\ell^p\) is Lipschitz, \(\theta_\tau:\ell^p\to X\) is bounded linear with \(\tau_n=\theta_\tau e_n\in M\), and the frame map \(S=\theta_\tau\theta_f:M\to M\) is invertible bi-Lipschitz with the stated reconstruction formula.

No assumption that \(M=X\), that \(M\) spans \(X\), or that \(\operatorname{Ran}(\theta_\tau)\) is closed is added.

## Proof
For every \(x\in M\), the reconstruction identity gives
\[
x=\sum_{n=1}^{\infty}(f_nS^{-1})(x)\tau_n
 =\theta_\tau\bigl(\theta_f(S^{-1}x)\bigr).
\]
Hence \(M\subseteq\operatorname{Ran}(\theta_\tau)\). The range of a linear operator is a linear subspace, so
\[
\operatorname{span}(M)\subseteq\operatorname{Ran}(\theta_\tau).
\]

Conversely, take \(a=(a_n)\in\ell^p\). Since \(p<\infty\), its coordinate truncations converge to \(a\) in \(\ell^p\). Boundedness of \(\theta_\tau\) therefore gives
\[
\theta_\tau(a)=\lim_{N\to\infty}\sum_{n=1}^{N}a_n\tau_n.
\]
Every partial sum lies in \(\operatorname{span}(M)\), because every \(\tau_n\in M\). Thus
\[
\operatorname{Ran}(\theta_\tau)\subseteq\overline{\operatorname{span}}(M).
\]
Taking closures of the two inclusions yields
\[
\overline{\operatorname{Ran}(\theta_\tau)}=\overline{\operatorname{span}}(M).
\]

For the counterexample, let \(X\) have dimension greater than one and choose \(0\ne u\in X\). Put \(M=\{u\}\), \(p=1\), and \(\tau_n=u\) for all \(n\). Define \(f_1(u)=1\) and \(f_n(u)=0\) for \(n\ge2\). The analysis map sends the only point to \(e_1\) and is Lipschitz. The synthesis operator is
\[
\theta_\tau(a)=\left(\sum_{n=1}^{\infty}a_n\right)u,
\]
which is bounded because \(\|\theta_\tau(a)\|\le\|u\|\|a\|_1\). The frame map satisfies \(S(u)=u\), so this is a Lipschitz \(1\)-Schauder frame. Yet
\[
\operatorname{Ran}(\theta_\tau)=\operatorname{span}\{u\}\ne X.
\]
Therefore synthesis surjectivity onto arbitrary ambient \(X\) does not follow from Definition 2.1.

## Verification
The proof uses only the reconstruction identity, linearity and boundedness of the synthesis operator, membership \(\tau_n\in M\), and norm convergence of coordinate truncations in \(\ell^p\) for finite \(p\). The singleton construction checks every clause of the definition directly and gives an explicit proper synthesis range whenever \(\dim X>1\).

The primary arXiv text was inspected at Definition 2.1, Theorem 2.5(iv), Theorem 2.6, and Problem 3.1. The 2026 journal version was separately inspected and retains the same surjectivity assertion as Theorem 2.1(iv). No erratum or corrected statement was located in the checked sources.

## Relationship to prior work
Krishna--Johnson's Definition 2.1 explicitly allows \(M\) to be an arbitrary subset of \(X\). Their Theorem 2.5(iv) in arXiv:2211.10652v1 states that the synthesis operator is surjective; the published Kragujevac Journal of Mathematics version retains this as Theorem 2.1(iv). The singleton frame above satisfies the definition but has one-dimensional synthesis range in any higher-dimensional ambient space, so the published assertion cannot hold without an additional spanning/range hypothesis.

The paper's factorization characterization itself only requires a bounded operator \(V:\ell^p\to X\) with \(V U(M)\subseteq M\) and \(V e_n\in M\); those conditions are compatible with a proper range. The range sandwich proved here is therefore the direct universal statement supported by the definition.

## Limitations
This finding corrects only the synthesis-range conclusion. It does not reassess other theorems in the paper or determine which later statements depend on surjectivity. The equality obtained is equality of closures in general; the synthesis range need not be closed. Surjectivity does follow under stronger hypotheses, for example if the algebraic span of \(M\) already equals \(X\), because then \(X=\operatorname{span}(M)\subseteq\operatorname{Ran}(\theta_\tau)\).

A residual literature risk is an erratum, note, or informal correction not indexed by the searches performed.

## References
1. K. Mahesh Krishna and P. Sam Johnson, *Lipschitz p-Approximate Schauder Frames*, arXiv:2211.10652v1, first public 2022-11-19; Definition 2.1 and Theorem 2.5(iv).
2. K. Mahesh Krishna and P. Sam Johnson, *Lipschitz p-Approximate Schauder Frames*, Kragujevac Journal of Mathematics 50(2) (2026), DOI 10.46793/KgJMat2602.217K; Theorem 2.1(iv).
