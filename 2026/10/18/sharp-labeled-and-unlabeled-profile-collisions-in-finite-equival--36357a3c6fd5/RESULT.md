# Sharp labeled and unlabeled profile collisions in finite equivalence structures

## Finding

**Theorem (profile transform and first nondegenerate collisions).** Work in the parameter-free relational language with equality and one binary relation symbol \(E\). Let \(A\) be a nonempty finite equivalence structure of cardinality \(n\), with equivalence-class sizes \(\lambda=(\lambda_1\ge\cdots\ge\lambda_s>0)\). For \(r\ge1\), write \(b_r(A)\) for the number of distinct **labeled** equivalence relations on \([r]\) that occur as induced substructures on \(r\) distinct elements of \(A\); set \(b_0=1\) and \(b_r=0\) for \(r>n\). Write \(u_r(A)\) for the analogous count up to isomorphism, and \(T_k(A)\) for the number of realized complete parameter-free quantifier-free types of ordered \(k\)-tuples, where \(k\ge1\).

For every partition \(\mu=(\mu_1\ge\cdots\ge\mu_t>0)\vdash r\), let \(m_j(\mu)\) be the multiplicity of part \(j\), and call \(\mu\) **admissible** when \(t\le s\) and \(\mu_i\le\lambda_i\) for all \(1\le i\le t\). Then

\[
 b_r(A)=\sum_{\substack{\mu\vdash r\\\mu\text{ admissible}}}
 \frac{r!}{\prod_i\mu_i!\prod_{j\ge1}m_j(\mu)!},\qquad
 u_r(A)=\#\{\mu\vdash r:\mu\text{ admissible}\},
\]

and the complete tuple-type and definable-relation spectra are

\[
 \boxed{T_k(A)=\sum_{r=1}^{\min(k,n)}\left\{\begin{matrix}k\\r\end{matrix}\right\}b_r(A),
 \qquad D_k(A)=2^{T_k(A)}.}
\]

Here \(\left\{\begin{smallmatrix}k\\r\end{smallmatrix}\right\}\) denotes a Stirling number of the second kind, and \(D_k\) is the number of parameter-free quantifier-free definable \(k\)-ary relations. The full sequence \((T_k)_{k\ge1}\) recovers \(n\) and every labeled coefficient \(b_r\):

\[
 \boxed{n=\lim_{k\to\infty}T_k(A)^{1/k}.}
\]

For a fixed \(n\), the first \(n\) values of \(T_k\) suffice to recover all \(b_r\) by triangular inversion. Nevertheless, these numerical invariants do not determine \(A\) up to isomorphism.

In fact, restrict attention to **nondegenerate** equivalence relations, meaning neither equality nor the total relation. The smallest cardinality at which two nonisomorphic structures have the same entire tuple-type spectrum is \(n=5\). At this cardinality there is exactly one nondegenerate collision pair, with class-size partitions

\[
 \boxed{\lambda=(3,2),\qquad \lambda'=(2,1,1,1).}
\]

For both structures, \((b_1,b_2,b_3,b_4,b_5)=(1,2,4,7,10)\), and hence for every \(k\ge1\)

\[
 \boxed{T_k=\left\{\begin{matrix}k\\1\end{matrix}\right\}
 +2\left\{\begin{matrix}k\\2\end{matrix}\right\}
 +4\left\{\begin{matrix}k\\3\end{matrix}\right\}
 +7\left\{\begin{matrix}k\\4\end{matrix}\right\}
 +10\left\{\begin{matrix}k\\5\end{matrix}\right\}.}
\]

The **unlabeled** induced-substructure profile loses information one element earlier: its smallest nondegenerate collision occurs at \(n=4\), already for \((3,1)\) versus \((2,1,1)\). Thus the labeled invariant is strictly more discriminating at the first possible collision boundary, but is still not reconstructive. In the five-element pair, one structure has an equivalence class of size three and the other does not, so even first-order equivalence fails.

## Assumptions and scope

The language has exactly one named binary equivalence predicate \(E\) and built-in logical equality; there are no constants, unary class names, parameters, or extra relation symbols. Every finite structure under discussion is nonempty. In particular, a class-size partition specifies the whole structure up to isomorphism. "Labeled" always means an equivalence relation on the *fixed* coordinate set \([r]\), not a labeled copy of the entire ambient structure. Quantifier-free types identify two tuples exactly when they satisfy the same atoms \(x_i=x_j\) and \(E(x_i,x_j)\). Only the **numbers** of types and definable relations are compared, not their formulas or their actual sets of signatures. The general formulas hold for all \(n,r,k\) in the stated ranges; the minimal collision classification concerns cardinalities at most five.

## Proof

**1. Admissibility.** An equivalence relation on \([r]\) has blocks of sizes \(\mu_1\ge\cdots\ge\mu_t\). It embeds as an induced relation on distinct points of \(A\) exactly when its \(t\) distinct blocks can be placed into \(t\) distinct ambient \(E\)-classes, respecting their capacities. Necessity of \(\mu_i\le\lambda_i\) follows by sorting the demanded and available sizes decreasingly: if the \(i\)-th demand exceeded the \(i\)-th largest capacity, there would be too few capacities large enough for the first \(i\) demands. Sufficiency is immediate by assigning the \(i\)-th largest demand to the \(i\)-th largest ambient class. Thus admissibility is exact.

For a fixed admissible block-size multiset \(\mu\), the number of set partitions of the *labeled* coordinate set \([r]\) with those sizes is \(r!/(\prod_i\mu_i!\prod_jm_j(\mu)!)\): divide by permutations within blocks and by permutations of equal-sized blocks. Summing gives \(b_r\); forgetting labels gives \(u_r\).

**2. All tuple types and definable relations.** An ordered \(k\)-tuple induces an equality partition of its coordinate set into \(r\) nonempty blocks, with \(1\le r\le\min(k,n)\). Number the blocks by their least coordinates. There are \(\left\{\begin{smallmatrix}k\\r\end{smallmatrix}\right\}\) equality partitions, and for each there are exactly \(b_r\) admissible \(E\)-patterns on its \(r\) distinct values. These two pieces uniquely specify the full atomic diagram and are freely combinable. This proves the Stirling-transform formula.

Each realized atomic diagram is defined by a conjunction of the relevant positive and negated equality and \(E\) atoms. Distinct diagrams are disjoint, and every union of them is defined by a finite disjunction. Hence there are exactly \(2^{T_k}\) definable \(k\)-ary relations, including empty and full relations.

The Stirling matrix \(\bigl(\left\{\begin{smallmatrix}k\\r\end{smallmatrix}\right\}\bigr)_{1\le r\le k\le n}\) is triangular with diagonal entries one, so \(T_1,\ldots,T_n\) determine \(b_1,\ldots,b_n\). Moreover \(b_n>0\), and for fixed \(n\), \(\left\{\begin{smallmatrix}k\\n\end{smallmatrix}\right\}\sim n^k/n!\), while terms with \(r<n\) are \(O((n-1)^k)\). Therefore \(T_k\sim (b_n/n!)n^k\) and its \(k\)-th root tends to \(n\). This also excludes cross-cardinality collisions of the complete numerical spectrum.

**3. The five-element collision.** Let \(A\) have class sizes \((3,2)\) and \(B\) have \((2,1,1,1)\). Enumerating admissible labeled partitions at each \(r\le5\) gives:

| \(r\) | Patterns in \(A\) | Patterns in \(B\) | Both \(b_r\) |
|---|---|---|---:|
| 1 | \((1)\) | \((1)\) | 1 |
| 2 | \((2),(1,1)\) | \((2),(1,1)\) | 2 |
| 3 | \((3),(2,1)\) | \((2,1),(1,1,1)\) | 4 |
| 4 | \((3,1),(2,2)\) | \((2,1,1),(1,1,1,1)\) | 7 |
| 5 | \((3,2)\) | \((2,1,1,1)\) | 10 |

For example, at \(r=4\), the first structure contributes \(4+3=7\) labeled relations while the second contributes \(6+1=7\). Therefore the five coefficients, and by Step 2 all quantifier-free type counts, coincide. Their class-size multisets differ, so they are not isomorphic. The first-order sentence asserting the existence of three pairwise distinct mutually \(E\)-related points holds in \(A\) and fails in \(B\).

**4. Minimality and uniqueness at five points.** Structures of a fixed cardinality \(n\) correspond to the integer partitions of \(n\). For \(n\le3\) there is at most one nondegenerate class-size partition. For \(n=4\) the nondegenerate profiles \((b_1,b_2,b_3,b_4)\) are:

| Class sizes | Labeled profile |
|---|---|
| \((3,1)\) | \((1,2,4,4)\) |
| \((2,2)\) | \((1,2,3,3)\) |
| \((2,1,1)\) | \((1,2,4,6)\) |

They are pairwise distinct. For \(n=5\), the five nondegenerate types and profiles are:

| Class sizes | Labeled profile |
|---|---|
| \((4,1)\) | \((1,2,4,5,5)\) |
| \((3,2)\) | \((1,2,4,7,10)\) |
| \((3,1,1)\) | \((1,2,5,10,10)\) |
| \((2,2,1)\) | \((1,2,4,9,15)\) |
| \((2,1,1,1)\) | \((1,2,4,7,10)\) |

The displayed pair is thus the unique nondegenerate collision through five points. Step 2 converts profile agreement to all-arity type-count agreement. Finally, for the unlabeled age profiles at \(n=4\), both \((3,1)\) and \((2,1,1)\) have \((u_1,u_2,u_3,u_4)=(1,2,2,1)\): the admissible types at \(r=3\) are respectively \((3),(2,1)\) and \((2,1),(1,1,1)\). Since there is only one nondegenerate partition at each cardinality at most three, this unlabeled collision is also minimal. This proves all claims.

## Verification

The companion `verify.py` uses two independent computations. It directly enumerates atomic signatures of injective tuples and arbitrary tuples from all 44 class-size partitions of universes of sizes one through seven; separately, it calculates the predicted profiles using integer partitions, factorial weights, capacity matching, and Stirling recurrence. It also directly checks the stated five-point collision through arity seven and the complete nondegenerate minimality classification through size five. Running `python3 verify.py` produced:

`VERIFY_OK partitions_tested=44 injective_profile_checks=240 direct_tuple_assignments=626590 first_nondegenerate_labeled_collision=n5 first_nondegenerate_unlabeled_collision=n4 n5_injective_profile=(1, 2, 4, 7, 10)`

The finite tests are independent consistency checks; the unbounded all-arity claim is proved in Steps 1–3.

## Relationship to prior work

Areces, Campercholi, Penazzi, and Ventura (2019) provide the general theory of open (quantifier-free) definability in finite relational structures and identify its characterization by partial isomorphisms. Campercholi, Tellechea, and Ventura (2023) treat tuple types and quantifier-free definability algorithms for algebraic, rather than purely relational, signatures. Pouzet and Thiéry develop the different, unlabeled age-profile invariant and its algebraic framework. These are established foundations; the general Stirling transform itself is elementary and is not presented as a new general principle.

The assessed distinct contribution is the sharp **nondegenerate** collision threshold for the fully labeled, all-arity quantifier-free definability count in the simplest equivalence-relation language, contrasted with the earlier unlabeled age-profile threshold. The historical general-profile results do not state these five-element class-size collisions or their exact minimality classification in the inspected material. The theorem concerns neither probability on random equivalence relations nor tuple-orbit counts of a fixed global automorphism group: quantifier-free diagrams are determined by local, induced structures.

## Limitations

The theorem concerns numeric profiles only. The two five-element structures do **not** have the same actual quantifier-free types, and they are not first-order equivalent. Degenerate equality and universal equivalence relations already give trivial numeric collisions for every cardinality at least two; their exclusion is essential for the sharp five-point statement. Nothing is claimed about uniqueness of nondegenerate collisions for cardinalities above five, or about numerical profiles in richer languages. Novelty is assessed from accessible primary literature and indexed records, not an exhaustive proof of publication priority. No independent external audit has been carried out.

## References

1. C. Areces, M. Campercholi, D. Penazzi, P. Ventura, *The Complexity of Definability by Open First-Order Formulas* (initial arXiv version April 9, 2019), arXiv:1904.04637, https://arxiv.org/abs/1904.04637.
2. M. Campercholi, M. Tellechea, P. Ventura, *Two algorithms to decide Quantifier-free Definability in Finite Algebraic Structures* (initial arXiv version March 29, 2023), arXiv:2303.17017, https://arxiv.org/abs/2303.17017.
3. M. Pouzet, N. M. Thiéry, *Some relational structures with polynomial growth and their associated algebras II: Finite generation* (initial arXiv version January 29, 2008), arXiv:0801.4404, https://arxiv.org/abs/0801.4404. Background on the distinct unlabeled age profile.
