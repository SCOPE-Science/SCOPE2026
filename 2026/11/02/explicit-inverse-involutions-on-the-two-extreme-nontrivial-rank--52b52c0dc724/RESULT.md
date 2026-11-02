# Explicit inverse involutions on the two extreme nontrivial rank classes of order-preserving transformations

## Finding
Let \(\mathcal O_n\) be the monoid of all order-preserving self-maps of the chain \([n]=\{1,\ldots,n\}\), where \(n\ge3\). A **matching by inverses** on a subset \(D\subseteq\mathcal O_n\) means a map \(\iota:D\to D\) with \(\alpha\iota(\alpha)\alpha=\alpha\) and \(\iota(\alpha)\alpha\iota(\alpha)=\iota(\alpha)\). An **involution matching** additionally satisfies \(\iota^2=\mathrm{id}_D\).

**Theorem.** The rank-two Green \(\mathcal D\)-class \(D_2\) and the rank-\((n-1)\) Green \(\mathcal D\)-class \(D_{n-1}\) of \(\mathcal O_n\) each admit an explicit involution matching that fixes precisely their idempotents. In each case the matching is defined by the following formulas, valid for every \(n\ge3\). When \(n=3\) the two classes coincide; both formulas remain valid independently.

**Rank two:** Encode a map by \((a;b,c)\), where \(1\le a<n\), \(1\le b<c\le n\), and it takes value \(b\) on \(\{1,\ldots,a\}\) and value \(c\) on \(\{a+1,\ldots,n\}\). Define
\[
\iota_2(a;b,c)=
\begin{cases}
(a;b,c),&b\le a<c,\\
(c-1;a,b),&a<b<c,\\
(b;c,a+1),&b<c\le a.
\end{cases}
\]
This matching has exactly \(\binom{n+1}{3}\) fixed points and \(\binom n3\) two-cycles, on a class of size \((n-1)\binom n2\). The nontrivial pairs are naturally indexed by triples \(\{a<b<c\}\subseteq[n]\).

**Rank \(n-1\):** Encode a map by \((a;b)\), where \(1\le a<n\) specifies the unique nonsingleton kernel block \(\{a,a+1\}\) and \(1\le b\le n\) specifies its missing image point. Define
\[
\iota_{n-1}(a;b)=
\begin{cases}
(a;b),&b\in\{a,a+1\},\\
(b;a+1),&b<a,\\
(b-1;a),&b>a+1.
\end{cases}
\]
This matching has exactly \(2(n-1)\) fixed points and \(\binom{n-1}{2}\) two-cycles, on a class of size \(n(n-1)\).

This is a theorem about two specified rank classes, **not** an involution matching of the entire monoid \(\mathcal O_n\) for all \(n\). In particular, nothing is asserted for intermediate ranks \(3\le r\le n-2\).

## Assumptions and scope
Functions act on the right in the conventional semigroup notation, but the formulas are composition-convention independent because they assert both sandwich identities. The rank of a map means the cardinality of its image. The two indicated parameterizations are bijective: a rank-two isotone function has a unique cut point and two increasing image values; a rank-\((n-1)\) isotone function has exactly one adjacent pair in a common kernel block and exactly one omitted image value. The latter description uses \(n\ge3\). For \(n=3\), both describe the same class but assign different coordinate labels.

## Proof
**Cross-transversal lemma.** Consider two isotone transformations \(\alpha,\beta\) of the same rank \(r\), with respectively ordered interval kernel blocks \(A_1,\ldots,A_r\) and \(C_1,\ldots,C_r\), and respective ordered images \(B=\{b_1<\cdots<b_r\}\) and \(D=\{d_1<\cdots<d_r\}\). Then \(\beta\) is a semigroup inverse of \(\alpha\) if and only if
\[
 d_i\in A_i\quad\text{and}\quad b_i\in C_i\qquad(1\le i\le r).
\]
Indeed, if these inclusions hold, then \(\beta(b_i)=d_i\) and \(\alpha(d_i)=b_i\). Consequently \(\alpha\beta\alpha=\alpha\) and \(\beta\alpha\beta=\beta\). Conversely, if both sandwich identities hold, the composite \(\alpha\beta\) fixes \(B\) and \(\beta\alpha\) fixes \(D\). The rank restrictions force these maps to carry each ordered image value into the correspondingly numbered kernel block, proving the inclusions. The lemma also follows from the crossed-square description of regular combinatorial \(\mathcal D\)-classes in Higgins (2026), but the preceding argument is direct.

For rank two, \(A_1=[1,a]\), \(A_2=[a+1,n]\). An image pair \(\{x<y\}\) is a transversal of this partition exactly when \(x\le a<y\). Hence \((a;b,c)\) and \((d;x,y)\) are mutual inverses exactly when
\[
 x\le a<y\quad\text{and}\quad b\le d<c.
\]
For \(b\le a<c\), the map is idempotent and is assigned to itself. If \(a<b<c\), its partner is \((c-1;a,b)\); the two inequalities are \(a\le a<b\) and \(b\le c-1<c\). Its partner lies in the opposite branch \(a\le b\le c-1\) (using the partner's coordinates), and substitution in that branch recovers the original triple. If \(b<c\le a\), the partner is \((b;c,a+1)\), and the inequalities become \(c\le a<a+1\) and \(b\le b<c\); substitution in the \(a<b<c\) branch recovers the original. These three cases partition all admissible rank-two data, so the map is a well-defined involution by inverses. A rank-two map is idempotent exactly when its image crosses its cut, that is, \(b\le a<c\). Thus the fixed points are precisely the idempotents.

For rank \(n-1\), every kernel block is a singleton except \(\{a,a+1\}\). An \((n-1)\)-element image subset is a transversal exactly when its omitted element lies in \(\{a,a+1\}\). Therefore \((a;b)\) and \((c;d)\) are mutual inverses exactly when
\[
 d\in\{a,a+1\}\quad\text{and}\quad b\in\{c,c+1\}.
\]
If \(b\in\{a,a+1\}\), the map is idempotent and is fixed. If \(b<a\), the assigned partner \((b;a+1)\) satisfies both displayed inclusions and is in the branch where its omitted point exceeds its double-block index by at least two; the reverse branch maps it back to \((a;b)\). If \(b>a+1\), the partner \((b-1;a)\) satisfies both inclusions and is in the branch where the omitted point lies below the double-block index; again the reverse branch maps back. Thus this is also an involution by inverses fixing precisely the idempotents.

Finally, rank two has \((n-1)\binom n2\) elements. Its idempotents are counted by \(\sum_{a=1}^{n-1}a(n-a)=\binom{n+1}{3}\). Every remaining element lies in a two-cycle, so the number of such cycles is \(\frac12\big((n-1)\binom n2-\binom{n+1}{3}\big)=\binom n3\). This also follows directly: each strictly increasing triple \(a<b<c\) gives exactly the pair \((a;b,c)\leftrightarrow(c-1;a,b)\). Rank \(n-1\) has \(n(n-1)\) elements; its idempotents are exactly the two missing-image choices for each \(a\), hence \(2(n-1)\). The remaining \((n-1)(n-2)\) elements form \(\binom{n-1}{2}\) two-cycles. All formula boundaries hold also at \(n=3\), where both classes coincide. This completes the proof.

## Verification
The standalone file `verify.py` generates every map of the two indicated ranks for \(2\le n\le18\); it verifies injectivity of the parameters, the involution property, both semigroup inverse sandwich identities by actual function composition, fixed-point/idempotent equivalence, and every displayed counting formula. The recorded run in `verification_output.txt` ends with `VERIFY_OK`. This is a finite cross-check only. The displayed case analysis and transversal lemma prove the result for all \(n\ge3\).

## Relationship to prior work
Higgins (2026, Theorem B) proves that the **whole** monoid \(\mathcal O_n\) has a permutation matching, using balanced weightings of the transversal incidence matrices. This is weaker than requiring a matching to have order two; the new formulas specify order-two maps for the two extreme nontrivial rank classes and reveal their precise cycle structures. Higgins (2014, 2019, 2024) develops inverse matchings and involution matchings; in particular the 2019 result gives an involution for the larger orientation-preserving monoid, without asserting that this particular involution preserves its order-preserving submonoid. The 2024 paper explicitly distinguishes the permutation and involution questions. The present result does not reprove the permutation theorem for the entire \(\mathcal O_n\).

## Limitations
No construction is provided for intermediate rank classes, and no all-ranks involution theorem follows. The displayed involutions need not be semigroup antihomomorphisms or be uniquely determined by the inverse relation. No claim of complete historical priority is made; the exact formulas might be independently derivable from older transformation-monoid methods. The verification script is not a proof for unbounded \(n\).

## References
- P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1 (submitted 2026-10-01), especially Theorems A and B and Section 3. https://arxiv.org/pdf/2610.01912
- P. M. Higgins, *Permutations of a semigroup that map to inverses*, Semigroup Forum **89** (2014), 169–182. https://repository.essex.ac.uk/11534/1/Permutations%20by%20inverses%20final.pdf
- P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum **98** (2019), 669–689. https://arxiv.org/pdf/1811.04472
- P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum **109** (2024), 141–147. https://doi.org/10.1007/s00233-024-10430-0
