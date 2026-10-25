# Unconditional fourth-order Gauss–Padé positivity on complete multipartite diffusion graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be any finite simple unweighted complete multipartite graph with \(r\ge 2\), integer part sizes \(n_i\ge 1\), and \(N=\sum_{i=1}^r n_i\). Let \(L\) be its combinatorial graph Laplacian. For any real timestep \(h\ge0\), define the completed two-stage Gauss–Legendre Runge–Kutta (fourth-order diagonal \([2/2]\) Padé) diffusion map

\[
T_h=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1}.
\]

**Theorem.** The inverse exists for all \(h\ge0\). For every \(h>0\), \(T_h\) is **strictly entrywise positive, symmetric, doubly stochastic, and a positive-definite contraction**. At \(h=0\), \(T_0=I\). In particular, the exact positivity-preserving timestep interval is the entire half-line \([0,\infty)\), regardless of the number or sizes of the parts.

The off-diagonal entries admit a closed form. Put \(d(z)=z^2+6z+12\). For distinct vertices \(u,v\), if they are in different parts then

\[
(T_h)_{uv}=\frac{12h}{d(Nh)}.
\]

If they are distinct vertices in the same part of size \(m\), then

\[
(T_h)_{uv}=\frac{12(N-m)h^2\bigl((2N-m)h+6\bigr)}{d((N-m)h)\,d(Nh)}.
\]

Both expressions are strictly positive for every \(h>0\). This is a graph-dependent unconditional positivity result for a fourth-order method whose general Markov-generator positivity is not unconditional.

**Boundary of the graph class.** For the ordinary four-vertex path, the same fourth-order method is entrywise nonnegative precisely for \(0\le h\le H\), where \(H\) is the unique positive zero of

\[
f(h)=h^4-6h^3-60h^2-108h-72,
\]

numerically \(H\approx11.8663785439266\). Thus the all-timestep conclusion cannot be asserted for general simple undirected graphs.

## Assumptions and scope

The graph is finite, connected by construction, undirected, loopless, unweighted, with at least two nonempty parts. The Laplacian is \(L=D-A\) in the standard real symmetric convention, and \(h\) is a nonnegative real scalar. The result concerns the **completed endpoint map** of the two-stage, fourth-order Gauss–Legendre method, not stagewise nonnegativity, roundoff behavior, or nonlinear equations. Positivity means entrywise nonnegativity of the linear operator's matrix in the original vertex basis. Strict positivity refers only to \(h>0\).

## Proof

Define the scalar real-axis stability function and denominator by

\[
r(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad d(z)=z^2+6z+12.
\]

For \(z\ge0\), the denominator is positive and the numerator equals \((z-3)^2+3>0\), whence \(0<r(z)\le1\) and \(1-r(z)=12z/d(z)\). Consequently \(T_h=r(hL)\) is well-defined, symmetric and positive definite; all eigenvalues belong to \((0,1]\).

Write \(J_k\) for the all-ones matrix of size \(k\), and \(J\) for the \(N\)-by-\(N\) all-ones matrix. Let \(P_0=J/N\), and for every part of size \(m=n_i\), let \(P_i\) be the orthogonal projector onto vectors supported on that part and summing to zero. Explicitly its block on that part is \(I_m-J_m/m\), with all other blocks zero. The remaining projector is

\[
P_N=\operatorname{blockdiag}(J_{n_i}/n_i)-J/N.
\]

These are pairwise orthogonal projectors adding to \(I\). Direct computation of the complete multipartite Laplacian gives the eigenspaces and corresponding eigenvalues

\[
L P_0=0,\qquad L P_N=N P_N,\qquad LP_i=(N-n_i)P_i.
\]

It follows that

\[
T_h=P_0+r(Nh)P_N+\sum_{i=1}^r r((N-n_i)h)P_i.
\]

When \(u,v\) occupy different parts, only \(P_0,P_N\) have nonzero \((u,v)\)-entries, equal to \(1/N\) and \(-1/N\) respectively. Therefore

\[
(T_h)_{uv}=\frac{1-r(Nh)}{N}=\frac{12h}{d(Nh)}>0.
\]

When \(u\ne v\) are in the same part of size \(m\), the projector entries instead yield

\[
(T_h)_{uv}=\frac{1-r(Nh)}N+\frac{r(Nh)-r((N-m)h)}m.
\]

Combining the fractions exactly and cancelling produces

\[
(T_h)_{uv}=\frac{12(N-m)h^2((2N-m)h+6)}{d((N-m)h)d(Nh)}>0.
\]

Here \(N-m>0\) because at least one other nonempty part exists. This establishes every off-diagonal entry. On the diagonal, spectral positivity also applies: since \(T_h\) is symmetric positive definite, \((T_h)_{uu}=e_u^{\mathsf T}T_he_u>0\). Finally, because \(L\mathbf1=0\) and \(r(0)=1\), \(T_h\mathbf1=\mathbf1\); symmetry gives column sums one. This finishes the theorem, including all part sizes and all \(h\ge0\).

For the scope boundary, the four-vertex path has Laplacian

\[
L_P=\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix}.
\]

Direct rational functional calculus yields, for an endpoint \(u\) and its adjacent vertex \(v\),

\[
(T_h)_{uv}=\frac{-3h\bigl(h^4-6h^3-60h^2-108h-72\bigr)}{2(h^2+3h+3)(h^4+12h^3+54h^2+72h+36)}.
\]

The denominator is positive for \(h\ge0\). The quartic \(f\) has exactly one positive root by Descartes' rule of signs and the signs \(f(0)<0\), \(f(h)\to+\infty\). Its entry is positive below the root and negative above. The other off-diagonal orbit representatives are

\[
\begin{aligned}
(T_h)_{1,3}&=\frac{9h^2(h^3+6h^2+16h+12)}{D(h)},\\
(T_h)_{1,4}&=\frac{3h^3(5h^2+18h+12)}{D(h)},\\
(T_h)_{2,3}&=\frac{3h(h^4+6h^3+24h^2+72h+72)}{D(h)},
\end{aligned}
\]

where \(D(h)=2(h^2+3h+3)(h^4+12h^3+54h^2+72h+36)>0\). All are nonnegative for \(h\ge0\). The remaining entries follow from path reversal and symmetry, and the diagonals are positive by positive definiteness. Therefore the four-vertex path has exactly the claimed finite nonreentrant interval.

## Verification

The included standalone `artifacts/verify_pade.py` symbolically reconstructs the scalar identities and the two multipartite off-diagonal formulas; it also independently forms the path's rational four-by-four map and verifies each distinct off-diagonal orbit formula. Exact rational matrix inversion checks 53 complete multipartite graphs, 12,760 matrix entries, and timesteps \(1/17\), \(1\), \(13/2\), and \(101\). The four-vertex path endpoint entry is also checked at \(h=11,12,100\). All checks passed. Run `python artifacts/verify_pade.py` with the version in `artifacts/requirements.txt`.

The symbolic proof above establishes the infinite graph family; the finite verification is corroboration, not an exhaustive proof.

## Relationship to prior work

Strong-stability-preserving Runge–Kutta theory describes method-wide monotonicity and step-size restrictions; it does not directly assert unconditional positivity on this particular graph class. Research on Padé discretizations of positive linear systems demonstrates positivity failures in general and supplies method-dependent sufficient conditions on broader operator classes. The present theorem is narrower in graph structure but stronger in stepsize: for these symmetric singular graph Laplacians, every positive step works.

In particular, the published eight-state Markov-chain Padé example establishes that the same rational function can fail positivity for arbitrarily small steps on certain directed generators. That fact cannot imply or negate the positive result for this complete multipartite graph family. Conversely, the theorem here does not imply any result about unrestricted Markov generators. The four-vertex path gives a direct undirected boundary example.

## Limitations

This is an exact-arithmetic matrix result, not a floating-point or internal-stage guarantee. It covers only complete multipartite unweighted graph Laplacians and the fourth-order \([2/2]\) diagonal Padé endpoint map; it does not assert all-step positivity for arbitrary undirected graphs or nonlinear systems. The classification of all undirected graphs exhibiting unconditional positivity is not attempted. Novelty relative to every historical specialized graph-positivity result cannot be guaranteed from the inspected literature.

## References

1. S. Gottlieb, C.-W. Shu, E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* 43 (2001), 89–112, https://doi.org/10.1137/S003614450036757X. Public electronic publication 2 February 2001.
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” *MTNS 2010*, https://mural.maynoothuniversity.ie/id/eprint/2195/.
3. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442, https://doi.org/10.1016/j.laa.2011.12.021.
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” publicly indexed mathematical result (2026), considered for method comparison.
