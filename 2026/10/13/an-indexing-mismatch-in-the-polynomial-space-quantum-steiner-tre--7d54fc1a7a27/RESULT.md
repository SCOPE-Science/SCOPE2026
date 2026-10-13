# An indexing mismatch in the polynomial-space quantum Steiner-tree tradeoff
## Finding
For dyadic terminal counts \(k=2^m\), Theorem 4 of arXiv:2510.09911v1 displays the amplitude-amplification factor
\[
T_{\mathrm{aa}}(k,\ell)=
\left[
\prod_{j=m-\ell+1}^m
\binom{k/2^{j-1}}{k/2^j}
\right]^{1/2},
\qquad 1\leq\ell\leq m.
\]
Reindexing with \(r=m-j\) gives the exact identity
\[
T_{\mathrm{aa}}(k,\ell)=
\left[
\prod_{r=0}^{\ell-1}
\binom{2^{r+1}}{2^r}
\right]^{1/2}.
\]
Thus, for fixed \(\ell\), this displayed factor is independent of \(k\). In the same derivation the exponential estimate contains
\[
\sum_{j=m-\ell+1}^m\frac{k}{2^j},
\]
but this sum is exactly
\[
2^\ell-1,
\]
not \(k(1-2^{-\ell})\). The displayed amplitude-amplification formula and the next exponential simplification therefore cannot both be correct.

Keeping the displayed factor and the paper's displayed total-cost model,
\[
T(k,\ell)=
\binom{k}{k/2^\ell}
\left(C^{k/2^\ell}+2^\ell\right)
T_{\mathrm{aa}}(k,\ell),
\]
with fixed \(C>1\), gives for every fixed \(\ell\)
\[
\lim_{m\to\infty}\frac{1}{k}\log T(k,\ell)
=
H(2^{-\ell})+2^{-\ell}\log C,
\]
where
\[
H(p)=-p\log p-(1-p)\log(1-p).
\]
More strikingly, if \(2^\ell\) is chosen within a constant factor of \(\sqrt{k\log k}\), then the same displayed cost obeys
\[
\log T(k,\ell)=O(\sqrt{k\log k}).
\]
This last consequence diagnoses the incompatibility in the displayed proof; it is not a claim that a subexponential exact Steiner-tree algorithm has been established.

## Assumptions and scope
The claim concerns exactly the formulas printed in the proof of Theorem 4 of arXiv:2510.09911v1. Restricting to \(k=2^m\) removes floor and divisibility ambiguities and is sufficient because the theorem and proof are asserted for all terminal counts. The constant \(C\) is any fixed value greater than one, as in the source's classical precomputation term. No claim is made that the source algorithm itself has subexponential running time after all implementation costs are reconstructed.

## Proof
Set \(k=2^m\). In the source product, put \(r=m-j\). As \(j\) runs from \(m-\ell+1\) through \(m\), the new index \(r\) runs from \(\ell-1\) down to zero, and
\[
\frac{k}{2^{j-1}}=2^{r+1},
\qquad
\frac{k}{2^j}=2^r.
\]
This proves the reindexed formula and fixed-\(\ell\) independence. The same substitution gives
\[
\sum_{j=m-\ell+1}^m\frac{k}{2^j}
=
\sum_{r=0}^{\ell-1}2^r
=2^\ell-1.
\]
By contrast, \(k(1-2^{-\ell})\) is the top-level sum \(\sum_{j=1}^\ell k/2^j\). Hence replacing the printed lower limit by a top-level range would repair this particular inconsistency, while retaining the printed range forces the bottom-level sum above.

For fixed \(\ell\), write \(p=2^{-\ell}\). Stirling's formula gives
\[
\frac{1}{k}\log\binom{k}{pk}\longrightarrow H(p).
\]
The reindexed \(T_{\mathrm{aa}}\) contributes \(o(k)\) to its logarithm, while
\[
\frac1k\log\left(C^{pk}+2^\ell\right)\longrightarrow p\log C.
\]
Adding the three terms proves the fixed-level rate.

For the growing-level consequence, put \(s=2^\ell\). The standard bound \(\binom{k}{k/s}\leq(es)^{k/s}\) and the central-binomial estimate \(\binom{2n}{n}\leq4^n\) imply
\[
\log T_{\mathrm{aa}}(k,\ell)
\leq(s-1)\log2.
\]
Therefore
\[
\log T(k,\ell)
=O\left(\frac{k}{s}\log s+\frac{k}{s}+\log s+s\right).
\]
Choosing a power of two \(s\asymp\sqrt{k\log k}\) yields \(O(\sqrt{k\log k})\).

## Verification
The packaged checker uses exact integer arithmetic to verify the reindexing and geometric-sum identities for many dyadic \(k\) and all allowed levels. It then evaluates logarithms of the exact displayed cost with log-gamma arithmetic, confirming convergence to the fixed-level rate and the decreasing normalized exponent in the growing-level regime. These finite calculations are corroborative; the proof above is analytic.

## Relationship to prior work
Theorem 4 of arXiv:2510.09911v1 prints the bottom-level product with indices from \(m-\ell+1\) to \(m\), then simplifies its exponent as though the product ran over the top levels. The older recursive quantum Steiner-tree analysis arXiv:1904.03581v3 explicitly uses the top-level product
\[
\binom{k}{k/2}\binom{k/2}{k/4}\cdots,
\]
whose logarithm is genuinely linear in \(k\) for a fixed positive number of top recursion levels. This provides a concrete alternative interpretation of what may have been intended, but it does not decide which formula in the newer proof should be changed.

## Limitations
The result identifies an internal inconsistency in the published complexity derivation. It does not prove Theorem 4 false, does not reconstruct every gate or oracle cost of the algorithm, and does not establish a subexponential exact Minimum Steiner Tree algorithm. A corrected proof could retain the later exponential behavior by changing the amplitude-amplification index range or could retain the displayed index range while adding costs omitted from the displayed model.

## References
1. L. Meng, D. Salvador Novo, A. H. Werner, and S. Bhatt, *Quantum Algorithms for the Minimum Steiner Tree problem with application to Binary Near-Perfect Phylogenies*, arXiv:2510.09911v1 (2025), especially Theorem 4 and its proof.
2. M. Miyamoto, M. Iwamura, K. Kise, and F. Le Gall, *Quantum Speedup for the Minimum Steiner Tree Problem*, arXiv:1904.03581v3, Appendix A.
3. F. V. Fomin, F. Grandoni, D. Lokshtanov, S. Saurabh, and M. Zehavi, *Parameterized Single-Exponential Time Polynomial Space Algorithm for Steiner Tree*, SIAM Journal on Discrete Mathematics 33 (2019), DOI:10.1137/17M1140030.
