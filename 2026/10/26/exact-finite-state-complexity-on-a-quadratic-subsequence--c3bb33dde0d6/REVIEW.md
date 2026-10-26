# Review

**Correctness — PASS.** For a transducer with \(s\) states, total stored transition-output length \(L\), and input length \(k\), the encoding costs at least \(2L+4s\), while the output length \(n\) satisfies \(n\le kL\). Hence every description costs at least \(2\sqrt{2n}+4s\ge2\sqrt{2n}+4\). The one-state construction with outputs \(0^a\) and \(arepsilon\) on input \(0^{2a}\) attains \(4a+4\) when \(n=2a^2\).

**Originality — PASS, with residual risk.** The inspected thesis establishes only \(C(0^n)\in\Theta(\sqrt n)\) with coarser constants; the inspected 2010 paper supplies the encoding framework but does not state this exact subsequence result in the examined sections. published-finding corpus semantic searches returned no directly matching claim. A related 2011 journal article was not inspected in full.

**Value — PASS.** The equality indices are forced by the lower-bound optimization, rather than chosen as an arbitrary finite slice. The result supplies exact values on an infinite natural subsequence and identifies the sharp equality case of a universal storage-versus-input lower bound.

**Closest literature and limits.** Roblot, *The Computation of Finite-State Complexity* (2011), Theorem 26, pp. 17–18; Calude, Salomaa, and Roblot (2010), arXiv:1008.1667. Values away from \(n=2a^2\) remain open here.

Self-review: passed. Independent audit: not yet performed.
