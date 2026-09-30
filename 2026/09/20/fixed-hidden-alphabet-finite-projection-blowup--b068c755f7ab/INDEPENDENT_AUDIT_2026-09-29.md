# Independent Audit — Fixed hidden alphabets preserve almost all finite-language projection blow-up

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `30e8d01115cd5b67111fc93963a9c78c1c05e403`  
**Audited current source tree:** `30e8d01115cd5b67111fc93963a9c78c1c05e403`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Replacing L distinct erased transitions out of the initial state by a rooted deterministic h-ary erased routing tree preserves the projected language: the epsilon-closure of the initial state contains the same original chain states, routing vertices have no visible behavior, and after the first visible transition no erased routing edge is available. The optimal routing overhead J follows from the exact edge-capacity inequality J+L<=h(J+1) and is achieved by a partially filled h-ary tree. The resulting input automaton is acyclic. Its chain states remain distinguished by visible accepting continuation length; routing states are distinguished from chain states by the need for an erased prefix and from one another by descendant-leaf continuations. The algebra converting N to n_N gives the stated exponent alpha_{k,h} and retained fraction rho_{t,h}; the epsilon choice indeed makes rho>1-epsilon.

## Originality — PASS

PASS. The open 2011 Jirásková--Masopust paper explicitly states, immediately before its finite-language k-letter lower-bound construction, that the domain alphabet in that construction is required to grow linearly with the number of states and that it remains open whether the domain alphabet can be bounded by a constant. The audited routing construction gives a concrete fixed-hidden-alphabet partial answer with quantified linear overhead and an exponent approaching the original rate. Targeted later-literature searches found fixed-alphabet results for other automata problems and projection subclasses, but no construction subsuming this finite-language tradeoff. Generic alphabet coding and finite-NFA determinization bounds are prior work and receive no novelty credit.

## Scientific value — PASS

PASS. The result addresses an explicit long-standing open aspect of the finite-language projection witness: it shows that a state-independent domain alphabet can preserve an arbitrarily large fraction of the known exponential rate. The exact overhead bound in the natural routing-only replacement model makes the tradeoff transparent. It does not overclaim the still-open exact fixed-alphabet exponent.

## Independent checks

- Read the open 2011 State Complexity of Projected Languages PDF; its finite-language section explicitly says the lower-bound construction needs a linearly growing domain alphabet and asks whether it can be bounded by a constant.
- Reconstructed the epsilon-closure argument showing that the routed and direct-fanout witnesses have the same visible projected language.
- Reproved the optimal routing-state count from deterministic h-ary outdegree and the matching tree construction.
- Rechecked acyclicity and distinguishability of all original and routing states.
- Recomputed the N-to-n_N asymptotics, alpha_{k,h}, rho_{t,h}, and the epsilon tradeoff.
- The later 2012 TCS source could not be obtained through authorized retrieval without human verification; no inaccessible text was claimed as read, and the 2011 open source already states the relevant constant-domain question.
- GitHub comparison found no changes under the assigned record path; both UTC-dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The construction approaches but does not attain the exact Jirásková--Masopust exponent with one fixed domain alphabet.
- The routing-overhead optimality is only for the stated deterministic routing-only replacement model, not for every conceivable fixed-alphabet witness.
- The 2012 journal full text remained behind human verification in this run; the relevant open question was independently verified in the openly available 2011 paper.

## Evidence and references

- https://users.math.cas.cz/~masopust/pubs/2011/dcfs2011.pdf
- https://doi.org/10.1007/978-3-642-22600-7_16
- https://doi.org/10.1016/j.tcs.2012.04.009
- https://dblp.org/rec/journals/jalc/SalomaaY97
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/fixed-hidden-alphabet-finite-projection-blowup--b068c755f7ab

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
