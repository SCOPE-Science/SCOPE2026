# Exact Sierpiński domination for cycles of length one modulo three

## Finding

Let \(n\ge3\) and \(k\ge1\) be integers. For the Sierpiński product of a cycle of order \(n\) with a cycle of order \(3k+1\), minimized over every connecting map, the domination number is
\[
\gamma_{\mathrm S}(C_n,C_{3k+1})=kn+\varepsilon(n,k),
\]
where \(\varepsilon(n,k)\in\{0,1\}\), with \(\varepsilon(n,k)=0\) precisely in the following three mutually exclusive cases:

1. \(k=1\) and \(4\mid n\);
2. \(k=2\) and \(n\notin\{3,5,6,10\}\);
3. \(k\ge3\) and \(n\notin\{3,6\}\).

In every other case \(\varepsilon(n,k)=1\). Thus the two possibilities established in the foundational domination paper are resolved for **every** cycle length in this residue class, including the exceptional short cycles. An exact equality criterion, formulated as a closed walk with prescribed steps, is proved below.

## Assumptions and scope

All graphs are finite, undirected and simple. Write \(\mathbb Z_r\) for the cyclic group of order \(r\), and put \(m=3k+1\). Given any map \(f:\mathbb Z_n\to\mathbb Z_m\), the Sierpiński product \(C_n\otimes_f C_m\) has vertex set \(\mathbb Z_n\times\mathbb Z_m\). Its edges are the cycle edges within every layer \(\{i\}\times\mathbb Z_m\), and exactly one connecting edge
\[
\big\{(i,f(i+1)),(i+1,f(i))\big\}
\]
for each \(i\in\mathbb Z_n\). The domination number \(\gamma\) uses closed neighborhoods. By definition,
\[
\gamma_{\mathrm S}(C_n,C_m)=\min_{f:\mathbb Z_n\to\mathbb Z_m}\gamma(C_n\otimes_f C_m).
\]
This product is not the Cartesian product and is not the usual iterated Sierpiński graph. All indices and second coordinates below are reduced modulo their corresponding cycle orders.

## Proof

**1. A layer bound and rigidity at equality.** Let \(D\) dominate \(C_n\otimes_f C_m\), and let \(D_i=D\cap(\{i\}\times\mathbb Z_m)\). A vertex of \(D_i\) dominates at most three vertices inside layer \(i\), and at most two vertices of that layer can be dominated from other layers (the endpoints of its two connecting edges). If \(|D_i|\le k-1\), at most \(3(k-1)+2=3k-1<m\) vertices of that layer are dominated, a contradiction. Hence \(|D_i|\ge k\) for every \(i\), and \(|D|\ge kn\).

Assume \(|D|=kn\). Then every \(|D_i|=k\); the internal closed neighborhoods of these \(k\) vertices leave at least one vertex in layer \(i\) undominated internally. There are \(n\) layers and \(n\) connecting edges, and a connecting edge can dominate at most one internally undominated endpoint (only if its opposite endpoint is selected). Therefore every layer has exactly one such hole, every connecting edge covers exactly one hole, and all \(k\) internal closed neighborhoods are pairwise disjoint. If the hole in layer \(i\) has second coordinate \(h_i\), then \(D_i\) is forced to be
\[
\{(i,h_i+2+3j):0\le j<k\}. \tag{1}
\]
Indeed, deleting the hole leaves a path on \(3k\) vertices, which must be dominated by \(k\) disjoint closed neighborhoods of size three. The first vertex of that path forces its second vertex into \(D_i\): choosing the first would leave \(3k-2\) vertices for only \(k-1\) centers, which can cover at most \(3k-3\). Repeating this argument every three vertices proves uniqueness and (1).

Orient each connecting edge from its selected endpoint to the unique hole it dominates. Every layer has indegree exactly one; on a cycle this forces one coherent cyclic orientation. Reverse the first cycle if necessary so that all edges point from layer \(i\) to layer \(i+1\). Then the hole in layer \(i\) is \(h_i=f(i-1)\) and the outgoing selected endpoint is \((i,f(i+1))\). Formula (1) implies
\[
f(i+1)-f(i-1)\in S_k:=\{2,5,8,\ldots,3k-1\}\pmod m\quad\text{for every }i. \tag{2}
\]
Conversely, if a map satisfies (2), take \(D_i\) as in (1) with \(h_i=f(i-1)\). All but \(h_i\) are dominated inside the layer; the selected endpoint \((i-1,f(i))\) on the preceding connecting edge dominates \((i,f(i-1))\). Hence \(|D|=kn\). This proves the exact equivalence
\[
\gamma_{\mathrm S}(C_n,C_m)=kn
\iff\exists f:\mathbb Z_n\to\mathbb Z_m\;\forall i,\quad f(i+2)-f(i)\in S_k. \tag{3}
\]
The reflected orientation yields the same conclusion, since \(-S_k=S_k\) in \(\mathbb Z_m\).

**2. Classification of the closed walks.** The permutation \(i\mapsto i+2\) of \(\mathbb Z_n\) consists of one cycle of length \(\ell=n\) when \(n\) is odd, and two cycles of length \(\ell=n/2\) when \(n\) is even. Condition (3) holds if and only if there is a closed walk of length \(\ell\) on \(\mathbb Z_m\) whose increments lie in \(S_k\). A single such walk can be assigned independently to every orbit.

There is a two-step closed walk for every \(k\): its increments are \(2,3k-1\), summing to \(m\). For \(k\ge3\), a five-step closed walk has increments \(3k-7,2,2,2,2\), summing to \(m\). For \(k\ge2\), a seven-step closed walk has increments \(3k-4,3k-4,2,2,2,2,2\), summing to \(2m\). Every displayed increment belongs to \(S_k\). Concatenating two-step walks gives every even length at least two, every odd length at least five if \(k\ge3\), and every odd length at least seven if \(k=2\).

There can be no three-step closed walk for any \(k\). Each increment in \(S_k\) is congruent to \(2\pmod3\); thus the sum of three increments is divisible by three. If it is also divisible by \(m=3k+1\), it must be a positive multiple of \(3m\). Yet that sum is at most \(3(3k-1)<3m\). If \(k=1\), the only increment is \(2\) in \(\mathbb Z_4\), so a walk closes exactly when its length is even. If \(k=2\), a five-step sum has form \(10+3j\) for \(0\le j\le5\). The only positive multiples of seven in the range \([10,25]\) are \(14\) and \(21\), neither of this form. These obstructions, together with the constructions, classify all admissible lengths \(\ell\ge2\):

- for \(k=1\), exactly the even lengths;
- for \(k=2\), exactly the even lengths and odd lengths at least seven;
- for \(k\ge3\), exactly the even lengths and odd lengths at least five.

Translating \(\ell=n\) for odd \(n\) and \(\ell=n/2\) for even \(n\) gives precisely the three zero-correction cases stated in the finding.

**3. Universal one-vertex upper correction.** To show that failure of (3) implies **exactly** \(kn+1\), it suffices to construct a dominating set with at most \(kn+1\) vertices for any \(n,k\). Set
\[
f(i)=\begin{cases}0,&i\bmod4\in\{0,1\},\\2,&i\bmod4\in\{2,3\},\end{cases}
\qquad D_i=\{(i,f(i-1)+2+3j):0\le j<k\}.
\]
The set \(\bigcup_iD_i\) has size \(kn\) and leaves only \((i,f(i-1))\) undominated internally in each layer. Its preceding connecting edge covers this hole exactly when \(f(i)\ne f(i-2)\): the difference is then \(2\) or \(-2\), both in \(S_k\). A succeeding connecting edge cannot cover that hole, because if its endpoint coincided with it, the opposite endpoint would itself be the unique hole in the succeeding layer. Checking the four possible wraparound residues gives the **complete** list of remaining holes:

- if \(n\equiv0\pmod4\), none;
- if \(n\equiv1\pmod4\), only \((1,0)\);
- if \(n\equiv2\pmod4\), exactly \((0,0)\) and \((1,0)\);
- if \(n\equiv3\pmod4\), only \((0,2)\).

When \(n\equiv2\pmod4\), the two holes are adjacent via the connecting edge between layers zero and one, so selecting \((0,0)\) covers both. In every other nonempty case select the unique hole. Thus \(\gamma_{\mathrm S}(C_n,C_m)\le kn+1\). Combining this upper bound with (3) and the closed-walk classification proves the theorem. \(\square\)

## Verification

The self-contained Python 3 standard-library program `verify.py` checks the direct graph definition. Its independently implemented neighborhood calculation validates explicit optimal sets for \(3\le n\le60\), \(1\le k\le9\), and tests the closed-walk criterion against independent modular reachability dynamic programming: 522 parameter pairs in total. It also checks the one-vertex upper-bound constructions throughout those ranges. For four small cases where the lower bound is unattainable, it exhausts all connecting maps normalized by a global rotation and all per-layer subsets of the candidate size. For the fifth case, it stops once an attaining witness is found. Reproduce with `python3 verify.py`; the expected captured output is `verify_output.txt`.

These finite checks test implementations and boundary cases. The unlimited-parameter conclusion follows from the structural proof and explicit closed-walk constructions, not from finite extrapolation.

## Relationship to prior work

Henning, Klavžar, Kleszcz and Pilśniak (arXiv:2309.15409, later *Ars Mathematica Contemporanea* 24 (2024), article P3.06) proved that \(\gamma_{\mathrm S}(C_n,C_{3k+1})\in\{kn,kn+1\}\) and established equality to \(kn\) whenever \(4\mid n\). Their concluding discussion gives a further isolated example at \((n,k)=(18,2)\), but does not classify all cases. The present theorem settles their remaining two-valued alternatives by characterizing tight domination as a zero-sum closed-walk problem and resolving its length spectrum. Kovič, Pisanski, Zemljič and Žitnik (arXiv:1904.04180) introduced the underlying product; their structural results concern connectivity, planarity and automorphisms, not this extremal domination problem.

## Limitations

The theorem concerns the ordinary, closed-neighborhood domination number minimized over all maps \(f\) for second-factor cycle length congruent to one modulo three. It does not determine the domination number for each *fixed* map, the number of minimizing maps, or the unresolved cases for second-factor lengths congruent to two modulo three. An independently formalized proof and a complete search of unindexed literature have not been supplied; an equivalent solution could exist outside the inspected sources.

## References

1. M. A. Henning, S. Klavžar, E. Kleszcz, M. Pilśniak, **The Sierpiński domination number**, *Ars Mathematica Contemporanea* **24** (2024), #P3.06, DOI: `10.26493/1855-3974.2892.f07`; original public preprint `arXiv:2309.15409v1` (27 September 2023). Accessible text: https://arxiv.org/pdf/2309.15409 and https://home.agh.edu.pl/~pilsniak/53.pdf.
2. J. Kovič, T. Pisanski, S. S. Zemljič, A. Žitnik, **The Sierpiński product of graphs**, *Ars Mathematica Contemporanea* **23** (2023), #P1.01, DOI: `10.26493/1855-3974.1970.29e`; preprint `arXiv:1904.04180`.
