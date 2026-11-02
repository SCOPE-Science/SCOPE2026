# A half-turn invariant simplex-boundary core in honeycomb perfect-matching complexes

## Finding
For every integer \(n\ge 2\), let \(H=H_{1\times2\times n}\) be the finite hexagonal honeycomb graph with opposite sides of lengths \(1,2,n\). Let \(K_n=\mathcal M_p(H)\) be its perfect-matching complex: a simplex is a set of graph edges contained in at least one perfect matching. In the standard edge labelling, put
\[
x=d_{0,0},\qquad y=d_{2,n},\qquad z_j=d_{1,j}\quad(1\le j<n).
\]
Then the **induced** subcomplex on \(\{x,y,z_1,\ldots,z_{n-1}\}\) is the boundary \(L_n=\partial\Delta^n\) of an \(n\)-simplex, and \(K_n\) simplicially collapses onto \(L_n\). The geometric half-turn \(\rho\) preserves \(L_n\), interchanging \(x,y\) and reversing the order of the \(z_j\). Consequently its action on the sole nonzero reduced integral homology group is
\[
\rho_*\bigm|_{\widetilde H_{n-1}(K_n;\mathbb Z)}=(-1)^{n(n+1)/2}\operatorname{id}_{\mathbb Z}.
\]
In particular, for the quotient by the half-turn, \(\widetilde H_*(K_n/\langle\rho\rangle;\mathbb Q)\) is \(\mathbb Q\) in degree \(n-1\) when \(n\equiv0,3\pmod4\), and vanishes in every degree when \(n\equiv1,2\pmod4\).

## Assumptions and scope
All graphs and simplicial complexes are finite. The notation \(H_{1\times2\times n}\), its edge labels \(a_{i,j},b_{i,j},d_{i,j}\), and the plane-partition correspondence are those of Bayer, Jelić Milutinović and Vega [1], Proposition 10. Each perfect matching is represented by an integer pair \((p,q)\) with \(n\ge p\ge q\ge0\). The relevant incidence rules are: \(x\) occurs except in \((0,0)\), \(y\) occurs except in \((n,n)\), and
\[
z_j\in(p,q)\quad\Longleftrightarrow\quad j>p\ \text{or}\ j<q.
\]
The full edge rules, also used for the finite checker, are as follows: \(a_{i,j}\) occurs when \(j=h_i\); \(b_{0,j}\) when \(j>h_1\), \(b_{1,j}\) when \(h_1\ge j>h_2\), and \(b_{2,j}\) when \(j\le h_2\); \(d_{0,j}\) when \(j<h_1\), \(d_{1,j}\) when \(j>h_1\) or \(j<h_2\), and \(d_{2,j}\) when \(j>h_2\), omitting nonexistent boundary edges. Here \(h_1=p,h_2=q\); indices obey their geometric ranges.

The half-turn is the geometric \(180^\circ\) rotation, acting on named graph edges by
\[
\rho(a_{i,j})=a_{3-i,n-j},\quad \rho(b_{i,j})=b_{2-i,n+1-j},\quad \rho(d_{i,j})=d_{2-i,n-j}.
\]
It maps the perfect matching \((p,q)\) to \((n-q,n-p)\), so acts simplicially on \(K_n\).

## Proof
**1. The embedded core is exactly a simplex boundary.** The two extreme perfect matchings \((0,0)\) and \((n,n)\) contain every \(z_j\) and, respectively, \(y\) and \(x\). For every \(1\le j<n\), matching \((j,j)\) contains \(x,y\) and every \(z_k\) except \(z_j\). Thus every proper subset of the \(n+1\) specified vertices is a simplex. For a nonextreme pair \((p,q)\), the integer interval \([q,p]\) contains a \(j\in\{1,\ldots,n-1\}\), so that matching lacks \(z_j\). Either extreme matching lacks \(x\) or \(y\). Hence no matching contains all \(n+1\) vertices and the full set is not a face. Therefore the induced subcomplex is \(\partial\Delta^n\).

**2. Relative acyclic matching and a genuine simplicial collapse.** Apply in order the two element-toggle matchings used in the proof of [1, Theorem 14]: first pair every currently available face \(\sigma\) without \(x\) with \(\sigma\cup\{x\}\), then similarly toggle \(y\) on the still-unmatched faces. The two-stage matching is acyclic by the standard sequential element-matching lemma [1, Theorem 8]. The proof of [1, Theorem 14] explicitly shows that its unique unmatched face is
\[
\tau=\{y,z_1,\ldots,z_{n-1}\},
\]
where the empty face is initially paired with \(\{x\}\).

No matched pair crosses between the core \(L_n\) and its complement. Indeed a first-stage pair \(\sigma\leftrightarrow\sigma\cup\{x\}\) belongs to \(L_n\) on both sides whenever either side does: all proper subsets remain proper on adjoining \(x\), except \(\tau\), for which adjoining \(x\) is forbidden already in \(K_n\). Every core face other than \(\tau\) is first-stage matched, so the second-stage pairs are outside the core. Consequently restriction of the original acyclic matching to the relative face poset \(K_n\setminus L_n\) has **no unmatched cells**. For a finite simplicial complex and a subcomplex, a complete acyclic matching on the relative face poset yields an ordered sequence of elementary simplicial collapses onto that subcomplex: choose a removable matched pair from the acyclic partial order, delete it, and iterate; the subcomplex cannot supply a blocking coface because it is downward closed. Thus \(K_n\searrow L_n\). This is an ordinary simplicial collapse; the chosen collapse order is not claimed to be half-turn equivariant.

**3. Integral symmetry character.** The inclusion \(L_n\hookrightarrow K_n\) is both a homotopy equivalence (by the collapse) and a \(\rho\)-equivariant map (because \(\rho\) preserves the set of core vertices). The oriented boundary of the \(n\)-simplex generates \(\widetilde H_{n-1}(L_n;\mathbb Z)\cong\mathbb Z\). On the ordered core vertex set \((x,y,z_1,\ldots,z_{n-1})\), the half-turn is one transposition \((x\ y)\), together with reversal of \(n-1\) elements, which contributes \(\lfloor(n-1)/2\rfloor\) further transpositions. Its induced degree is therefore
\[
(-1)^{1+\lfloor(n-1)/2\rfloor}=(-1)^{n(n+1)/2}.
\]
The equivariant inclusion transfers this integral degree to \(K_n\). All other reduced integral homology vanishes by the collapse onto the sphere.

**4. Rational quotient.** For a finite group action on a finite simplicial complex, rational transfer identifies homology of the orbit space with invariants in rational homology. The invariant part of the one-dimensional top representation is nonzero precisely when the above sign is positive. This happens for \(n\equiv0,3\pmod4\). Since \(n\ge2\), the space and its quotient are connected, completing the claim.

## Verification
The standalone Python 3 checker `check_honeycomb_core.py` enumerates all perfect matchings by their plane-partition parameters; verifies their half-turn images; constructs every face; constructs the embedded simplex boundary; and performs the exact two-stage matching. For \(n=2,3,4\), respectively, it obtains \(6,10,15\) perfect matchings and \(1347,17487,206127\) faces (including the empty face), with \(670,8736,103048\) matched pairs outside the core. For \(n=2,3\), a separate directed-Hasse-graph topological sort confirms that the relative matching is acyclic. At \(n=4\), exhaustive pairing is checked, while acyclicity follows from the general lemma rather than a separate graph sort. The checker terminates with `HONEYCOMB_INVARIANT_SPHERE_CORE_CHECKS_OK`.

The finite tests check the edge conventions and relative matching; the argument above, not finite extrapolation, proves the theorem for all \(n\ge2\).

## Relationship to prior work
Bayer, Jelić Milutinović and Vega [1] prove the nonequivariant sphere homotopy type \(\mathcal M_p(H_{1\times2\times n})\simeq S^{n-1}\) using the same two-stage matching. Their paper supplies the fundamental matching classification and the critical-cell argument. The present claim is **not** a new proof of that already published homotopy type: it isolates a canonical, half-turn invariant, induced minimal simplex-boundary spine, proves an actual simplicial collapse onto that specified spine, and computes the integral half-turn degree and the rational quotient dichotomy. The published theorem alone gives no homological action of the half-turn; the further identification of its invariant core is essential for this conclusion. The full accessible arXiv preprint [1] was inspected, including its definitions, Proposition 10, Lemmas 12–13, Theorems 8 and 14, and its conclusions. A published 2023 journal version has the same stated principal results [2].

## Limitations
The collapse is not asserted to be equivariant, and no claim is made about the homotopy type, torsion, or fixed-point stratification of the quotient. Only its **rational** homology follows from the character. The theorem concerns the perfect-matching complex, not the ordinary matching complex. The sign formula is intrinsic to the identified geometric half-turn; no full symmetry-group classification is asserted at exceptional side lengths. A bibliographically unindexed equivalent computation cannot be excluded.

## References
[1] Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first posted 2022-09-06, especially Sections 1.2 and 3.2–3.3, https://arxiv.org/html/2209.02803v1.

[2] Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics **30** (2023), paper P2.45, published 2023-06-16, DOI: 10.37236/11525.
