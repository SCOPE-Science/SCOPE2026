# Sharp persistent one-leaf instability of adjacency quantum walks on growing cliques

## Finding

For every integer \(m\geq 3\), let \(Z_m\) be the graph formed by adding a single new pendant vertex \(p\) to a distinguished vertex \(h\) of the complete graph \(K_m\). Compare the unweighted adjacency quantum walks on \(Z_m\) and its induced core \(K_m\) on the *same labeled core vertices*. Write \(U_G(t)=\exp(\mathrm{i}tA(G))\), and define
\[
\mathcal D_m=\sup_{t\geq0}\ \max_{u,v\in V(K_m)}
\left|\,|U_{Z_m}(t)_{uv}|-|U_{K_m}(t)_{uv}|\,\right|.
\]
Then the **sharp uniform-in-time induced-subgraph discrepancy** satisfies
\[
\boxed{\mathcal D_m=1-\frac1{\sqrt5}+O(m^{-1})\quad(m\to\infty).}
\]
In particular its limit is strictly positive, even though only one vertex and one edge are attached outside an arbitrarily large complete induced subgraph. The exceptional core entry is the return amplitude at the attachment vertex \(h\): every other core entry obeys a uniform complex-amplitude bound tending to zero. A *single fixed observation time*, \(t_*=\pi/\sqrt5\), already attains the limiting discrepancy.

## Assumptions and scope

All graphs are finite, simple, undirected, unweighted and labeled. Each graph uses the **adjacency** Hamiltonian and the convention \(U(t)=\exp(\mathrm{i}tA)\). A sign reversal of time does not change the asserted modulus comparison. The induced subgraph includes all \(m\) clique vertices; its distinguished attachment vertex \(h\) is not removed. The supremum is over the entire half-line of real observation times, with no finite-time horizon. The symbol \(O(m^{-1})\) asserts the existence of constants \(C,m_0\) such that the absolute error is at most \(C/m\) whenever \(m\geq m_0\); no optimal finite-size constant is asserted.

## Proof

**Step 1: Exact invariant subspace.** Put \(R=V(K_m)\setminus\{h\}\) and \(|w\rangle=(m-1)^{-1/2}\sum_{u\in R}|u\rangle\). The subspace spanned by \((|h\rangle,|w\rangle,|p\rangle)\) is invariant under the adjacency operator of \(Z_m\); its real symmetric matrix is
\[
B_m=\begin{pmatrix}
0&\sqrt{m-1}&1\\
\sqrt{m-1}&m-2&0\\
1&0&0
\end{pmatrix}.
\]
Every vector supported on \(R\) whose coordinates sum to zero is an eigenvector with eigenvalue \(-1\), orthogonal to \(|h\rangle\) and \(|p\rangle\). A determinant calculation gives
\[
f_m(x)=\det(xI-B_m)=x^3-(m-2)x^2-mx+(m-2).
\]
For \(m\geq3\), the signs of this polynomial at \(-2,-1,0,1,m-1,m\) exhibit three distinct real roots \(\lambda_{m,-}\in(-2,-1)\), \(\lambda_{m,+}\in(0,1)\), and \(\lambda_{m,H}\in(m-1,m)\). These are all its roots.

**Step 2: Limiting spectral masses at the marked vertex.** Uniformly on every bounded interval,
\[
\frac{f_m(x)}m=-(x^2+x-1)+\frac{x^3+2x^2-2}{m}.
\]
As the zeros of \(x^2+x-1\) are simple, elementary root continuity (or the mean-value theorem on fixed disjoint neighborhoods) gives
\[
\lambda_{m,\pm}=\frac{-1\pm\sqrt5}{2}+O(m^{-1}).
\]
For a simple eigenvalue \(\lambda\) of \(B_m\), its spectral projector's \((h,h)\) entry equals the diagonal resolvent residue,
\[
a_m(\lambda)=\frac{\lambda(\lambda-m+2)}{f_m'(\lambda)}.
\]
Indeed the cofactor of the \((h,h)\) entry of \(xI-B_m\) is \(x(x-m+2)\). Substituting the two bounded roots into the residue expression gives
\[
\begin{aligned}
a_{m,-}&=\frac{1+1/\sqrt5}{2}+O(m^{-1})=:\alpha+O(m^{-1}),\\
a_{m,+}&=\frac{1-1/\sqrt5}{2}+O(m^{-1})=:\beta+O(m^{-1}).
\end{aligned}
\]
All masses are nonnegative and sum to one, so the high-energy mass is \(a_{m,H}=1-a_{m,-}-a_{m,+}=O(m^{-1})\). Notice \(\alpha>1/2\), \(\alpha+\beta=1\), and \(\alpha-\beta=1/\sqrt5\).

**Step 3: Upper bound for the marked return discrepancy.** The diagonal return amplitude on \(Z_m\) is
\[
U_{Z_m}(t)_{hh}=a_{m,-}e^{\mathrm{i}\lambda_{m,-}t}+a_{m,+}e^{\mathrm{i}\lambda_{m,+}t}+a_{m,H}e^{\mathrm{i}\lambda_{m,H}t}.
\]
For all sufficiently large \(m\), \(a_{m,-}>1/2\). The reverse triangle inequality therefore yields, **for every real \(t\)**,
\[
|U_{Z_m}(t)_{hh}|\geq 2a_{m,-}-1=\frac1{\sqrt5}+O(m^{-1}).
\]
The clique return amplitude is exactly
\[
U_{K_m}(t)_{hh}=\frac1m e^{\mathrm{i}(m-1)t}+
\left(1-\frac1m\right)e^{-\mathrm{i}t},
\]
so \(1-2/m\leq|U_{K_m}(t)_{hh}|\leq1\). Because both moduli are at most one, their absolute difference is at most
\[
\max\{1-(2a_{m,-}-1),\,2/m\}
=1-1/\sqrt5+O(m^{-1}),
\]
uniformly over all times.

**Step 4: Matching lower bound at a fixed time.** Let \(t_*=\pi/\sqrt5\). The two bounded limiting eigenvalues differ by \(\sqrt5\), hence their exponentials at \(t_*\) have opposite phase. Step 2 and \(a_{m,H}=O(m^{-1})\) give
\[
\begin{aligned}
|U_{Z_m}(t_*)_{hh}|&=|\alpha e^{\mathrm{i}\lambda_-t_*}+\beta e^{\mathrm{i}\lambda_+t_*}|+O(m^{-1})\\
&=\alpha-\beta+O(m^{-1})=1/\sqrt5+O(m^{-1}),
\end{aligned}
\]
where \(\lambda_\pm=(-1\pm\sqrt5)/2\). The exact clique expression gives \(|U_{K_m}(t_*)_{hh}|=1+O(m^{-1})\). Thus the single \((h,h)\) comparison already equals \(1-1/\sqrt5+O(m^{-1})\).

**Step 5: Every other core amplitude is uniformly stable.** For \(u,v\in R\), decompose the standard basis vectors into \(|w\rangle\) and its orthogonal complement. With \(b_m(t)=\langle w|e^{\mathrm{i}tB_m}|w\rangle\), unitarity gives \(|b_m(t)|\leq1\), and
\[
\begin{aligned}
U_{Z_m}(t)_{uv}&=e^{-\mathrm{i}t}\left(\delta_{uv}-\frac1{m-1}\right)+\frac{b_m(t)}{m-1},\\
U_{K_m}(t)_{uv}&=e^{-\mathrm{i}t}\left(\delta_{uv}-\frac1m\right)+\frac{e^{\mathrm{i}(m-1)t}}m.
\end{aligned}
\]
The triangle inequality proves \(|U_{Z_m}(t)_{uv}-U_{K_m}(t)_{uv}|\leq2/(m-1)\) for every time. For \(u\in R\), the invariant-subspace decomposition and unitarity give \(|U_{Z_m}(t)_{hu}|\leq1/\sqrt{m-1}\); the complete-graph formula gives \(|U_{K_m}(t)_{hu}|\leq2/m\). Hence
\[
\sup_{t\geq0}\max_{(u,v)\ne(h,h)}
|U_{Z_m}(t)_{uv}-U_{K_m}(t)_{uv}|
\leq\max\left\{\frac2{m-1},\frac1{\sqrt{m-1}}+\frac2m\right\}\longrightarrow0.
\]
The absolute difference of moduli never exceeds the absolute difference of the complex amplitudes. Thus no other core pair affects the positive limiting supremum, and the bounds of Steps 3–4 prove the claim. \(\square\)

## Verification

A standalone checker is provided as `verify.py`. Run it with `python3 verify.py` in an environment containing NumPy and SymPy. It independently constructs the full adjacency matrices of \(Z_m\) and \(K_m\), compares their numerical matrix exponentials obtained by real-symmetric diagonalization against the reduced-block formula, verifies the cubic characteristic polynomial and cofactor symbolically, and checks the stated uniform bounds on a finite deterministic sample. It also evaluates the spectral masses at increasing \(m\). These finite calculations corroborate the formulas; the unrestricted assertion follows from the preceding proof, not from finite sampling.

## Relationship to prior work

Coutinho, Baptista, Godsil, Spier and Werner develop the spectral theory of adjacency-driven quantum walks, including exact treatment of transition amplitudes, their regions in the complex plane, and transfer-probability suprema [1]. That general framework supplies context but does not give the asymptotic one-leaf induced-clique discrepancy above. Kirkland and Monterde prove a vanishing uniform-in-time modulus bound for **join graphs** and explicitly ask for analogous bounds when a graph is merely an **induced subgraph**, singling out complete induced subgraphs [2, Section 12]. Attaching a pendant leaf does not satisfy their join hypothesis; this theorem exhibits a sharp obstruction to an unrestricted vanishing bound, localized to the attachment vertex. The later localization study [3] treats normalized adjacency evolution on barbell and star-of-cliques graph families and long-time inverse-participation statistics, rather than the unnormalized adjacency single-pendant clique or the supremum of differences against an induced subgraph. Prior work is not claimed to settle all formulations of this problem.

## Limitations

The result concerns exactly **one pendant vertex attached to one vertex of a growing clique**, with unnormalized adjacency evolution; it does not classify perturbations by longer paths, multiple leaves, weighted edges, normalized adjacency, or Laplacian dynamics. It determines the leading sharp asymptotic and first-order rate, not an exact closed formula for the supremum at each finite \(m\). No uniqueness of novelty across unpublished literature is asserted. Numerical checks cover finitely many sizes and times and cannot prove the infinite-domain statement.

## References

[1] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 18 August 2022), https://arxiv.org/html/2208.08971v1. Primary MSC 81P68.

[2] S. Kirkland and H. Monterde, *Quantum walks on join graphs*, arXiv:2312.06906v1 (12 December 2023), https://arxiv.org/html/2312.06906v1. Relevant Sections 11–12.

[3] S. Dhamapurkar and K. V. Subrahmanyam, *Localization Without Disorder: Quantum Walks on Structured Graphs*, arXiv:2603.05643v1 (5 March 2026), https://arxiv.org/html/2603.05643v1. Relevant Sections II–III and VII.
