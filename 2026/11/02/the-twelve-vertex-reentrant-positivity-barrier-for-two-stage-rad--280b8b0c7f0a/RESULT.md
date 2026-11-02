# The twelve-vertex reentrant positivity barrier for two-stage Radau IIA on balanced multipartite networks

## Finding

Let \(m\ge 2\), \(s\ge 1\) be integers and \(c>0\). On the balanced complete \(m\)-partite graph \(G=K_{s,\ldots,s}\), every edge has conductance \(c\), and \(L\) is the weighted combinatorial Laplacian. Apply the *endpoint* of the two-stage, third-order Radau IIA method to \(u'=-Lu\):
\[
P(h)=R(hL),\qquad R(z)=\frac{6-2z}{z^2+4z+6},\quad h\ge0.
\]
Put \(n=ms\). Every off-diagonal entry of \(P(h)\) is strictly positive whenever \(h>0\). The exact nonnegative-step domain is **all** \(h\ge0\) when \(n\le11\), but when \(n\ge12\) it is exactly
\[
[0,t_-/(sc)]\;\cup\;[t_+/(sc),\infty),
\]
where \(0<t_-<t_+\) are the *two and only two* positive roots of the explicit quartic
\[
\begin{aligned}
F_{m,s}(t)={}&m^2(m-1)^2t^4
-2m(m-1)(sm^2-6m+3)t^3\\
&-2m(sm^2-4sm-9m+9)t^2
+12sm(m+1)t+36sm.
\end{aligned}
\]
At both boundaries every diagonal entry is zero; between them every diagonal entry is negative. Thus increasing the timestep can first destroy and later *restore* endpoint positivity, with a universal sharp onset at twelve states for this graph family.

## Assumptions and scope

The graph is simple, connected, undirected and complete multipartite with \(m\) *equal* parts of size \(s\), including cliques when \(s=1\). All cross-part edges have the same positive conductance \(c\), and there are no within-part edges. The assertion concerns the end-step matrix for initial nonnegative data, not positivity of internal Runge–Kutta stages, and not arbitrary unequal part sizes or weighted generators.

Write \(t=sch\), \(D(x)=x^2+4x+6\), \(a=R((m-1)t)\) and \(b=R(mt)\). The exact three entry types are
\[
\begin{aligned}
P_{ii}(h)&=\frac{1+m(s-1)a+(m-1)b}{n},\\
P_{ij}(h)&=\frac{1-ma+(m-1)b}{n}, && i\ne j\text{ in the same part},\\
P_{ij}(h)&=\frac{1-b}{n}, && i,j\text{ in distinct parts}.
\end{aligned}
\]
The middle entry type is absent if \(s=1\). Every row sums to one for every \(h\ge0\), regardless of entry signs.

## Proof

**Spectral decomposition.** The Laplacian has eigenvalue \(0\) on constants; eigenvalue \(cs(m-1)\) on the direct sum of within-part zero-sum spaces (multiplicity \(m(s-1)\)); and eigenvalue \(csm\) on part-constant vectors of total sum zero (multiplicity \(m-1\)). If \(J\) is the full all-ones matrix and \(B\) the block diagonal matrix whose blocks are \(s\)-by-\(s\) all-ones matrices, the corresponding projectors are \(J/n\), \(I-B/s\), and \(B/s-J/n\). Applying \(R\) gives the three displayed entry formulas. Also \(R(0)=1\), so \(P(h)\mathbf 1=\mathbf 1\).

**Off-diagonal strict positivity.** For each \(x>0\), \(1-R(x)=x(x+6)/D(x)>0\), proving the cross-part assertion. A direct rational identity gives
\[
1-mR((m-1)t)+(m-1)R(mt)
=\frac{m(m-1)t^2\{m(m-1)t^2+(12m-6)t+18\}}{D((m-1)t)D(mt)}>0
\]
for \(t>0\), proving positivity of within-part off-diagonals whenever they exist.

**Why fewer than twelve states never fail.** The global minimum over \(x\ge0\) of \(R(x)\) is \(\rho=(5-3\sqrt3)/2\), at \(x=3+3\sqrt3\). Therefore every diagonal satisfies \(nP_{ii}(h)\ge 1+(n-1)\rho\). For \(n\le11\), this is at least \(1+10\rho=26-15\sqrt3>0\). Hence all steps are nonnegative for \(n\le11\).

**Why every graph with at least twelve states fails.** The identity
\[
R(x)+\frac1{11}=\frac{(x-6)(x-12)}{11D(x)}
\]
shows \(R(6)=R(12)=-1/11\), and \(R(x)<-1/11\) for \(6<x<12\). Choose \(t_0=6/(m-1)\), so \((m-1)t_0=6\) and \(mt_0\in(6,12]\). The diagonal obeys
\[
nP_{ii}(t_0/(sc))\le1-\frac{n-1}{11}=\frac{12-n}{11}.
\]
This is strictly negative for \(n>12\), and also for \(n=12\) if \(m>2\). The sole remaining case is \((m,s)=(2,6)\). Taking \(t=8\) gives
\[
12P_{ii}(8/(6c))=1+10R(8)+R(16)=-\frac{500}{8313}<0.
\]
Thus for every \(n\ge12\) some timestep has negative diagonal entries.

**Exactly one forbidden interval.** Multiplying the diagonal numerator by the strictly positive product \(D((m-1)t)D(mt)\) yields precisely \(F_{m,s}(t)\) above. Its leading, linear and constant coefficients are positive. For \(n=ms\ge12\), its cubic coefficient is strictly negative, because \(sm^2-6m+3=m(n-6)+3>0\). Regardless of the quadratic coefficient's sign, the descending coefficient list has exactly two sign changes. Descartes' rule bounds the number of positive roots, counted with multiplicities, by two. The diagonal is positive at \(t=0\) and approaches \(1/n>0\) as \(t\to\infty\), while the preceding paragraph proves negativity at an intermediate positive timestep. The intermediate value theorem therefore forces at least two distinct positive roots; hence exactly two, necessarily simple, with the claimed sign pattern. Off-diagonal positivity proves the full matrix statement.

## Verification

Run `python verify_radau.py` with Python 3 and SymPy. The checker independently reconstructs the Radau IIA stability function from its Butcher tableau, verifies the identities and quartic coefficients symbolically, compares the spectral projector formulas against exact rational matrix inverses for seven different multipartite networks, and isolates the positive roots of the quartic. It reports 917 exact assertions. The finite checks support the written proof; they do not substitute for its all-parameter reasoning.

As a concrete endpoint example, for \(K_{12}\) and unit conductance the nonnegative step domain is \([0,1/2]\cup[1,\infty)\). At \(h=0\) the update is the identity; at large steps it approaches the rank-one uniform averaging matrix.

## Relationship to prior work

Absolute monotonicity and strong-stability-preserving theory supply broad sufficient step-size conditions for general Runge–Kutta methods (Lóczi and Ketcheson, 2013). Bonaventura and Della Rocca (2015) analyze positivity and monotonicity of the distinct TR-BDF2 family and alternative integrators. Those frameworks do not state the present exact graph-family endpoint positivity domain. Earlier graph diffusion work on Crank–Nicolson and diagonal \([2/2]\), \([3/3]\) Padé/Gauss end-step maps uses different rational stability functions; in particular the two-interval reentrant phenomenon does not follow from their single-horizon results. The present claim concerns only two-stage Radau IIA on balanced multipartite Laplacians.

## Limitations

There is no assertion about internal stage positivity, inhomogeneous diffusion, nonlinear equations, unequal part sizes, nonuniform conductances, or other Runge–Kutta methods. The quartic roots are specified exactly by their uniqueness/order, not by radical expansions. The literature comparison cannot rule out specialized prior work that is not indexed or accessible. The mathematical review is not independent validation.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651, first publicly posted 2013-03-26. https://arxiv.org/abs/1303.6651
2. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303, first publicly posted 2015-10-14. https://arxiv.org/abs/1510.04303
