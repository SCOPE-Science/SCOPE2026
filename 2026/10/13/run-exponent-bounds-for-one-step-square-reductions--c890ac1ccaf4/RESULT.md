# The one-step square-reduction out-degree is a sum over runs

## Finding

For a nonempty finite word \(W\) of length \(n\), let \(\deg^+(W)\) count the distinct words obtained by replacing one occurrence of \(XX\) with \(X\) (with \(X\ne\varepsilon\)). A run \(R\) is an occurrence of a factor of least period \(d(R)\), length at least \(2d(R)\), and maximal under one-letter extension at either end preserving period \(d(R)\). Write \(e(R)=|R|/d(R)\). Then
\[
\deg^+(W)=\sum_{R\in\operatorname{Runs}(W)}\left\lfloor\frac{e(R)}2\right\rfloor\le n-1.
\]
In particular, the maximum one-step out-degree over words of length \(n\) over any alphabet of size \(k\ge2\) is at most \(n-1\), which implies Conjecture 3 of Grytczuk and Stankiewicz [1]. The sum counts run occurrences, not distinct run factors or distinct square factors.

## Proof

Fix a root length \(p\). Set \(M_p(t)=1\) when \(W_t=W_{t+p}\), and \(M_p(t)=0\) otherwise, for \(1\le t\le n-p\). A square starts at \(i\) precisely when \(M_p=1\) throughout \([i,i+p-1]\). Deleting the first or the second copy yields the same word. If \(i<j\) are square starts, deleting the first copy at \(i\) or \(j\) gives the same output if and only if \(W_{t+p}=W_t\) throughout \(i\le t<j\): these are the only positions at which the descriptions of the two outputs differ. Thus the distinct outputs at root length \(p\) correspond to maximal intervals \([a,b]\) of ones in \(M_p\) of length at least \(p\).

The factor \(W[a\,..\,b+p]\) associated with such an interval has length at least \(2p\) and is maximal for period \(p\). Its least period \(d\) divides \(p\) by Fine–Wilf [2], since \(\gcd(d,p)\) is a period whenever the length is at least \(d+p-\gcd(d,p)\). It is also maximal for \(d\), since a one-letter extension preserving \(d\) would preserve its multiple \(p\). This yields a run \(R\) and a period label \(p\).

Conversely, take a run \(R=W[a\,..\,c]\) and \(p\) a positive multiple of its least period \(d\), with \(2p\le |R|\). The factor has period \(p\). If the left boundary can be tested, then \(W_{a+p-1}=W_{a+d-1}\) by \(d\)-periodicity inside \(R\); these are the positions compared to \(W_{a-1}\) in the two respective extension tests. Therefore maximality for \(d\) forbids extending to the left with period \(p\). The same holds on the right because \(W_{c+1-p}=W_{c+1-d}\). Hence \([a,c-p]\) is exactly a maximal interval of ones in \(M_p\) of length at least \(p\). These constructions are inverse. There are \(\lfloor e(R)/2\rfloor\) labels for \(R\), and different \(p\) give different output lengths. This proves the exact formula.

For the bound, the disjoint Lyndon-root start sets of Bannai et al. [3, Lemma 8 and proof of Theorem 10] give
\[
\sum_{R\in\operatorname{Runs}(W)}\lfloor e(R)-1\rfloor\le n-1.
\]
Specifically, their start set for each run has at least \(\lfloor e(R)-1\rfloor\) positions, and the sets are pairwise disjoint and avoid the first position. One can regard \(W\) as a word over an alphabet of at least two symbols even if it uses only one symbol. For \(e\ge2\) one has \(e/2\le e-1\), hence \(\lfloor e/2\rfloor\le\lfloor e-1\rfloor\). The bound follows termwise.

## Relationship to prior work, scope and verification

The out-degree and its proposed coefficient-one bound come from [1]. The Lyndon-root bound used here is from [3]; the additional step is the correspondence between **distinct shortened words** and admissible run-period pairs. Neither the Lyndon-root bound by itself nor a bound on distinct square factors counts those shortened words.

The result is about one-step tandem-square contractions, not arbitrary deletions, the number of distinct square factors, or the number of square-free words reachable by iterating reductions. For example, `00100` has one distinct square factor (`00`) but produces `0100` and `0010`. The bound \(n-1\) is not asserted to be sharp for all alphabet sizes and lengths.

Run `python3 verify.py` to compare direct sets of shortened words against independently enumerated run occurrences. The script checks the exact equality, the charging inequality, and the upper bound on all 4,094 nonempty binary words through length 11 and all 3,279 nonempty ternary words through length 7. These are finite corroborations; the proof handles arbitrary length.

## References

1. J. Grytczuk and M. Stankiewicz, *Square-free reducts of words*, arXiv:2011.12822, Conjecture 3.
2. N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, Proc. Amer. Math. Soc. **16** (1965), 109–114.
3. H. Bannai et al., *The “Runs” Theorem*, SIAM J. Comput. **46** (2017), 1501–1514, doi:10.1137/15M1011032; arXiv:1406.0263, Lemma 8 and proof of Theorem 10 in the arXiv numbering.
