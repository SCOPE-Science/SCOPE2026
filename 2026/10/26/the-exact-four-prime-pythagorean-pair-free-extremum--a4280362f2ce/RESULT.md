# The exact four-prime Pythagorean-pair-free extremum

## Finding
Let \(p_1=2,p_2=3,p_3=5,p_4=7\), and define
\[
\Phi_4=\{2^a3^b5^c7^d:0\le a,b,c,d<4\}.
\]
A subset \(A\subseteq\Phi_4\) is *admissible* when there are no distinct \(u,v\in A\) for which \(u^2+v^2=w^2\) for some positive integer \(w\). The hypotenuse is unrestricted. The exact extremal cardinality, in the notation of Xiao, is
\[
\boxed{f(4)=\max_{A\subseteq\Phi_4\;\mathrm{admissible}}|A|=144.}
\]
Thus the maximum proportion is \(9/16\). A finite, reproducible certificate proves both the upper and lower bounds; it is not a sampling estimate.

## Assumptions and scope
Exponents are integers in \(\{0,1,2,3\}\), all values are positive integers, and both legs must be distinct members of the four-prime box. The third side of a right triangle need not be in the box. Only this precisely specified finite box is classified. The primary subject is number theory (MSC2020 11B30).

## Proof
Label the \(256\) distinct box elements by indices
\[
i=64a+16b+4c+d,\qquad v_i=2^a3^b5^c7^d,
\quad 0\le a,b,c,d<4.
\]
Define a graph \(G\) on \(\{0,\ldots,255\}\), with an edge \(\{i,j\}\), \(i<j\), precisely when \(v_i^2+v_j^2\) is a perfect square. Then the admissible subsets of the box are exactly the independent vertex sets in \(G\).

`CERTIFICATE.json` contains two explicit finite mathematical witnesses: an array `independent_indices` of \(144\) pairwise nonadjacent vertices, and an array `disjoint_edges` of \(112\) edges no two of which share a vertex. The accompanying `verify.py` reconstructs all \(256\) values and tests every one of the \(\binom{256}{2}=32640\) unordered index pairs by *integer square root*; it does not approximate any square root by floating point. It checks that precisely \(408\) pairs are edges, then checks directly that the stated \(144\) indices are distinct and span no edge and that all \(112\) listed pairs are distinct genuine edges with disjoint endpoints. Each check is an exhaustive finite integer assertion whose executable specification is included in the two files.

The independent set proves \(f(4)\ge144\). Conversely, any admissible subset can contain at most one endpoint from each of the \(112\) disjoint edges. Among \(256\) vertices this forces at least \(112\) exclusions, so \(f(4)\le256-112=144\). These inequalities prove the result. No optimal-matching solver, unverified optimization output, or graph-theoretic black box is required to check the witnesses.

## Verification
Run `python3 verify.py CERTIFICATE.json` in a directory containing both files. The independently rerun checker printed:

`CERTIFICATE_OK vertices=256 edges=408 matching_edges=112 independent_vertices=144 components=13`

The supplementary connected-component census is one component of size \(242\), two components of size \(2\), and ten isolated vertices. It is not used in the extremal proof. The proof is finite exhaustive: all potential pairs are checked, and the checked edge and independent-set witnesses jointly prove the exact optimum.

## Relationship to prior work
R. Xiao's October 2026 papers explicitly define \(f(N)\) for the same prime-power boxes and the same condition on distinct Pythagorean legs. *Pythagorean pairs in boxes of prime powers* (arXiv:2610.11965v1, first public 2026-10-08) establishes an upper-density estimate for sufficiently large \(N\). *Quantitative lower bound for Pythagorean pairs in boxes of prime powers* (arXiv:2610.20311v1, first public 2026-10-14) supplies an asymptotic lower bound. Their inspected main results do not determine this explicit finite value. The present claim is only the finite endpoint \(N=4\), not a strengthening of those asymptotic results.

## Limitations
The calculation does not determine \(f(N)\) for general \(N\), or imply an asymptotic density. An equivalent finite calculation could have appeared in unindexed sources. The certificate is mechanically reproducible by ordinary integer arithmetic; independent mathematical auditing has not been performed.

## References
1. R. Xiao, *Pythagorean pairs in boxes of prime powers*, arXiv:2610.11965v1 (2026-10-08), https://arxiv.org/abs/2610.11965.
2. R. Xiao, *Quantitative lower bound for Pythagorean pairs in boxes of prime powers*, arXiv:2610.20311v1 (2026-10-14), https://arxiv.org/abs/2610.20311.
