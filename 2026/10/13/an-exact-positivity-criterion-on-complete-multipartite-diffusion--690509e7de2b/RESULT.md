# An exact positivity criterion on complete multipartite diffusion graphs

## Finding

Let \(f:[0,\infty)\to\mathbb R\) be continuous with \(f(0)=1\), and define the scalar difference quotient
\[
\Phi_f(s)=\frac{1-f(s)}{s}\qquad(s>0).
\]
For each finite, connected, **unweighted complete multipartite graph** \(G\), write \(L_G=D_G-A_G\) for its combinatorial graph Laplacian. Then the following are equivalent:

1. For **every** such \(G\) and **every** step \(h>0\), the real symmetric matrix \(f(hL_G)\) is entrywise nonnegative.
2. For every \(s>0\), \(0\le f(s)\le1\), and \(\Phi_f\) is nonincreasing on \((0,\infty)\).

This is an if-and-only-if scalar test on the *entire graph family*: no fixed graph size, number of parts, or timestep bound is prescribed.

In particular, consider the fourth-order, two-stage Gauss–Legendre Runge–Kutta end-step map for unit-edge diffusion \(\dot x=-L_Gx\):
\[
T_h=\bigl(12I-6hL_G+h^2L_G^2\bigr)
       \bigl(12I+6hL_G+h^2L_G^2\bigr)^{-1}.
\]
Its scalar multiplier is
\[
f_\mathrm{G}(s)=\frac{s^2-6s+12}{s^2+6s+12},\qquad
\Phi_{f_\mathrm{G}}(s)=\frac{12}{s^2+6s+12}.
\]
Both scalar conditions hold strictly for every \(s>0\). Consequently, for **every** connected unweighted complete multipartite graph and every \(h>0\), \(T_h\) is **strictly positive entrywise, symmetric, positive definite, and doubly stochastic**. Thus this graph family admits an unrestricted positivity interval for the fourth-order Gauss end-step, even though this stability function has absolute-monotonicity radius zero over unrestricted linear problems.

## Assumptions and scope

The graph is \(G=K_{a_1,\ldots,a_k}\) with \(k\ge2\) and integers \(a_i\ge1\), and \(n=\sum_i a_i\). Its vertices are partitioned into \(k\) independent parts, with each edge between distinct parts present at unit conductance. The Laplacian is the **unnormalized** \(L_G=D_G-A_G\); the generator of continuous-time diffusion is \(Q=-L_G\). All spectral matrix functions use the real symmetric functional calculus. The universal quantifiers range over all such finite graphs and all real steps \(h>0\).

The scalar criterion does not require differentiability or analyticity of \(f\); continuity plus \(f(0)=1\) suffice. It concerns end-step entrywise nonnegativity, not stage-by-stage positivity of a Runge–Kutta method. For \(k=1\) the graph has no edges and its Laplacian is zero, a trivial case deliberately excluded from the strict-positivity conclusion.

## Proof

### Exact spectral projectors

Set \(J_m=\mathbf1_m\mathbf1_m^{\mathsf T}\). On the \(n\)-vertex space let
\[
E=\frac{J_n}{n},\qquad
B=\operatorname{diag}\!\left(\frac{J_{a_1}}{a_1},\ldots,\frac{J_{a_k}}{a_k}\right),
\qquad
W_i=I_{\mathrm{part}\ i}-\frac{J_{a_i}}{a_i},
\]
where each \(W_i\) is extended by zeros outside its part. The matrices \(E\), \(B-E\), and \(W_1,\ldots,W_k\) are mutually orthogonal projectors summing to \(I\). Directly from the complete multipartite adjacency pattern,
\[
L_GE=0,\qquad
L_G(B-E)=n(B-E),\qquad
L_GW_i=(n-a_i)W_i.
\]
Thus, for \(h>0\),
\[
\boxed{\ f(hL_G)=E+f(nh)(B-E)+\sum_{i=1}^k f((n-a_i)h)W_i.\ }
\tag{1}
\]
Because \(k\ge2\), each number \(n-a_i\) is positive.

### All entry types

If distinct vertices \(u,v\) are in different parts, formula (1) gives
\[
[f(hL_G)]_{uv}=\frac{1-f(nh)}{n}=h\Phi_f(nh).
\tag{2}
\]
If distinct vertices lie in the same part \(i\), putting \(d_i=n-a_i\) gives
\[
\begin{aligned}
[f(hL_G)]_{uv}
 &=\frac{a_i+d_i f(nh)-n f(d_i h)}{a_i n}\\
 &=\frac{d_i h}{a_i}\bigl(\Phi_f(d_i h)-\Phi_f(nh)\bigr).
\end{aligned}
\tag{3}
\]
For a vertex \(u\) in part \(i\), the diagonal is
\[
[f(hL_G)]_{uu}=\frac1n+\frac{d_i}{a_i n}f(nh)
 +\left(1-\frac1{a_i}\right)f(d_i h).
\tag{4}
\]
All coefficients in (4) are nonnegative. Therefore \(0\le f(s)\le1\) and nonincreasing \(\Phi_f\) make (2)--(4) nonnegative, proving sufficiency. Furthermore \(f(hL_G)\mathbf1=\mathbf1\) from \(f(0)=1\), and symmetry gives the column sums.

### Necessity of the three scalar restrictions

Suppose \(f(hL_G)\) is entrywise nonnegative for every graph and step.

First use \(G=K_2\), choosing \(h=s/2\) for arbitrary \(s>0\). The different-part entry (2) is \((1-f(s))/2\), hence \(f(s)\le1\).

Next use \(G=K_m\), viewed as \(m\) singleton parts, and set \(h=s/m\). Formula (4) becomes
\[
[f(hL_{K_m})]_{uu}=\frac{1+(m-1)f(s)}m\ge0.
\]
For each fixed \(s>0\) this inequality holds for all integers \(m\ge2\); letting \(m\to\infty\) yields \(f(s)\ge0\). The limit is only a device to infer a scalar sign from an infinite graph family; no finite computation is substituted for it.

Finally fix \(t>0\) and an arbitrary rational \(r>1\). Write \(r=1+p/q\) with positive integers \(p\ge2\), \(q\ge1\), multiplying numerator and denominator if needed. In the graph \(K_{p,q}\), choose two distinct vertices in the part of size \(p\) and set \(h=t/q\). Formula (3) is nonnegative only if
\[
\Phi_f(t)\ge\Phi_f(rt).
\]
Every real \(r>1\) is a limit of such rationals. Continuity of \(\Phi_f\) away from zero implies that \(\Phi_f(t)\ge\Phi_f(rt)\) for all real \(r>1\), proving monotonicity. All three conditions are therefore necessary, and the equivalence follows.

### Fourth-order Gauss consequence and strictness

For \(s>0\), \(s^2-6s+12=(s-3)^2+3>0\), while the denominator of \(f_\mathrm G\) exceeds the numerator by \(12s\). Hence \(0<f_\mathrm G(s)<1\). Moreover
\[
\Phi'_{f_\mathrm G}(s)=-\frac{12(2s+6)}{(s^2+6s+12)^2}<0.
\]
Thus the different-part entries in (2) are strictly positive; for parts with at least two vertices, the same-part entries in (3) are strictly positive because \(d_i<n\). All diagonal entries in (4) exceed zero. The eigenvalues of \(T_h=f_\mathrm G(hL_G)\) are \(1\), \(f_\mathrm G(nh)\) and \(f_\mathrm G((n-a_i)h)\) with the indicated multiplicities; all are strictly positive. This establishes the stated strict entrywise positivity, positive definiteness, and double stochasticity for every finite graph and step.

### A precise failure when the divided-difference condition is dropped

The first two scalar restrictions alone do not suffice. The continuous multiplier \(g(s)=1/(1+s^2)\) satisfies \(g(0)=1\) and \(0<g(s)\le1\). But \(\Phi_g(s)=s/(1+s^2)\) increases near zero. In \(K_{2,1}\) with \(h=1/10\), the same-part off-diagonal entry is
\[
\frac1{20}\left(\frac{1/10}{1+1/100}-\frac{3/10}{1+9/100}\right)<0.
\]
Hence the divided-difference inequality is not a redundant reformulation of scalar nonnegativity. Conversely, the Crank--Nicolson multiplier \((2-s)/(2+s)\) has decreasing \(\Phi\) but becomes negative for \(s>2\), and sufficiently large complete graphs detect that failure on their diagonals.

## Verification

The standalone, standard-library-only script `artifacts/verify.py` constructs rational graph Laplacians and the rational Gauss propagator independently of the projector formula. For every ordered multipartite composition with \(2\le n\le8\), it checks four positive rational steps, plus five larger targeted graphs: **993 exact rational graph-step cases**. For each case, it independently inverts the rational quadratic denominator, verifies the full entrywise projector identity, checks strict entrywise positivity, and checks exact row sums. It also checks the scalar inequalities and two examples showing the necessity of separate restrictions. It prints `VERIFY_OK` upon success.

The all-size claim is proved above by the projectors and elementary scalar inequalities; the finite checks merely test the algebra and implementation. For illustration, \(G=K_{2,1}\), \(h=1\) gives the exact transition matrix
\[
T_1=\begin{pmatrix}
131/247&40/247&4/13\\
40/247&131/247&4/13\\
4/13&4/13&5/13
\end{pmatrix},
\]
which is strictly positive and doubly stochastic despite having positive two-step connections between nonadjacent vertices.

## Relationship to prior work

Lóczi and Ketcheson study the absolute-monotonicity radius of rational stability functions and explicitly record radius zero for the fourth-order \([2/2]\) Padé approximant; this is a general unrestricted-method restriction, **not** a result about positive spectral functions on complete multipartite graph Laplacians. Zappavigna, Colaneri, Kirkland and Shorten give a nilpotent-chain counterexample to unconditional Padé positivity and a sufficient matrix-entry condition for short steps on Hurwitz Metzler matrices. Their condition requires a positive off-diagonal wherever certain squared-generator entries are nonzero; complete multipartite graphs with nonsingleton parts have pairs connected by two-step paths without direct edges, so their sufficient criterion does not imply this graph-family theorem.

Blanes, Iserles and Macnamara investigate positivity-preserving integrators using other constructions, not this exact iff characterization for a fixed graph family. The published result *Eight-state barrier for Markov positivity of the [2/2] Padé map* analyzes dimension-minimal small-step failures and one pure-birth generator; neither its dimension bound nor its witness determines positivity for all steps on all undirected complete multipartite graphs. The individual complete-bipartite fourth-order Padé positivity statement is treated as an existing special case, not as a stand-alone new result here. Known complete-multipartite Laplacian spectra are used in the present proof; the potentially new assertion is the **universal if-and-only-if criterion for every continuous scalar filter**. The Gauss method illustrates the scope of this criterion, including graphs with three or more parts, rather than constituting a second unrelated claim.

## Limitations

The characterization applies to **unweighted complete multipartite** undirected graphs, with no claim for arbitrary weighted, directed, normalized, or general undirected Laplacians. It guarantees positivity only of the **one-step matrix**, not internal Runge–Kutta stages, nonlinear transformations, or finite-precision computations. Because \(f_\mathrm G(s)\to1\) as \(s\to\infty\), the unconditionally positive Gauss method is not asserted to have stiff decay, optimal mixing, or a useful large-step accuracy bound. Positive definiteness here is spectral, not an independent numerical stability estimate. The bibliography comparison is not an exhaustive novelty certificate; older graph-matrix-function literature may express an equivalent classification with different terminology.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, first submitted 26 March 2013, Section 2.2.1. https://arxiv.org/abs/1303.6651
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially negative news about positive systems*, Linear Algebra and its Applications 436 (2012), 3425–3442, Section 4 and Theorem 3. https://doi.org/10.1016/j.laa.2011.12.021
3. S. Blanes, A. Iserles, S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242. https://arxiv.org/abs/2102.08242
4. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md
