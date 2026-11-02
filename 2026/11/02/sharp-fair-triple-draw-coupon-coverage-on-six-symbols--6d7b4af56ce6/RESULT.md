# Sharp fair triple-draw coupon coverage on six symbols

## Finding

Let \(V=\{1,2,3,4,5,6\}\), and let \(\mathcal H\) be any nonempty **simple**, \(3\)-uniform, **fair** family on \(V\): its blocks are distinct three-element subsets, every symbol lies in the same positive number of blocks, and each round independently draws one block uniformly from \(\mathcal H\). Write \(T_{\mathcal H}\) for the number of rounds up to and including the first round by which every symbol has appeared.

The exact maximum over all such fair families is

\[
\max_{\mathcal H}\mathbb E T_{\mathcal H}=\frac{157}{36}.
\]

Equality holds **if and only if** \(\mathcal H\) is a \(2\)-\((6,3,2)\) block design: it consists of ten distinct triples and each pair of symbols occurs in exactly two triples. One extremizer, with each string representing a three-element block, is

```text
123 124 135 245 345 236 146 346 156 256
```

In contrast, the full family \(\binom V3\) has expectation \(327/76\), which is strictly smaller by \(10/171\). Within the class of nonempty simple fair three-uniform families, \(6\) is the **smallest number of symbols** for which the full family fails to maximize expected coverage time: no such failure occurs for \(3\), \(4\), or \(5\) symbols.

## Assumptions and scope

All statements concern independent sampling *with replacement* from the support family; each distinct allowed block has equal draw probability. A draw discloses all three symbols of the selected block. Fairness means equal degrees, not merely equal marginal weights under an arbitrary weighted probability distribution. The family is simple (no repeated blocks), nonempty and finite. We make no claims for weighted or repeated-block mechanisms, other block sizes, or larger numbers of symbols.

For \(M=|\mathcal H|\), fairness implies that each vertex has degree \(M/2\), since the sum of six vertex degrees is \(3M\). In particular \(M\) is even, \(2\le M\le20\). For each pair \(e\subset V\), \(|e|=2\), denote by \(c_e\) the number of allowed triples containing that pair. Then

\[
0\le c_e\le M/2<M,\qquad \sum_{|e|=2}c_e=3M.
\]

## Proof

**1. Exact pair-codegree formula.** For a nonempty set \(A\subseteq V\), let \(p_A\) be the fraction of blocks intersecting \(A\). Every \(p_A>0\), because every vertex has positive degree. Inclusion-exclusion applied to the event that at least one symbol remains unseen after a given number of draws, followed by summing the geometric series, gives

\[
\mathbb E T_{\mathcal H}=\sum_{\varnothing\ne A\subseteq V}(-1)^{|A|+1}\frac1{p_A}.
\]

If \(|A|=1\), then \(p_A=1/2\); the six singleton contributions total \(12\). If \(A=e\) is a pair, then \(p_e=1-c_e/M\); the pair contributions total \(-\sum_{|e|=2}M/(M-c_e)\). If \(|A|=3\), its complement is the only possible triple disjoint from \(A\). Thus for the \(M\) choices with \(V\setminus A\in\mathcal H\), we have \(p_A=(M-1)/M\); for the other \(20-M\) choices, \(p_A=1\). The \(3\)-set contributions therefore total \(M^2/(M-1)+(20-M)=20+M/(M-1)\). Every set of four or more symbols intersects every triple, so their remaining contributions total \(-15+6-1=-10\). Consequently

\[
\boxed{\mathbb E T_{\mathcal H}=22+\frac{M}{M-1}-\sum_{|e|=2}\frac{M}{M-c_e}.}\tag{1}
\]

All denominators are strictly positive. Formula (1) uses only fairness, simplicity and the three-uniform six-symbol geometry.

**2. Exact upper envelope.** For fixed \(M\), the function \(f_M(x)=M/(M-x)\) is strictly convex for \(x<M\), and its successive integer increments are strictly increasing. Therefore, among fifteen integers with sum \(3M\), the sum of \(f_M\) is minimized when entries differ by at most one. Put

\[
a=\left\lfloor\frac M5\right\rfloor,\qquad b=3M-15a,\qquad 0\le b<15.
\]

There are \(15-b\) entries equal to \(a\) and \(b\) entries equal to \(a+1\). The strict discrete convexity argument is a pairwise smoothing: if two entries differ by at least two, moving one unit from the larger to the smaller strictly decreases their sum of \(f_M\). All these balanced entries fall below \(M\) for the permitted even values of \(M\). Equation (1) yields

\[
\mathbb E T_{\mathcal H}\le U_M:=22+\frac M{M-1}-(15-b)\frac M{M-a}-b\frac M{M-a-1}.
\]

The complete list of permissible support sizes and exact bounds is

| \(M\) | \(U_M\) |
|---:|---:|
| 2 | \(3\) |
| 4 | \(13/3\) |
| 6 | \(43/10\) |
| 8 | \(30/7\) |
| 10 | \(157/36\) |
| 12 | \(236/55\) |
| 14 | \(1231/286\) |
| 16 | \(838/195\) |
| 18 | \(2551/595\) |
| 20 | \(327/76\) |

Each listed value is strictly below \(157/36\) except the one at \(M=10\). When \(M=10\), strict convexity forces equality precisely when all fifteen pair codegrees equal \(2\). That condition is exactly the definition of a \(2\)-\((6,3,2)\) design (the vertex degree then necessarily equals \(5\)). The ten explicitly listed triples have degree \(5\) at each vertex and contain every pair exactly twice, proving existence and attaining \(157/36\). The full family has \(M=20\) and pair codegrees \(4\), yielding \(327/76\); subtraction gives \(10/171\).

**3. First-order cutoff at six symbols.** For three symbols, the only support is the single triple. For four symbols, fairness forces the support size to be divisible by four and at most four, so the full four-triple family is the only possibility. For five symbols, fairness forces the support size to be divisible by five, hence it is either five or ten. Ten gives the full family, of expectation \(29/9\). In a five-block fair family, each vertex has degree three; taking complements of the blocks produces a simple graph with five edges and every vertex degree two. Every such graph on five vertices is a five-cycle, so the support is unique up to relabeling. Counting the number of allowed blocks meeting a singleton, pair, triple, four-set or five-set gives, respectively, five contributions with denominator \(3/5\), five pair contributions with denominator \(4/5\) and five with denominator \(1\), and all other denominators equal to \(1\). Inclusion-exclusion yields

\[
\mathbb E T_{\mathrm{five\,blocks}}
=\frac{25}{3}-\left(\frac{25}{4}+5\right)+10-5+1
=\frac{37}{12}
<\frac{29}{9}=\mathbb E T_{\mathrm{full}}.
\]

Thus there is no smaller three-uniform fair support that exceeds the full mechanism, completing the proof.

## Verification

The accompanying standalone `verify.py` uses Python's exact rational arithmetic and has no external dependencies. Execute `python3 verify.py`. It recomputes every entry of the upper-envelope table and verifies strict maximality, all fifteen pair-codegrees and all vertex degrees of the extremizing design, the exact expectation both through inclusion-exclusion and through an independent absorbing-state dynamic program, the full-mechanism gap, and the five-symbol cycle comparison. The small finite checks corroborate the identities; the strict-convexity proof proves the maximum for all allowed supports without requiring exhaustive enumeration of support families.

## Relationship to prior work

Grunbaum and Yaakobi introduced fair uniform-block coverage mechanisms, derived general expectation and monotonicity results, and conjectured that the full model maximizes the coverage time. Barak-Pelleg and Berend disproved this conjecture using the seven-point Fano plane, developed projective and other fair examples, and explicitly identified determination of the maximal possible expected time among fair mechanisms as open. Their main examples do not determine the exact optimum over six-point triple supports. This result supplies a complete extremal theorem for the first nontrivial smaller parameter, identifies its design-theoretic equality condition, and establishes minimality among three-uniform simple fair supports. Inclusion-exclusion and convex smoothing are classical tools; the asserted contribution is their reduction to a sharp, previously unreported six-symbol classification, not novelty of those tools or of the classical block design.

## Limitations

The comparison is restricted to a nonempty *simple* equal-weight three-uniform support with each symbol in equally many allowed blocks. No characterization of optimal fair mechanisms for seven or more symbols is supplied. The proof does not cover multisets of blocks or arbitrary nonuniform draw weights, and it establishes no stochastic ordering beyond the stated expected-time maximum. Priority of the exact finite classification has not been independently audited; an unindexed combinatorial-design or coverage calculation could predate it.

## References

1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1 (first posted 2026-06-26). https://arxiv.org/abs/2606.28216
2. Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1 (first posted 2025-10-29). https://arxiv.org/abs/2510.25305
