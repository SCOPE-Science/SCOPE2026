# Uniqueness of the three-cell, two-write Rivest–Shamir WOM decoder

## Finding
Consider three binary write-once cells, with states \(x\in\{0,1\}^3\) ordered bitwise, and four messages. A decoder \(\alpha\) reads every state in both generations. The same update function \(\beta(x,m)\), of the current state and desired message alone, must permit two arbitrary writes starting from \(000\). Every such update must move weakly upward and decode to the requested message on each queried input.

Exactly \(4!=24\) decoders permit this. They are precisely the bijective labelings of the four complementary pairs \(\{000,111\},\{001,110\},\{010,101\},\{100,011\}\), i.e. all message relabelings of \(\alpha(a,b,c)=(b\mathbin{\oplus}c,a\mathbin{\oplus}c)\). The first-write states are forced to be \(000,001,010,100\), and for each decoder the update table on inputs reachable for either write is unique. No claim is made about update values on other inputs.

## Proof
From a state \(x\) used for a first write, the upper cone \(U(x)=\{y:y\ge x\}\) must contain all four labels. As \(|U(x)|=2^{3-\operatorname{wt}(x)}\), all first states have weight at most one. There are four such states and four labels, so each is used and their labels are distinct. Write \(m_0=\alpha(000)\) and \(m_i=\alpha(e_i)\) for the three unit vectors \(e_i\).

Each \(U(e_i)\) has exactly four states, so each of its labels occurs once. Its top state \(111\) cannot have label \(m_i\) for any \(i\), and hence has label \(m_0\). A state with ones in positions \(i,j\) belongs to \(U(e_i)\) and \(U(e_j)\), so it has neither label \(m_i\) nor \(m_j\), nor \(m_0\) because \(111\) belongs to both cones. It therefore has the label of its complementary unit vector. This forces the complementary-pair description.

Conversely, given such a labeling, define \(\beta(000,m)\) to be the unique state of weight at most one labeled \(m\). The cone of a unit vector contains exactly one member of each complementary pair, so from a unit vector set the update to that unique state with the target label. From \(000\) on the second write the same \(\beta(000,m)\) is used as on the first. This gives a feasible common update table, and each of its entries is forced. In particular there is not an independent choice between complementary states when the second write starts from \(000\): choosing the other state would change the first write for the same input. If one separately allows the updater to be told the generation, while keeping the decoder fixed, the second-write row for \(000\) can instead be chosen independently and there are \(2^4=16\) second-write tables. That is a different update model.

Three cells are minimal: with two cells all four states would be needed to represent the four first messages, but the cone of \(11\) cannot support a second arbitrary write.

## Verification
`verify.py` tests all \(4^8=65{,}536\) decoders and checks which upper cones are usable, the complementary-pair description, the unique common update table on reachable inputs, and the distinct count for a generation-aware updater. The search is exact on this finite cube.

## Relationship to prior work and scope
Rivest and Shamir give the motivating three-cell construction in Lemma 1 and Table 1 of [1]; the known minimum length and the decoder itself are not new. The classification is the necessity of this decoder up to message relabeling. Their formal definition on pp. 4–5 uses a single update function and iterates it from the all-zero state; their example explicitly allows the zero state to occur at more than one generation. Jiang, Bruck and Li [2] reuse this decoder as a component. The result is specific to three binary cells, four messages, two writes, and a common decoder. It does not classify larger problems or schemes with distinct first- and second-write decoders.

## References
1. R. L. Rivest and A. Shamir, “How to Reuse a Write-Once Memory,” *Information and Control* 55 (1982), 1–19, DOI 10.1016/S0019-9958(82)90344-8.
2. A. Jiang, J. Bruck and H. Li, “Constrained Codes for Phase-Change Memories,” *IEEE Information Theory Workshop* (2010), DOI 10.1109/CIG.2010.5592680.
