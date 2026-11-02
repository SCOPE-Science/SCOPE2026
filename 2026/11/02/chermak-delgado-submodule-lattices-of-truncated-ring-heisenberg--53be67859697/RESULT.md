# Chermak–Delgado submodule lattices of truncated-ring Heisenberg groups

## Finding

**Theorem.** Let \(q=p^f\) be any prime power, \(\ell\ge2\), \(n\ge1\), and \(R=\mathbb F_q[t]/(t^\ell)\). Let \(G=H_n(R)\) be the Heisenberg group of triples \((a,b,c)\) with \(a,b\in R^n\), \(c\in R\), and multiplication
\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+a\cdot b').
\]
Let \(Z=Z(G)=\{(0,0,c):c\in R\}\), \(V=G/Z\cong R^{2n}\), and let \(\pi:G\to V\) be the quotient map. Equip \(V\) with the perfect alternating \(R\)-bilinear form
\[
\omega((a,b),(a',b'))=a\cdot b'-a'\cdot b.
\]
For each subgroup \(H\le G\) set \(W=\pi(H)\), an additive subgroup of \(V\), and \(U=RW\), its \(R\)-linear span. Then
\[
\boxed{C_G(H)=\pi^{-1}(U^\perp),\quad
m_G(H)=|R|^{2n+2}\frac{|H\cap Z|}{|R|}\frac{|W|}{|U|},}
\]
where \(m_G(H)=|H||C_G(H)|\). In particular, \(m_G(H)\le |R|^{2n+2}\), with equality **exactly** when \(Z\le H\) and \(W=RW\) is an \(R\)-submodule. Every \(R\)-submodule of \(V\), whether free or nonfree, occurs this way, and every such subgroup is itself a centralizer. Consequently
\[
\boxed{\mathcal{CD}(G)=\mathcal C(G)=
\{\pi^{-1}(U):U\le_RR^{2n}\}
\cong \operatorname{Sub}_R(R^{2n}).}
\]
Here \(\mathcal C(G)\) is the lattice of centralizers of subsets (equivalently of subgroups), and \(\mathcal{CD}(G)\) is the Chermak–Delgado lattice. Orthogonality \(U\mapsto U^\perp\) is an inclusion-reversing involution on this lattice. The measure is increasing on the full subgroup lattice if and only if \(q=p\) and \(\ell=1\); in the present thickened range \(\ell\ge2\) it is never increasing. The statements and proofs extend unchanged to \(\ell=1\), whose finite-field lattice identification is prior work and is not separately claimed as new.

For the smallest non-field example, \(R=\mathbb F_2[t]/(t^2)\), \(n=1\), the quotient \(R^2\) has \(67\) additive subgroups but only \(15\) \(R\)-submodules. Thus \(G\), of order \(64\), has precisely \(15\) distinct centralizers and \(15\) Chermak–Delgado subgroups. For \(\mathbb F_3[t]/(t^2)\) the corresponding counts are \(212\) and \(23\).

## Assumptions and scope

All groups are finite and the symbol \(R\) denotes the unital commutative truncated polynomial ring above. An \(R\)-submodule is a subgroup of the additive quotient stable under multiplication by all elements of \(R\); not all such submodules are free. For an \(R\)-submodule \(U\le_R V\), define \(U^\perp=\{v\in V:\omega(u,v)=0\text{ for all }u\in U\}\). The Chermak–Delgado measure and lattice are defined by
\[
m_G(H)=|H||C_G(H)|,\qquad
\mathcal{CD}(G)=\{H\le G:m_G(H)=\max_{K\le G}m_G(K)\}.
\]
No restriction on the characteristic (including \(p=2\)), module rank \(n\), or length \(\ell\) is imposed. The novelty claim concerns the non-field case \(\ell\ge2\).

## Proof

**1. The central quotient and commutator.** Direct multiplication shows that for lifts \(g,g'\) with quotient coordinates \(u=(a,b)\), \(v=(a',b')\),
\[
[g,g']=(0,0,\omega(u,v)).
\]
The form is unimodular: choosing a standard basis vector in the opposite half of \(V\) detects every nonzero coordinate. Hence \(Z(G)=Z\). A group element centralizes \(H\) precisely when its quotient vector is orthogonal to every element of \(W\). Because \(\omega\) is \(R\)-bilinear, orthogonality to \(W\) is orthogonality to \(RW\). This establishes \(C_G(H)=\pi^{-1}((RW)^\perp)\), for *arbitrary* subgroups \(H\), not only subgroups containing \(Z\).

**2. Size and double annihilator of every submodule.** Let \(\rho:R\to\mathbb F_q\) extract the coefficient of \(t^{\ell-1}\), and choose a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). Set \(\chi=\psi\circ\rho\). The additive bicharacter \(B(u,v)=\chi(\omega(u,v))\) is nondegenerate: if \(u\ne0\), choose a coordinate \(u_i\) with lowest nonzero coefficient at degree \(d\); multiplying the dual coordinate by \(ct^{\ell-1-d}\), with suitable \(c\in\mathbb F_q\), makes \(\psi(\rho(\omega(u,v)))\ne1\). For an \(R\)-submodule \(U\), its annihilator for \(B\) equals \(U^\perp\): if \(B(u,v)=1\) for every \(u\in U\), then since \(ru\in U\) for all \(r\in R\), nondegeneracy of the generating character forces \(\omega(u,v)=0\). Finite-character orthogonality gives
\[
|U|\,|U^\perp|=|V|=|R|^{2n}.
\]
Applying orthogonality twice and using inclusion gives \((U^\perp)^\perp=U\). This proof includes torsion/nonfree submodules without assuming a basis for \(U\).

**3. Exact measure and equality.** Since \(\pi^{-1}(U^\perp)\) has cardinality \(|R|\,|U^\perp|\) and the kernel of \(\pi|_H\) is \(H\cap Z\), the formulas in the finding give
\[
m_G(H)=|H\cap Z|\,|W|\,|R|\frac{|R|^{2n}}{|RW|}
=|R|^{2n+2}\frac{|H\cap Z|}{|R|}\frac{|W|}{|RW|}.
\]
Both fractions are at most one. They equal one simultaneously exactly when \(H\) contains \(Z\) and \(W\) is already \(R\)-stable. If \(H\ge Z\), then necessarily \(H=\pi^{-1}(W)\). Every \(R\)-submodule \(U\) therefore produces a maximal-measure subgroup \(\pi^{-1}(U)\), proving the Chermak–Delgado description.

**4. All centralizers and self-duality.** The first step shows that every centralizer is \(\pi^{-1}(U^\perp)\) for some \(R\)-submodule \(U\). Conversely, choose \(U=T^\perp\) for any desired \(R\)-submodule \(T\). The double-annihilator identity gives \(C_G(\pi^{-1}(U))=\pi^{-1}(T)\). Thus all centralizers are precisely all inverse images of submodules; the quotient map preserves inclusion, intersection and sums at the subgroup level, identifying the two lattices with \(\operatorname{Sub}_R(R^{2n})\). The orthogonal-perpendicular correspondence is inclusion reversing and involutive.

**5. Sharp monotonicity boundary.** If \(R=\mathbb F_p\), every additive subgroup of \(V\) is \(R\)-linear, and the formula reduces to \(m_G(H)=|R|^{2n+1}|H\cap Z|\), nondecreasing with inclusion \(H\le K\). If \(|R|>p\), choose a nonzero standard vector \(e\) and its one-dimensional \(\mathbb F_p\)-span \(W=\mathbb F_p e\). Then \(RW=Re\), strictly larger than \(W\), and \(Z<\pi^{-1}(W)\), but
\[
m_G(\pi^{-1}(W))=|R|^{2n+2}\frac p{|R|}<m_G(Z)=|R|^{2n+2}.
\]
Thus monotonicity fails for every nonprime \(R\). This includes all \(\ell\ge2\) and all proper prime-power finite fields.

## Verification

The standalone `verify.py` provides independent finite checks of the formulas against explicitly implemented ring arithmetic and symplectic orthogonality. Its exhaustive cases cover all \(67\) additive subspaces of \(\mathbb F_2[t]/(t^2)^2\) and all \(212\) additive subspaces of \(\mathbb F_3[t]/(t^2)^2\), confirming the \(15\) and \(23\) submodule counts, respectively; it checks the corresponding double-annihilator and maximum-measure criteria. Separately, it constructs the \(64\)-element non-field Heisenberg group and directly checks centralizers for all relevant quotient subgroups and cyclic subgroups. It also checks \(399\) deterministic sample additive subspaces in rank two over \(\mathbb F_2[t]/(t^2)\), and the field boundary case. Run `python3 verify.py` alongside this file; the expected terminal line starts with `VERIFY_OK`. These finite checks corroborate, but do not replace, the uniform proof above.

## Relationship to prior work

An's 2021 work examines Chermak–Delgado lattices isomorphic to elementary-abelian subgroup lattices, a semisimple setting. The known finite-field Heisenberg identification \(\mathcal{CD}(H_n(\mathbb F_q))\cong\operatorname{Sub}_{\mathbb F_q}(\mathbb F_q^{2n})\) is explicitly treated as prior work. The new assertion identifies *nonsemisimple* module sublattices inside non-field Heisenberg groups for every \(n\) and \(\ell\ge2\), including all nonfree submodules and the precise measure defect for subgroups that are not \(R\)-stable.

Cocke and McCulloch give general monotonicity characterizations and a finite-field three-dimensional Heisenberg example, but their inspected statement does not supply this explicit truncated-ring submodule classification. An's 2022 realization theorem asserts existence of groups realizing abelian subgroup lattices, without identifying this specific group family and its whole lattice. Allen, La Luz, Majewicz and Zyman study Chermak–Delgado measure for mod-prime-power Heisenberg groups; their accessible abstract concerns the maximal measure rather than the entire lattice. Their full text was not accessible in this examination, so a possible implicit connection remains a substantive originality risk. It concerns a distinct coefficient ring from \(\mathbb F_q[t]/(t^\ell)\), and the current theorem additionally treats all symplectic ranks and every subgroup's measure.

## Limitations

The result is a self-contained proof, not independently audited or a claim of certified global publication priority. Accessible abstracts cannot exclude stronger implications of the unavailable paper on mod-prime-power Heisenberg groups. The theorem counts the submodules explicitly only in the two displayed small cases; the general formula classifies the lattice without providing a separate closed expression for its total number of members. No classification is asserted for arbitrary finite non-Frobenius coefficient rings or nonstandard Heisenberg central extensions.

## References

1. L. An, *Groups whose Chermak-Delgado lattice is a subgroup lattice of an elementary abelian \(p\)-group*, arXiv:2107.03108v1 (7 July 2021), https://arxiv.org/abs/2107.03108.
2. W. Cocke and R. McCulloch, *The Chermak–Delgado measure as a map on posets*, Archiv der Mathematik 123 (2024), DOI:10.1007/s00013-024-02015-8.
3. L. An, *Groups whose Chermak–Delgado lattice is a subgroup lattice of an abelian group*, Canadian Mathematical Bulletin 66 (2023), DOI:10.4153/S0008439522000418; first online 17 June 2022.
4. D. Allen, J. J. La Luz, S. Majewicz and M. Zyman, *Pseudocentralizers and the Chermak Delgado Measure of the Mod \(p^n\) Heisenberg Group*, arXiv:2405.07080v1 (11 May 2024). Later publication: *Pseudocentralizers and the pseudo Chermak–Delgado lattice of a finite group*, Communications in Algebra 53 (2025), DOI:10.1080/00927872.2025.2467197.
