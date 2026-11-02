# Sharp finite-size fractional-core thresholds for a peak--bridge committee election

## Finding
For every integer \(k\ge2\) and every real number \(1/2<v<1\), the maximum simultaneous utility improvement attainable by **any** proportional-budget coalition in the peak--bridge election below is exactly
\[
\rho_{2h+1}(v)=\frac{(2h+1)v}{h+v}\quad (h\ge1),\qquad
\rho_{2h}(v)=\frac{v(2h-1+2v)}{h-1+2v}\quad (h\ge1).
\]
The entire electorate attains the maximum. The only committee satisfying justified representation is the all-peak committee, so every lottery supported on justified-representation committees has that committee as its unique realization. Its marginal vector is \((\alpha,1)\)-fractionally core-stable exactly for \(\alpha\ge\rho_k(v)\) under strict blocking. The nonzero even/odd finite-size corrections converge to the asymptotic obstruction factor \(2v\).

## Assumptions and scope
There are \(k\) voters indexed by \(1,\ldots,k\) and \(2k-1\) candidates \(p_1,q_1,p_2,q_2,\ldots,q_{k-1},p_k\), with a committee of size \(k\). Voter \(i\) values only its peak \(p_i\), at \(1\), and adjacent existing bridges \(q_{i-1},q_i\), each at \(v\); all other utilities are zero. These additive preferences are single-peaked in the displayed candidate order. Every candidate has fractional selection weight \(0\le y_c\le1\); a coalition \(S\) can propose a partial fractional committee of total mass at most \(|S|k/k=|S|\).

Define \(u_i(y)=y_{p_i}+v(y_{q_{i-1}}+y_{q_i})\), omitting nonexistent endpoint bridge terms, and
\[
\rho_k(v)=\max_{\varnothing\ne S\subseteq\{1,\ldots,k\}}\max_{y\in[0,1]^{2k-1},\,\sum_c y_c\le |S|}\min_{i\in S}u_i(y).
\]
The maxima exist because the feasible sets are compact. The strict blocking convention declares \(x\) \((\alpha,1)\)-fractionally blocked when some coalition can give **every** member utility strictly greater than \(\alpha u_i(x)\). Here \(\alpha\ge1\).

## Proof
**1. Uniqueness of the JR committee.** Each individual voter is entitled to one candidate because there are as many voters as committee seats. The justified-representation test on the singleton voter and its peak demands utility at least \(1\). Voters \(1\) and \(k\) can meet this only when \(p_1\) and \(p_k\) are selected, since their alternative bridge contributes \(v<1\). If any interior peak is omitted, its voter needs both adjacent bridges: either bridge alone contributes less than \(1\). For a nonempty set of omitted interior peaks, each maximal consecutive run of \(r\) missing peaks therefore forces selection of \(r+1\) distinct bridges. Summing over runs would use more than \(k\) seats. Thus every peak must be selected and \(W^*=\{p_1,\ldots,p_k\}\) is the unique JR committee. It satisfies JR since each voter already obtains utility \(1\), the greatest single-candidate utility it can demand.

**2. Closed-form constructions for the grand coalition.** Write \(r=\rho_k(v)\) as displayed in the finding. For odd \(k=2h+1\), assign each bridge fractional weight \(r/(2v)\), each endpoint peak weight \(r/2\), and zero weight to other peaks. All non-endpoint voters gain \(2v[r/(2v)]=r\); each endpoint gains \(r/2+v[r/(2v)]=r\). The total mass is \((k-1)r/(2v)+r=k\). The bridge weights are at most one because \(v>1/2\), and endpoint weights are below one.

For even \(k=2h\), put \(z=h/(h-1+2v)\). Give alternating bridge weights \(1,z,1,z,\ldots,1\), both endpoint peaks weight \(vz\), and all other peaks zero. Each voter gains \(v(1+z)=r\), and total mass is \(h+(h-1)z+2vz=2h\). The bounds on fractional coordinates hold since \(0<z\le1\). Thus \(\rho_k(v)\) is **at least** the stated expression.

**3. Matching blockwise upper certificates.** Let a coalition contain a maximal interval of \(s\) consecutive voters. Let \(B\) be the total mass placed on peaks of those voters and on bridges incident to them, including possible bridges at the two outer boundaries. Assign nonnegative weights \(\lambda_i\) to the interval voters, summing to one.

For odd \(s=2h+1\), assign \(a=v/(h+v)\) to local positions \(1,3,5,\ldots,2h+1\) and \(b=(1-v)/(h+v)\) to positions \(2,4,\ldots,2h\). Then \((h+1)a+hb=1\). Every peak has weighted utility coefficient at most \(a\). Every bridge internal to the interval has coefficient exactly \(v(a+b)=a\), and a boundary bridge has coefficient at most \(va<a\). Consequently, if every voter in the interval obtains utility at least \(r\), then \(r\le aB\). Since \(s a=\rho_s(v)\) (including \(s=1\), for which the formula gives \(1\)), a common utility strictly exceeding \(\rho_s(v)\) requires \(B>s\).

For even \(s=2h\), assign \(a=v/(h-1+2v)\) to local positions \(1,3,5,\ldots,2h-1,2h\), and \(b=(1-v)/(h-1+2v)\) to the remaining even positions. Then \((h+1)a+(h-1)b=1\). Peaks and boundary bridges have weighted coefficients at most \(a\). Every internal bridge except the last has coefficient \(v(a+b)=a\). The last internal bridge has coefficient \(2va\), exceeding \(a\) by \((2v-1)a\); its fractional weight is at most one. Hence \(r\le a[B+(2v-1)]\). Since \(a[s+2v-1]=\rho_s(v)\), a common utility strictly above \(\rho_s(v)\) again requires \(B>s\).

**4. All disconnected coalitions.** Decompose any nonempty coalition into maximal consecutive intervals of sizes \(s_1,\ldots,s_t\). Their incident candidate sets are pairwise disjoint: a peak benefits only its owner and a bridge benefits only two consecutive voters. Therefore the corresponding incident masses sum to at most the coalition's total allowed mass \(\sum_j s_j\). The formulas are nondecreasing with interval size. In particular, for \(h\ge1\),
\[
\rho_{2h+1}-\rho_{2h}=\frac{v(1-v)(2v-1)}{(h+v)(h+2v-1)}>0,
\]
\[
\rho_{2h+2}-\rho_{2h+1}=\frac{v^2(2v-1)}{(h+v)(h+2v)}>0,
\]
and \(\rho_1=1<\rho_2=v+1/2\). If every coalition member had utility greater than \(\rho_k(v)\), then each interval, having size at most \(k\), would require incident mass strictly greater than its own number of voters by Step 3. Summing those masses would exceed \(|S|\), contradiction. Thus no coalition improves every member beyond the displayed \(\rho_k(v)\). The grand-coalition constructions attain equality and prove exactness.

**5. Exact approximate-core boundary.** Every voter receives utility \(1\) in \(W^*\). For \(\alpha<\rho_k(v)\), the grand-coalition witness in Step 2 strictly improves all voters above \(\alpha\), proving a fractional \((\alpha,1)\)-core violation. For \(\alpha\ge\rho_k(v)\), Step 4 excludes any strict blocking coalition. Since all ex-post JR lotteries are concentrated on \(W^*\), this yields the asserted if-and-only-if criterion.

## Verification
The accompanying standalone checker `verification/check_path_frontier.py` uses exact rational arithmetic to validate primal feasibility, utility equalization, dual coefficient inequalities, and consecutive-population monotonicity for \(80\) parameter choices with up to \(16\) voters. With SciPy's HiGHS linear optimizer, it additionally solves \(2505\) coalition max-min linear programs at population sizes \(2\) through \(8\), and verifies equality at the grand coalition. The exact analytical argument above, not numerical enumeration, establishes the theorem for every admissible integer population and real bridge value.

## Relationship to prior work
Avramidis, de Berg, and Schmidt-Kraepelin (2026), Theorem 10 and Appendix E, introduce this peak--bridge family to prove incompatibility below the asymptotic factor \(2\). Their concrete blocking witness chooses the interior \(k-2\) voters and yields \(2v(k-2)/(k-1)\). The present theorem keeps precisely their family and strict core convention, but finds the **exact** finite-population obstruction over **every** coalition and fractional deviation. It is stronger than their exhibited lower witness at each fixed eligible population and reveals the even/odd correction. Their general factor-\(2\) existence and impossibility theorems do not imply these finite-instance equalities. Jin, Liu, and Tao (2026) establish a different qualitative incompatibility for approval utilities; their construction does not give the present nonbinary peak--bridge formulas.

## Limitations
Only this explicit single-peaked election family and the \((\alpha,1)\) utility-based fractional-core convention are covered. No sharp universal approximation factor for all fixed-size single-peaked profiles, no behavior for \(\beta>1\), and no independent external audit are claimed. The range \(1/2<v<1\) is essential to these formulas and to the uniqueness argument as stated. Numerical linear programming is corroborative only.

## References
1. D. Avramidis, M. de Berg, and U. Schmidt-Kraepelin, *Best-of-Both Worlds Proportionality in Structured Committee Elections*, arXiv:2610.28151v1 (first public version, 20 October 2026), Theorem 10 and Appendix E. https://arxiv.org/html/2610.28151v1
2. J. Jin, X. Liu, and B. Tao, *Limitations of Best-of-Both-Worlds Solutions in Approval-Based Multiwinner Elections*, arXiv:2608.01830 (3 August 2026), Sections 1 and 3. https://arxiv.org/abs/2608.01830
