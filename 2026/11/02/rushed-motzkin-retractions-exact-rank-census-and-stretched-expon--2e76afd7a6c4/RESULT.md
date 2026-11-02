# Rushed Motzkin retractions: exact rank census and stretched-exponential rarity for weak cycle endomorphisms

## Finding
For every integer \(n\ge 3\), let \(C_n\) be the undirected simple cycle and \(W_n\) its weak-endomorphism monoid: a transformation \(f:\mathbb Z/n\mathbb Z\to\mathbb Z/n\mathbb Z\) belongs to \(W_n\) if successive image vertices are equal or adjacent. Define \(E_{n,r}\) to count idempotents in \(W_n\) with image size \(r\). With \(B_\ell\) the \((\ell+1)\)-by-\((\ell+1)\) matrix having ones on the main and immediately adjacent diagonals, the complete rank distribution is
\[
E_{n,\ell+1}=n(B_\ell^{n-\ell})_{0,\ell}\quad(0\le\ell\le\lfloor n/2\rfloor),\qquad E_{n,n}=1,
\]
and all remaining \(E_{n,r}\) vanish. There is no collision between the displayed ranks and \(n\) for \(n\ge3\). Define \(D_0(z)=1\), \(D_1(z)=1-z\), and \(D_j(z)=(1-z)D_{j-1}(z)-z^2D_{j-2}(z)\) for \(j\ge2\). An equivalent explicit coefficient formula is
\[
E_{n,\ell+1}=n[z^{n-2\ell}]D_{\ell+1}(z)^{-1}.
\]
Let \(E_n=\sum_{r=1}^n E_{n,r}\). As \(n\to\infty\),
\[
\log E_n=n\log3-c n^{1/3}+O(\log n),\quad
c=\tfrac32\left(\frac{2\pi^2(\log3)^2}{3}\right)^{1/3}.
\]
If \(R_n\) denotes the image size of an idempotent chosen uniformly from all idempotents in \(W_n\), then
\[
\frac{R_n}{n^{1/3}}\xrightarrow{\mathbb P}\kappa,
\qquad \kappa=\left(\frac{2\pi^2}{3\log3}\right)^{1/3}.
\]
Finally, writing \(T_n=[x^0](x^{-1}+1+x)^n\), the entire monoid has cardinality \(|W_n|=n(T_n+2)\), and therefore its idempotent density satisfies
\[
\log\frac{E_n}{|W_n|}=-c n^{1/3}+O(\log n).
\]
These statements concern *weak* graph endomorphisms, allowing collapse of an edge; the already-studied strict-endomorphism/Dyck-path enumeration is not claimed as new.

## Assumptions and scope
The cycle is simple, with \(n\ge3\), and all maps act on labeled vertices. A weak endomorphism is required to preserve or contract every edge; images of adjacent vertices may coincide. A retraction means an idempotent transformation and hence is the identity on its image. Rank means image cardinality, not the rank of a monoid generating set. The asymptotic parameter is the number of vertices \(n\) tending to infinity. Errors in asymptotic formulas are uniform in \(n\), with numerical constants absolute.

## Proof
**1. Images of idempotents.** The image of a connected graph under a weak homomorphism is connected. Thus, unless the image equals the entire cycle, it is a contiguous proper cyclic arc with \(\ell+1\) vertices, which can be labeled \(0,1,\ldots,\ell\) in order. The retraction fixes those vertices individually. There are exactly \(n\) choices of such an arc for every \(\ell<n-1\). The complementary boundary-to-boundary path of the original cycle contains \(n-\ell\) edges; its image is a walk of that length from endpoint \(\ell\) back to endpoint \(0\) within the fixed arc, with increments \(-1,0,+1\), never leaving the arc. Reversing orientation gives the transfer entry \((B_\ell^{n-\ell})_{0,\ell}\). Such a walk exists only when \(n-\ell\ge\ell\). Each walk extends uniquely to an idempotent. A surjective idempotent is the identity. This proves the complete rank spectrum and uniqueness without double counting. For \(\ell=0\), these are the \(n\) constant retractions.

**2. Exact rational generating function.** Set \(B_\ell=(\mathbf1_{|i-j|\le1})_{0\le i,j\le\ell}\). The resolvent entry \((I-zB_\ell)^{-1}_{0,\ell}\) is \(z^\ell/D_{\ell+1}(z)\), by the cofactor formula for a tridiagonal matrix; expansion as \(\sum_{N\ge0}z^NB_\ell^N\) gives the coefficient expression. Expanding its determinant along the last row proves the displayed continuant recursion.

**3. Perron eigenvalue and uniform dominant term.** The eigenvalues of \(B_\ell\) are \(1+2\cos(j\pi/(\ell+2))\) for \(j=1,\ldots,\ell+1\). The largest is \(\lambda_\ell=1+2\cos(\pi/(\ell+2))\). Its normalized eigenvector has coordinates \(\sqrt{2/(\ell+2)}\sin((i+1)\pi/(\ell+2))\), giving strictly positive endpoint projection
\[
a_\ell=\frac{2\sin^2(\pi/(\ell+2))}{\ell+2}.
\]
The other eigenvalues have absolute value at most \(\rho_\ell<\lambda_\ell\), for \(\ell\ge1\). Therefore, writing \(N=n-\ell\),
\[
(B_\ell^N)_{0,\ell}=a_\ell\lambda_\ell^N+O(\rho_\ell^N),
\]
where the error has an absolute coefficient bound one by orthonormality. For \(\ell=x n^{1/3}\) with \(x\) in any fixed compact subinterval of \((0,\infty)\), the spectral-gap bound \(\log(\lambda_\ell/\rho_\ell)=\Theta(\ell^{-2})\) implies that the error divided by the main term tends to zero uniformly, since \(a_\ell=\Theta(\ell^{-3})\) and \(N/\ell^2=\Theta(n^{1/3})\).

**4. Laplace principle and concentration.** Uniformly for \(x\) in compact positive intervals and \(\ell=x n^{1/3}+O(1)\),
\[
\log\bigl[n(B_\ell^{n-\ell})_{0,\ell}\bigr]
=n\log3-n^{1/3}\Phi(x)+O(\log n),\quad
\Phi(x)=x\log3+\frac{\pi^2}{3x^2}.
\]
Indeed \(\log\lambda_\ell=\log3-\pi^2/(3(\ell+2)^2)+O(\ell^{-4})\); the \(\ell\)-step fixed arc costs a factor \(3^{-\ell}\), and \(a_\ell\) contributes only a logarithmic term. The continuous function \(\Phi\) diverges at zero and infinity and has unique minimizer \(x=\kappa=(2\pi^2/(3\log3))^{1/3}\), at which \(\Phi(\kappa)=c=3\kappa\log3/2\).

For completeness, the contribution outside any fixed neighborhood of \(\kappa n^{1/3}\) is exponentially smaller on the \(n^{1/3}\) scale: the operator norm bound \((B_\ell^N)_{0,\ell}\le\lambda_\ell^N\) yields
\[
\log\bigl[n(B_\ell^N)_{0,\ell}\bigr]\le \log n+(n-\ell)\log\lambda_\ell.
\]
For small \(\ell\), the exact inequality \(\log(3/\lambda_\ell)\ge C/(\ell+2)^2\) gives the required large spectral penalty; for large \(\ell\), \(\lambda_\ell\le3\) gives the large-prefix penalty \(\ell\log3\). On any compact positive scaled interval, the strict uniqueness of the minimum gives a fixed positive rate gap away from \(\kappa\). There are at most \(n\) summands. A single term with \(\ell\) nearest \(\kappa n^{1/3}\) supplies the matching lower bound. This proves the logarithmic enumeration and the stated convergence in probability; the distinction between rank \(\ell+1\) and \(\ell\) is negligible after scaling.

**5. Size of the ambient monoid.** A weak endomorphism is a closed length-\(n\) walk on the target cycle, with \(n\) choices of initial vertex. Its step sequence belongs to \(\{-1,0,+1\}^n\) and the sum of increments must be divisible by \(n\). As its absolute value is at most \(n\), the only sums are \(0,+n,-n\). The latter two are the single all-positive and all-negative walks; zero-sum sequences are counted by the central trinomial coefficient \(T_n\). Thus \(|W_n|=n(T_n+2)\). By the elementary local central limit theorem, \(T_n=\Theta(3^n n^{-1/2})\) (more precisely \(T_n\sim\sqrt3\,3^n/(2\sqrt{\pi n})\)); taking logarithms yields the density claim.

## Verification
The accompanying `verify_weak_cycle.py` independently enumerates all weak graph endomorphisms for \(3\le n\le9\) by cyclic step sequences and direct transformation evaluation, tests idempotence, and records every rank. It separately computes the transfer-matrix formula by a dynamic program, and checks equality for every tested \(n\). This is an exhaustive finite cross-check, not a substitute for the all-\(n\) proof. It prints `VERIFY_OK` upon success. Example totals are \(E_6=157\), \(E_8=1025\), \(E_9=2620\); the corresponding monoid sizes are \(858\), \(8872\), and \(28269\).

## Relationship to prior work
Dimitrova, Fernandes, Koppitz, and Quinteiro (2023) study weak and ordinary endomorphism monoids of cycles, including structural properties and ambient cardinalities. Their theorems do not give the above weak-idempotent rank census or its probability scaling. Knauer and Pipattanajinda (2018) enumerate weak endomorphisms of *paths*, not weak-cycle idempotents. Bacher (2024), building on earlier bijections, studies *rushed Dyck paths* and one-sided trees; the strict cycle-retraction count has a known rushed-Dyck counterpart, and Bacher's stretched-exponential theorem covers that strict setting. It does **not** imply the weak Motzkin model, whose transfer matrix has diagonal steps, base \(3\) instead of \(2\), and a different saddle constant. Bacher explicitly raises the possibility of extensions beyond Dyck paths to Motzkin paths in the concluding discussion. The OEIS entry A287709 likewise covers the strict Dyck enumeration and is not an exact table of weak-cycle idempotents. We make no claim that the strict result is novel.

## Limitations
The result is for undirected simple cycles and weak maps allowing edge contraction; it does not classify nonidempotents or arbitrary graphs. Asymptotics are for large numbers of vertices, not fixed-rank limits. The principal novelty claim is relative to the inspected sources; an unlocated equivalent enumeration in Motzkin-path or transformation-semigroup literature remains possible. Independent audit has not been performed.

## References
1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149 (first posted 2023-10-06), https://arxiv.org/abs/2310.04149.
2. A. Bacher, *Progressive and Rushed Dyck Paths*, arXiv:2403.08120 (first posted March 2024), https://arxiv.org/abs/2403.08120.
3. U. Knauer and N. Pipattanajinda, *A formula for the number of weak endomorphisms on paths*, Algebra and Discrete Mathematics 26 (2018), https://admjournal.luguniv.edu.ua/index.php/adm/article/view/349.
4. OEIS A287709, *Rushed Dyck paths / related one-sided trees*, https://oeis.org/A287709 (strict-model comparator only).
