# A sharp spoke-price frontier for optimal spectral mixing on the Petersen graph

## Finding

The Petersen graph has a canonical decomposition into two five-cycles and a five-edge perfect matching. When the five matching edges have relative unit price \(t>0\), and the ten cycle edges have unit price, the exact conductance allocation maximizing algebraic connectivity is unique even though all fifteen conductances are allowed to vary independently. There is a sharp price frontier at \(t=2/5\): above it, all fifteen edge conductances must be equal, whereas below it the matching edges optimally carry a larger common conductance. No edge is deleted at any finite positive price.

Precisely, put
\[
R(t)=\begin{cases}
\displaystyle \frac{2\sqrt t+(4-5t)\sqrt{2-t}}{(8-5t)\sqrt t},&0<t<2/5,\\[5pt]
1,&t\geq2/5.
\end{cases}
\]
The unique optimal conductances on each cycle edge and matching edge, respectively, are
\[
u(t)=\frac{1}{5(2+tR(t))},\qquad v(t)=\frac{R(t)}{5(2+tR(t))}.
\]
The optimal Laplacian spectral gap is
\[
\gamma^*(t)=\frac{\frac52+R(t)-\sqrt{R(t)^2+\frac54}}{5(2+tR(t))}.
\]
The same formula holds at the frontier, where \(R(2/5)=1\) and \(\gamma^*(2/5)=1/6\). The gap has multiplicity four below the frontier and multiplicity five at and above it. As \(t\downarrow0\),
\[
R(t)\sim\frac1{\sqrt{2t}},\qquad
u(t)\to\frac1{10},\qquad
v(t)\sim\frac1{10\sqrt{2t}},\qquad
\gamma^*(t)=\frac14-\frac{\sqrt{2t}}8+O(t).
\]
The terminology “spectral mixing” here refers to the gap of the symmetric continuous-time generator \(-L\), not the discrete-time second-largest-eigenvalue-modulus problem.

## Assumptions and scope

Let \(j\) range over \(\mathbb Z/5\mathbb Z\). The vertices are \(o_j\) and \(i_j\). The fifteen undirected edges are \(o_jo_{j+1}\), \(i_ji_{j+2}\), and \(o_ji_j\). Give these edges arbitrary conductances \(a_j,b_j,s_j\geq0\), respectively, subject to the single linear budget
\[
\sum_{j=0}^{4}(a_j+b_j+t s_j)=1,\qquad t>0.
\]
The weighted Laplacian is \(L=\sum_{xy}w_{xy}(e_x-e_y)(e_x-e_y)^{\mathsf T}\). Write \(\lambda_2(L)\) for its second-smallest eigenvalue, including multiplicities. The optimization is over all fifteen individual conductances (not just uniform classes), with disconnected feasible networks allowed. The statement concerns the unique maximizing allocation at each fixed \(t>0\).

## Proof

**1. Reduction without assuming edgewise symmetry.** The feasible set is compact and the Rayleigh characterization
\[
\lambda_2(L)=\min_{f\perp\boldsymbol1,\,\|f\|=1}f^{\mathsf T}Lf
\]
makes \(\lambda_2\) concave in the edge conductances. A cyclic shift, index reversal, and the Petersen automorphism \(o_j\mapsto i_{2j}\), \(i_j\mapsto o_{2j}\) preserve the price classes and act transitively on the ten cycle edges and separately on the five matching edges. Group-averaging any optimizer therefore yields another optimizer in which all cycle edges have conductance \(u\) and all matching edges conductance \(v\). The budget becomes \(10u+5tv=1\). A connected positive-gap allocation exists, so its optimal gap is strictly positive; for an averaged optimizer this forces \(u,v>0\), since either zero disconnects the graph.

**2. Exact symmetric spectrum.** For a primitive fifth root \(\zeta\), Fourier vectors with coordinates \((o_j,i_j)=(p\zeta^{kj},q\zeta^{kj})\) reduce the Laplacian to
\[
B_k=\begin{pmatrix}
 u(2-2\cos(2\pi k/5))+v&-v\\
 -v&u(2-2\cos(4\pi k/5))+v
\end{pmatrix}.
\]
The mode \(k=0\) has eigenvalues \(0\) and \(2v\). Since the other modes interchange the two numbers \(\alpha=(5-\sqrt5)/2\) and \(\beta=(5+\sqrt5)/2\), with \(\alpha+\beta=5\) and \(\alpha\beta=5\), each of them has the eigenvalues
\[
\lambda_{\pm}=\frac{5u}2+v\pm\sqrt{\frac{5u^2}4+v^2}.
\]
These each have multiplicity four. In particular,
\[
\det(zI-L)=z(z-2v)\bigl[z^2-(5u+2v)z+5u(u+v)\bigr]^4.
\]
Consequently \(\lambda_2=\min\{2v,\lambda_-\}\). Writing \(r=v/u>0\) and using \(u=1/[5(2+tr)]\), observe that \(\lambda_-\geq 2v\) exactly when \(r\leq1\). Hence the objective is
\[
F_t(r)=\begin{cases}
\displaystyle \frac{2r}{5(2+tr)},&0<r\leq1,\\[5pt]
\displaystyle\frac{N(r)}{5(2+tr)},&r\geq1,
\end{cases}
\qquad N(r)=\frac52+r-\sqrt{r^2+\frac54}.
\]

**3. Unique scalar optimum and price frontier.** On \((0,1]\), \(F_t\) is strictly increasing. On \([1,\infty)\), its derivative has the sign of
\[
D_t(r)=(2+tr)N'(r)-tN(r).
\]
Because \(N''(r)=-(5/4)(r^2+5/4)^{-3/2}<0\), one has \(D_t'(r)=(2+tr)N''(r)<0\). Direct evaluation gives
\[
D_t(1)=\frac{2-5t}{3},\qquad \lim_{r\to\infty}D_t(r)=-\frac{5t}{2}.
\]
Thus the unique maximizer is \(r=1\) if \(t\geq2/5\). Otherwise it is the unique \(r>1\) satisfying \(D_t(r)=0\), equivalently
\[
\left(2-\frac{5t}{2}\right)\sqrt{r^2+\frac54}+\frac{5t}{4}=2r.
\]
Solving this equation and selecting the root above one yields the stated radical expression \(r=R(t)\). Substitution proves the claimed conductances, gap, and multiplicities. Expansion of the radical and the gap as \(t\downarrow0\) gives the displayed asymptotics.

**4. Uniqueness against arbitrary asymmetric conductances.** Let \(L_*\) be the symmetric maximizing Laplacian, and let \(\widetilde L\) be any maximizing Laplacian. The group average of \(\widetilde L\) is \(L_*\), because the scalar symmetric optimizer is unique. Every conjugate of \(\widetilde L\) has spectral gap \(\gamma^*\). For any \(f\) in the four-dimensional Fourier Fiedler subspace \(E\) of \(L_*\), all Rayleigh quotients on those conjugates are at least \(\gamma^*\), and their average is exactly \(\gamma^*\). Equality in the Rayleigh bound then forces \((\widetilde L-\gamma^* I)f=0\) for all \(f\in E\).

To extract individual weights, let \(\Delta a_j,\Delta b_j,\Delta s_j\) be the difference between \(\widetilde L\)'s weights and the respective symmetric weights. The \(k=1\) Fourier Fiedler vector has outer and inner amplitudes \((p,q)\), with \(p>q>0\), and the \(k=2\) one has amplitudes \((q,p)\); both assertions follow from the strictly negative off-diagonal entry of \(B_k\) and the ordering \(\alpha<\beta\). Taking the imaginary part of the outer-vertex equation for the \(k=1\) vector shows \(\Delta a_j=\Delta a_{j-1}\) for every \(j\); denote their common value by \(A\). Its real part gives \(p\alpha A+(p-q)\Delta s_j=0\). The outer real part for \(k=2\) gives \(q\beta A+(q-p)\Delta s_j=0\). Adding forces \((p\alpha+q\beta)A=0\), so \(A=0\) and all \(\Delta s_j=0\). Finally the imaginary part of the inner-vertex \(k=1\) equation forces \(\Delta b_j=\Delta b_{j-2}\); since the step of two traverses all five indices, these differences are a common value \(B\). Its real part forces \(q\beta B=0\), so \(B=0\). Thus \(\widetilde L=L_*\) edge by edge. In particular no asymmetric optimum exists, including at the frontier.

## Verification

Run `python3 verify.py` with Python 3. The standard-library exact-rational portion checks the ten-by-ten characteristic polynomial and budget at four rational price/conductance choices. With NumPy available, additional complete Laplacian eigenspectrum and arbitrarily perturbed feasible-weight comparisons are performed. A completed run produced: `VERIFY_OK 4 exact rational 10-by-10 characteristic identities; 12 full spectra, 720 arbitrary feasible allocations`. These finite checks test arithmetic and implementation only; the proof above establishes the assertions for every \(t>0\) and every feasible edge allocation.

At \(t=1/5\), the theorem yields \(u=7/81\), \(v=11/81\) and \(\gamma^*=5/27\). At \(t=2/5\), the unique optimizer assigns \(1/12\) to every edge and has gap \(1/6\). At \(t=1\), all weights are \(1/15\), giving gap \(2/15\).

## Relationship to prior work

Göring, Helmberg, and Wappler formulated the general unpriced algebraic-connectivity optimization problem and a semidefinite/embedding duality [1]. Boyd, Diaconis, Parrilo, and Xiao gave a symmetry-reduced *discrete-time* fastest-mixing treatment and explicitly solved the Petersen graph when all edges have the same role [2, §3.3.2]; their \(2/7\) transition probability and \(3/7\) SLEM optimize a different objective from the present continuous-time, price-budgeted spectral gap. The broader spectral decompositions of generalized Petersen graphs [3] are compatible with, but do not themselves optimize, arbitrary conductances. Kolokolnikov's graph-family study [4] considers changes in graph topology at fixed unweighted edges, rather than priced conductance allocation. Shakeri and collaborators [5] optimize one-to-one interlayer conductances with fixed intralayer Laplacians; their constraint does not permit simultaneous reallocation of the cycle-edge budget. Steinerberger and Thomas [6, Example 4.9] prove the Petersen graph is conformally rigid under a *uniform* edge-price sum, covering the \(t=1\) optimal-value specialization but not determining the \(t\ne1\) price frontier or the entire uniqueness statement. The claim assessed here is the precise heterogeneous-price classification and edgewise uniqueness, not the previously known equal-price or fixed-spectrum cases.

## Limitations

The result is exact for the ten-vertex Petersen graph with the specified two price classes, a symmetric continuous-time Laplacian, and a linear budget. It makes no claim for other generalized Petersen parameters, discrete-time second-largest eigenvalue modulus, nonlinear spending constraints, or objectives involving hitting times. The finite checker is not an exhaustive verification of all prices or edge assignments. The literature comparison cannot rule out an equivalent specialized historical treatment outside the inspected primary material; independent audit has not been performed.

## References

1. F. Göring, C. Helmberg, and M. Wappler, *Embedded in the Shadow of the Separator*, Optimization Online, publicly posted September 2, 2005, https://optimization-online.org/2005/09/1202/.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (September 6, 2007), https://arxiv.org/html/0709.0955v1.
3. R. Dudek, *On the Spectrum of the Generalised Petersen Graphs*, arXiv:1412.3531v1 (December 11, 2014), https://arxiv.org/abs/1412.3531.
4. T. Kolokolnikov, *Maximizing Algebraic Connectivity for Certain Families of Graphs*, arXiv:1412.6147v1 (December 17, 2014), https://arxiv.org/html/1412.6147v1.
5. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1 (October 22, 2015), https://arxiv.org/html/1510.06785v1.
6. S. Steinerberger and R. R. Thomas, *Conformally Rigid Graphs*, arXiv:2402.11758v1 (February 19, 2024), https://arxiv.org/html/2402.11758v1.
