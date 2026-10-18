# The first impartial-culture Borda-welfare reversal between probabilistic serial and random priority

## Finding

Consider a square random-assignment problem with \(n\) named agents, \(n\) unit-capacity named objects, and one complete strict preference order per agent. Under probabilistic serial (PS), all agents simultaneously consume their most-preferred remaining object at unit speed. Under random priority (RP), a uniformly random agent permutation chooses objects successively. Give an agent \(n-r\) Borda points for receiving her \(r\)-th-ranked object, for \(r=1,\ldots,n\); define \(\Delta(P)\) to be the expected *total* Borda points under PS minus those under RP at a fixed strict preference profile \(P\).

Under impartial culture (all \((n!)^n\) named profiles equally likely), the first reversal in the **mean sign** of this difference is between three and four agents. For \(n=2\), all four profiles satisfy \(\Delta=0\). For \(n=3\), exactly \(36\) of \(216\) profiles have \(\Delta=-1/12\) and the remaining \(180\) have \(\Delta=0\), giving \(\mathbb E_P[\Delta]=-1/72\). The three-agent lottery types are already implicit in the foundational random-assignment literature; the novel finite-census claim concerns the next market size.

For **\(n=4\)**, among all \(331{,}776\) named strict profiles, exactly

| Comparison of PS with RP by total Borda welfare | Number of profiles |
|---|---:|
| \(\Delta>0\) | \(87{,}408\) |
| \(\Delta=0\) | \(129{,}168\) |
| \(\Delta<0\) | \(115{,}200\) |

The complete signed average is

\[\mathbb E_P[\Delta(P)]=\frac{1283}{62208}>0.\]

Thus PS improves expected *impartial-culture mean* Borda welfare at four agents **despite losing at a larger number of individual profiles than it wins**. Moreover, for every integer \(n\ge4\), some strict profiles have \(\Delta>0\) and others have \(\Delta<0\); these sign witnesses embed the four-agent examples exactly.

## Assumptions and scope

Each object has supply one, every agent receives exactly one unit of the assignment lottery, all agents rank every object strictly, and they report these orders truthfully. The RP priority is uniform over all permutations. The Borda encoding is the equally spaced rank utility \(n-r\), not an arbitrary cardinal utility. All comparisons concern expected total welfare of the randomized allocation at a *fixed* preference profile; the expectation over profiles additionally imposes independent uniform preferences (impartial culture). No claim of dominance for other utility scores or other preference laws is made.

## Proof

**Exact random assignments.** Let \(p_{ij}\) denote the allocation probability of object \(j\) to agent \(i\). Under PS, while the remaining capacity of object \(j\) is \(c_j>0\), each agent consumes her highest-ranked nonexhausted object. If \(d_j\) agents currently consume \(j\), the next exhaustive event occurs after \(\min_{j:d_j>0}c_j/d_j\) time units; all allocations and capacities change by rational amounts. Under RP, enumerate the \(n!\) priorities and assign each agent her top currently unassigned object. For a preference profile \(P\), write \(r_i(j)\) for the rank of object \(j\) in agent \(i\)'s order and

\[ W(Q,P)=\sum_{i=1}^n\sum_{j=1}^n (n-r_i(j))Q_{ij},\qquad
\Delta(P)=W(\mathrm{PS}(P),P)-W(\mathrm{RP}(P),P).\]

Both allocation calculations use exact rational arithmetic, not floating-point ranking thresholds.

**Complete finite enumeration.** There are precisely \((n!)^n\) named strict profiles. Relabeling the objects simultaneously in all preferences leaves \(\Delta\) unchanged. Moreover, this group action is free, because the first agent has a strict total order. Consequently every relabeling orbit contains exactly one profile whose first agent's order is \((0,1,\ldots,n-1)\), and has size \(n!\). It therefore suffices to examine all \((n!)^{n-1}\) choices of the other agents' orders, assigning multiplicity \(n!\) to each exact value of \(\Delta\). The executable verifier implements these definitions directly and compares each computed value with a second independent formulation (PS interval-integrated welfare and RP subset-Bellman recursion). It exhausts \(2, 36, 13{,}824\) canonical profiles for \(n=2,3,4\), respectively, covering \(4,216,331{,}776\) labeled profiles. The two methods agree profile by profile. The resulting exact histograms imply all stated counts and the mean values. The included machine-readable certificate records all \(52\) rational difference values at four agents, their exact frequencies, their weighted sum \(20528/3\), and the quotient \(1283/62208\).

**Explicit opposite-sign profiles.** Write each preference order as its most-preferred-to-least-preferred object list. For four agents, the profile

\[P_+=((0,1,2,3),(0,3,2,1),(2,1,0,3),(2,3,0,1))\]

has \(\Delta(P_+)=1\); the profile

\[P_-=((0,1,2,3),(0,2,1,3),(1,0,3,2),(3,0,1,2))\]

has \(\Delta(P_-)=-1/3\). The exact matrices, and two independently computed welfare differences, are reproducible with the verifier.

**Persistence for every larger market.** Start with either four-agent witness, append \(m=n-4\) new agent/object pairs, and put every original object above every new object in the original agents' preference lists. Let each new agent rank her own new object first; complete the remainder of her order arbitrarily. Under PS, each new agent consumes only her own new object for the whole unit interval, while the original four agents' PS allocation among the original four objects is exactly unchanged. Under RP, every new agent receives her favorite new object regardless of priority; each original agent receives the same original object she would receive under the relative order of the original four agents alone. This relative priority order remains uniform. Each original agent's score for any original object increases by \(m\) in both mechanisms and hence cancels from the welfare difference; new agents contribute identical top-rank scores. Thus the expanded profile has the same \(\Delta\) as the base witness, proving both signs for every \(n\ge4\).

## Verification

Run `python3 verify_ps_rp_borda.py` with Python's standard library and compare its one-line JSON output byte-for-byte with `certificate.json`. The first evaluation uses exact PS allocation matrices and enumerates every random priority; the independent evaluation integrates instantaneous PS Borda welfare and solves RP by an exact Bellman recursion over remaining agents and objects. Both evaluate the complete reduced profile space. The certificate checks the three- and four-agent sign totals, exact means, and two four-agent witnesses. This is a complete finite census by group-action reduction, not a statistical sample. The extension to arbitrary market size has the analytic construction above.

## Relationship to prior work

Bogomolnaia and Moulin (first public online 2001-03-29) introduced PS and compared it with RP, including canonical three-agent configurations in which their random allocations differ and a four-agent direct-dominance example. This finding does **not** claim either previously known allocation pattern as new. Che and Kojima analyzed large replica economies, and Basteck discussed constrained efficiency and expected rank of alternative assignment mechanisms. Ortega and Zhao (2026) directly analyze PS versus RP under independent uniform preferences using average ranks, establishing nontrivial *asymptotic* and uniform-in-size bounds. These results concern overlapping objects and welfare concepts, but none of the inspected statements supplies the exact four-agent sign histogram, its contrary frequency-versus-mean comparison, or the sharp transition from negative to positive impartial-culture average difference. Separately published exact four-agent RP/PS ordinal-efficiency and stochastic-dominance censuses are related but do not imply signed Borda-welfare frequencies on incomparable profiles. Equivalence under a different finite rank-welfare enumeration remains a bibliographic risk.

## Limitations

This is an exact classification for \(n\le4\) and an existence construction for all \(n\ge4\), not an exhaustive classification of larger markets. Its average reversal depends on impartial culture and equally spaced Borda utilities, not on heterogeneous cardinal intensities, manipulation, noisy preferences or empirical demand. The finite proof is computationally enumerative with independent exact implementations; no external audit or human verification is claimed.

## References

1. A. Bogomolnaia and H. Moulin, *A New Solution to the Random Assignment Problem*, Journal of Economic Theory 100 (2001), 295–328, doi:10.1006/jeth.2000.2710; published online March 29, 2001. Full technical text: https://www.researchgate.net/publication/24056727_A_Simple_Random_Assignment_Problem_with_a_Unique_Solution .
2. Y.-K. Che and F. Kojima, *Asymptotic Equivalence of Probabilistic Serial and Random Priority Mechanisms*, Econometrica 78 (2010), 1625–1672, doi:10.3982/ECTA8354.
3. C. Basteck, *On (Constrained) Efficiency of Strategy-Proof Random Assignment*, Econometrica (2025), doi:10.3982/ECTA22762.
4. J. Ortega and G. Zhao, *The Remarkable Efficiency of the Probabilistic Serial Mechanism*, author-hosted manuscript dated October 9, 2026, https://www.josueortega.com/PS_versus_RP_simplified.pdf .
