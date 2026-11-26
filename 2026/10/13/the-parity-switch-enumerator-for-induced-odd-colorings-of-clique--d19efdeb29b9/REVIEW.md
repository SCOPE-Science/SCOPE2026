# Independent mathematical audit

## correctness

PASS

Fix the root color c. A positive clique color block different from c must have even size, because its vertices see exactly the other vertices in the block. A nonempty c block must be odd, since each of its vertices also sees the root. Thus odd r forces an odd c block and even same-color degree in the base; even r forces c absent and odd same-color degree in the base. Labeled multinomials over the allowed multiplicities give the stated exponential coefficients, and distinct cliques extend independently. The q=1 boundaries follow from these blocks (even r>0 is impossible); q>=2 always supplies a non-root color for even r. With two named colors, even base colorings are solutions of Lx=d over F_2. For y in ker L, y^Td=y^TLy=0 (off-diagonal terms cancel), so the system is consistent and has 2^nullity solutions. Exactly half the 2^r private binary assignments have an odd root-color multiplicity, proving the exponent. For the subdivided K_m, every subdivision vertex must match exactly one endpoint, so the m original vertices must use distinct colors; orienting K_m by a cyclic regular tournament lets each subdivision vertex match its head, giving odd indegree (m-1)/2 for m=3 mod 4. The base degrees are all even. Inspected the frozen verification script/log without executing the upload; independently reproduced 116 direct small-case corona counts versus parity-state dynamic programming (local replay: /tmp/opencode/frozen_independent_checks.py 5), including even r and q=1. The finite counts supplement the proof and do not establish the all-graphs result.

## originality

PASS

The distinct claim is the arbitrary-base, named-palette enumerator with its parity-dependent transfer. The known odd-partition invariant, Gallai-type binary even feasibility and Scott's subdivided cliques are premises, not new contributions. The closest title match in the literature is for a different coloring invariant.

## value

PASS

The exact all-palette transfer applies to any base, including disconnected, non-colorable and isolated cases. It exposes a sharp distinction: changing only attachment parity can collapse an unbounded invariant to one or preserve it exactly. It also gives an exact labeled two-color count for odd attachments, not merely a repeat of binary feasibility. These are useful quantitative and structural consequences even though counting on a general base remains unsolved by the formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
