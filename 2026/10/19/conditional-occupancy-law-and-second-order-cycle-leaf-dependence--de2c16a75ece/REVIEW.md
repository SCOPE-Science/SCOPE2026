# Review of conditional occupancy law and second-order cycle–leaf dependence

## Correctness

**PASS.** For a connected simple labeled graph with one cycle, selecting the unique cycle and the attached rooted forest is a bijection. The fixed-root forest count is \(k n^{n-k-1}\). Requiring \(r\) specified off-cycle vertices to be leaves deletes them, then chooses their parents among \(n-r\) vertices; the resulting probability is \((1-r/n)^{n-k-1}\). These are precisely the joint empty-box probabilities with \(n-k-1\) balls and \(n-k\) designated boxes, and their factorial moments determine the entire conditional distribution. The strict negative regression and mixed covariance follow from explicit conditional means and truncated-Poisson cycle lengths. The Gaussian component follows from conditioning independent Poisson box counts on their total using a full-span two-dimensional lattice local central limit argument. The analytic proof treats the boundary cycle without off-cycle vertices separately. All finite joint distributions through seven vertices were enumerated with exact arithmetic (86 aggregate equalities). A finite enumeration is corroboration and does not prove the asymptotic results.

## Originality

**PASS, with historical-priority risk.** Moon establishes the rooted-forest enumeration used as an input, and Janson–Knuth–Łuczak–Pittel establish the cycle-of-rooted-trees generating-function framework. Neither inspected portion states the conditional leaf-empty-box identity, the strict regression for every increasing cycle-length penalty, or the \(\sqrt n\)-order mixed covariance alongside independent leading fluctuations. Drmota–Fusy–Kang–Kraus–Rué prove degree statistics in broader subcritical block-stable ensembles, but their stated results do not directly evaluate this conditional joint law. The known count and the standard separate limit mechanisms are not asserted to be original. A general earlier marked-leaf cycle generating function may have implicitly encoded the result and remains the main residual risk; a bounded search is not a claim of global uniqueness.

## Mathematical value

**PASS.** The entire leaf distribution conditional on the unique-cycle length is a natural, parameter-free occupancy law, not a single isolated count. The resulting strict negative conditional-mean regression and the sharp negative covariance constant explain a subtle dependence invisible in the leading independent half-normal/Gaussian limit. The result provides an exact and asymptotic benchmark for single-cycle random-graph components.

## Sources and scope limits

Source comparisons used Moon (1970, Sections 3.5–3.6), Janson–Knuth–Łuczak–Pittel (original 1993 preprint, Section 3), Drmota et al. (original 2010 preprint, Sections 1 and 8), and Noy (enumerative rooted forests). Published research-index searches included unicyclic cycle/leaf dependence, occupancy equivalences, random-forest leaf covariance, and possible stronger cycle-length/leaf normal limits. No directly covering implication was found in the inspected materials, but earlier implicit enumeration remains possible. Exact day-specific first-public evidence is the original 1993-10-01 arXiv record; Moon's earlier book has a known publication year but its precise public day is not verified.

Self-review: passed. Independent audit: not yet performed.
