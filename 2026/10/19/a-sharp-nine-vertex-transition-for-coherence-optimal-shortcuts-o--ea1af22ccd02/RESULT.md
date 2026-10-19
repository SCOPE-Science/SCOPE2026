# A sharp nine-vertex transition for coherence-optimal shortcuts on paths

## Finding

**Theorem (global first transition and macroscopic optimal span).** Let \(n\geq3\) be an integer. In the unit-conductance path \(P_n\), with vertices \(0,1,\ldots,n-1\), insert exactly one previously absent edge \(\{i,j\}\), where \(0\leq i<j-1<n-1\), with prescribed conductance \(w>0\). Leave every original path conductance fixed at one. Minimize \(\operatorname{tr}(L^+)\), equivalently the Kirchhoff index \(n\operatorname{tr}(L^+)\) or half-trace stochastic consensus coherence, over all eligible edges.

1. For \(3\leq n\leq8\) and every \(w>0\), the **unique** optimal added edge joins the two endpoints \(\{0,n-1\}\).
2. For each \(n\geq9\) put
   \[
   W_n=\frac{12(n-2)}{(n-3)(n-1)(n-8)}.
   \]
   For \(0<w<W_n\), the endpoint edge is uniquely optimal. At \(w=W_n\), **exactly** the endpoint edge \(\{0,n-1\}\) and the next-inward edge \(\{1,n-2\}\) are optimal. For \(w>W_n\), the endpoint edge is strictly suboptimal. Thus nine vertices is the smallest size at which an interior chord can be globally optimal at any finite positive conductance, and \(W_9=7/4\). Moreover \(n^2W_n\to12\).
3. Every optimal edge of prescribed span \(d=j-i\) is as centered as possible: its left endpoint is one of \(\lfloor(n-1-d)/2\rfloor\) and \(\lceil(n-1-d)/2\rceil\). In particular, if \(w>0\) is independent of \(n\), then the span \(d_n\) of **every** globally optimal shortcut satisfies
   \[
   \frac{d_n}{n}\longrightarrow\frac34,\qquad
   \frac{i_n}{n}\longrightarrow\frac18,\qquad
   \frac{j_n}{n}\longrightarrow\frac78.
   \]
   Furthermore the best achievable trace satisfies
   \[
   \min_{i,j}\frac{\operatorname{tr}(L_n(i,j,w)^+)}{n^2}\longrightarrow\frac7{96},
   \]
   whereas choosing the endpoint edge at the same fixed conductance gives limit \(1/12\). The optimal large-path design therefore reduces the leading trace by one eighth relative to the endpoint-shortcut design.

The exact gain formula, valid for every admissible edge, is
\[
\operatorname{tr}(L_{P_n}^+)-\operatorname{tr}(L_n(i,i+d,w)^+)
=\frac{w}{1+wd}\left[
\frac{nd^2}{4}-\frac{d^3}{6}+\frac d6
-\frac{d^2(d+2i-n+1)^2}{4n}
\right].
\]

## Assumptions and scope

The graph is the *undirected* simple path, with unit conductances on its \(n-1\) original edges. The added edge is a nonedge and has the same prescribed positive conductance regardless of placement; no weight budget, joint reoptimization of existing weights, node-dependent price, or second shortcut is permitted. The Laplacian \(L_n(i,j,w)=L_{P_n}+w(e_i-e_j)(e_i-e_j)^{\mathsf T}\) is connected and has one-dimensional nullspace. The Moore–Penrose pseudoinverse is written \(L^+\), and \(\operatorname{tr}(L^+)\) is the sum of reciprocals of its positive eigenvalues. For the Itô process \(dX=-LX\,dt+dB\) with independent unit-intensity Brownian disturbances, total stationary variance of the disagreement coordinates equals \(\tfrac12\operatorname{tr}(L^+)\). All maximizations and all asserted uniqueness statements range over the explicitly specified chords only.

## Proof

**1. Rank-one trace reduction and explicit ramp.** Let \(b=e_i-e_{i+d}\). On the subspace perpendicular to constants, \(L_{P_n}\) is positive definite. Sherman–Morrison on this subspace gives
\[
\operatorname{tr}(L_{P_n}^+)-\operatorname{tr}((L_{P_n}+wbb^{\mathsf T})^+)
=\frac{w\|L_{P_n}^+b\|_2^2}{1+w\,b^{\mathsf T}L_{P_n}^+b}.
\]
The unit-resistance path has \(b^{\mathsf T}L_{P_n}^+b=d\). Define the clipped ramp
\[
\phi_k=\begin{cases}
0,&0\leq k\leq i,\\
k-i,&i<k<i+d,\\
d,&i+d\leq k\leq n-1.
\end{cases}
\]
Directly, \(L_{P_n}\phi=-b\), so \(L_{P_n}^+b=-(\phi-\bar\phi\mathbf1)\). If \(r=n-1-i-d\) is the right tail length, then
\[
\sum_{k=0}^{n-1}\phi_k=\frac{d(d-1)}2+(r+1)d,
\qquad
\sum_{k=0}^{n-1}\phi_k^2=\frac{d(d-1)(2d-1)}6+(r+1)d^2.
\]
Subtracting the squared mean yields
\[
V_n(i,d):=\|L_{P_n}^+b\|_2^2
=\frac{nd^2}{4}-\frac{d^3}{6}+\frac d6
-\frac{d^2(d+2i-n+1)^2}{4n}.
\]
Thus the gain is \(G_n(i,d,w)=wV_n(i,d)/(1+wd)\), proving the displayed formula. For fixed \(d\), its denominator is independent of \(i\), so optimality is equivalent to minimizing \(|d+2i-n+1|\); hence all fixed-span maximizers are centered.

**2. Endpoint comparisons.** Write \(N=n-1\), let \(V_d=\max_i V_n(i,d)\), and put \(t=N-d\) and \(e=t\bmod2\in\{0,1\}\). The preceding square term gives
\[
V_d=\frac{nd^2}{4}-\frac{d^3}{6}+\frac d6-\frac{ed^2}{4n},
\qquad V_N=\frac{n(n^2-1)}{12}.
\]
For any \(2\leq d<N\), define the difference of cross-multiplied gains
\[
D_d(w)=V_N-V_d+w(dV_N-NV_d).
\]
Because the denominators of the gains are positive, the endpoint chord is better than every chord of span \(d\) precisely when \(D_d(w)>0\); equality means a tie with centered chords of that span.

We always have \(V_N>V_d\). Indeed set \(u_k=k\). The ramp \(\phi\) and \(u-\phi\) are both nondecreasing sequences; moreover \(u-\phi\) is nonconstant unless \(d=N\). The pairwise-difference identity for covariance implies \(\operatorname{Cov}(\phi,u-\phi)\geq0\). Consequently \(\operatorname{Var}(u)=\operatorname{Var}(\phi)+\operatorname{Var}(u-\phi)+2\operatorname{Cov}(\phi,u-\phi)>\operatorname{Var}(\phi)\) for \(d<N\), as required. Therefore \(D_d(0)>0\).

For \(n\leq8\), an exact identity reads
\[
12\left(\frac{V_N}{N}-\frac{V_d}{d}\right)
=t(2t+4-n)+\frac{3ed}{n}.
\]
For \(t\geq2\), this is nonnegative because \(n\leq8\); for \(t=1\), it is also nonnegative when \(n\leq6\), and positive when \(n=7,8\) by direct substitution. Hence \(dV_N-NV_d\geq0\) for every competing span when \(n\leq8\). Together with \(D_d(0)>0\), this proves strict endpoint optimality for all \(w>0\). For \(n=3\) there is just one admissible chord.

**3. Sharp first transition for \(n\geq9\).** Define the positive critical value
\[
W_n=\frac{12(n-2)}{(n-3)(n-1)(n-8)}.
\]
Fix a competing span \(d=N-t\). First pretend the centering parity term is zero, so use \(V_d^{(0)}=nd^2/4-d^3/6+d/6\). Exact polynomial simplification gives
\[
D_d^{(0)}(W_n)
=\frac{n(n+1)t(t-2)(3n-10-2t)}{12(n-8)(n-3)}.
\]
The final factor is strictly positive for \(1\leq t\leq n-3\). For even \(t\geq2\), the true parity term is zero, so this expression is nonnegative and vanishes only at \(t=2\). For odd \(t\geq3\), the actual difference is even larger:
\[
D_d(W_n)=D_d^{(0)}(W_n)+\frac{d^2}{4n}(1+W_nN)>0.
\]
For the remaining odd value \(t=1\), direct cancellation gives
\[
D_{n-2}(W_n)=\frac{n+1}{(n-8)(n-3)}>0.
\]
It follows that the only zero comparison at \(w=W_n\) is \(t=2\), namely \(d=n-3\), whose sole centered placement is \(\{1,n-2\}\). Since \(D_d(0)>0\) and \(D_d(w)\) is affine in \(w\), every comparison is strictly positive for \(0<w<W_n\). The exceptional comparison satisfies
\[
V_N-V_{n-3}=2(n-2),\qquad
NV_{n-3}-(n-3)V_N=\frac{(n-3)(n-1)(n-8)}6>0.
\]
Thus \(D_{n-3}(w)<0\) for all \(w>W_n\), giving the advertised strict loss of endpoint optimality. Substituting \(n=9\) yields \(W_9=7/4\); direct leading-order division gives \(n^2W_n\to12\). The proof makes no assertion about the complete hierarchy of later, post-threshold span changes.

**4. Fixed-conductance large-path limit.** For a best-centered chord of span \(d\), the parity penalty in \(V_d\) is at most \(d^2/(4n)\). If \(d/n\to x\in(0,1]\), then for any fixed \(w>0\)
\[
\frac{G_n(d,w)}{n^2}\longrightarrow f(x):=\frac{x}{4}-\frac{x^2}{6}.
\]
When \(d/n\to0\), the bound \(G_n(d,w)\leq nd/4+d/6\) implies the normalized gain tends to zero, which is \(f(0)\). This establishes the required convergence along every sequence of candidate spans. The strictly concave function \(f\) has its unique maximum at \(x=3/4\), with value \(3/32\). Compactness and comparison with centered spans nearest to \(3n/4\) show that **every** maximizing span obeys \(d_n/n\to3/4\). Fixed-span centering then gives the two endpoint limits. The baseline path trace is \((n^2-1)/6\); subtracting the limiting maximum gain \(3n^2/32\) gives \(7/96\). The endpoint design corresponds to \(x=1\), with gain limit \(1/12\) and remaining trace limit \(1/12\), completing the theorem.

## Verification

The standalone standard-library script `verify.py` uses exact rational arithmetic. It constructs each updated Laplacian shifted by the constant projector, inverts it by rational Gauss–Jordan elimination, and compares its trace against the closed gain formula. It also exhaustively compares every eligible chord at selected exact positive conductances for sizes \(3\) through \(80\), including each applicable critical conductance, and checks near-asymptotic maximizing positions on four larger paths. Running `python3 verify.py` emitted:

`VERIFY_OK direct_rational_inverses= 304 global_exact_chord_comparisons= 246536 macroscopic= [(100, 75, 12), (200, 151, 24), (400, 301, 49), (800, 601, 99)]`

The universal threshold and large-size claims rely on the preceding analytic proof, **not** on the finite enumeration. The checker uses only Python's standard library and requires no external data or packages.

## Relationship to prior work

The total-resistance objective and edge-addition motivation are established in Ellens et al. (2011), especially their Section 3.6, which exhibits graph examples where the largest-resistance pair need not be the best insertion. Summers et al. (2014), especially Section III and Lemma 1, derive generic rank-one pseudoinverse updates for the same noisy-consensus objective. Wang et al. (2014) and Predari et al. (2023) study network resistance improvements from edge insertion with algorithms and examples. Those general results motivate the problem and yield the update *framework*, which is **not** claimed as new. The present contribution is the exact all-span **unit-path** comparison with fixed added conductance, the first-size and first-weight transition, unique critical tie, and the asymptotic three-quarter-span law. None of those exact conclusions appears in the inspected relevant material of those works; an unlocated equivalent historical result cannot be ruled out.

## Limitations

Only one extra chord is optimized; its conductance is given, and original path conductances are fixed. The theorem does not characterize the entire succession of optimal chord spans after the first threshold for finite \(n\), nor does it address heterogeneous edge prices, a joint conductance budget, other connected graphs, or multi-edge augmentation. Spectral gap optimization is different from trace-pseudoinverse optimization. The analytic first transition is fully proved, but independent mathematical review and historical priority verification have not been performed.

## References

- W. Ellens, F. M. Spieksma, P. Van Mieghem, A. Jamakovic, and R. E. Kooij, “Effective graph resistance,” *Linear Algebra and its Applications* **435** (2011), 2491–2506, DOI:10.1016/j.laa.2011.02.024. Relevant discussion: Section 3.6, pp. 12–14.
- T. Summers, I. Shames, J. Lygeros, and F. Dörfler, “Topology Design for Optimal Network Coherence,” arXiv:1411.4884v1 (first posted 2014-11-18), Sections II–III and Lemma 1. Full text: https://arxiv.org/html/1411.4884v1.
- X. Wang, Y. Koç, R. E. Kooij, and P. Van Mieghem, “Improving robustness of complex networks via the effective graph resistance,” *European Physical Journal B* **87** (2014), DOI:10.1140/epjb/e2014-50276-0.
- M. Predari, L. Berner, R. Kooij, and H. Meyerhenke, “Greedy optimization of resistance-based graph robustness with global and local edge insertions,” *Social Network Analysis and Mining* **13** (2023), article 130, DOI:10.1007/s13278-023-01137-1; https://link.springer.com/article/10.1007/s13278-023-01137-1.
