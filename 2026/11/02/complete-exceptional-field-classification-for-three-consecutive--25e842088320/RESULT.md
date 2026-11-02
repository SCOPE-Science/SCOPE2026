# Complete exceptional-field classification for three consecutive nonsquare cubes

## Finding

Let \(q\) be a prime power with \(q\equiv1\pmod6\), and let \(\mathbb F_q\) be the field with \(q\) elements. Write
\[
C_q=\{y\in\mathbb F_q^\times:y\text{ is a cube but not a square}\}
=\{y\in\mathbb F_q^\times:y^{(q-1)/6}=-1\}.
\]
There exists \(x\in\mathbb F_q\) such that \(x,x+1,x+2\in C_q\) **if and only if**
\[
q\notin E=\{7,13,19,25,31,37,43,49,61,67,73,79,97,103,109,121,127,
157,163,169,229,277,283,343,409,421,457,487,529,577,601,625,727,733,1399\}.
\]
The set \(E\) contains 28 primes and seven proper prime powers. Every field order \(q\ge105841\) in the stated congruence class admits such a triple by an analytic estimate; every smaller admissible field order is resolved by the included exact finite-field verifier.

## Assumptions and scope

A **consecutive triple** means \((x,x+1,x+2)\) in the additive structure of \(\mathbb F_q\); the three members are distinct because the characteristic is at least five. The property is invariant under a field isomorphism. Only prime powers \(q\equiv1\pmod6\) are considered, as an element can be simultaneously a non-square and a cube precisely when the cyclic multiplicative group has order divisible by six. A zero element is not counted as a cube in \(C_q\). The existence theorem does not count all witnesses or classify them into orbits.

The multiplicative characterization follows by choosing a generator \(g\) of \(\mathbb F_q^\times\): a cube that is not a square is \(g^{3(2k+1)}\); raising to \((q-1)/6\) gives \(-1\), and the converse follows because \(g^j\) maps to \(-1\) precisely when \(j\equiv3\pmod6\).

## Proof

**1. Character indicator.** Fix a multiplicative character \(\chi\) of order six, and for nonzero \(y\) define
\[
I(y)=\frac16\sum_{j=0}^{5}(-1)^j\chi(y)^j.
\]
The six-term geometric sum is one if \(\chi(y)=-1\) and zero otherwise. Hence for the number \(N(q)\) of desired starting points,
\[
216N(q)=\sum_{x\notin\{0,-1,-2\}}\ \sum_{a,b,c=0}^{5}
(-1)^{a+b+c}\chi(x)^a\chi(x+1)^b\chi(x+2)^c.
\]
The term \((a,b,c)=(0,0,0)\) contributes \(q-3\).

**2. Uniform character-sum bound.** For a nonzero exponent triple, let \(r\in\{1,2,3\}\) be the number of its nonzero components. Extending the corresponding sum to the entire field yields the sum of a nontrivial multiplicative character on a product of \(r\) *distinct* affine factors with exponents between one and five. For \(r=1\) the complete sum is zero, and for \(r=2\) and \(r=3\) the Weil bound gives respectively \(\sqrt q\) and \(2\sqrt q\). This applies because none of the nonzero exponents is divisible by six; thus the product is not a sixth power in \(\overline{\mathbb F}_q(X)\). Removing the excluded values \(0,-1,-2\) changes each complete sum by at most \(3-r\), since factors corresponding to the support already vanish at their own roots in the complete sum. There are \(15\) exponent triples with \(r=1\), \(75\) with \(r=2\), and \(125\) with \(r=3\). Consequently,
\[
\begin{aligned}
216N(q)&\ge(q-3)-15\cdot2-75(\sqrt q+1)-125\cdot2\sqrt q\\
&=q-108-325\sqrt q.
\end{aligned}
\]
For \(q\ge105841\), this is strictly positive. At the boundary the exact squared comparison is
\[
(105841-108)^2-325^2\cdot105841=11664>0,
\]
and the difference \(q-108-325\sqrt q\) increases thereafter. Thus every admissible \(q\ge105841\) has a triple.

**3. Exhaustive finite remainder.** To decide every smaller admissible prime power, execute the included standalone Python 3 file `verify_ns3.py`. It has no third-party dependencies or unverified file inputs. For every prime \(p<105841\) with \(p\equiv1\pmod6\), it examines successive \(a\in\{1,\ldots,p-3\}\) until finding a witness satisfying
\[
a^{(p-1)/6}\equiv(a+1)^{(p-1)/6}\equiv(a+2)^{(p-1)/6}\equiv-1\pmod p.
\]
If no witness exists, the loop has tested every possible starting point. The verifier constructs the complete list of proper prime powers \(q<105841\) with \(q\equiv1\pmod6\), and compares it with a supplied list of \(77\) explicit extension-field records. Every record specifies a monic defining polynomial, a candidate primitive element, and either a triple witness or an exception marker. It independently validates irreducibility by Rabin's finite-field criterion; it checks that the proposed generator has order \(q-1\); it then performs exact field exponentiation. Positive records are certified by evaluating their explicit witness. Negative records are certified by evaluating **every field element** as a possible triple start. The prime and prime-power portions together give exactly the displayed \(35\)-element list, with no further exceptional order below the cutoff. This proves both directions.

## Verification

Run `python3 verify_ns3.py` with a standard Python 3 interpreter. The reference execution produced:

```
VERIFY_OK primes=5037 extensions=77 exceptions=35 limit=105841
```

The verifier checks the completeness of the prime and extension-field ranges, validates all seven exceptional proper prime powers by exhaustive enumeration, and prints success only when the computed exceptional orders match \(E\) exactly. For nonexceptional fields it verifies a concrete witness, not just a count. The analytic bound, not the finite computation, proves the infinite tail. The checker is a reproducible finite certificate conditional only on exact standard integer arithmetic and its inspectable implementation; it is not an independent formal proof.

## Relationship to prior work

Cohen's 2026 paper proves a precise classification of *consecutive pairs* of non-square cubes; its Theorem 5.2 has six exceptional prime powers and its final Question 7.3 concerns *three* consecutive non-square non-primitive elements. Neither the pair classification nor that question gives the present triple classification. For example, \(q=31\) admits an NS3 pair but belongs to our triple exception list. The present NS3 requirement is stronger than the general NSNP condition; hence it does **not** resolve Cohen's question for every non-square non-primitive class.

The 1962 theorem of Lehmer, Lehmer, Mills and Selfridge classifies primes admitting *three consecutive cubic residues*, omitting the non-square restriction and proper prime powers. For example, their cubic-residue triple at \(p=97\) does not imply an NS3 triple: \(97\in E\). Gun, Luca, Rath, Sahu and Thangadurai prove sufficiently-large-prime existence of arbitrarily long strings of non-square non-primitive elements, without an exact NS3 exceptional-field list. Buell and Hudson study sequences in power-residue classes, an especially relevant older source; only abstract-level material was accessible in this review and overlapping coverage must remain a priority risk.

## Limitations

This is an exact **existence** classification for the one prescribed sixth-power coset, not a count of all triples or a classification of general NSNP triples. The finite cutoff is intentionally a sufficient analytic threshold, not claimed to be optimal. Published priority cannot be established from a finite search; the earlier Buell--Hudson work and other unindexed cyclotomic tables may imply parts of the answer. In particular, when \(q\equiv7\pmod{12}\), negation identifies the prescribed coset with the sixth-power subgroup, so older results about consecutive sixth powers merit specific independent comparison. No independent mathematical audit has been performed.

## References

1. S. D. Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429v1 (first posted 2026-04-23), Sections 1, 5 and 7, especially Theorem 5.2 and Question 7.3. https://arxiv.org/html/2604.21429v1
2. D. H. Lehmer, E. Lehmer, W. H. Mills and J. L. Selfridge, *Machine Proof of a Theorem on Cubic Residues*, Math. Comp. **16** (1962), 407–415, Theorem 1. https://www.cs.umd.edu/~gasarch/TOPICS/res/llms.pdf
3. S. Gun, F. Luca, P. Rath, B. Sahu and R. Thangadurai, *Distribution of residues modulo \(p\)*, Acta Arith. **129** (2007), 325–333, Theorem 1. https://www.impan.pl/shop/publication/transaction/download/product/83746
4. D. A. Buell and R. H. Hudson, *Sequences in power residue classes*, Internat. J. Math. Math. Sci. **9** (1986), 261–266, DOI: 10.1155/S0161171286000315 (abstract inspected; full text unavailable).
5. Standard multiplicative-character Weil bound for products of distinct affine factors (see Gun et al., Theorem 4 for the prime-field version, and Cohen, Section 2 for finite-field character-sum methods).
