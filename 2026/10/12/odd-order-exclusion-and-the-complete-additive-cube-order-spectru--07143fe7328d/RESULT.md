# Odd-order exclusion and the complete additive-cube order spectrum in base four

## Finding

For every **even integer** \(q\ge 2\), let \(s_q(j)\) be the sum of the base-\(q\) digits of the nonnegative integer \(j\), and let \(u_q(j)\in\{0,\ldots,q-1\}\) be the residue \(s_q(j)\bmod q\). A length-\(3n\) factor is an **additive cube of order** \(n\ge1\) when its three consecutive length-\(n\) blocks have equal ordinary integer letter sums.

**Theorem.** No \(u_q\) with even \(q\) contains an additive cube of odd order. For \(q=4\), the converse is exact: an additive cube of order \(n\ge1\) occurs if and only if \(n\) is even. Hence the complete order spectrum of additive cubes of \(u_4\) is \(\{2,4,6,\ldots\}\). Every cube produced below has each of its three block sums equal to \(3n/2\).

## Assumptions and scope

All letter sums are ordinary sums in the integers, not sums modulo \(q\). The word \(u_q\) is indexed starting at zero and is the generalized Thue–Morse fixed point of the cyclic length-\(q\) substitution, in the normalization \(u_q(qj+r)=(u_q(j)+r)\bmod q\) for \(0\le r<q\). The theorem does not assert the existence of even-order additive cubes for every even base \(q>4\). It does completely classify possible orders for base four and excludes every odd order for all even bases.

For explicit constructions write \(H_q(N)=2\sum_{i=0}^{N-1}u_q(i)-(q-1)N\), with \(H_q(0)=0\). A factor beginning at \(a\) consists of three equal-sum blocks of length \(n\) precisely when the four integers \(H_q(a+jn)\), for \(j=0,1,2,3\), form an arithmetic progression.

## Proof

**Step 1 — the universal parity obstruction.** For even \(q\), every pair of indices \(2j,2j+1\) belongs to one aligned length-\(q\) substitution block because \(2j\bmod q\) is even. The corresponding letters are successive residues modulo even \(q\), so they have opposite parity and their sum is odd. Consequently
\[
H_q(2j+2)-H_q(2j)=2\bigl(u_q(2j)+u_q(2j+1)-(q-1)\bigr)\equiv0\pmod4.
\]
Since \(H_q(0)=0\), every height at an even index is a multiple of four. Furthermore \(H_q(N)\equiv N\pmod2\), because \(q-1\) is odd.

Suppose an additive cube has odd order \(n\) and begins at \(a\). The four heights at \(a,a+n,a+2n,a+3n\) form an arithmetic progression with difference \(\Delta\). Since \(n\) is odd, its consecutive heights have opposite parities, so \(\Delta\) is odd. Among the four endpoints, the two of even index are exactly two steps apart; their heights are each divisible by four. Thus \(2\Delta\equiv0\pmod4\), contradicting that \(\Delta\) is odd. No odd-order additive cube exists for any even base.

**Step 2 — base-four heights.** A complete aligned length-four block of \(u_4\) is a cyclic permutation of \(0,1,2,3\), hence its sum is six and
\[
H_4(4j)=0\quad(j\ge0).
\]
For an endpoint of the form \(4j+2\), put \(x=u_4(j)\). Its first two digits after the block boundary are \(x\) and \((x+1)\bmod4\). Therefore
\[
H_4(4j+2)=2\bigl(x+((x+1)\bmod4)\bigr)-6
=\begin{cases}-4,&x=0,\\0,&x=1\text{ or }x=3,\\4,&x=2.\end{cases}
\]
In particular \(H_4(4j+2)=0\) whenever \(u_4(j)\) is odd.

**Step 3 — orders divisible by four.** If \(4\mid n\), choose the starting index \(a=0\). All four endpoints \(0,n,2n,3n\) are multiples of four and have height zero. Thus the three length-\(n\) block sums all equal \(3n/2\).

**Step 4 — orders congruent to two modulo four.** Let \(n=4v+2\) with \(v\ge0\), and put \(m=2v+1=n/2\). Choose any sufficiently large positive integer \(h\) such that \(4^h>m+v\) and \(3h-s_4(m-1)\) is odd. There are infinitely many such \(h\), since increasing \(h\) changes the latter parity. Set
\[
k=4^h-m>v,\qquad a=4(k-v)\ge0.
\]
The base-four digit-complement identity
\[
s_4(4^h-m)=3h-s_4(m-1)
\]
shows that \(u_4(k)\) is odd. Also \(k+m=4^h\) implies \(u_4(k+m)=1\), which is odd. The four endpoints of the candidate additive cube are
\[
a=4(k-v),\quad a+n=4k+2,\quad
 a+2n=4(k+v+1),\quad a+3n=4(k+m)+2.
\]
The first and third heights are zero by Step 2 at multiples of four; the second and fourth heights are zero by the odd-digit cases of Step 2. Thus all four heights are equal, and the three successive length-\(n\) block sums are equal to \(3n/2\). This construction works for every positive \(n\equiv2\pmod4\). Together with Steps 1 and 3, this proves the theorem.

## Verification

The accompanying standalone `check_base4_additive_cubes.py` additionally checks the base-\(q\) recurrence and height congruences for even bases from two through sixteen; computes base-four heights from explicit digit sums; tests the absence of odd-order cubes in a large finite prefix; checks all asserted explicit witnesses through order 120 against the original digits; and checks the construction for all positive even orders through 20000 using digit arithmetic. Run it with `python check_base4_additive_cubes.py`. Its observed output is recorded in `CHECK_OUTPUT.txt`.

These finite tests are consistency checks rather than proofs of the unbounded assertions. The all-orders theorem is proved above by parity and the explicit base-four digit-complement construction.

## Relationship to prior work

Popoli, Shallit and Stipulanti introduce and analyze additive word complexity, including generalized Thue–Morse examples and questions about additive powers. Their automatic-sequence and bounded-additive-complexity results guarantee the existence of additive powers at some block lengths; they do not imply which block lengths occur individually. In particular, their ternary generalized Thue–Morse analysis differs from the even-alphabet parity obstruction here. Chen and Wen determine Abelian complexity and individual-factor Parikh vectors of generalized Thue–Morse words; those single-factor statistics do not by themselves determine when three consecutive factors have the same integer sum. The result here classifies all additive-cube orders for the first nonbinary even base and supplies a universal prohibition for every even base.

## Limitations

No claim is made for odd bases, for additive powers with four or more blocks, or for which even orders necessarily occur in bases six and above. The existence of an unindexed earlier equivalent derivation cannot be entirely excluded by database and literature searches. No independent scientific validation is asserted.

## References

1. Pierre Popoli, Jeffrey Shallit and Manon Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1 (first public 2024-10-03); especially generalized Thue–Morse discussion and additive-power results. https://arxiv.org/abs/2410.02409
2. Jin Chen and Zhixiong Wen, *On the abelian complexity of generalized Thue–Morse sequences*, arXiv:1809.06554 (2018); generalized Thue–Morse factor Parikh vectors. https://arxiv.org/abs/1809.06554
