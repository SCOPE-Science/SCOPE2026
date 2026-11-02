# Independent mathematical audit

## correctness

PASS

PASS. For Q=Z/nZ, a(i)=i+1 and b replacing only state 0 by d, every strict rank-decreasing b in coordinates undone by cumulative rotations removes p and requires p+d still present. Consequently to delete H=Q\S with minimum k=n−|S| b letters, legal orders are exactly the linear extensions of induced forward-d paths; each maximal run of length ℓ_j is internally fixed, and interleavings give k!/∏ℓ_j!. A whole d-orbit in H would form an impossible directed cycle, so reachability occurs iff S meets all g=gcd(n,d) residue classes; converse uses rotations to implement each legal p sequence. For coprime d, run count at most min(k,n−k); factorial log-convexity and splitting show the balanced maximum with r=min(k,n−k), k=qr+t, count k!/(q!^(r−t)(q+1)!^t). Singleton complement is one long d-path, enforcing p_{j+1}=p_j+d and each minimal inter-b rotation a^(n−d), yielding the unique shortest reset word AMONG those with exactly n−1 b letters: b(a^(n−d)b)^(n−2), total length 1+(n−2)(n−d+1). No claim about unrestricted shortest reset words. Independent 0–1 shortest-path subset BFS exhaustively confirmed nonempty targets n=2..7 and all 1<=d<n; primary artifacts/verify.py implements all-target/schedule permutation checks through n=8. Infinite-parameter proof is combinatorial, not finite-sample inference.

## originality

PASS

PASS, carefully limited. Don 2015/2016 already proves strong subset reachability for coprime circular 1-contracting automata, so coprime existence itself is not new. The related 2026 published Resultary record proves a two-deletion target classification for arbitrary rank-(n−1) transitions, but not a factorial enumeration of all strict-collapse orders for arbitrary H. New potential content is exact poset/schedule count, all-k sharp envelope, noncoprime reachability obstruction and resource-constrained unique reset word. A generic poset linear-extension lemma is prior and not claimed original; its precise identification and all-parameter optimized schedule counts for this automaton family are not located in relevant primary results. An older automata enumeration under alternative labels could cover the result; priority is best-of-knowledge.

## value

PASS

PASS. The natural target-set reachability problem in a canonical one-defect synchronizing automaton is sharpened to exact counts of all minimum-resource deletion schedules, a sharp balanced extreme over missing sets, and rigidity of a resource-constrained reset witness. General multinomial identities alone cannot identify the automaton poset or optimize it; the invariant is a plausible reusable precise combinatorial fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
