# Autojoin rigidifies Cintioli's dense bounded finite-one degree
## Finding

Let \(U\) be the set constructed by Cintioli whose bounded finite-one degree consists exactly of a dense linear order of one-one degrees. Write
\[
\mathcal D_U=\{[B]_1:B\equiv_{\mathrm{bfo}}U\}.
\]

Direct sum induces a natural binary operation on these one-one degrees:
\[
[B]_1\boxplus[C]_1=[B\oplus C]_1.
\]

Cintioli's scalar calculus classifies the elements by positive dyadic rationals. If
\[
\mathbb D_{>0}=\mathbb Z[1/2]_{>0}
=
\left\{\frac{m}{2^e}:m\ge1,\ e\ge0\right\},
\]
the paper supplies representatives \(S_q\), for \(q\in\mathbb D_{>0}\), satisfying
\[
S_q\le_1 S_r
\quad\Longleftrightarrow\quad
q\le r,
\]
and
\[
S_q\oplus S_r\equiv_1 S_{q+r},
\]
and every member of the bounded finite-one degree is one-one equivalent to some \(S_q\).

Therefore
\[
\boxed{
(\mathcal D_U,\boxplus,\le_1)
\cong
(\mathbb D_{>0},+,\le).
}
\]

This upgrades the source's order-theoretic realization to a complete ordered-semigroup description.

Two further consequences follow.

First, the Grothendieck group completion is
\[
\boxed{
G(\mathcal D_U)\cong(\mathbb Z[1/2],+,\le).
}
\]

Second, every semigroup automorphism is a dyadic rescaling:
\[
\boxed{
\operatorname{Aut}(\mathcal D_U,\boxplus)
=
\{q\mapsto2^zq:z\in\mathbb Z\}
\cong(\mathbb Z,+).
}
\]

If the base degree
\[
[U]_1=[S_1]_1
\]
is distinguished, its automorphism stabilizer is trivial.

Thus the autojoin operation sharply rigidifies the dense order. The pure order is isomorphic to
\[
(\mathbb Q,\le),
\]
which has continuum many order automorphisms, whereas the natural operation-preserving automorphism group of the same degree structure is only countable.

## Assumptions and scope

The reducibilities and finite autojoins are those used by Cintioli.

For sets \(A,B\subseteq\omega\), \(A\oplus B\) denotes the standard disjoint tagged join. Passing to one-one degrees makes the induced operation well defined: one-one equivalences of the two coordinates can be combined tagwise into a one-one equivalence of the joins.

The scientific input taken from the source is its exhaustive dyadic scalar calculus:
\[
U_e\equiv_1 2U_{e+1},
\]
every degree in the bounded finite-one degree is represented by a finite autojoin \(mU_e\), and after writing
\[
q=\frac{m}{2^e},
\]
the corresponding representatives satisfy the order and addition laws displayed above.

The primary arXiv abstract was accessible, but the primary PDF was not retrievable through the available arXiv and open-access routes during verification. The exact scalar laws were therefore cross-checked against a detailed source-focused review reproducing the paper's scalar-calculus statements. This access limitation is recorded as a residual originality risk rather than hidden.

## Proof

### Ordered-semigroup identification

Define
\[
\Theta:\mathcal D_U\to\mathbb D_{>0}
\]
by
\[
\Theta([S_q]_1)=q.
\]

The source's exhaustivity theorem gives surjectivity onto the entire internal degree structure.

The source's order law
\[
S_q\le_1S_r\iff q\le r
\]
implies that
\[
[S_q]_1=[S_r]_1
\quad\Longleftrightarrow\quad
q=r.
\]
Hence \(\Theta\) is injective and is an order isomorphism.

The scalar addition law gives
\[
\Theta([S_q]_1\boxplus[S_r]_1)
=
\Theta([S_q\oplus S_r]_1)
=
\Theta([S_{q+r}]_1)
=
q+r.
\]
Thus \(\Theta\) is an ordered-semigroup isomorphism.

Since addition of positive dyadic rationals is commutative and cancellative, the same is true of \(\mathcal D_U\).

### Grothendieck completion

The group of formal differences of positive dyadic rationals is the full dyadic additive group.

Indeed, every difference
\[
q-r
\]
with \(q,r\in\mathbb D_{>0}\) lies in
\[
\mathbb Z[1/2].
\]

Conversely, every
\[
x\in\mathbb Z[1/2]
\]
is a difference of two positive dyadic rationals. For example, choose a sufficiently large positive integer \(N\) so that \(x+N>0\), and write
\[
x=(x+N)-N.
\]

Therefore
\[
G(\mathcal D_U)\cong\mathbb Z[1/2].
\]

The order induced by the positive cone is the ordinary order.

### Automorphism classification

Let
\[
F:\mathbb D_{>0}\to\mathbb D_{>0}
\]
be an additive semigroup automorphism, and put
\[
c=F(1).
\]

For every \(e\ge0\),
\[
2^eF(2^{-e})
=
F(1)
=
c.
\]
Because the ambient dyadic semigroup is cancellative inside the rationals,
\[
F(2^{-e})=\frac{c}{2^e}.
\]

Hence for every
\[
q=\frac{m}{2^e}\in\mathbb D_{>0},
\]
additivity gives
\[
F(q)
=
mF(2^{-e})
=
cq.
\]

So every additive endomorphism is multiplication by the positive dyadic number \(c\).

Such a map is surjective exactly when multiplication by \(c\) is invertible on \(\mathbb D_{>0}\), equivalently when both \(c\) and \(c^{-1}\) lie in \(\mathbb Z[1/2]_{>0}\).

The positive units of
\[
\mathbb Z[1/2]
\]
are exactly
\[
2^z,\qquad z\in\mathbb Z.
\]

Indeed, write
\[
c=\frac{m}{2^e}
\]
in lowest terms with \(m\) odd. If \(c^{-1}\) is dyadic, then
\[
\frac{2^e}{m}
\]
has denominator a power of two, forcing
\[
m=1.
\]

Thus
\[
F(q)=2^zq
\]
for a unique integer \(z\), and composition corresponds to addition of exponents. Therefore
\[
\operatorname{Aut}(\mathcal D_U,\boxplus)\cong(\mathbb Z,+).
\]

Finally,
\[
F(1)=1
\]
forces
\[
2^z=1,
\]
hence
\[
z=0.
\]
So the stabilizer of the distinguished degree \([U]_1\) is trivial.

## Verification

The derivation after the source's scalar calculus is elementary and was reconstructed in full.

The load-bearing source facts are:

- the weak dyadic tower relation;
- exhaustivity by finite autojoins;
- the exact order law on dyadic scalars;
- the exact direct-sum addition law on those scalars.

The accessible primary abstract confirms the weak dyadic tower and exhaustivity by finite autojoins. A detailed source-focused review records the exact scalar order and addition formulas.

The automorphism proof uses no finite sampling. It classifies an arbitrary additive bijection by its value at \(1\), and surjectivity is reduced exactly to the unit group of \(\mathbb Z[1/2]\).

The Grothendieck-completion proof similarly treats arbitrary dyadic differences.

## Relationship to prior work

Cintioli's 2026 paper resolves an exact-realization problem by constructing a bounded finite-one degree whose internal one-one degrees, under \(\le_1\), form exactly a countable dense linear order without endpoints.

The paper does more internally than the abstract order statement: its proof labels the exhaustive family by positive dyadic scalars and makes finite autojoin additive on those scalars.

The present result isolates the algebra carried by that construction. Once direct sum is retained instead of forgotten, the internal structure is not merely an unnamed copy of the rational order; it is the positive cone of the ordered dyadic group.

Cintioli's earlier paper embeds a dense chain, an infinite antichain, and every countable partial order inside one bounded finite-one degree, so it does not supply an exhaustive semigroup of the form above.

Richter, Stephan, and Zhang motivate the exact-realization problem for one-one degrees inside stronger reducibility degrees. Their order-theoretic question does not classify the direct-sum automorphisms of Cintioli's later exact witness.

Targeted searches for bounded finite-one degrees together with autojoin, dyadic semigroups, Grothendieck completion, and automorphism groups did not locate this structural consequence.

## Limitations

The theorem concerns the particular witness \(U\) constructed by Cintioli and the canonical direct-sum operation on its internal one-one degrees.

It does not say that every bounded finite-one degree whose underlying one-one order is dense carries the same semigroup structure.

The group completion is an algebraic completion of the internal semigroup; negative dyadic elements are not themselves one-one degrees inside the bounded finite-one degree.

The automorphism classification is for operation-preserving automorphisms. Pure order automorphisms are far more numerous.

Primary-PDF access was unavailable during this verification, so the exact scalar formulas were checked through the accessible abstract plus a detailed source-focused review rather than through direct inspection of the paper's proof pages.

## References

[1] Patrizio Cintioli, “A Bounded Finite-One Degree Whose One-One Degrees Form Exactly a Dense Linear Order,” arXiv:2609.08092, first posted 8 September 2026.

[2] Patrizio Cintioli, “Dense Chains, Antichains, and Universal Partial Orders Inside a Bounded Finite-One Degree,” arXiv:2603.27901, first posted 29 March 2026.

[3] Linus Richter, Frank Stephan, and Xiaoyan Zhang, “Chains and Antichains inside Many-One Degrees and Variants,” arXiv:2607.06218, first posted 7 July 2026.
