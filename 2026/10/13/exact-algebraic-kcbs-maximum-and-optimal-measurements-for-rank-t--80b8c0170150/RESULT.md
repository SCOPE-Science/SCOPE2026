# Exact algebraic KCBS maximum and optimal measurements for rank-two qutrit states

## Finding

Let \(\rho\) be any density matrix on \(\mathbb C^3\) with ordered eigenvalues \((a,b,0)\), where \(a\ge b\ge0\) and \(a+b=1\). Let \(P_1,\ldots,P_5\) be rank-one orthogonal projectors satisfying the pentagon adjacency conditions \(P_jP_{j+1}=0\) (indices modulo five), and define
\[
\mathcal K(\rho)=\max_{P_jP_{j+1}=0}\operatorname{Tr}\!\left(\rho\sum_{j=1}^{5}P_j\right).
\]
Put
\[
D(z)=\frac{(z-1)(5-z^2)}{3-z},\qquad N(z)=z^3-5z^2+3z+5.
\]
For \(0<b<a\), define \(q=b/(2a-b)\in(0,1)\). There is **exactly one** root \(z_*\in(2,\sqrt5)\) of the algebraic equation
\[
q^2N(z)^2=(z-1)(5-z^2)(3-z)^3,
\]
and the unrestricted (over all admissible pentagon projectors) maximum is
\[
\boxed{\mathcal K(\rho)=az_*+\frac b2\left(5-z_*+\sqrt{D(z_*)}\right).}
\]
The endpoint values are \(\mathcal K(\rho)=\sqrt5\) when \(b=0\), and \(\mathcal K(\rho)=2\) when \(a=b=1/2\). Thus \(z_*\) is a uniquely specified algebraic number, not an unresolved numerical maximization.

For the linear entropy \(s=\frac32(1-\operatorname{Tr}\rho^2)\in[0,3/4]\), set \(u=\sqrt{1-4s/3}\), \(a=(1+u)/2\), and \(b=(1-u)/2\). For the interior \(0<s<3/4\), the root parameter is \(q=(1-u)/(1+3u)\). The boxed expression therefore provides the entire rank-two boundary left without an analytic expression as curve AC in Xu–Su–Chen (2015).

## Assumptions and scope

The five measurements are arbitrary **complex** rank-one projectors on a qutrit, subject only to the cyclic adjacency orthogonality conditions. The state has rank at most two, with the eigenvalues and ordering above. Allowing coincident nonadjacent projectors at the endpoint is essential for the closed admissible domain; all interior optima admit nondegenerate pentagons. The result concerns the KCBS probability-sum functional, whose noncontextual bound is two, not the nine-projector KK inequality.

## Proof

**Step 1: spectral reduction.** For a fixed pentagon let \(M=\sum_jP_j\), with decreasing eigenvalues \(m_1\ge m_2\ge m_3\). Von Neumann's trace inequality gives \(\operatorname{Tr}(\rho M)\le am_1+bm_2\). Equality is attained by conjugating all five projectors with a common unitary aligning eigenvectors with those of \(\rho\).

The spectral geometry of qutrit pentagrams was established by Badziąg–Bengtsson–Cabello–Granström–Larsson (2009): writing \(r=2-A\) in their Eqs. (7)–(11), the spectral polynomial is
\[
\det(wI-M)=(w-1)(w-2)^2+r(w-3),\qquad 0\le r\le \frac{5\sqrt5-11}{2}.
\]
All these values are attainable, including by real symmetric pentagons. Their Eq. (19), and the later spectral treatment by Soeda and coauthors, already reduce the weighted mixed-state value to optimizing these eigenvalues; the contribution here is the explicit **solved global optimum** and constructive algebraic parameter selection for the complete rank-two family, not a new pentagram characteristic polynomial.

**Step 2: one-parameter eigenvalue curve.** Write \(z=m_1\). It ranges over \([2,\sqrt5]\); solving the characteristic polynomial for \(r\) yields
\[
r(z)=\frac{(z-1)(z-2)^2}{3-z}.
\]
The remaining roots sum to \(5-z\). Their discriminant, using their product \((4+3r(z))/z\), is exactly \(D(z)\). Hence
\[
m_2(z)=\frac{5-z+\sqrt{D(z)}}2,\qquad m_3(z)=\frac{5-z-\sqrt{D(z)}}2.
\]
The second-largest-eigenvalue identity holds throughout this interval, including its endpoints by continuity. Thus the entire optimization is that of \(f(z)=az+bm_2(z)\) on \([2,\sqrt5]\).

**Step 3: strict global optimality and root selection.** Direct differentiation gives
\[
D'(z)=\frac{2N(z)}{(z-3)^2},\qquad D''(z)=\frac{2(z-1)(z^2-8z+19)}{(z-3)^3}<0
\]
for \(2\le z<\sqrt5\): here \(z^2-8z+19=(z-4)^2+3>0\), while \(z-3<0\). Furthermore \(D(z)>0\) in the open interval. Thus \(\sqrt{D(z)}\) and \(f(z)\) are strictly concave whenever \(b>0\). At \(z=2\), \(D(2)=1\), \(D'(2)=-2\), and \(f'(2)=a-b\); as \(z\uparrow\sqrt5\), \(f'(z)\to-\infty\). If \(0<b<a\), there is a unique interior global maximizer satisfying
\[
0=f'(z)=a-\frac b2+\frac{bN(z)}{2(z-3)^2\sqrt{D(z)}}.
\]
Since \(D'(z)<0\) throughout the interval (by strict decrease from \(D'(2)=-2\)), the numerator \(N(z)<0\) there, so squaring this stationarity equation introduces **no extraneous root** within \((2,\sqrt5)\). Multiplication by the positive denominators yields exactly
\[
\left(\frac b{2a-b}\right)^2 N(z)^2=(z-1)(5-z^2)(3-z)^3.
\]
Strict concavity proves this degree-six equation has exactly one root in the specified open interval. When \(a=b\), the derivative begins at zero and decreases, giving the endpoint maximum \(f(2)=2\). When \(b=0\), \(f(z)=z\), maximized at \(\sqrt5\). This proves all cases, with no numerical assumption.

**Step 4: explicit optimal projectors.** Let \(\varphi=(1+\sqrt5)/2\). For the optimal spectral parameter \(z\) choose \(\xi\in[0,\varphi]\) solving
\[
\frac{\xi^2}{(1+\xi)^2(1+2\xi)}=r(z).
\]
The left side is continuous, strictly increasing on \([0,\varphi]\), with values \(0\) and \((5\sqrt5-11)/2\) at the endpoints. Hence \(\xi\) is uniquely determined. Put \(t=\sqrt\xi\) and take these five normalized real rays:
\[
\begin{aligned}
v_1&=(1,0,0),&v_2&=(0,1,0),&v_3&=(1,0,t)/\sqrt{1+t^2},\\
v_4&=(-t,-t,1)/\sqrt{1+2t^2},&v_5&=(0,1,t)/\sqrt{1+t^2}.
\end{aligned}
\]
Each successive pair is orthogonal, including the fifth and first. Direct expansion of \(\sum_jv_jv_j^{\mathsf T}\) gives trace five and characteristic polynomial \((w-1)(w-2)^2+[\xi^2/((1+\xi)^2(1+2\xi))](w-3)\). Consequently its ordered spectrum is precisely \((z,m_2(z),m_3(z))\). A common unitary aligning its eigenvectors with the ordered eigenvectors of \(\rho\) attains the global maximum. At equal top state eigenvalues, any corresponding rotation inside their eigenspace suffices.

## Verification

The accompanying `verify.py` checks the exact derivative identities, the exact characteristic polynomial of the explicit projector construction for five symbolic/rational/algebraic parameters, and seven independent numerical optimizations with separately diagonalized projectors. It prints `VERIFY_OK symbolic_spectral=passed exact_projectors=5 optimizer_cases=7` when these consistency checks succeed. The all-spectrum optimum and uniqueness are proved analytically above; sampled numerical cases are not substitutes for that proof. For example, at \((a,b)=(3/4,1/4)\), the unique root is approximately \(z_*=2.185716320127158\), yielding \(\mathcal K(\rho)\approx2.062246181255400\).

## Relationship to prior work

Badziąg and coauthors (2009) derive the complete pentagram operator's one-parameter spectrum and note the weighted expectation for spin-one pure states (their Eq. (19)); Soeda and coauthors (2012) restate the spectrum and eigenvalue-alignment optimization for biphoton contextuality (their Eqs. (12)–(14) and discussion). These spectral and reduction ingredients are **prior results**, not original here. Xu, Su and Chen (2015), in Eq. (1) and the paragraph preceding it, identify the rank-two maximal-contextuality curve AC but explicitly state that its analytic expression is missing. The new result resolves that specific maximization: an unambiguous sextic root, proof of unique global branch, boundary values, and a realizing pentagon for every rank-two state. No assertion of novelty is made for the earlier spectral curve or general trace inequality.

## Limitations

The formula covers only rank-at-most-two qutrit states and only the five-projector KCBS optimization. It does not give an analogous algebraic classification of the general full-rank qutrit simplex, the KK inequality, or uniqueness of the optimal projector configuration. A distinct prior derivation of the same selected-root formula under a different parametrization could exist despite targeted comparisons; the exact algebraic outcome remains subject to independent literature review. The characteristic polynomial of pentagram operators was already known in 2009.

## References

1. Z.-P. Xu, H.-Y. Su, J.-L. Chen, *Quantum contextuality of a qutrit state*, arXiv:1504.06942v1, 27 April 2015, Eq. (1) and Sec. II. https://arxiv.org/pdf/1504.06942
2. P. Badziąg, I. Bengtsson, A. Cabello, H. Granström, J.-Å. Larsson, *Pentagrams and Paradoxes*, arXiv:0909.4713v1 (2009), Eqs. (7)–(13), (19). https://arxiv.org/pdf/0909.4713
3. A. Soeda, P. Kurzyński, R. Ramanathan, K. Modi, D. Kaszlikowski, *The relation between nonlocality and contextuality for a biphoton*, arXiv:1207.1952 (2012), Eqs. (12)–(14) and following discussion. https://arxiv.org/pdf/1207.1952
