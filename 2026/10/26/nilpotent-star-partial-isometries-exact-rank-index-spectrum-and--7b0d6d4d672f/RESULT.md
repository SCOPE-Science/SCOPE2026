# Nilpotent star partial isometries: exact rank-index spectrum and a Gumbel extremal law

## Finding

Let \(S_{m+1}\) be the star on labeled vertices \(\{0,1,\ldots,m\}\), with hub \(0\), where \(m\ge1\). Denote by \(D(S_{m+1})\) its inverse monoid of partial distance-preserving bijections. For a nilpotent partial bijection \(f\), write \(r(f)=|\operatorname{dom} f|\) and \(\nu(f)=\min\{j\ge1:f^j=\varnothing\}\). Set
\[
E_{\ell}(x,u)=\exp\!\left(\sum_{j=1}^{\ell}x^j u^{j-1}\right),\qquad E_0(x,u)=1.
\]
The exact joint rank–nilpotency-index polynomial is
\[
\boxed{\sum_{\substack{f\in D(S_{m+1})\\ f\text{ nilpotent}}}u^{r(f)}v^{\nu(f)}
= m!\sum_{\ell=1}^{m}v^\ell[x^m]\bigl(E_\ell(x,u)-E_{\ell-1}(x,u)\bigr)
+2muv^2+m(m-1)u^2v^3.}
\]
In particular, the number of nilpotents is
\[
\boxed{m![x^m]\exp\!\left(\frac{x}{1-x}\right)+m(m+1).}
\]
A uniformly sampled nilpotent element \(F_m\) satisfies the following Gumbel limit for every real \(s\):
\[
\boxed{\lim_{m\to\infty}\Pr\left(\frac{\nu(F_m)-\frac12\sqrt m\log m}{\sqrt m}\le s\right)=\exp(-e^{-s}).}
\]
Thus the exceptional hub-involving nilpotents contribute two low-index atoms at finite sizes, but the typical largest chain has a \(\frac12\sqrt m\log m\) location and \(\sqrt m\) Gumbel fluctuations.

## Assumptions and scope

The star has one distinguished hub and \(m\) distinct leaves. All partial maps are injective and preserve all pairwise shortest-path distances on their domains, with composition of partial maps as monoid multiplication. Zero is the empty map. Every singleton leaf not in a domain or image is regarded as a length-one chain in the standard directed-path decomposition. The coefficient notation \([x^m]\) means extraction of the formal coefficient of \(x^m\). The theorem holds for every integer \(m\ge1\); the limit concerns uniformly distributed nilpotent maps among the finitely many nilpotents.

## Proof

**1. Exhaustive structural split.** Distances between distinct leaves are two, while the hub-to-leaf distance is one. A partial isometry of rank at least three either avoids the hub in both domain and image, or fixes the hub and maps leaves injectively to leaves. At rank two, an isometry with a hub in its domain must also have a hub in its image. Such a map either fixes the hub or has the form \(0\mapsto j,\ i\mapsto0\), with leaves \(i,j\). Rank-one isometries are arbitrary single arrows. Hence every nilpotent partial isometry is precisely one of: (i) a nilpotent partial injection supported entirely on the \(m\) leaves; (ii) one of the \(2m\) single arrows between a leaf and the hub; (iii) one of the \(m(m-1)\) length-two directed paths \(i\mapsto0\mapsto j\), for distinct leaves \(i,j\). Maps fixing the hub and two-cycles through it cannot be nilpotent. These three classes are disjoint. The extra classes have respective \((r,\nu)\) values \((1,2)\) and \((2,3)\).

**2. Exact enumerator.** A cycle-free partial injection on \(m\) labeled points consists of an unordered set of oriented chains, including isolated vertices as chains of size one. On a prescribed \(j\)-vertex set, there are \(j!\) linear orders, hence its labeled exponential generating function is \(x^j\). Such a chain has rank \(j-1\); the whole map has rank equal to the sum of these chain ranks and nilpotency index equal to the largest chain size. The exponential formula therefore gives \(E_\ell(x,u)\) for chain collections with largest size at most \(\ell\). Subtraction of \(E_{\ell-1}\) isolates index \(\ell\). Adding the exceptional hub classes proves the polynomial. Setting \(u=v=1\) and summing telescopically proves the total count.

**3. Conditioned Poisson representation.** Put \(a_m=m![x^m]\exp(x/(1-x))\), the number of cycle-free partial injections. Choose \(\rho_m\in(0,1)\) uniquely so that \(\rho_m/(1-\rho_m)^2=m\). Then \(1-\rho_m=m^{-1/2}+O(m^{-1})\). Let \(Z_j\), for integers \(j\ge1\), be independent Poisson variables with means \(\rho_m^j\), and let \(T=\sum_{j\ge1}jZ_j\). The exponential-formula coefficient weights show that, conditional on \(T=m\), the random vector of chain multiplicities has exactly the law of the chain multiplicities of a uniform cycle-free partial injection on \(m\) labels. Direct geometric-series differentiation yields
\[
\mathbb E T=m,\qquad \operatorname{Var}(T)=\frac{\rho_m(1+\rho_m)}{(1-\rho_m)^3}\sim2m^{3/2}.
\]

**4. Local conditioning estimate.** Fix \(s\in\mathbb R\), let \(L_m=\lfloor\sqrt m(\frac12\log m+s)\rfloor\), and write \(T_{\le L}=\sum_{j\le L}jZ_j\). The tail has
\[
\mathbb E(T-T_{\le L})=O(\sqrt m\log m),\qquad
\operatorname{Var}(T-T_{\le L})=O(m(\log m)^2),
\]
so both quantities are negligible at the full standard-deviation scale \(m^{3/4}\). Moreover, a lattice local central limit estimate gives
\[
\Pr(T=m)\sim\Pr(T_{\le L_m}=m)\sim\frac{1}{\sqrt{4\pi}\,m^{3/4}}.
\]
For completeness, these local estimates follow by Fourier inversion from the explicit characteristic functions \(\exp(\sum_{j\in J}\rho_m^j(e^{ijt}-1))\): on \(|t|\le m^{-3/4+\varepsilon}\), cumulant expansion gives the common centered Gaussian integral because the third absolute cumulant is \(O(m^2)\); outside this arc, the real exponent is bounded by \(-c\min(m^{3/2}t^2,\sqrt m)\) using only \(1\le j\le\lfloor\sqrt m\rfloor\), which are included in both \(J\) sets for large \(m\). Any fixed \(0<\varepsilon<1/12\) controls the cubic remainder. This proves the local estimates with no extrapolation from finite experiments.

**5. Extreme value and hub correction.** Independence and conditioning give
\[
\Pr(\max\{j:Z_j>0\}\le L_m\mid T=m)
=\exp\!\left(-\sum_{j>L_m}\rho_m^j\right)
\frac{\Pr(T_{\le L_m}=m)}{\Pr(T=m)}.
\]
The probability ratio tends to one, while \(\sum_{j>L_m}\rho_m^j=\rho_m^{L_m+1}/(1-\rho_m)\to e^{-s}\). The maximum chain size consequently converges, under the stated centering and scaling, to the standard Gumbel law. Finally, \(a_m\ge m!\) because all Hamiltonian directed paths are counted, whereas the total number of exceptional hub-involving nilpotents is only \(m(m+1)\). Their probability tends to zero, and their indices stay at two or three. The same limiting law therefore holds for uniform nilpotent star partial isometries.

## Verification

The standalone file `verify_star_nilpotent.py` enumerates every partial injection on labeled stars of orders two through seven, checks pairwise metric preservation directly, computes each power until either the empty map or a nonzero cycle is detected, and compares the complete rank/index frequency table with an independent enumeration of labeled sets of directed chains plus the two hub corrections. Exact agreement was obtained for all six tested leaf counts \(m=1,\ldots,6\): nilpotent totals \(3,9,25,93,531,4093\). Separately, exact coefficient recurrences for the truncated and untruncated exponential series at sizes \(100,500,2000\) numerically corroborated the stated Gumbel scaling; the proof of the limiting distribution does not rely on those finite numerical comparisons.

## Relationship to prior work

Fernandes and Paulista (first posted 2022-03-10) defined this star partial-isometry monoid and classified its elements by hub behavior in Proposition 2.1, as well as studying Green's relations, cardinality, rank, and presentations. The structural hub split here is credited to that work; it is not claimed as a new classification of all monoid elements. The assessed result is instead the complete nilpotent rank/index enumerator and, principally, the Gumbel limit for the nilpotency index under the natural uniform nilpotent measure. Stark (2021) studied component counts and maximal path sizes of random injections under a fixed-domain/codomain model, rather than this uniform nilpotent star inverse-monoid model or its exact limit law. The chain assembly exponential formula and the use of conditioned Poisson variables are standard combinatorial tools, not claimed as independent innovations.

## Limitations

The conclusion concerns labeled finite stars, not arbitrary graphs or all partial injections without the nilpotency condition. The Gumbel assertion is asymptotic as the number of leaves tends to infinity and supplies no uniform numerical error bound at finite size. Generic theorems on extremes of expansive combinatorial assemblies may subsume the conditional-Poisson limit mechanism; exhaustive bibliographic priority is not asserted. Direct finite verification is corroboration only and does not certify the proof independently.

## References

1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (first posted 2022-03-10); *Communications in Algebra* 51 (2023), 1028–1048; DOI 10.1080/00927872.2022.2121404.
2. D. Stark, *The component counts of random injections*, *Electronic Journal of Combinatorics* 28 (2021), paper P1.5, DOI 10.37236/9496.
