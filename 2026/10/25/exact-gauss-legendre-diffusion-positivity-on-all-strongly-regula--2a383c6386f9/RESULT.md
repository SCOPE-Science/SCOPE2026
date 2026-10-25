# Exact Gauss–Legendre diffusion positivity on all strongly regular graphs

## Finding

Let \(G\) be any finite connected, simple, unweighted, noncomplete strongly regular graph of parameters \((v,k,\lambda,\mu)\), with \(\mu>0\). Write \(L=kI-A\) for the combinatorial Laplacian and apply the completed two-stage, order-four Gauss–Legendre Runge–Kutta method to \(\dot u=-Lu\):
\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},\qquad h\ge0.
\]
Define \(S=2k-\lambda+\mu\), \(P=\mu v\), \(\delta=v-S\), and
\[
D(h)=P^2h^4+6PSh^3+12(S^2+P)h^2+72Sh+144.
\]
For distinct vertices \(u,v\), exact transition entries are
\[
T(h)_{uv}=\begin{cases}
\dfrac{12h(12+6\mu h-\mu\delta h^2)}{D(h)},&u\sim v,\\[3pt]
\dfrac{12\mu h^2(6+Sh)}{D(h)},&u\not\sim v.
\end{cases}
\]
Every diagonal entry is strictly positive for \(h\ge0\). In particular, the following criterion is exact:
\[
T(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad
\begin{cases}
 h\ge0,&\delta\le0,\\[3pt]
 0\le h\le H_G:=\dfrac{3+\sqrt{9+12\delta/\mu}}{\delta},&\delta>0.
\end{cases}
\]
If \(\delta>0\), exactly the adjacent off-diagonal entries vanish at \(H_G\), and every adjacent off-diagonal entry is strictly negative for every \(h>H_G\); positivity never reappears. Every nonedge off-diagonal entry remains strictly positive for all \(h>0\). In both regimes, \(T(h)\) is symmetric, positive definite, preserves constant vectors and satisfies \(\|T(h)\|_{2\to2}=1\) for every \(h\ge0\), including steps beyond its positivity threshold.

## Assumptions and scope

A strongly regular graph with the stated parameters has \(v\) vertices, every vertex has degree \(k\), two adjacent vertices share exactly \(\lambda\) neighbors, and two distinct nonadjacent vertices share exactly \(\mu\) neighbors. Connectedness and noncompleteness imply \(0<k<v-1\) and \(\mu>0\). Edges have unit conductance; there are no self-loops. The assertions concern the exact completed rational one-step map on \(\mathbb R^v\), not the internal stage values, finite-precision computations or general graph Laplacians.

Let \(r>s\) be the two restricted adjacency eigenvalues. The standard strongly regular identities give
\[
r+s=\lambda-\mu,\quad (k-r)(k-s)=\mu v.
\]
Set \(\alpha=k-r>0\), \(\beta=k-s>\alpha\), so \(\alpha+\beta=S\) and \(\alpha\beta=P\). Thus \(S>0\), \(P>0\) and \(D(h)=d(\alpha h)d(\beta h)>0\), with \(d(z)=z^2+6z+12\).

## Proof

The scalar stability function and its complement are
\[
R(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad g(z)=1-R(z)=\frac{12z}{z^2+6z+12}.
\]
The three orthogonal Laplacian spectral projectors are \(E_0=J/v\), \(E_r\) (eigenvalue \(\alpha\)), and \(E_s\) (eigenvalue \(\beta\)). Their entries are determined by
\[
E_r=\frac{A-sI-\beta J/v}{r-s},\quad E_s=I-E_0-E_r,
\quad T(h)=I-g(\alpha h)E_r-g(\beta h)E_s.
\]
For distinct vertices, \((E_r)_{uv}=(A_{uv}-\beta/v)/(r-s)\) and \((E_s)_{uv}=-1/v-(E_r)_{uv}\). Therefore
\[
T(h)_{uv}=\frac{g(\beta h)}{v}+
\bigl(g(\beta h)-g(\alpha h)\bigr)(E_r)_{uv}.
\]
A direct common-denominator calculation, including both restricted eigenvalues, yields
\[
g(\beta h)-g(\alpha h)
=\frac{12h(\beta-\alpha)(12-\alpha\beta h^2)}{d(\alpha h)d(\beta h)}.
\]
Using \(\beta-\alpha=r-s\), \(\alpha+\beta=S\), and \(\alpha\beta=P=\mu v\), simplification for \(A_{uv}=1\) or \(0\) gives the two displayed transition formulas. Multiplying the two denominators gives the stated polynomial \(D(h)\), and \(D(h)>0\) for all \(h\ge0\).

The nonedge numerator \(12\mu h^2(6+Sh)\) is strictly positive for \(h>0\). The edge numerator has the sign of
\[
q(h)=12+6\mu h-\mu\delta h^2.
\]
If \(\delta\le0\), then \(q(h)>0\) for every \(h\ge0\). If \(\delta>0\), its roots have opposite signs and its unique positive root is
\[
H_G=\frac{6\mu+\sqrt{36\mu^2+48\mu\delta}}{2\mu\delta}
=\frac{3+\sqrt{9+12\delta/\mu}}{\delta}.
\]
It follows that \(q(h)>0\) on \([0,H_G)\), \(q(H_G)=0\), and \(q(h)<0\) for every \(h>H_G\).

For \(z\ge0\), the numerator of \(R(z)\) is \((z-3)^2+3>0\) and its denominator exceeds that numerator by \(12z\). Consequently \(0<R(z)\le1\). Since \(L\) is symmetric positive semidefinite and has a zero eigenvalue, all eigenvalues of \(T(h)=R(hL)\) lie in \((0,1]\), one equals \(1\), and \(T(h)\) is positive definite and has operator norm exactly \(1\). In particular every diagonal entry is positive; \(T(h)\mathbf1=\mathbf1\). This proves the full claimed characterization, including nonreentry and spectral stability.

For illustrations, the Petersen graph \((10,3,0,1)\) has \(\delta=3\) and \(H_G=1+\sqrt5\). The rook graph \(K_q\square K_q\), \(q\ge2\), has \(\delta=q(q-3)\): the \(q=2,3\) graphs are unconditionally positive, while every \(q\ge4\) has the finite sharp horizon \((3+\sqrt{9+6q(q-3)})/[q(q-3)]\). Conference graphs have \(\delta=0\) and unconditional positivity. Nonisomorphic strongly regular graphs with identical parameters necessarily have the same positivity horizon.

## Verification

The standalone standard-library Python script `verify.py` independently constructs the graph Laplacian, rational numerator and denominator matrices, and exact rational matrix inverse. It reconstructs the stated transition identities for \(11\) representative strongly regular graphs, including Petersen and its complement, rook and triangular graphs, Paley graphs and imprimitive multipartite examples, at five rational timesteps per graph. A successful execution gives `VERIFY_OK: 11 strongly regular graphs; 55 exact rational Gauss matrices; 5580 exact off-diagonal identities; stochastic row sums; finite-cutoff signs`. The universal assertion is established by the preceding spectral projector argument, not by this finite test.

## Relationship to prior work

Strong-stability-preserving Runge–Kutta theory, including implicit and linear-operator methods, addresses method-wide sufficient conditions and absolute-monotonicity restrictions. Research on diagonal Padé maps for positive systems exhibits failures of positivity even with favorable stability properties. The finite-state eight-state Padé counterexample is directed and not a reversible strongly regular diffusion. Those results motivate, but do not imply, an exact parameter-only classification for the present symmetric graph family. Standard strongly regular graph spectral identities supply the projector algebra; the positive-step classification requires evaluating the particular rational map on those eigenspaces. Earlier classifications for complete multipartite graphs cover some imprimitive special cases but not general primitive strongly regular graphs.

## Limitations

Only the exact end-step map on finite connected noncomplete unweighted strongly regular graphs is classified. No claim is made for internal Runge–Kutta stages, variable conductances, other graph families, nonlinear systems, or preservation under roundoff. An unknown equivalent classification in specialized literature remains an originality risk. The proof is mathematical and the verification script is corroborative, not an exhaustive enumeration or independent external audit.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112. DOI: 10.1137/S003614450036757X. The original text states first electronic publication on 2 February 2001.
2. S. Gottlieb and L.-A. Gottlieb, *Strong Stability Preserving Properties of Runge–Kutta Time Discretization Methods for Linear Constant Coefficient Operators*, Journal of Scientific Computing 18 (2003), 83–109. DOI: 10.1023/A:1020338228736.
3. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications 436 (2012), 3425–3442. DOI: 10.1016/j.laa.2011.12.021. Public preprint: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf.
4. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, 2022, Chapter 1, Section 1.1, https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.
5. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
