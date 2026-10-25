# A fourth-to-sixth moment optimizer reversal for the two fundamental \(G_2\) characters

## Finding
Let \(G\) be the compact simply connected exceptional Lie group of type \(G_2\), equipped with Haar probability measure. Let \(u=\chi_7\) and \(v=\chi_{14}\) be the ordinary (unscaled) trace characters of its two fundamental irreducible representations of dimensions seven and fourteen. For any \(a,b\in\mathbb C\), and \(m\in\{2,3\}\),
\[
\int_G |a u(g)+b v(g)|^{2m}\,dg\le K_{2m}(|a|^2+|b|^2)^m.
\]
Both constants are optimal. Let
\[
\begin{aligned}
P_4(t)&=4+8t+18t^2+4t^3+5t^4,\\
P_6(t)&=35+180t+495t^2+640t^3+675t^4+240t^5+80t^6,\\
q_4(t)&=t^4+4t^3+3t^2-5t-2,\\
q_6(t)&=8t^6+29t^5+24t^4-24t^3-34t^2-26t-6.
\end{aligned}
\]
Each polynomial \(q_4,q_6\) has exactly one positive zero, denoted \(r_4,r_6\). The constants are exactly
\[
K_4=\frac{P_4(r_4)}{(1+r_4^2)^2}=9.7665142176534\ldots,\qquad
K_6=\frac{P_6(r_6)}{(1+r_6^2)^3}=296.816583521357\ldots.
\]
Equality for a nonzero coefficient pair holds, respectively, **if and only if**
\[
(a,b)=\lambda(1,r_4)\quad\text{or}\quad(a,b)=\lambda(1,r_6),\qquad \lambda\in\mathbb C\setminus\{0\},
\]
where the appropriate ratio is selected for the corresponding moment order. In particular,
\[
0<r_4=0.936281959416\ldots<1<r_6=1.145074777518\ldots,
\]
so the sharp fourth moment favors the seven-dimensional representation in squared-coefficient mass, while the sharp sixth moment favors the fourteen-dimensional adjoint representation. This is a strict reversal of the optimal mixture of the complete fundamental-character packet.

## Assumptions and scope
The two characters \(u\) and \(v\) are real-valued on \(G\), orthonormal in \(L^2(G,dg)\), and have \(u(e)=7\), \(v(e)=14\). The ratio \(b/a\) in the equality classes is real and strictly positive; arbitrary overall complex scalars are allowed. The assertion concerns arbitrary *complex* coefficients, with no assumption of real positivity, and only moment orders four and six. Both zero and one-character boundary cases are included in the inequality; neither is a nonzero extremizer.

## Proof
**1. Complete root data and Haar normalization.** On a maximal torus choose coordinates \((z,w)\in\mathbb T^2\). Let the three pairs of short and long root exponents be
\[
S=\{(1,0),(0,1),(-1,1)\},\qquad
L=\{(1,1),(2,-1),(1,-2)\}.
\]
For an exponent pair \(\alpha=(p,q)\) put \(Z_\alpha=z^pw^q\). Then the restrictions of the two fundamental characters are the explicit real Laurent polynomials
\[
u(z,w)=1+\sum_{\alpha\in S}(Z_\alpha+Z_\alpha^{-1}),\qquad
v(z,w)=2+\sum_{\alpha\in S\cup L}(Z_\alpha+Z_\alpha^{-1}).
\]
By Weyl integration for the twelve-element Weyl group, for every polynomial \(H\) in two real variables,
\[
\int_G H(u,v)\,dg=\frac{1}{12}\operatorname{CT}_{z,w}\!\left(H(u(z,w),v(z,w))W(z,w)\right),
\quad W(z,w)=\prod_{\alpha\in S\cup L}(2-Z_\alpha-Z_\alpha^{-1}),
\]
where \(\operatorname{CT}_{z,w}\) means the coefficient of \(z^0w^0\). Direct multiplication gives \(\operatorname{CT}W=12\), so the measure is probability normalized.

**2. Exact finite moment calculation.** Multiplying the explicit Laurent polynomials and extracting the constant terms gives the following *complete* mixed-moment arrays, ordered by \(j=0,1,\ldots,n\):
\[
\begin{array}{c|l}
n & (\int_G u^{n-j}v^j\,dg)_{j=0}^{n}\\\hline
2 &(1,0,1)\\
4 &(4,2,3,1,5)\\
6 &(35,30,33,32,45,40,80).
\end{array}
\]
This calculation is finite and exact; the complete coefficient-extraction algorithm and a second, nonaliasing torus-grid integration check are included in `check_g2.py`. In particular, the second moments verify orthonormality. Because \(u\) and \(v\) are genuine self-dual characters, all mixed moments in the displayed even total orders are nonnegative integers: they count invariant tensors in the corresponding tensor products. The fourth-moment entries can also be reconstructed from
\[
7\otimes7=1\oplus7\oplus14\oplus27,\quad
7\otimes14=7\oplus27\oplus64,\quad
14\otimes14=1\oplus14\oplus27\oplus77\oplus77'.
\]
The tensor-product notation refers to representation dimensions and distinguishes the two seventy-seven-dimensional irreducibles.

**3. Complex phases are rigid.** For \(m\in\{2,3\}\), expand
\[
\int_G |au+bv|^{2m}\,dg=\sum_{j,k=0}^m\binom mj\binom mk
 a^{m-j}b^j\overline a^{\,m-k}\overline b^{\,k}
\int_G u^{2m-j-k}v^{j+k}\,dg.
\]
All numerical mixed-moment coefficients are nonnegative. The triangle inequality therefore bounds this expression by the same expression with \((a,b)\) replaced by \((|a|,|b|)\). If \(ab\ne0\), equality requires \(a\) and \(b\) to have a common phase: the terms indexed by \((j,k)=(0,0)\) and \((0,1)\) have strictly positive coefficients because \(\int_G u^{2m}\,dg>0\) and \(\int_G u^{2m-1}v\,dg\) equals respectively \(2\) or \(30\). These terms force their phases to agree.

**4. Sharp one-variable optimization.** By homogeneity and step 3 it remains to take \(a>0\), \(b=ta\), \(t\ge0\). The arrays in step 2 yield
\[
\frac{\int_G|au+bv|^{2m}\,dg}{(|a|^2+|b|^2)^m}
=\frac{P_{2m}(t)}{(1+t^2)^m}.
\]
Exact differentiation gives
\[
\frac{d}{dt}\frac{P_4(t)}{(1+t^2)^2}=-\frac{4q_4(t)}{(1+t^2)^3},\qquad
\frac{d}{dt}\frac{P_6(t)}{(1+t^2)^3}=-\frac{30q_6(t)}{(1+t^2)^4}.
\]
The coefficient lists of both \(q_4\) and \(q_6\), read from leading degree to constant degree, each have **exactly one sign change**. Both take negative values at zero and positive values for sufficiently large positive arguments, so Descartes' rule of signs and continuity yield exactly one positive root in each case. Each moment ratio increases strictly up to that root and decreases strictly afterward. Thus the displayed values are sharp *global* maxima, and the equality classes are complete. Finally, \(q_4(1)=1>0\), whereas \(q_6(1)=-29<0\), proving \(r_4<1<r_6\) without numerical approximation. The case \(a=0\) follows as \(t\to\infty\), and \(b=0\) is \(t=0\), so there are no boundary extremizers.

## Verification
Run `python3 check_g2.py` with Python 3, SymPy, and NumPy. It reconstructs the two character Laurent polynomials and the Weyl density, verifies the exact second, fourth and sixth mixed-moment tables, confirms both derivative factorizations, rigorously checks rational intervals isolating the unique positive roots, and separately evaluates the same integrals on a 48-by-48 torus grid. The exact-grid check is valid because, at moment orders at most six, every exponent in the integrands has both coordinates strictly between \(-24\) and \(24\); the grid thus has no nonzero frequencies divisible by 48. The grid step uses floating arithmetic only as a redundant numerical check; exact results rely on the Laurent coefficient computation and analytic optimization. `check_g2_output.txt` records a completed execution.

## Relationship to prior work
Evans–Pugh determine the joint spectral measure and character restrictions for the two fundamental representations of \(G_2\) (arXiv:1404.1863), supplying a general source from which raw mixed moments may be extracted. Their joint-density theorem is not claimed as new, and the finite mixed-moment arrays themselves are treated as ingredients rather than as the contribution. Ratcliffe's thesis (first verified public repository deposit 2024-06-03) develops invariant-theoretic tools for \(G_2\)-modules; Collins surveys Haar moment calculus on compact groups. The new object determined here is the pair of *globally sharp coefficient-optimized* fourth- and sixth-moment inequalities, with complete complex equality classifications and the strict reversal of the favored fundamental representation. Searches for the exact parameter ratios, joint optimization, and exceptional-group moment inequalities did not identify an earlier statement of this paired theorem. A negative search does not prove priority.

## Limitations
No sharp assertion is made for non-even moments, moment orders other than four and six, general higher-weight character packets, matrix coefficients, or other exceptional groups. The two spectral laws from prior work determine the mixed moments in principle; the originality claim is confined to exact optimization, phase rigidity, and the moment-order reversal. Unindexed older equivalent statements remain a bibliographic risk. All proofs and computations have been checked within this package; no independent external mathematical audit has occurred.

## References
1. D. E. Evans and M. Pugh, *Spectral Measures for G2*, arXiv:1404.1863, first submitted 2014-04; see Sections 2 and 4, https://arxiv.org/abs/1404.1863 .
2. R. M. Ratcliffe, *Young-diagrammatic Methods for the Representation Theory of G2*, University of York PhD thesis (December 2023), public repository deposit 2024-06-03, https://etheses.whiterose.ac.uk/id/eprint/35009/ .
3. B. Collins, *Moment Methods on Compact Groups: Weingarten Calculus and Its Applications*, Proc. ICM 2022, DOI 10.4171/ICM2022/114, https://ems.press/content/book-chapter-files/33238 .
