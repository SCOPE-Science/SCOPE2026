# Exact signed-filter Lipschitz norms and finite-time heat contraction on two-subset Kneser graphs

## Finding

Let \(n\ge5\) be an integer, let \(G=KG(n,2)\) have the unit-edge shortest-path metric, and let \(A\) be its adjacency operator on real vertex functions modulo constants. For every \(\alpha,\beta\in\mathbb R\), the induced real Lipschitz operator norm is **exactly**
\[
\|\alpha I+\beta A\|_{\mathrm{Lip}\to\mathrm{Lip}}=
\begin{cases}
\max\{\,|\alpha|+3|\beta|,\ 4|\beta|\,\},&n=5,\\
|\alpha-\beta|+2(n-4)|\beta|,&n\ge6.
\end{cases}
\]
The adjacency algebra acts on functions modulo constants through operators of this form, so the formula determines the norm of **every real polynomial adjacency filter** on these Lipschitz spaces.

Write \(k=(n-2)(n-3)/2\) and let \(P_t=\exp[-t(kI-A)]\) be the rate-one, unnormalized-Laplacian heat semigroup. Its exact graph-distance Wasserstein-one contraction coefficient, equivalently its Lipschitz operator norm, is
\[
\mathcal C_n(t)=\sup_{x\ne y}\frac{W_1(P_t\delta_x,P_t\delta_y)}{d(x,y)}
=\begin{cases}
\dfrac{5e^{-2t}-2e^{-5t}}{3},&n=5,\\[5pt]
\dfrac{3(n-4)e^{-(k-1)t}-2(n-5)e^{-(k+n-3)t}}{n-2},&n\ge6.
\end{cases}
\]
For \(t>0\), \(0<\mathcal C_n(t)<1\), and its instantaneous logarithmic decay rate \(-\frac{d}{dt}\log \mathcal C_n(t)\) increases strictly from its value at zero to \(k-1\). Accordingly, for \(s,t>0\),
\[\mathcal C_n(s+t)<\mathcal C_n(s)\mathcal C_n(t).\]
For the exceptional Petersen graph \(KG(5,2)\), the initial decay rate is zero, but \(\mathcal C_5(t)=1-5t^2+O(t^3)\), so heat flow is strictly contractive at every positive time despite its vanishing infinitesimal Wasserstein curvature.

## Assumptions and scope

A vertex of \(KG(n,2)\) is a two-element subset of \(\{1,\ldots,n\}\); two vertices are adjacent if the subsets are disjoint. For every \(n\ge5\), this graph is connected of diameter two, with degree \(k\). For a real vertex function \(f\), set
\[\operatorname{Lip}(f)=\max_{x\sim y}|f(x)-f(y)|.\]
This becomes a norm on the space of functions modulo constants. The norm \(\|T\|_{\mathrm{Lip}\to\mathrm{Lip}}\) is the supremum of \(\operatorname{Lip}(Tf)\) over \(\operatorname{Lip}(f)\le1\); constant-preserving operators such as \(\alpha I+\beta A\) descend to the quotient. The measures in the Wasserstein formula are probability distributions on graph vertices, and \(W_1\) uses this unit-edge graph distance. No restrictions on the signs of \(\alpha\) and \(\beta\) are made.

## Proof

**1. A universal edge reduction.** Relabeling the ground set acts transitively on graph edges and commutes with \(A\). Thus the operator norm of \(T=\alpha I+\beta A\) is the largest possible value of \(|(Tf)(u)-(Tf)(v)|\) for one fixed edge \(u=\{1,2\}\), \(v=\{3,4\}\), over all \(\operatorname{Lip}(f)\le1\). Put \(R=\{5,\ldots,n\}\), \(U=\{\{i,j\}:i\in\{1,2\},j\in R\}\) and \(V=\{\{i,j\}:i\in\{3,4\},j\in R\}\). The neighbor rows cancel except for \(u,v,U,V\), leaving the **exact identity**
\[
(Tf)(u)-(Tf)(v)=(\alpha-\beta)(f(u)-f(v))
+\beta\biggl(\sum_{w\in V}f(w)-\sum_{w\in U}f(w)\biggr).
\tag{1}
\]
All vertices appearing in the signed measure underlying (1) are distinct.

**2. A matching determines the norm for \(n\ge6\).** The right side of (1) is bounded in absolute value by \(|\alpha-\beta|+2(n-4)|\beta|\), because \(u\sim v\) and the two sums can be paired at distance one: choose a fixed-point-free permutation \(\sigma\) of \(R\) and match \(\{i,j\}\in U\) with \(\{i+2,\sigma(j)\}\in V\). Each matched pair is disjoint and hence adjacent. This upper bound is sharp. Give value \(+1/2\) to every vertex supporting a positive coefficient in (1), value \(-1/2\) to every vertex supporting a negative coefficient, and zero to all other vertices. As the assigned values lie in an interval of length one, the resulting function is automatically \(1\)-Lipschitz; its value in (1) is the full sum of absolute coefficients. This proves the second branch simultaneously for all real \(\alpha,\beta\).

**3. The Petersen exception \(n=5\).** Here each of \(U,V\) has two vertices, but every pair \(w\in U\), \(w'\in V\) shares the sole external ground-set element and is at graph distance two. Averaging any test function over the swaps \(1\leftrightarrow2\) and \(3\leftrightarrow4\) retains expression (1), does not increase its Lipschitz seminorm, and gives common function values \(p\) on \(U\), \(q\) on \(V\). Write \(x=f(u)-f(v)\) and \(z=q-p\). The graph metric implies
\[|x|\le1,\qquad |z|\le2,\qquad |z-x|\le2.\]
The final inequality follows because each vertex in \(V\) is adjacent to \(u\), and each vertex in \(U\) is adjacent to \(v\). With \(y=2z-x\), these inequalities imply \(|y|\le4-|x|\), and (1) becomes \(\alpha x+\beta y\). Consequently,
\[
|(Tf)(u)-(Tf)(v)|\le
\max_{|x|\le1} \bigl(|\alpha|\,|x|+|\beta|(4-|x|)\bigr)
=\max\{4|\beta|,|\alpha|+3|\beta|\}.
\]
Both bounds are attained: prescriptions \((f(u),f(v),p,q)=(0,0,-1,1)\), \((0,-1,-1,1)\), and \((0,-1,0,-1)\), together with their negatives, realize all six vertices \((x,y)=(0,\pm4),(\pm1,\pm3)\). Every prescription obeys all graph-distance Lipschitz inequalities on the six supporting vertices; the McShane extension produces a \(1\)-Lipschitz function on the entire graph. This proves the first branch.

**4. All spectral filters and heat flow.** Counting common neighbors gives the matrix identity
\[
A^2=(n-3)I-(n-4)A+\binom{n-3}{2}J,
\tag{2}
\]
where \(J\) is the all-ones matrix. Since \(J\) vanishes on functions modulo constants, (2) shows that every polynomial in \(A\) induces an affine expression in \(A\). On nonconstant functions the two adjacency eigenvalues are \(1\) and \(-(n-3)\). Put
\[a=e^{-(k-1)t},\qquad b=e^{-(k+n-3)t}.\]
The heat operator modulo constants is \(\alpha_t I+\beta_t A\), where
\[
\alpha_t=\frac{(n-3)a+b}{n-2},\qquad \beta_t=\frac{a-b}{n-2}.\]
For \(t\ge0\), \(a\ge b>0\), so substitution into the signed-filter norm formula yields the asserted exact \(\mathcal C_n(t)\). Kantorovich–Rubinstein duality and transitivity on edges identify the Lipschitz norm with the maximum \(W_1\) contraction over pairs of Dirac measures; the triangle inequality along graph geodesics reduces the supremum over all pairs to edges. The operator norm also controls all pairs of probability measures by linear duality.

Finally write \(\mathcal C_n(t)=e^{-\lambda t}(C-De^{-\Delta t})\), with \(\lambda=k-1\), \(\Delta=n-2\), and
\[
(C,D)=\begin{cases}(5/3,2/3),&n=5,\\
(3(n-4)/(n-2),\ 2(n-5)/(n-2)),&n\ge6.
\end{cases}
\]
For every \(n\ge5\), \(C>D>0\) and \(C-D=1\). Therefore the logarithmic rate is
\[
h(t)=\lambda-\frac{D\Delta e^{-\Delta t}}{C-De^{-\Delta t}},\qquad
h'(t)=\frac{CD\Delta^2 e^{-\Delta t}}{(C-De^{-\Delta t})^2}>0.
\]
Direct substitution gives \(h(0)=0\) for \(n=5\), and \(h(0)=(n^2-9n+24)/2>0\) for \(n\ge6\). Thus \(h(t)>0\) for all \(t>0\). Strict monotonicity yields strict submultiplicativity by integrating \(h(t+s)>h(t)\). The Petersen Taylor coefficient follows directly from its exact formula. This completes the proof.

## Verification

The included `verify_kneser_exact.py` uses Python standard-library exact integer and rational arithmetic. Its executed checks covered 123188 adjacency-matrix entries, 767 signed-filter matching/potential certificates, and 225 rational spectral-heat identities for graph orders 5 through 19. The included `check_kneser_lp.py` independently solves finite Kantorovich dual linear programs using NumPy and SciPy for graph orders 5 through 9 and compares 75 signed-filter/heat cases, including matrix-exponential heat evolution. Both completed without an assertion failure. The infinite statements follow from the explicit argument above, not from these finite tests.

## Relationship to prior work

Münch and Wojciechowski (arXiv:1712.00875, initial version December 4, 2017) relate graph Ollivier curvature to heat-semigroup Lipschitz decay, giving a conceptual reason to study these norms. Cushing and collaborators (arXiv:1807.02384, initial version July 6, 2018) study sharp graph-curvature bounds and include Petersen spectral/curvature information. Bonini and collaborators (arXiv:1907.06733, initial version July 15, 2019) give curvature formulas for strongly regular graphs, including zero infinitesimal curvature of the Petersen graph. These infinitesimal and general estimates do not state the complete two-parameter signed-filter norm or the exact finite-time Kneser heat coefficient derived here. The special Petersen curvature-zero fact is prior work, not claimed new.

## Limitations

The exact formulas require two-subset Kneser graphs with \(n\ge5\), real-valued functions, unit-edge graph metric and the unnormalized rate-one generator. They do not assert a formula for general \(KG(n,r)\), weighted Kneser graphs, arbitrary functions of the Laplacian on different graphs, or Wasserstein exponents other than one. The same mathematical model proof and finite computation have not received independent mathematical audit. A historically equivalent formula under alternative spectral or transportation terminology may exist.

## References

1. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875v1 (December 4, 2017), https://arxiv.org/abs/1712.00875.
2. D. Cushing, S. Kamtue, J. Koolen, S. Liu, F. Münch and N. Peyerimhoff, *Rigidity of the Bonnet-Myers inequality for graphs with respect to Ollivier Ricci curvature*, arXiv:1807.02384v1 (July 6, 2018), https://arxiv.org/abs/1807.02384.
3. V. Bonini, C. Carroll, U. Dinh, S. Dye, J. Frederick and E. Pearse, *Condensed Ricci Curvature of Complete and Strongly Regular Graphs*, arXiv:1907.06733v1 (July 15, 2019), https://arxiv.org/abs/1907.06733.
