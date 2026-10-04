# A 64-member covering family for \([5]^5\) and a sharper DP-colouring threshold
## Finding
There exists an explicit covering family of \([5]^5\) with 64 members. Consequently,
\[
\kappa(5)\le 64.
\]
Kaul, Mudrock, Psyhogios, Sharma, Siutkin, and Upadhyay proved that \(\mu(\ell)=\kappa(\ell)\) for every positive integer \(\ell\). Hence
\[
\mu(5)\le64,
\]
and therefore
\[
\chi_{\mathrm{DP}}(K_{5,t})=6\qquad\text{for every integer }t\ge64.
\]
Their lower-bound theorem gives \(\mu(5)\ge28\), so the currently certified interval becomes
\[
28\le\mu(5)\le64.
\]

## Assumptions and scope
Write \([5]=\{1,2,3,4,5\}\), and let \(S_5\) be the symmetric group on \([5]\). A covering family for \([5]^5\) is a set \(\mathcal F\subseteq S_5^5\) such that, for every \(x=(x_1,\ldots,x_5)\in[5]^5\), some \((\sigma_1,\ldots,\sigma_5)\in\mathcal F\) makes the five values \(\sigma_1(x_1),\ldots,\sigma_5(x_5)\) pairwise distinct. The parameter \(\kappa(5)\) is the minimum possible size of such a family. The parameter \(\mu(5)\) is the least integer \(t\) for which \(\chi_{\mathrm{DP}}(K_{5,t})=6\).

The claim is an upper bound, not an exact determination of either parameter. The explicit certificate is stored in `covering_family_5.json`.

## Proof
The certificate `covering_family_5.json` lists 64 ordered five-tuples of permutations of \([5]\). For each of the \(5^5=3125\) tuples \(x\in[5]^5\), direct exhaustive evaluation finds at least one listed five-tuple of permutations for which the five images of the coordinates of \(x\) are pairwise distinct. Thus the listed set is a covering family and \(\kappa(5)\le64\).

Theorem 7 of Kaul et al. establishes \(\mu(\ell)=\kappa(\ell)\) for every positive integer \(\ell\). Applying it at \(\ell=5\) yields \(\mu(5)\le64\). By the definition of \(\mu(5)\), this is equivalent to the stated DP-colouring threshold \(\chi_{\mathrm{DP}}(K_{5,t})=6\) for every integer \(t\ge64\).

For context, their lower-bound theorem with \(\ell=5\) and \(s=2\) gives
\[
\mu(5)\ge
\left\lceil
\frac{2!\,5^3}{5!}
\left\lceil\frac{5^2}{2!}\right\rceil
\right\rceil
=28.
\]
No new lower bound is claimed here.

## Verification
The standalone script `verify_covering_family.py` checks that the certificate has exactly 64 distinct members, that every coordinate is a permutation of \([5]\), and that all \(3125\) points of \([5]^5\) are covered. Its exhaustive replay reports

`ALL CHECKS PASSED; family_size=64; tuples=3125; minimum_coverage=1; maximum_coverage=8`

The coverage multiplicities range from 1 to 8. This finite verification proves the certificate claim exactly; it is not an asymptotic or sampled computation. The transfer from \(\kappa(5)\) to \(\mu(5)\) uses the published theorem cited above.

## Relationship to prior work
The September 27, 2026 preprint of Kaul et al. introduces the covering-family formulation, proves \(\mu(\ell)=\kappa(\ell)\), determines \(\mu(4)=12\), and records the exact value of \(\mu(5)\) as unknown. Its table gives the upper bound \(\mu(5)\le134\). The 64-member certificate therefore lowers that published upper bound from 134 to 64.

Mudrock's earlier complete-bipartite DP-colouring bound implies a weaker upper bound at \(k=5\). Neither the initiating paper nor the earlier complete-bipartite threshold result contains the 64-member family or an implication yielding the bound \(64\). Searches under the covering-family, DP-colouring threshold, complete-bipartite, and permutation-family formulations located no stronger published bound for \(\mu(5)\).

## Limitations
The result does not determine \(\mu(5)\) exactly and does not improve the published lower bound \(28\). It makes no optimality claim for the 64-member family. A residual literature risk remains that an equivalent or stronger construction exists under terminology not retrieved by the checked searches. The DP-colouring consequence depends on the published identity \(\mu(5)=\kappa(5)\); the covering certificate itself is independently replayable from the included files.

## References
1. H. Kaul, J. A. Mudrock, E. A. Psyhogios, G. Sharma, I. Siutkin, and A. Upadhyay, *Covering Families for DP-Coloring of Cartesian Products with Complete Bipartite Graphs*, arXiv:2609.33966v1, first public version September 27, 2026.
2. J. A. Mudrock, *A Note on the DP-Chromatic Number of Complete Bipartite Graphs*, arXiv:1803.09141; Discrete Mathematics 341 (2018), 3143--3151, DOI 10.1016/j.disc.2018.08.003.
