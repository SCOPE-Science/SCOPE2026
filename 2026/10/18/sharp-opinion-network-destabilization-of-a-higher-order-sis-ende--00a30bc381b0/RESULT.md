# Sharp opinion-network destabilization of a higher-order SIS endemic equilibrium

## Finding

Consider the higher-order susceptible-infected-susceptible (SIS) model coupled to signed opinion dynamics defined below. For a natural self-exposure specialization with *arbitrary* population-network size and *arbitrary* symmetric weighted opinion graph, the homogeneous upper endemic equilibrium can be attracting along the synchronous plane yet repelling in the full state space. Its complete strict linear-stability criterion is an explicit largest-Laplacian-eigenvalue threshold. In the two-community rational example, the threshold is exactly \(w=1/6\) and is accompanied by an explicitly solvable **subcritical symmetry-breaking pitchfork** with two unstable asymmetric endemic equilibria.

### General spectral classification

Let \(n\ge2\), let \(L\) be the symmetric weighted graph Laplacian of any undirected opinion network on \(n\) communities, and take \(d, k, b>0\). Set the pairwise transmission matrix to zero, and let the sole higher-order exposure for community \(i\) be its own quadratic prevalence \(x_i^2\). The resulting full nonlinear model is specified in the next section. Suppose
\[
b>k,\qquad 0<d<\frac{(b-k)^2}{4b},\qquad
s_+=\frac{b-k+\sqrt{(b-k)^2-4bd}}{2b}\ne\frac12,
\]
and define \(a=b s_+(1-2s_+)\), \(h=k s_+\). If \(a<1\), the upper homogeneous endemic equilibrium is exponentially stable **relative to the synchronous invariant set**. Its strict full-space classification is:

- If \(a\le0\), it is locally exponentially stable for every symmetric opinion graph.
- If \(0<a<1\), it is locally exponentially stable if \(\lambda_{\max}(L)<h/a-1\), and linearly unstable if \(\lambda_{\max}(L)>h/a-1\).
- At equality, a nonconstant linear mode has a zero eigenvalue; no nonlinear stability conclusion is asserted by this criterion alone.

The threshold is strictly positive whenever \(a>0\) under the preceding two-root assumptions. The disease-free equilibrium is locally exponentially stable independently of \(L\).

### Exact two-community nonlinear realization

For \(d=1/3\), \(k=2\), \(b=9/2\), and an opinion edge of weight \(w\ge0\), the synchronous endemic states have prevalence \(s_-=2/9\) and \(s_+=1/3\). The upper state is exponentially stable within the synchronous set for every \(w\); in the complete four-dimensional dynamics it is locally exponentially stable precisely for \(0\le w<1/6\), unstable for \(w>1/6\), and has a simple zero eigenvalue at \(w=1/6\).

For \(0\le w<1/6\), there are exactly two **unequal, strictly positive endemic equilibria with both opinions negative**. Put \(t=1+2w\) and
\[
u=\frac12-\frac{2}{9t},\qquad
v=\pm\frac{\sqrt{(4-3t)(5t-4)}}{18t}.
\]
Their prevalences and shifted opinions are, respectively,
\[
(x_1,x_2)=(u+v,u-v),\qquad
(\eta_1,\eta_2)=(u+v/t,u-v/t).
\]
Both are linearly unstable. They merge with the upper synchronous endemic state as \(w\uparrow1/6\); for \(w\ge1/6\) no unequal strictly positive equilibrium exists in the both-negative-opinion chamber. With \(v=(x_1-x_2)/2\), the branch obeys the exact identity
\[
v^2=\frac{(1-6w)(1+10w)}{324(1+2w)^2}
\sim\frac{1}{36}\left(\frac16-w\right).
\]
The simple transverse eigenvalue crosses zero with derivative \(6/5\) with respect to \(w\). The two unstable branches existing below threshold establish a nondegenerate subcritical pitchfork in this smooth opinion-sign chamber.

## Assumptions and scope

Write \(x_i\in[0,1]\) for infected fractions and \(o_i\in[-1/2,1/2]\) for opinions, with \(\eta_i=o_i+1/2\). Use the signed-opinion convention \(\Phi(o)_{ii}=1\) when \(o_i\ge0\) and \(-1\) otherwise. The full model is
\[
\dot x_i=-\bigl(d+k\eta_i\bigr)x_i+b(1-x_i)x_i^2,\qquad
\dot o=x-\bigl(I+\Phi(o)L\Phi(o)\bigr)o-\tfrac12\mathbf1.
\]
This is the higher-order SIS--opinion system of Samadi, Caiza, Gracy and Paré (arXiv:2608.31032v1, equations (1)--(4)), with the admissible specialization \(A=0\), \(B_i=e_ie_i^{\mathsf T}\), baseline recovery \(d\), maximum recovery \(d+k\), constant higher-order transmission \(b\), and zero pairwise transmission. Repeated source indices in \(B_i\) are explicitly permitted in that model. The opinion graph is symmetric but need not be connected. There are no imported infections, no demographic turnover, and no stochastic forcing.

At a homogeneous state \(x=s\mathbf1\), \(o=(s-1/2)\mathbf1\) with \(s\ne1/2\), all opinions have the same strict sign. In a whole neighborhood of this state, \(\Phi(o)=\pm I\) is constant; the system is smooth there and its shifted opinion equation simplifies **exactly** to
\[
\dot\eta=x-\eta-L\eta.
\]
All local linear-stability statements are within this smooth chamber. At sign-switching surfaces no differentiability, uniqueness or bifurcation assertion is made.

## Proof

### 1. Synchronous equilibria

On the synchronous subspace, \(x_i=\xi\), \(\eta_i=\zeta\), the equations reduce to
\[
\dot\xi=\xi[-d-k\zeta+b\xi(1-\xi)],\qquad
\dot\zeta=\xi-\zeta.
\]
An endemic equilibrium has \(\zeta=\xi=s>0\) and therefore solves
\[
g(s)=-d+(b-k)s-bs^2=0.
\]
The assumed discriminant conditions give exactly two positive roots \(0<s_-<s_+<1\) as above. The disease-free state \((x,\eta)=(0,0)\) has infection eigenvalue \(-d\) and opinion eigenvalues \(-1-\ell\), \(\ell\in\operatorname{spec}(L)\), hence is locally exponentially stable.

At a positive synchronous equilibrium let \(a=b s(1-2s)\), \(h=ks\). Differentiating the infected equation and using \(d+ks=bs(1-s)\) yields the infection derivative \(a\) and the opinion derivative \(-h\). The synchronous Jacobian is
\[
J_0=\begin{pmatrix}a&-h\\1&-1\end{pmatrix}.
\]
At the upper root,
\[
h-a=-s_+g'(s_+)=s_+\sqrt{(b-k)^2-4bd}>0.
\]
Thus \(\det J_0=h-a>0\), and \(\operatorname{tr}J_0=a-1<0\) under the stated assumption. The upper equilibrium is exponentially stable along synchrony. At the lower root, \(\det J_0=-s_-g'(s_-)<0\), so that equilibrium is a synchronous saddle.

### 2. All-network transverse spectrum

At the homogeneous endemic state, the complete \(2n\)-by-\(2n\) Jacobian is
\[
J=\begin{pmatrix}aI&-hI\\I&-I-L\end{pmatrix}.
\]
Because \(L\) is real symmetric, orthogonal Laplacian eigenmodes reduce \(J\) into the \(2\)-by-\(2\) blocks
\[
J_\ell=\begin{pmatrix}a&-h\\1&-(1+\ell)\end{pmatrix},
\qquad \ell\in\operatorname{spec}(L).
\]
Their characteristic polynomials are exactly
\[
p_\ell(z)=z^2+(1+\ell-a)z+h-a(1+\ell).
\]
For real \(2\)-by-\(2\) matrices, both eigenvalues have negative real part exactly when the characteristic polynomial's linear and constant coefficients are positive. Since \(a<1\) and \(\ell\ge0\), the linear coefficient is always positive. If \(a\le0\), the constant coefficient is strictly positive for every \(\ell\ge0\). If \(0<a<1\), it is positive exactly when \(\ell<h/a-1\), zero at equality, and negative beyond. The largest Laplacian eigenvalue therefore gives precisely the claimed strict full-space stability classification. For \(a>0\), the threshold \(h/a-1\) is positive because \(h-a>0\).

### 3. Exact two-community symmetry breaking

For \(d=1/3\), \(k=2\), \(b=9/2\), the equilibrium polynomial factors as
\[
g(s)=-\tfrac16(3s-1)(9s-2).
\]
At the upper root \(s=1/3\), \(a=1/2\) and \(h=2/3\). For the edge Laplacian \(L=w\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\), the Laplacian eigenvalues are \(0\) and \(2w\). The transverse characteristic polynomial is
\[
p_{2w}(z)=z^2+(\tfrac12+2w)z+(\tfrac16-w).
\]
It has both roots in the left half-plane for \(0\le w<1/6\), a single zero root at \(w=1/6\), and a positive root for \(w>1/6\). At the crossing, the other transverse root is \(-5/6\); implicit differentiation of \(p_{2w}(z)=0\) gives \(dz/dw=6/5\).

For strictly positive unequal equilibria in the chamber where both opinions are negative, set
\[
x_1=u+v,\quad x_2=u-v,\quad
\eta_1=u+v/t,\quad \eta_2=u-v/t,\qquad t=1+2w.
\]
The opinion equilibrium equation gives the displayed expressions for the \(\eta_i\), and the infected equilibrium equations, after division by the positive \(x_i\), become
\[
\frac13+2u=\frac92[u(1-u)-v^2],\qquad
\frac{2v}{t}=\frac92v(1-2u).
\]
Since \(v\ne0\), the second equation forces \(u=1/2-2/(9t)\); the first then forces
\[
v^2=\frac{(4-3t)(5t-4)}{324t^2}.
\]
For \(w\ge0\), this is strictly positive exactly when \(1\le t<4/3\). In this range \(5/18\le u<1/3\) and \(0<|v|\le1/18\), so all four state coordinates \(x_i,\eta_i\) belong to \((0,1/2)\), verifying the sign-chamber hypotheses. Each sign of \(v\) yields one and only one unequal endemic equilibrium in this chamber.

At such an equilibrium, the infection-to-infection Jacobian is \(F=\mathrm{diag}[(9/2)x_i(1-2x_i)]\), the infection-to-opinion Jacobian is \(-2\operatorname{diag}(x_i)\), and the opinion blocks are \(I\) and \(-I-L\). The block determinant identity and the unequal-equilibrium relation \((9/2)(1-2u)=2/t\) give
\[
\det J=t x_1x_2\det\left(
\mathrm{diag}\left[\tfrac92(1-2x_i)\right]
-2(I+L)^{-1}\right)
=-81t x_1x_2v^2<0.
\]
A real \(4\)-by-\(4\) matrix with negative determinant has at least one positive real eigenvalue, so both unequal equilibria are unstable. The exact branch identity yields \(v^2\sim(1/6-w)/36\) from below. The simple transverse zero eigenvalue and its nonzero crossing derivative, together with this symmetric pair of unstable branches, prove the asserted nondegenerate subcritical pitchfork. No claim is made about attractors emerging far from the synchronous equilibrium.

## Verification

Run `python check.py` from the same package after installing `requirements.txt`. It symbolically checks the generic modal polynomial and root identities, the rational two-community equilibria, the exact unequal-branch formulas, the full four-dimensional determinant after imposing the equilibrium equations, and the square-root coefficient at the pitchfork. It also compares the complete Jacobian spectrum with the Laplacian-mode factorization on finite random weighted undirected networks with \(2\), \(3\), \(4\) and \(6\) vertices. This numerical finite-graph check is supplementary; the arbitrary-network conclusion follows from the proof above, not from finite enumeration.

## Relationship to prior work

Samadi, Caiza, Gracy and Paré derive the same full epidemic--opinion model and establish bistability **relative to a synchronous invariant set**. Their stability statement explicitly does not assert convergence of heterogeneous initial conditions to synchrony. The finding here sharpens the distinction: the upper endemic state can be stable in their reduced system yet unstable in the original full network, with an all-graph sharp spectral criterion. The exact two-community nonlinear pitchfork is an additional model-specific result.

Classical activator--inhibitor diffusion-driven (Turing) instability and network-mode analysis are prior mathematics, including Kouvaris, Hata and Díaz-Guilera's multiplex-network patterns. The higher-order bistable infection mechanism also has precedents, including Iacopini, Petri, Barrat and Latora. Neither mechanism is claimed as new in isolation. The contribution is the explicit parameter-wide stability separation for this higher-order SIS--opinion specialization, combined with the complete nonlinear asymmetric branch in the smallest network.

## Limitations

All stability conclusions are local to equilibria lying strictly away from opinion-sign changes. The graph is undirected with symmetric nonnegative edge weights; general directed or state-switching networks need not obey the same orthogonal-mode argument. The infection mechanism is deliberately local quadratic exposure, with no pairwise transmission or cross-community higher-order exposure; other admissible transmission tensors require separate analysis. At spectral equality the linear test is inconclusive except for the explicit two-community bifurcation. No general global attraction, practical epidemic prediction, or stochastic finite-population conclusion is asserted. The two-community asymmetric classification is limited to strictly positive equilibria in the both-negative-opinion chamber; mixed-sign and infection-boundary equilibria are not classified. The mechanism of Turing instability is classical, so originality is strictly model-specific.

## References

1. S. Samadi, J. I. Caiza, S. Gracy and P. E. Paré, *A Networked SIS Epidemic--Opinion Model with Higher-Order Interactions*, arXiv:2608.31032v1, first posted 2026-08-31. https://arxiv.org/abs/2608.31032
2. N. E. Kouvaris, S. Hata and A. Díaz-Guilera, *Pattern formation in multiplex networks*, Scientific Reports **5**, 10840 (2015). https://doi.org/10.1038/srep10840
3. I. Iacopini, G. Petri, A. Barrat and V. Latora, *Simplicial models of social contagion*, Nature Communications **10**, 2485 (2019). https://doi.org/10.1038/s41467-019-10431-6
4. W. Just, J. Saldaña and Y. Xin, *Oscillations in epidemic models with spread of awareness*, Journal of Mathematical Biology **76**, 1027--1057 (2018). https://doi.org/10.1007/s00285-017-1166-x
