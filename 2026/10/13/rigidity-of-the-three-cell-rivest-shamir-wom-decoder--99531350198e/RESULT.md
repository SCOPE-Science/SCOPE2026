# Rigidity of the three-cell Rivest–Shamir WOM decoder
## Finding
Consider a binary write-once memory with \(n\) cells, initially \(0^n\), where a write may change coordinates only from \(0\) to \(1\). A decoder is a single interpretation function \(\alpha:\{0,1\}^n\to M\), used after either write, where \(M\) has four messages. Say that \(\alpha\) is *two-write extendable* if there is a monotone update rule that can realize every ordered pair of messages.

Three cells are necessary and sufficient. More strongly, if \(n=3\), every two-write-extendable decoder has the same fibers: the four antipodal pairs
\[
\{x,\mathbf 1-x\}\qquad (x\in\{0,1\}^3).
\]
Thus there are exactly \(4!=24\) labeled valid interpretation functions. After relabeling the messages as \(\mathbb F_2^2\), every such decoder is the Rivest–Shamir parity decoder
\[
\alpha(a,b,c)=(b\mathbin{\oplus}c,\,a\mathbin{\oplus}c).
\]
Equivalently, the decoding partition is the coset partition of the binary repetition code \(\{000,111\}\). The classical decoder is therefore forced by the two-write requirement, up to message relabeling.

## Assumptions and scope
The model is exactly the generation-independent binary WOM model of Rivest and Shamir: one interpretation function is used for every cell state, while an update may depend on both the current state and the desired new message and must move upward in the Boolean lattice. The claim classifies interpretation functions that admit at least one correct update rule. It does not classify arbitrary values of an update function on states that are never reached before the second write, and it does not impose synchronization or error correction.

## Proof
For a state \(u\in\{0,1\}^n\), write \(U(u)=\{z:z\ge u\}\) for its upper interval under coordinatewise order. If message \(m\) is written first to state \(u_m\), then every one of the four possible second messages must occur among the decoder labels on \(U(u_m)\). Hence \(|U(u_m)|\ge4\).

For \(n=2\), only \(00\) has an upper interval of size at least four, so four distinct first messages cannot all have suitable first-write states. Thus two cells are impossible.

Now let \(n=3\). Since \(|U(u)|=2^{3-\mathrm{wt}(u)}\), every first-write state has weight at most one. There are exactly four such states, \(000,e_1,e_2,e_3\), and the four first messages require four distinct decoder labels, so these four states are precisely the first-write representatives. Relabel the messages so that \(\alpha(000)=0\) and \(\alpha(e_i)=i\) for \(i=1,2,3\).

Each \(U(e_i)\) has exactly four states and must contain all four labels exactly once. The state \(111\) lies in all three upper intervals. Its label cannot be any of \(1,2,3\), because that label would duplicate \(\alpha(e_i)\) in the corresponding \(U(e_i)\). Therefore \(\alpha(111)=0\).

For distinct \(i,j,k\in\{1,2,3\}\), the weight-two state \(e_i+e_j\) belongs to both \(U(e_i)\) and \(U(e_j)\). In the first upper interval it must have one of the two labels different from \(0\) and \(i\); in the second it must have one of the two labels different from \(0\) and \(j\). Their only common possibility is \(k\). Hence \(\alpha(e_i+e_j)=k=\alpha(e_k)\). This pairs every state with its bitwise complement and proves the antipodal partition.

Conversely, the antipodal partition is two-write extendable. Use \(000,e_1,e_2,e_3\) as first-write representatives. The interval \(U(000)\) contains all four labels, and each \(U(e_i)\) contains each label exactly once, so a monotone representative of any desired second message always exists. This proves necessity, sufficiency, and uniqueness up to relabeling.

Finally, the four antipodal fibers are exactly the fibers of \(\alpha(a,b,c)=(b\mathbin{\oplus}c,a\mathbin{\oplus}c)\). Since every permutation of the four elements of \(\mathbb F_2^2\) is affine, all \(24\) labeled decoders are output relabelings of this one.

## Verification
The accompanying `verify.py` independently enumerates all \(4^4=256\) decoders on two cells and all \(4^8=65,536\) decoders on three cells. A decoder is accepted exactly when each of the four messages has a first-write state whose upper interval contains all four labels. It finds no valid two-cell decoder and exactly \(24\) valid three-cell decoders. It also checks that every valid three-cell decoder is an output relabeling of the antipodal partition and that the displayed parity decoder induces exactly that partition.

A replay of the packaged verifier returns:
`VERIFY_OK n2_valid=0 n3_valid=24 all_antipodal=true one_output_relabeling_class=true`.

## Relationship to prior work
Rivest and Shamir introduced the WOM model and gave the three-cell, four-message, two-write construction as a motivating example, together with the parity decoder. Their formal model specifies a single interpretation function and monotone update function, but the inspected paper does not classify all interpretation functions for the example. The conference version first appeared on 1982-05-05; the later journal version gives the same construction in Table 1.

Haymaker and Kelley later call this the canonical WOM example, reproduce its two codebooks, and state the same parity decoder. Their treatment uses it as a building block for multilevel and geometric WOM constructions rather than giving an equality classification.

A public catalogue of short two-write binary WOM codes lists one length-three \(\langle4,4\rangle/3\) instance and records exactly the canonical mapping `0,1,2,3,3,2,1,0`; the catalogue describes itself as a list of known individual code instances, not an exhaustive classification of all decoders. OEIS A253548 records that four symbols require three holes and gives the same example, but likewise does not classify all valid interpretation maps. The present result supplies that missing rigidity statement.

The topic is within coding and information theory in computer science; a later write-once-memory paper explicitly lists AMS classification 68P30.

## Limitations
The classification is for exactly four messages, two writes, binary cells, and a generation-independent decoder. It does not classify full update functions: once the forced decoder is fixed, there can still be different choices of second-write representative from the all-zero first state, and update values on unreachable states are immaterial. It also does not address larger alphabets, more writes, error correction, or decoders that are additionally told the generation number.

## References
1. R. L. Rivest and A. Shamir, *How to Reuse a “Write-Once” Memory (Preliminary Version)*, STOC 1982, pp. 105–113, published 1982-05-05, DOI 10.1145/800070.802182.
2. R. L. Rivest and A. Shamir, *How to Reuse a “Write-Once” Memory*, Information and Control 55 (1982), 1–19, DOI 10.1016/S0019-9958(82)90344-8.
3. K. Haymaker and C. A. Kelley, *Geometric WOM codes and coding strategies for multilevel flash memories*, arXiv:1206.5762.
4. B. Dobbelaere, *Short 2-write binary WOM code list*, public catalogue, entry for the length-three four-by-four code.
5. OEIS A253548, *Minimal width for a paper tape with one guaranteed reuse*.
6. T. Moran, M. Naor, and G. Segev, *Deterministic History-Independent Strategies for Storing Information on Write-Once Memories*, Theory of Computing 5 (2009), 43–67; AMS classification includes 68P30.
