# A sharp stretched-exponential coefficient law for a golden-mean flip zeta

## Finding

For the natural reversal (flip) of the two-sided golden-mean shift, the infinite-dihedral Lind zeta function has the exact form
\[
\mathcal Z(z)=\frac{1}{\sqrt{1-z^2-z^4}}\exp\left(\frac{z+2z^2+z^3+z^4}{1-z^2-z^4}\right).
\]
The square root is the formal branch with constant coefficient one. Let \(c_n=[z^n]\mathcal Z(z)\), \(\varphi=(1+\sqrt5)/2\), and \(\rho=\varphi^{-1/2}\). Define the polynomial \(N(z)=z+2z^2+z^3+z^4\) and the positive constants
\[
p=2\rho^2+4\rho^4,\qquad A=\frac{N(\rho)}p,\qquad
B=-\frac{\rho N'(\rho)}p+\frac{N(\rho)(\rho^2+6\rho^4)}{p^2}.
\]
Then, as the integer \(n\) tends to infinity,
\[
\boxed{\displaystyle
c_n=\frac{e^{B+A/2}}{2\sqrt{\pi p}}\frac{\rho^{-n}}{\sqrt n}
\exp(2\sqrt{An})\left(1+O(n^{-1/2})\right).}
\]
Numerically \(A=1.04563122925493\ldots\), and the displayed leading constant is \(0.08988631850254\ldots\). The invariant of interest is the **coefficient growth** of the dihedral dynamical zeta function; the general definition and matrix formula for the function itself predate this calculation.

## Assumptions and scope

Let \(X\) be the compact two-sided subshift on \(\{0,1\}^{\mathbb Z}\) forbidding adjacent ones. Let \(T\) shift all coordinates one position and let the flip \(J\) act by \((Jx)_j=x_{-j}\). The relations \(J^2=1\) and \(JTJ=T^{-1}\) give an action of \(G=D_\infty=\langle a,b\mid b^2=1,\ bab=a^{-1}\rangle\), where \(a\) acts as \(T\) and \(b\) as \(J\). For any finite-index subgroup \(H\le G\), \(\operatorname{Fix}(H)\) is the set of points fixed by every element of \(H\). Define the formal Lind zeta series
\[
\mathcal Z(z)=\exp\left(\sum_{H\le G,\,[G:H]<\infty}
\frac{|\operatorname{Fix}(H)|}{[G:H]}z^{[G:H]}\right).
\]
Every fixed-point set in this definition is finite. All coefficient assertions concern this formal series, not the number of primitive dihedral orbits of bounded length and not the classical Artin–Mazur zeta function. The asymptotic uses positive integer \(n\) without a parity restriction.

## Proof

**1. Subgroups and finite fixed points.** A finite-index subgroup of \(D_\infty\) is either \(\langle a^m\rangle\), of index \(2m\), or \(\langle a^n,a^jb\rangle\), of index \(n\), where \(m,n\ge1\) and \(j\in\{0,\ldots,n-1\}\). These are the standard finite-index subgroup families. In the golden-mean shift, the number of points fixed by \(T^m\) is
\[
L_m=F_{m-1}+F_{m+1}=\operatorname{tr}\begin{pmatrix}1&1\\1&0\end{pmatrix}^{m},
\]
with \(F_0=0\), \(F_1=1\). Indeed, these fixed points are the cyclic binary words of length \(m\) without adjacent ones.

For the reflection subgroups, fixing \(T^n\) and \(T^jJ\) means that the cyclic word satisfies \(x_i=x_{j-i\pmod n}\). If \(n=2m+1\), each reflection has one fixed vertex and one fixed edge; the endpoints of that fixed edge are forced to zero, leaving a path on \(m\) free vertices. There are \(F_{m+2}\) independent-set configurations. If \(n=2m\), reflections with even \(j\) fix two opposite vertices and give independent sets on a path of \(m+1\) vertices, counted by \(F_{m+3}\); those with odd \(j\) fix two opposite edges, forcing four incident vertices to zero and leaving a path of \(m-2\) free vertices, counted by \(F_m\) (the empty-path convention covers \(m=1\)). Thus the average over the \(n\) reflections is
\[
r_n=\frac1n\sum_{j=0}^{n-1}|\operatorname{Fix}(T^n,T^jJ)|
=F_{\lfloor n/2\rfloor+2},
\]
where the even case uses \((F_{m+3}+F_m)/2=F_{m+2}\).

**2. Exact zeta function.** The subgroup classification and geometric-series identity for the Lucas numbers give
\[
\log\mathcal Z(z)=\sum_{n\ge1}r_nz^n+\sum_{m\ge1}\frac{L_m}{2m}z^{2m}
=R(z)-\frac12\log P(z),
\]
where \(P(z)=1-z^2-z^4\). For the Fibonacci recurrence,
\[
R(z)=\sum_{n\ge1}F_{\lfloor n/2\rfloor+2}z^n
=\frac{(1+z)(1+z^2)}{1-z^2-z^4}-1
=\frac{N(z)}{P(z)}.
\]
The last logarithm follows from \(\sum_{m\ge1}L_mt^m/m=-\log(1-t-t^2)\). Exponentiating gives the stated exact function.

**3. Two real dominant singularities and their unequal strengths.** The factorization
\[
P(z)=(1-\varphi z^2)(1+\varphi^{-1}z^2)
\]
shows that the singularities of smallest modulus are \(z=\rho\) and \(z=-\rho\); the other two poles have modulus \(\sqrt\varphi>\rho\). Set \(w=1-z/\rho\). Taylor expansion at the positive singularity yields
\[
P(z)=pw-(\rho^2+6\rho^4)w^2+O(w^3),\qquad
R(z)=\frac A w+B+O(w).
\]
Hence the local form is
\[
\mathcal Z(z)=p^{-1/2}w^{-1/2}e^{A/w+B}(1+O(w)).
\]
At the negative singularity, writing \(w_-=1+z/\rho\), the corresponding exponential coefficient is
\[
A_-:=\frac{N(-\rho)}p=0.12518916399501\ldots\quad\text{with}\quad 0<A_-<A.
\]
Both inequalities follow either by inserting the exact expressions for \(\rho\), or by \(N(\rho)>N(-\rho)>0\). This unequal residue is essential: the negative singularity makes an exponentially smaller contribution to coefficients, despite lying on the same convergence circle.

**4. Positive saddle and leading constant.** Apply Cauchy's coefficient formula on the circle \(|z|=\rho(1-\delta)\), where \(\delta=\sqrt{A/n}\). On its arc near the positive real radius, writing \(z=\rho(1-\delta)e^{i\theta}\), the natural contributing width is \(|\theta|=O(\delta^{3/2})\). Uniformly for \(|\theta|\le\delta^{3/2}\log(1/\delta)\), the real quadratic term in the exponent is \(-A\theta^2/\delta^3\); linear imaginary terms have size \(O(n^{1/2}\theta)\) after the saddle choice and contribute only a relative \(O(n^{-1/2})\) after symmetric Gaussian integration. Higher terms and the analytic prefactor have the same or smaller integrated relative order. Also,
\[
(1-\delta)^{-n}=\exp\left(\sqrt{An}+\frac A2+O(n^{-1/2})\right),\qquad
R(\rho(1-\delta))=\sqrt{An}+B+O(n^{-1/2}).
\]
The Gaussian integral is
\[
\frac1{2\pi}\int_{-\infty}^{\infty}
\exp(-A\theta^2/\delta^3)\,d\theta
=\frac{\delta^{3/2}}{2\sqrt{\pi A}}.
\]
Multiplying this by the local factor \(p^{-1/2}\delta^{-1/2}\) produces \(1/(2\sqrt{\pi pn})\). On the remainder of a neighborhood of \(\rho\), the real part of \(A/(1-z/\rho)\) is uniformly smaller than at the saddle by a positive multiple of \(\theta^2/\delta^3\), giving a negligible Gaussian tail. Outside fixed small neighborhoods of the two real singularities the analytic exponent is bounded; near \(-\rho\) it is at most \(A_-/\delta+O(1)\), exponentially below \(A/\delta\) because \(A_-<A\). Thus no other contour arc contributes to leading order. Standard Taylor estimates of the symmetric saddle integral yield the displayed relative \(O(n^{-1/2})\) remainder.

Combining the exponential, Gaussian, algebraic, and analytic factors proves the formula for all \(n\to\infty\).

## Verification

The accompanying standalone standard-library Python program `verify.py` enumerates all cyclic golden-mean words and reflection axes for lengths \(1\) through \(13\), verifies the rational reflection generating-function recurrence exactly through level \(35\), and independently builds initial coefficients from the fixed-point logarithm. It also computes normalized coefficients through level \(1200\) and checks their convergence towards the proven asymptotic. Its completed output begins with `VERIFY_OK`. These finite checks are consistency checks only; the singularity and saddle arguments above prove the infinite asymptotic.

## Relationship to prior work

Kim, Lee, and Park (2003) defined zeta functions of flip systems and proved their general decomposition into a square root of the Artin–Mazur zeta and a reflection-series exponential, including matrix formulas for shifts of finite type. This supplies the overarching framework and is **not new**. Miles (2015) placed dynamical zeta functions into a broader group-action setting. Ryu (2014) studied dihedral topological Markov chains and general zeta data. Nordin and Md Noorani (2021) obtained prime-orbit counting laws for dihedral shifts, a different counting sequence from the coefficient sequence here. The present result specifically evaluates the coefficient growth for the natural golden-mean flip and resolves the competing positive and negative dominant singularities to obtain a sharp constant and stretched-exponential factor. General saddle-point methods are classical and are credited as the analytic technique.

## Limitations

This theorem treats one specified reflection of one mixing binary shift of finite type, with the usual Lind zeta normalization. It does not classify flip zeta functions for all matrices, primitive orbit counts, or arbitrary dihedral actions. The general decomposition and the underlying Fibonacci identities are pre-existing. Earlier unindexed literature may contain an equivalent specialization; the bibliographic comparison does not certify absolute historical priority.

## References

1. Young-One Kim, Jungseob Lee, Kyewon K. Park, *A zeta function for flip systems*, Pacific Journal of Mathematics **209** (2003), 289–301. DOI: 10.2140/PJM.2003.209.289. Full text: https://msp.org/pjm/2003/209-2/pjm-v209-n2-p06-p.pdf.
2. Richard Miles, *A dynamical zeta function for group actions*, arXiv:1506.08555, initially submitted 2015-06-29. https://arxiv.org/abs/1506.08555.
3. Sieye Ryu, *On conjugacy invariants of \(D_\infty\)-topological Markov chains*, arXiv:1407.3988 (2014). https://arxiv.org/abs/1407.3988.
4. Azmeer Nordin and Mohd Salmi Md Noorani, *Counting finite orbits for the flip systems of shifts of finite type*, Discrete and Continuous Dynamical Systems **41** (2021). DOI: 10.3934/dcds.2021046.
5. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), saddle-point methods for exponential singularities.
