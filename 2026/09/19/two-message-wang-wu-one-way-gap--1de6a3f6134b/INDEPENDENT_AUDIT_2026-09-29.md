# Independent audit — Two messages suffice for the Wang–Wu separation, while one message costs polynomially more

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/two-message-wang-wu-one-way-gap--1de6a3f6134b`  
**Audited tree:** `df27d973c99b073ab2c20a860d383cdec7fb9cd1`

## Disposition

**PASSED.**

## Correctness

**PASS.** The two-message rearrangement and one-way lower bound are sound. In Wang–Wu's source protocol the first party sends sampled base bits, the second returns the estimated cheat-sheet address, and the first then sends four fully linear-PCP field values. Sending Bob's sample bits first lets Alice compute the same address and combine that address with her four field values in one second message; Bob then reconstructs the identical source test, so the error analysis is unchanged. For the one-way restriction, fixing Alice's base string to zero and Bob's blocks to all-zero/all-one realizes any promised address h; certificate uniqueness makes u_h=s_h e and v_h=c*(h)⊕e output exactly s_h for any nonzero e. XOR symmetry gives the reverse direction. The standard information-theoretic INDEX lower bound is Ω(m), and with n=Θ(k²m³), m=2^k, this becomes Ω(n^{1/3}/(log n)^{2/3}).

## Originality

**PASS.** PASS with elevated near-simultaneous priority risk. The Wang–Wu v1 source was checked through its total-function definition, uniqueness lemma, fully linear-PCP test, and explicit randomized protocol; those ingredients support the rearrangement but the source does not state a one-way INDEX restriction or a message-round separation. Targeted searches for the paper identifier/title together with one-way, two-message/two-round, and INDEX did not locate the refinement. Gavinsky's preceding cheat-sheet work supplies conceptual two-message precedent, so no novelty is claimed for the generic idea of two-message cheat-sheet verification; the claim is specific to the classical Wang–Wu witness and its bidirectional one-way obstruction.

## Scientific value

**PASS.** The result places the Wang–Wu total-function separation from adaptive NP-query communication already inside the two-message randomized subclass and simultaneously proves that either one-way direction requires polynomially more communication. This identifies a concrete polynomial one-message/two-message round hierarchy in the same function carrying the small-rectangle separation.

## Independent checks

- Inspected the lawful ECCC full text of Wang–Wu: the certificate uniqueness lemma, fully linear-PCP four-query decomposition, and three-transmission ordering support the proposed two-message reordering.
- Verified the INDEX restriction input by input: promised all-zero/all-one Gap-Hamming blocks select an arbitrary address and uniqueness of c*(h) forces output s_h.
- Re-derived the public-coin one-way INDEX information lower bound c≥m(1-h2(1/3)).
- Checked n=km(8d-3), d=k(m(m+3)+1), hence n=Θ(k²m³), k=Θ(log n), and m=Θ(n^{1/3}/(log n)^{2/3}).

## Evidence and literature

- https://eccc.weizmann.ac.il/report/2026/190/ — Wang–Wu ECCC TR26-190 full text; primary source inspected for uniqueness, fully linear PCP, and randomized protocol.
- https://arxiv.org/abs/2609.20763 — Wang–Wu arXiv landing page and current v1 metadata.
- https://arxiv.org/abs/2608.18784 — Gavinsky, conceptual cheat-sheet/two-message precedent; generic two-message idea excluded from novelty claim.
- https://doi.org/10.1016/0020-0190(91)90157-D — Newman's standard public-to-private randomness conversion; used only for the optional corollary.

## Limitations

- The Ω(n^{1/3}/(log n)^{2/3}) one-way lower bound is not proved tight.
- The result does not improve Wang–Wu's total communication, rectangle, or adaptive-query lower bounds.
- The source preprint is extremely recent and the reordering is short, so near-simultaneous observation or later source revision remains a material priority risk.

## Repository identity

The assigned source-tree SHA `df27d973c99b073ab2c20a860d383cdec7fb9cd1` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.
