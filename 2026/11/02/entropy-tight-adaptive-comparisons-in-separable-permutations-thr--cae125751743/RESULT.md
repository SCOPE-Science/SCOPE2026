# Entropy-tight adaptive comparisons in separable permutations through seven labels

## Finding
For every integer \(n\ge1\), let \(\mathcal S_n=\operatorname{Av}_n(2413,3142)\) be the separable permutations of \([n]\). Regard each \(\pi\in\mathcal S_n\) as a Boolean function on the query domain \(Q_n=\{(i,j):1\le i<j\le n\}\), whose value at \((i,j)\) is one precisely when \(\pi(i)<\pi(j)\). The VC dimension is exactly
\[
\operatorname{VCdim}(\mathcal S_n)=n-1.
\]
For \(n=1,2,3,4,5,6,7\), the exact Littlestone dimensions are \(0,1,2,4,6,8,10\), respectively. In all seven cases the adaptive dimension attains \(\lfloor\log_2|\mathcal S_n|\rfloor\). In particular,
\[
|\mathcal S_7|=1806,\qquad \operatorname{VCdim}(\mathcal S_7)=6,\qquad \operatorname{Ldim}(\mathcal S_7)=10.
\]
For every integer \(s\ge1\), the infinite family obtained by allowing any separable permutation on \(7s\) positions satisfies
\[
\operatorname{Ldim}(\mathcal S_{7s})\ge10s,\qquad
\operatorname{Ldim}(\mathcal S_{7s})-\operatorname{VCdim}(\mathcal S_{7s})\ge3s+1.
\]
The gap therefore grows without bound. The first strict gap in the exact finite table occurs at four positions.

| \(n\) | \(|\mathcal S_n|\) | VC | Littlestone | \(\lfloor\log_2|\mathcal S_n|\rfloor\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 0 | 0 |
| 2 | 2 | 1 | 1 | 1 |
| 3 | 6 | 2 | 2 | 2 |
| 4 | 22 | 3 | 4 | 4 |
| 5 | 90 | 4 | 6 | 6 |
| 6 | 394 | 5 | 8 | 8 |
| 7 | 1806 | 6 | 10 | 10 |

## Assumptions and scope
A permutation is separable if it is obtained from the one-point permutation by iterated direct sums and skew sums; equivalently, it avoids both classical four-point patterns \(2413\) and \(3142\). For permutations \(\alpha\) on \([a]\) and \(\beta\) on \([b]\), their direct sum has first block \(\alpha\) and second block \(a+\beta\). The skew sum has first block \(b+\alpha\) and second block \(\beta\). A query compares *values in two fixed positions*, not the order of two named values. Every adaptive tree here is a complete binary tree, and its depth is the number of comparisons along each root-to-leaf path. The theorem concerns exact noiseless Boolean labels, and no identification-tree complexity claim is made.

## Proof
**All-size static upper bound.** Suppose \(T\subseteq Q_n\) is VC-shattered. Its undirected support graph on the \(n\) positions must be a forest. Otherwise choose a simple cycle in the graph and assign the outcomes of its edge queries so that every edge points consistently around the cycle. This demands a strict cyclic chain of numerical inequalities and cannot be realized by any permutation. Thus \(|T|\le n-1\).

**All-size static lower bound.** Query the \(n-1\) adjacent position pairs \((i,i+1)\). For an arbitrary prescribed pattern of descents and ascents, break the positions into maximal runs connected by requested descents and take the direct sum of decreasing permutations on those consecutive runs. Within each run every adjacent comparison is descending; between runs every adjacent comparison is ascending. Each decreasing run is a repeated skew sum of singleton permutations, so this direct sum is separable. Hence every one of the \(2^{n-1}\) patterns occurs, proving the VC formula, including the empty support for \(n=1\).

**Finite adaptive lower bounds.** The included `certificates.json` provides a complete depth-\(d\) comparison tree for each \(1\le n\le7\), with \(d=0,1,2,4,6,8,10\), respectively. Every leaf carries a distinct separable permutation that answers all comparisons on that root-to-leaf path correctly. The tree at seven positions has \(1023\) internal queries and \(1024\) distinct leaf witnesses. The independent verifier reconstructs the entire separable class by both pattern avoidance and direct/skew sum closure, checks their equality, then recursively checks every internal branch and all leaf witness values. This is a finite exhaustive certificate check, not a statistical sample.

**Finite adaptive upper bounds.** If a finite class shatters a complete depth-\(d\) binary tree, each of its \(2^d\) leaves requires a different concept: a concept cannot follow paths diverging at a query. Thus \(2^d\le|\mathcal H|\). The independently enumerated class sizes for \(1\le n\le7\) are \(1,2,6,22,90,394,1806\), giving the precise upper bounds in the table. Together with the checked trees, these establish equality in every row.

**All-size separation.** A direct sum of \(s\) independent seven-position separable permutations is itself separable. Restrict queries to pairs lying within the same seven-position block. Concatenate the \(s\) complete depth-ten trees, attaching the next block's tree at every leaf of the preceding block's tree. Independent block witnesses realize all branches of a complete depth-\(10s\) tree in \(\mathcal S_{7s}\). Hence \(\operatorname{Ldim}\ge10s\). The proven static formula gives VC dimension \(7s-1\), and subtraction yields the stated gap.

## Verification
Using Python 3 and only its standard library, run `python3 build_certificates.py` followed by `python3 verify_separable.py` in a directory containing these files and `certificates.json`. The builder scans all permutations of size up to seven, filters forbidden patterns, and constructs complete depth-optimal trees by a memoized version-space recursion. The verifier independently generates the class by direct/skew closure and by pattern avoidance, compares the families for each size, checks every branch of the stored trees against actual permutations, establishes leaf distinctness, and checks every adjacent-comparison pattern. Its final line is `SEPARABLE_ALL_NEW_CHECKS_PASS`. The certificate source and verifier are embedded with this result; the mathematical induction for the all-size statements does not depend on the finite computations.

## Relationship to prior work
Pinsky's 2019 preprint on the infinite limit of separable permutations (arXiv:1911.05565, first public version 2019-11-13) studies the same separable family and its Schröder enumeration, with focus on probabilistic scaling. Its introductory definitions and enumerative recurrence agree with the finite concept counts used here, but its inspected statements do not provide adaptive comparison trees. Ghazi, Golowich, Kumar, and Manurangsi (ALT 2021) provide general Littlestone and threshold-dimension closure bounds, not these exact restricted-permutation values. Earlier work on unrestricted permutations and single length-three pattern avoidance does not determine the restricted class \(\operatorname{Av}(2413,3142)\) from class inclusion alone. Exact priority under unsearched terminology is not established by these comparisons.

## Limitations
Exact finite Littlestone dimensions are only claimed through seven positions. No exact dimension or matching asymptotic upper bound is claimed beyond that range, only the stated infinite lower bound. The seven-position lower bound relies on a fully specified, replayable finite tree; absence of indexed prior claims does not prove historical novelty. No noisy-query or average-case learning result follows.

## References
1. R. G. Pinsky, *The Infinite Limit of Separable Permutations*, arXiv:1911.05565 (first public version 2019-11-13); https://arxiv.org/abs/1911.05565 .
2. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Algorithmic Learning Theory, PMLR 132 (2021), 686--696; https://proceedings.mlr.press/v132/ghazi21a.html .
