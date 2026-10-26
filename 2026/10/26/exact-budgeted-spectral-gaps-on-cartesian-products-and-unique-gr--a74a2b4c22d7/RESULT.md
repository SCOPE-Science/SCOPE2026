# Exact budgeted spectral gaps on Cartesian products and unique grid conductances

## Finding

Fix an integer \(d\ge 1\). Let \(H_1,\ldots,H_d\) be connected simple undirected graphs, each with \(n_i\ge2\) vertices, and put \(N=\prod_i n_i\). An independent nonnegative conductance \(w_e\) is permitted on **every** edge of the Cartesian product \(G=H_1\square\cdots\square H_d\), subject only to \(\sum_e w_e=B>0\). All eigenvalues are those of the combinatorial weighted Laplacian \(L(w)\), so the objective is \(\lambda_2(L(w))\), the exponential consensus-rate spectral gap.

For each factor define its exact unit-budget optimum
\[
\alpha_i=\max_{u_e\ge0,\;\sum_{e\in E(H_i)}u_e=1}\lambda_2(L_{H_i}(u))>0.
\]
Then, even allowing conductances to vary arbitrarily between different fibers, the **unrestricted** product optimum is
\[
\boxed{\max_{w\ge0,\;\sum w_e=B}\lambda_2(L_G(w))=\frac{B}{\displaystyle\sum_{i=1}^d\frac{N/n_i}{\alpha_i}}.}
\]
An optimizer repeats a unit-budget optimum on every fiber of factor \(i\), scaled to give that factor the same spectral gap as every other factor. Uniqueness is **not** asserted for arbitrary connected factors.

For the rectangular grid \(G=P_{n_1}\square\cdots\square P_{n_d}\), there is a stronger complete classification. Its unique global optimizer, among all nonnegative and possibly fiber-asymmetric conductances, has
\[
\boxed{\lambda_*=\frac{12B}{N\sum_{i=1}^d(n_i^2-1)},\qquad
w^*_{i,k}=\frac{\lambda_*}{2}\,k(n_i-k)\quad(1\le k<n_i).}
\]
Here \(w^*_{i,k}\) is the rate of every grid edge whose \(i\)-th coordinate increases from \(k\) to \(k+1\); it is independent of all other coordinates. Every optimal edge rate is strictly positive. The entire optimized spectrum (with multiplicities) is
\[
\boxed{\left\{\frac{\lambda_*}{2}\sum_{i=1}^d r_i(r_i+1):\ 0\le r_i<n_i\right\}.}
\]
In particular the optimal Fiedler eigenspace has dimension exactly \(d\).

For cubic grids with each side length \(n\), the optimal gap divided by the gap at uniform conductance under the same total budget is exactly
\[
\frac{6}{n(n+1)(1-\cos(\pi/n))}\longrightarrow\frac{12}{\pi^2}\qquad(n\to\infty),
\]
independently of the dimension \(d\). Thus the limiting improvement is about \(21.6\%\), rather than a gain from merely tuning a small family of directionwise constant multipliers.

## Assumptions and scope

The graphs are finite, connected, simple, undirected, have at least two vertices each, and all rates are nonnegative with exactly the stated total **edge-conductance** budget. Each unoriented edge is counted once. The Laplacian has diagonal entries equal to the weighted degrees and negative off-diagonals equal to edge rates. No normalized-Laplacian or discrete-time transition-matrix convention is being used. For grids the vertices have integer coordinates \(1\le k_i\le n_i\); all numbers of dimensions and side lengths stated above are quantified.

## Proof

**General tensorization: upper bound.** For factor \(i\), let \(m_i=N/n_i\) denote the number of its parallel fibers. Let \(B_i\) be the total rates of all edges parallel to factor \(i\), and let \(\bar w^{(i)}_e=m_i^{-1}\sum_f w_{e,f}\) average the rate of each factor edge over those fibers. This averaged factor design has budget \(B_i/m_i\). Extend any centered factor vector constantly across all other coordinates. Its Rayleigh quotient for the product Laplacian equals its Rayleigh quotient for \(L_{H_i}(\bar w^{(i)})\): both numerator and denominator acquire the same factor \(m_i\) on the product. Hence, for every \(i\),
\[
\lambda_2(L_G(w))\le\lambda_2(L_{H_i}(\bar w^{(i)}))\le\alpha_i\frac{B_i}{m_i}.
\]
Because \(B=\sum_i B_i\), summing the implications \(B_i\ge m_i\lambda_2/\alpha_i\) proves the asserted upper bound. This step does **not** assume any symmetry, separability or identical fiber rates of the competitor.

**General tensorization: attainment.** By compactness choose a maximizing unit-budget factor design \(u^{(i)}\) for each \(i\). Put \(\ell=B/(\sum_i m_i/\alpha_i)\), and on every \(i\)-fiber use \(w_{e,f}=\ell u^{(i)}_e/\alpha_i\). Its budget is \(\sum_i m_i\ell/\alpha_i=B\). Its Laplacian is a Kronecker sum, and every summand has gap exactly \(\ell\). The nonzero spectrum of a Kronecker sum consists of sums of nonnegative factor eigenvalues, so its smallest positive eigenvalue is \(\ell\). This attains the bound.

**Optimal paths and grid construction.** On a path with vertices \(1,\ldots,n\), give its \(k\)-th edge conductance \(\ell k(n-k)/2\). Write \(w_0=w_n=0\). For the centered linear function \(f(k)=k-(n+1)/2\), direct subtraction gives
\[
(Lf)(k)=w_{k-1}-w_k=\ell\left(k-\frac{n+1}{2}\right)=\ell f(k).
\]
The operator sends polynomials of degree at most \(r\) into polynomials of degree at most \(r\), and its action on the highest coefficient of a degree-\(r\) polynomial is multiplication by \(\ell r(r+1)/2\). The polynomial evaluation spaces of degrees \(0,1,\ldots,n-1\) form a complete flag of dimensions \(1,2,\ldots,n\); therefore its **entire** spectrum is \(\{\ell r(r+1)/2:0\le r<n\}\). In particular the gap is \(\ell\), not merely an eigenvalue observed in the linear mode.

Summing \(k(n-k)\) over \(1\le k<n\) gives \(n(n^2-1)/6\). Thus, for the proposed grid rates, the total budget is
\[
B=\frac{\ell}{2}\sum_i\frac{N}{n_i}\sum_{k=1}^{n_i-1}k(n_i-k)
=\frac{\ell N}{12}\sum_i(n_i^2-1),
\]
which yields \(\ell=\lambda_*\). The Kronecker sum and the path eigenvalues give the complete displayed grid spectrum and Fiedler multiplicity \(d\).

**Unrestricted grid upper bound and uniqueness.** For each coordinate \(i\), use the centered test vector \(f_i(k_1,\ldots,k_d)=k_i-(n_i+1)/2\). It has squared norm \(\|f_i\|^2=N(n_i^2-1)/12=:D_i\). Only \(i\)-parallel edges contribute to its Laplacian quadratic form, each with squared difference one, so \(f_i^{\mathsf T}Lf_i=B_i\). Consequently \(\lambda_2(L)\le B_i/D_i\) for all \(i\), yielding \(B\ge\lambda_2\sum_iD_i\) without assuming separable rates. The displayed construction attains equality.

Now suppose **any** admissible design attains \(\lambda_*\). Each inequality \(B_i\ge\lambda_*D_i\) must then be equality. The Rayleigh quotient of \(f_i\) is the smallest possible on the orthogonal complement of constants; equality implies \(Lf_i=\lambda_* f_i\), even when the eigenspace is repeated. At every vertex, this eigen-equation reads
\[
w_{i,k-1,\mathbf z}-w_{i,k,\mathbf z}
=\lambda_*\left(k-\frac{n_i+1}{2}\right),\qquad
w_{i,0,\mathbf z}=w_{i,n_i,\mathbf z}=0,
\]
where \(\mathbf z\) fixes all other coordinates. Solving the recurrence from \(k=1\) gives uniquely \(w_{i,k,\mathbf z}=\lambda_* k(n_i-k)/2\), independently of \(\mathbf z\). This holds in every direction and for every fiber, proving **global uniqueness**.

**Uniform comparison.** The number of edges in a cubic grid is \(d(n-1)n^{d-1}\), so each uniform rate is \(B/[d(n-1)n^{d-1}]\). Its gap is that rate times \(2(1-\cos(\pi/n))\). Dividing the optimized gap by this value gives the ratio above. Taylor expansion of cosine proves the limit.

## Verification

The supplied `verify.py` uses exact rational arithmetic to verify budgets and coordinate eigen-equations on eight grid shapes; exactly factors four small characteristic polynomials and independently diagonalizes four larger Laplacians to verify the full spectrum; checks 1,440 genuinely non-product random edge allocations against the bound; and constructs a separate non-path example \(K_3\square P_4\) with exact gap \(1/19\). The executable `verification_output.txt` records the checked totals. These finite tests corroborate, but do not replace, the universal variational and polynomial-flag proof.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006), Section 5.2, already derive the parabolic optimum on a **single path** in their continuous-time fastest-mixing Markov-process problem and cite earlier work on absolute algebraic connectivity. No novelty is claimed for that one-dimensional profile. De Abreu (available online 17 October 2006) surveys algebraic connectivity and the ordinary Cartesian-product spectral identity. These prior facts are inputs, not new assertions.

The 2026 work by Indrani Y. R. L. and coauthors gives exact spectral design for Cartesian products with one **constant multiplier per direction**, under a directional-multiplier budget. It explicitly notes that its design does not optimize each individual edge. The present result uses a **global sum-of-conductances** budget, permits independently adjustable rates on every product edge, proves a sharp no-benefit-from-fiber-asymmetry result, and proves the unique nonuniform within-direction grid allocation. These results do not follow merely by substituting direction multipliers into that restricted optimizer. Wan and coauthors (2008) analyze necessary optimization structure and general spectral-design conditions, not the given global grid classification. Shakeri and coauthors (2015) optimize interconnection edges with existing layer Laplacians fixed, a different feasible set.

## Limitations

The theorem gives a reduction to factor-level optimal values for arbitrary connected factors, but does not solve every factor problem or classify all general-product maximizers. It assumes identical unit costs per conductance across all edges, an undirected combinatorial Laplacian, and a fixed total budget; distinct costs, directed chains, fixed node degrees, discrete-time stochastic normalization, and robustness objectives are not classified. Although direct specialized-source searches did not reveal an equivalent **unrestricted** product theorem and uniqueness statement, overlooked earlier coverage remains possible, and the proof combines classical spectral and variational techniques. No independent mathematical audit has been performed.

## References

1. N. M. M. de Abreu, “Old and new results on algebraic connectivity of graphs,” *Linear Algebra and its Applications* 423 (2007), 53–73; available online 17 October 2006. DOI: `10.1016/j.laa.2006.08.017`.
2. J. Sun, S. Boyd, L. Xiao and P. Diaconis, “The fastest mixing Markov process on a graph and a connection to a maximum variance unfolding problem,” *SIAM Review* 48 (2006), 681–699, especially Section 5.2. DOI: `10.1137/S0036144504443821`.
3. Y. Wan et al., “On the structure of graph edge designs that optimize the algebraic connectivity,” *47th IEEE Conference on Decision and Control* (2008). DOI: `10.1109/CDC.2008.4738734`.
4. Indrani Y. R. L., Sowmya S. B., Sudha S. and Somalatha M. T., “Algebraic connectivity and exact Laplacian spectra of generalized graph products,” *Journal of Integrative Science and Societal Impact* 2 (2026), 63–71. DOI: `10.29121/JISSI.v2.i2.2026.93`.
5. H. Shakeri et al., “Maximizing algebraic connectivity in interconnected networks,” arXiv:`1510.06785v1` (2015).
