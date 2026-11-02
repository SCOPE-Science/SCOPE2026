# Scientific review: Six agents are necessary and sufficient for cycling in two-coalition cutoff hedonic games

**Correctness — PASS.** The exact lower-bound exhaustion ranges over all labeled undirected enemy graphs and unordered nonempty two-coalition partitions for 2–5 players. This covers every cutoff instance, including all line embeddings. Singleton departures cannot improve, so states with one coalition cannot be in a cycle. The eight transitions of the six-person example strictly reduce the moving player's rational cost. The included `check.py` reproduced 1,098 graphs, 15,834 graph-state pairs, and 28,108 improving edges; it checked all eight strict decreases.

**Originality — PASS, subject to publication-priority risk.** The relevant 2026 preprint proves existence of cycles with a larger construction. Its inspected statements do not imply the exact minimum population or exclusion below six. Older group-formation literature uses average-distance incentives, not the ratio-of-enemies payoff. Targeted mathematical-record and literature searches found no equivalent exact threshold; unindexed work remains a possibility.

**Value — PASS.** A sharp minimum population is a natural structural boundary for nonconvergent updating, and the five-player impossibility strengthens the line-restricted theorem to all symmetric enemy relations. The example is shorter than the motivating construction and establishes attainability within the original line setting.

**Limitations.** The conclusion is for HIS cutoff costs, at most two coalitions, and strict unilateral jumps into existing coalitions. Neither multi-coalition cases nor other incentive rules are settled. No claim of publication priority or independent scientific validation is warranted.

Self-review: passed. Independent audit: not yet performed.
