# Exact cyclic \(k\)-spectrum fibers of repeated binary two-run words

## Finding
Let \(a,b\ge1\), \(t\ge2\), and \(n=t(a+b)\). Consider the binary necklace represented by
\[
W=(0^a1^b)^t.
\]
For \(2\le k\le n\), its **cyclic \(k\)-spectrum** is the multiset of its \(n\) length-\(k\) contiguous windows, including those crossing the cyclic boundary, with all multiplicities retained. Two words are identified only when they differ by rotation (not by reversal or complementation).

Define
\[
\rho_0=\max\{a-k+1,0\},\qquad \rho_1=\max\{b-k+1,0\}.
\]
The number of different length-\(n\) binary necklaces having precisely the same cyclic \(k\)-spectrum as \(W\) is exactly
\[
\boxed{\mathcal F_{a,b,t}(k)=\frac1t\sum_{d\mid t}\varphi(d)
\binom{\frac td(1+\rho_0)-1}{\frac td-1}
\binom{\frac td(1+\rho_1)-1}{\frac td-1}.}
\]
Here \(\varphi\) denotes Euler's totient and the binomial coefficients have nonnegative integer arguments.

More strongly, the entire inverse fiber is characterized as follows. Every realization has exactly \(t\) cyclic zero-runs and \(t\) cyclic one-runs. Its zero-run lengths total \(at\), and if \(a\ge k-1\) each is at least \(k-1\), whereas if \(a<k-1\) each is exactly \(a\). Independently, its one-run lengths total \(bt\), and if \(b\ge k-1\) each is at least \(k-1\), whereas if \(b<k-1\) each is exactly \(b\). These conditions are both necessary and sufficient.

Consequently, for every \(t\ge2\), the shortest read length at least two that uniquely reconstructs this necklace is exactly
\[
\boxed{k_{\mathrm{unique}}=1+\max\{a,b\}.}
\]

## Assumptions and scope
All words are binary and circular; rotations are equivalent. We retain every contiguous length-\(k\) window with its multiplicity, not merely the support of the window set, and no substitutions, omissions, or orientation errors are allowed. The result holds for all positive integers \(a,b\), all \(t\ge2\), and all integers \(2\le k\le t(a+b)\). The one-symbol observation \(k=1\) and linear (noncyclic) reads are outside the stated formula.

## Proof
**1. Recover the elementary data.** The cyclic \(k\)-spectrum determines all lower-order cyclic spectra, since mapping each length-\(k\) window to its first \(j\) symbols for any \(j\le k\) counts each cyclic length-\(j\) window once. Therefore a same-spectrum word has exactly \(at\) zeros, \(bt\) ones, and precisely \(t\) occurrences each of `01` and `10`. It must consequently have exactly \(t\) runs of each symbol.

**2. Characterize allowable run lengths.** Fix a symbol \(x\in\{0,1\}\), and write \(r=a\) for \(x=0\), \(r=b\) for \(x=1\). In a circular word containing both symbols, a maximal run of \(x\) of length \(s\le k-2\) yields the factor \(\bar x x^s\bar x\), whose length is at most \(k\). Such a factor is present in \(W\) if and only if \(r=s\). Conversely a run of length at least \(k-1\) contains \(x^{k-1}\); that factor occurs in \(W\) if and only if \(r\ge k-1\). All these shorter-factor presences are determined by the \(k\)-spectrum. Thus if \(r\ge k-1\), no candidate run may be shorter than \(k-1\). If \(r<k-1\), no candidate run may reach \(k-1\), and every candidate short run must have the unique possible length \(r\). The recovered letter totals give the stated sums.

**3. Show sufficiency.** The multiset of mixed (not monochromatic) cyclic length-\(k\) factors is insensitive to redistributing symbols among runs that all remain of length at least \(k-1\): any mixed factor uses at most \(k-1\) symbols from one run, so the contexts at either end of such a run, and hence every mixed factor with its multiplicity, are unaffected. Runs shorter than \(k-1\) are fixed by step 2. For either letter \(x\), the number of monochromatic factors \(x^k\) is \(\sum_i\max\{s_i-k+1,0\}\) over its runs; under the specified conditions this equals \(t\max\{r-k+1,0\}\), independent of the allocation. Hence all factor counts agree with those of \(W\).

**4. Count the cyclic realizations.** For each color with \(r\ge k-1\), write its \(t\) run lengths as \(k-1+u_1,\ldots,k-1+u_t\). The nonnegative excesses sum to \(t(r-k+1)=t\rho_x\). For \(r<k-1\), use instead the unique fixed vector of \(t\) copies of \(r\), equivalent for counting purposes to \(t\) zero excesses. Thus the full fiber corresponds bijectively to simultaneous cyclic-rotation orbits of two nonnegative \(t\)-vectors of respective sums \(t\rho_0\) and \(t\rho_1\). A cyclic shift of order \(d\mid t\) fixes precisely the vectors obtained by repeating \(d\) copies of a vector of length \(t/d\). By stars-and-bars, the two numbers of fixed vectors are
\[
\binom{\frac td(1+\rho_0)-1}{\frac td-1}
\quad\text{and}\quad
\binom{\frac td(1+\rho_1)-1}{\frac td-1}.
\]
There are \(\varphi(d)\) shifts of order \(d\). Burnside's lemma yields the displayed formula. The bijection is valid even for imprimitive words: one necklace corresponds to precisely one orbit of alternating run-pair vectors.

**5. Prove sharpness of the read threshold.** If \(k\ge1+\max\{a,b\}\), both excess totals vanish and the inverse fiber is a singleton. If \(2\le k\le\max\{a,b\}\), at least one excess parameter is positive. For \(t\ge2\), the constant vector with all entries equal to its positive excess and the vector placing the entire excess in one entry belong to different cyclic orbits. Fix the other color's run vector to its constant value. These yield two distinct necklaces with the same spectrum, establishing the sharp threshold.

## Verification
The standalone `verify.py` uses literal cyclic-window enumeration and a separate Burnside formula implementation. It exhaustively partitions all binary necklaces through length \(16\) by every cyclic \(k\)-spectrum and checks all admissible two-run periodic inputs with \(t\ge2\); it also produces randomized valid run redistributions at larger parameter values. Actual execution:

```text
VERIFY_OK exhaustive_parameter_k_cases=568 cyclic_necklaces_examined=8914 independent_constructed_words=26160 max_exhaustive_n=16 max_constructed_t=6
```

For example, with \((a,b,t)=(3,2,2)\), the fiber sizes for \(k=2,3,4\) are \(8,2,1\). With \((a,b,t)=(4,2,3)\), the sizes for \(k=2,3,4,5\) are \(184,10,4,1\). To reproduce: run `python3 verify.py` using Python 3.9 or later. This finite verification is an independent check of the formulas, not an infinite proof; the proof is given above.

## Relationship to prior work
Gabrys and Milenkovic [1] study lossless and noisy reconstruction codes for multiset substring spectra of **linear** strings, including repeat-replacement techniques and asymptotic coding rates. That work provides a relevant reconstruction framework but does not state these exact cyclic inverse fibers. Ota and Manada [2] give a weighted-automaton approach for reconstructing **primitive** circular binary strings from factor frequencies; their explicit assumption that the full-length rotations are all distinct excludes the repeated source \((0^a1^b)^t\) when \(t\ge2\). Their uniqueness criterion is also not an exact enumeration of all inverse necklaces. Standard Eulerian graph methods explain reconstruction from factor multiplicities in general, but do not by themselves give this all-read-length closed fiber count without the run-length characterization. Related small fixed-read-length results cover subfamilies; the present assertion is the uniform exact fiber classification and threshold across all \(k\), not novelty of Burnside's lemma or of general string assembly.

## Limitations
The statement addresses the exact deterministic read multiset for one structured periodic binary source family. It does not cover arbitrary source words, noisy/incomplete reads, linear reads, or unique recovery up to reversal. The relevant 2018 and 2023 primary works do not directly state the formula in the examined material, but a differently worded result derived from generic Euler-tour counts cannot be ruled out without independent literature review.

## References
[1] R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548, first submitted April 12, 2018. https://arxiv.org/abs/1804.04548

[2] T. Ota and A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Transactions on Fundamentals, E107-A(3), 409–416 (2024); online September 5, 2023. https://doi.org/10.1587/transfun.2023TAP0015
