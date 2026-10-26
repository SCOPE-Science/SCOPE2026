# A sharp stability radius and damping-induced divergence in three-step approximate proximal descent

## Finding

Consider three unprojected contraction-map evaluations of an implicit proximal saddle update, restarted at each outer iteration. For the two-dimensional monotone family defined below, their **sharp uniform outer-iteration contraction radius** is the algebraic number
\[
\rho_* = 0.940521095740431\ldots,
\]
uniquely specified by \(0<\rho_*<1\) and
\[
16\rho_*^{12}-32\rho_*^{10}+48\rho_*^8-104\rho_*^6+72\rho_*^4-8\rho_*^2+3=0.
\]
Every outer step strictly reduces Euclidean distance to the unique saddle for every member of the family whenever \(0<\gamma L<\rho_*\). At equality, one strongly convex–strongly concave member is an exact Euclidean isometry, so the strict uniform guarantee cannot include the endpoint. For any larger proposed uniform radius, an expanding member exists with \(\gamma L<1\). In particular, a strictly contracting *inner* Picard map does not guarantee stability of the three-call *outer* method.

An exact example has \(L=1\), \(a=2/3\), \(b=\sqrt5/3\), and \(\gamma=19/20\):
\[
\|z_{n+1}\|_2^2=\frac{1773279907}{1728000000}\|z_n\|_2^2>\|z_n\|_2^2
\]
for **every nonzero** outer state. This is damping-induced instability: at the same normalized step \(19/20\), the pure bilinear endpoint \(a=0\) and the uncoupled-gradient endpoint \(a=L\) are both strictly stable, whereas the intermediate strongly convex–strongly concave problem expands.

## Assumptions and scope

All calculations use exact arithmetic on \(\mathbb R^2\). For real parameters \(a\ge0\) and \(b\in\mathbb R\), take \(L=\sqrt{a^2+b^2}>0\) and the unconstrained saddle payoff
\[
 f_{a,b}(x,y)=\frac a2(x^2-y^2)-bxy.
\]
The saddle-gradient operator on \(z=(x,y)^{\mathsf T}\) is
\[
 F(z)=(\partial_x f,-\partial_y f)^{\mathsf T}=Kz,\qquad
 K=\begin{pmatrix}a&-b\\b&a\end{pmatrix}.
\]
The operator is monotone, Lipschitz with constant \(L\), and has unique zero \(z_*=0\). For \(a>0\), the payoff is strongly convex in \(x\) and strongly concave in \(y\).

For each outer state \(z_n\), start \(w_0=z_n\), apply exactly three inner evaluations
\[
 w_j=z_n-\gamma K w_{j-1}\quad(j=1,2,3),\qquad z_{n+1}=w_3,
\]
where \(0<\gamma L<1\). This is precisely the **unprojected three-call instance of Algorithm 1** in Cevher–Piliouras–Sim–Skoulakis (2023). It is not their recommended horizon-dependent Algorithm 2, which selects \(\gamma=1/(2L)\) and a growing logarithmic inner budget. No behavior of that full algorithm is contradicted or assessed here.

The statement is a **uniform** guarantee over this saddle family, and does not say that every instance diverges for \(\gamma L>\rho_*\). The exact implicit proximal-point step is \((I+\gamma K)^{-1}\), a strict contraction whenever \(a>0\), unlike the finite three-call approximation at the stated example.

## Proof

**1. Exact outer map.** Substituting the inner recurrence three times yields
\[
 z_{n+1}=P_3(\gamma K)z_n,\qquad P_3(\zeta)=1-\zeta+\zeta^2-\zeta^3=\frac{1-\zeta^4}{1+\zeta}.
\]
Let \(r=\gamma L\in(0,1)\) and \(c=a/L\in[0,1]\). The eigenvalues of \(\gamma K\) are \(r(c\pm i\sqrt{1-c^2})\). Because \(K\) is a real rotation–dilation matrix, \(P_3(\gamma K)\) is also such a matrix. Thus its squared Euclidean amplification is independent of the direction of the initial nonzero state, and is
\[
 q(r,c)=\frac{1+r^8-2r^4T_4(c)}{1+r^2+2rc},
 \qquad T_4(c)=8c^4-8c^2+1.
\]
The denominator is \(\lvert1+r(c+i\sqrt{1-c^2})\rvert^2>0\), and therefore
\[
 q(r,c)-1=\frac{G(r,c)}{1+r^2+2rc},\qquad
 G(r,c)=r^8-2r^4T_4(c)-r^2-2rc.
\]
Uniform strict contraction is equivalent to \(G(r,c)<0\) for every \(c\in[0,1]\).

**2. The small-radius region and angular boundaries.** Since \(\lvert T_4(c)\rvert\le1\) and \(c\ge0\),
\[
G(r,c)\le r^8+2r^4-r^2<0\quad (0<r\le1/2).
\]
Moreover, on both angular boundaries, for every \(0<r<1\),
\[
 G(r,0)=r^2(r^2+1)(r^4-r^2-1)<0,
\]
\[
 G(r,1)=r(r+1)^2(r^2-r+1)(r^3-r^2+r-2)<0.
\]
The final cubic is negative because \(r^3-r^2\le0\) and \(r-2<-1\). Consequently, any first loss of strict negativity before \(r=1\) must happen at an interior angle \(0<c<1\) satisfying both \(G=0\) and \(\partial_cG=0\).

**3. Complete elimination and unique candidate.** Direct polynomial elimination gives the **exact resultant identity**
\[
 \operatorname{Res}_{c}(G,\partial_cG)
 =65536r^{16}(4r^6+4r^4+4r^2+3)^2 H(r^2),
\]
where
\[
 H(u)=16u^6-32u^5+48u^4-104u^3+72u^2-8u+3.
\]
The polynomial \(H\) has exactly one zero in \((0,1)\). Indeed, letting \(u=t/(1+t)\) maps positive \(t\) bijectively to this interval, and
\[
 (1+t)^6H\!\left(\frac{t}{1+t}\right)
 =-5t^6+18t^5+133t^4+164t^3+77t^2+10t+3.
\]
Its coefficients, in decreasing degree, have **exactly one sign change**. By Descartes' rule of signs it has at most one positive zero; it has one since its value at \(t=0\) is positive and its leading coefficient is negative. Call the unique root of \(H\) in \((0,1)\) \(u_*\), and put \(\rho_*=\sqrt{u_*}\). Exact rational evaluations isolate \(u_*\) between \(884/1000\) and \(885/1000\).

**4. The candidate is genuine and sharp.** At \(r=19/20\) and \(c=2/3\), substitution gives
\[
 G\left(\frac{19}{20},\frac23\right)
 =\frac{172199486321}{2073600000000}>0.
\]
As every \(r\le1/2\) is strictly stable, continuity and compactness imply that there exists a first radius \(r_0\in(1/2,19/20)\) for which \(\max_{0\le c\le1}G(r_0,c)=0\). By step 2, the maximizing angle is interior, and so \(H(r_0^2)=0\). Uniqueness in step 3 forces \(r_0=\rho_*\). There can be no instability at any smaller radius, because its first onset would likewise require another zero of \(H\). This proves strict contraction throughout \(0<r<\rho_*\), and an exact neutral rotation at \(r=\rho_*\).

The neutral angle satisfies \(0<c_*<1\) (numerically \(c_*\approx0.6660362048\)), and hence \(a=Lc_*>0\) and \(b=L\sqrt{1-c_*^2}>0\). The outer update at this point is a real \(2\times2\) scaled rotation of unit modulus; every nonzero orbit retains its norm and does not converge to zero. The explicit point \(r=19/20<1\) is expanding, so any proposed uniform bound exceeding \(\rho_*\) is false: when the proposed upper bound is smaller than \(19/20\), continuity at the first crossing supplies an unstable radius just above \(\rho_*\), as uniqueness of interior tangencies prohibits a return to strict negativity before \(19/20\).

**5. Exact rational divergence certificate.** For \(a=2/3\), \(b=\sqrt5/3\), \(L=1\), \(r=\gamma=19/20\), direct polynomial matrix multiplication gives
\[
 P_3(\gamma K)^{\mathsf T}P_3(\gamma K)
 =\frac{1773279907}{1728000000}I_2.
\]
Repeated outer applications therefore satisfy
\[
 \|z_n\|_2^2=
 \left(\frac{1773279907}{1728000000}\right)^n\|z_0\|_2^2
\]
for every integer \(n\ge0\). Yet the corresponding inner Picard map \(w\mapsto z-\gamma Kw\) has Lipschitz constant \(19/20<1\), independent of \(z\); in contrast, the exact proximal map has strict Euclidean contraction because \(a>0\).

Finally, at fixed \(r=19/20\), both endpoint cases \(c=0\) and \(c=1\) are strictly contracting by the inequalities in step 2, while \(c=2/3\) is expanding. Continuity supplies an open unstable intermediate-damping interval. This proves the claimed stability–instability–stability phenomenon as curvature increases.

## Verification

The accompanying standalone `verify.py` uses exact symbolic arithmetic to check the polynomial resolvent identity, all coefficients in the elimination resultant, the Descartes substitution, rational isolation of \(u_*\), the stated rational amplification, and the matrix identity for the expanding witness. Run from the unpacked package with `python verify.py`; it requires `sympy>=1.12`. A finite grid is included only as a regression check; it is not used to infer any quantified stability statement. The reasoning in the proof, including boundary signs, the resultant and the unique-root argument, establishes all universal assertions.

## Relationship to prior work

Cevher, Piliouras, Sim, and Skoulakis (2023) introduced contraction-map approximations of a proximal saddle update. Their Algorithm 1 gives the **inner recurrence**, and Lemma 3.5 proves that its output approaches the implicit proximal solution when \(\gamma L<1\). Their end-to-end convergence statements prescribe the more conservative \(\gamma=1/(2L)\) and a horizon-dependent logarithmic inner budget, rather than asserting outer stability for three calls at all \(\gamma L<1\). The exact degree-three uniform radius and damping-induced divergence above do not follow from that approximation estimate.

Nemirovski's classical extragradient/prox method analyzes a different two-evaluation prox construction and monotone variational-inequality convergence. Our calculation instead covers exactly three restarted evaluations of the inner fixed-point equation, and derives its complete normal-plane outer stability frontier. The new claim does not encompass nonnormal operators or nonlinear problems.

## Limitations

The universal contraction statement is restricted to the normal two-dimensional saddle-gradient matrices \(aI+bJ\) with \(a\ge0\). A stability threshold over that restricted family is not a general stability theorem for all Lipschitz monotone nonlinear maps; nonnormal matrices can behave differently. It is an exact-arithmetic analysis of a **fixed three-call variant**, not a failure claim about the original logarithmic-budget method at its default step. The exact algebraic radius is obtained by elimination, not an optimized implementation recommendation. The originality assessment is a best-knowledge literature comparison and has not received an independent audit.

## References

- V. Cevher, G. Piliouras, R. Sim, and S. Skoulakis, *Min-Max Optimization Made Simple: Approximating the Proximal Point Method via Contraction Maps*, arXiv:2301.03931, first posted 2023-01-10; Algorithm 1 and Lemma 3.5, https://arxiv.org/abs/2301.03931.
- A. Nemirovski, *Prox-method with rate of convergence \(O(1/t)\) for variational inequalities with Lipschitz continuous monotone operators and smooth convex-concave saddle point problems*, SIAM Journal on Optimization 15 (2004), 229–251, doi:10.1137/S1052623403425629; author-accessible text https://www2.isye.gatech.edu/~nemirovs/SIOPT_MP_2004.pdf.
