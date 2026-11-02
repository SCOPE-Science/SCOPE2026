# The exact plateau set of the 2-adic multiplicity-restricted partition function

## Finding

Write \(P(n)\) for the number of partitions of \(n\ge0\) in which each positive part size \(m\) occurs at most \(2+\nu_2(m)\) times, where \(\nu_2(m)\) is the exponent of two in \(m\). Set \(P(-1)=0\). Let \(B(n)\) count partitions obeying these same upper bounds but using only part sizes in
\[
\mathcal A=\{m\in\mathbb Z:m\ge2\}\setminus\{3,9,27,\ldots\}.
\]
Then, for all \(n\ge0\),
\[
P(n)-P(n-1)=B(n).
\]
Thus the **complete list of positive plateau indices** is
\[
\{n\ge1:P(n)=P(n-1)\}=\{1,3\}.
\]
Equivalently, the sequence is nondecreasing everywhere and strictly increasing at every \(n\ge2\) other than \(n=3\).

## Assumptions and scope

Partitions are unordered multisets of positive integers. The empty partition is counted at zero; a negative argument has count zero. The bound \(2+\nu_2(m)\) applies separately to the multiplicity of *each* part size. The set of powers excluded from \(\mathcal A\) consists of \(3^k\) with \(k\ge1\); size one is also excluded. Every statement is exact for all nonnegative integer inputs.

## Proof

**Ternary-carry bijection.** In any partition counted by \(P(n)\), each part \(3^k\) (for \(k\ge0\)) has multiplicity \(d_k\in\{0,1,2\}\), since \(\nu_2(3^k)=0\). Keep all other parts unchanged and replace these powers-of-three parts by \(r=\sum_{k\ge0}d_k3^k\) copies of part one. This gives a partition of \(n\) with an unrestricted number of ones and all other parts in \(\mathcal A\), still within their original multiplicity bounds. Conversely, any number \(r\ge0\) of ones has a unique finite base-three expansion \(r=\sum_{k\ge0}d_k3^k\), with digits in \(\{0,1,2\}\). Replacing the ones by \(d_k\) copies of \(3^k\) reverses the map. Both maps preserve total weight and are mutually inverse.

For a fixed leftover \(\mathcal A\)-partition of weight \(j\), there is exactly one choice of \(r=n-j\) unrestricted ones for each \(n\ge j\). Hence
\[
P(n)=\sum_{j=0}^n B(j)\quad(n\ge0),
\]
where \(B(0)=1\), and subtraction gives the asserted difference identity (including the boundary \(n=0\)). Equivalently, as formal power series over the integers,
\[
(1-q)\sum_{n\ge0}P(n)q^n=
\prod_{\substack{m\ge2\\m\notin\{3,9,27,\ldots\}}}
\left(\sum_{a=0}^{2+\nu_2(m)}q^{am}\right).
\]
Only finitely many factors contribute to any fixed coefficient, so there is no convergence issue.

**Exact support.** No positive permitted part has size one, so \(B(1)=0\). The only permitted part size at most three is two, which cannot sum to three, so \(B(3)=0\). For \(n=2\), the singleton \((2)\) is allowed. For every \(n\ge4\) not a power of three, the singleton \((n)\) is allowed. For \(n=3^k\ge9\), the two-part partition \((n-2,2)\) is allowed: \(n-2\ge7\) is not a power of three because \(n-2\equiv1\pmod3\), and both multiplicities are one. Therefore \(B(n)>0\) for every \(n\ge2\) except \(n=3\), proving the sharp plateau classification.

## Verification

The standalone script `verify.py` independently calculates the restricted-partition coefficients and the coefficients after excluding all powers of three through index 512, checks the difference identity at every index, tests the exact plateau set and 5,000 ternary-digit decompositions. Run `python3 verify.py`. Output from the executed checker: `VERIFIED: independent coefficient tables 0..512, sharp plateau set, 5000 ternary conversions`.

## Relationship to prior work

Merca introduced this \(2\)-adic multiplicity-restricted partition function and its generating function in Theorem 2 of *Overpartitions in terms of 2-adic valuation* (first online September 6, 2024). The present statement determines the previously unreported *exact adjacent-equality set* and supplies a positive-coefficient interpretation for every first difference. The proof specializes the classical base-carrying/Glaisher correspondence to the entire chain of ternary powers in this size-dependent problem. Liu's work on positivity of truncated theta and pentagonal-type series (arXiv:2409.19907, sections 1 and 5) proves two different Merca conjectures, not this first-difference classification.

## Limitations

This is a theorem specifically about unweighted partition counts with multiplicity caps \(2+\nu_2(m)\); it is not a statement about Merca's binomially weighted representation of the ordinary overpartition function. The infinite identity follows from the bijection; finite program checks serve only as reproducibility checks. A general base-carrying principle underlies the proof, and unindexed prior applications to this exact function remain a priority risk. No independent scientific audit has been performed.

## References

1. Mircea Merca, *Overpartitions in terms of 2-adic valuation*, Aequationes Mathematicae 99 (2025), 1153–1173; first published online 2024-09-06. DOI: https://doi.org/10.1007/s00010-024-01117-6 (Theorem 2, Sections 3 and 6).
2. Ji-Cai Liu, *A general positivity result on coefficients of certain q-series*, arXiv:2409.19907 (2024), especially Sections 1 and 5. https://arxiv.org/abs/2409.19907.
3. G. E. Andrews, *The Theory of Partitions*, Cambridge University Press (1998), for classical Glaisher-type base-carrying bijections.
