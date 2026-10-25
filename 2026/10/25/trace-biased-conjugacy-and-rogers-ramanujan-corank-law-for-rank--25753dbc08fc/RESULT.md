# Trace-biased conjugacy and Rogers–Ramanujan corank law for rank-one averaging projections

## Finding

Let \(k\) be a field and \(n\geq1\). Consider rank-one \(k\)-linear maps \(P:M_n(k)\to M_n(k)\) satisfying \(P^2=P\) and both averaging identities
\[
P(X)P(Y)=P(XP(Y))=P(P(X)Y)\quad\text{for all }X,Y\in M_n(k).
\]
**One classification and enumeration theorem** gives the following equivalent coordinates, geometry, finite-field orbit counts, and corank limit.

**Canonical coordinates.** There is a unique pair \((E,C)\) such that
\[
P(X)=\operatorname{tr}(CX)E,\quad E^2=E\ne0,\quad EC=CE=C,\quad \operatorname{tr}C=1.
\]
In particular, \(E=P(I_n)\), an intrinsic idempotent of rank \(r\in\{1,\ldots,n\}\).

**Geometry and exact finite-field count.** The locus with \(\operatorname{rank}E=r\) is a smooth irreducible affine-hyperplane bundle over the variety of rank-\(r\) idempotent matrices, of dimension \(2r(n-r)+r^2-1=2nr-r^2-1\). For the full rank-one idempotent averaging-operator variety, these \(n\) disjoint strata are its connected and irreducible components. Over \(\mathbb F_q\), for every prime power \(q\),
\[
\#\{P:\operatorname{rank}P(I_n)=r\}={n\brack r}_q\,q^{nr-1},
\qquad
\#\{P\}=\sum_{r=1}^n{n\brack r}_q\,q^{nr-1}.
\]
Here \({n\brack r}_q\) is the Gaussian binomial coefficient; \(P\) always has **operator rank one** even though the matrix \(P(I_n)\) has rank \(r\).

**Conjugacy classes and a characteristic-sensitive trace law.** Under conjugation by \(\mathrm{GL}_n(\mathbb F_q)\), the component with \(\operatorname{rank}E=r\) has orbits indexed by similarity classes of \(r\times r\) matrices of trace one. Put \(K_q(0)=1\) and define \(K_q(m)\) by
\[
\sum_{m\geq0}K_q(m)z^m=\prod_{j\geq1}(1-qz^j)^{-1}.
\]
Writing \(p=\operatorname{char}\mathbb F_q\), its number of orbits is exactly
\[
\boxed{\mathcal O_{q,r}=
\frac{K_q(r)-\mathbf1_{p\mid r}K_q(r/p)}q.}
\]
The full dimension-generating series, in which the coefficient of \(z^n\) counts orbits for \(M_n(\mathbb F_q)\), is
\[
\boxed{\sum_{n\geq0}\#(\mathrm{GL}_n\backslash\mathcal P_n(\mathbb F_q))z^n=
\frac{K_q(z)-K_q(z^p)}{q(1-z)}},\quad
K_q(z)=\prod_{j\geq1}(1-qz^j)^{-1}.
\]
Set \(\mathcal P_0=\varnothing\), so the constant coefficient is zero.

**Asymptotic corank law.** Fix \(q\). Among uniformly chosen rank-one idempotent averaging operators over \(\mathbb F_q\), the corank \(j=n-\operatorname{rank}P(I_n)\) converges in distribution as \(n\to\infty\). With \(t=q^{-1}\), its limiting mass is
\[
\boxed{\Pr(j)=\frac{t^{j^2}/\prod_{i=1}^j(1-t^i)}
{\displaystyle\prod_{h\geq0}[(1-t^{5h+1})(1-t^{5h+4})]^{-1}}},
\qquad j=0,1,\ldots.
\]
The denominator is the classical first Rogers–Ramanujan product. In particular,
\[
\lim_{n\to\infty}q^{1-n^2}\#\mathcal P_n(\mathbb F_q)
=\sum_{j\geq0}\frac{t^{j^2}}{\prod_{i=1}^j(1-t^i)}
=\prod_{h\geq0}\frac1{(1-t^{5h+1})(1-t^{5h+4})}.
\]

## Assumptions and scope

All fields are allowed for the canonical classification and geometric components. Finite-field counts and conjugacy formulas hold for every prime power \(q\), including extension fields and characteristics dividing \(r\). The limit fixes \(q\) and lets \(n\) tend to infinity. The phrase averaging operator always requires **both** noncommutative averaging identities above; merely requiring one identity is a different problem. The spaces considered are rank-*one linear maps on the full matrix algebra*, not rank-one matrices or general (possibly non-idempotent) averaging maps. The algebraic-variety statements concern geometric reduced loci.

## Proof

**1. Rank-one normalization.** Write \(P(X)=\varphi(X)B\), with \(B\ne0\), \(\varphi\ne0\). The relation \(P^2=P\) forces \(\varphi(B)=1\). Choose \(Y\) with \(\varphi(Y)=1\). By the averaging identities,
\[
\varphi(X)B^2=\varphi(XB)B=\varphi(BX)B
\quad\text{for all }X.
\]
Taking \(X\) with \(\varphi(X)=1\), we obtain \(B^2=\lambda B\) and hence \(\varphi(XB)=\varphi(BX)=\lambda\varphi(X)\). At \(X=I_n\), the relation \(1=\varphi(B)=\lambda\varphi(I_n)\) shows \(\lambda\ne0\). Define \(E=B/\lambda\) and \(\psi=\lambda\varphi\). Then
\[
E^2=E,\quad \psi(I_n)=\psi(E)=1,\quad
\psi(XE)=\psi(EX)=\psi(X),\quad P(X)=\psi(X)E.
\]
The trace pairing \((C,X)\mapsto\operatorname{tr}(CX)\) on \(M_n(k)\) is nondegenerate in every characteristic. Thus \(\psi(X)=\operatorname{tr}(CX)\) uniquely. Cyclicity of trace and the identities just proved imply \(CE=EC=C\) and \(\operatorname{tr}(C)=1\). Conversely, any such \((E,C)\) obeys \(P^2=P\), since \(\operatorname{tr}(CE)=1\), and
\[
P(XP(Y))=\operatorname{tr}(CXE)\operatorname{tr}(CY)E=P(X)P(Y),
\]
with the other identity analogous. Finally, \(P(I_n)=\operatorname{tr}(C)E=E\) and nondegeneracy of trace make \(E,C\) unique.

**2. Geometry and rational points.** Fix \(r\in\{1,\ldots,n\}\). Every rank-\(r\) idempotent is conjugate to \(\operatorname{diag}(I_r,0)\), and its stabilizer is \(\mathrm{GL}_r\times\mathrm{GL}_{n-r}\). This homogeneous space is smooth, irreducible, and of dimension \(2r(n-r)\). Over such an idempotent \(E\), the equations \(EC=CE=C\) identify \(C\) with an endomorphism of \(\operatorname{im}E\), and \(\operatorname{tr}C=1\) cuts out a nonempty affine hyperplane of dimension \(r^2-1\). These fibers form a Zariski-locally trivial affine bundle. The coordinate identification is biregular: on each open subset where a chosen entry of \(E=P(I_n)\) is nonzero, the coefficient functional \(\operatorname{tr}(CX)\) is recovered regularly from the same entry of \(P(X)\). The characteristic polynomial of an idempotent of rank \(r\) is \(u^{n-r}(u-1)^r\); these are distinct for distinct \(r\) in every characteristic. Consequently the \(r\)-strata are simultaneously open and closed in the reduced parameter variety and are exactly its irreducible components.

Over \(\mathbb F_q\), an idempotent of rank \(r\) is equivalent to a choice of complementary subspaces \(U\oplus W=\mathbb F_q^n\) with \(\dim U=r\). There are \({n\brack r}_q\) choices of \(U\) and \(q^{r(n-r)}\) complementary subspaces \(W\). For each, the trace-one matrices \(C\) number \(q^{r^2-1}\), because trace is a surjective linear form on \(M_r(\mathbb F_q)\) even when \(p\mid r\). Multiplication gives \({n\brack r}_q q^{nr-1}\).

**3. Conjugacy.** The pair \((E,C)\) transforms under \(g\in\mathrm{GL}_n\) as \((gEg^{-1},gCg^{-1})\). Once \(E\) is brought to the standard diagonal idempotent, its stabilizer acts on \(C\) solely by similarity of its \(r\times r\) corner. Hence the orbit problem reduces exactly to trace-one similarity classes of arbitrary \(r\times r\) matrices.

For completeness, derive the trace-biased similarity-class formula. Rational canonical form associates to each monic irreducible \(f\in\mathbb F_q[u]\) a partition \(\lambda_f\), with \(\sum_f\deg(f)|\lambda_f|=r\). Define \(\tau(f)\) to be minus the coefficient of \(u^{\deg(f)-1}\) in \(f\). The class trace is \(\sum_f|\lambda_f|\tau(f)\). By unique factorization and the partition identity \(\sum_\lambda v^{|\lambda|}=\prod_{j\ge1}(1-v^j)^{-1}\), the unrestricted similarity-class series is
\[
K_q(z)=\prod_{j\ge1}\prod_f(1-z^{j\deg f})^{-1}
=\prod_{j\ge1}(1-qz^j)^{-1}.
\]
Fix a nontrivial additive character \(\chi\) of \(\mathbb F_q\). The corresponding trace-weighted series is
\[
\mathcal K_\chi(z)=\prod_{j\ge1}\prod_f
[1-\chi(j\tau(f))z^{j\deg f}]^{-1}.
\]
For a fixed \(j\), unique factorization interprets the inner product as a series over all monic polynomials, weighted by \(\chi(j\tau(h))\). For every positive degree, the next-to-leading coefficient of a monic polynomial ranges uniformly over \(\mathbb F_q\). Therefore the inner product equals \(1\) if \(p\nmid j\) and \((1-qz^j)^{-1}\) if \(p\mid j\). Thus \(\mathcal K_\chi(z)=K_q(z^p)\) for every nontrivial \(\chi\). Additive-character orthogonality now yields, for prescribed trace \(1\), exactly \((K_q(r)-\mathbf1_{p\mid r}K_q(r/p))/q\) classes. Summing the \(r\)-components across \(1\le r\le n\) proves the stated full dimension-generating series. Notice in particular why the correction occurs only for ranks divisible by \(p\): it is not a scalar-shift artifact.

**4. Corank limit.** Write \(j=n-r\) and set \(t=q^{-1}\). Divide the exact \(j\)-fiber size by \(q^{n^2-1}\). The resulting nonnegative weight is
\[
 b_{n,j}={n\brack j}_q q^{-nj}
=t^{j^2}\frac{\prod_{i=0}^{j-1}(1-t^{n-i})}{\prod_{i=1}^{j}(1-t^i)},
\qquad 0\le j<n.
\]
For each fixed \(j\), this converges to \(b_j=t^{j^2}/\prod_{i=1}^{j}(1-t^i)\). The bound \(0\le b_{n,j}\le t^{j^2}/\prod_{i=1}^{\infty}(1-t^i)\) is summable in \(j\), so dominated convergence gives a finite positive normalizing constant \(G(t)=\sum_{j\ge0}b_j\) and convergence in total variation of the normalized corank probabilities. The first classical Rogers–Ramanujan identity is
\[
\sum_{j\ge0}\frac{t^{j^2}}{\prod_{i=1}^{j}(1-t^i)}
=\prod_{h\ge0}\frac1{(1-t^{5h+1})(1-t^{5h+4})},\quad 0<t<1,
\]
and gives the advertised product. This classical analytic identity is used, not claimed as a new identity.

## Verification

The accompanying standalone Python 3 file `check_averaging.py` computes directly with field elements modulo \(2\) and modulo \(3\). It enumerates rank-one idempotent linear maps on \(M_2\) in normalized coefficient form and tests all averaging identities on every pair of matrix units, without using the coordinate classification. It finds exactly \(6,8\) operators with \(\operatorname{rank}P(I_2)=1,2\) over \(\mathbb F_2\), and \(12,27\) over \(\mathbb F_3\). The same checker enumerates rational-canonical invariants of all matrices of sizes \(1,2,3\) over these prime fields; their trace-stratified similarity-class multiplicities match the formula above. The observed counts support, but are not substituted for, the arbitrary-field and all-dimensions proofs.

For reproducibility, run `python3 check_averaging.py`; success ends with `RANK_ONE_AVERAGING_AND_TRACE_CLASSES_OK`. The checker uses ordinary prime-field modular arithmetic, so it **does not** directly test extension fields; extension-field coverage follows from the general proof.

## Relationship to prior work

Pei and Guo, *Averaging algebras, Schröder numbers, rooted trees and operads* (arXiv:1401.7386, first posted 2014-01-29), Definition (3) and Proposition 2.3, establish the two-sided averaging convention and a necessary and sufficient decomposition criterion for any idempotent averaging projection on an arbitrary algebra. That general criterion **covers the abstract projection property** and could be specialized to recover the preliminary rank-one normalization; the preliminary fact is therefore not claimed as a new general characterization. The present claim concerns its full matrix-algebra fibers, exact finite-field counts, trace-sensitive conjugacy-orbit generating function and asymptotic corank law, none of which is stated in the inspected relevant section of that paper.

Fulman, *Cycle indices for the finite classical groups* (arXiv:math/9712239, first posted 1997-12-09), §1–3, reviews rational canonical parameters, finite-field matrix counting and Rogers–Ramanujan phenomena for random matrices and classical groups. These classical tools explain the matrix-class generating function and product, which are used as established inputs. The source does not formulate a rank-one averaging-projection parameter space, its trace-one similarity reduction, or the corresponding operator corank distribution in the inspected passages. Cao, *An Algebraic Study of Averaging Operators* (arXiv:1401.7389, first posted 2014-01-29), develops related averaging algebra structures; its abstract/contents and relevant term searches yielded no directly comparable full-matrix finite-field enumeration, but the entire dissertation was not reviewed and broader coverage is a residual risk. Separate published findings about rank-one Rota–Baxter operators and nil-clean factorizations count genuinely different operators and do not imply these idempotent averaging formulas.

## Limitations

No claim is made for higher-rank or non-idempotent averaging operators, general finite-dimensional algebras, matrix algebras over nonfields, or scheme-theoretic nilpotent structure of the defining equations. The geometric variety is the reduced locus. The orbit series counts simultaneous conjugation by \(\mathrm{GL}_n\), not equivalence under the full linear automorphism group of the \(n^2\)-dimensional vector space. The standard rational-canonical parametrization and the Rogers–Ramanujan identity are prior mathematics, not novel results here. Although targeted overlap searches and primary-source comparisons found no theorem that directly gives the full four-part enumeration, a stronger older classification or generating function may subsume it. Independent mathematical review and comprehensive publication-priority determination have not been performed.

## References

1. J. Pei and L. Guo, *Averaging algebras, Schröder numbers, rooted trees and operads*, arXiv:1401.7386, first public version 2014-01-29, https://arxiv.org/abs/1401.7386. Proposition 2.3 and Section 2.
2. J. Fulman, *Cycle indices for the finite classical groups*, arXiv:math/9712239, first public version 1997-12-09, https://arxiv.org/abs/math/9712239. Introduction, rational canonical parametrization, and Section 3.
3. Y. Cao, *An Algebraic Study of Averaging Operators*, arXiv:1401.7389, first public version 2014-01-29, https://arxiv.org/abs/1401.7389. Abstract/contents and terminology comparison.
4. The classical first Rogers–Ramanujan identity, as recalled in Fulman and standard partition-theory literature.
