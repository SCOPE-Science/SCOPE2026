# Dyadic rigidity of cyclic factor classes in the period-doubling word

## Finding
Let \(p=0100010101000100\cdots\) be the one-sided binary period-doubling word defined by \(p=\mu(p)\), where \(\mu(0)=01\) and \(\mu(1)=00\). For every integer \(n\ge1\), let \(\mathcal C_n\) be the set of cyclic-conjugacy classes represented by length-\(n\) factors of \(p\). The map
\[
\Phi_n:\mathcal C_n\longrightarrow\mathcal C_{2n},\qquad [u]\longmapsto[\mu(u)]
\]
is a **bijection** for every \(n\ge1\). Consequently the cyclic complexity \(c_p(n)=|\mathcal C_n|\) obeys
\[
c_p(2n)=c_p(n)\quad(n\ge1),\qquad c_p(2^k m)=c_p(m)\quad(k\ge0,\ m\ge1).
\]
Thus the entire cyclic complexity at an even length is determined without loss by its odd part. For example \(c_p(2^k)=2\) and \(c_p(3\cdot2^k)=3\), all \(k\ge0\).

## Assumptions and scope
Factors are contiguous finite subwords of the fixed one-sided infinite word. A cyclic-conjugacy class consists of all rotations of one word; only classes represented by factors are counted. Indices are zero-based. The morphism is the particular two-uniform map \(0\mapsto01\), \(1\mapsto00\). The statement concerns every positive integer \(n\), including \(n=1\), and does not assert the same identity for arbitrary morphisms or arbitrary binary automatic words.

## Proof
**1. A parity observation.** Every even-indexed symbol of \(p\) is zero, since both images under \(\mu\) begin in zero. Therefore \(p\) contains no factor \(11\). In particular, every factor of length at least two contains a zero. For every finite binary word \(u=u_0\cdots u_{n-1}\), the image \(\mu(u)\) has zero at each even position and \(1-u_i\) at position \(2i+1\). For a factor \(u\) of length at least two, the latter image has at least one one because \(u\) contains a zero.

**2. Surjectivity.** Every factor \(z=p_i\cdots p_{i+2n-1}\) starts at an index \(i=2j\) or \(i=2j+1\). In the first case, \(z=\mu(p_j\cdots p_{j+n-1})\). In the second case, the first symbol of every morphism image is zero, so
\[
z=\operatorname{rot}_1\bigl(\mu(p_j\cdots p_{j+n-1})\bigr),
\]
where \(\operatorname{rot}_1\) is the left cyclic rotation by one position. Thus every cyclic class at length \(2n\) has a preimage. Also, a rotation of \(u\) by \(r\) letters induces a rotation of \(\mu(u)\) by \(2r\) positions, making \(\Phi_n\) well-defined.

**3. Injectivity for \(n\ge2\).** Suppose the images \(\mu(u)\) and \(\mu(v)\), for length-\(n\) factors \(u,v\), are cyclic conjugates. Each has at least one one, and all of its ones lie at odd indices. A cyclic rotation by an odd number would move each one to an even index, which is impossible in the other image. Thus the conjugating rotation has even length, say \(2r\). As the morphism is two-uniform, \(\operatorname{rot}_{2r}(\mu(u))=\mu(\operatorname{rot}_r(u))\). The images of the two alphabet letters differ, so \(\mu\) is injective on equal-length words. Hence \(v=\operatorname{rot}_r(u)\), proving injectivity on cyclic classes.

**4. The base length.** At \(n=1\), the two factor classes \([0]\) and \([1]\) map to \([01]\) and \([00]\). These are distinct, so the map is injective here also.

The four steps prove the bijection and equality of cyclic complexities. Applying that equality repeatedly yields the odd-part identity. Directly, \(c_p(1)=2\) and the five factors of length three form the three classes represented by \(000\), \(001\), and \(101\); the examples follow.

## Verification
The standalone checker generates a finite substitution prefix, enumerates cyclic classes by literal rotations (not by the proof's parity reduction), and compares the classes at lengths \(n\) and \(2n\) for each integer \(1\le n\le100\). It tests image-class equality and compares independently sampled windows of 4,000 and 8,000 starts. All 100 checks passed. Such finite tests are corroboration only; the universal result follows from the preceding proof.

## Relationship to prior work
Cassaigne, Fici, Sciortino and Zamboni introduced cyclic complexity and proved that this period-doubling word has \(c_p(2^k)=2\) by an argument showing that cyclic classes of length \(2n\) are represented by morphism images of classes at length \(n\). Their Proposition 17 establishes an inequality in its general uniform-substitution setting; it does not assert injectivity or bijectivity for this period-doubling morphism at all lengths. The new point is the reverse implication: zero-bearing factors force all possible conjugating rotations of their morphism images to respect the two-letter blocks. Thus *every* cyclic factor class, not merely the two classes at powers of two, is transported bijectively. The related group-complexity literature cites the period-doubling liminf result but does not state this dyadic-class bijection.

## Limitations
The proof does not yield a closed expression for \(c_p(m)\) at arbitrary odd \(m\). It is specific to the given fixed point and its substitution. The comparison does not preclude an earlier statement under an alternative terminology, and no independent audit has been performed. The examples are consequences of the bijection; the established powers-of-two fact is not claimed as new.

## References
1. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, first public arXiv version 24 February 2014, arXiv:1402.5843, especially Proposition 17 and Example 1. https://arxiv.org/abs/1402.5843
2. E. Charlier, S. Puzynina, L. Q. Zamboni, *On a group theoretic generalization of the Morse-Hedlund theorem*, preprint dated 29 August 2016, especially concluding comparison of cyclic complexity and the period-doubling word. https://orbi.uliege.be/bitstream/2268/192556/1/Group%20Complexity-orbi.pdf
