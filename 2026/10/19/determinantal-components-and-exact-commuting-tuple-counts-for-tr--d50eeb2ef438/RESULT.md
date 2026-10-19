# Determinantal components and exact commuting-tuple counts for truncated polynomial derivations

## Finding

Let \(n\ge 2\) and \(s\ge 2\). Let \(k\) be a field of characteristic zero or characteristic \(p>n+1\), and put
\[
A_n=k[t]/(t^{n+1}),\qquad L_n=\operatorname{Der}_k(A_n).
\]
For each integer \(i\) with \(0\le i<n\), write \(e_i=t^{i+1}\partial_t\) and \(F_i=\langle e_i,\ldots,e_{n-1}\rangle_k\), with \(F_n=0\). Put \(m=\lceil n/2\rceil\).

For \(0\le i<m\), define the closed reduced subvariety \(Z_i\subseteq L_n^s\) to consist of tuples \((v_1,\ldots,v_s)\) such that each \(v_a\) belongs to \(F_i\) and the \(s\)-by-\((n-2i)\) coefficient matrix of their images in \(F_i/F_{n-i}\) has rank at most one. Let \(D_{s,d}^{\le1}\) denote the reduced determinantal variety of \(s\)-by-\(d\) matrices of rank at most one.

Then the **reduced commuting-tuple variety**
\[
\mathcal C_s(L_n)_{\mathrm{red}}=
\{(v_1,\ldots,v_s)\in L_n^s:[v_a,v_b]=0\text{ for all }a,b\}_{\mathrm{red}}
\]
has precisely the \(m\) geometrically irreducible components \(Z_0,\ldots,Z_{m-1}\). More explicitly,
\[
Z_i\cong\mathbb A_k^{si}\times D_{s,n-2i}^{\le1},\qquad
\dim Z_i=n+s-1+i(s-2).
\]
Thus the reduced variety is equidimensional for \(s=2\), whereas it is not equidimensional for \(s\ge3\) and \(n\ge3\). The statement concerns the reduced variety; it makes no claim about reducedness of the original bracket-equation scheme.

For every prime power \(q\) whose characteristic exceeds \(n+1\), the same classification yields an exact count of all ordered pairwise-commuting \(s\)-tuples:
\[
\boxed{\displaystyle
\#\mathcal C_s(L_n)(\mathbb F_q)
=q^{s(n-m)}+(q^s-1)\sum_{i=0}^{m-1}q^{si+n-2i-1}.}
\]
The symbol on the left counts field-valued tuples, and hence is unchanged by reduction.

## Assumptions and scope

The derivation algebra is the **full** derivation Lie algebra: the hypothesis that \(n+1\) is invertible in \(k\) forces every derivation of \(A_n\) to send \(t\) into the ideal \((t)\). Thus every derivation is uniquely a linear combination of \(e_0,\ldots,e_{n-1}\). For the structural argument it suffices that all nonzero integer differences between indices in \(\{0,\ldots,n-1\}\) remain nonzero in \(k\); the stated stronger bound \(p>n+1\) guarantees both this and the full-derivation description. No algebraic-closure hypothesis is needed for the definitions, the coordinate isomorphisms, or the finite-field counts. Geometric irreducibility is established after extending scalars to an algebraic closure.

## Proof

**1. The truncated Witt bracket and its filtration.** The derivation condition at \(t^{n+1}=0\) is \((n+1)t^n D(t)=0\), so \(D(t)\in(t)\). A direct calculation gives
\[
[e_i,e_j]=\begin{cases}(j-i)e_{i+j},&i+j<n,\\0,&i+j\ge n.\end{cases}
\]
Consequently \([F_i,F_j]\subseteq F_{i+j}\), interpreting \(F_r=0\) for \(r\ge n\). In particular \([F_i,F_{n-i}]=0\), and \(F_{n-i}\) is abelian when \(0\le i<m\), since then \(2(n-i)\ge n\).

**2. An exact centralizer lemma.** If \(f\in F_i\setminus F_{i+1}\) with \(i<m\), then
\[
C_{L_n}(f)=kf\oplus F_{n-i}.
\]
To verify it, write \(f=a_i e_i+\cdots\), \(a_i\ne0\). For every \(j\) with \(0\le j<n-i\) and \(j\ne i\), the leading term of \([f,e_j]\) is \(a_i(j-i)e_{i+j}\ne0\). Distinct such columns have distinct leading degrees, and hence are linearly independent. Columns with \(j\ge n-i\) are zero. The omitted column \([f,e_i]\) belongs to the span of the other columns because \([f,f]=0\) and the coefficient of \(e_i\) in \(f\) is nonzero. Therefore \(\operatorname{rank}(\operatorname{ad}_f)=n-i-1\), so the centralizer has dimension \(i+1\). The displayed \(i+1\)-dimensional subspace centralizes \(f\), and thus it is the full centralizer. The directness follows from \(i<n-i\).

**3. Every determinantal piece consists of commuting tuples.** Fix \(i<m\). At a geometric point of \(Z_i\), the images of the \(s\) entries in \(F_i/F_{n-i}\) span a subspace of dimension at most one. Choose a lift \(u\in F_i\) of a generator when the image is nonzero. Then each entry is \(\lambda_a u+w_a\), with \(w_a\in F_{n-i}\). The containment \([F_i,F_{n-i}]=0\) and the abelianness of \(F_{n-i}\) give \([\lambda_a u+w_a,\lambda_b u+w_b]=0\) for every pair. When all images vanish, the same conclusion follows immediately. Hence \(Z_i\subseteq\mathcal C_s(L_n)_{\mathrm{red}}\).

**4. The pieces exhaust every commuting tuple.** For a nonzero tuple, let \(i\) be the smallest index of a nonzero coefficient among its entries. If \(i<m\), one entry \(f\) belongs to \(F_i\setminus F_{i+1}\). By step 2 every other entry lies in \(kf+F_{n-i}\). Therefore the quotient coefficient matrix has rank at most one, and the tuple belongs to \(Z_i\). If no entry has a nonzero coefficient below \(m\), all entries lie in \(F_m\). The quotient \(F_m/F_{n-m+1}\) has dimension at most one, so this tuple lies in \(Z_{m-1}\). The zero tuple also lies in every \(Z_i\). Thus the underlying sets over every algebraically closed extension satisfy \(\mathcal C_s(L_n)_{\mathrm{red}}=\bigcup_{i=0}^{m-1}Z_i\).

**5. Exactly these are the irreducible components.** The coordinates of \(F_{n-i}\) contribute an unrestricted affine space of dimension \(si\); the remaining coordinates obey precisely the rank-one determinantal equations. This proves \(Z_i\cong\mathbb A^{si}\times D_{s,n-2i}^{\le1}\). The rank-one determinantal variety is geometrically integral: its nonzero locus is parametrized by outer products of two vectors modulo one scalar, with dense charts of dimension \(s+(n-2i)-1\); adding the zero matrix does not create another component. Hence \(Z_i\) is geometrically irreducible of the stated dimension. Distinct \(Z_i\) cannot contain one another. If \(j>i\), the tuple \((e_i,0,\ldots,0)\) lies in \(Z_i\) but not \(Z_j\). If \(j<i\), the tuple \((e_i,e_{n-i},0,\ldots,0)\) belongs to \(Z_i\) but has two independent images in \(F_j/F_{n-j}\), hence does not belong to \(Z_j\). Since an irreducible closed subset contained in a finite union must be contained in some member, these are exactly the irreducible components of the reduced variety. The dimension formula follows.

**6. Exact finite-field enumeration.** Partition commuting tuples by their minimum nonzero coefficient index. All tuples in \(F_m^s\), including zero, are commuting and contribute \(q^{s(n-m)}\). For minimum index \(i<m\), the coefficient column at \(e_i\) is a nonzero vector in \(\mathbb F_q^s\), yielding \(q^s-1\) choices. Every one of the next \(n-2i-1\) quotient-coordinate columns is its scalar multiple, yielding \(q^{n-2i-1}\) choices. The remaining \(i\) top-degree coordinates in each of the \(s\) entries are free, yielding \(q^{si}\). Multiplying and summing gives the displayed closed formula. This is an exhaustive, disjoint partition, not an interpolation from finite samples.

## Verification

The companion standard-library program `verify.py` directly computes brackets in the \(e_i\) basis and exhaustively enumerates commuting pairs or triples over small prime fields in the allowed characteristic range. It also checks the determinantal-union condition where feasible and independently calculates adjoint ranks by modular row reduction. The reported checks are \((n,s,q)=(2,2,5),(2,3,5),(3,2,5),(3,3,5)\), with respective commuting-tuple counts \(145,745,1225,18725\). Adjoint-rank census checks use \((n,q)=(2,5),(3,5),(4,7),(5,7)\). All returned `VERIFY_OK` before packaging and were replayed from the embedded artifact after packaging. These finite checks support the proof but do not establish the general geometric assertions.

## Relationship to prior work

The modular Witt Lie algebra and its filtration are classical. Yao and Chang (2013, arXiv:1301.5667), especially Lemma 2.3 and Theorem 4.3, compute centralizers and classify commuting **nilpotent pairs** for the Witt algebra and the nilpotent cone of its Borel subalgebra. That centralizer-filtration strategy is antecedent; the present lemma is proved directly for each truncated full derivation Lie algebra. The earlier statements do not identify the all-arity reduced commuting varieties of \(\operatorname{Der}_k(k[t]/(t^{n+1}))\) in characteristic exceeding \(n+1\) with the explicit determinantal pieces \(Z_i\), and they do not give the displayed uniform finite-field formula for this family.

Further work by Yao (2015) treats nilpotent commuting tuples in the modular Witt algebra and certain subalgebras; Yao and Chang (2018) treat the full Witt commuting-pair variety; Yao and Zhang (2021) treat commuting tuples of the full Witt algebra. Those are substantial neighboring results, not merely title matches. Their stated objects are the full modular Witt algebra or nilpotent loci, whereas the present objects are the **full derivation algebras of shorter truncations** in sufficiently large characteristic, with no nilpotence restriction on tuple entries. Only the 2013 primary paper was accessible and examined in full. The other works were located and compared at the abstract/metadata level, so stronger implications in their full texts remain a residual risk rather than a declared exclusion.

## Limitations

The scheme cut out by all bracket coordinates is not asserted to be reduced or to have prime-component ideals equal to its primary components. The claim is about its reduced underlying variety, the explicit geometrically integral closed subvarieties, and field-valued point counts. Small-characteristic cases, including characteristics not exceeding \(n+1\), are excluded. Nothing is claimed about commuting tuples in the full modular Witt algebra or its nilpotent cone. The originality comparison is based on accessible publications and the stated, explicitly bounded literature risks; it is not a claim of exhaustive prior-art absence. No independent mathematical review has been performed.

## References

1. Y.-F. Yao and H. Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1 (23 January 2013), especially Lemma 2.3 and Theorem 4.3. https://arxiv.org/pdf/1301.5667
2. Y.-F. Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, Journal of Pure and Applied Algebra 219 (2015), 4042–4054, doi:10.1016/j.jpaa.2015.02.005. Full text not accessed.
3. Y.-F. Yao and H. Chang, *Commuting variety of Witt algebra*, Frontiers of Mathematics in China 13 (2018), 1179–1187, doi:10.1007/s11464-018-0725-9. Abstract and bibliographic record examined.
4. Y.-F. Yao and Y. Zhang, *Commuting variety of r-tuples over the Witt algebra*, Journal of East China Normal University (Natural Science) 2021(3), 1–7, doi:10.3969/j.issn.1000-5641.2021.03.001. Abstract and bibliographic record examined.
