# Sharp chord-activation threshold in spectral-gap design of asymmetric barbells

## Finding

For integers \(q\ge 2\) and \(p>2q\), join two complete graphs \(K_p\) and \(K_q\) by a single edge between distinguished hub vertices. Independently assign a nonnegative conductance \(w_e\) to every graph edge, with one unit of cost per unit of conductance, and fix \(\sum_e w_e=B>0\). Write \(\lambda_2(L(w))\) for the second-smallest eigenvalue of the combinatorial weighted Laplacian. Put

\[
D=p+4q-4,\qquad \Delta=p(p-1)-2(2q-1)^2,\qquad \ell=B/D.
\]

**Exact sharp structural transition.** If \(\Delta\le0\), then the global maximum is \(\ell\), and its **unique unrestricted** maximizing assignment is:

\[
\begin{aligned}
w_{u i}&=\ell &&\text{for every nonhub vertex }i\text{ in }K_p,\\
w_{v j}&=2\ell &&\text{for every nonhub vertex }j\text{ in }K_q,\\
w_{uv}&=(2q-1)\ell,\\
w_e&=0 &&\text{for every edge between two nonhub vertices.}
\end{aligned}
\]

If \(\Delta>0\), the unrestricted maximum is **strictly greater** than \(\ell\); moreover **every** optimal assignment places positive conductance on at least one edge between two nonhub vertices of the larger clique \(K_p\). In this second regime no formula for the new optimal value or complete optimal allocation is claimed.

The transition is nonempty and quantitative: for example \((p,q)=(7,3)\) has \(\Delta=-8\), so its optimum is \(B/15\) and all internal nonhub chords vanish; for \((p,q)=(8,3)\), \(\Delta=6\), the optimum exceeds \(B/16\), and at least one internal chord in the eight-vertex clique is indispensable. The theorem applies to completely unrestricted edgewise weights; symmetry of candidate weights is a conclusion, not an assumption.

## Assumptions and scope

Both input clique orders are integers, \(q\ge2\), \(p>2q\). The bridge links one distinguished hub of each clique. All existing edges can receive independent **nonnegative** real conductances, including zero; there are no edge-capacity or lower-positive-weight requirements. Edge costs are uniformly one; the exact budget \(B>0\) is used. The graph Laplacian is \(L(w)=\sum_{e=ij}w_e(e_i-e_j)(e_i-e_j)^\mathsf T\). Eigenvalues are listed in nondecreasing order with multiplicity. The claim concerns a continuous-time consensus/diffusion generator \(-L\), not a stochastic matrix with a second-largest-eigenvalue-modulus objective.

## Proof

**1. A four-level candidate and its exact spectral gap.** Let \(u\) be the hub of the \(p\)-clique and \(v\) the hub of the \(q\)-clique. Set \(\alpha=(2q-1)/(p-1)\), with \(0<\alpha<1\). Construct the real vector \(f\) by giving the \(p-1\) nonhub vertices of the first clique value \(-\alpha\), the hub \(u\) value zero, hub \(v\) value one, and the \(q-1\) remaining vertices value two. It is centered because \(-(p-1)\alpha+1+2(q-1)=0\).

Give every left spoke conductance \(\ell\), every right spoke conductance \(2\ell\), the bridge conductance \((2q-1)\ell\), and every nonhub chord conductance zero. The total cost is

\[
(p-1)\ell+2(q-1)\ell+(2q-1)\ell=D\ell=B.
\]

Direct evaluation gives \(Lf=\ell f\). At a left leaf the Laplacian value is \(-\alpha\ell\); at the left hub the contributions cancel because \((p-1)\alpha=2q-1\). At the right hub the incident-edge contributions are \((2q-1)\ell(1-0)+2(q-1)\ell(1-2)=\ell\); at a right leaf they equal \(2\ell(2-1)=2\ell\), as required.

To prove that \(\ell\) is the *smallest positive* eigenvalue, delete the row and column for hub \(u\). The grounded matrix splits into \(p-1\) singleton blocks of eigenvalue \(\ell\) and a \(q\)-vertex grounded weighted star. On the latter, the vector taking value one at \(v\) and two at each of its leaves is strictly positive and is an eigenvector of eigenvalue \(\ell\); irreducibility of this symmetric grounded \(M\)-matrix makes \(\ell\) its smallest eigenvalue. Hence the whole grounded matrix has smallest eigenvalue \(\ell\). Cauchy interlacing gives \(\lambda_2(L)\ge\ell\), while \(Lf=\ell f\) gives the reverse inequality. Thus \(\lambda_2(L)=\ell\). The positive quotient eigenvalue \(\ell\) is simple: its right grounded star vector is determined up to scale, and the hub equation uniquely fixes the left-leaf average. The left-leaf transverse eigenspace has eigenvalue \(\ell\) and dimension \(p-2\); right-leaf transverse modes have eigenvalue \(2\ell\).

**2. A universal semidefinite dual certificate.** Let \(P\) denote the orthogonal projector onto the sum-zero vector subspace supported on the \(p-1\) left nonhub vertices. Its rank is \(p-2\), each left-leaf diagonal is \((p-2)/(p-1)\), and the squared projected norm of a difference of two left leaves is two. Put

\[
\nu=\frac{(p-1)(1-\alpha^2)}{p-2}\ge0,
\qquad Z=ff^\mathsf T+\nu P.
\]

The matrix \(Z\) is positive semidefinite, has range orthogonal to constants, and satisfies

\[
\operatorname{tr} Z
=(p-1)\alpha^2+1+4(q-1)+\nu(p-2)=D.
\]

For any edge \(e=ij\), put \(g_e=(e_i-e_j)^\mathsf TZ(e_i-e_j)\). Each of the three mandatory edge classes (left spokes, right spokes and bridge) has \(g_e=1\); the right-clique nonhub chords have \(g_e=0\); and every left-clique nonhub chord has \(g_e=2\nu\). The inequality \(2\nu\le1\) is *equivalent* to

\[
p(p-1)\le2(2q-1)^2,
\]

i.e. to \(\Delta\le0\). Whenever this holds, arbitrary admissible conductances satisfy

\[
D\lambda_2(L(w))\le\operatorname{tr}(L(w)Z)
=\sum_e w_eg_e\le\sum_e w_e=B.
\]

This proves global optimality. Equality forces \(f\) to be an eigenvector of eigenvalue \(\ell\), since \(ff^\mathsf T\) is a positive component of \(Z\) and \(L-\ell(I-\mathbf1\mathbf1^\mathsf T/(p+q))\) is positive semidefinite. The leaf equations then force every left spoke to equal \(\ell\) and every right spoke to equal \(2\ell\), regardless of how the other edges are weighted, because chords connect vertices of equal \(f\)-value. The left hub equation forces the bridge weight \((2q-1)\ell\). These weights already exhaust the budget, so every chord has weight zero. This proves uniqueness **even at** \(\Delta=0\).

**3. Sharp necessity of larger-clique chords outside the certificate regime.** The same \(Z\) gives the bound \(\lambda_2(L(w))\le B/D\) whenever **all left nonhub chords are zero**, regardless of the size of \(\Delta\), because only their dual coefficients can exceed one. For \(\Delta>0\), we explicitly improve the tree allocation by turning on these chords. Set \(C=\binom{p-1}{2}\) and choose a real number \(k\) strictly between

\[
\frac{p-2}{2(1-\alpha^2)}<k<p-1.
\]

Such a \(k\) exists exactly when \(\Delta>0\). For small \(\varepsilon>0\), give *each* left nonhub chord weight \(\varepsilon\); change every left spoke from \(\ell\) to \(\ell-k\varepsilon\); change the bridge from \((2q-1)\ell\) to \((2q-1)\ell+[(p-1)k-C]\varepsilon\); leave all right spokes unchanged and all right nonhub chords zero. Every weight remains nonnegative for sufficiently small \(\varepsilon\), and the budget remains exactly \(B\).

The left-leaf transverse eigenvalue, initially \(\ell\), has derivative \(p-1-k>0\). The simple four-level quotient eigenvalue, initially \(\ell\), has by the Rayleigh eigenvalue-derivative formula a derivative with numerator

\[
(p-1)(1-\alpha^2)k-C>0,
\]

and positive denominator \(\lVert f\rVert^2\). All other positive eigenvalues were strictly above \(\ell\) at the tree allocation, so continuity ensures that **every** positive eigenvalue exceeds \(\ell\) for sufficiently small positive \(\varepsilon\). Hence the maximum over the full barbell is strictly larger than \(B/D\). Since every allocation with zero left nonhub chords has spectral gap at most \(B/D\), every global maximizer must use at least one such chord. Compactness of the closed budget simplex ensures maximizers exist.

## Verification

The bundled `verify.py` independently computes exact rational eigenvector identities, the budget identity, the dual certificate's trace and edge conditions, and strict feasible directional derivatives across finite families including both sides of the threshold. Its eight selected full-graph eigenvalue checks use symbolic exact arithmetic. The command `python verify.py` with SymPy installed prints `VERIFY_OK 699 exact rational certificate, edge, derivative and spectral checks`. The proof above, rather than finite enumeration, covers all integers and budgets in the stated domain.

## Relationship to prior work

Sun, Boyd, Diaconis, and Xiao (2006) introduced the semidefinite formulation of maximizing the weighted Laplacian spectral gap under an edge budget, together with exact examples and duality; the general framework is not new. Fiedler (1990) treated optimal weighted *trees*; the new result is not a claim of a new tree optimization method. The symmetric or moderately imbalanced sparse-support cases do not imply the more asymmetric regime treated here. The present theorem is restricted to **strictly imbalanced** clique orders and adds a nontrivial exact-value interval together with a proof that internal chords become indispensable beyond its sharp boundary. Ghosh, Boyd, and Saberi (2006) optimize *total effective resistance* of barbell networks, a different criterion with generally different edge utilization. Jafarizadeh and Jamalipour (2010) study discrete-time fastest-consensus eigenvalue modulus for barbell-related architectures; that problem differs from continuous-time algebraic-connectivity maximization. Balan and coauthors (2016) investigate other Laplacian conditioning objectives on weighted barbells.

## Limitations

The threshold distinguishes a region with fully explicit unique optimum from a region of strict improvement requiring large-clique chords; it does **not** calculate the optimal value or characterize every optimizer in the latter region. Unit costs, no edge caps, and complete cliques are essential to the formulation. Historical full-text coverage is incomplete: Fiedler's 1990 article and a 2024 paper on unweighted barbell connectivity were available only through abstracts or limited previews. Equivalent specialized analyses might exist and independent mathematical validation has not been performed.

## References

1. J. Sun, S. Boyd, P. Diaconis, and L. Xiao, “The fastest mixing Markov process on a graph and a connection to a maximum variance unfolding problem,” *SIAM Review* **48** (2006), 681–699. DOI: `10.1137/S0036144504443821`. Original author's PDF: `https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf` (electronically published 2006-11-02).
2. M. Fiedler, “Absolute algebraic connectivity of trees,” *Linear and Multilinear Algebra* **26** (1990), 85–106. DOI: `10.1080/03081089008817967`.
3. A. Ghosh, S. Boyd, and A. Saberi, “Minimizing effective resistance of a graph,” *MTNS* (2006), author PDF: `https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf`.
4. S. Jafarizadeh and A. Jamalipour, “Fastest distributed consensus problem on branches of an arbitrary connected sensor network,” arXiv:1004.5094 (2010), `https://arxiv.org/pdf/1004.5094`.
5. R. Balan, M. Begué, C. Clark, and K. Okoudjou, “Optimization methods for frame conditioning and application to graph Laplacian scaling,” arXiv:1609.02233 (2016), `https://arxiv.org/pdf/1609.02233`.
