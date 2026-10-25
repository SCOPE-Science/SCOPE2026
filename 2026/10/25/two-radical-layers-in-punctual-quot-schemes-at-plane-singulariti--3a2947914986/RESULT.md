# Two radical layers in punctual Quot schemes at plane singularities of multiplicity at least three

## Finding
Let \(k\) be any field and let \(R=k[[x,y]]/(f)\) be a reduced complete plane-curve local ring with nonzero \(f\in(x,y)^3\). For each integer \(d\ge1\), define \(Q_d\) to parametrize finite-length quotient maps \(R^d\twoheadrightarrow M\) such that \(\operatorname{length}_R M=d+2\) and \(\dim_k(M/\mathfrak m M)=d\), up to the usual equivalence of quotients. There is a two-stratum decomposition: the closed stratum is \(\operatorname{Gr}(2,2d)\), and the other is a vector bundle of rank \(2d-1\) on \(\mathbf P^{d-1}\times\mathbf P^1\). Therefore, putting \(\mathbb L=[\mathbf A^1]\),
\[
[Q_d]=[\operatorname{Gr}(2,2d)]+\mathbb L^{2d-1}[\mathbf P^{d-1}][\mathbf P^1].
\]
This is a formula for the actual geometric strata, not merely for their Euler characteristics. It is independent of every term of \(f\) of order three or higher.

For \(H_d(t)=\sum_{n\ge0}[\operatorname{Quot}^{d}_{d,d+n}(R)]t^n\), the first coefficients are \([t^0]H_d=1\), \([t^1]H_d=[\mathbf P^{2d-1}]\), and \([t^2]H_d=[Q_d]\). Consequently
\[
[t^2]\prod_{i=0}^{d-1}(1-\mathbb L^it)H_d(t)
=\mathbb L^{2d}\left({d\brack2}_{\mathbb L}+{d\brack1}_{\mathbb L}\right),
\]
where \({n\brack r}_{\mathbb L}=[\operatorname{Gr}(r,n)]\) denotes the Gaussian polynomial, with \({n\brack r}_{\mathbb L}=0\) when \(r>n\). Over \(\mathbf F_q\), the corresponding exact point count is
\[
\#Q_d(\mathbf F_q)={2d\brack2}_q+q^{2d-1}{d\brack1}_q(q+1).
\]

## Assumptions and scope
The characteristic of \(k\) is arbitrary. The equation is reduced, and its multiplicity at the chosen point is at least three. The Quot locus is supported entirely at that point, and the superscript \(d\) fixes the *minimal number of generators*; it is **not** the entire punctual Quot scheme of length \(d+2\). No global smoothness of the curve is claimed, and nothing is asserted for ordinary nodes or cusps of multiplicity two. Quot schemes are considered as varieties for the stated class identity; the strata are realized by explicit relative affine/vector bundles and Grassmannians.

## Proof
Write \(\mathfrak m\) for the maximal ideal of \(R\). Every quotient represented by \(Q_d\) has \(\dim_k\mathfrak mM=2\), since \(M/\mathfrak mM\cong k^d\) and the length is \(d+2\). Nakayama implies its kernel \(N\) is contained in \(\mathfrak mR^d\). The chain \(\mathfrak mM\supseteq\mathfrak m^2M\supseteq\mathfrak m^3M\supseteq\cdots\) has total length two, whence \(\mathfrak m^3M=0\). Thus all quotients factor through \((R/\mathfrak m^3)^d\), which is \((k[x,y]/(x,y)^3)^d\) because \(f\in(x,y)^3\).

Choose the degree filtration and its coordinate splitting:
\[
V_1=(\mathfrak m/\mathfrak m^2)^d\cong k^{2d},\qquad V_2=(\mathfrak m^2/\mathfrak m^3)^d\cong k^{3d}.
\]
If \(\mathfrak m^2M=0\), then \(N\) is determined by a codimension-two subspace \(U\subset V_1\), with all of \(V_2\) included in the kernel. This is the Grassmannian \(\operatorname{Gr}(2,V_1)\). The condition \(\mathfrak m^2M=0\) is closed in the Quot locus.

Otherwise the radical filtration is exactly \((d,1,1)\). Let \(U\subset V_1\) and \(W\subset V_2\) be the codimension-one intersections of the kernel with the two graded pieces. Choose \(\beta=(A,B,C)\in V_2^*\setminus\{0\}\), up to scale, such that \(W=\ker\beta\), where each of \(A,B,C\) is a covector on \(k^d\). Multiplication by \(x\) and \(y\) from \(V_1\) to \(V_2\) gives dual rows \((A,B)\) and \((B,C)\), respectively. Stability of the kernel is precisely \(U\subseteq\ker(A,B)\cap\ker(B,C)\). Since \(U\) has codimension one, the resulting two-by-\(2d\) matrix must have rank at most one. It cannot be zero because \(\beta\ne0\), so its rank is one and \(U\) is uniquely its common hyperplane kernel.

The rank-one equations for the block-Hankel matrix are equivalent, scheme-theoretically, to the Segre–Veronese parametrization
\[
(A,B,C)=(u^2w,uv w,v^2w),\qquad [u:v]\in\mathbf P^1,\quad[w]\in\mathbf P^{d-1}.
\]
For clarity, on the chart where some coordinate of \(A\) is nonzero, row proportionality forces \(B=sA\) and \(C=s^2A\), yielding an affine chart of the displayed product; the complementary chart is identical with \(C\ne0\). These two charts cover the rank-one locus, so the identification works in every characteristic and for arbitrary base change.

For each such \((U,W)\), a kernel modulo \(\mathfrak m^3\) is the graph of a map \(U\to V_2/W\), together with \(W\). All these graphs satisfy multiplication stability because the latter only depends on \(U\) and \(W\), and \(\mathfrak mV_2=0\). The graph parameter space is the vector bundle \(\operatorname{Hom}(\mathcal U,V_2/\mathcal W)\) of rank \(\dim U=2d-1\) over the Segre–Veronese base. This proves the two strata and their classes.

Finally, write \(S_1={d\brack1}_{\mathbb L}\), \(S_2=\mathbb L{d\brack2}_{\mathbb L}\); these are the first two elementary symmetric functions of \(1,\mathbb L,\ldots,\mathbb L^{d-1}\). The degree-two coefficient in \(\prod_{i=0}^{d-1}(1-\mathbb L^it)H_d(t)\) is \([Q_d]-S_1[\mathbf P^{2d-1}]+S_2\). Substitution of the stratum formula and the Gaussian Vandermonde identity \({2d\brack2}_{\mathbb L}=(1+\mathbb L^{2d}){d\brack2}_{\mathbb L}+\mathbb L^{d-1}{d\brack1}_{\mathbb L}^2\) yields \(\mathbb L^{2d}({d\brack2}_{\mathbb L}+{d\brack1}_{\mathbb L})\), as claimed.

## Verification
The standalone `verify.py` enumerates all projective covectors \(\beta\) in the block-Hankel rank-one locus over \(\mathbf F_2\) and \(\mathbf F_3\) for \(1\le d\le3\), checks the expected \(\mathbf P^{d-1}\times\mathbf P^1\) counts, and independently checks the finite-field versions of the two coefficient identities. It returns `VERIFY_OK`. These finite tests supplement, but do not replace, the all-fields argument above.

## Relationship to prior work
Huang–Jiang, *Motivic Coh and Quot zeta functions of singular curves* (arXiv:2312.12528, first public 2023-12-19), establishes a general rationality framework for reduced singular curves, and explicit formulas for double-cover plane germs \(y^2=x^n\). The earlier cusp study, arXiv:2305.06411, and its successor address multiplicity-two singularities; their rank-uniform formulas do not state the rank-one block-Hankel stratum for arbitrary multiplicity-at-least-three plane curves. Graffeo–Monavari–Moschetti–Ricolfi, arXiv:2406.14321, studies punctual smooth-ambient Quot schemes with fixed small quotient length (up to four), which is distinct from this length \(d+2\) and minimal-generator \(d\) family. The theorem here is a concrete first two-layer structural and motivic consequence compatible with the broader framework; no priority is claimed for the general rationality theorem or the general Quot-moduli construction.

## Limitations
Only the fixed-minimal-generator stratum is determined, and only its first length excess two. The argument does not compute higher punctual Quot coefficients, identify the scheme structure along the boundary between the two strata, or assert a complete motivic zeta function. The prior literature may contain equivalent small-length formulas not indexed by the exact geometric description; the novelty assessment therefore retains a residual overlap risk. This has not undergone independent audit.

## References
1. Y. Huang and R. Jiang, *Motivic Coh and Quot zeta functions of singular curves*, arXiv:2312.12528, first public 2023-12-19, https://arxiv.org/abs/2312.12528.
2. Y. Huang and R. Jiang, *Punctual Quot schemes and Cohen–Lenstra series of the cusp singularity*, arXiv:2305.06411, first public 2023-05-10, https://arxiv.org/abs/2305.06411.
3. M. Graffeo, S. Monavari, R. Moschetti, and A. T. Ricolfi, *The motive of the Hilbert scheme of points in all dimensions*, arXiv:2406.14321, first public 2024-06-20, https://arxiv.org/abs/2406.14321.
