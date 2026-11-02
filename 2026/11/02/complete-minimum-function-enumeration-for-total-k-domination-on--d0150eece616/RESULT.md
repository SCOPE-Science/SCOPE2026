# Complete minimum-function enumeration for total \(\{k\}\)-domination on paths

## Finding
For every integer \(n\ge2\) and \(k\ge1\), let \(M_{n,k}\) be the number of labelled minimum-weight total \(\{k\}\)-dominating functions of the path \(P_n\). Then
\[
M_{n,k}=\begin{cases}
1,&n=4s,\ s\ge1,\\
\binom{k+s-1}{s-1},&n=4s+1,\ s\ge1,\\
\binom{k+s}{s}^{2},&n=4s+2,\ s\ge0,\\
\binom{k+s+1}{s+1},&n=4s+3,\ s\ge0.
\end{cases}
\]
More precisely, in those four residue classes the set of minimum functions is lattice-bijective, respectively, to a point, the integer points of \(k\Delta_{s-1}\), the integer points of \(k(\Delta_s\times\Delta_s)\), and the integer points of \(k\Delta_{s+1}\), where \(\Delta_d=\{(t_0,\ldots,t_d)\in\mathbb R_{\ge0}^{d+1}:\sum_i t_i=1\}\). These bijections explicitly reconstruct all vertex labels. For \(s=0\) the two smallest orders \(n=2,3\) obey the displayed formulas.

The minimum total weights, previously known, are \(2sk\), \((2s+1)k\), \(2(s+1)k\), and \(2(s+1)k\), in the same four classes. Novelty here concerns the *complete set and multiplicity of minimizers*, not the minimum values.

## Assumptions and scope
The path \(P_n\) has labelled vertices \(v_1,\ldots,v_n\) in linear order. A total \(\{k\}\)-dominating function is a function \(f:V(P_n)\to\{0,1,\ldots,k\}\) satisfying \(\sum_{u\in N(v)}f(u)\ge k\) for every vertex \(v\), where \(N(v)\) is the *open* neighborhood. Its weight is \(w(f)=\sum_i f(v_i)\); the minimum is \(\gamma_t^{\{k\}}(P_n)\). Different vectors of labels count as different functions; no quotient by reversal is taken. All formulas hold for the full stated infinite ranges, without asymptotic qualifications.

## Proof
**Parity decomposition.** Write \(f_i=f(v_i)\). The first and last neighborhood inequalities force \(f_2=k\) and \(f_{n-1}=k\) (including \(n=2\), when both vertices are forced). Every interior inequality is exactly \(f_{i-1}+f_{i+1}\ge k\). Thus the subsequences on odd and even indices are independent chains: each is a sequence \((x_1,\ldots,x_m)\) with \(0\le x_i\le k\), all \(x_i+x_{i+1}\ge k\), and zero, one, or both endpoints prescribed equal to \(k\). The objective is the sum of the two chain weights. There are no remaining cross-parity constraints.

**Complete auxiliary-chain lemma.** For a chain of length \(m=2r\ge2\), the minimum weight and number of minimizing integer sequences are:

| Prescribed endpoints | Minimum weight | Number |
| --- | --- | --- |
| Neither | \(rk\) | \(\binom{k+r}{r}\) |
| Exactly one | \(rk\) | \(1\) |
| Both | \((r+1)k\) | \(\binom{k+r-1}{r-1}\) |

For \(m=2r+1\ge3\) they are:

| Prescribed endpoints | Minimum weight | Number |
| --- | --- | --- |
| Neither | \(rk\) | \(1\) |
| Exactly one | \((r+1)k\) | \(\binom{k+r}{r}\) |
| Both | \((r+1)k\) | \(1\) |

For \(m=1\), the unconstrained sequence has unique optimum \(0\), and any prescribed endpoint yields unique optimum \(k\).

Here are proofs and explicit parametrizations, not just counts. If \(m=2r\) has no prescribed ends, summing the disjoint constraints \(x_{2j-1}+x_{2j}\ge k\) gives the lower bound \(rk\). Equality demands every pair be tight. Set \(x_{2j-1}=a_j\), \(x_{2j}=k-a_j\); the remaining inequalities are exactly \(0\le a_1\le\cdots\le a_r\le k\). If only the first endpoint is forced, equality still demands tight pairs and the initial condition \(a_1=k\); monotonicity forces every \(a_j=k\), giving a unique alternating sequence. For only the last endpoint reverse the chain. If both ends are forced, use the disjoint lower bound from the two singleton endpoints \(x_1+x_{2r}=2k\) and the \(r-1\) pairs \(x_2+x_3,\,x_4+x_5,\ldots,x_{2r-2}+x_{2r-1}\). Equality gives \(x_{2j}=a_j\), \(x_{2j+1}=k-a_j\) for \(1\le j\le r-1\), and all remaining inequalities amount to \(0\le a_1\le\cdots\le a_{r-1}\le k\).

If \(m=2r+1\) has no prescribed endpoints, sum the \(r\) disjoint constraints \(x_2+x_3, x_4+x_5,\ldots,x_{2r}+x_{2r+1}\ge k\) and \(x_1\ge0\). Equality forces \(x_1=0\), \(x_2=k\), and then alternately \(x_3=0,x_4=k,\ldots,x_{2r+1}=0\), uniquely. If the first endpoint is prescribed \(k\), the same \(r\) paired inequalities together with \(x_1=k\) yield the lower bound \((r+1)k\). Equality gives \(x_{2j}=a_j\), \(x_{2j+1}=k-a_j\), with \(0\le a_1\le\cdots\le a_r\le k\). Prescribing only the last endpoint is the reversed case. With both endpoints prescribed \(k\), equality in the latter disjoint sum forces the last paired coordinate \(x_{2r}=0\), and all preceding pairs alternate \(k,0\) backwards; the minimizing sequence is unique. Explicit alternating sequences attain each of the stated lower bounds, completing the lemma.

For each integer \(d\ge0\), weak compositions of \(k\) into \(d+1\) parts are in bijection with monotone integer strings \(0\le a_1\le\cdots\le a_d\le k\) by successive differences \(a_1,a_2-a_1,\ldots,a_d-a_{d-1},k-a_d\). Hence the number is \(\binom{k+d}{d}\), and the parametrizations above identify the lattice-simplex structures exactly.

**Combine the chains.** If \(n=4s\), each parity chain has \(2s\) entries and exactly one prescribed endpoint, hence each has a unique minimizer. If \(n=4s+1\), the odd chain has \(2s+1\) entries and no prescribed endpoint (unique), while the even chain has \(2s\) entries and both endpoints prescribed, giving \(\binom{k+s-1}{s-1}\). If \(n=4s+2\), both parity chains have \(2s+1\) entries and exactly one prescribed endpoint (with the \(n=2\) singleton case interpreted directly); each contributes \(\binom{k+s}{s}\). If \(n=4s+3\), the odd chain has \(2s+2\) entries and neither endpoint prescribed, giving \(\binom{k+s+1}{s+1}\), while the even chain has \(2s+1\) entries with both endpoints prescribed and contributes one. Multiplying the independent multiplicities and adding minimum weights proves all statements.

## Verification
A standalone Python program `verify.py` independently computes optimum weights and numbers of optimum solutions by dynamic programming **directly on the original path neighborhood inequalities**. It matches the formulas for every \(2\le n\le80\) and \(1\le k\le12\), a total of \(948\) pairs. A second exhaustive enumeration of literal vertex-label vectors verifies \(31\) bounded cases with \(2\le n\le10\) and \(1\le k\le4\). The extracted packaged script prints `DP_MATCH 948 cases`, `EXHAUSTIVE_MATCH 31 cases`, and `VERIFY_OK`. Both checks test finite ranges only; the preceding disjoint-inequality proof and equality characterization establish the infinite theorem.

Examples: \(M_{6,3}=16\), \(M_{9,5}=6\), \(M_{10,7}=1296\), \(M_{18,4}=4900\).

## Relationship to prior work
Tan, Liu, and Liang (2018), Theorem 2.2, gives \(\gamma_t^{\{k\}}(P_n)\) and exhibits optimal functions for each residue class. That prior optimum-weight formula is used for context only; its proof does not enumerate *all* minimizing functions or give the simplex-product families. Escalante, Tolomei, and Lopez Pujato (first public preprint October 19, 2026) establish the total \(\{k\}\)-domination number of caterpillars as a multiple of their ordinary total domination number. A complete version of this new manuscript was not available for inspection; its abstract does not assert a path minimum-function enumeration, but omission from an abstract cannot exclude overlap. The present theorem is the exact multiplicity and parametrization of minimizers for the basic path family, rather than a new minimum-weight identity.

## Limitations
No assertion is made about minimizer counts for general caterpillars, cycles, or graphs with branching, nor about all nonminimum feasible functions. Priority remains provisional because the recent caterpillar preprint was abstract-accessible only and earlier equivalent enumerations under different terminology may exist. No independent audit has been completed.

## References
1. H. Tan, L. Liu, and H. Liang, “Total \(\{k\}\)-domination in special graphs,” *Mathematical Foundations of Computing* **1** (2018), 255–263, DOI: 10.3934/mfc.2018011. Primary full-text Theorem 2.2 (paths).
2. M. Escalante, P. Tolomei, and M. I. Lopez Pujato, “Total \(\{k\}\)-domination in caterpillars: Structural properties and exact results,” arXiv:2610.27181v1, first public October 19, 2026. Abstract and public metadata were accessible; full text not inspected.
