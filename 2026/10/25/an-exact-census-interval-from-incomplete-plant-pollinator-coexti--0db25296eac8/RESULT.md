# An exact census interval from incomplete plant–pollinator coextinction marginals

## Finding

**Theorem (complete fiber and sharp marginal-order boundary).** Fix an integer \(m\ge2\) and a known pollinator extinction probability \(q\in(0,1)\). Plants are labeled by \(P=[m]\). Pollinators have nonempty plant neighborhoods and are retained mutually independently, each with probability \(1-q\). A plant is counted as extant if at least one of its pollinator neighbors survives; no further dynamics is assumed. Repeated pollinators having identical plant neighborhoods are permitted.

Suppose exact observations give, for every \(\varnothing\ne S\subsetneq P\), the probability \(E(S)\) that *all* plants of \(S\) are extinct. Put \(u(\varnothing)=u(P)=0\) provisionally, and \(u(S)=\log E(S)/\log q\) for the observed proper subsets. If any observed probability is not a nonnegative-integer power of \(q\), no such finite network exists. Otherwise define for every \(A\subseteq P\)
\[
F_0(A)=-u(P\setminus A),\qquad
b_T=\sum_{A\subseteq T}(-1)^{|T|-|A|}F_0(A),\quad \varnothing\ne T\subseteq P.
\]
For all odd-size nonempty \(T\) and all even-size nonempty \(T\), respectively, put
\[
L=\max\left\{1,\max_{|T|\,\mathrm{odd}}(-b_T)\right\},\qquad
U=\min_{|T|\,\mathrm{even}}b_T.
\]
There is a compatible network **if and only if** \(L\le U\). Its compatible pollinator census sizes are **exactly the integers** \(N\in[L,U]\), and at every such \(N\) the unique neighborhood-type multiplicities are
\[
\boxed{x_T(N)=b_T+(-1)^{|T|+1}N,\qquad \varnothing\ne T\subseteq P.}
\]
Therefore the compatible networks, up to permutation of indistinguishable pollinators, form a complete consecutive-integer fiber. Specifying a census \(N\) uniquely selects one network; fixing fewer observation marginals may not. Indeed, for every \(m\ge3\), even with \(N\) and \(q\) known, all observations of order at most \(m-2\) can agree between two different networks with nonempty plant neighborhoods.

A three-plant family illustrates an actual three-member fiber. For each singleton \(S\), let \(E(S)=q^4\); for each pair let \(E(S)=q^6\). The compatible values are exactly \(N=6,7,8\), with
\[
x_T(N)=1+(N-7)(-1)^{|T|+1},\quad\varnothing\ne T\subseteq\{1,2,3\}.
\]
Thus \(N=6\) has two pollinators for each pair-type, \(N=7\) has one for every nonempty type, and \(N=8\) has two for each odd-cardinality type. All three structures have identical one- and two-plant extinction laws but distinct three-plant extinction probabilities \(q^6,q^7,q^8\).

## Assumptions and scope

Pollinator extinctions are independent and identically distributed with a known \(q\) strictly between zero and one; no pollinator has an empty neighborhood in the modeled plant guild. Plant survival is the Boolean OR of its pollinators' survival. There is no ecological feedback, spatial correlation, pollinator-specific mortality or observation error. Input probabilities are exact population probabilities, not finite-sample estimates. Labels of plants are retained; pollinator identities with identical neighborhoods are intentionally exchangeable. The number of pollinators \(N\) is not assumed known unless explicitly specified. The theorem allows a plant to lack any pollinator (in that case its extinction probability is one), but every *pollinator* must visit at least one plant.

## Proof

**Step 1: Convert coextinction to a coverage function.** Let \(x_T\in\mathbb Z_{\ge0}\) count pollinators adjacent to exactly the nonempty plant set \(T\subseteq P\); \(N=\sum_{T\ne\varnothing}x_T\). For \(S\subseteq P\), let
\[
u(S)=\sum_{T:T\cap S\ne\varnothing}x_T.\]
All plants of \(S\) are extinct exactly when every pollinator adjacent to at least one plant in \(S\) is extinct. Their independent extinction therefore gives \(E(S)=q^{u(S)}\). Since \(q\in(0,1)\) is known, each observed \(u(S)\) is uniquely determined. It must be a nonnegative integer. A known census would also supply \(u(P)=N\), but this single highest-order datum is deliberately omitted.

**Step 2: Parameterize every possible full incidence multiset.** Define the subset-sum function
\[
F_N(A)=\sum_{T\subseteq A}x_T=N-u(P\setminus A)\qquad(A\subseteq P).
\]
This follows by counting pollinators with no neighbors outside \(A\). At \(A=\varnothing\), \(F_N(\varnothing)=0\) because every pollinator has at least one plant neighbor. For observed proper coextinction subsets we know the right side except for the single unknown integer \(N=u(P)\); writing \(F_0(A)=-u(P\setminus A)\) with provisional \(u(P)=0\), we obtain \(F_N(A)=F_0(A)+N\mathbf1_{A\ne\varnothing}\) for **every** \(A\subseteq P\). Standard subset-Möbius inversion, performed here explicitly, gives
\[
x_T=\sum_{A\subseteq T}(-1)^{|T|-|A|}F_N(A)
=b_T+N\sum_{\varnothing\ne A\subseteq T}(-1)^{|T|-|A|}
=b_T+(-1)^{|T|+1}N.
\]
The final identity uses \(\sum_{A\subseteq T}(-1)^{|T|-|A|}=0\) for nonempty \(T\). No other incidence-vector solutions exist because subset-Möbius inversion is injective.

**Step 3: Sharp existence and bounds.** The \(b_T\) are integers whenever every observed \(u(S)\) is an integer. Nonnegativity of every \(x_T\) is equivalent to \(N\ge-b_T\) for odd-size \(T\) and \(N\le b_T\) for even-size \(T\). At least one pollinator requires \(N\ge1\). This is precisely the interval \(L\le N\le U\). Conversely, for any integer \(N\) in that interval the formula produces nonnegative integer multiplicities, and the inverse subset-sum transform reconstructs every prescribed proper \(u(S)\). In particular, \(\sum_{T\ne\varnothing}x_T=F_N(P)=N\). Independent pollinator extinctions on this constructed network reproduce every observed probability. This proves necessity, sufficiency, uniqueness at fixed census, and the absence of gaps in feasible censuses.

**Step 4: Sharpness of observing subsets through size \(m-1\).** Let \(B=P\setminus\{m\}\), with \(|B|=m-1\). Construct network \(G_{\mathrm{even}}\) with one pollinator adjacent to \(\{m\}\cup J\) for each even-cardinality subset \(J\subseteq B\); construct \(G_{\mathrm{odd}}\) similarly using odd-cardinality \(J\). Each has exactly \(2^{m-2}\) pollinators and every plant has a pollinator neighbor. When \(m\in S\), the number of pollinators incident to \(S\) is the full census in both networks. When \(S\subseteq B\) and \(|S|\le m-2\), the complement \(B\setminus S\) is nonempty and contains equal numbers of even- and odd-cardinality subsets. The number of pollinators *not* incident to \(S\) is therefore the same in both networks. Thus \(u_{\mathrm{even}}(S)=u_{\mathrm{odd}}(S)\) for all \(|S|\le m-2\), and all corresponding observed extinction marginals agree. For the subset \(S=B\) of size \(m-1\), only \(J=\varnothing\) avoids \(S\); this is present in the even construction but absent in the odd construction. Hence \(u_{\mathrm{even}}(B)=2^{m-2}-1\) and \(u_{\mathrm{odd}}(B)=2^{m-2}\). The networks are different and are distinguished at the next marginal order. This proves sharpness for \(m\ge3\).

**Step 5: The three-plant fiber.** For \(m=3\), the prescribed proper coverage counts are \(u(\{i\})=4\) and \(u(\{i,j\})=6\). Taking \(N=7\) yields \(x_T=1\) for each of the seven nonempty types and hence has those coverage counts. The formula from Step 2 gives \(b_T=1-7(-1)^{|T|+1}\), so \(L=6\) and \(U=8\); all and only the three advertised networks occur. Their all-plant extinction probabilities are \(q^N\), showing that the absent highest-order observation separates the models.

## Verification

The portable `verify.py` uses only the Python 3 standard library and exact `Fraction`/integer arithmetic. Run `python verify.py`; expected output is the complete `verification_certificate.json` payload. The execution checks 857 network profiles, 857 exact censuses/fiber identities, 1,217 allowable census parameters, 17,279 direct marginal probability comparisons, and seven parity-witness constructions for \(m=3,\ldots,9\), as recorded in the certificate. A total of 218,726 latent-pollinator outcomes is directly enumerated across the small configurations. The three-plant interval is also checked exactly. These are finite corroborations; Steps 1–5 prove the stated assertions for every admissible finite \(m\).

## Relationship to prior work

Burgos et al. [1] formulate the ecological extinction rule on bipartite mutualistic networks and analyze forward robustness/nestedness. Their result does not reconstruct incidence data from proper-subset coextinction marginals. Nguyen and Zheng [2] prove binary independent component analysis of OR mixtures is identifiable from the **complete joint law**, after collapsing indistinguishable latent neighborhoods; that broader complete-data identification is prior work, not claimed as new here. Unlike their complete-law identification statement, the present theorem describes the **entire set of feasible incomplete-marginal completions**, including the exact finite interval in an unknown integer census, realized networks at every integer in the interval, and the sharp lower-marginal parity obstruction even for known census and known common extinction probability. Hyttinen, Eberhardt and Hoyer [3] treat causal noisy-OR systems with latent confounding and interventions; their inspected identification statements are not the complete integer-fiber theorem for passive marginal coextinction observations. Standard Möbius inversion is a recognized mathematical tool here, not a claimed new method. General contingency-table marginal-parity theory could offer an equivalent formulation, so independent broad literature confirmation is warranted.

## Limitations

There is no finite-sample statistical recovery guarantee: with estimated probabilities, deciding whether logarithms are exact integers can be unstable. Results presume known homogeneous \(q\), independent pollinator extinction, no empty pollinator neighborhood, and an exact OR plant-survival rule. Unknown \(q\), unmodeled pollinator species, heterogeneous probabilities, ecological cascades, spatial or temporal dependence, and partial unlabeled plant data fall outside scope. The full-joint-law identifiability result is already known; only the sharp incomplete-marginal fiber, feasibility, and marginal-order boundary are claimed here. No independent scientific or bibliographic audit has been performed.

## References

[1] E. Burgos et al., “Why Nestedness in Mutualistic Networks?”, arXiv:q-bio/0609005v1, first public 2006-09-05. https://arxiv.org/abs/q-bio/0609005

[2] H. Nguyen and R. Zheng, “Binary Independent Component Analysis with OR Mixtures”, arXiv:1007.0528v1, first public 2010-07-04. https://arxiv.org/abs/1007.0528

[3] A. Hyttinen, F. Eberhardt and P. Hoyer, “Noisy-OR Models with Latent Confounding”, arXiv:1202.3735v1, first public 2012-02-14. https://arxiv.org/abs/1202.3735
