# Factorial spectral stratification of compact-core concentration in polyanalytic Bergman spaces

## Finding

For each integer \(q\ge3\), the full order-\(q\) polyanalytic Bergman space on the unit disk has exactly \(q\) eigenvalue branches in each nonnegative angular Fourier sector for concentration on the centered disk \(|z|<\sqrt{s}\), \(0<s<1\). Writing their eigenvalues in decreasing order as \(\lambda_{m,1}(s)\ge\cdots\ge\lambda_{m,q}(s)>0\), for \(m=0,1,\ldots\), every branch has the sharp asymptotic

\[
\boxed{\lambda_{m,j}(s)\sim
\left(\frac{(j-1)!}{(q-j)!}\right)^2
s^{m+2j-1}\,[m(1-s)]^{2(q+1-2j)},
\qquad j=1,\ldots,q.}
\]

For **every** \(m\ge0\), an additional exact identity holds:

\[
\boxed{\prod_{j=1}^{q}\lambda_{m,j}(s)=s^{q(m+q)}.}
\]

Put \(L=\log(1/\varepsilon)\) and \(\ell=\log(1/s)\), and let \(N_j(\varepsilon)\) count the members of branch \(j\) above \(\varepsilon>0\), with nonnegative Fourier degree and multiplicity one per sector. Then, as \(\varepsilon\downarrow0\),

\[
\boxed{N_j(\varepsilon)=\frac{L}{\ell}+
\frac{2(q+1-2j)}{\ell}\log L+O_{q,s}(1).}
\]

The finitely many negative-angular-frequency sectors do not affect the divergent terms. Hence the entire positive spectral counting function \(N(\varepsilon)\), counting multiplicity, and the extreme-branch separation satisfy

\[
\boxed{N(\varepsilon)=\frac{qL}{\ell}+O_{q,s}(1),\qquad
N_1(\varepsilon)-N_q(\varepsilon)=\frac{4(q-1)}{\ell}\log L+O_{q,s}(1).}
\]

Thus the \(q\) branchwise log–log corrections cancel *exactly* in the total count, even though their individual coefficients form a nontrivial arithmetic progression.

## Assumptions and scope

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(d\mu(z)=\pi^{-1}\,dA(z)\). Let \(\mathcal A_q^2\subset L^2(\mathbb D,d\mu)\) be the closed Hilbert space of functions \(f\) satisfying \(\bar\partial^q f=0\) distributionally. Equivalently, \(f(z)=\sum_{a=0}^{q-1}\bar z^a h_a(z)\) for analytic \(h_a\). Let \(P_q\) be its orthogonal projection, and set \(T_{q,s}=P_q\mathbf1_{\{|z|^2<s\}}|_{\mathcal A_q^2}\). The hypotheses are **fixed integer** \(q\ge3\) and **fixed** \(0<s<1\); no uniform claim is made as either parameter varies.

Rotation-invariance decomposes \(\mathcal A_q^2\) into mutually orthogonal angular sectors indexed by integers \(m\ge1-q\). The sector for \(m\ge0\) consists exactly of \(z^m p(|z|^2)\), with polynomial \(p\) of degree at most \(q-1\), and therefore has dimension \(q\). A negative sector \(1-q\le m\le-1\) has finite dimension \(q+m\). The compact positive operator \(T_{q,s}\) is strictly positive on every nonzero sector; its only spectral accumulation point is zero.

## Proof

**1. Exact Gram reduction and determinant.** In the sector of degree \(m\ge0\), let \(t=|z|^2\). Up to a common scalar, the uncut and cut Gram matrices in the polynomial basis \(1,t,\ldots,t^{q-1}\) are

\[
H_m(1)_{ij}=\frac1{m+i+j+1},\qquad
H_m(s)_{ij}=\frac{s^{m+i+j+1}}{m+i+j+1},
\quad0\le i,j<q.
\]

They are positive definite. The block eigenvalues are the generalized eigenvalues of \((H_m(s),H_m(1))\). Writing \(D_s=\operatorname{diag}(1,s,\ldots,s^{q-1})\) gives \(H_m(s)=s^{m+1}D_sH_m(1)D_s\). Taking determinants of the generalized eigenvalue equation proves

\[
\prod_{j=1}^{q}\lambda_{m,j}(s)
=s^{q(m+1)}(\det D_s)^2=s^{q(m+q)}.
\]

Moreover, on the Hilbert space \(\mathcal P_{q-1}\) of degree-at-most-\(q-1\) polynomials, with inner product \(\langle p,r\rangle_m=(m+1)\int_0^1p(t)\overline{r(t)}t^m\,dt\), the composition operator \((C_sp)(t)=p(st)\) has the property

\[
\lambda_{m,j}(s)=s^{m+1}\sigma_j(C_s)^2,
\]

where \(\sigma_1\ge\cdots\ge\sigma_q\) are singular values. This is simply the change of variable \(t=su\) in the cut norm; it does not presuppose diagonalizability of \(C_s\).

**2. Boundary-scaled orthogonal polynomials.** Put \(y=m(1-t)\) for \(m\ge1\), and transport the normalized measure \((m+1)t^m\,dt\) to the probability measure

\[
 d\nu_m(y)=\frac{m+1}{m}\left(1-\frac ym\right)^m
\mathbf1_{[0,m]}(y)\,dy.
\]

For every fixed nonnegative integer \(h\), its moments are exactly

\[
\int y^h\,d\nu_m(y)=
 h!\frac{m^h}{(m+2)(m+3)\cdots(m+h+1)}\longrightarrow h!.
\]

(The empty product for \(h=0\) is one.) Consequently, Gram–Schmidt on \(1,y,\ldots,y^{q-1}\) gives orthonormal polynomials \(P_{m,j}(y)\), chosen with positive leading coefficients, converging **coefficientwise** to \((-1)^jL_j(y)\), where \(L_j\) is the standard Laguerre polynomial, orthonormal for \(e^{-y}dy\) and having leading coefficient \((-1)^j/j!\). Each fixed coefficient differs from its limit by \(O_q(m^{-1})\), because the finite list of relevant moments has that rate and all limiting Gram determinants are positive.

The original dilation \(t\mapsto st\) becomes the affine transformation \(y\mapsto a+sy\), where \(a=m(1-s)\). Thus the upper-triangular matrix \(A_m\) of \(C_s\) in the orthonormal \(P_{m,j}\) basis has entries

\[
(A_m)_{ij}=\langle P_{m,i},P_{m,j}(a+s\,\cdot)\rangle_{\nu_m}
=\begin{cases}
\displaystyle\frac{s^i}{(j-i)!}\,a^{j-i}+O_{q,s}(a^{j-i-1}),&0\le i\le j<q,\\
0,&i>j.
\end{cases}
\]

To verify the leading term, the highest monomial of \(P_{m,j}\) has coefficient \(1/j!+O(m^{-1})\). Its expansion contains the monomial \(\binom ji a^{j-i}s^iy^i\), whose coefficient in \(P_{m,i}\) is \(i!+O(m^{-1})\); lower powers of the argument have strictly smaller \(a\)-degree. Since \(a\) is comparable with \(m\) for fixed \(s\), the stated error bound follows.

**3. Singular-value exterior powers.** The product of the \(k\) largest singular values of \(A_m\) equals \(\|\bigwedge^k A_m\|\). Each entry of \(\bigwedge^k A_m\) is a \(k\)-by-\(k\) minor of \(A_m\). A minor using row indices \(I\) and column indices \(J\) can have polynomial order in \(a\) no greater than \(\sum_{j\in J}j-\sum_{i\in I}i\). The **unique** maximal exponent \(k(q-k)\) occurs for rows \(I=\{0,\ldots,k-1\}\) and columns \(J=\{q-k,\ldots,q-1\}\).

For that minor, the nonzero leading coefficient is

\[
s^{k(k-1)/2}
\det\left[\frac1{(q-k+v-u)!}\right]_{u,v=0}^{k-1}
=s^{k(k-1)/2}\frac{\prod_{r=0}^{k-1}r!}{\prod_{r=q-k}^{q-1}r!}.
\]

The reciprocal factorial is interpreted as zero for a negative argument. To prove the determinant identity, multiply column \(v\) by \((q-k+v)!\); the resulting column has falling-factorial entries \((q-k+v)_{\underline u}\). Their determinant is the Vandermonde product \(\prod_{r=0}^{k-1}r!\), as the column nodes are consecutive integers. The identity also holds for \(k=q\); in this case it is \(\det A_m=s^{q(q-1)/2}\) exactly.

Because there are only finitely many minors, and all remaining minors have strictly smaller order in \(a\), the operator norm of the exterior power is asymptotic to the absolute value of this single leading minor. Therefore

\[
\prod_{j=1}^{k}\sigma_j(C_s)
\sim s^{k(k-1)/2}a^{k(q-k)}
\frac{\prod_{r=0}^{k-1}r!}{\prod_{r=q-k}^{q-1}r!}.
\]

Divide consecutive identities (taking the empty product as one). For every \(j=1,\ldots,q\),

\[
\sigma_j(C_s)\sim
\frac{(j-1)!}{(q-j)!}\,s^{j-1}a^{q+1-2j}.
\]

Squaring and multiplying by \(s^{m+1}\) proves the branch formula. No unproved assumption about the spectrum of a finite compression was used.

**4. Counting and cancellation.** Taking logarithms of the positive branch asymptotics gives

\[
\log\lambda_{m,j}(s)=
-m\ell+2(q+1-2j)\log m+O_{q,s}(1),
\qquad m\to\infty.
\]

For each fixed branch the ratio of successive eigenvalues tends to \(s<1\), so the branch is eventually strictly decreasing. Solving the inequality \(\lambda_{m,j}(s)>\varepsilon\) using the displayed estimate and integer rounding yields

\[
N_j(\varepsilon)=\frac L\ell+
\frac{2(q+1-2j)}\ell\log L+O_{q,s}(1).
\]

There are exactly \(q(q-1)/2\) dimensions in the negative angular sectors, so they contribute at most a fixed constant. Summing \(j=1,\ldots,q\), the coefficients cancel because \(\sum_{j=1}^q(q+1-2j)=0\). Taking the difference of the first and last branch gives the remaining formula. This also proves compactness and completes the proof.

## Verification

The accompanying `checker.py` uses exact rational arithmetic to test generalized-Gram determinant identities for several integer frequencies, orders and rational cutoff parameters, together with reciprocal-factorial minor determinants through order eight. Executing `python checker.py` produces `PASS: 126 exact rational determinant and factorial identities`. Independent high-precision generalized eigenvalue calculations were additionally compared against the asymptotic constants for orders three to five, cutoffs \(s=1/2\) and \(s=4/5\), and Fourier degrees up to one thousand; their ratios tend toward one. The analytical proof above, not a finite test, is the justification for asymptotic statements.

The exact Gram matrix also provides a reproducible numerical route: compute its positive generalized eigenvalues against the uncut Gram matrix, avoiding asymptotic substitutions at finite frequency. High precision is advisable because Hilbert-type Gram matrices are ill-conditioned as the order or degree grows.

## Relationship to prior work

Barrera-Castelán, Maximenko and Ramos-Vazquez (first preprint 2020) establish the full weighted polyanalytic Bergman Fourier decomposition and explicit radial Toeplitz matrix representations. Their later paper (first preprint 2023) characterizes the associated C*-algebras and scalar limits of radial operator blocks. These are the starting structural tools but do **not** state the sharp factorial constants for the compact-core indicator, the complete order-by-order branch stratification, or the canceling log–log counting corrections. Čučković and Le study algebraic Toeplitz relations on the same polyanalytic function space, not these asymptotics. Rozenblum studies compact-support eigenvalue estimates on analytic and harmonic Bergman-type spaces; Pushnitski studies boundary-power symbols on analytic Bergman space. Neither contains the present fixed-order, multiple-branch compact-core theorem. All comparisons concern the actual claims rather than titles alone.

## Limitations

The theorem concerns the **full** polyanalytic space, not an individual true-polyanalytic summand, the unweighted unit disk, a single concentric hard cutoff, fixed \(q\ge3\), and fixed \(0<s<1\). It does not provide uniformity in \(q\), the cutoff approaching a boundary, or nonsymmetric regions. The eigenvalue ordering is by size **within** each angular sector, not a global spectral ordering. The remainder \(O(1)\) in spectral counting cannot be replaced by an asserted convergent constant: integer rounding can oscillate. The proof does not establish a matching global eigenfunction limit or a finite-degree monotonicity threshold. Mathematical priority remains provisional pending specialist independent literature review.

## References

1. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, first posted 2020-09-29, arXiv:2009.14301, https://arxiv.org/abs/2009.14301 (especially Sections 5, 7 and 8).
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces*, first posted 2023-06-09, arXiv:2306.06231, https://arxiv.org/abs/2306.06231 (especially Sections 1, 3 and 4).
3. Ž. Čučković, T. Le, *Toeplitz operators on Bergman spaces of polyanalytic functions*, first posted 2010-12-13, arXiv:1012.2816, https://arxiv.org/abs/1012.2816.
4. G. Rozenblum, *On lower eigenvalue estimates for Toeplitz operators with radial symbols in Bergman spaces*, first posted 2010-12-16, arXiv:1012.3528, https://arxiv.org/abs/1012.3528.
5. A. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, first posted 2017-10-07, arXiv:1710.02652, https://arxiv.org/abs/1710.02652.
