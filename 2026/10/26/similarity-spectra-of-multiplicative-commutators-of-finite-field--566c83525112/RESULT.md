# Similarity spectra of multiplicative commutators of finite-field transvections

## Finding

Let \(q\) be any prime power and \(n\ge 2\). Independently choose nonidentity transvections \(A,B\) uniformly from \(\operatorname{SL}_n(\mathbb F_q)\), and put \(K=[A,B]=ABA^{-1}B^{-1}\). There are
\[
T=\frac{(q^n-1)(q^{n-1}-1)}{q-1}
\]
transvections. If \(A-I=u\varphi\), \(B-I=v\psi\), where the four vector/covector factors are nonzero and \(\varphi(u)=\psi(v)=0\), define \(t=\varphi(v)\psi(u)\in\mathbb F_q\). Then \(\Pr(K\in\mathcal C\mid A)\), for any similarity-stable set \(\mathcal C\), is determined by the following exact disjoint cases (the counts are numbers of choices of \(B\) for each fixed \(A\)):

1. \(K=I\) for exactly
\[
N_I=(q^{n-1}-1)+\frac{q(q^{n-2}-1)^2}{q-1}
\]
choices.
2. \(K\ne I\) is a transvection, hence \(K-I\) is square-zero of rank one, for exactly \(N_U=2q^{n-1}(q^{n-2}-1)\) choices.
3. For *each* \(t\in\mathbb F_q^\times\), exactly \(N_t=q^{2n-3}\) choices give \(\operatorname{rank}(K-I)=2\), and \(K\) is similar to \(I_{n-2}\oplus G_t\), where \(G_t\in\operatorname{SL}_2(\mathbb F_q)\) is nonscalar cyclic with characteristic polynomial
\[
P_t(X)=X^2-(2+t^2)X+1.
\]
Conversely, every possible similarity type belongs to one of these cases. In odd characteristic, \(t\) and \(-t\) define the same similarity class, so their counts add; in characteristic two, distinct nonzero \(t\)'s define distinct classes.

The spectral types of these cyclic two-dimensional blocks have complete finite-field counts:

- For odd \(q\), set \(\delta=2\) if \(q\equiv1\pmod4\) and \(\delta=0\) otherwise. Among the \(q-1\) nonzero \(t\)'s, precisely \(\delta\) yield a repeated-eigenvalue Jordan block \(J_2(-1)\), precisely \((q-3-\delta)/2\) yield two distinct eigenvalues in \(\mathbb F_q\), and precisely \((q+1-\delta)/2\) yield an irreducible quadratic. Each parameter accounts for \(q^{2n-3}\) transvection partners.
- For even \(q\), no nonzero parameter has repeated roots: exactly \(q/2-1\) yield two distinct eigenvalues over \(\mathbb F_q\) and exactly \(q/2\) yield irreducible quadratics. Split cases are characterized by \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(t^{-1})=0\).

For fixed \(q\) and \(n\to\infty\), the respective probabilities for identity, a nonidentity transvection, and the fixed nonzero scalar parameter \(t\) converge to
\[
\frac1{q^2},\qquad\frac{2(q-1)}{q^2},\qquad\frac{q-1}{q^2}.
\]
The last probability is for each \(t\ne0\), not their union. These formulas give the *full conjugation-invariant law* of \(K\), because the pair of uniform transvections is invariant under simultaneous conjugation.

## Assumptions and scope

Here a transvection means precisely \(I+N\) with \(N\ne0\), \(\operatorname{rank}N=1\), and \(N^2=0\). We use the multiplicative group commutator convention \([A,B]=ABA^{-1}B^{-1}\), not the additive Lie bracket. The finite field may have arbitrary prime-power order, including characteristic two; \(n=2\) is included. Similarity refers to \(\operatorname{GL}_n(\mathbb F_q)\)-similarity. A two-dimensional matrix is cyclic when its minimal polynomial has degree two. Every nonidentity transvection is conjugate under \(\operatorname{GL}_n(\mathbb F_q)\), so it suffices to fix \(A=I+e_1e_2^*\).

## Proof

**One-to-one parametrization and basic identity.** Each nonzero rank-one square-zero operator is an outer product \(u\varphi\) with nonzero \(u,\varphi\), \(\varphi(u)=0\); the only ambiguity is \((u,\varphi)\mapsto(cu,c^{-1}\varphi)\) for \(c\in\mathbb F_q^\times\). Counting such pairs gives \(T=(q^n-1)(q^{n-1}-1)/(q-1)\). Write \(E=A-I=u\varphi\), \(F=B-I=v\psi\), \(a=\varphi(v)\), \(b=\psi(u)\), and \(t=ab\). Then \(E^2=F^2=0\), \(EFE=tE\), \(FEF=tF\), and \(EFEF=tEF\). Multiplication of \((I+E)(I+F)(I-E)(I-F)\) yields
\[
K=I+(1+t)EF-FE-tE+tF.\tag{1}
\]

**The zero-parameter cases.** When \(t=0\), (1) becomes \(K=I+EF-FE\). Here \(EF=au\psi\) and \(FE=bv\varphi\). Since \(ab=0\), both products vanish exactly when \(a=b=0\); otherwise exactly one is nonzero and it is rank-one square-zero. Thus these are precisely the identity and nonidentity-transvection cases. Fixing \(u,\varphi\), for \(a=b=0\) there are \(q-1\) choices of \(v\) on \(\langle u\rangle\), each with \(q^{n-1}-1\) admissible nonzero \(\psi\); and \(q^{n-1}-q\) choices of \(v\in\ker\varphi\setminus\langle u\rangle\), each with \(q^{n-2}-1\) nonzero \(\psi\) annihilating both \(u\) and \(v\). After dividing by \(q-1\) for scalar redundancy, this gives \(N_I\). If \(a\ne0,b=0\), then \(v\) has \((q-1)q^{n-1}\) possibilities and \(\psi\) has \(q^{n-2}-1\); dividing by \(q-1\) gives \(q^{n-1}(q^{n-2}-1)\). Interchanging \(a\) and \(b\) gives the equal other contribution, proving \(N_U\).

**The nonzero-parameter cases.** Suppose \(t\ne0\). For every choice of \(a\in\mathbb F_q^\times\), the vectors satisfying \(\varphi(v)=a\) number \(q^{n-1}\). Since \(a\ne0\), \(u,v\) are independent, and the linear conditions \(\psi(v)=0\), \(\psi(u)=t/a\) have exactly \(q^{n-2}\) solutions. Dividing the product \((q-1)q^{n-1}q^{n-2}\) by the scalar multiplicity \(q-1\) proves \(N_t=q^{2n-3}\). The space decomposes as
\[
\mathbb F_q^n=\langle u,v\rangle\oplus(\ker\varphi\cap\ker\psi).
\]
On the second summand \(K=I\); on the first, in the ordered basis \((u,v)\), (1) is
\[
G_t=\begin{pmatrix}1+t+t^2&-ta\\ tb&1-t\end{pmatrix}.
\]
Its determinant is one and its trace is \(2+t^2\). Its off-diagonal entries are nonzero, so \(G_t\) is nonscalar and hence cyclic. It also follows that \(\operatorname{rank}(K-I)=2\), because \(\det(G_t-I)=2-\operatorname{tr}(G_t)=-t^2\ne0\). The characteristic polynomial determines the similarity type of the cyclic block, and thereby the full similarity type. The three case counts sum to \(T\), giving exhaustiveness and all boundaries, including \(n=2\).

**Arithmetic splitting.** If \(q\) is odd, the discriminant of \(P_t\) is \(t^2(t^2+4)\). The equation \(t^2=-4\) has \(\delta\) solutions: it is equivalent to \(-1\) being a square. Repeated roots are \(-1\) and the cyclic block must be \(J_2(-1)\). Let \(\chi\) be the quadratic character, extended by \(\chi(0)=0\). Counting solutions to \(y^2=t^2+4\) by the change of variables \((y-t)(y+t)=4\) gives precisely \(q-1\) pairs, so \(\sum_{t\in\mathbb F_q}\chi(t^2+4)=-1\). The excluded value \(t=0\) contributes one; hence among \(t\ne0\), the split-minus-nonsplit count is \(-2\). Together with the repeated-root count \(\delta\), this gives \((q-3-\delta)/2\) split parameters and \((q+1-\delta)/2\) nonsplit parameters.

For even \(q\), \(P_t(X)=X^2+t^2X+1\). Since \(t\ne0\), the formal derivative is \(t^2\ne0\), and repeated roots are impossible. Dividing by \(t^4\) after substituting \(X=t^2Y\) gives \(Y^2+Y=t^{-4}\), soluble over \(\mathbb F_q\) precisely when its absolute trace vanishes. Frobenius invariance makes this equivalent to \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(t^{-1})=0\). Exactly \(q/2-1\) of the nonzero \(t\)'s satisfy that condition; the other \(q/2\) yield irreducible quadratics.

**Limit.** For fixed \(q\), divide the exact case counts by \(T\), and take \(n\to\infty\). Since \(T\sim q^{2n-1}/(q-1)\), the claimed limits follow. The distribution of \(K\) is conjugation-invariant by simultaneous conjugation of \((A,B)\). A conjugation-invariant distribution is uniform within each similarity class, so its per-class mass as computed above determines its entire matrix-valued law.

## Verification

The self-contained checker `checks/check.py` enumerates every nonidentity transvection \(B\) with a fixed standard \(A\), computes the group commutator explicitly and independently measures \(\operatorname{rank}(K-I)\), trace, polynomial annihilation and characteristic-polynomial splitting. It exhaustively tests prime fields of orders \(2,3,5,7\) and the extension field of order \(4\), in dimensions \(2\), \(3\), and selected dimension \(4\) cases: twelve configurations and \(5163\) distinct partner matrices. Output is embedded at `checks/output.txt` and ends with `ALL_TRANSVECTION_COMMUTATOR_COUNTS_PASSED: cases=12 B_matrices=5163`. To reproduce, run `python checks/check.py` from the extracted package directory. The infinite-family assertion is proven above; these computations are finite tests, not a substitute for proof.

## Relationship to prior work

Eberhard (2023) studies diameter and generation of classical groups using transvections, including the vector–covector parametrization and two-cycle weights that underlie \(t\). The paper's stated results concern generation and diameter, not the class-by-class probability law for \([A,B]\). The previously available dimension-two result *Dimension-two boundary for double transvection commutators* concerns existence of nested commutators \([[g,A],B]\) with prescribed value, rather than the distribution of the single commutator \([A,B]\) for uniformly sampled transvections. The original classical commutator identities and quadratic-character facts are not presented as new. Fleischmann (2013) studies commutator structure in unipotent transvection groups and invariant theory; only its abstract was accessible, not its full text. The assessed new claim is the exact all-field, all-dimension similarity and arithmetic splitting distribution (plus its limiting masses), conditional on the literature inspected.

## Limitations

The distribution is for a pair of uniformly sampled **nonidentity** transvections, with independence and the stated multiplicative commutator convention; it does not describe arbitrary unipotent matrices, pairs of arbitrary group elements, symplectic transvection sampling, or additive matrix commutators. There is a genuine originality risk that a specialized conjugacy-class convolution or an inaccessible transvection-commutator paper contains an equivalent formula. In particular, the full text of Fleischmann (2013) was not available for comparison. A published count implying this entire distribution would cover the result regardless of different phrasing. No claim of independent validation is made.

## References

1. S. Eberhard, *Diameter of classical groups generated by transvections*, arXiv:2308.07086, first submitted 14 August 2023. https://arxiv.org/abs/2308.07086
2. P. Fleischmann, *On finite unipotent transvection groups and their invariants*, Quarterly Journal of Mathematics 65 (2014), 175–200, first published online 4 January 2013. https://doi.org/10.1093/qmath/has042
3. *Dimension-two boundary for double transvection commutators*, published mathematical record. https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-dimension-two-double-transvection-boundary--6c6e3f65efd6
