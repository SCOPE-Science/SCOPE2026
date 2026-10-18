# An exact parabolic-branch survival law for the orthogonal tents map

## Finding
On the two-torus with normalized Lebesgue area, let
\[
 u=\{x+2\min(y,1-y)\},\qquad
 H(x,y)=(u,\{y+2\min(u,1-u)\}),
\]
where \(\{t\}\) denotes the fractional part of \(t\). Define the negative-shear parabolic branch
\[
 P=\{(x,y)\in[0,1)^2:0<y<1/2,\ 1/2<u<1\},
\]
and the sets of orbits remaining on that branch for \(n\) consecutive observations,
\[
 S_n=\{z\in\mathbb T^2:H^j(z)\in P\text{ for }j=0,\ldots,n-1\}.
\]
For **every integer** \(m\ge1\), the exact area is
\[
 \boxed{\operatorname{Leb}(S_{2m})=\frac{2m-1}{4(4m-1)(4m-3)}.}
\]
In particular, \(\operatorname{Leb}(S_n)\sim 1/(16n)\) for *all* integer \(n\to\infty\). The result concerns an exact branch-survival observable, **not** an exact mixing-correlation asymptotic.

## Assumptions and scope
Coordinates are taken in the canonical fundamental square \([0,1)^2\); images are reduced modulo one. Switching lines and affine-cell boundaries carry zero area and are irrelevant to area identities. On \(P\), the derivative has eigenvalue \(-1\) twice with a nontrivial Jordan block. On this branch \(x+2y\in(1/2,2)\), so write \(f\in\{0,1\}\) for the integer part of \(x+2y\), and \(g\in\{0,1\}\) for the integer part of \(y+2(1-u)\). Code the four affine lifts by \(A=(0,0)\), \(B=(1,1)\), \(C=(0,1)\), \(D=(1,0)\). A word of length \(n\) means that its prescribed lift codes hold for \(H^jz\), \(0\le j<n\).

## Proof
**(1) A two-coordinate affine form.** Let \(s=x+y\). On the subcell of \(P\) with wrap bits \((f,g)\), direct substitution gives
\[
 (x',y')=(2s-x-f,\ x-3s+2+2f-g),
 \qquad (s',x')=(2+f-g-s,\ 2s-x-f).
\]
Consequently the admissible \(x\)-section of a coded subcell at fixed \(s\) is exactly the interval \(I_{f,g}(s)=[L_{f,g}(s),U_{f,g}(s)]\), where
\[
\begin{aligned}
L_{f,g}(s)&=\max\{0,s-\tfrac12,2s-f-1,3s-2-2f+g\},\\
U_{f,g}(s)&=\min\{1,s,2s-f-\tfrac12,3s-1-2f+g\}.
\end{aligned}
\]
Empty intervals are discarded. These inequalities simultaneously enforce the fundamental square, the lower horizontal tent, the upper vertical tent, and both modular wrap choices.

**(2) All allowed code words.** Using the preceding inequalities at two successive states (with the displayed affine recurrence), the only ordered pairs of letters with **positive area** are \(AB,AD,BA,CA\), each with exact preimage area \(1/48\). The other 12 pairs have zero area. Thus for any \(m\ge1\), up to the union of measure-zero boundaries, the length-\(2m\) survivor set has precisely four nonempty itinerary components:
\[
 (AB)^m,\quad(BA)^m,\quad CA(BA)^{m-1},\quad(AB)^{m-1}AD.
\]
Here \(C\) occurs only initially and \(D\) only terminally, as required by the positive-area transition graph.

**(3) The two recurrent components.** In the \(AB\) pair, write \(s=3/4+\delta\). Applying first \(A\), then \(B\), preserves \(s\) and translates \(x\) to \(x-4\delta\). Enforcing every state in \((AB)^m\) via the formulas in part (1) reduces the initial sections to
\[
\begin{array}{ll}
\frac12+2\delta\le x\le\frac34+(4m+1)\delta,&-\frac1{4(4m-1)}\le\delta\le0,\\[2pt]
\frac12+4m\delta\le x\le\frac34+\delta,&0\le\delta\le\frac1{4(4m-1)}.
\end{array}
\]
Both widths equal \(\frac14-(4m-1)|\delta|\). Their integral is
\[
 \operatorname{Leb}\{(AB)^m\}=2\int_0^{1/[4(4m-1)]}
 \left(\frac14-(4m-1)t\right)dt
 =\frac1{16(4m-1)}.
\]
For \(BA\), writing \(s=5/4+\delta\), the pair again gives \(x\mapsto x-4\delta\). Its initial sections are
\[
\begin{array}{ll}
\frac34+\delta\le x\le1+4m\delta,&-\frac1{4(4m-1)}\le\delta\le0,\\[2pt]
\frac34+(4m-1)\delta\le x\le1,&0\le\delta\le\frac1{4(4m-1)}.
\end{array}
\]
Their widths are the same, hence \(\operatorname{Leb}\{(BA)^m\}=1/[16(4m-1)]\).

**(4) The two transient components.** For \((AB)^{m-1}AD\), set \(s=3/4-\varepsilon\). The interval constraints from part (1), using the two-step translation through the repeated \(AB\) portion and the terminal \(D\) condition, become
\[
 \max\{\tfrac34-(4m+1)\varepsilon,\tfrac12-2\varepsilon\}
 \le x\le\tfrac34-(4m-1)\varepsilon,
 \quad0\le\varepsilon\le\frac1{4(4m-3)}.
\]
The section width is \(\min\{2\varepsilon,\frac14-(4m-3)\varepsilon\}\). For \(CA(BA)^{m-1}\), express its initial \(C\) state by the coordinates \((s_1,x_1)=(1-s_0,2s_0-x_0)\) of the ensuing \(A\) state. This change of coordinates has absolute Jacobian one. Writing \(s_1=3/4-\varepsilon\), the \(C\) entry constraint and the subsequent alternating steps give
\[
 \frac12\le x_1\le \min\{\tfrac12+2\varepsilon,\tfrac34-(4m-3)\varepsilon\},
 \quad 0\le\varepsilon\le\frac1{4(4m-3)}.
\]
Its section width is identical. The two linear bounds cross at \(\varepsilon_*=1/[4(4m-1)]\), yielding for **each** transient component
\[
 \int_0^{1/[4(4m-3)]}
 \min\left\{2t,\frac14-(4m-3)t\right\}dt
 =\frac1{16(4m-1)(4m-3)}.
\]
The four itinerary components have disjoint interiors. Adding their areas gives
\[
 \frac2{16(4m-1)}+\frac2{16(4m-1)(4m-3)}
 =\frac{2m-1}{4(4m-1)(4m-3)}.
\]
This proves the exact finite-time formula for all \(m\), not only sampled values.

**(5) All-time asymptotic.** The even-time identity gives \(\operatorname{Leb}(S_{2m})\sim1/(32m)\). The inclusions \(S_{2m+2}\subset S_{2m+1}\subset S_{2m}\) squeeze the odd-time measures to the same normalized limit, proving \(\lim_{n\to\infty}n\operatorname{Leb}(S_n)=1/16\). Since \(\operatorname{Leb}(P)=1/4\), the conditional survival tail for an initial point uniform in \(P\) is \(\operatorname{Leb}(S_n)/\operatorname{Leb}(P)\sim1/(4n)\).

## Verification
All affine inequalities above are explicit rational linear inequalities. The standalone `VERIFY.py` reproduces the coded convex polygons by exact rational clipping, checks the 16 two-code transitions and, for \(1\le m\le60\), checks all four component areas against the closed formulas. These finitely many computations test the algebra; the unrestricted theorem follows from the symbolic affine recurrence and interval integration in the proof, not extrapolation.

## Relationship to prior work
Myers Hill, Sturman and Wilson (2023), *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, establish polynomial \(O(1/n)\) correlation decay, identify parabolic period-two line segments, and analyze induced return/escape cells. Their Section 6 derives a bound for returns to a hyperbolic base, not the present exact distribution of consecutive residence in one fixed full parabolic branch. Their rational partition-geometry techniques are closely related, but the four-wrap-word enumeration, exact all-\(m\) total area, and coefficient \(1/16\) are separate statements requiring the global affine-cylinder calculation here. The same authors' 2022 papers establish mixing regimes for the wider shear family. Springham–Sturman (2013) treat polynomial mixing for different linked-twist maps, not this fixed branch observable.

## Limitations
This is a *specific* branch-survival statistic for the unperturbed orthogonal tents map. It neither computes the exact correlation decay coefficient nor the return-tail coefficient for the different inducing domain used in the 2023 paper. It proves the exact measure only at even times, plus the leading asymptotic at every time; it does not determine an all-order odd-time formula. The 2022 Myers Hill thesis, *Mixing in the Presence of Non-Monotonicity*, could not be read completely because its large PDF was not accessible within the current comparison, and may contain related earlier geometry. Independent mathematical scrutiny and exhaustive priority investigation remain outstanding.

## References
1. J. Myers Hill, R. Sturman and M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515v1 (first posted 15 March 2023); December 2023 revision, especially Sections 1, 4, 5 and 6 and Figure 1. https://arxiv.org/abs/2303.08515.
2. J. Myers Hill, R. Sturman and M. C. T. Wilson, *A Family of Non-Monotonic Toral Mixing Maps*, Journal of Nonlinear Science 32 (2022), article 31. DOI 10.1007/s00332-022-09790-0.
3. J. Myers Hill, R. Sturman and M. C. T. Wilson, *Exponential Mixing by Orthogonal Non-Monotonic Shears*, Physica D 434 (2022), 133224. DOI 10.1016/j.physd.2022.133224.
4. J. Springham and R. Sturman, *Polynomial Decay of Correlations in Linked-Twist Maps*, Ergodic Theory and Dynamical Systems, online 2013. https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/polynomial-decay-of-correlations-in-linkedtwist-maps/6C084706FA545B68037DE554EDA4C4B4.
