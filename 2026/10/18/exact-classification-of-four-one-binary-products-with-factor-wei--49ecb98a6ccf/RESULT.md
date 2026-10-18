# Exact classification of four-one binary products with factor weights two and three

## Finding

For a positive integer \(n\), let \(s_2(n)\) be the number of ones in its ordinary base-two expansion. Fix arbitrary integers \(u\ge1\) and \(1\le v<w\), and put
\[
 a=1+2^u,\qquad b=1+2^v+2^w.
\]
These are precisely the odd positive integers of binary weights \(2\) and \(3\), respectively, with their one-bits indexed from the least significant bit.

**Theorem.** The equation \(s_2(ab)=4\) holds if and only if **exactly one** of these five disjoint conditions holds:

1. \(u=v=1\) and \(w\ge4\).
2. \(u=v\ge3\) and \(w=u+1\).
3. \(u=v\ge2\) and \(w=2u\).
4. \(u=w\ge3\) and \(v=1\).
5. \(u=1\), \(v\ge2\), and \(w=v+1\).

Thus the entire first asymmetric \((s_2(a),s_2(b),s_2(ab))=(2,3,4)\) product class consists of five explicit unbounded exponent families; there are no sporadic solutions outside them. In particular several families contain both factors tending to infinity.

**Sharpness corollary.** For every \(u\ge3\), choose \(v=u\) and \(w=u+1\). The corresponding weights are \((2,3,4)\) and \(\min\{a,b\}=1+2^u\to\infty\). Thus the bounded-minimum conclusion of Kaneko and Stoll's weight-four theorem, stated for input weights \(\ell,m\ge3\), becomes false if that hypothesis is weakened to \(\ell,m\ge2\).

## Assumptions and scope

The theorem concerns the ordinary nonnegative binary expansion, positive odd factors, and exactly four nonzero bits in the product. The exponent conditions above include all permissible \(u,v,w\) with \(u\ge1\), \(1\le v<w\), with no upper cutoff. The parameters are ordered as indicated; exchanging factors would instead give the symmetric \((3,2,4)\) formulation.

## Proof

Expand the product as a multiset of six powers of two:
\[
 ab=2^0+2^u+2^v+2^w+2^{u+v}+2^{u+w}.\tag{1}
\]
Replacing two copies of \(2^t\) by one copy of \(2^{t+1}\) is the standard binary carry. Each such replacement reduces the number of summands by exactly one. Carrying until the powers have distinct exponents is deterministic and gives the binary representation. Starting with six summands, exactly two carrying operations are therefore needed for weight four.

All coincidences among the five positive exponents in (1), subject to \(u\ge1\) and \(1\le v<w\), occur only under one of the three relations
\[
 u=v,\qquad u=w,\qquad w=u+v.\tag{2}
\]
Indeed, ordering and positivity rule out all other pairwise equalities among \(u,v,w,u+v,u+w\). When none of (2) holds, all six powers are distinct, so the product has weight six. We now follow all carries, including any subsequent cascades.

**Case I: \(u=v\).** The first carry, at exponent \(u\), leaves the five formal exponents
\[
 0,\quad u+1,\quad w,\quad 2u,\quad u+w.\tag{3}
\]
They contain a new coincidence precisely if \(u=1\) (because \(u+1=2u\)), or \(w=u+1\), or \(w=2u\). The resulting complete subcase computation is:

- For \(u=1\), \(w=2\) the weight is \(3\), \(w=3\) the weight is \(2\), and every \(w\ge4\) gives weight \(4\). For the last range, carrying the two coincident terms at exponent \(2\) to exponent \(3\) leaves exactly \(0,3,w,u+w\), all distinct.
- For \(u=2\), \(w=3\) the weight is \(2\), \(w=4\) the weight is \(4\), and all \(w\ge5\) give weight \(5\). At \(w=3\), the carries at exponents \(2,3,4,5\) leave only \(0,6\).
- For \(u\ge3\), \(w=u+1\) and \(w=2u\) each give exactly one new collision in (3), hence weight \(4\), while every other \(w>u\) gives weight \(5\). The two listed values of \(w\) are distinct for \(u\ge3\).

These are precisely families 1–3.

**Case II: \(u=w\).** Here \(v<u\), and the first carry at exponent \(u\) leaves
\[
 0,\quad v,\quad u+1,\quad u+v,\quad 2u.\tag{4}
\]
A second coincidence occurs exactly when \(v=1\), between \(u+1\) and \(u+v\). If \(v=1\) and \(u=2\), the resulting term at exponent \(u+2=4\) collides again with \(2u=4\), giving weight \(3\). For \(v=1\) and \(u\ge3\), there is no further collision and the weight is \(4\). For \(v\ge2\) it is \(5\). This gives family 4.

**Case III: \(w=u+v\) with \(u\ne v\).** Since \(v>0\), this case cannot overlap Case II. The first carry at exponent \(w\) leaves
\[
 0,\quad u,\quad v,\quad w+1,\quad u+w.\tag{5}
\]
As \(u\ne v\), another equality among these exponents is possible only when \(u=1\), making \(w+1=u+w\). Then \(v\ge2\), and carrying the equal pair to exponent \(w+2\) leaves four distinct positions \(0,1,v,w+2\). For every \(u\ne1\), the weight is \(5\). This is precisely family 5. The overlap Case I with \(u=v\) and \(w=u+v\) was already counted there.

The three cases exhaust (2), and all remaining triples have weight six. Consequently the listed five families are necessary and sufficient, and they are pairwise disjoint. \(\square\)

## Verification

The standalone `VERIFY.py` reproduces the exact carry-free product and computes its actual `int.bit_count()` for every triple \(1\le u,v<w\le80\). It checks the equivalence with the five listed parameter conditions for every triple and verifies the four exceptional lower-weight triples. It also checks a sample from each infinite family and rejects nearby nonmembers. Run `python3 VERIFY.py` using Python 3.8 or newer with `int.bit_count()` support (Python 3.8 users may replace it with `bin(n).count('1')`; as written, Python 3.10 or later is required). The exhaustive finite calculation is a reproducibility check; the unrestricted theorem is established by the carry argument above.

## Relationship to prior work

Kaneko and Stoll's *Products of integers with few nonzero digits* (initial arXiv version 2021-12-06) establishes broad bounds for weights \(2\) and \(3\), constructions showing unbounded behavior for weight \(4\), and a minimum-factor bound for weight \(4\) when **both** factor weights are at least \(3\). Their Section 2 and complete proofs in Sections 3–6 do not give the present exact description of the asymmetric factor-weight \((2,3)\) boundary. The five families here prove that both factors can be unbounded already at this boundary, and exhaust all such weight-four cases.

An earlier mathematical-record finding titled *Exact \((3,2,3)\) binary-weight product classification* determines the **weight-three** product class for these same factor weights. That finite weight-three classification is distinct from the infinite **weight-four** classification proved here and is not claimed as new. No conclusion about publication priority or independent verification is asserted.

## Limitations

The result is specific to the binary base, factor weights \(2\) and \(3\), and target product weight \(4\). It neither classifies other weight triples nor supplies a general bound for higher factor weights. The finite verification does not replace the infinite proof. Previously unindexed equivalent literature could exist.

## References

1. H. Kaneko and T. Stoll, *Products of integers with few nonzero digits*, arXiv:2112.03077, first posted 2021-12-06; *Uniform Distribution Theory* **17** (2022), 11–28, doi:10.2478/udt-2022-0006. Full text: https://arxiv.org/abs/2112.03077.
2. *Exact \((3,2,3)\) binary-weight product classification*, published mathematical-record summary (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-3-2-3-binary-weight-product-classification--28456ef398f9. Referenced solely to distinguish the already covered weight-three case.
