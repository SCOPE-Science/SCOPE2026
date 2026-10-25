# Seven two-round theories of finite dicyclic groups

## Finding

Let \(\operatorname{Dic}_n\), for every integer \(n\ge2\), be the dicyclic group
\[
\langle a,b\mid a^{2n}=1,\ b^2=a^n,\ bab^{-1}=a^{-1}\rangle.
\]
Consider the first-order language with equality, an identity constant \(e\), and one ternary predicate \(R(u,v,w)\) interpreted as \(uv=w\); there is **no multiplication function symbol**. Write \(G\equiv_2 H\) when the two groups satisfy the same first-order sentences of quantifier rank at most two in this language.

**Theorem.** For all integers \(m,n\ge2\),
\[
\operatorname{Dic}_m\equiv_2\operatorname{Dic}_n
\iff
\bigl(m=n\in\{2,3,4\}\bigr)
\ \lor\ 
\bigl(m,n\ge5,\ [3\mid m]=[3\mid n],\ [4\mid m]=[4\mid n]\bigr).
\]
Here brackets denote truth values. Exactly **seven** rank-two theories occur. Their unique least-index representatives are indexed by \(2,3,4,5,6,8,12\), and have orders \(8,12,16,20,24,32,48\), respectively. In particular every group in this infinite family is rank-two equivalent to one with at most \(48\) elements, and the bound is attained by the class of \(\operatorname{Dic}_{12}\).

For example \(\operatorname{Dic}_5\equiv_2\operatorname{Dic}_7\equiv_2\operatorname{Dic}_{10}\), whereas \(\operatorname{Dic}_6\not\equiv_2\operatorname{Dic}_8\). The finite generalized quaternion \(2\)-groups form the power-of-two-index subfamily; the theorem also covers the non-\(2\)-group dicyclic cases.

## Assumptions and scope

All indices are integers at least two, groups are finite, and all relations are interpreted in the **ternary relational multiplication** signature described above. The result is not about the functional multiplication signature, which permits nesting group terms in atomic formulas, nor about ranks greater than two. We use the standard finite-structure Ehrenfeucht–Fraïssé characterization of quantifier rank.

Every element has a unique form \(a^j\) or \(a^j b\) with \(j\in\mathbb Z/(2n)\). Let \(z=a^n\), the unique involution. Every \(a^j b\) has order four and square \(z\). The cyclic subgroup \(\langle a\rangle\) has order \(2n\), and a cyclic element \(a^k\) is a square in the whole group, unless it equals \(z\), precisely when \(k\) is even. The exceptional element \(z\) is always a square of an element outside the cyclic subgroup.

## Proof

**1. The complete two-variable atomic test.** Fix two chosen group elements \(x,y\), along with the named identity \(e\). Their atomic diagram is the truth assignment to all equalities between \(e,x,y\), and all formulas \(R(s,t,u)\) where each of \(s,t,u\) lies in \(\{e,x,y\}\). No other atomic formulas exist. If \(x\ne e\) and \(y\notin\{e,x\}\), all nontrivial information in this diagram is the truth of
\[
V:[y^2=e],\qquad F:[y=x^2],\qquad G:[y^2=x],\qquad H:[xy=e],
\]
plus the fixed bit \([x^2=e]\). Indeed products equal to one of the selected values either involve an identity, a square, or the inverse relation; for example \(xy=x\) forces \(y=e\) and \(xy=y\) forces \(x=e\). The case \(x=e\), the case \(y=e\), and the case \(y=x\) are separately determined by identity and the involution bit. Hence a pointed rank-one theory is exactly determined by the involution bit and the set of occurring four-bit \((V,F,G,H)\) patterns for admissible \(y\), with the distinguished identity case handled separately.

For compactness write the following distinct patterns:
\[
U=(0,0,0,0),\ I=(1,0,0,0),\ E=(0,0,0,1),\ F_0=(0,1,0,0),\\
T=(0,1,1,1),\ J=(1,1,0,0),\ S=(0,0,1,0).
\]
An exhaustive case analysis, given immediately below, yields **exactly eight possible pointed rank-one types** over the entire dicyclic family:

| Type of \(x\) | Involution bit | Attainable patterns for \(y\notin\{e,x\}\) |
| --- | --- | --- |
| \(x=e\) | distinguished identity | identity-specific, independent of \(n\) |
| \(x=z\), \(n=2\) | 1 | \(\{S\}\) |
| \(x=z\), \(n\ge3\) | 1 | \(\{U,S\}\) |
| order four, not a square | 0 | \(\{U,E,J\}\) |
| order four, a square | 0 | \(\{U,E,J,S\}\) |
| order three | 0 | \(\{U,I,T,S\}\) |
| order at least five, not a square | 0 | \(\{U,I,E,F_0\}\) |
| order at least five, a square | 0 | \(\{U,I,E,F_0,S\}\) |

Here the phrase “not a square” for an order-four or larger element means no group element has square \(x\), not that its own square is absent. The eight rows are pairwise distinguishable as pointed rank-one types; the identity row is distinguished by \(x=e\), and the others by their listed bits/pattern sets.

**2. Proof that this pattern table is complete, uniformly in the index.** For \(x\notin\{e,z\}\), an admissible \(y=x^{-1}\) realizes \(E\) unless \(x\) has order three, when \(x^{-1}=x^2\) realizes \(T\). The value \(y=x^2\) realizes \(J\) when \(x\) has order four, \(T\) when it has order three, and \(F_0\) when it has order at least five. The unique involution \(y=z\) realizes \(J\) for order-four \(x\) and \(I\) otherwise. Each additional square root of \(x\), distinct from \(e,x,x^{-1},x^2\), realizes \(S\). Such a root exists exactly for square elements except that for order three one root is already \(x^{-1}\); the other, \(zx^{-1}\), realizes \(S\). For an order-four element outside \(\langle a\rangle\), no square root exists because every square lies in \(\langle a\rangle\).

The generic pattern \(U\) always occurs for nonidentity \(x\ne z\): if \(x\in\langle a\rangle\), choose any \(y\) outside it; if \(x\) lies outside, choose another element of the same coset distinct from \(x,x^{-1}\). For \(x=z\), every \(a^j b\) realizes \(S\). An \(a^j\) realizing \(U\) exists precisely when \(n\ge3\), for example \(y=a\). If \(n=2\), every element other than \(e,z\) has square \(z\), so only \(S\) occurs. All remaining possibilities are impossible by the four defining equations and the facts about squares above. This proves the table without a finite-index assumption or computational extrapolation.

**3. Which pointed types occur?** Three types occur in every group: the identity type, the nonsmall involution type except at \(n=2\), and the nonsquare order-four type (witnessed by \(b\)). For every \(n\ge3\), the element \(a\) has order \(2n\ge6\) and is not a square, so the nonsquare large-order type occurs. A square of order at least five exists precisely when \(n\ge5\), witnessed by \(a^2\), whose order is \(n\). An order-three element exists precisely when \(3\mid n\). Finally an order-four square exists precisely when \(4\mid n\): inside \(\langle a\rangle\) such an element is \(a^{n/2}\) or its inverse, and its square root equation \(2j\equiv n/2\pmod{2n}\) is solvable precisely when four divides \(n\). Outside elements are never squares. At \(n=2\), all nonidentity, noninvolutory elements have order four, and the exceptional involution type replaces the regular one.

Therefore, at \(n=2\) the rank-one pointed-type spectrum contains three of the table's types; at \(n=3\) it contains the identity, regular involution, nonsquare order-four, order-three, and nonsquare large-order types; at \(n=4\) it contains the identity, regular involution, nonsquare order-four, square order-four, and nonsquare large-order types. For every \(n\ge5\) it contains exactly the five base types (identity, regular involution, nonsquare order-four, nonsquare large-order, square large-order) and, independently, the order-three type if \(3\mid n\) and the square order-four type if \(4\mid n\).

**4. From pointed types to sentences.** The two-round Ehrenfeucht–Fraïssé criterion says that two structures have the same rank-two sentences if and only if their sets of pointed rank-one types coincide: a first move selects \(x\), and the second move tests precisely which atomic diagrams are possible with \(y\). The seven distinct spectra described in Step 3 are therefore exactly the seven rank-two equivalence classes asserted. Their least positive indices are \(2,3,4,5,6,8,12\), giving maximal least order \(4\cdot12=48\). This proves the theorem and sharpness.

## Verification

The included independent Python file `verify.py` constructs \(\operatorname{Dic}_n\) directly from ordered pairs and its multiplication law. It computes complete atomic diagrams of \((e,x,y)\), first with every element as a possible first move and then with automorphism-orbit representatives. The two computations agree for \(2\le n\le18\). Separately it checks the four-bit case table for \(2\le n\le40\), verifies pairwise distinction of all seven representatives, and compares the direct two-round signatures with the theorem's class formula for \(2\le n\le100\). Its recorded output is `verification_output.txt` and ends `VERIFY_OK`. The infinite proof is the case analysis in the preceding section, not the finite verification alone.

## Relationship to prior work

Gomaa's 2007 dissertation, particularly Chapter 3, develops Ehrenfeucht–Fraïssé methods for finite groups in the same relational multiplication signature, including finite abelian groups and bounds for dihedral groups. Those bounds do not determine the rank-two equivalence classes of the non-split dicyclic family. The documented quaternion group presentation and its element orders are standard algebraic facts, also represented in the Mathlib documentation. Previously published work on dicyclic noncyclic graphs concerns reconstruction from a different invariant, not sentences of quantifier rank two. The present classification addresses the interaction between a single involution, square roots of order-four elements, and divisibility by three in the index.

## Limitations

The result covers only the indicated family and precisely quantifier rank two in ternary relational group multiplication. It does not claim a corresponding classification in functional multiplication languages or at higher ranks. Independent audit has not been performed; a logically equivalent historical classification outside the inspected references may exist. The numerical checks are finite consistency tests, not replacements for the uniform group-theoretic argument.

## References

1. Walid Gomaa, *Model Theory and Complexity Theory*, University of Maryland doctoral dissertation, public repository date 2007-07-06, Chapter 3. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. *Mathlib.GroupTheory.SpecificGroups.Quaternion*, documentation of dicyclic-group multiplication and order formulas. https://math.iisc.ac.in/~gadgil/proofs-and-programs-2023/doc/Mathlib/GroupTheory/SpecificGroups/Quaternion.html
3. Walid Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, DOI 10.1142/S0218196710006047.
