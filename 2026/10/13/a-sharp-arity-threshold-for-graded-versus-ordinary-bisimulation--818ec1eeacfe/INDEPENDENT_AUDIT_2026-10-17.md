# Independent mathematical audit

## correctness

PASS

Rooted plain types are (color,set of child types), whereas graded types use child multisets. For constant outdegree two, multiplicities of a two-element child tuple follow from support, so both partitions coincide for all colorings and heights. For fixed q>=3, let t_0=2 and t_(k+1)=2 binom(t_k+q-1,q): the number of graded types possible at height k grows at most exp(C_q q^k). Summing min(q^(h-k),t_k) over residual heights gives G=O_q(N_h/log N_h); B>=h+1 gives ratio O_q(N_h/(log N_h)^2). In the restricted colouring with all internal vertices zero and both leaf colours below every height-one vertex, B=h+2, while g_1=q-1, g_(k+1)=binom(g_k+q-1,q) grows >= exp(c_q q^k) for k>=2. Assigning different height-k types to q^(h-k) disjoint subtrees at k=Theta(log h) gives G=Omega_q(N_h/log N_h), hence sharp ratio. If B=h+1 all heights have a single type and induction gives G=h+1. Independent complete enumerations: q=2,h=0..3 (32906 colourings) no split; q=3,h=0..2 (8210 colourings), exactly 2808 of 8192 height-2 colourings split, minimum B=4.

## originality

PASS

Best-of-knowledge original sharp q=2 versus q>=3 quotient ratio. Prior counting-bisimulation semantics and generic coalgebraic partition algorithms define the equivalences or compute them but do not by themselves imply a maximum relative quotient-size lower bound attained at ordinary footprint h+2. Real searches did not reveal dominating extremal tree compression theorem. This does not certify priority over unindexed set/multiset tree-compression literature.

## value

PASS

The phase transition at branching arity three and asymptotically tight near-minimal ordinary footprint quantify a natural loss of multiplicity information in finite-state coalgebraic/tree compression. The construction and rate are mathematically structural, not a routine quotient calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
