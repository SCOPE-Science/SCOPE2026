# Independent mathematical audit

## correctness

PASS

For each horizon T and vertex v let a_v count its excited events. Two consecutive excitations at a vertex are separated by ≥3 time steps. Along any edge every adjacent-time transmission uses distinct endpoint excitation events; otherwise same vertex would be excited at times distance two. Hence transmissions per edge ≤min(a_u,a_v), whereas each noninitial excitation requires q incoming transmissions. The layer-cake sum Σ_edges min(a_u,a_v)=Σ_{j≥1}|E[S_j]|≤ρ(G) Σ_v a_v gives (q−ρ)N_T≤qm. If ρ<q finite excitation budget forces extinction and initial refractory states clear by N+1. For K_{2q,2q}, ρ=q and explicit four-class state cycle is primitive period 4. Independent exhaustive graph/state enumeration checked all 216+5184+248589 initial states on all simple labeled graphs of size 3,4,5 with ρ<2, for q=2, including event budget and clock bound, independently of packaged verify_density.py. This finite check is corroboration, not the all-graph proof.

## originality

PASS

For Densest-subgraph excitation extinction threshold and finite event budget: exact final statement and implication were compared against relevant published original mathematical statements and Resultary findings. This gives strictly new general coverage compared to inspected prior statements by exploiting event matching/layer-cake, with explicit sharpness. Best-of-knowledge qualified by explicitly named risks.

## value

PASS

A structural universal extinction criterion in terms of induced density rather than maximum degree, with a quantitative total excitation-event budget and exact equality counterexample, is useful for finite-threshold excitable graph dynamics. It handles nonuniform high-degree graphs and supplies an energy/event-count invariant, not merely a routine maximum-degree estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
