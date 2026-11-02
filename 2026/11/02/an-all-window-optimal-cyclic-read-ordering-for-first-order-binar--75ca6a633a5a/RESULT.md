# An all-window optimal cyclic read ordering for first-order binary Reed–Muller codes

## Finding

Let \(m\ge2\) be an integer and \(N=2^m\). Regard the first-order binary Reed–Muller code \(\mathrm{RM}_2(1,m)\) as the evaluations of all affine Boolean functions on \(\mathbb F_{2^m}\). For a cyclic ordering \(\pi\) of its \(N\) coordinate labels, let \(d_b(\pi)\) be the minimum cyclic \(b\)-symbol distance for an overlapping window of width \(1\le b\le N\). Then

\[
\max_{\pi}d_b(\pi)=
\begin{cases}
2^m-2^{m-b},&1\le b\le m,\\
2^m,&m+1\le b\le2^m.
\end{cases}
\]

One ordering realizes **every one of these optima simultaneously**: if \(g\) is any primitive element of \(\mathbb F_{2^m}\), use the coordinates
\[
(0,1,g,g^2,\ldots,g^{2^m-2}).
\]
Thus the coordinate-ordering optimum is an exact hierarchy, not a collection of unrelated independent optima. In particular, this ordering reaches full cyclic \(b\)-symbol distance already when \(b=m+1\).

## Assumptions and scope

The field is binary of cardinality \(N=2^m\), with \(m\ge2\). The code comprises all vectors
\[
\left(\operatorname{Tr}(a x_j)+c\right)_{j=0}^{N-1},\qquad a\in\mathbb F_{2^m},\quad c\in\mathbb F_2,
\]
where \(x_0,\ldots,x_{N-1}\) are each field element exactly once. Here \(\operatorname{Tr}=\operatorname{Tr}_{\mathbb F_{2^m}/\mathbb F_2}\), and the trace pairing is nondegenerate. The code is linear of parameters \([2^m,m+1,2^{m-1}]_2\). An indexed circular codeword \(v\) has cyclic \(b\)-weight
\[
w_b(v)=\#\{j\in\mathbb Z/N\mathbb Z:(v_j,v_{j+1},\ldots,v_{j+b-1})\ne(0,\ldots,0)\}.
\]
The minimum distance \(d_b\) is the minimum of \(w_b(v)\) over **nonzero** codewords. All windows wrap around cyclically; no window exceeds \(N\) coordinates. A coordinate permutation changes the circular read channel but does not change the underlying ordinary Hamming code.

## Proof

**1. Universal upper bound for arbitrary orderings.** Fix \(1\le b\le m\), and put \(t=2^{m-b}\). Any \(b\) distinct coordinate labels impose at most \(b\) homogeneous linear constraints on the \(m+1\) affine-function coefficients. Therefore at least \(2^{m+1-b}=2t\) affine functions vanish at that particular ordered window, including the zero function. At least \(2t-1\) *nonzero* codewords consequently have an all-zero window at each of the \(N\) starting positions.

Count incidences \((\text{nonzero affine word},\text{all-zero width-}b\text{ window})\). There are at least \(N(2t-1)\) incidences. If every one of the \(2N-1\) nonzero words had at most \(t-1\) all-zero windows, there would be at most \((2N-1)(t-1)\) incidences, contradicting
\[
N(2t-1)-(2N-1)(t-1)=N+t-1>0.
\]
Hence some nonzero codeword has at least \(t\) all-zero width-\(b\) windows. Its \(b\)-weight is at most \(N-t\). This proves \(d_b(\pi)\le N-2^{m-b}\) for **every** permutation \(\pi\). For \(b\ge m+1\), the trivial upper bound is \(d_b(\pi)\le N\).

**2. Linear trace sequence on nonzero field elements.** Fix a primitive \(g\), set \(L=N-1\), and first order just the nonzero labels as \((1,g,\ldots,g^{L-1})\). Fix \(a\ne0\), and define its cyclic binary trace sequence by \(u_j=\operatorname{Tr}(a g^j)\), where indices are modulo \(L\). For every \(1\le b\le m\), the \(b\) linear functionals
\[
x\longmapsto \operatorname{Tr}(x),\ \operatorname{Tr}(gx),\ldots,\operatorname{Tr}(g^{b-1}x)
\]
are independent: a nontrivial dependence would imply a polynomial of degree below \(m\) annihilates \(g\), contradicting the degree of its minimal polynomial. Thus each prescribed binary \(b\)-tuple occurs exactly \(2^{m-b}\) times as \(x\) ranges over the **whole** field. When \(x=0\) is deleted, the all-zero tuple occurs exactly \(t-1\) times, while each nonzero tuple, in particular the all-one tuple, occurs exactly \(t\) times. As \(a g^j\) ranges over all nonzero field elements, these are the precise cyclic length-\(L\) pattern counts in \(u\).

**3. Insert the zero coordinate.** Insert the field element \(0\) at the cyclic cut between \(g^{L-1}\) and \(1\). For affine functions with \(a\ne0,c=0\), this inserts a **zero** symbol into \(u\). Inserting one zero into a circular word can increase its number of all-zero consecutive length-\(b\) windows by at most one: an existing cyclic zero-run containing the insertion grows by one, with at most one additional length-\(b\) subwindow. Therefore the number of all-zero windows is at most \((t-1)+1=t\).

For affine functions with \(a\ne0,c=1\), the nonzero-field word is the bitwise complement of \(u\) and already has exactly \(t\) all-zero \(b\)-windows. The inserted coordinate is a **one**. Inserting a one cannot create an all-zero window, so the number remains at most \(t\). The remaining nonzero affine word is the constant-one word and has no all-zero windows. Thus **all** nonzero codewords under the displayed ordering have at most \(t\) all-zero width-\(b\) windows, or \(w_b\ge N-t\). Combined with Step 1, this gives equality simultaneously for every \(1\le b\le m\).

**4. Full read distance from width \(m+1\).** For a nonzero linear trace word \(u\) on the nonzero field elements, Step 2 at width \(m\) says there are no \(m\) consecutive zero symbols: the all-zero tuple occurs \(2^{m-m}-1=0\) times. Inserting one zero can create at most a run of \(m\) zeros, never a run of \(m+1\) zeros.

Its complement cannot contain \(m+1\) consecutive zeros either. Indeed, write the irreducible degree-\(m\) polynomial of \(g\) as \(p(X)=X^m+\sum_{i=0}^{m-1}p_i X^i\). Since \(m\ge2\), the element \(1\) is not a root, and \(p(1)=1\), so \(\sum_i p_i=0\) in \(\mathbb F_2\). The trace sequence obeys
\[
u_{j+m}=\sum_{i=0}^{m-1}p_i u_{j+i}.
\]
If \(m\) consecutive trace values are all one, the next is zero; hence \(m+1\) consecutive ones cannot occur. The complement thus has no \(m+1\) zero-run before insertion; inserting a one cannot create one. The constant-one word has no zeros. Every nonzero affine codeword in the full \(N\)-coordinate construction has no \(m+1\) consecutive zeros. Therefore every width-\(m+1\) cyclic window is nonzero, giving \(d_{m+1}=N\), and the same holds for all larger widths. This proves the theorem.

## Verification

The accompanying stand-alone Python 3 program `verify.py` constructs finite fields from specified primitive binary polynomials, evaluates every affine Boolean word directly, and counts nonzero cyclic windows rather than invoking the proof's trace-incidence argument. It checks all widths \(1\le b\le m+1\) for every \(2\le m\le8\), including every one of the \(2^{m+1}\) affine functions at each dimension. Its independent dimension-three test exhausts all \(7!=5040\) cyclic orderings with coordinate \(0\) anchored. It prints `VERIFY_OK` upon success.

For example, for dimensions \(m=3,4,5\), the full optimal profiles through width \(m+1\) are respectively \((4,6,7,8)\), \((8,12,14,15,16)\), and \((16,24,28,30,31,32)\). These finite tests are corroboration; the arbitrary-dimensional assertion follows from Steps 1–4.

Run locally with `python3 verify.py` in the extracted package. No data files, third-party modules, network service or external calculation certificates are required.

## Relationship to prior work

The cyclic \(b\)-symbol metric and general Singleton-type bounds are developed in Ding–Zhang–Ge (2016), including construction results for other families of codes. Zhu–Shi (2022) derive \(b\)-symbol distributions for irreducible cyclic codes, which include related nonzero-field trace/simplex codes of length \(2^m-1\). These results do not, in their inspected statements, optimize the full \(2^m\)-coordinate first-order Reed–Muller code over arbitrary coordinate permutations.

Pan–Ling–Liu (2023), Theorem 4.6, compute the Reed–Muller cyclic \(b\)-symbol distance for their explicitly **lexicographic evaluation ordering**. For first-order binary codes it is \(\min(2^{m-1}+b-1,2^m)\). The coordinate reordering proved here can be strictly better; for instance, at \(m=4,b=3\), the published lexicographic value is \(10\), whereas the sharp coordinate-optimized value is \(14\). Consequently that fixed-order result does not imply the permutation optimum.

A known unpunctured simplex pair-distance result for length \(2^m-1\), a prior one-coordinate-punctured simplex pair-distance optimization, and a finite eight-coordinate extended-Hamming pair-spectrum classification cover related special cases. They do **not** give the all-width, all-dimensional optimum for the extended affine evaluation code. In particular, the principal additional content here is the simultaneous \(b\ge3\) exact hierarchy and the full-distance cutoff, not a claim of novelty for those previously established pair cases. The formula coincides numerically with the generalized Hamming weight hierarchy of this code, but that numerical agreement alone does not establish coordinate-permutation attainability; Steps 1–4 supply that construction and upper bound.

## Limitations

The theorem is specific to first-order **binary** Reed–Muller evaluation codes, circular overlapping windows, and freedom to permute all coordinates. It does not characterize all optimal orderings, give generalized results for higher-order Reed–Muller codes or nonbinary alphabets, or imply a physical storage performance guarantee. Verification through dimension eight is finite, not a substitute for the proof. An equivalent theorem may exist in unindexed literature; historical priority should be independently checked.

## References

1. B. Ding, T. Zhang, and G. Ge, *Maximum Distance Separable Codes for b-Symbol Read Channels*, arXiv:1609.09236v1, first posted 2016-09-29. https://arxiv.org/abs/1609.09236
2. H. Zhu and M. Shi, *The b-symbol weight distribution of irreducible cyclic codes and related consequences*, arXiv:2203.11567v1, first posted 2022-03-22. https://arxiv.org/abs/2203.11567
3. X. Pan, S. Ling, and H. Liu, *New bounds for b-Symbol Distances of Matrix Product Codes*, arXiv:2309.08920v1, first posted 2023-09-16; Theorem 4.6 and the lexicographic evaluation order in Section 4. https://arxiv.org/abs/2309.08920
