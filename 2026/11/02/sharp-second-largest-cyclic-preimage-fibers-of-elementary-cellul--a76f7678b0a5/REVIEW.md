# Scientific review: cyclic Rule-18 second-largest preimage fibers

**Correctness — PASS.** The two-matching zero-run decomposition is proved for all positive output weights, including the small ring cases. Independent Fibonacci corridor counts give the exact formula; strict inequalities prove the sharp modal ranking for every \(n\ge7\). The included `verify.py` reconstructs output fibers directly for \(1\le n\le16\), tests all \(131070\) possible outputs and checks independent transfer traces for \(n\le11\). This computational evidence corroborates, but does not replace, the general proof.

**Originality — PASS (historical-priority qualification).** Jen (1989) supplies general finite-block preimage recurrence machinery and Powley (2009) establishes the same rule's all-zero cyclic count; Fukś (2003; posted to arXiv May 2013) treats sequences of preimage numbers. None of the inspected relevant statements gives the sharp all-nonzero second mode or its complete equality cases. The comparison explicitly acknowledges that broader recurrence methods might imply the theorem once additional arguments are supplied. The 2010 homogeneous-count article was accessible in bibliographic abstract only; an unseen historical equivalent remains a risk.

**Value — PASS.** The result identifies the exact runner-up likelihood and all maximizing nonzero outcomes in an inverse-image distribution for a standard deterministic cellular automaton. The new natural invariant and infinite family are motivated by inverse uncertainty and extend beyond the known homogeneous count.

The theorem is restricted to one synchronous Rule-18 step on indexed cyclic binary rings, with ranking for \(n\ge7\). There is no independent validation or publication-priority certification.

Self-review: passed. Independent audit: not yet performed.
