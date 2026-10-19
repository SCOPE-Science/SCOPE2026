# Euler-transform enumeration of rank-three orbits of \(\operatorname{End}(\mathcal{T}_n)\)

## Finding
For every integer \(n\ge5\), the number \(r_3(n)\) of rank-three orbits in the semigroup endomorphism monoid of the full transformation monoid on \(n\) elements has the explicit ordinary generating function below. These rank-three orbits are precisely the essential rank-three orbits in the minimal-generator problem of Gould, Grau and Johnson [1].

\[
P(z)=\prod_{j\ge 1}(1-z^j)^{-1},\qquad
Q(z)=\prod_{j\ge 2}(1-z^j)^{-\lfloor j/2\rfloor},
\]
\[
B(z)=\frac{z}{1-z}P(z)Q(z),\qquad C(z)=\frac{z}{1-z}P(z).
\]
For any series \(U(z)=\sum_{j\ge1}u_jz^j\) with nonnegative integral coefficients, let
\[
\mathscr E(U)(z)=\prod_{j\ge1}(1-z^j)^{-u_j}.
\]
Then the ordinary generating function is
\[
\boxed{\sum_{n\ge0}r_3(n)z^n=\mathscr E(B)(z)-\mathscr E(C)(z).}
\]

In particular,
\[
(r_3(3),r_3(4),\ldots,r_3(13))=
(1,4,15,46,133,362,951,2419,6002,14591,34833).
\]
Although the generating function is defined for all nonnegative indices, the asserted identification with essential generator orbits is restricted to \(n\ge5\). The coefficients at smaller indices count the same compatible-pair orbits but are not claimed to constitute a minimal-generator contribution.

This also gives a finite divisor-sum recurrence: put \(b_j=[z^j]B(z)\), \(c_j=[z^j]C(z)\), and initialize \(F_0=G_0=1\). For every \(n\ge1\),
\[
 nF_n=\sum_{k=1}^{n}\left(\sum_{d\mid k}d b_d\right)F_{n-k},\qquad
 nG_n=\sum_{k=1}^{n}\left(\sum_{d\mid k}d c_d\right)G_{n-k},
\]
with \(r_3(n)=F_n-G_n\). Every coefficient involves finitely many factors and operations, so this is an exact effective answer to the rank-three part of the counting problem.

## Assumptions and scope
The symbol \(\mathcal T_n\) means all self-maps of \(\{1,\ldots,n\}\) with composition; \(\mathcal E_n=\operatorname{End}(\mathcal T_n)\) means *semigroup* endomorphisms, including those that do not fix the monoid identity. The rank of an endomorphism is its image cardinality, not the rank of an underlying point map. An orbit is the right orbit under the group \(\operatorname{Aut}(\mathcal T_n)\), isomorphic to the symmetric group.

The classification of Schein and Teclezghi, recorded as Theorem 2.1 in [1], identifies rank-three endomorphisms with pairs \((t,e)\) of self-maps satisfying
\[
t^3=t,\quad t e=e t=e^2=e,\quad t\ne t^2,
\]
where multiplication of maps is composition. Conjugating the pair simultaneously by a permutation agrees with right multiplication by an automorphism in \(\mathcal E_n\). For \(n=4\), there are exceptional additional endomorphisms of rank seven, which do not change this rank-three correspondence. Only the generator interpretation invokes \(n\ge5\).

## Proof
**Step 1: permitted components of \(t\).** From \(t^3=t\), every vertex is either fixed, belongs to a two-cycle, or is attached by one directed edge to a fixed vertex or a two-cycle vertex. No longer tail can occur: the image of \(t\) is acted upon by \(t\) as an involution. Thus every connected component of the functional graph of \(t\) is either a rooted star with a fixed root and some leaves, or a two-cycle with a set of incoming leaves at each endpoint. All component types are classified up to vertex relabeling.

**Step 2: what the commuting retraction \(e\) does.** Since \(e t=e\), the value of \(e\) is constant along every arrow of \(t\), and hence on each connected component of the functional graph of \(t\). Since \(t e=e\), every point of \(\operatorname{im}(e)\) is fixed by \(t\). Since \(e^2=e\), each such image point is fixed by \(e\) as well. Conversely, choosing for every functional-graph component of \(t\) one target among the fixed vertices of \(t\), and requiring that each chosen target maps to itself, produces exactly the permitted maps \(e\). These conditions are both necessary and sufficient.

**Step 3: the distinguished red blocks.** Group the components of \(t\) according to their common image under \(e\). Each group has exactly one distinguished rooted-star component: its root is the unique chosen \(e\)-fixed target. The group may contain an arbitrary multiset of further rooted stars and an arbitrary multiset of two-cycle components. Call this group a red block. The entire pair \((t,e)\), up to simultaneous permutation conjugacy, is uniquely an unordered multiset of red blocks. This is a bijection: the unique fixed root in each block reconstructs \(e\), and each blue component reconstructs \(t\).

**Step 4: local generating functions.** There is exactly one rooted-star type of size \(j\) for every \(j\ge1\); its ordinary generating function is \(z/(1-z)\). There are \(\lfloor j/2\rfloor\) two-cycle component types of total size \(j\ge2\): writing \(j-2=a+b\) for the numbers of attached leaves on the endpoints, the unordered pair \(\{a,b\}\) determines the type. Taking arbitrary multisets gives \(P\) for nondistinguished rooted stars and \(Q\) for two-cycle components. The single distinguished rooted star, together with these arbitrary multisets, gives one red block counted by \(B=(z/(1-z))P Q\). With two-cycles forbidden it is counted by \(C=(z/(1-z))P\).

**Step 5: outer multiset and rank-three condition.** The whole pair is an arbitrary multiset of red blocks. For a locally finite class with \(u_j\) block types of size \(j\), the multiset ordinary generating function is \(\prod_{j\ge1}(1-z^j)^{-u_j}\), proving that all compatible-pair conjugacy orbits are counted by \(\mathscr E(B)\), and those with no two-cycle by \(\mathscr E(C)\). Since \(t^3=t\), we have \(t\ne t^2\) exactly when at least one two-cycle exists. Subtracting therefore counts precisely rank-three orbits. Proposition 4.2 of [1] shows these are all essential for \(n\ge5\), proving the claimed application.

**Step 6: recurrence.** Logarithmically differentiating the formal Euler product yields
\[
 z\frac{d}{dz}\mathscr E(U)(z)
 =\mathscr E(U)(z)\sum_{k\ge1}\left(\sum_{d\mid k}d u_d\right)z^k.
\]
Comparing coefficients proves the stated recurrences; every use of differentiation is formal, so no analytic convergence assumption is needed.

## Verification
The accompanying standalone `CHECKER.py` contains two independently structured computations. One uses the symbolic multiset-product formulas and the other explicitly enumerates all self-maps \(t\) and idempotents \(e\) satisfying the displayed equations, then constructs conjugacy orbits using all permutations. Its exhaustive output at sizes \(n=1,2,3,4,5\) is as follows; the columns are the number of labeled compatible pairs, all orbits, and rank-three orbits:

| \(n\) | Pairs | All orbits | Rank-three orbits |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 0 |
| 2 | 5 | 3 | 0 |
| 3 | 34 | 8 | 1 |
| 4 | 297 | 21 | 4 |
| 5 | 3106 | 52 | 15 |

Running `python3 CHECKER.py` raises an assertion failure if the independent enumerations disagree; it prints formal-series coefficients through degree thirteen. The finite exhaustive checks test small boundary cases but are not a substitute for the all-size proof above.

## Relationship to prior work
Gould, Grau and Johnson [1], Section 4, determine the minimal-generator structure and identify the essential rank-three orbits. In Section 8 they explicitly propose deriving a recurrence or generating function for their number, \(r_3(n)\); no such formula is given there. The present result supplies that rank-three formula by separating two-cycle components in a nested multiset classification of the compatible pairs.

Grau's thesis [2], Chapter IV, develops the same endomorphism theory and discusses orbit descriptions as a remaining direction; it does not provide the rank-three orbit series. Krattenthaler and Müller [3], Theorem 4 and Corollary 5, enumerate *labeled* solutions of two commuting idempotent equations, unlike the nonidempotent allowed first map and simultaneous-conjugacy orbit invariant here. Their formulas therefore do not imply this answer merely by identifying the input transformation degree.

## Limitations
The finding does not evaluate the essential rank-two orbit count \(r_2(n)\), the complete minimal-generator cardinality \(3+r_3(n)+r_2(n)\), or asymptotic growth of that complete cardinality. No claim is made that this generating-function identity is analytically simple or that it resolves all counting questions about \(\mathcal E_n\). The proof depends on the published classification linking compatible pairs to rank-three endomorphisms; every new enumeration step is proved here. Related newer literature may remain unindexed.

## References
1. V. Gould, A. Grau, and M. Johnson, *The structure of End(T_n)*, arXiv:2307.11596v1 (first public 21 July 2023), Theorem 2.1, Proposition 4.2, Sections 4 and 8. https://arxiv.org/html/2307.11596v1
2. A. Grau, *Aspects of endomorphism monoids of certain algebras*, University of York PhD thesis (2023), Chapter IV and Section IV.9. https://etheses.whiterose.ac.uk/id/eprint/33804/1/GRAU-Aspects_of_endomorphism_monoids_of_certain_algebras.pdf
3. C. Krattenthaler and T. W. Müller, *Equations in finite semigroups: explicit enumeration and asymptotics of solution numbers*, arXiv:math/0303028v2 (2003), Theorem 4 and Corollary 5. https://arxiv.org/pdf/math/0303028
4. B. Schein and B. Teclezghi, *Endomorphisms of finite full transformation semigroups*, Proc. Amer. Math. Soc. 126 (1998), 2579–2587; classification quoted in [1, Theorem 2.1].
