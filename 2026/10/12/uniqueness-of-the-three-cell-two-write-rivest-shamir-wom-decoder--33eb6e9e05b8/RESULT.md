# Uniqueness of the three-cell, two-write Rivest–Shamir WOM decoder
## Finding
Consider a binary write-once memory with three cells. A cell state is a vector in \(\{0,1\}^3\), ordered coordinatewise, so a legal rewrite can change a zero to a one but never a one to a zero. Let the message alphabet have four values, and let
\[
\alpha:\{0,1\}^3\longrightarrow\{0,1,2,3\}
\]
be a generation-independent interpretation function in the sense of Rivest and Shamir. Call \(\alpha\) admissible when there exists an update rule that, starting from \(000\), can write an arbitrary first message and then an arbitrary second message without decreasing any cell.

Exactly \(24\) interpretation functions are admissible. They are precisely the \(24\) relabelings of the classical Rivest–Shamir decoder
\[
\alpha(a,b,c)=(b\mathbin{\oplus}c,\,a\mathbin{\oplus}c).
\]
Equivalently, every admissible decoder assigns the four messages bijectively to the four complementary pairs
\[
\{000,111\},\quad \{001,110\},\quad \{010,101\},\quad \{100,011\}.
\]
Hence the decoder is unique up to a permutation of the four message names.

The first-write representative of each message is forced: it is the lower-weight member of the corresponding complementary pair, so the four first-generation states are exactly \(000,001,010,100\). Once the decoder is fixed, the second-write transition table on these four reachable first-generation states has exactly \(16\) legal choices. This last count concerns only transitions that can actually be queried after the first write; it does not count arbitrary values assigned to an update function on unreachable states.

## Assumptions and scope
The model is exactly the original generation-independent WOM model: a single interpretation function decodes every cell pattern, and the update function must move only upward in the Boolean lattice. The claim concerns the \((4)^2/3\) problem: four messages, two writes, three binary cells.

Three cells are minimal. With only two cells, four distinct first messages would require all four cell states to occur as first-generation representatives. One representative would then be \(11\), whose upward cone contains only itself, so it could not be rewritten to three other messages.

The classification is of admissible interpretation functions and of their reachable second-write transitions. It does not enumerate arbitrary definitions of the update function on cell states that are never reached after the first write.

## Proof
For a state \(x\in\{0,1\}^3\), let \(U(x)=\{y:y\ge x\}\) be its upward cone. If \(x\) is used for a first message, then every one of the four possible second messages must occur somewhere in \(U(x)\). Therefore \(\lvert U(x)\rvert\ge4\). Since
\[
\lvert U(x)\rvert=2^{3-\operatorname{wt}(x)},
\]
every first-generation representative has Hamming weight at most one.

There are exactly four states of weight at most one, namely \(000,001,010,100\), and the four first messages require four distinct decoder values. Thus these four states are exactly the first-generation representatives and receive four distinct messages. Write their labels as
\[
\alpha(000)=m_0,\quad \alpha(100)=m_1,\quad \alpha(010)=m_2,\quad \alpha(001)=m_3.
\]
Consider the upward cones of \(100\) and \(010\). They are
\[
U(100)=\{100,110,101,111\},\qquad U(010)=\{010,110,011,111\}.
\]
Each cone must contain all four messages. Since their distinguished lower states have labels \(m_1\) and \(m_2\), the shared pair \(\{110,111\}\) must carry the remaining two labels \(\{m_0,m_3\}\). Similarly, comparing \(U(100)\) with \(U(001)\) gives
\[
\{\alpha(101),\alpha(111)\}=\{m_0,m_2\}.
\]
The only common label is \(m_0\), so \(\alpha(111)=m_0\). It follows that \(\alpha(110)=m_3\) and \(\alpha(101)=m_2\). The comparison of \(U(010)\) and \(U(001)\) then gives \(\alpha(011)=m_1\). Thus complementary vertices always share a message, and the four complementary pairs receive four distinct labels. There are exactly \(4!=24\) such labelings.

Conversely, every such complementary-pair labeling works: write a first message using the unique member of its pair of weight at most one. From each nonzero unit vector, its upward cone contains exactly one representative of every message; from \(000\), each message appears twice. Hence all four second messages are reachable. For the three unit-vector first states all second-write choices are forced, while from \(000\) there are two choices for each of four target messages. Therefore each decoder has exactly \(2^4=16\) reachable second-write transition tables.

## Verification
The standalone file `verify.py` exhaustively checks all \(4^8=65{,}536\) functions from the eight cell states to four message labels. It independently tests admissibility from the upward-cone condition, verifies that exactly \(24\) functions survive, verifies that these are exactly all message relabelings of the classical decoder, checks the forced first-generation representatives and complementary-pair property, and counts the \(16\) reachable second-write tables for each decoder.

The canonical newline-terminated list of the \(24\) admissible decoder strings has SHA-256 `9afddc5cdab8eeea0ca83cf1d4d5261165fd40795d7cc7648cf413d982201081`.

A fresh replay returned:
`VERIFY_OK states=8 interpretations_checked=65536 admissible_decoders=24 message_relabeling_orbits=1 forced_first_states=000,001,010,100 complement_pairs=true reduced_second_write_choices_per_decoder=16 reduced_schemes=384 decoder_sha256=9afddc5cdab8eeea0ca83cf1d4d5261165fd40795d7cc7648cf413d982201081`.

## Relationship to prior work
Rivest and Shamir introduced the WOM model and used this \((4)^2/3\) code as their motivating example. Their Table 1 gives one first/second representation scheme, and their Lemma 1 proves that three cells suffice to write two bits twice. They also define a WOM code formally by an interpretation function together with an update function. The paper records the exact small value \(w((4)^2)=3\), but it does not state a classification of all interpretation functions that attain it.

A later phase-change-memory paper by Jiang, Bruck, and Li again uses the same three-cell decoder as a building block, listing the eight decoded cell states as \(0,1,2,3,3,2,1,0\). This independent reuse makes the structural question natural: is that decoder one convenient choice or forced by the WOM constraints? The result above answers that it is forced up to message relabeling.

Targeted literature and published-finding searches for decoder uniqueness, Boolean-cube labelings, complementary-pair characterizations, and the exact count \(24\) did not locate an implication-equivalent result. The remaining priority risk is an obscure or unindexed finite classification.

## Limitations
The theorem is deliberately finite. It classifies the minimal three-cell, two-write, four-message interpretation functions, not WOM decoders for larger alphabets, more writes, multilevel cells, or generation-dependent decoding. The count \(16\) concerns only second-write transitions on states actually reachable after the first write; arbitrary behavior on unused states is outside the claim.

## References
1. Ronald L. Rivest and Adi Shamir, “How to Reuse a Write-Once Memory,” Proceedings of the 14th Annual ACM Symposium on Theory of Computing, 105–113, published 1982-05-05, DOI 10.1145/800070.802182.
2. Ronald L. Rivest and Adi Shamir, “How to Reuse a Write-Once Memory,” *Information and Control* 55 (1982), 1–19, DOI 10.1016/S0019-9958(82)90344-8.
3. Anxiao Jiang, Jehoshua Bruck, and Hao Li, “Constrained Codes for Phase-Change Memories,” IEEE Information Theory Workshop 2010, DOI 10.1109/CIG.2010.5592680.
