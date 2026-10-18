# Sharp quadratic Steinhaus modulus of a scalar–Hilbert one-sum

## Finding

**Theorem.** Let \(H\) be a real Hilbert space with \(\dim H\ge3\), possibly infinite-dimensional. Set \(X=\mathbb R\oplus_1H\), endowed with \(\|(s,u)\|=|s|+\|u\|_H\). For \(0<d<2\), \(a>0\), define the uniform Steinhaus modulus
\[
U_X(d;a)=\inf_{\substack{x,y\in S_X\\\|x-y\|\ge d}}\ \sup_{\|z\|\le a}\big|\|x+z\|-\|y+z\|\big|.
\]
Then for every fixed \(0<d<2\),
\[
\boxed{\lim_{a\downarrow0}\frac{U_X(d;a)}{a^2}=\frac{d}{4-2d}.}
\]
In particular \(X\) has uniform Steinhaus property \((S)\). Its small-radius separation decays quadratically, in contrast to the linear modulus known for atomless real \(L^1\).

## Assumptions and scope

Scalars are real. All norms of elements of \(H\) are Hilbert norms. The Hilbert dimension condition guarantees a unit direction orthogonal to any two given Hilbert vectors. The separation \(d\) is fixed before \(a\downarrow0\); no uniformity as \(d\uparrow2\) is claimed. We write \(B_{x,y}(a)=\sup_{\|z\|\le a}|\|x+z\|-\|y+z\||\). The infimum defining \(U_X\) is not assumed attained.

## Proof

**1. Sharp upper bound.** Fix \(d\in(0,2)\), put \(\delta=d/2\) and choose a unit vector \(e\in H\). For sufficiently small \(a>0\), let \(\varepsilon=\sqrt a\), \(R=1-\varepsilon\), \(S=1-\varepsilon-\delta>0\), and
\[
x=(\varepsilon,Re),\qquad y=(\varepsilon+\delta,Se).
\]
Both are unit vectors, and \(\|x-y\|=\delta+\|\delta e\|=d\). Write a perturbation as \(z=(r,w)\), with \(|r|+\|w\|\le a\). Since \(a<\varepsilon\), the scalar components of \(x+z\) and \(y+z\) stay positive. With \(w_\perp=w-\langle w,e\rangle e\), the Taylor expansion of the Hilbert norm on the compact radial interval containing \([S,R]\) gives, uniformly over \(\|w\|\le a\),
\[
\|x+z\|-\|y+z\|=\frac{\|w_\perp\|^2}{2}\left(\frac1R-\frac1S\right)+O_d(a^3).
\]
Indeed, \(\|Re+w\|=R+\langle w,e\rangle+\|w_\perp\|^2/(2R)+O_d(a^3)\), and analogously for \(S\). Hence
\[
 B_{x,y}(a)\le\frac{a^2\delta}{2RS}+O_d(a^3),\qquad
 \limsup_{a\downarrow0}\frac{U_X(d;a)}{a^2}\le\frac{\delta}{2(1-\delta)}.
\]
The transverse perturbation \(z=(0,a e_\perp)\), where \(e_\perp\perp e\) is unit, attains the same leading coefficient for this explicit family.

**2. Lower bound: reduce to nearly parallel Hilbert components.** Consider any sequence \(a_n\downarrow0\) and unit pairs \(x_n=(s_n,u_n)\), \(y_n=(t_n,v_n)\) with \(\|x_n-y_n\|\ge d\). Write \(B_n=B_{x_n,y_n}(a_n)\). If \(B_n/a_n^2\to\infty\) along a subsequence, that subsequence already obeys the desired lower bound. It therefore suffices to study arbitrary subsequences with \(B_n\le K a_n^2\) for some finite \(K\). Let \(R_n=\|u_n\|\), \(S_n=\|v_n\|\), and pass to a subsequence on which these scalar lengths converge to \(R,S\in[0,1]\).

For any unit \(q_n\in H\) orthogonal to both \(u_n,v_n\), the perturbation \(z=(0,a_nq_n)\) yields the **exact** identity
\[
\|x_n+z\|-\|y_n+z\|=h_{a_n}(R_n)-h_{a_n}(S_n),
\quad h_a(r)=\sqrt{r^2+a^2}-r=\frac{a^2}{\sqrt{r^2+a^2}+r}.
\]
The equality uses \(|s_n|+R_n=|t_n|+S_n=1\). Consequently \(B_n\ge|h_{a_n}(R_n)-h_{a_n}(S_n)|\). If exactly one of \(R,S\) were zero, this inequality divided by \(a_n^2\) would diverge, contradicting \(B_n\le Ka_n^2\). If both were zero, then \(|s_n|,|t_n|\to1\). Equal eventual scalar signs would give \(\|x_n-y_n\|\to0\). Opposite scalar signs would give, by perturbing with \((\pm a_n,0)\), a difference of perturbed-norm differences of \(4a_n\), whereas each difference has absolute value at most \(B_n\), again impossible. Thus
\[
R>0,\qquad S>0.
\]

Set \(e_n=u_n/R_n\) and \(f_n=v_n/S_n\) for large \(n\). For any unit \(q\in H\), evaluate the norm difference at \(z=(0,a_nq)\) and \(z=(0,-a_nq)\). Uniform Taylor expansion at the positive radii \(R_n,S_n\) shows
\[
2a_n|\langle e_n-f_n,q\rangle|\le 2B_n+O(a_n^3).
\]
Taking a supremum over unit \(q\) gives \(\|e_n-f_n\|\le B_n/a_n+O(a_n^2)=O(a_n)\). Thus the Hilbert directions are asymptotically parallel; no compactness of the unit sphere of \(H\) is used.

**3. The scalar signs must agree.** For any real \(r\), set \(F_n(r)=\|x_n+(r,0)\|-\|y_n+(r,0)\|\). Then \(|F_n(\pm a_n)|\le B_n\), and the elementary identity
\[
|s+a|-|s-a|=2\operatorname{sgn}(s)\min\{|s|,a\}
\]
(with \(\operatorname{sgn}(0)=0\)) implies
\[
\big|\operatorname{sgn}(s_n)\min\{|s_n|,a_n\}-\operatorname{sgn}(t_n)\min\{|t_n|,a_n\}\big|\le B_n.
\]
If the scalar signs were opposite or one scalar were zero along a subsequence, both scalar magnitudes would have to tend to zero (indeed every nonzero magnitude then is at most \(B_n\) for large \(n\), as \(B_n<a_n\)). Hence \(R_n,S_n\to1\); the previous step would give \(\|x_n-y_n\|\to0\), contradicting separation. If both scalars were zero, the same contradiction follows directly. Accordingly the scalar components have the same nonzero sign eventually.

Since \(|s_n|=1-R_n\) and \(|t_n|=1-S_n\), their scalar distance is now \(|R_n-S_n|\). Also \(\|R_ne_n-S_nf_n\|=|R_n-S_n|+o(1)\). Therefore
\[
 d\le\liminf_n\|x_n-y_n\|=2|R-S|,
 \qquad\delta_0:=|R-S|\ge d/2.
\]

**4. Sharp curvature comparison.** As \(R,S>0\), the exact perpendicular-perturbation estimate from Step 2 yields
\[
\liminf_n\frac{B_n}{a_n^2}
 \ge\left|\frac1{2R}-\frac1{2S}\right|=\frac{\delta_0}{2RS}.
\]
Because \(0<R,S\le1\) and their difference is \(\delta_0\), the larger is at most \(1\) and the smaller at most \(1-\delta_0\), so \(RS\le1-\delta_0\). It follows that
\[
\liminf_n\frac{B_n}{a_n^2}\ge
 \frac{\delta_0}{2(1-\delta_0)}\ge\frac{d}{4-2d}.
\]
Apply this sequence argument to approximately minimizing pairs, choosing \(B_n\le U_X(d;a_n)+a_n^3\), to obtain the same bound for the modulus itself. The upper bound from Step 1 proves the limit.

**5. Uniform property.** The strictly positive limit implies \(U_X(d;a)>0\) for all sufficiently small \(a\) at each fixed \(d\in(0,2)\). Because \(U_X(d;a)\) is nondecreasing in \(a\), it is positive for every \(a>0\), exactly the definition of uniform \((S)\).

## Verification

The sharp upper family is explicit and has unit norms and distance exactly \(d\). The lower proof treats all scalar-sign configurations, possible zero Hilbert components, arbitrary Hilbert directions, and the full infimum over separated unit pairs. Critical identities are the radial square-root formula for perpendicular perturbations, symmetric finite differences of the real absolute value, and uniform second-order Hilbert Taylor expansions at positive radii. The included checker evaluates the explicit family and its sharp transverse perturbation at decreasing scales; those finite calculations corroborate but do not replace the universal proof.

## Relationship to prior work

Johnson and Kania [1] introduced the uniform Steinhaus modulus and computed a **linear** exact formula for atomless real \(L^1\); their full preprint addresses different ambient geometries and does not determine the quadratic coefficient for this mixed atomic–Hilbert one-sum. Kania and Kochanek [2] studied ordinary property \((S)\), including a mixed \(\ell_1\)- and Hilbert-sum example, without the asserted quantitative limit. Two subsequent direct-sum findings [3,4] establish qualitative property \((S)\) for certain sums and the sharp obstruction arising from two real scalar blocks; their conclusions do not supply the sharp small-scale modulus for one real scalar and one Hilbert block. The current theorem quantifies the curvature cost of separating nearly collinear pairs in this borderline one-sum.

## Limitations

The result requires real scalars, a Hilbert block of dimension at least three, and fixed \(0<d<2\). It proves the leading small-radius coefficient only; it neither determines the exact modulus at finite radius nor addresses the endpoint \(d=2\), non-Hilbert smooth blocks, or a universal sum rule. No independent audit has been performed, and unindexed equivalent results remain a possible priority risk.

## References

[1] W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106v1, first publicly submitted 9 February 2026; version 2, 15 June 2026, Sections 1 and 3, Theorem B. https://arxiv.org/abs/2602.09106

[2] T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443, first publicly submitted 26 February 2013. https://arxiv.org/abs/1302.6443

[3] *Steinhaus permanence and its sharp exponent boundary for Banach direct sums*, publicly indexed 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-steinhaus-permanence-and-its-sharp-exponent-boundary-for-banach--aa4958e78249

[4] *Sharp Steinhaus criterion for \(\ell_1\)-sums of strictly convex spaces*, publicly indexed 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-steinhaus-criterion-for-ell-1-sums-of-strictly-convex-spac--61990e8279cd
