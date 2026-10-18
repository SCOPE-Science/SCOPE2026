# Exact Hilbert series of symmetric tensors on split elliptic ruled surfaces

## Finding

Let \(E\) be a complex elliptic curve, \(L\) a line bundle on \(E\) of degree \(-d\) with integer \(d\geq1\), and \(f:M=\mathbb P_E(\mathcal O_E\oplus L)\to E\) the ruled surface in the quotient-line convention. For every integer \(m\geq0\),
\[
\dim_{\mathbb C} H^0(M,\operatorname{Sym}^m T_M)=1+d\binom{m+2}{3},
\]
where the binomial coefficient is zero when \(m=0\). Hence its symmetric-tensor section algebra has Hilbert series
\[
\sum_{m\geq0}\dim H^0(M,\operatorname{Sym}^m T_M)t^m
=\frac1{1-t}+\frac{dt}{(1-t)^4}.
\]
Despite this rational Hilbert series, the algebra is **not finitely generated**, as established by Denisi and Höring. A more precise structural result is the direct-image decomposition below.

## Assumptions and scope

All varieties and vector bundles are over \(\mathbb C\). Denote by \(C_-\) the section with self-intersection \(-d\), by \(C_+\) the disjoint section with self-intersection \(d\), and put \(N=L^*\). Let \(\mathcal F\) be the elementary transformation constructed by Denisi and Höring, characterized by an exact sequence
\[
0\to\mathcal O_M(C_+)\to\mathcal F\to\mathcal O_M\to0,
\]
whose restriction to \(C_-\simeq E\) is the nontrivial extension \(\mathcal F_2\) of \(\mathcal O_E\) by \(\mathcal O_E\). For each integer \(r\geq1\), let \(\mathcal F_r\) denote Atiyah's unipotent indecomposable rank-\(r\), degree-zero bundle on \(E\), with \(\mathcal F_1=\mathcal O_E\). The complete stronger conclusion is
\[
\boxed{f_*\operatorname{Sym}^m\mathcal F\cong
\bigoplus_{j=0}^{m} N^{\otimes j}\otimes\mathcal F_{m-j+1},\qquad
R^1 f_*\operatorname{Sym}^m\mathcal F=0.}
\]
The displayed decomposition is an isomorphism of vector bundles, not an assertion about the multiplication of all graded pieces.

## Proof

**1. The extension is pulled from the elliptic base.** The two disjoint sections satisfy \(\mathcal O_M(C_+)\cong\mathcal O_M(C_-)\otimes f^*N\). The projection formula and the projective-bundle formula give
\[
f_*\mathcal O_M(C_+)\cong\mathcal O_E\oplus N,\qquad
R^1f_*\mathcal O_M(C_+)=0.
\]
The section \(\sigma\) defining \(C_+\) spans the \(\mathcal O_E\) summand: this follows because it restricts to a nowhere-vanishing section on the disjoint \(C_-\), whereas \(N\) is the kernel of that restriction map. Since \(\deg N=d>0\),
\[
H^1(M,\mathcal O_M(C_+))\cong H^1(E,\mathcal O_E)\cong\mathbb C.
\]
The extension class of \(\mathcal F\) is nonzero: its restriction to \(C_-\) is Atiyah's nonsplit bundle \(\mathcal F_2\). Therefore, after rescaling the quotient, \(\mathcal F\) is the pushout along \(\mathcal O_M\xrightarrow{\sigma}\mathcal O_M(C_+)\) of the pullback of the unique nonsplit extension \(0\to\mathcal O_E\to\mathcal F_2\to\mathcal O_E\to0\).

**2. The direct-image decomposition.** Choose local trivializations over an open cover of \(E\) for the preceding extension and the splitting \(f_*\mathcal O_M(C_+)\cong\mathcal O_E\oplus N\). Write \(a\) for the fiberwise section \(\sigma\), \(b\) for a local lift of the quotient \(\mathcal O_M\), and \(z\) for the fiberwise section belonging to \(N\). On overlaps, the nontrivial extension changes the lift by
\[
b\longmapsto b+c_{ij}a,
\]
where \((c_{ij})\) represents a nonzero class in \(H^1(E,\mathcal O_E)\); the \(z\) coordinate changes only by the transition of \(N\), and \(a\) is invariant. On each ruling fiber, \(\mathcal F|_{\mathbb P^1}\cong\mathcal O_{\mathbb P^1}(1)\oplus\mathcal O_{\mathbb P^1}\); therefore \(R^1f_*\operatorname{Sym}^m\mathcal F=0\), and its direct image has a local basis of the homogeneous monomials \(z^j a^i b^{m-j-i}\) for \(0\leq j\leq m\), \(0\leq i\leq m-j\). (The monomials here describe sections on a fiber, not free polynomial generators of a global algebra.)

The transition maps preserve each exponent \(j\). For fixed \(j\), the span of the \(m-j+1\) monomials \(a^i b^{m-j-i}\) transforms by the symmetric power of the nonsplit rank-two unipotent extension. In characteristic zero, this is the single unipotent Jordan block of rank \(m-j+1\): the infinitesimal action \(a\partial_b\) has one Jordan chain. Hence this block is \(\mathcal F_{m-j+1}\); accounting for \(z^j\) gives the claimed \(N^{\otimes j}\)-twist. Distinct \(j\) do not mix, so this is a *direct sum*, not just a filtration.

**3. Cohomology and the Hilbert series.** Atiyah's unipotent bundle \(\mathcal F_r\) has precisely one global section. For \(j\geq1\), \(N^{\otimes j}\otimes\mathcal F_r\) is semistable of positive degree \(rjd\) on an elliptic curve; Serre duality and semistability give \(H^1=0\), so Riemann–Roch gives
\[
h^0(E,N^{\otimes j}\otimes\mathcal F_r)=rjd.
\]
Consequently
\[
\begin{aligned}
h^0(M,\operatorname{Sym}^m\mathcal F)
&=1+d\sum_{j=1}^{m}j(m-j+1)\\
&=1+d\binom{m+2}{3}.
\end{aligned}
\]
Denisi and Höring establish an isomorphism of graded section rings \(R(M,T_M)\cong R(M,\mathcal F)\), by an elementary transform and the divisorial Zariski decomposition (their equation (10)). In particular, each homogeneous degree has the same dimension, proving the first formula. Finally \(\sum_{m\geq0}\binom{m+2}{3}t^m=t/(1-t)^4\), proving the Hilbert series.

## Verification

The standalone script `verify_sym_tensor.py` checks the finite-difference/binomial identity for \(0\leq m\leq24\) and \(1\leq d\leq8\), verifies the expected first Hilbert coefficients, and checks that the translation action \(b\mapsto b+a\) on degree-\(n\) binary forms gives one unipotent Jordan block for \(0\leq n\leq9\). These are reproducible algebraic consistency checks; the all-degree direct-image decomposition and Hilbert formula follow from the written proof rather than from finite testing.

## Relationship to prior work

Denisi and Höring (arXiv:2610.03048v1, October 2, 2026, Section 3, especially Proposition 3.5 and equation (10)) construct \(\mathcal F\), prove its restriction to \(C_-\) is the nonsplit Serre bundle, and prove non-finite generation of \(R(M,T_M)\). Their paper provides the principal structural input, but does not state the direct-image decomposition or the numerical all-degree Hilbert series derived here. Beauville and Liu study symmetric-tensor algebras and ruled surfaces over curves of genus at least two; that setting does not supply the elliptic unipotent decomposition. The Atiyah classification provides the standard description and cohomology of unipotent bundles. The calculation is therefore a refinement of the explicit split-elliptic case, not a new non-finite-generation theorem.

## Limitations

No description of minimal graded generators or of the non-Noetherian multiplication relations is claimed. The statement is restricted to **split** ruled surfaces over complex elliptic curves with \(\deg L<0\). It does not cover indecomposable ruled surfaces, arbitrary genus, positive characteristic, nor general canonical extensions. The decomposition depends on the fixed split structure and does not assert a canonical functorial decomposition without those choices. Publication priority beyond the specifically examined sources has not been independently certified.

## References

1. F. A. Denisi and A. Höring, *Canonical extensions of ruled surfaces over elliptic curves*, arXiv:2610.03048v1 (first public October 2, 2026), Section 3, especially equations (7), (10), Proposition 3.5 and Theorem 1.4.
2. A. Beauville and J. Liu, *The algebra of symmetric tensors on smooth projective varieties*, arXiv:2309.12888 (first public September 22, 2023).
3. M. F. Atiyah, *Vector bundles over an elliptic curve*, Proc. London Math. Soc. (3) 7 (1957), 414–452. DOI:10.1112/plms/s3-7.1.414.
