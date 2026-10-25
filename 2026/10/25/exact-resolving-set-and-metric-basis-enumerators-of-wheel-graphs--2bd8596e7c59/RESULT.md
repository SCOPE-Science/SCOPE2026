# Exact resolving-set and metric-basis enumerators of wheel graphs

## Finding

Let \(W_m=K_1\vee C_m\) be the wheel with \(m\ge 7\) labeled rim vertices and one hub. Define the *resolving-set polynomial* \(P_m(z)=\sum_{S\subseteq V(W_m),\ S\text{ resolving}}z^{|S|}\), using ordinary shortest-path distance. Write \(P_m(z)=(1+z)R_m(z)\), with \(R_m(z)=\sum_{k=3}^{m}c_{m,k}z^k\). For \(3\le k\le m\),

\[
\boxed{c_{m,k}=\frac{m}{k}\sum_{j=0}^{\lfloor k/2\rfloor}\frac{k}{k-j}\binom{k-j}{j}\left[\binom{k-j}{m-k-2j}+j\binom{k-j}{m-k-2j-1}\right].}
\]

A binomial coefficient is zero when its lower argument is outside \(0,\ldots,a\). The displayed formula is an integer for all indicated parameters. Thus it counts **all** resolving sets at **every** possible cardinality, with or without the hub, rather than only an optimal cardinality. Every inclusion-minimal resolving set avoids the hub.

The already-known minimum size \(\beta(W_m)=\lfloor 2(m+1)/5\rfloor\) is recovered from the polynomial. A further exact count of distinct labeled metric bases \(B_m=c_{m,\beta(W_m)}\) is, with the indicated integer \(s\),

\[
\begin{array}{c|c}
 m & B_m \\ \hline
 5s-1\ (s\ge2)&(5s-1)\left(1+\frac{s^2}{2}+\frac{s(s^2-1)(s+10)}{24}\right)\\
 5s\ (s\ge2)&\frac52\left(2+s^2(s+1)\right)\\
 5s+1\ (s\ge2)&5s+1\\
 5s+2\ (s\ge1)&(5s+2)\left(1+\frac{s(s+1)(s+5)}6\right)\\
 5s+3\ (s\ge1)&(5s+3)s.
\end{array}
\]

For example, the numbers of metric bases for rim sizes \(m=7,8,9,10,11,12,13,14,15,16\) are \(21,8,54,35,11,96,26,259,95,16\). These are counts of vertex subsets, not counts modulo wheel automorphisms.

## Assumptions and scope

All graphs are finite, simple, undirected, with ordinary geodesic distance. The wheel has one central vertex \(h\) and rim \(v_0,\ldots,v_{m-1}\), with indices modulo \(m\), \(m\ge7\). A set \(S\) resolves the graph when for all distinct vertices \(u,v\) some \(w\in S\) has \(d(u,w)\ne d(v,w)\). The binomial convention above is used throughout. These formulas do not assert anything for smaller rim cycles or for wheels missing spokes.

## Proof

**1. Hub reduction.** For selected rim vertices \(T=S\cap V(C_m)\), the hub has distance one to every vertex of \(T\). For any unselected rim vertex \(u\), its distances to \(T\) consist of ones precisely at \(T\cap\{v_{u-1},v_{u+1}\}\), and twos elsewhere. If \(|T|\le2\), the \(m-|T|\ge5\) unselected rim vertices would have at most \(2^{|T|}\le4\) possible binary signatures. Thus no resolving set has fewer than three rim landmarks. If \(|T|\ge3\), every unselected rim vertex is distinguished from the hub, since it has at most two adjacent rim landmarks; selected vertices distinguish themselves by distance zero. The hub cannot distinguish two rim vertices. Therefore \(S\) resolves the wheel exactly when \(T\) does; the hub is a free optional choice. This proves the factor \(1+z\) and the assertion about inclusion-minimal sets.

**2. Signature obstruction.** For a rim subset \(T\), define \(\sigma(u)=T\cap\{v_{u-1},v_{u+1}\}\) for each unselected rim vertex \(u\). The above distance characterization proves that \(T\) resolves exactly when these signatures are pairwise distinct. The empty signature occurs at the middle of a cyclic triple of unselected rim vertices. To have at most one such middle, every maximal zero-run must have length at most three, with at most one run of length three. If two distinct unselected vertices have the same *nonempty* signature, some landmark is adjacent to both. Since \(m\ge7\), they are its two rim neighbors. Equality of their signatures holds precisely when the two other vertices immediately beyond them are unselected, giving the cyclic word pattern \(00100\). It arises precisely when two zero-runs of length at least two are separated by a single selected vertex. Consequently, in the cyclic order of the \(k\ge3\) selected rim vertices, their intervening zero-gap lengths \(a_1,\ldots,a_k\) satisfy exactly:

\[
0\le a_i\le3,\qquad \#\{i:a_i=3\}\le1,\qquad a_i\ge2\Longrightarrow a_{i+1}\le1\text{ and }a_{i-1}\le1,
\]

where gap indices are cyclic. This is a necessary **and sufficient** test obtained directly from the graph distances. A related gap feasibility characterization appears in the 2021 literature cited below; no novelty is claimed for the feasibility characterization itself.

**3. Enumeration.** Let \(j\) be the number of long gaps, those of length two or three. Their positions form an independent \(j\)-set in a cycle of length \(k\). For \(k\ge3\) the number of choices is \(I(k,j)=\frac{k}{k-j}\binom{k-j}{j}\), for \(0\le j\le\lfloor k/2\rfloor\). Given these positions, either every long gap has length two, or exactly one of the \(j\) long gaps has length three. Their zero-count generating factor is \(u^{2j}(1+ju)\). Every other gap independently has length zero or one, contributing \((1+u)^{k-j}\). Therefore the number of ordered cyclic gap lists of total zero count \(m-k\), with a distinguished starting selected rim vertex, is

\[
\sum_{j=0}^{\lfloor k/2\rfloor}I(k,j)[u^{m-k}]\,u^{2j}(1+ju)(1+u)^{k-j}.
\]

Every labeled rim configuration with \(k\) selected vertices occurs \(k\) times as the distinguished starting vertex ranges over selected vertices, while choosing an initial rim position supplies \(m\) choices. Multiplying by \(m/k\) and extracting the coefficient proves the displayed formula, including integrality. This argument does not divide by graph automorphism orbits.

**4. Metric bases and their counts.** From the gap constraints, if there are \(j\) long gaps, then \(j\le\lfloor k/2\rfloor\) and \(\sum_i a_i\le k+j+1\). Hence

\[
m\le 2k+\lfloor k/2\rfloor+1=\lfloor 5k/2\rfloor+1.
\]

This bound is attained by putting long gaps on a largest independent vertex set of the gap cycle, giving one of those long gaps length three and all other permitted gaps their maximal lengths. Reducing gap lengths one unit at a time preserves legality and realizes every total rim size from \(k\) to this maximum. Thus \(\beta(W_m)=\lceil2(m-1)/5\rceil=\lfloor2(m+1)/5\rfloor\), agreeing with the known wheel metric dimension.

For the metric-basis multiplicities, put \(k=2s\) or \(k=2s+1\). The maximal rim lengths are respectively \(5s+1\) and \(5s+3\). For minimum \(k\), the prescribed \(m\) differs from the relevant maximum by at most two. Write \(U_{m,k}\) for the number of admissible cyclic gap lists with a distinguished first selected position, so \(B_m=mU_{m,k}/k\). Extracting the deficit-zero, deficit-one, and deficit-two coefficients in step 3 gives, for even \(k=2s\),

\[
U_{5s+1,2s}=2s,\quad U_{5s,2s}=2+s^2(s+1),\quad U_{5s-1,2s}=2s+s^3+\frac{s^2(s^2-1)(s+10)}{12}.
\]

For odd \(k=2s+1\) it gives

\[
U_{5s+3,2s+1}=(2s+1)s,\qquad U_{5s+2,2s+1}=(2s+1)\left[1+\frac{s(s+1)(s+5)}6\right].
\]

For clarity, in the even cases, only \(j=s,s-1,s-2\) can contribute; for odd cases only \(j=s,s-1\). In the even deficit-two case the contributions from these three choices, respectively, are \(2s+s^2(s-1)\), \(s^2+s^2(s^2-1)\), and \((s-2)s^2(s^2-1)/12\), which sum to the value displayed above. In the even deficit-one case they are \(2+2s^2\) and \(s^2(s-1)\). In the odd deficit-one case they are \((2s+1)[1+s(s+1)]\) and \((2s+1)s(s+1)(s-1)/6\). These explicit finite evaluations yield exactly the five expressions in the finding. No asymptotic or computational assumption enters the extraction.

## Verification

The standalone `verify_wheel.py` builds the graph and computes its distances by breadth-first search, independently of the gap proof. It checks **all** \(130{,}944\) rim subsets across \(m=7,\ldots,16\), testing each with and without the hub, and compares resolution, structural gap predicates, all polynomial coefficients, metric dimension, and number of bases. Exact-integer comparisons of the coefficient and residue-class formulas also cover every \(m=7,\ldots,200\). Running `python3 verify_wheel.py` reproduces `verification_output.txt` exactly.

## Relationship to prior work

The wheel metric dimension is previously established; it is not a new claim. Sooryanarayana, Suma and Chandrakala (2021), Theorems 7.1, 7.2 and 7.11, give respectively wheel scalar values and an essentially equivalent rim-gap feasibility characterization. In particular the structural feasibility criterion of the present proof is a reformulation, **not** a claim of first discovery. The assessed additional result is the evaluated **all-cardinality labeled counting formula**, together with the five explicit congruence-class formulas for the number of metric bases. The general minimal-resolving-set enumeration framework of Bergougnoux, Defrain and Mc Inerney (2023/2024) does not specialize to these enumerators. Bokhary and coauthors (2020) study metric bases for a related but different family of wheels with consecutive missing spokes, not the same all-size enumerator for ordinary wheels.

## Limitations

The results cover rim sizes at least seven. They count labeled vertex subsets and do not classify dihedral orbits. The general feasibility characterization and the metric dimension itself are already available in prior literature; originality and mathematical value concern the exact enumeration. The priority check is bounded by indexed literature, accessible primary texts, and available research records, so obscure or unindexed equivalent counting results remain a residual risk. No independent mathematical audit has been performed.

## References

1. B. Sooryanarayana, Suma A. S., Chandrakala S. B., *Certain Varieties of Resolving Sets of A Graph*, Journal of the Indonesian Mathematical Society **27** (2021), 103–114, Theorems 7.1–7.11. DOI: 10.22342/jims.27.1.881.103-114. Full text: https://www.jims-a.org/index.php/jimsa/article/download/881/pdf/3094 .
2. B. Bergougnoux, O. Defrain, F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419 (first public version 2023-09-29). https://arxiv.org/pdf/2309.17419 .
3. S. A. U. H. Bokhary, Zill-e-Shams, A. Ghaffar, K. S. Nisar, *On the metric basis in wheels with consecutive missing spokes*, AIMS Mathematics **5** (2020), 6221–6232, DOI: 10.3934/math.2020400. https://www.aimspress.com/article/doi/10.3934/math.2020400 .
