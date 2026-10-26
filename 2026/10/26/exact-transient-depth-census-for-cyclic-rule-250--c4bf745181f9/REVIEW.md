# Scientific review

## Correctness — PASS

For every binary cyclic ring of length at least three, the \(t\)-step occupied set equals the original occupied set translated by the length-\(t+1\) \(+2\)-walk interval. The exact first time at which all active step-two components are filled is therefore the maximum cyclic gap minus one. An OR-neighbor periodic configuration must already be invariant under the two-step support expansion, forcing each step-two orbit either full or empty. The rooted-gap bijection gives the polynomial \(B_{q,h}\); orbit independence yields the even-ring square, while the singleton condition and inclusion-exclusion establish both sharp extremizer counts. The source-code checker explicitly compared all 131,064 configurations for sizes 3–16 and 4,800 larger samples. The unrestricted proof is analytical.

## Originality — PASS under inspected evidence

Wolfram's 1983 introduction and MathWorld give Rule 250's OR-neighbor identity, but not an all-size initial-state preperiod histogram. Wolfram's 1984 full article derives structural regular-language properties and periodic sets, not the present cyclic maximum-gap and fixed-weight census. Stricker's 2023 inspected paper covers the set of possible finite-ring *cycle lengths*, rather than counts of states at each exact transient depth. Zhu and Richard's 2026 openly accessible article classifies ECA Koopman spectra but neither develops this fixed-weight transient-time polynomial nor yields the proposed closed count. Actual semantic literature searches for Rule 250, OR-neighbor relaxation, cyclic longest gaps, periodic orbits and finite-state preperiods surfaced other CA dynamics but not this statement. Previously available related claims on cyclic majority Rule 232, sequential Rule 254, and conservative Rule 184 were compared at the level of their hypotheses and do not imply the synchronous Rule-250 census. Accessible searches cannot establish absolute historical priority; the 1982 preprint preceding the 1983 source and historical general Boolean-CA results remain potential risks.

## Mathematical value — PASS

The all-size, all-weight, all-transient exact enumeration solves a natural finite-state dynamical census: it quantifies precisely how fast an OR-additive cellular automaton loses its initial-support structure, not just which attractor it reaches. The parity-dependent sharp absorption times and exact counts of maximally slow initial conditions provide finite-size reference cases for Boolean-network relaxation and show that the apparent uniformly ordered limit hides different labelled-state convergence distributions. Counting by maximum gap is standard combinatorics, but the complete dynamical identification and enumeration together answer a substantive classification question. No claim is made that the underlying inclusion-exclusion identity is new.

## Sources and limitations

The closest inspected mathematical sources are Wolfram (1984, formal-language theory, https://scispace.com/pdf/computation-theory-of-cellular-automata-4snltftqhc.pdf), Stricker (2023, cycle-length spectra, https://content.wolfram.com/sites/13/2024/01/32-3-1.pdf), and Zhu–Richard (2026, finite Koopman spectra, https://arxiv.org/html/2610.10967v1). The Rule-250 definition is independently stated by MathWorld (https://mathworld.wolfram.com/Rule250.html), and the early motivating paper is Wolfram (1983, DOI 10.1103/RevModPhys.55.601). Exhaustive finite computation cannot establish general validity, and historical priority remains uncertain without further specialist review. The result does not address asynchronous updates or infinite spatial lattices.

Self-review: passed. Independent audit: not yet performed.
