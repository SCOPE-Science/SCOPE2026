# Exact population-resolved census and entropy of fully satisfied radius-two Schelling rings

## Finding

Let \(n\geq5\) and \(0\leq m\leq n\) be integers. Label the vertices of a cyclic residential ring \(0,\ldots,n-1\), with precisely \(m\) residents of type \(1\), the rest of type \(0\). Every resident evaluates the **four distinct other residents** at cyclic offsets \(\pm1,\pm2\); a resident is satisfied if at least two of these four have the resident's own type. Let \(S_{n,m}\) count labeled binary configurations in which *every* resident is satisfied.

Define \(\binom{a}{b}=0\) for integers \(a<b\) or \(b<0\). Then the exact count, including every boundary case, is
\[
\boxed{S_{n,m}=
\mathbf 1_{\{m=0\text{ or }m=n\}}+
2\mathbf 1_{\{n\ {\rm even},\,m=n/2\}}+
\sum_{k=1}^{\min(\lfloor m/3\rfloor,\lfloor(n-m)/3\rfloor)}
\frac{n}{k}
\binom{m-2k-1}{k-1}
\binom{n-m-2k-1}{k-1}.}
\]
In particular a nonmonochromatic fully satisfied configuration is **either** one of the two strict alternating checkerboards (only for even \(n\)) **or** every maximal same-type cyclic run has length at least three. There are no other possibilities.

Writing \(H_n=\sum_{m=0}^n S_{n,m}\), one obtains a second exact formula:
\[
\boxed{H_n=2+2\mathbf1_{\{2\mid n\}}+
\sum_{k=1}^{\lfloor n/6\rfloor}
\frac nk\binom{n-4k-1}{2k-1}.}
\]
Let \(\lambda=1.465571231876\ldots\) be the unique positive root of
\(\lambda^3-\lambda^2-1=0\). The asymptotic law is
\[
H_n\sim\lambda^n,\qquad
\mathbb P(\hbox{all satisfied under independent fair binary coloring})
=\frac{H_n}{2^n}\sim\left(\frac{\lambda}{2}\right)^n.
\]
For a random *fixed-composition* coloring, the exact probability is
\(S_{n,m}/\binom nm\).

## Assumptions and scope

The ring is fully occupied, has two distinguishable types, labeled sites, and at least five sites so that the four neighboring sites are distinct. Both types have the same weak threshold of two agreeing neighbors among four. Cyclic rotations are **not** identified. Satisfaction refers to a static configuration, not necessarily to absorption of a particular swapping or moving dynamics. When a population count is prescribed it is invariant under type-swapping dynamics, but the theorem does not analyze which satisfied states are dynamically reachable.

The six-state transfer presentation below is only a counting device: it is not a claim that the original population process follows that update rule.

## Proof

**1. The short-run obstruction.** A maximal cyclic monochromatic run is a maximal consecutive block of equal types, allowing the full constant ring as a single run. Suppose the configuration contains both types. At a site forming a run of length one, its two immediate neighbors are opposite. It can be satisfied only if both second-nearest neighbors are of its own type. Consequently the two adjacent opposite-type runs must both have length one. Applying this implication successively around the finite cycle, **every** run must have length one. Hence the ring alternates, necessarily with even \(n\). Conversely every alternating configuration satisfies each site exactly at the threshold: its neighbors at distance two agree and those at distance one disagree.

If there are no singleton runs, a hypothetical run of length two has an endpoint whose exterior neighbor and second exterior neighbor both disagree, whose immediate interior neighbor agrees, and whose second interior neighbor is outside the run and disagrees. Such an endpoint has only one agreeing neighbor, a contradiction. Hence all runs are at least three. Conversely when each run has length at least three, each resident has at least two agreeing neighbors within its own run, and is satisfied. The two constant configurations are plainly satisfied. This proves the classification.

**2. Counting with a conserved type population.** For a configuration with both colors and all runs at least three, there are equally many runs of either color; write that number as \(k\). The \(k\) type-\(1\) run lengths are each at least three and sum to \(m\); they have
\(\binom{m-2k-1}{k-1}\) ordered choices. The \(k\) type-\(0\) run lengths sum to \(n-m\), with
\(\binom{n-m-2k-1}{k-1}\) ordered choices. Choose one labeled position as the beginning of a type-\(1\) run (there are \(n\) possible labels) and list the alternating run lengths cyclically. Each resulting labeled configuration is represented exactly \(k\) times, once for each of its type-\(1\) runs. Division by \(k\) gives the displayed sum. The two constant words and, when allowed, the two alternating words add the indicator terms. No other configurations occur by step 1.

**3. Counting without a population constraint.** Sum the preceding formula over \(m\). For each \(k\), concatenate the \(2k\) alternating run lengths (each at least three); the number of ordered compositions of \(n\) into those parts equals
\(\binom{n-4k-1}{2k-1}\). The same \(n/k\) positional factor applies. This proves the stated total formula.

**4. The exact entropy.** Define a six-state adjacency matrix \(T\) with states
\((0,1),(0,2),(0,3+),(1,1),(1,2),(1,3+)\), recording the current type and the run length capped at three. The allowed directed edges are
\[
(0,1)\to(0,2)\to(0,3+),\quad
(0,3+)\to(0,3+),\quad (0,3+)\to(1,1),
\]
together with their color-swapped copies. A cyclic binary word with all runs at least three has exactly one compatible cyclic state labeling, including either constant word, and conversely, for each \(n\ge5\). Thus
\(H_n=\operatorname{tr}(T^n)+2\mathbf1_{\{2\mid n\}}\).

Direct expansion gives
\[
\det(tI-T)=(t^3-t^2-1)(t^3-t^2+1).
\]
The directed graph is strongly connected and has a self-loop, so \(T\) is primitive. By Perron–Frobenius, its simple positive spectral radius is the root \(\lambda>1\) of \(t^3-t^2-1\); the other eigenvalues have strictly smaller modulus. Therefore \(\operatorname{tr}(T^n)=\lambda^n+o(\lambda^n)\). Adding the bounded checkerboard correction yields \(H_n\sim\lambda^n\). Dividing by \(2^n\) gives the probability statement. The fixed-composition probability follows from the equiprobability of the \(\binom nm\) labeled configurations.

## Verification

The standalone `CHECKER.py` uses the direct four-neighbor satisfaction predicate, independently computes all binary configurations for \(5\le n\le16\), compares their actual population-specific counts to the binomial formula, verifies the classification for each configuration, checks the six-state trace representation, and tests the polynomial matrix identity
\(T^6-2T^5+T^4-I=0\). Additional integer trace and binomial checks cover lengths through \(50\). The checker passed 134,474 assertions.

For small lengths the total stable counts are \(H_5=2\), \(H_6=10\), \(H_7=16\), \(H_8=28\), \(H_9=38\), \(H_{10}=54\). These finite tests independently audit the formulas in the tested ranges; the infinite assertions are proved by the run decomposition and Perron–Frobenius argument.

## Relationship to prior work

Brandt, Immorlica, Kamath, and Kleinberg (2012) give the exact equal-tolerance, nearest-neighborhood circular Schelling model and study eventual run lengths under random unhappy-pair swaps; their claims concern dynamics rather than counting every all-satisfied configuration at a prescribed population balance. Tosic and Agha (2004) identify long homogeneous runs as fixed configurations of majority cellular automata, establishing an important precursor to step 1; the classification of *all* radius-two equilibria, the fixed-composition counting formula, and its entropy are the precise claims assessed here. Goles Domic, Goles, and Rica (2011) study segregation energies and dynamics, with the explicit one-dimensional analysis using two neighboring sites rather than the four-site rule here.

Nakar and Ron (2022) establish broad structural restrictions on radius-\(r\) majority-automaton fixed and periodic configurations (their strongly stable runs and short-block periodic exceptions). That stronger general structural framework already covers key ideas underlying the run dichotomy; the distinct assertion here is the **complete explicit population-resolved census**, together with the six-state asymptotic entropy. It is not claimed that the short-run obstruction or the existence of long-run fixed configurations was previously unknown.

## Limitations

The static all-satisfied set can be strictly smaller than the set of states that are absorbing under pair-swap Schelling dynamics: no swap is possible when there are no unhappy members of one of the types, even if someone of the other type is unhappy. The exact counts do not give hitting probabilities or absorption times. The model excludes vacancies, heterogeneous thresholds, nonlocal movement rules, unequal weights, and rings of length below five. Large-\(n\) entropy counts stable states, not the probability of arriving at them from a random dynamic. The historical novelty of the explicit count is assessed against inspected sources but is not independently certified; an equivalent enumeration in an unlocated table remains possible.

## References

1. C. Brandt, N. Immorlica, G. Kamath, R. Kleinberg, *An Analysis of One-Dimensional Schelling Segregation*, first arXiv public submission 2012-03-28, https://arxiv.org/abs/1203.6346.
2. P. T. Tosic and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, 2004, https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
3. N. Goles Domic, E. Goles, S. Rica, *Dynamics and Complexity of the Schelling Segregation Model*, Physical Review E 83 (2011), DOI:10.1103/PhysRevE.83.056111.
4. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (2022), https://arxiv.org/abs/2205.08972.
