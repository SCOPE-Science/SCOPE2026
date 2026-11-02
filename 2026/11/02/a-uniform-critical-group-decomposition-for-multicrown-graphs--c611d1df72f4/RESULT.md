# A uniform critical-group decomposition for multicrown graphs

## Finding

For integers \(n\geq 3\) and \(k\geq 0\), define \(G_{n,k}\) to be the connected bipartite multigraph with vertex classes \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\), one edge \(a_i b_j\) for each \(i\ne j\), and exactly \(k\) parallel edges \(a_i b_i\) for each \(i\). Thus \(G_{n,0}\) is the ordinary crown graph and \(G_{n,1}=K_{n,n}\). Put
\[
 g=\gcd(n,k-1),\qquad q=n-2+2k,\qquad t=n-1+k.
\]
With \(\mathbb Z_s=\mathbb Z/s\mathbb Z\) (and \(\mathbb Z_1\) trivial), the critical/sandpile group is
\[
 \boxed{K(G_{n,k})\cong
 (\mathbb Z_g)^{n-2}\oplus
 \bigl(\mathbb Z_{nq/g}\bigr)^{n-2}\oplus
 \mathbb Z_{tq}.}
\]
This is a cyclic direct-sum decomposition, not necessarily listed in invariant-factor order. It implies the exact spanning-tree count
\[
 \boxed{\tau(G_{n,k})=n^{n-2}q^{n-1}t.}
\]
The decomposition includes the even-\(n\) cases with \(\gcd(n,k-1)>1\) not covered by the explicit formulas in the principal previously published treatment of multicrowns.

For example, when \(n\) is even and \(k=3\), the critical group is
\[
 K(G_{n,3})\cong (\mathbb Z_2)^{n-2}\oplus
 \bigl(\mathbb Z_{n(n+4)/2}\bigr)^{n-2}\oplus
 \mathbb Z_{(n+2)(n+4)}.
\]
In canonical invariant-factor order this becomes
\[
 \begin{cases}
 (\mathbb Z_2)^{n-2}\oplus\mathbb Z_{2(n+4)}\oplus
 (\mathbb Z_{n(n+4)/2})^{n-3}\oplus\mathbb Z_{n(n+2)(n+4)/4},&4\mid n,\\[3pt]
 (\mathbb Z_2)^{n-2}\oplus\mathbb Z_{n+4}\oplus
 (\mathbb Z_{n(n+4)/2})^{n-3}\oplus\mathbb Z_{n(n+2)(n+4)/2},&n\equiv2\pmod4.
 \end{cases}
\]
These are non-coprime examples at every even order, and the two residue classes have different invariant-factor structure.

## Assumptions and scope

All graphs are finite, undirected, and connected; parallel edges contribute their multiplicity to the Laplacian. The assertion holds for every integer \(n\ge3\) and every integer \(k\ge0\), without primality or coprimality assumptions. We define \(K(G)\) as the finite torsion subgroup of \(\operatorname{coker}L(G)\) for the integer graph Laplacian \(L(G)\). Equivalently, it is the cokernel of any reduced Laplacian, using a deleted row and the same deleted column. No statement for \(n=2,k=0\), which is disconnected, is included.

## Proof

Set \(m=k-1\), so \(t=n+m\) and \(q=t+m=n+2m>0\). The Laplacian, with the \(a\)-class indexed first, is
\[
 L=\begin{pmatrix}tI_n&-J_n-mI_n\\-J_n-mI_n&tI_n\end{pmatrix},
\]
where \(J_n\) denotes the all-ones matrix. In its integral cokernel presentation, let \(a_i,b_i\) also denote the generators. The \(2n\) relations are
\[
 t a_i-\sum_{j=1}^n b_j-mb_i=0,\qquad
 t b_i-\sum_{j=1}^n a_j-ma_i=0.
\]

Perform an integral unimodular change of generators: set \(u=b_n\), \(z=a_n-b_n\), and, for \(1\le i\le n-1\), \(d_i=a_i-a_n\), \(e_i=b_i-b_n\). The inverse change is \(a_n=u+z\), \(b_n=u\), \(a_i=u+z+d_i\), \(b_i=u+e_i\), so it is invertible over \(\mathbb Z\). Subtracting the relation for \(i=n\) from the corresponding relation for each \(i<n\), we obtain
\[
 td_i-me_i=0,\qquad te_i-md_i=0\qquad (1\le i<n).
\]
The two unsubtracted relations, at \(i=n\), become
\[
 tz-\sum_{i=1}^{n-1}e_i=0,\qquad
 -tz-\sum_{i=1}^{n-1}d_i=0.
\]
The generator \(u\) appears in no relation and supplies the single free \(\mathbb Z\) summand.

Write \(r=n-1\). Use the same unimodular integral transformation on the \(d\)- and \(e\)-coordinates and on the two corresponding families of relations: set
\[
 D_1=\sum_{i=1}^r d_i,\quad D_j=d_j\ (2\le j\le r),\qquad
 E_1=\sum_{i=1}^r e_i,\quad E_j=e_j\ (2\le j\le r).
\]
The determinant of each coordinate transformation is \(1\). Because the relations have the same scalar coefficients in each coordinate, they transform to \(tD_j-mE_j=0\) and \(tE_j-mD_j=0\) for all \(j\). The two extra relations now say \(E_1=tz\) and \(D_1=-tz\). Eliminate \(D_1,E_1\) integrally. Their two corresponding relations reduce to \(-t(t+m)z=0\) and \(t(t+m)z=0\), the same relation up to sign. Thus the cokernel is exactly
\[
 \mathbb Z\ \oplus\ \mathbb Z_{tq}\ \oplus\
 \bigoplus_{j=2}^{n-1}\operatorname{coker}
 \begin{pmatrix}t&-m\\-m&t\end{pmatrix}.
\]
No rational diagonalization or division by a nonunit has been used.

The displayed integral \(2\times2\) matrix has entry gcd \(\gcd(t,m)=\gcd(n,k-1)=g\), determinant \(t^2-m^2=(t-m)(t+m)=nq\), and full rank since \(nq>0\). Its integer Smith normal form is \(\operatorname{diag}(g,nq/g)\), proving the claimed critical-group decomposition.

For the spanning-tree count, the Laplacian above has real eigenvalues \(0\) (multiplicity one), \(2t\) (multiplicity one), \(n\) (multiplicity \(n-1\)), and \(q\) (multiplicity \(n-1\)). This follows by considering the constant symmetric and antisymmetric vectors and, separately, the symmetric and antisymmetric vectors whose \(n\) coordinates sum to zero. The matrix-tree theorem gives \(\tau=(2t)n^{n-1}q^{n-1}/(2n)=tn^{n-2}q^{n-1}\), also equal to the product of the finite cyclic orders found above.

Finally, for even \(n\) and \(k=3\), one has \(g=2\), \(q=n+4\), and \(t=n+2\). The stated invariant factors result by combining one pair of factors of orders \(n(n+4)/2\) and \((n+2)(n+4)\) into their gcd and lcm. The gcd is \(2(n+4)\) if \(4\mid n\), and \(n+4\) if \(n\equiv2\pmod4\); the remaining factors already form a divisibility chain. This proves the residue-class formulas.

## Verification

The standalone `verify_snf.py` directly builds the full weighted multigraph Laplacian, deletes one row and column, and computes its integer Smith normal form using SymPy. It separately Smith-normalizes the predicted diagonal presentation. All ninety pairs \(3\le n\le12\), \(0\le k\le8\) agree, including non-coprime and zero-matching cases.

The standalone `verify_treecount.py` uses a separate, pure-integer fraction-free Bareiss determinant implementation (no Smith-form library) on the directly constructed reduced Laplacian. It agrees with the independently derived spanning-tree product for all eighty-eight pairs \(3\le n\le13\), \(0\le k\le7\). Both scripts print explicit successful-comparison counts and raise exceptions on mismatches. Their finite tests are corroboration; the integral presentation argument is the proof for all parameters.

## Relationship to prior work

Machacek's 2011 Theorem 14 treats the ordinary crown graph obtained by deleting a perfect matching from \(K_{n,n}\), equivalent here to \(k=0\). Reiner and Tseng's 2013 preprint (2014 journal publication), Example 7.3 and Corollary 12.1, treat the multicrown family for odd \(n\); their Remark 12.2 additionally states a complete formula for even \(n\) when \(\gcd(k-1,n)=1\). In the odd case our pairwise cyclic factors are equivalent to their factors because \(\gcd(n,n-2+2k)=\gcd(n,k-1)\) when \(n\) is odd. In their even coprime case our formula reduces to theirs by combining the factors \(\mathbb Z_{nq}\) and \(\mathbb Z_{tq}\) through their gcd and lcm.

Neither of those printed statements supplies the even non-coprime case \(\gcd(n,k-1)>1\); the present integral presentation handles that case as well. In particular, \(k=3\) and even \(n\) are excluded by their explicit hypotheses but included here. This difference is in mathematical hypotheses and group invariants, not merely terminology or a numerical parameter relabeling. The earlier results are established prior art, not claimed as discoveries here.

## Limitations

The result concerns only the uniformly weighted diagonal matching in an otherwise complete bipartite graph; arbitrary different matching multiplicities are not classified. The noncanonical direct sum above is an exact group decomposition, although sorting its cyclic factors may require gcd/lcm operations. The earliest public reference is a 2013 preprint; earlier crown-graph calculations and later papers must be credited as applicable. No claim of independent external validation or exhaustive priority verification is made. An equivalent treatment under different multigraph or integral-matrix terminology could exist in literature not indexed by the searches described in the accompanying review.

## References

1. Victor Reiner and Dennis Tseng, *Critical groups of covering, voltage and signed graphs*, first public arXiv version 14 January 2013, arXiv:1301.2977; *Discrete Mathematics* **318** (2014), 10–40. Relevant full-text locations: Section 7.1, Example 7.3 and Corollary 7.6; Section 12.1, Corollary 12.1 and Remark 12.2. https://arxiv.org/abs/1301.2977
2. John Machacek, *The Critical Group of a Line Graph: The Bipartite Case*, 14 December 2011, Section 4.1, Theorem 14 and Lemma 15. https://www-users.cse.umn.edu/~reiner/HonorsTheses/Machacek_thesis.pdf
