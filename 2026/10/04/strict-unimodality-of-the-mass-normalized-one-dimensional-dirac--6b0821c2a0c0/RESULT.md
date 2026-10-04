# Strict unimodality of the mass-normalized one-dimensional Dirac collapse threshold
## Finding
For the one-dimensional massive Dirac Keller problem of Dolbeault--Gontier--Pizzichillo--Van Den Bosch, let \(m>0\), \(p>1\), and let \(\alpha_\star(p;m)\) denote the critical \(L^p\)-norm at which the optimal eigenvalue reaches the lower edge of the spectral gap. Define the mass-normalized threshold \(A(p)=m^{1/p-1}\alpha_\star(p;m)\). Then \(A\) is independent of \(m\) and is strictly unimodal on \((1,\infty)\): there is exactly one \(p_\star\in(1,3/2)\) such that \(A\) is strictly increasing on \((1,p_\star)\) and strictly decreasing on \((p_\star,\infty)\). The maximizer is the unique zero of \[H(p)=\log\frac{2}{p-1}-\log B\!\left(\frac12,p-\frac12\right)+p\left[\psi\!\left(p-\frac12\right)-\psi(p)\right],\] and numerically \(p_\star\approx1.317094285913839\) and \(A(p_\star)\approx3.821987752657050\). The numerical decimals are supplementary; uniqueness and strict monotonicity follow analytically from the strict decrease of \(H\).

The source gives the exact one-dimensional critical formula
\[
\alpha_\star(p;m)^p=p^p\left(\frac{2m}{p-1}\right)^{p-1}B\!\left(\frac12,p-\frac12\right),\qquad p>1,
\]
and Figure 1 reports numerically that, for \(m=1\), the curve has a maximum near \(p=1.32\). The result here turns that numerical observation into a global strict-unimodality theorem and proves uniqueness of the maximizing exponent.

## Assumptions and scope
The statement concerns the one-dimensional critical threshold \(\alpha_\star(p;m)\) from Theorem 1.3 of the cited Dirac Keller problem, with \(m>0\) and \(p>1\). The normalization \(A(p)=m^{1/p-1}\alpha_\star(p;m)\) removes the mass scaling, since the displayed source formula gives
\[
A(p)^p=p^p\left(\frac{2}{p-1}\right)^{p-1}B\!\left(\frac12,p-\frac12\right).
\]
No claim is made about the higher-dimensional radial quantities plotted elsewhere in the source, nor about sign-changing potentials or other Dirac nonlinearities.

## Proof
Put \(F(p)=\log A(p)\), \(L(p)=\log B(1/2,p-1/2)\), and \(q(p)=\log(2/(p-1))\). Direct differentiation of the exact formula gives
\[
F'(p)=\frac{H(p)}{p^2},\qquad
H(p)=q(p)-L(p)+pL'(p),
\]
where
\[
L'(p)=\psi\!\left(p-\frac12\right)-\psi(p).
\]
A second differentiation yields
\[
H'(p)=-\frac1{p-1}+p\left[\psi_1\!\left(p-\frac12\right)-\psi_1(p)\right].
\]
For \(p>1\), the trigamma integral representation gives
\[
\psi_1\!\left(p-\frac12\right)-\psi_1(p)
=4\int_0^\infty \frac{s e^{-(2p-1)s}}{1+e^{-s}}\,ds.
\]
Since \(1+e^{-s}>2e^{-s/2}\) for \(s>0\),
\[
\psi_1\!\left(p-\frac12\right)-\psi_1(p)
<\frac{2}{(2p-3/2)^2}.
\]
Moreover,
\[
(2p-3/2)^2-2p(p-1)=2(p-1)^2+\frac14>0,
\]
so
\[
H'(p)<-\frac1{p-1}+\frac{2p}{(2p-3/2)^2}<0.
\]
Thus \(H\) is strictly decreasing. As \(p\downarrow1\), the term \(\log(2/(p-1))\) diverges while the beta and digamma terms remain finite, hence \(H(p)\to+\infty\). At \(p=3/2\), the standard values \(B(1/2,1)=2\) and \(\psi(1)-\psi(3/2)=2\log2-2\) give
\[
H(3/2)=4\log2-3<0.
\]
(The final inequality follows, for example, from \(e^{3/4}>1+3/4+(3/4)^2/2>2\).) Therefore \(H\) has exactly one zero \(p_\star\in(1,3/2)\). Because \(F'(p)=H(p)/p^2\), \(F\), and hence \(A\), is strictly increasing before that zero and strictly decreasing after it. This proves the claim.

## Verification
The proof is analytic and does not depend on numerical root finding. The accompanying verifier evaluates the explicit \(H\) and \(A\) at high precision, checks that \(H(1.31)>0>H(1.32)\), locates the unique numerical root near \(1.317094285913839\), and reproduces the quoted maximum value. These computations only corroborate the decimals; the global uniqueness is proved by the trigamma inequality above.

## Relationship to prior work
The primary source derives the exact beta-function formula for \(\alpha_\star(p;m)\) and its Figure 1 labels a numerical maximum near \(p=1.32\). In the inspected theorem, figure discussion, and one-dimensional derivation, it does not state a strict-increase/strict-decrease theorem or prove uniqueness of the maximizing exponent. Targeted searches using the exact formula, “maximum at \(p\approx1.32\)”, strict-unimodality language, and critical-Dirac-norm aliases did not reveal a stronger published statement. The present claim is therefore the rigorous global monotonicity refinement of that numerical observation, not a new derivation of the source’s critical formula.

## Limitations
The source already identifies the location of the maximum numerically, so the new content is specifically the analytic strict-unimodality and uniqueness theorem. The quoted decimal values are numerical and are not used in the proof. A residual literature risk remains that an equivalent special-function argument exists under different terminology. The theorem is restricted to the one-dimensional scalar nonnegative-potential critical curve supplied by the source.

## References
- J. Dolbeault, D. Gontier, F. Pizzichillo, H. Van Den Bosch, “Keller and Lieb–Thirring estimates of the eigenvalues in the gap of Dirac operators”, arXiv:2210.03091v1 (2022); Revista Matemática Iberoamericana 40 (2024), DOI 10.4171/RMI/1443.
