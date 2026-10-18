# A universal square-root law for iterated Thom–Sebastiani Tjurina numbers

## Finding
Let \(h\in\mathbb C\{x_1,\ldots,x_d\}\), \(d\ge2\), satisfy \(h(0)=0\) and have an isolated critical point at the origin, and write
\[
A_h=\mathbb C\{\mathbf x\}/J_h,\qquad \mu=\dim_{\mathbb C}A_h.
\]
Let \(N\colon A_h\to A_h\) denote multiplication by the class of \(h\), with Jordan block lengths \(\ell_1,\ldots,\ell_t\). Set
\[
P_h(z)=\sum_{j=1}^{t}\sum_{a=0}^{\ell_j-1}z^{\ell_j-1-2a},
\qquad
\sigma_h^2=\frac{1}{3\mu}\sum_{j=1}^{t}\ell_j(\ell_j^2-1).
\]
For each integer \(r\ge1\), form the isolated singularity in pairwise disjoint variables \(F_r=\sum_{i=1}^r h(\mathbf x_i)\). Then
\[
\boxed{\mu(F_r)=\mu^r,\qquad
\tau(F_r)=[z^0]P_h(z)^r+[z^1]P_h(z)^r.}
\]
If \(N=0\), the ratio \(\tau(F_r)/\mu(F_r)\) is identically one. If \(N\ne0\), then \(\sigma_h^2>0\), and
\[
\boxed{\frac{\tau(F_r)}{\mu(F_r)}=
\sqrt{\frac{2}{\pi\sigma_h^2r}}\left(1+O_h(r^{-1})\right).}
\]
The limiting constant depends on the cubic moment of the Jordan lengths, not merely on \(\mu\) or on the initial Tjurina number \(\tau(h)\).

## Assumptions and scope
The base field is \(\mathbb C\), the germ vanishes at the origin, and the origin is an isolated critical point (hence the Milnor number is finite). For isolated singularities, the Milnor algebra is an Artin local algebra and \([h]\) lies in its maximal ideal, so \(N\) is nilpotent. Each length \(\ell_j\ge1\), with \(\sum_j\ell_j=\mu\). No upper bound on the Jordan lengths is assumed. The symbol \([z^k]\) denotes a Laurent coefficient. The asymptotic is for a fixed germ \(h\) while \(r\to\infty\); its error constant can depend on \(h\).

## Proof
**Separated Milnor and Tjurina algebras.** Because the variables separate, the Jacobian algebra of \(F_r\) is naturally \(A_h^{\otimes r}\), of dimension \(\mu^r\). Multiplication by \([F_r]\) is the nilpotent operator
\[
N_r=\sum_{i=1}^{r}I^{\otimes(i-1)}\otimes N\otimes I^{\otimes(r-i)}.
\]
The Tjurina algebra is its cokernel. Since \(N_r\) is an endomorphism of a finite-dimensional vector space, \(\tau(F_r)=\dim\ker N_r\).

**Exact character formula.** A nilpotent Jordan block of size \(m\) is the raising operator in the irreducible \(\mathfrak{sl}_2\)-module of dimension \(m\), with weights \(m-1,m-3,\ldots,1-m\). Therefore one can complete \(N\) to the raising operator on a (generally reducible) finite-dimensional \(\mathfrak{sl}_2\)-module \(V\), whose character is exactly \(P_h(z)\). The operator \(N_r\) is the diagonal raising operator on \(V^{\otimes r}\), of character \(P_h(z)^r\). Each irreducible summand contributes one dimension to its kernel.

Write the character as \(\sum_{k\in\mathbb Z}c_kz^k\), and write \(m_j\) for the multiplicity of the irreducible highest-weight-\(j\) module, with \(j\ge0\). Then \(m_j=c_j-c_{j+2}\). Telescoping separately over even and odd \(j\) gives \(\sum_{j\ge0}m_j=c_0+c_1\). This is the asserted Laurent-coefficient formula for every \(r\ge1\).

**Sharp asymptotic including parity.** Uniformly choose one of the \(\mu\) monomial terms of \(P_h(z)\), counted with multiplicity, and call its exponent \(X\). Its distribution is symmetric, so \(\mathbb E X=0\). For a block of size \(m\), the sum of squared weights equals \(m(m^2-1)/3\), giving \(\operatorname{Var}X=\sigma_h^2\). If \(N\ne0\), at least one block has size at least two and hence \(\sigma_h^2>0\). Write \(S_r\) for the sum of \(r\) independent copies of \(X\); then the exact formula reads
\[
\frac{\tau(F_r)}{\mu^r}=\Pr(S_r=0)+\Pr(S_r=1).
\]
If both parities occur among the exponents of \(P_h\), the lattice span is one and the fixed-site local central limit estimate, strengthened by the symmetry and finite support of \(X\), gives
\[
\Pr(S_r=k)=\frac{1}{\sqrt{2\pi\sigma_h^2r}}\bigl(1+O_h(r^{-1})\bigr)
\quad(k=0,1).
\]
If only one parity occurs, the lattice span is two: the presence of a nontrivial Jordan block ensures this span is exactly two. Exactly one of the sites \(0\) and \(1\) has the admissible parity for each \(r\); the other probability vanishes. The admissible site instead has probability
\[
\frac{2}{\sqrt{2\pi\sigma_h^2r}}\bigl(1+O_h(r^{-1})\bigr).
\]
These two cases give the same stated asymptotic. To justify the relative error, Fourier inversion expresses each fixed-site probability by a circle integral of the finite even characteristic polynomial to the \(r\)-th power. Near every maximal-modulus point its Taylor expansion is \(1-\sigma_h^2t^2/2+O_h(t^4)\); Gaussian integration gives an absolute error \(O_h(r^{-3/2})\). Away from the finitely many maximal-modulus points the contribution is exponentially small. This proves the \(O_h(r^{-1})\) relative remainder. If \(N=0\), every \(\ell_j=1\) and \(P_h(z)=\mu\), which makes the coefficient formula equal \(\mu^r\) identically.

**Boundary comparison.** If \(N^2=0\), with \(c\) blocks of length two and \(s\) blocks of length one, one has \(P_h(z)=s+c(z+z^{-1})\), \(\mu=s+2c\), and \(\sigma_h^2=2c/\mu\). The constant specializes to \(\sqrt{\mu/(\pi cr)}\), agreeing with the known square-zero self-sum case. For blocks of size at least three, the full variance above is essential.

## Verification
An included standalone exact-arithmetic program checks the character formula against ranks of Kronecker-sum Jordan matrices for finite blocks of sizes one, two and three, including mixed block configurations, with \(1\le r\le3\) and matrix dimension bounded by 64. It also checks normalization, variance, and finite large-\(r\) approaches to the predicted constant. The checker returns `VERIFY_OK` when all tests pass. These finite tests corroborate examples; the universal claim follows from the preceding algebraic and Fourier arguments.

## Relationship to prior work
Zheng and Zuo, *Hodge–Tjurina Numbers, Tjurina Spectra, and Thom–Sebastiani Formulas* (2026, arXiv:2610.08290v1), prove a general two-factor defect formula and express its ordinary Tjurina correction through Jordan-block counts (notably Theorem B and Section 5). Almirón, *The Tjurina Number for Sebastiani–Thom Type Isolated Hypersurface Singularities* (2023, arXiv:2205.12806), proves two-factor formulas and bounds. These are the algebraic starting points but do not state the arbitrary-iterate coefficient formula or the sharp all-Jordan Gaussian constant. Tate–Zelditch (2004) and Postnova–Reshetikhin (2018) provide broad tensor-multiplicity asymptotics; the precise Gaussian scaling may be implicitly derivable from these results. Neither inspected formulation explicitly states the Tjurina algebra formula or all-Jordan variance given here. Classical \(\mathfrak{sl}_2\) tensor characters and lattice local limit estimates provide the proof mechanism. The previously established square-zero self-join computation is recovered, not reproposed as an independent contribution.

## Limitations
The formula uses the full Jordan type of multiplication by \([h]\); in general its value cannot be inferred from \(\mu(h)\) and \(\tau(h)\) alone. The estimate is not uniform over varying germs. The statement does not determine Hodge-filtered Tjurina spectra, monodromy, or mixed joins of different germs. While relevant algebraic-geometry papers and mathematical records were inspected, an implicit statement in broader nilpotent-tensor or local-limit literature cannot be categorically excluded; no independent audit has been performed.

## References
1. S. Zheng and H. Zuo, *Hodge–Tjurina Numbers, Tjurina Spectra, and Thom–Sebastiani Formulas*, arXiv:2610.08290v1 (6 October 2026), especially Theorem B and Section 5.
2. P. Almirón, *The Tjurina Number for Sebastiani–Thom Type Isolated Hypersurface Singularities*, *Mediterranean Journal of Mathematics* **20** (2023), article 258; arXiv:2205.12806, DOI 10.1007/s00009-023-02458-3.
3. T. Tate and S. Zelditch, *Lattice path combinatorics and asymptotics of multiplicities of weights in tensor powers*, *J. Funct. Anal.* **217** (2004) 402–447; arXiv:math/0305251.
4. O. Postnova and N. Reshetikhin, *On multiplicities of irreducibles in large tensor product of representations of simple Lie algebras*, arXiv:1812.11236 (2018).
5. K. Coulembier, P. Etingof, V. Ostrik and D. Tubbenhauer, *Fractal behavior of tensor powers of the two dimensional space in prime characteristic*, arXiv:2405.16786 (2024), introduction on characteristic-zero \(\mathfrak{sl}_2\) tensor powers.
