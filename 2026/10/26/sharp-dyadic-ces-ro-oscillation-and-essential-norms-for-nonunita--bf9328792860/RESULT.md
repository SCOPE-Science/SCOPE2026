# Sharp dyadic Cesàro oscillation and essential norms for nonunitary Hilbert isometries

## Finding

**Theorem.** Let \(H\) be a complex Hilbert space and let \(V:H\to H\) be a **non-surjective isometry**: \(V^*V=I\) but \(VH\ne H\). For every integer \(n\ge1\) put
\[
 A_n(V)=\frac1n\sum_{j=0}^{n-1}V^j,\qquad D_n(V)=A_{2n}(V)-A_n(V).
\]
For every positive integer \(k\), let \(a_k(D_n(V))=\inf\{\|D_n(V)-F\|:\operatorname{rank}F<k\}\). Then
\[
 \boxed{\quad\|D_n(V)\|=\operatorname{dist}(D_n(V),\mathcal K(H))=a_k(D_n(V))=M_n\quad(k,n\ge1),\quad}
\]
where \(\mathcal K(H)\) denotes all compact operators on \(H\), and \(M_1=1\). For every integer \(n\ge2\), there is exactly one \(x_n\in(0,\pi)\) satisfying
\[
 \tan(x_n/2)=2n\tan(x_n/(2n)),
 \qquad M_n=\frac{\sin^2(x_n/2)}{n\sin(x_n/(2n))}.
\]
Write \(x_*\in(0,\pi)\) for the unique positive solution of \(\tan(x_*/2)=x_*\). Then, as \(n\to\infty\),
\[
 \boxed{\quad M_n=C+\frac{Cx_*^2}{24n^2}+O(n^{-4}),\qquad C=\frac{2x_*}{1+x_*^2}=0.7246113537767085\ldots.\quad}
\]
The next coefficient is positive: \(Cx_*^2/24=0.1640680577938391\ldots\). For **every** contraction \(T\) on a complex Hilbert space the universal bound \(\|A_{2n}(T)-A_n(T)\|\le M_n\) holds; scalar unitary contractions and every non-surjective Hilbert isometry realize it. Nevertheless, \(D_n(V)h\to0\) for each \(h\in H\), although \(\|D_n(V)\|\to C>0\).

## Assumptions and scope

All Hilbert spaces and operators are complex; no separability assumption is necessary. An isometry has \(\|Vh\|=\|h\|\) for all \(h\in H\), and its range is closed. Non-surjectivity is equivalent to \(\ker V^*\ne\{0\}\). The approximation-number convention is \(a_k(T)=\inf_{\operatorname{rank}F<k}\|T-F\|\) for \(k\ge1\). The essential norm is \(\operatorname{dist}(T,\mathcal K(H))\). All asymptotic error terms are absolute, independent of \(H\) and \(V\). This does not assert the same lower bound for arbitrary contractions: for example \(T=I\) has every dyadic difference zero.

## Proof

**1. Polynomial reduction and a uniform upper bound.** Define \(p_n(z)=\frac1{2n}\sum_{j=0}^{2n-1}z^j-\frac1n\sum_{j=0}^{n-1}z^j\). Factoring the geometric sums gives, for \(z\ne1\),
\[
 p_n(z)=-\frac{(1-z^n)^2}{2n(1-z)},\qquad p_n(1)=0.
\]
For \(z=e^{i\theta}\) and \(0<\theta\le\pi\), this yields
\[
 |p_n(e^{i\theta})|=f_n(\theta):=\frac{\sin^2(n\theta/2)}{n\sin(\theta/2)}.
\]
The modulus is even and periodic in the spectral phase. The von Neumann polynomial inequality (or unitary dilation) therefore proves for every Hilbert contraction \(T\)
\[
 \|p_n(T)\|\le\max_{|z|=1}|p_n(z)|=\max_{0\le\theta\le\pi} f_n(\theta)=:M_n.
\]
A scalar contraction \(T=e^{i\theta}I\), with \(\theta\) maximizing \(f_n\), realizes equality, proving the sharpness of the universal upper bound.

**2. Norm and essential-norm equality for every non-surjective isometry.** Choose a unit vector \(w\in\ker V^*\). Then \((V^j w)_{j\ge0}\) is an orthonormal sequence. Fix a point \(\zeta\) of modulus one. For integers \(L\ge1\) construct the unit vector
\[
 u_L=\frac1{\sqrt L}\sum_{j=L}^{2L-1}\zeta^{-j}V^jw.
\]
The support of \(u_L\) lies in the tail of an orthonormal sequence, so \(u_L\rightharpoonup0\) weakly. Direct cancellation of adjacent coefficients gives the **exact** identity \(\|(V-\zeta I)u_L\|=\sqrt{2/L}\). For fixed \(n\) and \(\zeta\), the polynomial \(p_n(z)-p_n(\zeta)\) is divisible by \(z-\zeta\), whence \(\|(p_n(V)-p_n(\zeta)I)u_L\|\to0\). For any compact \(K\), \(\|Ku_L\|\to0\). Consequently,
\[
 \|p_n(V)-K\|\ge \limsup_{L\to\infty}\|(p_n(V)-K)u_L\|=|p_n(\zeta)|.
\]
Choose \(\zeta\) maximizing \(|p_n|\). The upper bound in Step 1 and the choice \(K=0\) yield \(\|D_n(V)\|=\operatorname{dist}(D_n(V),\mathcal K(H))=M_n\). Since every finite-rank operator is compact and the zero operator has rank zero, the same equality holds for all \(a_k\).

**3. Exact finite-scale maximizer.** For \(n=1\), \(f_1(\theta)=\sin(\theta/2)\), whose maximum on \([0,\pi]\) is \(M_1=1\). For \(n\ge2\) and \(\theta\in[\pi/n,\pi]\), the numerator of \(f_n\) is at most one while its denominator is at least \(n\sin(\pi/(2n))\); hence \(f_n(\theta)\le f_n(\pi/n)\). As the derivative of \(f_n\) at \(\pi/n\) is strictly negative, the global maximum lies **strictly inside** \((0,\pi/n)\). On that interval its logarithmic derivative is
\[
 L_n(\theta):=\frac{f_n'(\theta)}{f_n(\theta)}=n\cot(n\theta/2)-\tfrac12\cot(\theta/2).
\]
Since \(\sin(nu)\le n\sin u\) on \(0\le u\le\pi/2\),
\[
 L_n'(\theta)=-\frac{n^2}{2\sin^2(n\theta/2)}+\frac1{4\sin^2(\theta/2)}\le-\frac1{4\sin^2(\theta/2)}<0.
\]
Moreover \(L_n(\theta)\to+\infty\) as \(\theta\downarrow0\) and \(L_n(\pi/n)<0\). Thus a unique \(\theta_n\in(0,\pi/n)\) is the global maximizer on \([0,\pi]\). Writing \(x_n=n\theta_n\) and setting \(L_n(\theta_n)=0\) gives \(\tan(x_n/2)=2n\tan(x_n/(2n))\), proving the claimed exact finite-scale formula.

**4. Limiting constant and its sharp correction.** Let \(F(x)=2\sin^2(x/2)/x\) on \((0,\pi]\). Its derivative has the sign of \(x\cot(x/2)-1\), so the unique interior maximum \(x_*\) satisfies \(\tan(x_*/2)=x_*\); existence and uniqueness follow because \(\tan(x/2)-x\) is negative just above zero and has strictly increasing derivative once \(x>1\). The maximizing locations in Step 3 stay in a compact subinterval of \((0,\pi)\) for large \(n\); uniform convergence of \(f_n(x/n)\) to \(F(x)\) and uniqueness of the limiting maximizer imply \(x_n\to x_*\). Taylor expansion yields
\[
 2n\tan\left(\frac{x}{2n}\right)=x+\frac{x^3}{12n^2}+O(n^{-4}),
\]
locally uniformly near \(x_*\). The derivative of \(\tan(x/2)-x\) at \(x_*\) is \((x_*^2-1)/2>0\), so the implicit-function expansion gives
\[
 x_n=x_*+\frac{x_*^3}{6(x_*^2-1)n^2}+O(n^{-4}).
\]
Finally
\[
 f_n(x/n)=F(x)\left(1+\frac{x^2}{24n^2}+O(n^{-4})\right)
\]
uniformly near \(x_*\). Since \(F'(x_*)=0\), displacement of the maximizing argument contributes only \(O(n^{-4})\), hence \(M_n=F(x_*)+F(x_*)x_*^2/(24n^2)+O(n^{-4})\). From \(\tan(x_*/2)=x_*\), one has \(\sin^2(x_*/2)=x_*^2/(1+x_*^2)\), so \(F(x_*)=2x_*/(1+x_*^2)=C\), as required.

**5. Strong but not norm convergence.** Each isometry is power-bounded and acts on a Hilbert space; by the Hilbert-space mean ergodic theorem \(A_n(V)\) converges strongly to the projection onto its fixed-vector space. Therefore \(D_n(V)=A_{2n}(V)-A_n(V)\to0\) strongly. Steps 2 and 4 show simultaneously \(\lim_n\|D_n(V)\|=\lim_n\|D_n(V)\|_{\mathrm e}=C>0\).

## Verification

The algebra in Step 1 can be checked by multiplying \(p_n(z)\) by \(1-z\), and the boundary value \(p_n(1)=0\) follows from the original polynomial. The weak-null vectors in Step 2 are normalized exactly and satisfy the residual identity exactly; no numerical estimate is used for the essential norm. Step 3 globally excludes all secondary trigonometric lobes and proves strict uniqueness, so numerical root searches need only target \((0,\pi)\). Bisection of \(\tan(x/2)-x\) near the nonzero root gives \(x_*=2.331122370414423\ldots\), \(C=0.724611353776709\ldots\), \(Cx_*^2/24=0.164068057793839\ldots\). Direct evaluation gives \(M_2=4/(3\sqrt3)=0.7698003589\ldots\), \(M_3=0.7436128025\ldots\), \(M_{10}=0.7262580115\ldots\), and \(M_{100}=0.7246277612\ldots\). These computations are checks, not substitutes for Steps 1–5. One can reproduce them with ordinary bisection of the strictly decreasing logarithmic derivative or the equivalent tangent equation.

## Relationship to prior work

Kalmes and Peša, *Mean and pointwise ergodicity for composition operators on rearrangement-invariant spaces* (arXiv:2510.12459, first public 2025-10-14), examine norm/pointwise convergence for a broad class of composition operators; their Example 5.12 treats forward-index sequence shifts. Chalmoukis, Colzani, Gariboldi and Monguzzi, *On the speed of convergence in the ergodic theorem for shift operators* (arXiv:2312.08922, 2023), prove pointwise and fixed-vector rates and in the proof of their Theorem 1.2 use \(\|A_n(V)\|=1\) on shift components. These are **single-scale** or vectorwise properties, and do not provide the sharp **two-scale** finite \(M_n\), its unique maximizing phase and correction, or the flat compact-approximation profile proved here. Wold decomposition, von Neumann's polynomial inequality and standard Toeplitz symbol estimates explain the functional-calculus *reduction*; the nontrivial remaining ingredient is the global exact optimizer and its sharp asymptotic. Jones, Kaufman, Rosenblatt and Wierdl (1998) establish oscillation inequalities for ergodic averages; no exact universal dyadic operator-norm constant was identifiable from the accessible abstract, and its inaccessible full text is a priority caveat.

## Limitations

The exact lower bound requires a nonzero unilateral-shift component, expressed intrinsically by \(VH\ne H\). A surjective unitary with a restricted spectrum can have a smaller dyadic difference norm, and a contraction may have none. The result concerns a **single dyadic scale difference**, not the norm of a full square-function or variation operator, and says nothing about rates for a fixed vector beyond strong convergence. Classical polynomial shift/Toeplitz essential-norm formulas subsume the reduction to a circle supremum; their existence must be distinguished from an explicit evaluation and \(n^{-2}\) correction. The older oscillation literature is extensive; bibliographic priority beyond the inspected sources requires independent examination. No independent proof audit has been performed.

## References

1. T. Kalmes and D. Peša, *Mean and pointwise ergodicity for composition operators on rearrangement-invariant spaces*, arXiv:2510.12459, first posted 14 October 2025. https://arxiv.org/abs/2510.12459
2. N. Chalmoukis, L. Colzani, B. Gariboldi and A. Monguzzi, *On the speed of convergence in the ergodic theorem for shift operators*, arXiv:2312.08922 (2023); Canadian Journal of Mathematics, published online 4 November 2024. https://arxiv.org/abs/2312.08922 ; https://doi.org/10.4153/S0008414X24000658
3. R. L. Jones, R. Kaufman, J. M. Rosenblatt and M. Wierdl, *Oscillation in ergodic theory*, Ergodic Theory and Dynamical Systems 18 (1998), 889–935. https://doi.org/10.1017/S0143385798108349
4. A. Dobrick, *Banach's principle in vector lattices*, arXiv:2608.14272, first posted 14 August 2026. https://arxiv.org/abs/2608.14272
