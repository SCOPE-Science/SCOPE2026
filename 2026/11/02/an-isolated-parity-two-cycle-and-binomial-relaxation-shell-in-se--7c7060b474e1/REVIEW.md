# Scientific review: sequential bi-threshold dynamics on complete graphs

## Correctness: PASS

The hypotheses are explicit: a complete graph of size \(n\ge3\), fixed permutation-sequential sweeps, population in the closed neighborhood (all vertices), common up-threshold \(k\), down-threshold \(k+2\), and \(1\le k\le n-2\). At total population at most \(k-1\), no vertex activates; at least \(k+2\), none deactivates. The only transiently undecided populations \(k,k+1\) alternate on local flips until escape. A state not escaping in its first two updates must start with the mixed pair \(01\) at population \(k\), or \(10\) at population \(k+1\). These states cannot become constant after a single sweep; they either escape later or consist of a fully alternating word. Only odd dimensions at the central threshold give mutually complementing fully alternating states. Counting the two disjoint first-two-bit gates gives \(\binom{n-2}{k-1}+\binom{n-2}{k}=\binom{n-1}{k}\); subtract the two exceptional periodic words to get the exact second-entry shell. The count and statewise characterization are reconciled for \(n=3\) and every admissible threshold. The local central-binomial limit gives the probability law. This reconstructs the infinite proof without relying on finite experiments.

`verify.py` independently computes the microscopic updates for 360456 states over 78 pairs \((n,k)\), \(3\le n\le14\), and 196 further nonidentity-order parameter checks. Re-running produces the documented output. Finite checks alone are not an infinite-family proof.

## Originality: PASS (qualified)

The full publicly accessible texts of Kuhlman–Mortveit–Murrugarra–Kumar, *Bifurcations in Boolean Networks* (2011 preprint, arXiv:1108.2974), and Defant, *Binary Codes and Period-2 Orbits of Sequential Dynamical Systems* (2015 preprint, arXiv:1509.03907), were inspected in the relevant sections. The former gives the critical-gap bifurcation and arbitrarily long *sequential* periodic behavior on cycles and trees; its *synchronous* period-two statement does not classify this sequential complete-graph family. The latter gives universal restrictions and extremal counts of two-cycles for general homogeneous complete-graph Boolean functions, but not the static bi-threshold parameter window, zero extra cycles or the exact first-entry histogram. The abstract of Wu–Adiga–Mortveit (2014) concerns dynamic rather than fixed thresholds. Record searches by bi-threshold, complete graph, fixed order, alternating cycles, threshold gap and binomial entry times found no implication-equivalent statement. The current accessible earlier claims were compared by substance rather than titles; relevant parity-automa findings concern linear XOR dynamics, not threshold hysteresis.

Risks: Kuhlman–Mortveit's 2015 generalized multi-threshold paper is particularly plausible but its complete text was unavailable after preprint/open-access attempts, and the authorized institutional request returned unavailable. Other unindexed historical results could subsume the theorem. Thus this is a qualified best-knowledge originality assessment, not a uniqueness guarantee.

## Mathematical value: PASS

A gap of two is the earliest threshold separation permitting nonfixed recurrent orbits under permutation-sequential bi-threshold systems on some graphs. The complete graph forms a natural topological boundary to the arbitrarily long oscillations of cycles and trees. The all-size theorem gives a sharp **isolated parity-only oscillation window**, uniform two-sweep stabilization, an explicit binomial transient-shell population, and a central-window probability scaling. It explains how graph completeness suppresses long cycles while retaining exactly one exceptional oscillator. Those are natural orbit and basin invariants of the cited model, not an arbitrary small parameter slice or merely computational tabulation.

## References and limitations

- Kuhlman, Mortveit, Murrugarra, Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974; https://dmtcs.episciences.org/en/articles/2975/download (relevant full text inspected).
- Defant, *Binary Codes and Period-2 Orbits of Sequential Dynamical Systems*, arXiv:1509.03907; https://dmtcs.episciences.org/en/articles/2654/download (relevant full text inspected).
- Wu, Adiga, Mortveit, *Limit cycle structure for dynamic bi-threshold systems*, DOI:10.1016/j.tcs.2014.06.042 (abstract inspected).
- Kuhlman and Mortveit, *Limit Sets of Generalized, Multi-Threshold Networks*, Journal of Cellular Automata 10 (2015) 161–193 (abstract inspected; full text inaccessible).

Self-review: passed. Independent audit: not yet performed.
