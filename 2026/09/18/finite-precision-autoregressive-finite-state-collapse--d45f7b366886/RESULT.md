# Finite-state collapse and bounded autoregressive generation at q precision

## Result

Consider the fixed-architecture causal soft-attention transformer model of Qiao, Yu, Qiu and Gao (2026), with finite vocabulary \(\Sigma\), depth \(D\), hidden width \(W\), and their \(q\)-decimal arithmetic. In this arithmetic every scalar is rounded to \(q\) decimal places inside \([-10^q,10^q]\), overflow is represented by `Inf`, and softmax uses their explicitly rounded numerator and denominator rules. Assume a fixed deterministic tie-breaking rule for next-token argmax, and consider prefixes on which the next-token computation is well-defined.

Let \(C\) be the finite period of the \(q\)-precision RoPE matrices from Qiao et al., so
\[
A_{i+C}=A_i
\qquad\text{for every }i.
\]
Put
\[
V_q=2\cdot 10^{2q}+3,\qquad
R_q=V_q^W,\qquad
B_q=10^{2q}+1.
\]
Here \(V_q\) is an upper bound for the number of scalar \(q\)-precision values after adjoining the special values `Inf` and `NaN`, and \(R_q\) therefore bounds the number of possible width-\(W\) hidden vectors.

Then every nonempty prefix \(s\) has a finite summary \(\Phi(s)\) taking at most
\[
\boxed{
S_q
=
C R_q (B_q+1)^{C D R_q}
}
\tag{1}
\]
values, with the following properties.

1. **Streaming sufficiency.** For every token \(a\in\Sigma\), \(\Phi(sa)\) is determined solely by \(\Phi(s)\) and \(a\).
2. **Readout sufficiency.** The next token chosen after \(s\) is determined solely by \(\Phi(s)\).
3. **Autoregressive dichotomy.** Starting from any input, generation either emits the end token within at most \(S_q\) generated non-end tokens, or else the infinite generated continuation is ultimately periodic. Its preperiod is \(<S_q\) and its period is at most \(S_q\).
4. **Finite range for total generators.** If the transformer halts on every input, its output lengths are uniformly bounded by \(S_q\), and hence its total string-valued input-output map has finite range.
5. **Regularity for total deciders.** If a total decision procedure is implemented by reading the input and then running this autoregressive decoder to a finite accept/reject outcome, the accepted language is regular.

Thus, in the exact finite-precision semantics of Qiao et al., an unbounded chain of thought cannot provide an unbounded serial workspace: every halting chain has a model-dependent constant length bound, independent of the input length.

## Finite sufficient state

For a prefix \(s=s_1\cdots s_n\), let
\[
h^{(m)}_i(s)\in\mathcal H_q
\]
be the hidden vector at position \(i\) entering transformer block \(m+1\), where \(m=0,\ldots,D-1\). Causality implies that appending tokens never changes \(h^{(m)}_i\) at an already existing position.

For every layer \(m\), residue \(r\in\mathbb Z/C\mathbb Z\), and hidden type \(h\in\mathcal H_q\), define
\[
N_{m,r,h}(s)
=
\#\{i\le n:\ i\equiv r\pmod C,\ h^{(m)}_i(s)=h\}.
\]
Store only the capped count
\[
\widetilde N_{m,r,h}(s)
=
\min\{B_q,N_{m,r,h}(s)\}.
\tag{2}
\]
The summary \(\Phi(s)\) consists of

- \(n\bmod C\);
- the final-position hidden vector after the last transformer block; and
- all capped counts (2), for \(m=0,\ldots,D-1\).

There are at most \(C D R_q\) capped counters, each with \(B_q+1\) possible values, and at most \(C R_q\) choices for the phase and final hidden vector. This gives (1). An additional start state handles the empty prefix.

## Why capped counts determine attention exactly

Fix one attention head while computing the newly appended final position. Once the current query hidden vector and current residue modulo \(C\) are known, every old position with the same pair
\[
(i\bmod C,\ h^{(m)}_i)
\]
has the same relative-RoPE matrix, the same attention logit, the same rounded exponential numerator \(E\), and the same value vector. Hence a head depends on old positions only through the counts of these finitely many types. In causal self-attention the newly appended current position is included as well; after its hidden type at the relevant layer has been computed, it is inserted with multiplicity one before evaluating that layer's head.

The only issue is that a count in (2) may have been truncated. Qiao et al.'s softmax convention makes exactly this truncation sufficient. Every positive \(q\)-decimal exponential numerator is at least \(10^{-q}\). Therefore, if a type with positive numerator occurs at least
\[
B_q=10^{2q}+1
\]
times, its contribution to the softmax denominator is already strictly larger than \(10^q\). The rounded denominator is then `Inf`. By their convention
\[
c/\mathrm{Inf}=0,
\]
every attention weight in that head is zero, so the head output is exactly zero.

If no positive-numerator type has reached the cap, every positive type has its exact count stored in (2). Zero-numerator types contribute nothing. The exact rounded denominator and each coordinate of the attention output can therefore be reconstructed from the stored finite counts. This remains true if several individually unsaturated types jointly overflow the denominator, because all of their counts are then known exactly.

Consequently the attention output at the new final position is determined by the summary and the new token. Positionwise residual and feed-forward operations are fixed \(q\)-precision maps on a finite set, so the new hidden vector is determined as well. Proceeding block by block determines the new hidden vector at every layer and updates the corresponding capped counters. This proves streaming sufficiency.

The output layer of Qiao et al. is applied only to the final position, so the final hidden vector determines the logits and, with fixed tie-breaking, the next token. This proves readout sufficiency.

## Autoregressive consequences

After the input has been scanned, autoregressive generation is therefore a deterministic orbit on a finite state set:
\[
\Phi_0\longmapsto \Phi_1\longmapsto\Phi_2\longmapsto\cdots .
\]
If the end token appears before a state repeats, generation halts. Otherwise two states among the first \(S_q+1\) states coincide. Determinism then forces the future states, and hence the future emitted tokens, to repeat periodically. This proves the dichotomy and the uniform bound for halting generations.

If the decoder halts for every input, only strings of length at most \(S_q\) over the finite vocabulary can be outputs, so the range is finite.

For a total decision procedure, the same finite summary can be updated token by token while scanning the input. Whether the subsequent deterministic generation eventually reaches the designated accept outcome is a property of the resulting summary state. The accepting inputs are therefore the inverse image of a finite set of summary states under a finite-state streaming transition, hence form a regular language.

## Relation to the motivating result

Qiao et al. prove that a fixed \(q\)-precision transformer cannot memorize a **non-converging** Turing machine, where a non-converging machine has a family \(xy^nz\) of halting inputs with pairwise distinct outputs. Their proof combines finite-precision RoPE periodicity with softmax saturation on sufficiently many repeated positions.

The finite-state summary above uses the same two model-specific facts but removes the repeated-input ansatz. It applies simultaneously to every prefix and therefore yields a global dynamical statement: every non-halting autoregressive continuation is ultimately periodic, while every halting continuation has a uniform constant length bound. In particular, the obstruction applies not only to infinite-range string functions but also to total nonregular decision problems with a fixed-size final answer.

The regular-language corollary is not claimed as a new general characterization of periodic-RoPE transformers. Jerad, Svete, Li and Cotterell (2026) independently characterize a related fully uniform finite-precision soft-attention model with component-periodic RoPE as exactly \(\mathrm{LTL}[P,\mathrm{MOD}]\), a regular-language class. Their finite-precision realization differs from Qiao et al.'s explicit q-decimal phase recursion and overflow semantics. The new claim here is the explicit capped-histogram sufficient state for the Qiao model and the resulting **uniform bounded-generation / ultimate-periodicity theorem for iterative autoregressive decoding**.

Merrill and Sabharwal (2024) show that chain-of-thought can increase transformer expressivity under a different theoretical model, with power depending on the number of decoding steps. The present result does not contradict that work: the collapse here relies on Qiao et al.'s fixed q-decimal arithmetic, periodicized RoPE, and overflow rule.

## Scope and limitations

The theorem is specific to the finite-precision semantics defined by Qiao et al. It does not apply to their infinite-precision model, to precision growing with input length, to external memory or tools, or to architectures whose positional state is not periodic in the realized computation. It also assumes a well-defined deterministic next-token choice; a fixed tie-breaking convention suffices.

The numerical state bound (1) is deliberately crude. It counts every possible width-\(W\) q-precision hidden vector at every layer and phase, even though a particular transformer may realize only a tiny subset. No optimality claim is made for the bound.

The originality claim is to the best of our knowledge. The closest identified prior result is the exact regular-language characterization for component-periodic RoPE by Jerad et al.; that prior result is explicitly excluded from the novelty claim. The inspected Qiao et al. full text was arXiv:2609.20335v1 dated 17 September 2026. Because the motivating preprint is extremely recent, later revisions or near-simultaneous notes remain a material originality risk.

## References

1. Y. Qiao, L. Yu, R. Qiu and X.-S. Gao, *On the Turing Completeness of Transformers and Agents*, arXiv:2609.20335, 2026. https://arxiv.org/abs/2609.20335
2. S. Jerad, A. Svete, J. Li and R. Cotterell, *Disentangling the Expressivity of RoPE*, arXiv:2608.11909, 2026. https://arxiv.org/abs/2608.11909
3. W. Merrill and A. Sabharwal, *The Expressive Power of Transformers with Chain of Thought*, ICLR 2024; arXiv:2310.07923. https://arxiv.org/abs/2310.07923
