# Independent Audit — Exponentially sharp logarithmic asymptotics for totative dominance thresholds

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `9864a7a17079b3645e45d085ef02788a4b74b681`  
**Audited current source tree:** `9864a7a17079b3645e45d085ef02788a4b74b681`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree is the assigned source tree. GitHub was used read-only. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. The primorial lower-envelope argument is consistent with classical extremality of n/phi(n), the de la Vallée Poussin-strength prime number theorem, and the corresponding Mertens product estimate. If p_j#<=n<p_{j+1}#, then x=p_j and y=log n satisfy y=x(1+O(exp(-c sqrt(log x)))), giving phi(n)/pi(n)>=e^{-gamma} y/log y times the same relative accuracy. Since A(n)<=pi(n), the shifted lower envelope for B(n)>kA(n) follows from B>kA iff phi>(k+1)A. Primorials P(x) match both envelopes because omega(P(x)) is exponentially negligible relative to pi(P(x)). Inverting F(y)=e^{-gamma}y/log y localizes the last failures at Y(h) with the stated exponential relative error. The Lambert-W expansion and the bound on log(N_{k+1}/M_k) then follow.

## Originality — PASSED

PASS, narrowly scoped. Fatehizadeh's current public statement proves exact small thresholds, M_k<=N_{k+1}, and equality for k<=5, but does not give asymptotic growth of N_k or M_k. Classical minimal-order totient estimates and Mertens/PNT estimates are prior work and receive no novelty credit. Targeted searches found no prior formula localizing these two newly defined threshold sequences at the Lambert-W inverse with de la Vallée Poussin relative accuracy.

## Scientific value — PASSED

PASS. The theorem supplies the first asymptotic scale for both exact threshold sequences and shows that the conjecturally equal pair M_k and N_{k+1} is exponentially close on the logarithmic scale. This complements, rather than repeats, the source's finite exact computations and clarifies the large-k structure of its conjecture.

## Independent checks

- Re-derived the uniform lower envelope from the primorial bound, PNT and Mertens product, including the conversion x≈log n.
- Re-derived the matching primorial witness and checked that omega(P(x))/pi(P(x)) is negligible at the asserted error scale.
- Checked the identity B>kA iff phi>(k+1)A and the consequent shift from k to k+1.
- Differentiated F at Y(h) and verified that the envelope errors translate into relative Y-errors of the same exponential order.
- Re-derived the Lambert W_{-1} representation and the displayed logarithmic expansion.
- Compared against Fatehizadeh's current public abstract, which lists exact small thresholds and M_k<=N_{k+1} but no large-k asymptotic formula.
- Verified no files under the assigned record changed between the dispatcher source-check commit and current main, and verified both dated independent-audit files and FAILED_ATTEMPT.md are absent.

## Limitations

- The result is asymptotic and does not prove the exact conjecture M_k=N_{k+1}.
- It relies on standard zero-free-region estimates and does not optimize their constant c.
- The motivating threshold problem is very recent, leaving a residual risk of contemporaneous unindexed work.

## Evidence and references

- https://arxiv.org/abs/2609.13852
- https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-6/issue-1/Approximate-formulas-for-some-functions-of-prime-numbers/10.1215/ijm/1255631807.full
- https://www.numdam.org/articles/10.5802/jtnb.1251/
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/totative-dominance-threshold-asymptotics--b4acd8c94b4b

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
