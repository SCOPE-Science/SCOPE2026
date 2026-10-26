# Fifteen two-round theories of finite abelian 2-groups

## Finding

Let \(G\) range over all finite abelian groups of order a power of two, including the trivial group. In the first-order language consisting of equality, a named identity \(0\), and one ternary relation \(R(x,y,z)\) interpreted as \(x+y=z\), there are **exactly fifteen** quantifier-rank-two theories. Each theory is realized by a group on the following list, and no two listed groups are rank-two equivalent:

\[
\begin{gathered}
1,\ C_2,\ C_2^2,\ C_4,\ C_2\oplus C_4,\ C_4^2,\ C_2\oplus C_4^2,\\
C_8,\ C_2\oplus C_8,\ C_4\oplus C_8,\ C_8^2,\\
C_{16},\ C_2\oplus C_{16},\ C_4\oplus C_{16},\ C_8\oplus C_{16}.
\end{gathered}
\]

Every finite abelian 2-group is rank-two equivalent to exactly one representative in this list. The maximum minimal representative order is **128**, attained only by the class represented by \(C_8\oplus C_{16}\). This maximum is sharp **within the stated family**.

The following explicit rule determines the representative. Write
\(G\cong\bigoplus_{i=1}^r C_{2^{a_i}}\), with \(a_i\geq1\), and define \(t=\#\{i:a_i\geq2\}\), \(u=\#\{i:a_i\geq3\}\), and \(v=\#\{i:a_i\geq4\}\). Thus \(r\geq t\geq u\geq v\geq0\). Read the first applicable row:

| Condition | Rank-two representative |
|---|---|
| \(r=0\) | \(1\) |
| \(t=0,r=1\) | \(C_2\) |
| \(t=0,r\geq2\) | \(C_2^2\) |
| \(u=0,t\geq1,r=t=1\) | \(C_4\) |
| \(u=0,t\geq1,r>t,t=1\) | \(C_2\oplus C_4\) |
| \(u=0,t\geq2,r=t\) | \(C_4^2\) |
| \(u=0,t\geq2,r>t\) | \(C_2\oplus C_4^2\) |
| \(v=0,u\geq1,r=t=u=1\) | \(C_8\) |
| \(v=0,u\geq1,r>t\) | \(C_2\oplus C_8\) |
| \(v=0,u\geq1,r=t>u\) | \(C_4\oplus C_8\) |
| \(v=0,u\geq1,r=t=u\geq2\) | \(C_8^2\) |
| \(v\geq1,r=t=u=1\) | \(C_{16}\) |
| \(v\geq1,r>t\) | \(C_2\oplus C_{16}\) |
| \(v\geq1,r=t>u\) | \(C_4\oplus C_{16}\) |
| \(v\geq1,r=t=u\geq2\) | \(C_8\oplus C_{16}\) |

In particular \(C_{16}\equiv_2 C_{32}\), although their sizes and exponents differ. There is no assertion of full elementary equivalence or of equivalence at quantifier rank three.

## Assumptions and scope

A finite abelian 2-group means an abelian group of order \(2^k\) for an integer \(k\geq0\). Its cyclic-factor multiset is unique. The language has a ternary **relation**, not a binary function: the entire equation \(x+y=z\) is atomic, but a nested term such as \(2(2x)\) is not a term of this language. Quantifier rank is nesting depth, with Boolean combinations taking the maximum depth. The equivalence relation \(G\equiv_2 H\) means agreement on **all** first-order sentences of rank at most two, without any variable-count or prenex restriction.

## Proof

**1. Exact two-round criterion.** For each \(x\in G\) define \(P_G(x)\) as the set of all quantifier-free atomic diagrams of the ordered pair \((x,y)\), with the named constant \(0\), as \(y\) ranges over \(G\). A two-round Ehrenfeucht–Fraïssé game has a winning duplicator strategy precisely when the two structures have the same sets \(\{P_G(x):x\in G\}\). Indeed, the first response must match the entire collection of possible second-round diagrams, regardless of which structure the second move is in; the converse uses a mismatched diagram as a second move. Unary atomic facts are included in every paired diagram. The standard game/sentence equivalence therefore gives \(G\equiv_2 H\) exactly when these collections agree.

**2. Complete atomic reduction.** Over the selected values \(0,x,y\), all equality atoms and every instance of \(R\) reduce to the eight Boolean tests

\[
 x=0,\quad y=0,\quad x=y,\quad 2x=0,\quad 2y=0,\quad
 x+y=0,\quad 2x=y,\quad 2y=x.
\]

The test order above encodes each atomic diagram as a bit mask \(\sum_{i=0}^7 2^i b_i\). For example, the constant pair \((0,0)\) has mask 255. No multiplication of three selected nonconstant elements is suppressed: all ternary \(R\)-instances on these values are equivalent to one of the displayed tests or its simple equality consequence.

**3. Universal pointed-profile lemma.** Put \(r=\dim_{\mathbf F_2}G[2]\); then \(|G[2]|=2^r\), and every nonempty fibre of doubling \(y\mapsto2y\) has exactly \(2^r\) members. Classify the first element \(x\) as \(Z\) (zero), \(I_+\) or \(I_-\) (order two, respectively in or outside \(2G\)), \(IV_+\) or \(IV_-\) (order four, respectively in or outside \(2G\)), and \(L_+\) or \(L_-\) (order at least eight, respectively in or outside \(2G\)). All members of each occurring category realize the same \(P_G(x)\). Here are the complete masks; conditional entries are included only under the accompanying condition:

| Category | Unconditional masks | Additional masks and conditions |
|---|---|---|
| \(Z\) | \(255\) | \(153\) if \(r>0\); \(9\) if \(t>0\) |
| \(I_+\) | \(60,90,136\) | \(24\) if \(r\geq2\); \(8\) if \(u>0\) or \(t\geq2\) |
| \(I_-\) | \(60,90\) | \(24\) if \(r\geq2\); \(8\) if \(t>0\) |
| \(IV_+\) | \(0,4,18,32,80,128\) | \(16\) if \(r\geq2\) |
| \(IV_-\) | \(4,18,32,80\) | \(16\) if \(r\geq2\); \(0\) unless \(G\cong C_4\) |
| \(L_+\) | \(0,4,16,18,32,64,128\) | none |
| \(L_-\) | \(0,4,16,18,32,64\) | none |

For completeness, derive the table rather than merely enumerating it. For fixed \(x\), every \(y\) satisfying one of the four equality/equation exceptions lies in
\(F_x=\{0,x,-x,2x\}\) or in the fibre \(\{y:2y=x\}\). Outside this union, the only remaining distinction is whether \(2y=0\). The sets \(F_x\) have respectively 1, 2, 4, and 4 members as the order of \(x\) is 1, 2, 4, and at least 8. Roots of \(2y=x\) exist exactly when \(x\in2G\), and every root fibre has size \(2^r\). For an order-two \(x\in2G\), a non-involutory nonroot remains exactly when \(|G|>2^{r+1}\), equivalent to \(u>0\) or \(t\geq2\); otherwise all non-involutions are roots. For an order-four \(x\), a generic non-involution remains except in the one-factor group \(C_4\), since its cardinality is \(|G|-2^r-2\) if \(x\notin2G\) and \(|G|-2^{r+1}-2\) if \(x\in2G\). For order at least eight these counts, with 3 rather than 2 exceptional non-involutions, are strictly positive whenever that category occurs. Generic involutions exist for order-two and order-four \(x\) exactly when \(r\geq2\), while for order at least eight a nonzero generic involution always exists. Directly evaluating the eight atomic tests on each of these disjoint possibilities yields every mask displayed in the table, with no omitted case.

**4. Which pointed categories occur.** The zero category always occurs. The two order-two categories occur precisely when \(t>0\) and \(r>t\), respectively. The order-four categories occur precisely when \(u>0\), and when \(t>0\) together with \((t>u\text{ or }r>t)\), respectively. The two order-at-least-eight categories occur precisely when \(v>0\) and \(u>0\), respectively. For example, \(t\) is the number of cyclic factors capable of supplying a nonzero involution in \(2G\), and the presence of a smaller cyclic factor produces an order-four element outside \(2G\) by adding a generator of that factor to an order-four element. Conversely, coordinatewise doubling rules out the excluded categories. These conditions follow immediately from the unique cyclic-factor decomposition and apply at arbitrarily high exponents and ranks.

**5. Fifteen-class conclusion.** Combining the occurrence conditions from step 4 with the complete mask profiles in step 3 yields exactly the fifteen cases in the first table. This reduction uses only the comparisons \(r>t\), \(t>u\), \(r=1\), \(t=1\), and the positivity of \(t,u,v\): no large-exponent or large-rank case is excluded by a finite search bound. Computing the distinct complete mask-signature sets for the fifteen representatives gives fifteen different signatures; their full values and a separately implemented enumeration check are supplied in the accompanying reproducibility artifacts. By step 1, different signatures are distinguishable by first-order sentences of quantifier rank at most two. Thus the classification is exact, both for equivalences and for separations.

**6. Sharpness.** The last signature requires \(v>0\), \(r=t=u\geq2\). Hence at least two cyclic summands have exponent at least eight, and at least one has exponent at least sixteen. Its minimal order is \(8\cdot16=128\). The remaining fourteen displayed representatives have smaller order. Since all fifteen signatures differ, no abelian 2-group of smaller order can represent the last theory. Thus the claimed maximum is optimal within this family.

## Verification

Run `python3 verify.py` and `python3 direct.py` using Python 3 and no third-party packages. The first script evaluates the closed profile formula for all multiplicity quadruples in a finite stress-test domain, then compares the formula with direct enumeration of the eight atomic tests for all cyclic partitions with total exponent at most eight. The second script independently enumerates **all** ternary \(R\)-atoms and equalities on the three selected values for the fifteen representatives; it does not call the mask reduction. Both check that the representatives are pairwise nonequivalent. Machine-readable complete signatures are in `profile_table.json`. Recorded outputs are in `verify_output.txt` and `direct_output.txt`. The infinite part of the proof is steps 1–5, not any finite testing bound.

## Relationship to prior work

Walid Gomaa's 2007 dissertation, *Model Theory and Complexity Theory*, Chapter 3, and the author-accessible full text of his 2010 article, *Descriptive Complexity of Finite Abelian Groups*, give Ehrenfeucht–Fraïssé upper/lower depth bounds for finite abelian groups and discuss the ternary group language used here. Their general estimates and the cyclic-group cases are **not** claimed as new. The inspected Chapter 3, Section 3.7 (dissertation pages 85–86), and the corresponding article Section 7 (article pp. 17–18) provide a general complexity comparison, not this exact fifteen-class rank-two spectrum or the optimal order-128 representative. The bound here is an explicit complete low-rank classification rather than a general distinguishing-complexity estimate. Searches also compared equivalent phrases using two-round games, finite abelian 2-groups, cyclic invariants, and short first-order types; no implication from a stronger identified published classification was established. This absence of a located source does not prove historical uniqueness.

## Limitations

The classification is specific to the relational language \(\{0,R\}\), finite abelian 2-groups, and quantifier rank at most two. It does not classify general finite abelian groups containing odd-primary components, all finite 2-groups, group structures in a binary-function language, or any rank-three theory. The proof and computational certificates are self-review; independent scientific validation has not been performed. Earlier or less-indexed literature may contain an equivalent exact classification.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland PhD dissertation (2007), deposited 2007-07-06, Chapter 3, Sections 3.2 and 3.7. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation **20** (2010), 1087–1116, DOI 10.1142/S0218196710006047; article Section 7. https://doi.org/10.1142/S0218196710006047
3. L. Libkin, *Elements of Finite Model Theory*, Springer (2004), for standard Ehrenfeucht–Fraïssé game equivalence. No new technical lemma is attributed to this reference.
