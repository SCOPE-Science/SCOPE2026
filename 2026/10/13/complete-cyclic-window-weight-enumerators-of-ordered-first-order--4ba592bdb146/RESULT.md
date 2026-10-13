# Complete cyclic window-weight enumerators of ordered first-order binary Reed–Muller codes

## Finding

For every integer \(m\ge1\), the cyclic \(b\)-symbol weight enumerator of the binary first-order Reed–Muller code in **increasing-binary-integer evaluation order** is given explicitly below for every \(1\le b\le 2^m\). This describes the number of codewords of each possible weight, not merely the minimum weight.

Write \(N=2^m\). For \(0\le t<m\), let \(B=2^t\), \(q=m-t-1\), and \(H=2^q\). Set \(J_0=\{0\}\) and \(\mu_0(0)=1\). For \(q\ge1\), let \(J_q=\{0,1,\ldots,2^{q-1}\}\), with \(\mu_q(0)=\mu_q(2^{q-1})=1\) and \(\mu_q(j)=2\) at the intervening integers. For real \(u\), write \(u_+=\max\{u,0\}\), and define

\[
F_{m,b}(t,j)=N-(H-2j)(B-b+1)_+-j(2B-b+1)_+.
\]

Then the complete enumerator, with equal exponents combined in the polynomial as usual, is

\[
\boxed{W_{m,b}(z)=1+z^N+\sum_{t=0}^{m-1}\sum_{j\in J_q}2\mu_q(j)z^{F_{m,b}(t,j)}.}
\]

In particular, a simple closed form holds for the symbol-pair channel (\(b=2\)) at every \(m\ge1\):

\[
W_{m,2}(z)=1+4\sum_{r=N/2+1}^{N-1}z^r+3z^N.
\]

The exact minimum nonzero \(b\)-symbol weight is \(\min\{N,N/2+b-1\}\); this last corollary follows from the zero-run structure and is included as a consistency consequence, not as an independently claimed coding bound.

## Assumptions and scope

The code is \(\operatorname{RM}(1,m)=\{(f(0),\ldots,f(N-1)):f(j)=c+\sum_{i=0}^{m-1}a_i\operatorname{bit}_i(j)\pmod2,\ a_i,c\in\{0,1\}\}\), where \(\operatorname{bit}_0\) is the least significant bit. The order of the \(N\) evaluation positions is fixed: \(j=0,1,\ldots,N-1\) in ordinary binary-integer order. The cyclic \(b\)-weight counts start indices whose \(b\) consecutive, cyclically wrapped symbols are not all zero. Arbitrary coordinate permutations need not preserve this metric or the enumerator. No claim concerns higher-order Reed–Muller codes, other coordinate orders, or nonbinary alphabets.

## Proof

**Step 1: canonical block decomposition.** The two constant functions contribute \(1\) and \(z^N\). For a nonconstant affine Boolean function let \(t\) be the least index with \(a_t=1\). Each consecutive block of \(B=2^t\) evaluations is constant, and consecutive pairs of such blocks are \((g(s),1-g(s))\), with \(s\) read cyclically modulo \(H=2^{m-t-1}\) and \(g(s)=c+\sum_{i=t+1}^{m-1}a_i\operatorname{bit}_{i-t-1}(s)\pmod2\).

**Step 2: classify the cyclic zero runs.** Among the \(2H\) blocks, exactly \(H\) are zero blocks. A pair-boundary joins two zero blocks precisely when \(g(s)=1\) and \(g(s+1)=0\). Write \(j\) for the number of cyclic \(1\)-to-\(0\) transitions in \(g\). There are exactly \(j\) zero runs of length \(2B\), and \(H-2j\) of length \(B\). This also holds for \(H=1\), when \(j=0\). Thus the number of cyclic all-zero \(b\)-windows is

\[
(H-2j)(B-b+1)_++j(2B-b+1)_+,
\]

proving the claimed weight formula for each fixed \(t,j\).

**Step 3: count transition parameters without enumeration.** For \(q\ge1\), put \(d_i=a_{t+1+i}\) for \(0\le i<q\), and write \(u_h=d_0+\cdots+d_h\pmod2\) for \(0\le h<q\). The linear map \((d_i)\mapsto(u_h)\) is invertible over \(\mathbb F_2\). Among the increments \(s\to s+1\) for \(0\le s<H-1\), exactly \(2^{q-h-1}\) have binary carry length \(h+1\), hence toggle \(g\) by \(u_h\). The cyclic closing increment \(H-1\to0\) toggles by \(u_{q-1}\). Therefore the number of cyclic changes is

\[
2j=\sum_{h=0}^{q-1}2^{q-h-1}u_h+u_{q-1}=v+(v\bmod2),
\]

where \(v=\sum_{h=0}^{q-1}2^{q-h-1}u_h\) runs bijectively over \(\{0,\ldots,2^q-1\}\). Hence \(j=\lceil v/2\rceil\). Its multiplicity is one at \(j=0\) and \(j=2^{q-1}\), and two at every strictly intermediate \(j\). For \(q=0\) there is one empty coefficient vector with \(j=0\). Independently choosing \(c\in\{0,1\}\) multiplies every multiplicity by two. Summing over the unique least nonzero coefficient index \(t\) yields the enumerator.

**Step 4: consequences.** For \(b=2\), any nonconstant affine word has \(N/2\) zero symbols. Each zero run removes one adjacent zero pair, hence its pair weight is \(N/2\) plus its number of zero runs, namely \(N/2+H-j\). As \(t\) varies, \(H\) traverses \(1,2,4,\ldots,N/2\). For a fixed \(H\), the weights form the integer interval from \(N/2+H/2\) through \(N/2+H\) when \(H\ge2\), with multiplicity two at both endpoints and four in the interior; for \(H=1\), the sole weight \(N/2+1\) has multiplicity two. Adjacent power-of-two intervals share their endpoint, contributing two plus two, while every other interior weight already has multiplicity four. At weight \(N\) the last endpoint contributes two and the constant-one word contributes one, giving coefficient three. For general \(b\), every nonconstant word has exactly \(N/2\) zero positions, so it has at most \((N/2-b+1)_+\) all-zero cyclic \(b\)-windows: splitting a fixed number of zero positions into more than one run cannot increase the count. The word \(0^{N/2}1^{N/2}\) is in the code and attains the bound. Thus its weight \(\min\{N,N/2+b-1\}\) is minimal among nonzero codewords.

## Verification

Run `python3 verify.py` with Python 3.10 or later and no dependencies. The program computes the displayed polynomial directly from its finite sums, and independently enumerates all \(2^{m+1}\) affine truth tables in natural position order and all cyclic windows for each \(1\le m\le8\) and \(1\le b\le2^m\). It compares exact integral coefficient maps, verifies total multiplicity and the stated minimum-distance and pair-spectrum consequences. Representative test: \(W_{3,2}(z)=1+4z^5+4z^6+4z^7+3z^8\). These computations are independent finite checks, whereas the proof above establishes all \(m,b\).

## Relationship to prior work

Shi, Zhu and Helleseth (2021, arXiv:2109.13764), Theorem 2, express general cyclic \(b\)-symbol weights in terms of zero-run counts and explicitly identify determining run distributions for special irreducible cyclic/simplex codes. Their conclusion describes determining further special-code distributions as a research direction. The present result derives the **complete zero-run multiplicity law and entire \(b\)-symbol weight enumerator** for the differently ordered affine-evaluation Reed–Muller family; the general run identity alone does not imply that law.

Luo, Ezerman, Güneri, Ling and Özbudak (2024, arXiv:2401.04941) prove a \(b\)-symbol Griesmer bound and construct optimal linear-code families, including extensions of cyclic codes. Their length-\(2^m\) extended-cyclic construction in Theorem 7 uses a primitive-field-element coordinate order, and its minimum pair weight is six at \(m=3\), whereas the increasing-integer-order code here has minimum pair weight five. Thus code-equivalent Hadamard/Reed–Muller descriptions cannot transfer these cyclic metric statements by arbitrary position permutation, and Theorem 7 does not state this ordered enumerator. Classical Hamming weight distributions do not determine cyclic window weights: at \(m=3\), the nonconstant affine words all have Hamming weight four, yet their symbol-pair weights range from five through eight.

## Limitations

The formula is **coordinate-order dependent**. Neither an arbitrary generator-matrix column ordering nor code equivalence preserving only Hamming distance preserves this conclusion. The argument is for the binary first-order code only; it does not imply minimum \(b\)-weight optimality against all codes of comparable size. An equivalent, unindexed earlier computation remains a priority risk.

## References

1. M. Shi, H. Zhu, T. Helleseth, *The connections among Hamming metric, \(b\)-symbol metric, and \(r\)-th generalized Hamming metric*, arXiv:2109.13764v1 (28 September 2021), https://arxiv.org/abs/2109.13764.
2. G. Luo, M. F. Ezerman, C. Güneri, S. Ling, F. Özbudak, *Griesmer Bound and Constructions of Linear Codes in \(b\)-Symbol Metric*, arXiv:2401.04941v1 (10 January 2024), https://arxiv.org/abs/2401.04941.
