# Sharp world cost and optimal censuses of irredundant S5 data knowledge

## Finding
Consider a pointed, labelled finite epistemic frame with \(r\ge2\) agents and an injective data variable. Suppose every agent regards **exactly \(k\) data values** as possible, the coalition of all agents knows the value, but *every proper coalition* remains ignorant. Write \(s=k-1\).

**Sharp existence and world cost.** Such a frame exists on \(n\) worlds if and only if
\[
 k\ge r,\qquad n\ge 1+\left\lceil\frac{r(k-1)}{r-1}\right\rceil.
\]
In particular, no amount of extra worlds permits irredundant \(r\)-way knowledge with fewer than \(r\) locally possible values per agent.

**Structural normal form.** Let \(q=n-1\), \(b=n-k\), and let \(C_i\) be the set of nonactual worlds that agent \(i\) rules out. The required knowledge pattern is *equivalent* to: \(|C_i|=b\), the \(C_i\) cover all \(q\) nonactual worlds, and every \(C_i\) has a private point belonging to no other \(C_j\). At the minimal carrier, the excess-incidence invariant
\[
 \delta=(r-1)q-rs=rb-q
\]
satisfies \(0\le\delta\le r-2\). It equals the sum, over nonactual worlds, of (the number of agents excluding that world minus one).

**Exact count.** Define
\[
 H_r(z_1,\ldots,z_r)=\prod_{i=1}^r(1+z_i)-1.
\]
For any admissible \(n,r,k\), the number of ordered \(r\)-tuples of labelled S5 equivalence relations realizing this knowledge pattern at a fixed actual world is exactly
\[
 B_b^r [z_1^b\cdots z_r^b]
 \sum_{J\subseteq[r]}(-1)^{|J|}
 \left(H_r-\sum_{j\in J}z_j\right)^q,
\]
where \(B_b\) is the \(b\)-th Bell number. If \(s=(r-1)b\) and the carrier is minimal, this simplifies to
\[
 \frac{(rb)!}{(b!)^r} B_b^r.
\]
For exactly three agents, the **complete sharp-carrier census** is
\[
 \begin{array}{ll}
 s=2b: &\displaystyle \frac{(3b)!}{(b!)^3}B_b^3,\quad b\ge1;\\[3pt]
 s=2b-1: &\displaystyle \frac{3(3b-1)!}{((b-1)!)^2b!}B_b^3,\quad b\ge2.
 \end{array}
\]
Examples of the three-agent counts at the smallest carriers are \(6,1440,720,630000\) for local budgets \(k=3,4,5,6\), respectively.

## Assumptions and scope
There are \(n\ge1\) *labelled* possible worlds, one designated actual world \(w\), and a *fixed injective* variable \(x\) assigning different values to different worlds. Agents \(i\in[r]\) carry arbitrary, independently specified S5 equivalence relations \(E_i\); no probability model or independence assumption is used. The number of values possible for group \(G\) at \(w\) is \(|\bigcap_{i\in G}E_i[w]|\). Assume \(|E_i[w]|=k\) for each \(i\). By monotonicity of distributed knowledge, it suffices to check the \(r\) maximal proper coalitions \([r]\setminus\{i\}\).

A counted object is an **ordered tuple of full equivalence relations**, not just an ordered tuple of local uncertainty sets. The actual world and injective valuation are fixed, not multiplied into the count; no claim of an unlabelled enumeration is made. \(B_0=1\).

## Proof
Put \(U=W\setminus\{w\}\), \(q=|U|\), \(S_i=E_i[w]\setminus\{w\}\), and \(C_i=U\setminus S_i\). Each \(S_i\) has size \(s=k-1\), each \(C_i\) has size \(b=q-s=n-k\).

**Step 1 (semantic reduction).** Injectivity of \(x\) makes a coalition know its value exactly when its uncertainty-cell intersection equals \(\{w\}\). Hence full-group knowledge is \(\bigcap_i S_i=\varnothing\), equivalently \(\bigcup_i C_i=U\). Removing agent \(i\) must leave some nonactual possible world, i.e. \(\bigcap_{j\ne i}S_j\ne\varnothing\). Under full-group knowledge, any such witness belongs to \(C_i\) but no other \(C_j\), a private point. Conversely a private point for every \(C_i\), plus covering, gives all maximal-proper ignorance conditions.

**Step 2 (necessary cutoff).** Distinct private witnesses force \(r\) different worlds, each lying in \(S_j\) for all but one agent, so \(s\ge r-1\), i.e. \(k\ge r\). Covering gives \(q\le\sum_i|C_i|=rb=r(q-s)\), hence \(q\ge\lceil rs/(r-1)\rceil\). This implies the claimed carrier bound.

**Step 3 (sufficient construction).** Assume \(s\ge r-1\) and \(q\ge\lceil rs/(r-1)\rceil\). Pick distinct points \(v_1,\ldots,v_r\in U\); reserve \(v_i\) privately for \(C_i\). Let \(V=U\setminus\{v_1,\ldots,v_r\}\). The \(r\) sets have a total of \(r(b-1)\ge q-r=|V|\) remaining positions. Assign each point in \(V\) to at least one \(C_i\), never exceeding capacity \(b-1\), then fill each \(C_i\) to size \(b\) with additional points of \(V\). Filling is feasible because \(|V|=q-r\ge b-1\), equivalent to \(s\ge r-1\). All reserved points remain private. Form an S5 partition for each \(i\) having \(\{w\}\cup(U\setminus C_i)\) as its actual-world block; partition each residual \(C_i\) arbitrarily. The construction works for every larger \(q\) as well.

**Step 4 (incidence normal form).** Each \(u\in U\) is excluded by a nonempty set \(T(u)=\{i:u\in C_i\}\). Thus \(\sum_{u\in U}(|T(u)|-1)=rb-q=\delta\). At minimal \(q=\lceil rs/(r-1)\rceil\), \(0\le(r-1)q-rs\le r-2\). In particular, if \(s=(r-1)b\), then \(q=rb\), \(\delta=0\): every point is excluded by exactly one agent, and the \(C_i\) are an ordered partition into \(r\) blocks of size \(b\).

**Step 5 (general census).** A nonactual world contributes the nonempty monomial \(\prod_{i\in T(u)}z_i\) of \(H_r\). Therefore the coefficient of \(z_1^b\cdots z_r^b\) in \(H_r^q\) counts local configurations with required exclusion sizes and full coverage. A coalition remains ignorant upon removing agent \(i\) exactly when the singleton pattern \(T(u)=\{i\}\) occurs. Inclusion-exclusion over missing singleton patterns gives the displayed coefficient. Each fixed \(C_i\) leaves \(b\) worlds outside agent \(i\)'s actual-world block, partitionable in \(B_b\) ways, independently for the \(r\) agents. Multiply by \(B_b^r\).

**Step 6 (optimal closed forms).** When \(\delta=0\), Step 4 yields exactly \((rb)!/(b!)^r\) ordered local partitions. For \(r=3\), if \(s=2b\), again \(\delta=0\). If \(s=2b-1\), the minimal \(q=3b-1\) has \(\delta=1\), so precisely one world is excluded by exactly two agents and all others by exactly one; triple exclusions are impossible. Choose the omitted pair in \(3\) ways. The singleton omission counts are \(b-1,b-1,b\), according as an agent is in the pair or not. The number of assignments of the \(q\) labelled worlds to these four patterns is \(q!/((b-1)!^2b!)\). All singleton counts are positive for \(b\ge2\), giving the stated census.

## Verification
The included self-contained `checker.py` enumerates all equal-size local cells for \((r,s)=(2,1\ldots4),(3,2\ldots5),(4,3\ldots4),(5,4)\). For each it checks that one fewer than the proposed minimum nonactual worlds yields zero configurations, the claimed minimum yields a positive count, and the closed-form optimal censuses match. It independently constructs full labelled set partitions on three small domains and checks the Bell multiplicity of complete S5 relations. The completed run returned `ALL_CHECKS_OK`. These are finite cross-checks; the universal claims follow from Steps 1–6, not from exhaustion.

## Relationship to prior work
Baltag and Smets (2025) give group knowing-value semantics via intersection of S5 indistinguishability relations. Their 2026 paper extends this to exact numerical bounds on possible group data values and dynamic exchanges. The present statement asks a **different finite extremal question**: fixed *exact* local value budgets, a value known only by the full group, sharp carrier size, and all optimally sized labelled S5 realizations. The simple semantic reduction is prior work, not claimed new.

The underlying set-theoretic obstruction is an irredundant family of equal-size sets with empty total intersection, equivalently an equal-capacity cover with private elements. General Helly-critical terminology and standard multinomial enumeration are relevant; this finding is restricted to the natural tied epistemic parameters and adds the exact carrier boundary and optimal three-agent census. The possibility of an equivalent older extremal set-family formulation remains an explicit priority risk.

## Limitations
Injectivity is essential: with repeated values, group knowledge need not require a singleton intersection. The result is pointed, uses exactly \(k\) possible worlds per agent, and requires every proper coalition to be ignorant. It does not cover arbitrary value repetitions, heterogeneous agent budgets, common knowledge, dynamic updating, or unlabelled frame orbits. No independent external mathematical audit has been performed.

## References
1. A. Baltag and S. Smets, *The Logic of Data Access and Data Exchanges*, 2026, arXiv:2606.31858; DOI:10.4204/EPTCS.447.6. https://arxiv.org/abs/2606.31858
2. A. Baltag and S. Smets, *Group Knowledge of Hypothetical Values*, EPTCS 437 (2025), 140–159; DOI:10.4204/EPTCS.437.15. https://arxiv.org/abs/2511.22379
3. A. Baltag, public seminar abstract, *The Logic of Data Access and Data Exchanges*, February 26, 2026. https://projects.illc.uva.nl/lgc/seminar/2025/12/lira-session-alexandru-baltag-6/
