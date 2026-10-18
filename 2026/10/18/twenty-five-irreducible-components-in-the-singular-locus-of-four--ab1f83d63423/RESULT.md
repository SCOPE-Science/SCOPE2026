# Twenty-five irreducible components in the singular locus of four orthogonal vectors

## Finding
Let \(M\ge5\) be an integer and let \(V=\mathbb C^M\) carry any nondegenerate symmetric bilinear form \(\langle\cdot,\cdot\rangle\). Set
\[
X_M=\{(v_1,v_2,v_3,v_4)\in V^4:\langle v_i,v_j\rangle=0\text{ for }i<j\}.
\]
Then \(X_M\) is an integral complete intersection of dimension \(4M-6\). Its **reduced singular locus has exactly twenty-five irreducible components**, all of dimension \(2M-1\), hence pure codimension \(2M-5\) in \(X_M\). Their complete geometric classification has four types:

1. Six components \(A_{ij}\), one for each unordered pair \(\{i,j\}\), on which \(v_i=v_j=0\); the remaining pair is orthogonal.
2. Four components \(T_i\), one for each zero column \(v_i=0\), where the other three vectors span a totally isotropic subspace of dimension at most two.
3. Twelve components \(R_{i\mid j}\), one for each ordered choice of distinct indices \(i,j\). Here \(v_i=0\), the other two indices \(k,l\notin\{i,j\}\) have \(v_k,v_l\) on a common isotropic line \(\ell\), and \(v_j\in\ell^\perp\). The component is the closed incidence image, including its degenerations when the two vectors on \(\ell\) vanish.
4. Three components \(P_{ij\mid kl}\), one for each partition of the indices into unordered pairs. Both pairs lie on (possibly equal) isotropic lines \(\ell_1,\ell_2\) with \(\ell_1\perp\ell_2\). This again denotes the closed incidence image.

In particular, the four types occur with multiplicities \(6+4+12+3=25\) among the **irreducible components of the reduced singular support**; no statement about the scheme-theoretic multiplicities of the Jacobian ideal is made.

## Assumptions and scope
All varieties and dimension statements are over \(\mathbb C\); the bilinear form is symmetric and nondegenerate. \(\operatorname{Sing}(X_M)_{\mathrm{red}}\) is the reduced support of the intrinsic scheme singular locus. The labels \(i,j,k,l\) range over \(\{1,2,3,4\}\), and lines and planes are vector subspaces of \(V\). A totally isotropic plane \(U\) means \(\langle U,U\rangle=0\). In the definitions of \(R\) and \(P\), lines are allowed to coincide when appropriate, and incidence closure is essential when one or more defining vectors vanish. For \(M\ge5\), the isotropic Grassmannian \(\operatorname{OGr}(2,V)\) is irreducible.

## Proof
**1. The Jacobian criterion reduces to disjoint-support column dependencies.** The defining six quadrics form a prime complete-intersection ideal for \(M\ge5\), by the prime and complete-intersection thresholds of Casabella–Sammartano (alternatively, the zero-fiber results of Xie in this regime). Let \(B\) be the \(M\times4\) matrix whose columns are the \(v_i\). A linear dependence between the six differentials corresponds exactly to a nonzero symmetric \(4\times4\) matrix \(C\) with vanishing diagonal and \(BC=0\): this follows by differentiating \(\langle v_i,v_j\rangle\) in each column. Because \(X_M\) has codimension six, singularity is equivalent to the existence of such a \(C\).

If \(\operatorname{rank} B\ge3\), then \(\operatorname{rank} C\le1\). A nonzero symmetric rank-one matrix over \(\mathbb C\) is \(\lambda aa^\top\); its zero diagonal forces \(a=0\), a contradiction. Thus every singular point has rank at most two.

Suppose \(\operatorname{rank} B=2\). Then \(C\ne0\) has rank exactly two. Factor \(C=D^\top J D\), where \(D\) has two rows and \(J\) is a nonsingular symmetric \(2\times2\) matrix. The four columns of \(D\) are \(J\)-isotropic because \(C_{ii}=0\). In a two-dimensional nondegenerate quadratic space, all nonzero isotropic vectors lie on exactly two lines. Consequently there are disjointly supported nonzero vectors \(a,b\in\mathbb C^4\) such that
\[
C=ab^\top+ba^\top,\qquad Ba=Bb=0.
\]
Indeed the first identity follows from the two isotropic directions, and \(BC=0\) implies both kernel equations since \(a,b\) are independent. Because these are two nontrivial dependencies on disjoint sets of at most four column labels, either some column is zero and the other three are linearly dependent, or the columns split into two proportional pairs. Conversely, both patterns give a nonzero hollow symmetric \(C\) annihilated by \(B\). The same description covers rank-at-most-one singular points by direct inclusion: an anisotropic rank-one orthogonal tuple has at most one nonzero column, while an isotropic rank-one tuple has all nonzero columns on an isotropic line. Therefore, *set-theoretically*,
\[
\operatorname{Sing}(X_M)=
\bigcup_i\{v_i=0,\ \operatorname{rank}(v_j:j\ne i)\le2\}
\ \cup\!\!\bigcup_{\{ij\mid kl\}}
\{\operatorname{rank}(v_i,v_j)\le1,\ \operatorname{rank}(v_k,v_l)\le1\}
\quad\text{inside }X_M.
\]
This description concerns points, not an asserted radical-ideal equality.

**2. The zero-column loci split into three geometric types.** On \(v_i=0\), let \(W\) be the span of the other three mutually orthogonal columns and assume \(\dim W\le2\). If \(\dim W=2\), the restriction of the form to \(W\) has rank \(2,1\), or \(0\). In rank two, at least one of the three columns must vanish (otherwise three nonzero pairwise-orthogonal vectors would occur in a nondegenerate two-plane), giving \(A_{ij}\). In rank one, the radical is an isotropic line, and the only column not in it is a distinguished anisotropic column \(v_j\); this is \(R_{i\mid j}\). In rank zero, all three columns span a totally isotropic plane, giving \(T_i\). If \(\dim W\le1\), the same three closed families cover the point: an anisotropic line supports at most one nonzero column, whereas an isotropic line extends to a totally isotropic plane because \(M\ge5\). Thus the zero-column loci are exactly the union of all \(A,T,R\).

**3. Proportional-pair loci produce no further components.** If all four columns in a proportional-pair locus are nonzero, the orthogonality equation within each pair forces its line to be isotropic, and cross-pair orthogonality makes the two lines perpendicular. This is precisely \(P_{ij\mid kl}\). If a column vanishes, the other three have rank at most two and are already in the preceding union. Hence the twenty-five displayed families exhaust the reduced singular support.

**4. Irreducibility, dimension, and noncontainment.** Each \(A_{ij}\) is an irreducible quadric hypersurface in \(V^2\), of dimension \(2M-1\). The incidence defining \(T_i\) is the total space of a rank-six vector bundle over \(\operatorname{OGr}(2,V)\), which is irreducible of dimension \(2M-7\); its image is closed, irreducible, and has generic unique isotropic plane, hence dimension \(2M-1\). For \(R_{i\mid j}\), choose an isotropic line \(\ell\) in the smooth quadric \(Q^{M-2}\), two vectors on \(\ell\), and \(v_j\in\ell^\perp\). This irreducible incidence has dimension \((M-2)+2+(M-1)=2M-1\), is closed under proper projection of the projective line parameter, and is generically one-to-one onto its image. For \(P_{ij\mid kl}\), the space of perpendicular ordered isotropic lines has dimension \((M-2)+(M-3)=2M-5\): over a fixed first line, the second-line locus is an irreducible rank-\((M-2)\) quadric cone because \(M\ge5\). Choosing four vectors along those lines adds four dimensions. Proper incidence projection again gives a closed irreducible image of dimension \(2M-1\).

The generic configurations distinguish all components: \(A\) has two zero columns and two independent anisotropic columns; \(T\) has exactly one zero column and three nonzero isotropic vectors spanning a plane; \(R\) has exactly one zero column, one marked anisotropic column, and two nonzero collinear isotropic columns; \(P\) has no zero column, with two independently marked proportional isotropic pairs. Within each type, these generic patterns distinguish the index choices. As all candidate components have the same dimension and none coincides, none contains another. The list is therefore complete.

## Verification
The accompanying self-contained Python program `verify.py` reconstructs all \(25\) indexed types with explicit vectors in a split nondegenerate quadratic space for \(M=5,6,7,8\). It checks all orthogonality equations and verifies that the six-by-\(4M\) Jacobian has rank exactly five at each rank-two witness, while rank-three and rank-four smooth witnesses have rank six. It additionally exhausts all rank-two hollow symmetric four-by-four matrices over \(\mathbb F_3\), checking bipartite cross-support. Its successful output is `VERIFY_OK witness_cases=108 hollow_rank_two_mod3=116`. These finite tests check algebraic details, **not** the general theorem: the proof above supplies the characteristic-zero rank lemma and the all-\(M\) decomposition.

## Relationship to prior work
Ying Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1 (1 October 2026), studies the same Gram zero-fiber family and establishes global rational-singularity and threshold properties, without giving the four-column twenty-five-component reduced singular-locus decomposition. Casabella and Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1 (31 December 2025), give primality, complete-intersection, component, and smoothness criteria for orthogonal-frame varieties. Their rank/isotropic-stratum descriptions and Jacobian formula are compatible with the calculation above, but the inspected paper does not present its full indexed irreducible singular-support classification. General rank-stratum descriptions alone do not imply the claimed count without the rank-two hollow-matrix splitting and irreducible-incidence argument.

## Limitations
This is a theorem only for \(M\ge5\) and for the **reduced singular support**. The bound avoids the two-component maximal isotropic Grassmannian in dimension four. No scheme-theoretic primary decomposition, embedded Jacobian components, transverse local analytic forms, component degrees, intersection-incidence poset, or positive-characteristic extension is asserted. General LSS-ideal and orthogonal-frame literature may encode parts of the classification implicitly; published-priority uniqueness is not certified.

## References
- Ying Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1 (1 October 2026), especially Sections 1 and 2 and the zero-fiber discussion.
- Laura Casabella and Alessio Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1 (31 December 2025), especially Sections 3, 5, 6, and 7.
