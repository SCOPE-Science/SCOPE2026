# Sharp one-vote reversal and bounded stabilization for random majority on complete graphs

## Finding
Consider the synchronous random-majority model (RMM) on the loopless complete graph \(K_n\), \(n\ge2\). Each of the \(n\) agents simultaneously adopts the strict majority color among its \(n-1\) neighbors. In a tie it independently chooses blue or white with probability \(1/2\) each, independently over agents and rounds. Start from an arbitrary configuration with exactly \(k\) blue agents. The **stabilization time** \(T\) is the least integer \(t\ge0\) at which the process enters a closed communicating class. All such classes are determined below, as are their hitting probabilities and \(\mathbb E[T]\).

For \(n=2r\) even, the two monochromatic configurations are fixed; each configuration with \(r\) blue agents is in a deterministic two-cycle with its complement, giving \(\binom{2r}{r}/2\) distinct two-cycles. If \(k<r\), respectively \(k>r\), one update reaches all white, respectively all blue. In particular, \(T=0\) when \(k\in\{0,r,n\}\) and \(T=1\) otherwise.

For \(n=2r+1\) odd, \(r\ge1\), only the two monochromatic fixed points are recurrent, and the process reaches one almost surely. If \(k\notin\{r,r+1\}\), one update yields unanimous color matching the initial strict majority (or \(T=0\) if already unanimous). In the two **one-vote margin** cases, the initially minority color wins with probability exactly
\[
\varepsilon_r=\frac{1}{2^{r+1}-r}.
\]
The expected first-consensus time from either critical configuration is
\[
E_r=2+\frac{r+1}{2^{r+1}-r-2}\,,
\]
which decreases strictly from \(4\) at \(r=1\) toward \(2\) as \(r\to\infty\). Hence \(\mathbb E[T]\le4\) for every \(n\ge2\) and initial coloring, with equality only for a nonunanimous initial \(K_3\). Moreover \(\varepsilon_r\sim 2^{-(r+1)}\).

For the exact law under independent initial blue probability \(p\in[0,1]\), let \(K\sim\operatorname{Bin}(n,p)\). With even \(n=2r\), the probabilities of all-blue, all-white and blinking outcomes are respectively \(\Pr(K>r)\), \(\Pr(K<r)\) and \(\Pr(K=r)\), and
\[
\mathbb E[T]=1-p^n-(1-p)^n-\Pr(K=r).
\]
With odd \(n=2r+1\), the probability of eventual all-blue is
\[
\Pr(K\ge r+2)+(1-\varepsilon_r)\Pr(K=r+1)+\varepsilon_r\Pr(K=r),
\]
and
\[
\mathbb E[T]=1-p^n-(1-p)^n+(E_r-1)\bigl(\Pr(K=r)+\Pr(K=r+1)\bigr).
\]
The odd all-white probability is the complement of the blue probability. These formulas include \(p=0,1\).

## Assumptions and scope
The graph is a **simple, loopless** complete graph. Opinions are binary. Updates are simultaneous and involve *all* other agents, not a random sample of neighbors and not an asynchronous one-at-a-time update. Tie coins are unbiased and mutually independent, conditionally on the current configuration. No claim is made for biased or correlated tie coins or other graph families. The notation \(T\) concerns entry into a closed class, not the time at which individual colors eventually stop alternating. In even balanced instances, agents continue alternating indefinitely.

## Proof
**Even order.** Every vertex has \(2r-1\) neighbors, so no neighborhood tie occurs. With exactly \(r\) blue agents, every currently blue vertex sees \(r\) white and \(r-1\) blue neighbors and hence turns white; every white vertex turns blue. The configuration therefore complements forever. From \(k>r\), a blue vertex sees \(k-1\ge r\) blue neighbors and a white vertex sees \(k\ge r+1\) blue neighbors; both update to blue. The case \(k<r\) is symmetric. These observations identify every closed class and every entrance time, including initial monochromatic configurations. Since the complement operation has no fixed balanced coloring, the number of balanced two-cycles is half the number of balanced configurations.

**Odd order.** Write \(n=2r+1\) with \(r\ge1\). Every vertex has \(2r\) neighbors. If \(k\ge r+2\), each initially blue vertex has at least \(r+1\) blue neighbors and each initially white vertex has at least \(r+2\); hence everyone becomes blue in the next round. If \(k\le r-1\), the same argument gives all white. If \(k=r+1\), every white vertex is forced to blue, while exactly the \(r+1\) blue vertices face ties, yielding the next blue count \(r+X\) with \(X\sim\operatorname{Bin}(r+1,1/2)\). From \(k=r\), the next blue count is \(X\) with the same law. The only possible continuing nonunanimous layers are therefore \(r\) and \(r+1\); all other nonunanimous states reach their corresponding unanimity after one further step.

Set \(a=2^{-(r+1)}\) and \(b=(r+1)2^{-(r+1)}\). In either critical layer, the next round reaches the opposite critical layer with probability \(a\), stays in the same critical layer with probability \(b\), reaches same-color unanimity directly with probability \(a\), and reaches a noncritical, not-yet-unanimous state with probability \(1-2a-b\). The latter state becomes unanimous in the following round. Since \(a+b=(r+2)/2^{r+1}<1\), the two critical layers are transient, proving almost-sure stabilization.

Let \(h_-\) denote the ultimate all-blue probability when the initial blue count is \(r\), and \(h_+\) the analogous probability for count \(r+1\). First-step decomposition gives
\[
 h_-=bh_-+ah_+,\qquad
 h_+=1-a-b+bh_++ah_-.
\]
Solving yields \(h_-=a/(1-b+a)=1/(2^{r+1}-r)\) and, by color symmetry, \(h_+=1-h_-\). The same decomposition for the critical expected time gives
\[
E_r=1+(a+b)E_r+(1-2a-b),
\]
where the last summand accounts for a second round needed by a noncritical intermediate state. Therefore \(E_r=(2-2a-b)/(1-a-b)=2+b/(1-a-b)=2+(r+1)/(2^{r+1}-r-2)\).

To see sharp uniform boundedness, \(a\) and \(b\) both decrease as \(r\) increases from one; the ratio \(b/(1-a-b)\) decreases, and at \(r=1\) it equals \(2\). Thus the unique maximal expected time is \(4\), attained in the two nonmonochromatic count layers of \(K_3\). Lastly \(r/2^{r+1}\to0\) gives the stated asymptotic. Conditioning on the binomial initial count proves the last two displayed outcome and time formulas.

## Verification
The accompanying `verify_clique_majority.py` independently constructs the exact blue-count transition probabilities, forms the transient-state Markov linear systems over rational numbers and compares their exact solutions to the theorem. It checks every initial blue count for each \(2\le n\le40\), comprising 858 count-state cases and 760 transient-state equations. It uses Python 3 and SymPy (no stochastic sampling). Run `python verify_clique_majority.py` after extracting the embedded file. This finite check corroborates, but does not replace, the unbounded analytic proof.

## Relationship to prior work
Zehmakan's 2023 original paper and the openly accessible 2024 article define synchronous independent fair-tie RMM and investigate stabilization and outcomes, in particular on cycle graphs. Their cycle result includes \(K_3=C_3\), so the three-agent case is **not** claimed as a new standalone result. Their general bounds and cycle classification do not supply the complete all-clique \(K_n\) parity law, one-vote reversal probability for odd \(n\ge5\), or its sharp expected stabilization-time formula. Earlier studies of majority dynamics with incumbent-retaining ties, asynchronous updating, or randomly sampled neighbors address different transition kernels, so do not imply the exact results for the specified dynamics. Elementary binomial and two-state Markov methods themselves are standard; the assessed contribution is the unified exact outcome and time law in this published model.

## Limitations
This result is for the complete graph and fair independent tie choices. In particular, it is not a statement that all RMM processes stabilize in constant time; general graphs can require exponentially many rounds. Prior-publication priority cannot be ruled out in unindexed literature. No independent external proof audit has been performed.

## References
- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, first public 2023-02-14. https://arxiv.org/abs/2302.06760
- A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems **38** (2024), article 21, DOI:10.1007/s10458-024-09651-y. https://link.springer.com/article/10.1007/s10458-024-09651-y
- N. Fountoulakis, M. Kang and T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, Random Structures & Algorithms (2020), DOI:10.1002/rsa.20970. https://doi.org/10.1002/rsa.20970
