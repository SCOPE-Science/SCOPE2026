# An affine-design transition for the sharp negative type of incidence metrics

## Finding

Let \(\mathscr D\) be an existing affine resolvable \(2\)-design \(\mathrm{AD}(n,\mu)\), with integers \(n\ge3\) and \(\mu\ge1\). Endow its point–block incidence graph \(G\) with shortest-path distance \(d\). Write \(\wp(G)\) for the supremal exponent \(p\ge0\) for which \(d^p\), with zero diagonal, is conditionally negative semidefinite on all real zero-sum vectors.

There is an exact dichotomy:

\[
\boxed{\displaystyle\wp(G)=
\begin{cases}
\log_2\!\left(\frac n{n-1}\right),&\mu=1,\\[3pt]
\text{the unique positive solution of }n\mu(3^p-1)^2=2^{3p},&\mu>1.
\end{cases}}
\]

For \(0\le p<\wp(G)\), the negative-type inequality is strict for all nonzero zero-sum coefficient vectors; at \(p=\wp(G)\) it is non-strict, and for every \(p>\wp(G)\) the inequality fails. Equivalently, the kernel \(\exp(-t d(x,y)^p)\) is positive semidefinite for every \(t>0\) precisely for \(0\le p\le\wp(G)\).

Define \(v=n^2\mu\), \(r=(v-1)/(n-1)\), and \(b=nr\). The nullity of the compressed powered-distance matrix on the zero-sum subspace at the critical exponent equals \(r-1\) if \(\mu=1\), but equals \(v-1\) for every \(\mu>1\). Accordingly the **least Euclidean dimension** in which \(d^{\wp(G)}\) can be represented as squared interpoint distances is \(v+b-r=2n^2-1\) for \(\mu=1\), and \(b\) for \(\mu>1\). The latter case constitutes a different, much larger endpoint nullspace.

Along any family of such designs with \(n\mu\to\infty\) and \(\mu>1\), the sharp exponent has the asymptotic
\[
\wp(G)\sim\frac{1}{(\log 3)\sqrt{n\mu}}.
\]
A concrete infinite example is the point–hyperplane incidence graph of \(\operatorname{AG}(m,q)\) for fixed prime power \(q\ge3\) and \(m\to\infty\), where \(n=q\) and \(\mu=q^{m-2}\).

## Assumptions and scope

An affine resolvable design is a \(2\)-\((v,k,\lambda)\) block design with a partition of its blocks into \(r\) parallel classes of \(n\) pairwise disjoint blocks covering all points, such that any two blocks from distinct classes intersect in exactly \(\mu\) points. Its necessary parameters are
\[
v=n^2\mu,\quad k=n\mu,\quad
\lambda=\frac{n\mu-1}{n-1},\quad
r=\frac{n^2\mu-1}{n-1},\quad b=nr=v+r-1.
\]
The theorem concerns only parameters for which such a design actually exists. The integer \(\lambda\) forces \(\mu\equiv1\pmod{n-1}\); therefore \(\mu>1\) entails \(\mu\ge n\). For distinct vertices in the incidence graph, \(d\) is \(1\) for incident point–block pairs, \(3\) for nonincident point–block pairs, \(2\) for distinct points or nonparallel blocks, and \(4\) for distinct parallel blocks. At \(p=0\), \(d^p\) is interpreted as one off the diagonal and zero on it.

## Proof

**1. Exact spectral decomposition.** Put \(s=n\mu\), \(a=2^p\), \(c=3^p\); let \(N\) be the \(v\)-by-\(b\) zero–one incidence matrix and \(P=I_r\otimes J_n\) the matrix marking pairs of blocks in the same parallel class. Standard design counting gives
\[
NN^{\mathsf T}=sI_v+\lambda J_v,\qquad
N^{\mathsf T}N=sI_b+\mu(J_b-P).
\]
The powered-distance matrix has exactly the block form
\[
D_p=\begin{pmatrix}
a(J_v-I_v)&cJ_{v,b}-(c-1)N\\
cJ_{b,v}-(c-1)N^{\mathsf T}&a(J_b-P)+a^2(P-I_b)
\end{pmatrix}.
\]
Because \(NN^{\mathsf T}\) is positive definite, \(N\) has full row rank. The block space splits orthogonally into the \((r-1)\)-dimensional kernel of \(N\) (vectors constant in each parallel class with total sum zero), the \((v-1)\)-dimensional \(N^{\mathsf T}\)-image of point-zero-sum vectors, and the block constants. Under compression to the full zero-sum subspace, \(D_p\) consequently has:

* \(r-1\) copies of the scalar \(\Lambda_{\mathrm{par}}=a((n-1)a-n)\);
* \(v-1\) copies of the symmetric two-by-two block
\[
M_p=\begin{pmatrix}-a&-\sqrt{s}(c-1)\\-\sqrt{s}(c-1)&-a^2\end{pmatrix};
\]
* one additional scalar \(\Lambda_{\mathrm{con}}=F(a,c)/(1+v/b)\), where
\[
F(a,c)=a(v-1)+\frac vb\big(a(b-n)+a^2(n-1)\big)-2s\big(1+(n-1)c\big).
\]
The last scalar is the Rayleigh quotient of the vector equal to one on all points and \(-v/b\) on all blocks, which spans the remaining zero-sum direction. These multiplicities add up to \(v+b-1\), so no spectral sectors are omitted.

**2. Excluding the constant-sector obstruction.** Define \(A=n/(n-1)\). For \(0\le p\le\log_2 A\), we have \(1\le a\le A\), and since \(\alpha=\log_2 3>3/2\),
\[
c=a^\alpha\ge1+\tfrac32(a-1).
\]
The function \(F\) strictly decreases with \(c\); thus it is bounded above by the quadratic \(F_*(a)=F(a,1+\tfrac32(a-1))\). This quadratic is strictly convex in \(a\), and its endpoint values simplify exactly to
\[
F_*(1)=-\frac{2ns-s-1}{ns-1}<0,\qquad
F_*(A)=-\frac{(n-3)s+n}{n-1}<0.
\]
Consequently \(\Lambda_{\mathrm{con}}<0\) throughout the entire range in which the parallel sector can be nonpositive.

**3. Competing thresholds.** The parallel scalar is nonpositive precisely for \(p\le p_{\mathrm{par}}=\log_2 A\). The two-by-two block has two negative diagonal entries and nonnegative determinant precisely when
\[
s(3^p-1)^2\le2^{3p}.
\]
The ratio \((3^p-1)/2^{3p/2}\) increases strictly from zero to infinity on \(p>0\): its logarithmic derivative is greater than \(\log3-\tfrac32\log2>0\). Hence there is a unique positive threshold \(p_{\mathrm{tr}}\) defined by equality. Steps 1–2 show \(\wp(G)=\min\{p_{\mathrm{par}},p_{\mathrm{tr}}\}\); beyond either threshold, its exhibited zero-sum sector has positive quadratic form.

**4. The sharp affine-design dichotomy.** The parameter integrality stated above says either \(\mu=1\) or \(\mu\ge n\). Let \(u=1/(n-1)\), so \(A=1+u\), and retain \(3/2<\alpha=\log_2 3<5/3\). At \(p=p_{\mathrm{par}}\), the ratio of the transversal determinant's adverse term to its positive term is
\[
R=\frac{n\mu(A^\alpha-1)^2}{A^3}.
\]
For \(\mu=1\) and \(n\ge4\), the mean-value bound \(A^\alpha-1<\alpha u A^{\alpha-1}\) yields \(R<\alpha^2u<25/27<1\). For \(n=3,\mu=1\), the inequalities \(\log_2(3/2)<3/5\) and \(3^{3/5}<2\) give \(R<3/(27/8)=8/9<1\). Thus the parallel mode reaches zero first for every affine plane.

For \(\mu>1\), we have \(\mu\ge n\). The lower mean-value estimate \(A^\alpha-1>\alpha u\) gives
\[
R\ge\frac{n^2(A^\alpha-1)^2}{A^3}>\frac{\alpha^2}{A}>1,
\]
using \(\alpha>3/2\) and \(A\le3/2\). Thus the two-by-two transversal mode reaches zero strictly before the parallel mode for every higher-index affine design. The two thresholds can never coincide for admissible parameters.

**5. Endpoint rank and asymptotics.** At the first threshold, exactly one of the two types of spectral sector vanishes: \(r-1\) parallel dimensions for \(\mu=1\), or the larger eigenvalue in each of the \(v-1\) transversal blocks for \(\mu>1\). The constant-sector eigenvalue remains strictly negative, proving the endpoint nullities and the least Euclidean squared-distance dimensions by double centering (Schoenberg's criterion). Finally, as \(s\to\infty\), the unique root of \(s(3^p-1)^2=2^{3p}\) tends to zero, and expansion of both sides yields \(s p^2(\log3)^2\to1\), establishing the stated asymptotic.

## Verification

A standalone numerical spectral crosscheck, `check_affine_incidence_negative_type.py`, builds incidence matrices independently from all points and hyperplanes of five finite affine geometries. It independently verifies the defining design Gram identities, all shortest-path distances by breadth-first search in four of those geometries, and the predicted **entire** compressed powered-distance spectrum at five exponent values per geometry including both sides of the sharp threshold. The run covers \(\mathrm{AG}(2,3)\), \(\mathrm{AG}(3,3)\), \(\mathrm{AG}(4,3)\), \(\mathrm{AG}(2,5)\), and \(\mathrm{AG}(3,5)\), with up to 280 incidence-graph vertices. It checks both critical-mode regimes and finishes with `AFFINE_RESOLVABLE_NEGATIVE_TYPE_SPECTRUM_OK`. The all-design theorem, its strict inequality, and the asymptotic are established by the algebraic argument above, not by numerical extrapolation. Python 3 and NumPy are required to execute the crosscheck.

## Relationship to prior work

Sánchez (2011) develops the general supremal-negative-type framework for finite metrics; his finite graph examples are not affine resolvable designs. Ma (2016) establishes the incidence-design parameters and the complete *ordinary* graph-distance spectrum at exponent \(p=1\); the spectral factors in Step 1 specialize to his ordinary-distance factors when \(a=2\), \(c=3\). In particular, the matrix identities and the decomposition underlying Ma's result are acknowledged prior work, not claimed as new here. His ordinary-distance characteristic polynomial does not state a sharp threshold over all real powered distances, the universal strict separation of the two critical modes for all admissible affine-design parameters, or the endpoint embedding dimensions. The affine-plane branch of the theorem is also independently known; the contribution is the higher-index \(\mu>1\) branch and the complete phase separation across all affine resolvable designs.

## Limitations

The theorem assumes a genuine affine resolvable \(2\)-design exists; it neither proves existence for every arithmetically admissible pair nor classifies such designs. The assertion about the Gaussian kernel concerns positivity simultaneously for all scales \(t>0\), not positivity at any individually chosen scale. The quantitative asymptotic is along existing families with \(\mu>1\). The proof is analytical; the finite numerical crosscheck is not a substitute. A mathematically equivalent historical treatment of powered-distance kernels in resolvable-design or distance-matrix literature remains possible. No independent mathematical validation is asserted.

## References

1. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first public version 2011-08-02, https://arxiv.org/abs/1108.0451.
2. Jianmin Ma, *The distance signatures of the incidence graphs of affine resolvable designs*, arXiv:1604.08922, first public version 2016-04-29, https://arxiv.org/abs/1604.08922.
