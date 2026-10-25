# Sharp normalized even-power Daugavet deficits on real Hilbert spaces

## Finding
Let \(H\) be a real Hilbert space of dimension at least two. For every **even integer** \(m\ge 2\) and every rank-one operator \(T\in\mathcal L(H)\) with \(\|T\|=1\), define the *normalized even-power Daugavet deficit*
\[
\Delta_m(T)=1+\|T^m\|-\|I+T^m\|\,.
\]
Writing \(a=|\operatorname{tr}T|\in[0,1]\), one has the **complete overlap formula**
\[
\boxed{\displaystyle
\Delta_m(T)=F_m(a):=\frac{2+a^{m-1}-\sqrt{4+4a^m+a^{2m-2}}}{2}
=\frac{2a^{m-1}(1-a)}{2+a^{m-1}+\sqrt{4+4a^m+a^{2m-2}}}.}
\]
Every overlap \(a\in[0,1]\) is realized already on \(\mathbb R^2\). Consequently the dimension-independent sharp constant is
\[
\beta_m:=\sup_{\substack{T:\ \operatorname{rank}T=1\\\|T\|=1}}\Delta_m(T)
=\max_{0\le a\le 1}F_m(a)>0.
\]
At the square endpoint the exact extremum and a global quadratic rigidity identity are
\[
\boxed{\displaystyle\beta_2=1-\frac{2}{\sqrt5},\qquad
 a_*=\frac1{\sqrt5},\qquad
 \beta_2-F_2(a)=\frac{2(a-a_*)^2}{\sqrt{4+5a^2}+a+4/\sqrt5}.}
\]
In particular, the maximizing overlap is unique and \(\beta_2-\Delta_2(T)\ge(a-a_*)^2/3\) for all normalized rank-one \(T\). Along **even** \(m\to\infty\), the sequence of sharp constants and all maximizing overlaps satisfy
\[
\boxed{\displaystyle \lim_{\substack{m\to\infty\\m\ \mathrm{even}}}m\beta_m=\gamma=W\!\left(\frac1{2e}\right),\qquad
\lim_{\substack{m\to\infty\\m\ \mathrm{even}}}m(1-a_m)=1+\gamma,}
\]
where \(W\) is the principal real Lambert function and \(a_m\) is **any** maximizer of \(F_m\). Numerically \(\gamma\approx0.157184951483814\).

## Assumptions and scope
The scalar field is \(\mathbb R\), the Hilbert dimension satisfies \(\dim H\ge2\) (finite or infinite), and all operators considered in the supremum are rank one of norm **exactly** one. We use the convention \((u\otimes v)(x)=\langle x,v\rangle u\). For finite rank-one operators the trace \(\operatorname{tr}T\) is well defined and equals \(\langle u,v\rangle\) in any unit-vector decomposition \(T=u\otimes v\). The parity restriction is substantive: sign cancellations change the positive-sign norm formula for odd powers. Deficits are nonnegative by the triangle inequality, and no conclusion about arbitrary bounded operators is asserted. The real-valued inverse \(W\) solves \(W(z)e^{W(z)}=z\) for \(z>0\).

## Proof
**(1) Reduction to a two-dimensional singular-value problem.** Represent \(T=u\otimes v\) with \(\|u\|=\|v\|=1\), and write \(c=\langle u,v\rangle\in[-1,1]\) and \(a=|c|\). The rank-one multiplication identity gives \(T^m=c^{m-1}T\), so \(\|T^m\|=a^{m-1}\). Since \(m\) is even, the rank-one operator \(T^m\) has positive trace \(c^m=a^m\); replacing its output vector by its sign-normalized unit direction, and taking a suitable orthonormal basis of \(\operatorname{span}\{u,v\}\), its nontrivial two-dimensional block is
\[
M_m(a)=\begin{pmatrix}
1+a^m&a^{m-1}\sqrt{1-a^2}\\0&1
\end{pmatrix}.
\]
If \(a=1\), the subspace of support has dimension one and the same block still embeds by adjoining any orthogonal unit vector (possible because \(\dim H\ge2\)). If \(a=0\), the even power vanishes; the formula also holds by continuity or directly. Outside the chosen plane, \(I+T^m\) is the identity. For the two singular values \(s_+\ge s_-\) of \(M_m(a)\), the determinant and Frobenius trace give
\[
s_+s_-=1+a^m,\qquad s_+^2+s_-^2=2+2a^m+a^{2m-2}.
\]
Hence \(s_+-s_-=a^{m-1}\), \(s_++s_-=\sqrt{4+4a^m+a^{2m-2}}\), so
\[
\|I+T^m\|=s_+=\frac{\sqrt{4+4a^m+a^{2m-2}}+a^{m-1}}2.
\]
Here \(s_+\ge1\), ensuring the untouched orthogonal complement never changes the norm. Substitution gives the first expression for \(F_m\); rationalization gives its second, manifestly nonnegative, expression. Every overlap is realized on \(\mathbb R^2\) by \(u=e_1\) and \(v=a e_1+\sqrt{1-a^2}\,e_2\). This proves that the optimization is independent of dimension and the supremum is a maximum. It is strictly positive because \(F_m(a)>0\) for \(0<a<1\).

**(2) Exact square maximizer and global stability.** At \(m=2\),
\[
F_2(a)=\frac{2+a-\sqrt{4+5a^2}}2,\qquad
F_2'(a)=\frac12\left(1-\frac{5a}{\sqrt{4+5a^2}}\right).
\]
The derivative is positive when \(a<1/\sqrt5\), zero only at \(a_*=1/\sqrt5\), and negative afterward. Substitution yields \(F_2(a_*)=1-2/\sqrt5\). The identity
\[
\sqrt{4+5a^2}-a-\frac4{\sqrt5}
=\frac{4(a-a_*)^2}{\sqrt{4+5a^2}+a+4/\sqrt5}
\]
proves the asserted exact quadratic deficit. As the denominator on \([0,1]\) is at most \(3+1+4/\sqrt5<6\), its right side yields \(\beta_2-F_2(a)\ge(a-a_*)^2/3\).

**(3) High even-power boundary layer.** Let \(c=m(1-a)\), so \(0\le c\le m\). For every \(m\ge2\), rationalization and \(a^{m-1}\le\exp(-(1-1/m)c)\le e^{-c/2}\) imply
\[
0\le mF_m(a)\le\frac12 c e^{-c/2}.
\]
The upper bound vanishes uniformly when \(c\to\infty\), and tends to zero as \(c\downarrow0\). For each fixed \(c\ge0\), put \(a=1-c/m\) (valid for \(m\ge c\)). Then \(a^{m-1}\to e^{-c}\), \(a^m\to e^{-c}\), and, uniformly on every compact interval of \(c\),
\[
mF_m(1-c/m)\longrightarrow f(c):=\frac{ce^{-c}}{2+e^{-c}}=\frac{c}{2e^c+1}.
\]
A trial choice \(c=1\) shows \(\liminf m\beta_m\ge f(1)>0\). The uniform tail bound and endpoint control force all maximizing boundary-layer parameters \(c_m=m(1-a_m)\) into a common compact subset of \((0,\infty)\) for sufficiently large \(m\); therefore uniform convergence implies every accumulation point of \(c_m\) maximizes \(f\), and \(m\beta_m\to\max_{c\ge0}f(c)\). Its derivative has sign
\[
\operatorname{sgn} f'(c)=\operatorname{sgn}\!\left(1+2e^c(1-c)\right).
\]
The parenthesized function is strictly decreasing for positive \(c\), starts positive, and tends to negative infinity. Its unique zero \(c_*>1\) obeys \((c_*-1)e^{c_*-1}=1/(2e)\), hence \(c_*=1+\gamma\), \(\gamma=W(1/(2e))\). At this critical point \(2e^{c_*}=1/(c_*-1)\) and \(f(c_*)=c_*/(2e^{c_*}+1)=c_*-1=\gamma\). Uniqueness forces \(c_m\to c_*\) for **every** maximizing selection. This finishes the proof.

## Verification
The exact two-dimensional norm calculation is independently reproducible from the displayed \(2\times2\) matrix, its determinant and squared Frobenius norm; the non-asymptotic proof works for each Hilbert dimension at least two and for every even positive integer at least two. `CHECK.py` uses only the Python standard library to recompute the closed-form and elementary matrix-derived singular-value expressions over a finite test grid and to check numerical maximizers and boundary-layer scaling. Such numerical tests are supplementary; the quantified theorem follows from the analytic proof above, not from numerical enumeration. The witness \(a=1/\sqrt5\) attains the exact square constant already on \(\mathbb R^2\).

## Relationship to prior work
Langemets, *Characterizing the Daugavet property by squares of rank-one operators* (2026), proves a **qualitative** equivalence between the full Daugavet property and either signed rank-one-square identity in real Banach spaces of dimension greater than one. It neither treats Hilbert-space best finite deficits nor their even-power boundary layers. Kadets, Martín, and Merí, *Norm equalities for operators on Banach spaces* (2007; earlier preprint 2006), study qualitative norm identities for functions of rank-one operators and pose the underlying square-property question, without the present sharp normalization and asymptotic. The public result *A one-scale rank-one projection test for the Daugavet property* establishes that rank-one projection identities at one scale suffice for the **qualitative** Daugavet property; it does not determine sharp Hilbert-space deficits or high even-power decay. A separate public rank-one Davis–Wielandt-radius study optimizes a different functional and does not imply the present operator-norm gap. In particular, the present computation is a quantitative obstruction benchmark in uniformly convex Hilbert spaces, rather than a claim of a new abstract Daugavet characterization.

## Limitations
Only real Hilbert spaces, norm-one rank-one operators, and **positive-sign even powers** are addressed. Odd powers have a different sign profile. The high-power result is first-order asymptotic along even degrees, without a claimed second-order expansion or uniqueness of the maximizer at every finite even degree beyond \(m=2\). The Lambert law does not assert anything about the global Daugavet deficit in arbitrary Banach spaces. The historical originality comparison cannot exclude unpublished or poorly indexed calculations of an equivalent elementary matrix optimization; independent scientific validation has not been performed.

## References
1. Johann Langemets, *Characterizing the Daugavet property by squares of rank-one operators*, arXiv:2609.27693v1 (first public 23 September 2026), https://arxiv.org/html/2609.27693v1.
2. V. Kadets, M. Martín, and J. Merí, *Norm equalities for operators on Banach spaces*, Indiana Univ. Math. J. **56** (2007), 2385–2412; preprint arXiv:math/0604102.
3. *A one-scale rank-one projection test for the Daugavet property*, public mathematical research record (4 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-scale-rank-one-projection-test-for-the-daugavet-property--9fa1c2436f2d.
4. *Sharp maximizer bifurcation and cubic-root cusp for rank-one Davis–Wielandt radii*, public mathematical research record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-maximizer-bifurcation-and-cubic-root-cusp-for-rank-one-dav--8213a478c378.
