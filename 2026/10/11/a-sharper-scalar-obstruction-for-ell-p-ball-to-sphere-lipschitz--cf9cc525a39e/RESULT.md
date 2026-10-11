# A sharper scalar obstruction for \(\ell_p\) ball-to-sphere Lipschitz retractions
## Finding
Let \(1<p\le 2\), and let \(k_0(\ell_p)\) denote the infimum of the Lipschitz constants of retractions from the closed unit ball of \(\ell_p\) onto its unit sphere. Every \(K\)-Lipschitz retraction satisfies \(K\ge3\). Put \(a=2^{1/p}/K\). Then every such retraction also satisfies
\[
a\le (1-a^p)^{1/p}-\frac1K\bigl(1-a^p+(1-a)^p\bigr)^{1/p}.
\]
Equivalently,
\[
\frac{2^{1/p}}K\le\left(1-\frac2{K^p}\right)^{1/p}-\frac1K\left(1-\frac2{K^p}+\left(1-\frac{2^{1/p}}K\right)^p\right)^{1/p}.
\]
If \(\Lambda_p\) is the infimum of the numbers \(K\ge3\) satisfying the displayed scalar inequality, then \(k_0(\ell_p)\ge\Lambda_p\).

## Assumptions and scope
The space is real \(\ell_p\) with \(1<p\le2\). A retraction \(R:B_{\ell_p}\to S_{\ell_p}\) means \(R(x)=x\) for every \(x\in S_{\ell_p}\). Its Lipschitz constant is \(K\). The universal lower bound \(K\ge3\) is classical and is used only to prove monotonicity of a one-variable function below.

The focal source, Mahesh, arXiv:2609.13342v1, derives before its final simplification the following inequality. For every sufficiently small \(\varepsilon>0\), there is \(r_\varepsilon\in[0,1]\) such that
\[
r_\varepsilon\ge\frac{\eta_\varepsilon}{K},\qquad
\frac{\eta_\varepsilon}{K}\le F_{p,K}(r_\varepsilon),
\]
where
\[
\eta_\varepsilon=\bigl((1-\varepsilon)+(1-\varepsilon^{1/p})^p\bigr)^{1/p},
\]
and
\[
F_{p,K}(r)=(1-r^p)^{1/p}-\frac1K\bigl(1-r^p+(1-r)^p\bigr)^{1/p}.
\]
The new step is to retain this exact expression and prove that it is decreasing on the entire interval forced by the construction.

## Proof
Take a sequence \(\varepsilon_j\downarrow0\). Passing to a subsequence, assume \(r_{\varepsilon_j}\to r\in[0,1]\). Since \(\eta_{\varepsilon_j}\to2^{1/p}\), the source inequalities give
\[
r\ge a:=\frac{2^{1/p}}K,
\qquad
a\le F_{p,K}(r).
\]
The latter inequality forces \(r<1\), since \(F_{p,K}(1)=0<a\).

It remains to show that \(F_{p,K}\) is nonincreasing on \([a,1)\). Write
\[
u(r)=(1-r^p)^{1/p},\qquad
v(r)=\bigl(1-r^p+(1-r)^p\bigr)^{1/p}.
\]
For \(0<r<1\),
\[
F_{p,K}'(r)=-A(r)+\frac1K B(r),
\]
where
\[
A(r)=\frac{r^{p-1}}{u(r)^{p-1}},\qquad
B(r)=\frac{r^{p-1}+(1-r)^{p-1}}{v(r)^{p-1}}.
\]
Because \(v(r)\ge u(r)\),
\[
\frac{B(r)}{A(r)}
=\left(1+\left(\frac{1-r}r\right)^{p-1}\right)
\left(\frac{u(r)}{v(r)}\right)^{p-1}
\le 1+\left(\frac{1-r}r\right)^{p-1}.
\]
For \(r\ge a\), set \(t=K/2^{1/p}-1\). Then \(0\le(1-r)/r\le t\). If \(t\le1\), then \(1+t^{p-1}\le2\le K\). If \(t\ge1\), the hypothesis \(p-1\le1\) gives \(t^{p-1}\le t\), hence
\[
1+t^{p-1}\le1+t=\frac K{2^{1/p}}<K.
\]
Thus \(B(r)/A(r)\le K\), so \(F_{p,K}'(r)\le0\) on \([a,1)\). Consequently
\[
a\le F_{p,K}(r)\le F_{p,K}(a),
\]
which is exactly the asserted scalar obstruction.

Finally, the scalar inequality retained here is strictly stronger than the last scalar inequality used in the focal source. Indeed, for \(0<a<1\),
\[
\bigl(1-a^p+(1-a)^p\bigr)^{1/p}>(1-a^p)^{1/p},
\]
so subtracting the former quantity divided by \(K\) gives a strictly smaller right-hand side than replacing it by the latter.

## Verification
The proof uses the exact pre-simplification inequality already established in the focal source and then only differentiation, compactness of \([0,1]\), and elementary monotonic estimates. No finite experiment or numerical root computation is used as proof. The endpoint \(p=2\) is included; the argument does not claim that this method attains the best known Hilbert-space lower bound. No claim is made for \(p>2\), where the estimate \(t^{p-1}\le t\) used above can fail.

## Relationship to prior work
Mahesh, arXiv:2609.13342v1, studies lower bounds for \(k_0(\ell_p)\). In the proof of its main lower-bound theorem, it obtains the exact two-radical expression used here but then upper-bounds the bracket by a simpler factor, producing a weaker scalar obstruction. The present result identifies a monotonicity regime \(1<p\le2\) in which that discarded term can be retained all the way to a closed scalar necessary condition.

Goebel's 2003 paper gives general lower-bound machinery for retractions of balls onto spheres and records the universal bound \(k_0(X)\ge3\), but does not give this \(p\)-specific retained-term obstruction. Benyamini--Sternfeld establishes existence of Lipschitz retractions in infinite-dimensional normed spaces rather than the present sharp lower-bound refinement.

## Limitations
The result is a necessary scalar obstruction, not an exact evaluation of \(k_0(\ell_p)\). It is tied to the specific witness construction in the focal source, and no claim is made that \(\Lambda_p\) is optimal. The proof is restricted to \(1<p\le2\). The literature search found no implication-equivalent statement, but an older equivalent reformulation under minimal-displacement terminology remains a residual originality risk.

## References
1. S. Mahesh, “Improved Bounds For The Lipschitz Retraction Constant In Classical Banach Spaces,” arXiv:2609.13342v1, first public 2026-09-11.
2. K. Goebel, “On the problem of retracting balls onto their boundary,” Abstract and Applied Analysis 2003 (2003), 101–110, DOI 10.1155/S1085337503204103.
3. Y. Benyamini and Y. Sternfeld, “Spheres in infinite-dimensional normed spaces are Lipschitz contractible,” Proceedings of the American Mathematical Society 88 (1983), 439–445, DOI 10.1090/S0002-9939-1983-0699410-7.
