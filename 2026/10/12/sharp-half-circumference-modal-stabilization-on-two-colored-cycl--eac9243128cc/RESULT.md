# Sharp half-circumference modal stabilization on two-colored cycles

## Finding

Consider the loopless, undirected cycle \(C_n\), for any integer \(n\ge3\), as a one-relation Kripke frame with \(iRj\) precisely when \(j=i\pm1\pmod n\). A single propositional variable \(p\) labels vertices by a binary cyclic word \(w=(w_0,\ldots,w_{n-1})\). Write \(u\equiv_t v\) when \(u\) and \(v\) satisfy the same basic modal formulas of nesting depth at most \(t\). Let \(D_n\) act on the vertex set by rotations and reflections, and let \(H_w\le D_n\) be the subgroup preserving the given binary labeling.

**Theorem.** At every depth \(t\ge0\), the \(\equiv_t\)-classes are exactly the classes of the length-\(2t+1\) cyclic factors of \(w\), identified up to reversal. Moreover,
\[
\boxed{\quad \equiv_{\lfloor n/2\rfloor-1}\;=\;\text{orbit equivalence of }H_w.\quad}
\]
Thus one propositional variable generates the full Boolean modal algebra \(\mathcal P(C_n)\) exactly when \(H_w\) is trivial. The bound on depth is optimal uniformly over binary labelings for every \(n\ge6\): the three-marked-vertex pattern
\[
\boxed{\quad V(p)=\{0,1,3\}\quad}
\]
has a discrete final modal partition, but its partition at depth \(\lfloor n/2\rfloor-2\) is still non-discrete. No binary valuation fully generates \(\mathcal P(C_n)\) for \(3\le n\le5\), whereas for \(n\ge6\) three marked vertices are necessary and sufficient.

There is also a complete *disconnected-cycle* generator criterion. For a finite disjoint union containing \(c_n\) labeled copies of \(C_n\) for each \(n\ge3\), a single binary valuation fully generates its powerset algebra if and only if each colored component is aperiodic and reflection-asymmetric and, among components of the same length, no two colorings are dihedrally equivalent. Consequently, its exact number of generating valuations is
\[
\boxed{\quad \prod_{n\ge3}(2n)^{c_n}\,(b_n)_{c_n},\quad}
\]
where \((b)_c=b(b-1)\cdots(b-c+1)\), \((b)_0=1\), and \(b_n\) is the **previously known** number of aperiodic reflection-asymmetric binary bracelets of length \(n\). In particular, the number is zero if any \(c_n>b_n\). The bracelet numbers themselves are not asserted to be new.

## Assumptions and scope

Only ordinary Boolean modal logic with one diamond for the undirected cycle adjacency and one propositional letter is used; no vertex constants, counting operators, global modalities or fixpoint operators are allowed. Modal depth counts nested diamonds or boxes. The generated Boolean modal algebra is the smallest Boolean subalgebra containing \(V(p)\) and closed under the diamond-image operation; its atoms are exactly the stable finite-depth modal-equivalence classes. The cycle vertices have their indicated fixed labels, and different components of a disjoint union are distinct labeled components. All assertions concern finite simple cycles of lengths at least three.

For a word \(w\) and vertex \(i\), define its centered cyclic factor
\[
F_t(w,i)=(w_{i-t},w_{i-t+1},\ldots,w_{i+t}),
\]
with subscripts modulo \(n\). Let \([F_t(w,i)]_{\rm rev}\) denote the unordered two-element possibility \(\{F_t(w,i),F_t(w,i)^{\rm rev}\}\), which may be a singleton for palindromes.

## Proof

**Lemma 1 (local reconstruction).** For any alphabet and integer \(t\ge1\), a centered word of length \(2t+1\) is determined up to reversal by its center symbol and the unordered pair of reversal classes of its length-\(2t-1\) factors centered one step to its left and right.

To see this, represent the first word by \((a_{-t},\ldots,a_t)\) and a candidate second word by \((z_{-t},\ldots,z_t)\). Reverse the second word, if needed, so that its left factor is paired with the first left factor, and its right factor with the first right factor. Each factor can be matched in its forward or reversed orientation. With both forward, the union of factors covers every position and gives \(z=a\). With exactly one reversed, equality on the overlapping positions forces the last two previously unassigned symbols to coincide with the corresponding symbols of \(a\); when \(t=1\) or \(2\), the same conclusion follows directly from the center and the overlap. For completeness, in the forward-left/reversed-right case, the overlap equations are \(a_x=a_{2-x}\) for \(-t+2\le x\le t-2\), which determine the two rightmost positions of \(z\) to be \(a_{t-1},a_t\). The opposite mixed-orientation case is its reflection. With both factors reversed, overlap gives \(a_x=a_{x+4}\) wherever both sides lie in the word, while equality of centers gives \(a_{-2}=a_0=a_2\) whenever those positions exist. The word is therefore four-periodic on its available interval with its two even residue classes equal, hence symmetric under the requisite two factor reversals; again \(z=a\). Thus the original un-oriented candidate was either \(a\) or its reversal. This proves the lemma.

**Lemma 2 (factor interpretation).** For every \(t\ge0\), two vertices have the same depth-\(t\) modal type if and only if their centered length-\(2t+1\) cyclic factors agree up to reversal.

At depth zero both tests read only the center bit. Assume the assertion at depth \(t-1\). The depth-\(t\) type is precisely the previous type together with the *set* of types occurring at the two neighbors. Since every vertex has exactly two neighbors, that set together with the previous type determines the neighbor *multiset*: when the set has size one, both neighbors have that type, and when it has size two, each appears once. This is the counting refinement signature. By the inductive hypothesis, the two neighbor types are the reversal classes of their centered factors of length \(2t-1\); Lemma 1 reconstructs the centered factor of length \(2t+1\), and the converse is immediate. The assertion follows by induction. In particular, ordinary and graded two-neighbor refinement agree on these cycles.

**Lemma 3 (half-circumference orbit bound).** Put \(T=\lfloor n/2\rfloor-1\). If \([F_T(w,i)]_{\rm rev}=[F_T(w,j)]_{\rm rev}\), a color-preserving rotation or reflection sends \(i\) to \(j\).

Choose a dihedral permutation \(h\) sending \(i\) to \(j\) and aligning the two oriented factors. The color equalities \(w_x=w_{h(x)}\) then hold on an interval of \(2T+1\) consecutive positions about \(i\). If \(n\) is even, this misses exactly one vertex. Because \(h\) permutes all positions, the total number of ones before and after applying \(h\) is equal, forcing equality also at the omitted position. Hence \(h\) is a color-preserving automorphism.

If \(n=2k+1\) is odd, the omitted vertices are the adjacent pair \(u=i+k\), \(v=i-k\). Equality of total color counts shows that either \(h\) preserves the word everywhere or there are two color discrepancies, exactly at \(u,v\), with the two bits exchanged. Suppose the latter. If \(h\) is a reflection, its discrepancy set is invariant under \(h\), so \(h\) interchanges \(u\) and \(v\). The reflection fixing that adjacent pair setwise also fixes its opposite vertex \(i\), yielding \(h(i)=i\), hence \(i=j\); the identity automorphism is then sufficient.

If instead \(h(x)=x+s\) is a rotation, the binary sequence changes along the successor step \(s\) precisely at \(u,v\). Each orbit of that step contains an even number of color changes. The adjacent positions \(u,v\) must therefore belong to the same orbit, which forces \(\gcd(s,n)=1\). The step visits all vertices and its color sequence consists of two monochromatic arcs separated by the boundary edges starting at \(u,v\). The reflection
\[
r(x)=u+v+s-x=2i+s-x\pmod n
\]
exchanges the two boundary edges while preserving each monochromatic arc, so it preserves all colors and sends \(i\) to \(i+s=j\). Lemma 3 is proved.

Every color-preserving automorphism preserves satisfaction of every modal formula. Lemma 2 and Lemma 3 show the reverse containment of the orbit partition in the depth-\(T\) modal partition; therefore the two partitions coincide. The finite powerset algebra is generated precisely when every modal type is a singleton, equivalently when all \(H_w\)-orbits are singletons. The action of \(D_n\) on vertices is faithful, so this is equivalent to \(H_w=\{1\}\).

For \(n\ge6\), the three occupied vertices \(0,1,3\) have circular gaps \(1,2,n-3\), which are positive and pairwise distinct. A nontrivial rotation would force three equal gaps; a reflection would force two equal gaps. Thus this valuation has trivial stabilizer. To prove its depth is exactly \(T\), take \(t=T-1\). For even \(n=2k\), the factors about \(k+1\) and \(k+2\) are respectively a one followed by \(2t\) zeros and \(2t\) zeros followed by a one. For odd \(n=2k+1\), use centers \(k+1\) and \(k+3\); their factors have the same two patterns. They therefore remain equivalent at depth \(t\). For \(n\le5\), every two-coloring has a nontrivial dihedral symmetry. Moreover, any marked set of size at most two in any cycle admits a reflection fixing it setwise, whereas the three-marker construction works for \(n\ge6\). This proves the sharp bound and the minimum-support statements.

Finally, consider disjoint cycles. Every modal type is determined by arbitrarily long centered periodic factors, up to reversal. If two states from different components are modally equivalent, a consistent choice of orientation along an infinite subsequence of factor lengths identifies their two doubly infinite periodic color words, up to translation and reversal. Hence the primitive periods agree and the primitive bracelets agree. A colored component with no internal dihedral symmetry necessarily has primitive period equal to its entire length; distinct such components are then modally disjoint exactly when their bracelet classes differ. This proves the disconnected generator criterion. For a given cycle length \(n\), each asymmetric primitive bracelet has exactly \(2n\) distinct labeled words, so assigning different bracelet classes to \(c_n\) labeled components gives \((2n)^{c_n}(b_n)_{c_n}\) possibilities. Multiplication over distinct lengths gives the census.

The classical bracelet count can be computed without a precomputed table by Möbius inversion. Let \(\mu\) denote the Möbius function and define
\[
c(m,a)=\begin{cases}(m+1)/2,&m\text{ odd},\\m/2+1,&m\text{ even and }a\text{ even},\\m/2,&m\text{ even and }a\text{ odd}.\end{cases}
\]
Then, for \(n\ge3\),
\[
b_n=\frac1{2n}\left(\sum_{d\mid n}\mu(d)2^{n/d}-\sum_{a=0}^{n-1}\sum_{d\mid n}\mu(d)2^{c(n/d,a)}\right).
\]
Indeed, the first sum counts primitive words, while the double sum counts primitive words fixed by a reflection. A primitive word is fixed by at most one reflection, because two distinct reflections compose to a nonidentity rotation. Dividing by \(2n\) counts the free dihedral orbits. The formula agrees with the pre-existing aperiodic chiral bracelet sequence and is included solely for a self-contained enumeration.

## Verification

Running the accompanying standard-library script with `python verify.py` produces a `VERIFY_OK` record. It exhaustively compares the ordinary modal partition, the centered-factor reversal partition, and the dihedral orbit partition for all \(8{,}184\) binary colorings of cycles of lengths \(3\) through \(12\). It checks \(43{,}688\) individual depth comparisons; independently builds the Boolean modal algebra in \(56\) smaller cases; checks \(28{,}672\) colorings across two-component frames; compares the Möbius bracelet counts with a brute-force census; verifies the sharp three-marker family through size \(120\); and runs \(320\) seeded random larger cases. Finite verification supports but does not replace Lemmas 1–3 or the unrestricted enumeration proof.

## Relationship to prior work

The interpretation of modal types by bisimulation and partition refinement is classical. Kiefer and McKay (2020, arXiv:2005.10182v1) analyze the iteration number of 1-dimensional Weisfeiler–Leman color refinement on general graphs, including a sharp general upper-bound phenomenon and path examples. Their inspected paper does not state the prescribed-initial-binary-color cycle orbit theorem or this sharp half-circumference bound. The present result concerns vertex-colored cycles and the one-atom modal algebra, not their general uncolored extremal construction.

Hadjicostas (2019), building on formulas credited there to Russell and Kociemba, already gives explicit generating functions and counting formulas for aperiodic, reflection-asymmetric binary bracelets. OEIS A032239 likewise records those numbers. **Neither the bracelet count nor the graph-theoretic concept of a distinguishing two-coloring is asserted to be novel.** The proposed incremental contribution is the exact *every-depth modal characterization*, the sharp uniform stabilization bound and its three-marker witness, and the consequent full modal-generator criterion on unions of cycles. Standard results on distinguishing colorings do not by themselves establish that ordinary modal equivalence reaches the same vertex orbit partition at a specified sharp depth.

## Limitations

This is a theorem only for one ordinary modal adjacency relation on disjoint unions of finite simple cycles. Its sharp-depth statement is for a single connected cycle; no uniform bound in terms of the maximum component length is claimed for all disconnected unions, because distinct components may require additional depth to separate. The originality comparison targeted the principal sources and selected searches, not every older result on circular-word reconstruction or colored equitable partitions. Independent mathematical audit has not been performed.

## References

1. Sandra Kiefer and Brendan D. McKay, *The Iteration Number of Colour Refinement*, first arXiv version, 20 May 2020, arXiv:2005.10182v1, https://arxiv.org/abs/2005.10182.
2. Petros Hadjicostas, *On the number of aperiodic chiral bracelets of two colors*, dated 6 June 2019, https://oeis.org/A032239/a032239.pdf (especially section 5).
3. OEIS A032239, *Number of identity bracelets of n beads of 2 colors*, https://oeis.org/A032239.
4. Martin Otto, *Graded modal logic and counting bisimulation*, arXiv:1910.00039v1, 30 September 2019, https://arxiv.org/abs/1910.00039.
