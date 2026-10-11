# No attracting three-left one-right four-cycle in the non-invertible two-saddle border-collision map

## Finding
For the planar piecewise-affine map \(F\) defined below, no locally asymptotically stable primitive four-cycle has a strict cyclic itinerary \(LLLR\) anywhere in the full four-parameter saddle region with \(\delta_L<0<\delta_R\). This is an itinerary-specific stability obstruction, **not** an assertion that this itinerary cannot exist. Both an unstable strict \(LLLR\) cycle and an attracting strict \(LRRR\) cycle occur at explicit rational parameter values in the same region.

## Assumptions and scope
For \((x,y)\in\mathbb R^2\), let
\[
F(x,y)=\begin{cases}
(\tau_Lx+y+1,-\delta_Lx),&x\le0,\\
(\tau_Rx+y+1,-\delta_Rx),&x\ge0.
\end{cases}
\]
The definitions agree at \(x=0\). Assume throughout
\[
\delta_L<0<\delta_R,\qquad
\tau_L>|1+\delta_L|,\qquad
\tau_R<-|1+\delta_R|.
\]
A *strict* cyclic itinerary \(LLLR\) means four successive periodic points with first coordinates \(x_0,x_1,x_2<0<x_3\), cyclically. No conclusion is claimed for orbits on the switching line or for other itineraries. The stability conclusion concerns the actual four-dimensional real parameter domain above, without any small-determinant, near-bifurcation, or numerical approximations.

## Proof
Put \(u=\tau_L\), \(v=\tau_R\), \(a=\delta_L\), and \(b=\delta_R\). Define
\[
A_L=\begin{pmatrix}u&1\\-a&0\end{pmatrix},\quad
A_R=\begin{pmatrix}v&1\\-b&0\end{pmatrix},\quad
M=A_RA_L^3,\quad
D=\det(I-M).
\]
Assume, for contradiction, that a strict \(LLLR\) orbit is asymptotically stable. Its branch derivative is the constant matrix \(M\), so both eigenvalues are strictly inside the unit disk. Therefore \(D>0\) and \(E:=\det(I+M)>0\), and \(I-M\) is invertible. Write
\[
K=uv+(a-1)(b-1),\quad U=u^2-(a+1)^2>0.
\]
Solving the exact four-step affine return equation \(z_0=M z_0+c\) gives
\[
x_1=\frac{(u+a+1)K}{D}.
\]
Since \(u+a+1>0\), the required \(x_1<0\) forces \(K<0\). Direct matrix expansion, with no approximation, gives
\[
E=(u^2-2a)K-(1+ab)U-2a^2-2ab.\tag{1}
\]
We prove that \(a<0<b\), the saddle inequalities, and \(K<0\) force \(E<0\), contradicting stability.

Set \(r=-a>0\) and \(w=-v>1+b\). Thus \(u>|1-r|\) and
\[
K=(r+1)(1-b)-uw.
\]
For fixed \(r,b,u\), the expression \(E\) strictly decreases as \(w\) increases, because its coefficient of \(w\) is \(-u(u^2+2r)<0\). Define the boundary value \(E_b(u)=E\vert_{w=1+b}\) and \(K_b=(r+1)(1-b)-u(1+b)\).

**Case A: \(K_b>0\).** This requires \(0<b<1\) and \(u<(r+1)(1-b)/(1+b)\). Combining with \(u>|1-r|\) implies both \(r>b\) and \(rb<1\). The value \(w_*=(r+1)(1-b)/u\) satisfies \(w_*>1+b\). At \(w=w_*\) one has \(K=0\), and identity (1) becomes
\[
E_* = -(1-rb)\bigl[u^2-(1-r)^2\bigr]+2r(b-r)<0.
\]
Actual admissibility \(K<0\) means \(w>w_*\), and monotonicity gives \(E<E_*<0\).

**Case B: \(K_b\le0\).** Monotonicity gives \(E<E_b(u)\). A direct derivative calculation shows
\[
E_b'(u)=-3(1+b)u^2-2bu+2r(u-1-b)<0\qquad (u>|1-r|).
\]
Indeed if \(u\le1+b\), all displayed terms are nonpositive and the first is strictly negative. If \(u>1+b\), use \(r<u+1\) to bound the last term by \(2(u+1)(u-1-b)\), which is smaller than the magnitude of the negative terms.

Put \(u_c=(r+1)(1-b)/(1+b)\). Because \(K_b\le0\), we have \(u\ge u_c\). The following boundary identities, valid by direct expansion, are enough:
\[
\begin{aligned}
E_b(1-r)&=2(r-b)(r^2-r+1),\\
E_b(r-1)&=-2(br^3-1),\\
E_b(u_c)&=-\frac{2(r-b)}{(1+b)^2}\left[2b^2r^2+r(1-b)^2+2\right].
\end{aligned}
\]
If \(r\le1\) and \(r\le b\), then \(u>|1-r|=1-r\) and the first value is nonpositive. If \(r\le1\) and \(r>b\), then \(u_c>1-r\), so the last value is strictly negative. If \(r\ge1\) and \(br\ge1\), then \(u>r-1\) and the middle value is nonpositive. Finally, if \(r\ge1\) and \(br<1\), then \(u_c>r-1\) and \(r>b\), so the last value is negative. In every case the strict decrease of \(E_b\) gives \(E_b(u)<0\), hence \(E<0\).

Both cases contradict \(E>0\). This proves the exclusion for all allowed parameters.

The exclusion concerns *stability*, not feasibility. At
\[
(u,a,v,b)=(9/2,-5,-10/3,2),
\]
the strict \(LLLR\) orbit has successive first coordinates
\[
\left(-\frac{37}{258},-\frac7{86},-\frac1{12},\frac{75}{344}\right),
\]
and the eigenvalues of its return derivative are \(-189\pm\sqrt{35971}\); thus it is unstable. Conversely at
\[
(u,a,v,b)=(9/5,-2,-7/5,1/5),
\]
there is a strict \(LRRR\) orbit whose first coordinates are
\[
\left(-\frac{25}{84},\frac{305}{1092},\frac5{364},\frac{505}{546}\right).
\]
Its return derivative has eigenvalues \((-477\pm\sqrt{252529})/1250\), both strictly between \(-1\) and \(1\); all branch inequalities are strict, hence the cycle is locally attracting. The \(LRRR\) phenomenon itself was described by Ghosh, McLachlan, and Simpson; the rational witness merely illustrates the asymmetry.

## Verification
The companion Python file `verify_left_triplet.py` uses exact symbolic identities to reconstruct \(x_1\), (1), the derivative and the three boundary formulas, and exact rational matrices to check both cycle itineraries and the attracting \(LRRR\) multipliers. Execute with `python verify_left_triplet.py` using SymPy. Its tests print `SYMBOLIC_IDENTITIES_OK` and `RATIONAL_ORBIT_CHECK_OK`. The inequalities and all-parameter deduction above are proved analytically; finite test runs are not substituted for quantifier proofs.

## Relationship to prior work
Ghosh, McLachlan, and Simpson's 2024 paper (arXiv:2402.05393v1, Section 9) identifies and plots a stable \(LRRR\) four-cycle region within the same non-invertible sign configuration, while its analysis of attractor-component bifurcations does not provide the all-parameter obstruction for \(LLLR\). Their 2023 work (arXiv:2307.05144v1) constructs robust chaotic regimes via trapping regions and expanding cones; those sufficient conditions do not by themselves prohibit \(LLLR\) attraction throughout the complete four-parameter saddle domain. The new comparison is about coverage and implications, not merely different words or orbit names. Earlier general border-collision literature could conceal an equivalent itinerary restriction; publication priority is not independently certified.

## Limitations
The theorem excludes only *locally asymptotically stable* strict \(LLLR\) four-cycles in the specified mixed non-invertible, two-saddle region. It does not prohibit unstable \(LLLR\) cycles (one is exhibited), boundary orbits, other symbolic words, more general piecewise-smooth maps, or stable cycles outside this parameter region. No global attractor theorem follows. Historical-priority risk remains for alternative symbolic-dynamics formulations of the border-collision normal form.

## References
1. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (February 8, 2024), https://arxiv.org/html/2402.05393v1, notably Section 9.
2. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *Robust chaos in orientation-reversing and non-invertible two-dimensional piecewise-linear maps*, arXiv:2307.05144v1 (July 11, 2023), https://arxiv.org/html/2307.05144v1.
3. T. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445v1 (2022); the abstract was available but not the full manuscript during comparison.
