# Seven rank-three theories of finite subspace-inclusion lattices

## Finding
For a prime power \(q\ge2\) and an integer \(d\ge0\), let \(\mathcal L_q(d)\) be the finite relational structure whose elements are **all** vector subspaces of \(\mathbf F_q^d\), including zero and the whole space, with equality and one binary relation \(\subseteq\). Neither endpoints nor lattice operations nor the rank function are named. For any such \(q,r,d,e\),
\[
\mathcal L_q(d)\equiv_3\mathcal L_r(e)
\quad\Longleftrightarrow\quad
\min(d,6)=\min(e,6).
\]
Thus the entire two-parameter family has exactly seven quantifier-rank-three first-order theories. In particular, the field order and characteristic are invisible at this rank, even at small dimensions, and every dimension at least six is indistinguishable from every other. A representative of every theory has at most \(2825\) elements, and this is the smallest possible universal bound within the family; \(\mathcal L_2(6)\) attains it.

## Assumptions and scope
First-order quantifier rank is maximum nesting depth, with unrestricted Boolean connectives and reusable variables; \(\equiv_3\) means agreement on **all sentences** of quantifier rank at most three. The field order \(q\) ranges over every prime power. The structure contains all subspaces, not only points, lines, or nontrivial subspaces. The only nonlogical relation is inclusion (strict inclusion is an abbreviation). This is an exact, uniform classification; it makes no claim for higher ranks or richer languages.

## Proof
**1. One further move from two selected subspaces.** Let \(V\) have dimension \(d\), and fix subspaces \(A,B\). Put
\[
c=\dim(A\cap B),\quad u=\dim A-c,\quad v=\dim B-c,
\quad w=d-c-u-v.
\]
All four parameters are nonnegative; conversely, every quadruple occurs, by choosing a direct-sum decomposition \(V=C\oplus U\oplus W\oplus T\) and \(A=C\oplus U\), \(B=C\oplus W\). Write \(a=c+u\) and \(b=c+v\). The atomic relation between \(A\) and \(B\) is equality when \(u=v=0\), \(A\subsetneq B\) when \(u=0<v\), \(B\subsetneq A\) when \(v=0<u\), and incomparability otherwise.

For an additional subspace \(Z\), encode its relation with each of \(A,B\) by \(0\) (equal), \(1\) (strictly below), \(2\) (strictly above), or \(3\) (incomparable). The patterns having a zero coordinate occur exactly when \(Z=A\) or \(Z=B\), and follow from the preceding atomic relation. All remaining possible patterns are characterized by the following complete table (with the first coordinate referring to \(A\)):

| Pattern | Necessary and sufficient condition |
|---|---|
| \((1,1)\) | \(a>0\) and \(b>0\) |
| \((2,2)\) | \(a<d\) and \(b<d\) |
| \((1,2)\) | \(v=0\) and \(u\ge2\) |
| \((2,1)\) | \(u=0\) and \(v\ge2\) |
| \((1,3)\) | \(a\ge2\), \(u>0\), and \(b>0\) |
| \((3,1)\) | \(b\ge2\), \(v>0\), and \(a>0\) |
| \((2,3)\) | \(d-a\ge2\), \(v>0\), and \(b<d\) |
| \((3,2)\) | \(d-b\ge2\), \(u>0\), and \(a<d\) |
| \((3,3)\) | \(0<a,b<d\) |

For example, a witness below \(A\) but incomparable with \(B\) exists precisely when \(A\) has dimension at least two, is not contained in \(B\), and \(B\) is nonzero: take a line of \(A\) outside \(B\). The dual case uses a hyperplane through \(A\) avoiding \(B\), and the final row uses a line outside the union of two proper subspaces. The chain-pattern rows follow from intermediate dimensions; the first two rows use zero and the ambient space. These constructions prove **sufficiency over every finite field**; the dimension and inclusion obstructions prove necessity. In particular, no row depends on \(q\).

Let \(F(c,u,v,w)\) denote the atomic type of \((A,B)\) together with the set of witness patterns from this table. This is exactly the one-remaining-round first-order type of the ordered pair, not merely its induced two-element order.

**2. A uniform truncation identity.** By inspection of the nine conditions, \(F\) depends only on the four parameters individually truncated at two. Moreover, uniformly in the two other parameters,
\[
F(2,2,v,w)=F(1,2,v,w),\qquad
F(c,u,2,2)=F(c,u,2,1).
\]
These two special identities follow by substituting the four coordinates into each row of the displayed table; they also appear as checked finite identities in the verifier. Increasing any coordinate already at least two does not change \(F\).

Fix \(X\) with \(a=\dim X\) and \(h=d-a\). The possible one-round types of \((X,Y)\), as \(Y\) varies over all subspaces, form the set
\[
S(a,h)=\{F(c,a-c,v,h-v): 0\le c\le a,\ 0\le v\le h\}.
\]
Every displayed split is realized by a suitable \(Y\), because \(X\) has an \(a\)-dimensional summand and its complement an \(h\)-dimensional summand. If \(a\ge4\), each split \(c+u=a\) has either one coordinate at least three, which can be reduced by one without changing \(F\), or the exceptional split \((c,u)=(2,2)\), reduced using the first identity above. Conversely, every split of \(a-1\ge3\) has a coordinate at least two and can be enlarged by one with unchanged \(F\). Hence \(S(a,h)=S(a-1,h)\) for \(a\ge4\). The second identity and its symmetric coordinate argument give \(S(a,h)=S(a,h-1)\) for \(h\ge4\). Consequently
\[
S(a,h)=S(\min(a,3),\min(h,3))
\]
for **all** nonnegative \(a,h\). This proves the field-independent *sufficiency* of the two clipped dimensions for the quantifier-rank-two type of \(X\).

**3. The pointed type also recovers the two clipped dimensions.** Define a strict order \(s<t\) to mean \(s\subseteq t\land s\ne t\). With \(x\) free, the following rank-at-most-two formulas express \(\dim x\ge1,2,3\), respectively:
\[
\exists y\,(y<x),\qquad
\exists y\,\exists z\,(z<y<x),
\]
\[
\exists y\,\bigl(y<x\ \land\ (\exists z\ z<y)\ \land\ (\exists z\ y<z<x)\bigr).
\]
The last formula requires a nonempty interval below \(y\) and a nonempty interval between \(y\) and \(x\), which is possible exactly when \(\dim x\ge3\). Reversing all inequalities gives the analogous tests for \(d-\dim x\ge1,2,3\). Thus the quantifier-rank-two type of \(X\) is **exactly** indexed by
\[
\bigl(\min(\dim X,3),\min(d-\dim X,3)\bigr).
\]

**4. The unpointed three-round classification.** At quantifier rank three, the theory of the entire lattice is determined by the **set** (not multiset) of rank-two types realized by its elements. By the preceding steps, that set is
\[
\Sigma_d=\{(\min(k,3),\min(d-k,3)):0\le k\le d\}.
\]
The sets \(\Sigma_0,\ldots,\Sigma_5\) are pairwise different. The first six include, respectively, the unique threshold pairs \((0,0)\), \((0,1)\), \((0,2)\), \((1,2)\), \((2,2)\), and \((2,3)\), which do not occur at smaller dimensions; direct evaluation of the formula makes the distinctions explicit. From \(d=6\) onward, \(\Sigma_d\) stabilizes to
\[
\{(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)\}.
\]
This proves the asserted equivalence criterion for all prime powers and all dimensions, including dimension zero.

**5. Sharp size.** Since dimensions zero through five remain distinct from dimension six, any universal representative set must include one lattice of dimension at least six. Its cardinality is at least that of the binary six-space subspace lattice:
\[
\sum_{k=0}^{6}{6\brack k}_2=1+63+651+1395+651+63+1=2825.
\]
The binary examples at dimensions zero through six represent every class, proving both the upper bound and sharpness.

## Verification
The accompanying Python program `verify_subspace.py` implements the nine witness conditions, verifies all finite coordinate-reduction identities on the exhaustive clipped parameter space, computes rank-three types through dimension 24, and separately reconstructs **actual subspace lattices** over fields of orders two, three and five. For each selected field and dimension, it enumerates all ordered-pair orbits by the triple of subspace ranks and intersection rank, and compares directly enumerated third-subspace witness patterns with the symbolic formulas. The recorded log is `verification_output.txt` and ends with `VERIFY_OK`. The computer checks corroborate the algebraic proof; the proof of all dimensions and prime powers is the preceding witness-construction and coordinate-reduction argument, not finite sampling.

## Relationship to prior work
Pikhurko and Verbitsky's 2010 survey explains logical depth and Ehrenfeucht games for finite graphs; it supplies the logical-comparison framework, but does not assert this result about non-distributive subspace lattices. Cusick (1998) studies the counting function of finite vector-space subspaces, rather than rank-bounded first-order theories. Yue (2014) studies the geometry and characteristic polynomials of subspace-derived lattices, rather than their bounded-rank theories. A previously recorded calculation for **Boolean** inclusion posets has the same dimension-six cutoff but applies to distributive subset lattices, not subspace lattices; its statement alone does not imply field independence or the present non-distributive result. The scope here is the pure inclusion-order reduct; richer lattice-operation and projective-incidence languages may distinguish more.

## Limitations
The theory neither classifies formulas with greater quantifier rank nor asserts independence of field order in such fragments. The optimal \(2825\) is relative to the finite subspace-lattice family. Published works not indexed or accessible to the present literature comparison may cover equivalent statements; no claim of independently certified originality is made.

## References
- Thomas W. Cusick, *Finite Vector Spaces and Certain Lattices*, Electronic Journal of Combinatorics 5 (1998), R17, DOI: 10.37236/1355 (first public publication date 1998-03-18).
- Oleg Pikhurko and Oleg Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865 (first posted 2010-03-25), especially §3 on Ehrenfeucht games.
- Mengtian Yue, *Lattices Associated with a Finite Vector Space*, Applied Mathematics 5 (2014), 672–676, DOI: 10.4236/am.2014.54064, especially §§1–3.
