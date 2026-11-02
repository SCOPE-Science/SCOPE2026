# Sharp Padé positivity horizons for two-community diffusion networks

## Finding

Let \(p,q\ge2\) be integers. Partition \(N=p+q\) vertices into communities \(A\) and \(B\), of sizes \(p\) and \(q\). Give each edge within \(A\) conductance \(a\ge0\), each edge within \(B\) conductance \(c\ge0\), and each edge between the communities conductance \(b>0\). Let \(L\) be the ordinary weighted graph Laplacian, with diagonal weighted degrees and negative off-diagonal conductances. Consider the fourth-order diagonal \([2/2]\) Padé update
\[
P(h)=\left(I+\frac h2L+\frac{h^2}{12}L^2\right)^{-1}
\left(I-\frac h2L+\frac{h^2}{12}L^2\right),\qquad h\ge0.
\]
The matrix \(P(h)\) is symmetric, has row sums one, and is positive definite for every finite \(h\ge0\). Nevertheless, its entrywise nonnegativity has a sharp two-parameter boundary:
\[
\boxed{P(h)\ge0\text{ entrywise for every }h\ge0
\iff \frac ab\le\frac{p+2q}{q}
\quad\text{and}\quad
\frac cb\le\frac{q+2p}{p}.}
\]
For arbitrary allowed parameters, the complete set of nonnegative timesteps is exactly \([0,H]\), where \(H\in(0,\infty]\) is specified below in closed form. If \(H<\infty\), entries between two distinct vertices within at least one community vanish at \(H\) and become strictly negative at every \(h>H\); no re-entrant positivity interval exists. The two community constraints decouple: the threshold for one community is independent of the conductance inside the other.

Write
\[
\alpha=\frac ab,\quad\gamma=\frac cb,\quad
u=p\alpha+q,\quad v=q\gamma+p,\quad t=bh,
\quad D(s)=1+\frac s2+\frac{s^2}{12}.
\]
Define the local horizon \(H_A=\infty\) when \(\alpha\le(p+2q)/q\). Otherwise set
\[
d_A=\frac{u(qu-N^2)}{12},\quad
v_A=\frac{pu}{2},\quad z_A=p\alpha,
\qquad H_A=\frac{v_A+\sqrt{v_A^2+4d_Az_A}}{2bd_A}.
\]
Define \(H_B=\infty\) when \(\gamma\le(q+2p)/p\). Otherwise set
\[
d_B=\frac{v(pv-N^2)}{12},\quad
v_B=\frac{qv}{2},\quad z_B=q\gamma,
\qquad H_B=\frac{v_B+\sqrt{v_B^2+4d_Bz_B}}{2bd_B}.
\]
Then \(\boxed{H=\min\{H_A,H_B\}}\), with the convention that the minimum of two infinities is infinite.

At either exact critical weight ratio, the corresponding within-community off-diagonal entry is positive for every finite positive timestep but decays as \(h^{-2}\). Precisely,
\[
\alpha=\frac{p+2q}{q}
\quad\Longrightarrow\quad
P(h)_{ij}=\frac{72q}{N^4b^2h^2}+O(h^{-3})
\quad(i\ne j\in A),
\]
with the swapped formula \(72p/(N^4b^2h^2)\) for \(B\). If \(\alpha\) exceeds its critical ratio by \(\varepsilon\downarrow0\), its individual horizon diverges as
\[
H_A\sim\frac{6}{bq\varepsilon};
\]
likewise \(H_B\sim6/(bp\varepsilon)\) as \(\gamma\) crosses its own threshold. These statements concern individual community horizons; when both constraints fail, the actual horizon is their minimum.

## Assumptions and scope

All assertions hold for all integers \(p,q\ge2\), real \(a,c\ge0\), \(b>0\), and finite real \(h\ge0\). Zero internal conductances are permitted; positive cross-community conductance makes the graph connected. Entrywise positivity means that every matrix element is nonnegative, not merely positive semidefiniteness. No symmetry constraint is imposed on initial diffusion data. There is no restriction that a timestep be small, and no limiting infinite-step matrix is counted as a finite timestep.

## Proof

Introduce the orthogonal projectors \(E_A\) and \(E_B\) onto zero-sum vectors supported on the two respective communities; they have dimensions \(p-1\) and \(q-1\). Let \(E_C\) project onto community-constant vectors orthogonal to the global constant, and let \(E_0=\mathbf 1\mathbf 1^{\mathsf T}/N\). The projectors are mutually orthogonal and sum to the identity. Directly from the Laplacian entries,
\[
L=buE_A+bvE_B+bNE_C,
\qquad
E_C=\frac{J_A}{p}+\frac{J_B}{q}-\frac{J_N}{N},
\]
where each \(J\) denotes the all-ones matrix embedded on the indicated vertex set. Here \(E_A=I_A-J_A/p\) and \(E_B=I_B-J_B/q\).

The scalar Padé multiplier at a nonnegative spectral argument \(s\) is
\[
r(s)=\frac{1-s/2+s^2/12}{D(s)}
=1-\frac{s}{D(s)}.
\]
Its numerator equals \((s-3)^2/12+1/4>0\), while \(D(s)>0\). Thus \(r(s)>0\) for finite \(s\ge0\), and \(P(h)\) is positive definite. Because \(r(0)=1\), it is row-stochastic. Put \(f(s)=s/D(s)\). Functional calculus gives the exact identity
\[
P(h)=I-f(ut)E_A-f(vt)E_B-f(Nt)E_C.
\]
For distinct vertices \(i,j\) in different communities,
\[
P(h)_{ij}=\frac{f(Nt)}{N}>0\quad(t>0).
\]
For distinct vertices in \(A\), respectively in \(B\), the off-diagonal entries are constant within each class and equal to
\[
X_A(t)=\frac{Nf(ut)-qf(Nt)}{pN}
=\frac{t}{pD(ut)D(Nt)}
\left[p\alpha+\frac{pu}{2}t+\frac{u(N^2-qu)}{12}t^2\right],
\]
\[
X_B(t)=\frac{Nf(vt)-pf(Nt)}{qN}
=\frac{t}{qD(vt)D(Nt)}
\left[q\gamma+\frac{qv}{2}t+\frac{v(N^2-pv)}{12}t^2\right].
\]
Both identities result from bringing the scalar rational expressions to a common denominator. Every denominator is strictly positive. Every diagonal entry of \(P(h)\) is strictly positive because \(P(h)\) is positive definite. Thus entrywise nonnegativity is equivalent to simultaneous nonnegativity of the two displayed quadratic brackets.

The \(A\) bracket has nonnegative constant term and strictly positive linear coefficient. Its quadratic coefficient is nonnegative exactly when \(qu\le N^2\), equivalent to \(\alpha\le(p+2q)/q\). In this regime the bracket is strictly positive for every \(t>0\), including when \(a=0\). If \(qu>N^2\), its quadratic coefficient is negative and its constant is strictly positive. It therefore has exactly one positive real root; the quadratic formula gives \(bH_A\) above. It is positive before the root, zero at it, and negative afterward. The identical argument with \(p,q,a,c\) interchanged establishes \(H_B\). Taking the minimum proves the entire interval classification and excludes later positivity windows.

At \(qu=N^2\), the quadratic bracket simplifies to \(p\alpha+(pu/2)t\). Using \(D(ut)D(Nt)\sim u^2N^2t^4/144\), the leading term is \(72/(uN^2t^2)=72q/(N^4t^2)\), as claimed. Just above the boundary, writing \(\alpha=(p+2q)/q+\varepsilon\) gives \(u=N^2/q+p\varepsilon\) and \(d_A=u(qp\varepsilon)/12\). Since \(v_A\to pN^2/(2q)\), the positive root is asymptotic to \(v_A/d_A\sim6/(q\varepsilon)\). Division by \(b\) proves the critical scaling; the second community is symmetric.

## Verification

For \(p=q=2\), \(a=4\), \(c=b=1\), the critical internal ratio is three. The first community violates it and the second does not. Substituting \(u=10\), \(N=4\) into the root formula gives the exact positivity endpoint
\[
\boxed{H=\frac{15+\sqrt{465}}{10}=3.6563858652847827\ldots.}
\]
At this timestep the only vanishing off-diagonal class is the first community's internal pair; thereafter those entries are negative while the cross-community entries remain positive.

The accompanying `verify.py` directly constructs dense Laplacians and their Padé matrices, compares independently evaluated spectral entry formulas, and checks row sums and positive eigenvalues. It performed 2,352 dense-matrix cases, 1,458 positive-root bracketing tests, two exact symbolic rational-identity checks with two exact critical-limit checks, and 18 critical-divergence checks. Execute with Python 3 using the packages specified in `requirements.txt`: `python verify.py`. These finite computations cross-check the exact identities but are not a substitute for the proof for arbitrary \(p,q,a,c,b,h\).

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2010) established general sufficient timestep inequalities for preserving positivity under diagonal Padé discretization, including a second-order diagonal Padé criterion (their Theorem 2). Their detailed treatment concerns generic Metzler matrices and contains no complete two-community weight-ratio phase diagram in the inspected sections and examples. Their 2012 paper develops general nonnegativity conditions, counterexamples, and an alternative method; its Section 4 does not state the present exact graph-family classification. The present theorem uses the familiar Padé rational function and elementary spectral projectors to obtain necessary-and-sufficient *all-timestep* inequalities and an exact finite horizon, unlike general sufficient small-timestep bounds.

## Limitations

The theorem is restricted to undirected complete two-community graphs with constant conductances within each of three edge classes and to the fourth-order \([2/2]\) Padé end-step. Arbitrary within-class conductance variation, more than two communities, nonsymmetric generators, or higher-order methods are not covered. The literature comparison cannot exclude a specialized earlier equivalent classification. The mathematical argument does not establish independent external validation or publication priority.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. N. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010. Public institutional copy: https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf (repository deposit 2010-10-15).
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, preprint (2012), later in Linear Algebra and its Applications. Public author copy: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf (repository deposit 2012-06-19).
