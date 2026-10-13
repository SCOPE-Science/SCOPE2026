# Uniform group-invertible lifting over finite local matrix rings

## Finding
Let \(R\) be a finite commutative local ring, let \(\mathfrak m\) be its maximal ideal, let \(R/\mathfrak m\cong\mathbb F_q\), and put \(j=|\mathfrak m|\). A matrix \(A\in M_n(R)\) is group invertible when there is a matrix \(A^\#\) satisfying
\[
AA^\#A=A,\qquad A^\#AA^\#=A^\#,\qquad AA^\#=A^\#A.
\]
For a group-invertible \(A\), its image is a free direct summand of \(R^n\); call its rank \(r\). For every \(0\le r\le n\),
\[
G_{n,r}(R)=\#\{A\in M_n(R):A^\#\text{ exists and }\operatorname{rank}_R(\operatorname{im}A)=r\}
=\frac{|\operatorname{GL}_n(R)|}{|\operatorname{GL}_{n-r}(R)|}.
\]
Since reduction modulo \(\mathfrak m\) gives
\[
|\operatorname{GL}_s(R)|=j^{s^2}|\operatorname{GL}_s(\mathbb F_q)|,
\]
the rank spectrum has the closed form
\[
G_{n,r}(R)=j^{r(2n-r)}\frac{|\operatorname{GL}_n(\mathbb F_q)|}{|\operatorname{GL}_{n-r}(\mathbb F_q)|}.
\]
Thus the total number is
\[
G_n(R)=\sum_{r=0}^n\frac{|\operatorname{GL}_n(R)|}{|\operatorname{GL}_{n-r}(R)|}.
\]

There is also an exact fiber statement. Fix a group-invertible \(\overline A\in M_n(\mathbb F_q)\) of nullity \(k\). Of the \(j^{n^2}\) matrices in \(M_n(R)\) reducing to \(\overline A\), exactly
\[
j^{n^2-k^2}
\]
are group invertible. Equivalently, a uniformly chosen lift survives group invertibility with probability \(j^{-k^2}\). This probability depends only on the nullity of the residue matrix and the size of the maximal ideal.

For example, \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) are nonisomorphic local rings but both have \(q=2\) and \(j=2\). In \(M_2\) both therefore have image-rank counts
\[
G_{2,0}=1,\qquad G_{2,1}=48,\qquad G_{2,2}=96,
\]
for a total of \(145\) group-invertible matrices.

## Assumptions and scope
The ring \(R\) is finite, commutative, local, and unital. The theorem counts ordinary ring-theoretic group inverses in \(M_n(R)\). The rank in the statement is the free rank of the image direct summand, which is defined because a finitely generated projective module over a commutative local ring is free. No assertion is made for arbitrary nonlocal rings or for Drazin index greater than one.

## Proof
Let \(A\) be group invertible and write \(B=A^\#\). The common product \(e=AB=BA\) is idempotent. Because \(eA=ABA=A\) and \(e=AB\), one has \(\operatorname{im}A=\operatorname{im}e\). Because \(e=BA\) and \(Ae=ABA=A\), one likewise has \(\ker A=\ker e\). Therefore
\[
R^n=\operatorname{im}A\oplus\ker A.
\]
On \(W=\operatorname{im}A\), the restriction of \(A\) is an automorphism whose inverse is the restriction of \(B\), while \(A\) vanishes on \(K=\ker A\).

Conversely, suppose \(R^n=W\oplus K\), with \(W\) and \(K\) free of ranks \(r\) and \(n-r\), and let \(U\in\operatorname{Aut}_R(W)\). The endomorphism \(A=U\oplus0\) is group invertible, with \(A^\#=U^{-1}\oplus0\). Therefore group-invertible matrices of image rank \(r\) are in bijection with pairs consisting of an ordered decomposition \(R^n=W\oplus K\) of ranks \(r,n-r\) and an automorphism of \(W\).

The group \(\operatorname{GL}_n(R)\) acts transitively on such ordered decompositions. The stabilizer of the standard decomposition \(R^r\oplus R^{n-r}\) is the block-diagonal subgroup \(\operatorname{GL}_r(R)\times\operatorname{GL}_{n-r}(R)\). Hence the number of decompositions is
\[
\frac{|\operatorname{GL}_n(R)|}{|\operatorname{GL}_r(R)|\,|\operatorname{GL}_{n-r}(R)|}.
\]
Multiplying by the \(|\operatorname{GL}_r(R)|\) choices for \(U\) gives the first formula.

Reduction modulo \(\mathfrak m\) maps \(\operatorname{GL}_s(R)\) onto \(\operatorname{GL}_s(\mathbb F_q)\). Its kernel is \(I_s+M_s(\mathfrak m)\), which has \(j^{s^2}\) elements. Thus \(|\operatorname{GL}_s(R)|=j^{s^2}|\operatorname{GL}_s(\mathbb F_q)|\), yielding the closed form.

For the fiber statement, let \(\overline A\) have image rank \(r=n-k\), image \(\overline W\), and kernel \(\overline K\). The number of ordered decompositions \(W\oplus K=R^n\) reducing to \(\overline W\oplus\overline K\) is the quotient of the local-ring and residue-field decomposition counts:
\[
j^{n^2-r^2-k^2}=j^{2rk}.
\]
For each such lifted decomposition, the invertible restriction \(\overline A|_{\overline W}\) has exactly \(j^{r^2}\) lifts in \(\operatorname{GL}_r(R)\). Hence the fiber has size \(j^{2rk+r^2}=j^{n^2-k^2}\). Since there are \(j^{n^2}\) unrestricted lifts, the survival proportion is \(j^{-k^2}\).

## Verification
The accompanying `verify.py` directly checks two nonisomorphic four-element local rings, \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\). It enumerates all \(256\) matrices in \(M_2\) over each ring and, for every matrix, searches all \(256\) possible candidates for a group inverse and tests the three defining equations. Both rings give exactly \((1,48,96)\) matrices in residue ranks \((0,1,2)\), for a total of \(145\). It also checks every residue fiber over \(M_2(\mathbb F_2)\) against the formula \(j^{n^2-k^2}\) and confirms that non-group-invertible residue matrices have no group-invertible lifts.

These finite checks test the theorem on rings of different characteristic and multiplication law. They are not a substitute for the all-ring proof.

## Relationship to prior work
Cao, Ge, Wang, and Zhang studied existence and formulas for group inverses of two classes of block matrices over rings; their paper was published online on 12 September 2013 and lists MSC \(15A09\) first. That work supplies a ring-level generalized-inverse context but does not enumerate the group-invertible locus of full matrix rings over finite local rings.

Zhong and Zhang later studied group inverses for matrices over the real dual numbers. Their Theorem 3.2 gives a block criterion for a dual matrix whose prime part has index one. In the square-zero local-ring specialization, that criterion is compatible with the lift law above, but it neither treats arbitrary finite local rings nor gives the rank spectrum or uniform fiber cardinalities.

Dolžan counted and bounded idempotents in finite matrix rings. In the local case, that paper uses the same finite-local general-linear-group cardinality and an orbit argument for idempotents. It is a close enumerative comparison, but its object is the idempotent locus rather than the group-invertible locus, and its formulas do not imply the image-rank spectrum above.

## Limitations
The theorem uses locality essentially: it ensures that the image and kernel direct summands of a group-invertible endomorphism are free and have well-defined ranks. For a general finite commutative ring, a decomposition into local factors replaces the scalar rank by a rank vector; that routine product extension is not included. No claim is made about matrices of Drazin index greater than one.

The literature search found no exact enumeration of group-invertible matrices over finite local rings under the formulations checked. A residual originality risk remains that an older finite-semigroup or generalized-inverse source not indexed by the searched terminology may contain an equivalent count.

## References
1. C. Cao, Y. Ge, Y. Wang, H. Zhang, “Group inverse for two classes of \(2\times2\) block matrices over rings,” *Computational and Applied Mathematics* \(33\) (2014), 469–479. DOI: 10.1007/s40314-013-0075-x. Published online 12 September 2013.
2. J. Zhong, Y. Zhang, “Dual group inverses of dual matrices and their applications in solving systems of linear dual equations,” *AIMS Mathematics* \(7\) (2022), 7606–7624. DOI: 10.3934/math.2022427.
3. D. Dolžan, “Bounds for the number of idempotents in finite rings,” *Communications in Algebra* \(49\) (2021), 4800–4807. DOI: 10.1080/00927872.2021.1929277.
