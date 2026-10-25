# A sharp part-size-eight transition for fastest mixing after one bipartite edge failure

## Finding
Let \(G_n\) be the graph obtained from the complete bipartite graph \(K_{n,n}\) by deleting one edge, with \(n\ge3\). Among all symmetric, entrywise nonnegative row-stochastic matrices \(P\) whose off-diagonal support is contained in \(G_n\), let \(\mu_n\) be the minimum second-largest eigenvalue modulus (SLEM). Then
\[
\mu_n=\begin{cases}
 n^{-1/2},&3\le n\le7,\\[3pt]
 \dfrac{n-2}{2}\,\dfrac{2}{2(n-1)+\sqrt{n^2-8n+8}},&n\ge8.
\end{cases}
\]
There is an optimal chain whose probability on each edge incident to one of the two defective vertices is \(x_n\), and on every remaining cross-part edge is \(y_n\), where
\[
(x_n,y_n)=\begin{cases}
\bigl(n^{-1},[2(n-1)]^{-1}\bigr),&3\le n\le7,\\[3pt]
\left(\dfrac{2}{2(n-1)+\sqrt{n^2-8n+8}},\dfrac{2-nx_n}{2(n-1)}\right),&n\ge8.
\end{cases}
\]
The diagonal entries are determined by row sums. Thus the optimal value has a structural transition between \(n=7\) and \(n=8\). Compared with the exact \(1/3\) optimum of the intact balanced biclique, the one-edge-failure penalty is positive for every finite \(n\ge3\), and
\[
\mu_n-\frac13=\frac{4}{9n^2}+O(n^{-3})\quad(n\longrightarrow\infty).
\]

## Assumptions and scope
The graph is simple, unweighted, undirected, and has two parts of exactly \(n\) vertices each, with just one absent cross-part edge. The transition probabilities themselves are free optimization variables: symmetry, nonnegativity, and stochastic row sums are required; transitions on missing off-diagonal edges are forbidden; holding probabilities on diagonal entries are allowed. No reversibility beyond symmetry is assumed, and no lower bounds on allowed-edge transition probabilities are imposed. The result concerns exact SLEM optimization, not total-variation mixing time at a prescribed finite horizon or nonsymmetric chains. The source motivating the setup has its publicly dated arXiv version on 2007-09-06 (arXiv:0709.0955); the present result is classified under MSC2020 90C22 (semidefinite/eigenvalue optimization).

## Proof
**Symmetry reduction.** Convexity of \(\|P-J/(2n)\|_2\), where \(J\) is the all-ones matrix, and averaging over automorphisms of \(G_n\) ensure an optimal automorphism-invariant \(P\). There are exactly two off-diagonal edge orbits: \(2(n-1)\) edges incident to one of the endpoints of the missing edge and \((n-1)^2\) other edges. Give them probabilities \(x\) and \(y\), respectively. Feasibility is precisely
\[
x\ge0,\quad y\ge0,\quad (n-1)x\le1,\quad x+(n-1)y\le1.
\]
The defective endpoints each have holding probability \(1-(n-1)x\); every ordinary vertex has holding probability \(d=1-x-(n-1)y\).

**Exact spectrum.** Decompose into constant vectors on the four vertex classes (the two defective singletons and two ordinary groups), and zero-sum vectors within each ordinary group. Interchanging the two original bipartite parts further splits the four-dimensional component into symmetric and antisymmetric blocks. The eigenvalues other than the Perron eigenvalue \(1\) are: \(1-nx\); the two eigenvalues of
\[
M(x,y)=\begin{pmatrix}
1-(n-1)x&-\sqrt{n-1}\,x\\
-\sqrt{n-1}\,x&1-x-2(n-1)y
\end{pmatrix};
\]
and \(d=1-x-(n-1)y\), with multiplicity \(2n-4\). Therefore
\[
\mu(x,y)=\max\{\,|1-nx|,\ \|M(x,y)\|_2,\ |d|\,\}.
\]
Write \(A=1-(n-1)x\) and \(g(x)=\sqrt{A^2+(n-1)x^2}\). Applying \(M\) to its first coordinate unit vector gives the universal lower bound \(\|M(x,y)\|_2\ge g(x)\). Direct completion of the square yields \(g(x)^2=n(n-1)(x-1/n)^2+1/n\), with equality at \(x=1/n\). Choosing
\[
y=y_0(x)=\frac{2-nx}{2(n-1)}\]
makes \(\operatorname{tr}M=0\), gives its eigenvalues \(\pm g(x)\), and gives \(d=(n-2)x/2\).

**The first branch.** For \(3\le n\le7\), the universal lower bound \(g(x)\ge1/\sqrt n\) is attained by \(x=1/n\) and \(y=y_0(x)\). Indeed, \(|1-nx|=0\), \(\|M\|_2=1/\sqrt n\), and \(d=(n-2)/(2n)\le1/\sqrt n\), the last inequality being equivalent to \((n-2)^2\le4n\).

**The second branch: construction.** For \(n\ge8\), define \(x_*\) as the smaller positive root of
\[
F_n(x)=1-2(n-1)x+\frac{3n^2-4}{4}x^2=0.
\]
Its rationalized expression is \(x_*=2/[2(n-1)+\sqrt{n^2-8n+8}]\). Since
\[
F_n\!\left(\frac{2}{3n-2}\right)=\frac{8(n-1)}{(3n-2)^2}>0,
\qquad F_n(1/n)=\frac{-n^2+8n-4}{4n^2}<0,
\]
and the root obtained by rationalization is the first positive root, one has \(2/(3n-2)<x_*<1/n\). Set \(y_*=y_0(x_*)\) and \(r_*=(n-2)x_*/2\). These are feasible, and the root equation gives \(g(x_*)=r_*\). Moreover, \(0<1-nx_*\le r_*\), so \(\mu(x_*,y_*)=r_*\).

**The second branch: global optimality.** The function \(\mu(x,y)=\|P(x,y)-J/(2n)\|_2\) is convex in its two variables. At the constructed point, the three convex functions \(f_+=\lambda_{\max}(M)\), \(f_-=-\lambda_{\min}(M)\), and \(f_d=d\) are all active and equal \(r_*\); their differentiable gradients supply a zero subgradient of \(\mu\). Here is an explicit nonnegative certificate. Put \(A_*=1-(n-1)x_*\), \(r=r_*\), and
\[
K=\frac{2(n-1)(1-nx_*)}{(n-2)r},\quad
s=\frac1{1+K},\quad t=s\left(K-\frac{A_*}{r}\right),\quad
\alpha=\frac{s-t}{2},\quad\beta=\frac{s+t}{2},\quad\gamma=Ks.
\]
One has \(\alpha+\beta+\gamma=1\). Since \(0<A_*/r\le1\) and \(x_*\ge2/(3n-2)\), one has \(-1\le K-A_*/r\le1\) and hence \(\alpha,\beta,\gamma\ge0\). Define
\[
u=\frac{-(n-2)A_*/2+(n-1)x_*}{r},\qquad v=\frac{(n-1)A_*}{r}.
\]
Differentiating the simple eigenvalues of \(M\) at the point where \(\operatorname{tr}M=0\) gives
\[
\nabla f_+=(-n/2+u,-(n-1)+v),\quad
\nabla f_-=(n/2+u,(n-1)+v),\quad
\nabla f_d=(-1,-(n-1)).
\]
Substitution of the displayed weights gives exactly
\[
\alpha\nabla f_++\beta\nabla f_-+\gamma\nabla f_d=(0,0).
\]
Thus a convex combination of supporting gradients of the globally convex objective is zero. This certifies global minimum at \((x_*,y_*)\), without numerical optimization or a limiting argument.

**Intact-biclique comparison.** On the intact \(K_{n,n}\), automorphism invariance makes all cross-part probabilities equal to some \(p\). The nontrivial eigenvalues are \(1-np\) and \(1-2np\). Their maximum absolute value has minimum \(1/3\), attained at \(p=2/(3n)\). For \(n\ge8\), the strict penalty follows directly from \(\sqrt{n^2-8n+8}<n-4\), which forces \(x_*>2/[3(n-2)]\) and hence \(r_*>1/3\); the smaller sizes are immediate. Direct Taylor expansion in \(1/n\) of the rationalized root yields \(\mu_n=1/3+4/(9n^2)+O(n^{-3})\).

## Verification
The accompanying standalone Python program `verify_fmmc.py` checks feasibility, the exact reduced-spectrum identities, the nonnegative convex-gradient certificate for integers \(8\le n\le500\), and a deterministic finite grid comparison for several small values of \(n\). It is supplementary, not a replacement for the all-\(n\) analytic argument. For example, it yields \(\mu_7\approx0.377964473009\), \(\mu_8\approx0.356539559849\), and \(\mu_{20}\approx0.334896084060\). Run from the package directory with `python3 verify_fmmc.py` using only the Python standard library.

## Relationship to prior work
Boyd, Diaconis, and Xiao (2004) formulated symmetric fastest mixing as a convex spectral-norm/SDP problem and determined the intact complete-bipartite case. Boyd, Diaconis, Parrilo, and Xiao (arXiv:0709.0955, 2007; SIAM Journal on Optimization 2009), especially sections 5.4.2 and 5.4.4 of the published full text (sections 5.3.2 and 5.3.4 in the arXiv version), gave symmetry-block methods and exact results for the intact biclique and for two cliques joined by a bridge. The latter graph is the complement of \(G_n\), but complementing admissible off-diagonal support does not transfer an optimal Markov transition matrix or its eigenvalue objective. Those formulas therefore do not imply the sharp \(n=8\) edge-failure transition here. General SDP methods can compute individual instances; the assertion here is the uniform analytic optimum and phase boundary under removal of one permitted cross-part edge.

## Limitations
This is not a classification of every optimum without automorphism averaging, and does not address multiple deleted edges, directed/nonreversible chains, prescribed nonuniform stationary measures, or finite-time mixing profiles. The novelty search cannot exclude unindexed exact solutions for this special defective biclique. The derivation has been checked by its authoring review process only; no independent audit or independent experimental validation is asserted. Numerical checks are finite and do not establish the all-\(n\) proof by themselves.

## References
1. S. Boyd, P. Diaconis, and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46 (2004), 667–689, DOI: 10.1137/S0036144503423264. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” arXiv:0709.0955v1, first posted 2007-09-06; *SIAM Journal on Optimization* 20 (2009), 792–819, DOI: 10.1137/070689413. Full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
