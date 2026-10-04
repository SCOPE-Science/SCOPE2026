# Zero Birkhoff saturation without an extremal pair in a reflexive strictly convex space
## Finding
For integers \(n\ge2\), put \(p_n=1+1/n\), and define
\[
X=\left(\bigoplus_{n=2}^{\infty}\ell_{p_n}^{2}\right)_{\ell_2}.
\]
Then \(X\) is separable, reflexive, and strictly convex. For every \(0\le\varepsilon<1\), its approximate Birkhoff--James James-type constant satisfies
\[
J_B^{\varepsilon}(X)=J(X)=2.
\]
Hence the Birkhoff saturation parameter introduced in arXiv:2609.37502v1 is \(\sigma_B(X)=0\). Despite this immediate saturation, the classical James supremum is not attained: there are no \(x,y\in S_X\) for which
\[
\min\{\|x+y\|,\|x-y\|\}=2.
\]
In particular, the finite-dimensional attained-max interpretation of the saturation threshold does not extend verbatim to infinite-dimensional spaces, even under reflexivity and strict convexity.

## Assumptions and scope
All spaces are real. For a normed space \(Y\), the James constant is
\[
J(Y)=\sup_{u,v\in S_Y}\min\{\|u+v\|,\|u-v\|\}.
\]
The quantity \(J_B^{\varepsilon}(Y)\) is the approximate Birkhoff--James profile from arXiv:2609.37502v1. Only two properties of that definition are used here: \(J_B^0(Y)\) restricts the supremum to Birkhoff--James-orthogonal pairs, and
\[
J_B^0(Y)\le J_B^{\varepsilon}(Y)\le J(Y)
\]
for \(0\le\varepsilon<1\). The saturation parameter \(\sigma_B(Y)\) is therefore zero whenever \(J_B^0(Y)=J(Y)\).

## Proof
Each exponent \(p_n\) lies in \((1,2)\). Thus every block \(E_n=\ell_{p_n}^{2}\) is finite dimensional and strictly convex. The countable \(\ell_2\)-sum \(X\) is separable and reflexive. It is also strictly convex: if \(x,y\in S_X\) and \(\|(x+y)/2\|=1\), equality must hold both in the scalar \(\ell_2\) Minkowski inequality for the coordinate norms and in the triangle inequality in each nonzero block. Equality in the outer \(\ell_2\) step forces matching coordinate norms, while strict convexity of every block forces matching coordinates; hence \(x=y\).

Fix \(n\ge2\). In the \(n\)-th block let \(e_1=(1,0)\) and \(e_2=(0,1)\). They are exactly Birkhoff--James orthogonal because for every real \(\lambda\),
\[
\|e_1+\lambda e_2\|_{p_n}=(1+|\lambda|^{p_n})^{1/p_n}\ge1=\|e_1\|_{p_n}.
\]
After embedding this pair in \(X\),
\[
\|e_1+e_2\|_X=\|e_1-e_2\|_X=2^{1/p_n}.
\]
Therefore
\[
J_B^0(X)\ge2^{1/p_n}\qquad(n\ge2).
\]
Since \(p_n\downarrow1\), the right-hand side tends to \(2\). Every James-type endpoint is bounded above by the triangle inequality, so \(J(X)\le2\). Consequently
\[
2\le J_B^0(X)\le J_B^{\varepsilon}(X)\le J(X)\le2,
\]
and hence all four quantities equal \(2\) for every \(0\le\varepsilon<1\). In particular \(\sigma_B(X)=0\).

It remains to prove nonattainment. Suppose unit vectors \(x,y\in X\) satisfied
\[
\min\{\|x+y\|,\|x-y\|\}=2.
\]
The triangle inequality gives both endpoint norms at most \(2\), so in fact
\[
\|x+y\|=\|x-y\|=2.
\]
Equality in \(\|x+y\|\le\|x\|+\|y\|\) in a strictly convex space forces \(x=y\), while equality in \(\|x-y\|\le\|x\|+\|y\|\) forces \(x=-y\). This is impossible for unit vectors. Thus \(J(X)=2\) is a nonattained supremum.

## Verification
The proof is symbolic and requires no finite enumeration or numerical extrapolation. The critical checks are: \(p_n>1\), so each block is strictly convex; exact Birkhoff--James orthogonality of the coordinate pair follows directly from its norm formula; \(2^{1/p_n}\to2\); and strict convexity rules out simultaneous equality in both triangle inequalities. Reflexivity follows from the standard duality of countable \(\ell_2\)-sums of reflexive spaces.

## Relationship to prior work
Fang, Xu, Liu, Gu, and Li introduce the approximate Birkhoff--James profile and its saturation parameter in arXiv:2609.37502v1. Their finite-dimensional formula expresses the saturation parameter through an attained maximum over James-extremal pairs, while their examples compute the profile on the classical spaces \(\ell_p\) and \(\ell_p^n\). The construction above uses those exact finite-dimensional coordinate witnesses as an asymptotic sequence but produces a reflexive strictly convex infinite-dimensional space where the limiting James value is never attained. Thus it isolates an infinite-dimensional boundary of the finite-dimensional witness formula rather than changing the underlying definition.

Baronti and Papini introduced the orthogonal James constant that forms the exact-orthogonality endpoint of the newer profile. Their work supplies background for the parameter but does not state the saturation/nonattainment phenomenon above.

## Limitations
The result gives one explicit reflexive strictly convex example. It does not classify when zero saturation is attained by an extremal pair, nor does it determine whether stronger geometric hypotheses such as uniform convexity force a positive saturation threshold or an attained witness. The originality comparison is statement-level and source-based; an equivalent construction could conceivably exist under older terminology about nonattainment of the James constant, but no checked source supplied the conjunction with the 2026 Birkhoff saturation parameter.

## References
1. Z. Fang, Y. Xu, Q. Liu, Z. Gu, and Y. Li, “James-type constants for Birkhoff--James orthogonality and approximate isosceles,” arXiv:2609.37502v1, first submitted 2026-09-26, https://arxiv.org/abs/2609.37502.
2. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” Constructive Mathematical Analysis 5 (2022), no. 1, 37--45, DOI:10.33205/cma.1067323.
