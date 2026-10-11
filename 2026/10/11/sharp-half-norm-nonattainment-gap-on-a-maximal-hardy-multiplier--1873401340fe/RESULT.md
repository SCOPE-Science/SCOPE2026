# Sharp half-norm nonattainment gap on a maximal Hardy multiplier ideal

## Finding
Let \(H^2\) be the complex Hardy Hilbert space on the disk and let \(A(\mathbb D)\) denote the disk algebra, with its uniform norm on the closed disk. For \(f\in A(\mathbb D)\) write \(M_fh=fh\) on \(H^2\), and let \(\mathcal A=\{M_f:f\in A(\mathbb D)\}\), equipped with the operator norm. For each \(\zeta\in\mathbb T\), define the boundary-vanishing ideal
\[
\mathcal J_\zeta=\{M_f\in\mathcal A:f(\zeta)=0\}.
\]
The following is a single sharp structural nonattainment theorem.

**(a) Attainment classification.** For every nonzero \(f\in A(\mathbb D)\), the operator \(M_f\) attains its operator norm if and only if it attains its minimum modulus, and this happens if and only if \(f\) is a nonzero scalar multiple of a finite Blaschke product (constants included). The zero operator attains both extrema. The norm-attaining subset of \(\mathcal A\) is norm closed and nowhere dense.

**(b) Maximal nonattaining ideal and sharp gap.** The space \(\mathcal J_\zeta\) is a closed, infinite-dimensional, codimension-one algebra ideal in \(\mathcal A\). Every nonzero member is injective, has nonclosed range and fails ordinary norm attainment, quasi norm attainment, and minimum-modulus attainment. It is maximal by inclusion among complex linear subspaces of \(\mathcal A\) with every nonzero element failing ordinary norm attainment. Moreover, for every \(M_f\in\mathcal J_\zeta\),
\[
\operatorname{dist}_{\mathcal A}\bigl(M_f,\operatorname{NA}(\mathcal A)\bigr)\geq\tfrac12\lVert M_f\rVert.
\]
The constant \(\tfrac12\) is the largest universal constant: for \(\zeta=1\), \(f(z)=(1-z)/2\), and the norm-attaining constant multiplier \(g(z)=1/2\), both the distance and \(\lVert f\rVert_\infty/2\) equal \(1/2\).

**(c) Width rigidity.** With the standard Hilbert-space definitions of approximation, Bernstein, Gelfand and Kolmogorov numbers, every nonzero \(M_f\in\mathcal J_\zeta\) satisfies, for every integer \(n\geq1\),
\[
a_n(M_f)=b_n(M_f)=c_n(M_f)=d_n(M_f)=\lVert M_f\rVert=\lVert f\rVert_\infty.
\]
Thus failure of both extremal attainment notions and of closed range coexists with a completely flat profile of all four finite-dimensional operator widths.

## Assumptions and scope
The field is \(\mathbb C\), \(\mathbb D\) is the open unit disk and \(\mathbb T\) its boundary. The norm on \(H^2\) is normalized boundary \(L^2\)-norm. The disk algebra consists of functions holomorphic in \(\mathbb D\) and continuous on its closure. Minimum modulus means \(m(T)=\inf_{\lVert h\rVert=1}\lVert Th\rVert\), with attainment at a unit vector. Quasi norm attainment means that the norm closure of \(T(B_{H^2})\) contains a vector of norm \(\lVert T\rVert\). All distances and linear-subspace maximality statements are **relative to \(\mathcal A\)**, not to the full operator algebra \(\mathcal L(H^2)\).

For a bounded Hilbert-space operator \(T\), use \(a_n(T)=\inf_{\operatorname{rank} R<n}\lVert T-R\rVert\), \(b_n(T)=\sup_{\dim E=n}\inf_{h\in S_E}\lVert Th\rVert\), \(c_n(T)=\inf_{\operatorname{codim} E<n}\lVert T|_E\rVert\), and \(d_n(T)=\inf_{\dim F<n}\lVert Q_FT\rVert\), where \(Q_F\) is the quotient map by a target subspace \(F\). Every such space \(E\) or \(F\) is closed when needed. These definitions include \(n=1\).

## Proof
### 1. Boundary kernels and extremal values
For \(0<r<1\) and \(\eta\in\mathbb T\), the normalized Szegő kernel is
\[
k_{r,\eta}(z)=\frac{\sqrt{1-r^2}}{1-r\overline\eta z},\qquad \lVert k_{r,\eta}\rVert_{H^2}=1.
\]
Its boundary squared modulus is the Poisson kernel concentrated at \(\eta\), and \(k_{r,\eta}\rightharpoonup0\) weakly in \(H^2\) as \(r\uparrow1\): for every polynomial the pairing tends to zero by the \(\sqrt{1-r^2}\) factor, and polynomials are dense. Therefore for any \(f\in A(\mathbb D)\),
\[
\lim_{r\uparrow1}\lVert M_fk_{r,\eta}\rVert=|f(\eta)|,
\]
and the integral boundary representation gives
\[
\lVert M_f\rVert=\max_{\eta\in\mathbb T}|f(\eta)|,
\qquad m(M_f)=\min_{\eta\in\mathbb T}|f(\eta)|.
\]
The second identity combines the pointwise lower bound with kernels concentrated at a minimizing boundary point.

### 2. Exact coincidence of norm and minimum attainment
Every nonzero \(h\in H^2\) has boundary values different from zero almost everywhere (the Hardy uniqueness theorem). If \(h\) attains the operator norm of \(M_f\), then
\[
\int_\mathbb T(\lVert f\rVert_\infty^2-|f|^2)|h|^2=0,
\]
forcing \(|f|\) to equal its maximum almost everywhere and hence everywhere by continuity. If \(h\) attains the minimum modulus, the same reasoning with \(|f|^2-(\min_{\mathbb T}|f|)^2\) forces constant boundary modulus. Conversely constant boundary modulus makes \(M_f\) a scalar multiple of an isometry, so both extrema are attained by every unit vector.

For nonzero \(f\in A(\mathbb D)\), constant nonzero boundary modulus implies that the zeros of \(f\) are finitely many and lie strictly inside the disk. Divide by the corresponding finite Blaschke product. The quotient is zero-free, analytic on the disk, continuous and nonzero on the closed disk, and has constant boundary modulus. The maximum and minimum modulus principles then force the quotient to be constant. This proves (a)'s classification. Uniform convergence of symbols preserves constancy of boundary modulus, proving that \(\operatorname{NA}(\mathcal A)\) is closed. It has empty interior: perturb a nonconstant finite Blaschke multiple by a small nonzero constant; perturb a constant (including zero) by a small nonconstant affine polynomial. The boundary modulus ceases to be constant. Hence the set is nowhere dense.

### 3. Codimension-one ideal and sharp uniform separation
Boundary evaluation \(f\mapsto f(\zeta)\) is a nonzero continuous multiplicative functional on the disk algebra, so its kernel is a closed codimension-one ideal. The independent functions \((z-\zeta)z^j\), \(j=0,1,2,\ldots\), show infinite dimension. The map \(f\mapsto M_f\) is an isometry by Step 1, hence transfers these conclusions to \(\mathcal J_\zeta\). Every proper linear super-space of a codimension-one subspace equals \(\mathcal A\) and contains the identity multiplier, which is norm attaining. This proves maximality in (b).

For \(f\in A(\mathbb D)\setminus\{0\}\) with \(f(\zeta)=0\), write \(M=\lVert f\rVert_\infty>0\). Then \(|f|\) is not constant on the boundary, so neither norm nor minimum is attained; by Step 1, the minimum modulus is zero. Multiplication by a nonzero holomorphic function is injective, hence the zero minimum is not attained and the range is not closed (otherwise an injective bounded map between Banach spaces would be bounded below). On the reflexive space \(H^2\), the image of the unit ball under a bounded linear operator is weakly compact and therefore norm closed, so quasi norm attainment implies ordinary norm attainment. Thus it also fails.

Let \(g\in A(\mathbb D)\) have norm-attaining multiplier and put \(t=\lVert g\rVert_\infty\). Step 2 implies \(|g|=t\) on the full boundary. Choose \(\eta\in\mathbb T\) where \(|f(\eta)|=M\). At the boundary points \(\zeta\) and \(\eta\), respectively,
\[
\lVert f-g\rVert_\infty\geq t,
\qquad
\lVert f-g\rVert_\infty\geq |M-t|.
\]
Consequently \(\lVert f-g\rVert_\infty\geq\max\{t,|M-t|\}\geq M/2\). Taking the infimum over all norm-attaining \(g\) proves the gap. When \(f(z)=(1-z)/2\), \(g(z)=1/2\), the gap equals \(\lVert f-g\rVert_\infty=1/2\) and \(M=1\), proving sharpness. Rotating the variable gives the same sharpness for every prescribed boundary point.

### 4. Four exact operator-width profiles
The upper bound \(a_n,b_n,c_n,d_n\leq M\) follows directly from the definitions. Choose \(\eta\in\mathbb T\) with \(|f(\eta)|=M\). The kernels \(k_{r,\eta}\rightharpoonup0\) while \(\lVert M_fk_{r,\eta}\rVert\to M\). Finite-rank operators take weakly null bounded sequences to norm-null sequences, so every finite-rank approximation to \(M_f\) has error at least \(M\), giving \(a_n=M\). For any finite-codimensional closed \(E\subset H^2\), orthogonally projecting \(k_{r,\eta}\) onto \(E\) changes it by a norm-null sequence; the projected vectors give \(c_n=M\). For any finite-dimensional target \(F\subset H^2\), the projection of \(M_fk_{r,\eta}\) onto \(F\) tends to zero in norm because the images are weakly null; therefore the quotient norm tends to \(M\), giving \(d_n=M\).

For Bernstein numbers fix \(n\geq1\) and \(\varepsilon>0\). Choose an open arc \(U\subset\mathbb T\) where \(|f|>M-\varepsilon\), and select distinct \(\eta_1,\ldots,\eta_n\in U\). Their normalized Szegő kernels have Gram matrix tending to the identity because
\[
\bigl\langle k_{r,\eta_i},k_{r,\eta_j}\bigr\rangle
=\frac{1-r^2}{1-r^2\overline{\eta_i}\eta_j}
\quad(i\neq j),
\]
while each kernel has \(L^2\)-mass tending to zero outside \(U\). Uniformly over unit vectors in the \(n\)-dimensional span of these kernels, the \(L^2\)-mass outside \(U\) is \(o(1)\) as \(r\uparrow1\). Hence \(M_f\) is bounded below on that span by \((M-\varepsilon)(1-o(1))\). Thus \(b_n\geq M-\varepsilon\), and letting \(\varepsilon\downarrow0\) gives \(b_n=M\). This proves (c) for every \(n\) without extrapolation from finite experiments.

## Verification
The analytical identities use the normalized Poisson approximate identity, Hardy boundary uniqueness, the maximum/minimum modulus principles, and finite-dimensional weak-null estimates. Sharpness can be verified directly: for \(f(z)=(1-z)/2\), \(g(z)=1/2\), one has \(\lVert f\rVert_\infty=1\), \(f(1)=0\), and \(\lVert f-g\rVert_\infty=1/2\). For \(f(z)=1-z\), the multiplier norm is \(2\), the minimum modulus is \(0\) and neither is attained. The proof of every \(s\)-number equality is analytic and valid for arbitrary finite index \(n\), not based on numerical sampling.

## Relationship to prior work
Ramesh and Sequeira (arXiv:2209.05841v1, 2022, Theorems 2.4 and 2.7) characterize **absolute** norm/minimum attainment of Toeplitz operators and already supply prior information about constant-boundary-modulus symbols. The elementary ordinary attainment classification in Step 2 is not presented as a stand-alone new breakthrough. Dantas, Falcó, Jung and Rodríguez-Vidanes (arXiv:2311.17426v1, 2023; later revised) study large linear spaces of non-norm-attaining operators, but their stated constructions concern different domain/range geometries. The present focused assertion is the quantitative optimal half-norm exclusion gap on a maximal analytic Toeplitz ideal, simultaneously with failure of both attainment notions and four flat operator-width profiles. Yoshino's 2002 work on norm-achieved Toeplitz operators is acknowledged as relevant to the ordinary norm-attainment component, without claiming its unseen full text excludes any overlap.

## Limitations
The distance bound concerns the norm-attaining subset **within** the disk-algebra analytic multiplier algebra; it makes no assertion of a positive distance from the norm-attaining operators of the entire \(\mathcal L(H^2)\). The universal bound is optimal but not asserted to equal the exact distance for every individual symbol. The maximality is relative to complex linear subspaces of \(\mathcal A\), not all bounded-operator subspaces. The theorem makes no assertion for arbitrary \(H^\infty\) symbols lacking continuous boundary values or for nonanalytic Toeplitz symbols. Prior results may cover some elementary ingredients, and an unindexed quantitative equivalent cannot be excluded without a separate independent literature audit.

## References
1. G. Ramesh and S. S. Sequeira, *Absolutely minimum attaining Toeplitz and absolutely norm attaining Hankel operators*, arXiv:2209.05841v1, first public 13 September 2022, Theorems 2.4 and 2.7; https://arxiv.org/html/2209.05841v1 .
2. S. Dantas, J. Falcó, M. Jung and D. L. Rodríguez-Vidanes, *Linear structures in the set of non-norm-attaining operators on Banach spaces*, arXiv:2311.17426, first public 29 November 2023; https://arxiv.org/html/2311.17426v2 .
3. T. Yoshino, *The structure of norm-achieved Toeplitz and Hankel operators*, Nihonkai Math. J. **13** (2002), 43–55 (bibliographic comparison only; full text not inspected).
