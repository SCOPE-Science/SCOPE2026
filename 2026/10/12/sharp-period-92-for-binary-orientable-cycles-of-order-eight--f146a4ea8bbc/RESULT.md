# Sharp period 92 for binary orientable cycles of order eight

## Finding
Among all nonempty cyclic binary words in which every length-eight cyclic factor differs from the reversal of every length-eight cyclic factor (including itself), the largest possible length is exactly
\[
\boxed{M_8=92}.
\]
The upper bound is proved by a finite integral dual certificate of weight \(28\) on a graph of \(240\) ports; a displayed cyclic word of length \(92\) attains it.

## Assumptions and scope
A cyclic binary word \(S=s_0\cdots s_{m-1}\), indexed modulo \(m\), is **orientable of order eight** if for every \(i,j\in\{0,\ldots,m-1\}\) its cyclic factors \(s_i\cdots s_{i+7}\) and \(s_j\cdots s_{j+7}\) are not reversals of one another. In particular, palindromic eight-bit factors are forbidden, as is using both members of a nonpalindromic reversal pair. Its \(m\) distinct factors correspond to directed edges in the binary order-seven de Bruijn graph, with every vertex having equal in- and out-degree. The theorem concerns cycles, not linear words or larger alphabets/orders.

Represent binary strings by fixed-width nonnegative integers with leading zeros retained. Let \(R_k\) reverse the \(k\) bits, and let
\[
P=\{w\in\{0,\ldots,255\}:w<R_8(w)\}.
\]
The \(16\) length-eight palindromes are omitted, leaving exactly \(|P|=120\) reversal pairs. Enumerate the elements of \(P\) in increasing numerical order as \(p_0,\ldots,p_{119}\). For each pair, create two labeled ports, numbered \(2i\) (prefix) and \(2i+1\) (suffix), at the reversal orbits of the first and last seven bits of \(p_i\), respectively.

## Proof
**1. Necessary local signed balance.** The \(128\) seven-bit vertices fall into \(72\) reversal orbits: \(56\) nonpalindromic pairs \(\{v,R_7(v)\}\) and \(16\) palindromic singletons. At a nonpalindromic orbit use its smaller representative \(v\). A port contributed by the prefix \(a\) of a canonical eight-word has sign \(+1\) when \(a=v\), otherwise \(-1\). A suffix port contributed by \(b\) has sign \(-1\) when \(b=v\), otherwise \(+1\). Equivalently, the sign is the canonical-versus-reversed representative sign, multiplied by \(+1\) for a prefix and \(-1\) for a suffix.

Write \(\delta(z)=d^+(z)-d^-(z)\) for the selected directed eight-factor edges at a seven-bit vertex. Whether the chosen orientation of a nonpalindromic pair is \(w\) or \(R_8(w)\), its contribution to \(\delta(v)-\delta(R_7(v))\) is precisely the sum of signs of its ports incident to this reversal orbit. This follows by comparing the endpoints \(a\to b\) of \(w\) with \(R_7(b)\to R_7(a)\) of \(R_8(w)\). Both represent the same signed source/sink incidence difference. Since the cyclic word has \(\delta(z)=0\) at every vertex, the selected ports at each nonpalindromic orbit have equally many positive and negative signs.

The \(16\) palindromic seven-bit vertices have either one or two ports: precisely two have one, and fourteen have two (this is directly enumerated by the definitions). Equal in- and out-degree forces an even number of selected incident ports. Therefore a one-port orbit selects none, and a two-port orbit selects either both or neither. At each two-port palindromic orbit give the first port sign \(+1\) and the second \(-1\); at each one-port orbit give its port sign \(+1\). With this convention **every** reversal orbit has equal numbers of selected positive and negative ports.

**2. A necessary perfect matching.** Construct an undirected edge-weighted graph \(H\) on the \(240\) ports. For each \(i\), connect ports \(2i\) and \(2i+1\) by an *omission edge* of cost \(1\). Within each seven-bit reversal orbit connect every positive port to every negative port by a *transition edge* of cost \(0\). The explicit construction yields \(120\) omission and \(210\) transition edges, without collisions between the two types, for a total of \(330\) edges.

Any orientable cycle induces a perfect matching of \(H\): match the two ports of every omitted reversal pair through its omission edge; for the selected pairs, match positive selected ports bijectively to negative selected ports inside each orbit. These choices cover each port exactly once. Its cost is exactly the number of the \(120\) reversal pairs not used by the cycle.

**3. Exact dual lower bound.** For port indices \(j\in\{0,\ldots,239\}\), the file `DUAL.txt` gives integer weights \(y_j\) in that order. The standalone verifier constructs all \(330\) edges and checks the exact inequalities
\[
\sum_{j=0}^{239}y_j=28,\qquad
 y_u+y_v\le c_{uv}\quad\text{for every }uv\in E(H),
\]
where \(c_{uv}\in\{0,1\}\) is the edge cost. For any perfect matching \(Q\), summing its edge inequalities counts each \(y_j\) exactly once, so
\[
\operatorname{cost}(Q)\ge\sum_j y_j=28.
\]
Consequently an orientable cyclic word must omit at least \(28\) of the \(120\) reversal pairs. Its length is at most \(120-28=92\). This argument requires no optimization package or unverified exhaustive search: the explicitly displayed integer vector and \(330\) finite inequalities form a self-contained upper-bound certificate.

**4. Attainment.** The file `WITNESS.txt` specifies the following cyclic binary word (wraparound understood):

```text
00000100011011100110100011101001100011110101000011010111011111001001010101101100100010100111
```

The verifier enumerates its \(92\) cyclic length-eight factors and checks their distinctness, that none is palindromic, and that no reversed factor occurs. Thus the word is orientable with least period \(92\) (distinct windows also exclude any shorter period). Together with the upper bound, the maximum is exactly \(92\).

## Verification
Place `verify.py`, `DUAL.txt`, and `WITNESS.txt` in the same directory and run `python3 verify.py` (Python 3 standard library only, assertions enabled). The expected final line is:

```text
VERIFY_OK order=8 pair_orbits=120 quotient_vertices=72 ports=240 certificate_edges=330 dual_sum=28 upper_bound=92 witness_period=92
```

The program reconstructs all indices and edges from the mathematical definitions, verifies the signed-incidence identity for both orientations of all \(120\) pairs, verifies every integer dual inequality and its objective \(28\), and independently checks the witness's \(92\) windows. No floating-point arithmetic, external solver, or time-limited enumeration is needed for replay.

## Relationship to prior work
Gabrić and Sawada, *Construction of orientable sequences in \(O(1)\)-amortized time per bit* (arXiv:2401.14341, first posted January 25, 2024), report a longest known binary order-eight orientable cycle of length \(92\), but retain the published upper bound \(96\) (Table 2) and state that the exact maxima had been known only through order seven. Mitchell and Wild, *Constructing orientable sequences* (arXiv:2108.03069, 2021; Table 1), give the bound \(96\). Their *New orientable sequences* (arXiv:2507.02526, 2025; Sections 1–2) develops general graph-based bounds and constructions without providing an exact binary order-eight maximum. Burris, Motta and Shipman study a related but different *cover-all-reversal-classes* problem, in which palindromes are required rather than forbidden; their unoriented de Bruijn graph does not establish the present maximum. This finding proves the previously unestablished optimality of the already-known attainable value \(92\), using a different finite dual bound.

## Limitations
The theorem does not classify all extremizing cycles, extend the exact value to order nine or higher, or establish a general formula. The dual vector is a finite exact certificate, not an asserted closed-form family of dual vectors at other orders. The historical priority comparison is based on the cited inspected sources and targeted literature searches; an unindexed equivalent proof cannot be excluded. Scientific interpretation remains subject to independent review.

## References
1. D. Gabrić and J. Sawada, *Construction of orientable sequences in O(1)-amortized time per bit*, arXiv:2401.14341 (first submitted 2024-01-25), https://arxiv.org/abs/2401.14341 ; inspected full HTML text, Table 2 and conclusions, version 4.
2. C. J. Mitchell and P. R. Wild, *Constructing orientable sequences*, arXiv:2108.03069 (first submitted 2021-08-06), https://arxiv.org/pdf/2108.03069 ; inspected full-text definition, Theorem 2.5 and Table 1.
3. C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526 (first submitted 2025-07-03), https://arxiv.org/pdf/2507.02526 ; inspected full-text Sections 1–2 and conclusions.
4. C. J. Mitchell and P. R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646 (2026), https://arxiv.org/pdf/2603.18646 ; inspected introduction and binary/nonbinary scope.
5. *De Bruijn Sequences and Universal Cycles*, orientable sequence data and bounds, https://debruijnsequence.org/db/orientable ; compared the known length \(92\) and stated maximum-status gap.
6. C. S. Burris, F. C. Motta, and P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480 (2016), https://arxiv.org/pdf/1608.08480 ; inspected the full-text definitions, quotient de Bruijn graph, and statement of the minimum-cover problem.
