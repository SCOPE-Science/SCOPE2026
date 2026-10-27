# Chordality dichotomy and complete clique polynomials for odd dihedral-quandle endomorphism monoids

## Finding

For each odd integer \(n\ge3\), equip \(R_n=\mathbb Z/n\mathbb Z\) with the dihedral-quandle operation \(x\triangleright y=2y-x\). Let \(\Gamma_n\) be the **full simple commuting graph** of its endomorphism monoid: vertices are every quandle endomorphism, and distinct maps are adjacent exactly when they commute under composition. Then
\[
\boxed{\Gamma_n\text{ is chordal if and only if }n\text{ is a prime power}.}
\]
For any odd prime \(p\), integer \(e\ge1\), and \(n=p^e\), the graph admits an explicit recursive perfect-elimination order and an exact polynomial counting **all** pairwise commuting subsets, not only maximal ones.

Put \(C_e(z)=\sum_{j\ge0}c_{e,j}z^j\), where \(c_{e,j}\) is the number of \(j\)-element subsets of \(\operatorname{End}(R_{p^e})\) whose members commute pairwise; in particular the empty set contributes \(1\). Set \(C_0(z)=1+z\). Then
\[
\boxed{C_1(z)=(p+1)(1+z)^p-p(1+z),}
\]
and for every \(e\ge2\),
\[
\boxed{\begin{aligned}
C_e(z)&=C_{e-2}\!\left((1+z)^{p^2}-1\right)\\
&\quad+p^{e-1}(p+1)(1+z)^{p^{e-1}}
\bigl((1+z)^{p^e-p^{e-1}}-1\bigr).
\end{aligned}}
\]
In particular, \(\Gamma_{p^e}\) is perfect, and \(\chi(\Gamma_{p^e})=p^e\). The clique number and number of maximum cliques are previously known from the equivalent deep-commuting graph of \((\mathbb Z/p^e\mathbb Z)^2\); these are NOT claimed here as new results.

## Assumptions and scope

The modulus is odd and at least \(3\); the graph includes **all** endomorphisms including the identity map, constant maps, and nonunits. Its edges are between distinct maps; a clique is a subset, not an ordered tuple, so its counting polynomial has constant coefficient \(1\). A chordal graph has no induced cycles of length at least four. The theorem says no general chordality assertion for even moduli; oddness is needed for the endomorphism normal form below.

We identify an endomorphism \(f_{a,b}\) with \(x\mapsto ax+b\) where \(a,b\in\mathbb Z/n\mathbb Z\), and reparametrize it by \((u,b)=(a-1,b)\). Under this bijection the adjacency condition is exactly
\[
\boxed{(u,b)\sim(v,d)\quad\Longleftrightarrow\quad ud-vb=0\pmod n}\qquad\text{for distinct labels.}
\]
This determinant graph was already studied under the name *deep commuting graph* of a homocyclic rank-two abelian group. Identifying this known graph is a reduction, not an originality claim.

## Proof

**Affine normal form.** Write \(h(x)=f(x)-f(0)\). The quandle homomorphism identity implies
\[
h(2y-x)=2h(y)-h(x),\quad h(0)=0.
\]
Putting \(y=0\) gives \(h(-x)=-h(x)\); putting \(x=0\) gives \(h(2y)=2h(y)\). Replacing \(x\) by \(-x\) consequently yields \(h(2y+x)=h(2y)+h(x)\). Since multiplication by \(2\) is surjective on \(\mathbb Z/n\mathbb Z\) when \(n\) is odd, \(h\) is additive. Thus \(h(x)=ax\) for some \(a\). Conversely, every \(x\mapsto ax+b\) respects \(x\triangleright y=2y-x\). There are exactly \(n^2\) endomorphisms.

**Determinantal commutation.** Direct composition gives
\[
f_{a,b}\circ f_{c,d}(x)=acx+ad+b,\qquad
f_{c,d}\circ f_{a,b}(x)=acx+cb+d.
\]
They commute exactly when \((a-1)d=(c-1)b\), the displayed determinant condition.

**Prime-power peeling.** Fix \(n=p^e\). A vertex \(v=(u,b)\) is *primitive* when at least one coordinate is not divisible by \(p\). The kernel of \(w\mapsto\det(v,w)\) over \(\mathbb Z/p^e\mathbb Z\) is the cyclic line \(Lv=\{tv:t\in\mathbb Z/p^e\mathbb Z\}\), of size \(p^e\): an invertible coordinate solves the kernel equation directly. Hence the closed neighborhood of \(v\) is exactly the complete graph on \(Lv\). The primitive elements of a fixed such line number \(\varphi(p^e)=p^e-p^{e-1}\) and are all simplicial. Two different primitive lines have no adjacent primitive elements, since a primitive neighbor lies on its unique line. The number of distinct primitive lines is
\[
\frac{p^{2e}-p^{2e-2}}{p^e-p^{e-1}}=p^{e-1}(p+1).
\]
Every line has exactly \(p^{e-1}\) nonprimitive elements, giving the common line-intersection clique with the nonprimitive core.

For \(e\ge2\), the induced graph on nonprimitive vectors \(p(\mathbb Z/p^{e-1}\mathbb Z)^2\) is the **complete \(p^2\)-clique substitution** of the determinant graph modulo \(p^{e-2}\). Indeed each vector in \((\mathbb Z/p^{e-2}\mathbb Z)^2\) has exactly \(p^2\) lifts, with all such lifts mutually adjacent; two fibers are fully joined if and only if their base vectors have zero determinant modulo \(p^{e-2}\), because \(\det(px,py)=p^2\det(x,y)\). The base case \(e=1\) is \(p+1\) cliques of size \(p\) meeting only in the zero vertex; for \(e=2\) the core is \(K_{p^2}\). Starting with all primitive vertices and then recursively lifting a perfect-elimination order of the smaller base graph gives an explicit perfect-elimination order; replacing a vertex by a clique preserves the simplicial-neighborhood property. Induction proves chordality for all \(p^e\).

**Exact polynomial.** Every clique lies entirely inside the nonprimitive core or contains a primitive point. In the latter case the primitive members determine one and only one primitive line, so for each of the \(p^{e-1}(p+1)\) lines one may choose a nonempty subset of its \(p^e-p^{e-1}\) primitive points and any subset of its \(p^{e-1}\) nonprimitive points. The core contributes \(C_{e-2}((1+z)^{p^2}-1)\), because a clique of \(j\) base points lifts to nonempty subsets of each of \(j\) disjoint \(p^2\)-cliques. This proves the recurrence. For \(e=1\) the zero vertex together with the \(p+1\) primitive lines gives \(C_1\) as stated, subtracting \(p\) copies of the common central subsets.

**Multiple prime factors.** Suppose \(n=rs\) with \(r,s>1\) coprime. By the Chinese remainder theorem choose nonzero orthogonal idempotents \(\epsilon_r,\epsilon_s\in\mathbb Z/n\mathbb Z\) with \(\epsilon_r\epsilon_s=0\). The four distinct vectors
\[
(\epsilon_r,0),\quad(\epsilon_s,0),\quad(0,\epsilon_r),\quad(0,\epsilon_s)
\]
in that cyclic order form an induced four-cycle: every consecutive determinant vanishes, whereas the two opposite determinants are \(\epsilon_r\ne0\) and \(\epsilon_s\ne0\). Hence \(\Gamma_n\) is not chordal.

**Chromatic number.** A chordal graph is perfect. Each primitive line has \(p^e\) vertices and is a clique. No clique can be larger: any clique containing a primitive point lies in its line, and a clique without primitive points is contained in the core. Inductively the maximum core clique size is \(p^2p^{e-2}=p^e\), with \(e=2\) core size \(p^2\); equality follows. Thus \(\omega=\chi=p^e\). The clique-number part also follows from the earlier maximum-clique classification cited below.

## Verification

Run `python3 verify.py` with the Python 3 standard library. The verifier constructs adjacency by the determinant congruence and independently checks all possible quandle endomorphisms for \(n=3,5\) against the affine normal form. For \((p,e)=(3,1),(3,2),(3,3),(5,1),(5,2)\), it checks an explicit proposed perfect-elimination order by testing all pairs of later neighbors. Bron--Kerbosch enumeration of maximal cliques checks \((p,e)=(3,1),(3,2),(5,1),(5,2)\). For \(n=3,9\), it enumerates all subsets of maximal cliques, deduplicates them, and compares every coefficient of \(C_e\); it also checks independently computed graph edge counts and the explicit induced cycle at \(n=15\). Its terminal output is `VERIFY_OK dihedral commuting graph chordality and clique recurrence`. Finite checks corroborate, but cannot replace, the proof for all moduli.

For example,
\[
C_2(z)=(1+z)^9+12(1+z)^3\bigl((1+z)^6-1\bigr)
\quad\text{when }p=3,
\]
so the graph has \(81\) vertices and \(432\) edges. The derived exact coefficients count every clique size, unlike counts of maximum cliques only.

## Relationship to prior work

Elhamdadi--Senesi--Zappala (2022) define finite dihedral quandles and examine regular representations, not full commuting graphs of endomorphism monoids. Singh (2023) studies residual finiteness of quandle endomorphism monoids, not this finite-graph census. Cameron--Kuzma (2020 preprint; 2023 journal) introduce deep commuting graphs. Hatui--Mukherjee--Patra (2025) study their group-theoretic properties, including descriptions for finite abelian groups and group-product reductions, but do not give this clique-polynomial recursion or chordality dichotomy in the inspected text.

Crucially, the already published published-finding corpus report *Maximum pairwise lift-commuting subsets in \(C_{p^a}\times C_{p^a}\)* establishes precisely the same determinant graph, classifies all maximum cliques and gives their exact number. Therefore the determinant identification, clique number and maximum-clique census are **acknowledged as covered prior work**, regardless of the different terminology. The present claim concerns the previously unaddressed chordality boundary and full (all clique sizes) counting-polynomial recursion. That report expressly leaves chromatic number uncomputed; chordality supplies it as a corollary. These distinctions are mathematical statement and implication comparisons, not just comparisons of titles. It remains possible that literature on graph substitutions or symplectic orthogonality over chain rings covers the new recurrence; exhaustive priority is not asserted.

## Limitations

Only odd \(n\ge3\) are addressed, and the graph includes all maps rather than only noncentral ones. For odd composite \(n\) the theorem proves failure of chordality but gives no full clique polynomial. For prime powers, the recurrence is explicit but its evaluation for high \(e\) may involve large coefficients. The clique-number part and maximum-clique count are known prior work, not newly discovered. Relevant general literature on modular determinant graphs and chordal graph substitutions may give logically stronger statements; absence of a search hit is not proof of uniqueness. There has been no independent mathematical audit.

## References

1. M. Elhamdadi, M. Senesi and M. Zappala, *Decomposition of the regular representation for dihedral quandles*, arXiv:2206.06311v1, first public 13 June 2022, https://arxiv.org/abs/2206.06311.
2. M. Singh, *Endomorphism monoid and automorphism group of residually finite and profinite quandles*, arXiv:2311.03708v1, first public 7 November 2023, https://arxiv.org/abs/2311.03708.
3. P. J. Cameron and B. Kuzma, *Between the enhanced power graph and the commuting graph*, arXiv:2012.03789v1, first public 7 December 2020; DOI 10.1002/jgt.22871.
4. S. Hatui, S. Mukherjee and K. L. Patra, *On the deep commuting graph of a finite group*, arXiv:2511.13303v1, 17 November 2025, https://arxiv.org/pdf/2511.13303.
5. *Maximum pairwise lift-commuting subsets in \(C_{p^a}\times C_{p^a}\)*, published mathematical record, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-maximum-pairwise-lift-commuting-subsets-in-c-p-a-imes-c-p-a--6b7aca53a924/RESULT.md.
