# Rank-refined idempotents and a Gaussian law for Catalan-character block transformations

## Finding
For all integers \(d\ge1\) and \(k\ge0\), let \(M_{k,d}\) be the monoid of maps preserving a partition into \(k\) labeled blocks of common size \(d\), with a nondecreasing, regressive induced block transformation. The image-rank polynomial of its idempotents is
\[
E_{k,d}(z)=\sum_{\substack{f\in M_{k,d}\\f^2=f}}z^{|\operatorname{im}f|}.
\]
Its exact bivariate generating function is
\[
\boxed{\sum_{k\ge0}E_{k,d}(z)t^k=\left(1-\sum_{r=1}^{d}\binom dr\frac{r^{d-r}z^rt}{1-r^dt}\right)^{-1}.}
\]
Here \(E_{0,d}(z)=1\). Consequently the total number of idempotents \(a_{k,d}=E_{k,d}(1)\) has exponential growth \(a_{k,d}\sim\gamma_d\lambda_d^k\), with uniquely and explicitly specified constants below. For each fixed \(d\), the image rank of a uniformly chosen idempotent satisfies a nondegenerate Gaussian central limit law with explicit linear mean and variance.

## Assumptions and scope
Fix \(d\in\mathbb Z_{\ge1}\). For \(k\ge1\), let \(X\) be the disjoint union of nonempty labeled blocks \(B_1,\ldots,B_k\), each with \(d\) distinguishable elements. Every \(f\in M_{k,d}\) maps each entire block \(B_i\) into a single block \(B_{\chi_f(i)}\). Require the induced map \(\chi_f:[k]\to[k]\) to satisfy \(\chi_f(i)\le i\) and \(\chi_f(i)\le\chi_f(i+1)\) for all meaningful indices. These maps form the full transformation monoid over the classical Catalan monoid of block characters. The image rank \(|\operatorname{im}f|\) counts individual points, not image blocks, and is between \(1\) and \(kd\) for \(k>0\). At \(k=0\), the sole map is the empty identity and has rank zero.

Define
\[
Q_d(z,t)=\sum_{r=1}^d\binom dr\frac{r^{d-r}z^rt}{1-r^dt},\qquad W_{d,m}(z)=\sum_{r=1}^d\binom dr r^{dm-r}z^r\quad(m\ge1).
\]
For each \(d\), let \(\rho_d\) be the unique real root of \(Q_d(1,\rho_d)=1\) in \((0,d^{-d})\). Define \(\lambda_d=\rho_d^{-1}\) and \(\gamma_d=\bigl(\rho_d\partial_t Q_d(1,\rho_d)\bigr)^{-1}\). Define a probability law on integer pairs \((M,R)\in\mathbb Z_{\ge1}\times\{1,\ldots,d\}\) by
\[
\Pr(M=m,R=r)=\binom dr r^{dm-r}\rho_d^m.
\]
Its total mass is \(Q_d(1,\rho_d)=1\). Set
\[
\mu_d=\frac{\mathbb ER}{\mathbb EM},\qquad
\sigma_d^2=\frac{\mathbb E(R-\mu_dM)^2}{\mathbb EM}.
\]
Both constants are finite and strictly positive. If \(R_{k,d}\) denotes image rank of a uniformly sampled idempotent in \(M_{k,d}\), then as \(k\to\infty\) with \(d\) fixed,
\[
\mathbb ER_{k,d}=\mu_dk+O_d(1),\qquad
\operatorname{Var}(R_{k,d})=\sigma_d^2k+O_d(1),\qquad
\frac{R_{k,d}-\mu_dk}{\sigma_d\sqrt{k}}\ \Longrightarrow\ N(0,1).
\]

## Proof
**1. Fixed block characters.** If \(f^2=f\), then its character \(\chi=\chi_f\) satisfies \(\chi^2=\chi\). Let \(S=\operatorname{im}\chi\) be its set of fixed indices. Since \(\chi(1)\le1\), the index \(1\) belongs to \(S\). For each index \(i\), the value \(\chi(i)\in S\) does not exceed \(i\). If \(s\in S\) is the largest fixed index not exceeding \(i\), monotonicity also gives \(\chi(i)\ge\chi(s)=s\); hence \(\chi(i)=s\). Conversely, for every \(S\subseteq[k]\) containing \(1\), the predecessor projection \(\chi(i)=\max(S\cap[1,i])\) is an idempotent nondecreasing regressive map. Therefore such characters correspond bijectively to compositions \(k=m_1+\cdots+m_j\) into consecutive nonempty runs. The first index of each run is the fixed target index for its entire run.

**2. Independent choices on each run.** Consider a run of \(m\) blocks with its first block fixed by \(\chi\). An idempotent \(f\) must fix every point in its image. Choose \(r\ge1\) image points in the target block (\(\binom dr\) ways). Each of the other \(d-r\) points of the target block has \(r\) choices of image, and each point of the other \(m-1\) source blocks has \(r\) choices. The run therefore contributes exactly \(\binom dr r^{d-r+d(m-1)}=\binom dr r^{dm-r}\) idempotent restrictions of rank \(r\). These choices are exhaustive and unique: points in different runs cannot share an image because their target blocks differ. Thus the weighted run polynomial is \(W_{d,m}(z)\), and the complete rank polynomial is
\[
E_{k,d}(z)=\sum_{m=1}^k W_{d,m}(z)E_{k-m,d}(z)\quad(k\ge1),\qquad E_{0,d}(z)=1.
\]
The geometric identity \(\sum_{m\ge1}r^{dm-r}t^m=r^{d-r}t/(1-r^dt)\) and the sequence-of-runs decomposition give the displayed rational generating function as an identity of formal power series.

**3. Exponential count.** For \(0\le t<d^{-d}\), the function \(Q_d(1,t)\) is strictly increasing from zero to positive infinity (the summand \(r=d\) diverges at the endpoint). Hence \(\rho_d\) exists uniquely and is positive. Its root is simple since \(\partial_tQ_d(1,\rho_d)>0\). All coefficients of \(\sum_{m\ge1}W_{d,m}(1)t^m\) are strictly positive. For \(|t|<\rho_d\), the triangle inequality gives \(|Q_d(1,t)|<1\). For \(|t|=\rho_d\), equality \(Q_d(1,t)=1\) forces \(t=\rho_d\), as the first and second powers both occur with positive coefficients. Thus \(t=\rho_d\) is the unique singularity of smallest modulus in the rational generating function, a simple pole with principal part \(\gamma_d/(1-t/\rho_d)\). Standard partial fractions yield \(a_{k,d}=\gamma_d\lambda_d^k(1+O_d(\eta_d^k))\) for some \(0<\eta_d<1\), and \(\lambda_d>d^d\).

**4. Gaussian rank law.** For complex \(z\) sufficiently close to \(1\), the implicit-function theorem yields a unique analytic root \(\rho_d(z)\) close to \(\rho_d\) satisfying \(Q_d(z,\rho_d(z))=1\), with \(\rho_d(1)=\rho_d\). By continuity of the finitely many poles of the rational generating function, this is uniformly the only dominant simple pole near \(z=1\). Consequently, uniformly for \(z\) in a small complex neighborhood of \(1\),
\[
E_{k,d}(z)=\gamma_d(z)\rho_d(z)^{-k}(1+O_d(\eta^k)),\qquad
\gamma_d(z)=\bigl(\rho_d(z)\partial_tQ_d(z,\rho_d(z))\bigr)^{-1},
\]
where \(\gamma_d(z)\) is analytic and nonzero and \(0<\eta<1\). Thus the moment generating function of \(R_{k,d}\) has logarithm
\[
\log\mathbb Ee^{sR_{k,d}}=k\,u_d(s)+O_d(1),\quad u_d(s)=\log\frac{\rho_d}{\rho_d(e^s)},
\]
with analytic error uniformly near \(s=0\), and the bounded term has bounded derivatives. From
\[
1=Q_d(e^s,\rho_d(e^s))=\mathbb E\exp\bigl(sR-u_d(s)M\bigr)
\]
under the displayed probability law, successive derivatives at \(s=0\) yield \(u'_d(0)=\mu_d\) and \(u''_d(0)=\sigma_d^2\). Positivity of \(\sigma_d^2\) follows because both \((M,R)=(1,1)\) and \((M,R)=(2,1)\) have positive weight, so \(R-\mu_dM\) cannot vanish almost surely. Taylor expansion at \(s=iu/(\sigma_d\sqrt{k})\) gives convergence of characteristic functions to \(e^{-u^2/2}\); hence the claimed normal limit. Differentiating the same uniform asymptotic twice yields the mean and variance estimates.

## Verification
The accompanying standalone program `verify.py` computes rank polynomials in two independently implemented ways: exhaustive enumeration of all admissible block-character maps and point maps, and the weighted-composition recurrence. It checks every \(0\le k\le3\) and \(1\le d\le3\), plus \((k,d)=(2,4)\). It checks the explicit \((k,d)=(2,2)\) polynomial \(2z+8z^2+4z^3+z^4\), with total \(15\). Additional moment calculations for \(d=2\) confirm convergence of the normalized mean and variance to the implicit-root predictions; finite calculations are supplementary and not substituted for the general proof. For \(d=1\), the expression reduces to \(E_{k,1}(z)=z(1+z)^{k-1}\) for \(k\ge1\). For \(d=2\), \(\lambda_2=4+\sqrt3\), while \(E_{3,2}(1)=81\).

## Relationship to prior work
Sarkar and Singh (2023, Proposition 3.9) give an idempotency characterization in general semigroups of partition-preserving transformations with constrained block characters; the local criterion used in Step 2 is compatible with their theorem. Dolinka and East (2014/2016, Propositions 3.1–3.2) count idempotents of uniform-partition endomorphism monoids when the character is an **arbitrary** transformation, rather than an element of the Catalan monoid. Al-Aadhami (2017, Section 4.3) enumerates idempotents in general wreath products over the full transformation monoid. The Catalan predecessor characters are a different constrained family: their consecutive-run structure produces a rank-marked composition law, an explicit rational generating function, and a Gaussian rank law not supplied by the cited unrestricted formulas. Ayık, Ayık, and Koç (2011) study fixed-point statistics in the ordinary Catalan monoid, corresponding to the \(d=1\) boundary; no novelty is claimed for that known endpoint.

## Limitations
The statements concern uniformly sized **labeled** blocks, *full* transformations, and only nondecreasing regressive block characters; they do not classify idempotents for arbitrary nonuniform partitions, other order constraints, or arbitrary wreath products. The asymptotics hold for each **fixed** \(d\) as \(k\to\infty\); no uniform joint limit in \(d,k\) is asserted. The work is a self-contained derivation from known structural criteria; an earlier equivalent restricted-character enumeration could remain unlocated. Independent validation has not been performed.

## References
1. M. Sarkar and S. N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414v1 (2023), especially Proposition 3.9. https://arxiv.org/abs/2310.19414
2. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312 (first posted 2014; published *Communications in Algebra* 44 (2016)), especially Propositions 3.1–3.2. https://arxiv.org/abs/1407.3312
3. A. D. H. Al-Aadhami, *Combinatorial Questions for S wr T_n for a semigroup*, PhD thesis, University of York (2017), Section 4.3. https://etheses.whiterose.ac.uk/id/eprint/19494/
4. G. Ayık, H. Ayık, and M. Koç, *Combinatorial results for order-preserving and order-decreasing transformations*, *Turkish Journal of Mathematics* 35 (2011), 617–625. https://doi.org/10.3906/mat-1010-432
