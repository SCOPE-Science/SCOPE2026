# Independent mathematical audit

## correctness

PASS

Every complete allocation with common utility t must consume t|S| approved distinct goods from Γ(S), so t≤κ. In the κ-copy matching, any subset of slots has precisely the neighborhood of its represented agents and is no larger than κ times their number, so Hall applies. Counting approvals gives |Γ(S)|≥d|S|/2. With n≥3, even a double-approved leftover has a nonapprover; assigning all leftovers this way preserves κ. Agent i values goods in any other single bundle at most d−κ, so envy is at most one, and zero for even d. Binary search over feasible slot counts up to d is polynomial with the explicit incidence representation. In the exact-two case m=nd/2 and the whole-agent capacity bound forces κ=floor(d/2), giving the claimed additive welfare loss. Assigning to endpoints attains m and is PO; conversely any good assigned to a nonapprover can be moved to an approver without reducing anyone's utility, so PO requires welfare m. This supplies the explicit implication needed for exclusion of EQ+PO at odd d, not just a comparison with maximum welfare. Balanced orientation by auxiliary pairing and Euler tours yields each indegree floor(d/2) or ceil(d/2); the same outside-approvals bound gives EF1, and full EF at even d. Empty or zero-approved goods do not invalidate the proof; odd d implies even n. The n=2 single shared good demonstrates the completion boundary. Independent replay `cd /workspace && python checks/independent_replay.py 5` enumerated 40,854 complete allocations on 11 fixtures, including zero/singleton approvals and parallel goods, checked the exact optimum over EQ allocations with and without the required envy bound, and corroborated the efficient parity guarantees. The replay and frozen census are finite checks, not the proof.

## originality

PASS

The supported original contribution relative to the evidenced earlier work is an optimal complete exact-EQ and EF1 guarantee for all normalized rank-two approval profiles with n≥3, together with the quantitative exact-equity versus efficiency contrast on the regular exact-two subfamily. The matching and balanced-orientation tools, binary EQ+PO implying EF, and the overlapping degree-two efficient case are not new. There is demonstrable equivalent catalogue coverage of the central Hall/EF1 optimum in the not-identical record 06daff579d6d over D≥2 (zero-approved goods can be dropped), and thus also of its exact-two optimal EQ welfare by specialization. That record is dated November 8 versus this record's November 2; it establishes overlap, not prior coverage. No exact earlier covering theorem for the supported contribution was established by the statement checks. This is not a claim that the result is unique across the current catalogue or that within-day priority is settled.

## value

PASS

This sparse graphical family is both a natural test of simultaneous envy and equitability and broad enough to allow nonlaminar systems and parallel goods. The theorem finds the full exact-EQ utility frontier while retaining EF1, even when completion must waste items and an endpoint-only fair allocation cannot be exactly equal. The exact-two additive gap n/2 and its disappearance after a one-unit relaxation give a useful concrete boundary, not a new assertion about Euler tours in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
