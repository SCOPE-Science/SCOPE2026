# Complete length–Rips persistence of well-separated two-level ultrametrics

## Finding
Let \(X=U\sqcup V\) consist of two nonempty disjoint clusters of respective cardinalities \(u,v\ge 2\), with \(N=u+v\). Give \(X\) the two-level ultrametric with constant distance \(\delta>0\) inside either cluster and constant distance \(B>(\max\{u,v\}-1)\delta\) between clusters. For \(r\ge0\), form the inclusive **length–Rips complex** \(\mathrm{LR}_r(X)\) as defined in the following section. Write
\[
b_t=\binom{N-1}{t}-\binom{u-1}{t}-\binom{v-1}{t},\qquad 2\le t\le N-1.
\]
Here every binomial coefficient outside its usual range is zero. Then, at every parameter satisfying
\[
B+(t-2)\delta\le r<B+(t-1)\delta,\qquad 2\le t\le N-1,
\]
there is an integral homotopy equivalence
\[
\mathrm{LR}_r(X)\simeq\bigvee^{b_t}S^{t-1}.
\]
The complex is contractible once \(r\ge B+(N-2)\delta\); below \(B\) it is the disjoint union of two equilateral simplex-skeleton filtrations.

Consequently, for homology with coefficients in **any field**, the *complete* persistence barcode is as follows (multiplicities are indicated by coefficients of multisets):
\[
\mathcal B_0=\{[0,\infty),[0,B)\}\uplus(N-2)\{[0,\delta)\},
\]
and for each \(1\le h\le N-2\),
\[
\begin{aligned}
\mathcal B_h={}&\left(\binom{u-1}{h+1}+\binom{v-1}{h+1}\right)
\{[h\delta,(h+1)\delta)\}\\
&\uplus b_{h+1}\{[B+(h-1)\delta,B+h\delta)\}.
\end{aligned}
\]
Any interval of multiplicity zero is omitted; there are no other positive-degree bars. This is one homotopy-and-persistence classification for the specified family, not a statement about arbitrary ultrametrics.

## Assumptions and scope
For each finite nonempty vertex set \(S\subseteq X\), let
\[
w(S)=\min_{(x_1,\ldots,x_m)\ \mathrm{ordering\ of}\ S}
\sum_{i=1}^{m-1}d(x_i,x_{i+1}),\qquad m=|S|,
\]
with \(w(\{x\})=0\). Set \(\mathrm{LR}_r(X)=\{\emptyset\ne S\subseteq X:w(S)\le r\}\), together with the empty face by convention. Because deleting a vertex from a path cannot increase its length in a metric space, this is a simplicial complex. It is the finite-subset, symmetrized \(\ell^1\)-Vietoris–Rips **simplicial complex**, not an assertion about the different ordered simplicial-set construction. All inequalities defining scale thresholds are inclusive on the left and exclusive on the right; \(r\) ranges over all nonnegative real numbers.

For a pure \(m\)-point subset, its weight is \((m-1)\delta\). A mixed \(m\)-point subset has weight \(B+(m-2)\delta\): every path makes at least one intercluster crossing, and grouping its vertices by cluster attains one crossing; any extra crossing adds the strictly positive surcharge \(B-\delta\). The imposed stronger gap ensures both pure clusters are full simplices before the first mixed edge appears. The claim requires both cluster sizes at least two.

## Proof
First consider \(0\le r<B\). No face meets both clusters. The component on a cluster of size \(s\) is the \(\lfloor r/\delta\rfloor\)-skeleton of its full \((s-1)\)-simplex, capped at its full dimension. The \(h\)-skeleton of an \((s-1)\)-simplex has reduced integral homology, for \(0\le h<s-1\), concentrated in degree \(h\) with rank \(\binom{s-1}{h+1}\), and the inclusion into the next skeleton kills it. This produces the early degree-positive bars, the \(N-2\) short zero-dimensional bars, and two components until \(B\).

Fix \(2\le t\le N-1\) and \(B+(t-2)\delta\le r<B+(t-1)\delta\). Put \(Y=\operatorname{sk}_{t-1}\Delta_{N-1}\), the full \((t-1)\)-skeleton on all \(N\) vertices. Put \(Z=\Delta_{u-1}\sqcup\Delta_{v-1}\), the two full cluster simplices. The weight formula and the separation condition give **exactly**
\[
\mathrm{LR}_r(X)=Y\cup Z,\qquad
Y\cap Z=\operatorname{sk}_{t-1}\Delta_{u-1}\sqcup\operatorname{sk}_{t-1}\Delta_{v-1}=:W.
\]
Each full simplex skeleton has free reduced homology only in its top skeletal degree. In dimension \(t-1\), the inclusions \(W\hookrightarrow Y\) induce an injection of free groups with a left inverse: for each of the two cluster subsets \(U,V\), the simplicial map from \(Y\) to that cluster's \((t-1)\)-skeleton, fixing vertices of that cluster and sending every other vertex to one fixed cluster vertex, restricts to the identity on its own summand and a constant map on the other summand. Their induced homology maps together give the left inverse because \(t-1\ge1\). Thus the Mayer–Vietoris sequence for \(Y\cup Z\), noting that \(H_0(W)\to H_0(Z)\) is an isomorphism, gives
\[
\widetilde H_i(\mathrm{LR}_r(X);\mathbb Z)
\cong\begin{cases}\mathbb Z^{b_t},&i=t-1,\\0,&i\ne t-1.\end{cases}
\]
There is no hidden torsion because the inclusion on top skeletal homology is split. For \(t\ge3\), \(Y\) is \((t-2)\)-connected, and attaching the pure cluster simplices missing from \(Y\) uses cells of dimension at least \(t\); therefore \(\mathrm{LR}_r(X)\) remains \((t-2)\)-connected. Choosing maps from spheres representing a basis of the integral homology, Hurewicz's theorem and the simply connected homology form of Whitehead's theorem give the stated wedge. At \(t=2\), contracting each of the two cluster simplices yields a connected graph with two vertices and \(uv\) parallel edges; its homotopy type is \(\bigvee^{uv-1}S^1\), and \(b_2=uv-1\). At the last threshold \(B+(N-2)\delta\), every subset has appeared, giving the full simplex and contractibility.

To identify **maps**, observe that the positive-degree homology at stage \(t\) is generated by images of cycles of \(Y=\operatorname{sk}_{t-1}\Delta_{N-1}\). Every such cycle bounds in the next skeleton \(\operatorname{sk}_{t}\Delta_{N-1}\), contained in the next filtered stage. Hence all degree-\(t-1\) classes die precisely at \(B+(t-1)\delta\), while fresh classes of degree \(t\) are born there; their dimensions are \(b_{t+1}\). At \(B\) the last two vertices-components become connected, killing exactly one remaining degree-zero class. This proves every asserted barcode interval over any field, including the endpoint conventions.

## Verification
A separate reproducible program `verification/verify_ultrametric.py` independently (1) constructs weights of every nonempty subset by shortest Hamiltonian-path subset dynamic programming without using the closed-form weight formula, and (2) computes the complete barcode from a mod-two filtered simplicial boundary reduction. It compares every interval, including exact births/deaths, with the formula for 48 admissible and boundary-testing small metric instances with cluster sizes at most five. It returns `VERIFY_OK`. The finite computation does **not** prove the uniform theorem or establish a separate coefficient-field result; the integral homotopy argument above supplies those.

For example, with \(u=3\), \(v=4\), \(\delta=1\), \(B=10\), the middle mixed stages have sphere ranks \(b_2=11\), \(b_3=19\), \(b_4=15\), \(b_5=6\), \(b_6=1\). The mod-two reduction confirms bars of corresponding lengths \(1\) at the successive mixed thresholds.

## Relationship to prior work
Ivanov and Xu introduced general \(\ell^p\)-Vietoris–Rips simplicial complexes and simplicial sets, including the finite-subset symmetrized weight and stability results. Their work provides the definition, but the inspected treatment does not supply this complete two-level-ultrametric homotopy-and-barcode formula. Blaser, Brun, Gardaa and Salbu study general monoidal Rips constructions; their framework is different and does not imply the stated binomial barcode calculation. Ordinary \(p=\infty\) Vietoris–Rips complexes of finite ultrametrics have only contractible components at each scale and therefore no positive-degree bars, whereas this \(p=1\) construction exhibits high-dimensional persistence. This contrast motivates the exact family.

## Limitations
The strong gap \(B>(\max\{u,v\}-1)\delta\), equal within-cluster distances, and two-cluster structure are essential hypotheses for the stated simple formulas. No assertion is made for arbitrary hierarchical ultrametrics, the ordered simplicial-set model, all coefficient systems, or other finite metric spaces. Exact novelty beyond the inspected indexed sources cannot be guaranteed; related unpublished or unindexed computations may exist. Independent external audit is not represented by the mathematical proof or by finite testing.

## References
1. Sergei O. Ivanov and Xiaomeng Xu, *On \(\ell_p\)-Vietoris–Rips complexes*, arXiv:2411.01857, first public version 2024-11-04. https://arxiv.org/abs/2411.01857 and https://arxiv.org/html/2411.01857v2.
2. Nello Blaser, Morten Brun, Odin Hoff Gardaa and Lars M. Salbu, *Monoidal Rips: stable multiparameter filtrations of directed networks*, arXiv:2503.14019; https://arxiv.org/abs/2503.14019.
3. Standard integral simplicial homology, Mayer–Vietoris, Hurewicz and Whitehead theorems, used in their usual finite-CW forms.
