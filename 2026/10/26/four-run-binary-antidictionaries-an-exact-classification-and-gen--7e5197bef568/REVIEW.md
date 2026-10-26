# Scientific review: four-run binary minimal absent factors

## Correctness

**PASS.** The all-parameter proof uses the exact factor rectangles of a four-run word, then the necessary-and-sufficient test that deleting either end letter of an absent candidate yields a factor. It exhausts candidates with one through four runs and excludes those with at least five runs. The explicit families are disjoint. Counting their indicators yields \(b+c+(1+\mathbf1_{a>c})(1+\mathbf1_{d>b})\); the same two indicators factor the rational bivariate generating function. For the extremal claim, exactly two strict comparisons permit the correction \(4\), and that case forces \(a,d\ge2\), with the isolated equality \((2,1,1,2)\). The independent `verify.py` constructs the actual factor set and checks equality of the *whole* minimal-absent set to the listed set on all \(8^4=4096\) positive quadruples with each parameter at most \(8\); it also checks maxima over lengths \(4\)–\(21\) and the joint generating counts through length \(17\). The infinite statement is proved symbolically, not inferred from finite experiments.

## Originality

**PASS under the stated source access, with residual priority risk.** The closest primary text inspected in detail was Akagi et al. (2022), arXiv:2202.13591, including its five-way MAW classification, three-run bridge lemma, general enumeration theorem and exact bridge graph test. Those results give output-sensitive algorithms and asymptotic bounds for arbitrary run-encoded words. They do not state or algebraically imply the displayed complete four-run binary family list, multiplicative boundary correction, joint rational counting series, or exceptional six-letter extremum without a new parametric analysis. Searches for equivalent formulas, forbidden-factor/antidictionary terminology, generating functions, and broader classes located no covering formula. A 2024 primary work on CDAWG enumeration was accessible only as an abstract; its full text could not be inspected because institutional VPN access was unavailable. That is a residual risk, not evidence that it does not contain the result. Source indexing is incomplete, so priority cannot be guaranteed.

## Mathematical value

**PASS.** Four alternating runs constitute the first simple binary RLE class with two separate \(0\)-to-\(1\) factor rectangles and a nontrivial splice condition. The exact answer is not merely a run-count bound: it identifies *every* minimal forbidden factor, proves a surprisingly small multiplicative correction governed by two competing run inequalities, and supplies an exact rational bivariate census of all word-length/antidictionary-size pairs. The sharp extremum has a genuine isolated exception at length six. This furnishes a structurally motivated complete classification for a natural compressed-word family, even though it is not a general algorithmic improvement.

## Closest literature and limits

Akagi et al., *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (2022), provide the general framework and algorithms; their three-run type-3 examples are relevant but not the claimed four-run enumeration. Inenaga et al., *Computing Minimal Absent Words and Extended Bispecial Factors with CDAWG Space*, arXiv:2402.18090 (2024), treat the same underlying invariant algorithmically; comparison with its full text remains unresolved by access. The word family is binary, linear and exactly four runs; no statement is claimed for larger alphabets, scattered subsequences or arbitrary run counts. Independent source-by-source verification of novelty and formal proof certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
