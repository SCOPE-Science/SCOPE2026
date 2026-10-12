# An all-or-nearly-even release theorem for two-site mate-limited establishment

## Finding

Let \(n\geq1\) males and \(n\) females be released across two distinct candidate habitats. Each founder independently survives the initial establishment bottleneck with probability \(0<p<1\); independently, each habitat is suitable with probability \(0<r\leq1\). A habitat counts as viable exactly when it is suitable and retains at least one founder of each sex. The objective is the probability that at least one habitat is viable. If the first habitat receives \(m\) males and \(f\) females, write this objective as \(P_n(m,f;p,r)\).

**Complete optimization theorem.** Every maximizing allocation is sex-balanced within each habitat. More precisely, for \(0<r<1\) and \(n\geq2\), all maximizers belong to the two classes, with site labels interchangeable:

1. **Concentration:** all \(n\) males and all \(n\) females at one habitat;
2. **Nearly-even paired division:** \(\lfloor n/2\rfloor\) males and as many females at one habitat, and \(\lceil n/2\rceil\) of each at the other.

There are no other maximizing allocations. Which class is optimal is determined exactly by the sign of
\[
\Delta_n(p,r)=r\bigl[a+b-c-rab\bigr],\quad
 a=\bigl(1-(1-p)^{\lfloor n/2\rfloor}\bigr)^2,\quad
 b=\bigl(1-(1-p)^{\lceil n/2\rceil}\bigr)^2,\quad
 c=\bigl(1-(1-p)^n\bigr)^2.
\]
When \(\Delta_n>0\), division alone is optimal; when \(\Delta_n<0\), concentration alone is optimal; and when \(\Delta_n=0\), precisely those two classes tie. If \(r=1\), concentration is always the only class of optimizers. For \(n=1\), division is equivalent to concentration up to habitat exchange.

For the **even founder budget** \(n=2k\), \(k\geq1\), and \(0<r<1\), this becomes a single sharp threshold. Set
\[
 z_*(r)=\frac{\sqrt{2(1-r)}-(1-r)}{1+r},\qquad
 p_*(k,r)=1-z_*(r)^{1/k}.
\]
Then concentration is uniquely optimal (up to habitat exchange) for \(0<p<p_*\), the two classes tie at \(p=p_*\), and equal division of the \(k\) pairs is uniquely optimal (up to habitat exchange) for \(p_*<p<1\). For fixed \(r\in(0,1)\), \(p_*(k,r)\sim-\log z_*(r)/k\) as \(k\to\infty\). Thus this finite model has an exact founder-budget threshold for the change from concentrating mate availability to insuring against independent habitat failure.

## Assumptions and scope

The two habitats are not connected by migration during the bottleneck. Suitability events at the two habitats are independent and identically distributed with probability \(r\). Founder survival events are independent and identically distributed with probability \(p\), independent of suitability. Sexes of the founders are fixed and known; exactly \(n\) founders of each sex are available. All integer assignments \((m,f)\in\{0,\ldots,n\}^2\) are admissible, including empty habitats. At least one surviving male and female is a **one-step viability proxy**; it does not assert subsequent reproduction or long-term population persistence.

Put \(t=1-p\). For any admissible allocation, independence gives the exact success probability
\[
P_n(m,f;p,r)=1-\left[1-r(1-t^m)(1-t^f)\right]
\left[1-r(1-t^{n-m})(1-t^{n-f})\right].
\]
The theorem applies to all positive integers \(n\), all \(0<p<1\), and all \(0<r\leq1\). The endpoints \(p=0,1\) and \(r=0\), where additional ties arise, are deliberately excluded.

## Proof

**1. Balancing the sexes at a fixed habitat size.** Fix the number \(s=m+f\) released into the first habitat. Its probability of retaining both sexes, conditional on suitability, is
\[
 g_1=1-t^m-t^f+t^s.
\]
The corresponding probability for the second habitat is
\[
 g_2=1-t^{n-m}-t^{n-f}+t^{2n-s}
 =1-t^{n-s}(t^m+t^f)+t^{2n-s}.
\]
Because \(0<t<1\), the strictly convex function \(x\mapsto t^x\) shows that \(t^m+t^f\), at fixed integral sum \(s\), is uniquely minimized when \(|m-f|\leq1\). This simultaneously maximizes \(g_1\) and \(g_2\), and the overall probability \(1-(1-rg_1)(1-rg_2)\) is strictly increasing in either \(g_i\) when the other is less than one. Thus any global optimum has \(|m-f|\leq1\) within the first habitat (and hence within the second).

**2. Removing odd-sized habitats.** For an odd first-habitat size \(s=2j+1\), the sex-balanced allocations are \((j,j+1)\) and its transpose. Compare the adjacent paired allocations \((j,j)\) and \((j+1,j+1)\). Define
\[
 a=(1-t^j)^2,\quad b=(1-t^{j+1})^2,\quad
 c=(1-t^{n-j})^2,\quad d=(1-t^{n-j-1})^2.
\]
The odd allocation has failure probability
\[
 L_{\mathrm{odd}}=(1-r\sqrt{ab})(1-r\sqrt{cd}),
\]
whereas the two adjacent paired allocations have failure probabilities \(L_j=(1-ra)(1-rc)\) and \(L_{j+1}=(1-rb)(1-rd)\). For any \(0\leq u,v\leq1\),
\[
 (1-r\sqrt{uv})^2-(1-ru)(1-rv)
 =r(\sqrt{u}-\sqrt{v})^2\geq0.
\]
Applying this separately to \((a,b)\) and \((c,d)\) yields \(L_{\mathrm{odd}}\geq\sqrt{L_jL_{j+1}}\geq\min\{L_j,L_{j+1}\}\). Both applications are strict for \(p,r\in(0,1)\) because \(a\ne b\) and \(c\ne d\). They are also strict for \(r=1\) when probabilities stay positive, as they do for \(0<p<1\). Hence no odd-sized allocation is globally optimal. Every optimizer must have \(m=f=j\) for some integer \(0\leq j\leq n\).

**3. Reducing the paired allocations to two endpoints.** By symmetry restrict to \(0\leq j\leq\lfloor n/2\rfloor\). Put \(z=t^j\), \(w=t^{n-j}\), \(T=zw=t^n\), \(S=z+w\), and \(F(z)=1-r(1-z)^2\). The failure probability for this paired allocation is \(F(z)F(w)\). Direct expansion using \(zw=T\) yields
\[
\begin{aligned}
F(z)F(w)={}&-r(1-r)S^2
+[2r(1-r)-2r^2T]S\\
&+(1-r)^2+2r(1-r)T+4r^2T+r^2T^2.
\end{aligned}
\]
For \(0<r<1\) this is a **strictly concave quadratic in \(S\)**. Since \(0<t<1\), the values \(S_j=t^j+t^{n-j}\) strictly decrease as \(j\) runs from \(0\) to \(\lfloor n/2\rfloor\). A strictly concave function attains its minimum on this finite ordered set only at one or both extreme \(S\)-values: \(j=0\) or \(j=\lfloor n/2\rfloor\). Minimizing failure is maximizing success. At \(r=1\) the same expression reduces to \(T(4+T-2S)\), which is strictly decreasing in \(S\), so \(j=0\) alone minimizes failure. This completes the global classification, including the exclusion of any third optimum.

**4. Exact comparison and even-budget transition.** At the paired near-half allocation put \(k=\lfloor n/2\rfloor\) and \(\ell=\lceil n/2\rceil\). The probabilities of success are
\[
P_{\mathrm{division}}=r(a+b)-r^2ab,
\qquad P_{\mathrm{concentration}}=rc,
\]
with \(a,b,c\) as in the Finding. Their difference is precisely \(\Delta_n\), establishing the exact decision rule for both parities. If \(n=2k\), set \(z=t^k\); then
\[
\Delta_{2k}=r(1-z)^2\bigl[2-(1+z)^2-r(1-z)^2\bigr].
\]
The bracket equals \((1-r)-2(1-r)z-(1+r)z^2\), which for \(0<r<1\) decreases strictly from a positive value at \(z=0\) to \(-2\) at \(z=1\). Its unique root in \((0,1)\) is \(z_*(r)\) above. Because \(z=(1-p)^k\) strictly decreases with \(p\), the stated transition follows. The asymptotic formula follows from \(1-\exp((\log z_*)/k)\sim-\log z_*/k\). All claims are proved for arbitrary integer founder numbers without extrapolating a finite census.

## Verification

The reproducibility program `check.py` (Python standard library only) calculates the exact probability using rational arithmetic and exhaustively compares all \((n+1)^2\) allocations for every \(1\leq n\leq12\) at sixteen rational \((p,r)\)-pairs. It checks the theorem's set of possible optimizers, the general contrast identity, and the even-budget factored identity. It also checks both sides of the smallest nontrivial transition with \(n=2\) and \(r=1/2\), where \(p_*=2/3\). On execution it reports `VERIFY_OK exact_profiles= 13088 population_sizes=1..12 parameter_pairs=16 special_transition=1`. The finite tests are supplementary to the quantified algebraic proof above.

## Relationship to prior work

Grevstad (1999) modeled the competing effects of environmental variability and Allee limitation on the size and number of biological-control releases; its published abstract reports regimes favoring one large release, many small releases, and an intermediate release size. Jerde, Bampfylde, and Lewis (2009) developed a hierarchical model of establishment for sexual species. Duncan et al. (2014) derived explicit one-location establishment relationships in heterogeneous environments, and Cassey, Prowse, and Blackburn (2014) simulated alternative introduction regimes in birds. These establish the biological motivation and broader model families, not the exact allocation theorem proved here. Koontz et al. (2018) report experiments and simulations with sequential introductions through time, a different decision problem. The present model fixes **two independent simultaneous habitats, known founder sexes, a one-step mating feasibility event, and one independent binary suitability shock per habitat**. It proves the complete global set of optimizers and the sharp even-budget transition. Mathematical novelty is claimed for that exact conjunction, not for the general observation that Allee effects favor aggregation or independent environmental hazards favor diversification.

## Limitations

Viability means the initial survival of at least one individual of each sex at a suitable site. It is not long-term establishment, ecological persistence, or a validated field-management prescription. Unequal individual survival probabilities, sex-specific mortality, dependent habitat suitability, migration between sites, more than two habitats, density dependence, inbreeding, and later demographic generations are outside the theorem. The optimum can change under these extensions. The exact condition for odd founder budgets is given by a sign test; this report does not assert a one-crossing theorem for that parity. Relevant historical papers not available in full text leave residual prior-coverage uncertainty; lack of a search result is not proof of novelty. No independent verification has been performed.

## References

1. F. S. Grevstad (1999), *Factors influencing the chance of population establishment: implications for release strategies in biocontrol*, Ecological Applications 9, 1439–1447. DOI: `10.1890/1051-0761(1999)009[1439:FITCOP]2.0.CO;2`. First published 1999-11-01.
2. C. L. Jerde, C. J. Bampfylde and M. A. Lewis (2009), *Chance establishment for sexual, semelparous species: overcoming the Allee effect*, American Naturalist 173, 734–746. DOI: `10.1086/598496`. Published online 2009-04-15.
3. R. P. Duncan, T. M. Blackburn, S. Rossinelli and S. Bacher (2014), *Quantifying invasion risk: the relationship between establishment probability and founding population size*, Methods in Ecology and Evolution 5, 1255–1263. DOI: `10.1111/2041-210X.12288`.
4. P. Cassey, T. A. A. Prowse and T. M. Blackburn (2014), *A population model for predicting the successful establishment of introduced bird species*, Oecologia 175, 417–428. DOI: `10.1007/s00442-014-2902-1`.
5. M. J. Koontz et al. (2018), *Parsing propagule pressure: number, not size, of introductions drives colonization success in a novel environment*, Ecology and Evolution 8, 8043–8054. DOI: `10.1002/ece3.4226`.
