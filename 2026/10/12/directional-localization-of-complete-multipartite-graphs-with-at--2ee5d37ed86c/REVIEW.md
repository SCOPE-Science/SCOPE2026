# Independent mathematical audit

## correctness

PASS

For a complete multipartite graph r≥3 all vertices in different parts are adjacent, those distinct but in the same part have distance 2. Full feedback from a probe in part P yields the robber vertex as a singleton when outside P; if the robber is elsewhere in P, the full set V\P is returned. One cop sweeps P; robber leaving P is immediately located and robber staying in P cannot switch within the same part in one move. Partial feedback: probing all s≤2 vertices of smallest part locates instantly; with s≥3, three probes from distinct parts distinguish each pair of candidate vertices because one probe is adjacent to both and returns the exact candidate. One or two cops below the stated bound always admit distinct candidate vertices x,y from different parts giving identical permissible feedback; after the robber moves N[x]∪N[y]=V resets all contamination, allowing an infinite adversarial response. Correct for all n_i≥1 including complete graphs s=1. Independently checked exact finite-state source and one-round separating probes for small multipartitions; this is corroboration not infinite proof.

## originality

PASS

Best-of-knowledge: the initiating Jones–Kinnersley arXiv:2609.01745 treats complete bipartite graphs, including ζd(K_{m,n})=min(m,n), and general graph bounds. The stated r≥3 exact formula and matched reset lower bounds differ from the r=2 formula and are not implied by general upper bounds. The 2026 invariant is very recent; the complete paper was not independently available in this execution, and the Oxford authorized retrieval returned vpn_disconnected. This source-access risk is named, not mistaken for proof of noncoverage.

## value

PASS

Exact full and partial feedback classifications for every complete multipartite graph with r≥3 form a natural infinite graph-family answer to the initiating game. The jump from possibly unbounded min(m,n) for two parts to at most three for three parts is structurally explanatory; winning strategies and matching lower bound, not merely computational samples, give the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
