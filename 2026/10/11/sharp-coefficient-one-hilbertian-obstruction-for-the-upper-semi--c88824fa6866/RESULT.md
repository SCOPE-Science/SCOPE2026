# Sharp coefficient-one Hilbertian obstruction for the upper semi-Fredholm comparison constant
## Finding
Let \(X\) be a Banach space. For every complemented infinite-dimensional subspace \(H\subset X\) whose inherited norm is a multiple of a Hilbert norm, define
\[
\Gamma_X(H)=\inf_{H_0\in\mathcal S(H)}\lambda_X(H_0),
\]
where \(\lambda_X(H_0)\) is the relative projection constant, and put
\[
\Gamma_{\mathrm{Hilb}}(X)=\sup_H\Gamma_X(H).
\]
For the upper semi-Fredholm comparison invariant
\[
\Lambda_{\mathrm{SF}}(X)=\inf\{\lambda\ge1:d_+(T)\le\lambda\,\operatorname{in}(T)\text{ for every Banach }Y\text{ and }T\in\mathcal L(X,Y)\},
\]
one has the sharper Hilbertian obstruction
\[
\Lambda_{\mathrm{SF}}(X)\ge\Gamma_{\mathrm{Hilb}}(X).
\]
The universal coefficient \(1\) is best possible. This improves the coefficient \(1/2\) obtained by the fixed numerical choice in the motivating Hilbertian-obstruction theorem.

## Assumptions and scope
Here \(\mathcal S(H)\) denotes the closed infinite-dimensional subspaces of \(H\). The quantity \(d_+(T)\) is the distance from \(T\) to the complement of the upper semi-Fredholm operators, and
\[
\operatorname{in}(T)=\inf_{M\in\mathcal S(X)}\|T|_M\|.
\]
The focal source proves the exact infinite-kernel formula
\[
d_+(T)=\inf\{\|E\|:\dim\ker(T-E)=\infty\}.
\]
Every \(H_0\in\mathcal S(H)\) is one-complemented in \(H\), so if \(P:X\to H\) is any projection then an orthogonal projection on \(H\), composed with \(P\), shows \(\Gamma_X(H)<\infty\). The claim is only a lower bound produced by complemented Hilbertian witnesses; it does not identify \(\Lambda_{\mathrm{SF}}(X)\) for arbitrary \(X\).

## Proof
Fix such a subspace \(H\), write \(\Gamma=\Gamma_X(H)\), and suppose first that \(\Gamma>1\). Choose \(1\le c<\Gamma\), a projection \(P:X\to H\), and put \(Z=\ker P\). Choose
\[
0<\varepsilon<\min\left\{\frac{1}{c(1+c)},\frac{\Gamma-c}{c\bigl(\Gamma(1+c)-c\bigr)}\right\}.
\]
Define
\[
T_\varepsilon x=(\varepsilon Px,(I-P)x):X\longrightarrow H\oplus_\infty Z.
\]
This is an isomorphism. Since \(H\) is infinite-dimensional and \(\|T_\varepsilon|_H\|=\varepsilon\),
\[
\operatorname{in}(T_\varepsilon)\le\varepsilon.
\]

We show \(d_+(T_\varepsilon)\ge c\varepsilon\). Suppose instead that an operator \(F=(F_1,F_2):X\to H\oplus_\infty Z\) has
\[
s:=\|F\|<c\varepsilon
\]
and that \(M=\ker(T_\varepsilon-F)\) is infinite-dimensional. For \(x\in M\),
\[
F_1x=\varepsilon Px,\qquad F_2x=(I-P)x.
\]
Consequently
\[
\|(I-P)x\|\le s\|x\|,
\qquad
\|Px\|\ge(1-s)\|x\|.
\]
Thus \(H_0=P(M)\) is a closed infinite-dimensional subspace of \(H\), and the inverse
\[
J=(P|_M)^{-1}:H_0\to M
\]
satisfies \(\|J\|\le(1-s)^{-1}\). Write
\[
Jh=h+k(h),\qquad k(h)\in Z.
\]
Then
\[
\|k(h)\|\le\frac{s}{1-s}\|h\|.
\]
Let \(Q:H\to H_0\) be the orthogonal projection, which has norm \(1\). Since \(F_1Jh=\varepsilon h\),
\[
QF_1h-\varepsilon h=-QF_1k(h).
\]
Hence, for
\[
A=\varepsilon^{-1}QF_1|_{H_0},
\]
we have
\[
\|A-I_{H_0}\|\le\theta:=\frac{s^2}{\varepsilon(1-s)}.
\]
The choice \(s<c\varepsilon\) and \(\varepsilon<1/(c(1+c))\) gives \(\theta<1\), so \(A\) is invertible. Therefore
\[
R=A^{-1}\varepsilon^{-1}QF_1:X\to H_0
\]
is a projection onto \(H_0\), and
\[
\|R\|\le B_\varepsilon(s):=
\frac{s(1-s)}{\varepsilon(1-s)-s^2}.
\]
On the range where the denominator is positive,
\[
B_\varepsilon'(s)=
\frac{\varepsilon(1-s)^2+s^2}{\bigl(\varepsilon(1-s)-s^2\bigr)^2}>0.
\]
Thus
\[
\|R\|<B_\varepsilon(c\varepsilon)
=
\frac{c(1-c\varepsilon)}{1-c(1+c)\varepsilon}
<\Gamma,
\]
where the final strict inequality is exactly the second restriction on \(\varepsilon\). This contradicts \(\lambda_X(H_0)\ge\Gamma\). Hence no perturbation of norm below \(c\varepsilon\) can give \(T_\varepsilon-F\) an infinite-dimensional kernel. By the focal source's infinite-kernel formula,
\[
d_+(T_\varepsilon)\ge c\varepsilon.
\]
Together with \(\operatorname{in}(T_\varepsilon)\le\varepsilon\), this yields
\[
\frac{d_+(T_\varepsilon)}{\operatorname{in}(T_\varepsilon)}\ge c.
\]
Letting \(c\uparrow\Gamma\) proves \(\Lambda_{\mathrm{SF}}(X)\ge\Gamma_X(H)\); taking the supremum over \(H\) proves the theorem. If \(\Gamma_X(H)=1\), the same conclusion follows from the defining bound \(\Lambda_{\mathrm{SF}}(X)\ge1\). If the supremum over \(H\) is infinite, the finite-\(c\) argument gives arbitrarily large ratios.

Finally, if \(X\) is an infinite-dimensional Hilbert space, every closed subspace has projection constant \(1\), so \(\Gamma_{\mathrm{Hilb}}(X)=1\); the focal source proves \(d_+(T)=\operatorname{in}(T)\) for Hilbert domains, hence \(\Lambda_{\mathrm{SF}}(X)=1\). Therefore no universal coefficient larger than \(1\) can replace the one above.

## Verification
The proof uses only the focal source's exact infinite-kernel characterization of \(d_+\), elementary Hilbert projection geometry, and the displayed rational estimate. The derivative of \(B_\varepsilon\) was recomputed symbolically from its quotient formula; its numerator reduces to \(\varepsilon(1-s)^2+s^2\), which is positive. The two explicit restrictions on \(\varepsilon\) separately guarantee invertibility of \(A\) and the contradiction \(\|R\|<\Gamma\). No finite experiment or asymptotic extrapolation is used.

## Relationship to prior work
Azzouz proves the same Hilbertian-witness mechanism with one fixed numerical choice of \(\varepsilon\), obtaining
\[
\Lambda_{\mathrm{SF}}(X)\ge\frac12\sup_H\inf_{H_0\in\mathcal S(H)}\lambda_X(H_0).
\]
The present argument keeps the perturbation size symbolic and optimizes the projection estimate, replacing \(1/2\) by the universally sharp coefficient \(1\). The earlier operational-quantity papers of González and Martinón study semi-Fredholm quantities and perturbation radii, while Oikhberg and Spinu develop subprojectivity and uniform subprojectivity; the inspected material does not state this coefficient-one Hilbertian profile bound.

## Limitations
The result does not settle whether \(\Lambda_{\mathrm{SF}}(X)=\Lambda_{\mathrm{usp}}(X)\), nor whether finiteness of these two invariants is equivalent in complete generality. It also does not assert that the infimum defining \(\Gamma_X(H)\), the supremum defining \(\Gamma_{\mathrm{Hilb}}(X)\), or the ratio defining \(\Lambda_{\mathrm{SF}}(X)\) is attained. The originality comparison includes the focal full text and closely related subprojectivity literature, but an older equivalent formulation under different semi-Fredholm terminology remains a residual indexing risk.

## References
1. A. Azzouz, *The upper semi-Fredholm radius, extensions of restrictions, and subprojectivity*, arXiv:2610.03835v1 (2026).
2. M. González and A. Martinón, *Operational quantities characterizing semi-Fredholm operators*, Studia Mathematica 114 (1995), DOI:10.4064/sm-114-1-13-27.
3. M. González and A. Martinón, *Quantities characterizing semi-Fredholm operators and perturbation radii*, Journal of Mathematical Analysis and Applications 390 (2012), DOI:10.1016/j.jmaa.2012.01.048.
4. T. Oikhberg and E. Spinu, *Subprojective Banach spaces*, Journal of Mathematical Analysis and Applications 424 (2015), arXiv:1401.4231.
