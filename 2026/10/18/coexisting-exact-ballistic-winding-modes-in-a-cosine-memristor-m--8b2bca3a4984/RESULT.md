# Coexisting exact ballistic winding modes in a cosine-memristor map

## Finding
Consider the planar map
\[
F(x,y)=\bigl(a+bcx\cos(dy),\ y+ex\bigr).
\]
For each integer \(m\ge1\), an explicit positive parameter choice supports **two simultaneously attracting, inequivalent one-step phase-locked states** on the angular cylinder. Their planar lifts have different vertical velocities, respectively \(2\pi m/d\) and \(2\pi(m+1)/d\), on disjoint nonempty open sets of initial conditions. These coexistence regions occur with feedback amplitudes tending to zero. The existence and Schur-stability of *all* one-step phase-locked states are classified below; no classification of higher-period states is asserted.

## Assumptions and scope
Assume \(a,c,d,e>0\), \(b>0\), and \(0<k=bc<1\). Set \(u=de\,x\), \(\theta=dy\pmod {2\pi}\), and \(A=ade\). The induced cylinder map is
\[
T(u,\theta)=\bigl(A+ku\cos\theta,\ \theta+u\pmod {2\pi}\bigr).
\]
A one-step phase-locked state of winding \(j\in\mathbb Z\) means a fixed point of \(T\) whose planar lift advances by \(2\pi j/d\) in one iterate. Necessarily \(u=2\pi j\). With \(0<k<1\), every such state has \(u>0\), so \(j\ge1\). For \(j\ge1\) put
\[
U_j=2\pi j,\qquad r_j=\frac{A}{U_j},\qquad S_j=U_j\sqrt{k^2-(1-r_j)^2}
\]
when \(|1-r_j|<k\).

**Exact classification.** At winding \(j\), the state exists precisely when \(|1-r_j|\le k\). There are exactly two angular states when this inequality is strict, at phases \(\theta_j^+=\arccos((1-r_j)/k)\in(0,\pi)\) and \(\theta_j^-=2\pi-\theta_j^+\). The positive-sine state is a hyperbolic attracting fixed point of the cylinder map if and only if \(S_j<r_j\); the negative-sine state is never attracting. At either equality \(|1-r_j|=k\), the sole state has eigenvalue \(1\) and is not hyperbolic. If \(S_j=r_j\) strictly inside the existence interval, the positive-sine state has a conjugate unit-modulus eigenpair and is not a hyperbolic sink.

**Infinite exact coexistence family.** For every integer \(m\ge1\), define
\[
\delta_m=\frac1{100(m+1)^2},\qquad
k_m=\frac{1+\delta_m}{2m+1},\qquad
A_m=\frac{4\pi m(m+1)}{2m+1}.
\]
Choose any positive \(c,d,e\), and set \(b=k_m/c\), \(a=A_m/(de)\). Then the cylinder has exactly four one-step phase-locked states: the two positive-sine hyperbolic sinks of windings \(m\) and \(m+1\), and the two nonattracting negative-sine companions. This remains true throughout a neighborhood of the parameter point (with the four states continued smoothly). Both sinks have open basins on the plane, and points in each such basin obey
\[
 x_n\longrightarrow\frac{2\pi j}{de},\qquad
 y_n=\frac{2\pi j}{d}\,n+C+o(1),
 \qquad j\in\{m,m+1\},
\]
with a constant \(C\) depending on the orbit. Moreover every planar initial state eventually has \(x_n>0\) and satisfies \(y_n\to+\infty\) for these explicit parameters.

## Proof
**Step 1 (fixed-state equations).** The cylinder fixed-state equations give \(u=2\pi j\) and \(u=A+ku\cos\theta\). Since \(1-k\cos\theta>0\) and \(A>0\), every fixed-state \(u>0\); hence \(j\ge1\). Substitution gives \(\cos\theta=(1-r_j)/k\), proving the precise existence and multiplicity conditions.

**Step 2 (complete Schur test).** The derivative in normalized coordinates is
\[
DT(u,\theta)=\begin{pmatrix}k\cos\theta&-ku\sin\theta\\1&1\end{pmatrix}.
\]
At the positive-sine branch the trace is \(2-r_j\) and determinant is \(1-r_j+S_j\). The three strict degree-two Jury–Schur inequalities are
\[
1-\operatorname{tr}+\det=S_j>0,\quad
1+\operatorname{tr}+\det=4-2r_j+S_j>0,\quad
1-\det=r_j-S_j>0.
\]
The middle inequality is automatic since \(0<r_j<1+k<2\). Hence both eigenvalues lie strictly inside the unit disk if and only if \(S_j<r_j\). At the negative-sine branch the first Schur quantity equals \(-S_j<0\), which actually yields a real eigenvalue strictly greater than \(1\) because the real characteristic polynomial is negative at \(1\). At \(S_j=r_j\), the positive-sine trace belongs to \((0,2)\) and determinant equals \(1\), giving a nonreal unit-modulus pair. At a phase-merger endpoint \(S_j=0\), the polynomial has a root at \(1\).

**Step 3 (adjacent windings coexist).** Write \(t=(2m+1)^{-1}\), \(\delta=\delta_m\). At the explicit parameters \(k=t(1+\delta)\), \(A=4\pi m(m+1)t\). Then
\[
r_m=1+t,\qquad r_{m+1}=1-t,\qquad
|1-r_m|=|1-r_{m+1}|=t<k.
\]
Thus both winding values have two circle phases. Their positive-sine stability quantities are \(S_j=2\pi j t\sqrt{2\delta+\delta^2}\). For the larger winding,
\[
\left(\frac{S_{m+1}}{r_{m+1}}\right)^2
=\frac{\pi^2}{m^2}\left(\frac1{50}+\frac1{10000(m+1)^2}\right)
<\frac{10}{m^2}\left(\frac1{50}+\frac1{40000}\right)<1,
\]
using \(\pi^2<10\) and \(m\ge1\). The ratio for winding \(m\) is smaller because \(S_m<S_{m+1}\) and \(r_m>r_{m+1}\). Both positive-sine states are therefore sinks, and both negative-sine companions are unstable.

**Step 4 (exclude every other winding).** The existence condition is equivalent to
\[
(1-k)j\le\frac{A}{2\pi}\le(1+k)j.
\]
Here \(A/(2\pi)=m(1+t)\). For the next lower integer \(j=m-1\), the difference between the center and upper endpoint is
\[
m(1+t)-(1+k)(m-1)=1+t-(m-1)t\delta>0.
\]
For the next higher integer \(j=m+2\), the difference between the lower endpoint and center is
\[
(1-k)(m+2)-m(1+t)=t\bigl(2m-(m+2)\delta\bigr)>0.
\]
The first inequality is vacuous when \(m=1\), since no positive lower integer exists. Both follow from \(\delta=1/[100(m+1)^2]\). Monotonicity in \(j\) excludes all smaller and larger positive windings. Therefore the two named winding values account for exactly four one-step fixed states on the quotient.

**Step 5 (open basins, lifts, and weak feedback).** A hyperbolic attracting fixed point of the smooth cylinder map has a nonempty open attracting neighborhood. There the deviations of \(u_n\) and the quotient phase decrease geometrically. Thus \(\sum_{n\ge0}|u_n-U_j|<\infty\); lifting \(\theta_{n+1}-\theta_n=u_n\) to the real line gives \(y_n=(2\pi j/d)n+C+o(1)\), and the corresponding \(x_n\)-limit. The two disjoint phase-locked sinks give disjoint open planar basins. All inequalities above are strict, hence the sinks and the absence of other one-step winding states persist under sufficiently small parameter changes; at the parameter points the excluded winding gaps are uniformly positive, so no extra integer winding enters under small perturbations. Since \(k_m\to0\), arbitrarily weak feedback admits this coexistence.

Finally \(k_m<1/2\) for every \(m\ge1\). For any real initial \(u_0\), iteration satisfies \(|u_{n+1}|\le A+k|u_n|\), so \(\limsup_{n\to\infty}|u_n|\le A/(1-k)\). Hence
\[
\liminf_{n\to\infty}u_{n+1}\ge A-\frac{kA}{1-k}
=\frac{A(1-2k)}{1-k}>0.
\]
All sufficiently late \(u_n\) are uniformly positive, and the lifted phase (equivalently \(y_n\)) grows at least linearly to \(+\infty\). No general winding limit is inferred for states outside the two attracting basins.

## Verification
The standalone script `checks.py` reconstructs the exact parameter identities using rational arithmetic, checks the two strict Schur inequalities and exclusion margins for a range of integer windings, and numerically iterates the normalized map near both sinks. Run `python3 checks.py`. The proof above, rather than finite tests, covers every \(m\ge1\), every initial condition in the asserted basins, and every allowed original parameter tuple.

## Relationship to prior work
Zhang, Liu, Wei, Jiang, Lyu and Bi introduced the exact cosine-memristor map as their equation (2), noted absence of planar fixed points and vertical periodicity, and reported numerical hidden periodic, chaotic, hyperchaotic and divergent responses for selected parameters. Their numerical analysis emphasizes bounded period-two and higher-period attractors and translational replicas. A planar trajectory whose vertical coordinate grows linearly is *not* a planar periodic orbit; after passage to the natural angular quotient, however, such a trajectory becomes a phase-locked fixed state. The exact Schur inequalities and explicit coexistence of two **different winding speeds** are additional assertions not established by the examined source. The general concept of mode-locking is classical, but does not imply the simultaneous stability and all-winding census of this particular two-dimensional map. A related 2022 paper by Ramadoss and collaborators addresses non-fixed-point memristor maps with small perturbations; available material was insufficient to compare all of its examples and is a residual antecedent risk.

## Limitations
The precise orbit classification is only for one-step phase-locked states on the angular quotient and their local basins, not for higher-period or chaotic invariant sets. The last assertion establishes global eventual upward drift only at the explicit weak-feedback parameters; it does **not** say every orbit has a limiting drift speed. These are mathematical deductions using previously studied equations, not an independent experimental observation. Independent validation and comprehensive literature priority certification have not been performed.

## References
1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, W.-P. Lyu and Q.-S. Bi, *Extremely hidden multi-stability in a class of two-dimensional maps with a cosine memristor*, Chinese Physics B 31 (2022), 100503. DOI: 10.1088/1674-1056/ac7294. Source equation (2), Section 3, and conclusion: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_10_100503.shtml (first public posting 2022-09-30, according to publisher metadata).
2. J. Ramadoss, A. Ouannas, V. K. Tamba, G. Grassi, S. Momani and V.-T. Pham, *Constructing non-fixed-point maps with memristors*, European Physical Journal Plus 137 (2022), 211. DOI: 10.1140/epjp/s13360-022-02433-z (abstract and source-paper description inspected; full mathematical text not inspected).
