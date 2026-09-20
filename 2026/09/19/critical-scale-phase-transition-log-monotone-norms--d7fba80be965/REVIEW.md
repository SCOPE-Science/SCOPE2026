# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument was checked at the level of the defining moment functionals and does not rely on numerical evidence.

The extension from Huang's power-law choice to an arbitrary sequence \(p_n=1-\delta_n\uparrow1\) uses only estimates already valid for every \(0<p_n<1\): Jensen's inequality, the quasi-triangle estimate with factor \(2^{1/p_n-1}\to1\), and the power-integral consequence of logarithmic submajorization. For bounded finite-support functions,
\[
d_nA_n^\delta(h)
\le
\frac{B S^{1/p_n}}{1+L_n}
e^{-L_n\delta_n/p_n},
\]
so vanishing does not require \(\delta_n\) to be a power of \(r_n\).

The key positive-regime estimate is two-sided. Writing
\[
m_n=T_n^{-1}K_{T_n}(h),\qquad
b_n=(1+L_n)^{-1}K_{T_n}(h),
\]
Jensen gives \(d_nA_n^\delta(h)\le b_n\). Since every \(h\in M_\psi\) is bounded, with \(B=\|h\|_\infty\),
\[
A_n^\delta(h)\ge
m_n\left(\frac{m_n}{B}\right)^{\delta_n/p_n}.
\]
Along any subsequence on which \(b_n\) stays bounded below,
\[
\log(B/m_n)\le L_n-\log(1+L_n)+O(1).
\]
Thus \(L_n\delta_n\to0\) forces the correction factor to \(1\), proving
\[
\Phi_\delta(h)=
\limsup_n \frac{K_{T_n}(h)}{1+L_n}
\]
for every \(h\), not just for test functions. The right-hand side is manifestly monotone under Hardy--Littlewood submajorization, so the full-symmetry conclusions follow.

For the extremal pair, the lower bound on the last block of \(g\) is
\[
d_nA_n^\delta(g)
\ge
\frac{r_n}{1+L_n}(1-e^{-r_n})^{\delta_n/p_n}\to1,
\]
while Jensen gives the matching upper bound. For \(f\), the exact identity
\[
d_nA_n^\delta(f)
=
\frac{e^{-q_n/p_n}}{1+L_n}
\left(1+\frac{e^{q_n}-1}{\delta_n}\right)^{1/p_n},
\qquad q_n=L_n\delta_n,
\]
gives \(F(c)=(1-e^{-c})/c\) for finite positive \(c\), \(F(0)=1\), and \(F(\infty)=0\). The limiting manipulations were checked for the endpoint regimes: \(\delta_n\log(1/\delta_n)\to0\), and \(r_n/L_n\to1\) converts Huang's power family into the stated \(\alpha\)-trichotomy.

No complementability, compactness, duality, or inheritance assertion is used.

## Originality

**PASS, to the best of our knowledge.** Huang's arXiv:2609.20270v1 was inspected at the definition of the Marcinkiewicz space, the construction of \(p_n,A_n,\Phi,N_\lambda,X\), Proposition 3.1, the \(\alpha=1\) computation, and the \(\alpha=\tfrac12\) computation. The paper explicitly fixes \(0<\alpha\le1\) and treats the two special choices \(\alpha=1\) and \(\alpha=\tfrac12\); it does not state an arbitrary-\(\delta_n\) formulation, a criterion in terms of \(L_n(1-p_n)\), the response curve \(F(c)\), or the fully symmetric phase \(\alpha>1\).

Targeted searches for the exact source identifier and title, logarithmically monotone Marcinkiewicz norms, Hardy--Littlewood solidity, asymptotic Marcinkiewicz seminorms, the scale \(L_n(1-p_n)\), and the response \((1-e^{-c})/c\) did not locate an equivalent phase-transition theorem.

The closest older background found was the theory of logarithmic submajorization and the literature on asymptotic/singular functionals in Marcinkiewicz ideals, including Dodds--Dodds--Sukochev--Zanin (2020) and Carey--Rennie--Sedaev--Sukochev (2007). Their available abstracts and public preprints concern the general order structure, determinant inequalities, Dixmier traces, and zeta asymptotics; no concrete statement matching this renorming transition was located. These sources were not exhaustively checked theorem-by-theorem for every possible reformulation, which remains a bibliographic risk. No inaccessible paper was identified as a concrete near-match whose unavailable statement gives positive evidence of coverage.

The originality claim is therefore limited to the critical-scale theorem, the exact response curve within Huang's construction, and the fully symmetric re-entry. Standard Marcinkiewicz-space facts, logarithmic submajorization, Jensen estimates, and the underlying functions \(f,g\) are prior art.

## Value

**PASS.** The result converts two apparently separate parameter choices in the source paper into a single sharp mechanism. The dimensionless quantity
\[
L_n(1-p_n)
\]
completely distinguishes a fully symmetric regime, a finite critical regime with an explicit strong-symmetry defect, and a supercritical regime in which the kernel itself loses Hardy--Littlewood solidity. In the original power family this identifies \(\alpha=1\) as the exact boundary and supplies a positive theorem for the previously untreated range \(\alpha>1\), rather than merely adding another negative example.

The proof also identifies the limiting object in the positive phase:
\[
\Theta(h)=\limsup_n K_{T_n}(h)/(1+L_n),
\]
which makes the restoration of full symmetry transparent and gives a reusable criterion for related sparse-moment constructions.

## Limitations

The result is tied to the rapidly separated scales \(L_n,T_n\) in Huang's construction. It does not classify arbitrary sampling sequences, does not settle the kernel \(X_\delta\) in the finite nonzero critical regime, and does not address oscillatory \(L_n\delta_n\) beyond the stated limits. No noncommutative extension is claimed.
