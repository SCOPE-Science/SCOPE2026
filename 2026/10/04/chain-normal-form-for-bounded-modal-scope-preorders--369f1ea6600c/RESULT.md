# Chain normal form for bounded-modal scope preorders
## Finding

Murase and Maniwa define a BML-structure as a preorder of scopes
\[
(D,\preceq)
\]
with a rooted modal preorder
\[
\sqsubseteq
\]
satisfying the stability condition
\[
\preceq\ \subseteq\ \sqsubseteq.
\]

When the scope order is a finite chain,
\[
D_n=\{0<1<\cdots<n-1\},
\]
all possible modal preorders admit a complete normal form.

A relation
\[
\sqsubseteq
\]
is a BML modal preorder on this chain if and only if the chain can be partitioned into contiguous nonempty blocks
\[
B_0<B_1<\cdots<B_r
\]
such that
\[
x\sqsubseteq y
\quad\Longleftrightarrow\quad
\operatorname{block}(x)\le\operatorname{block}(y).
\]

Equivalently, the equivalence classes of the total preorder \(\sqsubseteq\) are intervals in the chain.

Therefore the modal relation is determined by deciding, at each of the
\[
n-1
\]
adjacent gaps, whether that gap is a cut or whether the two adjacent scopes lie in the same modal-equivalence block. Consequently,
\[
\boxed{
\#\{\text{BML modal preorders on }D_n\}=2^{n-1}.
}
\]

There is also a closed form for the bounded-modal successor sets.

For each
\[
d\in D_n,
\]
let
\[
\ell(d)
\]
be the least element of the \(\sqsubseteq\)-equivalence block containing \(d\). Then
\[
\boxed{
d\sqsubseteq e
\quad\Longleftrightarrow\quad
\ell(d)\le e.
}
\]

Hence, if a classifier \(\gamma\) denotes
\[
b=\rho(\gamma),
\]
the local quantification domain in Murase--Maniwa's semantic clause for
\[
\Box_{\succeq\gamma}A
\]
is exactly
\[
\boxed{
\{e:d\sqsubseteq e,\ b\le e\}
=
\{e:e\ge\max(\ell(d),b)\}.
}
\]

Thus every bounded modality on a finite scope chain quantifies over one ordinary suffix.

The whole modal relation is encoded by the map
\[
\ell:D_n\to D_n,
\]
which satisfies
\[
\ell(0)=0
\]
and, for every
\[
0\le i<n-1,
\]
\[
\ell(i+1)\in\{\ell(i),i+1\}.
\]
Conversely, every map satisfying these conditions defines exactly one BML modal preorder.

So finite chain BML-structures have an exact \(n-1\)-bit modal representation rather than an arbitrary quadratic relation table.

## Assumptions and scope

The theorem fixes the intuitionistic scope preorder to the labelled finite chain
\[
0<1<\cdots<n-1.
\]

The modal relation is required to be a preorder and to satisfy the source paper's BML stability condition. In Definition 2.1, that condition is equivalent to
\[
\preceq\subseteq\sqsubseteq.
\]

The result classifies the modal-relation component of a BML-structure. Valuations remain arbitrary upward-closed sets, and the outer Kripke preorder between growing BML-structures in Definition 4.1 is not being classified.

The suffix formula concerns the local domain quantified over by the bounded-modal semantic clause. Formula truth still includes the source paper's outer persistence over larger Kripke worlds.

Because the labelled finite chain has only the identity order automorphism, the count
\[
2^{n-1}
\]
is also the number of isomorphism classes of modal-preorder expansions of this fixed chain.

## Proof

Let
\[
\le
\]
denote the chain order, and let
\[
R=\sqsubseteq.
\]

By the BML stability condition,
\[
\le\ \subseteq R.
\]
Because the chain order is total, any two points are already comparable by \(R\). Since \(R\) is a preorder, \(R\) is therefore a total preorder.

Define
\[
x\sim y
\quad\Longleftrightarrow\quad
xRy\ \text{and}\ yRx.
\]
This is the standard equivalence relation associated with a total preorder.

We first prove that every \(\sim\)-class is an interval.

Suppose
\[
i<j<k
\]
and
\[
i\sim k.
\]
The chain inclusion gives
\[
iRj
\quad\text{and}\quad
jRk.
\]
Since
\[
kRi,
\]
transitivity gives
\[
jRi.
\]
Thus
\[
i\sim j.
\]

Also,
\[
kRi
\quad\text{and}\quad
iRj
\]
give
\[
kRj,
\]
while
\[
jRk
\]
already holds. Hence
\[
j\sim k.
\]

Therefore equivalence classes are contiguous intervals.

Distinct equivalence classes inherit the left-to-right order of the chain. If a point in an earlier class lies to the left of a point in a later class, the chain order gives the corresponding \(R\)-edge. A reverse \(R\)-edge would merge the two classes. Hence
\[
xRy
\]
holds exactly when the block of \(x\) is no later than the block of \(y\).

Conversely, take any partition of the chain into contiguous nonempty blocks and define \(R\) by the block order. This relation is reflexive and transitive, and it contains the original chain order. Hence it is exactly a valid BML modal preorder.

A partition of an \(n\)-element chain into contiguous blocks is a composition of \(n\). Equivalently, each of the
\[
n-1
\]
adjacent gaps is independently declared either a cut or a tie. Therefore there are
\[
2^{n-1}
\]
such modal preorders.

Now define
\[
\ell(d)
\]
to be the least point in the block of \(d\).

We claim that
\[
dRe
\quad\Longleftrightarrow\quad
\ell(d)\le e.
\]

For the forward direction, suppose
\[
dRe.
\]
If
\[
e<\ell(d),
\]
then the chain order gives
\[
eRd.
\]
Together with \(dRe\), this would imply
\[
e\sim d,
\]
contradicting the minimality of \(\ell(d)\). Hence
\[
\ell(d)\le e.
\]

For the reverse direction, suppose
\[
\ell(d)\le e.
\]
Because \(d\) and \(\ell(d)\) lie in the same equivalence block,
\[
dR\ell(d).
\]
The chain inclusion gives
\[
\ell(d)Re.
\]
By transitivity,
\[
dRe.
\]

This proves the claimed description of modal successors.

Murase--Maniwa's bounded-modal semantic clause quantifies over exactly those \(e\) satisfying
\[
d\sqsubseteq e
\]
and
\[
\rho(\gamma)\preceq e.
\]
On the chain, if
\[
b=\rho(\gamma),
\]
these conditions are
\[
e\ge\ell(d)
\]
and
\[
e\ge b.
\]
Therefore the quantification domain is the suffix
\[
\{e:e\ge\max(\ell(d),b)\}.
\]

Finally, the interval-block description immediately gives
\[
\ell(0)=0.
\]
When moving from \(i\) to \(i+1\), either the points stay in the same block, giving
\[
\ell(i+1)=\ell(i),
\]
or a new block begins at \(i+1\), giving
\[
\ell(i+1)=i+1.
\]

Conversely, any map satisfying these recurrences specifies exactly which adjacent gaps are ties and which are cuts, so it reconstructs the unique block partition and hence the unique modal preorder.

## Verification

The bundled checker exhaustively enumerates every binary relation on the \(n\)-chain that already contains the chain order for
\[
1\le n\le6.
\]

It filters those relations for reflexivity and transitivity. For every surviving modal preorder it verifies:

1. the equivalence classes are contiguous intervals;
2. the relation is exactly the left-to-right order of those blocks;
3. the number of relations is
\[
2^{n-1};
\]
4. the map \(\ell\) satisfies
\[
\ell(0)=0,
\qquad
\ell(i+1)\in\{\ell(i),i+1\};
\]
5. for every pair of points,
\[
d\sqsubseteq e
\quad\Longleftrightarrow\quad
\ell(d)\le e;
\]
6. for every current point \(d\) and every classifier value \(b\), the bounded-modal quantification domain is exactly
\[
\{e:e\ge\max(\ell(d),b)\}.
\]

It independently reconstructs all relations from the \(n-1\) cut/tie bit strings and confirms exact agreement with the exhaustive preorder set.

The script prints `VERIFY_OK`.

## Relationship to prior work

Murase and Maniwa introduce BML in 2026 to make scope dependencies explicit in constructive modal reasoning for multi-stage programming. Their Definition 2.1 requires the modal relation to be a preorder containing the scope preorder, and their bounded-modal semantic clause quantifies over modal successors that are also above a classifier bound.

The checked full text does not specialize these structures to finite chains, classify the possible modal preorders, count them, or give the suffix normal form for bounded-modal successor sets.

The order-theoretic fact that a total preorder is an ordered family of equivalence classes is standard. The additional point here is the exact interaction with the **fixed chain inclusion**
\[
\preceq\subseteq\sqsubseteq:
\]
the classes must be contiguous, the choices reduce to adjacent cuts, and Murase--Maniwa's bounded-modal domain collapses to a single suffix beginning at
\[
\max(\ell(d),b).
\]

This specialization is natural for BML because linearly nested lexical scopes are a basic staging configuration. It gives an exact finite search space and a linear-size representation for the modal component of such scope structures.

Targeted searches for BML chain models, total-order BML structures, scope-chain modal preorders, and bounded-modality suffix semantics did not locate this classification.

## Limitations

The theorem concerns only finite linearly ordered scope structures. General finite partial orders can support many more modal preorders and need not admit a one-dimensional cut representation.

The result does not classify valuations, growing-domain Kripke worlds, proof terms, or classifier quantification.

The \(n-1\)-bit encoding describes the modal relation exactly, but it does not by itself prove a complexity bound for BML validity or satisfiability.

The interval-block classification is elementary order theory; the scientific content claimed here is its exact specialization to the new BML stability condition together with the resulting bounded-modal suffix semantics and finite census.

## References

[1] Yuito Murase and Akinori Maniwa, “Bounded Modal Logic: Explicit Scope Dependencies in Multi-Stage Programming,” arXiv:2602.09462, first posted 10 February 2026.

[2] B. A. Davey and H. A. Priestley, *Introduction to Lattices and Order*, second edition, Cambridge University Press, 2002.
