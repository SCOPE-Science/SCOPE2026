# Exact heat-flow Wasserstein amplification on incidence graphs of finite projective planes

## Finding

Let \(\Pi\) be an arbitrary finite projective plane of order \(q\ge2\), let \(G_\Pi\) be its bipartite point–line incidence graph with unit-edge shortest-path metric \(d_G\), and let \(A\) be its adjacency matrix. Write \(d=q+1\), \(v=q^2+q+1\), and \(P_t=\exp[-t(dI-A)]\), for real \(t\ge0\). The **optimal graph-distance Wasserstein-one coefficient**, equivalently the induced operator norm on real graph-Lipschitz functions modulo constants, is

\[
\mathcal C_q(t):=\max_{x\ne y}\frac{W_1(P_t\delta_x,P_t\delta_y)}{d_G(x,y)}
=e^{-dt}\left[\frac{4q}{v}\cosh(\sqrt q\,t)+\frac{4q^3}{v\sqrt q}\sinh(\sqrt q\,t)+\frac{q^2-3q+1}{v}e^{-dt}\right].
\]

Every incident point–line pair attains the maximum, for all \(t\ge0\), without any hypothesis that \(\Pi\) is Desarguesian or edge-transitive. The function starts at \(\mathcal C_q(0)=1\) with \(\mathcal C_q'(0)=2(q-1)>0\), has exactly one critical point on \((0,\infty)\), which is a strict global maximum, and crosses the level \(1\) at exactly one subsequent positive time. Thus the heat flow transiently *amplifies*, and ultimately contracts, graph-distance Wasserstein-one distances.

For existing projective-plane orders \(q\to\infty\), uniformly for \(s\) in compact subsets of \([0,\infty)\),

\[
\mathcal C_q(s/q)\longrightarrow g(s):=e^{-2s}+4s e^{-s}.
\]

If \(t_q\) is the unique time of maximum, then \(q t_q\to s_*\), where \(s_*\in(0,1)\) is the unique solution of \(2(1-s_*)=e^{-s_*}\), and

\[
\max_{t\ge0}\mathcal C_q(t)\longrightarrow g(s_*)\approx1.64046408905,
\qquad s_*\approx0.76803904701.
\]

## Assumptions and scope

A projective plane of order \(q\) has \(v=q^2+q+1\) points and the same number of lines, with exactly \(d=q+1\) points on each line, exactly \(d\) lines through each point, and a unique line through two points and a unique point on two lines. The theorem is conditional on existence; every prime-power order provides an example. Edges join incident point–line pairs and have length one. The semigroup uses **unnormalized rate-one edge jumps**; changing the time or Laplacian convention changes the formula. All measures are probability measures on vertices, and \(W_1\) uses the shortest-path cost, including cost three for a nonincident point–line pair. The assertion is about real-valued Lipschitz spaces, not about Hilbert-space or \(W_2\) contractions.

## Proof

**1. Heat matrix.** Let \(N\) be the \(v\)-by-\(v\) point–line incidence matrix, so \(NN^{\mathsf T}=qI+J\), \(N\mathbf1=d\mathbf1\), and \(A=\begin{pmatrix}0&N\\N^{\mathsf T}&0\end{pmatrix}\). Put

\[
C=\cosh(\sqrt q\,t),\quad S=\frac{\sinh(\sqrt q\,t)}{\sqrt q},\quad K=\frac{e^{-dt}-C+dS}{v},\quad z=e^{-dt}.
\]

Since the nonconstant singular values of \(N\) are all \(\sqrt q\) and its constant singular value is \(d\),

\[
(e^{tA})_{PP}=CI+\frac{\cosh(dt)-C}{v}J,\qquad
(e^{tA})_{PL}=SN+\frac{\sinh(dt)-dS}{v}J,
\]

and the line–line and line–point blocks are their dual counterparts. The identity \(\cosh(dt)-\sinh(dt)=e^{-dt}\) gives \(K\) as the point-versus-line block offset.

**2. Exact signed edge-column distribution.** Fix any incident point \(x\) and line \(y\), and set \(\mu=P_t\delta_x-P_t\delta_y\). Define

\[
a=z(C-S+K),\qquad b=z(S-K),\qquad c=zK.\]

The measure \(\mu\) takes the respective values \(+a,-b,+c\) on the single point \(x\), the \(q\) other points of \(y\), and the \(q^2\) points not on \(y\). On the line side it takes the values \(-a,+b,-c\) on \(y\), the \(q\) other lines through \(x\), and the \(q^2\) lines not through \(x\). At \(t=0\), \(a=1\) and \(b=c=0\). For \(t>0\), all three are positive: indeed \(K''-qK=e^{-dt}\) with \(K(0)=K'(0)=0\), whence

\[K(t)=\int_0^t\frac{\sinh(\sqrt q(t-u))}{\sqrt q}e^{-du}\,du,\qquad 0<K(t)<\frac{S(t)}d<S(t).\]

Also \(C>S\) for \(q>1\). Hence the signed support pattern holds for every positive time.

**3. Primal–dual sharp transport certificate.** Define a real vertex potential \(\varphi\) as follows: on the point side, \(\varphi(x)=1\), \(\varphi(p)=-1\) at all other points \(p\in y\), and \(\varphi(p)=1\) outside \(y\); on the line side, \(\varphi(y)=0\), \(\varphi(\ell)=2\) for the other lines \(\ell\ni x\), and \(\varphi(\ell)=0\) for lines \(\ell\not\ni x\). Every incidence edge has potential difference exactly \(1\) in absolute value: in particular, a line through \(x\), other than \(y\), meets \(y\) only at \(x\). Therefore \(\operatorname{Lip}(\varphi)=1\) and Kantorovich duality gives

\[W_1(P_t\delta_x,P_t\delta_y)\ge\langle\varphi,\mu\rangle=a+3qb+q^2c.\]

For the reverse inequality construct a transport plan from the positive part of \(\mu\) to its negative part. Send \(a\) from \(x\) to \(y\) at distance \(1\). Choose any bijection between the \(q\) lines through \(x\) distinct from \(y\) and the \(q\) points of \(y\) distinct from \(x\); send \(b\) across each of these nonincidences, at distance \(3\). Finally, the incidence graph between the \(q^2\) points outside \(y\) and the \(q^2\) lines not through \(x\) is **\(q\)-regular on both sides**: each of its points has exactly one line through \(x\), while each of its lines intersects \(y\) at exactly one point. A regular bipartite graph has a perfect matching; use such a matching to ship \(c\) along each incident pair at distance \(1\). Total cost is exactly \(a+3qb+q^2c\). Thus

\[W_1(P_t\delta_x,P_t\delta_y)=a+3qb+q^2c=z\big[C+(3q-1)S+(q^2-3q+1)K\big].\]

Substituting \(K\), using \(q^2+q+1-(q^2-3q+1)=4q\) and \((3q-1)v+(q^2-3q+1)d=4q^3\), yields the displayed closed form.

**4. Global optimality.** For every two vertices \(u,w\), choose a shortest incidence-edge path \(u=u_0,u_1,\dots,u_m=w\) of length \(m=d_G(u,w)\). The Wasserstein triangle inequality gives

\[W_1(P_t\delta_u,P_t\delta_w)\le\sum_{i=1}^m W_1(P_t\delta_{u_{i-1}},P_t\delta_{u_i})=m\,(a+3qb+q^2c).\]

Because every incidence edge itself attains equality, this is precisely the unrestricted coefficient. Kantorovich duality on a finite metric space also identifies it with the induced real Lipschitz-operator norm.

**5. One peak and one subsequent level crossing.** Let \(r=\sqrt q\), \(k=q^2-3q+1\), and

\[a_+=\frac{2q}{v}+\frac{2q^3}{vr}>0,\qquad a_-=\frac{2q}{v}-\frac{2q^3}{vr}<0.\]

The formula is \(\mathcal C_q(t)=a_+e^{-(d-r)t}+a_-e^{-(d+r)t}+(k/v)e^{-2dt}\). With \(\zeta=e^{-2rt}\in(0,1]\), multiply its derivative by \(e^{(d-r)t}\) to obtain

\[H_q(\zeta)=-(d-r)a_+ +(d+r)|a_-|\zeta-\frac{2dk}{v}\zeta^{(d+r)/(2r)}.\]

We have \(H_q(0)<0\) and \(H_q(1)=\mathcal C_q'(0)=2(q-1)>0\). For \(q=2\), \(k=-1\), so \(H_q\) is strictly increasing on \([0,1]\). For \(q\ge3\), \(k>0\) and \(H_q\) is strictly concave; its nonnegative superlevel set is a single interval reaching \(1\). Hence in either case there is exactly one root in \((0,1)\). Consequently \(\mathcal C_q\) rises strictly and then decreases strictly toward zero. Since its initial value is one and initial slope is positive, it crosses the value one exactly once more.

**6. Large-order limit.** Set \(t=s/q\). The identities \(d/q\to1\), \(v/q^2\to1\), \(k/v\to1\), and \(\sinh(s/\sqrt q)/(s/\sqrt q)\to1\) imply, uniformly on compact \(s\)-sets, \(\mathcal C_q(s/q)\to g(s)=e^{-2s}+4se^{-s}\), together with convergence of first derivatives with respect to \(s\). Now

\[g'(s)=2e^{-s}\big(2(1-s)-e^{-s}\big).\]

It changes sign exactly once, at \(s_*\in(0,1)\) defined above. Since \(g'(2)<0\), derivative convergence and the already-proved uniqueness of the finite-order maximizer give \(0<qt_q<2\) for sufficiently large \(q\); every subsequential limit must solve \(g'(s)=0\), so \(qt_q\to s_*\). Substituting into uniform convergence yields the stated peak-height limit.

## Verification

The attached `verify.py` reconstructs projective planes over the prime fields with \(q=2,3,5\), checks \(NN^{\mathsf T}=qI+J\) and graph distances, verifies the explicit potential is edge-1-Lipschitz, compares transport primal and dual values with the analytic formula at three times using linear programming, and (for the Fano plane) verifies the global coefficient against all vertex pairs. It also tests the large-order limit numerically. The recorded execution produced `CHECK_OK planes=3 incidence_edges=777 lp_instances=282`. Python 3 with NumPy and SciPy is sufficient. These finite tests are corroboration; the proof applies to **every** finite projective plane, including non-Desarguesian planes, through its incidence axioms.

## Relationship to prior work

Münch and Wojciechowski's 2017 semigroup characterization equates lower Ollivier-curvature bounds with exponential Lipschitz and Wasserstein estimates; that general theorem does not give the exact nonexponential operator norm for finite projective-plane incidence graphs. Fathi and Lakzian's 2022 curvature framework concerns general infinitesimal and discrete-time curvature functions, not this explicit continuous-time point-line transport optimum. Cushing, Kamtue, Kangaslampi, Liu, and Peyerimhoff study combinatorial curvature and an incidence design with different parameters; the inspected article does not determine the present heat-flow law. Related work on projective-plane incidence graphs addresses isoperimetric invariants rather than this semigroup norm. The new closed form and sharp large-order peak should not be confused with a direct consequence of a curvature lower bound, which supplies only a one-sided exponential estimate.

## Limitations

The formula is for unweighted point–line incidence graphs, real Wasserstein-one distance, and the unnormalized rate-one Laplacian. It does not imply results for unequal-order incidence structures, weighted graphs, or other Wasserstein exponents. The theorem is conditional on the existence of a projective plane of the indicated order; the asymptotic is along existing orders. The argument establishes uniqueness of the maximizing **time**, not uniqueness of the maximizing vertex pair or Lipschitz potential. Previous equivalent formulas under distance-regular or association-scheme terminology are a residual priority risk, and no independent mathematical validation is asserted.

## References

- Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first public version 2017-12-04), especially Theorem 3.8. https://arxiv.org/abs/1712.00875
- Zohreh Fathi and Sajjad Lakzian, *Discrete Ollivier-Ricci curvature*, arXiv:2203.16837 (first public version 2022-03-31), Section 6. https://arxiv.org/abs/2203.16837
- David Cushing, Supanat Kamtue, Riikka Kangaslampi, Shiping Liu, and Norbert Peyerimhoff, *Curvatures, graph products and Ricci flatness*, Journal of Graph Theory 96 (2021), 522–553, first published 2020-10-12, doi:10.1002/jgt.22630, particularly Sections 4–6.
- Andrew Elvey Price, Muhammad Adib Surani, and Sanming Zhou, *The Isoperimetric Number of the Incidence Graph of \(PG(n,q)\)*, Electronic Journal of Combinatorics 25 (2018), P3.20, doi:10.37236/6980.
