# Witt-sensitive retraction spectra of quadratic-bracket Leibniz algebras

## Finding

Let \(q\) be an odd prime power, let \(d\geq 2\), and let \((V,b)\) be a nondegenerate symmetric bilinear space of dimension \(d\) over \(\mathbb F_q\). Define the two-step Leibniz algebra
\[
L_b=V\oplus\mathbb F_q z,\qquad [v+sz,w+tz]=b(v,w)z.
\]
An **algebra retraction** is an \(\mathbb F_q\)-linear endomorphism \(E:L_b\to L_b\) preserving the bracket and satisfying \(E^2=E\). A **retract subalgebra** is its image. All counts below concern actual maps and embedded subspaces, not isomorphism classes.

**Theorem (retractions and symmetry orbits).** Every retraction is either the identity or uniquely has the form
\[
E(v+tz)=Pv+\theta(Pv)z,
\]
where \(U=\operatorname{im}P\) is a totally isotropic subspace of \((V,b)\), \(P^2=P\), \(P|_U=I_U\), and \(\theta\in U^*\). Conversely, every such triple gives a retraction. Each proper retract is a graph \(\{u+\theta(u)z:u\in U\}\), and every specified graph of dimension \(r\) admits exactly \(q^{r(d-r)}\) retractions.

Let \(w\) be the Witt index of \(b\), and put \(I_0=1\). For \(1\leq r\leq w\) let
\[
I_r=\frac{\prod_{j=0}^{r-1}Z_{d-2j}}{\prod_{i=1}^{r}(q^i-1)},
\quad
Z_m=\begin{cases}
q^{m-1}-1,&m\text{ odd},\\
q^{m-1}-1+\varepsilon(q-1)q^{m/2-1},&m\text{ even},
\end{cases}
\]
where, if \(d=2s\) is even, \(\varepsilon=\chi((-1)^s\det b)\in\{+1,-1\}\) with \(\chi\) the quadratic character. When \(d\) is odd only the odd branch is used. The Witt index is \(\lfloor d/2\rfloor\), except that it is \(d/2-1\) when \(d\) is even and \(\varepsilon=-1\).

The complete dimension distribution of retract subalgebras and the complete rank distribution of retractions are, respectively,
\[
\boxed{\mathcal R_b(T)=T^{d+1}+\sum_{r=0}^{w} I_r q^r T^r},\qquad
\boxed{\mathcal E_b(T)=T^{d+1}+\sum_{r=0}^{w}I_rq^{r(d-r+1)}T^r}.
\]
The \(r=0\) term in both expressions is the zero map or zero image; the leading term is the identity or the whole algebra.

There is an additional, specifically orthogonal, **rank-one orbit splitting**. Suppose \(w\geq1\), and act on retractions by conjugation with the ordinary \(\mathbb F_q\)-linear algebra automorphism group \(\operatorname{Aut}(L_b)\). Then:

* If \(d\) is even, the rank-one retractions form **exactly two orbits**, of cardinalities \(I_1q^{d-1}\) and \(I_1(q-1)q^{d-1}\).
* If \(d\) is odd, they form **exactly three orbits**, of cardinalities \(I_1q^{d-1}\), \(\frac{q-1}{2}I_1q^{d-1}\), and \(\frac{q-1}{2}I_1q^{d-1}\).

More precisely, write a rank-one projection as \(P(x)=b(a,x)u\), with \(b(u,u)=0\), \(b(a,u)=1\). The first orbit has \(b(a,a)=0\). In even dimension all nonzero values give the second orbit; in odd dimension the two other orbits correspond to the two quadratic-character classes of \(b(a,a)\). These descriptions are independent of the allowed rescaling of \((u,a)\).

For \(d=2\), a nonsplit plane has only the zero and identity retractions, whereas a split plane has exactly \(2q^2+2\) retractions, with rank-one orbit sizes \(2q\) and \(2q(q-1)\). For \(d=4\), \(q=3\), the split and nonsplit types have respectively \(7130\) and \(812\) retractions; their rank-one strata split into sizes \((432,864)\) and \((270,540)\). Thus the intrinsic endomorphism monoid distinguishes the two Witt types.

## Assumptions and scope

The coefficient field has odd cardinality \(q=p^f\), including nonprime fields. The symmetric form \(b\) is nondegenerate, and \(d\ge2\); no assumption of algebraic closedness or splitness is made. The bracket is symmetric, generally not alternating, so these algebras are usually non-Lie Leibniz algebras. The same formula applies to either left or right Leibniz convention because the derived ideal is central. The orbit assertion concerns only rank-one retractions, not an orbit classification in higher ranks. In the anisotropic two-dimensional case \(w=0\), there are no rank-one retractions and hence no rank-one orbits.

## Proof

**1. Reduction of endomorphisms.** Since \(b\) is nonzero and \([L_b,L_b]=\mathbb F_q z\), any bracket-preserving linear map has the unique form
\[
F(v+tz)=Av+(f(v)+ct)z
\]
for \(A\in\operatorname{End}(V)\), \(f\in V^*\), and \(c\in\mathbb F_q\). Applying \(F\) to the bracket and taking the bracket of images gives the necessary and sufficient condition
\[
b(Av,Aw)=c\,b(v,w)\quad\text{for all }v,w\in V.
\]
The equation \(F^2=F\) is equivalent to
\[
A^2=A,\qquad c^2=c,\qquad fA+cf=f.
\]
Since the coefficient field is a field, \(c\in\{0,1\}\). For \(c=1\), nondegeneracy of \(b\) makes \(A\) invertible; the equation \(A^2=A\) forces \(A=I_V\), and then \(fA=0\) forces \(f=0\). This is the identity. For \(c=0\), the form equation is exactly \(b(\operatorname{im}A,\operatorname{im}A)=0\). Writing \(P=A\), the identity \(fP=f\) is equivalent to \(f=\theta P\) for one \(\theta\in(\operatorname{im}P)^*\). Conversely these relations verify bracket preservation and idempotence, proving the classification.

**2. Images and projection fibers.** For a fixed totally isotropic \(r\)-space \(U\le V\), the image of \(E\) is the graph of exactly one functional \(\theta\in U^*\), yielding \(q^r\) embedded images. Linear projections \(P:V\twoheadrightarrow U\) with \(P|_U=I\) correspond bijectively to complementary \((d-r)\)-spaces \(K=\ker P\). Relative to one fixed complement, every other complement is the graph of a map \(V/U\to U\), so there are \(q^{r(d-r)}\) projections. Multiplication gives \(I_rq^{r(d-r+1)}\) rank-\(r\) maps, and \(I_rq^r\) rank-\(r\) images.

**3. Explicit orthogonal counts.** Standard Witt decomposition over an odd finite field writes the form as \(w\) hyperbolic planes plus an anisotropic core of dimension \(a\in\{0,1,2\}\). In a nondegenerate quadratic space of dimension \(m\), let \(N_0(m)\) be the number of vectors satisfying \(b(x,x)=0\), including zero. On adjoining a hyperbolic plane \(H\), the equation \(b(x,x)+2uv=0\) has \(2q-1\) solutions in \((u,v)\) when \(b(x,x)=0\) and \(q-1\) otherwise. Hence
\[
N_0(H\perp W)=q N_0(W)+(q-1)q^{\dim W}.
\]
The anisotropic cores in dimensions \(0,1,2\) each have precisely one zero-norm vector. Induction gives \(N_0(m)-1=Z_m\) as displayed above, with the usual split/nonsplit sign for even dimension. Given an ordered totally isotropic \(j\)-frame spanning \(U_j\), the next independent vector lies in \(U_j^\perp\setminus U_j\). Its image in the nondegenerate quotient \(U_j^\perp/U_j\), of dimension \(d-2j\) and the same anisotropic core, is nonzero and isotropic. Every such quotient vector has \(q^j\) lifts. Therefore the number of ordered totally isotropic \(r\)-frames is
\[
\prod_{j=0}^{r-1}q^jZ_{d-2j}.
\]
Each \(r\)-space has exactly \(\prod_{j=0}^{r-1}(q^r-q^j)\) ordered bases. Dividing, and cancelling \(q^{r(r-1)/2}\), gives the displayed formula for \(I_r\). This also proves all boundary cases, including \(I_r=0\) beyond the Witt index.

**4. Rank-one automorphism orbits.** Every automorphism of \(L_b\) has the form
\[
G(v+tz)=gv+(\ell(v)+ct)z,
\qquad b(gv,gw)=c\,b(v,w),
\]
where \(g\in\operatorname{GO}(V,b)\), \(c\ne0\) is its similitude multiplier, and \(\ell\in V^*\) is arbitrary. Conjugating a rank-one retraction by an automorphism with \(g=I\), \(c=1\), and variable \(\ell\) varies \(\theta\) freely on its image line. Thus \(\theta\) contributes a factor \(q\) to every orbit and causes no additional splitting.

For a rank-one projection \(P\), choose \(u\ne0\) spanning its isotropic image and write \(P(x)=b(a,x)u\) with \(b(a,u)=1\). Replacing \((u,a)\) by \((\alpha u,\alpha^{-1}a)\) preserves \(P\) and changes \(t=b(a,a)\) by \(\alpha^{-2}\). Conjugation by a similitude of multiplier \(c\) changes \(t\) by \(c^{-1}\). Therefore \(t=0\) is one invariant, while nonzero \(t\) is determined up to squares and the multiplier group.

All these invariants are complete. If two normalized pairs \((u,a)\) have equal \(t\), their spans have the identical nonsingular Gram matrix \(\begin{psmallmatrix}0&1\\1&t\end{psmallmatrix}\). The induced isometry of these spans extends to the whole space by Witt's extension theorem. If their parameters agree only up to a permitted square and multiplier, first rescale a representing pair and apply a similitude with that multiplier, then use the same extension theorem. Thus there are no hidden orbit invariants.

In dimension \(d\), a nondegenerate symmetric form is similar to its scalar multiple \(c b\) precisely when the determinant classes agree. Because scaling changes the determinant by \(c^d\), the similitude multipliers form all of \(\mathbb F_q^\times\) when \(d\) is even, and exactly its square subgroup when \(d\) is odd. This gives two nonempty parameter classes in even dimension (zero/nonzero) and three in odd dimension (zero/square/nonsquare).

Finally, fix a canonical generator \(u\) of any isotropic line. The hyperplane-functional parameter \(a\) is determined by \(b(a,u)=1\). In a Witt basis \((u,v,W)\), every such \(a\) is uniquely \(v+\beta u+w\) with \(w\in W\), and \(b(a,a)=2\beta+b(w,w)\). For each specified \(t\), there are therefore exactly \(q^{d-2}\) such \(a\). Multiplying by the \(I_1\) isotropic lines, the \(q\) possible \(\theta\), and the number of permitted values of \(t\) yields exactly the orbit cardinalities in the theorem.

## Verification

The accompanying standard-library script `check_retracts.py` enumerates totally isotropic subspaces using reduced row-echelon bases for ten finite prime-field configurations, including both four-dimensional Witt types. It also exhaustively enumerates all homomorphisms and composition-idempotents for the symmetric-bracket algebras of dimension \(d+1\) corresponding to \((q,d)=(3,2),(5,2),(3,3)\) (both Witt types in dimension two), comparing every rank count with the theorem. Finally, it explicitly enumerates the orthogonal similitude groups and conjugacy orbits of rank-one projections for the split planes over \(\mathbb F_3\) and \(\mathbb F_5\) and a three-dimensional form over \(\mathbb F_3\). These finite checks support but do not prove the general theorem; the proof above covers all odd prime powers and dimensions.

## Relationship to prior work

Mancini and La Rosa, *Two-step nilpotent Leibniz algebras* (arXiv:2106.12904, first public 2021-06-24), classify relevant two-step Leibniz structures through bilinear forms and study their Lie-rack integration. That classification motivates the quadratic-bracket family but does not give its retraction spectra or rank-one automorphism orbits. Kurdachenko, Subbotin, and Yashchuk, *On the endomorphisms and derivations of some Leibniz algebras* (arXiv:2104.05922), determine the endomorphism monoid of an infinite-dimensional **cyclic** Leibniz algebra, not this finite quadratic-bracket family.

The count of totally isotropic subspaces and Witt's extension theorem are classical and are used, not claimed as discoveries. Analogous isotropic-image parametrizations can be developed for alternating-form Heisenberg Lie algebras; replacing an alternating form by a symmetric form alone is not the claimed geometric contribution. The specifically **orthogonal rank-one conjugacy orbit splitting** and its exact multiplicities, together with its relation to retraction spectra of these Leibniz algebras, form the distinguishing statement assessed here. A general classification of similitude orbits on pairs of vectors could imply the orbit part after a specialization; no claim of historical priority is made without such comparison.

## Limitations

The orbit classification stops at rank one; higher-rank retractions may have additional invariants. The theorem excludes characteristic two and degenerate forms. Counts enumerate embedded subalgebras, not abstract isomorphism classes. The proof uses standard finite-field quadratic-form classification and Witt extension; they are not independently re-proved here. Literature searches cannot establish absolute historical uniqueness, particularly across general orthogonal orbit theory or finite Leibniz-algebra endomorphism literature. Independent validation has not been carried out.

## References

1. M. Mancini and G. La Rosa, *Two-step nilpotent Leibniz algebras*, arXiv:2106.12904v1 (2021-06-24), https://arxiv.org/abs/2106.12904 .
2. L. A. Kurdachenko, I. Ya. Subbotin, and V. S. Yashchuk, *On the endomorphisms and derivations of some Leibniz algebras*, arXiv:2104.05922v1 (2021-04-13), https://arxiv.org/html/2104.05922v1 .
3. T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67, American Mathematical Society (2005): standard finite-field Witt classification.
4. E. Artin, *Geometric Algebra*, Interscience (1957): classical extension and isometry principles.
