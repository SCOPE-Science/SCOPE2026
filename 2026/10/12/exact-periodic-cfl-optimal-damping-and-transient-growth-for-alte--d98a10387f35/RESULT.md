# Exact periodic CFL, optimal damping, and transient growth for alternating Adams–Bashforth two

## Finding
Consider the classical **variable-step, polynomial-interpolation Adams–Bashforth two** method applied to the scalar dissipative initial-value problem \(u'=-\lambda u\), where \(\lambda>0\). Fix alternating positive physical step lengths \(H,h,H,h,\ldots\), and write \(x=\lambda H\), \(y=\lambda h\), and \(L=x+y\). On the two-component value state \((u_k,u_{k-1})^\mathsf T\), let \(P(x,y)\) be the amplification matrix for a period consisting of an \(H\) step followed by an \(h\) step. Then
\[
\det P=\frac{xy}{4},\qquad
\operatorname{tr}P=1-L+\frac{L^2}{2}+\frac{xy}{4}.
\]
Three exact conclusions hold.

1. **Ratio-independent stability:** every solution tends to zero exactly when \(0<L<2\). For \(L=2\), every solution is bounded but some do not decay; for \(L>2\), some solutions grow exponentially. Thus the sharp negative-real decay stability boundary depends on the *sum*, not the ratio, of the two physical steps.
2. **Unique globally fastest two-step damping:** among all \(x,y>0\), the minimum Floquet spectral radius is \(1/3\), attained only at \(x=y=2/3\). More strongly, at every fixed \(L\in(0,2)\), equal steps \(x=y=L/2\) uniquely minimize the Floquet spectral radius. At the overall optimum, \(P(2/3,2/3)=I/3\), so every two-component perturbation is contracted by exactly \(1/3\) per period.
3. **Arbitrarily large stable transients:** for every fixed \(L\in(0,2)\), with \(x=L-y\),
\[
\lim_{y\downarrow0} y\,\|P(L-y,y)\|_2=L^2,
\qquad
\lim_{y\downarrow0}\rho(P(L-y,y))=1-L+\frac{L^2}{2}<1.
\]
Hence the period map can exhibit unbounded one-period Euclidean amplification while remaining asymptotically stable. Here \(\rho\) is spectral radius and \(\|\cdot\|_2\) is the Euclidean operator norm.

## Assumptions and scope
The variable-step AB2 formula extrapolates the previous two derivative samples *linearly in physical time* before integrating across the new step; it is not a Nordsieck coordinate restart or a constant-coefficient AB2 formula used with irregular steps. Explicitly, with positive current and previous steps \(s_k,s_{k-1}\),
\[
u_{k+1}=u_k+s_k\left[f_k+\frac{s_k}{2s_{k-1}}(f_k-f_{k-1})\right],\quad f_j=-\lambda u_j.
\]
We consider exact-arithmetic, infinite, two-periodic repetition and arbitrary two starting values. The norm in the transient statement measures perturbations in the **two stored solution values**, not in an alternative time-scaled Nordsieck state. The rate minimizes the error amplification per *two derivative evaluations* (one period); it is not a time-accuracy optimum, an adaptive controller theorem, or a claim for general nonlinear/complex-stiff equations.

## Proof
**1. Transfer matrix and invariants.** Writing \(a=\lambda s_k\), \(b=\lambda s_{k-1}\), the update is \(v_{k+1}=M(a,b)v_k\), where \(v_k=(u_k,u_{k-1})^\mathsf T\) and
\[
M(a,b)=\begin{pmatrix}
1-a-a^2/(2b)&a^2/(2b)\\
1&0
\end{pmatrix}.
\]
The two-step map is \(P(x,y)=M(y,x)M(x,y)\). Direct multiplication yields the asserted trace and determinant. Write \(d=xy/4\) and \(F(L)=1-L+L^2/2\). The characteristic polynomial is
\[
\Phi_{L,d}(z)=z^2-(F(L)+d)z+d,
\qquad 0<d\le L^2/16,
\]
with equality in the upper bound for \(d\) exactly when \(x=y\).

**2. Stability, including its boundary.** For \(0<L<2\), \(F(L)\in[1/2,1)\), \(d\le L^2/16<1/4\), and
\[
1-\operatorname{tr}P+\det P=L(1-L/2)>0,
\qquad 1+\operatorname{tr}P+\det P=1+F(L)+2d>0.
\]
These are the strict quadratic Schur conditions, together with \(d<1\), hence both eigenvalues have modulus below one. In fact they are positive and real: for the discriminant \(\Delta(d)=(F+d)^2-4d\),
\[
\Delta'(d)=2(F+d)-4<0,
\quad
\Delta(L^2/16)=\frac{(3L-4)^2(9L^2-8L+16)}{256}\ge0.
\]
Thus \(\Delta\ge0\), and equality occurs only for \(L=4/3\) and \(x=y=2/3\). When \(L=2\), \(F=1\), so the characteristic roots are exactly \(1\) and \(d\le1/4\), distinct; consequently all powers are bounded, but not all state vectors decay. When \(L>2\), \(F(L)>1\) and \(\Phi_{L,d}(1)=L(1-L/2)<0\), so \(\Phi_{L,d}\) has one real root larger than one. (Indeed the polynomial is positive for sufficiently large positive arguments.) This establishes the trichotomy for every starting pair.

**3. Fixed-period optimality.** For a fixed \(L\in(0,2)\), let \(q(d)\) denote the larger positive characteristic root. For \(d<L^2/16\), the roots are distinct, so implicit differentiation of \(q^2-(F+d)q+d=0\) gives
\[
q'(d)=\frac{q(d)-1}{q(d)-q_-(d)}<0,
\]
using \(0<q_-(d)<q(d)<1\). By continuity, \(q\) is strictly minimized when \(d\) is maximal, i.e. precisely when \(x=y=L/2\). The repeated-root endpoint at \(L=4/3\) is covered by continuity and strict decrease on the interior.

**4. Global optimality.** For equal steps \(x=y=z>0\), the one-step matrix \(M(z,z)\) has opposite-sign eigenvalues \(r_+(z)>0>r_-(z)\), which are the roots of
\[
r^2-(1-3z/2)r-z/2=0.
\]
The period-map radius is \(\max\{r_+(z)^2,r_-(z)^2\}\). Set \(c=1/\sqrt3\). For \(0<z\le2/3\), evaluating this quadratic at \(c\) shows it is nonpositive, hence \(r_+(z)\ge c\), strictly unless \(z=2/3\). For \(z\ge2/3\), evaluation at \(-c\) shows it is nonpositive, hence \(-r_-(z)\ge c\), strictly unless \(z=2/3\). Thus the equal-step period radius is at least \(1/3\), attaining equality only at \(z=2/3\). Step 3 handles unequal steps for \(L<2\), and Step 2 excludes \(L\ge2\) from global optimality. Direct substitution gives \(M(2/3,2/3)^2=I/3\).

**5. Transient limit.** Fix \(L\in(0,2)\), set \(x=L-y\), and let \(y\downarrow0\). The explicit matrices in Step 1 imply
\[
y P(L-y,y)\longrightarrow
\frac{L^2}{2}\begin{pmatrix}-1&1\\-1&1\end{pmatrix}.
\]
The displayed rank-one matrix has operator norm \(L^2\), proving the norm limit. Since \(d\to0\) and \(\operatorname{tr}P\to F(L)>0\), its eigenvalues tend to \(F(L)\) and \(0\), proving the spectral-radius limit. This establishes a genuine transient-versus-asymptotic distinction; it does not claim unbounded powers for any one fixed positive pair \((x,y)\) inside the stable region.

## Verification
The accompanying standalone standard-library Python checker (`checker.py`) independently constructs both one-step matrices using exact rational arithmetic, multiplies them, and checks the trace, determinant, characteristic boundary, discriminant factorization, and many fixed-period comparisons. It also checks the scalar optimum \(P(2/3,2/3)=I/3\) exactly and numerical transient scaling for increasingly unequal positive step pairs. Run `python3 checker.py`. Such finite checks are diagnostic, not a proof over all positive real step sizes; the proof above supplies the universal quantifiers.

## Relationship to prior work
Gear and Tu (1974), Skeel and Jackson (1983), and Calvo, Lisbona, and Montijano (1989) study stability of variable-step multistep/Nordsieck formulas, particularly step-ratio and zero-stability issues. The accessible descriptions do not state the combined scalar negative-real **two-period Floquet trace law, sharp total-step threshold, unique global damping optimum, and singular transient limit** established here. The oldest complete texts were not available, so historically equivalent specializations remain possible. Sandu and Constantinescu (2007) construct multirate Adams schemes for different spatial components under local CFL restrictions, not the same scalar sequence of alternated AB2 steps. Hadjimichael, Ketcheson, Lóczi, and Németh (2015 arXiv submission; later version inspected) optimize different variable-step SSP multistep formulas and their nonlinear monotonicity restrictions, not the present conventional interpolatory AB2 periodic optimization. The classical fixed-step AB2 scalar stability polynomial is not claimed as new.

## Limitations
The result concerns the real negative test eigenvalue \(-\lambda\), not all complex eigenvalues, nonnormal matrices, or nonlinear IVPs. It compares the asymptotic period radius and the Euclidean stored-value transient, not local truncation error, finite-time global accuracy, or every possible initialization. Sources published in print before their precisely dated online records may be older than the chosen day-verified citation anchor. Full texts of the most directly related early variable-step stability papers were unavailable through accessible lawful channels, leaving a nonzero historical-coverage risk. No independent mathematical audit has been conducted.

## References
- C. W. Gear and K. W. Tu, "The Effect of Variable Mesh Size on the Stability of Multistep Methods," *SIAM J. Numer. Anal.* **11** (1974), 1025–1043. DOI: `10.1137/0711079`.
- R. D. Skeel and L. W. Jackson, "The Stability of Variable-Stepsize Nordsieck Methods," *SIAM J. Numer. Anal.* **20** (1983), 840–853. DOI: `10.1137/0720056`.
- M. Calvo, F. Lisbona, and J. Montijano, "On the Stability of Interpolatory Variable-Stepsize Adams Methods in Nordsieck Form," *SIAM J. Numer. Anal.* **26** (1989), 946–962. DOI: `10.1137/0726052` (day-verified online record: 2006-07-14).
- A. Sandu and E. M. Constantinescu, "Multirate Explicit Adams Methods for Time Integration of Conservation Laws," technical report TR-07-30 (2007), `https://vtechworks.lib.vt.edu/bitstreams/e7d20454-b131-46be-a110-dcde8005bb77/download`.
- Y. Hadjimichael, D. I. Ketcheson, L. Lóczi, and A. Németh, "Strong Stability Preserving Explicit Linear Multistep Methods with Variable Step Size," arXiv:`1504.04107` (initial submission 2015-04-16).
