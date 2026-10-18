# Stirling–Gaussian enumeration of counting types for commuting involutions

## Finding

Let \(k\ge1\), and consider finite structures \(X\) with \(k\) *named binary relations* \(R_1,\ldots,R_k\). Assume that each \(R_i\) is the graph of a total involutive permutation \(s_i:X\to X\), and that the permutations commute pairwise. Fixed points and repeated permutations are allowed. Isomorphisms must preserve every relation name. Write \(\mathsf C^2\) for first-order logic with counting quantifiers and at most two variable symbols, over this relational language; the generating permutations are **not** function symbols.

Put \(G=\mathbb F_2^k\), with basis \(e_1,\ldots,e_k\), and set \(e_0=0\). Every transitive component of \(X\) is uniquely of the form \(G/H\) for a subgroup \(H\le G\). Define the partition \(\tau_H\) of \(\{0,1,\ldots,k\}\) by
\[
 i\sim_{\tau_H}j\quad\Longleftrightarrow\quad e_i+e_j\in H.
\]
Let \(m_H\) be the number of \(G/H\) components in \(X\), and for every set partition \(\tau\) put
\[
 N_\tau(X)=\sum_{H:\,\tau_H=\tau}m_H\,2^k/|H|.
\]
The background two-variable counting criterion specializes to: **two structures in this class satisfy precisely the same \(\mathsf C^2\) sentences if and only if their entire vectors \((N_\tau)_\tau\) agree**. This criterion is proved below for completeness; the enumerative products and sharp obstruction are the new conclusions.

Let \(I_k(n)\) count isomorphism types of size \(n\), and \(C_k(n)\) count \(\mathsf C^2\)-equivalence classes of structures of size \(n\) *within this class*. With \(\left[{k\atop d}\right]_2\) denoting the number of codimension-\(d\) subspaces of \(\mathbb F_2^k\) and \(\left\{{k+1\atop r+1}\right\}\) a Stirling number of the second kind, their ordinary generating functions are
\[
 \sum_{n\ge0}I_k(n)z^n
 =\prod_{d=0}^k(1-z^{2^d})^{-\left[{k\atop d}\right]_2},
\]
\[
 \boxed{\displaystyle
 \sum_{n\ge0}C_k(n)z^n
 =\prod_{r=0}^k
 (1-z^{2^{\lceil\log_2(r+1)\rceil}})^{-\left\{{k+1\atop r+1}\right\}}.}
\]
The empty structure is included as the constant term in both series.

For \(k\le2\), \(\mathsf C^2\)-equivalence within this class implies isomorphism at every size. For \(k\ge3\), this is true for sizes at most seven and false at size eight. For \(k=3\), **exactly one unordered pair** of nonisomorphic eight-element structures is \(\mathsf C^2\)-equivalent. Explicitly, it is a single three-dimensional Boolean cube with its three coordinate-flip relations versus the disjoint union of two four-element orbits where the third flip is the composite of the first two. For \(k=3\),
\[
 \sum_{n\ge0}I_3(n)z^n
 =\frac1{(1-z)(1-z^2)^7(1-z^4)^7(1-z^8)},
 \qquad
 \sum_{n\ge0}C_3(n)z^n
 =\frac1{(1-z)(1-z^2)^7(1-z^4)^7}.
\]
Thus \(I_3(8)=611\) and \(C_3(8)=610\), with equality of the two counts for sizes at most seven.

## Assumptions and scope

All structures are finite, with unrestricted cardinality and unrestricted nonfaithfulness of the \(G\)-action. Relations are **binary graphs of permutations**, not unary function symbols. The stated logical-equivalence result is *relative to the displayed commuting-involution class*; no claim is made about identification against arbitrary relational structures. The exact labels \(1,\ldots,k\) are part of the signature and cannot be permuted by isomorphisms. An orbit \(G/H\) uses left translation by each \(e_i\). We allow empty structures only to provide the constant coefficients of the generating functions.

The Gaussian coefficient can be computed as
\[
 \left[{k\atop d}\right]_2
 =\prod_{j=0}^{d-1}\frac{2^{k-j}-1}{2^{d-j}-1}
 \quad(0\le d\le k),
\]
and \(\left\{{a\atop b}\right\}\) counts partitions of an \(a\)-element set into \(b\) nonempty blocks.

## Proof

**1. Group-action normal form.** The pairwise commuting involutions give a unique \(G\)-action via the prescribed basis elements. Every orbit is transitive and hence isomorphic, with generator names retained, to \(G/H\), where \(H\) is its point stabilizer. Since \(G\) is abelian, all stabilizers in an orbit coincide. Moreover \(G/H\cong G/K\) as named \(G\)-sets only when \(H=K\). Therefore the multiplicities \(m_H\) are a complete isomorphism invariant and an orbit contributes \(2^k/|H|\) vertices.

**2. The background two-variable invariant (derived here for completeness).** At a vertex \(x\), write \(a_0(x)=x\) and \(a_i(x)=s_i(x)\). The partition of \(\{0,\ldots,k\}\) induced by equality among these \(k+1\) vertices is exactly \(\tau_H\) on the orbit \(G/H\). Each assertion \(a_i(x)=a_j(x)\) is expressible with the two variable symbols: when \(i,j>0\), use \(\exists y\,(R_i(x,y)\wedge R_j(x,y))\), and when one index is zero use \(R_i(x,x)\). Thus \(\tau_H\) is definable by a unary \(\mathsf C^2\) formula, and the exact counts \(N_\tau\) can be asserted by counting quantifiers. Equality of all \(N_\tau\) is therefore necessary for \(\mathsf C^2\)-equivalence.

For sufficiency, fix any vertex \(x\). The complete atomic two-variable type of a pair \((x,y)\) consists of equality \(x=y\), the diagonal relation facts at \(x,y\), and the set of \(i\) for which \(R_i(x,y)\) (equivalently \(R_i(y,x)\)). In the special structures considered here, each nonempty such set arises from a unique nonzero block of \(\tau(x)\) (or the zero block when \(x=y\)), and its occurrence has multiplicity exactly one. Every such \(y\) lies in the same orbit and has the same signature as \(x\), since all generators commute. All remaining vertices of signature \(\sigma\) are unrelated to \(x\) by every \(R_i\), in a quantity determined by \(N_\sigma\) and the foregoing finitely many neighbor types. Hence, conditional on \(\tau(x)\), the number of choices of \(y\) having each possible signature and atomic pair type depends only on the numbers \(N_\sigma\), not on the chosen vertex. Induction on formulas, with quantified variables alternating between the only two available symbols and with arbitrary numerical counting thresholds, shows that their truth at free vertices or pairs depends only on these signatures and atomic pair types. In particular two structures with the same \(N_\sigma\) satisfy exactly the same \(\mathsf C^2\) sentences.

**3. All possible signatures and their minimum component sizes.** A signature is exactly a set partition of \(\{0,1,\ldots,k\}\): partition its indices by equality of the images of \(e_i\), with the block containing zero representing the identity element. Conversely, for any such partition with \(r\) blocks not containing zero, assign distinct nonzero vectors to these \(r\) blocks in \(\mathbb F_2^d\), where \(d=\lceil\log_2(r+1)\rceil\). They can be chosen to span \(\mathbb F_2^d\), because \(r\ge d\) for \(r\ge1\); use \(d\) basis vectors among the assigned images and then any remaining distinct nonzero vectors. Sending \(e_i\) to the corresponding image gives a surjective homomorphism \(G\to\mathbb F_2^d\). Its kernel realizes the chosen signature with orbit size \(2^d\). No quotient having that signature can have fewer than \(r+1\) distinct elements and, because its order is a power of two, no smaller orbit size than \(2^d\). Every other orbit with that signature has size a multiple of \(2^d\), and repetitions of a minimum-size orbit realize **every** nonnegative multiple of \(2^d\) as the signature's vertex count. There are \(\left\{{k+1\atop r+1}\right\}\) signatures with exactly \(r\) nonzero blocks.

**4. Generating functions.** Since each subgroup \(H\) specifies an independent nonnegative component multiplicity, multiplying geometric series over subgroups and sorting by codimension yields the first formula. By Step 2, logical classes are determined by one independent integer \(N_\tau\) for every signature. By Step 3, each such integer ranges over all nonnegative multiples of \(2^{\lceil\log_2(r+1)\rceil}\). Their product of geometric series gives the second formula, including both the stated exponents and the exact treatment of empty structures.

**5. The sharp threshold.** When the quotient \(G/H\) has order at most four, it is a vector space of dimension at most two. Its labelled generating images \(e_i+H\) are determined up to a single invertible linear change of coordinates solely by which are zero and which coincide: a two-dimensional space has exactly three nonzero vectors, and any two distinct such vectors form a basis, with the third their sum. Thus among index-at-most-four subgroups, \(H\mapsto\tau_H\) is injective. Every orbit in a structure of size at most seven has size at most four, so Step 2 distinguishes every isomorphism type. For \(k\le2\), every subgroup has index at most four, giving identification at *all* sizes.

For \(k=3\), the sixteen subgroups have indices \(1,2,4,8\) in multiplicities \(1,7,7,1\). A direct application of the same argument shows the only signature shared by distinct subgroups is the partition consisting of four singleton blocks. It is realized by the trivial subgroup, giving an eight-point orbit, and by \(\langle e_1+e_2+e_3\rangle\), giving a four-point orbit. Therefore the unique possible difference at size eight replaces one eight-point orbit by two of these four-point orbits. No other types of size eight can differ while keeping their \(N_\tau\) equal. For \(k>3\), extend this pair by letting all extra named generators act identically. It remains nonisomorphic and \(\mathsf C^2\)-equivalent. The two alternatives are separated already by the three-variable sentence
\[
 \exists x\,\exists y\,\exists z\,
 \bigl(R_1(x,y)\wedge R_2(y,z)\wedge R_3(z,x)\bigr):
\]
it holds on the two four-point orbits because the three nontrivial translations sum to zero, but not on the eight-point cube, where they are independent.

## Verification

The standalone scripts `verify_subgroups.py`, `verify_series.py`, and `verify_witness.py` use only the Python standard library. Run each from a directory containing all three scripts, with `python3 verify_subgroups.py`, `python3 verify_series.py`, and `python3 verify_witness.py`. Their corresponding `.out` files contain complete outputs from successful executions.

`verify_subgroups.py` explicitly enumerates all subspaces and all orbit-multisets for one and two generators through twelve points, and three generators through eight points; it also verifies injectivity of the local signatures among rank-at-most-two quotients through six generators. `verify_series.py` independently compares subgroup index multiplicities with Gaussian coefficients, minimum signature orbit sizes with Stirling counts through four generators, and both generating-function coefficients against direct orbit-multiset enumeration through eight points for one, two, and three generators. `verify_witness.py` checks actual permutation actions, pairwise commutativity, the local atomic color-refinement fingerprint, orbit decomposition, and the separating three-variable formula on the eight-point witnesses, including extra identity generators.

These are **finite corroborations**, not proofs of the universal statements; the proofs are Steps 1–5 above.

## Relationship to prior work

Cai, Fürer and Immerman introduced a central counting-logic/Weisfeiler–Leman connection. Kopczyński and Tan analyzed \(\mathsf C^2\) models through regular and biregular colored graphs and proved semilinearity of spectra. Kiefer, Schweitzer and Selman developed a classification of graphs and finite relational structures identified by counting logic, including colored matching examples. These are relevant, stronger *general frameworks* for logical indistinguishability and identification, but the inspected results do not give the precise subgroup-signature parameterization for commuting-involution relational structures, the two closed enumeration series, or the unique eight-point collision for three named involutions. The subgroup normal form itself is classical, and the equality-signature criterion is a special case of the more general two-variable criterion for relationally presented commuting permutations. Neither is claimed here as an original stand-alone theorem. The new mathematical content is the exact Stirling/Gaussian type enumeration and sharp unique minimal collision.

## Limitations

Originality is assessed against the inspected primary texts and searches, not certified against all specialist work. A treatment of commuting involutions via named *functions*, a logic with three or more variables, or arbitrary noncommuting bijections has different expressive power or a different class of structures. The named-relations hypothesis and relative-isomorphism testing scope cannot be dropped. The verification programs cover finite parameter ranges only. No independent scientific audit or priority determination has been performed.

## References

1. J. Cai, M. Fürer and N. Immerman, *An Optimal Lower Bound on the Number of Variables for Graph Identification*, Combinatorica **12** (1992), 389–410. Available primary paper: https://people.cs.umass.edu/~immerman/pub/opt.pdf .
2. E. Kopczyński and T. Tan, *Regular graphs and the spectra of two-variable logic with counting*, arXiv:1304.0829, first publicly posted 2013-04-03. https://arxiv.org/abs/1304.0829 .
3. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30. https://arxiv.org/abs/1503.08792 .
