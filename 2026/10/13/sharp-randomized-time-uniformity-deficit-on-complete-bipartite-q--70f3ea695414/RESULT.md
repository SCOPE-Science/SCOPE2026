# Sharp randomized-time uniformity deficit on complete bipartite quantum walks

## Finding

Let \(a,b\) be positive integers. On the unweighted complete bipartite graph \(K_{a,b}\), use the adjacency Hamiltonian \(A\), the continuous-time walk \(U(t)=\exp(\mathrm{i}tA)\), and the transition-probability matrix \(M(t)_{ij}=|U(t)_{ij}|^2\). For every Borel probability law \(\mu\) on nonnegative observation times, set \(\overline M_\mu=\int M(t)\,\mathrm d\mu(t)\). We determine, without restricting the sampling law, the exact squared Frobenius deficit
\[
\Delta_{a,b}=\min_\mu\left\|\overline M_\mu-\frac{J_{a+b}}{a+b}\right\|_F^2.
\]
The minimum is attained. Except on the three-vertex path \(K_{1,2}\), **a single deterministic observation time attains this minimum**. In particular, random sampling cannot improve the Frobenius-optimal fidelity on any \(K_{a,b}\) other than \(K_{1,2}\). For \(K_{1,2}\), randomization makes the minimum zero, while no deterministic time does.

Put \(n=a+b\) and \(p=ab\), and define, for real \(u,v\),
\[
\begin{aligned}
 z&=1-2u+v,\\
 d_a&=1-\frac{2(1-u)}a+\frac{z}{a^2},& o_a&=\frac{z}{a^2},\\
 d_b&=1-\frac{2(1-u)}b+\frac{z}{b^2},& o_b&=\frac{z}{b^2},\\
 c&=\frac{1-v}{p},
\end{aligned}
\]
and the explicit nonnegative polynomial
\[
\begin{aligned}
 F_{a,b}(u,v)={}&a\left(d_a-\frac1n\right)^2+a(a-1)\left(o_a-\frac1n\right)^2\\
 &+b\left(d_b-\frac1n\right)^2+b(b-1)\left(o_b-\frac1n\right)^2
 +2p\left(c-\frac1n\right)^2.
\end{aligned}
\]
Its minimum is the following exact algebraic number, with the displayed optimizing observation law.

**Two vertices.** If \(a=b=1\), then \(\Delta_{1,1}=0\). The deterministic time \(t=\pi/4\) attains it.

**Three vertices.** If \(\{a,b\}=\{1,2\}\), then \(\Delta_{1,2}=0\). Let \(\alpha=\arccos(1/\sqrt3)\). Equal probability on the two times \(\alpha/\sqrt2\) and \((\pi-\alpha)/\sqrt2\) attains the minimum. Every optimizing law has cosine moments \(u=0\), \(v=1/3\); in particular, no deterministic law attains it.

**Other stars.** If \(\{a,b\}=\{1,m\}\), \(m\ge3\), then
\[
\boxed{\Delta_{1,m}=\frac{m(m-3)^2}{(m+1)^2},\qquad
 t_*={\arccos\bigl(-(m-1)/(m+1)\bigr)\over\sqrt m}.}
\]
One observation at \(t_*\) attains the minimum; every optimizing law has the same cosine almost surely.

**Both parts nontrivial.** If \(a,b\ge2\), define
\[
\begin{aligned}
 C&=2p^2-p(3n+4)+2n^2,\\
 K&=p(3n+4)-3n^2,\\
 H&=p^2-p(3n+4)+2n^2.
\end{aligned}
\]
The optimal cosine \(x_*\in[-1,0]\) is determined exactly by
\[
 x_*=\begin{cases}
 -1,&H\ge0,\\
 \text{the unique root in }(-1,0]\text{ of }n^2x^3+Kx+C=0,&H<0.
 \end{cases}
\]
Then
\[
\boxed{\Delta_{a,b}=F_{a,b}(x_*,x_*^2),\qquad
 t_*={\arccos(x_*)\over\sqrt{ab}}.}
\]
A single time \(t_*\) attains the global optimum. All optimizing observation laws have \(\cos(\sqrt{ab}\,T)=x_*\) almost surely; this is an optimizer characterization, not just a value formula.

The particularly transparent two-by-many subfamily satisfies
\[
\boxed{x_*=-\frac{m-2}{m+2},\qquad
\Delta_{2,m}=\frac{(m-2)^2(m+1)}{(m+2)^2}\quad(m\ge2).}
\]
For balanced graphs \(a=b=r\), \(r\ge2\), there is a **sharp change at \(r=6\)**: for \(2\le r\le5\), the optimal cosine lies in \((-1,0]\) and the optimal time allows a positive cross-part transition probability, whereas for every \(r\ge6\), the optimum is attained at \(\cos(rt_*)=-1\), so *all cross-part probabilities vanish at the Frobenius-optimal time*. In the latter regime,
\[
\boxed{\Delta_{r,r}=2r-17+\frac{48}{r}-\frac{32}{r^2}\quad(r\ge6).}
\]

## Assumptions and scope

All graph edges have unit, real, positive adjacency weight; there are no site potentials, decoherence operators, measurements during evolution, or restrictions on the Borel observation-time law. The loss is the **unnormalized squared Frobenius norm** of the complete \((a+b)\)-by-\((a+b)\) average mixing matrix relative to the all-uniform matrix. The same law must work for all initial and target vertices. Observation times are nonnegative real numbers; the quantum walk is finite-dimensional. The result does not address other norms, other Hamiltonians, bounded observation horizons, or the shortest time realizing the optimal cosine.

## Proof

**1. Exact two-moment reduction.** With the bipartition in order, the adjacency matrix has off-diagonal all-ones blocks. Direct multiplication gives \(A^3=pA\). Consequently,
\[
 e^{\mathrm{i}tA}=I+\frac{\mathrm{i}\sin(\sqrt p\,t)}{\sqrt p}A
 +\frac{\cos(\sqrt p\,t)-1}{p}A^2.
\]
Writing \(X=\cos(\sqrt p\,T)\), \(u=\mathbb EX\), \(v=\mathbb EX^2\), the probability of returning to a vertex in the size-\(a\) part is \(d_a\), that of reaching a distinct vertex in that part is \(o_a\), and analogously for the size-\(b\) part. Every cross-part ordered pair has probability \(c\). Counting respectively \(a\), \(a(a-1)\), \(b\), \(b(b-1)\), and \(2ab\) ordered pairs proves that the squared Frobenius loss equals \(F_{a,b}(u,v)\).

All, and only, moment pairs satisfying \(-1\le u\le1\) and \(u^2\le v\le1\) are feasible. Necessity is variance nonnegativity and \(|X|\le1\). For sufficiency with \(|u|<1\), combine a point mass at \(u\) with a \(\{-1,1\}\)-valued distribution of mean \(u\); choose the latter's mixing weight \((v-u^2)/(1-u^2)\). When \(|u|=1\) necessarily \(v=1\). Every such cosine law comes from a nonnegative-time law by the map \(T=\arccos(X)/\sqrt p\). Thus the optimization is *exactly* a compact, two-dimensional moment problem, not a relaxation.

**2. Strict convexity and gradients.** Set
\[
 C=2p^2-p(3n+4)+2n^2.
\]
Expansion and differentiation of the five counted block contributions give
\[
\begin{aligned}
 \partial_u F_{a,b}&=\frac{4}{p^2}\bigl(C+2[p(n+2)-n^2]u\bigr),\\
 \partial_v F_{a,b}&=\frac{2n}{p^2}(p-n+nv),\\
 \partial^2_{uv}F_{a,b}&=0,\\
 \partial^2_{uu}F_{a,b}&=\frac{8}{p^2}[p(n+2)-n^2],\\
 \partial^2_{vv}F_{a,b}&=\frac{2n^2}{p^2}.
\end{aligned}
\]
For \(n\ge3\), \(p\ge n-1\) and \(p(n+2)-n^2\ge n-2>0\). Therefore \(F_{a,b}\) is strictly convex and has a unique minimizing *moment pair*. The exceptional case \(n=2\) is treated directly below.

**3. Nontrivial bipartitions.** If \(a,b\ge2\), then \(p\ge n\). Throughout the feasible set,
\[
\partial_vF_{a,b}=\frac{2n}{p^2}(p-n+nv)\ge0.
\]
For fixed \(u\), minimizing requires \(v=u^2\); replacing a law by the point mass at \(X=u\) cannot increase the loss. Put \(h(x)=F_{a,b}(x,x^2)\), for \(-1\le x\le1\). Differentiation yields
\[
 h'(x)=\frac4{p^2}(n^2x^3+Kx+C),
 \qquad K=p(3n+4)-3n^2.
\]
Here \(n\ge4\), \(K\ge n-4\ge0\), and
\[
 C=2\left(p-\frac{3n+4}{4}\right)^2+
 \frac{7n^2-24n-16}{8}\ge0.
\]
The cubic \(g(x)=n^2x^3+Kx+C\) is strictly increasing. Hence \(g(0)=C\ge0\); a global minimizer cannot lie to the right of zero. Direct substitution gives
\[
 g(-1)=2H,
 \qquad H=p^2-p(3n+4)+2n^2.
\]
If \(H\ge0\), then \(g(x)\ge0\) throughout \([-1,1]\), and the unique minimizing cosine is \(-1\). If \(H<0\), there is exactly one zero in \((-1,0]\); its sign change gives the unique global minimum. This proves the exact formula, the one-time attainment, and uniqueness of the cosine under any minimizing law (since \(v=u^2\) is zero variance).

When \(a=2\), \(b=m\ge2\), direct substitution of \(x=-(m-2)/(m+2)\) into \(g\) gives zero; evaluation of \(F\) gives the displayed closed form. In the balanced case \(n=2r\), \(p=r^2\),
\[
 H=r^2(r^2-6r+4),
\]
which is negative for integers \(2\le r\le5\), and positive for every integer \(r\ge6\). Evaluating \(F_{r,r}(-1,1)\) produces \(2r-17+48/r-32/r^2\). The cross-part probability is \((1-x^2)/r^2\), zero precisely at the stated boundary cosine.

**4. Stars.** Let \(a=1\), \(b=m\ge3\), and set \(x_*=-(m-1)/(m+1)\). Direct exact algebra yields
\[
 \partial_v F_{1,m}(x_*,x_*^2)=\frac{2(m-3)}m\ge0,
 \qquad \partial_u F_{1,m}(x_*,x_*^2)=-2x_*\partial_vF_{1,m}(x_*,x_*^2).
\]
For any feasible \((u,v)\), the supporting linear functional at the candidate equals
\[
 \nabla F_{1,m}(x_*,x_*^2)\!\cdot\!(u-x_*,v-x_*^2)
 =\frac{2(m-3)}m\bigl[(v-u^2)+(u-x_*)^2\bigr]\ge0.
\]
The positive-definite Hessian shows this point is the unique global optimum even when \(m=3\) and the displayed functional vanishes. Substitution gives the star loss and its deterministic attaining time. Interchanging the two parts leaves the matrix norm unchanged.

**5. The two small cases.** For \(K_{1,2}\), setting the five block probabilities equal to \(1/3\) forces \(u=0\) and \(v=1/3\); conversely these moments make all entries \(1/3\). Strict convexity gives the unique optimum moments. The indicated equal-weight two-point cosine law has precisely these moments, so its induced observation-time distribution attains zero loss. No deterministic \(X\) can have \(v=1/3>u^2=0\). For \(K_{1,1}\), the transition matrix is
\[
 M(t)=\begin{pmatrix}\cos^2t&\sin^2t\\\sin^2t&\cos^2t\end{pmatrix};
\]
thus \(t=\pi/4\) attains zero loss. This completes the minimization for all positive part sizes.

## Verification

The accompanying standalone Python standard-library program `verify.py` builds the exact integer adjacency matrices and checks \(A^3=abA\); reconstructs every transition block from exact rational cosine samples; independently checks 432 exact gradient identities; and verifies exact closed formulas for the star, two-by-many, and balanced subfamilies over finite ranges. The executable produces:

`VERIFY_OK exact_gradient_tests=432 exact_matrix_entry_tests=138840 star_formula_tests=72 two_by_many_tests=73 balanced_threshold_tests=73 feasible_two_atom_tests=1872`

The 1,872 feasible two-atom calculations are finite numerical cross-checks, not proof of optimality for arbitrary sampling laws. All unrestricted quantifiers follow from the spectral identity and strict-convexity proof above.

## Relationship to prior work

Baptista, Coutinho, and Marques [1], especially Section 3.1 and Proposition 9, initiated arbitrary-observation-law averages and established the known four small positive complete-bipartite cases, together with a general exclusion for total order greater than seven; their Section 3.2 establishes randomized exact uniform mixing on the three-vertex path. Those known examples and exclusions are **not** claimed as discoveries here. The present contribution solves the distinct global quantitative optimization problem, determines its unique optimal moments, and exposes a sharp threshold at which the best balanced-graph protocol intentionally forbids interpart transport. The spectral formulation and related average-mixing questions surveyed in [2] provide broader context. The ordinary fixed long-time average studied in [3] is one specific sampling law and cannot itself solve a minimum over all sampling laws.

## Limitations

The result is specific to the unnormalized squared Frobenius loss and an unweighted adjacency-driven continuous-time walk. For a balanced graph above the stated threshold, the apparently nonmixing optimal protocol is optimal only for this **global matrix-loss criterion**; it does not maximize cross-part transport, minimize worst-entry error, or imply useful transfer between any selected vertices. Algebraic optimization supplies exact observation times in terms of cosine inverses and cubic roots, not a physically restricted finite-horizon or noise-robust protocol. The source comparison does not rule out an equivalent formula concealed in differently indexed spectral optimization or quantum-transport literature. The included finite calculations do not certify the infinite theorem independently.

## References

[1] Pedro Baptista, Gabriel Coutinho, and Vitor Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (first public 2023-08-31), especially Section 3; Quantum Information Processing 23, article 272 (2024), DOI:10.1007/s11128-024-04480-0.

[2] Gabriel Coutinho and Krystal Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236 (2024), sections discussing generalized average mixing.

[3] Gabriel Coutinho, Chris Godsil, Krystal Guo, and Hanmeng Zhan, *A New Perspective on the Average Mixing Matrix*, Electronic Journal of Combinatorics 25(4), P4.14 (2018), DOI:10.37236/7867.
