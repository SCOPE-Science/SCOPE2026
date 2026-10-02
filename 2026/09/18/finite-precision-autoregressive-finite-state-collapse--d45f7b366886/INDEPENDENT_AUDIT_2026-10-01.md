    # Independent mathematical audit — 2026-10-01

    ## Record

    **Finite-state collapse and bounded autoregressive generation at q precision**

    Disposition: **PASSED**.

    ## Correctness — PASS

    The finite summary is sufficient under the stated Qiao finite-precision semantics on well-defined prefixes. Realized RoPE phases are periodic and hidden vectors range over a finite set. At a new causal position, old keys/values of the same layer, RoPE phase, and hidden type contribute identically. Capping a type count at \(10^{2q}+1\) is exact: any finite positive rounded exponential is at least \(10^{-q}\), so a saturated positive type forces the rounded denominator beyond \(10^q\) and hence to Inf, making the well-defined head output zero under the source convention; otherwise every positive multiplicity is stored exactly. Thus the prefix update and readout are deterministic functions of a finite state. The eventual-periodicity and bounded-halting conclusions then follow by pigeonhole on the deterministic orbit.

    ## Originality — PASS

    The motivating Qiao paper proves a narrower non-memorization result using finite-precision RoPE periodicity and softmax saturation, not a global streaming state for every prefix or an ultimate-periodicity theorem for iterative decoding. Jerad--Svete--Li--Cotterell characterize a related fully uniform periodic-RoPE recognizer class as a regular temporal-logic class, but their model and claim concern one-pass language recognition, not this explicit capped-histogram state and the uniform autoregressive-generation dichotomy in Qiao's q-decimal overflow semantics.

    ### Equivalent formulations

Searches: finite precision transformer autoregressive ultimately periodic bounded generation RoPE; finite state transformer chain of thought bounded halting length; published SCOPE search: Qiao RoPE finite state

Evidence: No exact global finite-state/autoregressive-periodicity theorem for Qiao's q-decimal model was located.

Reasoning: Generic finite-state-machine eventual periodicity is elementary, but the nontrivial point is proving that this attention model admits the exact finite streaming summary. The searched literature does not supply that summary for the same arithmetic semantics.

### Broader coverage

Searches: Qiao Yu Qiu Gao On the Turing Completeness of Transformers and Agents arXiv:2609.20335; Jerad Svete Li Cotterell Disentangling the Expressivity of RoPE arXiv:2608.11909; Characterizing the expressivity of fixed-precision transformer language models

Evidence: Qiao et al. give finite-precision non-memorization using periodicity/saturation; Jerad et al. give an exact language class for a related component-periodic model.

Reasoning: Neither inspected result dominates the iterative-generation statement in the exact Qiao arithmetic. The regular-language corollary is partly contextual prior art, so originality is restricted to the sufficient state and autoregressive consequences.

### Exact database or table

Searches: published SCOPE repository search: Qiao RoPE finite state; published-record semantic query: finite precision transformer bounded autoregressive generation

Evidence: Repository code search returned no additional matching published record; the semantic record-search service returned no usable result.

Reasoning: No database/table supplies the finite-state bound; this is a structural theorem.

### Claim versus prior implication

Searches: arXiv:2609.20335 Theorem 4.1 Appendix C finite precision RoPE; arXiv:2608.11909 component-periodic RoPE LTL modular

Evidence: The Qiao proof uses repeated-block families rather than an all-prefix state quotient. The Jerad theorem concerns recognition expressivity and a distinct periodic schedule realization.

Reasoning: The prior theorems do not automatically imply the explicit cap \(10^{2q}+1\), the stated state-count bound, or the bounded-halting/ultimate-periodicity theorem for Qiao decoding.

    ## Source inspections

    - **On the Turing Completeness of Transformers and Agents** (arXiv:2609.20335): trigger — defines the exact q-decimal arithmetic and finite-precision RoPE model used by the claim; material read — finite-precision definition and main finite-precision theorem; Appendix C numerical/overflow conventions, RoPE periodicity lemma, and repeated-position saturation argument; assessment — NOT_COVERING the all-prefix finite-state/autoregressive-periodicity claim. Evidence: The source proves non-memorization for a selected class and supplies the periodicity/saturation lemmas, but the inspected sections do not construct the capped histogram state or state the global decoding dichotomy.
- **Disentangling the Expressivity of RoPE** (arXiv:2608.11909): trigger — closest prior exact finite-precision periodic-RoPE language characterization; material read — abstract and detailed lawful public rendering of the periodic-RoPE theorem and model distinction; assessment — RELATED_BROADER_LANGUAGE_CONTEXT but not implication coverage of iterative Qiao decoding. Evidence: The paper characterizes component-periodic RoPE recognizers as \(LTL[P,MOD]\), a regular-language class, and distinguishes its engineered periodic schedule from conventional RoPE.

    ## Checked sources

    - arXiv:2609.20335
- arXiv:2608.11909
- arXiv:2310.07923
- published SCOPE repository searches

    ## Residual risks

    - The motivating and closest RoPE papers are extremely recent, so near-simultaneous work remains possible.
- The theorem is specific to the source's exact overflow and deterministic decoding conventions; it should not be generalized to ordinary floating-point transformers.

    ## Scientific value — PASS

    The theorem turns a model-specific incompleteness mechanism into a complete dynamical restriction on every deterministic autoregressive continuation: halting serial work is uniformly bounded and nonhalting continuations eventually cycle. That is a motivated structural boundary for finite-precision chain-of-thought models, not merely a one-input experiment.

    ## Limitations

    The theorem is specific to the exact q-decimal finite-precision, periodic realized RoPE, overflow, and deterministic decoding conventions of the cited model. It does not apply to ordinary floating-point or growing-precision systems.

    This document records a mathematical assessment of the stated claim and its literature context. It does not convert historical same-model review evidence into independent evidence.
