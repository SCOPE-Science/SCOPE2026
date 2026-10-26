# Rank strata and individual-product fibers of square-zero products of finite-field idempotents

## Finding

Let \(\mathbb F_q\) be a finite field and \(n\ge0\). For ordered matrices \(E,F\in M_n(\mathbb F_q)\) satisfying \(E^2=E\), \(F^2=F\), and \((EF)^2=0\), write \(r=\operatorname{rank}E\), \(s=\operatorname{rank}F\), and \(b=\operatorname{rank}(EF)\). The complete three-rank distribution is

\[
P_{n,q}(r,s,b)={n\brack r}_q q^{r(n-r)}{n-r\brack s}_q{r\brack b}_q\left(\prod_{i=0}^{b-1}(q^s-q^i)\right)q^{s(n-s)-b^2}.
\]

It is positive precisely for \(0\le r\le n\), \(0\le s\le n-r\), and \(0\le b\le\min(r,s)\), and is zero otherwise. In particular, the product may be a nonzero square-zero matrix, which is **not** an idempotent product.

More precisely, fix any matrix \(H\in M_n(\mathbb F_q)\) satisfying \(H^2=0\) and \(\operatorname{rank}H=b\). The exact number of these pairs with the given individual product \(EF=H\) and factor ranks \((r,s)\) is

\[
\frac{P_{n,q}(r,s,b)}{{n\brack b}_q{n-b\brack b}_q\lvert\mathrm{GL}_b(\mathbb F_q)\rvert}.
\]

Both formulas hold for every prime-power field order, including nonprime fields, and in every allowed dimension. They include the zero product and zero-dimensional boundary without exceptions.

## Assumptions and scope

A matrix is idempotent when its square equals itself. A matrix is square-zero when its square is zero. All matrices act on a labeled \(n\)-dimensional vector space over \(\mathbb F_q\); pairs are ordered, and no commutativity is assumed. The Gaussian coefficient \({m\brack j}_q\) counts \(j\)-subspaces of an \(m\)-dimensional vector space, with value zero outside \(0\le j\le m\). Empty products are one and \(\mathrm{GL}_0\) has order one. The matrix product uses ordinary composition, with \(F\) applied first. The output counts labeled matrices, not simultaneous-conjugacy classes.

## Proof

**1. Fixing the first factor.** Fix an idempotent \(E\) of rank \(r\). Then \(V=R\oplus K\), where \(R=\operatorname{im}E\), \(K=\ker E\), and \(E\) is projection onto \(R\). Every rank-\(s\) idempotent \(F\) is uniquely specified by its image \(U\subseteq V\), \(\dim U=s\), and a retraction \(p:V\to U\) with \(p|_U=\operatorname{id}_U\), followed by the inclusion of \(U\) in \(V\).

**2. Transversality.** If \((EF)^2=0\), then \(U\cap R=0\): indeed, any nonzero \(v\in U\cap R\) would satisfy \(EFv=v\), contradicting nilpotence of \(EF\). Consequently, projection of \(U\) onto \(K\) is injective. It identifies \(U\) with the graph of a unique linear map \(\phi:H_0\to R\), where \(H_0\subseteq K\) has dimension \(s\). Thus necessarily \(s\le n-r\). Moreover, \(\operatorname{rank}(EF)=\operatorname{rank}(E|_U)=\operatorname{rank}\phi=b\).

Choose \(H_0\) in \({n-r\brack s}_q\) ways. Choose the image \(T=\operatorname{im}\phi\subseteq R\) of dimension \(b\) in \({r\brack b}_q\) ways. For this target, choose a surjection \(H_0\twoheadrightarrow T\) in \(\prod_{i=0}^{b-1}(q^s-q^i)\) ways. This accounts for every transverse \(U\) exactly once.

**3. The square-zero constraint on the retraction.** Since \(p(V)=U\), the image of \(EF=E p\) equals \(T\), and hence \((EF)^2=0\) is equivalent to \(E p(T)=0\). Because \(p(T)\subseteq U\), this is precisely \(p(T)\subseteq U\cap K\). The latter space has dimension \(s-b\), the kernel dimension of \(E|_U\). Furthermore \(U\cap T=0\), so \(U\oplus T\) is direct. The retraction is prescribed on \(U\), may send \(T\) arbitrarily into the \((s-b)\)-dimensional space \(U\cap K\), and is arbitrary from a complementary \((n-s-b)\)-space into \(U\). The number of choices is therefore

\[
q^{b(s-b)}q^{s(n-s-b)}=q^{s(n-s)-b^2}.
\]

These constructions are reversible: a pair gives \(U,H_0,\phi,T,p\), and every such datum gives a pair of the required ranks. Finally, the number of rank-\(r\) idempotents \(E\) is \({n\brack r}_q q^{r(n-r)}\), by choosing their image and then a complementary kernel. Multiplication gives the claimed distribution. For any feasible \((r,s,b)\), every displayed factor is strictly positive, showing sufficiency of the bounds. The formula also handles \(r=0\), \(s=0\), \(b=0\), and \(n=0\) with the empty-product conventions.

**4. Individual-product fibers.** Conjugation by \(\mathrm{GL}_n(\mathbb F_q)\) preserves idempotence, the three ranks, and the equation \(EF=H\). All square-zero matrices of a fixed rank \(b\) are conjugate, each having Jordan type consisting of \(b\) blocks of size two and \(n-2b\) blocks of size one. Their number is

\[
S_{n,q}(b)={n\brack b}_q{n-b\brack b}_q\lvert\mathrm{GL}_b(\mathbb F_q)\rvert:
\]

choose the \(b\)-dimensional image, then an \((n-b)\)-dimensional kernel containing that image, and finally an isomorphism from the quotient by the kernel to the image. Equal-sized conjugation fibers partition the rank-stratified pair count, proving the individual-matrix formula (and its integrality) without an extra assumption.

## Verification

Run the embedded standalone `verify.py` with standard Python. The implementation independently enumerates actual idempotent matrices and multiplies them in small prime fields. Fixed-first-factor exhaustive rank cells yielded `VERIFY_OK_IDEMPOTENT_SQUARE_ZERO_PRODUCT 342`. A different exhaustive loop over all ordered idempotent pairs and each actual square-zero target yielded `VERIFY_OK_IDEMPOTENT_SQUARE_ZERO_FIBERS 2378`. Tested pairs include \((n,q)=(4,2),(3,3),(2,5)\). For \((n,q)=(3,2)\), there are \(675\) pairs with zero product and \(504\) with nonzero square-zero product. The finite tests check examples only; the proof above establishes every dimension and prime power.

## Relationship to prior work

Botha's study of idempotent factorization (1996 print, verifiable online publication dated 1 April 2008) establishes existence of matrix factorizations with prescribed nullities. Botha's later paper on products involving idempotent and square-zero factors addresses factorability and allowable factor ranks. Hattingh's freely accessible 2019 preprint gives related criteria for products of singular quadratic matrices. These existence-level statements do not by themselves provide the present full finite-field multiplicities by three simultaneous ranks, nor the number of factorizations of each particular square-zero matrix. Ferraz, Polcino Milies and Taufer enumerate idempotent generators of left ideals, without imposing the present two-factor product equation.

The related established distribution for pairs of idempotent matrices whose product is **idempotent** concerns a different condition: a matrix that is simultaneously idempotent and square-zero is zero. Thus that result can only intersect the present theorem in the zero-product stratum; it cannot imply counts for nonzero square-zero targets without new arguments.

## Limitations

The result is a labeled finite-field enumeration, not a classification of simultaneous-conjugacy orbits, higher nilpotency indices, longer products, or arbitrary finite rings. Full texts of some historically plausible factorization papers were unavailable; historical priority remains an explicit risk despite checked abstracts, inspected accessible primary research, and comparison of the actual statements. The independent mathematical audit has not been performed.

## References

1. J. D. Botha, *Idempotent factorization of matrices*, Linear and Multilinear Algebra 40 (1996), 365–371. Publisher's recorded public online date: 2008-04-01. DOI: 10.1080/03081089608818452.
2. J. D. Botha, *Products of idempotent and square-zero matrices*, Linear Algebra and its Applications 497 (2016), 116–133. DOI: 10.1016/j.laa.2016.02.026.
3. C. J. Hattingh, *A note on products of quadratic matrices of singular type*, arXiv:1902.03584 (2019), freely accessible full text.
4. R. A. Ferraz, C. Polcino Milies, and E. Taufer, *Left ideals in matrix rings over finite fields*, arXiv:1711.09289 (2017), freely accessible full text.
