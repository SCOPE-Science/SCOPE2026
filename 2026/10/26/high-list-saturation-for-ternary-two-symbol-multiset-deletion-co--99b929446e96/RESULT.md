# High-list saturation for ternary two-symbol multiset deletion codes

## Finding

For each integer \(n\ge4\), let
\[
\mathcal S_{n,3}=\{(x_0,x_1,x_2)\in\mathbb Z_{\ge0}^{3}:x_0+x_1+x_2=n\}.
\]
A code \(C\subseteq\mathcal S_{n,3}\) is \(L\)-list decodable after deletion to exactly two **unordered** surviving symbols if each two-element received multiset has at most \(L\) possible parents in \(C\). Write \(M_3(n,L;2)\) for the largest size of such a code.

**Theorem.** For all integers \(L\ge5\) and \(n\ge \lceil L/2\rceil+1\),
\[
M_3(n,L;2)=\left\lfloor\frac{3L}{2}\right\rfloor+6.
\]
For every even \(L\ge6\), any code meeting this bound contains all twelve length-\(n\) vectors with exactly one coordinate of multiplicity at least two. Every remaining codeword has exactly two coordinates of multiplicity at least two; each of the three monochromatic two-symbol received multisets has exactly \(L\) codeword parents.

The restriction on \(n\) is a sufficient uniform saturation condition, **not** an assertion that saturation begins there for every \(L\).

## Assumptions and scope

The alphabet is the labeled set \(\{0,1,2\}\), and messages are unordered multisets represented by multiplicity vectors \(x\). Precisely \(n-2\) symbols are deleted, leaving one of six unordered received pairs: \(00,11,22,01,02,12\). A received pair \(y\) is possible from \(x\) if and only if \(y_i\le x_i\) for all \(i\). The list bound counts **distinct source messages**, not deletion patterns. There are no probabilistic assumptions.

Call a coordinate \(i\) of \(x\) *heavy* if \(x_i\ge2\). The monochromatic received pair \(ii\) has \(x\) as a possible parent exactly when \(i\) is heavy.

## Proof

**Upper bound.** For \(n\ge4\), each \(x\in\mathcal S_{n,3}\) has at least one heavy coordinate, because three coordinates all at most one sum to at most three. Exactly twelve source vectors have precisely one heavy coordinate: for each choice of heavy coordinate \(i\), the other two coordinates independently take values zero or one, forcing \(x_i\) to be \(n,n-1\), or \(n-2\), all at least two.

Fix any list-\(L\) code \(C\) of size \(M\), and let \(T\le12\) be the number of codewords with exactly one heavy coordinate. The total number \(H\) of incidences between a codeword and a monochromatic received pair satisfies
\[
2M-T\le H
=\sum_{i=0}^{2}|\{x\in C:x_i\ge2\}|
\le3L.
\]
Consequently,
\[
M\le\left\lfloor\frac{3L+T}{2}\right\rfloor
\le\left\lfloor\frac{3L}{2}\right\rfloor+6.
\]
This bound applies to every \(n\ge4\), without the theorem's extra length restriction.

**Construction for \(L\ge6\).** Put \(d=L-4\ge2\), and take the twelve one-heavy vectors
\[
(n,0,0),\ (n-1,1,0),\ (n-1,0,1),\ (n-2,1,1)
\]
and all their coordinate permutations, counting each distinct vector once. Thus every symbol is heavy in exactly four of the twelve vectors. Every mixed received pair \(ij\) belongs to exactly five: the two near-pure vectors with their heavy coordinates at \(i\) and \(j\), and the three one-heavy full-support vectors.

For each edge \(ij\) among \(01,02,12\), add \(t_{ij}\) distinct two-heavy vectors supported on that edge, with
\[
t_{01}=t_{12}=\lfloor d/2\rfloor,\qquad
t_{02}=\lceil d/2\rceil.
\]
Explicitly, on edge \(ij\) take \(x_i=a,\ x_j=n-a,\ x_k=0\) for every integer \(2\le a\le t_{ij}+1\), where \(k\) is the remaining symbol. Our length hypothesis implies
\[
n-3\ge\lceil d/2\rceil,
\]
so these are distinct valid two-heavy vectors. The new monochromatic loads increase at each symbol by at most \(d\): the respective edge-degree increments are \(d,d\) and \(d\) when \(d\) is even, and \(d,d-1,d\) when \(d\) is odd (after arranging the coordinate labels appropriately). Hence all monochromatic loads are at most \(4+d=L\).

A two-heavy edge word adds a parent only to the corresponding mixed received pair \(ij\). Its total load becomes \(5+t_{ij}\). Since \(\lceil d/2\rceil\le d-1\) for all \(d\ge2\), this is at most \(5+d-1=L\). All six received-pair loads therefore satisfy the list bound.

The code has
\[
12+2\lfloor d/2\rfloor+\lceil d/2\rceil
=12+\lfloor3d/2\rfloor
=\lfloor3L/2\rfloor+6
\]
distinct codewords, proving the desired equality for \(L\ge6\).

**The boundary case \(L=5\).** At source length \(n=4\), the full simplex \(\mathcal S_{4,3}\) has fifteen words, and each of the six received pairs has exactly six parents. Remove the two words \((2,2,0)\) and \((1,1,2)\). Their two received-pair signatures together cover all six pairs: the former covers \(00,11,01\), and the latter covers \(22,01,02,12\). Thus the remaining thirteen words form a five-list code, attaining \(\lfloor15/2\rfloor+6=13\).

This thirteen-word code lifts to every \(n\ge4\) without changing received-pair incidences: map \(x\) to \(F(x)=x+e_i\), where \(i\) is the smallest-index coordinate attaining the maximum in \(x\). Since every vector at length at least four has a heavy coordinate, increasing a maximal coordinate does not change which coordinates are positive or heavy, so no two-symbol receive signature changes. Moreover \(F\) is injective. Indeed, if distinct \(x,y\) had \(F(x)=F(y)=z\), with different selected coordinates \(i,j\), maximality would give simultaneously \(z_i-1\ge z_j\) and \(z_j-1\ge z_i\), a contradiction. Repeated lifting proves the five-list case.

**Rigidity for even \(L\).** Let \(L\ge6\) be even and \(M=3L/2+6\). Equality in the upper-bound chain gives
\[
3L+12=2M\le H+T\le3L+T\le3L+12.
\]
Every inequality is equality. Therefore \(T=12\), so the code includes **every** one-heavy vector. Also \(H=3L\), so every monochromatic list has exactly \(L\) parents. Finally, each other codeword must contribute exactly two monochromatic incidences; no selected word may have three heavy coordinates. These are necessary properties of all optimizers, and no uniqueness beyond them is claimed.

## Verification

The complete standard-library checker `CHECKER.py` constructs the codes, computes the six received-pair signatures directly from coordinate comparisons, checks distinctness and loads, and verifies the even-list structural assertions. It checked \(L=5,\ldots,70\) at three consecutive permitted lengths (198 cases), and independently tested the signature-preserving lift on all 9,119 vectors of lengths four through thirty-six. It also enumerated all \(2^{15}\) subcodes of \(\mathcal S_{4,3}\), obtaining exact list-capacity optima \(3,6,9,11,13,15,15\) for list bounds one through seven.

These are finite checks only. The universal capacity formula follows from the symbolic incidence inequality and the constructions above, not from experimental extrapolation. Reproduce by running `python CHECKER.py` with Python 3.

## Relationship to prior work

Kreindel, Barouch Essayag, and Zabokritskiy develop multiset deletion codes and determine exact **unique-decoding** bounds in the high-deletion regime, including their theorem for two surviving symbols. Their March 2026 paper studies deletion-ball geometry and packing bounds, again for unique decoding. Neither result specifies the maximum **bounded list size** for arbitrary \(L\ge5\) with three symbols and two survivors.

A related previously recorded special case determines the ternary four-list capacity \(11\) for \(n\ge4\), whereas the present theorem determines the whole high-list family \(L\ge5\). Previously recorded broader-alphabet results for \(2\le L\le k\) only address \(L\le2\) when the survivor count is \(k=2\). The present threshold regime is outside both ranges.

The exact coefficient \(3/2\) and six-unit correction arise from bounding the twelve exceptional one-heavy codewords and balancing the remaining two-heavy edge classes; neither follows from the unique-decoding pairwise disjointness criterion.

## Limitations

The theorem gives a sufficient uniform source length \(n\ge\lceil L/2\rceil+1\) for its formula and does not claim this is the least possible \(n\). It makes no assertion for \(L<5\), for shorter lengths, for other alphabet sizes, or for a different number of surviving symbols. Even-list equality forces structural conditions but is not a full enumeration of all optimal codes. No claim is made about unindexed or unpublished equivalent work. Independent mathematical review has not been performed.

## References

1. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636 (first publicly available 9 January 2026), https://arxiv.org/abs/2601.05636 .
2. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (first publicly available 18 March 2026), https://arxiv.org/abs/2603.18322 .
