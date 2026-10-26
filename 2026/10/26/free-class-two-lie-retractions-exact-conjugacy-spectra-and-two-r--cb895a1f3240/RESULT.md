# Free class-two Lie retractions: exact conjugacy spectra and two-rank concentration

## Finding

For every integer \(n\ge3\) and prime power \(q\), let \(V=\mathbb F_q^n\), \(N=\binom n2\), and let \(L=V\oplus\bigwedge^2V\) be the free class-two nilpotent Lie algebra with \([v+z,w+t]=v\wedge w\). A **retraction** means an idempotent \(\mathbb F_q\)-linear Lie-algebra endomorphism \(F:L\to L\); its image is a retract subalgebra. Set \(r=\operatorname{rank}(F\bmod[L,L])\) and \(R=\binom r2\).

**Complete orbit and rank spectrum.** Under conjugation by \(\operatorname{Aut}(L)\), idempotent Lie endomorphisms have exactly \(n+1\) orbits, indexed by \(r\in\{0,\ldots,n\}\). The orbit with index \(r\) consists precisely of maps with image dimension \(r+R\), and has cardinality
\[
T_{n,q}(r)= {n\brack r}_q\,q^{\,r(n-r)+r(N-R)+(n-r)R},
\]
where \({n\brack r}_q\) is the Gaussian binomial coefficient. The total number of idempotent Lie endomorphisms is \(\sum_{r=0}^n T_{n,q}(r)\). The number of **distinct image subalgebras** in that stratum is
\[
S_{n,q}(r)= {n\brack r}_q\,q^{\,r(N-R)},
\]
and every such image supports precisely \(q^{\,r(n-r)+(n-r)R}\) retraction maps. Every nonzero proper image is a free class-two Lie algebra on \(r\) generators (abelian if \(r=1\)) and is not an ideal of \(L\).

**Sharp two-rank concentration.** Select uniformly among all idempotent Lie endomorphisms and denote its quotient rank by \(J_n\). Put
\[
t_n=\frac{n-2+\sqrt{7n^2+8n+4}}6,
\qquad k_n=\lfloor t_n\rfloor,
\qquad C_q=\prod_{j=1}^{\infty}(1-q^{-j})^{-1}.
\]
Then, for all \(n\ge3\),
\[
\Pr(J_n\notin\{k_n,k_n+1\})\le (n+1)C_q\,q^{\,7-\sqrt{7n^2+8n+4}/2}.
\]
In particular, the probability of those **two consecutive ranks** tends to one exponentially fast, and
\[
\frac{J_n}{n}\xrightarrow[n\to\infty]{\Pr}\frac{1+\sqrt7}{6}.
\]
The rank concentration concerns the quotient-generator rank, not the full image dimension, which is \(J_n+\binom{J_n}{2}\).

## Assumptions and scope

The field is finite with \(q\ge2\) elements, in **any characteristic**, including characteristic two. The bracket is the alternating exterior product and the center of \(L\) equals \([L,L]=\bigwedge^2V\). The parameter \(n\ge3\) is the number of free generators. No assumption of normality of image or preservation of the displayed grading is made. Gaussian binomial coefficients use \({n\brack r}_q=\prod_{i=0}^{r-1}(q^{n-i}-1)/(q^{r-i}-1)\). The limiting statement fixes \(q\) and sends \(n\to\infty\).

## Proof

**1. All homomorphisms and the idempotence constraint.** A Lie homomorphism is uniquely specified by its generator images and hence by two linear maps \(A:V\to V\) and \(B:V\to\bigwedge^2V\). Its action on the derived ideal must be \(C=\bigwedge^2A\), so
\[
F(v+z)=Av+Bv+Cz.
\]
Conversely, this is a Lie homomorphism for every pair \((A,B)\): \(F([v,w])=Av\wedge Aw=[F(v),F(w)]\). Squaring yields \(F^2(v+z)=A^2v+(BA+CB)v+C^2z\). Therefore
\[
F^2=F\quad\Longleftrightarrow\quad A^2=A\ \text{ and }\ BA+CB=B.
\]
Indeed \(A^2=A\) implies \(C^2=C\).

**2. Explicit conjugacy and complete classification.** Write \(V=U\oplus K\), where \(U=\operatorname{im}A\) and \(K=\ker A\), of dimensions \(r\) and \(n-r\). Then \(C=\bigwedge^2A\) is a projection with image \(\bigwedge^2U\) of dimension \(R\) and kernel of dimension \(N-R\). The displayed equation is exactly
\[
B(U)\subseteq\ker C,\qquad B(K)\subseteq\operatorname{im}C.
\]
Define \(T:V\to\bigwedge^2V\) by \(T(u)=B(u)\) on \(U\) and \(T(k)=-B(k)\) on \(K\). Then \(B=TA-CT\). The central shear \(\Psi_T(v+z)=v+Tv+z\) is a Lie automorphism, and direct substitution shows
\[
F=\Psi_T\circ P_A\circ\Psi_T^{-1},\qquad
P_A(v+z)=Av+(\bigwedge^2A)z.
\]
Every rank-\(r\) vector-space projection \(A\) is conjugate under \(\operatorname{GL}(V)\) to the standard coordinate projection. Such conjugacy lifts to \(L\) via \(v+z\mapsto gv+(\bigwedge^2g)z\). Hence every retraction of a given \(r\) is conjugate to the same standard Lie projection, and different values of \(r\) cannot be conjugate because the quotient rank is invariant.

**3. Counting maps.** Choose \(U\) in \({n\brack r}_q\) ways and then its complement \(K\) in \(q^{r(n-r)}\) ways; these choices classify the rank-\(r\) idempotent \(A\). For each, the independent restrictions of \(B\) have \(r(N-R)\) and \((n-r)R\) free scalar coordinates. Multiplication gives \(T_{n,q}(r)\) exactly, with \(r=0,n\) both giving one map.

**4. Distinct retract images and the non-ideal boundary.** For a retraction of quotient image \(U\), its image has the intrinsic description
\[
\operatorname{im}F
=\{u+\gamma(u)+w:u\in U,\ w\in\bigwedge^2U\},
\]
where the class of \(\gamma\) is a linear map \(\beta:U\to(\bigwedge^2V)/(\bigwedge^2U)\). Conversely, every pair \((U,\beta)\) yields an image of a retraction: choose a complement, lift \(\beta\) to a central shear, and conjugate the standard projection. Two such descriptions have the same image exactly when \(U\) and \(\beta\) agree, so there are \({n\brack r}_q q^{r(N-R)}\) images. Division of the map count by the image count gives the asserted uniform fibre size. The bracket of its shifted generators is \(u\wedge u'\), proving that the image is freely generated in class two. For \(0<r<n\), choose nonzero \(u\in U\), \(k\in K\). Then \([u,k]=u\wedge k\notin\bigwedge^2U=\operatorname{im}F\cap[L,L]\); hence \(\operatorname{im}F\) is not an ideal.

**5. A quantitative saddle bound.** Factor the Gaussian coefficient as
\[
{n\brack r}_q=q^{r(n-r)}c_{n,q}(r),\quad
c_{n,q}(r)=\frac{\prod_{j=n-r+1}^n(1-q^{-j})}{\prod_{j=1}^r(1-q^{-j})},
\quad 1\le c_{n,q}(r)\le C_q.
\]
Thus \(T_{n,q}(r)=q^{E_n(r)}c_{n,q}(r)\), with
\[
E_n(r)=-r^3+\left(\frac n2-1\right)r^2+
\left(\frac{n^2}{2}+n\right)r.
\]
The polynomial increases on \([0,t_n]\) and decreases on \([t_n,n]\). Put \(S=\sqrt{7n^2+8n+4}\), \(k=\lfloor t_n\rfloor\), and \(\theta=t_n-k\in[0,1)\). The exact cubic Taylor identity gives
\[
E_n(t_n+s)=E_n(t_n)-\frac S2s^2-s^3.
\]
Consequently,
\[
E_n(k)-E_n(k-1)=\frac S2(1+2\theta)-(1+3\theta+3\theta^2)\ge\frac S2-7,
\]
and
\[
E_n(k+1)-E_n(k+2)=\frac S2(3-2\theta)+(7-9\theta+3\theta^2)\ge\frac S2+1.
\]
Where a neighboring rank lies outside \([0,n]\), simply omit it. Monotonicity implies that every rank outside \(\{k,k+1\}\) has \(E_n(r)\) at least \(S/2-7\) below \(\max\{E_n(k),E_n(k+1)\}\). A term in the denominator of the rank probability is at least \(q^{\max\{E_n(k),E_n(k+1)\}}\). Summing at most \(n+1\) excluded terms, each with bounded factor \(C_q\), proves the stated probability estimate. Since \(t_n/n\to(1+\sqrt7)/6\), the convergence in probability follows.

## Verification

The standalone file `verify.py` independently enumerates all generator-image pairs \((A,B)\) over small prime fields, explicitly constructs the induced endomorphism on \(V\oplus\bigwedge^2V\), checks the Lie brackets and the full matrix idempotence equation, counts each quotient-rank stratum, and counts distinct image subspaces using row-reduced canonical bases. No formula is used as an acceptance filter for enumerated maps; predicted totals are compared only after direct enumeration.

Executed checks: \((n,q)=(2,2),(2,3),(2,5),(3,2)\). The three-generator binary case checks \(262144\) homomorphisms, finding rank counts \((1,224,896,1)\) and distinct-image counts \((1,56,112,1)\). The two-generator cases are boundary consistency checks; the theorem's contribution is stated for \(n\ge3\). A separate integer-arithmetic check of exact formulas at larger \(n\) corroborated the two-rank concentration, but is not a proof of its limit.

## Relationship to prior work

Benito and Roldán-López, arXiv:1911.01897 (first submitted November 5, 2019; primary MSC 17B40), develop the derivation and automorphism description of free nilpotent Lie algebras, including the universal extension of maps on generators. This supplies the natural algebraic setting and the homomorphism parameterization, but their inspected results do not present the conjugacy and finite-field census of **idempotent Lie endomorphisms**, image-fibre counts, or the rank concentration bound.

Benito, de-la-Concepción and Laliena, arXiv:1604.02923, discuss grading projections and automorphism groups of free nilpotent Lie algebras, primarily in characteristic zero. Those degree projections are linear maps of the underlying vector space, not a classification of retractions as Lie-algebra homomorphisms. Cagliero, Gutierrez and Szechtman, arXiv:1703.06214, study uniserial representations of the same free class-two algebra, not its retraction spectrum.

Related results on automorphism fixed-space strata and order-two automorphisms of the free class-two Lie algebra concern **invertible** maps and do not imply the rank-\(r\) count of noninvertible idempotents; previous Heisenberg-group retraction results concern a different object and their three-dimensional case is only a boundary analogue. A general theorem on idempotent conjugacy in a broader algebraic category might subsume some of the orbit statement; no checked source supplies all the formulas and limiting law. Search nonappearance is not a uniqueness proof.

## Limitations

The classification concerns finite-field **linear Lie-algebra** homomorphisms, not abstract-group retractions or arbitrary additive/nonlinear maps. The two-point concentration fixes \(q\) and varies \(n\), not the reverse. The source comparison cannot exclude every equivalent presentation under module-projector, free-factor or retract terminology. Finite enumeration independently checks small cases but does not prove the unrestricted result.

## References

1. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1 (2019-11-05), https://arxiv.org/abs/1911.01897 .
2. P. Benito, D. de-la-Concepción, and J. Laliena, *Free nilpotent and nilpotent quadratic Lie algebras*, arXiv:1604.02923v1 (2016-04-11), https://arxiv.org/abs/1604.02923 .
3. L. Cagliero, L. Gutierrez, and F. Szechtman, *Free 2-step nilpotent Lie algebras and indecomposable modules*, arXiv:1703.06214v1 (2017-03-17), https://arxiv.org/abs/1703.06214 .
