# A seven-round plateau for binary additive groups in the ternary relational language

## Finding

For each integer \(d\ge1\), let \(V_d\) be the finite relational structure whose universe is \(\mathbb F_2^d\), with equality and one ternary predicate \(R\), interpreted by \(R(a,b,c)\) exactly when \(a+b=c\). The language has **no addition function, constant naming zero, or scalar operations**. Write \(V_d\equiv_q V_e\) when the structures satisfy the same first-order sentences of quantifier rank at most \(q\).

**Theorem.** At **both** quantifier ranks \(q=6\) and \(q=7\),
\[
 V_d\equiv_q V_e\quad\Longleftrightarrow\quad
 \min\{d,5\}=\min\{e,5\}.
\]
Thus exactly five theories occur, represented by dimensions \(1,2,3,4,5\). The sharp largest smallest representative has \(2^5=32\) elements. In particular, passing from rank six to rank seven creates *no new classes*, even though rank five has only four. The complete filtration through rank seven is:

| Quantifier rank | Equivalence classes by dimension | Number of classes |
|---|---|---:|
| \(1\) | all dimensions | 1 |
| \(2\) | \(\{1\},\{d\ge2\}\) | 2 |
| \(3\) or \(4\) | \(\{1\},\{2\},\{d\ge3\}\) | 3 |
| \(5\) | \(\{1\},\{2\},\{3\},\{d\ge4\}\) | 4 |
| \(6\) or \(7\) | \(\{1\},\{2\},\{3\},\{4\},\{d\ge5\}\) | 5 |

## Assumptions and scope

Quantifier rank is *maximum quantifier nesting*, with unrestricted Boolean combinations and reuse of variable symbols. Repeated choices are allowed. The structures are the full finite binary vector spaces, not their nonzero subsets, and the only nonlogical predicate is the three-place addition graph. The theorem covers all positive dimensions and all quantifier ranks from one through seven. It does not assert a formula for higher quantifier ranks or for other primes. The equality-only and functional-addition languages have different depth resources; the theorem refers exclusively to this relational language.

## Proof

**1. Ordered-tuple orbits.** For an ordered \(t\)-tuple \((v_1,\ldots,v_t)\) in \(V_d\), form the \(d\)-by-\(t\) coordinate matrix and let \(U\le\mathbb F_2^t\) be its row space. This is independent of the basis of \(V_d\). Two ordered tuples are in the same \(\mathrm{GL}(d,2)\)-orbit if and only if their row spaces agree: equality of row spaces gives equality of kernels of the maps \(\mathbb F_2^t\to\mathbb F_2^d\), and the resulting isomorphism of image subspaces extends to an automorphism of the whole space. Only subspaces \(U\) of dimension at most \(d\) occur.

**2. Atomic diagrams.** The atomic equality \(v_i=v_j\) holds precisely when every \(u\in U\) has \(u_i=u_j\). Likewise \(R(v_i,v_j,v_k)\) holds precisely when every \(u\in U\) has \(u_i+u_j=u_k\). Thus the entire ordered atomic diagram \(\operatorname{At}_t(U)\) is computed exactly from \(U\), including repeated indices and zero-valued tuple entries.

**3. All one-point extensions.** Write \(r=\dim U\). For a new vector within the span of \(v_1,\ldots,v_t\), the extended row space is the graph
\[
 W_\lambda=\{(u,\lambda(u)):u\in U\},
 \quad\lambda\in\operatorname{Hom}_{\mathbb F_2}(U,\mathbb F_2).
\]
Every such linear functional occurs, giving \(2^r\) distinct graph extensions. A new vector outside that span exists if and only if \(r<d\), and its extended row space is \(U\times\mathbb F_2\). These are **all** extension types: projection of the new row space onto the first \(t\) coordinates has image \(U\) and its kernel is either zero or the entire one-dimensional last-coordinate space.

**4. Exact finite recursion.** Define \(H_0(d,U)=\operatorname{At}_t(U)\) and, recursively,
\[
 H_{s+1}(d,U)=\left(\operatorname{At}_t(U),
 \{H_s(d,W):W\in\operatorname{Ext}_d(U)\}\right).
\]
Here \(U\le\mathbb F_2^t\) and \(W\le\mathbb F_2^{t+1}\) ranges through precisely the extensions in step 3. By induction on \(s\), this is the complete first-order \(s\)-type of the tuple: negation and Boolean combinations are determined by the present type, and one additional existential quantifier is determined by the **set** of realizable child types. Consequently equality of the root types \(H_q(d,\{0\})\) is equivalent to \(q\)-round Ehrenfeucht–Fraïssé equivalence.

The standalone `verify_types.py` implements the recurrence using row-reduced bases as canonical bit tuples and exact Python integers. Its subspace counts for ambient dimensions \(t=0,1,\ldots,7\) are respectively \(1,2,5,16,67,374,2825,29212\), with every subspace obtained from the two extension cases above. It performs the exhaustive recursion for each \(q=1,\ldots,7\) and dimensions \(d=1,\ldots,q+1\). The returned root-type identifiers (only equality of identifiers matters) are:

```
q=1: [1,1]
q=2: [1,2,2]
q=3: [1,2,3,3]
q=4: [1,2,3,3,3]
q=5: [1,2,3,4,4,4]
q=6: [1,2,3,4,5,5,5]
q=7: [1,2,3,4,5,5,5,5]
```

These are exact finite checks of the mathematically proved orbit/extension recurrence, not a sample of random vectors. A separate explicit-element recursion (`verify_direct.py`) independently obtains the same root partitions for dimensions one through three and ranks one through four.

**5. No omitted dimensions.** For any rank \(q\), a game has at most \(q-1\) selected elements before its last move. If \(d\ge q\), every such tuple has span dimension below \(d\), so the independent extension is always available. Hence all dimensions \(d\ge q\) have the same root \(q\)-type. In the finite rank-seven recursion dimensions five, six, and seven have equal root types; combining this equality with the general stabilization for dimensions at least seven gives one common class for **every** \(d\ge5\). The same argument applies at rank six. Distinct computed root types for dimensions one through four supply the converse, by the finite Hintikka-type/EF theorem.

The size bound is sharp within this family: the dimension-five class has no equivalent member of lower dimension at rank six or seven, and \(|V_5|=32\).

## Verification

Run `python3 verify_types.py` (Python standard library only); the output is contained in `verify_types.out` and ends in `EXACT_ORBIT_RECURRENCE_OK`. Run `python3 verify_direct.py`; its independently constructed type recursion ends in `DIRECT_VERIFY_OK`. Both were executed against these included source files. The first program enumerates all subspaces of \(\mathbb F_2^t\) for \(t\le7\), rather than all tuples of vectors from each large structure; steps 1–3 prove this reduction exhaustive. Each rank/dimension partition is asserted in code; a mismatch raises an exception.

## Relationship to prior work

Gomaa's *Model Theory and Complexity Theory* (2007, Chapter 3, especially Section 3.7) gives general logical-depth bounds for distinguishing finite abelian groups, using addition as a ternary relation in Ehrenfeucht games. Those coarse bounds do not specify the five exact rank-six/rank-seven types or the rank-seven plateau. Gomaa's subsequent 2010 paper gives the corresponding general descriptive-complexity results. Bova and Martin (2015, Sections 2 and 4) prove an efficient parameterized algorithm for first-order model checking on finite abelian groups in the **functional** signature \(\{+,-,0\}\), which does not state the exact bounded-rank partition in the weaker ternary language. Related results about vector spaces over algebraically closed fields likewise have a different field and signature. An earlier low-rank enumeration for elementary abelian groups determines the rank-three classes but does not imply the rank-five-through-seven cases. A historical-priority risk remains for implicit treatments of this special binary family.

## Limitations

The theorem is a bounded-depth classification only through quantifier rank seven; it does not predict rank eight or all-rank behavior. The proof uses an executable exact finite recurrence for the final finite list of root types; the recurrence itself is independently derived in steps 1–4, but its finite table has not received external mathematical validation. No claim of independent audit or historical-priority exhaustiveness is made.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, doctoral thesis, University of Maryland, publicly available 2007-07-06, Chapter 3. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116. https://doi.org/10.1142/S0218196710006047
3. S. Bova and B. Martin, *First-Order Queries on Finite Abelian Groups*, CSL 2015, 41–59. https://doi.org/10.4230/LIPIcs.CSL.2015.41
