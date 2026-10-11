# Exact type-B conjugacy-class Fourier spectra and tight sampling classification

## Finding
For every integer \(n\ge3\) and every conjugacy class \(C\) of the signed-permutation group \(B_n=C_2^n\rtimes S_n\), restriction to \(C\) of the complete Fourier block for the natural \(n\)-dimensional reflection representation has a four-sector, explicitly computable spectrum. The spectral data depend, after division by class density, only on the signed one-cycle and signed two-cycle counts. This yields necessary and sufficient conditions for injective restriction and for exactly tight sampling.

Write \(f_+,f_-\) for the numbers of positive and negative signed one-cycles and \(t_+,t_-\) for the numbers of positive and negative signed two-cycles. The sign of a signed cycle is the product of the signs on that cycle. Put
\[
f=f_++f_-,\qquad s=f_+-f_-,\qquad \tau=t_+-t_-,\qquad w=\frac{|C|}{2^n n!}.
\]
The entire spectrum, with multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
w s^2&1\\
w\dfrac{nf-s^2}{n-1}&n-1\\
w\dfrac{n-f+2\tau}{n-1}&\binom n2\\
w\dfrac{n-f-2\tau}{n-1}&\binom n2
\end{array}.
\]
Zero eigenvalues are included and multiplicities of coincident eigenvalues are added.

**Exact tightness classification.** The restriction frame is tight on the whole Fourier block, i.e. its concentration operator is a positive scalar identity, **if and only if**
\[
\boxed{f=1\quad\text{and}\quad t_+=t_-.}
\]
In every such case the operator is precisely \(wI\): its optimal reconstruction condition number is one. In particular, for every \(n\ge4\), any signed cycle type consisting of one signed one-cycle and one signed \((n-1)\)-cycle yields a tight full-rank class-sampling frame. There are no tight conjugacy classes when \(n=3\).

**Exact injectivity classification.** Restriction is injective on the entire Fourier block if and only if \(s\ne0\) and either the cycle type contains a cycle of length at least three, or both \(t_+>0\) and \(t_->0\). All four eigenvalues are strictly positive exactly in this situation. For such a class the optimal norm condition number is the square root of the largest divided by the smallest of the four positive displayed eigenvalues.

## Assumptions and scope
Let \(G=B_n\), realized as all signed \(n\times n\) permutation matrices, with \(|G|=2^n n!\). Give \(L^2(G)\) the normalized inner product \(\langle u,v\rangle=|G|^{-1}\sum_{g\in G}u(g)\overline{v(g)}\). Let \(\rho:G\longrightarrow O(n)\) be the natural reflection representation, and let \(H\) be the span of its \(n^2\) complex matrix-coefficient functions. The representation \(\rho\) is complex irreducible, so \(\dim H=n^2\). Define \(P_H\) to be the orthogonal projection in \(L^2(G)\) onto \(H\), and set
\[
K_C=P_HM_{\mathbf1_C}P_H\big|_H,
\]
where \(M_{\mathbf1_C}\) is multiplication by the class indicator. No symmetry or parity restriction is placed on the signed cycle type. The operator is positive semidefinite, with eigenvalues in \([0,1]\). The theorem concerns a **single conjugacy class**, not an arbitrary union of classes, not the ordinary permutation representation of \(S_n\), and not the full regular Fourier transform.

## Proof
**1. Isometric transfer to matrices.** The signed coordinate subgroup acts on \(\mathbb C^n\) with distinct coordinate weights and the permutation subgroup permutes them transitively; hence \(\rho\) is irreducible. Schur orthogonality gives the complex-linear isometry \(\mathcal F:\operatorname{Mat}_n(\mathbb C)\to H\):
\[
\mathcal F(A)(g)=\sqrt n\sum_{i,j=1}^n A_{ij}\rho(g)_{ij},\qquad
\|\mathcal F(A)\|_{L^2(G)}=\|A\|_F.
\]
Consequently, under this isometry \(K_C\) is the class-orbit frame operator
\[
\mathcal S_C(A)=\frac{n}{|G|}\sum_{U\in C}\left(\sum_{i,j}A_{ij}U_{ij}\right)U.
\]
This fixes the normalization, including the factor \(n\) and the class density \(w\).

**2. Four irreducible conjugation sectors.** Conjugation by signed permutations on matrices preserves the mutually orthogonal spaces
\[
V_0=\mathbb CI,\qquad V_D=\{\text{traceless diagonal matrices}\},
\]
\[
V_S=\{A:A^\mathsf T=A,\ A_{ii}=0\},\qquad
V_A=\{A:A^\mathsf T=-A\}.
\]
Their dimensions are \(1,n-1,\binom n2,\binom n2\). The diagonal traceless sector is the standard irreducible \(S_n\)-module. On off-diagonal entries the normal signed subgroup acts with distinct characters \(\varepsilon_i\varepsilon_j\), indexed by unordered pairs \(\{i,j\}\); the transitive permutation action forces each of \(V_S,V_A\) to be irreducible. A stabilizer transposition interchanges \(i,j\) and acts with opposite signs on their symmetric and skew generators, proving inequivalence of \(V_S,V_A\). Their normal-subgroup weights distinguish both from the diagonal sectors. The decomposition is therefore multiplicity-free for all \(n\ge3\).

Because \(C\) is a conjugacy orbit, \(\mathcal S_C\) commutes with conjugation. By Schur's lemma its scalar on \(V_j\), with \(d_j=\dim V_j\), is
\[
\mu_j=\frac{n|C|}{|G|}\frac{\|P_{V_j}U\|_F^2}{d_j},\qquad U\in C.
\]
Indeed, the trace on \(V_j\) of the rank-one operator \(A\mapsto(\sum A_{ab}U_{ab})U\) equals \(\|P_{V_j}U\|_F^2\), while that projection norm is constant across the conjugacy orbit.

**3. Projection energies from short signed cycles.** The diagonal of a signed permutation matrix \(U\) consists of \(f_+\) entries \(+1\), \(f_-\) entries \(-1\), and zeros elsewhere. Its trace is \(s\), so
\[
\|P_{V_0}U\|_F^2=\frac{s^2}{n},\qquad
\|P_{V_D}U\|_F^2=f-\frac{s^2}{n}.
\]
Writing \(U_\mathrm{off}\) for the matrix with diagonal removed, its squared Frobenius norm is \(n-f\). Furthermore,
\[
\sum_{i\ne j}(U_\mathrm{off})_{ij}(U_\mathrm{off})_{ji}=2\tau.
\]
Only two-cycles contribute to this sum, and the two nonzero entries of a signed two-cycle have product equal to its cycle sign. Splitting into symmetric and skew parts therefore gives
\[
\|P_{V_S}U\|_F^2=\frac{n-f}{2}+\tau,\qquad
\|P_{V_A}U\|_F^2=\frac{n-f}{2}-\tau.
\]
These four energies sum to \(n=\|U\|_F^2\). Substituting the dimensions in the Schur formula and writing \(w=|C|/|G|\) proves exactly the four claimed eigenvalues and multiplicities. This argument also proves their nonnegativity; equivalently \(n-f\ge2|\tau|\).

**4. Exact tightness and rank.** The trace of \(K_C\) is \(n^2w\), so if it is scalar it must equal \(wI\). The scalar-sector equation forces \(s^2=1\); the diagonal-traceless equation then forces \(nf-s^2=n-1\), so \(f=1\). The two off-diagonal equations now both equal one precisely when \(\tau=0\). Conversely, \(f=1,\tau=0\) implies \(|s|=1\) and every displayed normalized eigenvalue equals one. With \(n=3\), the two nonfixed coordinates form a single signed two-cycle, forcing \(|\tau|=1\), and tightness is impossible. For \(n\ge4\), the signed \((n-1)\)-cycle witness has \(f=1,\tau=0\), proving existence in every rank.

The scalar sector vanishes exactly when \(s=0\). If \(s\ne0\), then the diagonal-traceless sector is strictly positive: \(nf-s^2\ge f(n-f)\), with strict positivity if \(f<n\). Both off-diagonal sectors are strictly positive precisely when \(n-f>2|\tau|\). Decomposing nonfixed coordinates into signed two-cycles and cycles of lengths at least three shows that this inequality holds exactly when there is at least one cycle of length at least three, or there are two-cycles of both signs. This proves the injectivity classification, and strict spectral positivity gives the stated optimal singular-value condition number.

## Verification
A standalone standard-library Python checker, `artifacts/verify.py`, constructs all signed permutation matrices and partitions them by their signed cycle type for \(n=3,4,5\). For **every** conjugacy class it forms the full integer class-orbit operator and checks its action on an explicit basis of all \(n^2\) matrix directions against the four predicted scalar eigenvalues, using exact rational arithmetic. It also checks tightness and injectivity characterizations and verifies the group and class cardinalities.

The replay reports \(10\), \(20\), and \(36\) signed conjugacy classes respectively; all \(66\) complete class operators pass, with no floating-point tolerances. The exhaustive finite tests are not a proof for arbitrary \(n\); the representation-theoretic and signed-cycle identities above provide the all-rank proof.

## Relationship to prior work
Thill and Hassibi (arXiv:1509.05087 and arXiv:1509.05739) establish group-frame constructions, tight-frame criteria, and general finite-group Fourier machinery. The latter explicitly discusses conjugacy classes for control of inner-product multiplicities, but not the restriction spectrum of the natural signed-permutation Fourier block. Cherniavsky and Sklarz (arXiv:math/0411554) analyze matrix similarity and conjugacy preservation for natural and other representations of the **unsigned** symmetric group, rather than class-selected Fourier concentration for \(B_n\). These are substantial precedents for the framework, not the four signed-cycle eigenvalues, full-rank condition, or exactly tight class classification stated here. Generic Schur orbit averaging is standard and is used, not claimed as new.

## Limitations
The result is confined to one conjugacy class in the natural reflection block of \(B_n\) and to \(n\ge3\). It does not classify multi-class sampling or other irreducible blocks. The finite checker covers ranks three through five only. General group orbit-frame identities make related formulations plausible in older representation-theoretic or coding literature; the absence of an exact match in the examined sources is not exhaustive priority certification. No independent mathematical audit or external proof certification is claimed.

## References
- Y. Cherniavsky and M. Sklarz, *Conjugacy in Permutation Representations of the Symmetric Group*, arXiv:math/0411554, first public version dated 2004-11-24.
- M. Thill and B. Hassibi, *Group Frames with Few Distinct Inner Products and Low Coherence*, arXiv:1509.05087, first public version dated 2015-09-17.
- M. Thill and B. Hassibi, *Low-Coherence Frames from Group Fourier Matrices*, arXiv:1509.05739, first public version dated 2015-09-18.
- A. Ram, *The Hyperoctahedral Group*, representation-theoretic notes at https://math.soimeme.org/~arunram/Notes/hyperoctahedral.html (undated; not used to establish the literature anchor).
