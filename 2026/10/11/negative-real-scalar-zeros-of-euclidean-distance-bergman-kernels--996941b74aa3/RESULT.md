# Negative-real scalar zeros of Euclidean-distance Bergman kernels in every complex-ball dimension

## Finding
Fix an integer \(d\ge2\) and a nonnegative integer \(t\). For the Euclidean unit ball \(\mathbb B^d\subset\mathbb C^d\), let \(A^2_{d,t}\) denote the holomorphic functions with finite norm
\[
\|f\|_{d,t}^2=\int_{\mathbb B^d}|f(z)|^2(1-\|z\|)^t\,dV(z),
\]
where \(dV\) is unnormalized \(2d\)-dimensional Lebesgue volume and \(\|z\|\) is Euclidean length. Set \(s=\langle z,w\rangle=\sum_{j=1}^d z_j\overline{w_j}\), \(m=\lceil t/2\rceil\), and \(q=\lfloor t/2\rfloor\). The reproducing kernel is exactly
\[
K_{d,t}(z,w)=\frac{Q_{d,t}(s)}{|\mathbb S^{2d-1}|B(2d,t+1)(1-s)^{d+t+1}},\qquad
Q_{d,t}(s)={}_2F_1\!\left(-m,-q-\tfrac12;d+\tfrac12;s\right),
\]
where \(|\mathbb S^{2d-1}|=2\pi^d/(d-1)!\) and \(B\) denotes Euler's beta function. In particular, \(Q_{d,t}\) is a rational-coefficient polynomial of degree exactly \(m\), including the constant polynomial when \(t=0\).

**Complete scalar zero geometry.** Each of the \(m\) scalar roots of \(Q_{d,t}\) is simple, real and in \(( -\infty,0)\). Thus there are no nonreal scalar zeros. The number of scalar roots in the unit disk, counted without multiplicity, is given by the exact finite rational-arithmetic formula
\[
N(d,t)=\operatorname{Var}\left(Q_{d,t}(-1),Q'_{d,t}(-1),\ldots,Q_{d,t}^{(m)}(-1)\right),
\]
where \(\operatorname{Var}\) counts consecutive changes of sign after removing all zero entries. A root at \(s=-1\) is on the boundary and is excluded by this formula. Consequently the Bergman kernel is zero-free on \(\mathbb B^d\times\mathbb B^d\) precisely when \(N(d,t)=0\). Every admissible scalar root \(s\) can be realized as \(\langle z,w\rangle\) for some \(z,w\in\mathbb B^d\).

Three exactly computed examples distinguish neighboring dimensions and exponents:
\[
\begin{aligned}
Q_{2,3}(s)&=(35+42s+3s^2)/35,&\quad s_{\mathrm{inside}}&=-7+\tfrac43\sqrt{21}\in(-1,0),\\
Q_{3,3}(s)&=(21+18s+s^2)/21,&\quad s_\pm&=-9\pm2\sqrt{15}\in(-\infty,-1),\\
Q_{3,4}(s)&=(21+30s+5s^2)/21,&\quad s_{\mathrm{inside}}&=-3+\tfrac25\sqrt{30}\in(-1,0).
\end{aligned}
\]
The conclusion depends on the Euclidean distance \(1-\|z\|\); replacing it by \(1-\|z\|^2\) gives a different, zero-free classical weighted kernel.

## Assumptions and scope
The result holds for every integer pair \((d,t)\in\mathbb Z_{\ge2}\times\mathbb Z_{\ge0}\); no further regularity assumptions are needed. The polynomial degree and zero count refer to the **single complex scalar** \(s=\langle z,w\rangle\), rather than a notion of isolated points on the several-variable zero hypersurface. The weight density is exactly \((1-\|z\|)^t\), with no normalizing probability factor. The symbol \((a)_k\) denotes the rising factorial and \(\operatorname{Var}\) the explicitly defined sign-variation operator.

## Proof
**1. Exact moments and hypergeometric kernel.** Spherical integration of a holomorphic monomial with multi-index \(\nu\in\mathbb Z_{\ge0}^d\), \(|\nu|=k\), gives
\[
\int_{\mathbb S^{2d-1}}|\zeta^\nu|^2\,d\sigma(\zeta)
=|\mathbb S^{2d-1}|\frac{\nu!}{(d)_k}.
\]
The radial integral is \(B(2k+2d,t+1)\). Since these monomials are a complete orthogonal basis, the multinomial identity yields
\[
K_{d,t}(s)=\frac1{|\mathbb S^{2d-1}|}
\sum_{k=0}^\infty \frac{(d)_k}{k!\,B(2k+2d,t+1)}s^k.
\]
After dividing by the coefficient at \(k=0\), the beta quotient and the duplication formula give
\[
\frac{(d)_k B(2d,t+1)}{k!\,B(2k+2d,t+1)}
=\frac{\bigl(d+\tfrac{t+1}{2}\bigr)_k\bigl(d+\tfrac{t+2}{2}\bigr)_k}
{\bigl(d+\tfrac12\bigr)_k\,k!}.
\]
Thus the normalized kernel is \({}_2F_1(A,B;C;s)\), with \(A=d+(t+1)/2\), \(B=d+(t+2)/2\) and \(C=d+1/2\). Euler's hypergeometric transformation, for which \(C-A-B=-d-t-1\), gives
\[
{}_2F_1(A,B;C;s)
=(1-s)^{-d-t-1}{}_2F_1(-t/2,-(t+1)/2;C;s).
\]
One of the two upper parameters is the nonpositive integer \(-m\). Symmetry of the upper parameters therefore yields the claimed \(Q_{d,t}\) with \(q=\lfloor t/2\rfloor\). Its coefficient at degree \(m\) is nonzero because \(-q-1/2\) is never a nonpositive integer, proving the claimed degree. For \(t=0\), the degree is zero.

**2. All scalar roots are simple and negative.** Define \(\alpha=d-\tfrac12\) and \(\beta=(-1)^t/2\), so that \(\alpha,\beta>-1\). Pfaff's transformation followed by the Jacobi hypergeometric formula yields the *polynomial identity*
\[
Q_{d,t}(s)=\frac{m!}{(d+\tfrac12)_m}(1-s)^m
P_m^{(\alpha,\beta)}\!\left(\frac{1+s}{1-s}\right).
\]
The Jacobi polynomial \(P_m^{(\alpha,\beta)}\) is orthogonal for the strictly positive weight \((1-x)^\alpha(1+x)^\beta\,dx\) on \((-1,1)\); hence for \(m\ge1\) its \(m\) roots \(x_1,\ldots,x_m\) are all distinct and lie strictly inside \((-1,1)\). The inverse Cayley map sends each to
\[
s_j=\frac{x_j-1}{x_j+1}\in(-\infty,0).
\]
No cancellation occurs at \(s=1\) (the numerator is finite and the prefactor on the right only expresses a polynomial identity), and every degree-\(m\) root is accounted for. For \(m=0\) the assertion is vacuous. This proves complete scalar real-rootedness and simplicity.

**3. An exact boundary-aware disk count.** Put \(F(u)=Q_{d,t}(u-1)\). Its roots are real, simple and less than \(1\). The positive roots of \(F\) are exactly the scalar roots of \(Q_{d,t}\) in \((-1,0)\), which are precisely those admissible to \(|s|<1\). Taylor's formula at \(-1\) gives
\[
F(u)=\sum_{j=0}^{m}\frac{Q_{d,t}^{(j)}(-1)}{j!}u^j.
\]
For clarity, the required exact version of Descartes' rule follows directly from real-rootedness. First factor out any power of \(u\) and discard zero coefficients. Ordinary Descartes bounds the positive root count by \(V_+\), the sign variations of the coefficients. Applied to \(F(-u)\), it bounds the negative root count by \(V_-\). Between adjacent nonzero coefficients the two sign-change counts total at most their index gap, hence \(V_++V_-\le\deg F\) after removal of zero factors. But all remaining roots of \(F\) are nonzero and real, so their positive and negative counts sum to this degree. Therefore both Descartes inequalities are equalities and the positive count is exactly \(V_+\). The positive factors \(1/j!\) do not alter signs, giving the formula for \(N(d,t)\). A zero coefficient of \(F\) at degree zero exactly encodes a boundary root \(s=-1\) and is omitted.

Finally \(|\langle z,w\rangle|<1\) for \(z,w\) in the unit ball. Conversely every \(s\) with \(|s|<1\) occurs: take \(z=\sqrt{|s|}e_1\) and \(w=\sqrt{|s|}e^{-i\arg(s)}e_1\) for \(s\ne0\), and choose \(z=0\) for \(s=0\). The denominator \((1-s)^{d+t+1}\) never vanishes inside the disk; therefore the scalar count is exactly the zero-free classification for the full kernel.

## Verification
A standalone standard-library script, `check_ball_kernel.py`, calculates all coefficients using exact rational arithmetic in two independently implemented ways: direct spherical/beta moments and the finite hypergeometric numerator over the binomial denominator. Its recorded execution returned: `PASS: 5776 exact independent moment/closed-form coefficient identities; sample zero counts and numerator normalizations verified.` It checks each \(1\le d\le16\), \(0\le t\le18\), and \(0\le k\le18\), together with the displayed small cases and sign-variation evaluations. These finite consistency checks do **not** replace the all-integer proof above. To reproduce, place the attached script in the current directory and run `python3 check_ball_kernel.py`.

## Relationship to prior work
Marinescu and Xing (2026, arXiv:2609.24258v1, first public September 21, 2026) prove parameter regularity for Euclidean boundary-distance weighted Bergman kernels on smooth bounded pseudoconvex domains, but do not characterize kernel zeros, exact ball numerators or discrete dimension/exponent transitions. Beberok (2016, arXiv:1601.02989v1) uses Jacobi polynomials for kernels on intersections of complex ellipsoids; those are different domains and weights, and the stated results do not supply these Euclidean-distance ball zero levels. Zeytuncu (2010, arXiv:1009.2806v1) constructs zeros for bounded-comparable radial weights on the complex disk. Perälä (2017, arXiv:1703.05976v1) constructs prescribed finite zero numbers and proves a general finiteness statement for radial disk weights. Neither disk result gives this exact higher-dimensional Jacobi zero geometry. The Euler and Pfaff identities and Jacobi zero theorem used in the proof are classical (DLMF §§15.8, 15.9, 18.16), not claimed as new.

## Limitations
Only integer \(t\ge0\) and complex dimensions \(d\ge2\) are classified. The formula does not establish negative-real scalar zero geometry for arbitrary real boundary-distance exponents, nor an analogous result on general smooth domains. An equivalent proof could exist in literature not captured by the inspected sources. Exact finite rational count means mathematical exactness, not that the checker has exhaustively verified infinitely many pairs. No independent mathematical audit is asserted.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1 (2026), https://arxiv.org/abs/2609.24258.
2. T. Beberok, *The Bergman kernel: explicit formulas, deflation, Lu Qi-Keng problem and Jacobi polynomials*, arXiv:1601.02989v1 (2016), https://arxiv.org/abs/1601.02989.
3. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806v1 (2010), https://arxiv.org/abs/1009.2806.
4. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1 (2017), https://arxiv.org/abs/1703.05976.
5. NIST Digital Library of Mathematical Functions, §§15.8, 15.9 and 18.16, https://dlmf.nist.gov/15.8, https://dlmf.nist.gov/15.9, https://dlmf.nist.gov/18.16.
