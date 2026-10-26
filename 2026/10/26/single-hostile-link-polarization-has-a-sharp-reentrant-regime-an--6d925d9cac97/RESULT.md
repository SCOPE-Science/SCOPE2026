# Single-hostile-link polarization has a sharp reentrant regime and a four-vertex unweighted boundary

## Finding

Consider equilibrium expressed opinions in a signed Friedkin–Johnsen network obtained by starting with a connected positive weighted graph and adding one previously absent hostile link of strength \(t\geq0\). When the nonzero innate-opinion vector is entrywise nonnegative, equilibrium squared-norm polarization is **either strictly decreasing for every finite \(t\), or strictly decreases to one positive-strength global minimum and then strictly increases**. It never develops multiple turning points.

For a positive three-vertex path with consecutive friendly weights \(a,b>0\), hostile endpoint link, and innate opinions \(s=(s_0,s_1,s_2)\geq0\), the increasing-after-decreasing regime occurs **if and only if**
\[
(a-b)(2ab-1)(s_2-s_0)>2(a^2b+ab^2+4ab+a+b)s_1.
\]
In particular, asymmetric positive weights permit this response on three vertices, but **no connected unit-weight graph with at most three vertices** can exhibit it when the hostile link joins previously nonadjacent vertices and \(s\geq0\). Four vertices are sharp in the unit-weight case.

Two exact realizations are:

1. Three vertices: friendly edges \((0,1)\) of weight \(3\) and \((1,2)\) of weight \(1\), hostile edge \((0,2)\) of strength \(t\), and \(s=(0,0,1)\). Then
\[
P_3(t)=\frac{27t^2+32t+73}{6(13t+9)^2},\qquad P_3'(t)=\frac{35(t-23)}{3(13t+9)^3}.
\]
Thus the unique minimum is at \(t=23\), with \(P_3(0)=73/486\), \(P_3(23)=7/264\), and \(\lim_{t\to\infty}P_3(t)=9/338\).

2. Four vertices: unit friendly edges \((0,1),(1,2),(1,3),(2,3)\), hostile edge \((0,2)\), and \(s=(1,0,0,0)\). Then
\[
P_4(t)=\frac{7(37t^2+56t+96)}{4(51t+40)^2},\qquad P_4'(t)=\frac{14(13t-944)}{(51t+40)^3}.
\]
Its unique minimum occurs at \(t=944/13\), with \(P_4(0)=21/200\), \(P_4(944/13)=173/6952\), and \(\lim_{t\to\infty}P_4(t)=259/10404\).

## Assumptions and scope

Let \(G=(V,E,w)\) be a finite, connected, undirected graph with positive friendly weights, \(n=|V|\geq2\), positive Laplacian \(L_+\), and \(H=I+L_+\). Fix distinct **nonadjacent** vertices \(i,j\); the added enemy edge has signed incidence \(u=e_i+e_j\) and positive magnitude \(t\). In the weighted signed extension of the standard model, the signed Laplacian and equilibrium are
\[
L(t)=L_++tuu^{\mathsf T},\qquad z(t)=(I+L(t))^{-1}s.
\]
Assume \(s\in[0,1]^n\setminus\{0\}\). The polarization convention is the mean squared expressed opinion \(P(t)=\|z(t)\|_2^2/n\), about neutral opinion zero, **not** sample variance about the network mean. All anchoring coefficients are one; \(t\) is the magnitude of an antagonistic edge (its signed adjacency entry is \(-t\)). The weighted three-path criterion applies to every \(s\geq0\) (and in particular this unit-interval range).

## Proof

Write \(z_0=H^{-1}s\), \(v=H^{-1}u\), \(r=u^{\mathsf T}v\), \(c=u^{\mathsf T}z_0\), \(d=z_0^{\mathsf T}v\), and \(e=v^{\mathsf T}v\). Connectedness and positivity of the friendly weights make \(H\) an irreducible nonsingular \(M\)-matrix, hence \(H^{-1}\) is strictly positive entrywise. Since \(s\geq0\) is nonzero and \(u\geq0\) is nonzero, all of \(r,c,d,e\) are positive. Also \(H+tuu^{\mathsf T}\) is positive definite for all \(t\geq0\).

The Sherman–Morrison identity gives
\[
z(t)=z_0-\frac{tc}{1+tr}v.
\]
Setting \(q(t)=tc/(1+tr)\) and differentiating the squared Euclidean norm yields the exact signed-edge response
\[
P'(t)=\frac{2c}{n(1+tr)^3}\bigl[t(ce-rd)-d\bigr].
\]
Every denominator is strictly positive. If \(ce-rd\leq0\), the derivative is strictly negative for all finite \(t\geq0\). If \(ce-rd>0\), its numerator changes sign precisely once, at \(t_*=d/(ce-rd)\), from negative to positive. This proves both the universal dichotomy and the unique global minimum, without assuming all equilibria keep the same sign.

For the positive weighted three-path, direct inversion gives \(\det H=D=3ab+2a+2b+1\). With \(\Delta=(a-b)(2ab-1)\) and \(B=a^2b+ab^2+4ab+a+b>0\), the expression \(ce-rd\) is linear in \(s\) and evaluates on the three coordinate vectors to \(-\Delta/D^2\), \(-2B/D^2\), and \(\Delta/D^2\), respectively. Thus for arbitrary \(s\geq0\),
\[
ce-rd=\frac{\Delta(s_2-s_0)-2B s_1}{D^2},
\]
proving the necessary-and-sufficient three-path inequality, including equality (strictly decreasing). In the unit-weight case \(a=b=1\), this quantity is \(-s_1/4\leq0\). Any simple connected unit-weight graph with two vertices has no absent edge; the only noncomplete connected graph on three vertices is a path. Hence no such reentrance exists through three vertices.

For the weighted three-vertex witness take \((a,b)=(3,1)\), \(s=e_2\). The expression above is positive, since \(\Delta=10\). An exact inversion of \(H+tuu^{\mathsf T}\) gives the stated \(P_3\) and derivative, with the sign changing at \(23\). For the unit-weight four-vertex witness take the specified five edges (four friendly, one hostile). An exact inversion gives the stated \(P_4\) and derivative; its numerator \(13t-944\) changes sign only at \(944/13\). These examples establish existence and the sharp unit-weight order boundary. The three limit and minimum values in each witness follow by exact substitution and leading coefficients.

## Verification

The accompanying standalone `verify.py` uses rational SymPy linear algebra to reproduce the general rank-one formula for the given graph matrices, all three symbolic weighted-path coefficients, both full rational polarization functions and derivatives, their endpoints and limits, and the unit-weight three-path exclusion. Invoke \`python verify.py\` from the package directory after installing SymPy. The verifier prints a single PASS line on success. The universal-in-\(t\) claims come from the algebraic proof, not from numerical sampling.

## Relationship to prior work

Zhou, Sun, Xu, Li, and Zhang (2024) develop the signed Friedkin–Johnsen equilibrium and squared-opinion polarization used here. Their model uses unit signed edges; the present theorem specifies the standard positive-weight extension and includes an all-unit-weight witness. Their treatment supplies the measures and equilibrium representation, not the one-hostile-edge derivative sign classification or the sharp small-graph reentrant boundary. Bhalla, Lechowicz, and Musco (2021) analyze **unsigned positive** link insertions and deletions via Sherman–Morrison, deriving bounds principally for polarization-plus-disagreement under a centered-variance polarization convention. Their Sections 3.2–3.3 and Appendix A concern positive-link difference-incidence updates, not the hostile sum-incidence perturbation here or its complete nonnegative-innate single-link strength classification and sharp size boundary. The low-rank linear-algebra method is shared; the present sign regime and exact phase boundary are not stated or directly implied there. Existing findings about a single hostile **bridge** between two communities with constant innate \(+1\) treat a different graph and opinion regime and do not imply these path/chord and localized-innate statements.

## Limitations

This theorem concerns insertion of exactly one enemy edge into a connected positive base network; no claims are made for multiple hostile edges, existing signed base graphs, arbitrary signed innate opinions, unequal anchoring, directed edges, or centered variance. The weighted three-path criterion is complete within its stated family only, while the four-vertex claim proves sharp **size**, not a complete four-vertex classification. The instability is a change in polarization response, not a bifurcation or multiplicity of the equilibrium, which remains uniquely defined. An equivalent signed-edge sensitivity statement in uncatalogued work remains possible; further independent literature review is warranted.

## References

1. Xiaotian Zhou, Haoxin Sun, Wanyue Xu, Wei Li, and Zhongzhi Zhang, *Friedkin-Johnsen Model for Opinion Dynamics on Signed Graphs*, arXiv:2407.10680, first posted 15 July 2024. https://arxiv.org/html/2407.10680v2
2. Nikita Bhalla, Adam Lechowicz, and Cameron Musco, *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020, first posted 28 November 2021. https://arxiv.org/abs/2111.14020
