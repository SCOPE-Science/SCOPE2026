# Exact two-spike rank-support law on arbitrary finite groups
## Finding
Let \(G\) be a finite group of order \(N\). For each irreducible unitary representation \(\rho\) of dimension \(d_\rho\), use the Fourier transform
\[
\widehat f(\rho)=\sum_{z\in G} f(z)\rho(z)^{*}
\]
and define the rank-weighted Fourier support
\[
\sigma(f)=\sum_{\rho\in\widehat G}d_\rho\,\operatorname{rank}\widehat f(\rho).
\]
For any two-point function \(f=a\delta_x+b\delta_y\), with \(x\ne y\) and \(ab\ne0\), set \(g=x^{-1}y\) and \(m=\operatorname{ord}(g)\). Then
\[
\sigma(f)=
\begin{cases}
N-N/m,&-a/b\in\mu_m,\\
N,&-a/b\notin\mu_m,
\end{cases}
\]
where \(\mu_m\) is the set of \(m\)-th roots of unity.

If \(p\) is the least prime divisor of \(N\), it follows that
\[
\min_{|\operatorname{supp}f|=2}\sigma(f)=N(1-1/p).
\]
The minimum occurs exactly when \(\operatorname{ord}(x^{-1}y)=p\) and \(-a/b\in\mu_p\). Therefore the rank-support uncertainty product on the exact two-point stratum has sharp value \(2-2/p\). In particular, equality in the global product lower bound \(1\) occurs for a two-point function exactly when the separation is an involution and \(b=\pm a\).

## Assumptions and scope
The group is finite and otherwise arbitrary; commutativity is not assumed. The support has exactly two distinct group elements, and both coefficients are nonzero. The Fourier-support quantity is the rank-weighted quantity used in the compact-group uncertainty principle, not the unweighted number of irreducible representations on which the transform is nonzero.

## Proof
Left translation and multiplication of every Fourier block by an invertible unitary matrix do not change ranks, so it is enough to consider \(f=a\delta_e+b\delta_g\). Up to an invertible unitary factor, each Fourier block is
\[
aI+b\rho(g)^{*}.
\]
Because \(g\) has order \(m\), every eigenvalue of \(\rho(g)^*\) is an \(m\)-th root of unity. Hence the block has no kernel unless \(\lambda=-a/b\in\mu_m\).

Assume now that \(\lambda\in\mu_m\). The loss of rank is
\[
L_\lambda=\sum_{\rho\in\widehat G}d_\rho\,\dim\ker(\rho(g)^*-\lambda I).
\]
Decompose the left regular representation as \(\bigoplus_\rho d_\rho\rho\). Restricted to the cyclic subgroup \(H=\langle g\rangle\), the same regular representation is a direct sum of \(N/m\) copies of the regular representation of \(H\), because the left cosets of \(H\) are invariant \(H\)-orbits. Each character of the cyclic group \(H\), equivalently each \(m\)-th root of unity as an eigenvalue of \(g\), therefore occurs exactly \(N/m\) times. Thus \(L_\lambda=N/m\), proving \(\sigma(f)=N-N/m\). If \(\lambda\notin\mu_m\), the loss is zero and \(\sigma(f)=N\).

For the global two-point minimum, resonant coefficients are always better than nonresonant ones, and \(N-N/m\) is minimized by the smallest possible order \(m>1\). By Cauchy's theorem, the least such order is the least prime divisor \(p\) of \(N\). This gives \(N(1-1/p)\) and the stated equality class. Finally \(2(N-N/m)/N=2-2/m\) equals \(1\) only when \(m=2\), and resonance at \(m=2\) is exactly \(-a/b\in\{1,-1\}\), equivalently \(b=\pm a\).

## Verification
The proof is exact and uses only finite-dimensional representation theory. As a corroborative check, `verify.py` constructs regular permutation matrices for several finite groups and confirms the predicted rank losses for all tested element orders and resonant coefficient phases. These finite tests are not used as a proof of the universal statement.

## Relationship to prior work
Kaniuth studies minimizers for a different nonabelian uncertainty principle based on the Plancherel measure of the set of nonzero Fourier blocks. Alagic and Russell introduce the sharper rank-weighted quantity \(\sum d_\rho\operatorname{rank}\widehat f(\rho)\) and prove the global product inequality, together with subgroup examples. The exact coefficient-sensitive rank-support law above resolves the first nontrivial sparse stratum for that sharper quantity. The inspected Alagic--Russell text states the global inequality and subgroup tightness examples but does not state a two-point formula or an order-of-separation classification.

## Limitations
The theorem does not classify support sizes three or larger, and it does not determine the unweighted representation-support count \(\sum_{\widehat f(\rho)\ne0}d_\rho^2\). The originality search cannot exclude an equivalent calculation hidden in older group-algebra or coding-theory terminology; this is retained as a residual literature risk.

## References
1. E. Kaniuth, “Minimizing Functions for an Uncertainty Principle on Locally Compact Groups of Bounded Representation Dimension,” ESI Preprint 1740, first public 2005-11-12; later Proc. Amer. Math. Soc. 135 (2007), 217–227. Primary MSC 43A30, 43A40.
2. G. Alagic and A. Russell, “Uncertainty Principles for Compact Groups,” arXiv:math/0608702, first public 2006-08-28; Illinois J. Math. 52 (2008). MSC 43A30, 43A65, 43A77.
