# Sharp magnetic-cycle Sobolev embeddings and real–complex flux rigidity

## Finding

For an integer \(n\ge1\) and a twist angle \(0<\theta\le\pi\), put
\[
E_\theta(a)=\sum_{j=1}^{n-1}|a_{j+1}-a_j|^2+|a_1-e^{i\theta}a_n|^2.
\]
For \(\mathbb F\in\{\mathbb R,\mathbb C\}\), let \(C_{\mathbb F}(n,\theta)\) be the best constant in
\[
\sum_{j=1}^n|a_j|\le C_{\mathbb F}(n,\theta)\sqrt{E_\theta(a)},\qquad a\in\mathbb F^n.
\]
The exact, simultaneously sharp laws are
\[
\boxed{C_{\mathbb R}(n,\theta)^2=\frac{n(n-1)(n-2)}{12}+\frac{n^2}{2(1-\cos\theta)}},
\qquad
\boxed{C_{\mathbb C}(n,\theta)^2=\frac{n}{4\sin^2(\theta/(2n))}}.
\]
At each nonendpoint twist \(0<\theta<\pi\), every nonzero real extremizer is a nonzero real multiple of the strictly positive vector
\[
\boxed{a_j=\frac{j(n+1-j)}2+\frac{n\cos\theta}{2(1-\cos\theta)}},\qquad 1\le j\le n,
\]
and every nonzero complex extremizer is a nonzero complex multiple of
\[
\boxed{a_j=e^{-i(j-1)\theta/n}}.
\]
At the antiperiodic boundary \(\theta=\pi\), the real extremizers are precisely nonzero real multiples of \(G\varepsilon\), where \(G_{ij}=(n-2|i-j|)/4\) and the signs \(\varepsilon_j\in\{-1,1\}\) have at most one sign change between consecutive indices. For \(n\ge3\) the complex extremizers are precisely the two pure waves \(a_j=\kappa e^{\pm i(j-1)\pi/n}\); at \(n=2\), all complex vectors with equal coordinate moduli are extremizers; at \(n=1\), every nonzero vector is an extremizer. (For \(n=1\), the definition of \(G\) gives the scalar \(1/4\).)

For \(n\ge2\) and \(0<\theta<\pi\), the complex constant strictly exceeds the real constant. This strictness also holds at \(\theta=\pi\) for \(n\ge3\), while the constants agree for \(n=1\) and at \((n,\theta)=(2,\pi)\). Two distinct singular limits appear:
\[
\lim_{n\to\infty}\frac{C_{\mathbb C}(n,\theta)}{C_{\mathbb R}(n,\theta)}=\frac{\sqrt{12}}{\theta}\quad(0<\theta\le\pi),
\qquad
\lim_{\theta\downarrow0}\frac{C_{\mathbb C}(n,\theta)}{C_{\mathbb R}(n,\theta)}=\sqrt n\quad(n\ge1).
\]
Thus the dimension and zero-flux limits do not commute. The endpoint antiperiodic law is also obtainable from previously established zero-mean periodic-cycle results; its inclusion here describes the endpoint of the new continuum of twists.

## Assumptions and scope

All differences and norms are unweighted, with no normalization by dimension. The complex phase enters **only** the last edge. The underlying path has \(n\) sites and its ends are joined with a unitary magnetic holonomy \(e^{i\theta}\). For real entries, the last edge is a genuinely complex residual, with squared norm \(a_1^2+a_n^2-2\cos\theta\,a_1a_n\). The angle is restricted to \((0,\pi]\); the upper half of the flux circle is sufficient because conjugation does not change either optimal constant. The value \(\theta=0\) is excluded: constant vectors have zero energy, so no finite constant exists.

## Proof

**1. The real quadratic form.** Put \(c=\cos\theta\in[-1,1)\). For real \(a\), let \(L_c\) denote the positive-definite symmetric matrix with \(E_\theta(a)=a^\top L_ca\). For \(n\ge2\), it has path edges of unit weight and an additional boundary coupling \(-c(a_1a_n+a_na_1)\). In particular,
\[
L_c=L_{-1}-\frac{1+c}{2}uu^\top+\frac{1+c}{2}vv^\top,
\quad u=e_1+e_n,\quad v=e_1-e_n.
\]
The displayed decomposition remains correct for \(n=2\), when the boundary edge shares the two vertices with the path edge. The antiperiodic inverse is the explicit Green matrix
\[
G=L_{-1}^{-1},\qquad G_{ij}=\frac{n-2|i-j|}{4}.
\]
Indeed, for an interior index the second difference of each column vanishes except at its source; the first and last rows give the antiperiodic boundary conditions. Directly,
\[
Gu=\tfrac12\mathbf1,\qquad Gv=w,\qquad w_i=\frac{n+1-2i}{2},
\qquad u^\top Gu=1,\quad v^\top Gv=n-1,\quad u^\top Gv=0.
\]
Two orthogonal rank-one inverse updates therefore yield the exact **magnetic Green identity**
\[
\boxed{L_c^{-1}=G+\frac{1+c}{4(1-c)}\mathbf1\mathbf1^\top
-\frac{1+c}{n+1+(n-1)c}ww^\top}.
\tag{1}
\]
Each denominator is positive because \(-1\le c<1\).

**2. Sharp antiperiodic sign bound, including its equality structure.** By real \(\ell^1\) duality and Cauchy–Schwarz in the \(L_c\)-inner product,
\[
C_{\mathbb R}(n,\theta)^2=\max_{\varepsilon\in\{-1,1\}^n}\varepsilon^\top L_c^{-1}\varepsilon.
\tag{2}
\]
For \(c=-1\), let \(A=\{j:\varepsilon_j=1\}\) and \(k=|A|\). Using the explicit kernel, define the cross-distance sum \(F(A)=\sum_{i\in A,j\notin A}|i-j|\). Then
\[
\varepsilon^\top G\varepsilon
=\frac n4(2k-n)^2-\frac{n(n^2-1)}6+2F(A).
\]
If \(A=\{a_1<\cdots<a_k\}\), direct summation gives
\[
F(A)=\sum_{r=1}^k\left[a_r^2+(2k-n+1-4r)a_r\right]+\frac{kn(n+1)}2.
\]
Set \(b_r=a_r-r\). The ordered-set constraints become \(0\le b_1\le\cdots\le b_k\le n-k\). The displayed expression is strictly convex in the \(b_r\), hence has its maximum at a vertex of this simplex. Such vertices have an initial string of zeroes and then an ending string of \(n-k\)'s, corresponding to a union of two packed endpoint blocks. If \(r\) points are packed at one end and \(k-r\) at the other, direct summation gives
\[
F(A)=(n-k)\left(\frac{kn}{2}-r(k-r)\right)
\le\frac{kn(n-k)}2,
\]
with equality precisely when \(A\) is one terminal contiguous block. Substitution cancels every dependence on \(k\), proving
\[
\boxed{\varepsilon^\top G\varepsilon\le\frac{n(n^2+2)}{12}},
\tag{3}
\]
with equality precisely for signs with at most one internal change, including the constant-sign cases. For \(n=1\), this bound is checked directly and the same formula holds.

**3. Exact real law and rigidity away from antiperiodic twist.** Combining (1) and (3), for any signs \(\varepsilon\),
\[
\begin{aligned}
\varepsilon^\top L_c^{-1}\varepsilon
&=\varepsilon^\top G\varepsilon+
\frac{1+c}{4(1-c)}\Big(\sum_j\varepsilon_j\Big)^2
-\frac{1+c}{n+1+(n-1)c}\Big(\sum_jw_j\varepsilon_j\Big)^2\\
&\le\frac{n(n^2+2)}{12}+\frac{(1+c)n^2}{4(1-c)}\\
&=\frac{n(n-1)(n-2)}{12}+\frac{n^2}{2(1-c)}.
\end{aligned}
\]
Both inequalities are equalities when \(\varepsilon=\pm\mathbf1\), since \(w\perp\mathbf1\). When \(-1<c<1\), the positive coefficient multiplying the squared sign sum forces equality only for these two sign vectors. As \(L_c^{-1}\mathbf1\) has the explicit strictly positive components
\[
(L_c^{-1}\mathbf1)_j=\frac{j(n+1-j)}2+\frac{nc}{2(1-c)},
\]
its sign vector is indeed \(+\mathbf1\), proving attainment. Cauchy–Schwarz equality in (2) proves the classification up to real scaling. At \(c=-1\), (3) instead gives the complete sign-change classification. The \(n=1\) case follows directly from \(E_\theta(a)=2(1-c)|a_1|^2\).

**4. The complex law.** Define the unitary twisted cyclic shift \(U_\theta\) by
\[
(U_\theta a)_j=a_{j+1}\ (j<n),\qquad (U_\theta a)_n=e^{-i\theta}a_1.
\]
Then \(E_\theta(a)=\|(I-U_\theta)a\|_2^2\). The eigenvalues of \(U_\theta\) are \(\exp(i(2\pi r-\theta)/n)\) for \(r=0,\ldots,n-1\). Therefore
\[
E_\theta(a)\ge4\sin^2\!\left(\frac\theta{2n}\right)\|a\|_2^2,
\qquad \|a\|_1\le\sqrt n\,\|a\|_2.
\]
The wave \(a_j=e^{-i(j-1)\theta/n}\) has constant coordinate moduli and lies in the least-eigenvalue eigenspace, so both inequalities are equalities. For \(0<\theta<\pi\) that eigenspace is one-dimensional, proving its extremizer rigidity. At \(\theta=\pi\), two lowest eigenvalues tie. For \(n\ge3\), a superposition of the two eigenwaves has constant modulus at every site only when one coefficient is zero (the nonconstant cross term samples at least three distinct phases); for \(n=2\), every equal-modulus vector attains equality; \(n=1\) is immediate.

**5. Scalar-field gap and asymptotics.** A real vector attaining the complex constant would have equal-magnitude coordinates and lie in the least eigenspace. For \(0<\theta<\pi\), that eigenspace is the span of a genuinely nonreal phase wave whenever \(n\ge2\), which is impossible. At \(\theta=\pi,n\ge3\), a real equal-modulus eigenvector would be a sign vector. At any interior site, its eigenvalue would have to belong to \(\{0,2,4\}\) by the discrete second-difference formula, whereas the least eigenvalue \(4\sin^2(\pi/(2n))\) lies strictly between zero and two. Thus the gap is strict; the listed exceptional equalities follow directly. Fixed-flux large-\(n\) expansion gives \(C_{\mathbb R}\sim n^{3/2}/\sqrt{12}\) and \(C_{\mathbb C}\sim n^{3/2}/\theta\). At fixed \(n\), small-flux expansions give \(C_{\mathbb R}\sim n/\theta\) and \(C_{\mathbb C}\sim n^{3/2}/\theta\). These establish both limits.

## Verification

The standalone `check.py` checks (1) against exact rational inverses for every \(2\le n\le9\) at seven rational cosine values, exhaustively enumerates all real sign vectors at those sizes, checks all equality patterns and the real Green extremizer, and checks the complex spectral equality and random real/complex vectors for \(2\le n\le26\) at seven positive twist angles. It passed **13,741** grouped rational and floating-point assertions. All identities for arbitrary \(n\), all continuous fluxes, and all limit assertions rely on the proof, not on these finite tests.

## Relationship to prior work

Hindov, Nitzan, Olsen, and Rydhe [1] solve sharp \(\ell^1\)-to-first/higher-difference \(\ell^2\) embeddings for finite, **zero-extended** sequences. Their operator and boundary conditions differ from the unitary single-edge holonomy considered here. Izmestiev [2] and earlier Fan–Taussky–Todd theory concern \(\ell^2\) discrete Wirtinger and spectral-gap inequalities; they do not determine the real \(\ell^1\) sign optimization or its flux-dependent rigidity. Previously established sharp mean-zero periodic-cycle Sobolev constants also cover the antiperiodic endpoint by doubling the cycle and restricting to the odd sector. **The endpoint \(\theta=\pi\) alone is not claimed as new.** The contribution is the whole continuum \(0<\theta<\pi\), the exact rank-two magnetic Green identity, the collapse to a unique real extremal ray, the complex eigenwave classification, and the noncommuting real–complex limiting regimes.

## Limitations

The theorem applies to an unweighted first-difference energy on a single finite magnetic cycle; no higher differences, arbitrary edge weights, or infinite-dimensional extension is asserted. The endpoint \(\theta=0\) is singular and deliberately excluded. An older magnetic-graph or inverse-Green-function theorem could imply the formula under different terminology; originality is a best-knowledge assessment rather than a priority certificate. No independent mathematical audit has been performed.

## References

[1] R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1, first public 2026-10-13, https://arxiv.org/abs/2610.19010 .

[2] I. Izmestiev, *A general discrete Wirtinger inequality and spectra of discrete Laplacians*, arXiv:1502.03186, first public 2015-02-11, https://arxiv.org/abs/1502.03186 .

[3] Prior sharp mean-zero periodic-cycle \(\ell^1\)/difference \(\ell^2\) result (2026, publicly archived research record): for a cycle of length \(N\), the real squared constant is \(m(N-m)[m(N-m)+2]/(3N)\), \(m=\lfloor N/2\rfloor\); the complex squared constant is \(N/[4\sin^2(\pi/N)]\). Cited for its overlapping antiperiodic specialization, not as a novel ingredient.
