# Fifteen two-round theories of one-dimensional affine groups over finite fields

## Finding
For each prime power \(q=p^f\ge2\), let \(G_q=\operatorname{AGL}(1,\mathbb F_q)\) be the group of bijections \(z\mapsto az+b\), where \(a\in\mathbb F_q^\times\) and \(b\in\mathbb F_q\). Regard \(G_q\) as a first-order structure with equality, a named identity \(e\), and a **ternary relation** \(R(x,y,z)\) meaning \(xy=z\). Write \(\equiv_2\) for agreement on all sentences of quantifier rank at most two.

**Theorem.** The infinite family \(\{G_q:q\text{ a prime power},\ q\ge2\}\) has **exactly fifteen** \(\equiv_2\)-classes, described exhaustively by the following table. In the last six rows \(p\ge5\), and \(\nu_2(q-1)\) means the exponent of two dividing \(q-1\).

| Class | Exact condition | Least \(q\) | Group order |
|---|---|---:|---:|
| A | \(p=2, f=1\) | 2 | 2 |
| B | \(p=3, f=1\) | 3 | 6 |
| C | \(p=2, f=2\) | 4 | 12 |
| D | \(p=5, f=1\) | 5 | 20 |
| E | \(p\ge5, q>5,\nu_2(q-1)=1,3\mid q-1\) | 7 | 42 |
| F | \(p=2, f\ge3\text{ odd}\) | 8 | 56 |
| G | \(p=3,f=2\) | 9 | 72 |
| H | \(p\ge5,q>5,\nu_2(q-1)=1,3\nmid q-1\) | 11 | 110 |
| I | \(p\ge5,q>5,\nu_2(q-1)=2,3\mid q-1\) | 13 | 156 |
| J | \(p=2,f\ge4\text{ even}\) | 16 | 240 |
| K | \(p\ge5,q>5,\nu_2(q-1)\ge3,3\nmid q-1\) | 17 | 272 |
| L | \(p\ge5,q>5,\nu_2(q-1)\ge3,3\mid q-1\) | 25 | 600 |
| M | \(p=3,f\ge3\text{ odd}\) | 27 | 702 |
| N | \(p\ge5,q>5,\nu_2(q-1)=2,3\nmid q-1\) | 29 | 812 |
| O | \(p=3,f\ge4\text{ even}\) | 81 | 6480 |

Two groups are \(\equiv_2\)-equivalent **if and only if** their field orders occur in the same row. Every group in the family is \(\equiv_2\)-equivalent to one of order at most \(6480\), and this bound is sharp *within this family*. In particular \(G_{27}\not\equiv_2G_7\), even though both have \(q-1\) with exactly one factor of two, while \(G_{25}\not\equiv_2G_{81}\), despite both realizing many of the same small element orders.

## Assumptions and scope
Only finite fields, including nonprime fields, occur. Quantifier rank is measured in the explicitly stated **relational** language: multiplication is not a binary function symbol. The result does not assert two-round equivalence in a functional group language, in a language naming the translation subgroup, or among arbitrary Frobenius groups.

## Proof
**1. Complete two-move invariant.** For an ordered pair \((x,y)\) of group elements, set
\[
\alpha(x,y)=\bigl([x=e],[y=e],[x=y],[x^2=e],[y^2=e],[x^2=y],[y^2=x],[xy=e]\bigr)\in\{0,1\}^8.
\]
Here brackets denote truth values. Every atomic formula with variables among \(x,y\) and the constant \(e\) is determined by these eight bits: cancellation reduces all other products to these relations and equality; \(xy=e\iff yx=e\). Conversely each bit is an atomic relation or equality. Define \(U_G(x)=\{\alpha(x,y):y\in G\}\) and \(T(G)=\{U_G(x):x\in G\}\). By the elementary two-move back-and-forth criterion, \(G\equiv_2H\iff T(G)=T(H)\). Indeed a response to the first move must have identical available atomic diagrams for every possible second move, in either direction. Thus these sets are **complete** invariants, not sampled signatures.

**2. Explicit formula for all diagrams.** Write \((a,b)(c,d)=(ac,b+ad)\). Every element with \(a\ne1\) is conjugate to \((a,0)\). Every nonzero translation is conjugate to \((1,1)\) after choosing a nonzero translation coordinate. Put \(m=q-1\), and fix a generator \(\gamma\) of the cyclic multiplicative group.

For a nontranslation first element \(x=(\gamma^j,0)\), \(1\le j<m\), and a second element \(y=(\gamma^h,0)\), \(0\le h<m\), the eight bits, in order, are exactly
\[
(0,[h=0],[h=j],[2j\equiv0],[2h\equiv0],[h\equiv2j],[2h\equiv j],[h+j\equiv0]),
\]
with congruences modulo \(m\). For \(y=(\gamma^h,d)\) with \(d\ne0\), the bits are
\[
(0,0,0,[2j\equiv0],[(h=0\land p=2)\lor(m\text{ even}\land h=m/2)],0,0,0).
\]
Such \(d\ne0\) always exists. There are no further second-element types.

For a nonzero translation \(x=(1,b)\), use \(y=(1,rb)\), \(r\in\mathbb F_p\). The eight bits are
\[
(0,[r=0],[r=1],[p=2],[2r=0],[r=2],[2r=1],[r=-1]),
\]
with scalar equalities modulo \(p\). If \(q>p\), additional translations outside \(\mathbb F_pb\) give exactly \((0,0,0,[p=2],[p=2],0,0,0)\). Every \(y=(c,d)\) with \(c\ne1\) gives exactly \((0,0,0,[p=2],[c=-1],0,0,0)\), independently of \(d\). Finally the identity first element has the immediately obtained diagrams \(y=e\), nonzero translations, and the multiplicative cosets. These formulas are exhaustive and yield the independent executable evaluator in `verify.py`.

**3. Uniform reduction to the table.** The nontranslation formulas depend only on the collisions among \(0,j,2j,-j\), the roots of \(2h\equiv j\pmod m\), and the involution residue \(m/2\), if it exists. For an element whose multiplier has order \(d\), these collisions reduce to the five disjoint cases \(d=2\), \(d=3\), \(d=4\), \(d\ge5\) with a square root, and \(d\ge5\) without a square root. The order-four case has a root precisely when \(8\mid m\); the order-three case has a second, distinct root precisely when \(m\) is even. For \(d\ge5\), roots exist exactly when \(2h\equiv j\pmod m\) is soluble. If \(m\) is odd, they always exist. If \(m\) is even, the no-root case occurs for some \(d\ge5\) exactly when \(m\ge6\); a root-bearing case occurs whenever \(m\) has an odd divisor at least five or an even divisor at least six with strictly smaller \(2\)-adic valuation than \(m\).

The translation formula adds a generic root-bearing type when \(p\ge5\); when \(p=3\) it instead contributes a type with a three-cycle of coincidences, and when \(p=2\) only involutions. For \(p\ge5\) and \(q>5\), the complete spectra thus depend **only** on whether \(3\mid m\) and whether \(\nu_2(m)\) equals one, two, or at least three. The smallest field \(q=5\) is exceptional because \(m=4\) lacks a generic no-root multiplier.

For \(p=2\), \(m=2^f-1\) is odd: \(f=1,2\) are exceptional, and for \(f\ge3\) the remaining spectrum depends only on \(3\mid m\), equivalently the parity of \(f\). For \(p=3\), \(3\nmid m\), and \(\nu_2(3^f-1)=1\) for odd \(f\), equals three for \(f\equiv2\pmod4\), and equals at least four for \(4\mid f\). The explicit formulas yield four spectra: \(f=1\), \(f=2\), odd \(f\ge3\), and even \(f\ge4\); the order-three translation root behaves differently from an order-three complement root. These are exactly rows B,G,M,O. The \(p=2\) cases and the \(p\ge5\) cases produce the other eleven rows.

**4. Distinctness and sharpness.** Evaluate the preceding *complete* formulas at the fifteen least representatives \(q=2,3,4,5,7,8,9,11,13,16,17,25,27,29,81\). Their finite sets \(T(G_q)\) are pairwise distinct, as certified by `verify.py`, which enumerates every possible multiplier residue and second-element diagram, and independently checks actual group multiplication for fifteen small field orders. No statement about arbitrary \(q\) is inferred from this enumeration: Step 3 proves that the fifteen representatives exhaust every field order. Since the last class has smallest representative \(q=81\), the optimal maximum representative group size is \(81\cdot80=6480\).

## Verification
Run `python3 verify.py` with Python 3 and SymPy installed; the exact expected output is embedded as `verification_output.txt`. The evaluator computes mathematical truth vectors, not probability samples. `direct_profile` independently constructs field arithmetic and explicitly checks every ordered pair for field orders \(2,3,4,5,7,8,9,11,13,16,17,19,25,27,29\). The infinite case split is supplied in Step 3 and is not validated merely by checks through a finite cutoff.

## Relationship to prior work
Gomaa's 2007 dissertation, Chapter 3, fixes the same ternary-relational group language and applies Ehrenfeucht–Fraïssé games to cyclic and general finite abelian groups, with a section on dihedral groups. Its inspected Chapter 3 and bibliography do **not** give the fifteen-class classification for nonabelian affine groups. The standard one-dimensional affine-group semidirect product and orders are independently recorded in OEIS A220211 (2012); neither the elementary multiplication description nor group-order sequence gives the rank-two partition. Relevant research-index records on scalar Frobenius groups concern character-theoretic invariants and generating graphs, rather than this rank-two logical partition. The classification here is a separately proved extension to a natural sharply two-transitive nonabelian family, not a restatement of the known finite-field group structure.

## Limitations
This is a bounded-quantifier-rank, language-dependent classification. It does not classify higher logical ranks, affine groups in multiple dimensions, or arbitrary semidirect products. This is a self-review; no independent audit was performed. Unindexed equivalent historical work cannot be ruled out by a finite literature search.

## References
1. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland dissertation, publicly dated 2007-07-06, Chapter 3. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. B. Schott, OEIS A220211, *The order of the one-dimensional affine group in the finite fields*, 2012-12-07 initial author date, updated commentary 2012-12-22. https://oeis.org/A220211
3. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, DOI:10.1142/S0218196710006047.
