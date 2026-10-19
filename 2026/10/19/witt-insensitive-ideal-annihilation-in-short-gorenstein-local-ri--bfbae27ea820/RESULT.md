# Witt-insensitive ideal annihilation in short Gorenstein local rings

## Finding
Let \((R,\mathfrak m)\) be a **finite commutative Artinian Gorenstein local ring** with \(\mathfrak m^3=0\ne\mathfrak m^2\). Write \(k=R/\mathfrak m=\mathbb F_q\) and \(d=\dim_k(\mathfrak m/\mathfrak m^2)\ge1\). For an integer \(0\le a\le d\), write \({d\brack a}_q\) for the Gaussian binomial coefficient and set
\[
G_q(d)=\sum_{a=0}^{d}{d\brack a}_q,\qquad
H_q(d)=\sum_{a=0}^{d}{d\brack a}_q G_q(d-a).
\]
Let \(\mathcal I(R)\) be the complete set of ideals, including \(0\) and \(R\). For every integer \(s\ge2\), the probability that \(s\) independently and uniformly selected ideals have zero product is
\[
\boxed{\displaystyle
\zeta_s(R)=1-\frac{1+sG_q(d)+\binom{s}{2}\big(G_q(d)^2-H_q(d)\big)}{\big(G_q(d)+2\big)^s}.}
\]
This formula holds in arbitrary characteristic and does not require a coefficient field or a graded presentation. It depends only on \(q\) and \(d\), not on the isometry type of the nondegenerate multiplication pairing.

More precisely, let \(S=\mathfrak m^2\), \(V=\mathfrak m/S\), and let \(I_U\) be the inverse image in \(\mathfrak m\) of any \(k\)-subspace \(U\le V\). Every nonzero proper ideal is exactly one such \(I_U\), including \(I_0=S\) and \(I_V=\mathfrak m\). The multiplication on \(V\) induces a nondegenerate symmetric \(k\)-bilinear pairing \(B:V\times V\to S\cong k\). For \(0\le a,b\le d\), the exact *dimension-refined ordered zero-product incidence* is
\[
\boxed{\displaystyle
\#\{(U,W):\dim_k U=a,\;\dim_k W=b,\;I_UI_W=0\}
={d\brack a}_q\,{d-a\brack b}_q,}
\]
where the latter factor is zero if \(b>d-a\). Thus two rings with the same \(q,d\) have the same entire sequence of ideal zero-product probabilities and the same dimension-refined annihilation counts, even if their multiplication forms are inequivalent.

## Assumptions and scope
All rings are finite, commutative, unital, and local. The Artinian Gorenstein condition means the socle \(\operatorname{Ann}_R(\mathfrak m)\) is one-dimensional over the residue field. The radical satisfies \(\mathfrak m^3=0\ne\mathfrak m^2\) (Loewy length exactly three). The residue-field order \(q\) is any prime power; \(d\ge1\); the formula holds for all integers \(s\ge2\), with repeated ideals permitted and all \(G_q(d)+2\) ideals sampled uniformly. The dimension-refined count concerns nonzero proper ideals indexed by subspaces, not \(0\) and \(R\). No assertion is made for non-Gorenstein local rings, longer Loewy length, or arbitrary nonlocal rings.

## Proof
**1. The socle and all ideals.** Since \(\mathfrak m^3=0\), the nonzero ideal \(\mathfrak m^2\) is contained in the socle. Gorensteinness gives \(\dim_k\operatorname{Ann}_R(\mathfrak m)=1\), so
\[S=\mathfrak m^2=\operatorname{Ann}_R(\mathfrak m).\]
Every nonzero ideal \(I\) contains \(S\): choose a nonzero element of \(I\); multiplying it by a suitable power of \(\mathfrak m\), minimal before annihilation, produces a nonzero element of \(I\cap S\). As \(S\) is a simple \(R\)-module, \(S\subseteq I\). A proper ideal is contained in \(\mathfrak m\). The \(R\)-action on \(\mathfrak m/S\) factors through \(k\), because \(\mathfrak m\mathfrak m\subseteq S\); hence every \(k\)-subspace \(U\le\mathfrak m/S\) has an inverse-image ideal \(I_U\), and these are exactly the nonzero proper ideals. This gives \(|\mathcal I(R)|=G_q(d)+2\).

**2. A perfect multiplication pairing.** Products of lifts of \(u,v\in V=\mathfrak m/S\) lie in \(S\) and are independent of the lifts because \(S\mathfrak m=0\). The resulting pairing \(B:V\times V\to S\) is well-defined, symmetric, and \(k\)-bilinear. The \(k\)-action on \(S\) is canonical via \(R\to k\), so this construction does not presuppose a subfield \(k\subseteq R\). If \(u\) is in the radical of \(B\), a lift \(x\in\mathfrak m\) satisfies \(x\mathfrak m=0\), hence \(x\in S\) and \(u=0\). Thus \(B\) is nondegenerate.

**3. Dimension-refined annihilation.** For subspaces \(U,W\le V\), the equality \(I_UI_W=0\) holds precisely when \(B(U,W)=0\), or \(W\le U^\perp\). Nondegeneracy implies \(\dim_k U^\perp=d-\dim_k U\). Thus for every \(a,b\) there are exactly \({d\brack a}_q{d-a\brack b}_q\) ordered such pairs with dimensions \(a,b\). Summing over both dimensions gives exactly \(H_q(d)\) zero-product ordered pairs among the \(G_q(d)\) nonzero proper ideals. There are therefore \(G_q(d)^2-H_q(d)\) nonzero-product ordered pairs among them.

**4. All tuple lengths.** A product of \(s\) ideals can be nonzero only when none is \(0\), and at most two of them are proper, because the product of any three proper ideals is contained in \(\mathfrak m^3=0\). Exactly zero proper ideals gives one tuple \((R,\ldots,R)\). Exactly one proper ideal gives \(sG_q(d)\) tuples, each with nonzero product. Exactly two proper ideals gives \(\binom{s}{2}\big(G_q(d)^2-H_q(d)\big)\) tuples with nonzero product; order is accounted for by the ordered pair count. These cases exhaust nonzero products. Subtract their sum from the total \((G_q(d)+2)^s\) tuples and divide by that total to obtain the boxed formula.

**5. The sharp contrast between forms.** When \(d=2\), subspace enumeration yields \(G_q(2)=q+3\) and \(H_q(2)=3q+6\), so
\[\zeta_2(R)=\frac{5(q+3)}{(q+5)^2}.\]
Over \(\mathbb F_3\), consider the two finite local algebras
\[R_\epsilon=\mathbb F_3[x,y]/(xy,\;x^2-\epsilon y^2,\;x^3,\;y^3),\qquad \epsilon\in\{-1,1\}.\]
Both have \(d=2\), \(\zeta_2=15/32\), and the same complete probability sequence. Their nondegenerate multiplication forms are respectively split (\(\epsilon=-1\)) and anisotropic (\(\epsilon=1\)). The former has two isotropic lines, the latter none, so the numbers of *nonzero* ideals \(I\) with \(I^2=0\) are respectively three and one (the socle ideal in both, plus two lines in the split case). This shows that the ideal-zero-product probabilities are blind to a genuine multiplicative distinction, rather than forcing the forms to be isometric.

## Verification
The included `verify_ideal_probability.py` is executable with a standard Python 3 interpreter; run `python3 verify_ideal_probability.py`. It enumerates reduced-row-echelon subspaces of actual finite-dimensional maximal ideals, tests ideal closure by multiplication instead of assuming the classification, builds ideal-multiplication tables, and verifies the claimed ideal totals and all tuple products through length four. It checks twelve finite-field configurations, including \(q\in\{2,3,4,5\}\), dimensions through four, alternating and nonalternating characteristic-two pairings, and split/anisotropic ternary binary pairings.

A separate test constructs the characteristic-four ring \((\mathbb Z/4\mathbb Z)[x,y]/(2x,2y,xy,x^2-2,y^2-2)\) directly, enumerates *all* additive subgroups and filters its seven ideals, verifies associativity and distributivity on all elements, and exhaustively checks its ideal products. This guards against tacit use of a coefficient-field splitting. The program terminates with `VERIFY_OK` on successful tests. Finite checks are corroboration, not a proof for unrestricted \(q,d,s\); Steps 1–4 are the proof.

## Relationship to prior work
Chakraborty and Patra introduced the ideal zero-product probability, proved a universal formula for finite chain rings (Theorem 4.6), and extended to finite principal ideal rings via direct products; their Section 10, Problem 1 explicitly asks for universality beyond chain rings. The present theorem answers a distinct nonprincipal short-Gorenstein case, with a dimension-refined pair count and insensitivity to the isometry type. It does **not** assert that Loewy length alone suffices for all short Gorenstein rings: the answer depends on \(q,d\).

Aliniaeifard and Behboodi studied annihilating-ideal graphs of Artinian rings; their Lemma 2.8 uses the same short-Gorenstein hypotheses to exhibit a complete bipartite subgraph in high embedding dimension. It does not supply the entire ordered incidence distribution or the \(s\)-fold probability. Essa and Mohammad studied \(k\)-annihilating-ideal *hypergraphs*, whose edges use distinct ideals and require all \((k-1)\)-fold products to be nonzero; their finite-local results therefore count a different configuration and principally use nilpotency indices of principal ideals. Other literature on graph classification can distinguish forms or ideal incidence up to graph isomorphism, but those results do not themselves state the Gaussian formula or its probability consequences.

## Limitations
The Gorenstein socle condition and Loewy-length-three hypothesis are essential to this proof: without either, the ideal lattice need not be the full subspace lattice above a simple socle, and the pairing may be degenerate or higher products may survive. The result does not classify all ring isomorphism types and does not provide a formula for higher Loewy length. Identifying all equivalent forms of these counts in historical graph-theoretic literature remains a bibliographic uncertainty. The finite verifier covers stated small configurations only. No independent mathematical audit has been performed.

## References
1. S. Chakraborty and S. K. Patra, *Ideal Zero-Product Probability in Finite Commutative Rings*, arXiv:2608.14618v1 (2026), Sections 2, 4, and 10; https://arxiv.org/pdf/2608.14618.
2. M. Aliniaeifard and M. Behboodi, *Rings Whose Annihilating-Ideal Graphs Have Positive Genus*, arXiv:1102.4835v1 (2011), Lemma 2.8; https://arxiv.org/html/1102.4835v1.
3. S. S. Essa and H. Q. Mohammad, *On a k-Annihilating Ideal Hypergraph of Local Rings*, Communications in Mathematics and Applications **15** (2024), 253–263, doi:10.26713/cma.v15i1.2378; https://www.rgnpublications.com/journals/index.php/cma/article/download/2378/1671/10017.
4. A. R. Curtis, J. A. Diesl, and C. Rieck, *Classifying Annihilating-Ideal Graphs of Commutative Artinian Rings* (2018), doi:10.1080/00927872.2018.1439040 (abstract and bibliographic information consulted; full text not inspected).
