# Idempotent-commutator fibers and binary chromatic width in radical-square-zero quiver algebras

## Finding

Let \(Q=(V,E,s,t)\) be a finite loopless directed multiquiver with \(V\ne\varnothing\), let \(k=\mathbb F_q\), and let \(A=kQ/J^2\), where \(J\) is the ideal spanned by the arrows. For an arbitrary target \(z=\sum_{a\in E}z_a a\in J\), the number \(N_Q(z)\) of **ordered pairs of idempotents** \((P,R)\) whose additive commutator equals \(z\) is exactly

\[
N_Q(z)=\sum_{c:V\to\{0,1\}^2}\left(\prod_{a:z_a\ne0}
\mathbf 1_{\{c(s(a))\oplus c(t(a))=(1,1)\}}\right)
q^{\,|\{a\in E:c(s(a))\ne c(t(a))\}|}.
\]

Here \(\oplus\) denotes bitwise exclusive or on the two coordinates. All targets outside \(J\) have zero fibers. For targets inside \(J\), only the positions of the nonzero coefficients matter.

Form the simple undirected support graph \(H_z\) by retaining the unordered endpoints of arrows with \(z_a\ne0\), forgetting orientation and multiplicity. **A single idempotent commutator equals \(z\) if and only if \(H_z\) is bipartite.** This support criterion is valid over *every* field, not only finite ones.

More strongly, writing \(\ell(z)\) for the least nonnegative integer \(r\) such that \(z\) is a sum of \(r\) idempotent commutators, one has, over every field,

\[
\ell(z)=\left\lceil\log_2\chi(H_z)\right\rceil,
\quad\ell(0)=0.
\]

The chromatic number of an edgeless graph on a nonempty vertex set is taken to be \(1\). If \(H_Q\) is the underlying simple graph of the whole quiver, then \([A,A]=J\) and the maximum of \(\ell(z)\) over \(J\) equals \(\lceil\log_2\chi(H_Q)\rceil\). In particular, the idempotent restriction creates a genuinely field-size-independent, potentially unbounded commutator width.

For the zero target, the fiber additionally has the familiar Fortuin–Kasteleyn-type finite-sum form

\[
N_Q(0)=q^{|E|}\sum_{F\subseteq E}
\left(\frac{1-q}{q}\right)^{|F|}4^{\kappa(F)},
\]

where \(\kappa(F)\) is the number of components of the spanning multigraph \((V,F)\), including isolated vertices. This is an equivalent rewriting of the primary four-state formula, not an additional independent finding.

## Assumptions and scope

There are no loop arrows, but directed cycles, opposite arrows, parallel arrows, and isolated vertices are allowed. No assumptions on acyclicity or characteristic are made. Multiplication is the path-algebra multiplication truncated at paths of length two. A sum with no terms equals zero. The exact fiber cardinality requires \(k=\mathbb F_q\); the support and width conclusions hold over an arbitrary field. The width concerns only additive commutators of **two idempotents in the same algebra**, not unrestricted commutators or multiplication of idempotents.

## Proof

**1. Coordinate multiplication and idempotents.** Write an arbitrary element as \(X=\sum_{v\in V}x_v v+\sum_{a\in E}x_a a\). For \(a:u\to v\), the vertex and arrow coordinates of a product \(XY\) are respectively

\[
(XY)_v=x_vy_v,\qquad (XY)_a=x_u y_a+x_a y_v.
\]

If \(P^2=P\), each \(p_v\) lies in \(\{0,1\}\). Each arrow coordinate satisfies \((p_{s(a)}+p_{t(a)}-1)p_a=0\). Thus \(p_a\) is arbitrary precisely when the two endpoint bits differ, and it must vanish otherwise. This remains true in characteristic two.

**2. Exact commutator fibers.** Take two idempotents \(P,R\), with vertex-bit functions \(p,r:V\to\{0,1\}\). Their commutator is purely radical; its coordinate at \(a:u\to v\) equals

\[
[P,R]_a=(p_u-p_v)r_a-(r_u-r_v)p_a.
\]

If both vertex bits agree across \(a\), both arrow variables are forced to zero and the commutator coordinate vanishes, giving exactly one local choice. If exactly one bit changes, precisely one arrow variable is free, the commutator is still zero, and there are \(q\) local choices. If both bits change, two arrow variables are free and the displayed nonzero linear form assumes each prescribed value exactly \(q\) times. Consequently the local multiplicity is \(q\) whenever the paired vertex labels differ, except that a nonzero target requires *both* bits to change. All arrow coordinates are independent because \(J^2=0\). Multiplying local counts and summing over the four possible pairs of vertex bits proves the displayed formula and its support-only dependence. Every additive commutator is in \(J\), which excludes all other targets.

**3. Single-commutator support.** If \(z=[P,R]\) and \(z_a\ne0\), then both vertex bits of \(P,R\) change across that arrow. In particular \(p:V\to\{0,1\}\) is a proper two-coloring of \(H_z\). Conversely, suppose \(H_z\) is bipartite and choose a proper two-coloring \(b\). Take \(P=\sum_v b_v v\) and \(R=\sum_v b_v v+\sum_a r_a a\), with \(r_a=z_a/(b_{s(a)}-b_{t(a)})\) for arrows in the support and \(r_a=0\) for other arrows. Both are idempotent by step 1, and step 2 gives \([P,R]=z\). The division is legitimate over any field because the relevant differences are \(\pm1\).

**4. Sharp additive width.** Suppose \(z=\sum_{i=1}^h[P_i,R_i]\). For each \(i\), let \(b_i(v)\) be the vertex bit of \(P_i\). Every nonzero target arrow has a nonzero coordinate in at least one summand, so its endpoints differ for that \(b_i\). Therefore \(v\mapsto(b_1(v),\ldots,b_h(v))\) is a proper coloring of \(H_z\) with at most \(2^h\) colors. This proves \(\chi(H_z)\le2^h\).

Conversely, let \(h=\lceil\log_2\chi(H_z)\rceil\) and encode any proper coloring by \(h\)-bit strings. Assign each arrow in the nonzero support to one coordinate in which its endpoints differ. For each coordinate \(i\), take a pure-diagonal idempotent \(P_i\) with the corresponding vertex bit function, and an idempotent \(R_i\) with identical diagonal and radical coefficient \(z_a/(b_i(s(a))-b_i(t(a)))\) at arrows assigned to \(i\), zero elsewhere. Each commutator is supported on its assigned arrows and agrees there with \(z\). Their sum is exactly \(z\), proving the upper bound. If \(z=0\), take the empty sum. Since every arrow basis element is a commutator \([s(a),a]\), one has \([A,A]=J\). A target with all arrow coefficients nonzero realizes the whole underlying simple graph, giving the asserted global width.

**5. Zero fiber.** For \(z=0\), each vertex has four labels and an arrow contributes the weight \(1\) when its endpoints have the same paired label, otherwise \(q\). Expand each edge factor as \(q+(1-q)\mathbf1_{\{c(u)=c(v)\}}\), and sum over labelings; imposing equality on a selected arrow set \(F\) leaves exactly \(4^{\kappa(F)}\) labelings. The displayed finite sum follows.

## Verification

The accompanying standalone program `verify.py` constructs the full multiplication in the truncated quiver algebra, exhaustively enumerates idempotent pairs, calculates their commutators directly, and checks every radical target against the four-state formula. It tests ten quiver/field cases over fields of orders \(2,3,4\), including two parallel arrows, opposite arrows, a triangle, an isolated-vertex case, and the nonprime field \(\mathbb F_4\). A separate triangle test confirms that a fully supported characteristic-two target requires two summands. Run `python3 verify.py`; successful replay terminates with `VERIFY_OK`.

For example, on a triangle with one arrow per side over \(\mathbb F_2\), the single-commutator fiber has \(340\) solutions at zero, \(96\) per target supported on one arrow, \(16\) per target supported on two arrows, and \(0\) at the fully supported target. Their sum is \(676=26^2\), where \(26\) is the number of idempotents. This is an exhaustive finite check, not the proof of the general theorem.

## Relationship to prior work

The finite quiver-algebra setup is classical; see Nasr-Isfahani's account of the radical-square-zero quotient. Drnovšek–Radjavi–Rosenthal established general ring-theoretic tests for elements that are commutators of idempotents. Radjavi–Rosenthal examined triangularizability when the commutator of idempotents is nilpotent. Khurana–Lam established structure theorems for **invertible** commutators of idempotents. The present quiver commutators lie in the square-zero radical and are never invertible for nonzero algebras, so those invertibility results do not count the fibers here.

A previous unconstrained calculation for the same quiver family gives single-commutator support criterion \(\chi(H_z)\le q^2\) and unrestricted width \(\lceil\log_{q^2}\chi(H_Q)\rceil\). It does not require either input to be idempotent and therefore does not imply the present four-state formula or the stronger binary-coloring obstruction. For the triangle over \(\mathbb F_2\), a fully supported radical element is a single unrestricted commutator but not a single idempotent commutator. For complete underlying graphs on \(n\) vertices, the two respective widths differ by \(\lceil\log_2 n\rceil-\lceil\log_{q^2} n\rceil\), unbounded at fixed \(q\). Standard graph-coloring and Potts expansions supply background identities, not priority for the constrained algebraic multiplicity statement.

## Limitations

No result is asserted for looped quivers, nonfield vertex coefficient rings, quotients with nonzero length-two products, or other restricted classes of factors. The full text of the 2002 general-characterization paper was not available during the literature comparison; a different historical derivation cannot be excluded. An inaccessible primary source creates bibliographic uncertainty, not evidence of novelty. The enumeration tests cover only finite examples; arbitrary sizes, orientations, and fields follow from the coordinate proof. No independent mathematical audit has been carried out.

## References

1. H. Radjavi and P. Rosenthal, “On Commutators of Idempotents,” *Linear and Multilinear Algebra* **50** (2002), 121–124; online 18 October 2010. DOI: `10.1080/03081080290019540`.
2. R. Drnovšek, H. Radjavi, and P. Rosenthal, “A characterization of commutators of idempotents,” *Linear Algebra and its Applications* **347** (2002), 91–99. DOI: `10.1016/S0024-3795(01)00533-X`.
3. A. R. Nasr-Isfahani, “Singular equivalence of finite dimensional algebras with radical square zero,” arXiv:`1603.04191v1` (14 March 2016).
4. D. Khurana and T. Y. Lam, “Commutators and Anti-Commutators of Idempotents in Rings,” arXiv:`1808.02308v1` (7 August 2018).
