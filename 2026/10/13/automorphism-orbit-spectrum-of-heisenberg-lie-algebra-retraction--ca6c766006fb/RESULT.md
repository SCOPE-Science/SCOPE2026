# Automorphism-orbit spectrum of Heisenberg Lie algebra retractions over finite fields

## Finding
Let \(H_m\) be the \((2m+1)\)-dimensional Heisenberg Lie algebra over \(\mathbb F_q\). The full Lie automorphism group has exactly
\[
1+\sum_{r=0}^{m}\left(\left\lfloor\frac r2\right\rfloor+1\right)
\]
orbits on the set of idempotent Lie algebra endomorphisms \(F^2=F\). The identity forms a singleton orbit. Each remaining orbit has a unique pair of indices \((r,s)\), \(0\le r\le m\), \(0\le s\le\lfloor r/2\rfloor\), and size
\[
B_{m,r,s}(q)=I_{m,r}(q)q^{r+2r(m-r)+r(r+1)/2}{r\brack2s}_q\frac{|\mathrm{GL}_{2s}(\mathbb F_q)|}{|\mathrm{Sp}_{2s}(\mathbb F_q)|},
\qquad I_{m,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2(m-j)}-1}{q^{r-j}-1}.
\]
Empty products and the order ratio for zero-dimensional classical groups are one. In particular, the exact total number of idempotent Lie endomorphisms is
\[
1+\sum_{r=0}^{m} I_{m,r}(q)q^{r(2m-r+1)}.
\]
All statements include characteristic two and all finite extension fields.

## Assumptions and scope
Fix a prime power \(q\), \(k=\mathbb F_q\), and integer \(m\ge1\). Let \(V\) be a \(2m\)-dimensional vector space with a fixed nondegenerate alternating form \(\omega:V\times V\to k\). Define \(H_m=V\oplus kz\) with \([v,w]=\omega(v,w)z\) and \([z,H_m]=0\). An idempotent Lie endomorphism is a \(k\)-linear Lie algebra homomorphism \(F:H_m\to H_m\) satisfying \(F\circ F=F\). Equivalence means conjugacy \(F\sim gFg^{-1}\) under the *full* \(k\)-linear Lie automorphism group.

For \(0\le r\le m\), \(I_{m,r}(q)\) is the number of totally isotropic \(r\)-dimensional subspaces of \(V\). For \(0\le 2s\le r\), the Gaussian binomial \({r\brack2s}_q\) counts \((2s)\)-dimensional quotient choices. The classical group orders mean the usual groups over \(\mathbb F_q\); in dimension zero both orders are one. Each orbit \((r,s)\) has representatives \(F(z)=0\), \(F(v)=Av\), where \(A\) projects onto an isotropic \(r\)-space \(W\) along a complementary subspace \(K\), and
\[
\operatorname{rank}(\omega|_K)=2(m-r+s).
\]
The group \(\operatorname{GSp}(V,\omega)\) and the automorphism shears act on these endomorphisms as detailed below.

## Proof
**1. Reduction to isotropic projections.** Write a Lie endomorphism as \(F(v)=Av+f(v)z\), \(F(z)=\lambda z\); the second equation is forced because \(z=[u,v]\) for suitable \(u,v\). Preservation of the bracket is equivalent to \(\omega(Au,Av)=\lambda\omega(u,v)\) for every \(u,v\). Idempotence is exactly
\[
A^2=A,\qquad \lambda^2=\lambda,\qquad fA+\lambda f=f.
\]
Over a field, \(\lambda\in\{0,1\}\). If \(\lambda=1\), nondegeneracy makes \(A\) invertible; hence \(A=I\), and the last equation forces \(f=0\). This is the identity. If \(\lambda=0\), \(A\) is a projection whose image \(W\) is totally isotropic, and \(fA=f\). Its complementary kernel \(K\) has dimension \(2m-r\), and \(f\) is an arbitrary linear functional of the \(r\)-dimensional image.

**2. Eliminating the central coordinate.** Every automorphism acts as \(g(v)=Pv+h(v)z\), \(g(z)=cz\), where \(c\ne0\) and \(P\in\operatorname{GSp}(V,\omega)\) has multiplier \(c\); conversely these data define an automorphism. Conjugating \(F\) by a central shear \(g(v)=v+h(v)z\) changes \(f\) by \(hA\). Since \(fA=f\), choosing \(h=-f\) removes \(f\). Therefore the problem reduces exactly to \(\operatorname{Sp}(V,\omega)\)-orbits of ordered decompositions \(V=W\oplus K\) with \(W\) totally isotropic. Scalar conformal multipliers do not further merge the rank types proved below.

**3. Classification of complementary pairs.** The subspace \(E=K\cap W^\perp\) has dimension \(2(m-r)\). Since \(W^\perp=W\oplus E\), its restricted form is nondegenerate. Thus \(V=E\perp E^\perp\); after projecting \(K\) orthogonally to \(E\), its remaining \(r\)-space \(Y\subseteq E^\perp\) complements \(W\), which is a Lagrangian in the symplectic \(2r\)-space \(E^\perp\). The pairing \(W\times Y\to k\) is perfect. In dual bases, the restriction of \(\omega\) to \(Y\) is an alternating matrix, and changing bases in \(W\) acts by matrix congruence. Alternating forms over *any* field, including characteristic two, have canonical rank \(2s\). The symplectic group is transitive on the corresponding pairs because a prescribed perfect cross-pairing and alternating \(Y\)-form uniquely determine a symplectic basis up to isometry. Consequently \(r\) and \(s\) are complete invariants, each \(0\le 2s\le r\) occurs, and \(\operatorname{rank}(\omega|_K)=2(m-r)+2s\).

**4. Counting each orbit.** The isotropic-image count is the standard symplectic Grassmannian formula \(I_{m,r}(q)\) above, obtained by counting ordered isotropic independent sequences and dividing by ordered bases of an \(r\)-space. Fix one such \(W\), and fix a symplectic Witt decomposition \(V=W\oplus U\oplus W^*\), where \(\dim U=2(m-r)\). Every complement \(K\) of \(W\) is uniquely a graph of a linear map \(U\oplus W^*\to W\). Its \(U\)-component has \(q^{2r(m-r)}\) possibilities. For each such component the induced alternating form on the quotient complementary \(r\)-space is the skew part of an \(r\times r\) matrix, plus a fixed alternating offset. The map from matrices to alternating forms \(D\mapsto D-D^T\) is surjective over **every** field, including characteristic two, with kernel dimension \(r(r+1)/2\). Hence each alternating form occurs \(q^{2r(m-r)+r(r+1)/2}\) times. The number of alternating forms on an \(r\)-space with rank exactly \(2s\) is
\[
N_{r,s}(q)={r\brack2s}_q\frac{|\mathrm{GL}_{2s}(\mathbb F_q)|}{|\mathrm{Sp}_{2s}(\mathbb F_q)|}.
\]
Indeed, choose the radical of dimension \(r-2s\), then a nondegenerate alternating form on the quotient, whose \(\mathrm{GL}_{2s}\)-orbit has stabilizer \(\mathrm{Sp}_{2s}\). Finally, each projection \(A\) admits exactly \(q^r\) compatible central functionals \(f\). Multiplying proves the asserted orbit size. Because \((r,s)\) already labels exactly one orbit, this enumeration is the orbit size, not merely a stratum count.

**5. Completeness and total.** The pair classification yields \(\lfloor r/2\rfloor+1\) orbits for each rank \(r\), plus identity. For each fixed \(W\), the number of complements is \(q^{r(2m-r)}\) and the number of compatible \(f\) is \(q^r\). Summing directly gives the total \(1+\sum_{r=0}^m I_{m,r}(q)q^{r(2m-r+1)}\). This independently agrees with summing the \(B_{m,r,s}(q)\) over \(s\), since every alternating matrix has some even rank.

## Verification
The accompanying standalone Python program `verify_retracts.py` uses exact modular arithmetic, enumerates all isotropic images and complementary kernels for \((m,q)=(1,2),(2,2),(2,3)\), and independently enumerates all projection matrices, central functionals, and orbits under symplectic transvections and central shears for \((m,q)=(2,2)\). The latter has four nonidentity orbits with sizes \(1,240,480,480\), plus singleton identity. Run `python3 verify_retracts.py`; the successful terminator is `VERIFY_OK`. Finite computations check special instances only; the preceding argument establishes the theorem in arbitrary dimension and finite characteristic.

## Relationship to prior work
The Heisenberg Lie algebra and its symplectic quotient are classical. Rojas's 2012 work concerns minimal faithful representations, not endomorphism-retraction orbit sizes. Lorand and Weinstein's 2015 classification concerns *two isotropic subspaces*, whereas here only \(W\) is required isotropic and \(K\) generally is not. Sergeichuk's 1990 canonical-form theory studies general pairs of subspaces in spaces with scalar products (in characteristic not two): its geometric methods are a substantial antecedent and may recover the underlying rank classification in odd characteristic. The present scope is specifically the complete finite-field Heisenberg idempotent Lie **endomorphism** census, including central-functional fibers and exact orbit multiplicities in characteristic two as well as odd characteristics. Related results on automorphism fixed points and subalgebra commutativity do not determine this census. This comparison does not establish exhaustive priority over unpublished or differently named results.

## Limitations
Only idempotent Lie algebra endomorphisms, not all endomorphisms or all associative-algebra retractions, are classified. The formulas count orbits over finite fields, not group-scheme orbit strata over arbitrary bases. The finite verifier covers three small parameters and direct conjugacy only in one; it is not an infinite proof. Equivalence with an unlocated specialized retraction classification remains a bibliographic risk. No independent scientific audit is asserted.

## References
1. M. A. Rojas, *Minimal Faithful Representation of the Heisenberg Lie Algebra with Abelian Factor*, arXiv:1206.5867, first posted 2012-06-26. Available at https://arxiv.org/abs/1206.5867 .
2. A. Lorand and A. Weinstein, *(Co)isotropic Pairs in Poisson and Presymplectic Vector Spaces*, arXiv:1503.00169, first posted 2015-02-28. Available at https://arxiv.org/abs/1503.00169 .
3. V. V. Sergeichuk, *Classification of pairs of subspaces in scalar product spaces*, 1990; lawful author-hosted full text at https://www.imath.kiev.ua/~sergeich/sergeichuk_files/pairs.of.subsp.pdf .
