# Review

## Correctness
PASS. The state domain is explicit and positivity is controlled by \(a_k,c_k,d_k\ge0\), \(a_k+c_k+d_k=1\), and \(|w_k|^2\le a_kd_k\). A direct Bell contraction gives the exact two-link update, including the factor \(1/2\). The upper-triangular matrix product then proves the heterogeneous \(L\)-link formula by induction. Trace gives the branch probability, while the X-state concurrence formula and an independent partial-transpose eigenvalue calculation both give the exact entanglement criterion. If every \(w_k\ne0\), positivity implies positive branch probability and \(W_L\ne0\), so the endpoint is entangled for every finite \(L\). The source-family specialization reduces exactly to \(\rho_{s^L,\kappa^L}\). The checker reproduces these identities on independent finite contractions and returns `VERIFY_OK`.

## Originality
PASS. The closest recent source, arXiv:2609.11021v1, proves a universal finite horizon for full-rank links and supplies one explicit two-parameter rank-three family with all-depth persistence. It does not state closure or persistence for the full four-real-parameter kernel face, nor heterogeneous links. The closest older X-state source, arXiv:1311.6784v1 / doi:10.1103/PhysRevA.89.064301, gives general formulas for one Bell swap and threshold conditions, but no repeated right-left chain semigroup or all-length heterogeneous theorem. arXiv:2506.22245v1 studies multi-parameter network paths statistically and does not imply the exact branchwise law. Targeted semantic searches for rank-deficient X-state chains, kernel faces, Bell-swap semigroups, heterogeneous links, and the exact recent source found no covering published-finding corpus record or published statement.

Residual risk remains that an older channel-composition or cascade calculation states an equivalent triangular law under different terminology. The searches included X-state, Bell-swapping, repeated-chain, amplitude-damping, rank-deficient, Choi, heterogeneous-link, and entanglement-horizon aliases, and the most relevant full texts were checked at the statement and implication level.

## Value
PASS. The recent full-rank/no-long-range theorem makes the structure of the low-rank exception mathematically consequential. The finding shows that persistence is not confined to a specially tuned two-parameter example: an entire natural state-space face, including heterogeneous network links, is exactly closed and has a computable success probability and concurrence at every depth. This gives a reusable structural mechanism for constructing and analyzing postselected repeater paths, while cleanly separating conditional entanglement persistence from its probability cost.

Self-review: passed. Independent audit: not yet performed.
