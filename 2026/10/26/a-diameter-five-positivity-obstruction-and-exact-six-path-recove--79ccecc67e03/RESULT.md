# A diameter-five positivity obstruction and exact six-path recovery for third-order Radau IIA

## Finding

Let \(G\) be a finite, connected, undirected graph with strictly positive edge conductances, and let \(L\) be its weighted combinatorial Laplacian. For \(h\geq0\), define the completed two-stage, third-order Radau IIA heat step
\[
T_G(h)=(6I-2hL)(6I+4hL+h^2L^2)^{-1}.
\]
Then the following statements hold.

**Universal diameter obstruction.** If \(G\) has graph-theoretic diameter at least five, then \(T_G(h)\) has a strictly negative entry for every sufficiently small \(h>0\). In fact, for any vertices \(u,v\) at graph distance exactly five,
\[
[T_G(h)]_{uv}=-\frac{W_5(u,v)}{108}h^5+O_G(h^6),
\]
where \(W_5(u,v)>0\) is the sum of the products of edge conductances over all length-five walks from \(u\) to \(v\). Conversely, every such connected graph has \(T_G(h)\) strictly positive entrywise for all sufficiently large \(h\). No assertion of uniqueness of the positivity-recovery threshold is made for a general graph.

**Sharp unweighted path boundary.** For the unit-edge path \(P_n\) with integer \(n\ge1\), the completed heat step is entrywise nonnegative at *every* timestep \(h\ge0\) if and only if \(n\le5\). When \(2\le n\le5\), all entries of \(T_{P_n}(h)\) are strictly positive for \(h>0\).

**Exact first failing path.** On \(P_6\), every entry except the two opposite-endpoint entries is strictly positive for every \(h>0\). The two exceptional entries agree and satisfy
\[
[T_{P_6}(h)]_{0,5}=[T_{P_6}(h)]_{5,0}=
\frac{h^5\bigl(h^5+35h^4+168h^3+216h^2+60h-12\bigr)}{
(h^2+4h+6)(2h^2+4h+3)(3h^2+4h+2)(h^4+16h^3+100h^2+96h+36)}.
\]
Let \(\tau\) be the unique positive root of
\[
q(h)=h^5+35h^4+168h^3+216h^2+60h-12.
\]
It lies strictly between \(0.131359\) and \(0.131360\), and \(\tau=0.131359689579\ldots\). The complete admissible set is
\[
T_{P_6}(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad h=0\text{ or }h\ge\tau.
\]

## Assumptions and scope

Each undirected edge has a strictly positive real conductance, graph distance counts edges rather than electrical lengths, and \(L_{uu}=\sum_{v\sim u}w_{uv}\), \(L_{uv}=-w_{uv}\) for adjacent distinct vertices. The graph is finite and connected. The path claims use unit weights and the natural endpoints numbered \(0,\ldots,n-1\). For the one-vertex path the step is the identity. Positivity refers to the *completed* transition matrix, not to intermediate stage vectors, and is entrywise, not a claim of positive definiteness. The Laplacian is symmetric positive semidefinite, so the denominator matrix is invertible at every \(h\ge0\); moreover \(T_G(h)\mathbf 1=\mathbf1\). The primary subject is numerical time integration (MSC2020 65L06).

## Proof

**1. The order-five sign and the diameter obstruction.** The two-stage Radau IIA stability function is
\[
R(z)=\frac{1+z/3}{1-2z/3+z^2/6}
=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{36}-\frac{z^5}{108}+O(z^6).
\]
For the heat generator \(-L\), its completed step is \(R(-hL)\). If \(d_G(u,v)=5\), then \(((-L)^k)_{uv}=0\) for every \(k<5\): every nonzero summand in a matrix-power entry would need at least five off-diagonal moves. For \(k=5\), diagonal stays are impossible, and every contributing term is a product of five positive edge conductances. Thus \(((-L)^5)_{uv}=W_5(u,v)>0\), giving the displayed strictly negative leading coefficient. A graph of diameter at least five contains such a pair along a geodesic, so no sufficiently small positive timestep preserves entrywise nonnegativity.

For the large-timestep assertion, spectral calculus gives \(R(-h\lambda)\to0\) for each positive Laplacian eigenvalue \(\lambda\), while \(R(0)=1\). Connectedness implies \(T_G(h)\to \mathbf1\mathbf1^{\mathsf T}/|V(G)|\). Its entries are strictly positive; because the graph is finite, all entries of \(T_G(h)\) are strictly positive once \(h\) is sufficiently large.

**2. The safe paths and the first failure.** For \(n=2,3,4,5,6\), set
\[
Q_n(h)=6I+4hL_n+h^2L_n^2,\qquad A_n(h)=6I-2hL_n.
\]
The coefficients of \(\det Q_n(h)\) are strictly positive, and \(\det Q_n(h)>0\) for \(h\ge0\) also follows spectrally. Multiply \(Q_n(h)^{-1}A_n(h)\) by \(\det Q_n(h)\) and expand each of its \(n(n+1)/2\) independent upper-triangular entries as an integer polynomial. The complete coefficient arrays for the 55 entries over \(n=2,3,4,5,6\) are given in `certificates/path_radau_coefficients.json`, checked by `verify.py` directly against exact symbolic matrix inverses. For \(n\le5\), every coefficient of every numerator is nonnegative and each numerator has a positive coefficient, so every entry is strictly positive for \(h>0\). For \(n=6\), the same property holds for all upper-triangular entries except \((0,5)\), for which the explicitly displayed rational identity is verified exactly. Symmetry gives the corresponding \((5,0)\) entry. This finite coefficient certificate is exhaustive over the specified path orders; it is not extrapolated to larger orders.

**3. The exact recovery boundary for \(P_6\).** Every factor in the denominator of the displayed opposite-endpoint formula is strictly positive on \([0,\infty)\). The polynomial \(q\) has one sign change in descending coefficient order, so Descartes' rule gives at most one positive root. Since \(q(0)=-12<0\) and \(q(h)\to+\infty\), there is exactly one positive root. Exact rational substitution isolates it between \(131359/10^6\) and \(131360/10^6\). Thus the opposite-endpoint entries are negative precisely for \(0<h<\tau\), vanish at \(\tau\), and are positive beyond it. All remaining entries are strictly positive for \(h>0\), proving the stated admissible timestep set. At \(h=0\), \(T_{P_6}(0)=I\).

## Verification

With SymPy 1.14.0, run `python verify.py` from the directory containing this file. The script reconstructs every listed path Laplacian, the rational step matrix, determinant and all 55 upper-triangular numerator coefficients for \(2\le n\le6\), compares them to the standalone certificate, checks row stochasticity symbolically, establishes the exceptional exact rational identity, isolates the unique root over rational endpoints, verifies the fifth Taylor coefficient, and checks a nonuniformly weighted six-path using an independent exact rational matrix inverse. The completed run prints:

`VERIFY_OK 55 independent path entries, exact denominators, unique P6 root, Radau coefficient, root-isolation and weighted-path checks`

Only the finite certificate concerns \(2\le n\le6\); the all-graph diameter statement is established by the general matrix-power argument above.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten studied loss of positivity under *diagonal* Padé discretization of positive linear systems, with general counterexamples and sufficient criteria; the accessible full text's introduction, Padé definition, positivity theorem and closing discussion do not give the present *subdiagonal* two-stage Radau IIA sharp path boundary or the six-path recovery quintic. The classical two-stage Radau IIA tableau and its stability function are independently documented by Ketcheson's Numipedia. Prior examples of positivity failure for other Padé orders or other graph geometries do not imply the present complete path threshold or exact \(P_6\) classification. The elementary coefficient-to-geodesic mechanism used here supplies an additional universal graph-diameter consequence. The comparison supports a bounded originality assessment, not a claim of exhaustive historical priority.

## Limitations

The exact all-timestep classification is specific to *unweighted paths* up to the sharp six-vertex boundary; the universal diameter result concerns small and large timesteps but does not classify all intermediate positivity windows for arbitrary graphs. The independent certificate confirms finitely many rational identities, not the arbitrary-graph argument by enumeration. The theorem is about the completed third-order Radau IIA step and must not be transferred to different Runge–Kutta schemes or stagewise positivity without proof. Unrecognized equivalent results in specialized historical literature remain possible. No independent mathematical audit has been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, publicly deposited 19 June 2012, Maynooth University repository, https://mural.maynoothuniversity.ie/id/eprint/3761/ ; full text: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .
2. D. I. Ketcheson, *Numipedia: Radau IIA2*, two-stage third-order tableau and stability function, https://ketch.github.io/numipedia/methods/RadauIIA2.html .
