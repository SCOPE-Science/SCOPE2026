# Independent mathematical audit

## correctness

PASS

Exactly k windows contain the joker, so the resolved occurrence count is N+k. At counting equality for k>=3, the two resolved walks U→V and the nonempty ordinary V→U walk would partition the de Bruijn edges. Balance forces U=V, where the two resolutions already use both possible outgoing edges, precluding the ordinary walk. For k=2 the two length-2 hosts each miss a constant pair; the stated k=1,2,3 witnesses give the upper bounds. For k>=4 inspect the one-positions of U b V, indexed from zero: k−2 and 2k−3, plus k−1 for b=1. With b=0 the first and last windows coincide, the intervening single-one windows have distinct positions, and one window has two extreme ones. With b=1 the adjacent pair moves through distinct offsets, the unique triple is distinct, and the final two-one window has distance k−2. These patterns prove that the resolved walks delete exactly 2k−1 distinct edges, with the sole duplicate U0:U→V. Hence the complement has imbalance +1 at V and −1 at U. Only the three displayed deletions can block append-one; after two steps the edges end in at least three ones, while a second-step block requires the unique deleted edge ending in 11. The four explicit retained edges attach all exceptions to the append-one component. Euler's criterion therefore yields the complementary trail, and writing its bits between the joker's following V and preceding U gives a cyclic host with exactly the required windows and length. Multiplicity then follows by counting for every optimum. `python3 /workspace/branches/independent_replay.py 2` independently exhausted the counting-bound hosts for k=2–4 and checked the deleted edge multiplicities, balances, and weak connectivity for k=4–12; these checks do not replace the all-order proof.

## originality

PASS

The lower-bound obstruction follows already from known k-periodicity for exact-once partial cycles. The credited distinction is an explicit all-order attainment with one unavoidable repeated resolution under the single-total-joker cyclic constraint. The available exact-once and repeating-template results do not yield that attainment.

## value

PASS

Allowing repetitions opens a natural next question beyond nonexistence of exact-once cyclic partial words. The result answers it for the basic binary single-joker case: exactly one extra resolution is both necessary and sufficient at every nontrivial order. The constructive retained-edge trail certifies that this small additive gap is achievable rather than a counting artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
