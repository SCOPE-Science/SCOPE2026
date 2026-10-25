# Pseudo-Frobenius spectra for consecutive-deletion Sally numerical semigroups

## Finding

Let \(e,k,j\) be integers with \(k\geq3\), \(e\geq 2k+1\), and \(1\leq j\leq e-k-1\). Define the numerical semigroup
\[
S=S(e,k,j)=\big\langle e+a:0\leq a\leq e-1,\ a\notin[j,j+k-1]\big\rangle.
\]
Intervals of integers are inclusive. The multiplicity of \(S\) is \(e\), its embedding dimension is \(\nu=e-k\), and its largest minimal generator is \(2e-1\).

Write \(\operatorname{PF}(S)\) for the set of pseudo-Frobenius numbers: integers \(z\notin S\) such that \(z+s\in S\) for every nonzero \(s\in S\). Then
\[
\boxed{\operatorname{PF}(S)=
\begin{cases}
[2e+2j-1,\,2e+j+k-1],&1\leq j\leq k,\\
[j+k,\,e-1]\ \cup\ [e+j,\,e+j+k-1],&k<j\leq e-k-1.
\end{cases}}
\]
In particular its Cohen--Macaulay type \(t(S)=|\operatorname{PF}(S)|\) is
\[
\boxed{t(S)=\begin{cases}k-j+1,&j\leq k,\\e-j,&j>k.\end{cases}}
\]
For each fixed \(e,k\), the deletion position \(j\) induces a **bijection** from \(\{1,\ldots,e-k-1\}\) onto the full type spectrum \(\{1,\ldots,e-k-1\}\). Thus every possible integer type between \(1\) and \(\nu-1\) occurs **exactly once** within this natural fixed-multiplicity, fixed-embedding-dimension family.

For any field \(K\), let \(K[S]\) be the semigroup algebra, presented as a quotient of the polynomial ring on its \(\nu\) minimal generators. Its last nonzero total Betti number is exactly
\[
\beta_{\nu-1}(K[S])=t(S).
\]
Finally, the almost-symmetric defect \(\Delta(S)=2g(S)-F(S)-t(S)\) satisfies
\[
\boxed{\Delta(S)=\begin{cases}2(k-j),&j\leq k,\\k-1,&j>k,\end{cases}}
\]
so \(S\) is almost symmetric if and only if \(j=k\), in which case it is symmetric. In this range there are no nonsymmetric almost-symmetric members.

## Assumptions and scope

The ranges \(k\geq3\), \(e\geq2k+1\) and \(1\leq j\leq e-k-1\) are part of the theorem, not experimental cutoffs. In particular the deleted interval does not remove \(e\) or \(2e-1\). Because every listed positive generator lies between \(e\) and \(2e-1\), none is a sum of two nonzero semigroup elements, and all are minimal. The semigroup is cofinite by the proof below.

For a numerical semigroup \(S\), \(g(S)=|\mathbb N\setminus S|\) is the genus and \(F(S)=\max(\mathbb N\setminus S)\) is its Frobenius number. A numerical semigroup is almost symmetric precisely when \(2g(S)=F(S)+t(S)\); symmetric semigroups have type one and satisfy the same equality. The theorem does not treat \(e\leq2k\), nonconsecutive deletions, or Betti numbers other than the last one.

## Proof

**1. Gap geometry.** Put \(A=[0,j-1]\), \(B=[j+k,e-1]\); these are precisely the offsets of the generators. In the first positive block \([e,2e-1]\), the gaps are \([e+j,e+j+k-1]\). Numbers in \([1,e-1]\) are also gaps.

First suppose \(j>k\). The two-generator offset sums include \(A+A=[0,2j-2]\) and \(0+B=B\). Since \(2j-2\geq j+k-1\), their union contains every integer in \([0,e-1]\). Hence \([2e,3e-1]\subseteq S\). Together with the undeleted generators \([e+j+k,2e-1]\), this gives \(e\) consecutive semigroup elements starting at \(e+j+k\); repeated addition of \(e\) proves that every larger integer belongs to \(S\). Therefore
\[
\mathbb N\setminus S=[1,e-1]\cup[e+j,e+j+k-1]
\quad(j>k).
\]

Now suppose \(j\leq k\). At the two-generator level, \(A+A=[0,2j-2]\), and \(A+B\) contains \([j+k,e-1]\). The other two-generator sums \(B+B\) begin at \(2(j+k)>j+k-1\). Therefore the missing offsets in \([0,e-1]\) are exactly \([2j-1,j+k-1]\), so the third gap block is \([2e+2j-1,2e+j+k-1]\).

We must still prove that no later gaps remain. The whole interval \([2e+j+k,3e-1]\) belongs to \(S\). Also \([3e,3e+j+k-1]\subseteq S\), as follows. Any offset \(r\in[0,3j-3]\) is a sum of three offsets from \(A\), hence \(3e+r\in S\). For any \(r\geq2(j+k)-e\) with \(r\leq j+k-1\), the integer \(e+r\) belongs to \(B+B=[2(j+k),2e-2]\), hence \(3e+r\in S\) as a sum of two generators. The inequality \(e\geq2k+1\) gives \(2(j+k)-e\leq2j-1\). If \(j\geq2\), then \(3j-3\geq2j-1\), and the two ranges cover every \(r\in[0,j+k-1]\). When \(j=1\), the first range contains \(0\) and the second starts no later than \(1\), so the same conclusion holds. Thus \([2e+j+k,3e+j+k-1]\) is a run of \(e\) consecutive elements of \(S\). Adding \(e\) repeatedly gives all larger elements. Consequently
\[
\mathbb N\setminus S=[1,e-1]\cup[e+j,e+j+k-1]
\cup[2e+2j-1,2e+j+k-1]\quad(j\leq k).
\]
All three intervals are disjoint under the assumed ranges. This proves cofiniteness and both exact gap descriptions.

**2. Pseudo-Frobenius numbers when \(j>k\).** Every gap in \([e+j,e+j+k-1]\) is pseudo-Frobenius, since adding any generator gives a number larger than \(F(S)=e+j+k-1\). A gap \(x\in[j+k,e-1]\) is also pseudo-Frobenius, because \(x+s\geq e+j+k\) for every positive \(s\in S\). Conversely, for \(x\in[1,j-1]\), the generator \(e+(j-x)\) sends \(x\) to the gap \(e+j\). For \(x\in[j,j+k-1]\), the generator \(e\) sends \(x\) to a deleted number. These are all the remaining gaps, establishing the second line of the formula.

**3. Pseudo-Frobenius numbers when \(j\leq k\).** Each gap in the third (highest) interval is pseudo-Frobenius because addition of any nonzero semigroup element exceeds its Frobenius endpoint. No lower gap is pseudo-Frobenius. For \(x\in[1,j-1]\), add the generator \(e+(j-x)\) to reach \(e+j\), a gap. For \(x\in[j,j+k-1]\), add \(e\) to reach a deleted generator. For \(x\in[j+k,e-1]\), let \(b=e+j+k-1-x\). Then \(b\in B\), and \(x+(e+b)=2e+j+k-1\), the highest gap. Finally, for \(x=e+j+r\), \(0\leq r\leq k-1\), choose \(a=\max(0,j-1-r)\in A\). The sum \(x+(e+a)=2e+j+r+a\) lies in the third gap interval because \(j-1\leq r+a\leq k-1\). This exhausts the gap set and proves the first line of the formula.

**4. Types, spectrum and almost symmetry.** Counting the gaps in Step 1 and the pseudo-Frobenius intervals in Steps 2--3 yields
\[
(g,F,t)=\begin{cases}
(e+2k-j,\,2e+j+k-1,\,k-j+1),&j\leq k,\\
(e+k-1,\,e+j+k-1,\,e-j),&j>k.
\end{cases}
\]
Direct substitution gives the displayed defect formula. Since \(k\geq3\), its second branch is strictly positive, while the first vanishes exactly when \(j=k\); the latter also has type one. As \(j\) runs from \(1\) to \(k\), the type values run from \(k\) down to \(1\). When the range \(j>k\) is nonempty, its types run from \(e-k-1\) down to \(k+1\). These are disjoint consecutive intervals covering \(1\) through \(e-k-1\), each exactly once.

**5. The last Betti number.** Let \(P=K[X_1,\ldots,X_\nu]\) be the polynomial ring mapping its variables to the monomials of the minimal generators of \(S\), with \(X_1\mapsto t^e\). The one-dimensional ring \(R=K[S]\subseteq K[t]\) is Cohen--Macaulay; \(t^e\) is a nonzerodivisor. Quotienting a minimal \(P\)-free resolution of \(R\) by \(X_1\) gives a minimal resolution of \(R/(t^e)\) over \(K[X_2,\ldots,X_\nu]\). The last Koszul homology of that Artinian quotient is its socle. A monomial basis of the quotient is indexed by the Apéry set \(\operatorname{Ap}(S,e)=\{w\in S:w-e\notin S\}\), and its socle monomials are exactly \(t^{e+z}\) for \(z\in\operatorname{PF}(S)\). Thus the socle dimension, and therefore the last total Betti number \(\beta_{\nu-1}(R)\), equals \(|\operatorname{PF}(S)|\). This argument is independent of the characteristic of \(K\).

## Verification

The file `verify.py` is a standalone standard-library Python program. Run it from this folder with `python3 verify.py --max-e 48`. It independently computes Apéry minima via shortest paths on residue classes modulo \(e\), derives membership, enumerates actual gaps and pseudo-Frobenius numbers, and compares them with every displayed formula for all admissible parameters with \(7\leq e\leq48\). For \(e\leq22\), it additionally checks the shortest-path membership test against a separate forward dynamic-programming algorithm. It verifies the complete type spectrum at each admissible \((e,k)\). The observed output was `VERIFY_OK cases=10857 checked_gap_counts=530299 e_max=48`. These finite checks do **not** constitute the proof for all integers; Steps 1--5 do.

For example, taking \(e=12\) and \(k=3\), the admissible positions \(j=1,\ldots,8\) produce types \(3,2,1,8,7,6,5,4\), a permutation of \(1,\ldots,8\). The semigroups have the same multiplicity \(12\), embedding dimension \(9\), and width \(11\), while their Cohen--Macaulay types vary over the full allowed interval.

## Relationship to prior work

Goel, Şahin, Singh and Srinivasan, *Numerical Semigroups of Sally Type II* (arXiv:2512.10812, first posted December 11, 2025), compute Cohen--Macaulay types and pseudo-Frobenius information for Sally semigroups with one or two deleted generators; their Theorems 2.2 and 3.3 do not treat the regime of three or more consecutive deleted generators. Singh and Srinivasan, *Structure and Symmetry of Sally Type Semigroup Rings* (arXiv:2512.18136, first posted December 19, 2025), study exactly the consecutive-deletion family, compute Frobenius numbers and genera and classify Gorenstein members; the accessible full text does not give the full pseudo-Frobenius sets or the type spectrum for \(k\geq3\). The prior Gorenstein criterion \(j=k\) is **not** claimed as new. The present contribution is the exact all-position pseudo-Frobenius classification, its complete bijective type spectrum, the resulting terminal Betti numbers, and the sharp almost-symmetry defect.

The earlier paper by Dubey, Goel, Şahin, Singh and Srinivasan, *Numerical Semigroups of Sally Type* (arXiv:2507.11738, first posted July 15, 2025), concerns the two-deletion setting and related ring invariants. Standard general descriptions of pseudo-Frobenius numbers using Apéry sets, including work of Rosales and García-Sánchez, are compatible with but do not directly state the closed consecutive-deletion formulas above.

## Limitations

Novelty here is assessed relative to identified accessible literature and published research records, not proven by exhaustive coverage of mathematical publication databases. Equivalent formulas in unindexed sources or in literature using different terminology remain possible. The theorem requires \(e\geq2k+1\); when \(e\leq2k\), extra higher-level gaps can appear and the stated formulas are not asserted. The result fixes a single consecutive deleted block; arbitrary deletion patterns and intermediate Betti numbers remain outside its scope. The computation checks finitely many instances and supplies no independent infinite verification.

## References

1. K. Goel, N. Şahin, S. Singh and H. Srinivasan, *Numerical Semigroups of Sally Type II*, arXiv:2512.10812v2 (first public version 2025-12-11), https://arxiv.org/html/2512.10812v2.
2. S. Singh and H. Srinivasan, *Structure and Symmetry of Sally Type Semigroup Rings*, arXiv:2512.18136 (first public version 2025-12-19), https://arxiv.org/abs/2512.18136.
3. S. Dubey, K. Goel, N. Şahin, S. Singh and H. Srinivasan, *Numerical Semigroups of Sally Type*, arXiv:2507.11738 (first public version 2025-07-15), https://arxiv.org/abs/2507.11738.
4. J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*, Developments in Mathematics 20, Springer, 2009 (standard Apéry and pseudo-Frobenius theory).
