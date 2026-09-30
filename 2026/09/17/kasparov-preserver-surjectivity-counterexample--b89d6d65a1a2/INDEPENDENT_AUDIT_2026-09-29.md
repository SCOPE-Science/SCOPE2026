# Independent audit — 2026-09-29

Record: `2026/09/17/kasparov-preserver-surjectivity-counterexample--b89d6d65a1a2`  
Assigned and audited source tree: `3fa4a3fabaa01a73a0418d4049611897a2d04dd3`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The amplification counterexample is correct under the literal hypothesis transcribed by the record. For a unitary U:H⊕H→H, Phi(T)=U(T⊕T)U* sends compacts to compacts and induces an injective unital *-endomorphism Psi of the Calkin algebra. Injectivity makes Calkin-unitarity equivalent before and after Psi, and an injective unital C*-homomorphism preserves spectrum. The range is proper: every T⊕T commutes with P=diag(I,0), while the flip F has [P,F] with identity off-diagonal entries and hence noncompact commutator, so q(UFU*) cannot lie in the range. Thus a condition of the form 'for every T there exists S with Phi(T)-S compact' is vacuous and cannot imply quotient surjectivity. The proposed repair using target-surjectivity modulo compacts correctly makes the quotient map onto; unitary preservation/reflection then yields a bounded Jordan *-automorphism, and the kernel argument with 1±a is valid. The Hamel-complement projection also correctly shows that equality Phi(K(H))=K(H) does not follow from the literal algebraic hypotheses when continuity is not imposed.

## Originality

**qualified_current_correction**. Sharifi's arXiv preprint was posted 16 September 2026 and its current public abstract still states the surjectivity-mod-compacts automorphism theorem. Targeted searches through 29 September found no public erratum, revised version, or independent correction of the specific reversed/vacuous condition. Older linear-preserver literature supplies the standard target-surjectivity convention, so novelty is only claimed for diagnosing this particular 2026 statement and giving the explicit Calkin amplification counterexample and repair.

## Scientific value

**high_value_targeted_correction**. A vacuous hypothesis in a theorem about induced Calkin automorphisms is a substantive correctness issue, and the record does more than flag it: it gives a transparent counterexample, states the standard quotient-surjectivity replacement, and repairs the core Kasparov-cycle theorem. This has immediate value for readers of the very recent preprint.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/kasparov-preserver-surjectivity-counterexample--b89d6d65a1a2
- https://arxiv.org/abs/2609.18619
- https://doi.org/10.3390/math11092208
- https://doi.org/10.1016/j.jmaa.2009.01.032

## Limitations

- The finding concerns the literal current preprint statement and may be superseded by an author revision.
- The independent audit verified the counterexample and repair algebraically; the exact displayed definition was available through the archived record transcription rather than a separately parsed full-text copy of the preprint in this run.
- The repaired argument is complete for the Kasparov-cycle automorphism conclusion, not a replacement proof for every spectral-preserver statement in the preprint.
- The Hamel-complement example is algebraic and discontinuous; it addresses the literal linear-map hypotheses and would not by itself refute an added boundedness assumption.
