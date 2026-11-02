# Commuting square-zero rank-one Nijenhuis operators on \(\mathfrak{sl}_2\): exact counts and component growth

## Finding
Let \(k\) be a field of characteristic different from \(2\). On \(\mathfrak g=\mathfrak{sl}_2(k)\) with basis \(e,f,h\) and brackets \([e,f]=h\), \([h,e]=2e\), \([h,f]=-2f\), a linear map is algebraic Nijenhuis when
\[
[Nx,Ny]-N([Nx,y]+[x,Ny])+N^2[x,y]=0
\]
for all \(x,y\). We study ordered, pairwise-commuting tuples of maps of rank at most one, each square-zero and algebraic Nijenhuis. All the counts below include the zero map.

**Single-operator classification.** For \(N=v\otimes\varphi\) of rank one, with \(v=ae+bf+ch\ne0\) and \(\varphi=ue^*+wf^*+zh^*\ne0\), the algebraic Nijenhuis condition is equivalent to
\[
4uw+z^2=0.
\]
The square-zero condition is exactly \(\varphi(v)=au+bw+cz=0\). In particular the projective covector lies on a smooth split conic \(\mathcal C\subset\mathbb P(\mathfrak g^*)\); every projective covector on this conic admits a two-dimensional space of square-zero image vectors.

**Simultaneous annihilation.** For any two rank-at-most-one square-zero maps, commutativity implies that their two ordered products vanish. Thus all tuples in question obey \(N_iN_j=0\) for every pair of indices.

**Finite-field enumeration.** Suppose \(k=\mathbb F_q\) with \(q\) odd and let \(m\ge1\). For \(s\ge1\), the number of compatible tuples with nonzero operators in any given set of exactly \(s\) positions and zero operators elsewhere is
\[
C_s(q)=(q+1)(q^2-1)^s+\binom{q+1}{2}(2^s-2)(q-1)^s,
\qquad C_0(q)=1.
\]
The complete joint-rank generating polynomial (the exponent at position \(i\) is \(\operatorname{rank}N_i\)) is
\[
\begin{aligned}
\Phi_{m,q}(T_1,\ldots,T_m)
={}&1+(q+1)\left[\prod_{i=1}^m(1+(q^2-1)T_i)-1\right]\\
&+\binom{q+1}{2}\left[\prod_{i=1}^m(1+2(q-1)T_i)
-2\prod_{i=1}^m(1+(q-1)T_i)+1\right].
\end{aligned}
\]
Consequently the number of all compatible ordered tuples is
\[
\boxed{|X_m(\mathbb F_q)|=1+(q+1)(q^{2m}-1)
+\binom{q+1}{2}\bigl((2q-1)^m-2q^m+1\bigr).}
\]
This counts actual operators, not similarity classes, and works for every positive integer \(m\).

**Geometric components.** Over an algebraic closure of any field of characteristic different from \(2\), the *reduced* affine variety \(X_m\) defined by these rank, square-zero, Nijenhuis and commutativity equations is irreducible of dimension \(3\) when \(m=1\). For \(m\ge2\), it has exactly \(2^{m-1}\) geometrically irreducible components: one of dimension \(2m+1\), and \(2^{m-1}-1\) of dimension \(m+2\). They are indexed by a common-covector-line family and by unordered nontrivial bipartitions of the tuple positions, respectively. Thus \(X_m\) is non-equidimensional for every \(m\ge2\).

## Assumptions and scope
The Nijenhuis identity is that of an ordinary Lie algebra, not an associative or a higher-arity Lie algebra. The underlying Lie algebra is the split three-dimensional \(\mathfrak{sl}_2\), and the maps have ordinary linear rank \(0\) or \(1\); characteristic \(2\) is excluded. The finite-field formula assumes an odd prime-power cardinality \(q\). The geometric assertion concerns irreducible components of the underlying *reduced* affine variety; no claim is made about nonreduced scheme structure. The compatible tuple length \(m\) is arbitrary and positive.

## Proof
**1. Direct torsion reduction.** Substitute \(N(x)=\varphi(x)v\) in the Nijenhuis identity. In the indicated basis and for \(Q(\varphi)=4uw+z^2\), its values on the three basis wedges \((e,f),(e,h),(f,h)\), respectively, are
\[
 cQ(\varphi)v,\qquad -bQ(\varphi)v,\qquad aQ(\varphi)v.
\]
Because \(v\ne0\), all torsions vanish exactly when \(Q(\varphi)=0\). Also \(N^2(x)=\varphi(v)N(x)\), establishing the square-zero criterion. The quadratic form \(4uw+z^2\) is nonsingular and isotropic in odd characteristic, hence its projective zero locus is a smooth conic isomorphic to \(\mathbb P^1\), with exactly \(q+1\) rational points over \(\mathbb F_q\).

**2. Commutativity forces annihilation.** Let \(A=v\otimes\varphi\) and \(B=w\otimes\psi\) be nonzero rank-one square-zero maps. Their products are \(AB=\varphi(w)v\otimes\psi\) and \(BA=\psi(v)w\otimes\varphi\). If they are equal and nonzero, equality of rank-one images and row lines implies \(v,w\) are proportional and \(\varphi,\psi\) are proportional; therefore \(A,B\) are proportional, which contradicts \(AB\ne0\) because \(A^2=0\). Thus commuting implies \(AB=BA=0\); the converse is immediate. If one map is zero there is nothing to prove.

**3. At most two covector lines.** For a compatible tuple whose nonzero members are \(v_i\otimes\varphi_i\), every \(v_i\) annihilates \(W=\operatorname{span}\{\varphi_j\}\). Since \(v_i\ne0\) in a three-dimensional space, \(\dim W\le2\). If \(\dim W=1\), the covectors share one of the \(q+1\) conic lines, and every chosen \(v_i\) is an arbitrary nonzero vector in a fixed two-dimensional annihilator: \((q+1)(q^2-1)^s\) tuples for a specified set of \(s\) nonzero positions.

If \(\dim W=2\), the projective line \(\mathbb P(W)\) intersects the nonsingular conic in at most two distinct points, counted over an algebraic closure. As it already contains at least two distinct rational points from the \(\varphi_i\), it contains *exactly* these two conic points. Choose their unordered pair in \(\binom{q+1}{2}\) ways; assign the \(s\) labeled positions to the two points, using both, in \(2^s-2\) ways; and choose each \(v_i\ne0\) in the common one-dimensional annihilator in \(q-1\) ways. This yields the second summand of \(C_s\). The two cases exhaust all tuples without overcounting. The multivariate polynomial follows by binomial expansion on each fixed nonzero support, and setting all variables to one gives the displayed total.

**4. Geometric components.** Work over an algebraic closure. The closure \(A\) of tuples with all nonzero covectors on one isotropic projective line has an irreducible parameter space: a point of \(\mathcal C\) (dimension one), followed by \(m\) unrestricted vectors in its two-dimensional annihilator (total fiber dimension \(2m\)). Its generic parametrization is one-to-one, so \(\dim A=2m+1\).

For any nonempty proper subset \(S\subsetneq\{1,\ldots,m\}\), define \(B_S\) as the closure of tuples whose covectors on \(S\) lie on one isotropic line, those on the complement on a *different* isotropic line, and whose images lie in the common annihilator of the two lines. The open parameter space has two freely varying distinct points of the conic (dimension two) and \(m\) free scalars in their common image line. It is irreducible of dimension \(m+2\), and the generic tuple recovers the unordered pair of lines, so this is also the dimension of \(B_S\). Relabeling the two lines identifies \(B_S=B_{S^c}\), giving \(2^{m-1}-1\) distinct such closures for \(m\ge2\).

The classification in step 3 over the algebraic closure shows these closed irreducible sets cover the entire reduced solution locus, including zero coordinates (which lie in their closures). A generic point of \(A\) has image-span dimension two, but every \(B_S\) has image-span dimension at most one. Conversely a generic point of \(B_S\) has two distinct nonzero covector lines, whereas every point of \(A\) has covector-span dimension at most one. Generic covector assignments distinguish two different unordered partitions. Hence no listed set is contained in another, so all are the irreducible components. For \(m=1\) only \(A\) occurs.

## Verification
The standalone program `check_nij.py` reconstructs the Lie bracket from the displayed structure constants and checks the *original* torsion identity on each basis wedge for **every rank-one linear map** over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and the genuine extension field \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). It then independently checks all pairwise compositions, commutation, and the complete ordered pair and triple counts. Observed counts for nonzero square-zero Nijenhuis maps; pairs; triples are: \((32,369,3345)\) for \(q=3\), \((144,4225,100945)\) for \(q=5\), \((384,21217,983521)\) for \(q=7\), and \((800,71361,5469921)\) for \(q=9\). Each matches the exact formulas. Reproduce using `python3 check_nij.py`; the captured output is in `check_output.txt`. These finite checks do not constitute an infinite proof or a computational certification of the geometric component decomposition.

## Relationship to prior work
Panasyuk [1] develops algebraic Nijenhuis operators, including the classical subalgebra-splitting constructions for \(\mathfrak{sl}_2\), and focuses on associated Poisson pencils. The algebraic Nijenhuis identity and the existence of many low-rank examples are not claimed as new. Ngo and Šivic [2] study the irreducibility of the **unrestricted** commuting nilpotent matrix variety, which is irreducible in matrix size three; that does not imply irreducibility of the restricted rank-one Nijenhuis locus, and indeed this locus has many components. Liu, Sheng, Zhou, and Bai [3] develop higher Lie-algebra Nijenhuis operators but do not provide the present finite-field joint distribution. Zhikhareva [4] treats regular semisimple operators on real and complex three-dimensional Lie algebras, rather than nilpotent square-zero operators. The new asserted content is the exact arbitrary-arity compatibility census together with the complete, non-equidimensional component classification; the elementary torsion reduction is the proof ingredient, not a priority claim about all Nijenhuis operators.

## Limitations
Only rank-at-most-one, square-zero algebraic Nijenhuis operators on the specified three-dimensional split Lie algebra are covered. Ordinary commuting pairs of arbitrary Nijenhuis operators, characteristic two, nonsplit forms and higher-dimensional Lie algebras are outside the theorem. The geometric statement concerns the reduced variety only. The finite-field computer checks cover only four fields and tuples of lengths up to three, whereas the general theorem is proved symbolically. The publication-priority assessment is provisional; an unidentified general theorem about rank-one Nijenhuis tuples or constrained commuting varieties could subsume the result. No independent mathematical audit has been performed.

## References
[1] A. Panasyuk, *Algebraic Nijenhuis operators and Kronecker Poisson pencils*, arXiv:math/0504337v1 (public 2005-04-16), https://arxiv.org/abs/math/0504337.

[2] N. V. Ngo and K. Šivic, *On varieties of commuting nilpotent matrices*, arXiv:1308.4438v1 (public 2013-08-20), https://arxiv.org/abs/1308.4438.

[3] J. Liu, Y. Sheng, Y. Zhou and C. Bai, *Nijenhuis operators on n-Lie algebras*, arXiv:1601.02356v1 (public 2016-01-11), https://arxiv.org/abs/1601.02356.

[4] E. S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1 (public 2024-10-14), https://arxiv.org/abs/2410.10536.
