# Fifteen two-round theories of finite cyclic groups, with a sharp 24-element kernel

## Finding

Let \(C_n=(\mathbb Z/n\mathbb Z;R,0)\), for each integer \(n\ge1\), in the **relational** first-order language consisting of equality, a constant \(0\), and \(R(x,y,z)\) meaning \(x+y=z\). Addition is **not** a function symbol. Write \(\equiv_2\) for agreement on every first-order sentence of quantifier rank at most two. Then

\[
\boxed{C_m\equiv_2 C_n\quad\Longleftrightarrow\quad
\bigl(m=n\in\{1,2,3,4,5,6,8\}\bigr)
\ \lor\
\bigl(m,n\notin\{1,2,3,4,5,6,8\}\ \land\ \gcd(m,24)=\gcd(n,24)\bigr).}
\]

There are exactly **15** rank-two theories in this infinite family. Their minimum-order representatives are

\[
C_1,C_2,C_3,C_4,C_5,C_6,C_7,C_8,C_9,C_{10},C_{12},C_{16},C_{18},C_{20},C_{24}.
\]

The optimal uniform representative-size bound **within the cyclic family** is 24 elements. In particular, \(C_{24}\) is not rank-two equivalent to any smaller cyclic group, while every larger cyclic group is rank-two equivalent to one of the listed representatives.

## Assumptions and scope

All groups are finite and cyclic, including the trivial group. Quantifier rank counts nesting depth, not the total number of quantifiers across separate branches. The constant \(0\) is named, and the only operation information available atomically is the ternary addition relation. The result would be a different question if addition were a function symbol, inverse were named, or counting quantifiers were allowed. The classification concerns equivalence within the stated family, not the minimum cardinality of an arbitrary structure sharing a theory.

## Proof

**1. The complete two-point atomic diagram.** With a previously selected element \(x\), a prospective second choice \(y\), and the named identity \(0\), every atomic equation, including all permutations of arguments to \(R\), is determined by eight Boolean conditions:

\[
\begin{gathered}
x=0,\quad y=0,\quad x=y,\quad 2x=0,\quad 2y=0,\\
2x=y,\quad 2y=x,\quad x+y=0.
\end{gathered}
\]

Indeed, an equation with summands and target in \(\{x,y,0\}\) either is a tautological group-identity instance, asserts one of these eight conditions, or is equivalent to one of them. Let \(\alpha_n(x,y)\) denote this eight-bit vector. The *pointed one-step profile* of \(x\) is

\[
\tau_n(x)=\bigl(x=0,\;2x=0,\;\{\alpha_n(x,y):y\in C_n\}\bigr).
\]

The ordinary two-round Ehrenfeucht–Fraïssé criterion gives

\[
C_m\equiv_2 C_n\iff
\{\tau_m(x):x\in C_m\}=\{\tau_n(x):x\in C_n\}.
\]

This identity is exact: after the first selection, the second player needs only to match the quantifier-free diagram of the second selection, and every first-round selection can be matched precisely when the pointed profiles agree. Notice that multiplicities of equal profiles do not matter in two rounds.

**2. Uniform profile lemma.** Fix \(x\). A second element \(y\) may have a non-generic diagram only when it belongs to

\[
E_x=\{0,x,-x,2x\}\cup\{y:2y=0\}\cup\{y:2y=x\}.
\]

Each of the last two sets has at most two elements. Thus \(|E_x|\le8\). Every group with \(n\ge9\) has at least one \(y\notin E_x\), and all such elements have the same generic diagram. For \(n=7\), the group is odd, every nonzero \(x\) has order seven, and \(|E_x|\le5\), so the same conclusion holds.

All identifications among the special elements and all eight atomic predicates depend solely on the following finite data: whether \(n\) is odd or even; whether the order of \(x\) is \(1,2,3,4\), or at least \(5\); and whether the equation \(2y=x\) is solvable. To see completeness, the only possible coincidences among \(0,x,-x,2x\) are controlled by \(x=0\), \(2x=0\), or \(3x=0\); the predicate \(2(2x)=0\) adds the order-four case. A half of \(x\) can coincide with one of these four points only when \(x=0\) or \(3x=0\). A point satisfying \(2y=0\) is either \(0\), or the unique nonzero involution when \(n\) is even. Two halves of \(x\), when they exist, differ by that involution. This checks every possible intersection among the sets defining \(E_x\). Since a generic \(y\) is also available, there are no other profile parameters.

In a cyclic group the equation \(2y=x\) is always solvable when \(n\) is odd; when \(n\) is even, it is solvable exactly for \(x\in2C_n\). More specifically:

- order \(2\) occurs iff \(2\mid n\), and its element is a double iff \(4\mid n\);
- order \(3\) occurs iff \(3\mid n\), and its elements are always doubles;
- order \(4\) occurs iff \(4\mid n\), and its elements are doubles iff \(8\mid n\);
- when \(n\ge9\) is odd, an element of order at least five exists and is a double;
- when \(n\ge10\) is even, both a double and a non-double of order at least five exist: use the residues \(2\) and \(1\), respectively.

For \(n=7\), all nonzero elements fall in the odd, double, order-at-least-five case. Therefore, for every \(n\ge7\), \(n\ne8\), the set of realized pointed profiles depends **only** on the four divisibility facts \(2\mid n\), \(3\mid n\), \(4\mid n\), and \(8\mid n\). Those four facts are equivalent to specifying \(\gcd(n,24)\). This proves the forward direction of the asserted equivalences within the nonexceptional family.

**3. Explicit rank-two separators and the small exceptions.** Define the following formulas, writing addition notation only as a readable abbreviation for instances of \(R\):

\[
\begin{aligned}
A(x)&:=\exists y\,[2x=y\land y\ne0\land y\ne x\land 2y\ne0\land x+y\ne0],\\
H(x)&:=\exists y\,[2y=x],\\
G(x)&:=\exists y\,[y\ne0\land y\ne x\land x+y\ne0\land2x\ne y\land2y\ne0\land2y\ne x].
\end{aligned}
\]

Here \(A(x)\) holds exactly when \(x\) has order at least five; \(H(x)\) exactly when \(x\) is a double; and \(G(x)\) exactly when a generic second element exists. Consider the seven sentences

\[
\begin{aligned}
\sigma_2&:=\exists x\,[x\ne0\land2x=0],\\
\sigma_3&:=\exists x\exists y\,[x\ne0\land2x=y\land x+y=0],\\
\sigma_4&:=\exists x\exists y\,[x\ne0\land2x=0\land2y=x],\\
\sigma_8&:=\exists x\,[x\ne0\land(\exists y\,[2x=y\land y\ne0\land2y=0])\land H(x)],\\
\sigma_{\ge5}&:=\exists x\,A(x),\\
\sigma_{\mathrm{half},\ge5}&:=\exists x\,[A(x)\land H(x)],\\
\sigma_{\mathrm{generic}}&:=\exists x\,[x\ne0\land G(x)].
\end{aligned}
\]

Each displayed equation is an atomic \(R\)-instance, or an equality, and all seven sentences have quantifier rank at most two. The first four hold exactly when \(2,3,4,8\), respectively, divide \(n\). The fifth holds iff \(n\ge5\). The sixth holds iff \(n\) is odd and at least five, **or** \(n\) is even and at least ten. The seventh holds iff \(n\ge6\): it fails for every nonzero \(x\) when \(n\le5\), holds in \(C_6\) with \(x=1,y=4\), holds in \(C_7\) with \(x=1,y=3\), holds in \(C_8\) with \(x=1,y=3\), and for \(n\ge9\) follows from \(|E_x|\le8\).

The seven truth-value vectors, in the displayed order, are distinct for the 15 minimum representatives. Written as zero-one strings, they are

| \(n\) | \((\sigma_2,\sigma_3,\sigma_4,\sigma_8,\sigma_{\ge5},\sigma_{\mathrm{half},\ge5},\sigma_{\mathrm{generic}})\) |
|---:|:---|
| 1 | `0000000` |
| 2 | `1000000` |
| 3 | `0100000` |
| 4 | `1010000` |
| 5 | `0000110` |
| 6 | `1100101` |
| 7 | `0000111` |
| 8 | `1011101` |
| 9 | `0100111` |
| 10 | `1000111` |
| 12 | `1110111` |
| 16 | `1011111` |
| 18 | `1100111` |
| 20 | `1010111` |
| 24 | `1111111` |

By the uniform profile lemma, every \(n\ge9\) is equivalent to the smallest displayed representative with matching gcd with \(24\). The same applies to \(n=7\). The seven other orders \(1,2,3,4,5,6,8\) have distinct seven-sentence signatures and no signature equal to any stabilized class. Thus all 15 classes are necessary and sufficient.

**4. Sharp bound.** The gcd class \(\gcd(n,24)=24\) contains only positive multiples of \(24\), so its smallest cyclic representative has exactly 24 elements. All other class representatives are smaller. This proves sharpness.

## Verification

Run `python3 verify.py` in the same directory. It exhaustively generates **every** atomic equality and ternary-addition statement on \((x,y,0)\), independently reduces them to the eight-bit diagram, computes exact rank-two pointed profiles for all cyclic group orders through 128, checks the proposed 15-class partition pairwise, evaluates all seven distinguishing formulas, and spot-checks ten additional orders up to 360. See `VERIFY_OUTPUT.txt`. The mathematical uniform profile lemma, not the finite tests, is what proves the infinite classification.

## Relationship to prior work

W. Gomaa, *Model Theory and Complexity Theory* (2007), Chapter 3, Section 3.3, defines precisely this relational language and examines Ehrenfeucht–Fraïssé games on cyclic groups. Sections 3.4–3.7 derive bounds on distinguishing depth in terms of subgroup divisors. Those cited statements do not give the 15 exact rank-two classes or the sharp 24-element representative bound. Gomaa's later journal paper, *Descriptive Complexity of Finite Abelian Groups* (2010), treats related general depth bounds. The present result uses the standard two-round EF criterion but replaces general depth estimates with an exact two-element atomic-diagram classification.

Independent prior contributions about depth reductions for prime cyclic groups and an explicit two-quantifier separation of \(C_5\) from \(C_{25}\) address proper subcases; the latter separation follows from the current classification, but does not imply its general statement. Searches of indexed prior work have not established exact equivalent coverage. Absence from a search index is not proof of novelty.

## Limitations

This is a self-reviewed result, not an independent audit or external certification. The claimed originality is subject to equivalent results in unindexed historical literature. The classification relies essentially on treating addition as a **ternary relation**; it must not be transferred to the usual language with a binary addition function. The 24-element bound is optimal only among cyclic representatives, not among all structures in the language.

## References

1. Walid Gomaa, *Model Theory and Complexity Theory*, University of Maryland dissertation, public repository date 2007-07-06, especially Chapter 3 §§3.2–3.7. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 ; full text https://drum.lib.umd.edu/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/download.
2. Walid Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116. DOI:10.1142/S0218196710006047.
3. Leonid Libkin, *Elements of Finite Model Theory*, Springer, 2004, standard EF-game characterization of bounded quantifier-rank equivalence.
