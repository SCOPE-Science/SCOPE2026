# Review of four-run Lyndon factors

## Correctness — PASS

The complete factor list follows from the proper-suffix Lyndon criterion. For nontrivial Lyndon factors in \(0^a1^b0^c1^d\), only two- and four-run patterns are possible; the two-run patterns form a union of rectangles and the four-run patterns are decided by \(i>c\) or \(i=c, j>b\). The exact length polynomial is an exhaustive disjoint classification. The three-case expression for \((a+c)(b+d)-L(w)\) proves the sharp extremum and every equality case, independently of finite experiments. The rational generating function is derived by formal geometric-series summation, and the limit/moments follow from a Dirichlet change of variables and exact rational integration. The standalone brute-force verifier checks 2,401 complete spectra, every composition through length 30, and the rational integrals. Risk: computational checks are necessarily finite, but the general arguments cover every positive quadruple.

## Originality — PASS

Theorem 1 of Glen–Simpson–Smyth (2017), DOI 10.37236/6915 / arXiv:1701.00928, gives the unrestricted binary maximum \(\lfloor n^2/4\rfloor+2\), not the sharp maximum conditional on exactly four nonempty runs, its equality rigidity, its full length-resolved factor set, or the conditional generating function and limit. Its Theorem 8 concerns Lyndon/Christoffel words, a special subset rather than the arbitrary four-run family. Hirakawa–Nakashima–Inenaga–Takeda (2021), arXiv:2106.01190, treats unrestricted factor statistics and subsequences, not fixed-four-run exact factors. Searches for four-run Lyndon counting and run-length formula equivalences in published mathematical records yielded no dominating result. This is best-knowledge originality, not a proof that no independently discovered specialization exists. Residual risk: publications or theses not indexed in the searched records.

## Mathematical value — PASS

Distinct Lyndon factors are a standard stringological invariant with established global extremal and expectation results. Imposing exactly four positive runs introduces two competing zero runs and an interior matching suffix. The theorem provides the full length spectrum, a provably sharp three-unit extremal loss compared with unrestricted binary words, and unique or double rigid optimizers for every length. Uniform run-composition sampling yields a distinct, nondegenerate conditional law with exact rational mean/variance and a finite-length aggregate generating function. These connect structural string enumeration to conditional probabilistic asymptotics rather than merely recomputing a known general bound.

## Literature and limitations

Reviewed original accessible source material in the 2017 *Counting Lyndon factors* paper, especially its unrestricted maximum (Theorem 1), unrestricted expectation (Section 4), and special Christoffel result (Theorem 8), and in the 2021 *Counting Lyndon Subsequences* paper, especially Tables 1–2 and Sections 1–3. Those statements differ in assumptions or resulting information. No claim is made about other alphabets, more runs, factor multiplicities, a simpler CDF of the limit, or independence of the review.

Self-review: passed. Independent audit: not yet performed.
