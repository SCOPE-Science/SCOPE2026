# Quadratic Walsh uniqueness on the spanning-tree slice of a complete graph

## Finding

For every integer \(n\ge 3\), let \(E=E(K_n)\), \(m=\binom n2\), and \(\mathcal T_n\) be the labelled spanning trees of \(K_n\). For an edge \(e\in E\), put \(x_e(T)=\mathbf 1_{\{e\in T\}}\) and \(\chi_e(T)=1-2x_e(T)\). Let the degree-at-most-two coordinate Walsh system be
\[
\mathscr W_{\le2}=\{1\}\cup\{\chi_e:e\in E\}\cup\{\chi_e\chi_f:\{e,f\}\in\tbinom E2\}.
\]
Its evaluation matrix on \(\mathcal T_n\) has rank exactly \(\binom m2\) and nullity exactly \(m+1\). All relations are generated, in the squarefree polynomial space of degree at most two, by the \(m+1\) independent identities
\[
R_0=\sum_{e\in E}x_e-(n-1)=0,\qquad
R_e=x_e\!\left(\sum_{f\in E}x_f-(n-1)\right)
=\sum_{f\ne e}x_ex_f-(n-2)x_e=0\quad(e\in E).
\]
Equivalently, the \(\binom m2\) two-edge inclusion functions \(T\mapsto x_e(T)x_f(T)\), indexed by unordered distinct pairs \(\{e,f\}\), are linearly independent over \(\mathbb C\). This also gives the exact rank and nullspace of the probability-normalized Gram matrix for **any** probability law assigning positive mass to every labelled spanning tree.

## Assumptions and scope

Edges are unordered pairs of distinct vertices in \([n]\), and trees are all simple spanning trees with those labelled vertices. All vector spaces and ranks in the theorem are over \(\mathbb C\) (the same statements hold over \(\mathbb R\)). No edge weights or independence assumptions are imposed on the probability measure, except full support when a Gram matrix is mentioned. Products of coordinate functions use the Boolean identity \(x_e^2=x_e\) when reduced to multilinear form. For \(n=3\), the full assertion includes the three possible trees and is not an asymptotic convention.

## Proof

**Step 1: a linear uniqueness lemma.** On spanning trees of \(K_s\), for every \(s\ge3\), if \(\sum_e a_ex_e(T)=0\) for all trees \(T\), then every coefficient \(a_e=0\). Indeed, for any two distinct edges \(e,f\), choose a cut crossed by both (isolate their common endpoint if they meet; otherwise put one endpoint of each on each side). Choose a spanning tree on each side of the cut, forming a two-component spanning forest \(F\). Both \(F\cup\{e\}\) and \(F\cup\{f\}\) are spanning trees, so subtraction shows \(a_e=a_f\). Thus all coefficients equal a common \(a\); evaluating any tree gives \((s-1)a=0\), hence \(a=0\).

**Step 2: pair uniqueness by induction.** The assertion for \(n=3\) holds because each of its three spanning trees has a different two-edge set; the three pair-inclusion functions form the identity evaluation matrix after reordering. Let \(n\ge4\) and assume pair uniqueness for \(K_{n-1}\). Suppose
\[
P(T)=\sum_{\{e,f\}\in\binom E2}w_{ef}x_e(T)x_f(T)=0
\]
for every spanning tree \(T\) of \(K_n\), with \(w_{ef}=w_{fe}\). Reserve vertex \(n\). Write \(E_0=E(K_{n-1})\), and let \(a_i=\{i,n\}\) be the star edge to old vertex \(i\).

Fix any spanning tree \(T'\) on the old vertices. For any \(i,j\), the two trees \(T'\cup\{a_i\}\) and \(T'\cup\{a_j\}\) both have one edge incident to vertex \(n\). Subtracting their zero polynomial evaluations gives
\[
\sum_{e\in T'}(w_{e,a_i}-w_{e,a_j})=0.
\]
The linear uniqueness lemma on \(K_{n-1}\) implies \(w_{e,a_i}=w_{e,a_j}\) for every \(e\in E_0\). Denote this common value by \(t_e\).

Since an old spanning tree has exactly \(n-2\) edges, its linear term is expressible in pair monomials:
\[
\sum_{e\in T'}t_e
=\frac1{n-3}\sum_{\{e,f\}\in\binom{T'}2}(t_e+t_f).
\]
Evaluating \(P(T'\cup\{a_i\})=0\) and invoking the pair-induction hypothesis yields
\[
w_{ef}=-\frac{t_e+t_f}{n-3}
\qquad\text{for all distinct }e,f\in E_0.
\tag{1}
\]

Now evaluate at the full star \(\{a_i:1\le i\le n-1\}\) to obtain
\[
W:=\sum_{1\le i<j\le n-1}w_{a_i,a_j}=0.
\tag{2}
\]
Let \(s_j=\sum_{i\ne j}w_{a_i,a_j}\). For each old edge \(e=\{i,j\}\), consider the tree comprising every star edge except \(a_j\), plus \(e\). Its evaluation, using \(W=0\), is
\[
0=W-s_j+(n-2)t_{\{i,j\}},\qquad
(n-2)t_{\{i,j\}}=s_j.
\tag{3}
\]
For each \(j\), this holds for every \(i\ne j\), while \(t_{\{i,j\}}=t_{\{j,i\}}\). Therefore every \(s_j\) has one common value and every \(t_e\) has one common value \(t\). Summing \(s_j\) and using (2) gives \((n-1)(n-2)t=2W=0\). Consequently, \(t_e=0\) for all old edges, all \(s_j=0\), and (1) gives \(w_{ef}=0\) when both edges are old. The previously established mixed coefficients \(w_{e,a_i}=t_e\) also vanish.

It remains to show \(w_{a_j,a_k}=0\) for two distinct star edges. Join \(n\) to each old vertex except \(j,k\), and attach both excluded vertices to any one included old vertex using two old edges. This is a tree for every \(n\ge4\); all pair coefficients containing an old edge have already vanished. Hence
\[
0=\sum_{\substack{1\le i<\ell\le n-1\\i,\ell\notin\{j,k\}}}w_{a_i,a_\ell}
=W-s_j-s_k+w_{a_j,a_k}=w_{a_j,a_k}.
\]
Every coefficient of \(P\) is zero, completing the induction.

**Step 3: complete relation space and Gram matrices.** On any spanning tree \(T\), exactly \(n-1\) edges are present. Consequently
\[
x_e(T)=\frac1{n-2}\sum_{f\ne e}x_e(T)x_f(T),
\qquad
1=\frac{2}{(n-1)(n-2)}\sum_{e<f}x_e(T)x_f(T).
\]
Thus degree-at-most-two coordinate monomials span exactly the pair-inclusion functions, which were proved independent. The identity \(\chi_e=1-2x_e\) gives a triangular invertible change of basis between degree-at-most-two monomial coefficients and Walsh coefficients. The rank therefore equals \(\binom m2\), and the nullity is \(1+m+\binom m2-\binom m2=m+1\).

The displayed \(R_0,R_e\) all vanish because \(\sum_e x_e=n-1\) on trees. They are coefficientwise independent as multilinear polynomials: \(R_0\) is the only one with nonzero constant term, and, after its coefficient is zero, the linear term of \(R_e\) is \(-(n-2)x_e\), so the \(m\) remaining coefficients are zero. They therefore form a basis of the entire relation space. For a strictly positive measure \(\mu\) on \(\mathcal T_n\), the Gram matrix is \(A^*\operatorname{diag}(\mu(T))A\) and has exactly the same kernel and rank as the evaluation matrix \(A\). This completes the proof.

## Verification

The standalone `VERIFY.py` enumerates labelled trees by Prüfer sequences, builds the pair-inclusion matrix, and performs modular row reduction over the prime field with \(1{,}000{,}003\) elements. It returns full column rank for \(n=3,4,5,6\), with respectively \(3,16,125,1296\) trees and \(3,15,45,105\) independent pair columns. Modular full column rank implies rational full column rank in each tested case, but finite tests are **not** the proof of the infinite theorem. The induction above establishes the theorem for every integer \(n\ge3\). Reproduction: run `python3 VERIFY.py` in a directory containing the standalone file; only the Python standard library is used.

## Relationship to prior work

Burton and Pemantle (arXiv:math/0404048, initial arXiv posting 2004-04-02; original journal work 1993) derived the transfer-current determinant for joint edge-inclusion probabilities of uniform spanning trees. That identity can calculate entries of any finite Gram matrix after expanding character products; it does not itself assert this all-size rank and precise relation-space theorem. Kassel and Wu (arXiv:1312.2946) develop spanning-tree edge correlations and pattern fields, including covariance constraints related to the fixed total edge count. Filmus (arXiv:1406.0142) supplies orthogonal Fourier analysis on the **entire** fixed-weight Boolean slice. The spanning-tree set is a proper structured subset of that slice; a basis for the full slice does not establish injectivity after restriction to spanning trees. The present argument supplies the missing exact rank and all quadratic dependencies for that restricted family.

## Limitations

This is a rank/nullspace theorem, not an explicit formula for every nonzero Gram eigenvalue or a quantitative conditioning bound. It applies only to labelled spanning trees of complete simple graphs and coordinate degree at most two; higher degrees face immediate forbidden-cycle monomials, and arbitrary host graphs can have extra degree-two restrictions. The result has undergone only self-review, not independent mathematical audit or validation. A broader historical theorem about matroid-basis inclusion matrices might imply this special case; that possibility was not eliminated by the bounded literature review.

## References

1. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, arXiv:math/0404048 (posted 2004-04-02); Annals of Probability **21** (1993), 1329–1371.
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (posted 2013-12-10).
3. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (initial posting 2014-06-01).
